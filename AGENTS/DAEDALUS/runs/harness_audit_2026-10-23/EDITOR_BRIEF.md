# WQ-508 editor brief (DAEDALUS, 2026-10-23)

**Authority.**
- WQ-508 RULED APPROVE: Will, 2026-10-23 10:27 ET, verbatim "ok approved". It covers one batch of instruction-file edits.
- At 10:39 ET Will directed DAEDALUS to apply the desks' lines directly ("Can you make the line changes? Just avoid the agents already spawned (PROME WALTER TERRY)").
- You are applying them as DAEDALUS's editor. Every desk assigned to you was verified idle at 10:4x ET.

**Your input per desk:** `AGENTS/<DESK>/inbox/2026-10-23_from-DAEDALUS_WQ508-harness-audit-lines.md`.
- Section **A** lists lines resolved by ruling R0: no edit.
- Section **B** lists the lines to apply.
- REGINALD and OZK also carry a "Trade-idea wording" paragraph. Apply it as one more line: the desk sends TERRY the trigger state, the evidence and its grade, labelled NOT-FIRED; TERRY's card carries size and risk in figures. Remove any "size and risk" duty from the desk's own packet text.

Raw reader ledgers with fuller context: `AGENTS/DAEDALUS/runs/harness_audit_2026-10-23/READER_*.md`. The 10/08 proposed texts are in `AGENTS/DAEDALUS/runs/2026-10-08_HARNESS_CHANGELIST_A.md` and `_B.md`.

## Rules (hard)

1. **Edit only** the instruction files a row names: `AGENTS/<DESK>/CLAUDE.md`, `CLOSEOUT.md` or `OPERATIONS.md`. Never edit STATUS, workbooks, scripts, inbox files, or any file outside your assigned desks.
2. **No git commands that write.** No add, commit, stash, checkout, restore, reset or mv. Read-only git (diff, log, show) is fine. DAEDALUS commits after reviewing your diff.
3. **Read the file around each line before editing.** Line numbers in the packet are at the time of the audit and may have shifted; locate by the quoted text.
4. **Apply the smallest edit that carries the direction.** The direction is a hint, not paste text. Keep every stricter-and-safe local rule. Never weaken git safety, trade approval (root rules #5 and #10), or any threshold or route.
5. **Under R0, a desk's own packets are delivered direct and self-committed.** If a direction says "send to WALTER" for the desk's OWN threshold fire or analysis, do not apply that part. Apply only the part about naming a real delivery address instead of an outbox nobody collects.
6. **SKIP a row, and record why, when:**
   - it is marked DEFER, or "owner call", "PROME call" or "Will call";
   - it asks for domain judgment (a threshold value, a method choice, which reading of a rule governs);
   - it needs content you cannot verify in the repo;
   - the quoted text is not found.
   Skipping is fine; guessing is not.
7. **Glued words/numbers rows:** insert the missing spaces only ("under32,550B" → "under 32,550 B", "October23" → "October 23"). Do not reword, and stay inside the cited lines.
8. **History-in-step rows:** move the dated history sentence out only if the desk already has an archive or provenance file the row names. Otherwise SKIP; don't delete history.
9. **Size discipline:** a file may grow by no more than about 1%. Prefer shortening.
10. **After editing each file, re-read the changed lines,** and run `git diff --stat -- <file>` to confirm only intended lines moved.

## Ledger (write it incrementally)

Write to your named path. Per desk, a table: `row_id | file:line (after) | APPLIED / SKIPPED | what changed (≤20 words) or skip reason`. End with every file you edited and its byte size before → after.
