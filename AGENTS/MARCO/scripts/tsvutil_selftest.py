#!/usr/bin/env python3
"""Standing invariant check for tsvutil against MARCO's real ledgers.

WHY THIS IS A SCRIPT AND NOT A ONE-TIME ASSERTION
--------------------------------------------------
On 2026-08-21 `tsvutil.read_tsv` was repaired from a raw `split("\\t")` to a
csv-aware reader, after a doubling-quote corruption compounded across four
commits of VX.tsv. The repair was verified by asserting the write round-trip
ONCE, by hand, and the lesson was written up as *"assert
read(write(read(x))) == read(x) ONCE."*

Hours later, the SAME module's `read_tsv_numbered` — forty lines below the fixed
function, directly under its warning comment — was still on the raw split. The
one-time assertion could not catch it, because a one-time assertion tests the
reader you were thinking about. Measured at discovery: the two readers disagreed
on 5 of MARCO's 6 ledgers, and the disagreement reached an operator-facing
surface as advice that would have re-created the original corruption.

So the invariant is now a re-runnable check over the real files, wired into boot.
The point is not that these three properties are hard; it is that a SECOND reader
(or a third) must be forced to prove it agrees with the first, every session,
without anyone remembering to think of it.

INVARIANTS
----------
  A. READER AGREEMENT — read_tsv and read_tsv_numbered must return identical
     headers and identical cell content for every ledger. This is the one that
     would have caught the s23 defect on the day it was introduced.
  B. LINE-NUMBER TRUTH — every line number read_tsv_numbered reports must be the
     physical file line that record actually STARTS on. Warnings cite these
     numbers; a re-based number sends the operator to an innocent row, which is
     worse than no warning.
  C. WRITE ROUND-TRIP — read → write_tsv → read must be a fixed point, the banner
     must survive verbatim, and the output must be LF-only. Written to a temp
     file; the real ledgers are never touched.
  D. STORED LINE ENDINGS — the ledger on disk is LF-only. C proves what write_tsv
     emits; D proves what is already there, and they are not the same claim.

USAGE
    python3 scripts/tsvutil_selftest.py              # exit 0 clean, 1 on failure
    python3 scripts/tsvutil_selftest.py --verify-guard
        Re-runs invariant A against a deliberately reintroduced raw-split reader
        and requires it to FAIL. A guard that has never been observed failing is
        not known to be wired to anything (MARCO MEMORY: *test the guard, not
        just the guarded* — version_drift_check v1 passed clean against its own
        founding case).
"""
import sys
import tempfile
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
MARCO_DIR = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from tsvutil import read_tsv, read_tsv_numbered, write_tsv, banner_of  # noqa: E402

# Every TSV ledger MARCO reads programmatically. A new ledger belongs here the
# day it gets a reader — the cost is milliseconds and the failure it prevents is
# silent.
LEDGERS = [
    "thesis/PREDICTIONS.tsv",
    "workbook/VX.tsv",
    "workbook/KB.tsv",
    "workbook/FLOW.tsv",
    "workbook/MIGRATION_PROXIES.tsv",
    "docket/CATALYSTS.tsv",
]


def _raw_split_reader(path):
    """The PRE-FIX read_tsv_numbered, kept ONLY so --verify-guard can prove the
    check fails on it. Never call this for real work."""
    raw = Path(path).read_text(encoding="utf-8").split("\n")
    i = 0
    while i < len(raw) and (not raw[i].strip() or raw[i].lstrip().startswith("#")):
        i += 1
    body = raw[i:]
    if not body:
        return [], []
    header = body[0].split("\t")
    rows = []
    for off, ln in enumerate(body[1:], start=1):
        if not ln.strip():
            continue
        cells = ln.split("\t")
        if not cells or not cells[0].strip():
            continue
        rows.append((i + off + 1, cells))
    return header, rows


def check_agreement(path, numbered_fn=read_tsv_numbered):
    """A — the two readers must see the same file."""
    h1, r1 = read_tsv(path)
    h2, r2 = numbered_fn(path)
    cells2 = [c for _, c in r2]
    fails = []
    if h1 != h2:
        fails.append(f"header differs: read_tsv={len(h1)} cols, numbered={len(h2)} cols")
    if len(r1) != len(cells2):
        fails.append(f"row count differs: read_tsv={len(r1)}, numbered={len(cells2)}")
    for idx, (a, b) in enumerate(zip(r1, cells2)):
        if a != b:
            rid = a[0] if a else "?"
            # Name the LIKELY cause, because "they differ" sends nobody anywhere.
            why = ("escaped-vs-decoded (one reader is not csv-aware)"
                   if any('"' in c for c in a + b) else "field split differs")
            fails.append(f"row {idx} ({rid}) differs — {why}")
            break
    return fails


