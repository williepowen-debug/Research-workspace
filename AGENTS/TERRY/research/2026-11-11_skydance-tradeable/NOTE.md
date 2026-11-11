# Skydance Q3 10-Q: tradeability read (TERRY, 2026-11-11)

**Asked by:** PROME prome-2b, packet `inbox/processed/2026-11-11_from-PROME_skydance-10q-tradeability-read.md` (Will 11/10 18:03 ET, "always look for the trade"). **Source read:** `PROME/themes/ellison/reports/2026-11-11_skydance-q3-10q-read.md` (read whole), thesis `PROME/themes/ellison/theses/2026-10-22_ellison-collateral-loop.md`. **Desk:** TERRY, Claude Code, Claude Opus 5.5, desktop. **No order, no fill, no card term, gate, threshold or level changed.**

## Answer: NO CARD

Nothing in the 10-Q gives a Skydance trade with a trigger anyone can measure, and the one new fact that bears on the Ellison loop points the other way. Kept as `TRY-NOTRADE-SKYD-NOV11`, reference screen only.

## Why, in figures

| # | Reason | Figures (date, basis) |
|---|---|---|
| 1 | **The new fact weakens the Ellison-specific channel.** Ellison cash in the placement was $14.85B of $47.01B; about $32B came from sovereign and institutional buyers (PIF, QIA, L'Imad, LionTree). The loop the theme tracks runs through Ellison's balance sheet; most of the Skydance equity it would act on is not his. | 10-Q Notes 2, 6, 11 (reader, FILED) |
| 2 | **No measurable trigger exists before the 10-K.** The covenants (5.50x total, 3.25x first-lien net) are tested quarterly, but no post-close leverage ratio, EBITDA or headroom is filed; the purchase-price allocation is deferred to the 10-K (about Feb/Mar 2027, date not verified). A card keyed to covenant stress has nothing to read until then. | 10-Q Note 2, Note 8; reader § Not found |
| 3 | **The debt size is not new to the market.** The $72.1B issued or assumed was announced in the 10/6 and 10/13 8-Ks; the 10-Q confirms it. The stock has traded $6.80 to $8.70 since 10/14 (it was $9.27 on 10/13; part of that one-day drop may be the warrant ex-date, see Known unknowns). A put now pays for a story already in the tape. | vendor daily bars, 30 bars 9/29–11/10 |
| 4 | **The equity is a thin stub on a large secured stack.** At $8.04 the market value is about $40.6B (5,044M shares) against about $86.6B face debt (reader's arithmetic, not re-checked): equity about 32% of enterprise value, so a 1% move in enterprise value moves the stock about 3%. That is why vol is high in both directions, and why a direction call needs a thesis owner, not the desk's own leverage arithmetic. | cover share count 11/4; TERRY arithmetic |
| 5 | **No owner holds a bearish Skydance view.** The theme's own thesis says "Not a trade" for Skydance; its priced asymmetry is Oracle, already carried by the ORCL put card (WQ-499, not re-opened). Building a SKYD bear card on the desk's own read would be re-underwriting (hard boundary 3). | thesis § What it is NOT |
| 6 | **Holders at $12 are anchored, not forced.** Ellison Family 35.0% of equity and 77.5% of voting Class A; RedBird bought 4.9M warrants at $2.80 on 10/16 (code P). Underwater sponsors who are adding are not a forced-selling setup until something forces them. | 10-Q Note 6; Form 4 (reader) |

## The one dated feature worth recording: the placement overhang

About 2,245M placement shares (44.5% of outstanding; reader's 45%, TERRY's count of 3,918 − 1,240 − 433) bought at $12.00 are locked up 180 days from 10/6, to about **4/4/2027**, with a carve-out for pledging and a company waiver. Mark-to-market loss on the whole placement at $8.04: about **$15.5B** (Ellison's piece about $4.9B). The block is about 79 days of the 20-day average volume (28.4M shares). The resale registration naming holders is due about **12/22 to 12/23/2026** (reader's INFERRED date). This is a supply-overhang timing feature, not a credit trigger, and the buyers named so far are long-horizon sovereign funds; it is logged, not carded.

## Reference screen (not a proposal)

**Live chain at the read: UNAVAILABLE.** `chain_fetch.py --no-cache` at 08:50 and 09:36 ET returned bid 0.00 / ask 0.00 (DEAD) on every SKYD put strike in Dec-18, Jan-15 and Jun-17. HYG Jan-15 came back DEAD at 09:36 as well, so the outage is the vendor's whole option feed, not SKYD liquidity (same as the 11/9 open). Spot SKYD $8.06 +0.22%, SKYD-WT $3.61 (vendor, 09:36 ET). No debit is computed from dead quotes (finding 5b; construction rule #14).

What the feed does show is structure, not price: listed expiries Nov-13 through Jan-19-2029 (17), $1 strikes, open interest of thousands of contracts at the $5–$8 strikes (e.g. Jan-15 7P 15,828; Jun-17 8P 2,000; 11/10 vendor). Last trades on 11/10, for scale only, **not quotes and not at one timestamp**: Jan-15 7P $0.28, 8P $0.71; Jun-17 5P $0.21, 7P $0.75 (11/4), 8P $1.10. Realized vol 67.0% over 10 bars, 79.1% over 60 (vendor daily closes, 128 bars pulled). A Jun-17 put spread is the shape that would span both the ~12/22 registration and the ~4/4/2027 unlock; it is not priced here, and a revived idea is priced from scratch on the broker chain.

## What would change the answer (each a fresh build on that day's chain)

1. **A filed pledge of Skydance shares** by an Ellison entity (Form 4, 13D, proxy) while Oracle is falling: that is the theme's confirmer and the first point at which Oracle stress has a mechanical path into SKYD supply.
2. **A company waiver of the placement lock-up**, or a resale prospectus (about 12/22) whose selling-stockholder table registers holders other than the sovereigns for sale.
3. **A post-close leverage figure** (10-K, a rating report, or a lender disclosure) that puts the 5.50x test within reach, read by a credit owner (BROCK or LIQUID), not by this desk.
4. **Legacy Paramount CDS or the second-lien notes** moving on Oracle-specific news beyond HY (the theme's own falsifier test, inverted). Nobody read either today.

## Small items logged (WQ-622)

`SIGNALS.tsv` `COMBO-CREDIT-FOLLOWING` gains: Skydance ~$6B/yr interest on ~$86.6B face, covenants 5.50x/3.25x, legacy notes at about 83% of carrying value [9/30]; lock-up end about 4/4/2027. Logging is not scoring.

## Known unknowns

- The 10/14 one-day drop of 24% ($9.27 to $7.06, vendor bars) may be largely the ex-date of the warrant distribution (470.7M warrants at $12.00 distributed 10/13 to non-sponsor holders of record 10/5; SKYD-WT last $3.53 on 11/10, vendor). The warrants-per-share ratio is not in the reader's report, so the desk has not split the drop into ex-date and market move. Placement buyers settled 10/6, after the record date, so the $8.04 vs $12.00 comparison is the right one for them. The drop inflates the 20-day realized vol (119.6%) against the 10-day (67.0%).
- Post-close cash and leverage, rating actions after close, Paramount CDS: not read by anyone today.
