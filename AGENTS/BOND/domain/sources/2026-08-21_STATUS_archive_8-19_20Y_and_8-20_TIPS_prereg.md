# BOND STATUS — archived: the 8/19 20Y and 8/20 30Y TIPS pre-registration block

**Archived 2026-08-21** by BOND during the Will-tasked STATUS audit.

⚠️ **WHY IT WAS ARCHIVED, and it is a defect worth naming: this block was still titled `★ UPCOMING` on 2026-08-21, with both events in the PAST and BOTH ALREADY GRADED** — the 20Y on 8/19 (`BND-14` resolved FALSE, −2.02pp) and the 30Y TIPS on 8/20 (`BND-17` resolved TRUE, +8.28pp). Its 'Why it matters to BOND' column was written in the future tense and it quoted `DFII10` at **2.41**, a level three sessions stale.

**It is retained verbatim because the FROZEN BARS are the record** — a pre-registration is only evidence if the bars it was frozen against survive unedited. **Figures here are pre-print and must never be cited as current.** Grades live in `KB-BND-136` (20Y) and the `BND-17` row of `thesis/PREDICTIONS.tsv`; benchmarks are re-derivable at any time via `monitors/grade_auction.py --cusip <CUSIP>`.

⚠️ **Note for the checker:** `assertion_check`'s EXPIRED rule did NOT catch this. Its PENDING vocabulary has no token for *'UPCOMING'*, so a section header can advertise a past event as forthcoming indefinitely. Vocabulary extended the same day.

---

## ★ UPCOMING — 8/19 20Y and 8/20 30Y TIPS (dates + instruments VERIFIED at the TreasuryDirect primary, 2026-08-18)

⚠️ **A date and an instrument correction — and a CORRECTION TO MY OWN FIRST VERSION OF IT, made the same session.** WALTER `SIG-W-20260817-005` §4 wrote, inside a *US* long-end signal, *"the 20Y auction is Thursday 2026-08-20 … and PROME has it as a promoted adjudicator."* **I verified the auction date at the TreasuryDirect primary and was right about the US auction — then repeated WALTER's ATTRIBUTION without checking it, and told PROME its row was wrong.** It was not. **PROME's DOCKET 194 is the *JGB* 20Y — Japan, SAM's adjudicator — and Thursday 8/20 is its CORRECT date**, verified by PROME at the MOF primary (`mof.go.jp/…/2608e.htm`). **WALTER fused a true Japan date and a true PROME label onto a US auction that is on 8/19; I caught the date and let the false attribution travel.** *(`finding_fused_true_facts_false_premise` — and `finding_asymmetric_rigor_counterparty_claims` pointing inward: I applied primary-source rigor to the number and none to the claim about another desk.)* **Net: 8/20 carries TWO long-end supply tests in two countries — JGB 20Y (SAM's) and US 30Y TIPS (mine) — and they must be held separately.** US legs verified at `TA_WS/securities/upcoming`:

| Date | Instrument | CUSIP | Size | `tips` | `reopening` | Why it matters to BOND |
|---|---|---|---:|---|---|---|
| **Wed 8/19, 1PM ET** | **20-Year, NEW issue** | `912810UX4` | **$16B** | **No** | No | The first nominal long-end test since the 19-year-high close. **Prices one hour before the FOMC minutes at 2PM** — the T7 resolver. |
| **Thu 8/20, 1PM ET** | **30-Year TIPS, REOPENING** (29Y-6M) | `912810US5` | **$8B** | **Yes** | Yes | **A REAL-MONEY referendum on the real-yield level** with DFII10 at 2.41 — the cleanest read available on whether the term-premium expansion is being validated by real-money duration buyers. |

**20Y trailing-12 benchmark (nominal, n=12, 2025-08-20 → 2026-07-22):** BTC med **2.67**, min 2.36, max 2.86 · indirect med **64.95%**, **min 55.17%**, max 71.57 · dealer med **9.88%**, min 6.21, **max 17.59%**.
⇒ **Composition-failure test for 8/19: indirect <55.17% AND dealer >17.59%.**
> ⚠️ **Spec observation, flagged at authorship rather than at resolution:** the indirect **min** and the dealer **max** come from **the same single auction (2026-02-18: ind 55.17 / dlr 17.59)**. The failure test is therefore calibrated to exactly reproduce one historical print, so it fires only on a repeat of that specific auction or worse. **That is a narrow gate and I am naming it now, not after it fails to fire.** It is the `KB-BND-099` defect class (thresholds whose joint satisfiability is never checked).

**30Y TIPS benchmark — ⚠️ RECONCILED 2026-08-20 PRE-PRINT: the tool returns n=7, not the n=3 this line carried since 8/18.** `grade_auction.py --cusip 912810US5` benchmarks on a **trailing-7 SAME-TENOR SAME-TIPS** window (**2023-02-16 → 2026-02-19, n=7**), % of competitive accepted: **BTC med 2.48** (min 2.38, max 2.78) · **indirect med 76.17%** (min **70.44**, max 78.30) · **dealer med 6.89%** (max **9.87**). *(The 8/18 hand-derived n=3 read BTC med 2.75 / ind med 77.48 / dlr med 4.46 — **different METHOD, not different data**: a 12-month calendar window vs trailing-7 auctions. The tool's n=7 supersedes: it clears the tool's own n≥6 refusal floor, states its method, and is reproducible from one command. Predicting against the hand-derived 77.48 would have been a **1.31pp harder bar chosen by nobody on purpose**.)* ⚠️ **The 8/18 no-composition-gate ruling STANDS and is untouched** — n=7 clears the tool's floor for reporting a *bar*, and BOND is still not wiring a composition **gate** at this tenor. The tool's failure test (**indirect <70.44 AND dealer >9.87**) is reported for grading, not registered as a trigger. **`BND-17` registered pre-print** (45%, indirect ≥ 76.17%) — a **Will-directed CALIBRATION row, nothing rides on it**; see `thesis/PREDICTIONS.tsv`.

