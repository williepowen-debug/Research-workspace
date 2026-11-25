# WQ-744 RULED: root `CLAUDE.md` trim batch, items 1 and 2

**Will, in PROME's chat 2026-11-23 20:47 ET (prompt clock), verbatim:** "1 and 2 approved go ahead". Recorded by PROME (context 0b555415) at 2026-11-23 20:53 ET (`date`). He was answering PROME's review of about 20:24 ET, which listed three trims and recommended 1 and 2. Item 3 (the Gate C custody paragraph) was not approved and is untouched. Path: the Trim batch rule, `PROME/CLAUDE.md` § Review budget (WQ-701 D): one ruling, one blind result read, this record.

**Sizes:** `python3 PROME/tools/measure.py CLAUDE.md` and the same for `docs/GIT_WORKTREE_PROCEDURES.md`; before and after are `git show` on the commit that carries this record.

## Item 1: MOVED verbatim, root § Git Protocol "At session end" → `docs/GIT_WORKTREE_PROCEDURES.md` § At session end

| Moved (whole numbered step, verbatim) | Where the rule stands now | On a boot-read path? |
|---|---|---|
| 1b Orphan check | the destination section, same number | Root keeps a mandatory line: "read and execute ... § At session end in full", in the form already used for "Before committing" and "Before pulling" |
| 1c Consumer check | same | same |
| 1c-bis Ledger nudge | same | same |
| 1d Memory-index check | same; carve-out ③ in root still names its command | same |
| 1e Claim check | same | same |
| 3 Non-ff recovery (overlap check, rebase, escalation test) | same; root keeps the step's bold lead "If safe-push aborts (non-ff), do NOT force." and the pointer | same |

Steps 1 and 2 (commit locally; auto-push and the receipt line) stay in root word for word. Step numbers are unchanged, so "root session-end step 1d" and "step 3" still resolve, through the pointer.

**Text added, not moved (the reader's attention goes here):** two pointer lines in root (step 1b–1e and step 3), one heading line in the destination, and root's "Latest amendment" line.

## Item 2: DELETED from root § Git Protocol, the "Never" paragraph, its last three sentences

| Deleted sentence (opening words) | Where the same rule still stands |
|---|---|
| "Git refuses a rebase pull while ANY tracked file is modified or staged ... pull again after they commit." | `docs/GIT_WORKTREE_PROCEDURES.md` § Before pulling, step 2 ("The dirty-owner stop is Git's own refusal ... STOP; do not stash, reset or commit them; continue on your current checkout ... pull again after they commit"); root's own "Before pulling" line makes that section mandatory |
| "If the rebase stops on a conflict in a commit you did not author ... yours to resolve." | same section, step 3 |
| "Untracked files block only when an incoming commit adds the same path — move yours aside, never delete, pull again." | same section, step 2, last sentence |

The first sentence of the "Never" paragraph (the list itself, including the one pull form and the `--autostash` limit) is unchanged.

## Declared residue

- A desk that does not open the procedures file at session end no longer sees the five checks at boot. PROME's closeout gate runs 1c, 1d and 1e mechanically; desks have no such gate. Told to Will before he ruled.
- The deleted first sentence said the refusal is "never an error to work around"; the destination says it in other words ("The dirty-owner stop is Git's own refusal ... STOP"). Judged the same rule; the blind reader is asked to test it.
- Other files that quote the moved steps as living "in root" still resolve through the pointer and are not edited here.

## Blind result read (2026-11-24 22:22 ET, one coldreader on Sonnet; the first launch of 11/23 20:5x ET died on a lost connection and returned nothing): ❌ 0 · ⚠️ 6

reads: 1 of 1 (result read; no plan read on this path). Six moved steps byte-identical at the destination (6 of 6, by script); no other root change; both pointers resolve; three counterexample attempts found no divergence for a reader who follows the pointers. Nothing was edited after the read. **Residue, declared and not fixed:**
1. Deleted sentence 1's words "whoever owns it" and "never an error to work around" survive only in other words (the destination splits your own files from another agent's and says STOP).
2. Deleted sentence 3's word "only" (untracked files block in no other case) is dropped; the instruction survives.
3. Citations of "root session-end step 3" and "1b to 1e" (PROME's charter, the AEOLUS, CORAL and HAWK charters, root's own "Never" paragraph) now resolve in two hops; "overlap check first" is visible only at the second.
4. Moved steps 1b and 1d say "carve-out ①" and "carve-out ③" without naming root, where the carve-outs are defined.
5. Root's step 3 line no longer says that a non-ff means another session pushed (routine); that sentence is in the destination only.
6. The reader could not verify from the files two claims in this record: that PROME's closeout gate runs 1c, 1d and 1e mechanically (source: `PROME/CLOSEOUT_PROCEDURES.md` § Final gate rules), and that Will was told of the first residue item before ruling (source: PROME's chat message of about 20:24 ET 11/23, "One risk to weigh on trim 1").
