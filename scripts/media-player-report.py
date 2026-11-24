#!/usr/bin/env python3
"""Add a Media Player Test Report issue to the Tested Media Players table."""

import argparse
import calendar
import datetime
import difflib
import json
import re
import sys
from pathlib import Path

# Column header (and report form label) -> footnote id part
FORMATS = {
    "DV P5": "dv-p5", "DV P7": "dv-p7", "DV P8": "dv-p8", "FEL": "fel", "MEL": "mel",
    "HDR10": "hdr10", "HDR10+": "hdr10plus", "TrueHD ATMOS": "truehd-atmos", "DTS X": "dts-x",
    "DD+ ATMOS": "ddplus-atmos", "TrueHD": "truehd", "DTS-HD MA": "dts-hd-ma", "FLAC/PCM": "flac-pcm",
    "DD+/E-AC3": "ddplus-eac3", "DTS": "dts", "AAC": "aac", "DD/AC3": "dd-ac3",
    "Hi10": "hi10", "ASS/SSA": "ass-ssa", "PGS": "pgs",
}
HEADER = ["Device", "Player/Product", *FORMATS]
RESULTS = {"✅ Yes": ":white_check_mark:", "❌ No": ":x:"}
SYMBOLS = {":white_check_mark:": "✅", ":x:": "❌", ":grey_question:": "❔"}
TEXT_FIELDS = (
    "Device", "Player/Product", "Discord thread", "Device note", "Player/Product note",
    "Tested by", "Date of test", "TV / AVR used",
)
NOTE_FIELDS = ("Dolby Vision and HDR notes", "Audio notes", "Video and subtitles notes")
FIELDS = {*TEXT_FIELDS, *FORMATS, *NOTE_FIELDS, "AI disclosure"}
DISCORD = re.compile(r"https://discord\.com/channels/492590071455940612/\d+(?:/\d+)?")
NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9 ()+./&',-]{0,79}")
TESTER = re.compile(r"\w[\w .'()-]{0,39}")
DATE = re.compile("(?:" + "|".join(calendar.month_name[1:]) + r") \d{4}")
# No [ ] ^ { } so a link can't hold a footnote reference or attribute list
URL = re.compile(r"https?://[^\s<>\"'`\\|\[\]{}^]*[^\s<>\"'`\\|\[\]{}^.,;:!?)]")
REF = re.compile(r"\[\^([^\]\s]+)\]")
DEF = re.compile(r"\[\^([^\]\s]+)\]: ")
MARKER = "///Footnotes Go Here///"


class ReportError(Exception):
    """Problems the reporter fixes by editing the issue."""


class TableError(Exception):
    """The table isn't in the layout this script reads."""


def escape(text):
    """Entity-encode Markdown and HTML syntax so typed text shows as typed."""
    return re.sub(r"[\\`*_{}\[\]|^~=<>&#+:]", lambda m: f"&#{ord(m.group())};", text)


def plain(text):
    """Text as Markdown that shows what was typed, with http(s) links kept clickable."""
    out, pos = [], 0
    for match in URL.finditer(text):
        url = match.group()
        if text[match.end():match.end() + 1] == ")" and url.count("(") > url.count(")"):
            url += ")"
        out += [escape(text[pos:match.start()]), f"<{url}>"]
        pos = match.start() + len(url)
    return "".join(out) + escape(text[pos:])


def block(text):
    """plain() for text that starts a block: a leading - + 1. : ! ? would start a list or block."""
    text = plain(text)
    return text if text[0].isalpha() or text[0] in "<&" else f"&#{ord(text[0])};{text[1:]}"


def code(text):
    """Reporter text as a code span it can't break out of."""
    return "`" + text.replace("`", "'")[:60] + "`"


def bare(cell):
    return REF.sub("", cell).strip()


def split_row(line):
    if not (line.startswith("|") and line.endswith("|")):
        raise TableError(f"`{line[:60]}` isn't a table row")
    return [cell.strip() for cell in line[1:-1].split("|")]


