import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "media-player-report.py"
SPEC = importlib.util.spec_from_file_location("media_player_report", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {SCRIPT}")
REPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPORT)

HEADER = (
    '| Device | Player/Product | DV P5 | DV P7 | DV P8 | FEL | MEL | HDR10 | <abbr title="HDR10+ note.">HDR10+</abbr>'
    " | TrueHD<br>ATMOS | DTS X | DD+<br>ATMOS | TrueHD | DTS-HD<br>MA | FLAC/PCM | DD+/E-AC3 | DTS | AAC | DD/AC3"
    " | Hi10 | ASS/SSA | PGS |"
)
OK, NO, UNKNOWN = ":white_check_mark:", ":x:", ":grey_question:"


def row(device, player, *results):
    """A table row as the guide writes it: an empty cell is `| |`."""
    cells = [device, player, *results] + [""] * (20 - len(results))
    return "|" + "|".join(f" {cell} " if cell else " " for cell in cells) + "|"


ALPHA_PLEX = row("Alpha Box[^alpha-tested]", "Plex for Alpha", OK, f"{NO}[^fallback]", OK)
ALPHA_INFUSE = row("Alpha Box[^alpha-tested]", "Infuse", OK, NO)
GAMMA = row("Gamma Stick", "Plex for Android (TV)", NO, NO, NO, "", "", OK, f"{UNKNOWN}[^untested]", OK, OK, OK, OK, OK, OK, OK, NO)
ZETA = row("Zeta TV[^zeta-tested]", "Plex for Zeta", OK, OK, OK, "", "", OK, f"{UNKNOWN}[^untested]", OK, f"{UNKNOWN}[^zeta-dtsx]")
TABLE = f"""---
hide:
    - navigation
---

# Tested Media Players

<div class="media-players" markdown>

{HEADER}
| --- | --- |{" :---: |" * 20}
{ALPHA_PLEX}
{ALPHA_INFUSE}
{GAMMA}
{ZETA}

</div>

///Footnotes Go Here///

[^alpha-tested]: Test Result Provided by: Tester One<br>
    Test Result: <https://discord.com/channels/492590071455940612/100000000000000001>

    A second paragraph.
[^fallback]: Will fallback to HDR10
[^untested]: No result yet.
[^zeta-tested]: Test Result Provided by: Tester Two
[^zeta-dtsx]: Not tested yet.

*[DV P5]: DV Profile 5.
"""
THREAD = "https://discord.com/channels/492590071455940612/100000000000000002"
TEXT = ("Device", "Player/Product", "Discord thread", "Device note", "Player/Product note")
SECTIONS = {
    "Dolby Vision and HDR notes": ("DV P5", "DV P7", "DV P8", "FEL", "MEL", "HDR10", "HDR10+"),
    "Audio notes": ("TrueHD ATMOS", "DTS X", "DD+ ATMOS", "TrueHD", "DTS-HD MA", "FLAC/PCM", "DD+/E-AC3", "DTS", "AAC", "DD/AC3"),
    "Video and subtitles notes": ("Hi10", "ASS/SSA", "PGS"),
}


def issue(results=(), notes=(), **fields):
    """An issue body laid out the way GitHub renders the report form."""
    fields = {"Device": "Beta Box", "Player/Product": "Plex for Beta", "Discord thread": THREAD, **fields}
    results, notes = dict(results), dict(notes)
    parts = [(name, fields.get(name) or "_No response_") for name in TEXT]
    for section, names in SECTIONS.items():
        parts += [(name, results.get(name, "Not tested")) for name in names]
        lines = "".join(f"{name}: {notes.get(name, '')}\n" for name in names)
        parts.append((section, f"```text\n{lines}\n```"))
    parts += [(name, fields.get(name) or "_No response_") for name in ("Tested by", "Date of test", "TV / AVR used")]
    parts.append(("AI disclosure", "- [ ] This issue was created with AI assistance."))
    return "\n\n".join(f"### {name}\n\n{value}" for name, value in parts) + "\n"


class TableFile(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.dir.cleanup)
        self.table = Path(self.dir.name) / "table.md"
        self.table.write_text(TABLE, encoding="utf-8")

    def run_script(self, *args):
        out = io.StringIO()
        with redirect_stdout(out):
            code = REPORT.main([str(arg) for arg in args])
        return code, out.getvalue()

    def apply(self, body, number=7):
        path = Path(self.dir.name) / "body.md"
        path.write_text(body, encoding="utf-8")
        code, out = self.run_script(
            "apply", self.table, "--body", path, "--issue", number,
            "--author", "octo-cat", "--created", "2026-11-24T03:00:00Z", "--repo", "TRaSH-Guides/Guides",
        )
        self.assertEqual(code, 0)
        return json.loads(out)

    def text(self):
        return self.table.read_text(encoding="utf-8")


