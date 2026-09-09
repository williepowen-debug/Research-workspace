# BOJ pricing — source and ingestion contract

**Effective September 8 ET / September 9 JST, 2026.** `BOJ_OIS.tsv` is FROZEN historical material from the impeached centralbank.watch/3m-TONA feed. Do not cite its rows as current. The unchanged file preserves earlier grades and source failures.

`scripts/boj_ois.py` remains in the existing boot sequence, but now writes **`BOJ_MEETING_OIS.tsv`**, a separate schema for [Totan's indicative meeting-to-meeting OIS medians](https://www.totan.com/archives/15647). It does not splice the instruments or carry forward the former cumulative probability fields.

The table reports incremental policy-change equivalents under 25bp steps and cumulative expected hike counts. A count above one is valid. An incremental equivalent can be read as a binary hike probability only under the no-change/one-step assumption; the script does not generalize that interpretation to later meetings. These are indications, not exchange trades, and there is no last-traded timestamp. Reference terms are quoted from the table, not inferred from calendar T+1.

## Review and ingestion

1. Save the source page and table image under a dated research package. Inspect the image, including its timestamp, all columns and reference terms. Use a white rendering for transparent PNGs if needed; preserve the original bytes.
2. Add a dated JSON in `boj_ois_reviews/`, using the existing September 9 review as the schema. Transcribe the table, record its row count, source URL and SHA256, and preserve the evidence path. Record the nearest BOJ decision date from the official schedule as `valid_until` (conservatively expires at 00:00 JST that day). The publisher's timestamp has no printed timezone; the JST assumption must travel.
3. Run `.venv/bin/python3 AGENTS/SAM/scripts/boj_ois.py --no-write`. It fetches the live source, verifies the policy-only/25bp methodology, table link and exact image hash, then validates reference terms, source age, expiry and arithmetic. A changed image, future or >4-day-old quote, inconsistent transcription or same-vintage revision must be investigated; never update a hash without re-reading the chart.
4. Run without `--no-write` to ingest. Repeat runs on the same vintage write nothing. Quotes retain source time, pull time, source identity, units and image hash. Never relabel an old quote with the fetch date. Use `--history` only for explicitly historical output.

**Limitation:** image decoding is not automatic. Boot can verify and ingest a reviewed chart; a newly published chart returns `UNAVAILABLE` until SAM visually reviews it. That is an unresolved automation enhancement, not permission to restore the impeached source or silently use yesterday's number. No OCR dependency was installed. The standalone cumulative chart is not combined with the table: its timestamp can lag independently.

The four-day age limit is an operational freshness maximum, not a guarantee that unchanged pricing is informative. New data during market stress can require an earlier review. Any consumer reading the TSV directly must check quote age and `valid_until`; `quality=REVIEWED_INDICATIVE` records validation at ingestion, not perpetual freshness.

Validation: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python3 -m unittest discover -s AGENTS/SAM/scripts/tests -p test_boj_ois.py -v`. Changes to methodology/layout require source re-verification and new fixtures. No prediction or position rules are embedded in this feed.
