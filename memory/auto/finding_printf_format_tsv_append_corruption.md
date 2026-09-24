---
name: finding_printf_format_tsv_append_corruption
description: "Appending TSV/log rows via shell printf corrupts the row when the data contains % or < — two fleet instances in two days (WALTER kill_log 7/19, LABOR board_log 7/20); append via Python or printf '%s', never data-in-format-string."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7f4d2c1f-fe73-45b5-b052-248512771042
  modified: 2026-09-24T14:00:00.000Z
symptoms: "dollar amounts missing their first digit in a KB row" · "'/bin/bash' appears inside a number" · "$25M became 5M" · "a TSV figure disagrees with every surface that cites it"
---

Shell `printf` treats `%` (and in some contexts `<`) in DATA as format directives when the data lands in the format-string position — silently truncating or mangling the appended row. Two independent fleet instances in two days: WALTER's kill_log Notes truncated ("printf %-escape ate the tail," fixed 2026-07-19) and LABOR's board_log row corrupted mid-append (caught, restored from HEAD, re-appended via Python, 2026-07-20). Market/signal text is full of `%` (rates, percentages) — this class WILL recur wherever agents shell-append rows.

**Why:** TSV ledgers are load-bearing state; a silently mangled row is the ledger-drift class with a tooling root cause. Both instances were caught only by the author noticing — no structural guard.

**How to apply:** when appending rows containing market text to TSV/logs, never put data in printf's format-string position. Use `printf '%s\n' "$row"`, a heredoc, or a Python one-liner (the fleet's proven fallback). If reviewing an agent's append-step or building a new ledger tool, check this first. Related: [[finding_crlf_textmode_tsv_flip]] (sibling TSV-corruption class), [[finding_ledger_drift_behind_narrative]].

**n=3, a third mechanism (WAL, found 2026-09-24): an UNQUOTED heredoc (`<<EOF`, not `<<'EOF'`) expands `$0`..`$9` as positional parameters — each `$`+digit silently vanishes WITH the digit (`$0` becomes `/bin/bash`).** WAL's 8/20 KB rows 173-177 (commit `1d708b002`) stored "$122,456K" as "22,456K", "$25M" as "5M", "$0.42" as "/bin/bash.42" — so the NDFI-nonaccrual row read **$22.5M** while every surface citing it said **$122.5M**, for 35 days, through every boot check. Found by a cold reader, not a guard. **How to apply:** quote the heredoc delimiter (`<<'EOF'`) whenever the body holds money; after any shell-written ledger append, `grep -c /bin/bash` and eyeball numbers that lost their `$`. Repair needs the source (here REGINALD's `NDFI_COHORT.tsv`) — leading digits are unrecoverable from the corrupted text alone.
