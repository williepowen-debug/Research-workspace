# SAM Predictions — Calibration Archive

Full post-mortems for **closed** predictions (FAILED + resolved-special). Reference-only — NOT loaded at boot. The live record (date, confidence, outcome, one-line lesson) stays in [`PREDICTIONS.tsv`](PREDICTIONS.tsv); the one-line calibration warnings live in that file's scoreboard preamble. This file holds the blow-by-blow that used to bloat the per-row `Notes`.

Created 2026-05-29 (boot-slimming target (b)). Each section = one Pred_ID; text is the verbatim post-mortem moved from PREDICTIONS.tsv.

---

## SAM-08

**April BOJ hike to 1.00% if Shunto strong** | made 2026-02-15 | conf 85%→90% | Apr 2026 | FAILED 2026-04-28 | FALSE

Shunto condition met (5.26% Rengo) but BOJ held 0.75% at Apr 28 meeting. 3 dissents for 1.00% (biggest split since 2016) but no actual hike. Same outcome as SAM-20 (which was the more direct April hike prediction at 60%); SAM-08 was the earlier Feb 15 conditional version at 85→90%. Calibration miss: high-confidence (90%) prediction failed. Lesson: Takaichi political ceiling overrode strong macro data — the conditional ("if Shunto strong → hike") missed that the 0.75% line was more binding than the data case. Same lesson as SAM-20.

---

## SAM-14

**At least one Big 4 insurer announces UST reduction** | made 2026-02-15 | conf 60% | H1 2026 | FAILED 2026-05-27 | FALSE

**RESOLVED FALSE.** Big 3 mutual ESR window (Nippon + Meiji Yasuda + Sumitomo all May 26) confirmed 3-of-3 that the response to ESR pressure is FOREIGN ALLOCATION GROWING + M&A INTO US, not foreign cuts. Sumitomo: total foreign securities +¥1.11T (+9.3% to 35.5% of GA); foreign bonds +¥543B (+6.2%); Symetra in-force +23.7% via Dearborn Life partial acquisition. Nippon: Resolution Life $10.6B M&A direction INTO US; foreign book +¥3.99T unrealized gain (+¥909B YoY). Meiji: Stancorp/Allstate INTO US; foreign book +¥709B gain. Dai-ichi May 13: ~220% resilient with no foreign reduction language. **Big 4 → 4-of-4 confirmed pattern is opposite of prediction.** Lesson: ESR pressure does not force UST/foreign-bond sale at multi-year amplitude — capital actions + equity rally + hedge-cost relief absorb it. Calibration: 60% confidence on TRUE was a significant miss — overweighted v1.0 thesis mechanism without prob-weighting M&A capital-action alternative. Same lesson cluster as SAM-19, SAM-25.

---

## SAM-15

**Oil-in-yen forces repatriation regardless of rate differential** | made 2026-03-20 | conf 80% | Q2-Q3 2026 | FAILED 2026-05-29 | FALSE (mechanism falsified)

**RESOLVED FALSE — mechanism falsified on all four embedded claims, not merely unfired.** Original premise: Dubai $166 (+140% YTD), 6-month infrastructure lag, trade deficit forces asset liquidation to fund imports = structural carry-unwind driver independent of BOJ policy. (1) **Oil-spike premise evaporated** — Brent collapsed ~$108→$92 on the Iran/Hormuz MOU; 80% conf failed to prob-weight oil mean-reversion on a war-driven premise. (2) **Core mechanism INVERTED** — April TB (May 21) printed ¥+301.9B SURPLUS because blockade severity collapsed import VOLUMES (crude -64% YoY); supply destruction = smaller deficit, so the widening-deficit precondition never materialized even at peak oil stress (v1.4 OIL-IN-YEN finding). (3) **"Independent of rate differential" falsified** — yen weakened May 12-21 DESPITE the surplus, driven by rate differential + fiscal supply + lifer absence; the trade channel was both small and inverting. (4) **Forced repatriation NOT visible** — Big 3 ESR 3-of-3 showed insurers GROWING foreign books (Sumitomo +¥1.11T) + M&A INTO US, not liquidating (SAM-19/14/25 direction-error cluster). Distinct from SAM-25 (true-in-letter/false-in-spirit): here neither letter nor spirit holds. NEW lessons: (a) **premise-dependence** — high conf on a prediction resting on a transient geopolitical shock inherits that shock's reversal risk; (b) **standalone-channel overreach** — don't claim a NEW channel "independent of rate differential" without isolating its magnitude. Carry unwind, if it fires later via June BOJ or Fed cuts, is a DIFFERENT mechanism — not vindication. (Q3 window technically still open, but premise + mechanism both broken → resolved now per flag "do NOT leave parked at 80%.")

---

## SAM-17

**Feb TIC shows Japan net UST selling > $10B** | made 2026-04-13 | conf 65% | Apr 15 | FAILED 2026-04-15 | FALSE

