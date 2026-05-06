# JOINT_PROPOSAL — RED sections — 2026-05-06

Drafted by RED for integration into repo-root `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` (2-way: RED + WALTER, **parallel to** — not folded into — the existing 3-way `JOINT_PROPOSAL_2026-05-05_walter_carl_brent.md`). WALTER stitches per LIAISON Turn 4 path proposal — these sections fill RED's slots within the WALTER-proposed 5-section structure.

Source LIAISON: `AGENTS/RED/handoff_WALTER/LIAISON.md` Turns 1-5 (RED+WALTER architectural thread, May 6 — converged in 5 turns).

RED scaffolding commit: `7f3e9ddf` (2026-05-06) — channel + Turns 1-5 + 3 deliverables (FALSIFICATION_TRIGGERS.tsv, CHALLENGES.tsv BOARD_Refs col + 5 backfilled, bifurcation classification TSV) + workbook SCHEMA bumps.

Section ownership (per LIAISON Turn 4):
- §1 (RED) — RED domain framing + 97% routing-target finding *(this draft)*
- §2 (WALTER) — FALSIFICATION_TRIGGERS.tsv at-dispatch evaluation logic *(WALTER drafts in parallel; placeholder slot below)*
- §3 (WALTER) — ROUTING_TABLE v0.7 delta + CHECKLIST delta *(WALTER drafts in parallel; placeholder slot below)*
- §4 (RED) — CHALLENGES.tsv evolution + RED CLAUDE.md boot-step pending Will-approval *(this draft)*
- §5 (WALTER) — v0.9 candidates: unanimity_state *(WALTER drafts in parallel; placeholder slot below)*

---

## §1 — RED CONTEXT (RED draft)

### §1.1 — RED domain framing

RED is the network's **adversarial overlay** — not action-primary on any domain data. RED reads what other Tier-1 agents (CARL, REGINALD, BRENT, LIQUID, HAWK, SAM, HENRY, NEXUS, VIOLET, BROCK, MARCO, OZK) produce and stress-tests it. Mandate: **find what's WRONG with every thesis** through five canonical artifacts:

1. **Counter-evidence vector registry** — `AGENTS/RED/workbook/VX.tsv` (counter-signals with explicit bull/bear weights and flip conditions)
2. **Falsifiable predictions** — `AGENTS/RED/thesis/PREDICTIONS.tsv` (RED-NN with public scoring; resolved record 4 WRONG / 1 CORRECT / 9 ACTIVE as of 2026-05-06, Will-corrected from earlier overstatement)
3. **Pre-registered falsification triggers** — `AGENTS/RED/STATUS.md` FALSIFICATION CRITERIA + as of 2026-05-06 also `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` (8-col machine-readable)
4. **Formal challenges** — `AGENTS/RED/workbook/CHALLENGES.tsv` (CHG-RED-NNN with target agent, grade, status, KB/VX cross-links)
5. **Knowledge base** — `AGENTS/RED/workbook/KB.tsv` (KB-RED-NNN with Admiralty confidence digraph, Stale_By dates, methodology corrections)

RED owns no primary feed. Everything published derives from other agents' work + adversarial framework. Current thesis state: confidence 73% on bear thesis (was 70%, +3 after pre-committed Apr 18 trigger fired clean Apr 21 on WAL/OZK MISS/MUTED); thesis bifurcated paper-vs-structural; 6 competing hypotheses with explicit probabilities.

### §1.2 — The 97% routing-target finding (LIAISON Turn 2 empirical reframe)

RED Turn 1 framed the consumption gap as *"WALTER (BOARD): Mostly absent — see retrospective"*, identifying only 1 direct-route signal (SIG-W-20260411-001 HY OAS pierced, Apr 11). WALTER's Turn 2 empirical correction inverted the diagnosis:

| Recipient state for RED | Count | % |
|-------------------------|-------|---|
| RED in `to:` (action) line | **19** | 17% |
| RED in `info:` line | **100** | 91% |
| RED in to/info combined | **107** | **97%** |
| Total BOARD signals | 110 | — |

**RED has been a routing target on 97% of dispatches** since Apr 7. The 19 `to:` (action-primary) signals span falsification-counter, counter-evidence-cluster, cluster-bifurcation, and adversarial-counter-thesis routings — ~3.5 per week. The 100 info-cc signals deliver to a queue RED has not been draining.

**Architectural implication:** the gap is RED-side **consumption**, not WALTER-side **dispatch**. The fix is structured artifacts that let WALTER's existing high-volume routing become consumable by RED, not "more dispatch."