class CheckTests(TableFile):
    def test_accepts_a_table_in_the_written_layout(self):
        self.assertEqual(self.run_script("check", self.table), (0, ""))

    def test_rejects_footnotes_out_of_order(self):
        self.table.write_text(TABLE.replace("[^fallback]: Will fallback to HDR10\n[^untested]: No result yet.\n",
                                            "[^untested]: No result yet.\n[^fallback]: Will fallback to HDR10\n"))
        code, out = self.run_script("check", self.table)
        self.assertEqual(code, 1)
        self.assertIn("in the order they're first used", out)

    def test_rejects_unused_and_missing_footnotes(self):
        self.table.write_text(TABLE.replace(f"{NO}[^fallback]", f"{NO}[^fallbak]"))
        code, out = self.run_script("check", self.table)
        self.assertEqual(code, 1)
        self.assertIn("footnote fallbak is used but has no text", out)
        self.assertIn("footnote fallback has text but isn't used", out)

    def test_rejects_a_layout_it_would_rewrite(self):
        self.table.write_text(TABLE.replace("[^untested]: No result yet.\n", "[^untested]: No result yet.\n\n"))
        code, out = self.run_script("check", self.table)
        self.assertEqual(code, 1)
        self.assertIn("line 27 isn't in the layout", out)

    def test_rejects_a_renamed_column(self):
        self.table.write_text(TABLE.replace("| Hi10 |", "| Hi-10 |", 1))
        code, out = self.run_script("check", self.table)
        self.assertEqual(code, 1)
        self.assertIn("the columns are", out)

    def test_rejects_a_broken_row_or_a_footnote_defined_twice(self):
        twice = TABLE.replace("[^untested]: No result yet.\n", "[^untested]: No result yet.\n[^untested]: Again.\n")
        separator = "the row under the header must be 22 cells like `---` or `:---:`"
        gap = TABLE.replace(f"{ALPHA_INFUSE}\n", f"{ALPHA_INFUSE}\n\n")
        row = gap.split("\n").index(GAMMA) + 1
        for broken, error in (
            (gap, f"line {row} is a table row after the table ended at line {row - 2}; remove the break above it"),
            (TABLE.replace("///Footnotes Go Here///\n", "").replace("# Tested", "///Footnotes Go Here///\n\n# Tested"),
                "the footnote marker must come after the table"),
            (TABLE.replace("| --- | --- |", "| broken | --- |", 1), separator),
            (TABLE.replace("| --- | --- |", "| --- |", 1), separator),
            (TABLE.replace(GAMMA, GAMMA[:-2]), "the row for Gamma Stick has 21 cells instead of 22"),
            (twice, "footnote untested is defined twice"),
        ):
            with self.subTest(error):
                self.table.write_text(broken)
                self.assertEqual(self.run_script("check", self.table), (1, f"::error file={self.table}::{error}\n"))


