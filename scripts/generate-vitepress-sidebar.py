#!/usr/bin/env python3
"""Generate an explicit VitePress sidebar from the repo's `.pages` files.

Pre-commit hook that turns the human-curated `docs/**/.pages` files (the
same files `mkdocs-awesome-pages-plugin` already reads for the MkDocs nav)
into an explicit, path-keyed VitePress `sidebar` object, written to
`docs/.vitepress/sidebar.generated.json` and imported by `config.mts`.

Why `.pages` and not a new override file:
    Every guide directory that needs a curated order already has a `.pages`
    file with a `nav:` list (title + explicit ordering, external links,
    absolute-path overrides, etc). Reusing it means there is exactly one
    place to reorder a guide, it stays valid input for MkDocs too during
    the migration, and no new override mechanism has to be documented or
    kept in sync.

Ordering rules (mirrors mkdocs-awesome-pages defaults):
    - A directory with a `.pages` file: its `nav:` list is transcribed
        1:1, in order, into sidebar items.
    - A directory without a `.pages` file: falls back to an auto-listing,
        `index.md` first (as "Home"), then subdirectories (alphabetical,
        only if they contain markdown), then remaining `.md` files
        (alphabetical). Titles are derived from the file/directory name.
    - Top-level sections follow `docs/.pages`' root `nav:` order; any
        top-level directory not listed there (with markdown content) is
        appended alphabetically, so a brand new guide category gets a
        sidebar section automatically with no `config.mts` edit required.

`.pages` `nav:` entry forms supported:
    - `index.md`: bare file entry.
    - `Title: relative/file.md`: file link with an explicit title.
    - `Title: /Absolute/Path/`: passthrough link, already in VitePress's
        clean-URL form. Used for links into a sub-directory that has no
        `.pages` of its own.
    - `Title (ext.link): https://...`: external link. The `(ext.link)`
        marker is stripped from the title.
    - `SubdirName`: bare subdirectory reference, recursed into as a
        collapsed group.
    - `Title: subdir-name`: subdirectory reference with a title override.

A `.pages` entry that references a file or directory that does not exist
on disk is skipped with a warning (non-fatal) rather than crashing the
commit.

Idempotent: re-running with no `.pages`/doc changes produces byte-identical
output and exits without touching the file. Regenerated output is staged
automatically so it lands in the same commit.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

DOCS_ROOT = Path("docs")
OUTPUT_PATH = DOCS_ROOT / ".vitepress" / "sidebar.generated.json"
EXT_LINK_MARKER_RE = re.compile(r"\s*\(ext\.link\)\s*$", re.IGNORECASE)
WORD_SPLIT_RE = re.compile(r"[-_]+")


def humanize(name: str) -> str:
    """Title-case a dash/underscore-separated name, leaving mixed-case words alone."""
    words = [w for w in WORD_SPLIT_RE.split(name) if w]
    return " ".join(w if w != w.lower() else w.capitalize() for w in words)


def has_markdown(directory: Path) -> bool:
    return any(directory.rglob("*.md"))


def read_nav(directory: Path) -> list | None:
    """Return the `nav:` list from `directory/.pages`, or None if absent/invalid."""
    pages_file = directory / ".pages"
    if not pages_file.exists():
        return None
    data = yaml.safe_load(pages_file.read_text()) or {}
    nav = data.get("nav")
    return nav if isinstance(nav, list) else None


def file_link(url_prefix: str, rel_path: str) -> str:
    """Resolve a relative `.md` path to its VitePress clean-URL link."""
    if rel_path == "index.md":
        return url_prefix
    stem = rel_path[: -len(".md")] if rel_path.endswith(".md") else rel_path
    return f"{url_prefix}{stem}"


def build_entry(directory: Path, url_prefix: str, entry) -> dict | None:
    if isinstance(entry, str):
        title, target = None, entry
    elif isinstance(entry, dict) and len(entry) == 1:
        ((title, target),) = entry.items()
    else:
        print(
            f"WARN: skipping unrecognised .pages entry in {directory}: {entry!r}",
            file=sys.stderr,
        )
        return None

    if not isinstance(target, str):
        print(
            f"WARN: skipping unrecognised .pages entry in {directory}: {entry!r}",
            file=sys.stderr,
        )
        return None

    if target.startswith(("http://", "https://")):
        text = EXT_LINK_MARKER_RE.sub("", title or target)
        return {"text": text, "link": target}

    if target.startswith("/"):
        # Already a resolved VitePress link (file or directory root) --
        # used for cross-referencing a file inside an un-`.pages`'d subdir.
        return {"text": title or target.rstrip("/").rsplit("/", 1)[-1], "link": target}

    if target.endswith(".md"):
        text = title or (
            "Home" if target == "index.md" else humanize(Path(target).stem)
        )
        return {"text": text, "link": file_link(url_prefix, target)}

    # Bare or titled reference to a subdirectory -- recurse as a group.
    subdir_name = target.rstrip("/")
    subdir = directory / subdir_name
    if not subdir.is_dir():
        print(
            f"WARN: {directory / '.pages'} references missing directory '{target}', skipping",
            file=sys.stderr,
        )
        return None
    return build_group(
        subdir, f"{url_prefix}{subdir_name}/", title or humanize(subdir_name)
    )


def build_items(directory: Path, url_prefix: str) -> list[dict]:
    nav = read_nav(directory)
    if nav is not None:
        items = []
        for entry in nav:
            item = build_entry(directory, url_prefix, entry)
            if item is not None:
                items.append(item)
        return items

    # No `.pages`: fall back to an alphabetical auto-listing.
    items = []
    if (directory / "index.md").exists():
        items.append({"text": "Home", "link": url_prefix})

    subdirs = sorted(
        d
        for d in directory.iterdir()
        if d.is_dir() and not d.name.startswith(".") and has_markdown(d)
    )
    for d in subdirs:
        items.append(build_group(d, f"{url_prefix}{d.name}/", humanize(d.name)))

    md_files = sorted(
        f
        for f in directory.iterdir()
        if f.is_file() and f.suffix == ".md" and f.name != "index.md"
    )
    for f in md_files:
        items.append({"text": humanize(f.stem), "link": file_link(url_prefix, f.name)})

    return items


def build_group(directory: Path, url_prefix: str, title: str) -> dict:
    return {
        "text": title,
        "collapsed": True,
        "items": build_items(directory, url_prefix),
    }


def discover_top_level_sections() -> list[str]:
    """Order top-level `docs/` directories per `docs/.pages`, then alphabetically."""
    ordered: list[str] = []
    seen: set[str] = set()

    for entry in read_nav(DOCS_ROOT) or []:
        name = None
        if isinstance(entry, str) and not entry.endswith(".md"):
            name = entry
        elif isinstance(entry, dict):
            ((_, target),) = entry.items()
            if (
                isinstance(target, str)
                and not target.endswith(".md")
                and not target.startswith("http")
            ):
                name = target.rstrip("/").lstrip("/")
        if name and (DOCS_ROOT / name).is_dir():
            ordered.append(name)
            seen.add(name)

    remaining = sorted(
        d.name
        for d in DOCS_ROOT.iterdir()
        if d.is_dir()
        and not d.name.startswith(".")
        and d.name not in seen
        and has_markdown(d)
    )
    ordered.extend(remaining)
    return ordered


def build_sidebar() -> dict[str, list[dict]]:
    sidebar: dict[str, list[dict]] = {}
    for name in discover_top_level_sections():
        directory = DOCS_ROOT / name
        items = build_items(directory, f"/{name}/")
        if items:
            sidebar[f"/{name}/"] = items
    return sidebar


def main() -> int:
    output = json.dumps(build_sidebar(), indent=2) + "\n"

    if OUTPUT_PATH.exists() and OUTPUT_PATH.read_text() == output:
        return 0

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(output)
    print(f"Updated: {OUTPUT_PATH}")

    # Auto-stage so the regenerated sidebar lands in the same commit.
    subprocess.run(["git", "add", "--", str(OUTPUT_PATH)], check=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
