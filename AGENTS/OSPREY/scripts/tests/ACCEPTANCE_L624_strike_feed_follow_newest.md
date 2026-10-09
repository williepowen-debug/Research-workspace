# ACCEPTANCE — DOCKET L624: `strike_feed.py` follow_newest bulletin (written BEFORE the fix edit)

**Owner:** OSPREY · **Class:** WQ-229 consequential (a RECURRED dead-source-looks-quiet defect) ⇒ an independent reader devises ≥1 counterexample of its own before this is called fixed. · **Written:** 2026-10-09 10:56 EDT (from `date`), OSPREY fix-pass session. · **Committed alone, before any edit to `strike_feed.py`.**
**reads: 2** — read 1: coldread-l624 (Opus, PROME prome-75), 2026-10-09 10:30 EDT, ledger `PROME/reports/2026-10-09_L624_strike-feed-patch_read_1.md` → STILL UNRESOLVED (3 ❌ · 4 ⚠️). Read 2: coldread-l624-2, 2026-10-09 11:09 EDT, ledger `PROME/reports/2026-10-09_L624_strike-feed-patch_read_2.md` → STILL UNRESOLVED (1 ❌ · 7 ⚠️) — answered by **PASS 2** below; READ 3 (the episode's last) is PROME's to commission.

## The defect, in its own terms

The `follow_newest` source (Palaemon's weekly maritime-security bulletin, client-rendered, `BULLETIN — read manually`) is the feed's only maritime-dated leg. A source that yields no row, or a row indistinguishable from a fresh read, looks like a quiet week (DAEDALUS 9/10 finding (3); recurred at L309 10/8). Patch `46d6f6dea` exempted the whole SOURCE from the age filter. Read 1 found:
- ❌3 the evidence offered (10/9 row, cross-month slug dated by its LAST day 10/04 ≥ cutoff 9/29) passes the OLD filter too — it cannot discriminate.
- ❌9 the exemption is keyed on the source, and `items = [newest]` only runs when the body fetch succeeds — on a body-fetch failure every index link skips the age filter (X1: May/June bulletins emitted).
- ❌10 a months-old bulletin emits `BULLETIN — read manually`, NOT_READ=0, identical to a fresh read; and `newest = items[0]` takes document order, so an older link first on the page is shown as the week's bulletin and the real newest is dropped with no trace (X2).
- ⚠️ no test file · undated bulletin never labelled `UNDATED` (README:14) · the `[body not machine-readable …]` warning is appended to a field never written (:184).

## Acceptance conditions (properties; each must hold on the test file below)

- **AC1 — the followed bulletin is the NEWEST dated link, not the first in document order.** Among the index links matching `link_pattern`, the followed item is the one with the latest bulletin-window END date; ties keep document order. Older index links are never emitted as rows by this source. *(X2 must fail closed: the June link first on the page is NOT the row; the 28 Sep–4 Oct link is.)*
- **AC2 — the age-filter exemption covers exactly ONE item: the followed bulletin.** No other index link of a `follow_newest` source, and no item of any other source, bypasses the age filter. On a body-fetch failure the source emits exactly one `FETCH_FAILED (newest post)` row naming the followed URL and its date, and NO other index links. *(X1 must fail closed: body 503 ⇒ 1 row, no May/June rows, NOT_READ ≥ 1.)*
- **AC3 — a stale bulletin is labelled and counted NOT READ.** If the followed bulletin's window END date is before the run's cutoff (`run_date − days_back`), its row carries `ledger_match` = `BULLETIN_STALE …` (naming the bulletin date and the cutoff) and the printed `NOT_READ` count includes it. *(d_stale_months: a 2026-06-01 bulletin read 10/9 ⇒ BULLETIN_STALE, NOT_READ=1.)* **Basis choice, stated because a reader checks it:** staleness is measured on the window END, not on the slug's first day — the slug regex dates a within-month window by its first day and a cross-month window by its last, so a first-day test would mark a legitimately newest within-month bulletin stale (the L309 case, read ≥10 d after its week opened). END is the latest date the bulletin can cover, so END < cutoff means nothing in the bulletin is inside the window.
- **AC4 — the L309 reproduction is DISCRIMINATING evidence.** A within-month bulletin whose slug start date is BEFORE the cutoff but whose window end is inside it (21st–27th Sep read 10/2, cutoff 9/22): pre-patch code ⇒ 0 rows (silent); fixed code ⇒ one fresh `BULLETIN — read manually` row, NOT_READ=0. This replaces the 10/9 row as the TESTED evidence; the 10/9 shape is kept only as a labelled non-discriminating regression.
- **AC5 — an undated or implausibly dated bulletin is labelled and counted NOT READ.** If no matching link has a parseable date, the followed item is the first link and its row reads `BULLETIN_UNDATED …` (README's UNDATED label, applied to the bulletin row), counted in NOT_READ — freshness unknown fails closed. A link whose slug START date is after the run date (X3, year typo 2062) is ineligible as newest and is named in the row's note; if no eligible dated link remains, the row is `BULLETIN_UNDATED`.
- **AC6 — the body warning reaches the output.** When the bulletin body is under 1,500 chars after tag-stripping (client-rendered page or bot-block stub), the row's `note` column carries `[body not machine-readable — client-rendered page; open the URL]` with the character count; an empty body (X4) is distinguishable from a short one in that note.
- **AC7 — no behaviour change elsewhere.** RSS and non-follow `html_index` sources: stale items still filtered, FETCH_FAILED / EMPTY_FEED / PARSER_STALE rows unchanged, diff/match logic untouched, no new columns (COLS unchanged).
- **AC8 — the old code is seen to fail first.** The test file runs against any module path (`STRIKE_FEED_PATH`); run against `46d6f6dea` it FAILS AC1, AC2, AC3, AC5, AC6; run against `46d6f6dea^` it FAILS AC4. Both runs are recorded below.
- **AC9 — re-runnable by a stranger.** One committed test file, stdlib `unittest` only, no network, no read of the live tree's ledger or feed dir (fixtures build their own config, ledger and out_dir in a temp dir; `fetch` and the date are injected).

## Neighbours (CONSIDER all five; justified N/A is an answer)

| # | Category | Disposition |
|---|---|---|
| 1 | Ordinary | fresh cross-month bulletin (10/9 shape) and fresh within-month bulletin (AC4) ⇒ one `BULLETIN — read manually` row, NOT_READ=0. Tested. |
| 2 | Overlap | the followed bulletin in TWO failure states at once — body fetch FAILED **and** stale ⇒ exactly one row (the FETCH_FAILED one, carrying the stale date in its note), NOT_READ counted once, not twice. Two links with the SAME window end ⇒ document order. Tested. |
| 3 | Wrong owner | the exemption must not reach other sources: a config with palaemon + a stale RSS item + a stale non-follow html_index item ⇒ both stale items filtered. Tested (AC7). |
| 4 | Missing information | undated slug (AC5) · future-dated slug (AC5/X3) · empty body (AC6/X4) · index with zero matching links (EMPTY_FEED, unchanged). Each fails loud. Tested. |
| 5 | Concurrent activity | N/A: single-writer CLI, one run per session, writes one dated output pair; a second same-day run overwrites (pre-existing, unchanged by this fix). |

## Files

- Test file: `AGENTS/OSPREY/scripts/tests/test_strike_feed_L624.py` (added in the fix commit).
- Fix: `AGENTS/OSPREY/scripts/strike_feed.py`; README `AGENTS/OSPREY/domain/energy-strikes/feed/README.md` (labels).

## Completion states (never merged) — filled 2026-10-09 11:01 EDT (from `date`)

- **IMPLEMENTED:** `strike_feed.py` — `bulletin_window()` (window START..END from the anchor TITLE first, slug second; cross-year by month order; span 0–14 d else unparsed), `pick_newest()` (latest END, ties → document order, START after run date ineligible and named), the followed-bulletin block moved out of the index `try` (one followed item on body success; on body failure ONE `FETCH_FAILED (newest post)` row carrying the followed date, its stale/undated label and window, `items = []`), the age-filter exemption keyed on the ITEM (`it.get("followed")`), labels `BULLETIN_STALE` / `BULLETIN_UNDATED`, body warning to `note` (char count; `EMPTY` distinguished), `NOT_READ` counts `NOT_READ_TITLES` (title) + `NOT_READ_MATCHES` (ledger_match), EMPTY_FEED / PARSER_STALE keyed on the INDEX count (`n_index`) so narrowing to one item cannot trip them, summary names the followed label. Also one pre-existing line: config read via `with open(...)` (the unclosed handle made the `-W error::ResourceWarning` run noisy). README labels updated.
- **TESTED:** `python3 -W error::ResourceWarning -m unittest AGENTS/OSPREY/scripts/tests/test_strike_feed_L624.py` → **Ran 20, OK** (`grep -c 'def test_'` = 20). **Fails first (AC8):** same file with `STRIKE_FEED_PATH` = `git show 46d6f6dea:…/strike_feed.py` → **12 failures** (AC1 ×3, AC2 ×2, AC3 ×2, AC5 ×3, AC6 ×2); with `46d6f6dea^` → **11 failures + 2 errors** (the AC4 within-month reproduction FAILS there, as required; the 2 errors are IndexError on 0 rows = the silent drop). The 10/9-shape test passes on all three versions and is labelled non-discriminating. AC7's three regression tests pass on all three versions (no change elsewhere). *(Corrected in pass 2, read-2 ⚠️15: this line said "four". The class has three: wrong_owner, index_404_and_empty, columns_unchanged. The 10/9-shape test is AC4's.)* Real fixture: all 14 live titles parse to a window; the live mis-slugged link (`…7th-13th-september-2026-1`) reads 14–20 Sep from its title.
- **INDEPENDENTLY VERIFIED:** **NO — pending READ 2** (PROME commissions; WQ-229 consequential class). Passing the author's suite establishes TESTED only.
- **STILL UNRESOLVED / declared residue (⚠️, not fixed):**
  1. Read-1 ⚠️7 stands: the 9/19–9/24 missing-bulletin runs are not on disk and the on-disk 9/29 run has no palaemon row, so "the patch covers every observed absence" is not established from disk. No code change can repair that evidence base.
  2. A cross-year SLUG with the year mid-string (`29th-december-2026-4th-january-2027`) does not parse as a window; the TITLE does, and the title is read first. Slug-only cross-year falls back to the legacy single date.
  3. A PAST-year typo on the real newest (2025 for 2026) is not caught: the link sorts as old, a genuinely older bulletin is followed, and the typo'd one is dropped with no note. The future-date guard covers only START > run date.
  4. The followed body is cut at 20,000 chars; the live page normalises to 715,081 chars, script-dominated, with the incident list at char ~480,659 — so `matched_tokens` on the bulletin row are not read from the report text. Pre-existing; out of L624 scope; the row still says read manually.
  5. Network was used once, only to build the real fixture (index 200, 1,160,782 B; one post 200, 909,909 B). No live `strike_feed.py` run was made in this session.

---

# PASS 2 — READ 2 ❌8 (acceptance written BEFORE the pass-2 edit)

**Written:** 2026-10-09 12:58 EDT (from `date`), OSPREY fix-pass-2 session (PROME prome-75 spawn). **Committed alone, before any pass-2 edit to `strike_feed.py`.**
**reads: 2** — read 2: coldread-l624-2 (Opus, PROME prome-75), 2026-10-09 11:09 EDT, ledger `PROME/reports/2026-10-09_L624_strike-feed-patch_read_2.md`. It found **STILL UNRESOLVED** (24 claims: 16 ✅ · 7 ⚠️ · 1 ❌) against fix `04d8f06be`. ⚠️ **This is OSPREY's SECOND correction pass on this file, so the two-correction stop trips after it.** Any later change needs READ 3, the episode's last read. `strike_feed.py` stays **WITHHELD** from operational use until READ 3 is clean.

## The defect (❌8, in its own terms)

`pick_newest()` skips a link with an unusable date and leaves no note (`if s is None: continue`). It names only FUTURE links. Then the note writes "newest of N index links" on an older item. So when the real newest has a date defect, last week's bulletin is followed and labelled fresh (`BULLETIN — read manually`, NOT_READ=0), and the real newest appears nowhere. This is the "row indistinguishable from a fresh read" that AC3/AC5 exist to end. Pass-1 residue 3 (past-year typo) was this silence written down as a limit. The four failing cases:
- **CX1:** title year typo on a cross-year newest ("29th December - 4th January 2026", slug `…-2027`).
- **CX1b:** past-year typo in title AND slug.
- **CX2:** format drift ("5th - 11th Oct 2026").
- **CX2b:** "Week 41, 2026".

The live index is newest-first in document order (real fixture). So a followed item that is not the first matching link is a free tell, and the code threw it away.

## Acceptance conditions (pass 2)

- **AC10: no matching link that could be newer than the followed bulletin is skipped silently.** A **doubt link** is any matching index link of a `follow_newest` source, other than the followed one, that meets either test:
  - **(a)** it sits ABOVE the followed link in document order; or
  - **(b)** it has no usable window date, anywhere on the index. That covers an unparseable date (format drift) and a START after the run date (future typo).

  If one or more doubt links exist and the followed bulletin is dated, the row is handled as follows:
  - its `ledger_match` reads `BULLETIN_NEWEST_UNSURE …`, and NOT_READ counts it;
  - its `note` names every doubt link (URL plus the reason: *above the followed link* / *no parseable date* / *FUTURE start*), up to 5, then "+N more";
  - if the followed bulletin is also stale, the label says `BULLETIN_STALE` inside it. It is still one row, counted once.

  If no eligible dated link exists, the row is `BULLETIN_UNDATED` as before, and the note names the other unusable links. On a body-fetch failure, the one `FETCH_FAILED (newest post)` row's note carries the same tokens and names. The note never says "newest" for the followed item. It says "latest window END of K dated links, position P of N".
  - **Counterexamples that must fail closed:** CX1 · CX1b · CX2 · CX2b ⇒ `BULLETIN_NEWEST_UNSURE`, NOT_READ = 1, the real newest's URL in the note.
  - **Pass-1 expectations SUPERSEDED BY DESIGN, stated so a reader does not read them as regressions:**
    - X2 (a June "most read" link above the real newest) changes NOT_READ 0 → 1.
    - X3 (a 2062 future typo above the real newest) changes NOT_READ 0 → 1.

    In both, date and document order disagree, and the safe direction is NOT read. AC1 still holds: the followed row is the 28 Sep–4 Oct link, and no older link is emitted as a row.
  - **Must NOT fire (no crying wolf):** the real 10/9 index (14 links, newest-first) read 10/9 ⇒ fresh, NOT_READ = 0, no `NEWEST_UNSURE`. Dated links BELOW the followed one are not doubt links.
  - **Interpretation, stated because the reader can contest it:** the owner's "past-dated" is detectable only through order. A past-typo'd real newest sits ABOVE the followed link on a newest-first page, so (a) catches it. A past-typo'd link BELOW the followed one looks the same as an honest older bulletin. That case is declared residue, not fixed.
- **AC11: the three READ-2 ⚠️ that are code (16, 17, 18) are fixed.**
  - **⚠️16:** the followed row's `pub_date` = the window END (the date staleness keys on), and the note says `pub_date = window END`. Live mis-slug fixture: `pub_date` 2026-09-20, not 2026-09-07.
  - **⚠️17:** on a body-fetch failure, the stdout summary reads `(followed: FETCH_FAILED (newest post))`, never `(followed: BULLETIN)`.
  - **⚠️18:** `BULLETIN_STALE` names its cutoff basis (`run − days_back N d`). When `days_back` < 10, it says an on-time weekly bulletin can read STALE at that window, and it does not give "publisher stopped" as the cause. CX5b: `--days 3`, 28 Sep–4 Oct read 10/9 ⇒ `BULLETIN_STALE` (still NOT_READ, the safe direction) with `days_back 3` and `on-time` in the label.
- **AC12: the prior code fails first (AC8, pass 2).** Every new pass-2 test FAILS with `STRIKE_FEED_PATH` = a copy of `04d8f06be`'s `strike_feed.py`. The fixed code passes the whole file, old tests included.

## Neighbours (pass 2; CONSIDER all five)

| # | Category | Disposition |
|---|---|---|
| 1 | Ordinary | real 10/9 index ⇒ fresh, NOT_READ 0, no UNSURE. Older dated links BELOW the followed one (AC7 `index(OCT, JUN)`, AC2 body-success) ⇒ no doubt. Tested. |
| 2 | Overlap | doubt + stale followed bulletin ⇒ one row, `NEWEST_UNSURE` naming the doubt link AND carrying `BULLETIN_STALE`, NOT_READ 1. doubt + body-fetch failure ⇒ one `FETCH_FAILED (newest post)` row whose note carries `BULLETIN_NEWEST_UNSURE` and the name, NOT_READ 1. Tested. |
| 3 | Wrong owner | the doubt rule runs only on `follow_newest` sources. A non-follow `html_index` with an undated link listed first is unchanged: no UNSURE, NOT_READ 0. Tested. |
| 4 | Missing information | an unparseable link BELOW the followed one ⇒ still a doubt link (the index's newest is unknown) ⇒ UNSURE. A future-start link below ⇒ UNSURE. Tested. Duplicate hrefs keep their first position (pre-existing dedup, unchanged; not re-tested). |
| 5 | Concurrent activity | N/A, as in pass 1: a single-writer CLI with one dated output pair per run. |

## Completion states, pass 2 (never merged). Filled 2026-10-09 13:02 EDT (from `date`)

- **IMPLEMENTED** (`strike_feed.py`):
  - `pick_newest()` records each link's document position. It collects **doubt links**: links above the followed one, plus any link with no parseable date or a FUTURE start, anywhere on the index. It returns `(followed, eligible, doubts, n_dated)`.
  - New label `BULLETIN_NEWEST_UNSURE`, added to `NOT_READ_MATCHES`. Its note names every doubt link and its reason (5 shown, then "+N more"). When the followed bulletin is also stale, the label carries `BULLETIN_STALE` inside it.
  - The note says "latest window END of K dated index link(s), position P of N in document order". "newest of N" is gone.
  - `pub_date` = window END for the followed row (⚠️16).
  - The summary reads `(followed: FETCH_FAILED (newest post))` on a body failure (⚠️17).
  - The STALE text names `run − days_back N d`. Below `CADENCE_DAYS` = 10 it says an on-time bulletin can read STALE, and gives no publisher cause. With a doubt link present it names the doubt link as a possible cause (⚠️18).
  - On a body failure, the FETCH_FAILED note carries every `BULLETIN_*` state token.
  - The output-file header lists the new label.
  - README: the `BULLETIN_NEWEST_UNSURE` row, the `BULLETIN` and `BULLETIN_STALE` rows reworded, and the follow_newest bullet now leads with the current rule, with history after it (⚠️19).
- **TESTED:** `python3 -B -W error::ResourceWarning -m unittest AGENTS/OSPREY/scripts/tests/test_strike_feed_L624.py` gives **Ran 32, OK**, and `python3 -I -B <test file>` also gives OK. That is 12 new tests (AC10 ×9, AC11 ×3) plus 3 pass-1 tests changed by design (X2, X3, real index).
  - **Fails first (AC12):** `STRIKE_FEED_PATH` = `git show 04d8f06be:…/strike_feed.py` gives **14 failures**: 11 of the 12 new tests, plus all 3 changed tests.
  - ⚠️ **AC12 as written over-claimed "every new pass-2 test FAILS".** `test_wrong_owner_non_follow_index_unchanged` passes on `04d8f06be` by design: it is a must-not-reach neighbour test, labelled NON-DISCRIMINATING in its docstring, like pass 1's 10/9-shape test.
  - Older versions for the record: `46d6f6dea` gives 23 F, and `46d6f6dea^` gives 20 F + 4 E.
  - Reader CX1 / CX1b / CX2 / CX2b each give `BULLETIN_NEWEST_UNSURE`, NOT_READ = 1, with the real newest named in the note. CX5b gives STALE with `days_back 3 … on-time`.
  - The real 10/9 index stays fresh, NOT_READ = 0, at "position 1 of 14", with no UNSURE.
- **INDEPENDENTLY VERIFIED: NO.** READ 3 is PROME's to commission, and it is the episode's last read. ⛔ This is OSPREY's second correction pass on this file, so the two-correction stop has tripped. Any further change needs READ 3's independent eye. `strike_feed.py` stays **WITHHELD** from operational use until READ 3 is clean.
- **STILL UNRESOLVED / declared residue (pass 2):** each of READ 2's seven ⚠️ is named, then the new items.
  - ⚠️15: **FIXED**. The pass-1 TESTED line is corrected in place, with a marker.
  - ⚠️16, ⚠️17, ⚠️18: **FIXED** (AC11, tested).
  - ⚠️19: **FIXED** (README).
  - ⚠️21: **CLOSED IN EFFECT on a newest-first page.** CX1 now fails closed through AC10(a), because the typo'd newest sits above the followed link. Title-first and pass-1 residue 2 (a cross-year slug with the year mid-string does not parse) are **unchanged**. Remaining limit: on a page that is NOT newest-first, a year-typo'd real newest placed BELOW the followed link looks the same as an older bulletin and is still skipped. An order signal does exist for every such link except the LAST one on the page (see N6; READ 3 ⚠️2).
  - ⚠️22: **DECLARED out of scope; pass-1 residue 4 stands.** The `matched_tokens` on the BULLETIN row come from the first 20,000 chars of a script-dominated page, not from the report. The row still says read manually.
  - Pass-1 residue 3 (past-year typo): **SUPERSEDED.** AC10 closes it for the newest-first case, and the remaining limit is the same as ⚠️21's.
  - Pass-1 residue 1 (the 9/19–9/24 evidence base is not on disk) and residue 5 stand.
  - **N1, false alarms in the loud direction.** A pinned or featured older post, or a non-bulletin URL matching `link_pattern` above the newest, makes every run `BULLETIN_NEWEST_UNSURE` until the page changes. The live 10/9 index has none (real-fixture test). If it appears, the repair is `link_pattern`, never loosening AC10.
  - **N2.** `WIN_RE` has no left digit boundary, so `\d{1,2}` can start inside a year. For example, `…2026-4th-january-2027` is tried as day 26. The 0–14-day span check rejects the one case found. No wrong window is known. Not fixed: noticed in pass 2 and outside ❌8.
  - **N3.** `BULLETIN_NEWEST_UNSURE`, like pass 1's `BULLETIN_STALE` and `BULLETIN_UNDATED`, is a script-output token. It is not registered in `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md`, which is DAEDALUS's to rule.
  - **N4.** AC10's reading of "past-dated" (detectable only through order) is OSPREY's. READ 3 may contest it.
  - **N5.** No network was used in pass 2, and no live `strike_feed.py` run was made.
  - **N6 (added 2026-10-09 after READ 3 ⚠️2; text only, no code change).** Two signals are unused.
    - **Order:** on a page that is not newest-first, a date-typo'd newest below the followed link breaks the monotone run of window ENDs down the page. READ 3 R3-Q ran 10-04, then 2025-10-11, then 09-27. That breaks the monotone run for every such link except the last. The real 10/9 fixture's 14 ENDs are monotone non-increasing, so a "dated link below the followed one whose END is later than an earlier link's" doubt rule would not fire on the live page.
    - **Dedup:** `parse_html_index` keeps a duplicate's FIRST position, which loses the list position.
    - A title-vs-slug year disagreement (READ 3 ⚠️4) is a second unused tell.
    - Not fixed here: the two-correction stop has tripped on `strike_feed.py`. PROME registers a DOCKET row for an out-of-order-date check as a later, separate episode. READ 3 ⚠️3/⚠️5/⚠️6/⚠️7 travel with it.
