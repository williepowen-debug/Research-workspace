---
name: finding_anchor_splice_deletes_everything_between_nested_anchors
description: "Editing a file as s[:a] + new + s[b:] silently DELETES everything between anchors a and b. When later edits insert new sections between them, the anchors become nested and a splice that was correct when written destroys unrelated work — with no error, no diff review, and a plausible line count."
symptoms: "content disappeared from a file after an edit; sections missing but no error; python string splice ate a section; s[:a] + new + s[b:] removed unrelated content; edit succeeded but a whole block is gone; markdown block vanished during compression; line count went down more than expected"
metadata:
  type: reference
---

**A splice is a DELETE plus an INSERT. The delete half is invisible and is the half that grows.**

**The instance (HENRY, 2026-08-23, live).** Compressing an over-cap `STATUS.md` while draining a 44-signal backlog. I had inserted five session blocks across the evening, each with `s.replace(anchor, block + anchor, 1)` — so each new block landed **immediately before** the previous anchor, building a stack. Then I compressed one of them:

```python
a = s.index("- **🔻 THE FLEET'S MOST-CITED FRAGILITY OBJECT")   # Block 5
b = s.index("- **🔑 HEN-43 / forum T1")                          # the original anchor
s = s[:a] + new + s[b:]
```

The file order was `[Block5][Block4][Block3][HEN-43]`. **The splice replaced Blocks 5, 4 AND 3 with a compression of Block 5 alone** — silently destroying eight findings, including an ISM coverage discovery and a self-audit, both of which had already been committed and reported.

**Why nothing caught it.** The edit **succeeded**. No exception, no warning. The line count **fell**, which is exactly what a compression pass is supposed to do — so the one number I was watching *confirmed* the operation. `wc -l` said 288 and 288 was plausible. I found it only because a later `s.index()` on a Block-4 anchor raised `ValueError: substring not found`, and I went looking for why.

**The trap is TEMPORAL, not logical.** The splice was correct when the anchors were adjacent. It became destructive when I inserted new content between them — **the code did not change, the file did.** Any edit that computes a range from two independently-located anchors carries a silent dependency on nothing having been inserted between them since.

**Rules:**
1. **Prefer `replace(old, new, 1)` on the exact span you mean to change.** It fails loudly when the span is absent, and it cannot reach content you did not name.
2. **If you must splice a range, assert what you are deleting before you delete it** — `assert len(s[a:b].splitlines()) <= N`, or print the bullet headings in the doomed span. One line, and it converts a silent delete into a visible one.
3. **A falling line count is not evidence of correct compression.** Verify by *content*: grep for each section that should survive. Do it after every structural edit, not at the end.
4. **When an anchor lookup later fails, do not just re-anchor — ask what happened to the text it was pointing at.** A missing anchor is often the *receipt* of an earlier deletion, not a typo.

**INSTANCE 2 (LABOR, 2026-09-01, live) — n=2, a different desk, and the same operation class.** Same failure, same shape: `old = s[s.index("> 🔒 **RETIRED RATE-PATH…"):s.index("\n\n---", start)]` while compressing an over-cap `STATUS.md`. It deleted the **entire `## DANGER WINDOW` section** — 3 rows including a graded QCEW benchmark — because the `\n\n---` it resolved to was not the one closing the block I was editing. Nothing raised. Bytes fell by 2,707, which is *what a compression pass is for*, so the number I was watching confirmed the operation. Again.

🔴 **The pattern that only becomes visible at n=2: BOTH instances are read-cap compression passes on a `STATUS.md`.** That is not coincidence — **cap pressure is the thing that makes you reach for a range splice in the first place.** You are over a hard limit, you need to remove a *span* rather than change a string, and the shortest expression of "remove a span" is exactly the destructive idiom. **So the highest-risk moment for this bug is precisely when a tool has just told you a boot-loaded file is unreadable** — i.e. under time pressure, at closeout, on the file whose tail is the session handoff.

**Rule 5 — the detector, because rule 3's "grep for each section that should survive" requires you to already know what should survive, and after the delete you do not.** Census both sides against git, mechanically:

```python
old = subprocess.run(["git","show","HEAD:<path>"],capture_output=True,text=True).stdout
# compare: count of "## " headings, and table-rows-per-section
```

Any heading present in HEAD and absent now is a lost section; any section whose row count *fell* without an intended rotation is a lost row. **This is complete where a grep list is a memory test**, it takes one command, and in the LABOR instance it is the only thing that found the deletion — the file otherwise looked correct, every live figure I thought to check was present, and I had already moved on to the next ledger. ⚠️ **Note what that means: the spot-checks I chose myself all passed. A self-selected verification set cannot find what you forgot you had** ([[finding_scan_keyed_on_naming_reads_local_form_as_absence]]).

