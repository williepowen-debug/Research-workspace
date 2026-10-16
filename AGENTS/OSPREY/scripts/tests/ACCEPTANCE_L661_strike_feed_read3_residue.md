# ACCEPTANCE — DOCKET L661: `strike_feed.py` READ-3 residue (a NEW episode; written BEFORE any code edit)

**Owner:** OSPREY · **Class:** WQ-229 consequential (the instrument's defect class — a dead or mis-dated source that looks like a quiet week — has recurred: DAEDALUS 9/10, L309 10/8, L624 10/9) ⇒ an independent reader devises ≥1 counterexample of its own before this is called fixed. · **Written:** 2026-10-16 17:12 EDT (from `date`), OSPREY session `osprey-1016` (PROME prome-7b spawn, Tier 1, WQ-184 due row). · **Committed alone, before any edit to `strike_feed.py`, its tests or the feed README.**
**reads: 0** — this episode's budget is fresh (DOCKET L661). The L624 episode's three reads are SPENT; its record stays in `ACCEPTANCE_L624_strike_feed_follow_newest.md` (same dir) and `PROME/reports/2026-10-09_L624_strike-feed-patch_read_{1,2,3}.md`. PROME commissions this episode's reads.
**Baseline code:** `strike_feed.py` at `4ea2b4539` (RELEASED 10/9 at L624 with declared limit ⚠️21; `46e5e67bf` changed text only).

## The defect, in its own terms

`pick_newest()` follows the matching link with the latest window END (title first, slug second) and names a link as a DOUBT only if it sits ABOVE the followed link or has no usable date. READ 3 (`PROME/reports/2026-10-09_L624_strike-feed-patch_read_3.md`) showed it still discards three free tells and mis-states one date:
- **⚠️2 ORDER.** A date-typo'd real newest listed BELOW the followed link is skipped silently. R3-Q: a pinned 28 Sep–4 Oct link on top, the real newest past-year-typo'd "5th - 11th October 2025" below it, 21–27 Sep below that, run 10/13 ⇒ `BULLETIN — read manually`, NOT_READ 0, the real newest nowhere. The ENDs down the page run 10-04, **2025-10-11**, 09-27: not monotone, so the order tell exists for every such link except the LAST one on the page. **And** `parse_html_index` dedup (:84) keeps a duplicate's FIRST listing (a featured spot), discarding the list position that would have put the real newest ABOVE the followed link.
- **⚠️4 TITLE vs SLUG.** When a link's title and slug disagree by a year, the title wins with no note. R3-H: slug 2025, title 2026, run 10/13 ⇒ fresh, NOT_READ 0, nothing said. This tell catches CX1-shape typos (title typo, slug right) whatever the page order.
- **⚠️3 TWO-YEAR WINDOW.** "29th December 2026 - 4th January 2027" does not parse (title or slug: L624 pass-1 residue 2). The code falls back to the slug's single date (12-29), writes `pub_date = window END` (false: it is the window START), and read 2027-01-12 shows `BULLETIN_STALE … publisher stopped` on an on-time bulletin, ~6 days early (R3-I2). Loud, but the label states a false cause.
- **⚠️5** AC10's "up to 5, then +N more" and its UNDATED naming clause hold but no test pins them: mutants M4 (`doubts[:5]`→`[:1]`) and M5 (doubt note dropped when UNDATED) pass the suite.
- **⚠️6** `ACCEPTANCE_L624…:94` (AC12 "Every new pass-2 test FAILS") is left live beside its own correction at :120.
- **⚠️7** A page that is not newest-first gives a permanent loud UNSURE (fails safe; alarm-fatigue risk).

## Acceptance conditions (properties; each must hold on the test file named below)

Terms. **Matching link:** an index anchor whose href contains `link_pattern`. **Listing:** one occurrence of a matching link in document order (a link can be listed more than once). **Dated:** has a usable window — title first, slug second, single date third — with START ≤ run date. **Followed:** the dated link with the latest window END, ties to document order (AC1, unchanged). **Doubt link:** AC10's term — named in the note, the row reads `BULLETIN_NEWEST_UNSURE`, counted in NOT_READ, one row, `BULLETIN_STALE` carried inside when also stale (AC10's handling is unchanged; only who counts as a doubt grows). **Every new rule runs only on a `follow_newest` source.**