### §1.3 — Verify-research verdict distribution validation

WALTER's Turn 2 surfaced verdict-distribution data across 94 verified BOARD signals:

| Verdict | Count | % |
|---------|-------|---|
| CONFIRMED | 45 | 48% |
| **CORRECTED-FRAMING** | **44** | **47%** |
| INDETERMINATE | 3 | 3% |
| FALSE | 2 | 2% |

RED's prior MEMORY entry (`feedback_corrected_framing_calibration.md`) flagged CORRECTED-FRAMING as "the most-frequent verify verdict" — the 47% measurement validates this empirically and tightens it to "tied with CONFIRMED as modal." The recurring CORRECTED-FRAMING pattern is **direction-confirmed-specifics-imprecise** — the cell where RED's adversarial overlay adds the most value (preventing "directionally correct + magnitude inflated" from being reified into "thesis confirmed at full magnitude" downstream).

### §1.4 — Bifurcation cluster sizing

21-22 historical BOARD signals (19-20% of total dispatch volume) carry bifurcation / divergence / tape-vs-substance / paper-vs-structural language. RED produced a v0.1 classification of these signals at `AGENTS/RED/handoff_WALTER/bifurcation_classification_2026-05-06.tsv` (LIAISON Turn 5 deliverable, 22 rows):

| RED_class | Count | Pct |
|-----------|------:|----:|
| HENRY-tape | 8 | 36% |
| RED-structural | 9 | 41% |
| both | 5 | 23% |
| **Total** | **22** | — |

14 of 22 lean structural (RED-structural + both = 64%) — matches WALTER's Turn 2 hypothesis ("13-14 of 21 lean second way") within rounding. Three findings emerged from the classification pass:

- **VIOLET emerges as primary recipient on 3 vol-family signals** (419-002, 419-003, 419-007). VIOLET is distinct enough from HENRY in REGISTRY to be its own action-primary on vol-family signals. Implication: VIOLET must be in the agent-set explicitly when computing `unanimity_state` (§5 enum). *(Refinement post-WALTER §5.3: today's strict-staleness N is 6 not 9 — LIQUID 04-16, HENRY 04-17, HAWK 04-20 all >14d STALE and excluded per Q15. VIOLET 05-03 stays in. RED's Turn 5 framing of "N=9 including VIOLET" was pre-staleness-filter; WALTER §5.3 calculation is canonical.)*
- **All 5 "both" signals are event-anchored bifurcations** (HY OAS pierced, Iran SoH reclosure, Tuapse 2nd strike, Merz ally-rhetoric, Brent May 5 tape divergence). Pattern: bifurcation framing emerges when a discrete event or print contradicts an active narrative.
- **Apr 19 = 9 of 22 signals (41% in 1 day).** Iran cluster Apr 19 was the highest-density bifurcation-cluster moment in the 25-day arc (2 days pre-Apr 21 WAL/OZK earnings + ceasefire expiry). **Network observation:** dense-bifurcation-day correlates with high-stakes-decision-day. Pattern worth flagging in RED's CALENDAR catalyst tagging.

### §1.5 — Operational state after RED Turns 1-5

- 8/8 RED-asked questions resolved (Q1, Q3, Q4, Q6, Q7 pre-cosigned; Q2 deferred to v0.9; Q5 deferred to calibration cycle 1; Q8 priming-offer accepted via Q13).
- 4/4 WALTER-asked questions resolved (Q9 scope-b boot-step; Q10 narrow-precision cross-ref; Q11 RED-level ≥4 cutoff with bull-side fresh-active calibration; Q12 CORRECTED-FRAMING auto-cc).
- 3 close-loop questions resolved Turn 5 (Q13 TSV format locked; Q14 WALTER takes complete CHG backfill; Q15 fresh-active-only denominator).
- 3 deliverables shipped: FALSIFICATION_TRIGGERS.tsv (Q1), CHALLENGES.tsv BOARD_Refs col (Q7), bifurcation classification (Q8/Q13).
- 2 RED-side post-Will deliverables pending: CLAUDE.md boot-step add (Q9), MEMORY.md 97%-routing-target calibration entry.
- Calibration cycle 1 clock starts **2026-05-06**, synced with BRENT's cycle 1 (ETA May 20-27).

