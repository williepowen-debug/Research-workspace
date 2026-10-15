# BOND -> RED · 2026-10-15 · F2 read, buyback op 2026-10-15 (10Y to 20Y) — OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)

**Signal:** F2 per-op CUSIP concentration for the 2026-10-15 stepped-up long-end op: recent_share **0.33%** vs the >50% on-the-run cut ⇒ **OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)**.
**Op:** 10Y to 20Y · cap $6.0B · offered $40.836B · accepted $6.000B (100.00% of cap) · 3 of 42 eligible · offer-to-cover vs cap 6.81x.
**Metric:** recent_share = accepted par in eligible CUSIPs ORIGINALLY ISSUED ≥ 2023-11-30 (newest quartile of the eligible list by original issue date, TreasuryDirect; ranked by maturity until 2026-09-24) ÷ total accepted, exact Decimal. Companions (descriptive, never a verdict): legacy (coupon ≤2.50%) 93.00% · top-3 100.00%.
**Top accepted CUSIPs:**
| CUSIP | coupon | maturity | par | share |
|---|---|---|---:|---:|
| 912810TC2 | 2.000 | 2041-11-15 | $5,580M | 93.00% |
| 912810TH1 | 3.250 | 2042-05-15 | $400M | 6.67% |
| 912810UL0 | 5.000 | 2045-05-15 | $20M | 0.33% |
**Source:** FiscalData `od/buybacks_operations` + `od/buybacks_security_details`, operation_date=2026-10-15, re-fetched cache-busted at read time (both endpoints; ops row NOT a cached capture — KB-BND-272 lesson).
**Priority:** 🟡 · Instrument: `AGENTS/BOND/monitors/buyback_f2.py --op 2026-10-15` · ledger `AGENTS/BOND/registry/f2_reads.tsv`.
⛔ Cut is BOND-declared (base rate 0/52), not Will-ruled; a fire is a marker, never a YCC-lite verdict.

**Context (BOND, 2026-10-15):** 93.00% went into one 2% coupon Nov-2041 bond (912810TC2) — deep-discount, low-coupon legacy paper, same pattern as the 9/10, 10/1 and 10/8 ops. Detail rows sum to the ops row ($5,580M + $400M + $20M = $6,000M). The op ran into a ~10bp long-end rally (Yahoo ^TNX 5.085 at 13:35 ET); a full fill at 6.81x offer-to-cover says holders were eager sellers of seasoned paper, not that Treasury supported the benchmark. Five in-scope ops, five OFF-THE-RUN.
