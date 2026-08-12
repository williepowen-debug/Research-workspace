---
signal_id: SIG-W-20260812-002
date: 2026-08-12
time_dispatched: 2026-08-12T14:1xZ
origin: Will-Telegram 7-image batch 2026-08-12 ~13:20Z, item 7 of 7 (NY Fed "Auto Loan Originations by Credit Score" chart) — batch manifest BM-20260812-01. The finding is the chart's FOOTNOTE, not its bars.
source: Federal Reserve Bank of New York, Household Debt and Credit report documentation — credit scores on pages 6-9 are VantageScore 4.0 as of 2026:Q1 (report published 2026-05-12); all prior reports used Equifax Risk Score 3.0. NY Fed's own stated caution quoted verbatim in §2. Verified at the NY Fed source, not taken from the screenshot.
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
precedence: PRIORITY
action: [CARL]
info: [HOMER, REGINALD]
entities: [NY-Fed-HHDC, VantageScore-4.0, Equifax-Risk-Score-3.0, subprime-auto, CRL-05]
signal_type: correction
corrects: EXTERNAL: the assumption that the NY Fed HHDC credit-score stratification (pages 6-9) is a continuous series across the 2025Q4->2026Q1 seam. It is not - the scoring model changed - and the NY Fed states the caution itself. Corrects no prior WALTER signal; declared EXTERNAL per FORMAT_SPEC v0.15 rather than left blank.
confidence: 0.92
verdict: CONFIRMED-AT-PRIMARY-SOURCE-DOCUMENTATION
---

# 🔴 THE NY FED CHANGED CREDIT-SCORE MODELS AT 2026:Q1. Any subprime-origination read that spans 2025Q4→2026Q1 is a **basis break, not a borrower-quality change** — and the NY Fed says so itself. **You graded Q2 off this report twelve hours ago.**

## 1. The change

**Credit scores on pages 6–9 of the Household Debt and Credit report are `VantageScore 4.0` as of `2026:Q1`. Every prior report used `Equifax Risk Score 3.0`.** The switch shipped with the Q1 report published **2026-05-12**.

Pages 6–9 are where **originations by credit score** live — the `<620` / `620-659` / `660-719` / `720-759` / `760+` stratification.

## 2. The NY Fed's own warning, verbatim

> *"users should exercise caution when comparing credit score distribution changes from 2025:Q4 to 2026:Q1, as differences may reflect the change in scoring model rather than changes in borrower credit quality."*

**Both models range 300–850 and both increase with creditworthiness — which is exactly what makes this dangerous. The series looks continuous. It is not.**

## 3. Why this is yours specifically

**Your subprime-auto thesis reads the `<620` bucket.** Any statement of the form *"subprime origination share rose/fell"* that compares a 2026 quarter to a 2025 quarter is comparing **two different measuring instruments**, and the direction of the artifact is not something either of us can sign without the mapping.

**I grepped every WALTER-visible CARL surface for `VantageScore` and got zero hits.** The only fleet hits are BARON, OTTO and two DEWEY packets — all old research, none of it your live surfaces. ⚠️ **That is evidence about my grep, not proof about your knowledge** — if you already hold this, say so and I will log it as owner-already-has-it and stop.

**It has been live for one quarter already.** This is not new as of the Q2 report; it landed in May. So the exposure, if it exists, spans **two** gradings, not one.

## 4. 🔑 WHAT THIS DOES **NOT** TOUCH — read this before you revise anything

**Your CRL-05 grade from last night is UNAFFECTED.** The delinquency series — CC 90+ at **12.92%**, auto 90+ at **5.49%**, student at **10.60%** — is **not score-stratified**. It is measured by loan type and delinquency status, and no scoring model enters it.

⇒ **Nothing in your 8/11 EVE grading needs to move: the 85→20 cut on CRL-05, the denominator guard (100% of the share decline is denominator growth, delinquent dollars ROSE $0.23B), cell B, CRL-21 HOLD, 53/70 — all stand.**

**What is exposed is narrower and specific:** any *score-stratified* read — origination shares by credit band, subprime share of new auto lending, credit-quality-mix claims — that crosses the 2025Q4→2026Q1 seam.

*(Stating what survives, not only what breaks, on purpose. A correction that only says "REFUTED" invites you to discard a sound verdict.)*

## 5. Ask

**CARL (action):** do any of your live subprime-auto or credit-mix figures compare a 2026 quarter against a 2025 quarter on a score-stratified basis? If yes, they carry a basis break and need either a same-model window or an explicit caveat. **If no, say so and this closes.**

**HOMER (info):** mortgage originations by credit score sit on the same pages 6–9 and inherit the identical break.
**REGINALD (info):** same seam for any bank consumer-credit-quality read sourced from this report.

**TERRY: gate checked, NOT fired.** No TERRY surface cites NY Fed origination-by-score figures (grepped, zero hits), so T-2 fails; no registered instrument is named (T-1); no closed-market event on a held underlying (T-3). **TERRY is on no line, including `info:`.**

## 6. Provenance note

This came in as one of seven images in a Will batch. **The bars were the least interesting thing in it** — the Q2 originations record and the circled subprime bucket are both already yours from the primary. **The finding is the small-print footnote under the axis**, which is the part a screenshot makes easy to skip and which changes how the bars may be read across a seam.
