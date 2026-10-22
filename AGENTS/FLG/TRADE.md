# FLG — TRADE SURFACE

> **LIVE — state as of 2026-10-21 (re-stated against the mirror by FLG, catch-up wave 2). Position state: NO POSITION in the mirror.**
> This is a live surface, not a frozen one: it carries a current-state claim and must be re-stated whenever the position state changes or a session reads it against the mirror. Position truth is **off-repo** (Will / broker direct); `FORGE/STATUS.md` is the fleet's structured mirror. **Never cite a price from this file** (root Critical Rule 4) — pull live via `FORGE/tools/market-data/fetch.py price FLG`.

## Current position

**NONE in the mirror.** Re-checked 2026-10-21 against `FORGE/STATUS.md` (ANVIL reconcile 2026-10-20, Fidelity Traditional IRA only): no FLG row. ⚠️ The Robinhood block is 9/29 vintage and was NOT provided on 10/20, so absence there is unverified for 22 days. *(Prior: verified 2026-08-20 against the 8/14 reconcile, both accounts — no FLG row.)*

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
- ✅ The build-time bar on proposals (FIRST LIVE SESSION protocol) was spent 2026-08-28. ⚠️ *(Corrected 2026-10-21: this line said K-1 was "one quarter from firing"; that was the retired total-loans instrument — on multi-family HFI, 0 of 2 quarters are satisfied, `EXIT_PROTOCOL.md` log 2026-10-21.)* Any trade on this name is TERRY's construction and Will's [Approve]; this desk proposes none at the Q3 print.

*Re-state this surface whenever position state changes. A trade surface anchored to an old date with no banner reads as current when it is not (PAT-023).*
