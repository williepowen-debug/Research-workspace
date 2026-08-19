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

> **★ MANDATORY COMPANION — persist the reader deliverables (PAT-100, adopted 2026-08-12).** Every Mode-A fan-out writes a `*_READER_REPORTS.md` beside its synthesis carrying **(a)** each reader's raw tables verbatim, **(b)** a pointer map of where each slice landed, **(c)** **every reader's not-read / coverage-limit list.** **CONTRACT = the FILENAME AND the substance, disambiguated 2026-08-17 (self-audit F31 — the 8/17 SAM+BRENT 6-reader review was substance-compliant under six ad-hoc names, so any filename-keyed check misreads it as a miss; and the war-triad shipped a companion with NO synthesis beside it — the pair inverted):** the canonical `<TOPIC>_READER_REPORTS.md` name is REQUIRED; an enumerated-cluster form (per-reader files) is allowed ONLY with an index stub under the canonical name listing every cluster file. Both halves of the pair must exist beside each other — a companion without a synthesis is as non-compliant as the reverse. Pre-2026-08-12 fan-outs are grandfathered (their records say so via the 8/17 banner pass). The synthesis alone is NOT persistence: conclusions land in files while the evidence and coverage limits die with the session — and that failure is *selective*, so the output looks complete and survives a self-check. **(c) is the expensive half:** once conclusions are summarized, nobody can see what was never checked, and the next pass trusts cells nobody verified. **Corollary: a reader's flagged caveat is a BLOCKER on the claim it qualifies, not a footnote under it** — resolve it before the claim leaves your desk (8/12: a forwarded REG-T claim carried an explicitly-flagged unresolved caveat; checking it inverted the finding). *(n=3 — 8/11 DARK_CENSUS, 8/11 PAT-093, 8/12 RED audit — every one found by Will asking, never by my own closeout.)*
>
> **★ ROUTING RECONCILIATION (PAT-102, adopted 2026-08-12).** When a fan-out feeds more than one output surface — the usual case is a **profile** (comprehension) plus a **packet** (the owner's fix-list) — reconcile the owner-facing surface against **each reader's own ranked route list, item by item, before shipping.** The readers sort their findings by what needs routing; that ranking IS the checklist. **Do not dedupe against "did I capture this?" — dedupe against "did this reach the owner?"** A finding filed in the durable layer *reads as handled* and will survive repeated completeness passes untouched (8/12: six findings, incl. a reader's own ranked #4, sat in `profiles/RED.md` through four audits and never reached RED). Distinct from PAT-100: there the evidence died; here the evidence lived and the **routing** died.
>
> **Reader-ops floor (measured, 10-of-12 across three fan-outs):** readers idle holding their results even with an explicit deliver-before-idle instruction in the prompt. **The instruction does not work; the chase does.** A fan-out is not complete when the spawns return — chase every silent reader.

> **★ RUN THE SUBJECT'S GUARDS — BOTH DIRECTIONS — RATHER THAN READING ITS VALIDATION CLAIMS (adopted 2026-08-19, VIRGIL review; the highest-yield hour of that session).** `CHECK_STANDARD` §3 and the charter's ★ rule are written **self**-directed — *don't ship your own guard unverified*. Point them **outward** at the agent under review: a validation claim in a doc is a claim, and executing it is usually minutes.
>
> **The one-direction trap:** "66 tests, validated 66/66" was TRUE, and proves only that the reference agrees with the tests. **It says nothing about whether the tests catch a wrong answer.** The second run — 66/66 **fail** on the stub — is what establishes the instrument DISCRIMINATES, and it is the run nobody documents. Ask of any subject's check: *what does its PASS prove, and what did I watch FAIL?* (PAT-074, applied outward.)
>
> Three more from that session, all cheap: **(a)** a claimed redundancy/backup mechanism — check it has actually RUN (artifacts on disk), not merely that it exists; **(b)** a claimed downstream CONSUMER — grep for it, because a phantom reader named in two files is indistinguishable from a real one *(VIRGIL: no such consumer existed, and a third file asserted the opposite)*; **(c)** a teardown/reset path — the state it leaves behind decides whether the NEXT run is valid, and a silently-invalid run poisons the ledger it feeds.
>
> ⚠️ **Expect to be wrong sometimes and record it.** I predicted VIRGIL's harness would render a silent `0/0` on a broken module; it renders `0 passed, 4 errored` and is never falsely green. **A refuted hypothesis about the subject is a result — write it beside the confirmed ones**, or the review reads as uniformly damning and its confirmed findings get discounted with it.

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
