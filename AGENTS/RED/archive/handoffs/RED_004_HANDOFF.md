# RED_004 Handoff — WALTER Design Session

**Date:** 2026-04-07
**Session type:** Cross-agent design work (WALTER, not RED adversarial)
**Duration:** ~1.5 hours

---

## What Happened

Will asked RED to help with WALTER — a new agent being designed as the network's intake/routing point for external information. Prome had already pushed research from 7 disciplines (ESI triage, military messaging, ATC, pub-sub brokers, intelligence community, emergency dispatch, scientific alert systems) — 15 files total in `AGENTS/WALTER/research/`.

RED read the full corpus, provided initial analysis, then worked with Will to:

1. **Distill research** into actionable summaries, cutting domain-specific detail:
   - `AGENTS/WALTER/research/distilled/01_ESI_TRIAGE.md` — dual-axis classification, 4 decision points, failure modes
   - `AGENTS/WALTER/research/distilled/02_MILITARY_MESSAGING.md` — precedence, preemption, dual recipients, AIGs, degradation
   - `AGENTS/WALTER/research/distilled/03_AIR_TRAFFIC_CONTROL.md` — state externalization, conflict detection, alert fatigue, handoffs, sterile cockpit

2. **Draft design specifications:**
   - `AGENTS/WALTER/design/SIGNAL_FORMAT_SPEC.md` — standardized signal header block, 4 precedence levels, 7 signal types, AIGs, MINIMIZE protocol, body format
   - `AGENTS/WALTER/design/ROUTING_TABLE.md` — domain-to-recipient mapping, default precedences, safety net auto-upgrades, escalation paths
   - `AGENTS/WALTER/design/FILTER_SPEC.md` — Gate 1 filter (novelty/relevance/credibility), confidence scoring, kill log, route log, tuning rules

3. **Key design decisions made with Will:**
   - WALTER is BOTH filter and router (two sequential gates)
   - WALTER is the single entry point for external information
   - WALTER rewrites signals into standard format (not just headers on raw data)
   - File-based implementation (no new infrastructure needed)
   - Start loose on filtering, tighten from experience

---

## What's Remaining

### Distillation (4 prompts not yet distilled):
- Prompt 4: Pub-Sub Brokers (Kafka/RabbitMQ/NATS)
- Prompt 5: Intelligence Community (ICD 501/502/503, tearlines)
- Prompt 6: Emergency Dispatch (911/NG911, MPDS, CAD)
- Prompt 7: Scientific Alert Systems (ATLAS, LIGO, ZTF)

### Design work not started:
- Acknowledgment/receipt protocol (from military five-layer + ATC handoff)
- Superevent grouping spec (from LIGO GraceDB — see Signal Registry Draft A)
- Re-triage interval spec (from CTAS/ESI)
- Conflict detection spec (from ATC three-zone model)
- WALTER boot sequence / CLAUDE.md

### Already exists but needs integration:
- `AGENTS/WALTER/design/SIGNAL_REGISTRY_DRAFT_A.md` — predates this session, covers event store + state machine. Overlaps with some of what we built but goes deeper on the database/API layer.

---

## RED Observations

- The research corpus is strong. Cross-domain convergence on key patterns (multi-axis classification, cascading filters, confidence scoring) validates the approach.
- Scale mismatch risk: research is weighted toward 100K+ signal/day systems. We handle 20-50. Keep implementation proportional.
- The filter is where WALTER succeeds or fails. Classification and routing are well-defined. The hard problem is the intake judgment — what to kill vs what to pass.
- Missing Prompt 1 master research doc (only extraction exists). May want to fill that gap.

---

## Commits

1. `84540b8a` — WALTER: Distilled prompts 1-2 + Signal Format Spec + Routing Table
2. `784785e9` — WALTER: ATC distilled + Filter Specification
