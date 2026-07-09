# LABOR — Open Threads
**As of:** 2026-07-09 ~18:05 ET (PROME-directed sweep). Ranked within each bucket. Dated gates (claims 7/23, NFP 8/7, etc.) excluded by design — see STATUS MONITORING CALENDAR for those.

## 1. OPEN QUESTIONS

| # | Question | State | What settles it |
|---|---|---|---|
| 1 | **"Shadow-adjusted ~270K" claims vs headline 215K — which is right?** | Traces to the May-2026 FL-suppression thesis (headline+70K shadow premium). **WEAKENED to effectively dead** — the Jun-2 read found no claims spike when DHS-shutdown suppression lifted May 1 (`STATUS_archive_20260602.md`). LABOR carries **no live shadow-adjustment premium today**; the vector 13 read uses headline 215K straight. Any packet citing "~270K shadow" as current is stale. | Nothing pending — this is a **correction to propagate**, not an open test. |
| 2 | **LAB-04 (FL foreclosures) — CARL pickup limbo.** | Reclassified→CARL Jun 16; kept OPEN in LABOR's ledger only so boot-scan keeps flagging it. `predictions_due.py` now shows it **9 days overdue** (due 6/30). | CARL either formally owns it or LABOR closes/reclassifies the row — currently nobody's clock. |
| 3 | **NEXUS_BRIEF re-pin owed** (flagged in today's self-sweep). | VIEW/CALIBRATION dated Jul 2; ISM Svs, MSFT/Xbox, WARN cluster, tonight's claims grade all post-date it. | A full re-pin session (not urgent — STATUS.md is current). |
| 4 | **S&P Global vs ISM mfg employment — which read leads?** | S&P Global: "fastest cuts since May-20" (flash confirmed final). ISM Mfg emp: 49.7, improving, best since Jan-25. BLS realized: +3K. 2-of-3 say no acceleration; S&P is the outlier pending realized data. | ISM Mfg July (~Aug 3) or a realized mfg-employment move. |

## 2. GAPS (coverage holes, no instrument)

| # | Gap | Why it matters |
|---|---|---|
| 1 | **TX WARN feed still not repointed** to the TWC Excel primary (diagnosis done 7/2, fix not yet applied — `warn_texas.py` still reads the stale Socrata API, false-quiet). | TX is a top-5 WARN state; cron reads are silently wrong until fixed. |
| 2 | **No state/MSA-level JOLTS** — LABOR tracks national aggregate only, despite "geographic employment" being in-scope. | Can't localize the freeze (FL, TX, WA) beyond claims-level anecdote. |
| 3 | **WA-ESD WARN filing** for MSFT round-2 has no automated puller — manual check only, watching for it ~Jul 13+. | First hard domestic count vs the announced ~5,700; currently a "remember to look" not a feed. |
| 4 | **Insider Form-4 scanner (WAL/OZK) never built** — flagged as a gap since Feb 28, still `⬜ PENDING`. Framework (14x sell/buy ratio) exists; no live pull feeds it. | 3-6mo layoff lead-indicator sitting unused on the bank watchlist. |
| 5 | **Job-posting-withdrawal tracker** (LinkUp/Revelio/TrueUp) — same story, flagged Feb 28, never built. | 4-12wk lead indicator, cheapest early-warning layer LABOR doesn't have live. |

## 3. THREADS TO PULL (nobody's chased these)

| # | Thread | Why it matters | What pulling it takes | Urgency |
|---|---|---|---|---|
| 1 | **8-firm big-tech WARN wave — who files 9th?** Is there a leading indicator (insider selling / posting withdrawal) on other large software/SaaS names not yet in the cluster? | LAB-17/LAB-11 both hinge on whether this cohort is closed or still growing. | Cross-ref Form-4 + job-posting data for software/SaaS names adjacent to the cluster (chips stayed quiet — is that durable?). | **This-week** — informs LAB-17 odds before the Jul-18 window opens. |
| 2 | **LFPR less-than-HS-diploma cohort drop — composition math.** Is the national LF −720K genuinely ICE/supply-shrink, or partly demographic (aging-out/retirement)? | This is the mechanism behind U-3 suppression (L-06) — if it doesn't hold, LAB-12's premise weakens further. | Decompose LFPR by education tier over a longer window; cross-check vs MARCO's removal/self-deport estimates. | **This-month** — feeds LAB-12 (Q3-Q4). |
| 3 | **Construction hiring-rate (3.5%, ties record) vs openings (10mo-high ~298K, data-center/electrician) mismatch.** Skills-mismatch (benign) or early demand-destruction with openings lagging (not benign)? | Construction is a canary for both AEOLUS/CORAL climate-driven build activity and rates-sensitive CRE. | Occupation-level JOLTS detail (not industry-level) + regional data-center-buildout openings vs regional hiring-rate. | **Background** — next natural check-in is JOLTS June (Aug 4). |
| 4 | **Robert Half "32% of AI-cut roles rehired" stat — durable or one-off?** Load-bearing for LAB-11 (55% conf) but sourced 2nd-hand via CNBC. | If it doesn't replicate, the AI-narrative-shield-breaks case loses its strongest FOR datum. | Pull the Robert Half primary report; look for a second corroborating rehire dataset (Indeed/LinkedIn). | **This-month** — feeds Q2-earnings read (Jul-Aug). |

---
*Sources: STATUS.md, NEXUS_BRIEF.md, PREDICTIONS.tsv, board_log.tsv, domain/sources/STATUS_archive_{20260504,20260602}.md, LESSONS.md, workbook/VX.tsv archive. No trade recs.*
