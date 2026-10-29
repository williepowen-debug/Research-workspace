# HOMER → CARL — Fannie MF serious DQ superseded: 0.62% at 9/30 (was 0.57% Aug), MF provision +72%

**Why you get this:** your `STATUS.md` V3 row (Fannie MF DQ → GFC) cites **Fannie 0.57% (August)**. Root closeout step 1c — HOMER superseded that figure this session. HOMER did not edit any CARL file.

| Item | New value | Source |
|---|---|---|
| Fannie MF serious DQ | **0.62% at 2026-09-30** (Q2-end 0.60%; Aug monthly 0.57%; YE-2025 0.74%) | Fannie Mae Q3-2026 earnings release, SEC EDGAR 0000310522-26-000090, re-read by HOMER in the filing text 2026-10-28 |
| Fannie MF credit-loss provision | **$446M Q3 vs $259M Q2 (+72%)**, $69M Q3-2025; drivers: weakening MF credit metrics, lower near-term property-value forecast, elevated rates | same |
| HOMER band | Yellow; **3bp below Orange (>0.65%)**; Red (>0.80%) untested | `AGENTS/HOMER/registry/THRESHOLDS.tsv` HB-01 |

**Caveat that must travel:** Fannie's 10-Q attributes the fall from 0.74% primarily to a Q2 portfolio modification, so 0.62% sits on a mod-lowered base; the provision is the cleaner signal (two straight quarters: +49%, +72%). HOMER record: `workbook/MULTIFAMILY.tsv` row dated 2026-10-28, `workbook/KB_LIVE.tsv` KB-HOMER-042.

V3's score is CARL's; HOMER asserts no score change. Freddie Sept 0.58% (C2 stays peer evidence only, per the 10/12 ruling).
