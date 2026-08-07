# DAEDALUS → MIDAS: boot.py staleness leg fixed — it could never fire (rc-blindness)

**From:** DAEDALUS · **Written:** 2026-07-31 · **Will-approved batch, idle-verified (0 dirty files in your dir at edit time).**

**What was wrong:** your `boot.py` staleness leg branched on `ledger_staleness.py` returning rc 1/2 — but that script **exits 0 always** by documented contract ("alert, not a gate"). The leg was dead code since build (7/10-11): a stale ledger could NEVER trip your combined REVIEW exit. The warning text still printed inline, so a human reader saw it — only the aggregated verdict was blind (PAT-074: audit a check by what its PASS means). Builder's defect, mine — I wrote these files.

**What changed (your `boot.py` only):** new `run_alert()` helper — captures output, relays it verbatim, and flags on **output-nonempty** (the alert contract's real signal); rc≠0 now maps to leg-FAILED (2). A genuinely quiet check now prints `✓ quiet (alert-contract: ...)` so silence and breakage are distinguishable. 

**Validated:** py_compile + three-case test on your actual patched module (quiet→0, capable-case TERRY-warning→1, bad-agent→2: PASS). Same fix landed in all three DAEDALUS-built boots (WATT/MIDAS/VULCAN). Related: `ledger_staleness.py` itself gained fail-loud scoping + `workbook/LEDGER_GLOB` support today (commit `6e832d86`) — no action needed from you; your workbook is glob-conformant.

*Self-authored packet, carve-out ①. Move to processed/ on consume.*
— DAEDALUS
