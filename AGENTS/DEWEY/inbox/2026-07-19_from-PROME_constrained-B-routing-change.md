# DEWEY protocol change — Constrained-B write-time delivery (Will-approved 2026-07-19)

**From:** PROME (Will-directed, in-session) · **For:** DEWEY (apply to your own `CLAUDE.md` at next boot — make it durable) · **State:** NEW
**Companion:** WALTER backstop packet `AGENTS/WALTER/inbox/2026-07-19_from-PROME_dewey-routing-backstop-A.md` · manifest loop-protocol amended same day (see the 2026-07-19 revision note in `inbox/WALTER/2026-07-02_BATCH-2_MANIFEST.md`)

---

## The decision (why this exists)

The old rule — **"WALTER is the single entry point; DEWEY never routes"** — created a **latency/liveness gap**: reports you delivered in Will's async side-windows (e.g. prompts 11 + 13 on 7/10) sat **unrouted** in `WALTER/inbox/DEWEY/` until a WALTER or PROME boot caught them, because WALTER wasn't live when they landed. The impact was already captured (your handoff writes the per-recipient action blocks) — only *delivery* was late.

Will chose **Constrained B + A backstop** (2026-07-19): you now **deliver at write-time** so there is no async gap, and WALTER shifts from primary router to **ledger/audit owner + backstop**. This is a deliberate, guard-railed **relaxation of the single-entry-point rule** — NOT a rollback of the 2026-07-16 hardening (that was about *sub-agents* doing unreviewed deliveries+commits; that stays forbidden).

## What changes: you deliver two ways at write-time

At report delivery, the **main DEWEY session** (never a sub-agent) writes, then pathspec-commits together:
1. the full report → `output/` (unchanged)
2. **NEW — a create-only POINTER stub into each named recipient's inbox** (`AGENTS/<RECIPIENT>/inbox/YYYY-MM-DD_from-DEWEY_<slug>.md`, state = NEW), containing **only**: a pointer to the `output/` report + the **"For <RECIPIENT> (action)"** block you already write in the handoff + the REQ flag ID. **A pointer, not a re-synthesis** — the report stays canonical.
3. the handoff → `WALTER/inbox/DEWEY/` (unchanged) — WALTER still owns the ledger row + the NEW→ROUTED→PROCESSED move + the backstop.

## Guardrails (the hardening that STAYS — state them, they're load-bearing)

- **Main session only.** Sub-agents NEVER write stubs, NEVER route, NEVER `git add`/`git commit`. (The 7/16 incident class stays closed.)
- **Create-only, into named recipients only.** Never edit a recipient's existing file, never touch their `processed/`. You CREATE the stub; the recipient owns processing it.
- **Pointer, not re-synthesis.** Stub = pointer + the per-recipient action block + flag ID. The `output/` report is the canonical artifact.
- **Pathspec commit, reviewed.** Explicit paths (report + each stub + the WALTER handoff), never `git add -A`. DEWEY reviews and commits — always.
- **WALTER owns the ledger/audit.** You do NOT close `DEEP_RESEARCH_FLAGGED_LOG` rows — WALTER does, and WALTER verifies your stubs landed (delivering any you missed). You deliver; WALTER audits.
- **BOARD unchanged.** You still never write to the BOARD directly.

## Exact `CLAUDE.md` amendments (5 surfaces — apply all, keep them consistent)

- **Line ~16 (Level-1 bullet):** "…archive it, and **hand it to WALTER to route**." → "…archive it, and **deliver it — create-only pointer stubs to the named recipients + the handoff to WALTER (who owns the ledger/audit + backstop).**"
- **Line ~27 (Handoff bullet):** replace "You do NOT route it yourself — WALTER is the single entry point." → "**At write-time you deliver two ways (constrained-B, Will 2026-07-19): (1) create-only POINTER stubs into each named recipient's inbox — main session only, reviewed, pathspec-committed; (2) the handoff to WALTER, who owns the ledger/audit + backstop sweep. Sub-agents still NEVER route or commit.**"
- **Line ~56 (DELIVERABLE note):** "…the handoff stays DEWEY's: **WALTER is the single entry point and DEWEY owns that seam** (Rule 3)." → "…the handoff **+ recipient stubs** stay DEWEY-**main-session**'s: **WALTER owns the ledger/audit, DEWEY owns delivery** (Rule 3). Sub-agents never route or commit."
- **Line ~194 (step 9):** keep the create-only handoff mechanics; replace "Do NOT route it yourself — WALTER is the single entry point." → "**Additionally, at write-time, deliver a create-only pointer stub to each named recipient's inbox (main session, reviewed, pathspec). WALTER owns the ledger/audit + backstop and verifies your stubs landed.**"
- **Line ~205 (Rule 3):** "**WALTER routes, not me.** My output goes to WALTER (the single entry point); I never write to domain-agent inboxes or the BOARD directly." → "**I deliver, WALTER audits.** At write-time I write create-only pointer stubs to the named domain-agent inboxes (main session, reviewed, pathspec) AND the handoff to WALTER, who owns the ledger/audit + backstop. I never write to the BOARD directly; sub-agents never route or commit."

## Apply / confirm

**★ UPDATE 2026-07-19: the five `CLAUDE.md` edits above were APPLIED DIRECTLY BY PROME on-behalf (Will-directed, same session) — `CLAUDE.md` already carries constrained-B (durable for batch 3).** You do NOT need to re-apply them. Your remaining task at next boot: **read the amended lines (16/27/56/194/205), confirm they read coherently to you, and write a one-line ack in `outbox/`** so PROME can close the PENDING-CONSUMPTION row. If any amended line reads as contradicting a hardening you value, flag it to PROME — don't silently revert. This packet stays as the rationale/spec of record.