**Convergence in 5 turns** — same as BRENT, 2 turns faster than CARL. The "open-with-substance Turn 1 + concede-on-diagnosis Turn 3 + ship-deliverables-in-Turn-3 + close-Turn-5" pattern compressed convergence vs CARL pilot. Saving as a finding for next-LIAISON channels (NEXUS, REGINALD, HENRY).

---

## §2 — FALSIFICATION_TRIGGERS.tsv WALTER-side eval logic

*[WALTER drafts in parallel — `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md` §2. Placeholder slot for stitching.]*

WALTER's at-dispatch evaluation logic for `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv`: read-loop, threshold-eval, dispatch-trigger, last_fired_date update. Out of scope for v1: continuous live-tape polling (WALTER doesn't have always-on session).

---

## §3 — ROUTING_TABLE v0.7 delta + CHECKLIST delta

*[WALTER drafts in parallel — `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md` §3. Placeholder slot for stitching.]*

ROUTING_TABLE v0.7 additions:
- `cluster_mediating: true → RED auto-cc` (Q3, locks at v0.8 sign-off)
- `verdict CORRECTED-FRAMING → RED auto-cc` (Q12, composes with Q3 with de-dupe at routing-time)

CHECKLIST Phase 2 additions:
- "if `cluster_mediating: true`, ensure RED in info line"
- "if verdict CORRECTED-FRAMING, ensure RED in info line"
- "at dispatch, scan FALSIFICATION_TRIGGERS.tsv for threshold cross"

---

## §4 — RED ARTIFACT EVOLUTION (RED draft)

### §4.1 — CHALLENGES.tsv schema bump (Q7 — shipped)

**Decision:** RED does NOT stand up `board/BOARD_LOG.tsv` (CARL/BRENT pattern). Instead, RED extends `workbook/CHALLENGES.tsv` with a new column `BOARD_Refs` (col 11) carrying semicolon-separated SIG-W-IDs. This keeps RED's adversarial-overlay role distinct from primary-thesis-integration agents (CARL/BRENT use BOARD_LOG.tsv for calibration-of-integration; RED uses CHALLENGES.tsv for calibration-of-challenge).

**Schema after bump:**

| Col | Name | Type | Purpose |
|-----|------|------|---------|
| 1 | CHG_ID | String | CHG-RED-NNN |
| 2 | Date | YYYY-MM-DD | Date challenge issued |
| 3 | Target | String | Agent / position / thesis being challenged |
| 4 | Grade | String | Letter grade A+ to F |
| 5 | Key_Finding | String | Core finding |
| 6 | Status | Categorical | ACTIVE; RESOLVED; SUPERSEDED; RESOLVED-CONVERGED; WEAKENED |
| 7 | Resolved_Date | YYYY-MM-DD | When resolved |
| 8 | Resolution | String | How it was resolved |
| 9 | KB_Links | String | KB-RED-NNN refs |
| 10 | VX_Links | String | VX-RED-NNN refs |
| 11 | **BOARD_Refs** | **String** | **SIG-W-YYYYMMDD-NNN refs (semicolon-separated)** — NEW 2026-05-06 |

**Backfill state (LIAISON Turn 3 shipped):** 5 historical CHGs backfilled with relevant SIG-W-IDs (CHG-RED-014, -018, -019, -021, -023). 18 historical CHGs untouched. CHG-RED-024 (BRENT v2.0, May 6) retro-flagged.

**Forward convention:** every new CHG-RED-NNN populates BOARD_Refs at issue if any BOARD signals motivated or are challenged by the CHG. Empty cell allowed (not all challenges derive from BOARD signals).

**Complete-backfill task ownership (Q14):** WALTER takes complete CHG-RED backfill as follow-up to Q4 `design/CROSS_REFS/RED.md` self-task. Mechanical-grep approach once cross-ref cache exists. RED concentrates on adversarial substance forward; backfill leaves RED's plate.

### §4.2 — SCHEMA.tsv updates (shipped)

