#!/usr/bin/env python3
"""Validate SourceSpecification value semantics per app.

Radarr's QualitySource enum spans 1-9; Sonarr's spans 1-7. The shared
schemas/specs/source-spec.json enforces the union (1-9) at the JSON
Schema layer. This script enforces the per-app rules:

    1. Range. Sonarr values must be 1-7; values 8 and 9 don't exist
        in Sonarr's enum. Radarr's 1-9 matches the schema, so this is
        a no-op there.
    2. Name->value semantics. For spec *names* with an unambiguous
        expected value per app, the value must match. Example: a spec
        named "WEBDL" must be value 7 under radarr/cf/ and value 3
        under sonarr/cf/. When the wrong value happens to match the
        other app's encoding, the error includes a hint pointing at
        the likely copy-paste source.

The mapping tables below were verified against:
    Radarr/Radarr  src/NzbDrone.Core/Qualities/QualitySource.cs
    Sonarr/Sonarr  src/NzbDrone.Core/Qualities/QualitySource.cs

Known limitations (intentional):

    The `name` field on a SourceSpecification is editorial -- maintainers
    choose it as a human label, not the C# enum identifier. A few labels
    in this repo are intentionally ambiguous:

        - Sonarr CFs often use name="WEB" with value=1 (Sonarr's
            Television source) to catch indexers that misclassify
            streaming content as TV-sourced. "WEB" is therefore NOT in
            the Sonarr table; the schema's 1-7 enum is the only check
            that applies.

    Only labels with a single, unambiguous expected value per app are
    enforced. If a future label becomes ambiguous (the maintainer reuses
    it for a different value), drop it from the table here rather than
    adding exceptions per file.

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

# Per-app valid integer ranges for SourceSpecification.fields.value.
# The shared JSON schema only enforces the union (1..9); per-app bounds
# live here so the schema stays simple.
VALID_VALUES = {
    "radarr": set(range(1, 10)),
    "sonarr": set(range(1, 8)),
}


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

    valid = VALID_VALUES[app]

    for spec in data.get("specifications", []):
        if spec.get("implementation") != "SourceSpecification":
            continue
        spec_name = spec.get("name", "")
        value = spec.get("fields", {}).get("value")

        # Per-app range check. The shared JSON schema accepts the union
        # 1..9; this catches values valid in the other app but not here
        # (e.g. value=8 or 9 in a Sonarr CF).
        if value not in valid:
            errors.append(
                f"[{app}] cf/{path.name}: SourceSpecification"
                f" '{spec_name}' has value {value}, which is outside"
                f" {app}'s QualitySource range {sorted(valid)}"
            )
            continue

        key = normalize(spec_name)
        expected = table.get(key)
        if expected is None:
            # Unknown label — range check above is the only constraint.
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
