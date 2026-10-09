# ACCEPTANCE — DOCKET L624: `strike_feed.py` follow_newest bulletin (written BEFORE the fix edit)

**Owner:** OSPREY · **Class:** WQ-229 consequential (a RECURRED dead-source-looks-quiet defect) ⇒ an independent reader devises ≥1 counterexample of its own before this is called fixed. · **Written:** 2026-10-09 10:56 EDT (from `date`), OSPREY fix-pass session. · **Committed alone, before any edit to `strike_feed.py`.**
**reads: 1** — read 1: coldread-l624 (Opus, PROME prome-75), 2026-10-09 10:30 EDT, ledger `PROME/reports/2026-10-09_L624_strike-feed-patch_read_1.md` → STILL UNRESOLVED (3 ❌ · 4 ⚠️). The fix that answers it is UNREVIEWED until READ 2.

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
- **TESTED:** `python3 -W error::ResourceWarning -m unittest AGENTS/OSPREY/scripts/tests/test_strike_feed_L624.py` → **Ran 20, OK** (`grep -c 'def test_'` = 20). **Fails first (AC8):** same file with `STRIKE_FEED_PATH` = `git show 46d6f6dea:…/strike_feed.py` → **12 failures** (AC1 ×3, AC2 ×2, AC3 ×2, AC5 ×3, AC6 ×2); with `46d6f6dea^` → **11 failures + 2 errors** (the AC4 within-month reproduction FAILS there, as required; the 2 errors are IndexError on 0 rows = the silent drop). The 10/9-shape test passes on all three versions and is labelled non-discriminating. AC7's four regression tests pass on all three versions (no change elsewhere). Real fixture: all 14 live titles parse to a window; the live mis-slugged link (`…7th-13th-september-2026-1`) reads 14–20 Sep from its title.
- **INDEPENDENTLY VERIFIED:** **NO — pending READ 2** (PROME commissions; WQ-229 consequential class). Passing the author's suite establishes TESTED only.
- **STILL UNRESOLVED / declared residue (⚠️, not fixed):**
  1. Read-1 ⚠️7 stands: the 9/19–9/24 missing-bulletin runs are not on disk and the on-disk 9/29 run has no palaemon row, so "the patch covers every observed absence" is not established from disk. No code change can repair that evidence base.
  2. A cross-year SLUG with the year mid-string (`29th-december-2026-4th-january-2027`) does not parse as a window; the TITLE does, and the title is read first. Slug-only cross-year falls back to the legacy single date.
  3. A PAST-year typo on the real newest (2025 for 2026) is not caught: the link sorts as old, a genuinely older bulletin is followed, and the typo'd one is dropped with no note. The future-date guard covers only START > run date.
  4. The followed body is cut at 20,000 chars; the live page normalises to 715,081 chars, script-dominated, with the incident list at char ~480,659 — so `matched_tokens` on the bulletin row are not read from the report text. Pre-existing; out of L624 scope; the row still says read manually.
  5. Network was used once, only to build the real fixture (index 200, 1,160,782 B; one post 200, 909,909 B). No live `strike_feed.py` run was made in this session.
