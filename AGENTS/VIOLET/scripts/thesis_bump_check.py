#!/usr/bin/env python3
"""VIOLET thesis-bump check — has the framework fallen behind its own findings?

WHY THIS EXISTS (built 2026-08-04, same evening as the v3.9 bump it would have caught)
--------------------------------------------------------------------------------------
**v3.8's headline claim was "the specification family closes at five fields."
I spent 2026-08-04 writing on STATUS and in the NEXUS brief that
estimator-independence was a SIXTH field.** So my live surfaces asserted the
framework was incomplete while the framework asserted it was closed.

🔑 **Neither surface was stale by any check I run.** Both were fresh, internally
consistent, committed the same day — and contradicting each other. It surfaced
only because Will asked "anything else open?" a second time.

⚠️ **A THESIS BUMP IS THE CLOSEOUT STEP MOST LIKELY TO BE SILENTLY SKIPPED,
BECAUSE NOTHING FIRES WHEN IT IS MISSED.** No ledger ages. No boot check reddens.
No consumer is broken. The framework simply keeps asserting a claim its own agent
has already disproved, indefinitely and quietly. Every other staleness class in
this agent has a detector; this one had none.

WHAT IT MEASURES — and what it deliberately does NOT
-----------------------------------------------------
Counts KB rows dated AFTER the thesis's own version date, split by the signal
each carries. It is **ADVISORY**: a prompt to look, never an instruction to bump.

  · RETRACTIONS (`SUPERSEDED` / `CORRECTED`) weigh most — a retracted finding is
    the single most likely thing to have invalidated a framework claim.
  · RESOLVED findings (`CONFIRMED`) weigh next.
  · `ACTIVE` rows weigh least: an open question is not yet a framework change.

⚠️ **I did NOT try to classify rows by thesis-trigger keywords** ("new
transmission channel", "conviction shift", …). That would be a text-matching
heuristic on prose, and prose-matching is what produced `consumer_check.py`'s
9-of-9 false positives. **Counting by STATUS is exact.** The judgement of whether
those rows amount to a bump stays with the agent, where it belongs.

⚠️ **IT CANNOT DETECT THE 8/4 CASE DIRECTLY.** That was a *semantic contradiction*
between a thesis sentence and a STATUS sentence — no counter can see that. What it
does is make the CONDITION visible ("21 findings since the last bump, 3 of them
retractions"), which is the moment to go and look. **Honest scope: it raises the
question, it does not answer it.**

Exit codes: 0 = within tolerance; 1 = over the review threshold (with --strict).
"""
from __future__ import annotations
import argparse, csv, re, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THESIS = ROOT / "thesis" / "VIX_THESIS.md"
KB = ROOT / "workbook" / "KB.tsv"
# review thresholds — deliberately loose; this is a prompt, not a gate
MAX_FINDINGS = 12
MAX_RETRACTIONS = 3


def thesis_version() -> tuple[str, date] | None:
    if not THESIS.exists():
        return None
    head = THESIS.read_text().split("\n", 1)[0]
    v = re.search(r"v(\d+\.\d+)", head)
    d = re.search(r"(20\d\d-\d\d-\d\d)", head)
    if not (v and d):
        return None
    try:
        return v.group(1), date.fromisoformat(d.group(1))
    except ValueError:
        return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--boot", action="store_true")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()

    tv = thesis_version()
    if tv is None:
        print("  ⚠️  could not parse the thesis version header — expected 'v X.Y … YYYY-MM-DD' on line 1")
        return 0
    ver, vdate = tv

    if not KB.exists():
        return 0
    since, retract, resolved, active = [], [], [], []
    for r in csv.DictReader(KB.open(), delimiter="\t"):
        try:
            rd = date.fromisoformat(r["Date"])
        except (ValueError, KeyError):
            continue
        if rd <= vdate:
            continue
        since.append(r)
        st = r["Status"].strip().upper()
        (retract if st in ("SUPERSEDED", "CORRECTED")
         else resolved if st == "CONFIRMED" else active).append(r["ID"])

    over = len(since) > MAX_FINDINGS or len(retract) > MAX_RETRACTIONS
    icon = "🔴" if over else "✓"
    print(f"  {icon} thesis {ver} ({vdate}) — {len(since)} KB row(s) since: "
          f"{len(retract)} retraction(s), {len(resolved)} resolved, {len(active)} active")
    if retract and not a.boot:
        print(f"     retractions: {', '.join(retract)}")
    if over:
        print(f"     ⚠️  Over review threshold (>{MAX_FINDINGS} findings or >{MAX_RETRACTIONS} retractions).")
        print(f"     ⚠️  ADVISORY — go READ the thesis headline against what those rows now say.")
        print(f"     ⚠️  This counter cannot see a semantic contradiction; it can only tell you when to look.")
        return 1 if a.strict else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
