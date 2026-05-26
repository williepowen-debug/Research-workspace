# PROME STATUS.md
**Updated:** 2026-05-26 ET (CC-Prome — closeout after 5/24-5/26 rolling session: HANDOFF archive + memory salvage + 6/18 v0.2 default-pass + push-train ride)

## Core State

**Regime:** BDC/private-credit credit/mark stress is confirmed, but public-credit contagion remains unconfirmed. Surface tape is still calm: HY OAS **276bps** and VIX **18.43**. Stress is concentrated in Brent/gas, USD/JPY, BIZD, WAL/KRE, and pending bank/BDC decision rails.

**Working model:** sponsor-supported private-credit/BDC deterioration + vol-suppressed public tape. Treat HY OAS <300 and VIX <20 as constraint against broad cascade adds, not as an all-clear.

---

## Latest Sync / Architecture State

| Item | Status | Note |
|---|---|---|
| GitHub sync | ✅ Synced at HEAD `02da0047` (SAM transition docs sync); 2 PROME commits from this session on origin (`045fdc59` archive + memory salvage; `c4680e51` v0.2 default-pass + approval packet — rebased via SAM push-train) | Push-train pattern 3rd concrete instance. |
| REGINALD update | ✅ Pulled | WAL Investor Day findings + May 17 closeout integrated into Prome state. |
| WALTER update | ✅ Pulled | Multi-session closeout confirms signal-routing ownership and May 18 callbacks. |
| Claude Code Prome scaffold | ✅ Present | Phase 2 complete; Phase 3 dry run still pending. |
| WALTER/Prome split | ✅ Codified | WALTER owns signal/news routing; Prome owns tasking, rails, and synthesis. |
| memory-audit-001 teams test | ✅ Complete | First bounded Agent Teams primitive run. Adversarial-pair pattern validated. 3 MEMORY.md entries + 2 in-place updates landed. META_EVAL at `PROME/scratch/teams_memory_audit_001/META_EVAL.md`. |
| Orchestral layer design | ✅ Captured + prototyped | Fleet scan + adversarial-pair top-N + revival proxies. Full design at `PROME/ORCHESTRAL_LAYER_DESIGN.md`; fleet-scan prototype live. |
| Execution-rails architecture | ✅ Created 5/23 | New system files: `PROME/EXECUTION_RAILS.md`, `PROME/ACTIVE_DECISIONS.md`, `PROME/DECISION_ARTIFACTS_INDEX.md`. Action-card template upgraded; 6/18 cluster promoted into wrapper card. |

---

## Active Decision Layer

