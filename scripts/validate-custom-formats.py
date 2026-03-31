#!/usr/bin/env python3
"""Validate custom format consistency per CONTRIBUTING.md rules.

Checks:
    1. Global trash_id uniqueness across CF files, cf-groups, and quality profiles
    2. cf-groups entries reference valid CFs (trash_id exists, name matches)
    3. CF filenames follow naming conventions (lowercase, dashes only)

Exit code 0 on success, 1 on any failure.
"""

import json
import re
import sys
from pathlib import Path

APPS = ("radarr", "sonarr")
BASE = Path("docs/json")
FILENAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_json(path: Path, errors: list[str]) -> dict | list | None:
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        errors.append(f"Failed to parse {path}: {e}")
        return None


def validate_app(app: str) -> list[str]:
    errors: list[str] = []

    cf_dir = BASE / app / "cf"
    cf_groups_dir = BASE / app / "cf-groups"
    profiles_dir = BASE / app / "quality-profiles"

    # --- Load all CF files ---
    cf_by_tid: dict[str, tuple[str, str]] = {}  # trash_id -> (filename, name)
    if cf_dir.is_dir():
        for f in sorted(cf_dir.glob("*.json")):
            data = load_json(f, errors)
            if data is None:
                continue
            tid = data.get("trash_id", "")
            name = data.get("name", "")
            if tid:
                cf_by_tid[tid] = (f.name, name)

    # --- Check 3: CF filename conventions ---
    if cf_dir.is_dir():
        for f in sorted(cf_dir.glob("*.json")):
            if not FILENAME_RE.match(f.stem):
                errors.append(
                    f"[{app}] CF filename '{f.name}' violates naming convention"
                    " (must be lowercase alphanumeric with dashes)"
                )

    # --- Collect all trash_ids for global uniqueness (Check 1) ---
    # Format: trash_id -> list of locations
    all_ids: dict[str, list[str]] = {}

    # CFs
    for tid, (filename, _) in cf_by_tid.items():
        loc = f"cf/{filename}"
        all_ids.setdefault(tid, []).append(loc)

    # cf-groups (group-level trash_ids)
    cf_groups_data: dict[str, dict] = {}  # filename -> data
    if cf_groups_dir.is_dir():
        for f in sorted(cf_groups_dir.glob("*.json")):
            data = load_json(f, errors)
            if data is None:
                continue
            cf_groups_data[f.name] = data
            tid = data.get("trash_id", "")
            if tid:
                all_ids.setdefault(tid, []).append(f"cf-groups/{f.name}")

    # Quality profiles
    if profiles_dir.is_dir():
        for f in sorted(profiles_dir.glob("*.json")):
            data = load_json(f, errors)
            if data is None:
                continue
            tid = data.get("trash_id", "")
            if tid:
                all_ids.setdefault(tid, []).append(f"quality-profiles/{f.name}")

    # Report duplicates
    for tid, locations in all_ids.items():
        if len(locations) > 1:
            locs = " and ".join(locations)
            errors.append(
                f"[{app}] Duplicate trash_id '{tid}' in {locs}"
            )

    # --- Check 2: cf-groups entries reference valid CFs ---
    for filename, data in cf_groups_data.items():
        for entry in data.get("custom_formats", []):
            entry_name = entry.get("name", "")
            entry_tid = entry.get("trash_id", "")
            if not entry_tid:
                errors.append(
                    f"[{app}] cf-groups/{filename} has entry '{entry_name}'"
                    " missing trash_id"
                )
                continue

            if entry_tid not in cf_by_tid:
                errors.append(
                    f"[{app}] cf-groups/{filename} references trash_id"
                    f" '{entry_tid}' ({entry_name}) which doesn't exist"
                    f" in {app} CFs"
                )
                continue

            cf_filename, cf_name = cf_by_tid[entry_tid]
            if entry_name != cf_name:
                errors.append(
                    f"[{app}] cf-groups/{filename} name mismatch:"
                    f" '{entry_name}' but cf/{cf_filename} has '{cf_name}'"
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

    print("All custom format validations passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
