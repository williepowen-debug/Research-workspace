> **Independent read of `monitors/buyback_f2.py`, commissioned by BOND 2026-09-24 ~13:08 ET (Opus subagent, read-only, no repo edits) — the second read owed since 9/17 before the first in-scope F2 packet to RED. Disposition: ⚠️1 (partial publication graded as final) FIXED same day with `complete()` + 5 fixtures, mutation-tested; ⚠️3 (10Y–20Y maturity ≠ vintage) owed BEFORE the 10/1 op; ⚠️2/4/6/7/8 carried to the 10/1 refresh; ⚠️5 (the >50% cut is BOND-declared, not in RED-FT-11) is a RED-letter question, routed with the 9/24 packet.**

# buyback_f2.py review (read-only, 2026-09-24)

Runs: `--selftest` 0 failures; `--pending` rc=0, 9/24 shows ⏳ ANNOUNCED, TODAY. Today's eligible list pulled live and tested: 35 rows = `nbr_issues_eligible` 35, 35 distinct maturities from 2047-02 to 2056-02, cut 2054-02-15, so the recent set is 9 CUSIPs (TX6 through UR7), all 4.125% or higher, issued 2024-26.

**❌ none that would give a wrong verdict today, if the data is complete.** For 20Y-30Y, maturity order matches issue order because every eligible bond was issued as a 30Y.

## ⚠️ Risks, ranked

1. **Partial results get graded as final** (`:170`, `:290`, `:527`). A null `par_amt_accepted` inside a published op becomes 0. The totals cross-check is skipped when the ops row is null (`accepted_ops_row is not None`). That is exactly the state the docstring predicts at 14:15: details first, ops row lagging (KB-BND-272). Test: today's 35 rows with only UR7 = $2B and RV2 = $1B filled, the rest null, ops row null. Result: **66.67%, ON-THE-RUN FIRES**, owed=1, gaps=0, and `--op` would render the packet with rc=0. Fix: require every row non-null and `len(rows) == nbr_issues_eligible`. While the ops row is null, grade PROVISIONAL.
2. **The quartile cut uses whatever rows are present, with no eligibility-count check** (`:173-178`). The code has no `n_elig` vs `nbr_issues_eligible` assert and no `n_acc` vs `nbr_issues_accepted` assert. Test: details list only the accepted rows (4 old + 1 newest, equal par). The cut moves to 2056-02-15 and the result is 20%. The cut is only correct because the feed happens to publish zero-accepted rows (the fixture has 40/40).
3. **Next 10Y-20Y op (10/1): "newest by maturity" is not "newest by issue"** (`:173`). The 9/10 cut is 2045-05-15, and 6 of the 11 "recent" CUSIPs are 2015-16 vintage 30Ys (RM2, RN0, RP5, RQ3 2.5%, RS9 2.5%, RT7 2.25%), sharing maturities with 2025-26 20Ys. Test: the 9/10 fixture with $1B each in RQ3/RS9/RT7 gives **recent 100% → FIRES ON-THE-RUN, legacy 100%**, a contradiction. For the 10Y-20Y bucket, rank by issue vintage (CUSIP series/coupon), not maturity.
4. **Small n** (`:175-176`, banker's `round`). The recent set is 1 distinct maturity for every q from 1 to 5, and 2 for q from 6 to 10. With q=1, any purchase = **100% FIRES**. There is no floor. Ties are included (≥ cut), which is correct.
5. **The letter does not contain the cut.** The RED-FT-11 row defines F2 only as "per-operation CUSIP concentration", ON vs OFF-the-run. There is no 50%, no quartile, no recent_share. The strict `>` (`:188`) is implemented correctly, but it is BOND-declared (admitted at `:60`). v1.1 already activated on 9/10. The verdict string still says "v1.1 ... ACTIVATES", and the letter gives no consequence for a later ON read.
6. **Mis-scope stays silent** (`:156`, `:307-308`). A bucket label variant (e.g. `20Y-30Y`) → ℹ️ OUT OF SCOPE, and the schedule loop `continue`s because the date is in `ops_by`, so no GAP, rc=0. Today's label is `20Y to 30Y`, verified, and every historical label matches. The schedule row should override a feed-row out-of-scope call.
7. **Packet says "re-fetched cache-busted"** (`:358`), but `_get` (`:110-114`) sends no cache-busting param or header.
8. **The selftest does test the math**: 9/10 recent 1.79%, synthetic 75% fires, exactly 50% does not. It does not cover partial-null rows, a null ops row with populated details, q<4, a missing eligible row, or the mixed-vintage 10Y-20Y case. The 1.79% is BOND's own figure; RED verified legacy/top-3/vintage 11.95%, not 1.79%. `:486` reads the live ledger, so it is not hermetic.

## ✅ Verified correct

- Numerator = accepted par in eligible CUSIPs with maturity ≥ cut. Denominator = total accepted par from details. Offered amounts are not used (`:178`, `:184`). Exact Decimal.
- Quartile is computed on the full eligible list for 9/10 and today (rows include zero or null accepted).
- An HTTP 200 with null results is not read as zero purchases. `published()` needs a non-null par (`:163`), so the result is ANNOUNCED, then a GAP once the date is past. A missing `data` key goes to fetch failure (rc=2). An empty `data` today gives 📅 plus a 9/10 GAP (rc=1, not clean).
- All-zero par gives verdict None, not OFF (declared residue).
- Strict `>` at 0.50 (`:188`, and selftest `:478`).
- Scope = LS + Nominal + {10Y-20Y, 20Y-30Y}, normalized. Null field → UNCLASSIFIED GAP. Same-date multi-op → GAP.
- No mode writes the ledger. The only write is the selftest tempdir.