| Artifact | Status | Purpose |
|---|---|---|
| `HEARTBEAT.md` | ⚠️ Stale (May 16 levels); BROCK + REGINALD posterior shifts NOT yet integrated | Scenario, levels, catalyst/position rails. Will-approval gate; fold post-auction. |
| `PROME/SCRATCH.md` | ✅ Fresh 5/26 (CC-Prome closeout — 5/24-5/26 rolling session) | Ephemeral next-action state; entry point for next session |
| `PROME/ACTIVE_DECISIONS.md` | ✅ Updated 5/25 (CC) | Current live rows: TLT `BROKER_PENDING` (Tue 5/27 open); 6/18 theta-killer cluster `PROPOSED` (Will-review pending on v0.2 packet). |
| `PROME/EXECUTION_RAILS.md` | ✅ New 5/23 | Canonical spec for state vocabulary, trigger/default/backstop rails, active-decision index, cluster rails, and promotion rules. |
| `PROME/DECISION_ARTIFACTS_INDEX.md` | ✅ New 5/23 | Inventory/taxonomy of action cards, trigger sets, decision memos, trade logs, and promotion rules. |
| `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` | ✅ Active 5/22 | TLT Jun18 $85P 2/1 split + Sep 19 $85P roll. State now explicit: `BROKER_PENDING` — Will approved 5/22; broker execution pending Tue 5/27 open. Conditional triggers C1–C5 live through 6/06 EOD. |
| `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` | ✅ `PROPOSED` 5/25 (CC) | Will-facing wrapper around `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` (v0.2). Default-pass applied 5/25 (BROCK + REGINALD silent at 5/24 EOD). Default: no trigger = let theta-killers expire. Next: Will review approval packet. |
| `PROME/action-cards/JUN18_V0.2_APPROVAL_PACKET_2026-05-25.md` | ✅ New 5/25 (CC) | Will-decision artifact for v0.2 adoption. Three default-picks PROME made: A1 HYG no pre-spec (BROCK validates at fire); A5 WAL $67.5P → Sep; A6 KRE → Aug 21. |
| `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` | ✅ v0.2 `PROPOSED` 5/25 (CC) | Source-of-truth for 6/18 cluster execution rail. Pending language stripped; default-picks locked; calibration tracking shows BROCK/REGINALD default-pass + HENRY routed to TLT card. |
| `PROME/archive/CC_HANDOFF_2026-05-pre-22.md` | ✅ New 5/24 (CC) | Archive of 5/17-5/21 CC HANDOFF entries (844 lines). Salvage manifest at top — 4 findings promoted to MEMORY before archive. |
| `FORGE/tools/market-data/README.md` | ✅ Fresh May 21 (Citation Convention section added) | Canonical FRED date-stamp convention reference |
| `FORGE/tools/market-data/dashboard.py` | ✅ Fresh May 21 (As-of column for FRED rows; `_date_stamp` helper) | Live tape; auto-displays observation date |
| `PROME/FLEET_SCAN.md` | ✅ Fresh 5/23 (OpenClaw scanner; paired with execution-rails landing) | Live working surface — fleet situation report |
| `PROME/CLOSEOUT.md` | ✅ Fresh May 18 | Standardized session-end procedure |
| `PROME/BOOT.md` | ✅ Refreshed May 18 | TOSCANINI references cleaned; FLEET_SCAN + CLOSEOUT integrated |
| `PROME/ORCHESTRAL_LAYER_DESIGN.md` | ✅ Fresh May 19 (v3 brief spec folded) | Design + ranking rubric + revival-proxy v3 brief spec (9 items from LIQUID + HENRY prototypes) |
| `PROME/TODAY.md` | ⚠️ Stale (May 17) | Superseded by FLEET_SCAN.md as live working surface |
| `PROME/HANDOFF.md` | ✅ Updated 5/24 (CC appended HAWK relocation entry) | Telegram-Prome surface; CC adds entries only when relocating misfiled OpenClaw content. |
| `PROME/CLAUDE_CODE_HANDOFF.md` | ✅ Fresh 5/26 (CC appended; 5/24-5/26 closeout) | CC-Prome session report. Archived entries 5/17-5/21 live in `archive/CC_HANDOFF_2026-05-pre-22.md`. |
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
| **HENRY teams-mode revival (5/21 PM)** | ✅ Complete 5/21 | Commit `36a8219b` (gap-fill: USD/JPY, PCE CONFIRMED, claims, PREDICTIONS.tsv). Boot integrated 3 revival packets, swept inbox 18→0, NVDA 5/20 read-through. UUID `abf1cd8d4ed725569` standing by. |
| **VIOLET teams-mode revival (5/21 PM)** | ✅ Complete 5/21 | Commit `1608fac2` + gap-fill `60b2e49c`. R12 SKEW>140 regime terminated; R11 clock running 5/28-6/02 prior 36%; FRED spot-check found BROCK numbers 2d stale. UUID `ad7350e8d26f70249` standing by. |
| **HENRY-VIOLET LIAISON channel** | ✅ Complete 5/21 | Auto-converged via VIOLET outbox file + HENRY pre-commit integration. ~90min in-session resolution. New finding: `finding_liaison_convergence_pattern` validated for live (not stale-stale) pairings. |
| **BOND 5/21 1pm auction read** | ✅ Complete with correction | Was actually 9Y8M TIPS reopening (CUSIP 91282CPU9), NOT nominal 10Y. Matrix Q4 dual-grade test reschedules to June 9-11 (CUSIP 91282CQQ7 reopening). BOND TIPS read commit `724169c3`: real-money showed up at 2.17% real, BTC 100th-pctile, demand-hole thesis qualitatively weakened. |
| **FRED publication-lag fix Phases 1-3** | ✅ Complete 5/21 | Commit `ded870e0`: README convention + BOOT.md pointer + dashboard.py As-of column + 4 agent SIGs (BROCK/LIQUID/REGINALD/HENRY inboxes, untracked-by-design). Phase 4 (HEARTBEAT propagation) + Phase 5 (compliance audit) deferred. |
| **APO / ARES June premium review** | ✅ Resolved 5/21 | BROCK: APO Dec hold, APO Jun + ARES Jun let-expire. |
| **FSK fresh-premium discussion** | ✅ Resolved 5/21 | BROCK: no; KKR structurally long defense. |
| **BDC/private-credit decision prompt** | ✅ Resolved 5/21 | BROCK: no fresh entry yet; entry triggers documented. |
| **WAL Q1 10-Q integration** | ✅ Resolved 5/21 | REGINALD V2.2. |
| **Matrix Q4 deployment timing decision** | 🔵 Deferred to June 9-11 | TIPS-not-nominal correction. BOND's pre-auction baseline + sentiment-context lens apply to June test. Treasury announcement ~June 3-5. |
| **Q5 decision (v2-native backtest re-run)** | 🔵 Pairs with Q4 | Same June 9-11 window. |
| **BOND-TIPS cross-flag to BROCK** | ✅ Filed 5/21 ~14:15 | SIG in BROCK inbox flagging duration-channel vector re-weight question. Untracked-by-design; BROCK integrates next boot. |
| **BOND-TIPS cross-flag to HENRY** | ✅ Integrated 5/21 ~14:20 | HENRY commit `526d3586`: R11 trigger #6 imminence SOFTENED ("long end clearing demand at price"); breakeven decomposition added as 3rd independent Fed-can't-cut confirmation (PCE + duration + breakeven all triangulating). 2 new MEMORY findings. |
| **SAM FXY Tranche 2 decision** | ✅ Executed 5/21 ~12:46 | SAM Tranche 2 executed at $57.66, 5 shares (commit `fb539597`). Total FXY now 13 shares + 1 Jun-18 $58C. Discovered post-closeout via cross-agent verification of SAM outbox-to-PROME signal. Next SAM Will-pending: Sep-18 $60C × 5-10 contracts (post-CPI cheaper entry). |
| **FORGE rehab Steps 1-4** | ✅ Done 5/21 by CC | Commit `ec7e8ad9` (Will-authorized). STATUS reconciled against Fidelity CSV (5/21 14:03 ET) + SAM v1.4. Position tables rewritten (KRE 19 / WAL 8 / TLT 7 / APO 2 / OZK 7 / Other Puts 14 / Longs 8). Immediate Actions rebuilt around 6/18 expiry-cluster decisions. PORTFOLIO + ACTIVE_TRADES marked SUPERSEDED. JOURNAL gap entry for Feb 27 → May 21 (~22 equity closures + 6 expirations + 4 rolls + ~13 new opens). Recon worksheet: `FORGE/scratch/REHAB_RECON_2026-05-21.md`. **Open Will-decisions surfaced:** 6/18 theta-killer cluster dispositions (HYG×8/EGBN/AAL×2/WAL×3/KRE), TLT $88P May 15 disposition unknown (was +100% pending), FXY $58C reconciliation (not in CSV), APD new long thesis tag, VIOLET 4/15 VIX/SKEW trade overdue. |
| **Execution-rails architecture v1** | ✅ Created 5/23 by OpenClaw | Files created/updated: `EXECUTION_RAILS.md`, `ACTIVE_DECISIONS.md`, `DECISION_ARTIFACTS_INDEX.md`, `DECISION_FLOW.md`, action-card template, TLT card. Core rule: `WILL_APPROVED` ≠ execution; `BROKER_PENDING` = live risk. |
| **6/18 trigger set v0.1 + 3 calibration SIGs** | 🟠 Partial → promoted 5/23 | SIGs filed to BROCK (HY OAS R2/R4 + HYG roll target + sub-90¢/bank-PC language), REGINALD (KRE bear-line + WAL break-zone + WAL/KRE/EGBN roll targets), HENRY (VIX R1 + TLT decision packet). HENRY replied 5/22 → TLT action card. BROCK + REGINALD still owe replies; deadline 2026-05-24 EOD default-pass. Promoted into `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` + `ACTIVE_DECISIONS.md`; next = v0.2 approval packet. |
| **TLT $85P decision (Jun18 cluster sub-leg)** | 🔴 Approved, broker-exec pending | Will [Approve] stamped 5/22 ~15:00 ET on action card. Plan: SELL 3 × TLT Jun18 $85P / BUY 1 × TLT **Sep 19** $85P (HENRY-recommended monthly, not Sep 30 quarterly). Computer crashed before broker action. Memorial Day Monday 5/25 closed. Earliest exec Tue 5/27 open. TRADE_DECISIONS.md logged; Outcome: Pending. Conditional triggers C1–C5 (TLT $85.50 / $85.20-grind / <$82 / 6/06 backstop / HY-OAS-or-R11 substance break) live through 6/06 EOD. |
| **HAWK armed-pause consolidation** | ✅ Done + pushed 5/22 by OpenClaw (commit `888a5e9d`) | HAWK frame: **armed pause / controlled grind**; C 57% / D 35% / B 8%; Hormuz ~10/day vs 125-140 normal; Barakah direct-Iran attribution unconfirmed; old zero-crossing and uninsurable language superseded. May 23 close re-check + May 28 IRAN_WAR boundary are next gates. |
| **CARL 5/22 inbox-processing crash recovery** | 🟠 Held back — CARL owns | CARL was mid-session at crash. 5 inbox items moved to `processed/` (dispositions file written), ROADMAP/SCRATCH/BOARD_LOG dirty, STATUS atomic-rename interrupted → `STATUS.md.tmp.542915.8a61cc80397b` leaked. Tmp diff = one Gas Pump row update ($4.564 May 21 / all-50-states ≥$4 per SIG-W-20260521-030). CARL on next boot: finish row patch, clean own tmp, commit. PROME did NOT touch. |
| **WALTER bull-counter calibration** | ✅ Responded 5/21 ~14:45 | WALTER filed `SIG-WALTER-PROME-20260521-bull-counter-tier-rec.md`: both Tier-2; forced steelman ("regime may LAST not BREAK"). Folded into HEARTBEAT regime line. |
| **HEARTBEAT.md refresh** | ✅ Done 5/21 by CC | Path B refresh shipped 15:55 (`8f3fa922`); surgical fix 16:25 (`a0aa4232`). 98→38 lines. Refresh-cadence design question remains open (now self-referentially listed as Blocking on Will inside HEARTBEAT). |
| **MEMORY.md sweep** | ✅ Done 5/21 by CC | 2 new entries + 3 footnotes (`d60616cc`). Will-authorized cross-surface boundary. |
| **PROME/COMM/ mailbox integration** | ✅ Done 5/21 by CC | BOOT.md step 7 inserted (`28dd3e13`). First two ACKs filed: bond-cusip-caveat (completed; cross-surface convergence finding) + comm-mailbox-live (acknowledged). |
| **V1 MI3 / FFIEC PDD status check** | 🟠 | REGINALD V1-fast falsifier; window 5/14-16 passed. REGINALD-owned next session. |
| **PROME design note: execution rails** | ✅ Created 5/23 | BROCK LESSONS #16 converted into architecture: `EXECUTION_RAILS.md` + `ACTIVE_DECISIONS.md` + artifact index + 6/18 wrapper. Next test is live 6/18 cluster end-to-end. |
| **Regional-bank Call Report / Bank decision prompt** | 🟠 | Reduced priority post-V2.2. MI3/PDD remains V1-fast trigger. |