def join_row(cells):
    return "|" + "".join(f" {cell} |" if cell else " |" for cell in cells)


class Table:
    def __init__(self, text):
        lines = text.split("\n")
        try:
            self.head = next(i for i, line in enumerate(lines) if line.startswith("| Device |"))
            marker = lines.index(MARKER)
        except (StopIteration, ValueError):
            raise TableError("can't find the `| Device |` header row or the footnote marker") from None
        if marker < self.head:
            raise TableError("the footnote marker must come after the table")
        header = [re.sub(r"<[^>]+>", "", re.sub(r"<br\s*/?>", " ", cell)) for cell in split_row(lines[self.head])]
        if header != HEADER:
            raise TableError(f"the columns are {header}, the report script expects {HEADER}")
        separator = split_row("".join(lines[self.head + 1:self.head + 2]))
        if len(separator) != len(HEADER) or not all(re.fullmatch(r":?-+:?", cell) for cell in separator):
            raise TableError(f"the row under the header must be {len(HEADER)} cells like `---` or `:---:`")
        end = next((i for i in range(self.head + 2, len(lines)) if not lines[i].startswith("|")), len(lines))
        stray = next((i for i in range(end, marker) if lines[i].startswith("|")), None)
        if stray is not None:
            raise TableError(f"line {stray + 1} is a table row after the table ended at line {end}; remove the break above it")
        self.rows = [split_row(line) for line in lines[self.head + 2:end]]
        for row in self.rows:
            if len(row) != len(HEADER):
                raise TableError(f"the row for {row[0]} has {len(row)} cells instead of {len(HEADER)}")
        start = next((i for i in range(marker, len(lines)) if DEF.match(lines[i])), len(lines))
        stop = next((i for i in range(start, len(lines)) if lines[i].startswith("*[")), len(lines))
        self.before, self.middle, self.tail = lines[:self.head + 2], lines[end:start], lines[stop:]
        self.defs = {}
        for line in lines[start:stop]:
            match = DEF.match(line)
            if match:
                if match.group(1) in self.defs:
                    raise TableError(f"footnote {match.group(1)} is defined twice")
                chunk = self.defs[match.group(1)] = []
            chunk.append(line)
        for chunk in self.defs.values():
            while chunk and not chunk[-1]:
                chunk.pop()
        self.used = set(self.refs())

    def refs(self):
        """Footnote ids in order of first use."""
        text = "\n".join(self.before + [join_row(row) for row in self.rows] + self.middle)
        return list(dict.fromkeys(REF.findall(text)))

    def add_footnotes(self, new):
        """Add footnotes, drop the ones the rows stopped using, and keep them in first-use order."""
        order = self.refs()
        defs = {k: v for k, v in self.defs.items() if k not in self.used or k in order} | new
        self.defs = {k: defs[k] for k in order if k in defs} | {k: v for k, v in defs.items() if k not in order}

    def render(self):
        lines = self.before + [join_row(row) for row in self.rows] + self.middle
        for chunk in self.defs.values():
            lines += chunk
        return "\n".join(lines + [""] + self.tail)

    def problems(self, text):
        refs, found = self.refs(), []
        found += [f"footnote {fid} is used but has no text" for fid in refs if fid not in self.defs]
        found += [f"footnote {fid} has text but isn't used" for fid in self.defs if fid not in refs]
        if not found and list(self.defs) != refs:
            found.append("footnotes must be listed in the order they're first used, or their numbers come out of order")
        if not found and self.render() != text:
            line = next(i for i, (a, b) in enumerate(zip(text.split("\n") + [None], self.render().split("\n") + [None])) if a != b)
            found.append(f"line {line + 1} isn't in the layout the report script writes (one blank line before the abbreviations, none between footnotes)")
        return found


