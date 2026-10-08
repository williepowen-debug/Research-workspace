# WQ-252 sitting prep — what is still open after WQ-386, and the options for it (DOCKET L472 → Will's sitting L471)

**Written:** 2026-10-08 08:19 EDT (DAEDALUS, PROME `prome-fc` wake, Tier 1 WQ-389). **Replaces nothing:** the 10/1 memo (`PROME/inbox/processed/2026-10-01_from-DAEDALUS_WQ-252-crack-contract-month-options-memo.md`) stays the record of the full option set; this note narrows it to what WQ-386 left open and carries three corrections to it.
**Owner of the choice:** Will. HENRY is conflicted on every option (each moves its own falsifier line toward or away from firing). DAEDALUS is the gate-basis owner and prepares options only. **$0 · no threshold moved · no trade view · the held VLO share's rule is NOT re-opened.**

## The whole story first

On 10/7 Will settled the part of this question that touches money: for the ONE held VLO share (bought 9/18 at $412), the diesel-margin exit is read on the **November** contracts through the 10/14 settlement and on **December** from 10/15 through 11/19, with no roll window and no adjustment (WQ-386, `PROME/proposals/2026-10-07_VLO-december-management-RULED.md`; TERRY recorded it at `76c75516b`). **What is still open is HENRY's own falsifier on the airline-fuel thesis (HEN-46 F1, "crack below $95 = stand down, below $90.16 = thesis dead")**, which loses its measurement basis after 10/14, and an optional successor to the spent HEN-F3 check. My design read: **put HEN-46 F1 on exactly the held share's letter**, so one diesel-margin reading on one contract month grades both lines on the same day. Its cost is stated plainly below: on today's downward-sloping curve it reads about $5 lower than November, so it fires HENRY's falsifier more easily than any November-keyed option.

## What is open, what is not

