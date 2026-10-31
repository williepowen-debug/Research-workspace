# DAEDALUS -> PROME: WQ-560 A part 2 — independent counterexample review of `claim_check --check glued`; read_cap message; own surfaces re-spaced; inbox drained

**Date:** 2026-10-30 (Fri) 21:1x ET · **From:** DAEDALUS (Claude Code, Opus 5.5, spawned by PROME prome-34) · **Ruling:** `PROME/proposals/2026-10-30_wq560-RULED.md` (Will 20:57 ET, "okay REC A approved") · **Boot reads (bounded reader, each to `eof: true`):** root `CLAUDE.md` 5 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/DAEDALUS/CLAUDE.md` 4; desk boot reads OPERATIONS 4, STATUS 4, FLEET_DIRECTORY 3, PATTERNS_HOT 1; boot gate rc 2 (profile-clock CANNOT-EVALUATE HENRY/OSPREY, unchanged from 16:31).

## Task 1 — verdict

**HOLD part 3 (the root step-1e edit) on two ❌, each a few lines of code; once both are fixed: ACCEPT WITH NAMED RESIDUE (⚠️ F3–F8).** The mode does what its four patterns say, its masks work, the default `--check` set is unchanged (line 620 `weekday,hash,units,pointer`; `prome_gate.py:1936` still passes `weekday` only), and flags exit 1 with the advisory closing line. Selftest 61/61 (author's; re-run here, not counted as evidence).

**Against STRICT_TEXT's DO-NOT-BUILD ruling — plainly:** the DATE half of this mode is **outside** what that ruling forbade. The ruling (`BLUEPRINTS/STRICT_TEXT.md` § What this is not) banned a linter for the ten STRICT rules because "deliberate density and sloppy density are byte-identical from the condition alone". A glued date has no deliberate-density reading: root `CLAUDE.md` § Output Canon now forbids it outright, and it breaks a machine-read referent (the fleet's date instruments), which is STRICT's own cost-bearing concern, not prose style. **But the `word+date` and `date+word` patterns also flag glued COUNTS** (`consumer0/4`, `Score53/70`, `selftest61/61`), and the code comment says it "flags only a DATE … and leaves every other density choice alone". That slice is the style screen the ruling forbade: the Output Canon does forbid it too, but the date rationale that justifies this carve-out does not cover it. Fix F1 and the mode is fully inside the carve-out.

### Counterexamples (mine, run through `check_text(…, {"glued"}, 2026)`; script `/tmp/claude-1000/-home-willi-Research-workspace-PROME/69a75857-1a35-419a-bd61-8b789e4acf17/scratchpad/cx.py`)

| # | Line | Should flag | Flags | Class |
|---|---|---|---|---|
| FN1 | `landed Oct25 and Nov3` | 2 | 0 | abbreviated month missed |
| FN3 | `due by11/04 and graded on10/30` | 2 | 0 | two-letter word missed |
| FN4 | `values as of9/28` | 1 | 0 | "as of" spaced, "of9" missed |
| FN5 | `header settled2026-10-27` | 1 | 0 | word + ISO date missed |
| FN7 | `settled10/27/2026` | 1 | 0 | word + M/D/YYYY missed |
| FN8 | `## OCTOBER25 SESSION` | 1 | 0 | all-caps month missed |
| FN12 | `OriginaldueOctober5/last_runJuly7` (my own REGISTRY.tsv) | 2 | 0 | month glued AFTER a word: `\b` fails mid-word |
| FP1 | `selftest61/61 and consumer0/4 and Score53/70` | 0 | 3 | counts flagged as dates |
| FP4 | `Will, verbatim: *"move it to October25"*` | 0 | 1 | verbatim quote flagged with "write October 25" |
| FP6 | `the October10/27 cell` | 1 | 2 | one glue point counted twice |
| — | `--check glud` (typo) on a dirty file | rc 2 | **rc 0, "✓ 1 file(s) clean [glud]"** | unknown check name certifies clean |
| ctrl | `Oct 25 · by 11/04 · as of 9/28 · settled 2026-10-27` | 0 | 0 | clean control, watched |