- **AC13 — ORDER (⚠️2a).** A dated link listed below every listing of the followed link, whose window END is EARLIER than the END of some dated link listed below it, is a doubt link. Its reason names that later link and both ENDs (`out of date order: END X listed above <url> END Y`).
  - Must fail closed: **R3-Q** (as above, run 10/13) ⇒ UNSURE, NOT_READ 1, the 2025-typo'd URL named with the order reason.
  - Must NOT fire: ENDs that never increase down the page, ties allowed — the real 10/9 fixture and a new real 10/16 fixture (AC21) ⇒ fresh, NOT_READ 0, `position 1 of 14`.
- **AC14 — DUPLICATE LISTINGS (⚠️2b).** A link listed more than once keeps its first listing's data, and every listing is kept as a position. A link whose first listing is above ANY listing of the followed link is a doubt link — AC10(a) is measured against the followed link's LOWEST listing. When the link sits between the followed link's first and lowest listings, the reason says so.
  - Must fail closed: a featured copy of last week's bulletin at the top, then the list — the past-year-typo'd real newest, then last week's bulletin again, and nothing below (so AC13 has no later link to compare) ⇒ UNSURE naming the real newest.
  - Must NOT fire: a featured copy of the followed link directly above its own list entry (nothing between) ⇒ fresh, NOT_READ 0; the note says the followed link is listed twice.
  - **Cost, declared before the edit:** a followed link ALSO listed at the bottom of the page (e.g. a sidebar rendered after the list) makes every link above that listing a doubt — loud, the safe direction, ⚠️7 class. The live index lists every matching link exactly once on 10/9 and on 10/16.
- **AC15 — TITLE vs SLUG (⚠️4).** For a link whose title window AND slug reading (the slug's window, else the slug's single date) both exist and lie **more than 180 days apart** (the gap between the two windows; a year-class disagreement), the disagreement is never resolved silently when a reading could change the row:
  - (i) on the FOLLOWED link, if the slug reading's START ≤ run date ⇒ a doubt naming the followed link itself (its own date is in doubt), with both readings;
  - (ii) on any OTHER link, if the slug reading's START ≤ run date and its END is later than the followed END ⇒ a doubt, with both readings.
  - Must fail closed: **R3-H** (one link, slug 2025, title 2026, run 10/13) ⇒ UNSURE, NOT_READ 1 (was fresh, NOT_READ 0). A CX1-shape link (title year typo, slug right) listed BELOW the followed link and LAST on the page ⇒ UNSURE through (ii).
  - Must NOT fire: the live mis-slug (title 14–20 Sep, slug 7–13 Sep — 1 day apart) ⇒ no doubt, in both real fixtures. A year-class disagreement on an old link whose slug reading ends before the followed END ⇒ no doubt. A slug reading with a FUTURE start ⇒ no doubt (an impossible reading cannot change the row).
- **AC16 — TWO-YEAR WINDOW (⚠️3; closes L624 pass-1 residue 2).** `bulletin_window` parses "29th December 2026 - 4th January 2027" (title) and "29th-december-2026-4th-january-2027" (slug) as 2026-12-29..2027-01-04. The second year must equal the first or the first + 1; the 0–14-day span check still applies.
  - **R3-I2** read 2027-01-12 (cutoff 2027-01-02) ⇒ fresh `BULLETIN — read manually`, `pub_date` 2027-01-04, not STALE.
  - When only a single date is available (basis `slug date`), the note never says `pub_date = window END`. It says the END is unknown and the date may be the window START. A STALE label on that basis says an on-time bulletin can read STALE up to ~6 days early.
  - Must not regress: every one-year form that already parsed — all 14 real titles in each real fixture, cross-month and within-month, and every L624 test window — parses to the same window.
