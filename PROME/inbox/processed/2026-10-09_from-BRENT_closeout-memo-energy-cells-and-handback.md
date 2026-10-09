## 2026-10-09 — To: PROME (prome-75), from BRENT (written 11:18 EDT from `date`)

**Signal:** BRENT AM session closed at 11:2x ET on Will's word. Energy cells for the post-close HEARTBEAT base are below. ⚠️ **Three items owed today are HANDED BACK UNDONE:** the COT #9 grade, the MMA 10/9 read and the settle-window crack.
**Priority:** 🟠
**ACTION (PROME):** route the three handed-back items (below) to a live BRENT session, or record them as owed; nothing else is asked.

### ⚠️ Handed back, NOT done (session closed before these printed)

| Item | When | Exact method | Note |
|---|---|---|---|
| **COT #9** `GATE-BRENT-COT-35B` (review_by TODAY) | ~15:30 ET Fri 10/9, as-of Tue 10/6 | `.venv/bin/python3 AGENTS/BRENT/scripts/cot_grade.py --expect 2026-10-06` + independent raw `f_disagg.txt` pull | cot_grade.py Leg-B now compares exactly (L546, `085bac42a`); the 9/29 regrade reproduces 6.8901% NOT-SPENT. **Grade before Fri 10/16** (no stacking). TRACKER line 8 stays ARMED |
| **MMA shut-in 10/9** | ~13:00 CDT | BSEE `…/mma-monitors-gulf-response-isaias3` (`isaias2` = 10/8; `isaias3` was 404 until at least ~11:15 ET) | 10/8 = 1,282,879 b/d = 62.89% |
| **Settle-window matched crack** (WQ-386 leg A is TERRY's grade) | 14:28–30 ET | `research/2026-10-08_isaias-hormuz/pm_crack_pull.py` method | ESTIMATE only |

### Energy cells (dated, basis-tagged; for the HEARTBEAT base)

| Cell | Value | Basis / date |
|---|---|---|
| Dec Brent `BZZ26` | $104.11 | single-vendor quote 10:12 ET 10/9, **not a settle** |
| Nov WTI `CLX26` | $91.58 | same; 10/8 settle $91.49 (Newsquawk relay) |
| Dec WTI−Brent | −$13.51 | same pull |
| Nov diesel crack (HOX26×42−CLX26) | **$109.15** [EST] | same pull; −$4.43 vs the 10/8 14:28–30 window $113.58. Diagnostic, not a WQ-386 observation |
| **Dated Brent physical (EIA RBRTE)** | **$125.44** (10/6); $135.51 (10/2) | EIA API primary (FRED republishes it, one lineage). **>$110 every print since 9/9. REGISTRY >$120 line reads above. ⛔ This SUPERSEDES BRENT's 10/8 "anomaly / not a real breach" label: that label was wrong** |
| 10/8 official ICE `BZZ26` settle | **UNAVAILABLE to BRENT** | NEXUS L553 answered (b); window VWAP $104.273 [EST] is not a settle |
| Gulf shut-in (Isaias) | 62.89% oil / 57.35% gas | BSEE/MMA 11:00 CDT 10/8 (no newer release read) |
| Isaias | Cat 3, 120 mph, 959 mb | NHC 7:20 CDT via WALTER -004; refineries: no cut found (Chevron's "operational" = Thursday) |
| SPR stocks | 282.983M bbl (wk 10/2) | EIA WCSSTUS1 API; last-4-wk draws 0.06–0.11 mb/d; 13-wk avg ~0.40. **The Dallas Fed's ~1.2 mb/d is not visible in this series** |
| SPR exchange (bids 10/6) | awards UNPUBLISHED | DOE OPR page + search, 10:5x ET |
| China product exports | ~3.7 Mt approved for Oct | Reuters Singapore 10/9 (unofficial: 4 traders + 2 participants); Sep ~4 Mt expected, Aug 4.6 Mt actual. Paper, not shipments |
| TD3C VLCC | $1,221,893/day, WS1145 | Baltic 10/2 (wk-41 print bot-gated, UNREAD) |
| War-risk insurance | 6–10% of hull per voyage | FT brokers via IBTimes 10/8 / TBS 10/7 (relay) |
| Forward curve (11:11 ET, vendor) | WTI−Brent −13.84 (Dec26) → −6.46 (Dec27); diesel crack 104.50 → 69.44 | vs 2025 spot averages −3.58 / 32.45 (FRED, 244 days; different basis) |
| USO | $148.81 | 11:14 ET vendor; Oct-9 $150C at $0.23/$0.25 screening. Will's 15:00 rail; disposition UNKNOWN to BRENT |

### Done this session (commits `a16831e82` → closeout)
- Inbox fully consumed (11 = 11 board_log rows).
- L546 fix. LESSONS_INDEX semantic reconcile plus a real separator defect fixed: L05 had been invisible to `--spec`.
- Incident re-verify of 5 rows.
- China catalyst graded.
- #8 switch date recorded: **BZZ26 LTD Fri 10/30 → Jan legs Mon 11/2** (ICE primary; sent to WALTER).
- Structural-cost research note (concept only, TERRY constructs).
- STATUS rule-5 rotation.

**Will-facing caveat that must survive:** Will said he expects further escalation. BRENT gave roll facts on the expiring call, not a proposal. A Nov/Dec same-strike roll (~$885–1,155 ask) exceeds the ~$500 new-risk norm. A spread-priced roll via TERRY was offered; Will closed without asking for it, so **no TERRY ask was sent.**
**Source:** BRENT session 2026-10-09; files above. $0.
