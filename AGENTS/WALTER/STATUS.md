# WALTER STATUS

**Updated:** 2026-09-03 ~22:1x ET (Thu) — **TIER-2 FULL closeout on Will's *"lets close out"*, after a long routing session (`walter-e5`, ~15:0x → ~22:1x ET).** **12 dispatches · 5 errata on live BOARD rows · 4 lifecycle tags · 16 inbox packets consumed · 3 batch manifests all closed (BM-20260903-01 2/2 · -02 16/16) · 0 kills · 0 verify-spawns.** BOARD **867 → 879**. **Two doorbells FIRED AND CONVERTED** (NEXUS + LIQUID on the PJM signal, gate `P0.L1.L2.L3a`) — the **first v3-form passes** in the ledger; PROME spawned both, deviating from the recommended combined touch in the direction that makes each leg independently measurable. **Staleness sweep run** (16d overdue): 199 candidates, 4 tagged, and its main finding is that its own P2 pattern is mostly false positives. **Boot 6b repointed** to RED's generated scan view (6,840 B vs 48,989 B canon). REGISTRY 6 rows (BROCK · LIQUID · LABOR · NEXUS · TERRY · DAEDALUS). *(Prior lead, 2026-09-01 ~22:2x ET Tier-2 `walter-e5`:)* PROME `2026-09-01b` CONSUMED → `BOARD_CONSUMPTION_SPEC` v0.22 (leg 3b SELF-NORMALISING with DECLARED parameters, ≥7d RETIRED, soak review 9/30); 2 dispatches (`-015` LABOR grade → CARL · `-016` MOF ¥15,399.3B → LIQUID); first `DOORBELL_LOG` row under the v3 form (LIQUID, L3-FAIL).

