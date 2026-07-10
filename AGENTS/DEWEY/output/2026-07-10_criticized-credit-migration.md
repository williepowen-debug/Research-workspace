# Criticized-credit migration — FFIEC tier pull + leading-bucket→NCO conversion base rates
**Date:** 2026-07-10 | **Mode:** Thesis | **Confidence:** _[TBD]_
**Flag:** REQ-DEWEY-20260702-009 (Batch-2 #13) | **Feeds:** REGINALD (V1 falsifier un-blind; REG-24/25), RED (CHG-RED-040; WAL/OZK beat/miss tree), CORAL/OZK/TERRY (info)

> ⛔ **IN-PROGRESS / BLOCKED (2026-07-10 ~mid-day ET) — session rate limit hit (resets 2:10pm ET).** Leg 2 (base rates) recovered from 13 verified fan-out claims + DEWEY synthesis (below). **Leg 1 (Q1-2026 bank data pull) FAILED mid-run — NOT yet done; this is the load-bearing un-blind of REGINALD's V1 falsifier. Report is NOT deliverable until leg 1 re-runs after the reset.** Recovery plan: (a) resume fan-out `wf_5c06f468-d60` (resumeFromRunId — 73 agents cached, only the failed verify votes + synthesize re-run) to firm the GFC/2023 texture; (b) re-spawn the leg-1 bank-data primary pull. Then finalize + closeout.
> **DRAFT — filling as the /deep-research base-rate fan-out + DEWEY FFIEC/10-Q primary pull return. Not yet delivered.**
> **Freshness re-anchor (docket):** WAL & OZK Q2 prints are **7/21 AMC** (not the prompt's "~7/16") — single-day triple w/ ALLY. OZK's Seattle U-District deed-in-lieu (recorded wk-7/2) is a **Q3 subsequent event** → the 7/21 Q2 print shows the *specific-reserve build* vs REGINALD's pre-registered **$15-30M fail-band** ($20M mid already in the $628.5M ACL). This run grades **Q1 state + base rates** so the 7/21 Q2 prints can be graded live.

## Key Finding
_[1–2 sentences — does the leading criticized creep confirm the bear's early edge (CHG-RED-040) or revert? how much confidence should REG-24/25's Q2 build-vs-revert grading carry?]_

---

## Required sub-answers (completeness-critic checklist)

| # | Sub-question | Status | Where |
|---|---|---|---|
| 1 | **FFIEC/10-Q data pull** — Q1-2026 special-mention / classified / 30-89d CRE buckets + QoQ vs Q4-25 for WAL/OZK/EGBN/BKU/SBCF | ☐ (DEWEY primary) | §(1) |
| 1b | **WAL reconciliation** — confirm/correct 10-Q Special Mention $403M / Classified $947M; un-blind the MI3 line | ☐ (DEWEY primary) | §(1) |
| 2 | **Base rate** — how often does a ≥20-25% QoQ special-mention/criticized/30-89d surge CONVERT to NCOs within 1-2Q vs REVERT? (GFC / 2015-16 energy / 2023) | ☐ (fan-out core) | §(2) |
| 2b | **Discriminating features** — bucket breadth, single-vs-multi-credit, reserve build, appraisal timing, quarter-end lumpiness, office share | ☐ (fan-out) | §(2) |

**Decision outputs owed:** adjudicate CHG-RED-040 (RED vs REGINALD/CORAL); re-grade REG-24 (70%) / REG-25 (75%); pre-position RED's WAL/OZK beat/miss tree (beat-clean cuts RED 69→62); un-blind REGINALD's V1 Bear-fast falsifier (dark 5+ wks).

---

## Evidence

### (1) Q1-2026 criticized-credit data pull (WAL/OZK/EGBN/BKU/SBCF)  *(DEWEY primary)*
⛔ **BLOCKED — primary-pull agent died on the session rate limit mid-run (last: mid-SBCF, no structured result returned).** The load-bearing leg (un-blinds REGINALD's V1 falsifier) is **NOT done**. Targets to recover on re-run: for each of WAL/OZK/EGBN/BKU/SBCF — special-mention $, classified/criticized $, 30-89d CRE, ACL + QoQ build, all QoQ vs Q4-25; **WAL reconciliation vs 10-Q Special Mention $403M / Classified $947M + the MI3 line.** _[Re-spawn after 2:10pm ET reset.]_

### (2) Conversion-vs-reversion base rates + discriminating features  *(DEWEY synthesis of 13 verified fan-out claims; workflow synth step was rate-limited — GFC/2023 texture thinner pending resume)*
**Base rate — a one-quarter criticized/past-due surge converts to NCOs SLOWLY, LAGGED, and often INCOMPLETELY in the near term; near-term reversion in the *reported* number is common and NOT reassuring on its own:**
- **2023 (closest analog):** CRE past-due-and-nonaccrual (PDNA) surged **+72% ($16.7B→$28.7B)** in a year, PDNA rate 0.77%→**1.28%** (highest since Q3-2015) — yet contemporaneous aggregate CRE **NCOs stayed <$1B**: a large past-due migration that had NOT (yet) converted to losses [PRIMARY: OFR Brief 24-04].
- **GFC (severity precedent):** CRE **NCOs LAG PDNA**; full loss severity took *several years*, cumulating **$93B (7.3% cumulative net CO rate)** — conversion happens, but over years, not quarters [PRIMARY: OFR].
- **Post-pandemic CRE:** valuation deterioration (from 2022:Q1) → only a small NPL-ratio rise with a **~2-year lag**, NCOs similarly lagged [PRIMARY: NY Fed SR1130].
- **2015-16 energy (a surge that DID partly convert but stayed contained):** classified O&G **0.7%→15.2% (~$24B)**, special-mention ~$15B; NPL **+50%** vs peer banks; OCC judged it real ("requires further provisioning") — BUT it stayed **sector-boxed** (no broad CRE spillover, no widespread failures) [PRIMARY: OCC SRP Spring-2016, NY Fed Liberty St, Dallas Fed].

**Discriminating features — real build vs quarter-end noise:**
1. **Slow multi-quarter grind = real; one-quarter lumpy spike = suspect.** Current CRE cycle PDNA ratio 1.08%→**1.42% over NINE consecutive quarters** [PRIMARY: FDIC 2025 Risk Review] — a steady build reads real; a single-quarter jump is more likely appraisal-timing/quarter-end.
2. **Migration DEEPER into classified while special-mention FALLS = real progression, not curing.** 2024→25 SNC Real-Estate&Construction classified rose **$28.2B→$32.5B** even as special-mention fell $17.5B→$13.5B [PRIMARY: OCC SNC 2025].
3. **⚠️ Capital-driven loss-deferral (extend-and-pretend) — the key trap:** less-capitalized banks are **SLOWER to classify** distressed CRE as nonperforming and show *fewer* defaults → a **LOW / reverting NPL reading can MASK deterioration, not signal health**. For $10-100B CRE-concentrated regionals specifically, tighter capital ↔ **SMALLER** NPL ratios (inverse) [PRIMARY: NY Fed SR1130]. **Directly relevant to WAL/OZK — a benign print at a capital-constrained regional is not self-evidently reassuring.**
4. **Reserve/ACL build alongside migration** = management treating it as real (the OCC 2015-16 "further provisioning" tell).
5. **Breadth vs concentration:** the energy episode stayed contained *because* it was sector-boxed; breadth across buckets/geographies is what turns an idiosyncratic surge systemic.

**Implication for the WAL/OZK Q2 (7/21) read (feeds RED beat/miss tree + REG-24/25):** the base rate says a one-quarter criticized surge is **more often a slow-grind leading indicator than a near-term NCO event** (NCOs lag PDNA by quarters-to-years). So **a clean Q2 NCO beat does NOT falsify the bear** — it's too early for conversion; RED's "beat-clean cuts 69→62" should be conditioned on WHICH metric beats (an NCO beat is nearly-mechanical given the lag; a *criticized/special-mention* build is the real leading tell). Tempers REG-24/25: the leading creep is signal-consistent, but conversion is slow — and at capital-constrained names a benign classified print may be deferral, not health (feature #3). *(GFC + 2023 single-name texture to firm on fan-out resume.)*

---

## Counter-Evidence
_[what argues the creep reverts (noise/lumpiness) vs converts]_

## Source Quality Assessment
_[reliability; gaps]_

## References
_[full URLs, dated]_

## Process Report
**Searches run:** _[fill]_
**Data gaps:** _[fill]_
**Source frustrations:** _[fill — expect FFIEC CDR registration wall; SEC 403 on generic fetch (UA workaround)]_
**Confidence in findings:** _[fill]_
**If I had more time/tools:** _[fill]_
**Suggestions:** _[fill]_