| Line | State after WQ-386 | Open at L471? |
|---|---|---|
| GATE-TERRY-VLO-HELD-01 leg A (the held share) | **RULED** — Nov through 10/14 settle; Dec matched 10/15–11/19; strict < $95 notice / < $90.16 SELL rec; review by 11/18 | **No** (do not re-open) |
| **HEN-46 F1** (HENRY's falsifier; thesis resolves on AAL/LUV Q3 prints, late October, row backstop 10/31) | November basis through 10/14 only; "basis after 10/14 = the sitting's" (`AGENTS/HENRY/STATUS.md:141`) | **Yes — the main question** |
| **HEN-F3 successor** (optional, WQ-344 rider: new id, window = 10/31 ban expiry + 10 sessions ≈ 11/02–11/13, base rate stated) | Not registered; only this sitting may register it | **Yes — optional** |
| GATE-TERRY-VLO-SCALE | Terminal since 9/25 | No |

## Today's levels and the step (single vendor, NOT CME settlements ⚠️)

Vendor daily `Close` on named contracts (yfinance `HO<m>.NYM` ×42 − `CL<m>.NYM`), pulled 2026-10-08 08:16 EDT. The 10/8 row is an **overnight/pre-market intraday read (08:06 ET bars), not a close.**

| Session | Nov | Dec | Jan | Nov−Dec step |
|---|---:|---:|---:|---:|
| 10/01 | 102.09 | 97.77 | 95.36 | 4.33 |
| 10/02 | 97.94 | **93.58** | 91.37 | 4.36 |
| 10/05 | 101.47 | 96.60 | 93.69 | 4.86 |
| 10/06 | 102.47 | 97.34 | 94.20 | 5.13 |
| 10/07 | 105.87 | 100.47 | 97.12 | 5.41 |
| 10/08 (08:06 ET, intraday) | 109.48 | 103.62 | 100.12 | 5.85 |

So what: no line is in play on either month this morning (Dec is $8.62 above $95). But the Nov−Dec step has **widened every session this month, $4.33 → $5.41 at the 10/7 close**, against a September median of $4.72 (range −$0.03 to $7.24; HENRY replicated this on the same vendor, 10/2 — a replication of the arithmetic, not a second source).

**Base rates, 9/1–10/7, 26 vendor closes:** Dec < $95 on **7 of 26** sessions (9/3, 9/4, 9/8, 9/24, 9/28, 9/29, 10/2); Nov < $95 on 1 of 26 (9/25, at $94.998). Neither month closed below $90.16 on any of the 26. Nov and Dec sat on opposite sides of $95 on 8 of 26. In 15 of the 17 rolling 10-session windows, Dec closed below $95 at least once; in 0 of 17 below $90.16. These are counts on one vendor's history, not forecasts.

## The options for HEN-46 F1 after 10/14

| # | Option | What it costs | Which way it cuts on HEN-46 |
|---|---|---|---|
| **F-A** | **Same letter as the held share:** Dec matched 10/15 → resolution (backstop 10/31 is well inside Dec's window, which runs to 11/19), same source order (CME settle → vendor row within $0.15 → 14:28–14:30 ET proxy labelled ESTIMATE), strict thresholds, missing = UNKNOWN | One step at 10/15 (October so far $4.33–$5.41). The month switch alone can stand HENRY down — the same consequence Will accepted for the share. | Against the thesis: easier to fire stand-down (Dec < $95 on 7/26 recent sessions vs Nov 1/26) |
| F-A′ | Expiry schedule for F1 only: Nov through 10/19, Dec from 10/20 | Three sessions (10/15, 10/16, 10/19) on which **F1 and the held share read different months on the same day** — the cross-desk split A′ was meant to prevent. Same step, three sessions later. | Against the thesis, three sessions later |
| F-B | Dec + k, k = Nov−Dec frozen on 10/14 | The graded number is a construction, not a tradable price, and differs from the share's graded number by k (~$5 at today's step) every session — two "crack" figures for one evening | For the thesis by k: keeps F1 in November terms |
| F-0 | No basis: F1 is suspended 10/15 → resolution; HEN-46 grades on its CONFIRM/DENY at the Q3 prints with F2/F4/F5 still live | The crack-collapse check is blind for roughly 6–12 sessions before the prints | Neutral on the line; removes one falsifier for the run-in |

Not re-offered: **C** (a persistence test or a moved line — the second is HENRY's threshold and the share's letter rejected both) and **D** (the roll-window rule as written has no instruction for the days the outgoing crude contract has stopped trading — see correction 2).

**DAEDALUS design read (labelled; the choice is Will's): F-A.** One observation, one contract month, one number grades both the share's exit and HENRY's falsifier on the same session; nothing has to be reconciled between desks, and the switch consequence is one Will has already accepted once. If Will's view is that HENRY's lines were drawn for November specifically, F-B is the honest alternative, at the price of a constructed number. F-0 is the cheapest to run and the least informative.

## The optional HEN-F3 successor

Under F-A, a successor window of ~11/02–11/13 lies **entirely inside December's window (to 11/19)**, so no contract switch happens during it. Base rate to state on registration: Dec closed below $95 on 7 of 26 recent sessions, and 15 of 17 recent 10-session windows held at least one such close (single vendor, 9/1–10/7). Registering it is Will's call (WQ-344 rider); a window this likely to fire on curve shape alone is a weak falsifier unless its letter says what a fire means for HEN-46.

## Corrections to my 10/1 memo (carried, each with its source)

1. **A′ kept November for three extra sessions, not four** (10/15, 10/16, 10/19). Source: the PROME review helpers recorded in the WQ-386 RULED record. My "4 sessions" was wrong.
2. **D's "up to two sessions" delay was not established by its own letter.** Its ±2-session window around a 10/20 switch includes 10/21–10/22, when CLX26 no longer trades, so a fresh November reading cannot exist; with missing data treated as UNKNOWN, D needs a cutoff and a missing-contract rule it does not have (`PROME/reviews/2026-10-07_VLO/MANAGEMENT_PASS.md` line 45).
3. **The $90.16 calibration pair is UNVERIFIED, not "probably mismatched".** HENRY withdrew its own "matched" claim (10/2) and established only that the 7/23 crude leg was most likely September (CLU26); the heating-oil leg is UNKNOWN. ⚠️ **$90.16 is a front-of-curve level of uncertain composition; no option here validates it for December.**

## Known-unknowns that could change the choice

- ⚠️ **No figure here is a CME settlement** (CME is blocked from our tools). The vendor row matched the settlement window to ≤ $0.10 on 3 sessions (HENRY 9/24) — a small sample.
- ⚠️ The vendor re-stitches continuous history (HENRY 9/30); named-contract rows are what this note uses, and the held-share letter rejects continuous tickers outright.
- AAL/LUV print dates are carried from HENRY's calendar ("late Oct"); not re-verified here.

## Owed by others (not by this memo)

PROME puts this in front of Will at L471 and registers his ruling on HEN-46 F1 (HENRY's row) — HENRY's PREDICTIONS row needs a basis by the 10/14 settlement or F1 is suspended by default. TERRY's consequence delivery for the original memo was SEARCH-NOT-FOUND at PROME's 10/7 pass; it is superseded for the held share by WQ-386 and not needed for HEN-46.
