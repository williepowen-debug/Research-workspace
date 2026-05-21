# PROME STATUS.md
**Updated:** 2026-05-21 ~11:30 ET (post BROCK + REGINALD live closeouts; pre-BOND 1pm auction)

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
| `HEARTBEAT.md` | ⚠️ Stale (May 16 levels); BROCK + REGINALD posterior shifts NOT yet integrated | Scenario, levels, catalyst/position rails. Will-approval gate; fold post-auction. |
| `PROME/SCRATCH.md` | ✅ Fresh May 21 ~11:30 ET (post BROCK + REGINALD closeouts) | Ephemeral next-action state; entry point for next session |
| `PROME/FLEET_SCAN.md` | ⚠️ Fresh May 18 (v2 prototype); 3 days old | Live working surface — fleet situation report |
| `PROME/CLOSEOUT.md` | ✅ Fresh May 18 | Standardized session-end procedure |
| `PROME/BOOT.md` | ✅ Refreshed May 18 | TOSCANINI references cleaned; FLEET_SCAN + CLOSEOUT integrated |
| `PROME/ORCHESTRAL_LAYER_DESIGN.md` | ✅ Fresh May 19 (v3 brief spec folded) | Design + ranking rubric + revival-proxy v3 brief spec (9 items from LIQUID + HENRY prototypes) |
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
| **HENRY revival proxy (Step 4 #2)** | ✅ Complete 5/18 | Packet + STATUS draft + framing note in `AGENTS/HENRY/inbox/`. See SCRATCH. |
| **HENRY framing-precision note** | ✅ Complete 5/18 | New artifact type canonized. See SCRATCH §3 + `finding_framing_precision_overlay` memory. |
| **v3 brief spec folded into ORCHESTRAL_LAYER_DESIGN.md** | ✅ Complete 5/19 | 9 items consolidated under 7-section spec. See SCRATCH §4. |
| **BROCK revival proxy (Step 4 #3)** | ✅ Complete 5/19 | First exercise of v3 brief spec. Packet + STATUS draft in `AGENTS/BROCK/inbox/`. See SCRATCH §5. |
| **LIQUID revival packet integration** | ✅ Complete 5/19 | LIQUID booted, integrated, committed (commits b6d38b3d / 53019ce5 / 6d4d5408). End-to-end revival-proxy pattern validated. |
| **BOND teams-mode spawn experiment** | ✅ Complete 5/19 PM | First domain-agent teams-spawn. Boot handshake refined two-track frame + flagged 5/21 10Y reopening as second-leg test. |
| **BOND 5/20 20Y post-auction read** | ✅ Complete 5/20 PM | Teams-mode respawn. Verdict: no orange. Tail verified 0bp via ZH. Commit `4eb21894` pushed. Posterior shift: P(5/21 weak Leg 2) ~35-40% → ~20-25%. |
| **BOND background build-out (5 sub-agents)** | ✅ Complete 5/20-21 | WI playbook + auction history dataset (v1 + v2 enriched) + cross-tenor base-rates + escalation matrix backtest. 5 artifacts in `AGENTS/BOND/{analysis,data,research,proposals,inbox}/` untracked-by-design. See SCRATCH §Thread 2. |
| **BOND matrix v2 draft (Q1-Q5 walkthrough)** | ✅ Complete 5/21 | Teams-mode DRAFT-ONLY spawn. Proposal at `proposals/MATRIX_V2_DRAFT_prome-spawned.md`. Q1/Q2/Q3 RESOLVED, Q4 DEFERRED-with-conditional-rule, Q5 OPEN. See SCRATCH §Thread 4. |
| **BROCK live closeout (5/21)** | ✅ Complete 5/21 AM | 5 commits f47b9a30 → 1310ed42. FSK Q1 Strong Bear classified, position decisions formalized vs Fidelity PDF marks, WALTER NDFI REQ closed ($1.4T framework), inbox swept (6 items), TRADE.md May 1 framework SUPERSEDED, KB +5 / VX +2, LESSONS #15-16 added. See SCRATCH §Thread A. |
| **REGINALD live closeout (5/21)** | ✅ Complete 5/21 AM | Commit `f91ee9fb`. WAL V2.1→V2.2 shipped: B1 fired ($99M life-sci office walk-away), V4 new (Curley resignation), V2 inventory clean. Scenario reweight Bear-medium 30% dominant; EV $67.98; REG-25 55→75%. Q2 print late-July is next critical test. See SCRATCH §Thread B. |
| **APO / ARES June premium review** | ✅ Resolved 5/21 | BROCK: APO Dec hold (thesis vehicle), APO Jun + ARES Jun let-expire (residuals too small for ticket cost). See `AGENTS/BROCK/domain/sources/POSITION_DECISIONS_MAY21.md`. |
| **FSK fresh-premium discussion** | ✅ Resolved 5/21 | BROCK: no — KKR structurally long defense ($450M+ package, $11 tender = hard floor). Fresh PC premium would go to BIZD or ARCC Q2 if triggers fire. See `AGENTS/BROCK/domain/sources/FSK_Q1_READ_MAY21.md`. |
| **BDC/private-credit decision prompt** | ✅ Resolved 5/21 | BROCK: no fresh entry yet; HY OAS 286 widening from kill, cushion 26bps. Entry triggers documented (HY OAS <270 sustained, GCRED/OTF release in 30d, bank PC loss disclosure, sub-90¢ arms-length BDC loan). |
| **WAL Q1 10-Q integration** | ✅ Resolved 5/21 | REGINALD V2.2: B1 fired + V4 new + V2 clean. Bear-slow → Bear-medium speed. |
| **BOND 5/21 10Y auction read (dual-grade)** | 🔴 | Next event. Respawn ~12:30pm pre-auction + ~2pm post-auction. Dual-grade format mandatory — mechanically resolves Q4. |
| **v2 matrix deployment + Q5 decision** | 🔵 | Triggered by Q4 branch resolution after 5/21 10Y print. |
| **SAM FXY Tranche 2 decision** | 🔴 | FXY $57.80 below previously-forfeited $58.00-58.25 band. Will-direction required. |
| **HEARTBEAT.md refresh** | 🟠 | ~3-4d stale + BROCK V2.2 framework + REGINALD V2.2 scenario reweight + trap-clinching framing all owed. Will-approval gate; fold post-auction. |
| **V1 MI3 / FFIEC PDD status check** | 🟠 | REGINALD's V1-fast falsifier; window 5/14-16 passed without integration. REGINALD-owned next session. |
| **PROME design note: execution rails** | 🔵 | BROCK LESSONS #16 flagged — HYG roll Jun→Dec never executed during dark window because no mechanism existed. Same gap as May 15 ladder. Worth a Prome-side rail design pass. |
| **VIOLET revival proxy (Step 4 #4 candidate)** | 🔵 Deferred | Pushed behind BOND v2 deployment. |
| **HENRY revival packet integration** | 🔵 | HENRY's own task on next own boot. Packets untracked-by-design in HENRY inbox. Prome tracks only. |
| **Regional-bank Call Report / Bank decision prompt** | 🟠 | Reduced priority post-V2.2 (REGINALD owns WAL thesis state). REG-25 75% confidence locks Sep $77.5P/$70P as core REINFORCED-HOLD per V2.2 deltas. MI3/PDD still the V1-fast trigger. |

---

## Agent / Domain Notes

| Domain | Status | Note |
|---|---|---|
| WALTER / signal routing | 🟠 | Owns signal/news routing. NDFI REQ-BROCK-20260514 now closed by BROCK ($1.4T framework). |
| REGINALD / banks | 🔴 | Persistent/managed — do not spawn. WAL V2.2 shipped 5/21 (Bear-medium 30% dominant, EV $67.98). MI3/FFIEC PDD V1-fast falsifier still owed. Q2 print late-July is next critical test. |
| BROCK / private credit | 🔴 | 20-day dark window closed 5/21. Convergence 46/60 🔴🔴. Position decisions formalized. 2 new vectors (sponsor-bifurcation + duration-channel). Next: CDR Q1 5-cat pull + OTF release date confirmation. |
| LIQUID | 🟠 | Duration-channel reframe (5/18) now propagated through BROCK convergence matrix. 10Y +42bps over 20d window is the live transmission. |
| HENRY / market structure | 🟠 | Framing-precision discipline now canonized in BROCK STATUS (trap-clinching vs soft-kill). NVDA 5/20 read-through still owed; revival packet untracked in HENRY inbox. |
| SAM / Japan | 🔴 | FXY $57.80 below forfeit band; Will-direction owed. Route via persistent SAM, not spawn. |
| BOND | 🟠 | Teams-mode operational. Matrix v2 draft awaiting today's 1pm 10Y auction for Q4 branch resolution. 5 artifacts untracked-by-design in `AGENTS/BOND/`; BOND commits on next live boot. |
| NEXUS | 🟠 | Stale but high-leverage if multiple domains converge; WALTER still wants revival. |
| PROME | 🔴 | Chief of staff: keep rails/state current, assign decision work, synthesize Will-ready prompts. Execution-rails design note owed per BROCK LESSONS #16. |

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

**Primary (clock-driven):** Respawn BOND ~12:30 PM ET 5/21 for pre-auction tape pull; respawn ~2 PM ET for post-1pm verdict using mandatory dual-grade format (v1 + v2 simultaneously). The dual-grade output mechanically resolves Q4 (v2 matrix deployment timing). Branch rules + Q5 pairing in SCRATCH.

**Post-auction:** Propose HEARTBEAT refresh to Will folding in (a) today's tape, (b) BROCK trap-clinching framing + convergence 46/60, (c) REGINALD V2.2 scenario weights (Bear-medium 30% / EV $67.98), (d) BOND verdict + Q4 branch outcome.

**Carry (not clock-driven):** SAM FXY Tranche 2 needs Will-direction (FXY $57.80 below forfeit band). PROME execution-rails design note (LESSONS #16) for a maintenance pass when the auction window closes.
