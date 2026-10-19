# WQ459 / L16 — guarded HY credit letter · FROZEN / REGISTERED

**Registered:** 2026-10-19T11:43:36-04:00. **Authority:** `PROME/proposals/2026-10-19_wq459-guarded-hy-RULED.md`, Will's October19 optionA ruling; admitted instrument, section2A and Break±6pp mapping. Ruling/input commit `bbf3cc41a`. Approved source: v2.1 section2A at `c1f2f4321`; operative body below copied exactly (hash in registration record). Section2B is NOT approved. Existing real-rate letter not rewritten. No additional draft review/grid/candidate search.

**Current state:** registration complete; **ANCHOR PENDING** publication/qualification of **2026-10-19**, otherwise the next qualifying observation. L, C₀, numerical UP/DOWN levels and actual anchor date are all PENDING. Latest displayed10/16 values are pre-ruling context, never substitutes. Zero post-anchor cells; no grade/C/VOID consumed; split20/47/33 HELD. The credit-admission rider is satisfied; the test awaits an actual anchor before evaluation. Source/first-read receipts: `2026-10-19_WQ459_registration/SOURCE_RECEIPT.json`, `../analysis/WQ342_grading_log.tsv`.

## Registration calendar — all dates below PROVISIONAL

Assuming10/19 qualifies and weekdays each provide a non-carry observation: cell3 **Thu10/22**, expected publication/read **Fri10/23**; cell15 **Mon11/09**, expected publication/read **Tue11/10**; inclusive anchor+35 **Mon11/23 end ET**. No actual anchor/fire/end/backstop date is certified yet. FRED five pages display next release10/20, not a guarantee of target-cell availability. Next ordinary check10/20(L554), no polling.

**Counts govern dates.** All-five unchanged dates neither count nor break a run; missing HY/CCC is no observation. Auxiliary missing-series handling is frozen below. FRED notes weekend month-end observations:10/31 may qualify; if it is an extra observation and all weekday dates qualify, cell15 would be **Fri11/06**, expected read **Mon11/09**. Carry/missing exclusions may move the end later. If10/19 does not qualify, use the next qualifying date and recompute all dates including+35. Calendar carrier: `2026-10-19_WQ459_registration/CALENDAR.json`; PROME receives wake request.

## Precision, ties and first-read implementation

Published spreads have **1bp precision** (0.01 percentage points); parse decimal percent ×100 exactly into integer bp. Inclusive HY≥L+10 / HY≤L−10 and CCC≤C₀ include exact ties. The existing grid loads `round(float(value)*100)` and compares inclusive integer edges; valid two-decimal source cells map identically. No new grid run or rounding of a finer-precision surprise; unexpected precision is recorded for reconciliation. First-read rows preserve actual read time/source and all five available series. Context rereads below the ruling date are labeled non-operative; anchor/window values will be logged on first actual read. At grade, retrieve both HY/CCC anchors and all window cells again and grade both vintages as the frozen body requires. IG/B mechanism context at the eventual anchor/fire must also be retained for the separate Disc-A tests, never silently made a branch leg.

## Decision caveats — accepted, not cured by approval

Two design steps followed inspection: run5→3 and CCC guard. Three-year history averages few opposing episodes; ex-live regime DOWN94.4%. Refreshed10/19 live UP32.6/DOWN4.7/NV62.8%, ratio7.0, fails symmetry robustness. The original approved draft's29.3/4.9/NV65.9 is its earlier data vintage, not a second present estimate. Guard protects fire day only: both prior live relief fires saw CCC back above anchor within15 observations;92/296 historical guarded DOWN fires did too (31%). No durable-relief claim. **Only10/15 observations leave actionable time** (15−1publicationlag−3run−1trading=10; BASIS-UNNAMED/actionable-life disclosed). ±10bp≈0.38σ of a15-session HY move in the draft; run requirement carries the weight. Shared HY with RED/LIQUID/REGINALD never supplies a second vote; L13 count-once rule below applies. L708 completed but cause unresolved: CARL MIXED, LIQUID/OTTO NO_INSTRUMENT; supplementary equity MIXED is no support/absence proof, CARL n5~99.8% noise rate is not OTTO n2. LIQ07S2 tests only reserve-channel coupling.

