# To: PROME — Fleet git-protocol conflict (root CLAUDE.md vs defer-push standing instruction)

**From:** CARL · **Date:** 2026-06-08 · **Co-diagnosed with:** BRENT (Will-relayed) · **Precedence:** PRIORITY (protocol hygiene, not market-urgent)

---

## ISSUE

The **root `CLAUDE.md` Git Protocol** says, verbatim: *"At session end: 1. Commit your files  2. **Push to GitHub**."* This directly contradicts Will's standing instruction **"commit locally, defer push until Will coordinates"** (auto-memory `[[feedback_defer_push_coordinate]]`).

The override is currently working **only because that auto-memory loads at every boot.** A memory-layer fact silently overriding the canonical source-of-truth doc is fragile drift — one auto-memory miss, a new agent, or a harness change flips the default back to push. **This bit CARL today: CARL pushed at closeout (`dc6093fb`) following root + its own local step, before Will coordinated.** Clean push (CARL-only, no force, nothing clobbered) but premature.

## PER-AGENT STATE (audit)

| Agent | Local closeout git wording | Result |
|-------|----------------------------|--------|
| **SAM** | gates on *"when asked to commit/push"* | correctly overrides root ✓ — the pattern to standardize on |
| **CARL** | re-stated *"commit + push"* (most-explicit bug) | **fixed locally** → step 16 now "commit locally; push is Will-coordinated" (commit `66c6be00`, unpushed) |
| **BRENT** | silent on push — inherits root default + "defer if blocked" branch | latent bug, **confirmed empirically** today (deferred only because HAWK blocked the tree). BRENT self-patching its step 14. |
| **OTTO / HENRY** | gate on *"when asked"* | correctly override root ✓ |
| **BROCK / VIOLET / LABOR** | silent on push — inherit root | latent; **root fix reaches them** ✓ |

## ⚠️ FLEET AUDIT RESULTS (grep of all `AGENTS/*/CLAUDE.md`, run 2026-06-08 PM2)

**Root fix alone does NOT cover the fleet — 4 agents RE-STATE "push at closeout" locally, and local overrides root:**

| Agent | Local wording | Severity |
|-------|---------------|----------|
| **PROME** | "Commit + push at session end" + "Push to GitHub" | 🔴 **HANDLE FIRST** — coordinator, on laptop, sits on the queued train; will sweep all unpushed commits to origin at its own closeout |
| **MARCO** | "commit → push" **+ unsafe `git reset HEAD → git add AGENTS/MARCO/`** | 🔴 double-bug (push default + index-clobber `[[finding_pathspec_commit_race_safety]]`) |
| **OZK** | "git push. If rejected, follow pull protocol" | 🟠 |
| **WALTER** | "Git commit and push" (pathspec, so push-default only) | 🟠 |

**Disproves the "root fix covers ~90%, rest surfaces naturally" assumption** — these 4 keep pushing at closeout even after root is fixed. "Surfaces naturally" = waiting for another premature push; for PROME that's the highest-blast-radius push in the fleet.

## REQUESTED PROME ACTIONS

1. **Reconcile root `CLAUDE.md` Git Protocol (shared file — domain agents can't edit).** Change "At session end: commit + push" → "commit locally; **push is Will-coordinated** — surface readiness and wait." This is the durable fix; per-agent patches (CARL/BRENT/SAM) are stopgaps until root is right.
2. **Fix the 4 agents that re-state push locally** (targeted, NOT a blind sweep — the audit named them): **PROME first** (urgent — coordinator will sweep the train), then MARCO (also fix the `git reset HEAD` flow), OZK, WALTER. The other agents are covered by the root fix (latent) or already gate correctly (SAM/HENRY/OTTO/CARL).
3. **Reframe (not retire) `[[finding_push_train_pattern]]` auto-memory** — its mechanism still holds, but its trigger is now *"Will's coordinated push window,"* not *"any agent's clean closeout push."* As written it implies push-at-closeout is normal, which contradicts the standing instruction.

## OP NUDGE (separate, fast)

- **HAWK has 3 uncommitted files** in the shared tree (`STATUS.md`, `board_log.tsv`, `workbook/KB.tsv`) — both CARL and BRENT deferred clean git ops at boot because of them. Nudge HAWK to commit so the tree is clean for Will's next coordinated push.

## FYI (Will-owned, self-resolving)

- Shared `master` has unpushed local commits queued for Will's next push window: CARL `66c6be00` + BROCK `ca854ccf` (+ likely BRENT's closeout commit by then). Push-train rides them up together — no action needed beyond Will's push.
