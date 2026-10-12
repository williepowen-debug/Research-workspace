# October 9 CSV inspection — October 12, 2026

Inspected 2026-10-12T10:39:41.399658-04:00. All eight files are the final raw inputs from the tracked producer and match its committed `evidence.json`. Retain and commit each file unchanged. No deletion or overwrite.

| File | Rows | UTF-8 bytes | Result |
|---|---:|---:|---|
| CLX26.NYM_1d.csv | 9 | 1213 | Exact saved-evidence match; no duplicate timestamps or invalid OHLCV |
| CLX26.NYM_1m.csv | 6354 | 787528 | Exact saved-evidence match; no duplicate timestamps or invalid OHLCV |
| CLZ26.NYM_1d.csv | 9 | 1161 | Exact saved-evidence match; no duplicate timestamps or invalid OHLCV |
| CLZ26.NYM_1m.csv | 6052 | 747489 | Exact saved-evidence match; no duplicate timestamps or invalid OHLCV |
| HOX26.NYM_1d.csv | 9 | 1237 | Exact saved-evidence match; no duplicate timestamps or invalid OHLCV |
| HOX26.NYM_1m.csv | 5004 | 633836 | Exact saved-evidence match; no duplicate timestamps or invalid OHLCV |
| HOZ26.NYM_1d.csv | 9 | 1238 | Exact saved-evidence match; no duplicate timestamps or invalid OHLCV |
| HOZ26.NYM_1m.csv | 4378 | 554540 | Exact saved-evidence match; no duplicate timestamps or invalid OHLCV |

Total 2,728,242 bytes. Full hashes, ranges and recomputed values: [manifest](CSV_INSPECTION_2026-10-12.json).

Four minute files cover October5–9 and end at14:34EDT October9. Each contains all three14:28/14:29/14:30 historical bars, with positive window volume. Separate recomputation reproduces November/December typical-price cracks $107.15941/$101.68866 and Close cracks $107.21518/$101.75503 [EST historical single vendor; original unrounded calculations retained in evidence]. Six zero-volume rows per minute file are preserved; none is in that historical window.

Four daily files have nine rows September29–October9. The October9 rows were still forming at capture. Every leg repeats October7 volume on October8; these daily rows are rejected for a finalized settlement observation. They are useful evidence of the vendor defect, not a second price-source lineage.

The script includes the14:30-start bar and computes typical-price VWAP, with Close as a companion. WQ420 was approved prospectively October11 and specifies two opening-time bars14:28/14:29 and Close×Volume separately for each leg. This inspection preserves the prior observation; it does not authorize a historical regrade or use these CSVs as Monday data. CSV ticker labels alone do not certify maturity. Do not rerun `crack_pull.py` here: it would overwrite evidence with a later pull.
