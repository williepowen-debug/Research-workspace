# PROME STATUS.md
**Updated:** 2026-05-18 (session closeout)

## Core State

**Regime:** BDC/private-credit credit/mark stress is confirmed, but public-credit contagion remains unconfirmed. Surface tape is still calm: HY OAS **276bps** and VIX **18.43**. Stress is concentrated in Brent/gas, USD/JPY, BIZD, WAL/KRE, and pending bank/BDC decision rails.

**Working model:** sponsor-supported private-credit/BDC deterioration + vol-suppressed public tape. Treat HY OAS <300 and VIX <20 as constraint against broad cascade adds, not as an all-clear.

---

## Latest Sync / Architecture State

| Item | Status | Note |
|---|---|---|
| GitHub sync | ✅ Complete | Pulled cleanly; local `master` = `origin/master` at `8a44dbe2`. |
| REGINALD update | ✅ Pulled | WAL Investor Day findings + May 17 closeout integrated into Prome state. |
| WALTER update | ✅ Pulled | Multi-session closeout confirms signal-routing ownership and May 18 callbacks. |
| Claude Code Prome scaffold | ✅ Present | Phase 2 complete; Phase 3 dry run still pending. |
| WALTER/Prome split | ✅ Codified | WALTER owns signal/news routing; Prome owns tasking, rails, and synthesis. |
| memory-audit-001 teams test | ✅ Complete | First bounded Agent Teams primitive run. Adversarial-pair pattern validated. 3 MEMORY.md entries + 2 in-place updates landed. META_EVAL at `PROME/scratch/teams_memory_audit_001/META_EVAL.md`. |
| Orchestral layer design | ✅ Captured (not yet prototyped) | Fleet scan + adversarial-pair top-N + revival proxies. Full design at `PROME/ORCHESTRAL_LAYER_DESIGN.md`. Next-session entry point = Step 1. |

---

## Active Decision Layer

| Artifact | Status | Purpose |
|---|---|---|
| `HEARTBEAT.md` | ✅ Fresh May 16; levels rechecked May 17 | Scenario, levels, catalyst/position rails |
| `PROME/SCRATCH.md` | ✅ Fresh May 18 (closeout) | Ephemeral next-action state; entry point for next session |
| `PROME/FLEET_SCAN.md` | ✅ Fresh May 18 (v2 prototype) | Live working surface — fleet situation report |
| `PROME/CLOSEOUT.md` | ✅ Fresh May 18 (new) | Standardized session-end procedure |
| `PROME/BOOT.md` | ✅ Refreshed May 18 | TOSCANINI references cleaned; FLEET_SCAN + CLOSEOUT integrated |
| `PROME/ORCHESTRAL_LAYER_DESIGN.md` | ✅ Fresh May 18 | Design + ranking rubric (HUNTING dimensions distilled in) |
| `PROME/TODAY.md` | ⚠️ Stale (May 17) | Superseded by FLEET_SCAN.md as live working surface |
| `PROME/HANDOFF.md` | ⚠️ Stale (May 17) | Telegram-Prome surface; defer to SCRATCH for CC-Prome continuity |
| `PROME/CLAUDE_CODE_HANDOFF.md` | ✅ Fresh May 18 (appended) | CC-Prome session report |
| `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` | ✅ Active | FSK Q1 branch-to-action rails |
| `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md` | ✅ Active | Bank expiry / Call Report triage rails |
| `PROME/AUTONOMY.md` | ✅ Salvaged from TOSCANINI | Tier 1/2/3 permission model + change log |
| `PROME/COMPLETION_SPEC.md` | ✅ Salvaged from TOSCANINI | LAST_COMPLETION.md format for sub-agent reports |
| `PROME/archive/TOSCANINI_2026-03/` | 📦 Archived | Retired Mar 26 governance framework |

---

## Pending Work

