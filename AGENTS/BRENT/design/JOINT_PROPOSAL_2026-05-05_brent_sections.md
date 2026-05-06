# JOINT_PROPOSAL — BRENT sections — 2026-05-05/06

Drafted by BRENT for integration into repo-root `design/JOINT_PROPOSAL_2026-05-05.md` (3-way: CARL + BRENT + WALTER). WALTER stitches per LIAISON Turn 6 path proposal — these sections fill BRENT's slots within the WALTER-proposed 5-section structure.

Source LIAISONs:
- `AGENTS/CARL/handoff_WALTER/LIAISON.md` Turns 1-7 (CARL+WALTER architectural thread, May 5)
- `AGENTS/BRENT/handoff_WALTER/LIAISON.md` Turns 1-3 (BRENT+WALTER architectural thread, May 5-6)
- BRENT scaffolding commits: `707a2f79` (channel + Turn 1/2/3 + STATUS retro-tag), `bf8c2c9e` (back-disposition pass)

---

## §1.1 — BRENT context coda

*[Stitch instruction: merge into §1 CONTEXT after CARL's CARL+WALTER summary]*

BRENT joined the architectural dialog **2026-05-05 23:15 UTC**, after the CARL+WALTER thread had converged earlier the same day. Channel scaffolded at `AGENTS/BRENT/handoff_WALTER/` (README + LIAISON.md, mirrored CARL's pattern); BOARD_LOG.tsv stood up with the same 9-col schema CARL adopted including the May 5 Post_Hoc_Conf column.

BRENT inherited all CARL+WALTER decisions in flight (FORMAT_SPEC v0.8, ROUTING_TABLE v0.6, NEXUS-precedence-on-cluster-narrative, calibration-cycle protocol) and contributed **three substantive deltas**:

1. **Energy-cluster outbound tagging** — added `lng_substitution` to `consumer_transmission` enum (mechanically distinct from pump-pass-through); proposed separate `energy_transmission` (10-value) + `regime_state` (5-value) enums for outbound-from-BRENT signals as a v0.9 candidate stack.

2. **BRENT-IMMEDIATE threshold-cross dispatch list** — 8 boundary thresholds for BRENT-primary IMMEDIATE-precedence dispatches (Brent ≥$120 / ≤$75 sustained, Cushing <20M, HY Energy OAS >400bps, VLCC WS sustained-cross-from-baseline, gasoline crack threshold-cross logic, US oil rigs +50, Brent 3:2:1 crack >$50). WALTER drafts as §2c.

3. **BURST_WINDOW_OPEN protocol** — proposed declared event-window mode for Phase 2 trigger events (FLASH-only routing during 24-72h window with rolling Telegram thread + daily 00:00 UTC roll-up). LESSONS #11/#16 say price collapses Day 3-8 of announcement; daily-batch loses the window. WALTER drafts as §2d.

**Operational state after BRENT Turns 1-3:**
- 47 unique BRENT-routed signals back-dispositioned (Apr 14 → May 5; commit `bf8c2c9e`): 30 INTEGRATED / 12 INFO_ONLY / 4 REFERRED / 1 BRENT_ORIGIN
- 5 Post_Hoc_Conf deltas surfaced for WALTER verify-research calibration (detail in §3e.1)
- STATUS retro-tag landed for SIG-W-20260505-012 placeholder-narrative caveat
- Calibration cycle 1 clock starts **2026-05-06** (N=15 forward dispositions OR 21 days, whichever first)

Three BRENT close-loop questions (Q13-Q15) remain open for WALTER Turn 4 — stitcher mechanics, BRENT-cycle-1 trigger confirmation, Path A live-rehearsal protocol.

---

## §2e — BRENT cosign on FORMAT_SPEC v0.8 + outbound-side enum proposals

*[Stitch instruction: append as §2e under §2 FOR WILL SIGN-OFF]*

### §2e.1 — Cosign on FORMAT_SPEC v0.8

BRENT cosigns the four-field FORMAT_SPEC v0.8 stack as drafted in §2a:
- `consumer_transmission` (final 9-value enum below)
- `signal_role` (`primary_substance | cluster_mediating | counter_evidence | thesis_confirmation`)
- `consumer_lens` (`tier_stratified | broad_collapse | mixed | counter`)
- `cluster_secondary` (optional, comma-separated, primary-by-substance + secondary by descending action-relevance)

3-way cosign rationale: BRENT is action-primary on energy-cluster substance and the data-primary recipient when WALTER tags a signal `cluster_mediating`. The v0.8 fields are load-bearing across CARL (consumer-side pull) AND BRENT (energy-side push) — three-way cosign demonstrates the stack works at both ends of the major transmission paths, not just CARL ergonomics.

### §2e.2 — `consumer_transmission` enum extension: `lng_substitution`

**Final 9-value `consumer_transmission` enum** (BRENT's `lng_substitution` added; `refining_margin_pass_through` dropped per WALTER pushback):

```
pump_pass_through       — gasoline / heating-oil retail-price transmission (CARL-anchored)
wage_pressure           — labor-market-tight → wage-side cost transmission
wealth_effect           — equity / housing → top-decile reverse-wealth-effect
policy_pass_through     — tariff / regulation cost-side transmission to consumer
discretionary_demand    — observation-side discretionary-pullback (Black Box restaurants type)
services_export         — services-export demand destruction (AHLA WC2026 type)
lng_substitution        — heating-fuel substitution at residential / commercial / industrial level
counter_evidence        — within-cluster counter-channel (BofA Card / JPM Q1 type)
none                    — signal carries no consumer-side transmission mechanism
```

**`lng_substitution` rationale** (mechanically distinct from `pump_pass_through`):

LNG drives a separate consumer-cost vector from gasoline/diesel pump transmission. Worked example pulling from BRENT KB: when **Qatar lost ~12.8 MTPA of LNG export capacity from the March 2 Iranian drone strikes on Ras Laffan + Mesaieed** (force majeure declared March 24, with at-least-2-yr expansion-wave delay per IEA Gas Market Report April 2026), the consumer-side transmission paths bifurcate:

- **Pump path** (`pump_pass_through`) — Hormuz/Brent shock → US/EU refining → wholesale gasoline → AAA $4.45 retail (this is CARL's KB-CARL-259 mechanism)
- **LNG path** (`lng_substitution`) — Qatar outage → JKM Asia / TTF Europe → industrial-load curtailment + residential heating-cost spike + Korea/Japan/Taiwan FX/inflation pressure (SAM-anchored, with HENRY energy-CPI cross-feed)

These mechanisms compose differently into consumer cost-of-living: pump is **transportation-fuel**, LNG is **heating + electricity-generation + industrial-feedstock**. A signal tagged `lng_substitution` routes differently downstream (SAM primary, CARL secondary on residential heating) vs `pump_pass_through` (CARL primary). Tagging at dispatch tightens batch-folding for both agents.

### §2e.3 — `refining_margin_pass_through` dropped

BRENT's Turn 1 proposal to add `refining_margin_pass_through` is **withdrawn** per WALTER's Turn 2 pushback. Refining margin → wholesale → retail pump is a sub-component of `pump_pass_through`, not a mechanically distinct mechanism — taggable in dispatch_note prose ("via refining-margin component") rather than enum value. Avoids enum proliferation; keeps `pump_pass_through` as canonical for the entire crude→pump pathway.

### §2e.4 — `energy_transmission` v0.9 candidate (separate Will-surface)

For outbound-from-BRENT signals (mirror of `consumer_transmission`'s outbound-from-CARL framing), proposing a 10-value `energy_transmission` enum on a v0.9 candidate stack — **not blocking v0.8 sign-off**, surfaced separately when v0.8 lands and the enum schema is in production:

```
kinetic_supply           — direct kinetic event affecting physical supply (refinery hit, port closure, vessel strike)
sanctions_enforcement    — OFAC / SDN / sanctions actions (Hengli Dalian type)
inventory_dynamics       — ex-Gulf / refining-product / LNG inventory data (drawdowns and buildups)
posture_only             — diplomatic / doctrine / military-posture without kinetic
operational_anomaly      — OSINT operational-stress signals (USAF tanker squawks, EAM/HFGCS)
ceo_supply_balance       — corporate-CEO substantive supply-balance call (Wirth Milken type)
tape_pricing             — market-tape-vs-cluster-substance pricing read (-012 type)
framing_meta             — analyst / media reframings of cluster narrative (MS 1990v2026 type)
refining_capacity        — refinery damage / turnaround / utilization (Geelong / Pachpadra / Tuapse / Corpus Christi)
freight_premium          — VLCC / Suezmax / Aframax rate moves; war-risk insurance pricing
```

**Paired `regime_state` 5-value enum** (orthogonal axis — *what mechanism* × *where in two-phase arc*):

```
phase_1_squeeze              — supply squeeze active (current state since Feb 27 2026)
phase_1_to_2_transition      — Path A (Hormuz reopen) or Path B (demand destruction) firing in real time
phase_2_destruction_demand   — Path B fires first (demand destruction emerges ahead of reopen)
phase_2_unwind_opec          — Path A fires (Hormuz reopens, OPEC+ unwind cascades)
post_phase_2_normalization   — post-resolution rebalancing
```

Cross-tag examples: SIG-W-20260420-001 Tuapse 2nd strike = `kinetic_supply` + `refining_capacity` (multi-tag, comma-separated like `cluster_secondary`) × `phase_1_squeeze`. SIG-W-20260505-012 Brent tape divergence = `tape_pricing` × `phase_1_squeeze`. A hypothetical Iran climbdown announcement = `posture_only` (rhetorical) or `kinetic_supply` (operational) × `phase_1_to_2_transition`.

**Why separate from v0.8:** energy_transmission is BRENT-domain analog to consumer_transmission, useful but not blocking the consumer-side proposal. regime_state is BRENT's two-phase thesis structure made into a routing tag — has value across cluster-mediating dispatches (signal-relevance at boundary phases differs sharply from within-phase signals). Both v0.9-candidate; surface to Will when v0.8 stabilizes.

---

## §3e — BRENT-side FYI

*[Stitch instruction: append as §3e under §3 FOR WILL FYI]*

### §3e.1 — BOARD_LOG.tsv back-disposition pass shipped

**Commit `bf8c2c9e`** (2026-05-06) — 47 unique BRENT-routed signals dispositioned for the period Apr 14 → May 5 2026, sourced from `AGENTS/WALTER/handoff_BRENT/route_log_brent_slice.tsv` (48 dispatch events; SIG-W-20260419-029 appears twice with verify-research uplift, logged once).

**Disposition breakdown:**
| Disposition | Count | Notes |
|-------------|------:|-------|
| INTEGRATED | 30 | Energy-cluster substance folded to STATUS / KB / thesis |
| INFO_ONLY | 12 | Kinetic / HAWK-domain context, weak-source, no BRENT mechanism |
| REFERRED | 4 | LIQUID / ZHAO / HENRY primary, no BRENT-acting path |
| BRENT_ORIGIN | 1 | Price tape (-029-001), already in STATUS via direct intake |

**5 Post_Hoc_Conf deltas surfaced for WALTER verify-research calibration:**

| Signal_ID | WALTER conf | BRENT Post_Hoc | Reason |
|-----------|------------:|---------------:|--------|
| SIG-W-20260419-021 (MS 1990v2026) | 0.65 | **0.55** | Gasoline-burden axis at 1.8% understates current ~3.5% post-AAA $4.45 surge — counter-framework holds 4 of 6 axes, not 6 |
| SIG-W-20260419-027 (Energy Sec gasoline >$3) | 0.50 | **0.40** | Tautological at current $4.45 retail; weak Polymarket-cited source |
| SIG-W-20260419-030 (InfraA Qatar LNG) | 0.50 | **0.85** | Retrospective uplift — Qatar LNG core verified by SIG-W-20260505-002 (IEA primary) |
| SIG-W-20260424-008 (Corpus Christi water) | 0.80 | **0.70** | Water-emergency rain-relief probability hedge + Sep 2026 timeline distance |
| SIG-W-20260505-009 (Wirth Milken 1970s) | 0.85 | **0.75** | Chevron CEO book-bias on 1970s-magnitude framing; per BRENT Turn 3 Q8 magnitude is ~0.6× not 1.0× |

These deltas inform WALTER's verify-research threshold tuning at the next calibration cycle review.

### §3e.2 — `design/CROSS_REFS/BRENT.md` cache (WALTER self-task)

Per LIAISON Turn 3 Q6 — WALTER caches BRENT identifier index (FLOW.tsv, KB.tsv, PREDICTIONS.tsv, SCHEMA.tsv) at `AGENTS/WALTER/design/CROSS_REFS/BRENT.md`. **Dual-trigger refresh mechanism**: cache refreshes when `AGENTS/BRENT/thesis/THESIS.md` version-string changes OR `AGENTS/BRENT/workbook/SCHEMA.tsv` mtime changes (mirrors CARL Turn 7 freshness mechanism). Thesis v2 CHANGELOG bump (Project Freedom + bypass-pair pattern) expected this week — cache will refresh on that bump.

### §3e.3 — FLOW.tsv outbound expansion (BRENT self-task, ETA this week)

Per LIAISON Turn 3 Q6 — BRENT to add explicit `FLOW-BRT-X.YY` rows for active outbound transmission paths. Canonical row already exists; new rows pending:
- `FLOW-BRT-3.04` pump-pass-through to CARL (canonical example)
- LNG-substitution to SAM (Japan / Korea / Taiwan)
- Energy-credit cross-feed to LIQUID (HY-energy OAS, E&P debt)
- Energy-PPI / CPI to HENRY (oil-driven inflation components)
- Oil-price feedback to HAWK (scenario-framework input)

Once shipped, WALTER's dispatch_note cross-refs can carry `transmits via FLOW-BRT-3.04 to CARL Vector #5 (KB-CARL-259) pump-pass-through` style at dispatch time. Will flag in commit message so WALTER's cache (§3e.2) catches the expansion.

### §3e.4 — Thesis v2 CHANGELOG bump (BRENT self-task, ETA this week)

Project Freedom (May 4) + bypass-pair pattern (Petroline Apr 9 + Fujairah May 4) materially refines BRENT's two-phase Phase 1 framing. v2 thesis update will trigger §3e.2 cache refresh per the dual-trigger mechanism. Thesis CHANGELOG entry will narrate the refinement; THESIS.md first-line version string will increment.

### §3e.5 — STATUS.md retro-tag for SIG-W-20260505-012 (shipped)

Per LIAISON Turn 3 Q3 operational rule (workbook-citable = substance authoritative; cross-cluster narrative = pending-NEXUS placeholder). STATUS.md line 4 — "tape disagrees with admin framing" — now carries inline caveat `[BRENT-placeholder-narrative pending REQ-NEXUS-20260505 — narrative-interpretation only; substance facts (kinetic events, prices, framing-quote attributions) remain authoritative]`. Workbook (KB.tsv / PREDICTIONS.tsv / FLOW.tsv) stays clean of placeholder caveats; STATUS prose carries them. Shipped commit `707a2f79`.

### §3e.6 — BRENT calibration cycle 1 clock

Per LIAISON Turn 3 Q14 (open — pending WALTER Turn 4 confirm) — BRENT's calibration cycle 1 trigger: **N=15 forward BOARD dispositions OR 21 days from 2026-05-06**, whichever first. Lower N than CARL (CARL's N=20 / 14 days) because BRENT-cluster signal volume is higher (8 of 12 May 5 signals were energy-cluster); 15 forward = ~10-14 days at current pace. Clock starts now that back-disposition pass has shipped.

---

## §4 — BRENT decisions locked Turns 1-3

*[Stitch instruction: merge BRENT-Q rows into §4 unified decisions list alongside CARL Q1-Q22 and WALTER co-signs. Cross-reference CARL Q-numbers where the BRENT decision inherits CARL's framing.]*

| BRENT-Q | Turn | Decision | Co-signed |
|---------|:----:|----------|-----------|
| **Q1** | T1 | Use WALTER `route_log_brent_slice.tsv` (48 dispatch events, 47 unique signals) as canonical back-disposition input. Inherits CARL's diff-against-INDEX pattern. | WALTER T2 |
| **Q2** | T1 | BRENT joins as 3rd cosigner on FORMAT_SPEC v0.8 joint proposal. `lng_substitution` accepted; `refining_margin_pass_through` dropped (compositional sub-vector of pump_pass_through, not mechanically distinct). | WALTER T2 |
| **Q3** | T1 | Substance/narrative line: workbook-citable claims = substance authoritative; cross-cluster narrative interpretations = pending-NEXUS placeholder, flagged inline with `[BRENT-placeholder-narrative pending REQ-NEXUS-20260505]` caveat. Mirrors CARL Turn 5 placeholder convention. | WALTER T2 |
| **Q4** | T1 | BRENT-IMMEDIATE threshold dispatch list — 8 rows (full table in §2c, WALTER draft). Two redlines accepted: (a) VLCC PRIORITY-not-IMMEDIATE with sustained-cross-from-baseline trigger (sustained ≥2× trailing 30-day median, not absolute level); (b) gasoline crack converted to threshold-cross logic (initial dispatch on first re-cross from <$30 back ≥$30 OR single-day spike ≥$50; standing $42 = no fresh fire). Re-fire convention: one signal per boundary cross, no re-fire on continued state. | WALTER T2 |
| **Q5** | T1 | BURST_WINDOW_OPEN protocol accepted (FLASH-only routing during declared window + rolling Telegram thread + daily 00:00 UTC roll-up + close-of-window summary). Either-side-can-declare; BRENT-declares-open on Path A 4/4 trigger fire, WALTER-declares-close after ≥48h stable post-event state. Daily-batch-only opposed (LESSONS #11/#16 — price collapses Day 3-8 of announcement). Flagged for Will sign-off in §2d. | WALTER T2 |
| **Q6** | T1 | BRENT cross-feed outbound paths use `workbook/FLOW.tsv` as canonical (FLOW-BRT-X.YY); WALTER dispatch_note carries cross-refs at dispatch. REGISTRY stays coarse (Upstream/Downstream agent-level only); FLOW.tsv has mechanism granularity. consumer_transmission + cluster_secondary tags cover signal-level mechanism; FLOW-BRT-X.YY covers agent-internal vector lookup. Two layers, no overlap. | WALTER T2 |
| **Q8** | T2 | Wirth 1970s analog magnitude: **0.6×** (5 features present: ME supply shock, refining-margin compression, jet-fuel substitution emergency, oil-price direction, mechanism analog; 7 features attenuated or absent: smaller price magnitude, no wage-price spiral, US net exporter, SPR/IEA cushion exists, aging demographics, service economy, post-Volcker Fed credibility). Chevron CEO book-bias on amplification framing flagged. | n/a (BRENT direct answer; feeds RED steelman) |
| **Q9** | T2 | Tape-vs-substance read on SIG-W-20260505-012: **mixed (i) risk-premium-already-priced + (iii) over-corrected on doctrine-without-kinetic + thread of (ii) under-priced; REJECT (iv) noise**. Implication: keep cluster-mediating dispatches coming; -012 type was useful calibration data, not over-fired by WALTER. Don't tighten the dispatch trigger on cluster-mediating signal_role. | n/a |
| **Q10** | T2 | HAWK-proxy useful for event-fact aggregation, less useful for doctrinal interpretation. On HAWK refresh: **HAWK supersedes proxy on doctrinal/kinetic interpretation; BRENT keeps own oil-substance synthesis** (price/structure/storage/refining/credit). Proxy archived as transitional artifact in WALTER tree on HAWK refresh. | WALTER T2 |
| **Q11** | T2 | `energy_transmission` enum 10-value (kinetic_supply, sanctions_enforcement, inventory_dynamics, posture_only, operational_anomaly, ceo_supply_balance, tape_pricing, framing_meta, refining_capacity, freight_premium) + `regime_state` 5-value (phase_1_squeeze, phase_1_to_2_transition, phase_2_destruction_demand, phase_2_unwind_opec, post_phase_2_normalization) — separate orthogonal axes. **FORMAT_SPEC v0.9 candidate**, separate Will-surface from v0.8 (not blocking). | WALTER T2 conditional accept |
| **Q12** | T2 | BOARD consumption: **(c) hybrid** — 6-row signal-type triage table (primary-source dups → BRENT_ORIGIN; cluster-mediating → INTEGRATED+placeholder-narrative; counter-evidence → INTEGRATED; aggregator-with-verify-research → INTEGRATED if verdict adds calibration value; pure HAWK-kinetic → INFO_ONLY/REFERRED; non-energy-cluster on info → INFO_ONLY rare). CLAUDE.md gets BRENT-specific spawn protocol delta (primary-source-heavy intake → more BRENT_ORIGIN dispositions than CARL has). | n/a (BRENT self-task) |
| **Q13** | T3 | *Open* — Joint Will-surface stitcher: WALTER stitches at repo-root `design/JOINT_PROPOSAL_2026-05-05.md`. CARL + BRENT submit per-agent sections to WALTER's tree. | open — pending WALTER T4 |
| **Q14** | T3 | *Open* — BRENT calibration cycle 1: **N=15 forward dispositions (post-back-pass) OR 21 days from 2026-05-06**, whichever first. Lower N than CARL because energy-cluster volume is higher; 15 forward ≈ 10-14 days at current pace. | open — pending WALTER T4 |
| **Q15** | T3 | *Open* — Path A trigger live-rehearsal: BURST_WINDOW_OPEN auto-declared on announcement (not first verification gate); LESSONS #18 disambiguation closes window early on rhetorical-not-operational announcements. False-positive cost (~24h FLASH on non-event) << false-negative cost (missing actual reopen Day 3-8). | open — pending WALTER T4 |

**Asymmetric note:** BRENT decisions Q1-Q12 are LOCKED with WALTER co-sign. Q13-Q15 require WALTER Turn 4 close-loop. CARL's parallel architectural items closed at Q22; BRENT's three open items are operational mechanics rather than blocking architecture.

---

## §5 — Next review (BRENT contribution)

*[Stitch instruction: merge into §5 NEXT REVIEW alongside CARL's calibration cycle and WALTER's review-window]*

**BRENT calibration cycle 1 trigger:** N=15 forward BOARD dispositions OR 21 days from 2026-05-06, whichever first. First cycle ETA roughly **2026-05-20 to 2026-05-27** at current dispatch rate.

**Calibration deliverable per cycle (per LIAISON Turn 3 acceptance + Turn 5 CARL-pattern):** BRENT summarizes Post_Hoc_Conf deltas accumulated since prior cycle; WALTER tunes verify-research thresholds and sub-agent prompts; cycle delta logged as new turn in `AGENTS/BRENT/handoff_WALTER/LIAISON.md`.

**Architectural-thread close-loop dependency:** WALTER Turn 4 close-loop on Q13-Q15 (stitcher mechanics + BRENT-cycle-1 trigger confirm + Path A live-rehearsal protocol). Until Turn 4 lands, treat Q13-Q15 as proposed-not-locked.

---

*BRENT sections file lives at `AGENTS/BRENT/design/JOINT_PROPOSAL_2026-05-05_brent_sections.md`. WALTER stitches into repo-root `design/JOINT_PROPOSAL_2026-05-05.md` for the final Will-surface artifact.*