class NewRowTests(TableFile):
    def test_adds_a_sorted_row_with_credit_and_escaped_notes(self):
        result = self.apply(issue(
            {"DV P5": "✅ Yes", "HDR10": "❌ No"},
            {
                "DV P5": "Plays <b>fine</b> [x](javascript:alert(1)) *bold* ++ctrl++ :x: see https://example.com/a_b.",
                "HDR10": "*Washed out* colours, https://en.wikipedia.org/wiki/HDR_(video)",
            },
            **{"Device note": "- 2. starts like a list", "Tested by": "Some_One", "TV / AVR used": "LG C9 + AVR"},
        ))
        self.assertEqual(result["status"], "changed")
        self.assertEqual(result["title"], "feat(plex): Add test results for Beta Box with Plex for Beta")
        self.assertEqual(result["summary"], "- Adds a row for **Beta Box** with **Plex for Beta**.\n- Adds DV P5 ✅, HDR10 ❌.")
        beta = "| Beta Box[^report-7-tested] | Plex for Beta | :white_check_mark:[^report-7-dv-p5] | | | | | :x:[^report-7-hdr10] |" + " |" * 14
        self.assertIn(f"{ALPHA_INFUSE}\n{beta}\n{GAMMA}\n", self.text())
        self.assertEqual(self.text().count("| Beta Box"), 1)
        self.assertIn(
            "[^fallback]: Will fallback to HDR10\n"
            "[^report-7-tested]: Test Result Provided by: Some&#95;One<br>\n"
            f"    Test Result: <{THREAD}><br>\n"
            "    Date of Test: November 2026<br>\n"
            "    TV / AVR: LG C9 &#43; AVR<br>\n"
            "    Report: <https://github.com/TRaSH-Guides/Guides/issues/7>\n"
            "\n"
            "    &#45; 2. starts like a list\n"
            "[^report-7-dv-p5]: Plays &#60;b&#62;fine&#60;/b&#62; &#91;x&#93;(javascript&#58;alert(1)) &#42;bold&#42; &#43;&#43;ctrl&#43;&#43; &#58;x&#58; "
            "see <https://example.com/a_b>.\n"
            "[^report-7-hdr10]: &#42;Washed out&#42; colours, <https://en.wikipedia.org/wiki/HDR_(video)>\n"
            "[^untested]: No result yet.\n",
            self.text(),
        )
        self.assertEqual(self.run_script("check", self.table), (0, ""))

    def test_new_row_sorts_before_the_first_row(self):
        result = self.apply(issue({"AAC": "✅ Yes"}, Device="AAA Player"))
        self.assertEqual(result["summary"], "- Adds a row for **AAA Player** with **Plex for Beta**.\n- Adds AAC ✅.")
        rows = [line for line in self.text().split("\n") if line.startswith("| ") and "---" not in line]
        self.assertEqual(rows[1], "| AAA Player[^report-7-tested] | Plex for Beta |" + " |" * 15 + " :white_check_mark: |" + " |" * 4)

    def test_hints_a_near_miss_device_or_player(self):
        result = self.apply(issue({"DV P5": "✅ Yes"}, Device="alpha bx"))
        self.assertIn("No row has this device yet, so this adds a new row. Did you mean **Alpha Box**?", result["summary"])
        self.table.write_text(TABLE)
        result = self.apply(issue({"DV P5": "✅ Yes"}, **{"Device": "Alpha Box", "Player/Product": "Infuze"}), number=8)
        self.assertIn("No row has this player/product yet, so this adds a new row. Did you mean **Infuse**?", result["summary"])

    def test_defaults_the_credit_to_the_author_and_issue_month(self):
        self.apply(issue({"PGS": "❌ No"}).replace("\n", "\r\n"))
        self.assertIn("[^report-7-tested]: Test Result Provided by: octo-cat<br>\n", self.text())
        self.assertIn("    Date of Test: November 2026<br>\n    Report: <https://github.com/TRaSH-Guides/Guides/issues/7>\n", self.text())

    def test_reads_a_note_box_edited_without_its_fence(self):
        body = issue({"PGS": "✅ Yes"}, {"PGS": "Sharp"}).replace("```text\nHi10: ", "Hi10: ").replace("PGS: Sharp\n\n```", "PGS: Sharp")
        self.assertEqual(self.apply(body)["status"], "changed")
        self.assertIn("[^report-7-pgs]: Sharp\n", self.text())