Japan UST holdings ROSE to $1,239.3B in Feb (from $1,185.5B Dec) — stock +$53.8B Dec→Feb. Directionally opposite. Miss driven by conflating MOF ITS weekly outflows (Japan-resident trading, sector-specific) with TIC aggregate holdings (all Japanese holders, includes banks, retail Toshin, retained coupons, price effects). Lesson: use flow series (ITS) for flow predictions, not stock series (TIC).

---

## SAM-18

**MOF ITS Apr 5-11 week LT-debt net selling > ¥1.5T** | made 2026-04-13 | conf 55% | Apr 16 | FAILED 2026-04-16 | FALSE

Actual: +¥698B NET BUYING. Mar 29-Apr 4 ¥-2.46T confirmed as FY-end seasonal spike, not regime change. 4-week rolling dropped from ¥-5.0T (stress) to ¥-2.74T (base case pace). Apr 16 release was DECISIVE AGAINST rebalancing to Option C. Calibration: 55% was appropriate for 50/50 seasonal-vs-regime call.

---

## SAM-19

**At least 2 of first 5 insurer FY2026 plans announce foreign bond cuts** | made 2026-04-13 | conf 75% | Apr 14-25 | FAILED 2026-04-24 | FALSE

Zero of first 5 plans announced clean foreign bond CUTS. Nippon Life (Apr 22): paring YEN bonds, foreign direction ambiguous. Meiji Yasuda: INCREASING hedged foreign credit for ALM. Dai-ichi: no formal Apr announcement; prior stance doubled overseas strategic investment. Sumitomo: PC expansion + outsourcing to Symetra (restructuring, not cut). Fukoku: stopped super-long JGBs (domestic, not foreign). Miss driven by (1) conflating JGB avoidance with foreign bond cuts in the setup, (2) model oversimplification — insurers are rotating unhedged → hedged foreign, not net-cutting. Thesis nuance logged in MEMORY (candidate for v1.4 refinement).

---

## SAM-20

**BOJ hikes to 1.00% at April 28 meeting** | made 2026-04-13 | conf 60% | Apr 28 | FAILED 2026-04-28 | FALSE

Held 0.75% — but with 3 dissents (Takata, Tamura, Nakagawa) for 1.00%, biggest split since 2016 + first under Ueda. GDP forecast cut 1.0%→0.5%, inflation forecast upgraded, Ueda hawkish presser. Swap markets repriced June to 74%. Calibration: 60% confidence on TRUE was significant miss — overweighted hawkish signals (Takata dissent, Shunto, wages) vs dovish political cover (oil uncertainty, Takaichi mortgage line, ME-caution language Apr 13). Lesson: when political ceiling is explicit (Takaichi 0.75% line) and external uncertainty is high (oil/war), the BOJ defers to consensus optics even when data supports action. Hawkish dissents are how the board telegraphs intent without breaking that consensus. SAM-21 (June @70%) tracking BULL on the dissent split.

---

## SAM-22

**CFTC JPY net short does NOT cover below -75K contracts before next hike** | made 2026-04-24 | conf 65% | Through Jun BOJ | FAILED 2026-05-08 | FALSE

Net short -102,059 (Apr 28) → -61,738 (May 5). Crossed above -75K by 13,262 contracts. Cover driven by MOF intervention Apr 30 + May 6 (¥10T, $63.5B combined — largest since 2022) + Bessent-Katayama affirmation May 11-12. The hedged scenario fired (mass covering event = intervention deterrent). Lesson: when MOF intervention trigger is near (USDJPY 160 zone), CFTC short cover risk is much higher than 35% — the same level that triggers intervention also triggers speculator covering. Should have prob-weighted intervention scenarios into SAM-22 directly. Thesis-wise: half the unwind fuel is now burned through intervention itself; June BOJ hike still primary but less violent.

---

## SAM-25

**At least 1 of 3 Big 3 mutual lifers (Nippon, Meiji Yasuda, Sumitomo) prints FY2025 ESR below 200%** | made 2026-05-21 | conf 40% | May 25-29 | RESOLVED — TRUE-IN-LETTER / FALSE-IN-SPIRIT 2026-05-26 | TRUE (literal) / FALSE (mechanism)