def parse_fields(body, errors):
    fields, current = {}, None
    for line in body.split("\n"):
        heading = re.fullmatch(r"### (.+)", line)
        if heading:
            current = heading.group(1)
            if current not in FIELDS:
                errors.append(f"{code('### ' + current)} isn't a field of the report form. Remove that line.")
            elif current in fields:
                errors.append(f"`### {current}` appears twice. Remove the extra one.")
            fields[current] = []
        elif current:
            fields[current].append(line)
    values = {name: "\n".join(lines).strip() for name, lines in fields.items()}
    return {name: "" if value == "_No response_" else value for name, value in values.items()}


def read_notes(values, results, errors):
    notes = {}
    for field in NOTE_FIELDS:
        lines = values.get(field, "").split("\n")
        lines = lines[1:-1] if lines[0].startswith("```") and lines[-1].startswith("```") else lines
        for line in filter(str.strip, lines):
            name, colon, note = (part.strip() for part in line.partition(":"))
            if not colon or name not in FORMATS:
                errors.append(f"In **{field}**, {code(line.strip())} must start with a format name and a colon, like `DV P5: note`.")
            elif note and name in notes:
                errors.append(f"**{name}** has two notes. Keep one.")
            elif note and name not in results:
                errors.append(f"**{name}** has a note but no result. Set its result or remove the note.")
            elif note:
                notes[name] = note
    return notes


def read_report(body, author, created):
    errors = []
    values = parse_fields(body, errors)
    report = {}
    for name in TEXT_FIELDS:
        report[name] = values.get(name, "")
        if "\n" in report[name]:
            errors.append(f"**{name}** must be one line.")
    for name in ("Device", "Player/Product"):
        if not NAME.fullmatch(report[name]):
            errors.append(f"**{name}** must be filled in with up to 80 letters, numbers, spaces and `( ) + . / & ' , -`.")
    if not DISCORD.fullmatch(report["Discord thread"]):
        errors.append("**Discord thread** must link to your post on the TRaSH Guides Discord: `https://discord.com/channels/492590071455940612/...`")
    report["Tested by"] = report["Tested by"] or author
    if not TESTER.fullmatch(report["Tested by"]):
        errors.append("**Tested by** can be up to 40 letters, numbers, spaces and `. ' ( ) - _`.")
    report["Date of test"] = report["Date of test"] or f"{calendar.month_name[created.month]} {created.year}"
    if not DATE.fullmatch(report["Date of test"]):
        errors.append("**Date of test** must be a month and year, like `November 2026`.")
    results = {}
    for name in FORMATS:
        value = values.get(name, "")
        if value in RESULTS:
            results[name] = RESULTS[value]
        elif value not in ("", "Not tested"):
            errors.append(f"**{name}** must be Not tested, ✅ Yes or ❌ No.")
    if not results:
        errors.append("Set at least one result to ✅ Yes or ❌ No.")
    report["notes"] = read_notes(values, results, errors)
    report["results"] = results
    if errors:
        raise ReportError(errors)
    return report


def hints(table, device, player):
    def near(word, words):
        folded = {w.casefold(): w for w in words}
        match = difflib.get_close_matches(word.casefold(), folded, n=1, cutoff=0.6)
        return folded[match[0]] if match else None

    devices = list(dict.fromkeys(bare(row[0]) for row in table.rows))
    if device not in devices:
        guess, what = near(device, devices), "device"
    else:
        guess, what = near(player, [bare(row[1]) for row in table.rows if bare(row[0]) == device]), "player/product"
    if not guess:
        return []
    return [f"No row has this {what} yet, so this adds a new row. Did you mean **{guess}**? If so, edit this issue and copy the name from the table."]


def credit(fid, report, issue, repo):
    parts = [
        f"Test Result Provided by: {plain(report['Tested by'])}",
        f"Test Result: <{report['Discord thread']}>",
        f"Date of Test: {report['Date of test']}",
        *([f"TV / AVR: {plain(report['TV / AVR used'])}"] if report["TV / AVR used"] else []),
        f"Report: <https://github.com/{repo}/issues/{issue}>",
    ]
    chunk = [f"[^{fid}]: {parts[0]}<br>"] + [f"    {part}<br>" for part in parts[1:-1]] + [f"    {parts[-1]}"]
    return chunk + (["", f"    {block(report['Device note'])}"] if report["Device note"] else [])


