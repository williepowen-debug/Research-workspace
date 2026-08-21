#!/usr/bin/env python3
"""Banner-tolerant TSV reading for MARCO's workbook/docket ledgers.

WHY THIS EXISTS
---------------
MARCO's ledgers are moving to the PAT-044 two-clock header — a leading comment
line carrying `Last real data refresh: YYYY-MM-DD`. That header is the *portable*
staleness signal: it survives clone-flattened git history (cloud sessions) and it
survives a hygiene-edit commit, both of which make git-time grading go
false-clean on genuinely stale data.

The cost is that every reader must skip it, and the naive skips fail in two ways
that do NOT announce themselves:

  1. `header = f.readline()` reads the BANNER as the header row. Column lookups
     like `header.index("Status")` then miss, the code takes its
     not-found fallback, and every row silently classifies as unclassified.
     Nothing raises. The check keeps printing, and prints wrong.

  2. `next(f)` (or `awk NR>1`) skips the banner and then reads the REAL HEADER
     ROW AS DATA — inflating the denominator by exactly one. RED hit this on its
     own VX.tsv (S33: published "9 of 18 live vectors" when the true denominator
     was 17). The numerator was unaffected, because the header's date cell is the
     literal string "Last Updated" and loses a date comparison. So the error
     surfaces ONLY in the total: an off-by-one that FLATTERS a ratio and is
     invisible by eye.

Both failure modes are silent-degradation, not crashes, which is why this is a
function rather than a prose warning in the banner. RED's own note says it best:
*prose warnings do not parse.* MARCO's VX.tsv banner warns too — and this module
is what actually enforces it.

Ported from RED's `scripts/review_debt.py::rows()` (donor named deliberately —
porting a fix EXPOSES what a reinvention would hide, and RED had already paid for
this bug in production).

USAGE
-----
    from tsvutil import read_tsv, write_tsv, banner_of
    header, rows = read_tsv(path)          # rows are lists of cells
    write_tsv(path, header, rows, banner_of(path))   # LF-safe round-trip
    idx = col(header, "Last Updated")      # -1 if absent, never raises
"""
from pathlib import Path


def strip_banner(lines):
    """Drop leading comment/blank lines so lines[0] is the real header row.

    Skips '#'-prefixed lines and blank lines ANYWHERE in the leading block —
    a multi-line banner (MARCO's FLOW.tsv carries eight) must not leave a
    stray comment where the header is expected.
    """
    i = 0
    while i < len(lines) and (not lines[i].strip() or lines[i].lstrip().startswith("#")):
        i += 1
    return lines[i:]


def read_tsv(path):
    """Return (header_cells, data_rows) with any leading banner removed.

    Blank lines anywhere are dropped; rows whose first cell is empty are dropped
    (trailing-newline and spacer artifacts), matching what the callers already did
    inline. Returns ([], []) for a missing or banner-only file rather than raising,
    so a caller's own "not found" message stays the one the user sees.
    """
    p = Path(path)
    if not p.exists():
        return [], []
    lines = [ln.rstrip("\n") for ln in p.read_text(encoding="utf-8").split("\n")]
    lines = strip_banner(lines)
    if not lines:
        return [], []
    # ⚠️ CSV-AWARE, NOT a raw split("\t"). The naive split was this module's own
    # founding bug (2026-08-21): it returned the ESCAPED text of a quoted field as
    # literal characters, so a read->edit->csv.writer round-trip re-escaped what was
    # already escaped and DOUBLED every quote. Five VX rows compounded 12 decoded
    # quotes into 3,574 across four passes in one session before a byte-level diff
    # caught it. A raw split ALSO silently truncates any field containing an
    # embedded newline. csv.reader handles both; nothing else does.
    #   ⚠️ Correction 2026-08-21 (s23): the founding comment cited VX as a live
    #   instance of the embedded-newline half — "VX has several, which is why its 57
    #   rows occupy 91 physical lines." That is FALSE and was never true: all 49
    #   commits of VX.tsv were scanned and ZERO have an embedded newline in any cell.
    #   The 91 lines are 33 banner + 1 header + 57 rows. The QUOTING half above is
    #   real and is the reason this reader is csv-aware; the newline half is a
    #   fabricated corroborating detail written during the fix pass that repaired the
    #   quoting. Kept as a warning about the failure mode, not as a claim about VX.
    import csv as _csv
    rows = []
    header = None
    for cells in _csv.reader(lines, delimiter="\t"):
        if header is None:
            header = cells
            continue
        if not cells or not cells[0].strip():
            continue
        rows.append(cells)
    return (header or []), rows


