# November 6 window read, BRT-33 first session

**Captured:** c1 2026-11-06 14:45 EST, c2 15:05 EST, `pull.py`, raw bars in `raw/`. Vendor one-minute bars, proxies, not settlements. No exchange page read.

## Result

| Row | Value, [14:28,14:30) ET | Basis |
|---|---|---|
| BRT-33 M1−M3, BZF27 − BZH27 | **NO OBSERVATION** | BZH27 has no bar in the window in either capture |
| BZF27 | 98.3500, 2 bars, 411 lots | [EST vendor proxy] |
| BZH27 | none | last bars 14:25 (93.45, 1,066 lots), then nothing until a zero-volume 14:53 |
| BZG27 | 95.6800, 2 bars, 572 lots | [EST vendor proxy] |
| M1−M2 | +2.6700 | record only |
| CLZ26 | 90.8551 | [EST vendor proxy] |
| January 3:2:1, boundary #8 | $37.1868, count 0, line $50 | (2×RBF27 2.7279 + HOF27 4.2254) × 42/3 − BZF27 |
| December crack | $91.1225 | HOZ26 4.3328 × 42 − CLZ26, record only |

**F-a:** window NOT MEASURABLE, same as 11/5. Same-minute 14:25 read, BZF27 98.49 less BZH27 93.45, is +5.04, not an observation and never a substitute under the row. Not near +$3.50.

## BRT-33 count

Valid sessions 0 of 1. Row needs at least 8 valid sessions, otherwise NO-VERDICT.

BZH27 printed a positive-volume bar in the window on 5 of the last 7 sessions (10/29, 10/30, 11/2, 11/3, 11/4 yes; 11/5, 11/6 no), from `yf` 1-minute bars pulled 15:0x ET 11/6. Both misses are the last two sessions. Small sample.

Sessions left: 14 if Thanksgiving 11/26 has no window session, 15 if it does (the holiday schedule was not read). Chance of fewer than 8 valid sessions, binomial: at the 5/7 rate 7.4% on 14 left, 3.8% on 15; at a 50% rate 60.5% on 14 left, 50.0% on 15. Own arithmetic, independent-sessions assumption, guide only. March volume should rise as January nears expiry; that is reasoning, not measured.

This is a NO-VERDICT risk for the row, not an amendment. The row stands as registered. No change from BRENT without Will.

## Settles and rigs

November 6 settles not found on one search at 15:0x ET (too early for indexing). Baker Hughes not found on one search. Friday Close routine, 16:15 ET, carries both.

## After the close, third capture and settles

**Captured:** c3 2026-11-06 17:10 EST, same `pull.py`, raw in `raw/`; CLF27 added 17:13 EST for line 10. Live session, on PROME's relay of Will's 17:08 ET word.

| Row | c1 14:45 | c3 17:10 | Basis |
|---|---|---|---|
| BRT-33 M1−M3 | NO OBSERVATION | **NO OBSERVATION** | BZH27 has no bar in [14:28,14:30) in any of three captures |
| BZF27 | 98.3500 | 98.3534 | [EST vendor proxy], 411 lots |
| CLZ26 | 90.8551 | 90.8501 | [EST vendor proxy] |
| M1−M2 | +2.6700 | +2.6734 | record only |
| January 3:2:1, boundary #8 | $37.1868 | $37.1778, count 0 | line $50 |
| December crack | $91.1225 | $91.1275 | record only |
| WTI−Brent, month-matched, line 10 | not pulled | −$8.7491 | CLF27 89.6043 − BZF27 98.3534, expiry check CLF27 12/21 against CLZ26 11/20 |

Vintage spread between captures is under 1 cent on every derived row. BRT-33 stays valid 0 of 1, and the 5 of 7 presence count is unchanged.

**BZH27 same-minute, record only, never a substitute under the row:** 14:22 +5.12, 14:25 +5.04, 14:53 +5.04 (3 lots), 14:55 +5.01. F-a is not near +$3.50. Positive-volume BZH27 bars by hour: 10:00 6, 11:00 14, 12:00 23, 13:00 24, 14:00 11, 15:00 3. The contract trades midday and then thins out before the window, which is the shape of the NO-VERDICT risk.

### November 6 settles [EST wire, no exchange page read]

| Contract | Settle | Change | Source | Window proxy control |
|---|---|---|---|---|
| Brent January (BZF27) | **$98.32** | +$0.03 | CNBC, closes; Bloomberg via Rigzone names January, "settle at $98.32" | 98.3534, 3.3 cents off |
| WTI December (CLZ26) | **$90.83** | +$0.31 | CNBC, settle; Bloomberg via Rigzone names December | 90.8501, 2.0 cents off |

Both changes tie to the 11/5 wire settles: 98.29 + 0.03, 90.52 + 0.31. These two reports are one wire-level class, not an exchange read.

**Not settles:** the vendor daily rows dated 11/6, BZF27 97.76 and CLZ26 90.34, are the 16:59 ET last trades. Boot's "−0.54%" on Brent is that last trade against the 11/5 settle, so it is not the session change. BZH27 92.79 is a zero-volume 16:56 ET mark.

**Stays missing:** HOZ26, RBZ26, HOF27, RBF27 and BZH27 settles. No wire names them and the CME still blocks this machine, so products stay on window proxies.

### The week, same contract

| Contract | 10/30 [EST vendor row] | 11/6 [EST wire] | Change |
|---|---|---|---|
| BZF27 | 113.43 | 98.32 | **−13.3%** |
| CLZ26 | 104.12 | 90.83 | **−12.8%** |

CNBC's "Brent fell more than 16%" is a roll artefact (LESSONS #23): BZ=F 117.64 on 10/30 was the expiring December contract, and 117.64 → 98.32 is −16.4%. The same-contract fall is about 13%. Bloomberg via Rigzone has front-month futures down about 13.2%, biggest weekly loss since 2022. Dated Brent went 120.15 on 10/30, 107.03 on 11/3 [CONF EIA RBRTEd file pulled 11/6]; nothing newer is published.

### Rigs

US oil 463 (+1), total 604 (+1), gas 131 (+1), misc 10 (−1), week to 11/6: read at Reuters via BOE Report this session, matches the Friday routine. Baker Hughes primary 403 twice, with and without a minimal client name; no further attempt. Secondary, not primary. Record only.

### Flow claim, logged not adopted

Bloomberg via Rigzone, 11/6: "a revival in crude exports from the Persian Gulf"; physical crude "slumped in recent weeks, in some cases flipping to discounts as Saudi Arabia and the United Arab Emirates restore shipments to prewar levels"; Riyadh cut Asian crude prices "to a fresh six-year low"; product exports from the Gulf "remain more constrained". No figure, no vendor named, and this was the wire's market colour, not a flow print. It cuts against BRENT's record: Reuters 11/3 had Vortexa Gulf crude and condensate at 14.0, about 86% of pre-war, and October flows dipping, and "near pre-war" was rejected 11/4. Not verified. Not a thesis change. Logged on combo:gulf-flow-basis and combo:paper-physical-gap.
