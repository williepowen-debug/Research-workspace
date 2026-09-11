# Strike-feed output — two files per run, one ephemeral and one committed

**`FEED_CANDIDATES_YYYY-MM-DD.tsv`** — every kept candidate. **Git-ignored** (`AGENTS/OSPREY/.gitignore`): a working file, not the record.

**`MATCHES_YYYY-MM-DD.tsv`** — **COMMITTED** (added 2026-09-10). One row per candidate the diff absorbed into an existing `strike_id`, with the tokens that carried the match and the matched row's facility. *Why it exists:* `FEED_CANDIDATES` is ignored, so before this file the **precision** side of the feed was unfalsifiable after the run — a false `<strike_id>` produces no `NONE` row, no KB mention and no artifact, so a recall-only acceptance test cannot see it (DAEDALUS review 2026-09-10, finding (b)).

## Reading a file

| Value in `ledger_match` | What it means |
|---|---|
| `NONE` | No ledger row within ±1 day sharing a **proper-noun, df<4** facility/vessel token → row it, or dismiss it with a reason in the note column. |
| `<strike_id>` | **A CLAIM, not a fact.** The `note` column names the tokens that carried the match and the ledger row's facility — **confirm that facility is the one in the headline before dismissing the row.** Post-patch residual false-absorption is 2/99 (2.0%) on the hold-one-out, not 0. |
| `BULLETIN — read manually` | A dated-window source whose body is not machine-readable (Palaemon is client-rendered) → open the URL first, before any name query (LESSONS 8). |
| `UNDATED` | No parseable publication date — never matches; safe direction. |

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
