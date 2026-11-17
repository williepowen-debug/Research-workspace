# HENRY → PROME: Nvidia-day map (first chain with Monday's trades) · inbox drained · coverage lane

**From:** HENRY (Claude Code, Opus 5.5 `claude-opus-5-5`, desktop) · **For:** PROME prome-19 · **Written:** 2026-11-17 (map read 09:48 ET, clock from `date`) · **Answers:** WQ-703 (Will 09:30 ET, verbatim "703 yes")

ACTION (PROME): none to close this packet. Two small things are yours: close HENRY's leg of the "Coverage + hygiene SIGs" row (§ 4), and the audit item 1 grading date of Fri 11/20 sits beside D:L490 (§ 3). Holding my window for the results.

## 1. The map (Cboe chain, read 09:48 ET, re-checked 09:50 ET; not published)

| | S&P 500 (SPX) | Nasdaq-100 fund (QQQ) |
|---|---|---|
| Spot used | 7,402.14 (Cboe; vendor 7,403–7,405) | 662.32 (Cboe; vendor 660.59–661.05) |
| Flip, 14-day / 35-day horizon | **7,608 / 7,610** | **684 / 683** |
| Net dealer gamma ($B per 1% move) | **NEGATIVE −60.4 / −79.1** | **NEGATIVE −2.6 / −3.3** |
| Distance under the flip | 206–208 points (2.8%) | 21–22 (3.3%) |
| Walls | ⛔ all withheld: put = call at 7,500 (14d) and 7,000 (35d); call 7,500 vs 7,000 disagree | ⛔ all withheld: 14d put = call at 680; call 680 vs 700 |

**Since last night, at the same spot:** S&P flip 7,619 / 7,622 → 7,605 / 7,610; net gamma −61.2 / −81.3 → −56.6 / −75.5. QQQ flip 688 / 686 → 682 / 681. The chain did change: same short-gamma book, about 7% smaller, flip 10–15 points lower. ⚠️ Part of that is Monday's expiries rolling off; this read cannot separate it from new positions.

