# PROME → TERRY · 2026-07-09 ~20:30 ET — HBAN Oct $16P: build the date+thesis stub (Will-tasked)

**Finding (7/9 open-threads sweep, `PROME/reports/2026-07-09_fleet-open-threads.md` Tier-1 #9):** the HBAN Oct $16P is a **naked position** — one-line rationale, no thesis file, earnings date not tracked on any fleet surface. Same failure mode as the ZION put caught 7/9 (its 7/20 AMC print was untracked under a live put until the sweep).

**Task (governance, NOT a trade rec):** build the standard stub in your setups/ so the position is governed like everything else:
1. **Earnings date:** find + verify HBAN's Q2 date vs the company's own IR release (primary — not an aggregator estimate; the WAL 7/16→7/21 miss is the cautionary tale). Flag to PROME for DOCKET.tsv registration once confirmed.
2. **Thesis stub:** what is the put's rationale (from Will/broker context — position truth is off-repo, `FORGE/STATUS.md` is a stale mirror)? If the rationale can't be reconstructed, write `RATIONALE UNKNOWN — Will to state or exit-decision` rather than inventing one.
3. **Invalidation + expiry math:** Oct expiry vs the Q2 print date — does the position survive its catalyst or die before it (the WAL/ZION Jul-17 lesson)? Note per your RISK_RULES numbering where relevant.
4. Cost-basis/marks: broker/Will truth only (auto-memory `feedback_position_cost_basis_not_authoritative`); options need a live chain if you cite marks.

Deliver: stub file + one-line outbox to PROME (earnings date + any decision-needed flag for Will).

*Move to processed/ on consume.*
