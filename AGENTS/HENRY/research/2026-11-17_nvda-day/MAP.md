# Nvidia-day gamma map, Tue 2026-11-17 (first chain carrying Monday's trades)

**Desk:** HENRY (Claude Code, Opus 5.5 `claude-opus-5-5`, desktop) · **Wake:** PROME prome-19, WQ-703 (Will 09:30 ET, verbatim "703 yes") · **Read:** 09:48 ET, re-checked 09:50 ET (clock from `date`) · **Not published** to `workbook/PUBLISHED.tsv`.

## 1. The map

Command: `gamma_flip.py --both` (SPX) and `gamma_flip.py --both --underlying QQQ`, 09:48:05–09:48:11 ET, Cboe chain (`src=cboe`, no fallback, so implied vol was populated; the open-window IV = 0 problem did not apply).

| | SPX | QQQ |
|---|---|---|
| Spot used | 7,402.14 (Cboe feed, 09:48 ET); vendor 7,405.27 (09:48), 7,403.35 (09:50) | 662.32 (Cboe); vendor 661.05 (09:48), 660.59 (09:50) |
| Flip 14d / 35d | **7,608 / 7,610** | **684 / 683** |
| Net gamma 14d / 35d ($B per 1%) | **NEGATIVE −60.4 / −79.1** | **NEGATIVE −2.6 / −3.3** |
| Distance under the flip | 206–208 pts (2.8%) | 21–22 (3.3%) |
| Put wall | ⛔ WITHHELD: put = call at 7,500 (14d) and 7,000 (35d), put side unresolved | ⛔ WITHHELD: 14d put = call at 680 (35d put 680 is clean, +30%, but the 14d side is unresolved) |
| Call wall | ⛔ WITHHELD: 14d 7,500 vs 35d 7,000, horizons disagree | ⛔ WITHHELD: 14d 680 vs 35d 700 |

**Change since last night, same spot** (control run 09:50 ET with `--spot 7416.59` / `--spot 662.26`, the spots of my 11/16 20:5x ET read):

| | 11/16 evening (11/13 open interest) | 11/17 09:50 (11/16 open interest) |
|---|---|---|
| SPX flip 14d / 35d | 7,619 / 7,622 | 7,605 / 7,610 |
| SPX net gamma 14d / 35d | −61.2 / −81.3 | −56.6 / −75.5 |
| QQQ flip 14d / 35d | 688 / 686 | 682 / 681 |
| QQQ net gamma 14d / 35d | −3.0 / −3.8 | −2.4 / −3.2 |

So the chain did change overnight: the flip came down 10–15 S&P points and the short-gamma book is about 7% smaller. ⚠️ Part of that is Monday's expiries rolling off, not new positions; this read cannot separate the two.

## 2. Tape at the read (vendor, 09:47–09:50 ET; FRED for 11/16)

S&P 7,403–7,405 (−0.15 to −0.18%); NVDA $155.51 (−0.40%); QQQ $661.05; SMH $461.97 (+0.02%); RSP $218.79 (−0.06%); IWM $272.67; KRE $71.96 (−0.33%); 10Y (^TNX) 5.15; USD/JPY 159.40. VIX 22.98–23.04, VIX9D 23.46–23.63, VIX3M 22.97: the nearest maturity sits highest, which is where an event premium shows (VIOLET owns that read). FRED posted 11/16: SP500 **7,416.59** and VIXCLS **22.91**, both confirming my close read. ICE credit (HY, BB, CCC) for 11/16 was **not posted** at 09:48 ET; last is 11/13 (HY 323, YELLOW). Fed G.17 October industrial production came out 09:15 ET (ISHM packet): total −0.4%, manufacturing +0.3%; no visible tape reaction.

## 3. What the close must do

Nvidia reports **after** today's close, so today's close is the starting line, not the verdict. The results trade in tonight's futures and in Wednesday's session; Wednesday's close (11/18) is the first close that reflects them, and Wednesday morning's chain is the first that carries today's positioning.

| Close | Meaning |
|---|---|
| Over 7,500 | The 11/16 break under my last published put wall (7,500, published 11/12) failed |
| Over about 7,610 (flip band 7,605–7,610 today) | Dealers turn from amplifying moves to damping them. About +2.8% from 7,403 |
| Between about 7,343 and 7,500 | Still under the broken wall, still short gamma; no line crossed |
| Under about 7,343 | HEN-60 resolves YES (S&P closes under its 200-session average by 11/30). The line recomputes each close: 7,342.71 on the 11/16 basis by today's own calc, against 7,342.33 in my 11/16 record (0.38 apart, a vendor bar difference not resolved; it does not move any reading). About 60 pts (0.8%) under 7,403 |
| Under 7,200 / 7,100 / 7,037.04 | Yellow / orange / red (red = −10% from the 10/6 peak 7,818.93, WQ-609 A) |

**So what (working model, not a call):** Nvidia reports into a book that is still short gamma about 200 S&P points under the flip, a little less short than last night. Whichever way the result goes, dealer hedging adds to the move instead of absorbing it. This tells you **how big** a move can get, not **which way**. Getting back to the damping side needs about +2.8%; a fall needs about 0.8% to resolve HEN-60.

## 4. Caveats that travel

1. ⚠️ **Free-tier proxy.** The sign and the flip are the reliable part. The $B figures assume dealers are long calls and short puts, and hold implied vol fixed; real dealer positioning is not observed. Not SpotGamma-grade.
2. ⚠️ **Age of the positioning.** This chain carries **Monday 11/16's** open interest. Anything put on today, including hedges for tonight's results, is invisible until Wednesday morning's chain. By Wednesday's open the map is one day old.
3. ⚠️ The overnight change mixes new positions with expiry roll-off (§ 1).
4. ⚠️ No wall passes the guard on either index; there is no new wall. The reference stays the last published put wall, 7,500 [11/12], which the S&P closed under on 11/16.
5. ⚠️ Read at 09:48 ET, at the edge of the about-09:47 window; the script used the Cboe chain with populated vol, and the 09:50 re-run agrees.
6. Credit for 11/16 unknown at the read.

## 5. Trade-assessment handoff (WQ-696)

**This map supports no new investment implication.** It implies an index move around the results that dealers amplify rather than absorb, over the horizon of the 11/17 close through about the 11/19 close, with no direction. Whether that is already in option prices is a priced-vol question, VIOLET's. It is invalidated by a close over about 7,610, or by Wednesday's chain moving the flip down to spot. Unknown: real dealer positioning, today's event hedges, and Monday's credit. The directional finding (first close under 7,500) already went to TERRY via WALTER (SIG-W-20261116-011); TERRY returned NO CARD (relayed by PROME). No second TERRY packet.
