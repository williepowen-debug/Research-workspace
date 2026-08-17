# AUTONOMY TIERS

**Created:** 2026-03-25 · **Updated:** 2026-08-09 (spine-audit #8: header git note DEMOTED to a bare pointer per the 8/9 T1-a census pattern — its restated copy carried the pre-8/3 non-ff rule [no `--autostash`, plus the retired "simultaneous-use signature" escalation class that produced a false escalation, CORAL 8/3]; a reader acting on it would falsely escalate routine concurrent pushes. Scope manifest: header note + this stamp only.) Prior: 2026-07-01 PM (de-OpenClaw refresh; git/commit/push autonomy explicitly ceded to root `CLAUDE.md` Git Protocol)
**Purpose:** What Prome can do without asking, what needs approval, and the gray zone.

> **Git / commit / push autonomy is owned by root `CLAUDE.md` Git Protocol** (auto-injected canon — recovery commands and escalation conditions live THERE, deliberately not restated here; demoted to pointer 8/9, spine-audit #8), **not this doc** — don't re-add a git rule here. This file owns the *general* Tier 1/2/3 logic below.
> *(The March-era OpenClaw staleness warning is retired — this file was de-OpenClaw refreshed 2026-07-01. Tier logic unchanged; capability examples now current.)*

---

## Tier 1 — FREE (no approval needed)

These are internal actions that don't change thesis, don't touch positions, don't edit other agents' files, and don't go external.

- Read any file in the workspace
- Search the web for public information
- Update Prome's own state: `PROME/` docs (STATUS, SCRATCH, HANDOFF, etc.) + `memory/YYYY-MM-DD.md` + auto-memory
- Scan/triage to-PROME signals (`AGENTS/*/outbox/*to-PROME*` at boot) and Prome's own intake; route operational **task packets** to domain agents. *(WALTER owns signal/news routing; cross-agent **inbox** writes are exception-only, Will-authorized — `[[feedback_cross_agent_inbox_writes]]`.)*
- **Flag** stale/erroneous content in another agent's files to its owner (SIG/packet) — *editing* another agent's files is Will-scoped per root canon, not Tier 1 *(March-era "fix any agent file" grant removed 7/1 — it contradicted the live "no agent domain edits unless scoped" constraint)*
- Archive resolved Prome items to `PROME/archive/` (rotation discipline: HANDOFF, drafts, served-purpose reports)
- Cross-reference and link existing research
- **Build architecture required by in-progress work** (e.g., signal processing needs a folder → build it, don't stop to propose)
- **Follow-up spawns within an already-approved workstream** (same direction, not new direction)
- **Research/verification sub-agent spawns** (read-only fan-outs, verify passes) — report at closeout, not per-spawn. *(Full revival/catch-up programs are Tier 2 below.)*
- **Prome inbox triage** — reading, summarizing, and archiving Prome's own intake. Housekeeping, not a proposal.

**Visibility rule:** Tier 1 work is done freely and batched into the **closeout synthesis** (HANDOFF/SCRATCH update + Will-facing summary) rather than individual mid-session FYI pings. Exception: if a Tier 1 action surfaces something unexpected or thesis-relevant, flag it immediately.

---

## Tier 2 — PROPOSAL REQUIRED

These change structure, create new work streams, or have cost implications.

- **New research folders/architecture that are NOT required by in-progress work** (proactive structure changes)
- **New agent spawn for research** (costs tokens, takes time)
- **New tracking frameworks** (new TSVs, new monitoring protocols — note the data-hygiene FROZEN/LIVE ledger rule in root `CLAUDE.md`)
- **Protocol changes** (modifying how agents operate, new rules)
- **Thesis-level conclusions** (upgrading/downgrading confidence, changing scenarios)
- **Cross-agent signal routing** that changes an agent's priority or focus
- **Reviving / catching-up stale agents** (revival packets, multi-agent catch-up spawns — high cost; `[[finding_revival_proxy_pattern]]`)

---

## Tier 3 — ALWAYS ASK

These are never autonomous regardless of trust level.

- Anything external (emails, messages to people, public posts)
- Position recommendations or trade proposals
- Deleting files (trash > rm, but still ask)
- Modifying `AGENTS.md` core sections (roster / routing / spawn rules) or other agents' core/identity docs
- Spending money (API calls with cost, marketplace purchases)
- Contacting anyone on Will's behalf

---

## Gray Zone

When unsure, ask yourself:
1. **Is it reversible?** → Lean toward Tier 1
2. **Does it create new ongoing work?** → Tier 2
3. **Could Will disagree with the direction?** → Tier 2
4. **Does it touch the outside world?** → Tier 3

---

## Trust Evolution

This doc should get MORE permissive over time. As patterns emerge (in the Change Log below + HANDOFF / daily `memory/` records):
- If Will approves the same type of proposal 5+ times → consider moving to Tier 1
- If Will rejects a category consistently → note it here as "don't propose"
- Review quarterly (or when it feels stale) — **last full review: 2026-07-01 (this refresh)**
- **Behavior-changing grants/revokes also propagate to the auto-loaded `PROME/CLAUDE.md` Ask-First section** (that's what's actually read every boot) — log here, mirror there.

**Trust goes both ways.** Track demotions too — if Prome screws up a Tier 1 action and it should've been Tier 2, log it. Accountability builds trust faster than optimism.

### Autonomy Change Log
| Date | Change | Direction | Reason |
|------|--------|-----------|--------|
| 2026-03-25 | Initial tiers created | — | — |
| 2026-03-25 | Mid-flow architecture → Tier 1 | ⬆️ Promotion | Stopping to propose kills momentum during signal processing |
| 2026-03-25 | Follow-up spawns (same workstream) → Tier 1 | ⬆️ Promotion | Pre-authorized by design — new direction still Tier 2 |
| 2026-03-25 | Tier 1 FYI receipts (early phase) | 📋 Process | Over-communicate until trust calibrates |
| 2026-03-26 | AGENT OPS spawns → Tier 1 | ⬆️ Promotion | 17/17 approvals across 2 sessions. Zero rejections. |
| 2026-03-26 | Prome inbox triage → Tier 1 | ⬆️ Promotion | Housekeeping, not proposal-worthy. |
| 2026-06-26 | Signal/news routing → **WALTER-owned** (Quick-WALTER retired) | ➡️ Ownership move | WALTER owns ingest/filter/dedupe/route; Prome = operational tasking + Will-facing synthesis |
| 2026-06-26 | Commit-local + **auto-push at closeout** → root `CLAUDE.md` Git Protocol | ⬆️ Promotion | Will-approved after soak; push-train automated (`safe-push.sh`, ff-gated) |
| 2026-07-01 | Non-ff push abort = **routine rebase** (serial multi-machine amendment) | ⬆️ Promotion | Root Git Protocol amendment, Will-approved — was "stop, flag Will" |
| 2026-07-01 | Tier-1 "refresh/fix any agent file" grant **removed** | ⬇️ Demotion | March grant contradicted the live "no agent domain edits unless scoped by Will" constraint; flag-to-owner replaces it |
| 2026-07-01 | De-OpenClaw refresh (HERMES cron, KB.tsv logging, 250-line prune, Session Report → retired/replaced) | 📋 Process | 24-file PROME .md audit (Will-approved hygiene pass); mechanisms without live substrate removed |
| 2026-07-30 | **FORGE ownership → PROME** (commits PROME-standard; reconcile-class work via ANVIL spawns; root-doc FORGE *lines* stay Will-gated) | ⬆️ Promotion | Will-ruled, DAEDALUS FORGE-audit S1 disposition (PAT-071). ⚠️ *Row logged 2026-08-16 S4, 17 days late — DAEDALUS sweep-1 item 6 caught the grant in root canon + practice (`7318799c4`) but in NEITHER this log NOR the Ask-First mirror, violating this file's own "log here, mirror there" rule. Both reconciled same commit.* |
