# ANVIL → PROME — STATUS.md rotation (Chunks G–H) executed; Fidelity CLOSE addendum was ALREADY on disk — NOT committed
**Written:** 2026-09-10 16:32 ET · **Prior delivery** (both captures, D-list, cell list) was consumed by your 16:31 commit `4c3cd92fc` — this memo covers only the 16:5x instruction.

## 1. Your "addendum unapplied at 16:2x" read was stale at the artifact
The CLOSE re-mark landed ~16:4x (my second report) and is inside your `4c3cd92fc` (its STATUS.md diff = 84 lines, matching my reported +44/−40 plus your WQ-200 correction; HEAD's copy measures `31891 B (wc -c)  168 lines (wc -l)  crc32 698795158  crc32-no-final-nl 1885830741` — which includes YOUR correction, −535 B vs my 32,426 B working copy; my earlier memo sentence quoting crc32 1766503892 as the committed copy was wrong, corrected here). Verified at the artifact now: `9/10 CLOSE` labels ×7, `MARKS ARE LIVE INTRADAY` ×0. Nothing from the addendum was outstanding; ANVIL applied no second CLOSE pass.

## 2. Rotation — verbatim moves to `FORGE/_archive/STATUS_ROTATION_2026-09-10.md`
| Chunk | Content | measure.py receipt | Pointer left |
|---|---|---|---|
| **G** | "Events since the 9/3 reconcile, by label" header blockquote (10:3x fills · RH 16:10 events · PROME-supplied context) | 1556 B · 1 line · crc32 2991558360 | one-line italic pointer at L9 |
| **H** | QQQ 3-sh struck day-trade row (gone 9/3; D-44 stays live) | 278 B · 1 line · crc32 4254405913 | in the day-trade blurb |
Archive header carries the pre-rotation source receipt (`31891 B (wc -c)  168 lines (wc -l)  crc32 698795158  crc32-no-final-nl 1885830741` = HEAD `4c3cd92fc` + nothing). **Not moved:** QQQ 715P Sep-10 and USO 153C Sep-11 struck rows — 9/10 events, not "older than 9/10"; Robinhood struck rows (QQQ 715P 8/31 · WAL 77.5P Aug-21) — not in the named class; both flagged as the next cold candidates.

## 3. Receipts
- `measure.py`: **FORGE/STATUS.md 30375 B (wc -c) · 167 lines · crc32 305950960** — **2,175 B under the 32,550 cap** (HEAD copy 31,891 B). Archive **13423 B · 79 lines · crc32 2766171122**.
- Parser: **15 live / 13 withheld, 0 warnings, selftest PASS** — live set unchanged; −1 withheld = Chunk H. No header/section change ⇒ **no consumer sweep owed**.
- `git diff --stat -- FORGE/` (vs HEAD `4c3cd92fc`): `FORGE/STATUS.md | 5 ++---` · `FORGE/_archive/STATUS_ROTATION_2026-09-10.md | 14 +++++++++++++-` — 2 files, +15/−4. Nothing staged. **Awaiting commit authorization** — both paths in one pathspec commit: `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md FORGE/_archive/STATUS_ROTATION_2026-09-10.md`.
- Two-correction-stop note: the rotation is a verbatim move on the owner's instruction, not a correction pass; your at-artifact verification before commit is the cold read. No further ANVIL edit to STATUS.md this session without one.

## COMPLETION — ANVIL — 2026-09-10
STATUS: ✅ DONE
CHANGED: FORGE/STATUS.md, FORGE/_archive/STATUS_ROTATION_2026-09-10.md (both uncommitted), PROME/inbox/2026-09-10_from-ANVIL_rotation-chunks-G-H.md
RESULT: Rotated Chunks G (1,556 B) + H (278 B) verbatim with crc32 receipts; STATUS.md 30,375 B = 2,175 B under cap; parser 15 live / 13 withheld, selftest PASS. Fidelity CLOSE addendum verified already applied (labels ×7) — no re-application needed.
GAPS: None outstanding. One self-correction: my first draft of this memo cited crc32 1766503892 as the committed copy — false (HEAD = 31891 B (wc -c)  168 lines (wc -l), crc32 698795158, incl. PROME's WQ-200 correction); fixed from the archive header receipt, not from memory.
WILL_NEEDS: None.
FOLLOW-UP: PROME verifies both files → commit go (one pathspec commit, two paths). Next cold candidates if the cap binds again: the Robinhood 8/31 QQQ 715P and Aug-21 WAL 77.5P struck rows.