---

## Agent / Domain Notes

| Domain | Status | Note |
|---|---|---|
| WALTER / signal routing | 🟠 | Owns signal/news routing. NDFI REQ closed by BROCK. **Bull-counter calibration SIG awaiting WALTER boot** for SIG-006/007 tier-ranking against 4-agent convergence. |
| REGINALD / banks | 🔴 | Persistent/managed — do not spawn. WAL V2.2 shipped 5/21 (Bear-medium 30% dominant, EV $67.98). MI3/FFIEC PDD V1-fast falsifier still owed. Q2 print late-July is next critical test. FRED-citation SIG in inbox. |
| BROCK / private credit | 🔴 | 20-day dark window closed 5/21. Convergence 46/60 🔴🔴. Position decisions formalized. 2 new vectors (sponsor-bifurcation + duration-channel). **BOND-TIPS cross-flag in inbox raises duration-vector re-weight question.** FRED-citation SIG also in inbox. |
| LIQUID | 🟠 | Duration-channel reframe (5/18) now propagated through BROCK convergence matrix. HAWK routed OFAC/IRGC/PGSA toll-payment risk as legal/funding choke point. |
| HENRY / market structure | 🟠 | Teams-mode revival 5/21 (UUID `abf1cd8d4ed725569`). NVDA absorbed cleanly; macro/structure tape supports Stage-2-late. HEN-27 PCE CONFIRMED. **5/22 replied to TLT calibration SIG** (new teams UUID `a9200162cddd73274`) with verdicts on 2/1 split + Sep $85P + 6/06 backstop + $85.50+velocity trigger — drove TLT action card construction. Reply lives at `AGENTS/HENRY/outbox/REPLY-PROME-2026-05-22-tlt-decision.md` (untracked-by-design; HENRY commits on next boot). |
| VIOLET / vol/SKEW | 🟠 | **Teams-mode revival complete 5/21** (UUID `ad7350e8d26f70249`). Stage 2-late confirmed; R12 SKEW>140 regime terminated; R11 clock running 5/28-6/02 prior 36%. 7-trigger Stage 3 watch list canonized. Standing by — context 114K/200K. |
| SAM / Japan | 🟠 | Tranche 2 executed 5/21 at $57.66; v1.4 thesis bump shipped (`fb539597` / `2c079ab8` / `a5852d99`). Total FXY 13 shares + Jun-18 $58C. Next SAM Will-pending: Sep-18 $60C × 5-10 contracts. Filed outbox-to-PROME signal asking for FORGE rehab (workflow note: signal lived in his outbox, not PROME/inbox — discovery gap closed via Will-prompted scan). |
| BOND | 🟠 | **Teams-mode operational, persistent** (UUID `ad32628b028661b70`). Today's auction was TIPS not nominal; matrix Q4 deferred to June 9-11 (CUSIP 91282CQQ7 reopening). TIPS read commit `724169c3` local-only (not yet pushed). Standing by. Calendar update: re-check Treasury announcement June 3-5. |
| NEXUS | 🟠 | May 21 divergence reset fresh. HAWK routed armed-pause / controlled-grind frame; next synthesis should reconcile Iran bifurcation with Stage-2-late divergence. |
| PROME | 🔴 | Chief of staff: keep rails/state current, assign decision work, synthesize Will-ready prompts. Execution-rails v1 now exists; use `ACTIVE_DECISIONS.md` at boot before new research. Next proof test = 6/18 cluster v0.2 + TLT broker-pending closeout. |

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

