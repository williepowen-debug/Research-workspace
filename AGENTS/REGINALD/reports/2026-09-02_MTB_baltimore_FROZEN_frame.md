# MTB — Baltimore CRE reassessment + the largest absolute MI3 book in the cohort
## ⚑ FROZEN PRE-REGISTRATION — written 2026-09-02, BEFORE any data is pulled

**Status:** FROZEN. ⛔ **Do not edit the thresholds below after reading data.** Fill the RESULT column only. If a threshold turns out to be badly specified, say so in §6 and grade against it anyway — a frame rewritten after the fact grades nothing. *(Same construction as the 7/18 watch-cards, which scored 4-of-4 and whose value was that the bar was set first.)*

---

## 1. Why this, why now

Two independent things point at MTB and neither was chased:

**(a) An unverified claim, carried 4 months.** `SIG-W-20260426-009` (Will signal, 2026-04-26, Baltimore Sun-sourced): **−$1B / 29% of reassessed CRE in Baltimore.** Never taken to primary. It has sat as an aged ROADMAP row since April.

**(b) My own instruments now say something the claim would fit.** Verified at `workbook/MI3_COHORT.tsv` on 2026-09-02:

| Quarter | MI3 book | v1a % | YoY |
|---|---|---|---|
| 6/30/2025 | $4.28B | 9.17 | **−18.9%** |
| 9/30/2025 | $4.61B | 9.81 | −13.4% |
| 12/31/2025 | $4.54B | 9.33 | −7.1% |
| 3/31/2026 | $5.07B | 10.05 | **+9.6%** |
| 6/30/2026 | **$4.95B** | 9.69 | **+15.7%** |

★ **The trajectory INVERTED monotonically over five quarters — from double-digit contraction to double-digit growth.** And **$4.95B is the largest absolute MI3 book in the cohort by ~1.9×** (next: WAL $2.55B · HBAN $2.21B · CFG $2.14B).

⚠️ **The tension that makes this worth a session:** my rebuilt Convergence Matrix scores **MTB 1** — near-clean on both instrumented channels — while MTB carries the cohort's largest absolute hidden-CRE-class book, growing. **My own 8/13 report flags exactly this as invisible to a ratio screen**, and leaves the question open in writing: *"whether MTB's $4.95B absolute book warrants a Matrix row"* (`reports/2026-08-13_MI3_cohort_rerun.md` §Owed next).

⛔ **A `1` on the matrix means clean on TWO SCORED CHANNELS, never a clean bill of health** — the same caveat already carried for CFG (scores 0 holding ~$44.5B committed PC-NDFI).

---

## 2. What I am NOT claiming going in

- **MI3 growth is not deterioration.** A bigger CRE-purpose-C&I book can be origination, an acquisition, or a reclassification. **The whole point of the mechanism finding is that the BUCKET moves; the ratio alone never says why.**
- **The Sun figure may be wrong, stale, or about a different perimeter** (city vs MSA; assessed value vs loan exposure; a reassessment cycle vs a credit event). **Assessed-value reassessment is a MUNICIPAL TAX event and is NOT a bank charge-off** — conflating them would be the headline error available here.
- MTB is **not** on the watchlist and this frame does **not** propose adding it.

---

## 3. Pre-registered legs (thresholds SET BEFORE DATA)

| # | Test | Source | Threshold set 9/2 | RESULT |
|---|---|---|---|---|
| **L1** | Does the Sun claim reproduce at primary? | Baltimore Sun piece + whatever it cites (city assessment record / SDAT) | **REPRODUCES** = the −$1B and the 29% both trace to a named, dated primary. **PARTIAL** = one half traces. **FAILS** = neither, or the perimeter is not MTB's book | |
| **L2** | Is the object a BANK exposure at all? | The claim's own perimeter | **BANK** = MTB loan/collateral exposure. ⛔ **MUNICIPAL** = assessed-value reassessment → **the claim is TRUE AND IRRELEVANT to my thesis**; say so plainly and stop | |
| **L3** | What drives the MI3 reversal? | FFIEC RC-C item 4 → item 9.a per-quarter; MTB 10-Q (CIK **0000036270**) | **ORIGINATION** = item 4 and 9.a both grow · **MIGRATION** = 9.a grows while 4 falls (the mechanism this desk discovered) · **M&A** = a named acquisition dates the step | |
| **L4** | Does the step-detector fire on MTB? | `scripts/mi3_cohort_screen.py` step_flag column | Already computed — **read it, do not re-derive**; a flagged step is a reporting/classification change, not growth | |
| **L5** | **Does MTB earn a Matrix row?** (the registered open question) | Above + `BANK_EXPOSURE_MATRIX.md` method | **YES** only if L3 = MIGRATION **or** (L1 REPRODUCES **and** L2 = BANK). **NO** if the book grows by origination/M&A with clean credit — *large is not stressed* | |

---

## 4. The discriminator I must not skip

**Every instrument built on 8/20 needed a SECOND instrument to tell two opposite stories apart** (de-risking vs deterioration; cure vs charge-off; disposition vs release). **A level scores a state; only the series says which direction produced it.** Here the second instrument is **L3's item-4 → item-9.a split**: absolute book size alone cannot distinguish a bank originating more CRE-purpose C&I from a bank relabelling existing exposure into it.

⚠️ **MTB's own credit line is the counterweight and it must be quoted, not omitted:** the 6/8 cohort decomposition graded MTB **GENUINE** on NCO (0.34%→0.31%, reserve **build** +$35M) — with one flag: **CRE ACL −31% against loans −10%, "optimistic into the wall."** If L3 comes back ORIGINATION and credit is still clean, **the honest answer is NO ROW**, and I should expect to write that.

---

## 5. Budget and stop rule

**~45-60 min.** ⛔ **Stop at L2 if the object is municipal** — that is a complete answer and the cheapest possible one. ⛔ **Do not weight the Sun figure before L1 returns**; it has been carried unverified for 4 months, which is exactly how an aggregator figure hardens into a "precise" claim.

## 6. Post-hoc notes on the frame itself
*(fill after grading — was any threshold mis-specified, and did a leg go unexercised because another decided first? A conjunctive spec whose decisive leg always fires reads exactly like one that works.)*
