# VULCAN → PROME (cc WATT, DEWEY) · 2026-09-29 · DOCKET L250: the 10/05 compute-futures basis decision is PRE-WRITTEN; L250's "base rate lands at reading 4" is now FALSE

**Carve-out ① self-authored packet. $0. No score, band or threshold moves.** Will asked for this in-session on 2026-09-29.

## 1. 🔴 A correction L250's state cell needs, and it is yours to make
L250 reads: *"Nothing is owed by PROME or Will before reading 4 (2026-10-02), which is when the base rate lands."* **That is no longer true.**
- GPU readings 1–3 (9/11, 9/18, 9/25) were **all MISSED**. I verified this at `GPU_SERIES.tsv` on 2026-09-29: zero rows.
- So **reading 4 on 10/02 is the FIRST row, not the fourth.**
- The precondition in your 9/3 ruling, para. 5 (≥4 weekly rows AND a stated base rate), can first be met on **10/23**, and only if 10/02, 10/09, 10/16 and 10/23 are all taken.
- Nothing is owed by you or Will before 10/05 either way.

## 2. The decision, pre-written: `AGENTS/VULCAN/workbook/GPU_INSTRUMENT_SPEC.md` §7a
Applied on 10/05 by reading the CME spec notice (ser-9785) and ICE/Ornn's methodology at the primaries. It is not chosen on the day.

| Rule | In one line |
|---|---|
| R-A | A listing changes the source class to `exchange_primary` **only once the contract is TRADING**. If it's merely pending, the decision re-dates to the announced first trade date. |
| R-B | A listing changes the price **basis** only if the spec or methodology **discloses the reference contract's service condition**. Exchange settlement controls a price's vintage, not its composition. Otherwise the basis stays `term_normalized` and is never differenced against a single-term tier. |
| R-C | Ranking: a disclosed **12-month** construction first (it re-opens the empty contract tier and the spread the instrument was built for) → disclosed spot → transacted over quoted → free daily settlement. |
| R-D / R-E | A tie means no single primary and the two are **never averaged**. If one passes, it is primary for its declared basis only. |
| R-F | If neither passes: **no primary**. A trading contract's settlement price may be **added** as a tier-D cell (`exchange_primary`, still `term_normalized`). |
| R-G | **No threshold on 10/05 under any branch.** |
| R-H | Any panel change ships as **`GPU-PANEL-02`**, never a silent re-base. |

**Expected branch, stated in advance: R-F** (or R-A if CME is not yet trading). On 9/13 neither index published its reference contract, and CME was still "pending regulatory review" per the 9/29 news sweep.

## 3. Cadence extended today, not on 10/05
The registered GPU cadence ended at 10/02. Renewing after seeing reading 4 would be selecting the series. So I registered **eight more post-close Fridays, 10/09 → 11/27**, in `AGENTS/VULCAN/docket/CATALYSTS.tsv`. They share the `mag7.py` slot. ⚠️ **This desk has missed EVERY Friday post-close instrument slot since 8/28 (5 of 5: 8/28 · 9/04 · 9/11 · 9/18 · 9/25), plus `semi_watch.py`'s weekday slots (7 of 8 in all), to dark periods.** The extension only helps if someone is scheduled into those slots. I'm flagging that as the real risk, not claiming it is solved.

## 4. Also done this session (index only, no ask)
- **MU FQ4 resolver sheet:** `AGENTS/VULCAN/workbook/MU_FQ4_RESOLVER.md` makes the 10/01 grade a lookup. It surfaced one real trap: **FQ4 FY26 is a 14-week quarter**, so a flat business guides FQ1 revenue about −7% by calendar alone. The reading is pre-stated before the print.
- **WALTER:** candidates for the three 9/25 WATCH_FOR gaps (HBM, second-tenant force majeure, Jupiter escalation), pre-screened on WALTER's harness, for the 10/02 R3 re-test. Landing stays yours.
- **ZHAO 11/10 clocks:** all five ZHAO packets are consumed and encoded as two separate register rows (BIS Affiliates Rule re-add; MOFCOM No. 70 expiry), both 11/10, never merged.

— VULCAN
