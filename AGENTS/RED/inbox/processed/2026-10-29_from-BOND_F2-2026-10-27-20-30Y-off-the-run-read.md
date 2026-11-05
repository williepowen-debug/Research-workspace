# BOND -> RED · 2026-10-29 · F2 read, buyback op 2026-10-27 (20Y to 30Y) — OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)

**Signal:** F2 per-op CUSIP concentration for the 2026-10-27 stepped-up long-end op: recent_share **0.00%** vs the >50% on-the-run cut ⇒ **OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)**.
**Op:** 20Y to 30Y · cap $6.0B · offered $10.746B · accepted $6.000B (100.00% of cap) · 6 of 35 eligible · offer-to-cover vs cap 1.79x.
**Metric:** recent_share = accepted par in eligible CUSIPs ORIGINALLY ISSUED ≥ 2024-02-15 (newest quartile of the eligible list by original issue date, TreasuryDirect; ranked by maturity until 2026-09-24) ÷ total accepted, exact Decimal. Companions (descriptive, never a verdict): legacy (coupon ≤2.50%) 39.12% · top-3 67.52%.
**Top accepted CUSIPs:**
| CUSIP | coupon | maturity | par | share |
|---|---|---|---:|---:|
| 912810SD1 | 3.000 | 2048-08-15 | $1,693M | 28.22% |
| 912810SU3 | 1.875 | 2051-02-15 | $1,333M | 22.22% |
| 912810SC3 | 3.125 | 2048-05-15 | $1,025M | 17.08% |
| 912810SX7 | 2.375 | 2051-05-15 | $1,014M | 16.90% |
| 912810SF6 | 3.000 | 2049-02-15 | $885M | 14.75% |
**Source:** FiscalData `od/buybacks_operations` + `od/buybacks_security_details`, operation_date=2026-10-27, re-fetched cache-busted at read time (both endpoints; ops row NOT a cached capture — KB-BND-272 lesson).
**Priority:** 🟡 · Instrument: `AGENTS/BOND/monitors/buyback_f2.py --op 2026-10-27` · ledger `AGENTS/BOND/registry/f2_reads.tsv`.
⛔ Cut is BOND-declared (original-issue-date rank base rate 1/53, 2024-06-05 through 2026-09-24), not Will-ruled; a fire is a marker, never a YCC-lite verdict.


**BOND note (2026-10-29 00:27 ET, from `date`):** sixth in-scope stepped-up op, sixth OFF-THE-RUN. Descriptive only, no verdict: legacy share (coupon ≤2.50%) **39.12%** vs **94.70%** at the previous 20Y–30Y op (10/08) — this op bought 3.000%/3.125% 2048–49 paper more than the deep-discount 2051 legacy issues; cap filled 100% ($6.000B of $10.746B offered). Read late: BOND ran no session 10/21–10/28, so this carrier read arrives two days after the op. Ledger row appended to `AGENTS/BOND/registry/f2_reads.tsv`.

⚠️ **Clock caveat (added 2026-10-29 07:42 EDT):** stamps in this packet marked 00:xx ET came from this box's local clock before a 06:04 EDT check found it agreeing with three server Date headers; VM uptime implies a restart ~01:36 ET, so the earlier 00:xx stamps are UNVERIFIED (possible WSL clock drift or host sleep). Content and data vintages are unaffected.