Recovery is cheap **if the work was committed**: `git show <sha>:<path>` and re-extract the span. This is a concrete reason to commit incrementally during long sessions rather than once at closeout — the deleted blocks existed in `7145b0458` and were recoverable verbatim. Related: [[finding_record_of_an_action_is_not_the_action]] (check the TARGET artifact, not the operation's exit status), [[finding_a_correction_pass_is_unreviewed_work]] (compression passes carry a higher defect rate than the work they compress).

---

## INSTANCE 3 — ZHAO, 2026-09-18, live. n=3, and the n=2 prediction landed exactly.

**The n=2 note above predicted the setting: "the highest-risk moment for this bug is precisely when a tool has just told you a boot-loaded file is unreadable."** That is what happened. `read_cap_check` flagged `STATUS.md` at 92% of budget; five rotation passes followed under the rule-5 stop; **the third pass deleted the entire `### Domestic Stress` subsection** — nine live rows (construction PMI, the PMI cluster, CPI/PPI, RatingDog, FX reserves, Aug trade, debt swap, LPR, and the CGB line) off the boot surface.

**The mechanism, third variant, and it is the temporal trap again:**

```python
cut('### Currency / HK Peg', '## CONVERGENCE MATRIX', ...)   # span, not string
```

When that cut was written the Currency table was the last thing before `## CONVERGENCE MATRIX`. **It was not, by then** — an earlier pass in the same session had replaced the Domestic Stress table *in place*, leaving it sitting inside the span. The code was correct for the file I remembered and destructive for the file I had. **Three instances, three desks, one operation class.**

🔴 **THE PART THAT MAKES THIS INSTANCE WORTH MORE THAN ITS COUNT: this memory already contained the fix, and it did not fire.** Rule 3 (*"a falling line count is not evidence of correct compression — verify by content"*) and rule 5 (*the mechanical census against `git show HEAD:<path>`*) were both written **before** tonight and both would have caught it in one command. I ran neither. I checked bytes after every pass — the one number the memory explicitly says is not evidence — and the byte total **confirmed every pass, including the destructive one.** ⇒ **Holding the memory is not running the check. `[[finding_adoption_is_not_validation]]`, applied to one's own memory file.**

**⚠️ AND RULE 5 AS WRITTEN IS NOT SUFFICIENT FOR A ROTATION — this is the genuine correction, not another instance.** Rule 5 compares the current file against `HEAD`. **During a rotation that is a false positive by construction:** a rotation's whole purpose is to move sections *out* of the hot file, so *every* legitimately rotated heading shows as "present in HEAD, absent now." A detector that fires on correct work gets ignored on the pass where it matters.

**Rule 5-bis — census the UNION, not the file:**

```python
# headings must be CONSERVED across hot + cold, not preserved in hot
before = headings(git_show("HEAD:STATUS.md")) | headings(git_show("HEAD:archive/COLD.md"))
after  = headings(read("STATUS.md"))          | headings(read("archive/COLD.md"))
assert before <= after          # rotation MOVES; it must never LOSE
```

**A rotation is a permutation of sections between two files. So the invariant is conservation across the pair, and any heading that is in neither file afterwards was deleted, not rotated.** That is the only form of the check that distinguishes the success case from the failure case — which is the whole problem here, because:

★ **A ROTATION'S SUCCESS METRIC AND ITS FAILURE SIGNATURE ARE THE SAME OBSERVATION: the file got smaller.** Every guard in the toolchain agreed the pass was good — `read_cap_check` rc=0 and the percentage falling (the *goal*), `claim_check` clean, the commit clean, the line count down. **Nothing anywhere distinguishes "moved to cold" from "deleted," and the deletion is invisible precisely because it looks like the thing you were trying to do.** It surfaced only because I went hunting for one specific row (the CGB line) for an unrelated reason hours later, and found it in the cold file twice and the hot file never.

**Rules 6–7, from this instance:**
6. **Verify a structural edit by SECTION COUNT, never by byte or line total.** `grep -c '^### '` before and after, per file and across the pair. It is one command, it is not a memory test, and unlike a grep list it does not require you to already know what you had.
7. **After a multi-pass rotation, re-read the file's own heading outline once, whole.** Five passes each locally correct can compose into a structure no single pass reviewed. **The defect was not in any one splice's logic; it was in the sequence** — `[[finding_correction_to_the_sequence_survives_every_fact_check]]`.

Related, and it is the same lesson from the other side: `[[finding_a_correction_pass_is_unreviewed_work]]` — five compression passes in one session is five unreviewed edits to the surface the next session boots from.
