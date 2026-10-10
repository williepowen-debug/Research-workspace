#!/usr/bin/env python3
"""done_rows_check.py — parser-INDEPENDENT check of PROME/WILL_QUEUE.md decision rows and their ledger events.

WHY THIS EXISTS (2026-10-10, WQ-417 P1; CATO's condition; coldread-wq417 counterexamples)
----------------------------------------------------------------------------------------
Two RECENTLY DONE rows (WQ-416 JANUS, WQ-415 AEOLUS bands) were written with TWO cells. The Deck's
`parse_done_table` skips rows with fewer than three cells, `wq_ledger.py` builds its events through that
parser, and the Decided view renders from it — so Will's rulings were on the queue and nowhere downstream.
`table_check.py` could not see it: the RECENTLY DONE block has no header/separator, so to it the lines are
prose, and its contract calls short rows harmless. Rendering tolerance is not consumer completeness.

CONTRACT — this check is BROADER than the parsers it guards, never equal to them
--------------------------------------------------------------------------------
* Imports NOTHING from decision_deck.py or wq_ledger.py. Two sides sharing one parser omit the same malformed
  row and falsely agree (CATO, 2026-10-10 16:50 ET). DONE_MIN agreement with decision_deck.DONE_ROW_MIN_CELLS is
  asserted by a TEST, never by an import.
* The parsers' row shape is MIRRORED here only to know what they SEE; every `|` line in a decision section that
  they would NOT see is a ❌ (UNPARSED), not a skip — the historical `| | **316 …` shape, `| **WQ-418 …`, an
  indented row, an empty number cell. A ruling token on a non-row line is ❌ ORPHAN-RULING.
* Section detection is STRICTER than the Deck's: exact `## OPEN` / `## RECENTLY DONE` (case-sensitive, like the
  Deck); a case-variant heading is ❌ HEADING-CASE; a second RECENTLY DONE heading is ❌ DUPLICATE-SECTION (the
  Deck reads only the first); either heading missing → rc 2.
* ❌ (rc 1): UNPARSED · SHORT (< DONE_MIN cells) · SHORT-OPEN · UNPARSED-OPEN · DUPLICATE · HEADING-CASE ·
  DUPLICATE-SECTION · ORPHAN-RULING · ROW-OUTSIDE-SECTIONS (a numbered row with a ruling word under any other heading) ·
  NO-LEDGER-EVENT · NOT-TERMINAL (the LAST event is not terminal) · and, for a RULING-CLASS row (RULED/APPROVED/DECLINED
  in its text) whose last ledger event was WRITTEN (`written_at`) on/after REPAIR_DATE:
  VERDICT-DASH (ledger verdict '—'), VERBATIM-LOST (the row says 'verbatim', the ledger holds none), OVER-DONE
  (more than DONE_MIN cells — a shifted cell loses the verdict). Archives: UNPARSED-ARCHIVE · SHORT-ARCHIVE.
* ⚠️ (rc 0): the same three on rows dated BEFORE REPAIR_DATE (grandfathered, counted in the acceptance file) ·
  OVER-OPEN · DATE-FUTURE (any event dated after today — the 2027-05-01 class) · NO-LEDGER-EVENT in an archive.
  In --quiet mode the advisories still print as ONE summary line by kind — never hidden.
* rc 0 clean / rc 1 finding / rc 2 could not establish (missing file or heading).
Acceptance: PROME/tools/tests/ACCEPTANCE_argus_P1_done-rows_2026-10-10.md · tests/test_done_rows_check.py
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import glob
import io
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
QUEUE = ROOT / "PROME/WILL_QUEUE.md"
LEDGER = ROOT / "PROME/registry/WQ_LEDGER.tsv"
ARCHIVE_GLOB = "PROME/archive/WILL_QUEUE_ROWS_*.md"
DONE_MIN = 3                      # title | done | record — the Decided view's contract (tested against decision_deck)
REPAIR_DATE = "2026-10-10"        # ruling-class rules BLOCK for rows whose last ledger event was WRITTEN on/after this (the ledger's own
                                  # `written_at` stamp — never `at`, which the ledger copies from the row's first date and a new ruling can carry an old one;
                                  # read 2 ❌1). An event with no written_at counts as recent (fail closed).
TERMINAL = {"RULED", "DECLINED", "CLOSED"}
STRICT_ROW_RE = re.compile(r"^\|\s*\**\s*(\d+[a-z]?)\b")             # what the Deck/ledger parser accepts (mirror)
OPEN_ROW_RE = re.compile(r"^\|\s*(\d+[a-z]?)\s*\|")
LOOSE_NUM_RE = re.compile(r"\|\s*(?:\|\s*)*\**\s*(?:WQ-)?(\d{2,4}[a-z]?)\b", re.I)   # what a human reads as the number
RULING_RE = re.compile(r"\b(RULED|APPROVED?|DECLINED?)\b")
ISO_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
_SEP_RE = re.compile(r"^:?-{1,}:?$")
_ESC = "\x00"


def split_cells(line: str) -> list[str]:
    s = line.strip().replace("\\|", _ESC)
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.replace(_ESC, "\\|") for c in s.split("|")]


def _is_sep(line: str) -> bool:
    cells = split_cells(line)
    return bool(cells) and all(_SEP_RE.match(c.strip() or "x") for c in cells)


def _is_header(line: str) -> bool:
    first = split_cells(line)[0].strip().lower() if line.strip().startswith("|") else ""
    return first in ("#", "item", "decision", "wq")


def sections(text: str):
    """Exact headings, like the Deck. → (secs, heading_findings). secs = {'OPEN': [(lineno, line)], 'RECENTLY DONE': [...]} (first block each);
    secs['_OUTSIDE'] = every line under any OTHER heading (read 2 ❌2: a ruling row under `## DECIDED TODAY` is invisible to every side)."""
    out: dict[str, list[tuple[int, str]]] = {"_OUTSIDE": []}
    findings = []
    cur = None
    seen: dict[str, int] = {}
    for i, line in enumerate(text.split("\n"), 1):
        if line.startswith("## "):
            h = line[3:].strip()
            key = "OPEN" if h.startswith("OPEN") else "RECENTLY DONE" if h.startswith("RECENTLY DONE") else None
            if key is None:
                up = h.upper()
                if up.startswith("OPEN") or up.startswith("RECENTLY DONE") or up.replace("⚖️", "").strip().startswith("OPEN"):
                    findings.append({"kind": "HEADING-CASE", "wq": "—", "line": i, "detail": f"heading {h!r} is not the exact `## OPEN` / `## RECENTLY DONE` the Deck matches — its rows are invisible downstream"})
                cur = "_OUTSIDE"
                continue
            if key in seen:
                findings.append({"kind": "DUPLICATE-SECTION", "wq": "—", "line": i, "detail": f"second `## {key}` heading (first at L{seen[key]}) — the Deck reads only the first block"})
                cur = "_OUTSIDE"
                continue
            seen[key] = i
            cur = key
            out[key] = []
            continue
        if cur:
            out[cur].append((i, line))
    return out, findings


def read_ledger(text: str) -> dict[str, list[dict]]:
    rows = list(csv.DictReader(io.StringIO(text), delimiter="\t", quoting=csv.QUOTE_NONE))
    by: dict[str, list[dict]] = {}
    for r in rows:
        by.setdefault((r.get("wq") or "").strip(), []).append(r)
    return by


def _f(kind, wq, line, detail, file=None):
    return {"kind": kind, "wq": wq, "line": line, "detail": detail, "file": file}


def scan(queue_text: str, ledger_by_wq: dict[str, list[dict]], today: str | None = None, archives: dict[str, str] | None = None):
    """→ (findings, advisories, stats). Raises ValueError when § OPEN or § RECENTLY DONE is absent (rc 2 at main)."""
    today = today or dt.date.today().isoformat()
    secs, findings = sections(queue_text)
    if "RECENTLY DONE" not in secs:
        raise ValueError("no exact '## RECENTLY DONE' heading — cannot establish the done set")
    if "OPEN" not in secs:
        raise ValueError("no exact '## OPEN' heading — cannot establish the open set (DUPLICATE is undecidable)")
    advisories = []
    # ---- § OPEN
    open_nums: dict[str, int] = {}
    width = None
    open_lines = secs["OPEN"]
    for k, (ln, line) in enumerate(open_lines):
        if line.strip().startswith("|") and k + 1 < len(open_lines) and _is_sep(open_lines[k + 1][1]):
            width = len(split_cells(line))
            break
    for ln, line in open_lines:
        if not line.strip().startswith("|") or _is_sep(line) or _is_header(line):
            continue
        m = OPEN_ROW_RE.match(line)
        if not m:
            lm = LOOSE_NUM_RE.search(line[:80])
            findings.append(_f("UNPARSED-OPEN", lm.group(1) if lm else "?", ln, "a `|` line in § OPEN the Deck's open parser cannot read as `| NNN |` — the decision is invisible to the view"))
            continue
        n = m.group(1)
        open_nums[n] = ln
        c = len(split_cells(line))
        if width is not None and c < width:
            findings.append(_f("SHORT-OPEN", n, ln, f"{c} cells in a {width}-column OPEN table — the Deck's open parser and the view drop it"))
        elif width is not None and c > width:
            advisories.append(_f("OVER-OPEN", n, ln, f"{c} cells in a {width}-column table — table_check reports the dropped cells"))
    # ---- § RECENTLY DONE
    done_nums: dict[str, tuple[int, str]] = {}
    for ln, line in secs["RECENTLY DONE"]:
        s = line.strip()
        if not s:
            continue
        if s.startswith("|"):
            if _is_sep(line) or _is_header(line):
                continue
            m = STRICT_ROW_RE.match(line)
            if not m:
                lm = LOOSE_NUM_RE.search(line[:80])
                findings.append(_f("UNPARSED", lm.group(1) if lm else "?", ln, f"a `|` line in § RECENTLY DONE the Deck/ledger parser cannot read as a numbered row ({line[:40]!r}) — the ruling is invisible downstream"))
                continue
            n = m.group(1)
            if n in done_nums:
                findings.append(_f("DUPLICATE", n, ln, f"also a done row at L{done_nums[n][0]}"))
                continue
            done_nums[n] = (ln, line)
            c = len(split_cells(line))
            if c < DONE_MIN:
                findings.append(_f("SHORT", n, ln, f"{c} cell(s) < {DONE_MIN} (title | done | record) — the Decided view and the event ledger SKIP this row"))
        elif not s.startswith("#") and RULING_RE.search(s):
            findings.append(_f("ORPHAN-RULING", "?", ln, f"a ruling token outside any table row ({s[:60]!r}) — no parser will ever record it"))
    for n in sorted(set(open_nums) & set(done_nums), key=lambda x: int(re.sub(r"\D", "", x) or 0)):
        findings.append(_f("DUPLICATE", n, done_nums[n][0], f"also OPEN at L{open_nums[n]} — two live states"))
    # ---- numbered rows under any OTHER heading that carry a ruling word (read 2 ❌2): no parser reads them
    for ln, line in secs.get("_OUTSIDE", []):
        if line.strip().startswith("|") and not _is_sep(line) and not _is_header(line) and RULING_RE.search(line):
            m = STRICT_ROW_RE.match(line) or OPEN_ROW_RE.match(line)
            lm = LOOSE_NUM_RE.search(line[:80])
            findings.append(_f("ROW-OUTSIDE-SECTIONS", (m or lm).group(1) if (m or lm) else "?", ln, "a numbered row with a ruling word under a heading that is neither `## OPEN` nor `## RECENTLY DONE` — invisible to the Deck, the ledger and this check's section scan"))
    # ---- the ledger, per done row
    for n, (ln, line) in done_nums.items():
        evs = ledger_by_wq.get(n, [])
        if not evs:
            findings.append(_f("NO-LEDGER-EVENT", n, ln, "a done row with NO event in WQ_LEDGER.tsv — the ruling never reached the ledger"))
            continue
        for e in evs:
            at = (e.get("at") or "").strip()
            if at and at > today:
                advisories.append(_f("DATE-FUTURE", n, ln, f"ledger event {e.get('event')} dated {at}, after today {today} — the event took a date from the wrong cell (the 2027-05-01 class)"))
        last = evs[-1]
        if not ((last.get("event") or "").strip() in TERMINAL or (last.get("status_after") or "").strip() in TERMINAL):
            findings.append(_f("NOT-TERMINAL", n, ln, f"the LAST ledger event ({last.get('event')} → {last.get('status_after')}) is not terminal — the ledger still reads this decision as open"))
            continue
        ruling = bool(RULING_RE.search(line))
        written = (last.get("written_at") or "").strip()[:10]
        recent = (not written) or written >= REPAIR_DATE          # the ledger's own clock; empty = fail closed
        sink = findings if (ruling and recent) else advisories
        tag = "" if (ruling and recent) else (f" [grandfathered: ledger event written {written}, before the 2026-10-10 repair]" if ruling else " [not a ruling-class row]")
        c = len(split_cells(line))
        if c > DONE_MIN:
            sink.append(_f("OVER-DONE", n, ln, f"{c} cells > {DONE_MIN} — the parser takes cell 2 as 'done' and cell 3 as 'record'; a shifted cell loses the verdict{tag}"))
        if (last.get("verdict") or "—").strip() in ("—", ""):
            sink.append(_f("VERDICT-DASH", n, ln, f"terminal ledger event carries verdict '—' — the record cell has no lead token (RULED / APPROVED / DECLINED / CLOSED / EXECUTED …){tag}"))
        if "verbatim" in line.lower() and not (last.get("will_verbatim") or "").strip():
            sink.append(_f("VERBATIM-LOST", n, ln, f"the row says 'verbatim' but the ledger's current event holds no will_verbatim — Will's words did not reach the ledger{tag}"))
    # ---- archives (structure ❌; ledger ⚠️ — rotated history, BACKFILL-era)
    arch_rows = legacy = 0
    for name, text in sorted((archives or {}).items()):
        for ln, line in enumerate(text.split("\n"), 1):
            if not line.strip().startswith("|") or _is_sep(line) or _is_header(line):
                continue
            c = split_cells(line)
            if c and c[0].strip()[:1] in ("—", "–"):
                legacy += 1                      # pre-numbering history rows ("| — root rule-6 mirror …"); no parser owns them
                continue
            if OPEN_ROW_RE.match(line) and len(c) >= 6:
                arch_rows += 1
                continue
            m = STRICT_ROW_RE.match(line)
            if not m:
                lm = LOOSE_NUM_RE.search(line[:80])
                findings.append(_f("UNPARSED-ARCHIVE", lm.group(1) if lm else "?", ln, "a `|` line no archive parser reads as a row", file=name))
                continue
            arch_rows += 1
            if len(c) < DONE_MIN:
                findings.append(_f("SHORT-ARCHIVE", m.group(1), ln, f"{len(c)} cell(s) < {DONE_MIN} — parse_archive drops it", file=name))
            elif not ledger_by_wq.get(m.group(1)):
                advisories.append(_f("NO-LEDGER-EVENT", m.group(1), ln, "archived row with no ledger event (history; BACKFILL-era)", file=name))
    stats = {"open_rows": len(open_nums), "done_rows": len(done_nums), "open_width": width, "archive_rows": arch_rows, "archive_legacy_rows": legacy}
    return findings, advisories, stats


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--queue", default=str(QUEUE))
    ap.add_argument("--ledger", default=str(LEDGER))
    ap.add_argument("--no-archives", action="store_true", help="skip PROME/archive/WILL_QUEUE_ROWS_*.md")
    ap.add_argument("--quiet", action="store_true", help="findings, an advisory summary line, and the verdict")
    a = ap.parse_args(argv)
    try:
        qt = pathlib.Path(a.queue).read_text(encoding="utf-8")
        lt = pathlib.Path(a.ledger).read_text(encoding="utf-8")
        archives = {} if a.no_archives else {pathlib.Path(p).name: pathlib.Path(p).read_text(encoding="utf-8")
                                             for p in glob.glob(str(ROOT / ARCHIVE_GLOB))}
    except OSError as e:
        print(f"⚠️  DONE-ROWS UNKNOWN — cannot read {e.filename}: {e.strerror}")
        return 2
    try:
        findings, advisories, stats = scan(qt, read_ledger(lt), archives=archives)
    except ValueError as e:
        print(f"⚠️  DONE-ROWS UNKNOWN — {e}")
        return 2
    for f in findings:
        print(f"❌ DONE-ROWS WQ-{f['wq']} {f['kind']} ({f.get('file') or a.queue}:{f['line']}) — {f['detail']}")
    if a.quiet:
        if advisories:
            kinds: dict[str, int] = {}
            for w in advisories:
                kinds[w["kind"]] = kinds.get(w["kind"], 0) + 1
            print("⚠️  DONE-ROWS advisories: " + " · ".join(f"{k} ×{v}" for k, v in sorted(kinds.items())) + " (run without --quiet for the rows)")
    else:
        for w in advisories:
            print(f"⚠️  DONE-ROWS WQ-{w['wq']} {w['kind']} ({w.get('file') or a.queue}:{w['line']}) — {w['detail']}")
    if findings:
        print(f"❌ DONE-ROWS {len(findings)} finding(s) over {stats['done_rows']} done / {stats['open_rows']} open / {stats['archive_rows']} archived row(s) — fix the ROW; a row the parsers cannot see is a ruling that vanished")
        return 1
    print(f"✅ DONE-ROWS ok — {stats['done_rows']} done row(s) parsed, each with a terminal ledger event; {stats['open_rows']} open row(s) at width {stats['open_width']}; {stats['archive_rows']} archived row(s) parse (+{stats['archive_legacy_rows']} un-numbered legacy)"
          + (f" ({len(advisories)} advisory)" if advisories else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
