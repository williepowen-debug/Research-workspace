# Strike-feed output — two files per run, one ephemeral and one committed

**`FEED_CANDIDATES_YYYY-MM-DD.tsv`** — every kept candidate. **Git-ignored** (`AGENTS/OSPREY/.gitignore`): a working file, not the record.

**`MATCHES_YYYY-MM-DD.tsv`** — **COMMITTED** (added 2026-09-10; ⚠ silently git-ignored 2026-09-15 → 2026-10-08 by a `.gitignore` line, re-committed 10/8). One row per candidate the diff absorbed into an existing `strike_id`, with the tokens that carried the match and the matched row's facility. *Why it exists:* `FEED_CANDIDATES` is ignored, so before this file the **precision** side of the feed was unfalsifiable after the run — a false `<strike_id>` produces no `NONE` row, no KB mention and no artifact, so a recall-only acceptance test cannot see it (DAEDALUS review 2026-09-10, finding (b)).

## Reading a file

| Value in `ledger_match` | What it means |
|---|---|
| `NONE` | No ledger row within ±1 day sharing a **proper-noun, df<4** facility/vessel token → row it, or dismiss it with a reason in the note column. |
| `<strike_id>` | **A CLAIM, not a fact.** The `note` column names the tokens that carried the match and the ledger row's facility — **confirm that facility is the one in the headline before dismissing the row.** Post-patch residual false-absorption is 2/99 (2.0%) on the hold-one-out, not 0. |
| `BULLETIN — read manually` | The latest-dated bulletin (Palaemon, client-rendered), its window END inside the run's `days_back` window, and it is the FIRST matching link on the index, with every other link dated → open the URL first, before any name query (LESSONS 8). The `note` gives the window, its basis (title or slug), its position in document order, and, if the body was under 1,500 chars, `[body not machine-readable …]`. `pub_date` = the window END. |
| `BULLETIN_STALE` | The latest-dated bulletin ends before the cutoff (`run − days_back`). At the default `days_back` (≥ 10) this means the publisher stopped or the index is cached. Below 10, the label says that an on-time bulletin can read STALE at that window. **Counted in NOT_READ** (stale ≠ quiet; L624). |
| `BULLETIN_NEWEST_UNSURE` | One or more matching links could be newer than the followed bulletin. Each one sits ABOVE it in document order (the live index is newest-first), or has no usable date (unparseable, or a FUTURE start). The `note` names each link and its reason. On a newest-first index (the live page's layout, verified on the 10/9 fixture), a date defect on the real newest (past-year typo, title year typo, format drift such as "Oct" or "Week 41") lands here. ⚠️ **Not guaranteed off that layout:** a date-typo'd real newest listed BELOW the followed link is skipped silently. Declared limit: `scripts/tests/ACCEPTANCE_L624_strike_feed_follow_newest.md` residue ⚠️21 (READ 3 ❌1, 2026-10-09). If the followed bulletin is also stale, the label says `BULLETIN_STALE` inside it. **Counted in NOT_READ** (L624 pass 2, read-2 ❌8). |
| `BULLETIN_UNDATED` | No usable bulletin date (unparseable, or only future-dated typos) — freshness unknown. **Counted in NOT_READ** (L624). |
| `UNDATED` | No parseable publication date (non-bulletin rows) — never matches; safe direction. |

| Row in `title` | What it means |
|---|---|
| `FETCH_FAILED` | The source was **NOT read** this run — an absent feed must look different from a quiet one. |
| `EMPTY_FEED` | HTTP 200, zero items. Applies to **every** source kind since 2026-09-10 (it was RSS-only, so a dead HTML scraper was indistinguishable from a quiet week). |
| `PARSER_STALE` | Fewer items than the source's `expect_min_items` — the parser, not the source, is the likely cause. |

## Diff rule (v2, 2026-09-10)

Ledger tokens are **proper-noun tokens of the raw Facility+Region cell** (capitalisation read *before* lower-casing), minus any token carried by **≥4 ledger rows** — a token four facilities share is a category, not an identity, and the df test is self-maintaining as the ledger grows where a hand-extended stoplist is not. Measured hold-one-out on this ledger: **v1 15/99 (15.2%) false absorption → v2 2/99 (2.0%)**, true-dedupe 99/99 → 89/99 (89.9%). The recall cost falls in the safe direction: a missed dedupe emits a `NONE` a human reads.

## Acceptance test 2026-09-08 → 2026-10-06 — TWO legs

1. **Recall** (original): the feed surfaces ≥1 event the manual sweep missed, or an independent backfill finds 0 misses. *(Met on run 1: Kstovo/NORSI 8/26, Novorossiysk terminal 9/8-9.)*
2. **Precision** (added 2026-09-10, DAEDALUS ACTION 4): of the N `<strike_id>` rows in the committed `MATCHES_*.tsv` files over the four weeks, **M were confirmed at the named ledger facility**. Without this leg a 15–37% false-absorption rate would run the full window and be recorded as a PASS.

## RESULT — evaluated 2026-10-08 (DOCKET L309) → `../L309_STRIKE_FEED_EVALUATION_2026-10-08.md`

**Recall: PASS on the first disjunct, and the second fails** (the 9/19 independent backfill found ARMADA LEADER 9/12 and others). **Precision: PASS on the audited runs**, 9/11 rows confirmed and 0 silent deletions; the 9/15 and 9/29 runs cannot be audited. **Retained as a LAND (refinery) instrument: 9/9 refinery rows surfaced. NOT a maritime instrument: 2/9 vessel rows surfaced.** Three things changed on 10/8:
- `MATCHES_*.tsv` is committed again. A 9/15 `.gitignore` line had silently reversed the 9/10 fix.
- militarnyi was repointed to `/en/news/feed/`. The old URL served an itemless stub on every run.
- **The `follow_newest` bulletin (current rule, L624 pass 2, 2026-10-09):** the age-filter exemption covers ONE item, the latest-dated bulletin by window END (title first, slug second). It is labelled `BULLETIN_STALE`, `BULLETIN_UNDATED` or `BULLETIN_NEWEST_UNSURE`, and all three count in NOT_READ. On a newest-first index, any link that could be newer is named and fails closed. Off that layout, see the declared limit at `scripts/tests/ACCEPTANCE_L624_strike_feed_follow_newest.md` residue ⚠️21 (READ 3 ❌1, 2026-10-09). On a body-fetch failure the source emits one `FETCH_FAILED (newest post)` row and nothing else. ⛔ **WITHHELD from operational use until READ 3 is clean** (DOCKET L624). Acceptance and tests: `scripts/tests/ACCEPTANCE_L624_strike_feed_follow_newest.md`, `scripts/tests/test_strike_feed_L624.py`. *History: the 10/8 rule ("the bulletin is never age-filtered", which fixed a within-month bulletin dated by its first day and dropped with no row) was superseded by L624 pass 1 (`04d8f06be`) and then by pass 2.*

