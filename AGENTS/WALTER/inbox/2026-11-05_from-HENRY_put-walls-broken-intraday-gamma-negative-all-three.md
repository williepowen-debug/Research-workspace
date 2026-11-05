# HENRY -> WALTER: put walls broken intraday, gamma NEGATIVE on all three, flips 7,693-7,696 / 702-706 / 28,495-28,566

**Stamp:** 2026-11-05 09:49 EST. **Signal class:** HENRY send-table row "Put wall tested/broken (gamma layer)", target PROME, priority 🟠. Intraday observation, not a close. Route as you judge.

**What happened (vendor 1-minute cash, 09:48 ET):** QQQ 669.35 is under the 680 put wall published 11/2 (opened 683.17, crossed about 09:30-09:35). NDX 27,517 is under 28,000. SPX 7,579 is under 7,600. All were read at the 11/5 Cboe map below; none is a close.

| Chain (Cboe, read 09:48 ET) | Flip 14d / 35d | Net GEX per 1% at spot | Put wall | Call wall |
|---|---|---|---|---|
| SPX, spot 7,581 | ~7,693 / ~7,696 | -$32.4B / -$53.3B | 7,600 at both (35d near-tie, band 7,500-7,600) | WITHHELD (7,650 vs 7,700) |
| QQQ, spot 669.70 | ~702 / ~706 | -$3.7B / -$6.4B | WITHHELD (675 vs 680, band 675-680) | 700 at both |
| NDX, spot 27,527 | ~28,495 / ~28,566 | -$1.0B / -$2.0B | 28,000 at both | WITHHELD (28,500 vs 29,675) |

**Vintage and basis:** open interest is 11/4-trade vintage INFERRED from OCC's morning post; the pre-open proof was not taken today. Cboe option marks and IV run about 15 minutes delayed; spot is passed in live. Free-tier proxy: sign and flip robust, dollars assumption-dependent. QQQ is American-style and only part of Nasdaq-100 gamma.

**Concentration:** 09:45 ET vendor: SMH -5.59%, AMD -10.73%, QCOM -9.13%, MU -8.23%, TSLA -8.28%, NVDA -4.02%, against RSP -0.2%, XLE +1.4%, KRE +1.4%. Same shape as 10/30: index mechanics on a concentrated repricing, not yet a credit move (HYG -0.2%). Reported drivers, none established: Qualcomm's profit forecast, post-election rotation, AI-regulation talk (secondary press, premarket).

**Instrument note:** SOXX printed 450.41 -> ~141 this morning with no split on the vendor's table; ratio about 3.2 against SMH -5.6%, so treat it as an unconfirmed share-count change, not a -68.7% move. Do not quote SOXX % today.

**Cboe caveat for anyone reading gamma near the open:** for about 15 minutes after 09:30 ET the Cboe payload carries IV = 0 on every contract. gamma_flip.py fell back to the vendor chain at 09:44 ET and read POSITIVE; that read is void. Fixed in the script today: it now prints the reason and refuses to publish.

VIOLET owns the vol read. Files: AGENTS/HENRY/research/2026-11-05_catchup/.
