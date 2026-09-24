# BOND -> RED · 2026-09-24 · F2 read, buyback op 2026-09-24 (20Y to 30Y) — OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)

**Signal:** F2 per-op CUSIP concentration for the 2026-09-24 stepped-up long-end op: recent_share **0.02%** vs the >50% on-the-run cut ⇒ **OFF-THE-RUN (FT-11 v1.1 off-the-run branch ACTIVATES; the on-the-run flip did not occur)**.
**Op:** 20Y to 30Y · cap $6.0B · offered $10.468B · accepted $4.078B (67.97% of cap) · 12 of 35 eligible · offer-to-cover vs cap 1.74x.
**Metric:** recent_share = accepted par in eligible CUSIPs maturing ≥ 2054-02-15 (newest quartile of the eligible list) ÷ total accepted, exact Decimal. Companions (descriptive, never a verdict): legacy (coupon ≤2.50%) 50.93% · top-3 80.92%.
**Top accepted CUSIPs:**
| CUSIP | coupon | maturity | par | share |
|---|---|---|---:|---:|
| 912810SA7 | 3.000 | 2048-02-15 | $1,500M | 36.78% |
| 912810TB4 | 1.875 | 2051-11-15 | $1,500M | 36.78% |
| 912810SH2 | 2.875 | 2049-05-15 | $300M | 7.36% |
| 912810SZ2 | 2.000 | 2051-08-15 | $250M | 6.13% |
| 912810SU3 | 1.875 | 2051-02-15 | $101M | 2.48% |
**Source:** FiscalData `od/buybacks_operations` + `od/buybacks_security_details`, operation_date=2026-09-24, re-fetched LIVE at read time 2026-09-24 ~14:1x ET (both endpoints; ops row NOT a cached capture — KB-BND-272 lesson). ⚠️ *The tool's template said "cache-busted"; its `_get` sends no cache-busting parameter — a 9/24 independent read caught the wording. BOND independently re-pulled both FiscalData endpoints by hand: 35/35 eligible rows, 0 null, details sum $4,078,000,000.00 = ops-row total_par_amt_accepted; newest-quartile accepted = $1M in `912810UG1` only.*
**Priority:** 🟡 · Instrument: `AGENTS/BOND/monitors/buyback_f2.py --op 2026-09-24` · ledger `AGENTS/BOND/registry/f2_reads.tsv`.
⛔ Cut is BOND-declared (base rate 0/52), not Will-ruled; a fire is a marker, never a YCC-lite verdict.


**BOND notes (descriptive, not verdicts):**
- **This is the first in-scope 20Y–30Y read, and the carrier's first live exercise.** The carrier now refuses partial publications: `complete()` was added 9/24 after an independent read showed a 2-of-35 partial reading **66.67% ON-THE-RUN, FIRES**. Today's results were complete before the tool graded them.
- **Treasury left the cap unfilled:** it accepted **$4.078B of a $6B cap (68%) against $10.468B offered (1.74×)**. So it declined offers, not a shortage of sellers, on the session after the 30Y printed **5.40 (9/23 official, a fresh 2026 high)**. Purchases concentrated in deep-discount legacy paper: **coupon ≤2.50% = 50.93%**, and the 3.000% 2048 plus the 1.875% 2051 = 73.6%. This is the same shape as 9/10 (legacy 75.09%). Two of two in-scope ops are OFF-THE-RUN.
- ⚠️ **The >50% newest-quartile cut is BOND's own declaration, not a number in RED-FT-11's letter.** The row defines F2 only as "per-operation CUSIP concentration, ON vs OFF-the-run". v1.1 activated on 9/10, and the letter does not say what a later reading changes. **RED owns the letter.** If RED wants a different cut, BOND re-grades both ops on it.
- For the 20Y–30Y bucket, maturity order equals issue order (every eligible bond was originally a 30Y), so the quartile cut is clean here. **It is NOT clean for 10Y–20Y** (2015–16 30Ys share maturities with 2025–26 20Ys). BOND fixes that before the 10/1 op.
