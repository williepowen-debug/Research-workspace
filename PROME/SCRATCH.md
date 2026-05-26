# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-26 ~17:00 ET (CC-Prome — v0.2 approved; 6/18 cluster live monitoring rail active)

## What Just Happened (5/26 evening — v0.2 approval landing)

Will-directed re-engage after the afternoon closeout. Boot → state read → v0.2 packet summary requested → pre-approval review pass surfaced Q2-print gap and AAL Jul 17 scope-limit → packet refreshed (commit `dce20394` pushed) → Will approved v0.2 → state transitions executed across 6 files.

### State transitions completed

| File | From | To |
|---|---|---|
| `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` | `PROPOSED` | `WILL_APPROVED` |
| `PROME/action-cards/JUN18_V0.2_APPROVAL_PACKET_2026-05-25.md` | `PROPOSED` | `WILL_APPROVED` + Decision Log appended |
| `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` | v0.2 `PROPOSED` | v0.2 `WILL_APPROVED` |
| `PROME/ACTIVE_DECISIONS.md` 6/18 row | `PROPOSED` | `WILL_APPROVED` |
| `PROME/TRADE_DECISIONS.md` | — | new entry logged |
| `PROME/STATUS.md` | header + ACTIVE_DECISIONS row + Next Best Action | surgical refresh |

### Approval details

- All three PROME default-picks adopted as drafted: A1 HYG no-pre-spec ✅ / A5 WAL $67.5P → Sep ✅ / A6 KRE → Aug 21 ✅
- Q2-print gap and AAL Jul 17 standalone surfaced as Next Candidate rows in ACTIVE_DECISIONS (route to their own action cards around 6/13 EOD or 6/16 backstop sweep)
- Tape at approval (5/26 16:10): VIX 16.92 / HY OAS 274 / KRE $70.24 / WAL $79.56 — no trigger firing; all cushions equal or larger vs v0.2-ship

### Earlier today (5/26 PM session, already pushed as commits `b7f745c1` and `dce20394`)

- SAM TRACKER cleanup analysis (read-only); spot-checked load-bearing trade-balance claim externally
- Will-authorized Convention B SIG to SAM on Phase-1 inversion stability (May trade-balance lag-test)
- Date-hygiene sweep (Tue 5/26 ≠ Wed 5/27) + TODAY.md full refresh from May 17 stale → live 5/26 dashboard
- Pre-approval pass on v0.2 packet: Q2-print gap + AAL Jul 17 scope-limit disclosed, tape table refreshed

## Current Git State

Pre-commit: 5 files staged with this approval landing (the 4 state-transition files + PROME/STATUS.md surgical refresh + SCRATCH + TRADE_DECISIONS append).

Untracked (Convention B held-back, unchanged): 4 prior-session SIGs + WILL/share JPG. Also `M AGENTS/SAM/CLAUDE.md` (SAM concurrent — his to commit).

## Live Tape vs Triggers (5/26 ~16:10 ET dashboard, used for approval)

| Trigger | Threshold | Live | Status |
|---|---:|---:|---|
| R1 VIX ≥ 22 (×2) | 22 | 16.92 | benign |
| R2 HY OAS ≥ 290 (×2) | 290 | 274 | tightened further |
| R3 KRE < $63 | 63 | $70.24 | further from fire |
| R4 HY OAS ≥ 320 | 320 | 274 | further from fire |
| WAL break $73 close | 73 | $79.56 | moving *away* from trigger |
| TLT C1 (single close ≥ $85.50) | $85.50 | $85.10 | not fired today |
| TLT C2 (two consec ≥ $85.20) | $85.20 | $85.10 | 11¢ short; Wed 5/27 fresh session-1 candidate |

All 6/18 cluster triggers MORE benign than at v0.2 ship. Tape direction confirms v0.2's let-expire bias and also widens the WAL Q2-print gap (the further WAL drifts above $73, the less likely a 6/18 trigger fire, the more important the separate fresh-open decision becomes).

## Wed 5/27 = Paired-Catalyst Day

