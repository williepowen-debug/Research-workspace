---
name: Cross-agent inbox writes are exception-only
description: Writing to another agent's inbox/ directory normally violates "subagents own their files"; only do it when Will explicitly authorizes for a specific delivery. Also covers commit-on-behalf-of-offline-recipient orphan-prevention.
type: feedback
originSessionId: cb6074d0-be53-45bd-bb7d-0e0e01061c58
---
When CARL needed to deliver an outbox signal to REGINALD on 2026-05-02 and HERMES wasn't running (messaging-overhaul deferral), Will granted one-time permission to write directly to `AGENTS/REGINALD/inbox/` and commit the cross-agent change.

**Why:** No other Claude Code agents were active in the session, so there was no risk of a write race or stomping on REGINALD's in-progress work. The normal rule (root CLAUDE.md: "git add ONLY files inside your own AGENTS/<NAME>/ directory") and the agent-isolation rule (Critical Rule #2: "Subagents own their files. Don't edit a file another agent is updating.") still hold.

**How to apply (write side):**
- Default = never write to another agent's directory. Use outbox/ and let HERMES (or Will) deliver.
- One-time exceptions are OK only when (a) Will explicitly authorizes the cross-agent write for a specific file, AND (b) no other agents are concurrently active. Both conditions required.
- When delivering an exception: copy file to recipient's `inbox/` (root, not `inbox/processed/` — that's the recipient's classification), and move source to your own `outbox/delivered/` for audit trail.
- Commit cross-agent changes in a single commit with a `<SOURCE>→<DEST>:` prefix in the subject so the cross-boundary intent is auditable.
- Do not generalize from the exception — next time HERMES is down, ask Will again rather than assuming the prior authorization stands.

**How to apply (commit side — orphan-prevention path, added 5/21/26):**

There's a distinct sub-pattern for *committing* PROME-authored cross-agent inbox SIGs that the recipient won't be processing soon:
- **Default after Will-authorized cross-agent write:** leave the file untracked-by-design; recipient commits when they boot and process their inbox.
- **Exception (orphan-prevention):** if recipient won't boot soon and the SIG would sit untracked indefinitely, Will can authorize PROME-side commit on the recipient's behalf. Trigger words from Will: "they aren't working right now," "commit these," etc.
- **When committing on behalf:** stage explicit files only (never broad add), include a commit message that flags (a) per-instance Will authorization, (b) which recipients are offline vs active (active recipients' SIGs stay untracked for them to process), (c) that the SIG's PROVENANCE preamble already noted the authorization.
- **Active recipients' SIGs DO NOT get committed by PROME** — let the active agent process their own inbox per the standard pattern. The exception only fires for dormant/offline recipients.
- Validated 5/21/26: committed 4 SIGs (BROCK ×2, LIQUID, REGINALD — all offline) in one PROME commit; left WALTER SIG untracked because WALTER was actively booted in his own session.
