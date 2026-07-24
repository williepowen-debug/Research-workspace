---
name: finding_pandas_column_method_collision
description: "pandas columns named like DataFrame methods (skew, var, std, count, min, max, mean, rank, diff, size) silently return the METHOD via dot-access — bracket-index every financial-series column"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: bb7157d5-ce41-4617-93d6-e7c269a75229
  modified: 2026-07-24T00:37:10.741Z
---

`df.skew` returns the **bound `.skew()` method**, not the column named `skew`. Dot-access on a pandas DataFrame/Series resolves methods before columns, so it fails *silently at the attribute level* and only blows up downstream — VIOLET's cheap-tail build died on `float() argument must be a string or a real number, not 'method'`, three frames away from the actual mistake.

**Why:** the collision surface is large and financial-series columns land right in it — `skew`, `var`, `std`, `count`, `min`, `max`, `mean`, `sum`, `rank`, `diff`, `shift`, `size`, `pop`, `all`, `any`. A vol/credit/rates workbook column is *more* likely to collide than a random name, not less. The same file had `df.vix` and `df.vvix` working fine right next to `df.skew` failing — which makes the bug read as data-specific rather than syntax-specific and sends you hunting the wrong thing.

**How to apply:** in any pandas script over a market series, use **bracket indexing** (`df["skew"]`, `last["skew"]`, `sub["skew"].max()`) as the default for column access — do not mix dot-access in "just for the safe-looking ones," because the next column added may collide. When a numeric op throws `not 'method'` / `not 'function'`, suspect a column-vs-method collision *before* suspecting the data. Related: [[finding_crlf_textmode_tsv_flip]], [[finding_printf_format_tsv_append_corruption]] — same family of silent tooling traps that corrupt or crash a market-data pipeline without an obvious error at the point of the mistake.
