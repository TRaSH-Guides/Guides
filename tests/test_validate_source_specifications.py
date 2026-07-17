import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "validate-source-specifications.py"
SPEC = importlib.util.spec_from_file_location("validate_source_specifications", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load validator from {SCRIPT}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class RemuxValidationTests(unittest.TestCase):
    def check_specs(self, specifications, app="radarr", check_remux=True):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "test.json"
            path.write_text(json.dumps({"specifications": specifications}), encoding="utf-8")
            return VALIDATOR.check_file(app, path, check_remux=check_remux)

    def test_accepts_bluray_source_with_remux_modifier(self):
        errors = self.check_specs(
            [
                {
                    "name": "Bluray",
                    "implementation": "SourceSpecification",
                    "fields": {"value": 9},
                },
                {
                    "name": "Remux",
                    "implementation": "QualityModifierSpecification",
                    "fields": {"value": 5},
                },
            ]
        )

        self.assertEqual(errors, [])

    def test_accepts_not_remux_modifier_value_5(self):
        errors = self.check_specs(
            [
                {
                    "name": "Not Remux",
                    "implementation": "QualityModifierSpecification",
                    "fields": {"value": 5},
                }
            ]
        )

        self.assertEqual(errors, [])

    def test_accepts_mixed_sources_with_bluray_and_remux(self):
        errors = self.check_specs(
            [
                {
                    "name": "WEB-DL",
                    "implementation": "SourceSpecification",
                    "fields": {"value": 7},
                },
                {
                    "name": "WEBRip",
                    "implementation": "SourceSpecification",
                    "fields": {"value": 8},
                },
                {
                    "name": "Bluray",
                    "implementation": "SourceSpecification",
                    "fields": {"value": 9},
                },
                {
                    "name": "Remux",
                    "implementation": "QualityModifierSpecification",
                    "fields": {"value": 5},
                },
            ]
        )

        self.assertEqual(errors, [])

    def test_rejects_remux_as_radarr_source(self):
        for name in ("Remux", "Not REMUX", "Bluray Remux", "BLURAYREMUX"):
            with self.subTest(name=name):
                errors = self.check_specs(
                    [
                        {
                            "name": name,
                            "implementation": "SourceSpecification",
                            "fields": {"value": 5},
                        }
                    ]
                )

                self.assertEqual(len(errors), 1)
                self.assertIn("use Bluray source value 9", errors[0])
                self.assertIn("QualityModifierSpecification value 5", errors[0])

    def test_rejects_wrong_radarr_remux_modifier_value(self):
        errors = self.check_specs(
            [
                {
                    "name": "Not Remux",
                    "implementation": "QualityModifierSpecification",
                    "fields": {"value": 4},
                }
            ]
        )

        self.assertEqual(len(errors), 1)
        self.assertIn("expected 5 for Radarr Remux", errors[0])

    def test_remux_modifier_is_ignored_when_check_disabled(self):
        errors = self.check_specs(
            [
                {
                    "name": "Not Remux",
                    "implementation": "QualityModifierSpecification",
                    "fields": {"value": 4},
                }
            ],
            check_remux=False,
        )

        self.assertEqual(errors, [])

    def test_sonarr_remux_remains_a_source(self):
        errors = self.check_specs(
            [
                {
                    "name": "Remux",
                    "implementation": "SourceSpecification",
                    "fields": {"value": 7},
                }
            ],
            app="sonarr",
        )

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
