#!/usr/bin/env python3
"""board_log.tsv pre-append SIZE GATE: the only sanctioned way to add disposition rows.

WHY (ML-RED-246 / ML-RED-258, three breaches in three sessions, S44-S46): every breach was
committed by a session that had READ the warning. S44 predicted the breach in writing, S45
breached and wrote the two-state rule, and S46 read the rule and breached anyway. A remembered
ritual is not a control (finding_mechanize_the_cap_not_the_ritual). This script REFUSES an
append that would land the file at or above the READ_CAP rule-5 rotation line, so the breach
cannot happen by appending.

BUDGET  32,550 B (root CLAUDE.md read-cap; board_log is boot-read at 1.5 / 5.5)
REFUSE  post-append size >= 75% (24,412 B): READ_CAP rule 5's rotation START
WARN    post-append size >= 60%: room is running out, rotate at the next closeout
ROTATE  `--rotate` moves the OLDEST data rows VERBATIM to
        archive/board_log_pre-<first kept row's date>.tsv until the live file is < 60%.
        It keeps the comment banner + header. boot.py section 5 reads archive/board_log*.tsv,
        so rotated ids stay counted as dispositioned.

USAGE
  board_log_append.py ROW [ROW ...]        each ROW = 5 tab-separated fields:
                                           timestamp_read  signal_id  disposition  source  notes
  board_log_append.py -                    rows from stdin, one per line
  board_log_append.py --rotate             rotate now (no append)
  board_log_append.py --check              print size/percent, exit 0/1/2 (ok/warn/over)
Exit: 0 appended/ok · 1 warn (appended) · 2 REFUSED / over · 3 malformed row (nothing written)

Field rules (fail closed, nothing is written if ANY row fails): exactly 5 fields; disposition
in {acted, noted, deferred, info-only, skipped}; source in {BOARD, INBOX_WALTER, INBOX_GENERAL};
no field empty except notes. Splits on TAB only; never the csv module (ML-RED-168).
"""
import sys
from pathlib import Path

RED = Path(__file__).resolve().parents[1]
LOG = RED / "board_log.tsv"
BUDGET = 32550
REFUSE_AT = int(BUDGET * 0.75)  # 24,412
WARN_AT = int(BUDGET * 0.60)    # 19,530
DISP = {"acted", "noted", "deferred", "info-only", "skipped"}
SRC = {"BOARD", "INBOX_WALTER", "INBOX_GENERAL"}


def nbytes(text):
    return len(text.encode("utf-8"))


def validate(row):
    f = row.split("\t")
    if len(f) != 5:
        return f"expected 5 tab-separated fields, got {len(f)}"
    if any(not x.strip() for x in f[:4]):
        return "empty field among timestamp_read/signal_id/disposition/source"
    if f[2] not in DISP:
        return f"disposition {f[2]!r} not in {sorted(DISP)}"
    if f[3] not in SRC:
        return f"source {f[3]!r} not in {sorted(SRC)}"
    return None


def split_file(text):
    lines = text.splitlines(keepends=True)
    head = [l for l in lines if l.startswith("#") or l.startswith("timestamp_read")]
    data = [l for l in lines if not (l.startswith("#") or l.startswith("timestamp_read"))]
    return head, data


def rotate():
    text = LOG.read_text(encoding="utf-8")
    head, data = split_file(text)
    moved = []
    while data and nbytes("".join(head + data)) >= WARN_AT:
        moved.append(data.pop(0))
    if not moved:
        print(f"rotate: nothing to do ({nbytes(text):,} B < {WARN_AT:,} B)")
        return 0
    first_kept = data[0].split("\t", 1)[0][:10] if data else "EMPTY"
    arc = RED / "archive" / f"board_log_pre-{first_kept}.tsv"
    banner = (f"# FROZEN - rows rotated VERBATIM from board_log.tsv by scripts/board_log_append.py --rotate; "
              f"read-only history. boot.py section 5 reads this file.\n")
    if arc.exists():  # never overwrite an archive: append below what is there
        with arc.open("a", encoding="utf-8") as fh:
            fh.writelines(moved)
    else:
        arc.write_text(banner + "timestamp_read\tsignal_id\tdisposition\tsource\tnotes\n" + "".join(moved),
                       encoding="utf-8")
    LOG.write_text("".join(head + data), encoding="utf-8")
    after = nbytes("".join(head + data))
    print(f"rotate: moved {len(moved)} row(s) -> {arc.relative_to(RED)}; "
          f"live {after:,} B = {after / BUDGET:.1%}. Commit both paths.")
    return 0


def main(argv):
    if not argv or argv == ["-h"] or argv == ["--help"]:
        print(__doc__)
        return 0
    if argv == ["--rotate"]:
        return rotate()
    cur = LOG.read_text(encoding="utf-8")
    if argv == ["--check"]:
        n = nbytes(cur)
        rc = 2 if n >= REFUSE_AT else 1 if n >= WARN_AT else 0
        print(f"board_log.tsv {n:,} B = {n / BUDGET:.1%} of {BUDGET:,} "
              f"({['OK', 'WARN: rotate at next closeout', 'OVER: run --rotate'][rc]})")
        return rc
    rows = [l.rstrip("\n") for l in sys.stdin] if argv == ["-"] else argv
    rows = [r for r in rows if r.strip()]
    for r in rows:
        err = validate(r)
        if err:
            print(f"MALFORMED, nothing written: {err}\n  row: {r[:120]}")
            return 3
    add = "".join(r + "\n" for r in rows)
    if cur and not cur.endswith("\n"):
        add = "\n" + add
    after = nbytes(cur) + nbytes(add)
    if after >= REFUSE_AT:
        print(f"REFUSED: append would take board_log.tsv to {after:,} B = {after / BUDGET:.1%} "
              f"(>= {REFUSE_AT:,} B, READ_CAP rule-5 rotation line). Nothing written.\n"
              f"  Run: python3 AGENTS/RED/scripts/board_log_append.py --rotate   then re-run this append.")
        return 2
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(add)
    msg = f"appended {len(rows)} row(s); board_log.tsv {after:,} B = {after / BUDGET:.1%}"
    if after >= WARN_AT:
        print(msg + f"  ⚠️ WARN >= 60%: rotate at this closeout (--rotate)")
        return 1
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
