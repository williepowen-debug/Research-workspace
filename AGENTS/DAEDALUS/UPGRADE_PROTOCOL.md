# DAEDALUS Upgrade Protocol — section-at-a-time

> Note (2026-07-22): profiles may carry a **Δ refresh-at-touch banner** (Production Review playbook path) — deltas banked in the review report, full refresh deferred to the next firming touch. A Δ-bannered profile is NOT a Step-0 violation; read profile + banked deltas together.

**Owner:** DAEDALUS · **Created:** 2026-06-27 (Will: "the job is too big to upgrade a whole agent in one go — one section at a time")

> **The upgrade unit is `one agent × one blueprint section` — never a whole agent at once.** A whole-agent rewrite is a giant diff: hard to review, hard to approve, impossible to roll back cleanly, and it fights every principle we set (batch-approval, additive handles, floor-not-ceiling). A "CORAL upgrade" is not one job — it's a *queue* of small section-tasks, done independently, in priority order.

---

## Why section-at-a-time

- **Reviewable:** one section = one small before/after Will can actually check.
- **Approvable:** one section = one batch-changelist (PAT-005), one decision.
- **Reversible:** if a section change is wrong, it's isolated.
- **Respects floor-not-ceiling (PAT-015):** each section is judged on its own — "does this section even apply to this agent?" — so we never force-fit a whole template.
- **Concurrency-safe (PAT-004):** small idle-window edits, or one task-packet per section to a live agent.

## Step 0 — COMPREHEND first (prerequisite for heavy agents)

**You cannot section-task an agent you don't understand, and you can't hold a heavy agent in one context.** Before any upgrade work, build (or refresh) the agent's **Profile** — `profiles/<AGENT>.md` (template: `profiles/_TEMPLATE.md`). It maps the labyrinth: file anatomy, where the richness lives, how the agent expresses each dimension in its own words, and what not to touch.

- **How to build one on a heavy agent:** fan-out readers over file-clusters (Mode-A), each returning a structured profile-slice → synthesize into one compressed, faithful Profile. (Same method as the best-practices harvest.)
- **Then every section-task reads the relevant Profile slice**, not the raw heavy agent — the Profile is the durable understanding that makes section-by-section feasible at scale.
- The Profile is compressed; when you actually *apply* a change, re-read the specific file (PAT-009: don't trust a summary for the edit).

Flow per agent: **COMPREHEND (profile) → DECOMPOSE (upgrade card) → SECTION-TASKS.**

## The section-task lifecycle (7 steps)

For one agent, one blueprint section (operating against the Profile from Step 0):

1. **READ** — current state of that section in the agent, *including where its richness lives* (e.g. `thesis/THESIS.md`, `COVERAGE.md`). Don't grep STATUS only (PAT-009).
2. **GRADE** — vs the blueprint section. Classify the gap: **missing handle** (cheap, additive) vs **missing substance** (real work) vs **conformant**.
3. **JUDGE — does it apply?** Floor-not-ceiling: a transmitter may not need a full convergence matrix; a utility agent has no TRADE.md. Mark `N/A`, `ADAPTED`, or `APPLIES`. *Never force.*
4. **PROPOSE** — the *minimal additive* change. Add the comparable handle; keep all local richness. Before/after, ≤ the smallest diff that closes the gap.
5. **APPROVE** — Will signs off (batch per agent, or per section).
6. **APPLY** — only if the agent is **idle**; else route a task-packet to its `inbox/`.
7. **RECORD** — update the agent's `FLEET_MAP.tsv` row; log any new design lesson to `PATTERNS.tsv`.

## The artifact: an upgrade card

Per agent, an `upgrades/<AGENT>_CARD.md` — the 8 blueprint sections as rows: `current state | applies? | gap type | proposed handle | priority | status`. The card IS the work queue. Sections are picked off one at a time, never batched into a rewrite.

## Priority order (which section first)

1. **Quick wins** — high value, low effort, unambiguously additive (BOTTOM LINE, session counts).
2. **Judgment calls** — high value but need an applies?/adapt decision (convergence handle on a transmitter).
3. **Builds** — real substance to add (prediction ledger, threshold bands).
4. **Polish** — disciplines, routing refinements.

Do quick wins first: they prove the method cheaply and raise the floor before the hard calls.
