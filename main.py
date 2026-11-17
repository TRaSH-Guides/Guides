"""mkdocs-macros entry point.

Builds lookup tables from `docs/json/{radarr,sonarr}/` and registers the
`render_profile_cfs` macro used by the quality-profile guides to auto-populate
their required/optional CF tables from `cf-groups/*.json`.

Required CFs are the profile's `formatItems` plus the `required` and `default`
CFs of each default-on cf-group that lists the profile in
`quality_profiles.include`. Everything else in an attached group is optional,
mirroring how Recyclarr selects CFs. Each bucket renders as a collapsible
admonition per group with a markdown table of the CFs.
A group may set an optional `info` field (markdown string) to render narrative
text above its table, e.g. the Audio Formats / HDR Formats groups (see
`schemas/cf-groups.schema.json`).
Per-profile overrides (skip a group, force required/optional) live in
`docs/json/{app}/quality-profile-groups/groups.json` under a per-profile
`profile_overrides` entry (see `schemas/profile-groups.schema.json`).
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

APPS = ("radarr", "sonarr")
JSON_ROOT = Path("docs/json")
COLLECTION_URL = {
    "radarr": "/Radarr/Radarr-collection-of-custom-formats/",
    "sonarr": "/Sonarr/sonarr-collection-of-custom-formats/",
}
BASE_PROFILE_NAME = "Base Profile"
PROFILE_CFS_TITLE = "[Required] Profile Custom Formats"


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


def _is_true(value: Any) -> bool:
    return str(value).lower() == "true"


def _variant_label(profile_name: str) -> str:
    """`[French MULTi.VF] HD Remux` -> `MULTi.VF`, used as a score column label."""
    match = re.match(r"\[(?:French )?([^\]]+)\]", profile_name)
    return match.group(1) if match else profile_name


def _render_table(
    app: str,
    rows: list[tuple[dict[str, Any], dict[str, str]]],
    cf_index: dict[str, str],
    cfs_by_slug: dict[str, dict[str, Any]],
) -> list[str]:
    """Render CF rows as a table. `rows` pairs each CF entry with its score per
    profile variant. One `Score` column is used unless the variants disagree (or
    a variant lacks the CF), in which case each variant gets its own column."""
    labels = list(rows[0][1]) if rows else []
    per_variant = len(labels) > 1 and any(
        len(scores) != len(labels) or len(set(scores.values())) > 1
        for _, scores in rows
    )
    if per_variant:
        head = ["Custom Format"] + [f"{label} Score" for label in labels] + ["Trash ID"]
        align = ["---"] + [":---:"] * len(labels) + ["---"]
    else:
        head = ["Custom Format", "Score", "Trash ID"]
        align = ["---", ":---:", "---"]
    lines = ["    | " + " | ".join(head) + " |", "    | " + " | ".join(align) + " |"]
    for entry, scores in rows:
        tid = entry.get("trash_id", "")
        slug = cf_index.get(tid)
        if not slug:
            cells = [entry.get("name", "?")] + ["?"] * (len(labels) if per_variant else 1)
            lines.append("    | " + " | ".join(cells + [f"`{tid}` (unresolved)"]) + " |")
            continue
        cf = cfs_by_slug.get(slug, {})
        name = cf.get("name", entry.get("name", slug))
        link = f"[{name}]({_cf_slug_link(app, slug)})"
        if per_variant:
            cells = [scores.get(label, "-") for label in labels]
        else:
            cells = [next(iter(scores.values()))]
        lines.append("    | " + " | ".join([link] + cells + [cf.get("trash_id", tid)]) + " |")
    return lines


def _render_info(info: str) -> list[str]:
    """Indent a group's optional narrative `info` block to nest it inside the
    admonition, mirroring the indentation used for the table rows."""
    lines = [f"    {line}" if line else "" for line in info.split("\n")]
    lines.append("")
    return lines


def _render_section(
    app: str,
    section: dict[str, Any],
    cf_index: dict[str, str],
    cfs_by_slug: dict[str, dict[str, Any]],
) -> str:
    body = [f'??? abstract "{section["title"]} - [Click to show/hide]"', ""]
    if section["info"]:
        body.extend(_render_info(section["info"]))
    body.extend(_render_table(app, section["rows"], cf_index, cfs_by_slug))
    body.append("")
    return "\n".join(body)


def _split_entries(
    group: dict[str, Any],
    forced: str | None,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Split a group's CFs into (required, optional) the way sync tools select them.

    In a default-on group only `required: true` and `default: true` CFs are always
    enabled; the rest are opt-in. A group that is not default-on is entirely
    opt-in. `forced` ("required" or "optional") overrides this for the whole group.
    """
    entries = group.get("custom_formats", [])
    if forced == "required":
        return list(entries), []
    if forced == "optional" or not _is_true(group.get("default")):
        return [], list(entries)
    always = [e for e in entries if _is_true(e.get("required")) or _is_true(e.get("default"))]
    return always, [e for e in entries if e not in always]