def check_linenos(path):
    """B — a reported line number must be where that record starts."""
    raw = Path(path).read_text(encoding="utf-8").split("\n")
    _, rows = read_tsv_numbered(path)
    fails = []
    last = 0
    for ln, cells in rows:
        if not (1 <= ln <= len(raw)):
            fails.append(f"line {ln} out of range (file has {len(raw)} lines)")
            continue
        if ln <= last:
            fails.append(f"line {ln} not increasing (previous was {last})")
        last = ln
        first = cells[0]
        physical = raw[ln - 1]
        # A quoted first field starts with '"' in the raw line; an unquoted one
        # starts with its own text.
        if not (physical.startswith(first) or physical.startswith('"')):
            fails.append(f"line {ln} does not start record {first!r} "
                         f"(raw line starts {physical[:30]!r})")
    return fails


def check_stored_lf(path):
    """D — the ledger ON DISK is LF-only.

    Added 2026-08-21 (s23) after `docket/CATALYSTS.tsv` was found still CRLF: the
    8/21 LF-pinning fixed `write_tsv` and normalised VX, and every ledger nobody
    happened to rewrite that day kept its CRLF. Invariant C only proves what
    write_tsv EMITS; it says nothing about what is already stored. The cost is a
    one-row edit producing a whole-file diff in which the real change is invisible
    — which is how the original quote-doubling hid for four commits.

    FROZEN ledgers (workbook/ML.tsv) are deliberately NOT in LEDGERS: rewriting a
    frozen file to fix its line endings is churn against a file nobody parses.
    """
    if b"\r\n" in Path(path).read_bytes():
        return ["stored file is CRLF — a one-row edit will re-terminate every line "
                "and bury the real change; rewrite once via tsvutil.write_tsv"]
    return []


def check_roundtrip(path):
    """C — read → write → read is a fixed point; banner and LF survive."""
    h, r = read_tsv(path)
    b = banner_of(path)
    fails = []
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d) / Path(path).name
        write_tsv(tmp, h, r, b)
        h2, r2 = read_tsv(tmp)
        if h != h2 or r != r2:
            fails.append("round-trip is not a fixed point — write_tsv alters content")
        if banner_of(tmp) != b:
            fails.append("banner not preserved verbatim through write_tsv")
        blob = tmp.read_bytes()
        if b"\r\n" in blob:
            fails.append("write_tsv emitted CRLF (csv.writer default leaked)")
    return fails


def main():
    verify_guard = "--verify-guard" in sys.argv
    print(f"\n{'='*72}")
    print("  MARCO tsvutil Self-Test — reader agreement · line-number truth · round-trip")
    print(f"{'='*72}\n")

    total = 0
    for rel in LEDGERS:
        p = MARCO_DIR / rel
        if not p.exists():
            print(f"  ⚠️  {rel} — MISSING (listed in LEDGERS but not on disk)")
            total += 1
            continue
        fails = (check_agreement(p) + check_linenos(p)
                 + check_roundtrip(p) + check_stored_lf(p))
        if fails:
            total += len(fails)
            print(f"  ❌ {rel}")
            for f in fails:
                print(f"       · {f}")
        else:
            print(f"  ✓ {rel}")

    if verify_guard:
        print("\n  --verify-guard: invariant A against the pre-fix raw-split reader")
        caught = sum(len(check_agreement(MARCO_DIR / rel, _raw_split_reader))
                     for rel in LEDGERS if (MARCO_DIR / rel).exists())
        if caught:
            print(f"       ✓ guard FAILS as required ({caught} disagreement(s) detected)")
        else:
            print("       ❌ guard did NOT fail on a known-bad reader — it is inert")
            total += 1

    print()
    if total:
        print(f"  ❌ {total} invariant failure(s) — tsvutil does not agree with itself.")
        print("     Do NOT hand-edit the ledger. Fix the reader, then re-run.")
        return 1
    print(f"  ✅ clean — {len(LEDGERS)} ledgers, 4 invariants each.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
