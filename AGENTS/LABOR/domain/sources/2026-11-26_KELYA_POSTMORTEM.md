# KELYA $7.5P (Aug 21 2026) — post-mortem, one page

**Written:** 2026-11-26 by LABOR, on Will's word (15:40 ET, verbatim *"Lets go with your recommendations for the three open items you flagged"*; LABOR recommended a one-page version). **Question owed since 2026-08-21** (`TRADE.md` §2): *was the entry sound on the March data, or was the company-vs-industry conflation already inferable then?* Thesis side only. Premium, sizing and structure are FORGE's and TERRY's and are not restated here. **Outcome:** expired worthless 2026-08-21, KELYA close $17.09 against the $7.50 strike (`domain/sources/TRADE_archive_20261126.md`).

## Answer: the conflation was inferable at entry, from the canonical series, on the day the call was registered

| Date | What LABOR's surfaces said | What the canonical industry series said (BLS CES temporary help services, TEMPHELPS, SA, **as published that day**, ALFRED) |
|---|---|---|
| 2026-02-18 (LAB-01 registered, *"Temp YoY stays <−6%"*, **85%**) | the call itself | Jan 2026 **2,480.1K** vs Jan 2025 2,539.3K ⇒ `2,480.1 / 2,539.3 − 1 = −2.33%`. **Already above the −6% line it was betting on** |
| 2026-03-02 (STATUS, position live) | dashboard *"Temp Employment YoY **−12%** 🔴 Re-accelerating"*; same table: *"RHI/KFRC bottoming after 12Q"* as a counter-signal (`git show e96ea339cc:AGENTS/LABOR/STATUS.md`, lines 33, 93) | — |
| 2026-03-06 (Feb jobs report, the Mar 7 generation's data) | thesis *"temp staffing patient zero"* | Feb 2026 **2,447.4K** vs Feb 2025 2,533.0K ⇒ `2,447.4 / 2,533.0 − 1 = −3.38%`; Nov–Feb 2,465.5 / 2,451.4 / 2,453.9 / 2,447.4, i.e. `2,447.4 − 2,465.5 = −18.1K` over three months, near flat |
| 2026-06-05 (after LAB-01 ❌ on 6/2) | — | May 2026 2,490.0K, `−0.92%` YoY, three straight monthly gains (Feb 2,471.9 → Mar 2,479.9 → Apr 2,488.6 → May 2,490.0) |

- **The −12% was not the industry series.** Its source was not recorded. The nearest company figures in the March file were KELYA's own segment declines (ETM −18.6%). The dashboard row carried no source tag.
- **So the entry rode a figure that was not the industry series, presented as if it were** (most likely company-tier, unproven). The canonical series that the 85% call named was already contradicting it by about 3.7 points (`−6.0 − (−2.33) = −3.67pp`) on the day of registration. The staffing-canary counter-signal (RHI/KFRC turning) was on the same March page and was rated as "complicated", not as disconfirming.
- **What was right:** KELYA's own weakness was real (Q1 revenue −10.7% YoY, a miss). The company read was sound; the inference from it to the labour market was not, and the market priced the company, not the macro thesis.

## What would have caught it, and whether it exists now

| Control | Existed at entry? | Now |
|---|---|---|
| Name the canonical series and read it at registration | No | **Yes:** gate #1 *canonical-not-proxy* of the 15 pre-write gates (`workbook/PREDICTIONS_SCOREBOARD.md` §C); L-01 *company-tier revenue ≠ industry employment* |
| `[CONF]` needs a named primary | No | **Yes:** charter OUTPUT RULES |
| Read the counter-signal as possibly disconfirming | No | Partly: gate #3 threshold-vs-mechanism; RED's challenge seat |

**No new rule is proposed:** the two controls that would have caught this were built after it (gate #1, the `[CONF]` rule), and Will has asked for fewer rules. **For TERRY (trade construction owns trade post-mortems):** on a single-name put that rides a macro thesis, the macro leg should be checked against the canonical series at entry, not the company's own prints. That is TERRY's call to adopt or not.

*Sources: ALFRED TEMPHELPS observations at realtime 2026-02-18, 2026-03-06, 2026-06-05 (FRED API, pulled 2026-11-26); `domain/sources/TRADE_archive_20260307.md`; `domain/sources/TRADE_archive_20261126.md`; `workbook/PREDICTIONS.tsv` LAB-01; `LESSONS.md` L-01.*
