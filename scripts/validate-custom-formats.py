#!/usr/bin/env python3
"""Validate custom format consistency per CONTRIBUTING.md rules.

Checks:
    1. Per-app trash_id uniqueness across CF files, cf-groups, and quality profiles
    2. cf-groups entries reference valid CFs (trash_id exists, name matches)
    3. CF and cf-groups filenames follow naming conventions (lowercase, dashes only)
    4. conflicts.json entries reference valid CFs (trash_id exists, name matches)

Exit code 0 on success, 1 on any failure.
"""

import json
import re
import sys
from pathlib import Path

APPS = ("radarr", "sonarr")
BASE = Path("docs/json")
FILENAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_json(path: Path, errors: list[str]) -> dict | None:
    try:
        with open(path) as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        errors.append(f"Failed to parse {path}: {e}")
        return None
    if not isinstance(data, dict):
        errors.append(f"Expected JSON object in {path}, got {type(data).__name__}")
        return None
    return data


def validate_app(app: str) -> list[str]:
    errors: list[str] = []

    cf_dir = BASE / app / "cf"
    cf_groups_dir = BASE / app / "cf-groups"
    conflicts_file = BASE / app / "conflicts.json"
    profiles_dir = BASE / app / "quality-profiles"

    # --- Load all CF files ---
    # Track first occurrence for name matching; all_ids tracks every location
    cf_by_tid: dict[str, tuple[str, str]] = {}  # trash_id -> (filename, name)
    all_ids: dict[str, list[str]] = {}  # trash_id -> list of locations
    if cf_dir.is_dir():
        for f in sorted(cf_dir.glob("*.json")):
            data = load_json(f, errors)
            if data is None:
                continue
            tid = data.get("trash_id", "")
            name = data.get("name", "")
            if tid:
                all_ids.setdefault(tid, []).append(f"cf/{f.name}")
                if tid not in cf_by_tid:
                    cf_by_tid[tid] = (f.name, name)

    # --- Check 3: CF filename conventions ---
    if cf_dir.is_dir():
        for f in sorted(cf_dir.glob("*.json")):
            if not FILENAME_RE.match(f.stem):
                errors.append(
                    f"[{app}] CF filename '{f.name}' violates naming convention"
                    " (must be lowercase alphanumeric with dashes)"
                )

    # --- Check 3: cf-groups filename conventions ---
    if cf_groups_dir.is_dir():
        for f in sorted(cf_groups_dir.glob("*.json")):
            if not FILENAME_RE.match(f.stem):
                errors.append(
                    f"[{app}] cf-groups filename '{f.name}' violates naming"
                    " convention (must be lowercase alphanumeric with dashes)"
                )

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
            errors.append(f"[{app}] Duplicate trash_id '{tid}' in {locs}")

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

    # --- Check 4: conflicts.json entries reference valid CFs ---
    if conflicts_file.is_file():
        conflicts_data = load_json(conflicts_file, errors)
        if conflicts_data is not None:
            for group in conflicts_data.get("custom_formats", []):
                for tid, entry in group.items():
                    if tid == "$schema":
                        continue
                    if not isinstance(entry, dict):
                        continue
                    entry_name = entry.get("name", "")

                    if tid not in cf_by_tid:
                        errors.append(
                            f"[{app}] conflicts.json references trash_id"
                            f" '{tid}' ({entry_name}) which doesn't exist"
                            f" in {app} CFs"
                        )
                        continue

                    cf_filename, cf_name = cf_by_tid[tid]
                    if entry_name != cf_name:
                        errors.append(
                            f"[{app}] conflicts.json name mismatch:"
                            f" '{entry_name}' but cf/{cf_filename}"
                            f" has '{cf_name}'"
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
