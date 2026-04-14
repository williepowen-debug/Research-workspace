# WALTER MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to design docs/CLAUDE.md or delete, never just accumulate.*

*Distinct from STATUS.md (operational state) and LAST_COMPLETION.md (latest session's deliverables). This file holds durable learnings that shape how WALTER works, not what WALTER did.*

---

## Feedback

- [2026-04-07] Will directed iterative COP architecture ("treat this as a living process, iterate as we learn") rather than comprehensive upfront design. Apply: ship Layer 1 before designing Layer 2/3 in detail.
- [2026-04-07] Will raised achievability concern on elaborate workflows — scoped realistic cycle: boot → read STATUS files → update COP → write signals → ping Telegram if FLASH → done. Apply: when proposing new infrastructure, budget against the real session cadence, not the theoretical capacity.
- [2026-04-10] Will challenged duplication on SIG-001/SIG-002 draft pair. "One file per action recipient" in FORMAT_SPEC means dispatch mechanics, not content splitting. Apply: never split the same underlying data into multiple signals because different agents care about different angles — frame it once, route to multiple recipients via to/info fields.
- [2026-04-11] When uncertain about canonical source for a spec change, ask before editing dependents. Canonical-source-first rule added to CLAUDE.md as Rule 8 + canonical-source lookup table. Apply: before modifying any design doc, check the lookup table to find the owning doc, edit there first, then propagate.
- [2026-04-14] Will's preferred push-vs-pull threshold: FLASH only direct-to-inbox; everything else archive-only. Apply: Signal archive at `signals/` is the default destination. Only FLASH bypasses to recipient inboxes + Telegram.
- [2026-04-14] When asked "is the architecture built correctly?", give honest POV not reflexive agreement. Will wants the real answer, not the comfortable one. Apply: when Will frames a question as "I'm just asking," he still wants a genuine recommendation.

## Findings

- [2026-04-11] `/COP.md` existed on disk since Apr 7 (commit 62eb644a) while NEXT_SESSION.md claimed it didn't. **Trust disk over memory.** Run `ls` on the file before believing a handoff doc that says something doesn't exist.
- [2026-04-11] Stale-agent flagging in the registry is the single highest-leverage boot output. Agents with Status/Updated/Focus columns >5 days old should be surfaced explicitly, not buried in the STATUS table — drives RED/HAWK/NEXUS refresh cycles.
- [2026-04-11] SAM pioneered `git pull --rebase --autostash` for dirty-tree cases. Autostash captures tracked changes only; leaves untracked files (other agents' new work) untouched. Safer than manual `git stash push --`.
- [2026-04-13] Islamabad talks outcome was a multi-agent delta (SAM/HAWK/BRENT/LIQUID/HENRY all had to reprice). A single geopolitical event can invalidate multiple COP domains simultaneously — flag convergent changes explicitly in the refresh.
- [2026-04-13] FORGE/STATUS.md staleness (now 19 days) has operational cost: every COP requires an Exposure caveat, and any trade approval flows through stale position data. Escalating to Will is overdue after Prome flag went unanswered.
- [2026-04-14] `outbox/` doing double duty as drafts + archive is an architectural bug at scale. Fixed Apr 14 — drafts in `outbox/`, dispatched signals in `signals/` as append-only archive.

## References

- **Root `CLAUDE.md`** — git protocol (commit/push steps), agent lifecycle rules, cost model, hierarchy of 🟢/🟡/🟠/🔴 status keys.
- **`AGENTS/WALTER/CLAUDE.md`** — spawn protocol, canonical-source lookup table, the 8 RULES, closeout checklist including 11a-11f git steps.
- **`AGENTS/WALTER/design/`** — all spec docs. Change FORMAT_SPEC first for signal-schema changes, ROUTING_TABLE for routing, FILTER_SPEC for filter, CHECKLIST for process.
- **`AGENTS/WALTER/research/distilled/`** — the 10 distilled principles (ESI triage, military messaging, ATC, pub/sub, IC dissemination, emergency dispatch, scientific alerts, open output systems, newsroom editorial, trading desk). Source material for all architectural decisions.
- **`/COP.md`** — live at repo root. Refreshed each WALTER session. Template at `design/COP_TEMPLATE.md`.
- **Market data:** `.venv/bin/python3 FORGE/tools/market-data/dashboard.py` (needs venv, not system python).

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 13 → Apr 14)
- Telegram MCP disconnected mid-session. No direct delivery to Will until reconnected.
- LAST_COMPLETION.md created (first structured closeout record for WALTER).
- Git closeout in CLAUDE.md tightened to numbered 11a-11f checklist.
- Signal archive built at `signals/` with INDEX.md.
- SIG-001 moved from `outbox/` to `signals/`. Outbox now empty (correct state — no drafts in flight).
- MEMORY.md created (this file). WALTER now matches SAM's file structure.

### NEXT SESSION
1. **Refresh COP** — Islamabad-post network state will have moved (SAM/HAWK/BRENT/LIQUID/HENRY expected to reprice).
2. **RED result integration** — Will is booting RED to process Apr 10 falsification. Expect RED/STATUS.md refresh. Route thesis-confirmation signal to info-recipients if RED shifts confidence materially.
3. **FORGE escalation** — if still stale at Mar 25, escalate to Will directly (Prome flag from Apr 11 went unanswered).
4. **Network boot sequence decision** — still pending Will's approval to roll "read `/COP.md` + WALTER signal archive" into other agents' boot protocols. Blocker for full pull-model activation.
5. **SIGNAL_INTAKE.md rollout** — only SAM + BRENT have subscription specs. Other Tier 1 agents need them for keyword-matched routing to work at scale.

### OPEN DESIGN DECISIONS (need Will)
- COP refresh cadence: WALTER-only, or also Prome-triggered?
- Signal archive boot-read: mandatory for all Tier 1 agents, or opt-in?
- Filter model v1→v2 review trigger: 10 dispatches or 30 days — currently at 3 dispatches, target ~May 11.
