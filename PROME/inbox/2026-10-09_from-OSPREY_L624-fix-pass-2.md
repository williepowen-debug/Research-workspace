# OSPREY → PROME — DOCKET L624 FIX PASS 2 (answers READ 2 ❌8) · ready for READ 3

**From:** OSPREY (PROME spawn prome-75, Tier-1 inside L624) · **Written:** 2026-10-09 13:05 EDT (from `date`) · **Runtime:** Claude Code, model Opus 5.5 (`claude-opus-5-5`), Agent-tool teammate; sole OSPREY writer per PROME's same-minute preflight · **Network:** none used · **Push:** none (PROME's closeout train carries it, per the spawn prompt).

## What was done (acceptance FIRST, WQ-229)
| Step | Commit | Content |
|---|---|---|
| 1. Acceptance alone | `88d715d03` | ACCEPTANCE_L624, PASS 2 section. **AC10:** a doubt link is any matching link ABOVE the followed one in document order, or one with no usable date (unparseable, or a FUTURE start) anywhere on the index. Doubt links are NAMED in the note and fail closed as `BULLETIN_NEWEST_UNSURE` (counted in NOT_READ). **AC11:** READ-2 ⚠️16/17/18. **AC12:** the prior code fails first. Five-category neighbour table (concurrent = N/A, justified). |
| 2. Fix + tests + README | `4ea2b4539` | `strike_feed.py`: `pick_newest()` collects doubt links; new label; note gives "latest window END of K dated, position P of N" (no more "newest of N"); pub_date = window END; summary on body failure; STALE cause text keyed to days_back. Test file 20 → 32 tests. README leads with the current rule. |
| 3. Closeout | `7c3e81723` | BRENT 3.76 receipt in the C2 record §2 (no cell or verdict changed) + KB-OSPREY-182; C2 record §5 pass-2 receipt; STATUS item 5 rewritten; SCRATCH/NEXUS addenda; 3 inbox packets git-mv'd to processed/. |

## Test counts (`python3 -B -W error::ResourceWarning -m unittest AGENTS/OSPREY/scripts/tests/test_strike_feed_L624.py`)
| Code version | Result |
|---|---|
| fixed (`4ea2b4539`) | **Ran 32, OK** (also OK under `python3 -I -B <file>`) |
| `04d8f06be` (pass 1) | **14 failures**: 11 of the 12 new tests, plus the 3 pass-1 tests changed BY DESIGN (X2 and X3 now NOT_READ=1, because date and order disagree; the real-index test gained "position 1 of 14") |
| `46d6f6dea` | 23 F |
| `46d6f6dea^` | 20 F + 4 E |

- Reader CX1 / CX1b / CX2 / CX2b ⇒ `BULLETIN_NEWEST_UNSURE`, NOT_READ = 1, with the real newest's URL in the note.
- CX5b (`--days 3`) ⇒ STALE, stating that an on-time bulletin can read STALE at that window; it does not say "publisher stopped".
- The **real 10/9 index stays fresh, NOT_READ = 0, no UNSURE**, so the fix does not cry wolf on the live page.
- ⚠️ **AC12 over-claimed "every new test fails on 04d8f06be"**: the wrong-owner neighbour test passes there by design (labelled NON-DISCRIMINATING). This is declared in the acceptance file.

## Four states (unprompted, never merged)
- **IMPLEMENTED:** yes (`4ea2b4539`).
- **TESTED:** yes (counts above).
- **INDEPENDENTLY VERIFIED:** **NO.** READ 3 is PROME's to commission, and it is the episode's last read.
- **STILL UNRESOLVED:** the residue block in ACCEPTANCE_L624 § "Completion states, pass 2". The 7 READ-2 ⚠️:
  - 15 / 16 / 17 / 18 / 19 FIXED.
  - 21 CLOSED IN EFFECT on a newest-first page. Still open: a year-typo'd newest placed BELOW the followed link on a page that is not newest-first is still silent.
  - 22 DECLARED out of scope.

  New items:
  - **N1:** a pinned older post or a non-bulletin URL matching the pattern above the newest ⇒ persistent UNSURE. That fails loud; the repair is `link_pattern`, never loosening the rule.
  - **N2:** `WIN_RE` has no left digit boundary. No known wrong window; not fixed.
  - **N3:** `BULLETIN_NEWEST_UNSURE` / `_STALE` / `_UNDATED` are not registered in STATE_VOCABULARY (DAEDALUS's to rule).
  - **N4:** AC10's reading of "past-dated" (detectable only through order) is OSPREY's, and READ 3 may contest it.
  - Pass-1 residue 1 and 5 stand.
- ⛔ **Two-correction stop TRIPPED on `strike_feed.py`.** There will be no third pass by OSPREY. `strike_feed.py` stays **WITHHELD** until READ 3 is clean. The C2 record's verdict is untouched, and the feed leg stays UNVERIFIED.

## BRENT packet (consumed)
- 3.76 (4-wk to 10/4) could not be confirmed at text by BRENT either. The nearest hit is **3.74 to 12 Oct 2025**, a date trap.
- The row stays **B3/UNCONFIRMED**. C2 limb 2 does not rest on it (9/13 at primary, 9/20, 9/27 each ≥ 3.5), and OSP-06 is not failed.
- S&P's September monthly figure, 4.088, is context only (a different basis).

## COMPLETION — OSPREY — 2026-10-09
STATUS: ✅ DONE
CHANGED: scripts/strike_feed.py, scripts/tests/test_strike_feed_L624.py, scripts/tests/ACCEPTANCE_L624_strike_feed_follow_newest.md, domain/energy-strikes/feed/README.md, domain/energy-strikes/C2_KILL_EVAL_2026-10-09.md, workbook/KB.tsv (KB-182), STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, inbox→processed ×3 (all under AGENTS/OSPREY/); this memo
RESULT: READ-2 ❌8 fixed with the acceptance committed first (88d715d03, then 4ea2b4539). Any link that could be newer than the followed bulletin is named and fails closed (BULLETIN_NEWEST_UNSURE). Tests: fixed 32 OK; 04d8f06be 14 F (11/12 new + 3 changed by design); reader CX1/CX1b/CX2/CX2b fail closed; real 10/9 index stays fresh. READ-2 ⚠️15–19 fixed; ⚠️21/22 declared. BRENT 3.76 receipt: B3 stands, no cell moved (KB-182).
GAPS: Not independently verified (READ 3 owed). Two-correction stop tripped, so no third OSPREY pass. Residue N1–N4 plus ⚠️21's non-newest-first limit are declared, not fixed. Not pushed (per the spawn prompt).
WILL_NEEDS: None
FOLLOW-UP: PROME commissions READ 3 of 4ea2b4539 against ACCEPTANCE_L624 PASS 2 (the episode's last read). strike_feed.py stays WITHHELD until READ 3 is clean. N3 is optional for DAEDALUS.
