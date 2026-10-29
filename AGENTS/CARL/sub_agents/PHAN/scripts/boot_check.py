#!/usr/bin/env python3
"""
PHAN boot check: the mechanical half of DOSSIER.md §8 BOOT step 0. Informational:
it prints what a session must look at, and exits 0 unless it cannot read its inputs.

WHY THIS EXISTS (2026-10-28 file-structure comparison against mature desks)
  1. The boot inbox scan used a RELATIVE `find inbox`. A CARL spawn runs from
     AGENTS/CARL/, so it counted CARL's inbox: 7 packets that night, four of them
     PHAN's own outgoing packets. A plausible wrong number. Every path here is
     anchored to the repo root.
  2. Boot never surfaced due predictions or the docket. Five rows come due 12/31.
  3. Nothing checked whether CARL acted on what PHAN sent. The OWED block said
     "packet sent" and stopped there. (STUE's boot step 2b is the model.)

USAGE (from any directory):  python3 AGENTS/CARL/sub_agents/PHAN/scripts/boot_check.py
"""
import datetime, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from closeout_check import PHAN, ROOT, next_docket_row  # one implementation, shared

TODAY = datetime.date.today()
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def packet_date(p):
    """Authored date: filename prefix first (PHAN/CARL convention), else git add date.
    Never mtime: git sync restamps it (root Data Hygiene)."""
    m = DATE_RE.match(p.name)
    if m:
        return datetime.date.fromisoformat(m.group(1))
    out = subprocess.run(["git", "log", "--diff-filter=A", "--format=%ad", "--date=short", "-1", "--",
                          str(p)], cwd=str(ROOT), capture_output=True, text=True).stdout.strip()
    return datetime.date.fromisoformat(out) if out else None


def window_end(tf):
    """Last day of a free-text window: 'H2 2026', 'Q3-Q4 2026', 'FY2026', 'EOY 2026', '2026'.
    ⚠️ 'FY' is read as the CALENDAR year (right for Klarna/P02). An Affirm-fiscal row (FY ends June)
    must carry an explicit date or quarter in its Timeframe cell."""
    y = re.findall(r"(20\d\d)", tf or "")
    if not y:
        return None
    year = int(y[-1])
    qs = re.findall(r"Q([1-4])", tf)
    if qs:
        q = int(qs[-1])
        return datetime.date(year, 3 * q, 31 if q in (1, 4) else 30)
    if re.search(r"\bH1\b", tf):
        return datetime.date(year, 6, 30)
    return datetime.date(year, 12, 31)


def main():
    print("=" * 78)
    print(f"  PHAN BOOT CHECK · {TODAY} · repo {ROOT}")
    print("=" * 78)

    # 1 · inbox (anchored, lane-descending, README excluded)
    inbox = sorted(p for p in (PHAN / "inbox").rglob("*.md")
                   if "processed" not in p.parts and p.name != "README.md")
    print(f"\n[1] PHAN inbox: {len(inbox)} unprocessed packet(s)  ({(PHAN / 'inbox').relative_to(ROOT)})")
    for p in inbox:
        d = packet_date(p)
        age = (TODAY - d).days if d else None
        flag = "  ⚠️ >30d: TELL THE SENDER FIRST" if age is not None and age > 30 else ""
        print(f"    · {p.relative_to(PHAN)}  ({age if age is not None else '?'}d){flag}")

    # 2 · predictions due
    rows = []
    for l in (PHAN / "workbook/PREDICTIONS.tsv").read_text(encoding="utf-8").splitlines():
        f = l.split("\t")
        if l.startswith("#") or len(f) < 6 or f[0] == "Pred_ID":
            continue
        rows.append(f)
    print(f"\n[2] predictions (ledger of record workbook/PREDICTIONS.tsv; CARL resolves)")
    for f in rows:
        pid, pred, conf, tf, status = f[0], f[2], f[3], f[4], f[5]
        if status != "OPEN":
            print(f"    · {pid:9s} {status:7s} {pred[:44]}")
            continue
        end = window_end(tf)
        left = (end - TODAY).days if end else None
        tag = ("⛔ DUE: route to CARL for resolution" if left is not None and left < 0 else
               "⚠️ due within 60d: write the expectation BEFORE the print" if left is not None and left <= 60 else "")
        print(f"    · {pid:9s} OPEN {conf:>4s}  '{tf}' ends {end} ({left}d)  {pred[:38]}  {tag}")

    # 3 · docket
    nxt = next_docket_row()
    print("\n[3] next PHAN row in CARL docket/CATALYSTS.tsv")
    for r in nxt[:3] or ["NONE: ask CARL for a docket row (CARL owns the docket)"]:
        print(f"    · {r}")

    # 4 · packets PHAN sent: delivered vs consumed
    sent = sorted(list(ROOT.glob("AGENTS/*/inbox/*from-PHAN*.md")) +
                  list(ROOT.glob("AGENTS/*/*/inbox/*from-PHAN*.md")) +
                  list(ROOT.glob("PROME/inbox/*from-PHAN*.md")))
    sent = [p for p in sent if "processed" not in p.parts and "sub_agents/PHAN/" not in p.as_posix()]
    print(f"\n[4] packets PHAN sent that the recipient has NOT filed to processed/: {len(sent)}")
    for p in sent:
        d = packet_date(p)
        print(f"    · {p.relative_to(ROOT)}  ({(TODAY - d).days if d else '?'}d)")
    print("    For every OWED row marked 📤: if its packet is filed, confirm the recipient's files")
    print("    actually carry the change (CARL STATUS / thesis/PREDICTIONS.tsv) before closing the row.")
    print("    Filed is not the same as actioned.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:                    # fail loud: a silent boot check is worse than none
        print(f"⛔ BOOT CHECK ERROR: {type(e).__name__}: {e}")
        sys.exit(2)