## Approved operative text — copied from v2.1 section2A

The calendar examples and L316/C₀1267 counterexamples in this preserved body are **illustrations**, not actual anchors or certified dates; current registration calendar above states the contingent dates. The rule itself is unchanged.

**Instrument:** FRED `BAMLH0A0HYM2` (ICE BofA US High Yield OAS), integer bp; guard series FRED `BAMLH0A3HYC` (CCC & lower OAS). Each cell **as first read by NEXUS**, logged at read in `analysis/WQ342_grading_log.tsv` (created at registration). **A date on which all five ICE series (`BAMLH0A0HYM2` · `BAMLH0A1HYBB` · `BAMLH0A2HYB` · `BAMLH0A3HYC` · `BAMLC0A0CM`) equal their prior cell is not an observation**: it does not count toward the window and does not break a run (if one of the five has no cell that date, the test uses those that do; an observation needs both HY and CCC). A cell not yet published is not an observation.
**Anchor:** L = the HY cell and C₀ = the CCC cell for the **observation date of Will's ruling** (if he rules Mon 10/19: the 10/19 observation, published ~10/20); if that date is not an observation, the next one.
**Window:** the **15 observations after the anchor.** If the anchor is obs 10/19: earliest fire = cell 3 = obs Thu 10/22; cell 15 = obs Mon 11/9. NEXUS packets PROME these two dates and the backstop date for DOCKET wake rows on registration.
**Backstop:** if cell 15 is not published by the end of **the anchor's observation date + 35 calendar days** (inclusive; Mon 11/23 for a 10/19 anchor), grade on the observations published: a branch whose full condition is met fires (for DOWN, a run observation with CCC ≤ C₀); ≥3 observations and no branch met ⇒ C; **fewer than 3 ⇒ VOID** (instrument fault; does not consume C#1; re-anchor only on Will's word). A backstop C re-anchors on the first observation dated after the backstop date.

| Branch | Condition | Consequence on the split (Break · Grind-lasts · Unresolved) |
|---|---|---|
| **UP — broad credit stress** | 3 consecutive observations with HY **≥ L + 10** | **Break +6pp, from Grind-lasts** |
| **DOWN — genuine relief** | 3 consecutive observations with HY **≤ L − 10**, completing on an observation where **CCC ≤ C₀** | **Break −6pp, to Grind-lasts** |
| **C — NO-VERDICT** | neither completes by cell 15 | scores nothing; written EARNED |

**A branch completes when its full condition is met** (for DOWN, including the guard); the first branch to complete wins. No observation can satisfy both HY edges, so UP and DOWN are exclusive; UP / DOWN / C / VOID are exhaustive. A DOWN run that completes with CCC > C₀ does not fire on that observation; it fires on the first later observation that both extends the run (HY ≤ L − 10) and has CCC ≤ C₀. Unresolved-divergence is untouched.