def _forced(slug: str, force_required: set[str], force_optional: set[str]) -> str | None:
    if slug in force_required:
        return "required"
    if slug in force_optional:
        return "optional"
    return None


def _profile_score_set(
    profiles_by_name: dict[str, dict[str, Any]],
    profile_name: str,
) -> str:
    profile = profiles_by_name.get(profile_name) or {}
    return profile.get("trash_score_set") or "default"


def _collect_groups(
    cf_groups: dict[str, dict[str, Any]],
    profile_name: str,
    exclude: set[str],
    add: set[str],
) -> list[tuple[str, dict[str, Any]]]:
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


def _read_overrides(
    profile_groups: list[dict[str, Any]],
    profile_name: str,
) -> dict[str, Any]:
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

    def build_plan(
        app: str,
        profile_name: str,
        exclude_groups: list[str] | None,
        add_groups: list[str] | None,
        force_required: list[str] | None,
        force_optional: list[str] | None,
    ) -> dict[str, list[dict[str, Any]]]:
        """Select the CFs a profile enables, split into required and optional.

        Required: the profile's `formatItems`, plus the `required` and `default`
        CFs of each default-on cf-group that lists the profile. Optional: the
        rest of those groups and every CF of the other attached groups.
        """
        data_overrides = _read_overrides(profile_groups_raw[app], profile_name)
        exclude = set(data_overrides.get("exclude_groups") or []) | set(exclude_groups or [])
        add = set(data_overrides.get("add_groups") or []) | set(add_groups or [])
        force_req = set(data_overrides.get("force_required") or []) | set(force_required or [])
        force_opt = set(data_overrides.get("force_optional") or []) | set(force_optional or [])
        include_cfs = {
            k: set(v) for k, v in (data_overrides.get("include_cfs") or {}).items()
        }
        exclude_cfs = {
            k: set(v) for k, v in (data_overrides.get("exclude_cfs") or {}).items()
        }
        documented = set(data_overrides.get("documented_elsewhere") or [])

        score_set = _profile_score_set(profiles_by_name[app], profile_name)
        shown: set[str | None] = set()

        def rows_for(slug: str, entries: list[dict[str, Any]]) -> list:
            keep = include_cfs.get(slug)
            drop = exclude_cfs.get(slug, set())
            rows = []
            for entry in entries:
                cf_slug = cf_index[app].get(entry.get("trash_id", ""))
                if keep is not None and cf_slug not in keep:
                    continue
                if cf_slug in drop or cf_slug in documented or cf_slug in shown:
                    continue
                score = _resolve_score(cfs[app].get(cf_slug, {}), score_set)
                rows.append((entry, score))
            return rows

        plan: dict[str, list[dict[str, Any]]] = {"required": [], "optional": []}

        def emit(bucket: str, title: str, info: str | None, rows: list) -> None:
            if rows:
                shown.update(cf_index[app].get(entry.get("trash_id", "")) for entry, _ in rows)
                plan[bucket].append({"title": title, "info": info, "rows": rows})

        profile = profiles_by_name[app].get(profile_name) or {}
        format_items = [
            {"name": name, "trash_id": tid}
            for name, tid in (profile.get("formatItems") or {}).items()
        ]
        emit("required", PROFILE_CFS_TITLE, None, rows_for("", format_items))

        split = [
            (slug, group, _split_entries(group, _forced(slug, force_req, force_opt)))
            for slug, group in _collect_groups(cf_groups[app], profile_name, exclude, add)
        ]
        with_info: set[str] = set()
        for slug, group, (always, _opt) in split:
            rows = rows_for(slug, always)
            if rows and group.get("info"):
                with_info.add(slug)
            emit("required", group.get("name", slug), group.get("info"), rows)
        for slug, group, (_always, opt) in split:
            # A group's `info` renders once, above its first table.
            info = None if slug in with_info else group.get("info")
            emit("optional", group.get("name", slug), info, rows_for(slug, opt))
        return plan

    @env.macro
    def render_profile_cfs(
        app: str,
        profile_name: str | list[str],
        exclude_groups: list[str] | None = None,
        add_groups: list[str] | None = None,
        force_required: list[str] | None = None,
        force_optional: list[str] | None = None,
        only: str | None = None,
        emit_headers: bool = True,
    ) -> str:
        """Render required + optional CF tables for `profile_name` in `app`.

        Per-call overrides supplement the data-driven overrides from
        `quality-profile-groups/groups.json` `profile_overrides`.

        - `profile_name` may be a list of profiles that share one guide section
            (e.g. the French VOSTFR / MULTi.VF / MULTi.VO variants). Tables whose
            scores differ between them get one score column per profile.
        - `only="required"` / `only="optional"` renders just one bucket.
        - `emit_headers=False` suppresses the bold section labels when the
            caller (e.g. the German guide) manages headers itself.
        """
        if app not in cf_groups:
            raise ValueError(
                f"render_profile_cfs: unknown app '{app}' (expected one of {APPS})"
            )

        names = [profile_name] if isinstance(profile_name, str) else list(profile_name)
        labels = [_variant_label(n) for n in names] if len(names) > 1 else [""]
        plans = [
            build_plan(
                app, n, exclude_groups, add_groups, force_required, force_optional
            )
            for n in names
        ]

        rendered: dict[str, list[str]] = {}
        for bucket in ("required", "optional"):
            merged: dict[str, dict[str, Any]] = {}
            for label, plan in zip(labels, plans):
                for section in plan[bucket]:
                    target = merged.setdefault(
                        section["title"],
                        {"title": section["title"], "info": section["info"], "rows": {}},
                    )
                    for entry, score in section["rows"]:
                        row = target["rows"].setdefault(entry.get("trash_id", ""), (entry, {}))
                        row[1][label] = score
            rendered[bucket] = [
                _render_section(
                    app,
                    {**sec, "rows": list(sec["rows"].values())},
                    cf_index[app],
                    cfs[app],
                )
                for sec in merged.values()
            ]

        chunks: list[str] = []
        if rendered["required"] and only != "optional":
            if emit_headers:
                chunks.append("**The following Custom Formats are required:**\n")
            chunks.extend(rendered["required"])
        if rendered["optional"] and only != "required":
            if emit_headers:
                chunks.append("**The following Custom Formats are optional:**\n")
            chunks.extend(rendered["optional"])
        if not chunks:
            raise ValueError(
                f"render_profile_cfs: no custom formats found for {names} in {app};"
                " check the profile name and quality_profiles.include in"
                " cf-groups/*.json"
            )
        return "\n".join(chunks)

    env.variables["cf_index"] = cf_index
