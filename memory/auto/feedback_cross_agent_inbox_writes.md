---
name: Cross-agent inbox writes are exception-only
description: Writing to another agent's inbox/ directory normally violates "subagents own their files"; only do it when Will explicitly authorizes for a specific delivery. Also covers commit-on-behalf-of-offline-recipient orphan-prevention.
type: feedback
symptoms: "leave it untracked for the recipient to commit"; SIG sits in another agent's inbox as ?? in git status; packet "delivered" but absent on the other machine; class declared closed on one box while untracked residue sits on the other
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

---

## ⚠️ SUPERSEDED on the commit side (appended 2026-08-28, PROME — read this before the 5/21 section above)

**The 5/21 default — *"leave the file untracked-by-design; recipient commits when they boot"* — is DEAD canon.** Root `CLAUDE.md` **carve-out ①** (ratified 2026-07-23, Will-approved, HENRY orphan-gap memo: ~12% of packets orphaned this way) reversed it: **a packet you authored into another agent's inbox is YOURS to commit, and you MUST** — the author's commit is the delivery guarantee. Will re-affirmed it 2026-08-27, verbatim *"row 102 ruled (a)"*, when an agent-local line carrying the old default (`AGENTS/OTTO/CLAUDE.md:213`, *"never commit it"*) orphaned four 🔴 signal packets in one day; record `PROME/proposals/2026-08-27_row102-carveout1-vs-otto-local-RULED-a.md`. The 5/21 section stays above as history of where the untracked-by-design idea came from — do not apply it.

**Instance n=1 of the mechanism the old default hides (2026-08-28):** untracked files are **machine-local** — they never travel across Will's serial desktop⇄laptop switch. The row-102 execution ran on the laptop and committed "the two currently-untracked drops" it could see; the ruling record itself counted FOUR packets, but the other two (OTTO s019, written on the desktop 8/27 19:51/20:20 — First Brands conf-denied→Ch7, SEC v. Chu/OBK board seat) were invisible from the laptop, so the class was recorded closed at 2/4. Found at the desktop's next boot as `??` in `git status`; committed via a PROME Tier-1 OTTO spawn (`015f977cc`). **A "class closed" verdict about untracked files is a claim about ONE box.** Pairs with [[finding_record_of_an_action_is_not_the_action]] (execution report ≠ class closure) and [[finding_dirty_path_means_in_flight_not_orphaned]] (the boot-banner `??` at a machine switch with NO live session is the orphan case, not the in-flight case — check `ListAgents` and the file's closer before deciding).

**How to apply now:** author commits its own cross-agent packet at authoring, explicit pathspec, recipient named in the subject (`<YOU> -> <RECIPIENT>: <what>`). A pointer packet is a delivery REPAIR for an interval where the author could not commit (the OTTO:213 conflict) — it is retired for future drops (ruling step 3). If a boot banner shows `??` in another agent's inbox with no live session on the box, the file is an orphan: the owner-desk commits it (Tier-1 spawn if dark), never PROME directly, never a sweep.
