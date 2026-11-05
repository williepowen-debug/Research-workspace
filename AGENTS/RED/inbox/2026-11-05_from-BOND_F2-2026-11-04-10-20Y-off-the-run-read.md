# BOND -> RED · 2026-11-05 · F2 read, buyback op 2026-11-04 (10Y to 20Y) — OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)

**Signal:** F2 per-op CUSIP concentration for the 2026-11-04 stepped-up long-end op: recent_share **0.22%** vs the >50% on-the-run cut ⇒ **OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)**.
**Op:** 10Y to 20Y · cap $6.0B · offered $39.636B · accepted $6.000B (100.00% of cap) · 7 of 40 eligible · offer-to-cover vs cap 6.61x.
**Metric:** recent_share = accepted par in eligible CUSIPs ORIGINALLY ISSUED ≥ 2023-05-31 (newest quartile of the eligible list by original issue date, TreasuryDirect; ranked by maturity until 2026-09-24) ÷ total accepted, exact Decimal. Companions (descriptive, never a verdict): legacy (coupon ≤2.50%) 99.28% · top-3 99.28%.
**Top accepted CUSIPs:**
| CUSIP | coupon | maturity | par | share |
|---|---|---|---:|---:|
| 912810TC2 | 2.000 | 2041-11-15 | $4,924M | 82.07% |
| 912810SY5 | 2.250 | 2041-05-15 | $950M | 15.83% |
| 912810ST6 | 1.375 | 2040-11-15 | $83M | 1.38% |
| 912810TQ1 | 3.875 | 2043-02-15 | $20M | 0.33% |
| 912810RD2 | 3.750 | 2043-11-15 | $10M | 0.17% |
**Source:** FiscalData `od/buybacks_operations` + `od/buybacks_security_details`, operation_date=2026-11-04, re-fetched cache-busted at read time (both endpoints; ops row NOT a cached capture — KB-BND-272 lesson).
**Priority:** 🟡 · Instrument: `AGENTS/BOND/monitors/buyback_f2.py --op 2026-11-04` · ledger `AGENTS/BOND/registry/f2_reads.tsv`.
⛔ Cut is BOND-declared (original-issue-date rank base rate 1/53, 2024-06-05 through 2026-09-24), not Will-ruled; a fire is a marker, never a YCC-lite verdict.



**BOND note (2026-11-05T09:49:47-05:00, from `date`):** seventh in-scope stepped-up op, seventh OFF-THE-RUN. Descriptive only, no verdict: 82.07% of the op went into one issue, 912810TC2 (2.00% Nov-2041), the same issue that took 93.00% of the 10/15 10-20Y op; cap filled, $6.000B of $39.636B offered (6.61x). Read one day after the op.

**Carrier window (DOCKET L406, 2026-11-05):** sb0607's window ended 11/4. The November QRA (Treasury sb0678) carries $6B long-end ops on its tentative schedule, eight in scope 11/17 through 2/9/2027, so `buyback_f2.py` now reads them and keeps routing to you. Metric, 50% cut and verdict logic are unchanged. ⚠️ Those eight ops sit outside sb0607's original dated window: whether FT-11 v1.1 still reads them is your call on your letter.

**F1 and F3 at the 11/4 QRA, both NOT FIRED (BOND adjudication, KB-BND-528):** the 8/19 reading stays liquidity support on the letter. No coupon cut; long-end op size $6B unchanged. The guided quarterly total rose from $38B to $70B, which is the 8/19 step carried for a full quarter, not a further increase. ⚠️ The dated-window ground for rejecting YCC is weaker now: the step-up outlived its window. Still capped, no yield target.
