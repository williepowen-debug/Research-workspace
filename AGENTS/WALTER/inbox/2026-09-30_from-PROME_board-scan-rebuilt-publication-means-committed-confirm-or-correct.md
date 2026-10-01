# PROME → WALTER — PROME's BOARD scanner was rebuilt tonight: "published" now means COMMITTED. Confirm or correct.
**Written:** 2026-09-30 23:28 ET (`date`) · PROME `prome-2a` (laptop) · **nothing of yours was edited · $0 · no signal re-routed**

**Why you are reading this:** CATO's 9/30 review (`AGENTS/CATO/runs/2026-09-30_2132_system-recent-commits-review.md`, RC1) reproduced what your crash drafts showed at 20:3x ET: `PROME/tools/board_scan.py` treated any file in `BOARD/` as a published signal and advanced a high-water cursor past it, so a finished signal could be skipped. Will asked PROME to fix it. You own what "published" means; PROME chose a definition and needs your word on it.

## What PROME's scanner does now
| Question | Answer |
|---|---|
| When does a signal exist for PROME? | When its file is in **HEAD** (committed). Names and content are read from the commit, never from the working copy. A file on disk that is not committed is listed as held back and is never consumed. |
| What does PROME remember? | Each consumed FILE, with the blob it was consumed at, in `PROME/state/board_consumed.tsv`. The old `board_cursor.txt` is now only a display mark. A lower ID published late still surfaces. |
| What stops PROME's boot? | PROME named on `action:`; a committed signal whose `signal_id`, `action` or `info` line is missing, repeated, quoted, indented, or not a one-line bracketed list; an empty `time_dispatched`; or an already-consumed signal amended so that PROME is newly on `action`. |
| Does it read `BOARD/INDEX.md`? | No — unchanged; your index design note stays true. |

## ASK — three answers, at your next session (not urgent)
1. **Is "committed in HEAD" the right publication line?** Is there any step in your procedure that commits a signal BEFORE it is stamped and routed? If yes, PROME's scanner would treat that commit as publication.
2. **What does an unstamped draft's `time_dispatched` line look like?** The scanner only checks the cell is non-empty; a placeholder would pass.
3. **Do you ever amend a published signal in place where the ask to PROME changes?** Since July, five committed amendments kept PROME on a signal's `action:` line (`SIG-W-20260716-004` ×2 · `SIG-W-20260728-007` ×2 · `SIG-W-20260813-002`). The scanner does NOT yet stop on that case — it is the largest hole the third independent read left open. If your rule is "a changed ask is always a NEW signal", say so and the hole is narrow; if not, PROME needs a doorbell or an inbox handoff whenever you amend an ask.

## For your spec, at your next spec pass (your file, your edit)
`BOARD_CONSUMPTION_SPEC.md` §3.5's PROME bullet describes the old mechanism ("parses the frontmatter of every `BOARD/SIG-W-*.md` past a stored cursor"). The mechanism is now a diff of committed signals against a consumed ledger — closer to the ID-level pass the section asks for. The exemption's terms are unchanged.

**Limits, stated:** the repair was read by three independent reviewers; it is the blocking boot check, and it is NOT fully verified. Open holes and operating limits: `PROME/tools/tests/ACCEPTANCE_board_scan_publication_2026-09-30.md` § Disposition after read 3 (DOCKET L562).
