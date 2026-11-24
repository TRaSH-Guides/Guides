"""Runs the report workflow's shell steps as written, with a fake gh in front of the real jq."""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts" / "media-player-report.py"
WORKFLOW = yaml.safe_load((ROOT / ".github" / "workflows" / "media-player-report.yml").read_text(encoding="utf-8"))
SPEC = importlib.util.spec_from_file_location("media_player_report", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {SCRIPT}")
REPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPORT)

# Answers from a JSON file per command, applies --jq like gh does, and keeps the last body it posts
FAKE_GH = r"""#!/bin/bash
printf '%s\n' "$*" >> "$GH_LOG"
expr= source=
for ((i = 1; i <= $#; i++)); do
    arg=${!i} next=$((i + 1))
    case "$arg" in
        --jq) expr=${!next} ;;
        --body-file) cp "${!next}" "$GH_POSTED" ;;
        body=@*) cp "${arg#body=@}" "$GH_POSTED" ;;
    esac
done
case "$1 $2" in
    "issue view") source=$GH_ISSUE ;;
    "issue list") source=$GH_ISSUES ;;
    "pr list") source=$GH_PRS ;;
    api\ *) [[ -n "$expr" ]] && source=$GH_COMMENTS ;;
esac
[[ -n "$source" ]] || exit 0
if [[ -n "$expr" ]]; then jq -rc "$expr" "$source"; else cat "$source"; fi
"""
TABLE = f"| {' | '.join(REPORT.HEADER)} |\n|{' --- |' * len(REPORT.HEADER)}\n\n{REPORT.MARKER}\n"
THREAD = "https://discord.com/channels/492590071455940612/100000000000000002"
ISSUE = {
    "author": {"id": "U_1", "is_bot": False, "login": "octo-cat", "name": ""},
    "body": f"### Device\n\nTest Box\n\n### Player/Product\n\nTest Player\n\n### Discord thread\n\n{THREAD}\n\n### DV P5\n\n✅ Yes\n",
    "createdAt": "2026-11-24T03:00:00Z",
    "state": "OPEN",
}
MARKER = "<!-- media-player-report -->"
COMMENTS = [
    {"id": 111, "user": {"login": "octo-cat"}, "body": f"{MARKER}\n\nNot from the workflow"},
    {"id": 222, "user": {"login": "github-actions[bot]"}, "body": f"{MARKER}\n\nAn earlier result"},
]
FAILED = "Something went wrong while adding this report. A maintainer can check the [workflow run](https://example.invalid/run)."