Fleet scale, measured over every file globbed from READS.tsv `whole` rows (2,144 .md/.tsv files, includes BOARD class members; same masks): the mode flags 1,555; impossible-M/D (month >12 or day >31) among `word+date`/`date+word` = 44 of 314 (14%); the extra forms it misses = 121 (abbreviated month 62 · lowercase two-letter word 29 · word+ISO 15 · word+M/D/YYYY 15). 0 flags fell inside fenced code blocks.

### Findings (claim → artifact → command → observed → proposed change)

- ❌ **F1 — narrowness claim false.** Claim: "flags only a DATE … leaves every other density choice alone" → `scripts/claim_check.py` comment above `RE_GLUED` + `GLUED_SELFTEST` row `("Cboe9/8 SKEW148.86 breaks the run: consumer0/4", 2)` → `check_text` on FP1 → 3 flags, all counts; fleet 44 of 314 impossible dates; the selftest LOCKS the count case in as a positive → bound the two M/D patterns to month 1–12 and day 1–31 (a callable replacement or a post-match test), move `consumer0/4` to the negative set; or, if PROME wants counts flagged under the Output Canon, relabel that kind `word+count` and correct the comment, docstring and the STRICT_TEXT reasoning in the ruling record — a scope change that is Will-visible. Residue either way: `Score3/4` is a plausible date and still flags.
- ❌ **F2 — unknown check name passes clean** (pre-existing, not introduced here, but part 3 makes it load-bearing: 1e will carry a new opt-in name that desks copy into charters). Claim: AC4/AC5 "flags exit 1" → `scripts/claim_check.py` `--check` parsing (membership test only) → `claim_check.py --check glud <dirty file>` → "✓ 1 file(s) clean [glud]", rc 0 → reject any name outside {weekday, hash, units, pointer, glued} with rc 2 and a message naming the valid set; add the typo case to the selftest. This is CHECK_STANDARD §3 (a clean line on a case where nothing ran).
- ⚠️ **F3 — two-letter words.** `on10/30`, `by11/04`, `to11/5`, `at10/14`, `as of9/28` → `RE_GLUED` word+date `[A-Za-z]{3,}` (by design, to silence `HY10/27`) → 29 fleet hits missed → add a lowercase list `(?:on|by|to|at|of|in)` before the date; capitals (HY, BB, IG) stay silent; `rc1/2` (`EVOLUTION.md:49`) shows why a free `[a-z]{2}` would be wrong.
- ⚠️ **F4 — abbreviated months** (`Oct25`, `Sep30`, `Dec18`; 62 hits). Not a simple add: `Dec18 $95P` / `Oct17 68P` is option-expiry notation. Name it as NOT searched in the docstring; add only behind an option-notation guard.
- ⚠️ **F5 — ISO and M/D/YYYY glued to a word** (`Registered2026-10-20`, `through1/31/27`, `Original10/5/last_run`; 30 hits + the `(?![\d/])` lookahead drops any date followed by `/`). ISO is the fleet's primary machine-read date form. Add `[A-Za-z]{2,}(?=\d{4}-\d\d-\d\d)`, the mirror ISO+word form, and an optional `/\d{2,4}` year tail.
- ⚠️ **F6 — double count.** `October10/27`, `October15/16` fire `month` AND `word+date` (FP6) and the month suggestion "write October 10" is wrong for a range → skip the month kind when the digits are followed by `/`. The 341 figure in the commit is inflated by these.
- ⚠️ **F7 — the per-flag text is an unconditional "write X Y"** on verbatim quotes and receipted blocks. Live instance: after my re-spacing, 6 flags remain in `AGENTS/DAEDALUS/profiles/` and every one is a verbatim desk quote or a reader record (`BROCK.md:74,104`, `CARL.md:149`, two REFRESH_ reader files) — they will flag at every run forever. The closing "prompt to LOOK" line mitigates → append to the per-flag text: "leave verbatim quotes and receipted archive blocks as they are". This matters more now that `read_cap_check` tells owners to move history verbatim into `archive/` (task 2): a default changed-files run with `glued` would flag those moved lines.
- ⚠️ **F8 — STRICT rule 9.** The clean line "✓ N file(s) clean [glued]" does not say what was not searched → name the four forms and the not-searched forms (abbreviations, two-letter words, ISO, all-caps, month after a word) in the docstring and, briefly, on the clean line.
- Residue, no change proposed: an unclosed backtick masks to the next backtick and can hide a real glue (FN10); `**October**25` escapes (FN11).

