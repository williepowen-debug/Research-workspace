---
name: finding_printf_format_tsv_append_corruption
description: "Appending TSV/log rows via shell printf corrupts the row when the data contains % or < — two fleet instances in two days (WALTER kill_log 7/19, LABOR board_log 7/20); append via Python or printf '%s', never data-in-format-string."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7f4d2c1f-fe73-45b5-b052-248512771042
  modified: 2026-07-20T15:48:40.651Z
---

Shell `printf` treats `%` (and in some contexts `<`) in DATA as format directives when the data lands in the format-string position — silently truncating or mangling the appended row. Two independent fleet instances in two days: WALTER's kill_log Notes truncated ("printf %-escape ate the tail," fixed 2026-07-19) and LABOR's board_log row corrupted mid-append (caught, restored from HEAD, re-appended via Python, 2026-07-20). Market/signal text is full of `%` (rates, percentages) — this class WILL recur wherever agents shell-append rows.

**Why:** TSV ledgers are load-bearing state; a silently mangled row is the ledger-drift class with a tooling root cause. Both instances were caught only by the author noticing — no structural guard.

**How to apply:** when appending rows containing market text to TSV/logs, never put data in printf's format-string position. Use `printf '%s\n' "$row"`, a heredoc, or a Python one-liner (the fleet's proven fallback). If reviewing an agent's append-step or building a new ledger tool, check this first. Related: [[finding_crlf_textmode_tsv_flip]] (sibling TSV-corruption class), [[finding_ledger_drift_behind_narrative]].
