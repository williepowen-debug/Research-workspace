# FLG — TRADE SURFACE

> **LIVE — state as of 2026-08-20 (build). Position state: NO POSITION.**
> This is a live surface, not a frozen one: it carries a current-state claim and must be re-stated whenever the position state changes or a session reads it against the mirror. Position truth is **off-repo** (Will / broker direct); `FORGE/STATUS.md` is the fleet's structured mirror. **Never cite a price from this file** (root Critical Rule 4) — pull live via `FORGE/tools/market-data/fetch.py price FLG`.

## Current position

**NONE.** Verified 2026-08-20 against `FORGE/STATUS.md` (reconciled 2026-08-14, Will screenshot pair): no FLG row in either the Fidelity or Robinhood block.

## History — this desk's name has been traded before

| Date | Instrument | Size | Cost | Source |
|---|---|---|---|---|
| 2026-06-10 | FLG $13P | ×3 | $45 | `AGENTS/RED/research/POSITION_RECONCILE_2026-06-10.md:37` |
| 2026-07-10 (T-7) | FLG in the Jul-17 expiry cluster | — | — | `AGENTS/RED/CALENDAR.md:160` |

⚠️ **Outcome UNRECORDED, not zero.** Neither row was traced to a close in this build. Do not book either at $0 (`finding_record_of_an_action_is_not_the_action`). A Robinhood/Fidelity activity view settles it if it ever matters.

**Why the history matters at build:** FLG is optionable and this desk has used it, at a strike (**$13**) that is ~ATM against the 2026-08-20 live print of **$13.49**. The build is not proposing a novel instrument.

## Cohort context — read this before proposing anything

The book's bank exposure sits in **WAL, OZK, KRE, HBAN, VLY** (`FORGE/STATUS.md`, 2026-08-14 intraday marks). REGINALD's convergence matrix v2.0 (`75f0dd18b`, 2026-08-20) scores **WAL and OZK mid-pack** and **FLG first**. Three of those bank legs mark at exactly **$0.05**, which FORGE's own **D-21** caveat says must **not** be read as realizable on illiquid deep-OTM strikes.

## Standing rules

- **Trade construction is TERRY's lane.** FLG produces the evidence and the trigger; it does not size, strike or structure.
- **Trade proposals go to Will and require [Approve]** (root Critical Rule 5). No execution without it.
- Root rule 6 (puts on green days, calls on red days) and rule 7 (roll duration, don't trim size) are **TERRY-owned trade-construction rules** — cited here, applied there.
- ⚠️ **No position may be proposed on this name before the FIRST LIVE SESSION protocol is spent** — specifically before the seed is re-verified at a primary and the open construct-validity question is answered. The desk's founding score is MIRROR-grade evidence, and `EXIT_PROTOCOL.md` leg **K-1 is one quarter from firing.**

*Re-state this surface whenever position state changes. A trade surface anchored to an old date with no banner reads as current when it is not (PAT-023).*