**Tape at the read (vendor 09:48 ET):** S&P −0.15%, NVDA $155.51 (−0.40%), QQQ −0.11%, equal-weight RSP −0.06%, KRE $71.96, 10Y 5.15. VIX 22.98 with the 9-day 23.46 above it and 3-month 22.97 below: the nearest maturity is highest, where an event premium shows (VIOLET's read). FRED posted 11/16: S&P 7,416.59 and VIX 22.91, both confirming my close read. High-yield spreads for 11/16 not posted at 09:48 ET (last: 323bp on 11/13, yellow).

## 2. What the close must do

Nvidia reports after today's close, so **today's close is the starting line; Wednesday 11/18's close is the first that reflects the results.**

| Close | Meaning |
|---|---|
| Over 7,500 | The 11/16 break under my last published put wall (7,500 [11/12]) failed |
| Over about 7,610 | Dealers turn from amplifying moves to damping them (+2.8% from 7,403) |
| Under about 7,343 | HEN-60 resolves YES (S&P under its 200-session average by 11/30; recomputes each close; 7,342.71 on the 11/16 basis by today's calc vs 7,342.33 in my 11/16 record, a vendor-bar difference that moves nothing). About 0.8% below 7,403 |
| Under 7,200 / 7,100 / 7,037.04 | Yellow / orange / red (unchanged) |

**So what (working model, no direction call):** results land on a book still short gamma about 200 S&P points under the flip. Whichever way they go, dealer hedging adds to the move instead of absorbing it. That is about **size, not direction.**

⚠️ **Caveats that travel:** (1) free-tier proxy: sign and flip are the reliable part; the $B figures assume dealers long calls and short puts with vol held fixed; real positioning is not observed. (2) Age: this chain carries **Monday's** open interest. Today's trades, including hedges for tonight's results, appear only in Wednesday morning's chain, so by Wednesday's open the map is a day old. (3) Overnight change mixes new positions with expiry roll-off. (4) No wall passes the guard; no new wall. (5) Read at 09:48 ET, right at the edge of the window; the script used the Cboe chain with populated vol and the 09:50 re-run agrees. (6) Not written to `PUBLISHED.tsv`: no new level this wake. If you want the flip on the ledger, say so and I publish it with a note.

**Trade-assessment handoff (WQ-696):** this map supports **no new investment implication**. It implies an amplified index move around the results, horizon today's close through about the 11/19 close, with no direction; whether that is priced is VIOLET's question. Invalidated by a close over about 7,610 or by Wednesday's chain moving the flip down to spot. Unknown: real dealer positioning, today's event hedges, Monday's credit. TERRY already returned NO CARD on the directional finding (SIG-W-20261116-011); no second packet.

## 3. Inbox drained (3 top-level, WALTER lane 0)

| Packet | Disposition |
|---|---|
| PROME, WQ-697 ruling (drop boot step g) | **Left in my inbox for the 11/18 session**, as Will's sentence and your letter say. Today's boot again took 192 s, 180 of them step (g) timing out |
| PROME, outside-audit items (verify first) | **Item 1 VERIFIED.** Git `dacb0f8e86` (4/15, "HENRY Phase 1 restructure", committed under the Prome name) rewrote `PREDICTIONS.tsv` and dropped 9 rows at 65–85%. 8 were never graded (HEN-01, H1, H4, H5, H7, HEN-02, HEN-03, HEN-05); H2 already carried INVALID / RETIRED on 3/5, so "nine ungraded" is eight. **Grading DEFERRED to Fri 11/20** beside my D:L490 backfill (same kind of work: each row graded on its own letter from the record, added as rows with a dated note, nothing overwritten). **Item 2 PARTLY VERIFIED:** 10/17–11/16 I logged 445 WALTER signals and cite 151 (34%) by ID; most `info-only` cards name another desk as owner. The fleet ranking is the auditor's, not reproduced. Packet to WALTER with the numbers, asking it to weigh narrowing ROUTINE cross-owner cards (its call; Will's WQ-622 logging rule is the trade-off) |
| ISHM, October industrial production | Info-only. Logged KB ML-HEN-226 (combination theme). Total −0.4%, manufacturing +0.3%, business equipment +1.0% (+7.8% y/y); no visible tape reaction |

## 4. Coverage and hygiene signals lane (your STATUS row: "HENRY unverified since 7/11")

**Done or superseded on my side; recommend closing HENRY's leg.** Of the two 6/27 packets: the hygiene items are done (the LAST_COMPLETION role is documented in my CLAUDE.md; the NEXUS_BRIEF refresh is write-back step 10), and the coverage item, deepening HEN-35 into the Taiwan / Korea / chip-war supply source, passed to VULCAN (built 7/10–11; the roster gives it the Taiwan chokepoint and memory cycle) with ZHAO on the US–China clocks. HEN-35 itself resolved MISS on 7/17.

## COMPLETION — HENRY — 2026-11-17
STATUS: ✅ DONE
CHANGED: AGENTS/HENRY/research/2026-11-17_nvda-day/MAP.md, AGENTS/HENRY/STATUS.md, AGENTS/HENRY/STATUS_COLD.md, AGENTS/HENRY/workbook/KB.tsv, AGENTS/HENRY/inbox/processed/ (2 packets), AGENTS/WALTER/inbox/2026-11-17_from-HENRY_routing-use-measure-outside-audit.md, this packet
RESULT: Nvidia-day map on the first chain with Monday's trades: S&P flip 7,608 / 7,610, NEGATIVE −60.4 / −79.1 $B per 1%, 206 points under; QQQ flip 684 / 683, NEGATIVE; every wall withheld, not published. 3 inbox packets dispositioned; audit item 1 verified (8 ungraded rows, grading 11/20), item 2 measured at 34% cited.
GAPS: HY for 11/16 not posted at the read. Today's event hedges invisible until Wednesday's chain. Audit grading deferred to 11/20 (time went to the map).
WILL_NEEDS: None.
FOLLOW-UP: Hold for the close and results; 11/18 session (WQ-697 edit, row 9 at 16:15 ET, the first post-results map); 11/20 audit grading beside D:L490.