> 📌 **This `**Updated:**` line was ADDED 2026-08-31 and its absence was a real defect, not cosmetics.** Every other desk carries one; WALTER did not, so `walter_doctor`'s own `registry_self_lag` check reported *"no parseable Updated header — self-registry lag unchecked."* ⇒ **the desk that audits every other desk's staleness was the one desk whose own staleness could not be measured.** Found by running the LOW items instead of skimming them. **Do not remove it, and do not let a regeneration eat it** — that is exactly how `## BOTTOM LINE

**WALTER is GREEN, the desk is CURRENT for the first time in three days, and the theater is still HOT.** The inbox went 16 → 0 and the BOARD carries all of it: a **live PJM capacity emergency** (DOE §202(c) Order 202-26-41 running to **9/8**, EEA-1 three straight days, RT LMP $1,868.78/MWh at 99.85% energy — WATT's P1 fired 2→5, cascade did NOT trip), **USD/JPY 156.14** with SAM's 2% bar ARMED-not-graded on an unregistered basis, a **LIQUID trigger that has sat FIRED since ~June 3** and needs one line from BROCK, and the **route-around census: 10 desks, 14 ROUTE-AROUND + 4 rows naming a router retired 64 days.**

🔑 **THE PATTERN OF THE DAY, and it is worth more than any single dispatch: THREE DESKS INDEPENDENTLY FOUND A BROKEN ROUTE IN THEIR OWN CANON INSIDE 48h — LIQUID, OTTO and SAM — AND ALL THREE FOUND IT THE SAME WAY: BY AUDITING RULES THAT HAD NEVER FIRED.** LIQUID's `KB-LIQ-124` is the statement of it: *a defect inside a rule whose consequence is currently inoperative generates no evidence of itself, because the suppressor ends exactly when the rule starts mattering — so the defect and its first consequence arrive in the same event.* **OTTO's first exercise would have been a 5th fraud case at 🔴 URGENT.** ⇒ **The DAEDALUS census number is a FLOOR, not a total**, and the generalisable instruction is *audit the rules that are NOT firing.*

⚠️ **AND THE UNREGISTERED-BASIS CLASS HIT THREE DIFFERENT DESKS IN TWO DAYS, WITH OPPOSITE CONSEQUENCES: `RED-FT-10` is `>=` (non-strict — an exact 150.00 FIRES) · `CREED-T-01a` is `>` (strict — an exact 12.00 does NOT) · SAM's 2% gap has NO registered basis and the two readings disagree (2.01% fires / 1.90% does not). Same shape, opposite verdicts, and NONE of it is legible from the four-column summary table six desks actually hold.**

**Near-trigger board, every level with its own print date:** **RED-FT-12** HY OAS <260 s=3 → **266 [9/2 FRED, T+1]**, 6bp out, count 0 · **RED-FT-10** SKEW ≥150 → **144.12 [9/2, CBOE publisher of record]**, 5.88 out, count 0 — ⚠️ yfinance printed **150.63 [9/3]** but CBOE has not published 9/3, and **sustain is 4**, so even on confirmation that is 1-of-4 · **GATE-TERRY-ROLL70-EXIT** WAL ≥$81.90 ×3 → **$81.00 [9/3]**, $0.90 out, 0-of-3 · **CREED-T-01a** office CMBS DQ >12 → **exactly 12.00 [Trepp Aug]**, NOT FIRED. ⛔ **Kill-on-sight: *"FT-10 fired"* · *"SKEW crossed 150"* · *"WATT-02 trending MISS"* · the BCRED *"$1.7bn"* · *"FT-10 0.77 below"*.**

🔴 **TELEGRAM IS HALF-BROKEN AND THE BROKEN HALF IS THE SILENT ONE: OUTBOUND WORKS (confirmed twice, from two different sessions), INBOUND DOES NOT.** Will's 6:39 PM reply never reached the session; it was only discovered because he screenshotted it into the terminal. The Bot API exposes no history, so a missed inbound message is GONE, not queued. **Until fixed, assume WALTER does not receive what Will sends there.** *(The 9/1 note "Telegram MCP failed to connect" was the wrong description — one direction works fine.)*

## MISSION

Single entry point for external information into the agent network. WALTER filters, classifies, and routes signals — and is evolving toward maintaining a Common Operating Picture (COP) that gives all agents and Will shared situational awareness without inbox silos.

**I am not an analyst.** I don't evaluate thesis correctness. I decide: Does this information reach the network? Who gets it? How urgently? And increasingly: What does the full picture look like right now?

---

## STATE POINTERS

- **Live ops state** → header paragraph above (BOARD count, today's dispatches/kills/verify-spawns, push state, cluster updates, routing pressure flags).
- **Design + infra completeness** → `design/STATE.md` (specs at version, scaffolding files, active policies, COP/BOARD status, agent rollouts).
- **Filter posture (current mode + safety net triggers)** → FILTER POSTURE section below — **RESTORED 2026-08-20 after a 28-day absence; this pointer resolved to nothing from 7/23 to 8/20.**
- **Network awareness (per-agent state)** → NETWORK AWARENESS section below + REGISTRY.tsv (canonical).
- **Recent session activity** → **[`SESSION_LOG.md`](SESSION_LOG.md) — the ONLY tier.** *(Corrected 2026-08-20: this line advertised an in-STATUS "last 5" table that the 2026-07-23 regeneration deleted 28 days ago. See the SESSION LOG section at the foot of this file.)*
- **Last session closeout** → `LAST_COMPLETION.md`.
- **Cross-session feedback / findings** → `MEMORY.md`.

---

## NETWORK AWARENESS

**Canonical agent directory:** `REGISTRY.tsv` — refreshed at every boot per spawn protocol step 8 (read other agents' STATUS file headers, update Status / Updated / Focus columns). Status / Key Concern columns of the prior in-STATUS table just duplicated REGISTRY and went stale; dropped in Pass 4 of STATUS.md refactor (2026-05-05). The "today's routing + stale agents" view below regenerates each closeout from the freshly-refreshed REGISTRY.



*(Prior: 2026-08-10 Tier-2 — 3 rows [HAWK · OSPREY · FALCON], all three returning from dark periods INSIDE Will's war-theaters forum the same day; standing caveat that all three were STILL COMMITTING when the rows were written.)* *(Earlier: 8/03 5 rows+self · 8/02 6 rows · 7/31 19 rows clearing 15 MEDs · 7/23 27-row broad refresh — details in git history.)*

*Prior refresh — 2026-07-23 Tier-2 BROAD REFRESH, 27 rows: Status/Updated/Focus regenerated from agents' own STATUS headers; cleared the multi-week deferral + all 22 doctor `registry_lag` MEDs. Material row changes then: FALCON → 🔴 (GATE-FALCON-001 leg-1 FIRED 7/23) · LIQUID → 🟠 (duration regime re-established both legs 7/23) · OZK → 🟠 (Q2 cycle CLOSED benign) · BRENT 🔴 ($100 threshold #1) · SAM/CORAL/LABOR/MIDAS/OSPREY refreshed to 7/23-same-day state. Prior refresh 2026-07-21 (WALTER row only). fs-scan clean (no unregistered dirs).

### 🚨 IRAN-WAR ANCHOR

**Canonical anchor file:** [`anchors/IRAN_WAR.md`](anchors/IRAN_WAR.md) — read at every boot. Pulled out of STATUS.md on 2026-05-04 (Pass 3 of refactor) so it can be updated without touching STATUS, with explicit verified-as-of stamp + re-verify trigger.

**🔴 THE IRAN STATE IS NOT RESTATED HERE — READ [`anchors/IRAN_WAR.md`](anchors/IRAN_WAR.md).** This section's standing position is *stop restating, don't restate more often*; the 8/10 self-catch found it headlining week-old state, and the derived paragraphs were rotated verbatim to `SESSION_LOG.md` on 8/20.

🔴 **THE ANCHOR IS THREE FILES (split ②, 2026-08-30 · split ③, 2026-08-31) — READ THE RIGHT ONE:** **`IRAN_WAR.md`** = current state + the gates + re-verify ladder, **the boot read** (⛔ no byte figure here — it crossed its trigger and was split AGAIN on 9/1; measure with `reads_check`) (it was 263,371 B = 809% of budget, read at ~4%, which shipped two operator-facing defects; split ② took it to 18,590 B and ADDENDUM #22 alone pushed it back to 26,555 B = 82%, over its own ≥75% re-rotation trigger, in ONE session). **`IRAN_WAR_GUARDS.md`** **55,415 B = the 23-block** standing triage / kill-on-sight corpus, **read PRE-DISPATCH on any Iran-cluster signal, never at boot** — the anchor carries a named inventory of all 23 so no reader can be unaware of it. **`IRAN_WAR_HISTORY.md`** **346,908 B** = dated narrative, **grep-on-demand.** 📌 **Split ③ moved ADDENDUM #21, the superseded 7/10 ladder and a STALE 8/26 lead that CONTRADICTED the file's own current addendum; conservation proved by `split_verify.py` exit 0.**

🔴 **RE-VERIFIED 2026-09-01T21:45Z (ADDENDUM #23) on the anchor's own trigger — a SECOND US strike wave.** Two waves (8/30 Larak · 9/1 multi-target), each answered by Iranian missiles at Jordan; two VLCCs (*Sidr*, *Senegal Prosperity*) hit by projectiles off Khasab 8/31, crews safe; the IRGC mine claim FALSE (CENTCOM). GATE 1 FIRM-NEGATIVE · GATE 2 NOT FIRED · losses 1 · next ~**9/7** or on a THIRD wave / named oil asset / mine detonation / US accept-reject. **"Ceasefire" remains kill-on-sight.** `[[finding_seeded_selfsweep_secondary_surface_rot]]`


### 🤝 Active LIAISON channels + countdowns (manifest)

*Paired-agent architectural-alignment dialogs. Each active channel = file at `AGENTS/{TARGET}/handoff_WALTER/LIAISON.md` (generic glob `find AGENTS/*/handoff_WALTER -name LIAISON.md`). Read at boot via spawn-protocol step 9 (conditional on new turns since last boot). Auto-flag rule: status flips ACTIVE → DORMANT after 30 days without a turn at next closeout — manifest-staleness guard. Calibration trigger: **14-day calendar primary** (next-trigger column), **N=20 BOARD dispositions early-fire** (whichever first). Calendar dates are observable; counts require maintenance.*

| Channel | Last_Turn_Date | Status | Next_Trigger | Notes |
|---------|----------------|--------|--------------|-------|
| WALTER ↔ CARL | 2026-05-06 (Turn 7 closed) | **DORMANT (auto-flagged 6/20 — 45d no turn, >30d rule)** | Re-open: refresh the calibration-cycle-1 ask (CARL post-hoc-conf delta → WALTER threshold tuning) when CARL next active | 7-turn dialog 2026-05-05 → 06; architectural thread converged. Output: 4 v0.8 spec proposals + ROUTING_TABLE v0.6 override + Post_Hoc_Conf shipped + scheduled-scan budget pending Will sign-off + design/CROSS_REFS/CARL.md cache spec + DATA_RELEASE_CALENDAR.md (CARL self-task ETA this week). Cycle 1 trigger fires CARL post-hoc-conf delta summary → WALTER threshold tuning. |
| WALTER ↔ BRENT | **2026-06-06 (formally CLOSED — stamp + git mv to `handoff_WALTER/CLOSED/` per 6/6 walkthrough decision #4)** | **CLOSED** | Re-open trigger: BURST_WINDOW state-change OR Phase-2 structural break | **5-turn dialog 2026-05-05 → 06; architectural thread converged in 4 turns** (substrate prep saved 2-3 turns vs CARL). Output: 3-way JOINT_PROPOSAL cosign on FORMAT_SPEC v0.8 (9-value enum incl. `lng_substitution`) + BRENT-IMMEDIATE 8-row threshold-cross dispatch list + BURST_WINDOW state machine + `energy_transmission` (10-val) + `regime_state` (5-val) v0.9 candidates + BRENT-pattern BOARD_CONSUMPTION (energy-domain template w/ BRENT_ORIGIN class) + 47-signal back-disposition (5 Post_Hoc_Conf deltas: SIG-019-021 0.65→0.55, SIG-019-027 0.50→0.40, SIG-019-030 0.50→0.85 retro-uplift, SIG-024-008 0.80→0.70, SIG-005-009 0.85→0.75) + thesis v2.0 + FLOW.tsv outbound expansion. BRENT shipped 6 commits in parallel with WALTER architectural drafting. |
| WALTER ↔ RED | **2026-06-06 (Turn 7 WALTER re-engagement sent — light substance + 2 open questions per walkthrough decision #4)** | **CONVERGED / DORMANT (7/3)** | Turn 7's 4 substance items all aged out — the 6/4 inaugural RED-FT fires + overdue-detection + peak per-session-vs-day-aggregate all SHIPPED into CHECKLIST v0.12; the VIX<16 watch is 4wk-stale (RED-FT-06, still unfired). Only residue = the low-priority calibration-cycle-1 retro cadence Q; RED active-since (6/10, 6/23) w/o prioritizing it. Re-open ONLY to run that retro if/when wanted. (An upside VIX-spike trigger is a real small RED-registry gap but low-priority w/ vol compressed ~16.) | **6-turn dialog 2026-05-06 (architectural thread converged Turn 5; Turn 6 = parallel-drafting close-loop, RED 21:00 UTC stamp).** RED revived overnight w/ 6 Session-8 commits + Session 9 closeout `254f6e40`; opened LIAISON 10:08 EDT before Will paged WALTER 14:18 UTC. Output: 2-way RED+WALTER joint-proposal §1+§4+§6+§7 (RED `e6477450`) + §2+§3+§5 (WALTER) all committed-in-tree. **5-of-5 batch APPROVED end-to-end + IMPLEMENTED:** RED §4.3 CLAUDE.md boot-step 1.5 b1-b4 + §4.4 MEMORY entry committed `b1ed0420` 11:52 EDT; WALTER §2 ledger `registry/FALSIFICATION_FIRED_LOG.tsv` + spawn-protocol step 6b + §3 ROUTING_TABLE v0.7 + CHECKLIST v0.10 + §5 V0_9_STACK.md tracker shipped this session 16:00-16:30 UTC. 6 RED deliverables (FALSIFICATION_TRIGGERS.tsv 7-trig registry + CHALLENGES.tsv col-11 BOARD_Refs + 5 backfilled + SCHEMA bumps + bifurcation classification 22 sigs 8H/9R/5both 64% lean structural + handoff_WALTER/README). RED Turn 6 surfaced data-correction: effective N=6 not 9 after Q15 staleness filter (RED §1.4 self-corrected). 97%-routing-target reframe = highest-leverage finding (RED in to/info on 107/110 BOARD signals; gap was RED-side consumption not WALTER-side dispatch). Repo-root stitch `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` next-session WALTER pickup. |
| WALTER ↔ NEXUS | n/a | PENDING — **UNBLOCKED 6/8** | NEXUS ACTIVE again (6/8 hygiene + brief-integration session) — revival blocker gone. Open when REQ-NEXUS cluster-classification ask is refreshed (the 5/5 REQ content is 36d stale; re-scope before opening). | High-leverage — NEXUS owns cluster-narrative authority. OC-side, file-mediated. |
| WALTER ↔ REGINALD | **2026-06-06 (Turn 6 WALTER re-engagement sent per walkthrough decision #4)** | **CLOSED (7/3 — REGINALD archived from their side)** | Channel archived by REGINALD → `AGENTS/REGINALD/archive/handoff_WALTER/`; nothing to await. Re-open only on a fresh cross-agent architectural need. | 5-turn convergence locked 5/10-11; THRESHOLDS.tsv + BOARD_LOG + By Convergence v0.9 all shipped. **7/3 correction: REGINALD archived the channel from their side — the "awaiting Turn 7" state was stale; the Turn-7 calibration retro is effectively dropped.** |
| WALTER ↔ HENRY | n/a | PENDING | Post-RED + REGINALD | OC-side, file-mediated relay works. Equities/VIX/Fed expectations + POSITIONING_VALUATION cluster owner. CARL Turn 5 ranked 2nd post-RED. |
| WALTER ↔ BROCK | n/a | PENDING | Mid-priority | OC-side. PC-stress cluster owner (Blue Owl, Apollo, OBDC, BDC stress). Cross-feed with REGINALD + LIQUID. |

### Today's routing + stale agents (regenerated each closeout from REGISTRY)

**🔄 REGENERATED 2026-09-03 ~22:1x ET (Tier-2) from the session-refreshed REGISTRY — 6 rows moved (BROCK · LIQUID · LABOR · NEXUS · TERRY · DAEDALUS); every `registry_lag` LOW cleared.**

**As-of Thu 9/3 ~22:1x ET — 12 dispatches / 0 kills / 0 verify-spawns (BM-20260903-01 2/2 · BM-20260903-02 16/16):** `-001` IMMEDIATE → VIOLET, RED (SKEW 150.63 NOT gradeable) · `-002` PRIORITY → REGINALD, TERRY (WAL $81.00, exit guard 0.90 out) · `-003` IMMEDIATE → NEXUS, LIQUID (live PJM emergency) · `-004` PRIORITY → HENRY (USD/JPY 156.14) · `-005` PRIORITY → BROCK (LIQUID trigger fired since June) · `-006` PRIORITY → REGINALD (office DQ exactly 12.00) · `-007`…`-012` info-only (OTTO ×2, BCRED filing type, gold attribution, Bernstein re-score, route-around census). **47 handoffs across 18 desks, all reconciled `delivered`.** CARL/RED/PROME/TERRY exempt per §3.5.

**Agent states at close (basis: `ListAgents` + `ORCH_LOG` + doctor):** **LIVE** — TERRY (`terry-0f`, idle), BROCK (`brock-46`, idle), DAEDALUS (`daedalus-8b`, busy), PROME (`prome-c8`, busy). **IN-FLIGHT** — none open; NEXUS and LIQUID were spawned on this desk's doorbell at 19:4x–19:5x and **both closed their drains** (NEXUS 7/7 consumed ~20:1x; LIQUID 11 items ~20:3x). **DARK and carrying ACTION — only 4 unconsumed >2d across 4 agents, 1 ACTION / 3 INFO, oldest 46d** (AEOLUS 1A · DEWEY · SHADE · FLG) [basis: `delivery_log.timestamp_routed`, 2 on mtime].

🔑 **THAT BACKLOG FIGURE IS 149 → 4 IN TWO DAYS AND THE CAUSE MUST TRAVEL WITH IT: it is PROME's 9/2–9/3 orchestration wave draining ~15 desks, NOT a change in this desk's routing.** Reporting a 97% fall without its cause would read as an improvement nobody made — the same discipline the 9/1 close applied to the 4× weekend-aging jump in the other direction. `[[finding_window_start_at_an_extremum_inverts_the_move]]`

✅ **Doorbells: 2 FIRED, 2 CONVERTED, 2 logged L3-FAIL.** NEXUS + LIQUID passed on **L3a DECAY, not cadence** — both dark only 1d, but the DOE order lapses 9/8 inside their own p75 intervals (8d / 13d). **First v3-form PASSES in the ledger** (the 9/1 LIQUID row was a v3 refusal), which is what the 9/30 soak review needed. ⚠️ **PROME deviated from the recommendation — separate spawns with whole-inbox drains rather than the recommended combined touch — and it went the useful way:** the 9/1 BRENT leg had to carry `drained=NA` because a combined spawn is not evidence about both legs. **Recorded as a deviation so the ledger does not imply the recommendation was followed.** HENRY (`-004`) and REGINALD (`-006`) logged L3-FAIL with the failing leg named; BROCK was LIVE, so no row owed.

**Owed by others (short, and materially shorter than 9/1):** **BROCK** — one line on `SIG-W-20260903-005` (is a pro-rated tender a "gate"?) · **REGINALD** — CREED's two `REG-T-07` asks, open since 8/20 · **RED** — the 8/28 yfinance-omission example in its own FT-10 basis packet does not reproduce · **AEOLUS** — the fleet's only ACTION item >2d.

**Routing pressure: HIGH but CLEARING.** Inbound today: 16 inbox packets, 2 PROME cross-session asks, 24 lane breaches (**NOT processed — carried**).

*(Prior regen, 2026-09-01 ~22:2x ET: 7 rows; 149 unconsumed across 20 agents, 33 ACTION; one v3 DOORBELL row, LIQUID L3-FAIL.)*

## FILTER POSTURE

> 🔴 **RESTORED 2026-08-20 boot, verbatim from `f29933a20` (2026-07-23) with ONE deliberate correction, marked below. This section was DELETED by the 2026-07-23 STATUS spine regeneration and was ABSENT FOR 28 DAYS — the same regeneration, and the same commit, that ate `## BOTTOM LINE`.** ⚠️ **The BOTTOM LINE loss was found and fixed 2026-08-18 (PAT-113, named into closeout step 12(e)) — and NOBODY DIFFED THAT REGENERATION FOR ITS OTHER CASUALTIES.** **Three surfaces pointed at this block while it did not exist: STATUS `STATE POINTERS` (*"Filter posture → FILTER POSTURE section below"*), `design/STATE.md` §5 (*"See STATUS.md FILTER POSTURE section — not duplicated here, STATUS.md is the canonical source"*), and closeout step 12(c) (*"refresh FILTER POSTURE only if it changed"*), which has been a silent no-op for 28 days.** 🔑 **So the posture that governs how aggressively this desk dispatches had NO WRITTEN HOME — every pointer to it resolved to nothing, and a closeout step named it every session without noticing.** ⇒ **Generalisable, and it is the lesson worth keeping: when you find ONE artifact eaten by a regeneration, DIFF THAT REGENERATION FOR THE OTHERS — a fix aimed at the instance leaves the siblings standing.** `[[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]]` · `[[finding_record_of_an_action_is_not_the_action]]`

**Current: BALANCED** (Apr 20 2026 onward — START LOOSE retired by Filter v2 Seg A). *Posture re-confirmed BALANCED by the empirical `design/FILTER_V3_REVIEW.md` (2026-07-04): filter structurally healthy, zero false-positive kills in the review window. No posture change has been proposed since; the 28-day absence of this block was a LOSS OF THE RECORD, not a change of state.*
- Tuning rules (FILTER_SPEC § Tuning Rules) as primary guide
- Pre-catalyst (≤72h before WAL/ZION/OZK earnings, Fed, CPI/NFP, **US–Iran MOU / negotiation-deadline events**, BOJ) → shift toward LOOSE on the relevant domain
  > ⚠️ **THE ONE CORRECTION, AND IT IS NOT COSMETIC:** the 7/23 text read *"Iran **ceasefire** expiry."* **`anchors/IRAN_WAR.md` makes "ceasefire" KILL-ON-SIGHT — there was never a ceasefire; there was a 60-day MOU negotiation window, which EXPIRED 2026-08-17 with no deal.** A verbatim restore would have reinstated a term this desk kills on sight in other people's copy. **A 28-day-old verbatim recovery carries 28 days of stale vocabulary — restore the structure, re-verify the terms.**
- Low-information stretches → shift toward TIGHT
- Confidence threshold: 0.30 minimum (unchanged)
- MINIMIZE level: Normal (all signals route)

**Pre-Apr-21 bypass reaffirmation (explicit triggers):**
- WAL or ZION gap-down >5% premarket → FLASH
- KRE intraday drop >3% → FLASH
- Iran kinetic-interdiction of US naval vessel → FLASH
- HY OAS +25bps single session → FLASH (safety net)
- VIX +5 intraday → FLASH (safety net)
- Will explicit FLASH flag via Telegram → FLASH

**Watched metrics for safety net (RULE 5):**
- VIX > 30 or +5 intraday → auto-upgrade to IMMEDIATE
- HY OAS widening > 25bps single session → auto-upgrade
- 2+ agents flag same theme in 24h → convergence flag
- Held-position liquidity drop → FLASH

**Standing flags (active operational state, not posture):**
- ✅ **COP: RETIRED 2026-06-28** (Will-approved) — file archived → `design/history/COP_RETIRED_2026-06-28.md`, boot steps 5 + 10 tombstoned, all refs removed. No standing COP obligation remains.
- ✅ **Quick WALTER: RETIRED 2026-06-26.** ONE mode — Full WALTER.
- 🟠 **`design/STATE.md` §5 points here and says this file is canonical — that pointer is now TRUE again.** It was false from 7/23 to 8/20.

---

## SESSION LOG

*Newest first — **STATUS keeps NO rows; the full archive is [`SESSION_LOG.md`](SESSION_LOG.md)**, which is live and current (670 KB, newest entry 2026-08-19 evening).*

> 🔴 **POINTER REPAIRED 2026-08-20 boot.** The in-STATUS 5-row table was deleted by the same 2026-07-23 regeneration as FILTER POSTURE above. **Unlike the posture block, NOTHING WAS LOST — `SESSION_LOG.md` has been maintained continuously throughout, and rotation to it is the documented behaviour.** **What was broken was only the POINTER:** `STATE POINTERS` still advertised *"SESSION LOG section below (last 5)"* and closeout step 12(d) still said *"prepend a SESSION LOG entry (older rows roll to `SESSION_LOG.md`)"* — describing a two-tier structure that had collapsed to one tier 28 days earlier. **Recorded rather than re-created: a 5-row duplicate of the top of `SESSION_LOG.md` is a derived surface that will rot** (`[[finding_seeded_selfsweep_secondary_surface_rot]]`), and this desk's own standing position is *stop restating, don't restate more often.* **Step 12(d) should therefore be read as "prepend to `SESSION_LOG.md`" — flagged for the next Tier-2 to amend in `CLAUDE.md`.**
