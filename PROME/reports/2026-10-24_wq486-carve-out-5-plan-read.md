COLDREAD (PLAN) · WQ-486 carve-out ⑤ draft · record: PROME/proposals/2026-10-24_wq505-486-517-493-488-RULED.md § B (lines 44-55) vs root CLAUDE.md lines 76-106
Format: claim -> artifact -> verification -> observed -> proposed change. Nothing edited.

## ❌ (changes meaning or fails to apply): NONE FOUND

## ⚠️ (unclear / could be misread)
W1. "standing-bucket" is undefined in root.
  Claim: record L48 bullet ⑤ "a standing-bucket forum post you authored".
  Artifact: root CLAUDE.md has no definition; bullet's only pointer is "FORUM/README.md § standing buckets (WQ-482 A)". README heading is "## Standing buckets — the lightweight mode" (README:25). Bucket = "a folder with no date prefix" (README:29).
  Verified: grep of root lines 76-106 for the term; README:25-35 read.
  Observed: a root-only reader cannot tell a standing bucket from a session tree. The filename pattern in the parenthesis does the real fencing, but a session-tree post (`FORUM/<date>_<slug>/NN_<AGENT>_<slug>.md` or `P0_...`) is excluded only by inference.
  Change: one clause, e.g. "(a dateless `FORUM/<bucket>/` folder; session-tree posts stay orchestrator-committed)".
W2. Pattern vs. real folders: FORUM/keeper/ exists, is dateless, and its posts are ordinal-named (001_PROME_opening.md ... 010_PROME_paste-sweep.md), not stamped. README:34 lists only banks/ and orchestration/ as open buckets.
  Verified: ls FORUM/ ; ls FORUM/keeper.
  Observed: by the draft's literal filename pattern keeper posts are NOT covered; by "standing-bucket" (dateless folder) they might be. Two readings.
  Change: state that the filename pattern is the test (it is the narrower and safer reading), or have PROME say what keeper is.
W3. "<stamp>" and "<YOU>" undefined in root. Real files (FORUM/banks, ls): 8 of 8 match ^YYYY-MM-DD_HHMM_<DESK>_<slug>.md, e.g. 2026-10-22_1117_OZK_l520-call-read.md, 2026-10-22_1115_PROME_opening-will-question.md. So the pattern is right, but "<stamp>" = date_HHMM is only in README:30. Also "your own name in the filename" relies on the DESK token, which forum.py takes from --desk NAME (README:31) - self-declared, not authenticated. A desk could commit a file bearing its own name that it did not write, or another desk's file renamed. Low-risk but the grant is only as tight as the token.
  Change: optional - write the stamp as `<YYYY-MM-DD>_<HHMM>`; accept the self-declared-token limit or add "and that you created".
W4. "yours to commit, explicitly pathed, and only that file."
  Ambiguity: "only that file" can read as (a) the grant covers only that one file per commit, or (b) the commit may contain nothing else. A desk with two posts, or a post plus its own STATUS.md, is unclear. Carve-outs ①-④ do not say "only that file" except ④ ("stage and commit that single path"), which is single-path by design. Not a widening, so not ❌.
  Change: "each post you authored, by exact path; no directory or glob pathspec."
W5. "WQ-482 A" in the pointer. README:25 says "added 2026-10-22, WQ-482, Will's word 11:13 ET" - no letter "A". The "A" is unverified from the artifact set I was allowed. Also the pointer cites "§ standing buckets" while README:32 carries the line "Commit authority PENDING ROOT CANON" that this very edit makes stale (record L28 says PROME re-points it afterwards; that is a follow-up, not part of the three touches).
  Change: cite "(WQ-482)" or confirm the A; ensure README:32 is re-pointed in the same commit set as the record promises.
W6. "a session charter, a rulings record, `README.md`" - who commits them is not stated in root. README:16 says the session orchestrator (PROME unless stated) commits the forum tree; README:11 makes the rulings record a PROME post. Draft says "stay with their existing owners" - correct but root can't resolve "existing owners" for README.md (PROME-owned per record L28) or CHARTER_TEMPLATE.md/forum.py (also "any other FORUM/ file"). Safe direction: the list is illustrative, the catch-all "any other FORUM/ file" governs.
  Change: none needed beyond "e.g." before the list.
