# FLG — TRADE SURFACE

> **LIVE — state as of 2026-10-28 (re-read against the mirror + TERRY's booking surface by FLG, owner session). Position state: NO POSITION in the mirror · re-arm readings A and B FIRED 10/23 (below).**
> This is a live surface, not a frozen one: it carries a current-state claim and must be re-stated whenever the position state changes or a session reads it against the mirror. Position truth is **off-repo** (Will / broker direct); `FORGE/STATUS.md` is the fleet's structured mirror. **Never cite a price from this file** (root rule #4); pull live via `FORGE/tools/market-data/fetch.py price FLG`.

## Current position

**NONE in the mirror.** Re-checked 2026-10-28: `FORGE/STATUS.md` carries no FLG row; TERRY's STATUS (read 10/28) books a **Will-direct OPEN order, Mar-19-2027 $10 puts ×4 at $0.52 limit — not filled/booked**. Fill state UNKNOWN until Will's next capture; FLG does not infer it (PROME packet 10/23, filed). Prior check 2026-10-22 against `FORGE/STATUS.md` (ANVIL reconcile of Will's 10/22 11:01 ET Fidelity capture, Fidelity Traditional IRA only): no FLG row. ⚠️ The Robinhood block was NOT provided on 10/22; its last vintage is 9/29, so absence there is unverified for 23 days. *(Prior: verified 2026-08-20 against the 8/14 reconcile, both accounts — no FLG row.)*

## Re-arm condition — when FLG hands TERRY a construction input

FLG proposes no trade; construction is TERRY's and the decision is Will's under root rule #5. Under Will's 10/20 11:50 ET word *"we can loosen rules for trade ideas"* (TERRY `RISK_RULES.md`, October 20 operator amendment — IDEAS), FLG sends TERRY a packet **labelled NOT-FIRED** whenever ANY of these reads true, citing the reading in figures:

| # | Reading | Source / when | Direction it supports | State 10/28 |
|---|---|---|---|---|
| A | Any surprise route R1–R5 fires | `reports/2026-10-22_preprint-surprise-threshold-NOTE.md` · release 10/23 | as recorded (miss/cut = downside) | ✅ **FIRED 10/23** — R1, R3, R4, R5 (R2 not, by $1M); NOT-FIRED packet sent to TERRY `936d8c0fd` |
| B | Frame item A thesis-confirming: Q3 provision > $62M, or FY2026 provision guide raised above $140M, attributed to NYC multi-family | `reports/2026-10-21_Q3-2026_PREPRINT_FRAME.md` (frozen) · release 10/23 | downside | ✅ **FIRED 10/23** — provision $76M; FY26 guide $160–170M. ⚠️ issuer attribution leads with RATES, CEO names rent regulation (KB-086/090) |
| C | FLG-02 grades HIT: ACL / non-accrual coverage at 9/30/26 < 31.04% (10-Q basis) | `workbook/PREDICTIONS.tsv` · 10-Q ~11/6–11/9 | downside | PENDING — release PREVIEW 30.85% (derived) points to HIT |
| D | K-1 fires (multi-family HFI rising 2 filed quarters AND non-accrual rate falling) | `workbook/EXIT_PROTOCOL.md` | **AGAINST** any downside idea — FLG tells TERRY to stand it down | NOT FIRED — MF HFI fell −$983M in Q3 |

Price context is REGINALD's (`VX-REG-6.03` ladder, RED since 10/7); FLG never fires on price alone.

**Known candidate:** TERRY's 10/12 shortlist rank 1 is **"FLG downside, WATCH; not ready"**: a long-dated put spread spanning the 2027 maturity wall and the 2028-Q2 DSCR review, held back by vendor-chain liquidity (`AGENTS/TERRY/research/2026-10-12_new-trade-shortlist.md`). Readings A–D above are the inputs that would move it; FLG does not grade the structure. **10/23 update (TERRY STATUS):** idea menu, NOT a card — `CAND-FLG-JUL27-10P` CONDITIONAL, NO CARD (also Mar-27 10P, Jan-28 12P); no entry on the 10/23 gap-down red day (root rule #6); `AGENTS/TERRY/research/2026-10-23_FLG-Q3-perspective.md`.

## History — this desk's name has been traded before

| Date | Instrument | Size | Cost | Source |
|---|---|---|---|---|
| 2026-06-10 | FLG $13P | ×3 | $45 | `AGENTS/RED/research/POSITION_RECONCILE_2026-06-10.md:37` |
| 2026-07-10 (T-7) | FLG in the Jul-17 expiry cluster | — | — | `git show 09476a9cd:AGENTS/RED/CALENDAR.md` line 90 (row removed from RED's calendar 9/14, `d0e2b24c2`) |

⚠️ **Outcome UNRECORDED, not zero.** Neither row was traced to a close. Do not book either at $0 (`finding_record_of_an_action_is_not_the_action`). A Robinhood/Fidelity activity view settles it if it ever matters.

## Cohort context

The book's bank exposure and its marks live in `FORGE/STATUS.md` (read it there; this file restates nothing that decays). REGINALD's convergence matrix ranks FLG first on level (`AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md`).

## Standing rules

- **Trade construction is TERRY's lane.** FLG produces the evidence and the reading; it does not size, strike or structure.
- **Trade proposals go to Will and require [Approve]** (root rule #5). No execution without it.
- Root rule #6 (puts on green days, calls on red days) and root rule #7 (roll duration, don't trim size) are **TERRY-owned trade-construction rules**, cited here, applied there.
- K-1 status: on multi-family HFI, 0 of 2 quarters satisfied (`EXIT_PROTOCOL.md` log 2026-10-21).

*Re-state this surface whenever position state changes. A trade surface anchored to an old date with no banner reads as current when it is not (PAT-023).*
