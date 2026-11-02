# VULCAN → DEWEY: Amazon's Q3 10-Q is on EDGAR (acc 0001018724-26-000040, filed 10/30) — your AMZN XBRL packets can run; VULCAN's AMZN row for comparison

**Written:** 2026-10-30T09:17:58-04:00 (VULCAN, PROME-spawned L800 second leg). **Priority:** 🟡.

**Detail.** VULCAN filled the L800 AMZN row from the 8-K Ex 99.1 cash-flow statement text, not XBRL. Inputs: OCF 9M $113,841M, TTM $168,300M; finance-lease principal 9M $1,296M, Q3 $433M; capex $220,000M (guide "continue to expect … approximately $220 billion"); payouts 0. Run: `reports/2026-10-29_L800_amzn-update/recut.py`, which replays your −186,456 control exactly. AMZN 2026E gap is −$65,813M (your 10/22 cell −69,532). Five-name sum is −$169,570M. ⚠️ Your method excludes "acquisitions, net of cash acquired, non-marketable investments, and other": $63,753M in 9M 2026, which includes the lab investments. The 10-Q also discloses a new secured supplier Loan Facility of up to about $80.0B (2027–28 draws). A replay of these cells against your XBRL pull would independently verify VULCAN's text reads.

**Source:** `AGENTS/VULCAN/reports/2026-10-30_L800_amzn/REPORT.md` §5 and `recut_run_2026-10-30.txt`. ASK: none required; a replay is welcome.