`AGENTS/RED/workbook/SCHEMA.tsv` adds 9 rows (1 for CHALLENGES.BOARD_Refs + 8 for the new FALSIFICATION_TRIGGERS.tsv file). The schema file is now self-documenting for both CHALLENGES (11 cols) and FALSIFICATION_TRIGGERS (8 cols, network-grep-able for WALTER's at-dispatch eval logic per §2).

### §4.3 — RED CLAUDE.md boot-step add (Q9 — pending Will-approval)

**Decision (LIAISON Turn 5 locked):** boot-step (b) **scoped scan**, structured as 4 sub-tiers:

- **(b1)** Scan `/BOARD/INDEX.md` cluster ToC at boot — fastest layer, ~10s read
- **(b2)** Pull signals where RED in `to:` line (action) — full body read, treat as direct ASK
- **(b3)** Pull signals where `cluster_mediating: true` (once v0.8 lands) OR prose-tagged paper-vs-structural in dispatch_note (interim) — full body read for adversarial-overlay relevance
- **(b4)** Pull signals carrying CORRECTED-FRAMING verdict in dispatch_note — *body skim only*, looking for direction-confirmed-magnitude-imprecise patterns to flag in MEMORY's CORRECTED-FRAMING calibration

**Skip default-routine info-cc** unless one of b3/b4 fires. Reasoning: at 100/110 info-cc volume, treating all of them as "must read" inverts the small+precise discipline. Better to read 10-15 high-quality signals per cycle than scan 100.

**Insertion point:** between current step 1 (Read MEMORY.md) and step 2 (Read STATUS.md) in `AGENTS/RED/CLAUDE.md` BOOT SEQUENCE — i.e., new step 1.5.

**Why pending Will-approval:** boot-step changes affect every future RED session. RED holds the CLAUDE.md edit until Will signs off because session-permanent boot changes are best made on explicit instruction, not architectural-LIAISON consensus alone.

**Sign-off ask:** Will approves boot-step (b) scope as drafted. RED edits CLAUDE.md and the change ships in next RED commit.

### §4.4 — RED MEMORY.md 97%-routing-target calibration entry (pending Will-approval)

**Proposed memory file:** `finding_red_walter_97pct_routing_target.md`

**Content:** RED was in to/info on 97% of 110 BOARD signals (107/110) since Apr 7 — not "mostly absent" as RED Turn 1 framed. The architectural fix is RED-side consumption, not WALTER-side dispatch. Lesson: when diagnosing a routing gap, check the empirical dispatch surface before describing the gap; "I don't see X" can mean "X has been dispatched and I haven't drained the queue" rather than "X hasn't been dispatched."

**Why pending Will-approval:** MEMORY.md is the institutional layer; RED holds the addition until Will signs off so calibration entries reflect Will's framing of the lesson, not RED's first cut.

**Sign-off ask:** Will approves the memory-file content + adds index pointer in MEMORY.md. RED writes the file in next commit.

### §4.5 — Joint-proposal §1 + §4 deliverable (this file)

This file is the §1 + §4 deliverable (LIAISON Turn 4 ownership). Status: **drafted in this session per Will direction; pending Will-approval before commit.** Once Will signs, RED commits the file alongside any §4.3 / §4.4 sign-offs.

---

## §5 — v0.9 candidates: `unanimity_state`

*[WALTER drafts in parallel — `AGENTS/WALTER/design/JOINT_PROPOSAL_2026-05-06_walter_red_sections.md` §5. Placeholder slot for stitching.]*

`unanimity_state: low | moderate | high | extreme` 4-value enum, computed at RED-level **≥4** cutoff (Q11), denominator = **fresh-active-only Tier-1 agents** (≤14d Updated; today's N≈9 including VIOLET) per Q15. Bull-side symmetric (`unanimity_bull` at GREEN/YELLOW = RED-level ≤2). Sub-tag `event_anchored: true` candidate per LIAISON Turn 5 finding.

v0.9 timing — not blocking v0.8. Folds in once v0.8 lands and CARL/BRENT calibration cycle 1 fires.

---

## §6 — RED decisions locked Turns 1-5

| RED-Q | Turn | Decision | Co-signed | Status |
|-------|:----:|----------|-----------|--------|
| **Q1** | T1 | Falsification-trigger registry as separate TSV at `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` (not STATUS.md table-pull); 8-col schema; at-dispatch evaluation by WALTER. | WALTER T2 | LOCKED + SHIPPED |
| **Q2** | T1 | `unanimity_state` 4-value enum on v0.9 stack (post-v0.8-land); RED-level cutoff refined to ≥4 (Q11). | WALTER T2/T4 | LOCKED v0.9 |
| **Q3** | T1 | `cluster_mediating: true → RED auto-cc` ROUTING_TABLE rule (locks at v0.8 sign-off). | WALTER T2 | LOCKED |
| **Q4** | T1 | `AGENTS/WALTER/design/CROSS_REFS/RED.md` cache (WALTER self-task); refresh trigger: RED thesis-version bump OR new VX/CHG/RED-NN row. | WALTER T2 | LOCKED (WALTER self-task pending) |
| **Q5** | T1 | DEFER `formal_challenge` precedence; observe CHG-RED-024 propagation; revisit calibration cycle 1 (May 20-27). Interim bridge: WALTER cross-refs CHG-RED-NNN via OUTBOX surface. | WALTER T2 | DEFERRED |
| **Q6** | T1 | Prediction-resolution context as body-prose annotation in dispatch_note (NOT YAML field). | WALTER T2 | LOCKED |
| **Q7** | T1 | NO `BOARD_LOG.tsv`; use `CHALLENGES.tsv` with new `BOARD_Refs` col. | WALTER T2 | LOCKED + SHIPPED |
| **Q8** | T1 | DEFER tape-vs-structural primary; RED pre-classifies 21 historical bifurcation signals as seed (Q13 deliverable). | WALTER T4 | DEFERRED + SEED SHIPPED |
| **Q9** | T2/T3 | Boot-step (b) scoped scan (b1-b4 sub-tiers) — pending Will-approval on RED CLAUDE.md edit. | WALTER T4 | LOCKED-PENDING-WILL |
| **Q10** | T2/T3 | Narrow-precision scope for prediction-resolution cross-ref (only signals about the metric/thesis a RED-NN was directly about). | WALTER T4 | LOCKED |
| **Q11** | T2/T3 | `unanimity_state` RED-level cutoff = **≥4** (RED4/RED5 = trade-actionable consensus); not WALTER's default ≥3. | WALTER T4 | LOCKED |
| **Q12** | T2/T3 | CORRECTED-FRAMING auto-cc to RED as a class; composes with Q3 with de-dupe at routing-time. | WALTER T4 | LOCKED |
| **Q13** | T4 | Bifurcation classification format: TSV at `AGENTS/RED/handoff_WALTER/bifurcation_classification_2026-05-06.tsv`, 5 cols. | WALTER T4 | LOCKED + SHIPPED |
| **Q14** | T4 | WALTER takes complete CHG-RED backfill (mechanical-grep follow-up to Q4 CROSS_REFS cache). | WALTER T4 | LOCKED (WALTER follow-up) |
| **Q15** | T4 | `unanimity_state` denominator: **fresh-active-only** (≤14d Updated; current N≈9). | WALTER T4 | LOCKED |

**Asymmetric note:** RED decisions Q1-Q4, Q6, Q7, Q9-Q15 are LOCKED with WALTER co-sign. Q5, Q8 are DEFERRED with explicit revisit windows. No items remain open as proposed-not-locked. Two items LOCKED-PENDING-WILL (Q9 boot-step, Q4.4 MEMORY entry — both this file's §4.3/§4.4).

---

## §7 — Next review (RED contribution)

**RED calibration cycle 1 trigger:** earliest of three conditions (per LIAISON Turn 4-5):

- FALSIFICATION_TRIGGERS.tsv first auto-dispatch (whenever WALTER's at-dispatch eval logic ships and a threshold crosses)
- v0.8 lands at Will sign-off (estimated this week given CARL/BRENT cosign already)
- CHG-RED-024 BRENT response (next BRENT session, 1-3 days)

**Calibration deliverable per cycle (RED-side):** review FALSIFICATION_TRIGGERS.tsv fire history (true positives / false positives / missed crossings); review CHALLENGES.tsv BOARD_Refs population on new CHGs; review bifurcation classification accuracy on new cluster_mediating dispatches; surface findings as new turn in `AGENTS/RED/handoff_WALTER/LIAISON.md` Turn 6.

**Synced with BRENT calibration cycle 1** — both surface at network state-of-routing review ETA 2026-05-20 to 2026-05-27.

**Architectural-thread close-loop dependencies:**
- §4.3 RED CLAUDE.md boot-step — pending Will-approval
- §4.4 RED MEMORY.md calibration entry — pending Will-approval
- §2/§3/§5 (WALTER) — drafted in parallel this session per WALTER LIAISON Turn 4 commitment

Until Will sign-off lands on §4.3/§4.4, those items remain LOCKED-PENDING-WILL. Until WALTER ships §2/§3/§5 sections, the stitched repo-root document remains incomplete.

---

*RED sections file lives at `AGENTS/RED/design/JOINT_PROPOSAL_2026-05-06_red_sections.md`. WALTER stitches into repo-root `design/JOINT_PROPOSAL_2026-05-06_red_walter.md` for the final Will-surface artifact, parallel to (not folded into) the existing 3-way `JOINT_PROPOSAL_2026-05-05_walter_carl_brent.md`.*
