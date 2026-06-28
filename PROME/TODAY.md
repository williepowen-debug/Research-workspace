# TODAY.md — Sunday June 28, 2026
**Updated:** 2026-06-28 (Sun, DESKTOP) closeout ~17:50 ET — infra/coordination day. Laptop AM pre-registered the 6PM oil test; desktop PM did: FORGE-ref sweep, SHADE/CREED/BROCK catch-up, the **DAEDALUS maturity thread** (BATCH_01 applied, firm-next-7 all→L4, BATCH_02 queued, utility-blueprint greenlit), **WALTER boot-split** (landed+verified), and **COP retired** (Will's call). **No trade executed** (standing rule held). Weekend — Brent $71.99 is 6/26 Fri-close. **⚠ The 6PM oil grade was LEFT UNDONE — closed out ~12m before the reopen; it's the #1 next-session item.**

**Objective:** the day's live event was the ~6PM oil reopen — pre-registered AM, but **left ungraded** at this close. Everything else (FORGE, catch-up, DAEDALUS/WALTER architecture) was coordination/infra.

---

## ⏰ THE LIVE EVENT — ~6:00 PM ET CME oil reopen (LIVE NOW — UNGRADED; grade FIRST next session)
| If Brent... | Read | Action |
|---|---|---|
| **<$74** HOLDS (~45%) | decoupling survived; thesis *strengthens* | none (XLE $65C stub more lapse-leaning) |
| **$74-76** AMBER (~30%) | partial, thin Sunday tape | **wait, don't chase** |
| **>$76, or $74-76 sustaining >$75 into Mon London** CRACKS (~25%) | RED-FT-04 inverts | **re-arm** → USO call-spread ≤$500, to Will AFTER the sustain |

**Grade the sustain, not the gap.** Leading tell (premium→barrels): 2nd vessel struck / mine detonation on a hull / P&I-insurer pull / transit collapse. Pre-reg detail: `AGENTS/BRENT/PREREG_20260628_CME_reopen.md` · `AGENTS/HAWK/REMARK_20260628.md`. HAWK scenarios B20/C44/D36 (was 34/44/22).

## Session Posture
| Item | State |
|---|---|
| Origin | Laptop Claude Code (sole writer); desktop later today. |
| Git | Clean, synced 0/0, all pushed. **Online/web CC app is now a live 2nd writer** (AEOLUS pushed from it) — pull before committing; safe-push ff-aborts on divergence. |
| Agents | BRENT+HAWK spawned (fan-out, delivered, idle). WALTER ran live earlier (self-closed). Not warm — spawn fresh next session. |
| Push rule | AUTO-PUSH at closeout via `safe-push.sh` (ff-gated). Non-ff abort = 2nd writer → flag Will, don't force. |

## Regime (one-line) — weekend, 6/26 Fri-close orientation
**Energy tail RE-ARMING** (Iran re-escalated 6/28, confirmed kinetic) — but **decoupling held at last print** (Brent $71.99 fell as US struck); the ~6PM open is the live test. Credit-bear **ARMED, pre-trigger**; HY 278 [6/25], 2bp from >280 (auto-watched). **Refresh dashboard/FRED before citing any level live.**

## Standing rule (Will 6/26)
Deploy fresh capital ONLY on a fired (sustained) trigger; $500/card max-loss. No mechanical book-reshape. ([[feedback_deploy_on_trigger_not_calendar]])

## Watch next 24-72h
0. **~6PM ET oil reopen** (above) — the live one.
1. HY vs 280 (278 [6/25], auto-watched). 2. 10Y 6/30 · JOLTS 6/30. 3. EIA 7/1 · NFP 7/3 · CFTC COT 7/3. 4. Bank prints OZK/WAL/CFG Jul-16. 5. June CPI 7/14.

## Fresh-boot checklist
1. Verify git sync — **2nd writer live (online app); pull first.** 2. **Grade the 6PM oil open** if it's past ~6PM ET (SCRATCH = entry point). 3. Refresh dashboard/FRED before citing levels. 4. ✅ Root `CLAUDE.md` FORGE-ref sweep + FORGE/STATUS staleness banner DONE 6/28 desktop (b169e149). 5. No agents warm — spawn fresh.