**Acceptance file state:** AC1–AC6 as written are met. F1 and F2 are outside them (F2 is the "missing information" neighbour the file declared covered by "the existing partition" — the partition handles files, not check names). Independently verified: no, not yet — on F1+F2 fixed, I accept without a further read of mine unless the fix touches the masks.

## Task 2 — `scripts/read_cap_check.py` message (commit 8a385ab8e)
Message text only, two sites: the rule-5 "REMOVE N MORE B" line and the READ-CAP 1 over-budget paragraph now prescribe rotation (move dated history verbatim to `archive/` with a one-line pointer, or split hot/cold) and say never to meet the budget by deleting the spaces between words and numbers (root `CLAUDE.md` § Output Canon). No constant, threshold, rc or exit code changed. `--selftest` 131/131 before and after; watched both lines print live: `--agent DAEDALUS` rc 0 (REMOVE line), `--agent AEOLUS` rc 1 (over-budget paragraph; AEOLUS `CLAUDE.md` 149% of budget, its own, unchanged).

## Task 3 — own surfaces re-spaced
164 spaces inserted at glue points, nothing else changed: `FLEET_MAP.tsv` (14 rows), `sweeps/REGISTRY.tsv` (11 rows, incl. two hand fixes the tool misses: `Originaldue`, `Original10/5/last_run`), `EVOLUTION.md` (3 lines), and the line-3 banner of 27 profiles (+ `profiles/PROME.md:5`); `FLEET_DIRECTORY.md` regenerated (render rc 0). Re-check: 6 boot/registry files clean. The CREED cell the ruling names was already clean (re-cut at the 10/30 CREED refresh; `as-of9/28` survives only in run records and the `_prior/` snapshot). Left alone by rule: `archive/`, `runs/`, `upgrades/`, `profiles/_prior/`, reader-record profiles, and the verbatim quotes listed at F7.

## Task 4 — inbox
1 packet, from CREED (item 8: charter 40,535 → 25,448 B). Verified at the artifact: `measure.py` 25,448 B; `read_cap_check --agent CREED` rc 0, rotation_due 0; archive `AGENTS/CREED/archive/CHARTER_HISTORY_2026-10-30.md` present (e212f88b6). CONSUMED · VERIFIED; logged in `AGENTS/DAEDALUS/runs/2026-10-30_INBOX_DISPOSITIONS.md`, moved to `inbox/processed/`. CREED's L5 re-adjudication is NOT done here (a grade change, outside this task); it rides my next session with items 2–4 verified at the artifact. Note: the charter sits at 78% of budget, inside the rotate tier, but rule 20 keeps charters out of the perimeter, so nothing is owed by the tool.

## COMPLETION
STATUS: DONE (task 1 verdict HOLD on part 3 until F1 + F2 are fixed; then ACCEPT WITH NAMED RESIDUE)
CHANGED: scripts/read_cap_check.py (message text only) · AGENTS/DAEDALUS/ FLEET_MAP.tsv, FLEET_DIRECTORY.md, sweeps/REGISTRY.tsv, EVOLUTION.md, 27 profiles, STATUS.md, inbox log · this memo
RESULT: glued mode: date half is outside STRICT_TEXT's DO-NOT-BUILD; ❌ F1 counts flagged as dates (44 of 314), ❌ F2 `--check glud` certifies clean rc 0; ⚠️ F3–F8 named; 164 own glue points re-spaced
GAPS: F1–F8 fixes are PROME's (I may not edit claim_check.py); no independent reader of my own review; CREED L5 re-grade deferred to my next session
WILL_NEEDS: nothing new — F1's alternative (keep counts flagged, relabel) would be a scope change for Will's eyes
FOLLOW-UP: PROME fixes F1 + F2 then lands part 3; F3–F8 at PROME's choice; DAEDALUS re-grades CREED L5 next session (DOCKET L889 cited on STATUS)
