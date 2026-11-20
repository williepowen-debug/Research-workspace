# BRT-33 window read, session 2026-11-20 (with pickup reads of 11/18 and 11/19)

`pull.py c1` (the 11/17 script, date and path changed) ran at 14:44:14 EST, after the window, from vendor one-minute bars, `period=5d`. One capture covers 11/16 through 11/20. Raw bars are in `raw/c1_*.json`, the summary in `window_c1.json`, the console output in `run_c1.txt`. [EST vendor proxy, labelled as such; no settlement substitution.] The 12:00 EST `t0` capture is pre-window context only.

## Control: the capture reproduces the earlier reads

Computed from this capture, 11/16 gives +4.5200 and 11/17 gives +5.0920, the same to four decimals as the reads taken on those days in separate captures (`../2026-11-16_brt33/NOTE.md`, `../2026-11-17_brt33/NOTE.md`). The vendor did not restate those bars, so the 11/18 and 11/19 rows below come from the same unrevised series. 11/13 falls outside the 5-day reach of this capture and is not re-read.

## Window [14:28,14:30) ET

| Session | BZF27 VWAP (bars, lots) | BZH27 VWAP (bars, lots) | M1−M3 | Valid? |
|---|---|---|---|---|
| Wed 11/18 (pickup) | 91.9156 (14:28 91.89 on 340; 14:29 91.94 on 357) | 86.8500 (14:29 86.85 on 244; no 14:28 bar) | **+5.0656** | valid: each leg has a positive-volume bar |
| Thu 11/19 (pickup) | 91.9813 (14:28 92.00 on 218; 14:29 91.96 on 192) | 87.1300 (14:28 87.13 on 223; no 14:29 bar) | **+4.8513** | valid |
| **Fri 11/20** | 92.5089 (14:28 92.57 on 186; 14:29 92.44 on 165) | **no bar** (bars at 14:27 87.76 on 252 and 14:30 87.50 on 56, none inside the window) | — | **NO OBSERVATION**: a session missing a leg is no observation, never a substitute (prediction row) |

Neither valid read is under +3.5000.

**Why 11/18 and 11/19 are read now:** the earlier sessions read 11/16 and 11/17 and named 11/20 as the next read. The registered rule settles on raw one-minute bars saved at each read within the vendor's reach of about 8 days. Both legs come from one capture, as the row requires, so these are ordinary BRT-33 observations, read late. They are not substitutes for 11/20.

## Count

Valid sessions: 11/9 +3.8039, 11/10 +3.7552, 11/11 +3.8713, 11/12 +4.2394, 11/13 +4.9903, 11/16 +4.5200, 11/17 +5.0920, 11/18 +5.0656, 11/19 +4.8513 = **9 valid, none under +3.5000.** No observation: 11/6 and 11/20 (BZH27 had no window bar both days).

**Consequence on the row's letter:** the 8-valid-session floor is met, so NO-VERDICT is no longer reachable. **BRT-33 resolves NO at the first read after 11/27 unless a window on 11/23, 11/24, 11/25, 11/26 or 11/27 prints under +3.5000** (Thanksgiving hours on 11/26 and 11/27 are unread; CME is IP-blocked). Not graded today: the timeframe is still open.

**Projection (mine, not registered):** today's same-minute pairs ran +4.25 (09:22 ET) to +4.97, and about +4.7 to +4.85 around the window. A cross needs a fall of about 1.35 to 1.6 in at most five sessions. The nine valid windows moved between 0.03 and 0.75 a session (standard deviation about 0.4). On that spread of moves, a cross is about a 10% chance, lower than the 20% registered on 11/5, when the pair stood at +4.42 to +4.50. What would change it: a deal or reopening headline that sells the front month, the kind that drove the 11/4 low.

## Context from the same capture (not registered reads)

| Read | 11/20 window | Note |
|---|---|---|
| M1−M2 BZF27−BZG27 | +2.6126 | +2.7662 on 11/17 |
| Jan 3:2:1 (RBF27, HOF27 vs BZF27) | 30.6995 | 32.4657 on 11/17 |
| **Dec HO−CL (HOZ26×42 − CLZ26)** | **80.5110** | HOZ26 3.9205 (2 bars, 760 lots); CLZ26 84.1500 (one positive bar, 14:28 on 172 lots; 14:29 bar zero volume) on CLZ26's last trading day. Vendor proxy, not a settlement. 11/17 83.9944. This is the last December-pair observation for D:L783 (`../2026-11-20_diesel-commission/REPORT.md` § Window). |

No line, gate, band or prediction moves. No TERRY packet: the spread moved away from the line, so there is nothing to trade.