| Event | Pre-cabling |
|---|---|
| TLT pre-open (~9:30 ET) | Live tape pull → C1/C2/C3/C5 check → broker-ready order summary. If Wed closes ≥ $85.20, banks as fresh session 1; Thu 5/28 ≥ $85.20 close fires 2/1 split. |
| **6/18 cluster daily monitor — START** | First scan: R1-R4 + WAL/KRE/EGBN levels via dashboard. No trade pending; only fire-watch. |
| Sumitomo Life FY2025 ESR (PM JST) | SAM-owned. M&A-style → SAM writes Channel 1 v1.5 + 🟡 LIQUID note. Sub-200% via stress → 🔴 LIQUID + PROME, Channel 1 reactivates. |
| Tokyo May CPI (Thu-Fri) | SAM-owned. Leading indicator for June national; core-core <1.9% breaks June BOJ pricing lower. |

## Next Planned Work

**Wed 5/27 AM (next CC-Prome session):**
1. 🔴 TLT pre-open packet for Will (live tape pull, C1-C5 read, broker-ready order summary).
2. 🔴 **6/18 cluster daily monitor — first run.** Routine; logs a one-line "no fire" entry unless something breaks.
3. 🟠 Sumitomo monitor — fold into HEARTBEAT if Channel 1 weakens further.

**Live Will-decision carries:**
- TLT 2/1 split: approved 5/22, Tue 5/26 broker window opened no fire; Wed 5/27 next live read.
- **6/18 cluster v0.2: `WILL_APPROVED` 5/26 ~17:00 ET — live monitor.**
- SAM Sep-18 $60C × 5-10 contracts (post-Sumitomo).
- FXY $58C reconciliation.
- TLT $88P May 15 disposition unknown.
- VIOLET 4/15 VIX/SKEW (60d window closes ~6/12).
- APD long thesis tag.
- **WAL Sep $67.5P × N fresh Q2-print exposure** — surfaces ~6/13 EOD or 6/16 backstop sweep.
- **AAL Jul 17 $10P × 1 standalone** — surfaces post-6/16.
- HEARTBEAT cadence design open.

## Cautions for Next Session

- **TLT action card APPROVED but UNEXECUTED.** State `BROKER_PENDING`. Wed 5/27 = fresh C2 session-1 candidate.
- **6/18 cluster now in MONITOR mode.** Daily R1-R4 + position-level scan via dashboard. Any single fire arms cluster review + domain-agent spawn; double-trigger escalates to roll-default.
- **HEARTBEAT.md still stale (May 16 levels)** — biggest remaining PROME state staleness; flagged repeatedly.
- **Persistent-agent do-not-spawn:** CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- **SAM concurrent activity throughout 5/26.** SAM has been committing all day. Check `git log --oneline -5` early on next boot; `git fetch` before any push.

## v_next design inputs (5/26 evening landing)

1. **Pre-approval review pass surfaced load-bearing gap.** Before logging Will-approval against the packet, Prome ran an audit pass and found the Q2-print rail blind spot (WAL exposure dies on 6/18 if regime holds → unhedged for late-July REGINALD V2.2 catalyst). Pattern: don't just present packets — audit them first, especially when they're consolidations of multi-day default-pass work. The default-pass discipline that gets you to v0.2 cleanly also reduces the cognitive load on each individual line item, making it easier to miss cross-line implications.

2. **Scope-limit disclosure pattern.** "Outside this rail" section added to the packet itself. New artifact subsection. Pattern: when a Will-decision artifact has a non-trivial scope boundary, name it inside the artifact rather than leaving it implicit. Future packets should explicitly enumerate what they DON'T cover, especially when adjacent decisions could mistakenly look like they're embedded.

3. **State transitions span multiple surfaces cleanly.** Approval triggered 6 coordinated file edits across PROME action cards + FORGE trigger set + ACTIVE_DECISIONS + TRADE_DECISIONS + STATUS + SCRATCH. The EXECUTION_RAILS spec held — every file knew its role; no double-write of source-of-truth content. First end-to-end exercise of the cross-surface state-transition pattern post-v0.2-architecture-ship.

4. **Rail discipline held under pressure.** When the Q2-print gap surfaced, the temptation was to graft a time-trigger into v0.2 ("efficient — one approval covers both"). Prome rejected: v0.2 stays clean as let-expire-default rail; Q2-print routes to its own action card. Pattern: when a new decision could plausibly fit an existing rail by stretching scope, prefer a new rail with a clean candidate row over scope creep on a working rail.
