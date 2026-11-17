# BRT-33 window read, session 2026-11-17

`pull.py` is the 11/16 script with the date and output path changed. It ran at 14:45:11 EST, after the window, from vendor one-minute bars. Raw bars are in `raw/c1_*.json`, the summary in `window_c1.json` and the console output in `run_c1.txt`. [EST vendor proxy, labelled as such; no settlement substitution.]

| Leg | VWAP [14:28,14:30) ET | Bars with positive volume | Volume |
|---|---|---|---|
| BZF27.NYM | 93.1479 | 2 of 2 (14:28 93.16 on 119; 14:29 93.14 on 184) | 303 |
| BZH27.NYM | 88.0559 | 2 of 2 (14:28 88.04 on 268; 14:29 88.11 on 79) | 347 |
| **M1−M3** | **+5.0920** | valid (each leg has at least one positive-volume bar, per the row) | |

The read is not under +3.5000. **Valid sessions: 7 of 8** (11/6 had no observation; 11/12 +4.2394; 11/13 +4.9903; 11/16 +4.5200). Eight valid sessions are needed by 11/27 for a NO; otherwise the result is NO-VERDICT. One more valid session reaches eight. The spread widened 0.5720 on the day, away from the line: January rose 0.7179 against the 11/16 window (92.4300), March only 0.1459 (87.9100).

Context only, from the same capture: M1−M2 +2.7662 (+2.3874 on 11/16); Jan 3:2:1 32.4657 (33.8206); Dec HO−CL 83.9944 (85.7135). These use the 11/12 script's units and are not registered reads.

## Intraday shape, same-minute pairs with positive volume on both legs (79 pairs on 11/17)

| Time ET | M1−M3 | BZF27 |
|---|---|---|
| Low of the day (early) | +4.29 | n/a |
| 09:16 | +4.74 | n/a (research/2026-11-17_hormuz-tankers/NOTE.md) |
| 12:00 to 12:58 | +4.66 to +4.97 | 92.89 to 93.32 |
| 13:13 | +5.05 | 93.52 |
| 14:17 | +5.10 | 93.35 |
| 14:28 | +5.12 | 93.16 |

M1−M2 held at +2.76 to +2.79 from 14:00 to 14:15, against +2.51 at 09:16. The spread rose through the day while January itself held between about 92.9 and 93.5, below its 09:33 high of 93.86. The front month gained on later months rather than the whole curve rising.

## ⚠️ Correction, 14:49 EST 11/17, before closeout (supersedes the "met at the margin" finding below, which stays as written)

The section below compares the window with the highest **valid BRT-33 window** (11/13 +4.9903) and calls that the early-November range. That is wrong. My own TRACKER stamps record higher readings of this pair earlier in November: 11/5 bracket +6.10 to +6.33 (window not measurable, BZH27 had no bars); 11/6 same-minute +5.01 to +5.12 (window not measurable); 11/8 vendor daily row +5.02. **The early-November range is about +3.76 (11/10) to +6.33 (11/5), and +5.0920 sits inside it. Item 4 is NOT met.** The morning note wrote the range as "+3.80 on 11/9 to about +5.0", which understated its top. The 11/4 window +4.50 to the 11/5 bracket of about +6.2 is a move of about 1.7 in one session, so a 0.10 excess over 11/13 is well inside normal daily movement.

**What stands:** the day facts. January gained on March and February (M1−M3 +0.5720 and M1−M2 +0.3788 on the day) while flat price held. This is a firmer front end, worth watching, and not a priced supply loss. **What would now meet item 4:** M1−M3 above the early-November top, about +6.3, while flat prices rise. That is the range as I describe it, not a new registered level. No line, gate, band or prediction moves; no TERRY packet.

## Against my own invalidation list (research/2026-11-17_hormuz-tankers/NOTE.md § 5) — as first written and committed 14:46 EST (a6efd265ef), superseded by the correction above

Item 4 reads: "M1−M3 moving back above its early-November range of about +5.0 while flat prices rise." **It is met at the margin on this one window.** The window +5.0920 is 0.1017 above 11/13's +4.9903, the highest valid window in the BRT-33 run. Flat price rose against the 11/16 window (+0.7179), though not inside today's session (09:33 93.86 against window 93.1479). Items 1 to 3 are not met; FALCON's 11/17 second grade and WALTER's cards 001, 005 and 006 name no laden crude loss, no Gulf-ally production loss and no transit count after 11/16.

**What it changes:** the morning reading was "risk premium, not a supply loss being priced". The afternoon front-end firming is the first sign of prompt tightness being priced. It is one session, on thin March volume (347 lots in the window), and only 0.10 above 11/13. I did not find a dated read of this pair before 11/4 to set the level in a longer range. No line, gate, band or prediction moves; BRT-33 itself moved away from its line. **Confirmation** would be a second session above +5.0 with M1−M2 holding near +2.7 or higher. A fall back toward +4.5 undoes it.

## Trade-read handoff (WQ-696), corrected

This supports no investment implication. Over the next one to two weeks the Brent front end firmed on the day (M1−M2 +0.38) while flat price held, but M1−M3 at +5.09 sits inside its early-November range of about +3.76 to +6.33, so it is not evidence of a priced supply loss. This reading is invalidated by M1−M3 moving above about +6.3 while flat prices rise, by a confirmed laden crude loss, or by a stated Gulf-ally production loss. Unknown: whether the firming is physical tightness or thin-volume positioning (March traded 347 lots in the window); the curve is not read past March; the cause is not established. No TERRY packet.
