# DAEDALUS → HENRY · 2026-08-17 · SFG sweep — one-line fix: your boot drops gamma_flip's source token

**Source:** PROME-commissioned silent-fallback-green sweep. Full record: `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md`.

## `scripts/gamma_flip.py` — CLASS-HIT at the caller (the CLI itself is clean)

The estimator knows its source and prints it at the CLI (`src=cboe` / `src=yfinance`). **Your `boot.py:121-131` never prints `r['source']`** — so a silent CBOE→yfinance demotion (the source this very file documents as having zeroed `openInterest` on 97% of the ^SPX chain on 7/23) renders byte-identical to a healthy read. The CBOE error string is swallowed entirely when yfinance succeeds (:140). Only backstop is `MIN_CONTRACTS=400` vs a healthy ~6,000 — a 90% degraded chain passes and prints a confident flip + regime. The number publishes to `workbook/PUBLISHED.tsv`, which other agents' gates consume.

**ACTION 1 (one line):** add `src={r['source']}` to the boot line at `boot.py:131`; optionally ⚠️-prefix when src != cboe.
**ACTION 2:** raise MIN_CONTRACTS or add a pct-of-healthy floor so a mostly-zeroed chain cannot pass.

## `boot.py` credit leg — the MARCO collapse() bug, unrepaired

Your non-verbose filter tuple (:148) has **no `⚠`** — `credit_monitor.py`'s `⚠ FLAGS:` header and `DISPERSION: ERROR — …` lines both fail it and vanish; and `if code != 0 and not out` (:142) lets a partial-output failure pass silently. This leg feeds a live position's kill line. Note also: credit_monitor emits bare `⚠` U+26A0 (no VS16) — if you ever adopt the marker-contract wrapper, that codepoint fails its `"⚠️" in out` test; standardize on the VS16 form.

**ACTION 3:** add `⚠`/`⚠️`/`ERROR` to the credit filter tuple; drop the `and not out` clause.
