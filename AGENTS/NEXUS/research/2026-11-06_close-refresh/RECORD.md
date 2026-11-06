# NEXUS close refresh, November 6, 2026

**Task:** Will's 17:08 ET word via PROME (prome-51): boot, drain, refresh through the 11/6 close. Not the L554 pass. No spawns, no new thread, no card. Tier STANDARD (a correction commit). Runtime Claude Code, Opus 5.5.

**Result:** no grade, Conf, split, band or letter moved. Two letters will resolve on Monday's FRED cells; neither is graded here, because an unpublished cell stays missing.

## Test readings

| Letter | Published cells | Not yet a cell | State at this pass |
|---|---|---|---|
| M-04b | VIXCLS 16.61 [11/4], 28.18 [11/5] | Cboe close 25.64 [11/6, 16:15:01 ET print, VIOLET row TICK; also TERRY vendor 25.64]. FRED had no 11/6 row at 17:17 ET | UP 1 of 2, OPEN. **If the FRED cell is ≥ 22.45, UP fires, M-04 30→34.** Mechanism is HENRY's gamma sign at that cell: negative on all three chains at 11/6 09:55 ET, the 11/6 close map not read |
| L13 | DFII10 cell 13 2.64 [11/4], cell 14 2.60 [11/5, published 11/6] | Treasury real 10Y 2.63 [11/6] is the permitted early copy, FRED governs | DOWN 2, UP 0 on FRED. With 2.63, DOWN 3 of 5 at cell 15: no run can complete. **C#2 is the only outcome left unless a revised cell changes it; graded when FRED cell 15 publishes, about 11/9.** C#2 means EXHAUSTED: the split line returns to "currently un-falsifiable", no third window without Will's word |
| M-08b | B 367, CCC 1,320 [11/5] | 11/6 unpublished | Runs 0, unchanged |
| HY family | HY 348 [11/5], IG 93, BB 213 | 11/6 about 10:10 ET Monday | M-01 closed; L4 88 bp above 260; PRED-24 needs 350 ×2 |
| M-05 | Closed 11/5 | KRE 72.20 [11/6, vendor, TERRY] | No test open; shown for the chain row only |

Pull: `pull.py` here, `fred/` first-published JSON, run 17:15 and 17:17 ET. Treasury curves read 17:15–17:16 ET: real 2.60 → 2.63 [11/5–11/6]; nominal 2Y 4.46 → 4.51, 10Y 4.84 → 4.86, 30Y 5.25 → 5.26. Agrees with BOND 17:12 ET. Cboe history file not reachable from this box (Cloudflare block page); no evasion, VIOLET's print is the owner read.

## Owner reads taken directly (close-dated)

| Desk, stamp | Figure used |
|---|---|
| LIQUID 17:14 ET | HYG 77.23 (−0.06%), JNK −0.09%, XCCC −0.43%, BKLN +0.24%, QQQ +1.40%, IREN +20.02% [11/6, vendor]. Fund prices give no spread direction on a day yields rose. Oracle CDS 342.5 high [10/20], 305 [11/5], 306 to 314 converted [11/6, partial] |
| VIOLET 16:38 ET | VIX 25.64, VIX3M/VIX 0.9594, VVIX 121.94 [11/6 print]; convergence 38/50 RISING_VOL |
| TERRY 17:12 ET | Neither fired card (HYG, UNG) had an eligible finish; KRE 72.20, ORCL 116.10, RSP −0.38% [11/6, vendor] |
| BOND 17:12 ET | Front-led session; refunding sizes unchanged; December odds are HENRY's, 76% vendor last trade, not settlement |
| BRENT 17:1x ET | BZF27 98.32, CLZ26 90.83 settles [11/6, wire, no exchange page]; week −13.3% and −12.8% same contract; December crack proxy 91.12 [11/6 window, vendor] vs the $90.16 sell line |
| LABOR 16:49 ET | Freeze-thaw v2 fired on +165K first print, 15K over the bar; low-fire holds |
| RED 16:50 ET | HOLD 72, net-bear 68, no weight moved |
| REGINALD 16:51 ET | H.8 11/6 unread at its close; no score change |

## Counter-signal (Disc-D)

AI equities took back most of 11/5 while credit funds did not bounce, and yields rose: the equity tape says relief, the fund tape says nothing yet. VIX3M/VIX 0.9594 is a second inverted close on an up day. The HY 11/6 cell is the discriminator. One repricing class, no root added.

## Correction taken: WALTER notice, cards 041 and 042

| Item | Disposition |
|---|---|
| Card 041, SoftBank | **Corrected.** `READ.md` route 5 and the loop sentence, `EDGE_MAP.md` rows 6, 7 and the watch row, the diagram, `RECORD.md` L40, L59, L109 (originals kept there, labelled). The bridge leg of the "too worried" list is removed: it was already repaid, so it could never have tested anything. Conclusion unchanged: separate chains, no loop, no alert |
| Card 042, Oracle CDS history | **NO-OP.** The read used 292 and 305 only, both hold; it never carried 3.25% or 288 |

Residue grep across `AGENTS/NEXUS/` for 21.5%, $118, 13.7, $40B bridge, bridge balance: remaining hits are RETAINED-HISTORY: `RECORD.md` (labelled), `COLDREAD.md` (ledger of the draft) and the WALTER packet. Two other hits are unrelated 21.5% figures (the 9/24 letter's grid, the 10/20 record).

## Not read

BOOT 6 digest and the full matrix sweep (no spawns, owed L554 11/10). No brief read whole; owner STATUS headers only. Desks with no close-dated update at read time were not refreshed and keep their dates: HENRY 11/6 close map, FALCON, CARL, SAM, VULCAN, ZHAO, OSPREY, WATT, SHADE beyond headers, and the Tier-2 desks. Their rows stay dated, not presented as live.

## Closing freshness, 2026-11-06T17:19:16-05:00

Moved after the reads above: LIQUID brief, BRENT, SAM, VULCAN, WALTER cards 043–046. Header reads only for SAM and VULCAN: both report no score moved (VULCAN 15/25; SMH +3.62% [11/6, vendor]; SAM: no Japan-led carry unwind). No card reached NEXUS's lane. Flagstar's 10-Q was filed 11/6 16:15 ET (card 045), unread by WALTER and here, so M-05's row now says filed, unread. Card 043 (Qatar), 044 (consumer credit), 046 unread, deferred to L554 11/10. Delta-annotated, not re-swept. FRED re-checked 17:19 ET: VIXCLS 11/6 still absent.
