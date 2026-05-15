#!/usr/bin/env python3
"""Validate SourceSpecification value semantics per app.

Radarr and Sonarr both accept integer values 1-9 for SourceSpecification,
but the underlying enums differ. A CF authored for Sonarr that uses Radarr's
WEBDL value (7) will silently match the wrong source in Sonarr (BlurayRaw),
and vice versa. JSON Schema can't catch this because both ranges overlap;
the only signal is which folder the CF lives in.

This script enforces the mapping for spec names that have an unambiguous
expected value per app. Specs whose names don't match a known label are
ignored (the schema's 1-9 enum still applies to those).

Exit code 0 on success, 1 on any failure.
"""

import json
import re
import sys
from pathlib import Path

BASE = Path("docs/json")

# name -> expected fields.value, per app.
# Keys are normalized (uppercased, non-alphanumerics stripped).
RADARR_SOURCE = {
    "CAM": 1,
    "TELESYNC": 2,
    "TS": 2,
    "TELECINE": 3,
    "TC": 3,
    "WORKPRINT": 4,
    "WP": 4,
    "DVD": 5,
    "TV": 6,
    "WEBDL": 7,
    "WEBRIP": 8,
    "BLURAY": 9,
}

SONARR_SOURCE = {
    "TELEVISION": 1,
    "TELEVISIONRAW": 2,
    "WEBDL": 3,
    "WEBRIP": 4,
    "DVD": 5,
    "BLURAY": 6,
    "BLURAYRAW": 7,
    "REMUX": 7,
    "BLURAYREMUX": 7,
}

EXPECTED = {"radarr": RADARR_SOURCE, "sonarr": SONARR_SOURCE}


def normalize(name: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", name.upper())


def check_file(app: str, path: Path) -> list[str]:
    errors: list[str] = []
    try:
        with open(path) as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        return [f"[{app}] cf/{path.name}: failed to parse: {e}"]

    table = EXPECTED[app]
    other_app = "sonarr" if app == "radarr" else "radarr"
    other_table = EXPECTED[other_app]

    for spec in data.get("specifications", []):
        if spec.get("implementation") != "SourceSpecification":
            continue
        spec_name = spec.get("name", "")
        value = spec.get("fields", {}).get("value")
        key = normalize(spec_name)
        expected = table.get(key)
        if expected is None:
            # Unknown label — skip (schema enum still bounds value to 1-9).
            continue
        if value == expected:
            continue

        msg = (
            f"[{app}] cf/{path.name}: SourceSpecification '{spec_name}'"
            f" has value {value}, expected {expected} for {app}"
        )
        # Helpful hint when the value matches the *other* app's mapping.
        if other_table.get(key) == value:
            msg += (
                f" (value {value} is the {other_app} encoding for"
                f" '{spec_name}' — looks like a copy-paste from"
                f" {other_app}/cf/)"
            )
        errors.append(msg)

    return errors


def main() -> int:
    all_errors: list[str] = []
    for app in ("radarr", "sonarr"):
        cf_dir = BASE / app / "cf"
        if not cf_dir.is_dir():
            continue
        for f in sorted(cf_dir.glob("*.json")):
            all_errors.extend(check_file(app, f))

    if all_errors:
        print(f"\nFound {len(all_errors)} SourceSpecification error(s):\n")
        for err in all_errors:
            print(f"  ERROR: {err}")
        return 1

    print("All SourceSpecification values match the expected per-app mapping.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