**Current posture (5/26 closeout):** 5/24-5/26 rolling CC session shipped 3 landings (HANDOFF archive + memory salvage; 6/18 v0.2 default-pass + approval packet; push-train ride + tape verify). State clean; ready for fresh session boot. Tomorrow's TLT broker window is the next clock-driven event.

**Immediate next action (likely next CC-Prome session):**
1. 🔴 **Tue 5/27 ~9:30 ET — TLT pre-open packet for Will.** Live tape pull, conditional-trigger read (C1 $85.50 / C2 $85.20×2 / C3 $82 / C5 substance), broker-ready order summary. Per 5/26 dashboard TLT $85.27 → C2 fires if 5/27 closes ≥ $85.20. After fills: FORGE/STATUS TLT row update + TRADE_DECISIONS fills log + action card → `COMPLETED`.
2. 🟠 **Wed 5/27 PM — Sumitomo Life FY2025 ESR (SAM-owned).** If confirms Nippon/Meiji pattern, Channel 1 v1.5 downgrade warranted. PROME-side: fold into HEARTBEAT if Channel 1 weakens further.
3. 🟠 **v0.2 Will review** — `PROME/action-cards/JUN18_V0.2_APPROVAL_PACKET_2026-05-25.md` sitting in Will's queue. No clock; could pair with TLT-execution review.

**Live Will-decision carries:**
- TLT $85P × 3 → 2/1 split + Sep 19 $85P roll — **approved 5/22, broker exec Tue 5/27**.
- 6/18 cluster v0.2 — `PROPOSED`, awaiting Will review.
- SAM Sep-18 $60C × 5-10 contracts — pending post-CPI cheaper entry, deferred until post-Sumitomo.
- FXY $58C reconciliation.
- TLT $88P May 15 disposition unknown.
- VIOLET 4/15 VIX/SKEW trade adjudication — 60d window closes ~6/12.
- APD long thesis tag unassigned.
- TODAY.md / CALENDAR.md broader refresh; HEARTBEAT cadence design open.

**Pre-6/16 FOMC:** v0.2 approval still needed for daily monitor activation. All R1-R4 triggers MORE benign than at v0.2 ship (5/26 tape).