| Action | Pri | Status |
|---|---:|---|
| **Fleet scan Step 1 prototype** | ✅ Complete | v1 + v2 landed; v2 production-ready; ranking criteria captured in ORCHESTRAL_LAYER_DESIGN.md. |
| **Step 4 revival-proxy prototype (LIQUID)** | ✅ Complete | First Step 4 run produced revival packet + STATUS draft for LIQUID. Pattern validated. 4 v2-improvements deferred. |
| **TOSCANINI retirement + CLOSEOUT/BOOT cleanup** | ✅ Complete | TOSCANINI salvaged (AUTONOMY + COMPLETION_SPEC to PROME/, HUNTING distilled, rest archived). CLOSEOUT.md created. BOOT.md cleaned. |
| **HENRY revival proxy (Step 4 prototype #2)** | 🔴 Candidate | 31d self-commit stale; NVDA Tuesday 5/20 catalyst. Tests pattern generalization from plumbing → market-structure. |
| **BROCK revival proxy (Step 4 prototype #2 alt)** | 🔴 Candidate | 17d stale; APO sustained $130+ (zone change 🔴→🟢 today); FSK fresh-premium discussion blocked on refresh. |
| **Fold v3 fleet-scan feedback into ORCHESTRAL_LAYER_DESIGN.md** | 🟠 | 4 items: directional semantics, time-series pass-through, sweep-internal triage, closeout-authorization. ~15 min. |
| **LIQUID revival packet integration** | 🔵 | LIQUID's own task on next boot. Packet at `AGENTS/LIQUID/inbox/...prome-spawned.md`. Prome tracks only. |
| **Regional-bank Call Report / WAL triage** | 🔴 | REGINALD May 17: WAL 10-Q filed but not integrated; Schedule O / Table 16 cross-credit inventory test pending; MI3/FFIEC PDD status check due. (Carried forward.) |
| **Bank decision prompt** | 🔴 | Prome-owned synthesis: KRE/WAL/OZK/ZION/SSB cleanup, hold/roll/cut rails, live tape and option pricing required. |
| **BDC/private-credit decision prompt** | 🔴 | FSK Strong Bear allows fresh downside discussion. Needs live pricing and Will approval before trade. Blocked partly on BROCK revival. |
| **APO / ARES June premium review** | 🔴 | APO $134.07 (live tape); sustained above $130 watch; zone change 🔴→🟢 today. Premium under pressure. |
| **SAM FXY Tranche 2 decision** | 🔴 | FXY $57.80 today, below previously-forfeited $58.00-58.25 band. Will-direction required. |
| **HEARTBEAT.md tape refresh** | 🟠 | Today's dashboard numbers not yet propagated to HEARTBEAT (shared file; Will-approval gate). |

---

## Agent / Domain Notes

| Domain | Status | Note |
|---|---|---|
| WALTER / signal routing | 🟠 | Owns signal/news routing. May 17 closeout: BOARD 213; May 18 Iran + TIC callbacks. |
| REGINALD / banks | 🔴 | Persistent/managed — do not spawn. WAL Investor Day bearish increment; 10-Q/MI3 checks due. |
| BROCK / private credit | 🔴 | FSK validates stress; BROCK stale and has WALTER NDFI scope-correction REQ pending. |
| LIQUID | 🟠 | HY OAS benign is main falsification pressure; VIOLET flagged CCC/HY proximity. |
| HENRY / market structure | 🟠 | Stale and pre-NVDA 5/20 catalyst; tape/vol suppression follow-up remains relevant. |
| SAM / Japan | 🔴 | USD/JPY above red threshold; route via persistent SAM, not spawn. TIC March May 18 is live. |
| NEXUS | 🟠 | Stale but high-leverage if multiple domains converge; WALTER still wants revival. |
| PROME | 🔴 | Chief of staff: keep rails/state current, assign decision work, synthesize Will-ready prompts. |

---

## Rules of Engagement

- **No trade execution without Will approval.**
- **No fresh broad cascade short** while HY OAS <300 and VIX <20.
- **No broad bank-premium add** unless Call Reports/tape move to Bear / Strong Bear.
- **No rolling every losing June contract.** Prefer one or two higher-delta roll candidates only if confirmed.
- **Do not panic-sell Sep/Dec runway into green tape.**
- **Do not spawn CARL, REGINALD, OZK, SAM, RED, BRENT, or Claude Code Prome** (updated persistent-agent list per today's MEMORY.md edit).
- **WALTER routes signals/news; Prome tasks and synthesizes.**
- **Use explicit path staging only; never `git add .` or `git add -A`.**

---

## Next Best Action

Open with Will: decide between **HENRY revival proxy** (Step 4 prototype #2; NVDA Tuesday catalyst) vs **BROCK revival proxy** (Step 4 alt; APO/ARES decision pressure + FSK fresh-premium blocker) for the next revival run. Or **fold v3 fleet-scan feedback into ORCHESTRAL_LAYER_DESIGN.md first** before next revival (~15 min, locks in pattern improvements). Will-direction items on FXY Tranche 2, APO hold/roll, FSK fresh-premium are also live carries from FLEET_SCAN.md Section 7. Boot follows updated `PROME/BOOT.md` which now reads `PROME/FLEET_SCAN.md` at step 4.
