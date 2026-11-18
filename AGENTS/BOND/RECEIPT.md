# BOND receipt — 2026-11-18 13:1x ET, PROME prome-6e registered wake (DOCKET L1184, L1166, L1168)

Task: PROME's task letter (not typed by Will): WQ-709 domain update through the 11/17 close; grade the 11/18 20Y; apply WQ-699 A; answer three inbox questions; apply WQ-719 A to BOND's own instructions; drain the inbox. Runtime Claude Code, model `claude-opus-5-5`, Linux/WSL desktop. Tools: bash, `.venv` python (yfinance, numpy), repo scripts, SendMessage (deferred tool). Failed to connect: mtnewswire, Definite (not needed). MSRB EMMA returned 403 (blocked; stopped).

| Item | Result | Evidence |
|---|---|---|
| Boot | explicit reads; no pull (PROME's limit); docket_check rc=0; corrections rc=1 → COR-20261117-02 NO-OP; boot_recompute rc=1 (3 findings, all serviced) | boot outputs |
| 20Y `912810UZ9` | REGISTERED CLEAN on bars frozen 11/16; counter 1 → 2; health 3 held | KB-BND-584; `analysis/2026-11-18_20y/grade_912810UZ9.txt` |
| Series through 11/17 | Treasury, real, breakevens, ACM, Fed path, SOFR, ICE credit, VIX | KB-BND-585, 586 |
| F2 11/17 op | OFF-THE-RUN, routed to RED, ledger row | KB-BND-587; `registry/f2_reads.tsv` |
| WQ-699 A | rates_context.py matched basis (57/57 selftest), VX-BND-17 row; 213bp [11/12] | KB-BND-588 |
| WQ-719 A | CLOSEOUT.md C11, CLAUDE.md line 37, closeout_run.py JUDGEMENT line | this commit |
| Questions | archive 29 rows / 28 scorable; Florida muni NO; HANS T-16 logged | KB-BND-589, 590; PROME packet |
| Stale KB | 15 retired to STALE, 0 refreshed | KB.tsv Notes |
| Inbox | 10 of 10 processed; 4 board_log rows | `inbox/processed/`, `inbox/WALTER/processed/` |
| Bars | 2Y/5Y/7Y month-end frozen early | `registry/auction_bars/` |
