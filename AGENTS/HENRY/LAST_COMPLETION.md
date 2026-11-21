# HENRY — 2026-11-21 18:02–18:2x ET (late wake): the S&P closed Friday through its −10% line; options dealers offer no cushion down to about 6,400 — CLOSED on PROME's ask

**RESULT:** The S&P 500 closed Friday 11/20 at 6,910.39, down 3.70%, which is 126.65 points under my red line at 7,037.04 and 11.62% under the October record. The line fired and WALTER routed it to CARL and PROME. The fall was led by chips (Nvidia −14%), while the average stock, regional banks and junk-bond funds fell far less and Treasury yields dropped sharply. Options dealers are positioned so their hedging enlarges moves both ways at the same strength from about 6,400 to 7,100, so Monday can swing hard in either direction.

**CHANGED:** `STATUS.md` · `STATUS_COLD.md` (§ ROT-11/21) · `MEMORY.md` · this file · `NEXUS_BRIEF.md` · `board_log.tsv` · `registry/corrections_receipts.tsv` · `workbook/PREDICTIONS.tsv` (HEN-64 note, HEN-65 new) · `workbook/KB.tsv` (ML-HEN-240, -241) · `workbook/MARKET_DATA.tsv` (11/19, 11/20) · `research/2026-11-21_close-read/CLOSE.md` · inbox moves · packets to WALTER, TERRY and PROME.

## Session work

| Item | Outcome |
|---|---|
| Red line 7,037.04 | **Fired** on the Friday close (vendor figure; the official FRED figure posts Monday). Signal to WALTER, routed as SIG-W-20261121-004 to CARL (household wealth score) and PROME. No trade or gate attached |
| HEN-64 (close under 7,100 by 11/25, 40%) | Happened, 189.61 under. Graded Monday on the official FRED figure, as its wording requires |
| HEN-65, new (close at or under 6,700 by 12/4) | Registered at 40%; history since 1990 says 32–48% |
| Dealer map | Rebuilt by hand: the data vendor's weekend volatility figures are broken and Cboe blocks this laptop. Short gamma about $52–57B per 1%, flat from 6,400 to 7,100. Not published |
| Inbox | All 5 cleared, including WALTER's late VIX alert |
| TERRY | Handoff: the evidence points to big swings both ways over about 9 sessions, not a direction |

## Honest scope

- **Every figure is a Friday closing figure read on Saturday.** The laptop slept through the planned Friday afternoon read.
- **Two of my default commands each sent one ordinary request to Cboe** before I switched data source by hand; both were refused, and I made no attempt to get around it.
- VIX 35.89 is provisional: no proof it is the official 4:15 PM close until FRED posts Monday.
- The dealer map uses my volatility assumption, not market prices, and leaves out Friday's own options trading.
- The forecasts (about 65% the S&P closes back over 7,037 by 12/4; about 60% Monday closes higher) are my judgment, separate bets, unscored. Only HEN-65 (40%) is scored.

## GAPS / still pending

FRED S&P, VIX and junk-bond spreads for 11/20 post Monday. Dashboard v6 (11/12) not refreshed. LESSONS.md at 76% of its size cap.

## COMMITS

`555dcc3fdd` desk files · `7189ef0c82` TERRY packet · `2c58a0e3a6` WALTER late alert · `2d69f62740` PROME packet · WALTER packet committed by WALTER in `b0243970a6` · closeout commit "HENRY: 11/21 closeout". Not pushed (PROME pushes).

## NEXT SESSION FOLLOW-UP

Mon 11/23: grade HEN-64 on FRED; confirm the red line; junk-bond spread for 11/20 (at or over about 370bp would push me toward the downside). HEN-64 window ends Wed 11/25. FOMC 12/9 (HEN-63, hike, 70%).

## THESIS SNAPSHOT (frozen at close)

AI and chip unwind broke the index through −10%; rates rallying (2Y 4.63%); credit lagging (HY 352bp on 11/19, the 2026 high, 11/20 unknown); dealers short gamma with no cushion to about 6,400.

## WILL_NEEDS

None.
