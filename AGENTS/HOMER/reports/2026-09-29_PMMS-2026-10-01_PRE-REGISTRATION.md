# PMMS 2026-10-01 — PRE-REGISTRATION (written 2026-09-29, before the print; Will-directed)

**Instrument:** Freddie Mac PMMS 30-year fixed, weekly, Thursday 12:00 ET. **Band letter (CLAUDE.md, unchanged):** Yellow >5.5% · Orange >6.5% · **Red >7.0%**. Strict inequality. **No sustain clause.** Graded 9/24: **7.03%, RED crossed by 3bps.**

⛔ **No threshold moves.** "Hold / soften / lift" below are **reporting states**. The band grade stays binary on the letter. SOFTEN is still RED.

## 1. The three outcomes, fixed now

| State | PMMS 10/01 | Band grade (letter) | What I report |
|---|---|---|---|
| **HOLD** | **≥ 7.05%** | 🔴 RED | "RED, second print above the line, +X bps. No uncrossed rung." The 9/24 caveat (*"3bps is less than one week's move"*) is retired. |
| **SOFTEN** | **7.01–7.04%** | 🔴 RED (unchanged) | "RED on the letter, within one median week (4bps) of lifting." The 9/24 caveat stands. I do not describe the RED as confirmed. |
| **LIFT** | **≤ 7.00%** | 🟠 ORANGE (>6.5%) | "Back below RED. Highest uncrossed rung RED, X bps away." **The 9/24 cross is not retracted:** it was correct on the letter, and the letter has no sustain clause, so the band can flip back. Same-day note to PROME (the 9/25 HEARTBEAT carried the RED). |

**Where the SOFTEN width comes from:** the **median absolute weekly PMMS move over the 52 weeks to 9/24/2026 is 4bps** (mean 5.2, p75 7, p90 10, max 19). Source: Freddie Mac `PMMS_history.csv`, read 2026-09-29. A print within 4bps of the line is within one ordinary week of flipping.

## 2. What the inputs already imply (the base case, not a forecast)

| Input | Value | Source |
|---|---|---|
| 10Y Treasury par yield | 5.11 [Wed 9/23] → 5.18 [9/24] → 5.17 [9/25] → **5.24 [Mon 9/28]** | Treasury daily par curve CSV, read 2026-09-29 |
| Survey-matched spread (PMMS − Wednesday 10Y) | **192–194bps, flat four weeks** (n=4) | `workbook/RATES.tsv` |
| MND daily 30Y | 7.45 [9/24] → **7.50 [Mon 9/28]** | mortgagenewsdaily.com |

**Treasury-implied PMMS for 10/01 = Wed 9/30 10Y + 1.92–1.94.** On Monday's 5.24 that is **~7.16–7.18% ⇒ HOLD.**

**What LIFT requires:** Wed 9/30 10Y at **≤ ~5.06–5.08%**, a **16–18bp rally in two sessions** (4× a median PMMS week). Or the spread compresses by the same amount, which it has not done in four weeks. **Both are possible and neither is the base case.**

## 3. Diagnostics to run on the print (fixed now)

1. **Residual vs Treasury-implied:** PMMS − (Wed 9/30 10Y + 1.93). If **|residual| > 10bps** (the p90 weekly move), the spread moved. Then the move is no longer "all Treasury", and I say so separately from the band grade.
2. **Year check (LESSONS §46):** confirm the page reads **10/1/2026** before grading. 7.0x prints existed in 2023–25.
3. **15-year** (6.42 on 9/24) is reported alongside, not graded.

## 4. Who is affected
- **PROME:** the HEARTBEAT carried the RED on 9/25. A LIFT means a same-day note; HOLD and SOFTEN go through the normal NEXUS_BRIEF fold.
- **CARL / REGINALD:** read via NEXUS_BRIEF. No packet unless LIFT.
- **Docket:** `docket/CATALYSTS.tsv` PMMS row points here.

— HOMER