Nippon Life printed 195% (vs 222% prior, -27pt) — BELOW 200% threshold. Literal resolution: TRUE. Calibration: 40% was well-calibrated for the literal threshold. **However**, decomposition (gaiyo PDF p.7) shows -28pt driver is Resolution Life $10.6B M&A full-subsidiarization, NOT market stress (economic environment only -4pt; new business + sub-debt +5pt). Foreign securities unrealized GAIN +¥3.99T (+¥909B YoY) — book profitable and growing. Tape priced as capital action (USDJPY 158.95 → 159.24, yen WEAKER post-print). The intent behind SAM-25 ("forced repatriation visible") did NOT fire — this is the threshold-vs-mechanism trap logged in MEMORY 2026-05-25. Meiji Yasuda 208% (manageable band; +¥709B foreign gain). **Sumitomo May 26 EXTENDS the pattern (logged May 27): ESR ↑+19pt to 197% with foreign book GROWING +¥1.11T (+9.3%) — the OPPOSITE direction of forced repatriation. 3-of-3 Big 3 confirm v1.5 Channel 1 demotion.** Lesson: ESR-threshold predictions need explicit mechanism qualifier ("via market stress, not capital action") AND need to prob-weight M&A / capital-action absorption pathway — the threshold-vs-mechanism trap is now the dominant calibration warning for any balance-sheet threshold prediction (auto-memory [[finding_threshold_vs_mechanism]]).

---

## SAM-32

**Japanese life insurers (Big-3 mutuals + Dai-ichi) do NOT return to SUSTAINED net buying of super-long (30Y/40Y) JGBs through Dec 31 2026** | made 2026-06-30 | conf 72% | Through Dec 31 2026 | FAILED 2026-07-02 | FALSE

**Fastest falsification on record — 48 hours from opening to resolution.** The pre-registered bright line (RED CH-015, written 2026-06-30) had two legs: (1) realized flow ≥¥300B/mo net super-long buying × 2 consecutive months, OR (2) "a lifer H2-FY2026 plan explicitly announces a super-long re-build." Leg 2 fired 2026-07-01: **Meiji Yasuda (Big-3 mutual, a named entity in the prediction) doubled its FY2026 super-long JGB purchase plan to >¥2T (~$12.3B)**, with its asset-management head calling ~4% 30Y yields a **"perfect buying opportunity"** — funded partly by selling low-yield legacy JGBs (crystallizing losses to roll up book yield). Verified on two independent outlets before propagation (Nikkei Asia Jul-1 06:32 JST; Bloomberg Jun-30 headline: "Meiji Yasuda Doubles 2026 Super-Long Government Bond Buying Plan").

**Resolution judgment (letter question, resolved without wiggle):** the falsifier's leg-2 wording said "H2-FY2026 plan" — the anticipated *vehicle* (Oct-Nov plan season). The actual event was a mid-year FY2026 plan REVISION announced Jul 1. Test applied: if the identical content had arrived in the October H2 announcement, SAM would resolve FALSE without hesitation; arriving 3 months EARLY makes the evidence stronger, not weaker. Treating it as unfired would be true-in-letter/false-in-spirit gaming in reverse (the SAM-25 lesson). Resolved FALSE.

**What was wrong (three layers):**
1. **Flow-direction misread (SAM-17/18/19 family):** the thesis's key demand-leg evidence — lifers net-SOLD ~¥201B of super-long in May 2026 — was very likely the **SELL-LEG of a yield roll-up rotation** (sell low-coupon legacy, realize losses, buy new paper at ~4%), not abandonment. Dai-ichi had stated exactly this intent in Jul-2025 ("selling has dominated… we want to increase buying going forward"); Nippon signaled shift-to-longer-duration intent by Apr-2026. Gross/net selling prints and duration re-build intent COEXIST in a rotation. Reading the flow's sign without reading the *program* behind it was the error.
2. **"No re-entry yield near current / re-entry = 2-3yr rollover process" falsified:** the re-entry level had a name — ~4.0% 30Y — and the re-entry vehicle was a mid-year plan revision, not a multi-year rollover cycle.
3. **RED CH-010 resolved its first live data point toward RED:** the economic-value J-ICS read (higher yields → duration-gap-closing BUYING, solvency-improving) beat SAM's asset-markdown/forced-seller read at the 4.0% level. The contested 4.5% "forced-selling reflexive zone" is now doubly suspect — a lifer just called 4% a buying opportunity 50bp below it.

**What survives:** the demand-REDUCTION observation (Fukoku/Asahi pivoted out of 30/40Y; foreigners first net-sell in 16 months; MOF had to cut FY2026 super-long gross issuance to a 17-yr low — the vacuum was real enough that supply adjusted). What died is the ONE-WAY framing: the vacuum is buffer-AND-yield-conditional, with the first named demand floor at ~4%.

**Post-mortem texture (does not reopen the resolution):** announcement ≠ realized flow — the roll-up funding means net super-long flow could still print small; Jul-7 30Y and Jul-22 40Y auctions + MoF/lifer monthly flows will show whether the announced bid is real. If flow never materializes, the lesson is bright-line construction (single-lifer plan-leg was hair-triggered), logged here, not a re-litigation. Bright-line design worked as intended in one respect: it forced a same-week, documented resolution instead of a slow drift.

**Calibration:** 72% failing in 48h is a bad miss on its face; mitigation is that the falsifier was SAM's own pre-registered design (with RED), caught immediately, and resolved honestly. The failure joins pattern (2) — flow-data interpretation — with a new sub-clause: **rotation sell-leg vs abandonment.**
