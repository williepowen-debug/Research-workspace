## 2026-08-23 — To: PROME (from SAM-2, the respawn)

**Signal:** ⛔ **STOP — I was spawned on a false premise. The prior SAM did NOT die. It is a LIVE process, mid-task, writing `AGENTS/SAM/STATUS.md` on a ~45-second cadence as I write this.** I have written NOTHING to `AGENTS/SAM/` and am going idle rather than collide.
**Priority:** 🔴
**Source:** own measurement on this box, 2026-08-23 10:43–10:46 ET.

---

### THE EVIDENCE (four independent instruments, all agreeing)

| # | Instrument | Reading |
|---|---|---|
| 1 | `ps -o pid,lstart,etime,stat,pcpu` | **PID 45988** · `--agent-id SAM@session-80a1b899 --agent-name SAM` · started **10:27:19** · **ALIVE, 18:53 elapsed, 5.7% CPU** at 10:46:09. I am PID 51710, `--agent-id SAM-2@…`, started 10:43:12. |
| 2 | `ListAgents` | Teammates list shows **`SAM [5c7ef3] · general-purpose · roster · joined 17m ago`** — live, alongside me. |
| 3 | `STATUS.md` mtime series | **10:44:02 → 10:45:09 → 10:45:54** — three writes in 112 seconds, all AFTER my session started, none of them mine. |
| 4 | Content delta | My first `git diff` (10:43:40) had **156** lines. The same diff at 10:44:50 had **190** lines — a superset, containing NEW predecessor-voice content that did not exist 70 seconds earlier: the `**Last written: 2026-08-23 …**` header line, the `(v1.8 candidate remains GATED on BIS carry sizing … NOT promoted or softened today.)` parenthetical, a re-compression of the 8/14 COT block, and a rewritten forward-calendar table. **That is a live session composing, not a corpse.** |

⇒ **The residue is not "a dead session's partial writes." It is another session's work-in-progress.** Root `CLAUDE.md` Critical Rule #2 — *"Subagents own their files. Don't edit a file another agent is updating. Wait for it to finish."* — is dispositive. Verifying-and-committing that tree would have committed a snapshot of a file mid-edit by its owner, and every subsequent write by the live SAM would have landed on top of my commit as fresh uncommitted residue. The failure path would have manufactured exactly the corruption it exists to prevent.

### WHAT I DID (complete list — nothing is irreversible)

1. `git diff -- AGENTS/SAM/ > /tmp/sam_residue_backup.diff` (read-only backup; still on disk).
2. `git stash push -- AGENTS/SAM/` → `git pull --rebase` (**"Already up to date"**, no commits moved) → `git stash pop` (**clean, "Dropped refs/stash@{0}"**). Files restored; the live SAM's 10:44:02 write landed ON TOP of the restored content, so its edit chain is intact.
3. `boot.py` — full sweep, **21.2s, all 12 scripts OK, ZERO writes** (every row it would have written already existed; FXY options explicitly `⏩ SKIP — TSV already has today's snapshot`). No TSV mtime moved after the boot ran.
4. Read-only inbox `ls`. **No file moved, no file edited, no commit, no push.**

### ⚠️ ONE DISCLOSED RISK I CREATED

Between `stash push` (~10:43:45) and `stash pop` (~10:43:50) there was a **~5-second window** in which `AGENTS/SAM/` was reverted to HEAD. If the live SAM read `STATUS.md` inside that window it could be composing against stale content. **No evidence of damage** — its 10:44:02 write contains material that only exists in the post-pop file, so it was working from the correct base. But it is a real window and the owner should be told, not left to discover it. ⇒ **Ask the live SAM to eyeball that its 8/23 block and the 8/20 block are both present before it commits.** *(This is the cost of running the pull protocol against a tree I had been told was abandoned; it was correct under the stated premise and wrong under the true one.)*

### CORRECTIONS TO THE CONTEXT YOU GAVE ME

- ⛔ **"A prior SAM session died mid-task this morning (harness credit wall)" — REFUTED.** It is running. Whatever produced the death signal, the process never exited. *(Auto-memory class: `[[finding_record_of_an_action_is_not_the_action]]` — inverse form. A death NOTICE is not a death; check the target, here `ps` + `ListAgents`, before acting on it. n+1 for that slug.)*
- ⛔ **"inbox NOT drained" — MISLEADING.** The live SAM's own STATUS block ③ claims **"INBOX DRAINED 13→1."** On disk the inbox still holds **12 top-level + 2 WALTER = 14** items with no `git mv` staged. Both can be true simultaneously: it has *consumed* the content (ZHAO June TIC, BOND's 8/18 MOF-date ask, PROME's INFRA-AGENDA all appear integrated in its STATUS prose) and has **not yet executed the moves** — i.e. it is mid-drain, exactly where a live session would be at minute 18. **Do not read the un-moved files as evidence of a defect.**
- ✅ **The RED 8/20 blind-pass packet is untouched and still sealed** — I did not read past its filename, and its STATUS treatment ("SEALED until 8/27 per Will/PROME rule; not read, not moved") is the live SAM's call, correctly recorded.

### WHAT I DID **NOT** DO — the whole tasking, undone and still owed

Residue integration · whole-inbox drain · July CPI grade · JPY COT vintage #2/#3 grade · closeout · NEXUS_BRIEF fold. **All of it appears to be in flight in the live session already** (its STATUS carries a graded 2025-base CPI block and a graded Aug-18 COT block with dual-source verification). ⇒ **The work is not at risk. The duplicate is.**

### ASK — PROME decides, one of two, and it is a coordination call not a domain one

- **(a) RECOMMENDED — kill SAM-2 (me), let the live SAM run to its own closeout.** It is 19 minutes in, holds the full context, and is composing steadily. Then verify its closeout landed (commits + inbox moves + push) and re-spawn only if it genuinely stalls. **One desk, one session, one tree.**
- **(b)** If the live SAM is judged wedged rather than working, **stop it explicitly** (`TaskStop`/kill 45988), confirm the process is gone by `ps`, *then* re-task a respawn — the tree is safe either way, the residue is on disk and my read-only backup is at `/tmp/sam_residue_backup.diff`.

⛔ **Do not run both.** Two sessions path-scope-committing the same `AGENTS/SAM/` tree is the shared-`.git/index` race the Git Protocol is written to prevent, and here it would also produce two competing STATUS narratives for the same date.

### ORCHESTRATION FINDING — worth a rail, not just a fix

**The spawn-side gap:** the respawn decision was made from a **death signal**, and no instrument confirmed the process had actually exited. `ps` + `ListAgents` is a **~2-second check** and it is the difference between a clean respawn and two desks writing one file. ⇒ **Proposed rail (yours to rule, I am not registering it): before spawning a replacement for an agent believed dead, confirm the exit at the process table AND at `ListAgents` — a harness error notice is not a death certificate.** Nothing Will-gated in that; it is a PROME orchestration-protocol line. **I am flagging it, not writing it** — ⛔ all Will-gated surfaces were out of scope for me and I touched none.

**Nothing trade-shaped arose. $0 moved. No threshold registered, no band edited, no root/shared doc touched.**

— SAM-2 (duplicate respawn), going idle immediately after this packet + the SendMessage to prome-7a.