W7. Interaction with the Scope note (root:86) and line 76: line 76 says domain agents' ONLY commit exceptions are "the carve-outs below" - automatically covers ⑤. Scope note says "PROME commits PROME/ ... Everyone else: own AGENTS/<NAME>/ dir". ⑤ is a path outside both; fine as a carve-out, but PROME as a poster is also a "YOU": PROME's own bucket posts are covered, PROME's session-tree commits remain under README:16 only. Not contradictory; a reader might wonder.
W8. Invariant "root stays under its read-cap budget" - I measured only the BEFORE: PROME/tools/measure.py: CLAUDE.md 22726 B (wc -c), 121 lines, crc32 2661298220 (committed head cdb58ceb4, `git status --short CLAUDE.md` clean at read time). Cap in root Data Hygiene = 32,550 B, so the ~500 B insertion fits with ~9.8 KB headroom. AFTER cannot be checked at plan stage (UNVERIFIED until the result read).

## ✅ (verified)
V1. Lead-in quote (record L47) "**Carve-outs ①–④ — four fleet-wide self-authorship carve-outs (④ activation-gated); …" matches root:78 byte-for-byte (grep -F hit, line 78). Replacement "①–⑤ … five fleet-wide" is internally correct; the rest of the line ("the separate PROME-only Gate C custody grant is the paragraph AFTER them, not a numbered carve-out:") unchanged and still true after insertion because ⑤ goes before that paragraph.
V2. Never-clause quote (record L51) "(the carve-outs ①–④, the Scope-note grants …" matches root:104 byte-for-byte (grep -F hit, line 104). Replacement "①–⑤" correct.
V3. Insertion point: record says "directly AFTER the ④ bullet (line 82), BEFORE the Gate C custody paragraph". Root:82 is the ④ bullet; root:83 blank; root:84 "**Gate C custody (PROME only).**". Correct.
V4. Exhaustiveness of ①–④ range citations in root: grep '①–④|four fleet|carve-out' on root finds only lines 76, 78, 92 (carve-out ①), 95 (carve-out ③), 104. Only 78 and 104 carry the range; so "no other root line changes" holds for root. (Citations OUTSIDE root, e.g. other docs saying "①–④", were not in scope and are UNVERIFIED.)
V5. Grant scope vs. ruling. Will: "a desk's own explicitly pathed forum post. No authority to edit or commit others' posts or sweep shared directories." Draft: own post, "explicitly pathed", names no-edit/commit-of-another's-post, "sweep a shared directory", and "any other FORUM/ file". It adds no "must" (unlike ①/③), no edit authority, no push/auto-push change, no inbox/outbox or other directory. Matches the ruling and is, if anything, narrower (stricter than README:32's "each desk commits ITS OWN posts"). It does not carry the ruling's third sentence ("Follow the existing amendment and review procedure") into the text, correctly - that is process, and record L28 states it.
V6. Gate C custody paragraph keeps "not a numbered carve-out" status: root:84 untouched; line 78 still says so. Invariant holds.
V7. Filename pattern: 8/8 files in FORUM/banks/ match ^\d{4}-\d{2}-\d{2}_\d{4}_<DESK>_<slug>.md; the cited example 2026-10-22_1117_OZK_l520-call-read.md exists.
V8. Pointer FORUM/README.md § standing buckets resolves (README:25-35). README:32 confirms the gap this carve-out fills ("a forum post is not an inbox packet ... Registered for Will as WQ-486") and README:32 matches the record's statement that it is "PENDING ROOT CANON".
V9. Self-containment of the three-touch description: sufficient to apply mechanically (find lines, quote before/after); no ambiguity about where the new bullet goes.

## Unverifiable invariants
- "Plan read: PENDING at write" (record L58) - this ledger is that read; record not updated by me.
- WQ-482 "A" letter (W5) and the Will ruling text for WQ-486 beyond the record's own quote.
- Citations of "①–④" outside root CLAUDE.md.
- Post-insertion byte size (W8).

COUNTS: ❌ 0 · ⚠️ 8 · ✅ 9
VERDICT: INSERT AS DRAFTED is defensible (no ❌; quotes exact, grant no wider than the ruling); recommended wording tweaks W1/W2/W4 are optional but cheap. Per the plan-read rule ⚠️ go to a declared residue block unless the PROME editor chooses a one-word fix. -> INSERT AS DRAFTED.