def read_tsv_numbered(path):
    """Like read_tsv, but each row is (file_lineno, cells) with lineno 1-BASED.

    Exists because predictions_due.py reports schema warnings by file line number
    ("PREDICTIONS.tsv:14 has 8 cols, expected 9"). If a banner is added and the
    reader silently re-bases its numbering, every one of those warnings points at
    the wrong row — a defect that makes the check ACTIVELY misleading rather than
    merely wrong, because the operator goes and inspects an innocent line.
    Preserving true file position is therefore part of the contract, not a nicety.

    ⚠️ FIXED 2026-08-21 (s23) — THIS FUNCTION WAS LEFT ON THE RAW `split("\\t")` THAT
    `read_tsv` WAS REPAIRED OFF THE SAME DAY. The fix cleared the region being looked
    at, not the module: the corrected reader and the uncorrected one sat 40 lines
    apart, and the second one had the first one's warning comment directly above it.
    Live consequence: `predictions_due.py` is the only caller, and it received
    ESCAPED text, so its doubled-quote check fired on FOUR correctly-escaped rows of
    PREDICTIONS.tsv and told the operator to *"collapse "" to ""* — remediation that
    would have re-introduced the exact corruption class the check was written to
    catch. Measured at the time of the fix: the two readers DISAGREED on 5 of 6
    MARCO ledgers (PREDICTIONS, VX, KB, FLOW, CATALYSTS), agreeing only on
    MIGRATION_PROXIES, which happens to contain no quoted field.

    Line numbering under csv.reader: `reader.line_num` counts PHYSICAL lines
    consumed, so a record that spans an embedded newline still reports the line it
    STARTED on. That is the number an operator needs to go look at.
    """
    p = Path(path)
    if not p.exists():
        return [], []
    raw = p.read_text(encoding="utf-8").split("\n")
    # Banner offset in PHYSICAL lines — `i` is the 0-based index of the header row,
    # so file line numbers below are `i + <lines consumed> + 1`.
    i = 0
    while i < len(raw) and (not raw[i].strip() or raw[i].lstrip().startswith("#")):
        i += 1
    body = raw[i:]
    if not body:
        return [], []
    import csv as _csv
    reader = _csv.reader(body, delimiter="\t")
    header = None
    rows = []
    consumed = 0
    for cells in reader:
        start = i + consumed + 1        # 1-based file line this record STARTS on
        consumed = reader.line_num      # physical lines of `body` read so far
        if header is None:
            header = cells
            continue
        if not cells or not cells[0].strip():
            continue
        rows.append((start, cells))
    return (header or []), rows


def write_tsv(path, header, rows, banner=""):
    """Write a TSV with LF terminators, preserving an optional banner block.

    ⚠️ USE THIS INSTEAD OF csv.writer DIRECTLY. Python's csv.writer defaults to
    `lineterminator="\r\n"` on every platform, so a routine "read, edit one row,
    write back" silently converts an LF ledger to CRLF — or, worse, produces a
    MIXED file when a banner written with plain write() sits above rows written by
    csv.writer. That is exactly what happened to VX.tsv on 2026-08-21: 58 CRLF
    lines under 26 LF banner lines.

    The data impact was nil — Python text-mode reads normalise line endings, so no
    parser ever saw the stray \r — but the diff impact was not: renumbering two
    IDs in KB.tsv produced a 105-line diff in which the two real edits were
    invisible. A review that cannot see the change it is reviewing is the cost.
    """
    import csv as _csv
    with open(path, "w", newline="", encoding="utf-8") as f:
        if banner:
            f.write(banner if banner.endswith("\n") else banner + "\n")
        w = _csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def banner_of(path):
    """Return the leading comment block of a TSV verbatim (including its newlines)."""
    p = Path(path)
    if not p.exists():
        return ""
    out = []
    for ln in p.read_text(encoding="utf-8").split("\n"):
        if ln.lstrip().startswith("#") or (not ln.strip() and out):
            out.append(ln)
        else:
            break
    return "\n".join(out) + ("\n" if out else "")


def col(header, name, default=-1):
    """Index of a named column, or `default`. Never raises.

    Callers previously wrapped `header.index(...)` in try/except and fell back to
    a positional guess. That fallback is exactly what turns failure mode (1) above
    into a silent wrong answer, so prefer checking for the sentinel explicitly.
    """
    try:
        return header.index(name)
    except ValueError:
        return default


def cell(row, idx, default=""):
    """Safe cell access for ragged rows."""
    if idx is None or idx == -1:
        return default
    if -len(row) <= idx < len(row):
        return row[idx]
    return default


def content_vintage(path):
    """Return the PAT-044 'Last real data refresh: YYYY-MM-DD' date, or None.

    Mirrors the regex the fleet-wide scripts/ledger_staleness.py uses, so a MARCO
    surface and the fleet checker agree on what a ledger's vintage IS. Read the
    banner block only — a date deeper in the file is data, not a vintage stamp.
    """
    import re
    p = Path(path)
    if not p.exists():
        return None
    pat = re.compile(r"last\s+real\s+data\s+refresh[:\s]+(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
    for ln in p.read_text(encoding="utf-8").split("\n"):
        if not (ln.lstrip().startswith("#") or not ln.strip()):
            break  # left the banner block
        m = pat.search(ln)
        if m:
            return m.group(1)
    return None
