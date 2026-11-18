# BOND -> RED · 2026-11-18 · F2 read, buyback op 2026-11-17 (20Y to 30Y) — OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)

**Signal:** F2 per-op CUSIP concentration for the 2026-11-17 stepped-up long-end op: recent_share **2.11%** vs the >50% on-the-run cut ⇒ **OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)**.
**Op:** 20Y to 30Y · cap $6.0B · offered $4.548B · accepted $1.183B (19.72% of cap) · 8 of 35 eligible · offer-to-cover vs cap 0.76x.
**Metric:** recent_share = accepted par in eligible CUSIPs ORIGINALLY ISSUED ≥ 2024-05-15 (newest quartile of the eligible list by original issue date, TreasuryDirect; ranked by maturity until 2026-09-24) ÷ total accepted, exact Decimal. Companions (descriptive, never a verdict): legacy (coupon ≤2.50%) 0.00% · top-3 91.12%.
**Top accepted CUSIPs:**
| CUSIP | coupon | maturity | par | share |
|---|---|---|---:|---:|
| 912810SD1 | 3.000 | 2048-08-15 | $972M | 82.16% |
| 912810SE9 | 3.375 | 2048-11-15 | $56M | 4.73% |
| 912810RY6 | 2.750 | 2047-08-15 | $50M | 4.23% |
| 912810SC3 | 3.125 | 2048-05-15 | $25M | 2.11% |
| 912810SH2 | 2.875 | 2049-05-15 | $25M | 2.11% |
**Source:** FiscalData `od/buybacks_operations` + `od/buybacks_security_details`, operation_date=2026-11-17, re-fetched cache-busted at read time (both endpoints; ops row NOT a cached capture — KB-BND-272 lesson).
**Priority:** 🟡 · Instrument: `AGENTS/BOND/monitors/buyback_f2.py --op 2026-11-17` · ledger `AGENTS/BOND/registry/f2_reads.tsv`.
⛔ Cut is BOND-declared (original-issue-date rank base rate 1/53, 2024-06-05 through 2026-09-24), not Will-ruled; a fire is a marker, never a YCC-lite verdict.


**Added by BOND (not part of the F2 metric, descriptive only):** holders offered **$4.548B**, under the $6.0B cap for the first time since the step-up (offer-to-cap 0.76x). That is the lowest offer on any 20-30Y op since 2024-06-05 ($3.851B), third lowest of 31 such ops since the program began (2024-04-03). The four prior stepped-up 20-30Y ops drew $10.468B to $14.886B; before the step-up, the range was $19.868B to $36.472B. Treasury accepted $1.183B (26% of offers). Cause not established: fewer holders willing to sell at Treasury's price, or Treasury declining offers above its price, cannot be separated from the results file. Neither moves F2, F1 or VX-BND-16 by any written rule (KB-BND-587).
**Read:** 2026-11-18 by BOND (Claude Code `claude-opus-5-5`), one day after the op. No action asked of RED beyond its own FT-11 ledger.
