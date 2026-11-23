# Will's rulings of 11/23, the paper book's stage-two figures, the HYG facts, and the 11/20 high-yield print

**Written:** 2026-11-23, started 12:05 EST (`date`), TERRY, Claude Code, Claude Opus 5.5, laptop. Task letter `inbox/2026-11-23_from-PROME_will-rulings-724-declined-730-arithmetic-HYG-wording.md` (6df81509fa); Will's words verified at `PROME/proposals/2026-11-23_wq732-follow-up-RULED.md` (items 4 and 8, and "WQ-724 ... declined"). $0. No trade, no order, no new tracker. Prices are vendor intraday screens with their pull times; option marks are SCREENING marks (durable finding 5b).

## 1. WQ-724, IDEA-QQQ-CAPIT-NOV20: DECLINED

Recorded on the card, `setups/INDEX.md`, `SETUPS.tsv`, `TRADE_BOOK.md` and `CARD_LEDGER.tsv` (root rule #10). Never filled, $0, no order.

What the card's own terms say about today: the credit filter needed an HY cell ≤ 350, and the 11/20 cell printed 376 (FRED, pulled 12:09 EST); the entry needed a red QQQ session at ≤ $635, and QQQ was $651.07, +7.00% (vendor 12:09 EST). So the card could not have entered today. The bounce it was built for came on a session it could not enter, kept out by the credit filter added on LIQUID's 11/20 packet and by the red-day rule. CAL-0009 (the trigger forecast, graded 1 on the 11/20 closes) is unchanged. Not a re-grade; a datum for the base-rate method if it is ever reused.

## 2. Paper book stage two (WQ-730): the corrected figures

### 2.1 Why PB-0002 was not in my $1,204.70, and what the right July figure is

My 11/22 note left PB-0002 out without saying why. That was a defect. The reason, stated now:

- **PB-0001 and PB-0002 are two records of one card, TRY-FIRE-004, in one contract (TLT Sep-30 77P).** PB-0001 is the paper fill at the 7/17 trigger, ×45 at $0.11 = **$495** (Will passed; the card says "HELD 7/17 (banked)"). PB-0002 is Will's real fill when the card re-fired on 7/20, ×30 = **$346.90**.
- The stage-two desk funds every would-fire card whatever Will decides, and treats his real fill as a tag on that card (`PAPER_BOOK_DESIGN.md` §3 RULING C). It makes no add without a scale rule written on the card (§2), and it caps a card at $500 (PAPER_BOOK guardrail 3: same $500 per card as the real book). With $495 charged on 7/17, the 7/20 re-fire could draw at most $5 more. The card's charge is **$495, at most $500**.
- The count already treats it this way: the 8/13 counter fix (Will-authorized) keys PB-0001 and PB-0002 as "two rows, ONE observation of TRY-FIRE-004". I applied that to the dollars on 11/22 without writing it down.

**Will's $2,128.76.** It counts PB-0002's 25-contract lot three times. PB-0002b, c and d each carry 289.08 in `risk_$`, the opening cost of the 25-contract lot at the 8/7 split, copied into each child at every later re-split. PB-0002 was one fill:

| Row | Contracts | `risk_$` cell | This lot's own share |
|---|---:|---:|---:|
| PB-0002a | 5 | 57.82 | 57.82 |
| PB-0002b | 15 (25 at the 8/7 split) | 289.08 | 173.45 |
| PB-0002c | 5 | 289.08 | 57.82 |
| PB-0002d | 5 | 289.08 | 57.81 |
| **Sum** | **30** | **925.06** | **346.90** |

(The cells sum to $925.06, not $924.06, so the total built on them is $2,129.76; the $1 is immaterial next to the triple count.) The cells are left as written; `PAPER_BOOK.tsv` now has a header line and a note on each child saying to sum per fill, never per row.

**If PB-0002 were charged as well,** July would be $495 + $346.90 + $287.70 + $422 = **$1,551.60**, over $1,500 by $51.60. That figure charges one card $841.90 against its $500 cap, so the design's rules do not produce it.

### 2.2 Matching periods, the design's own unit (`risk_$` per fill)

**Calendar months** (the design's tranche: $1,500, topped up on the 1st, unspent capital does not roll):

| Month | Charged under the design's rules | Outlay | Share of $1,500 | Not charged, and why |
|---|---|---:|---:|---|
| July | PB-0001 $495 (TRY-FIRE-004) · PB-0003 $287.70 (VIXCS) · PB-0004 $422 (FIRE-001) | **$1,204.70** | 80.3% | PB-0002 $346.90 (same card, Will's real-fill tag; §2.1) |
| August | none | $0 | 0% | PB-0005 $260 (RULING E: excluded until Will flips inclusion) |
| September | PB-0006 $220 (WAL roll) · PB-0007 $412 (VLO) | $632 | 42.1% | none; PB-0007 is contestable (failed its own entry gate on the fill day), $220 without it |
| October | none | $0 | 0% | PB-0008 $936.70 (Will's own QQQ trade ahead of the card's trigger; its row says the paper rules would not have filled it) |
| November to 11/23 | PB-0009 $380 (RSP) · PB-0010 $235 (UNG) · PB-0011 $230 (HYG) | **$845** | 56.3% | none |

**Equal 14-day stretches:** 7/17 to 7/30 = $1,204.70 (3 cards, 4 rows); 11/5 to 11/18 = $845 (3 cards, 3 rows). Every July and November fill falls inside those stretches, so the 14-day and calendar-month figures are the same.

**Did the budget bind in July? No, on the design's rules: $1,204.70, $295.30 under.** It goes over $1,500 only if TRY-FIRE-004 is charged twice ($1,551.60), and no calendar month goes over even with every excluded row put back (August $260, October $936.70). A 30-day window that straddles two months goes over only by putting Will's own QQQ trade beside November ($936.70 + $845 = $1,781.70, 10/23 to 11/21), and the tranche is monthly.

### 2.3 Each stage-two condition, separately

| Condition (`PAPER_BOOK_DESIGN.md`) | Test | Met? | Rows |
|---|---|---|---|
| **1. Six in 90 days** (§Phase 2 and Sharpening 4, Will 7/24): trailing-90-day would-fire count ≥ 6 cards | `paper_book_mark.py` `would_fire_90d`, replayed day by day 7/17 to 12/10 | **Counter: yes.** 6 on 10/23 to 10/25, 7 since 11/6, 6 again from 12/2. **Honest count: no.** Peak 5 (on 9/18, and today); 4 without PB-0007 | Counter today: PB-0006, 0007, 0008a, 0008b, 0009, 0010, 0011. The honest count drops PB-0008a/b: one trade the counter keys as two instruments after the split (its legs differ), and Will's own hand, not a would-fire. 9/18 peak: TRY-FIRE-004, VIXCS, FIRE-001, WAL roll, REFINER |
| **2. Four cards a month** (§Phase 2: the salary "binds once would-fire runs ≥ 4 cards/month") | distinct counted cards per calendar month | **No.** Peak 3 (July; November) | July: TRY-FIRE-004 (2 rows), VIXCS, FIRE-001. November: RSP, UNG, HYG. A 30-day window reaches 4 only with an excluded row: USOARM PB-0005 (RULING E) in 7/17 to 8/15, or Will's QQQ PB-0008 in 10/23 to 11/21 |
| **3. Outlay over the tranche** (§Decision Logic 3: "would-fire outlay demand > available tranche that month", charged at `risk_$` per fill) | calendar-month outlay against $1,500 | **No.** Peak $1,204.70 (July) | §2.2. Over only by charging TRY-FIRE-004 twice (July $1,551.60) |

Condition 1 is the only one that reads as met, and only on the counter. Exceeding $1,500 would not by itself have met condition 2, and in July condition 1 read 3 of 6 on the counter.

**Correction to my 11/22 note §3:** the counter first read 6 on 10/23 (PB-0008a and b entering the window), not on 11/5 to 11/6. It fell back to 4 by 10/29 and returned to 6 on 11/5.

### 2.4 Recommendation, as it now stands

**Unchanged: retire the stage-two gate; do not activate.** Corrected reasons: (1) on the design's own unit and calendar months, card flow peaked at $1,204.70 of $1,500 (July) and $845 in November, so the tranche has never forced a choice; (2) the four-cards-a-month test has never been met (peak 3); (3) the 7 of 6 on the counter comes from counting (one QQQ trade, Will's own, counted twice), the honest count peaked at 5; (4) stage one keeps every would-fire row with its opening time and `risk_$`, so if card flow ever outruns $1,500 a month, funded and unfunded can be worked out from the book after the fact. Retiring loses no data. The alternative, "not now", keeps the counter printing, and it would need the PB-0008a/b split fix or it stays tripped by counting. What changed since 11/22: the reasoning is now written down, the July figure keeps its exclusion visible, and the "first tripped" date is corrected. The recommendation itself does not change.

## 3. IDEA-HYG-FOLLOW-NOV05: the two facts kept apart

As Will set them on 11/23, on the card (new top block), `setups/INDEX.md`, `SETUPS.tsv`, `CARD_LEDGER.tsv`, `PAPER_BOOK.tsv` PB-0011, `TRADE_BOOK.md` and STATUS: **(1) fill UNKNOWN, reason UNRESOLVED; (2) approval standing, GATES `GATE-TERRY-HYG-FOLLOW-01` APPROVED, UNFILLED, entry window to 2026-12-04.** No reminder text. Today's print does not change the card's terms: its void clock (HY ≤ 330 on 5 closes) stays at 0 of 5 (352 [11/19], 376 [11/20]).

## 4. The 11/20 high-yield print: tradeability read (Will's 11/10 word)

**Verified at FRED myself (public CSV, pulled 12:09 EST):** HY OAS **376 bp [11/20]** (+24 from 352 [11/19]); CCC **1,402** (+41 from 1,361); BB **229** (+19 from 210). Context from the same pull, bar counts stated (construction rule #19; the public CSV holds 784 daily bars, 2023-11-24 to 2026-11-20): 376 is the 2026 high (234 bars) and the widest since 2025-05-01; CCC minus BB, 1,173 bp, is the widest in all 784 bars; +24 bp is the fifth one-day widening of 24 bp or more in 783 changes. BROCK adds that CCC/BB as a ratio fell, 6.48 → 6.12 (KB-BRK-522): the widening was led by the B and BB tiers, not CCC.

**Today's tape (vendor, 12:09 to 12:12 EST):** SPY $722.52 +4.74%, QQQ $651.07 +7.00%, NVDA $166.31 +32.49%, SMH +15.12%, RSP +2.46%, IWM +3.13%, KRE $69.20 +1.29%, VIX 28.14 −21.59%, VIX3M 26.14, HYG $76.64 +0.41%, JNK +0.43%, LQD +0.14%. Cause of the NVDA gap, established after my first read: Nvidia's 8-K (accepted 08:57:54 ET today, read at SEC by WALTER, SIG-W-20261123-001): the board reinstated Jensen Huang as CEO on 11/22, effective immediately; the investigation and the government inquiries continue, and the filing does not mention accounting or the SEC. VULCAN owns the read.

**Read: NO CARD.**
- The 376 is Friday's cell from the red-line day. Monday's tape reversed in stocks, and credit has barely followed: HYG +0.41% against SPY +4.74%. HENRY reads that as credit not confirming the rebound.
- REG-T-04 (REGINALD's: HY > 350 on three consecutive closes) stands at 2 of 3 (352, 376). The 11/23 cell, out about Tue 11/24, completes it if it prints over 350. To fail, HY must tighten 26 bp or more in one day, which happened 3 times in 783 changes (the largest −38 on 2025-05-12, a tariff-truce rally day). REGINALD grades it.
- None of TERRY's live cards turns on that print: the WQ-513 HYG ×4 card lapsed 11/13; the QQQ bounce card is declined (§1); the HYG ×5 card's terms are unaffected (§3).
- A second credit put would be the same driver as the existing HYG card (WQ-615 already put two HYG cards on one idea at $711.70, over the $500 default). A credit-long bet that spreads catch up with stocks has no owner direction behind it, and two owners (HENRY, BROCK) read credit as unconfirmed or not their mechanism. No structure clears the bar.
- Recorded `TRY-NOTRADE-HY376-NOV23` in `SETUPS.tsv`; `combo:credit-following` member added in `SIGNALS.tsv`.

**Forward view (unscored; REGINALD's gate, TERRY's projection):** the 11/23 cell prints over 350 and REG-T-04 completes, about 70%. Alternative: a rally-day tightening like 2025-05-12 takes it under 350, about 30%. Horizon: the Tue 11/24 FRED post. What would change my mind: HYG closing today up 0.8% or more (about twice its intraday gain), which would point to a tightening big enough. No card consequence either way.

## 5. Inbox, every sender

| Packet | Read |
|---|---|
| AEOLUS 11/22, Mississippi forecast low-water fall (+ AEOLUS correction 11/23 12:07 ET) | **NO CARD.** Taken with the corrections: barge rates fell two weeks running, not three (564.06 → 564.06 → 548.21 → 529.72% of tariff); Contargo's end of surcharges is a forecast; the 2022 and 2023 lows were 4.0 and 5.3 ft below the −6.8 ft forecast; no Mississippi trigger exists, so none could be met. The book holds no grain-basis or barge-exposed line (FORGE/STATUS.md, SETUPS.tsv, INDEX.md: no ADM, BG, CORN, WEAT, SOYB, KEX, DBA or barge line), so the 12/10 date has nothing to check here. No vehicle; AEOLUS agrees. No matching combo theme exists; logged here only (no new tracker). `TRY-NOTRADE-MISSRIVER-NOV23` in SETUPS. |
| BROCK 11/23, thesis grade IDEA-CREDIT-HYG-BDC-OCT23 + Car-Mart | Grade recorded in `POSTMORTEMS.md` (2026-11-21 owner-grades entry, now 6 of 12; owed: REGINALD, WAL, BOND, LIQUID, DEWEY, RED, PROME (ORCL)). Car-Mart: no listed lender or buyer named, equity $0.75; **NO CARD**, agreed. |
| HENRY 11/23 12:12 ET, red line reclaimed intraday, credit unconfirmed | **NO CARD.** My 11/21 condition (`TRY-NOTRADE-SPXGAMMA-NOV21`: two-week straddle-implied at or under 10-day realised at a close, S&P under about 7,400) reads met **intraday, not at a close**: SPY Dec-4 723 straddle mid $25.89 (vendor 12:12 EST, screening), about 25.8% implied (chain IV 23.9 to 25.8%) against 35.6% 10-day realised including today's bar (27.0% through 11/20; 65 vendor bars); S&P 7,245.69 (HENRY 12:07 ET). Reasons: the gap is a moment property on an intraday bar (construction rule #14), and the 10-day figure is two outlier days, −3.70% [11/20] and +4.85% today; implied falling 21% in one session is a decay reading that carries no direction (construction rule #15); the straddle needs SPY under about $697 or over about $749 by 12/4 to break even, against HENRY's own ~45% for a retest close under 7,037 by then; and it costs $2,598 per contract at the ask, 5.2× the $500 default, with no two-sided index structure at or under $500. |
| REGINALD 11/23 12:12 ET, REG-T-04 at 2 of 3 (HY 376) | **NO CARD**, agreed. Same state as §4, read independently (REGINALD 12:06 ET, mine 12:09 EST). REGINALD's projection that the 11/23 print fires it is about 75% (fitted 4.6 bp per 1% of SPY puts the print near 354); mine is about 70%. Bank leg BANK-ABSENT; no bank card. The one HY-keyed card I hold (HYG ×5) is unaffected (§3). |
| REGINALD 11/23 12:12 ET, thesis grades (3 cards) | Recorded in `POSTMORTEMS.md` (now 7 of 12; owed: WAL, BOND, LIQUID, DEWEY, RED, PROME (ORCL)): WAL Sep-18 pair WRONG for its window; TRY-WAL-ROLL70 UNRESOLVED (price leg resolves at the 12/18 close; WAL $67.90 on 11/20 under $70); IDEA-CREDIT-HYG-BDC-OCT23 WRONG for its window. |
| MIDAS 11/23, gold through the 11/19 to 11/20 break | **NO CARD.** GLD $335.75 +3.99% (vendor 12:16 EST). Recorded on `setups/GLD-SHARES_management-rails_2026-10-24.md` as a record: do not count GLD as protection for the put book (GLD up on 1 of 6 stress days since 10/22, MIDAS). No direction implied, so no card. Read in full at 12:16 EST while uncommitted; MIDAS committed it unchanged (9dbca95550, same bytes), then filed to `processed/`. |
| BOARD SIG-W-20261123-001 (IMMEDIATE, action names TERRY): Nvidia 8-K reinstates Huang | **NO CARD.** The cause of today's move is governance news, the same class as Friday's fall; the gap is done by the time of reading (NVDA $166.79 +32.87% about 12:15 ET), so any long is a chase, and the SEC accounting inquiry and the pending 10-Q stay a two-sided event (`TRY-NOTRADE-NVDASEC-NOV21` unchanged). VULCAN owns direction. Logged `acted` in `board_log.tsv`. |
| PROME 11/23, Will's rulings | §1 to §4 above. |

**BOARD scan run, 3 new since SIG-W-20261121-004, 1 logged** (-001 names TERRY, acted; -002 names LIQUID and REGINALD; -003 has no action line).
