# Strike-feed output (ephemeral)

`FEED_CANDIDATES_YYYY-MM-DD.tsv` files are written here by `scripts/strike_feed.py` (one per run) and are **git-ignored** (`AGENTS/OSPREY/.gitignore`) — they are working files, not the record. The record is: the STRIKES.tsv rows a human adds from them, the KB row per session that states the run's numbers (rows · NONE · FETCH_FAILED · which sources failed), and — at the end of the 4-week acceptance test (9/8 → 10/6) — one committed snapshot plus the recall verdict in KB.

Reading a file: `NONE` = no ledger row within ±1 day sharing a facility/vessel token → row it or dismiss it with a reason. `BULLETIN — read manually` = a dated-window source whose body is not machine-readable (Palaemon is client-rendered) → open the URL first, before any name query (LESSONS 8). `FETCH_FAILED` = the source was NOT read this run — an absent feed must look different from a quiet one.
