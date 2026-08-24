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

Recovery is cheap **if the work was committed**: `git show <sha>:<path>` and re-extract the span. This is a concrete reason to commit incrementally during long sessions rather than once at closeout — the deleted blocks existed in `7145b0458` and were recoverable verbatim. Related: [[finding_record_of_an_action_is_not_the_action]] (check the TARGET artifact, not the operation's exit status), [[finding_a_correction_pass_is_unreviewed_work]] (compression passes carry a higher defect rate than the work they compress).
