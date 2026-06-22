# YEYOU — STATUS

**Updated:** 2026-06-22 (scaffold — not yet live) | **Runtime:** GLM (Z.ai) on VM | **Phase:** 1 (digest-to-PROME only)

> Review agent (meta). Exempt from domain-agent sections (Convergence Matrix / EXIT / TRADE) — those are for market-domain agents. YEYOU's "dashboard" is the finding ledger at `reviews/REVIEW_LOG.tsv`.

---

## State

🟡 **SCAFFOLDED** — files created, not yet running. Pending before first live run:
1. GLM (Z.ai) runtime wired on the VM (persistent, scheduled to wake on new pushes).
2. Roster registration — `AGENTS.md`, `AGENTS_DIRECTORY.md`, `AGENTS/_INDEX.md`, `AGENTS/_NETWORK.md` (shared files → Will/PROME, not YEYOU).
3. Baseline watermark chosen (recommend: current HEAD, so YEYOU reviews only *new* pushes, not full history).

## Watermark

None yet. First run starts from the Will-chosen baseline commit forward (see `reviews/STATE.tsv`).

## Open findings

None (not yet run).

## Escalation budget (today)

Direct inbox writes used: 0 / 2 per agent. **Phase 1 = digest-to-PROME only; no direct agent writes.**

---

## BOTTOM LINE

YEYOU is scaffolded as the GLM half of the Codex+GLM review funnel: review each agent's diff on push for **discipline + internal consistency**, log findings to the ledger, escalate 🔴 blockers to PROME, and send PROME a consolidated digest. Not live until the GLM runtime is wired and Will registers it in the roster. Next: wire runtime → pick baseline watermark → first review pass on the next batch of agent pushes.
