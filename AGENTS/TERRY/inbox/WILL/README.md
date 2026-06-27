# Will's trading-data drop zone

**Reserved for Will.** Drop trading data here and tell me — "Terry, new drop" (or just point me at it). This is the standing intake for the day-trading review loop and for position truth.

## What to drop (best → acceptable)
1. **Broker history / positions CSV export** — *best.* Captures the two things a feed hides: **assignment/exercise outcomes** and **roll strikes/expiries**. Without these, realized P&L is a *range*, not a number.
2. **Activity-feed export or paste** — works; I mark assignment-gated and roll-book figures `UNKNOWN`.
3. **Screenshots** — OK as a fallback; least precise (no clean parse).

## Tell me three things with the drop
- **Broker** (Robinhood, etc.)
- **Window** the data covers (dates)
- **Market open or closed** when I pull marks

## What I do with it
- **Trading results →** run the day-trading review loop (`../../daytrading/`): reconstruct realized P&L by instrument thread, mark open positions live, score against the 5 rules, append a narrative entry to `JOURNAL.md` + a metrics row to `LEDGER.tsv`.
- **Open-position truth →** existing-position triage (`../../POSITION_INTAKE.md`).
- I'll move a drop to `processed/` (local) once I've consumed it, or you can delete it.

## Privacy — important
**Raw drops here are gitignored: they stay on this machine and are NEVER pushed to GitHub.** Only my processed analysis (JOURNAL/LEDGER, postmortems) gets committed — never your raw broker/account data. So drop freely; account numbers, balances, and full fills never leave the desk.