- **AC17 — AC10's two unpinned clauses get tests (⚠️5).** (a) With 7 doubt links the note names exactly 5 and then `+2 more`. (b) A `BULLETIN_UNDATED` row's note names the other unusable link(s). Mutants M4 (`doubts[:5]`→`doubts[:1]`) and M5 (doubt note dropped when no eligible dated link exists) each FAIL the suite.
- **AC18 — `ACCEPTANCE_L624…:94` (⚠️6).** AC12's wording is replaced in place by the accurate statement (every DISCRIMINATING pass-2 test fails on `04d8f06be`; the one must-not-reach neighbour test is labelled NON-DISCRIMINATING). The history is a pointer to this file and git, not a second live instruction.
- **AC19 — no change elsewhere.** The 32 L624 tests pass unchanged. Non-follow `html_index` and RSS sources are unchanged (no new doubt reasons; same rows). COLS unchanged; the summary line unchanged in form.
- **AC20 — fails first.** Every new DISCRIMINATING test fails with `STRIKE_FEED_PATH` = a copy of `4ea2b4539`'s `strike_feed.py`. A test that passes there by design is labelled NON-DISCRIMINATING in its docstring (the must-not-fire tests, and AC17's pins of behaviour the released code already has — their discrimination is shown by the mutants).
- **AC21 — live must-not-fire evidence (evidence, not a test).** The live index fetched 2026-10-16 17:10 EDT (one GET; no feed run): 14 matching links, each listed once, newest-first (newest 5–11 Oct), no title/slug disagreement wider than the known 1-day mis-slug. It is added as a NEW dated fixture (trimmed the same way as the 10/9 one; the 10/9 fixture is not refreshed in place), and the new rules raise no doubt on it.

## Neighbours (CONSIDER all five)

| # | Category | Disposition |
|---|---|---|
| 1 | Ordinary | Both real fixtures (10/9, 10/16) ⇒ fresh, NOT_READ 0, `position 1 of 14`, no doubt. Tested. |
| 2 | Overlap | One link meeting two new rules (order + title/slug) ⇒ ONE doubt entry carrying both reasons, counted once. A new doubt + a stale followed bulletin ⇒ one UNSURE row carrying `BULLETIN_STALE`. A new doubt + a body-fetch failure ⇒ one `FETCH_FAILED (newest post)` row whose note carries `BULLETIN_NEWEST_UNSURE` and the name. Tested. |
| 3 | Wrong owner | The new rules run only under `follow_newest`. A non-follow `html_index` with out-of-order and duplicate links is unchanged (rows, NOT_READ). Tested (NON-DISCRIMINATING by design). |
| 4 | Missing information | Title-only link (no slug date) and slug-only link (title unparsed) ⇒ no title/slug comparison, no AC15 doubt. Undated links stay AC10(b) doubts and are left out of AC13's comparison. A single-date basis is labelled per AC16. Tested. |
| 5 | Concurrent activity | N/A — single-writer CLI, one dated output pair per run (unchanged by this episode). |

## Not in scope, declared before the edit

- **⚠️7 is NOT changed.** Every candidate fix suppresses a fail-closed alarm, i.e. trades loud-and-safe for silent. N1's repair (fix `link_pattern`, or re-check the layout) stands.
- **N2** (`WIN_RE` has no left digit boundary): unchanged; no wrong window is known. The new two-year pattern carries its own left boundary.
- **N3** (state-token registration): DAEDALUS's to rule.
- **⚠️21's limit after AC13–AC15, stated so no surface over-claims it:** (i) a date-typo'd real newest listed below the followed link, LAST on the page, with title and slug agreeing (both typo'd) is still silent — no index-level signal exists for it; (ii) an under-dated typo that still fits the page's date order (e.g. a same-year month typo landing between two honest links) is silent; (iii) title/slug disagreements of 180 days or less are resolved to the title without a note (the live page carries a benign 1-day mis-slug, so any tighter threshold must stay above it).

## Files

- Tests: `AGENTS/OSPREY/scripts/tests/test_strike_feed_L661.py` (new; reuses the L624 harness by import), plus the unchanged `test_strike_feed_L624.py`.
- Fix: `AGENTS/OSPREY/scripts/strike_feed.py`; README `AGENTS/OSPREY/domain/energy-strikes/feed/README.md`; ⚠️6 in `ACCEPTANCE_L624_strike_feed_follow_newest.md`.
- New real fixture: `AGENTS/OSPREY/scripts/tests/fixtures/palaemon_index_2026-10-16_anchors.html`.

## Completion states (never merged) — filled after the edit
*(pending — written in the fix commit)*
