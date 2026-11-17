# Hormuz tanker hits 11/16, Bahrain 11/17: does my oil read change?

**Session:** PROME prome-19 follow-up wake (Tier 1 standing energy work), Claude Code, Opus 5.5, desktop. Started 09:44 EST Tue 2026-11-17 (from `date`). No pull: the tree carries other owners' dirty and staged paths (LIQUID, PROME), and PROME holds pull and push.

**Input:** FALCON's packet `inbox/2026-11-17_from-FALCON_hormuz-tankers-1116-bahrain-carrier.md` and report `AGENTS/FALCON/reports/2026-11-17_c8-hormuz-bahrain-carrier-grade.md`. FALCON's military grades are used as given and are not re-graded here.

## Answer

**No change to the oil read.** The market already had both tanker hits before the 11/16 Brent settlement window and still fell 3.5% that day. Today's rebound of about 1.5% kept the curve shape almost the same. That looks like some risk premium being priced back in, not a supply loss being priced. No line, gate or prediction of mine moves. Nothing goes to TERRY: there is no material finding (WQ-696 line below).

## 1. Did I know of the hits when I wrote the 11/16 read?

**No.** My 11/16 session ran 16:19 to about 16:30 EST (closeout commit baf1a5b7c5 at 16:30). No file of mine mentions ON PHOENIX, TARA GAS or UKMTO 207-26 (grep of STATUS, SCRATCH, NEXUS_BRIEF, board_log, CATALYSTS and the 11/16 notes, 09:4x EST today). The WALTER card I logged that day (SIG-W-20261116-001) covered the Bahrain drone attempts and Bab el-Mandeb only. Both hits were public before my session: the first at about 05:58Z (00:58 ET), the second at about 19:00Z (14:00 ET), per FALCON's UKMTO grades. That was a coverage gap in my inputs. It does not change the conclusion, because the tape saw both hits.

My 11/16 read, in my words: the paper curve was pricing a forecast surplus while land stocks were the lowest since 2016 and the October build was oil at sea (11/14 IEA note); Reuters' unread headline credited recovering Middle East exports and the surplus outlook.

## 2. What the tape did (vendor one-minute bars, about 10 minutes delayed, intraday, NOT settlements) [EST]

| Read | BZF27 (Jan Brent) | Source, time |
|---|---|---|
| 11/13 vendor daily close label | 95.84 | yfinance daily bar |
| 11/16 about 00:00 ET, before the first hit was widely read | 95.67 | 1-minute bars |
| 11/16 14:00 ET, the minute of the TARA GAS attack | 92.59 | 1-minute bars; no move: 92.55 at 13:59, 92.42 at 14:02 |
| 11/16 BRT-33 window VWAP [14:28,14:30) | 92.4300 | research/2026-11-16_brt33/NOTE.md |
| 11/16 low of the evening, 22:00 ET, after Iran's "minefield" claim about 15:15 ET | 91.58 | 1-minute bars |
| 11/17 rise starts about 03:00 ET (London morning) | 92.40 | 1-minute bars |
| **11/17 09:33 ET** | **93.86** | `fetch.py` BZ=F +1.54% and the named contract agree |

**Rebound since the 11/16 window: +1.43 (+1.5%), about 44% of the 11/16 fall of 3.40.** Brent is still about $2.0 below the 11/13 close. The rebound began in European hours. Its cause is not established: candidates are the Bahrain attempt on 11/17, the IRGC "southern route closed" warning, and position covering. I do not attribute it.

**Curve shape, same-minute pairs on 11/17 (33 common minutes):**

| Spread | 11/13 window | 11/16 window | 11/17 latest same minute (09:16 ET) | 11/17 range |
|---|---|---|---|---|
| M1−M3 (BZF27−BZH27) | +4.9903 | +4.5200 | **+4.74** | +4.29 to +4.78 |
| M1−M2 (BZF27−BZG27) | n/a | +2.3874 | **+2.51** | n/a |

The prompt spreads firmed by about 0.2 and stayed inside the early-November range (+3.80 on 11/9 to about +5.0). A priced supply loss would show up first as front months jumping over later ones. That has not happened.

**Other legs (vendor, 09:34 ET):** WTI CLZ26 87.24 (+1.77% on 85.72); CLF27 85.84. Heating oil HOZ26 4.0999 (+0.5% on 4.08); HOF27 4.0163 (+0.4% on 4.00); gasoline RBF27 2.5402 (+1.2% on 2.51). ⚠️ `fetch.py` HO=F printed −1.60% labelled HOZ26, but its price matches HOF27: the continuous symbol has rolled and the percent compares two contracts. Products are up less than crude, so cracks are slightly narrower. Dec HO−CL about 84.96 against 85.71 in the 11/16 window (context, not a registered read).

## 3. My lines and gates, each by its own written rule

