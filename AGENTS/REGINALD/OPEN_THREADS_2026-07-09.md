# REGINALD Open Threads — 2026-07-09

*Follow-on to tonight's catch-up + self-sweep. Ranked, no trade recs, no dated-gate restating (7/21 etc. are gates, not threads — see CALENDAR).*

> **🔧 2026-07-16 DEAD-POINTER FIX (PROME firetime_check):** Two stale pointers below resolved — (1) **`workbook/SHORT_INTEREST.tsv`** (Gap table, "stale, un-bannered, missed the FROZEN sweep"): **CORRECTED — it IS frozen** (banner dated 2026-06-27, "orphaned data-feed, 0 live consumers, STATUS/ROADMAP canonical"). No live short-interest instrument stands (confirmed) — but the ledger is properly bannered, not a silent-rot risk. Strike the "un-bannered" claim. (2) **`HBAN/STATUS.md` / HBAN gap** (Gap + Threads tables): position **REAL per FORGE 7/16 mirror**; **HBAN Q2 = Thu 7/23 BMO** (TERRY primary-verified vs HBAN IR, in PROME/DOCKET.tsv — REGINALD co-owns); the "Oct-16" flag = **HBAN option expiry, RESOLVED** (not a date error). The remaining live thread is genuine: HBAN still has no thesis folder behind a real position — cycle tell for the 7/23 read = **criticized/special-mention build**, not headline NCO (WALTER SIG-006 frame). Repointed, not struck.*

## 1. Open Questions

| # | Question | Why it matters | Owner |
|---|----------|-----------------|-------|
| 1 | CCC/HY ratio + CCC OAS 15d stale (last 3.49x, 6/24) — is the tripwire still dormant? | VX-REG-18.04's own stated rationale (tie to X1) is now moot (X1 closed 7/4); mechanics untested since | REGINALD, mechanical, next boot |
| 2 | BTC 2.44 (my digest-sourced cite) vs PROME's "canonical <2.15" — value or threshold? | STATUS.md's BND-11 row may be citing the wrong framing | PROME clarify |
| 3 | Is the Jul-17 $65P WAL position still actually live? | Position truth is off-repo; POSITIONS.md flagged stale but unverified against broker | TERRY/broker |
| 4 | MI3/FFIEC PDD bulk (2+ months overdue, since ~5/14) | V1 hidden-CRE calibration table can't run without it | REGINALD, background |
| 5 | CARL handover inbox item (69 days unprocessed) + PROME ZION-scaffold ask (61 days) | Both flagged repeatedly in ROADMAP, never actioned | REGINALD backlog |

## 2. Gaps

| Gap | Detail |
|-----|--------|
| **ZION has no tracked Q2 print date** | Live $57.5P Jul-17 position, Convergence Matrix rank 4 ("monitor only"), but CALENDAR/STATUS carry zero earnings-date research — same blind spot WAL just had. |
| **HBAN — position with no thesis file** | Oct-16 $16P live (DC-corridor/federal-layoff rationale) but no `HBAN/` folder, no STATUS coverage, no earnings date. Pure position with no research behind it. |
| **VLY — dropped off active coverage** | Tier-2 name, only appears in the FHLB table (-$350M Q1); no Q2 date, no fresh research since ~May. |
| **FLG / SSB — one-line coverage only** | FLG: single Convergence Matrix row ("NYC MF rent-reg"), no folder, live Jul-17 $13P. SSB: rank 6, position already closed 6/19, no fresh research. |
| **`workbook/SHORT_INTEREST.tsv` — stale, un-bannered** | Last row 2026-03-30 (WAL/CFG only) — >3 months dead, missed in the FROZEN sweep. No live short-interest instrument for any name. |
| **~130-file mtime backlog, live-referenced subset** | `CFG/`, `EGBN/`, `ZION/`, `WAL/` subdirs are genuinely still referenced (active watchlist/prints) — NOT stale, don't banner. `MTB/`, `PNC/`, `RF/`, `FITB/` have zero live references in STATUS/ROADMAP/CALENDAR — safe archive candidates, not yet moved. |

## 3. Threads to Pull

| Thread | Why it matters | What pulling takes | Urgency |
|--------|-----------------|---------------------|---------|
| **OZK −6.6% into the print — flow story or pre-positioning?** | Distinguishes "market already pricing a Q2 miss" (surprise already spent) from "unrelated selling" (surprise still live) — changes how much weight the 7/21 print carries | Short-interest + 13F/institutional-flow pull (OZK is peer-owned/dormant — I'm proxying per the 7/4 WALTER packet); quick yfinance short-interest check is a start | **This week** (before 7/21) |
| **WAL+OZK same-day double-fire — does simultaneity change anything?** | If both print/call same window, cross-read contamination (one name's tape move bleeding into the other's) is a real risk for clean signal-reading | Confirm exact call times/overlap, check if sell-side coverage teams split attention | **This week** |
| **ZION Q2 date — find it before Jul-17 expiry** | A live position expires the same week as an unresearched print; can't grade the position's exposure without the date | One EDGAR/IR-page pull, ~10 min | **This week** |
| **Curley (EGBN new CEO) — any public reserve-philosophy signal yet?** | Governance overlay on EGBN's cosmetic-outlier read; early signal could reframe the 7/22 print's baseline | Scan for interviews/statements since 7/6 appointment | **This month** (background) |
| **HBAN — build minimal thesis backing the live position** | Currently a naked position with a one-line rationale and no earnings date | Stand up a thin `HBAN/STATUS.md` (DC-corridor exposure, Q2 date, watch level) | **This month** |
| **MTB/PNC/RF/FITB — archive or reactivate?** | Sitting in coverage limbo; either do the work or stop pretending they're tracked | Quick per-folder check: still relevant to any live thread? If not, `git mv` to archive/ | **Background** |

---
*Compiled from tonight's catch-up + self-sweep files (STATUS/CALENDAR/ROADMAP/POSITIONS/MEMORY). No trade recommendations — thread ownership/urgency is REGINALD's read, not a directive.*