**Counterexamples** (L = 316, C₀ = 1,267; computed by running the rule):
| Case | Observations (HY, CCC) | Grade |
|---|---|---|
| Lower boundary, inclusive | (306, ≤1,267) ×3 | DOWN at cell 3 |
| CCC exactly at C₀ (inclusive) | (306, 1,267) ×3 | DOWN at cell 3 |
| One bp inside the lower edge | 307 ×3, then 316 | C |
| Upper boundary, inclusive | 326 ×3 | UP at cell 3 |
| Mixed: UP run of 2 broken, then a DOWN run | 326, 330, 316, 306, 305, 304 (CCC ≤ C₀) | DOWN at cell 6 |
| Mixed: both edges touched, never three | alternating ~±12 around L | C |
| **K-shape: DOWN run completes with CCC wider, then CCC eases** | (305, 1,280), (304, 1,290), (303, 1,295), (302, 1,270), (301, 1,260), … | **DOWN at cell 5** (the first run cell with CCC ≤ C₀) |
| **K-shape throughout** | HY ≤306 every cell, CCC above 1,267 every cell | **C** |
| n = 0 at the backstop | none | VOID |
| n = 1 at the backstop | 330 | VOID |
| n = 2 at the backstop | 330, 331 | VOID |
| K-shape still blocked at the backstop | (305, 1,300) ×8 published | C |
| Blocked DOWN run, then an UP run | (305, 1,300) ×3, then (326, 1,300) ×3 | UP at cell 6 (the blocked DOWN never completed) |
| Short window at the backstop | 316, 316, 316, 305, 300, 299, 316 (7 obs; CCC ≤ C₀) | DOWN at cell 6 |

**Non-renewable:** C#1 ⇒ exactly one re-anchored window (L₂, C₀₂ = cell 15, or for a backstop C the first observation dated after the backstop); C#2 ⇒ EXHAUSTED, terminal; the split line then reads **"credit leg EXHAUSTED — currently un-falsifiable on credit"**; no third window without Will's word.
**Vintage (mirrors PRED-50 C1):** at every grade, including C, re-pull the anchor and every window cell of both series. If any revision changes the outcome (moves L or C₀, creates or breaks a run, or flips the guard), grade on both vintages; if they differ ⇒ INDETERMINATE-BY-VINTAGE (= C); if they agree, the grade stands.
**Count-once:** with the real-yield letter (L13's re-anchored window 2, running in parallel): same direction with fire observation dates ≤30 calendar days apart ⇒ apply **one** ±6pp (a shared antecedent is presumed unless a registered test separates them); opposite directions ⇒ both apply (net 0), conflict written on the grade. With `RED-FT-02` and every other HY line: one series, one observation — never a second vote anywhere.
**Disc-A — the residual mechanism test, graded separately and never a branch leg; Δ = value at the fire observation − value at the anchor:**
- **UP is TRUE-in-spirit iff ΔIG > 0** (`BAMLC0A0CM`: the stress reached investment grade). ΔIG ≤ 0 ⇒ TRUE-in-letter / FALSE-in-spirit (a high-yield-only move). Base rate: TRUE in 196 of 220 past UP fires, 11 of 12 live.
- **DOWN's mechanism (relief reaching the weakest tier) is a branch leg here**, so its Disc-A residue — ΔB ≤ 0 — is recorded but uninformative (TRUE in all 296 past guarded DOWN fires).
- The letter's consequence applies as written either way; a letter/spirit split is recorded and routed to PROME. The commissioned read (DOCKET L708) informs the Disc-A note, never the branch.
  - *Receipt 2026-10-15 (sourced; changes no letter, number or recommendation):* L708 legs 1–2 of 3 in — H1 consumer attribution: CARL MIXED (a ladder that returns MIXED ~99.8% under noise ⇒ no support, absence uncertified), LIQUID NO_INSTRUMENT; LIQUID: CCC excess over B-beta +66.9bp, 7/7 sessions 10/2→10/13, not the rebalance ⇒ a real dispersion move of unnamed cause (relevant to §2B's Disc-A). OTTO's leg due10/19 at this historical receipt. Record `research/2026-10-15_L708_consumption.md`.
  - *Completion receipt 2026-10-19T11:15:00-04:00:* OTTO a95429b7c formal H1 NO_INSTRUMENT(strictn0: no verified tier/index/daily-data join); conditional two-name equity MIXED is supplementary only. No consumer attribution support or proof of absence; n5 noise-model caveat is not an n2 calibration. All three returns consumed; PROME records L708 closure. No letter/number/recommendation change. Current evidence → `research/2026-10-19_full_synthesis/RECORD.md`§G.

**Grade:** first NEXUS session on/after the fire observation, cell 15, or the backstop is published. Owner NEXUS; no other desk grades it.