class WorkflowStep(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.dir = Path(temp.name)
        bin_dir = self.dir / "bin"
        bin_dir.mkdir()
        for name, text in (("gh", FAKE_GH), ("python", f'#!/bin/sh\nexec "{sys.executable}" "$@"\n')):
            (bin_dir / name).write_text(text, encoding="utf-8")
            (bin_dir / name).chmod(0o755)
        self.env = {
            **os.environ, **WORKFLOW["env"],
            "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}", "RUNNER_TEMP": str(self.dir),
            "GITHUB_OUTPUT": str(self.dir / "output"), "GH_LOG": str(self.dir / "gh.log"), "GH_POSTED": str(self.dir / "posted.md"),
            "GH_REPO": "TRaSH-Guides/Guides", "GITHUB_REPOSITORY": "TRaSH-Guides/Guides", "ISSUE": "7",
        }

    def answer(self, name, data):
        path = self.dir / "answers" / f"{name}.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(data), encoding="utf-8")
        self.env[f"GH_{name.upper()}"] = str(path)

    def run_step(self, job, name, **env):
        for path in (self.dir / "output", self.dir / "gh.log", self.dir / "posted.md"):
            path.unlink(missing_ok=True)
        script = self.dir / "step.sh"
        script.write_text(next(step for step in WORKFLOW["jobs"][job]["steps"] if step["name"] == name)["run"], encoding="utf-8")
        return subprocess.run(["bash", "-e", str(script)], cwd=self.dir, env={**self.env, **env}, capture_output=True, text=True)

    def outputs(self):
        found, lines = {}, iter((self.dir / "output").read_text(encoding="utf-8").splitlines())
        for line in lines:
            name, sep, value = line.partition("=")
            if not sep:
                name, _, end = line.partition("<<")
                value = "\n".join(iter(lines.__next__, end))
            found[name] = value
        return found

    def calls(self):
        return (self.dir / "gh.log").read_text(encoding="utf-8").splitlines()


class ListStep(WorkflowStep):
    def test_a_report_is_recognised_by_the_label_the_workflow_adds(self):
        self.assertIn(f"contains(github.event.issue.labels.*.name, '{WORKFLOW['env']['LABEL']}')", WORKFLOW["jobs"]["list"]["if"])

    def test_a_dispatched_number_is_built_and_anything_else_refused(self):
        self.assertEqual(self.run_step("list", "List the reports to build", NUMBER="42").returncode, 0)
        self.assertEqual(self.outputs(), {"issues": "[42]"})
        refused = self.run_step("list", "List the reports to build", NUMBER="42abc")
        self.assertEqual((refused.returncode, refused.stdout), (1, "::error::The issue must be a number.\n"))

    def test_a_refresh_lists_open_labelled_reports_and_warns_at_the_limit(self):
        self.answer("issues", [{"number": number} for number in range(1, 257)])
        result = self.run_step("list", "List the reports to build", NUMBER="")
        self.assertEqual(self.calls(), ["issue list --label Type: Media Player Report --state open --limit 256 --json number --jq map(.number)"])
        self.assertEqual(result.stdout, "::warning::There are 256 or more open reports; only 256 are refreshed.\n")
        self.assertEqual(json.loads(self.outputs()["issues"]), list(range(1, 257)))


class ApplyStep(WorkflowStep):
    def setUp(self):
        super().setUp()
        (self.dir / "scripts").mkdir()
        (self.dir / "scripts" / SCRIPT.name).write_bytes(SCRIPT.read_bytes())
        self.table = self.dir / "docs" / "Plex" / "tested-media-players.md"
        self.table.parent.mkdir(parents=True)
        self.table.write_text(TABLE, encoding="utf-8")

    def apply(self, **changes):
        self.answer("issue", {**ISSUE, **changes})
        return self.run_step("report", "Add the report to the table")

    def test_an_open_report_is_added(self):
        self.assertEqual(self.apply().returncode, 0)
        self.assertEqual(self.outputs(), {
            "status": "changed", "title": "feat(plex): Add test results for Test Box with Test Player",
            "summary": "- Adds a row for **Test Box** with **Test Player**.\n- Adds DV P5 ✅.",
        })
        self.assertIn("\n| Test Box[^report-7-tested] | Test Player | :white_check_mark: |", self.table.read_text(encoding="utf-8"))

    def test_another_kind_of_issue_is_skipped(self):
        for changes in ({"body": "How do I set up Plex?"}, {"body": None}):
            with self.subTest(changes):
                result = self.apply(**changes)
                self.assertEqual((result.returncode, self.outputs()), (0, {"status": "skipped"}))
                self.assertEqual(result.stdout, "::warning::Issue 7 isn't an open media player report, so there's nothing to build.\n")
                self.assertEqual(self.table.read_text(encoding="utf-8"), TABLE)

    def test_a_table_the_script_cant_read_fails_with_the_reason_in_the_log(self):
        self.table.write_text(TABLE.replace("| Hi10 |", "| Hi-10 |"), encoding="utf-8")
        result = self.apply()
        self.assertEqual(result.returncode, 1)
        self.assertTrue(result.stdout.startswith("::error file=docs/Plex/tested-media-players.md::the columns are "), result.stdout)


    def test_closing_a_report_closes_its_own_pull_request_only(self):
        listed = (
            "pr list --head feat/plex-media-player-report-issue-7 --state open --json number,isCrossRepository "
            "--jq map(select(.isCrossRepository | not)) | .[0].number // empty"
        )
        for prs, expected in (
            ([{"number": 321, "isCrossRepository": False}], [
                listed, "pr close 321 --comment Closed because #7 was closed.",
                "api --method DELETE repos/TRaSH-Guides/Guides/git/refs/heads/feat/plex-media-player-report-issue-7",
            ]),
            ([{"number": 999, "isCrossRepository": True}], [listed]),
            ([], [listed]),
        ):
            with self.subTest(prs):
                self.answer("prs", prs)
                result = self.apply(state="CLOSED")
                self.assertEqual((result.returncode, result.stdout, self.outputs()), (0, "", {"status": "skipped"}))
                self.assertEqual(self.calls(), ["issue view 7 --json body,author,createdAt,state", *expected])
                self.assertEqual(self.table.read_text(encoding="utf-8"), TABLE)


class CommentStep(WorkflowStep):
    def comment(self, status, summary, operation=""):
        self.answer("comments", COMMENTS)
        env = {"STATUS": status, "SUMMARY": summary, "PR": "321", "OPERATION": operation, "RUN": "https://example.invalid/run"}
        self.assertEqual(self.run_step("report", "Comment on the issue", **env).returncode, 0)
        return (self.dir / "posted.md").read_text(encoding="utf-8")

    def test_each_outcome_tells_the_reporter_what_happened(self):
        merged = "#321 adds your results to the table once a maintainer merges it."
        for status, operation, summary, intro in (
            ("changed", "created", "- Adds DV P5 ✅.",
                f"Thanks for testing! {merged} To change something, edit this issue and the pull request updates."),
            ("unchanged", "closed", "- Nothing to change in the table.",
                "There's nothing new to add to the table. The pull request for this report is closed."),
            ("in-table", "", "- This report is already in the table.", "Your results are in the table. Thanks for testing!"),
            ("invalid", "", "- Set at least one result to ✅ Yes or ❌ No.",
                "Your report needs a fix before it can be added. Edit this issue to fix it. "
                "Until then, any pull request for this report keeps its earlier results."),
            ("failed", "", "", FAILED),
        ):
            with self.subTest(status):
                self.assertEqual(self.comment(status, summary, operation), f"{MARKER}\n\n{intro}\n\n{summary}\n")

    def test_a_failed_run_does_not_list_results_as_added(self):
        self.assertEqual(self.comment("failed", "- Adds DV P5 ✅."), f"{MARKER}\n\n{FAILED}\n\n\n")

    def test_it_edits_its_own_comment_and_never_anyone_elses(self):
        self.comment("in-table", "- This report is already in the table.")
        patched = [call.split()[3] for call in self.calls() if call.startswith("api --method PATCH")]
        self.assertEqual(patched, ["repos/TRaSH-Guides/Guides/issues/comments/222"])
        self.answer("comments", COMMENTS[:1])
        self.assertEqual(self.run_step("report", "Comment on the issue", STATUS="in-table", SUMMARY="", PR="", OPERATION="", RUN="").returncode, 0)
        posted = [call for call in self.calls() if not call.startswith("api --paginate")]
        self.assertEqual(posted, [f"issue comment 7 --body-file {self.dir / 'comment.md'}"])


if __name__ == "__main__":
    unittest.main()
