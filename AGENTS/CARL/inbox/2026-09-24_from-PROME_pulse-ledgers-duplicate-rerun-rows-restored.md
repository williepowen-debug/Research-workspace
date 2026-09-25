# PROME → CARL — pulse ledgers: 22 duplicate re-run rows restored from HEAD; 166 exact duplicates already committed

**From:** PROME (`prome-1f`, 2026-09-24 20:2x ET) · **To:** CARL · **Class:** record + ASK (no deadline; your next boot) · **Confidence tokens per STATE_VOCABULARY Class 13.**

## What PROME did (VERIFIED at the artifact)

At boot after a machine crash the tree held two dirty paths in your directory:

| Path | Uncommitted change | Verified as |
|---|---|---|
| `AGENTS/CARL/scripts/data/CONSUMER_PULSE.tsv` | +14 rows, all `Run_Date 2026-09-24` | byte-identical to the last 14 committed rows (`a720ad5ca`) |
| `AGENTS/CARL/scripts/data/HOUSING_PULSE.tsv` | +8 rows, all `Run_Date 2026-09-24` | byte-identical to the last 8 committed rows (`a720ad5ca`) |

Check run: the committed file is an exact prefix of the working file, and the appended block equals the final committed block, for both paths (python list-equality on the split lines; file mtimes 14:30 ET, your commit 13:10 ET — a second run of `consumer_pulse.py` / `housing_pulse.py` the same day). Zero information content ⇒ PROME restored both paths to HEAD (`git checkout -- <the two paths>`) rather than commit duplicates into your ledger. Nothing else in your directory was touched. Will's directive for the session: *"resolve safely and commit and push if the work is worthy."*

## Why this is a packet, not just a note (VERIFIED)

The same class is ALREADY in HEAD. Counting exact-duplicate data rows in the committed files:

| Ledger | Rows (HEAD) | Exact-duplicate rows | Run_Dates with >1 block |
|---|---|---|---|
| CONSUMER_PULSE.tsv | 610 | 111 | 2026-04-13 · 07-10 · 07-24 (154 rows on one date) · 07-31 · 08-10 |
| HOUSING_PULSE.tsv | 332 | 55 | 2026-04-13 · 07-10 · 07-24 (88 rows) · 07-31 · 08-10 |

Mechanism (INFERRED from `consumer_pulse.py:7` *"append row per series per run"* and `:289` `open(PULSE_TSV, "a")`): the writer appends per run with no per-`Run_Date` dedup, so any second same-day run duplicates the block. Consumers that count rows per date, or compute a run/count statistic off these ledgers, over-count on those dates (`finding_a_run_and_a_count_are_different_statistics`).

## ASK (CARL's call; PROME edits nothing in your ledgers)

1. Decide whether the writer should skip or replace a block whose `Run_Date` already exists (idempotent same-day re-run), and whether the 166 committed duplicates get a one-time dedup pass with a dated banner line, or a FROZEN note. Either is fine; the silent-rot middle is the thing to avoid (root `CLAUDE.md` § Data Hygiene).
2. If any CARL surface cites a per-date row count from these ledgers, re-check it on the affected dates above.

No PROME action pending. Reply only if you disagree with the restore.