class ExistingRowTests(TableFile):
    def test_fills_only_untested_cells_and_lists_the_rest(self):
        result = self.apply(issue(
            {"DV P5": "✅ Yes", "FEL": "✅ Yes", "HDR10+": "✅ Yes", "DTS": "❌ No"},
            {"FEL": "- Plays the FEL", "HDR10+": "https://example.com/hdr shows it", "DTS": "Same as before", "DV P5": "Clashes"},
            **{"Device": "Gamma Stick", "Player/Product": "Plex for Android (TV)", "Player/Product note": "1. Version 1.2"},
        ), number=8)
        self.assertEqual(result["summary"], "\n".join([
            "- Updates the row for **Gamma Stick** with **Plex for Android (TV)**.",
            "- Adds FEL ✅, HDR10+ ✅.",
            "- Already in the table: DTS ❌.",
            "- Left as they are, because the table has a different result: DV P5 (table ❌, report ✅). A maintainer can change these by hand.",
            "- Notes not added, because the table already has a result there: DV P5, DTS.",
        ]))
        gamma = row("Gamma Stick[^report-8-tested]", "Plex for Android (TV)[^report-8-player]", NO, NO, NO, f"{OK}[^report-8-fel]", "",
                    OK, f"{OK}[^report-8-hdr10plus]", OK, OK, OK, OK, OK, OK, OK, NO)
        self.assertIn(f"\n{gamma}\n", self.text())
        self.assertIn(
            "[^report-8-player]: &#49;. Version 1.2\n[^report-8-fel]: &#45; Plays the FEL\n"
            "[^report-8-hdr10plus]: <https://example.com/hdr> shows it\n"
            "[^zeta-tested]: Test Result Provided by: Tester Two\n[^untested]: No result yet.\n",
            self.text(),
        )
        self.assertEqual(self.run_script("check", self.table), (0, ""))

    def test_removes_a_footnote_nothing_uses_any_more(self):
        self.apply(issue({"DTS X": "✅ Yes"}, **{"Device": "Zeta TV", "Player/Product": "Plex for Zeta"}))
        zeta = row("Zeta TV[^zeta-tested][^report-7-tested]", "Plex for Zeta", OK, OK, OK, "", "", OK, f"{UNKNOWN}[^untested]", OK, OK)
        self.assertIn(f"\n{zeta}\n", self.text())
        self.assertNotIn("zeta-dtsx", self.text())
        self.assertIn("[^untested]: No result yet.\n", self.text())
        self.assertEqual(self.run_script("check", self.table), (0, ""))

    def test_matches_names_that_differ_only_in_capitals_and_keeps_the_table_spelling(self):
        result = self.apply(issue({"MEL": "❌ No"}, **{"Device": "gamma STICK", "Player/Product": "plex for android (tv)"}))
        self.assertEqual(result["title"], "feat(plex): Add test results for Gamma Stick with Plex for Android (TV)")
        self.assertEqual(result["summary"], "- Updates the row for **Gamma Stick** with **Plex for Android (TV)**.\n- Adds MEL ❌.")
        gamma = row("Gamma Stick[^report-7-tested]", "Plex for Android (TV)", NO, NO, NO, "", NO, OK, f"{UNKNOWN}[^untested]", OK, OK, OK, OK, OK, OK, OK, NO)
        self.assertIn(f"\n{gamma}\n", self.text())
        self.assertEqual(self.text().count("| Gamma Stick"), 1)
        self.table.write_text(TABLE)
        result = self.apply(issue({"MEL": "❌ No"}, **{"Device": "alpha box", "Player/Product": "Kodi"}), number=8)
        self.assertEqual(result["summary"], "- Adds a row for **Alpha Box** with **Kodi**.\n- Adds MEL ❌.")
        self.assertIn(f"{ALPHA_INFUSE}\n| Alpha Box[^report-8-tested] | Kodi |", self.text())

    def test_changes_nothing_when_every_result_is_already_there(self):
        result = self.apply(issue({"DV P5": "✅ Yes"}, **{"Device": "Alpha Box", "Player/Product": "Infuse"}))
        self.assertEqual(result["status"], "unchanged")
        self.assertIn("- Nothing to change in the table.", result["summary"])
        self.assertEqual(self.text(), TABLE)

    def test_a_report_already_in_the_table_is_not_added_twice(self):
        body = issue({"MEL": "✅ Yes"})
        self.assertEqual(self.apply(body)["status"], "changed")
        once = self.text()
        self.assertEqual(self.apply(body), {"status": "in-table", "title": "feat(plex): Add test results for Beta Box with Plex for Beta",
                                            "summary": "- This report is already in the table."})
        self.assertEqual(self.text(), once)


class InvalidReportTests(TableFile):
    def test_lists_every_problem_and_leaves_the_table(self):
        body = issue(
            {"DV P7": "✅ Yes", "DTS": "Maybe"}, {"AAC": "No result for this"},
            **{
                "Device": "Bad | Box", "Discord thread": "https://discord.com/channels/1/2", "Date of test": "Nov 2026", "Tested by": "<b>",
                "Device note": 'First line\n--8<-- "mkdocs.yml"',
            },
        ) + "\n### Screenshots` @someone `x\n\n_No response_\n"
        result = self.apply(body.replace("DV P8: \n", "Just `some` text\n").replace("HDR10: \n", "DV P7: one\nDV P7: two\n"))
        self.assertEqual(result, {"status": "invalid", "summary": "\n".join([
            "- `### Screenshots' @someone 'x` isn't a field of the report form. Remove that line.",
            "- **Device note** must be one line.",
            "- **Device** must be filled in with up to 80 letters, numbers, spaces and `( ) + . / & ' , -`.",
            "- **Discord thread** must link to your post on the TRaSH Guides Discord: `https://discord.com/channels/492590071455940612/...`",
            "- **Tested by** can be up to 40 letters, numbers, spaces and `. ' ( ) - _`.",
            "- **Date of test** must be a month and year, like `November 2026`.",
            "- **DTS** must be Not tested, ✅ Yes or ❌ No.",
            "- In **Dolby Vision and HDR notes**, `Just 'some' text` must start with a format name and a colon, like `DV P5: note`.",
            "- **DV P7** has two notes. Keep one.",
            "- **AAC** has a note but no result. Set its result or remove the note.",
        ])})
        self.assertEqual(self.text(), TABLE)

    def test_needs_at_least_one_result(self):
        result = self.apply(issue())
        self.assertEqual(result["summary"], "- Set at least one result to ✅ Yes or ❌ No.")

    def test_a_field_twice_is_rejected(self):
        result = self.apply(issue({"DTS": "✅ Yes"}) + "\n### DTS\n\n❌ No\n")
        self.assertEqual(result["summary"], "- `### DTS` appears twice. Remove the extra one.")


if __name__ == "__main__":
    unittest.main()
