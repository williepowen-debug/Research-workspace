# November 27 evening boot threshold scan (WALTER, laptop, after the half-day close)

Written 2026-11-27T22:00:21Z (date command). Vendor pulls 21:57:20Z, FRED pulls 21:58:41Z. Registry check: RED scan view banner sha bca82363 equals canon; REGINALD THRESHOLDS.tsv read whole (8 rows; only REG_T02_EXIT_LOG changed since the 11/27 03:46Z scan, b99b631056); CREED and HANS registries unchanged since that scan (git log), states carried from it.

| IDs | Result |
|---|---|
| HY (RED-FT-01, 02, 12; REG-T-03, 04) | FRED 377 [11/25]; FRED also prints 377 for 11/26, a NON-SESSION by RED nonsession.py (Thanksgiving): bridge, not counted. Fired states continue; FT-02 exit <300 not near; FT-01 <280 and FT-12 <260 not near |
| CCC (RED-FT-07) | 1,417 [11/25]; 11/26 bar 1,417 NON-SESSION. FIRING-BANKED continues |
| HY one-session widening (safety net >25 bp) | 11/24 to 11/25 +5 bp; not met |
| VIX (safety net >30; RED-FT-06) | vendor ^VIX 23.81 at the 13:00 ET 11/27 close (vendor bar, not Cboe-certified); VIXCLS 26.80 for 11/26 is a NON-SESSION by the calendar (owner-completed holiday-bar check per 11/27 calendar row). Not met; FT-06 not re-armed |
| RED-FT-10 SKEW | ^SKEW vendor pull failed (no data); UNKNOWN; fired, exit 0 of 4 [11/25] per RED |
| RED-FT-09 (5y5y >2.55) | T5YIFR 2.11 [11/25]; not near |
| RED-FT-05, REG-T-05 claims | ICSA 189k [w/e 11/21]; not near 250 or 300 |
| REG-T-08 SOFR-IORB >15 | SOFR 3.95 [11/25] less IORB 3.90 = +5 bp; not met |
| REG-T-01 KRE <60 | 70.35 [11/27 close, vendor]; not near |
| REG-T-02 WAL <78 | 71.38 [11/27 close, vendor] inside the fired cycle; exit (>=81.90 x3) not met; no new fire |
| RED-FT-03, 04 Brent | DCOILBRENTEU 91.80 [11/24]; BZF27 96.48 vendor 11/27 03:53Z (prior read); neither near 130 nor 75 |
| Cushing | 25.613M [w/e 11/20]; next print Wed 12/02 |
| HANS-T-05, 06, 09, 10, 11, 07, 08, 16 | Carried from the 11/26 TE reads and HANS grades (11/27 03:46Z scan); 11/27 European closes NOT pulled: UNKNOWN for today |
| CREED rows | owner-graded monthly; states carried from the 11/25 scan |
| UNKNOWN | SKEW, HY Energy, gilt 30Y (HANS-T-13), 11/27 Bund, gilt, BTP, OAT, TTF; crack rows #6 and #8 not pulled |

No registered row newly fired. Near-trigger (within 5% one-sided): none new.