def apply(table, report, issue, repo):
    """Add the report to the table. Returns (status, summary bullets)."""
    device, player = report["Device"], report["Player/Product"]
    fid = f"report-{issue}-tested"
    if fid in table.defs:
        return "in-table", ["This report is already in the table."]
    new = {fid: credit(fid, report, issue, repo)}
    row = next((r for r in table.rows if bare(r[0]) == device and bare(r[1]) == player), None)
    summary = [f"Updates the row for **{device}** with **{player}**."]
    if row is None:
        summary = [f"Adds a row for **{device}** with **{player}**.", *hints(table, device, player)]
        row = [device, player] + [""] * len(FORMATS)
        key = device.casefold()
        table.rows.insert(sum(bare(r[0]).casefold() <= key for r in table.rows), row)
    row[0] += f"[^{fid}]"
    if report["Player/Product note"]:
        new[f"report-{issue}-player"] = [f"[^report-{issue}-player]: {block(report['Player/Product note'])}"]
        row[1] += f"[^report-{issue}-player]"
    added, same, clashes = [], [], []
    for name, result in report["results"].items():
        cell = HEADER.index(name)
        current = bare(row[cell])
        if current in ("", ":grey_question:"):
            row[cell] = result
            if name in report["notes"]:
                note = f"report-{issue}-{FORMATS[name]}"
                new[note] = [f"[^{note}]: {block(report['notes'][name])}"]
                row[cell] += f"[^{note}]"
            added.append(name)
        elif current == result:
            same.append(f"{name} {SYMBOLS[result]}")
        else:
            clashes.append(f"{name} (table {SYMBOLS.get(current, current)}, report {SYMBOLS[result]})")
    results = report["results"]
    summary += [f"Adds {', '.join(f'{name} {SYMBOLS[results[name]]}' for name in added)}."] if added else []
    summary += [f"Already in the table: {', '.join(same)}."] if same else []
    summary += [f"Left as they are, because the table has a different result: {', '.join(clashes)}. A maintainer can change these by hand."] if clashes else []
    dropped = [name for name in report["notes"] if name not in added]
    summary += [f"Notes not added, because the table already has a result there: {', '.join(dropped)}."] if dropped else []
    if not added:
        return "unchanged", summary + ["Nothing to change in the table."]
    table.add_footnotes(new)
    return "changed", summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", help="fail if the table isn't in the layout apply writes")
    check.add_argument("table", type=Path)
    run = commands.add_parser("apply", help="add one report to the table and print the result as JSON")
    run.add_argument("table", type=Path)
    run.add_argument("--body", type=Path, required=True, help="file holding the issue body")
    run.add_argument("--issue", type=int, required=True)
    run.add_argument("--author", required=True)
    run.add_argument(
        "--created", type=lambda value: datetime.datetime.fromisoformat(value.replace("Z", "+00:00")),
        required=True, help="issue creation time, ISO 8601",
    )
    run.add_argument("--repo", required=True)
    args = parser.parse_args(argv)
    text = args.table.read_text(encoding="utf-8")
    try:
        table = Table(text)
        if args.command == "check":
            problems = table.problems(text)
            for problem in problems:
                print(f"::error file={args.table}::{problem}")
            return 1 if problems else 0
        report = read_report(args.body.read_text(encoding="utf-8"), args.author, args.created)
    except TableError as error:
        print(f"::error file={args.table}::{error}")
        return 1
    except ReportError as error:
        print(json.dumps({"status": "invalid", "summary": "\n".join(f"- {e}" for e in error.args[0])}))
        return 0
    status, summary = apply(table, report, args.issue, args.repo)
    if status == "changed":
        args.table.write_text(table.render(), encoding="utf-8")
    print(json.dumps({
        "status": status,
        "title": f"feat(plex): Add test results for {report['Device']} with {report['Player/Product']}",
        "summary": "\n".join(f"- {line}" for line in summary),
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
