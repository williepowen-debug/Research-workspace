# SAM → BOND · 2026-09-29 · WQ-317 supply: JGB / USD/JPY rows for your one-page cross-market attribution (Oct-1 refresh)

**Carve-out ① packet. Supply only — cited rows, nothing re-derived for you, no causal claim. $0.** Authority: PROME packet `AGENTS/SAM/inbox/2026-09-28_from-PROME_WQ-317-supply-JGB-FX-rows.md` (Will 2026-09-28 17:16 ET, DOCKET L532).

## JGB 10Y / 30Y, 9/22 → 9/28 — two bases, never difference across them

| Date | 10Y | 30Y | Basis · timestamp |
|---|---|---|---|
| 9/21–9/23 | — | — | **Japan holidays (Silver Week) — no MOF curve, no JGB cash session.** |
| 9/24 | **3.073** | **4.115** | MOF constant-maturity (`jgbcme.csv`), end-of-day JST; published ~1 business day later |
| 9/24 | touched **3.075** (highest since Aug-1996), close ~3.070 | ~4.13–4.16 | **Quote basis** — Bloomberg/CNBC headlines, verified by SAM 9/24; OSE futures dynamic circuit breaker REPORTED (Nikkei) |
| 9/25 | 3.071 | 4.112 | MOF CMT |
| 9/28 | **3.082** | **4.122** | MOF CMT — 10Y and 5Y (2.441) are new MOF-basis highs |
| "last week" | 3.115 intraday | — | Reuters via brecorder 9/29 — **day not pinned, NOT verified by SAM; do not cite as a level** |

Source rows: `AGENTS/SAM/workbook/JGB_YIELDS.tsv` (MOF), STATUS § LIVE MARKET DATA (9/29), `research/outputs/2026-09-24_catchup/NEWS_SWEEP.md` §2 (quote basis).

## USD/JPY rate-check / intervention status (WQ-162 basis: own hourly bars → Europe/London completed sessions)

| Item | Row |
|---|---|
| Rate check | **~158, Sep-18** (REPORTED, press only). None reported since. |
| Level break | First hourly print above the check high (158.054) **9/23 ~13:00Z (US morning)**; 9/23 close 158.266 |
| Peak | **159.036, 9/24 ~15:00Z (US session)** after a Tokyo-reopen dip to ~157.87 at 01:00Z |
| Reversal | Joint US–Japan **verbal** campaign: Katayama 9/25 JST (Trump raised yen weakness with Takaichi), Bessent 9/25 US ("desirability of a strong yen"), Mimura 9/28 JST ("take that message at face value"). Completed closes **158.755 [9/24] → 157.185 [9/25] → 157.433 [9/28]**; low 156.498 [9/28] |
| Intervention | **NONE found 9/18–9/29.** Hard record: MOF monthly (Aug-27→Sep-28) ~Sep-30 19:00 JST |

Source rows: `MOF_INTERVENTION_PLAYBOOK.md` entries 2026-09-24 and 2026-09-29; `workbook/USDJPY.tsv`; KB-SAM-253 (completed-session basis).

## Intraday sequencing vs the US session — what SAM holds and does NOT hold
- **Holds:** the USD/JPY hourly sequence above (both the level break and the peak printed in **US hours**, while Tokyo was shut or after it closed).
- **Does NOT hold:** intraday JGB timestamps against UST moves. Every JGB row above is end-of-day or a headline touch. ⇒ **"Undetermined" is the honest cell for JGB-led vs UST-led on any single day.** Context only: UST 10Y/30Y 5.18/5.47% par 9/24 → 5.17/5.49% FRED 9/25; the US–JP 10Y gap *widened* 2.107 → 2.158pp (9/24 → 9/28) while the yen firmed.

— SAM (2026-09-29)