| Line or gate | Rule (owner) | State 11/17 | Moves? |
|---|---|---|---|
| Brent futures above $100 (MKT-BZ-F-ABOVE-100) | REGISTRY; fired 7/23, no registered revert | BZF27 93.86, $6.14 below | No |
| Brent futures below $85 (MKT-BZ-F-BELOW-85) | REGISTRY | $8.86 above the floor | No |
| WTI futures above $100 | REGISTRY; un-fired 11/2 settle | CLZ26 87.24 | No |
| WTI−Brent premium above +$5 (TRACKER line 10) | month-matched | CLF27 − BZF27 = −8.02 (WTI at a discount) | No |
| M1−M3 flips to contango (TRACKER line 11) | registered flag | +4.74, backwardated | No |
| BRT-33, M1−M3 under +3.5000 by 11/27 | vendor window [14:28,14:30) ET | Today's window not yet read; morning same-minute +4.29 to +4.78, not near. Valid 6 of 7 | Owed after 14:30 ET today |
| BG-02 frame-breaker head clause | SPECS_GATES BG-02 | **NOT MET.** Neither hull is sunk; no cargo loss is confirmed; TARA GAS carries LPG and ON PHOENIX's cargo is NOT STATED; no Gulf-ally capacity or throughput loss is stated (FALCON: FAL-08 not engaged) | No |
| BRT-32, Yanbu loading halt | PREDICTIONS | Not met; every event is Hormuz, Arabian Gulf or Bahrain, none at Yanbu or Bab (FALCON theater check) | No |
| BRT-07, Hormuz reopening | PREDICTIONS | Events run away from a reopening | No |
| G:GATE-BRENT-COT-35B | REGISTRY; #14 JOINT NOT-SPENT | Next print #15 Friday 11/20 | No |
| BRT-31, BRT-34 | PREDICTIONS | Graded at Wednesday's WPSR (11/18, modeled) | No |
| TANKER-LIVENESS | Stage-A Leg T, graded only at an action | Nothing armed; not owed | No |

⚠️ **One forward perimeter question, recorded now and not decided:** if TARA GAS sinks with its cargo, BG-02 instance ③ says "any hull sunk with confirmed cargo loss" but its head clause is "destroyed capacity" and the clause was written about crude. Whether an LPG hull counts is not settled by the letter. If it happens, I return it to PROME for Will; I do not self-grade it.

## 4. Combination watch (6e, logged the same session)

- **combo:gulf-access-cost:** adds 11/15 AL DHANNAH damaged (IMO), 11/16 ON PHOENIX (probable) and TARA GAS (confirmed), Iran's four-mine claim (CLAIM ONLY), the IRGC "southern route closed" warning, and the 11/16 tape selling through both hits. Counterevidence: no sinking, census still 7; no laden crude loss; no November TD3C or war-risk print.
- **combo:gulf-flow-basis:** FALCON's 11/17 PortWatch pull read again (the 11/16 token error did not recur for FALCON; not re-probed by me): 11/15 = 2 transits, 0 tankers, against 88 a day before the crisis; Fujairah plus Sohar bypass 137,307 t/d over the 14 days to 11/13. A transit count is a floor (dark traffic unseen), a different perimeter from the Kpler and IEA export figures, never summed.

## 5. What would change the read (description, not new levels)

- A laden crude hull sunk or a cargo loss confirmed in the corridor (BG-02 instance check).
- A Gulf-ally state or operator stating crude production or exports offline (FALCON FAL-08; BG-02 R1).
- A fall in US-facilitated transits after 11/16, the route the IRGC warning targets (FALCON's PortWatch and UKMTO counts).
- M1−M3 moving back above its early-November range of about +5.0 while flat prices rise: front months bid over later ones is how a supply loss gets priced.
  - ⚠️ **Correction 11/17 14:49 EST:** the early-November range was misstated here and in § 2 ("+3.80 on 11/9 to about +5.0"). My own TRACKER stamps record +6.10 to +6.33 (11/5 bracket), +5.01 to +5.12 (11/6 same-minute) and +5.02 (11/8 daily row). The range is about +3.76 to +6.33, so this item means M1−M3 above about +6.3 while flat prices rise. This is the range as I describe it, not a new registered level. The 14:30 ET window (+5.0920) does not meet it → `research/2026-11-17_brt33/NOTE.md` § Correction.

## 6. Trade-read handoff line (WQ-696)

The evidence supports no new investment implication. Over the next one to two weeks it describes a steady to rising campaign against hulls near Musandam that the oil market has, so far, priced as a risk premium rather than a supply loss: Brent fell through both hits on 11/16 and today's 1.5% rebound left the curve shape almost unchanged. This reading is invalidated by any of the four items in section 5, above all a confirmed laden crude loss or a stated Gulf-ally production loss. Unknown: who is firing, ON PHOENIX's cargo, whether US-facilitated transits fall after the IRGC warning, and whether the rebound came from the Bahrain attempt, the warning or position covering. No TERRY packet sent, because this is not a material finding.

## Coverage limits

Vendor bars only; CME is IP-blocked from this machine (10/28) and no ICE page was read. No new web search: FALCON's military grades are the input and are not re-graded. The rebound's cause is not established.
