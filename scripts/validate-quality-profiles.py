#!/usr/bin/env python3
"""Validate quality profile consistency per CONTRIBUTING.md rules.

Checks:
    1. Every profile file has a matching entry in groups.json (slug + trash_id)
    2. Every groups.json entry has a corresponding profile file
    3. No duplicate trash_ids across profile files
    4. cf-groups quality_profiles.include entries reference valid profiles
    5. Filenames follow naming conventions (lowercase, dashes only)

Exit code 0 on success, 1 on any failure.
"""

import json
import re
import sys
from pathlib import Path

APPS = ("radarr", "sonarr")
BASE = Path("docs/json")
FILENAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_json(path: Path) -> dict | list | None:
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"ERROR: Failed to read {path}: {e}")
        return None


def validate_app(app: str) -> list[str]:
    errors: list[str] = []

    profiles_dir = BASE / app / "quality-profiles"
    groups_file = BASE / app / "quality-profile-groups" / "groups.json"
    cf_groups_dir = BASE / app / "cf-groups"

    # Load profile files
    profile_files: dict[str, dict] = {}  # slug -> data
    if not profiles_dir.is_dir():
        errors.append(f"[{app}] quality-profiles directory not found: {profiles_dir}")
        return errors

    for p in sorted(profiles_dir.glob("*.json")):
        slug = p.stem
        data = load_json(p)
        if data is None:
            errors.append(f"[{app}] Failed to parse profile: {p.name}")
            continue
        profile_files[slug] = data

    # Check filename conventions
    for slug in profile_files:
        if not FILENAME_RE.match(slug):
            errors.append(
                f"[{app}] Profile filename '{slug}.json' violates naming convention"
                " (must be lowercase alphanumeric with dashes)"
            )

    # Check duplicate trash_ids across profiles and ensure presence
    seen_ids: dict[str, str] = {}  # trash_id -> slug
    for slug, data in profile_files.items():
        tid = data.get("trash_id")
        if not tid:
            errors.append(
                f"[{app}] Profile '{slug}.json' missing required field 'trash_id'"
            )
            continue
        if tid in seen_ids:
            errors.append(
                f"[{app}] Duplicate trash_id '{tid}' in profiles:"
                f" '{seen_ids[tid]}.json' and '{slug}.json'"
            )
        else:
            seen_ids[tid] = slug

    # Load groups.json
    if not groups_file.is_file():
        errors.append(f"[{app}] groups.json not found: {groups_file}")
        return errors

    groups_data = load_json(groups_file)
    if groups_data is None:
        errors.append(f"[{app}] Failed to parse groups.json")
        return errors

    # Build groups lookup: slug -> trash_id
    groups_lookup: dict[str, str] = {}
    for group in groups_data:
        for slug, tid in group.get("profiles", {}).items():
            groups_lookup[slug] = tid

    # Check: every profile file has an entry in groups.json
    for slug, data in profile_files.items():
        tid = data.get("trash_id", "")
        if slug not in groups_lookup:
            errors.append(
                f"[{app}] Profile '{slug}.json' (trash_id: {tid})"
                " missing from quality-profile-groups/groups.json"
            )
        elif groups_lookup[slug] != tid:
            errors.append(
                f"[{app}] Profile '{slug}.json' trash_id mismatch:"
                f" file has '{tid}', groups.json has '{groups_lookup[slug]}'"
            )

    # Check: every groups.json entry has a profile file
    for slug, tid in groups_lookup.items():
        if slug not in profile_files:
            errors.append(
                f"[{app}] groups.json entry '{slug}' (trash_id: {tid})"
                " has no corresponding file in quality-profiles/"
            )

    # Build profile name -> trash_id lookup, detect duplicate names
    name_to_tid: dict[str, str] = {}
    for slug, data in profile_files.items():
        name = data.get("name", "")
        tid = data.get("trash_id", "")
        if not name or not tid:
            continue
        if name in name_to_tid:
            errors.append(
                f"[{app}] Duplicate profile name '{name}' in '{slug}.json'"
                f" (already defined with trash_id '{name_to_tid[name]}')"
            )
        else:
            name_to_tid[name] = tid

    # Check cf-groups quality_profiles.include references
    # Skip known placeholder profiles (e.g. "Radarr Dummy") used for cf-groups
    # that are not tied to specific quality profiles
    skip_names = {n for n in ("Radarr Dummy", "Sonarr Dummy")}

    if cf_groups_dir.is_dir():
        for cfg_path in sorted(cf_groups_dir.glob("*.json")):
            cfg_data = load_json(cfg_path)
            if cfg_data is None:
                continue
            qp = cfg_data.get("quality_profiles")
            if qp is not None and not isinstance(qp, dict):
                errors.append(
                    f"[{app}] cf-groups/{cfg_path.name} has malformed"
                    " 'quality_profiles' (expected object)"
                )
                continue
            include = (qp or {}).get("include", {})
            if include and not isinstance(include, dict):
                errors.append(
                    f"[{app}] cf-groups/{cfg_path.name} has malformed"
                    " 'quality_profiles.include' (expected object)"
                )
                continue
            for profile_name, ref_tid in include.items():
                if profile_name in skip_names:
                    continue
                if profile_name not in name_to_tid:
                    errors.append(
                        f"[{app}] cf-groups/{cfg_path.name} references"
                        f" profile '{profile_name}' which doesn't exist"
                    )
                elif name_to_tid[profile_name] != ref_tid:
                    errors.append(
                        f"[{app}] cf-groups/{cfg_path.name} references"
                        f" profile '{profile_name}' with trash_id '{ref_tid}'"
                        f" but profile has '{name_to_tid[profile_name]}'"
                    )

    return errors


def main() -> int:
    all_errors: list[str] = []
    for app in APPS:
        all_errors.extend(validate_app(app))

    if all_errors:
        print(f"\nFound {len(all_errors)} error(s):\n")
        for err in all_errors:
            print(f"  ERROR: {err}")
        return 1

    print("All quality profile validations passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
