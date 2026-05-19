"""mkdocs-macros entry point.

Builds lookup tables from `docs/json/{radarr,sonarr}/` and registers the
`render_profile_cfs` macro used by the quality-profile guides to auto-populate
their required/optional CF tables from `cf-groups/*.json`.

The macro filters cf-groups by `quality_profiles.include[<profile name>]` and
renders a collapsible admonition per group with a markdown table of the CFs.
Per-profile overrides (skip a group, force required/optional) live in
`docs/json/{app}/quality-profile-groups/groups.json` under a per-profile
`profile_overrides` entry (see `schemas/profile-groups.schema.json`).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

APPS = ("radarr", "sonarr")
JSON_ROOT = Path("docs/json")
COLLECTION_URL = {
    "radarr": "/Radarr/Radarr-collection-of-custom-formats/",
    "sonarr": "/Sonarr/sonarr-collection-of-custom-formats/",
}
BASE_PROFILE_NAME = "Base Profile"


def _load_dir(directory: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    if not directory.is_dir():
        return out
    for path in sorted(directory.glob("*.json")):
        try:
            with path.open() as f:
                out[path.stem] = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
    return out


def _cf_slug_link(app: str, slug: str) -> str:
    return f"{COLLECTION_URL[app]}#{slug}"


def _resolve_score(cf: dict[str, Any], score_set: str) -> str:
    scores = cf.get("trash_scores") or {}
    if score_set in scores:
        return str(scores[score_set])
    if "default" in scores:
        return str(scores["default"])
    # CFs with no trash_scores are informational (effective score 0).
    return "0"


def _render_table(app: str, group: dict[str, Any], cf_index: dict[str, str],
                  cfs_by_slug: dict[str, dict[str, Any]],
                  score_set: str) -> list[str]:
    lines = [
        "    | Custom Format | Score | Trash ID |",
        "    | --- | :---: | --- |",
    ]
    for entry in group.get("custom_formats", []):
        tid = entry.get("trash_id", "")
        slug = cf_index.get(tid)
        if not slug:
            # Unresolvable CF reference — render the bare name so the build
            # fails loud rather than silently dropping it.
            lines.append(
                f"    | {entry.get('name', '?')} | ? | `{tid}` (unresolved) |"
            )
            continue
        cf = cfs_by_slug.get(slug, {})
        name = cf.get("name", entry.get("name", slug))
        link = _cf_slug_link(app, slug)
        score = _resolve_score(cf, score_set)
        lines.append(f"    | [{name}]({link}) | {score} | {cf.get('trash_id', tid)} |")
    return lines


def _render_group(app: str, slug: str, group: dict[str, Any],
                  cf_index: dict[str, str],
                  cfs_by_slug: dict[str, dict[str, Any]],
                  score_set: str) -> str:
    title = group.get("name", slug)
    body = [f'??? abstract "{title} - [Click to show/hide]"', ""]
    body.extend(_render_table(app, group, cf_index, cfs_by_slug, score_set))
    body.append("")
    return "\n".join(body)


def _bucket(group: dict[str, Any], slug: str,
            force_required: set[str], force_optional: set[str]) -> str:
    if slug in force_required:
        return "required"
    if slug in force_optional:
        return "optional"
    return "required" if group.get("default") == "true" else "optional"


def _profile_score_set(profiles_by_name: dict[str, dict[str, Any]],
                       profile_name: str) -> str:
    profile = profiles_by_name.get(profile_name) or {}
    return profile.get("trash_score_set") or "default"


def _collect_groups(cf_groups: dict[str, dict[str, Any]],
                    profile_name: str,
                    exclude: set[str],
                    add: set[str]) -> list[tuple[str, dict[str, Any]]]:
    out: list[tuple[str, dict[str, Any]]] = []
    seen: set[str] = set()
    for slug, group in cf_groups.items():
        if slug in exclude:
            continue
        include_map = (group.get("quality_profiles") or {}).get("include") or {}
        if profile_name in include_map or slug in add:
            out.append((slug, group))
            seen.add(slug)
    # Force-add any explicitly-requested group that isn't already attached.
    for slug in add:
        if slug in seen or slug in exclude:
            continue
        if slug in cf_groups:
            out.append((slug, cf_groups[slug]))
    return out


def _read_overrides(profile_groups: list[dict[str, Any]],
                    profile_name: str) -> dict[str, Any]:
    """Find profile_overrides for `profile_name` by trash_id lookup."""
    for group in profile_groups:
        overrides_map = group.get("profile_overrides") or {}
        for slug, override in overrides_map.items():
            if override.get("profile_name") == profile_name:
                return override
    return {}


def define_env(env):
    cfs: dict[str, dict[str, dict[str, Any]]] = {}
    cf_groups: dict[str, dict[str, dict[str, Any]]] = {}
    profiles_by_name: dict[str, dict[str, dict[str, Any]]] = {}
    cf_index: dict[str, dict[str, str]] = {}
    profile_groups_raw: dict[str, list[dict[str, Any]]] = {}

    for app in APPS:
        cfs[app] = _load_dir(JSON_ROOT / app / "cf")
        cf_groups[app] = _load_dir(JSON_ROOT / app / "cf-groups")

        profile_files = _load_dir(JSON_ROOT / app / "quality-profiles")
        by_name: dict[str, dict[str, Any]] = {}
        for data in profile_files.values():
            name = data.get("name")
            if name:
                by_name[name] = data
        profiles_by_name[app] = by_name

        index: dict[str, str] = {}
        for slug, data in cfs[app].items():
            tid = data.get("trash_id")
            if tid:
                index[tid] = slug
        cf_index[app] = index

        groups_file = JSON_ROOT / app / "quality-profile-groups" / "groups.json"
        if groups_file.is_file():
            try:
                with groups_file.open() as f:
                    profile_groups_raw[app] = json.load(f) or []
            except (json.JSONDecodeError, OSError):
                profile_groups_raw[app] = []
        else:
            profile_groups_raw[app] = []

    @env.macro
    def render_profile_cfs(app: str, profile_name: str,
                           exclude_groups: list[str] | None = None,
                           add_groups: list[str] | None = None,
                           force_required: list[str] | None = None,
                           force_optional: list[str] | None = None) -> str:
        """Render required + optional CF tables for `profile_name` in `app`.

        Filters `docs/json/{app}/cf-groups/*.json` by `quality_profiles.include`.
        Per-call overrides supplement the data-driven overrides from
        `quality-profile-groups/groups.json` `profile_overrides`.
        """
        if app not in cf_groups:
            return f"<!-- render_profile_cfs: unknown app '{app}' -->"

        data_overrides = _read_overrides(profile_groups_raw[app], profile_name)
        exclude = set(data_overrides.get("exclude_groups") or [])
        add = set(data_overrides.get("add_groups") or [])
        force_req = set(data_overrides.get("force_required") or [])
        force_opt = set(data_overrides.get("force_optional") or [])
        if exclude_groups:
            exclude.update(exclude_groups)
        if add_groups:
            add.update(add_groups)
        if force_required:
            force_req.update(force_required)
        if force_optional:
            force_opt.update(force_optional)

        score_set = _profile_score_set(profiles_by_name[app], profile_name)

        groups = _collect_groups(cf_groups[app], profile_name, exclude, add)

        required: list[str] = []
        optional: list[str] = []
        for slug, group in groups:
            bucket = _bucket(group, slug, force_req, force_opt)
            rendered = _render_group(app, slug, group, cf_index[app], cfs[app], score_set)
            (required if bucket == "required" else optional).append(rendered)

        chunks: list[str] = []
        if required:
            chunks.append("**The following Custom Formats are required:**\n")
            chunks.extend(required)
        if optional:
            chunks.append("**The following Custom Formats are optional:**\n")
            chunks.extend(optional)
        if not chunks:
            return (
                f"<!-- render_profile_cfs: no cf-groups list profile '{profile_name}'"
                f" for {app}; check quality_profiles.include in cf-groups/*.json -->"
            )
        return "\n".join(chunks)

    env.variables["cf_index"] = cf_index
