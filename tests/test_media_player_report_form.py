import datetime
import importlib.util
import re
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts" / "media-player-report.py"
FORM = yaml.safe_load((ROOT / ".github" / "ISSUE_TEMPLATE" / "media-player-test-report.yml").read_text(encoding="utf-8"))
WORKFLOW_TEXT = (ROOT / ".github" / "workflows" / "media-player-report.yml").read_text(encoding="utf-8")
WORKFLOW = yaml.safe_load(WORKFLOW_TEXT)
STALE = yaml.safe_load((ROOT / ".github" / "stale.yml").read_text(encoding="utf-8"))
SPEC = importlib.util.spec_from_file_location("media_player_report", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {SCRIPT}")
REPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPORT)

FIELDS = [item for item in FORM["body"] if item["type"] != "markdown"]
THREAD = "https://discord.com/channels/492590071455940612/100000000000000002"
CREATED = datetime.datetime(2026, 11, 24, tzinfo=datetime.timezone.utc)


def render(answers):
    """The issue body GitHub writes for this form, with answers keyed by field id."""
    parts = []
    for item in FIELDS:
        attrs = item["attributes"]
        if item["type"] == "dropdown":
            value = answers.get(item["id"], attrs["options"][attrs["default"]])
        elif item["type"] == "checkboxes":
            value = "\n".join(f"- [ ] {option['label']}" for option in attrs["options"])
        else:
            value = answers.get(item["id"], attrs.get("value", "")) or "_No response_"
            if attrs.get("render") and value != "_No response_":
                value = f"```{attrs['render']}\n{value}\n```"
        parts.append(f"### {attrs['label']}\n\n{value}")
    return "\n\n".join(parts) + "\n"


class FormTests(unittest.TestCase):
    def test_fields_match_what_the_script_reads(self):
        self.assertEqual(sorted(item["attributes"]["label"] for item in FIELDS), sorted(REPORT.FIELDS))
        dropdowns = {item["attributes"]["label"]: item["attributes"]["options"] for item in FIELDS if item["type"] == "dropdown"}
        self.assertEqual(dropdowns, {name: ["Not tested", *REPORT.RESULTS] for name in REPORT.FORMATS})
        required = [item["id"] for item in FIELDS if item.get("validations", {}).get("required")]
        self.assertEqual(required, ["device", "player", "discord_thread"])

    def test_the_workflow_and_stale_settings_use_the_form_label(self):
        self.assertEqual(FORM["labels"], [WORKFLOW["env"]["LABEL"]])
        self.assertIn(WORKFLOW["env"]["LABEL"], STALE["exemptLabels"])

    def test_the_workflow_only_picks_issues_by_the_form_discord_thread_heading(self):
        thread = next(item for item in FIELDS if item["id"] == "discord_thread")["attributes"]["label"]
        self.assertEqual(set(re.findall(r"### ([^'\"]+)", WORKFLOW_TEXT)), {thread})

    def test_note_boxes_list_each_format_once(self):
        notes = [item["attributes"] for item in FIELDS if item["attributes"]["label"] in REPORT.NOTE_FIELDS]
        names = [line.partition(":")[0] for attrs in notes for line in attrs["value"].splitlines()]
        self.assertEqual(names, list(REPORT.FORMATS))

    def test_a_filled_in_form_reads_as_a_report(self):
        hdr = next(item for item in FIELDS if item["id"] == "hdr_notes")["attributes"]["value"]
        body = render({
            "device": "Beta Box", "player": "Plex for Beta", "discord_thread": THREAD,
            "dv_p5": "✅ Yes", "aac": "❌ No", "hdr_notes": hdr.replace("DV P5: ", "DV P5: Plays fine"),
        })
        report = REPORT.read_report(body, "octo-cat", CREATED)
        self.assertEqual(report["results"], {"DV P5": ":white_check_mark:", "AAC": ":x:"})
        self.assertEqual(report["notes"], {"DV P5": "Plays fine"})
        self.assertEqual((report["Device"], report["Tested by"], report["Date of test"]), ("Beta Box", "octo-cat", "November 2026"))

    def test_a_form_left_on_not_tested_asks_for_a_result(self):
        body = render({"device": "Beta Box", "player": "Plex for Beta", "discord_thread": THREAD})
        with self.assertRaises(REPORT.ReportError) as raised:
            REPORT.read_report(body, "octo-cat", CREATED)
        self.assertEqual(raised.exception.args[0], ["Set at least one result to ✅ Yes or ❌ No."])


if __name__ == "__main__":
    unittest.main()
