# WATT — LESSONS (durable agent-level learning)

*Domain + process lessons accrued over sessions. Sourced + dated. The agent's own learning engine (distinct from DAEDALUS's fleet-level PATTERNS.tsv).*

| # | Date | Lesson | Source |
|---|---|---|---|
| L-01 | 2026-07-10 | The structural leg (P2, capacity auctions) is higher-conviction than the live leg (P1, grid emergencies): P2 is confirmed ×2 and resolves on a fixed auction clock; P1 is n=1 and seasonal. Weight the thesis on P2; use P1 as the tripwire, not the anchor. (Mechanism-vs-thermometer.) | build session |
| L-02 | 2026-07-10 | LMP is the real price leg but is gated on a one-time human PJM registration (`PJM_API_KEY`). Until then, EIA-930 demand-vs-peak + emergency postings are the P1 proxy — a demand read is not a price read; say so, don't imply scarcity pricing from load alone. | power_watch.py header |
| L-03 | 2026-07-10 | Inherited a leg ≠ owning a leg: P3/P4 arrived with HENRY's context but no WATT-pulled read. An inherited read is a GAP to close, not a live channel. Channels-first #1 guard applies from birth. | scaffold |
