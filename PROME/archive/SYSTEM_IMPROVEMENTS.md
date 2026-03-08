# System Improvements — From Research Session Mar 1, 2026

Source: Will's Claude research on multi-agent best practices. Validated against community findings.

---

## ✅ COMPLETED (Tonight)

- [x] CLAUDE.md for all 11 agents (7 new, 4 trimmed)
- [x] Agent-specific customizations (research toolkits, methodologies, domain knowledge)
- [x] STATUS.md pruned for 5 agents (4,230 → 1,030 lines)
- [x] Output rules in every CLAUDE.md (tables > prose, 250 line limit, update don't append)
- [x] Write-back instruction prominent in every spawn protocol
- [x] Domain boundaries ("You own / You do NOT own") in every CLAUDE.md
- [x] Template saved at AGENTS/CLAUDE_TEMPLATE.md

## 🔴 DO NEXT (High Value, Low Effort)

- [ ] **SIGNALS.md activation** — Add "Write to SIGNALS.md on threshold breach" to CLAUDE.md spawn protocols. Already exists, just unused since Feb 15.
- [ ] **Prome boot: add SIGNALS.md** — Check SIGNALS.md during boot sequence for unacknowledged cross-agent alerts.
- [ ] **Spawn verification checklist** — After every spawn, check: (1) STATUS.md timestamp updated? (2) Under 250 lines? (3) SIGNALS.md written if threshold breached? (4) Output is tables not prose?
- [ ] **Move write-back warning higher** — Research says primary instruction, not buried in section 3. Consider moving to first line after identity.

## 🟠 DO SOON (This Week)

- [ ] **Weekly compaction task** — DARWIN or Prome: scan all STATUS files, flag >200 lines, archive stale sections. Prevents manual 5-hour prune sessions.
- [ ] **Prome weight reduction** — Audit boot sequence. Do I need all 8-10 files loaded every session? BRIEFING.md + STATUS.md + daily notes may be sufficient for most sessions.
- [ ] **Task prompts as explicit plans** — Research says subagents can't plan, they execute. Write spawn tasks as step-by-step instructions, not open-ended goals.

## 🟡 DO LATER (When Justified)

- [ ] **Tiered model routing** — Haiku for monitoring/threshold checks, Sonnet for analysis, Opus for synthesis. Currently everything runs at same tier.
- [ ] **Agent ROI audit** — Track which agents produce actionable output vs noise. HANS and ZHAO are candidates for consolidation or demotion to monitoring-only.
- [ ] **Section max lengths in STATUS.md** — Define per-section token budgets (e.g., dashboard 40 lines, thesis 20 lines, predictions 25 lines).
- [ ] **Error propagation audit** — Trace a key number (e.g., HY OAS 298bps) through the chain. Did every agent that references it get the same value? Any drift?

## ❌ NOT DOING (Overkill for Our Scale)

- LLM-as-judge spawn evaluation ($0.02-0.05 per eval, not worth it at 11 agents)
- Spawn quality log in STATUS.md (we can eyeball at our scale)
- JSON/YAML structured data store (Level 3) — Level 2 structured markdown is sufficient
- Vector database / embeddings (Level 4)
- Trajectory evaluation tools (Langfuse/LangWatch — designed for API systems)
- Full A2A protocol (enterprise-grade, we just need SIGNALS.md)

---

## Key Principles (From Research)

1. **Lightweight > heavyweight.** <3K token CLAUDE.md files get followed. Bloated ones get deprioritized.
2. **Write-back is the primary instruction.** Not an afterthought.
3. **Blackboard > direct signaling.** Agents write signals, orchestrator decides what to act on.
4. **An agent that remembers everything remembers nothing useful.** Prune or die.
5. **Subagents execute, they don't plan.** Task prompts should be explicit step sequences.
6. **The teams that fail skip the maintenance.** Architecture is easy. Discipline is hard.
