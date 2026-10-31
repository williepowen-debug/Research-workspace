# ACCEPTANCE — `scripts/claim_check.py --check glued` (WQ-560 A part 2)

**Written before the edit** (WQ-229), 2026-10-30 21:0x ET, PROME prome-34. Ruling: `PROME/proposals/2026-10-30_wq560-RULED.md`. Baseline: `--selftest` = 42/42 before the change.

**The defect, in its own terms:** a date written glued to the word beside it (`October25`, `settled10/27`, `10/27settled`, `as-of9/28`) is a different token to every date-reading instrument in the fleet, and nothing flags it at the moment of writing. The fleet carried ≥273 such tokens on 122 boot-read files at 20:5x ET.

## Acceptance conditions
- **AC1 (ordinary):** each of the four forms is flagged once per occurrence on an ordinary prose line, with the file, the line and the spaced replacement named.
- **AC2 (negative controls):** correctly spaced forms do not flag; neither do ISO dates (`2026-10-27`), hyphenated month abbreviations (`Oct-16`), identifiers (`L884`, `WQ-558`, `S5`, `MIDAS-16`), a month followed by a four-digit year, or a two-letter prefix.
- **AC3 (overlap):** a glued token inside a backtick code span, a markdown link target or a URL does not flag, while an unwrapped glued token on the SAME line still does. A line carrying both a weekday mismatch and a glued date raises both flags, each under its own kind.
- **AC4 (opt-in):** the default `--check` set is unchanged; `prome_gate.py`'s `--check weekday` call and every existing weekday case behave exactly as before.
- **AC5 (advisory):** flags exit 1 like the other checks; the tool edits nothing; the closing advisory sentence still prints.
- **AC6 (falsifiable):** `--selftest` carries the glued cases and exits 1 if any misbehaves; its last line stays the one-line summary (`validate_all.py` leg A4 reads the rc).

## Neighbour categories (considered)
- ordinary — AC1 · overlap — AC3 · missing information — an empty or unreadable file is handled by the existing partition (unchanged code path), no new case · **wrong owner — N/A:** the mode reports file:line only and assigns no owner · **concurrent activity — N/A:** a read-only, single-pass scan of the working tree.

## State (four states, never merged)
- **IMPLEMENTED** 2026-10-30 21:1x ET (PROME): `RE_GLUED` (four patterns) + `glued_flags()` with code-span / link-target / URL masks; opt-in `--check glued`; default set unchanged.
- **TESTED** (author's own, not verification): `--selftest` 61/61 (was 42/42; +18 glued cases incl. AC3 masks and the masked-plus-unmasked overlap line, +1 weekday-and-glued overlap); `--check weekday` output on PROME/STATUS.md and PROME/SCRATCH.md identical before and after (both empty; the old-version rc was read through a pager and is not evidence); fleet run over 122 boot-read files = 341 flags (month 182 · word+date 158 · as-of 1); every word+date match reviewed by eye, 0 false positives observed. Note: the `word+date` kind also catches a word glued to a COUNT (`VULCAN15/25`, `Score53/70`) — still a glued token, but the kind label says date.
- **INDEPENDENTLY VERIFIED:** PENDING — DAEDALUS counterexample review (WQ-229 consequential: a shared fleet check).
- **STILL UNRESOLVED:** root closeout step 1e does not yet call the mode (WQ-560 part 3 waits on the review).
