# Caution review — asks (a) and (b), and (c)/(d) status

**TERRY**, Claude Code, Claude Opus 5.5 (claude-opus-5-5), laptop · written 2026-11-26 16:31 EST onward (clock from `date`) · Thanksgiving, NYSE closed.
**Launch:** PROME letter `inbox/2026-11-26_from-PROME_launch-letter-caution-review-four-asks.md` (Will 15:59 and 16:19 ET; DOCKET D:L1278). One-off. **NO ORDER. $0. No card term, rule, size or X1 changed.**

## Method (read this before the table)

- **Scope:** every card in `CARD_LEDGER.tsv` that reached Will on or after 2026-10-22 and ended lapsed, declined, passed, parked, not taken, ended or void: **12 cards**. Excluded and listed at the foot: the QQQ put wall (Will placed it), the high-yield hedge and CoreWeave (both still live), and four cards that reached Will on 10/20 but were ruled after 10/22.
- **"Own terms"** = the card's trigger, window, day colour and cost cap as written. A card that never met them is $0.
- **"Bought at once"** = an order at the card's limit placed when the card was written: the fill is the card-time outer quote (ask of the long leg minus bid of the short leg) when that is under the limit; where the outer was ABOVE the limit, the fill is the limit and is marked **fill doubtful**. Then the card's own harvest, kill and time stop are applied on daily bars (intraday high/low checked for harvest). Fees $0.65 a contract a side ($1.30 a spread each way).
- **Marks, in order of preference:** (1) a vendor quote recorded in the repo on the date (card trigger-state lines, `research/2026-11-06_close-refresh/NOTE.md`, paper book); (2) the vendor chain's last two-sided quotes from the 11/25 regular session, pulled 2026-11-26 16:2x EST (market closed today, so these are the 11/25 closing quotes; screening marks under durable finding 5b, never broker fills); (3) a Black-Scholes model at each leg's implied vol, interpolated between the card-time IV and the 11/25 IV, on yfinance unadjusted daily bars pulled 2026-11-26. Exit at "bid" = model mid less the card-time half-width.
- **Model check against recorded quotes:** ORCL 11/5 6.05 quoted vs 5.92 model · ORCL 11/25 8.38 vs 8.29 · QQQ 670/680 11/5 4.57 vs 4.41 · QQQ 640/650 11/25 5.09 vs 5.35 · NVDA 155/165 11/25 4.00 vs 4.06 · UNG 11/25 0.72 vs 0.73 · CF 11/2 2.80 vs 2.88 · TLT runs 0.14 to 0.20 LOW (corrected +0.17 below) · **RSP 11/6 model 3.46 vs recorded 2.525: the model is badly HIGH on RSP, so the recorded mark is used.** Model values are estimates and are labelled `model`.

## (a) The table

| # | Card (reached Will) | State | Own terms | Bought at once, managed by its own exits | Exit that governs | Basis and date of every mark |
|---|---|---|---:|---:|---|---|
| 1 | MRNA Oct-30 200/220C ×1 (10/22) | lapsed 10/23, no ruling (WQ-498; TERRY rec decline) | **$0** | **−$300 to −$770** (fill at $7.70 doubtful: outer $8.85) | time stop: sell Mon 10/26 by 10:30 ET | 10/22 close chain on card; MRNA 10/26 bar O 186.90 L 181.65 H 203.82 C 198.85; model, post-readout IV unknown (60–106% tried) |
| 2 | OKTA Nov-20 220/230C ×1 (10/22) | parked WQ-492 B, shelved 10/29 | **$0** | **−$200 to −$300** | kill: close $184.87 < $185 on 11/2, sold 11/3 (harvest $6.80 never reached: model peak ~$5.0 at the 10/28 high $228.72) | card 10/22 13:32 quotes, fill $3.40; model IV 80% fitted to card mid ($2.85 vs $2.72) |
| 3 | USO Jan-15 170/185C ×1 (10/22) | not taken (WQ-491) | **$0** | **−$255 to −$280** | kill: close $145.41 < $150 on 11/4, sold 11/5 | card 10/22 fill $4.60; model 11/4–11/5 mid $2.19–2.47; 11/25 vendor mid $1.05 (held to now would be −$358) |
| 4 | HYG Jan-15 77/74P ×4 (10/23) | **approved** conditional WQ-513 A; lapsed unfired 11/13 | **$0** | **−$40 to −$155** (open) | none fired: harvest $2.00 not reached (model $0.91 at the 11/20 low); HY ≤ 330 ×5 reached 4 of 5 twice (10/26–10/29, 11/10–11/13); time stop 1/8/2027 | fill at the $1.00 limit (10/23 regular-hours mid ~$0.84); 11/25 vendor 77P 1.11/1.46, 74P 0.25/0.47 = mid $0.925, bid side $0.64 |
| 5 | ORCL Dec-18 115/100P ×1 (10/23) | **approved** conditional WQ-514 A; lapsed unfired 11/20 | **$0** | **+$373 to +$396** (open) | none fired: harvest $10.00 NOT reached on model (mid $9.12 at the 11/20 low $100.25, $9.43 at the 11/25 low $99.34); kill ≥ $145 ×2 not met (one close, $144.54 on 10/28); time stop 12/4 | fill $4.39 (10/23 card quote); 11/25 vendor 115P 15.95/16.20, 100P 7.60/7.80 = mid $8.375, bid side $8.15 |
| 6 | UNG Jan-15 10/12C ×5 (10/31) | approved WQ-573; ended unbought by Will 11/7 | **+$37 to +$112** (fired 11/5) | **same** (open) | none fired: harvest $1.00 not reached (model $0.76 at the 11/18 high $10.61); kill = CPC 12/3 test, pending; time stop 1/8 | PB-0010 fill $0.47 (11/5 14:38 ask side); 11/25 vendor 10C 1.27/1.39, 12C 0.52/0.70 = mid $0.72, bid side $0.57 |
| 7 | TLT Jan-15 82/78P ×2 (11/2) | declined WQ-592 B | **$0** | **−$15 to +$30** | time stop 11/20 close $81.45 (harvest $2.50 not reached: model $2.32 at the 11/13 low $79.11) | card 11/2 10:26 fill $1.41; model + $0.17 bias correction |
| 8 | CF Dec-18 125/135C ×1 (11/2) | declined WQ-593 B | **$0** | **−$205 to −$310** (fill at $3.30 doubtful: outer $4.10) | kill: close $111.68 < $115 on 11/4, sold 11/5 (open $115.64) | card 11/2 10:26 quotes (round trip 93% of mid); model mid $1.54–2.07 less half-width $1.30 |
| 9 | RSP Dec-18 220/230C ×1 (11/5) | passed WQ-616 B | **−$130 to −$155** (fired 11/5) | **same** | **invalidation: HY first-published 348 [11/5] > 344, readable 11/6, sell 11/6** | PB-0009 fill $3.80 (11/5 13:33); recorded mark $2.525 MID 11/6 17:10 EST (`research/2026-11-06_close-refresh/NOTE.md`); bid not recorded, taken $0.00–0.225 below |
| 10 | QQQ Dec-18 670/680C ×1 (11/5) | not approved WQ-617 C; lapsed 11/20 | **$0** (T1 met 3 sessions; debit $5.10 / $5.25 / $6.31 vs $4.90) | **−$25 to +$45** | **invalidation: same HY 348 [11/5] cell, sell 11/6** (QQQ 11/6 range $653.99–664.52, close $656.10) | card 11/5 13:33 fill $4.67; model 11/6 mid $4.54–5.23 |
| 11 | NVDA Jan-15 155/165C ×1 (11/12) | void 11/17 (WQ-677 B) | **$0** | **−$58 to −$95** (fill at the $4.00 cap doubtful: model mid $4.44 at $153.47; chain never priced on the card) | invalidation: close $145.98 < $148.80 on 11/19, sold 11/20 (open $143.52) (harvest $7.00 not reached: model $5.9 at the 11/13 high $170) | model; 11/25 vendor check 4.00 vs 4.06 |
| 12 | QQQ Dec-18 640/650C ×1 (11/20) | declined WQ-724 | **$0** (void: REG-T-04 fired on the 11/19–11/23 cells) | **+$20 to +$65** (open) | harvest $8.00 not reached (model $6.75 at the 11/23 high $657.53); invalidation pending: 363 [11/23], 372 [11/24], **11/25 cell unpublished** — if > 350, sell at the next session's bid | card 11/20 fill $4.41; 11/25 vendor 640C 19.64/20.26, 650C 14.73/15.00 = mid $5.085, bid side $4.64 |

**Totals (12 cards):**

| Group | Own terms | Bought at once |
|---|---:|---:|
| All 12 | **−$20 to −$115** (only UNG and RSP ever entered) | **−$530 to −$1,680**, central about **−$1,050** |
| All except MRNA (no ruling; TERRY recommended decline; fill doubtful) | same | **−$240 to −$900** |
| Approved and lapsed: HYG 77/74, ORCL | $0 | **+$220 to +$355, open marks, not banked** (ORCL's time stop is 12/4; its FQ2 print, unverified ~12/8–12/11, sits after that) |
| Will's own declines / not taken / ended: USO, UNG, TLT, CF, RSP, QQQ 640/650 | −$20 to −$115 | **−$380 to −$700**: his rulings avoided that much |
| No ruling, parked, void or not approved: MRNA, OKTA, QQQ 670/680, NVDA | $0 | −$505 to −$1,190 |

**Where my figures differ from the outside reviewer's** (theirs from underlying moves, no option quotes; mine outrank per the letter):

| Card | Reviewer | TERRY | Difference and why |
|---|---|---|---|
| ORCL 115/100P | about +$560, harvest "very likely hit around 11/20" | **+$373 to +$396 at 11/25 quotes, harvest NOT reached on model** | −$165 to −$190. Put IV rose to 87–93% by 11/25, which holds the spread below intrinsic: with ORCL at $103.88 the spread quoted $8.15–8.38, not ~$11. ⚠️ An intraday IV spike could have printed $10; the model says about $0.90 short at the 11/20 low. |
| QQQ 670/680C | −$200 to −$450 (credit exit 11/18) | **−$25 to +$45 (exit 11/6)** | +$200 to +$470. The card's credit exit fires on the first-published 11/5 cell, 348 > 344, readable 11/6; the reviewer used 11/18. |
| RSP 220/230C | −$265 (paper book at 11/23) | **−$130 to −$155 (exit 11/6)** | +$110 to +$135. Same 11/5 cell fires the RSP invalidation; ⚠️ **my own paper book missed it** (PB-0009 still OPEN, see § Finding). |
| QQQ 640/650C | +$150 to +$300 at the 11/23 peak | **+$20 to +$65 at 11/25 quotes** | −$85 to −$280. No exit rule fires at a peak; the $8.00 harvest was not reached (model $6.75 at the 11/23 high). |
| OKTA 220/230C | cannot be priced | **−$200 to −$300** | priced: the $185 kill fired on the 11/2 close $184.87. |
| TLT 82/78P | −$100 to +$200, very low | **−$15 to +$30** | narrower: model with measured bias correction; time stop 11/20 close $81.45. |
| MRNA 200/220C | −$400 to −$600 | −$300 to −$770 | wider: post-readout IV is unknown, and the fill at $7.70 was doubtful. |
| HYG 77/74P ×4 | −$50 to −$60 | −$40 to −$155 | the low end is the 11/25 bid side ($0.64; the 74P quote is wide). |
| UNG, USO, CF, NVDA | +$50/+100 · −$250/−350 · −$170/−330 · −$100/−250 | +$37/+112 · −$255/−280 · −$205/−310 · −$58/−95 | within or near their ranges; NVDA narrower because the 148.80 exit fired on 11/19 before the 11/20 gap. |
| **Net** | −$400 to −$1,500 | **−$530 to −$1,680** | agree in sign and size. |

**What this does and does not show.** It agrees with the reviewer's corrected line: on this window, caution has not visibly cost money. Bought at once, the twelve lose about $1,050 central; on their own terms they did about nothing. The one place the conditions cost money is the two **approved** cards (ORCL, HYG 77/74), about +$220 to +$355 on open marks, and ORCL's own T1 (Oracle 5Y CDS ≥ 350 bp) did not fire inside its window (high 342; it crossed after, 356 [11/24] and 364 [11/25]), and by then T2 (ORCL ≥ $120) had failed, so fixing the uncheckable earnings-date condition alone would not have entered it. Twelve cards in one selloff-and-rebound window cannot show more than that.

### Finding — PB-0009 missed its own invalidation (TERRY's record)

`PAPER_BOOK_DESIGN.md` close table: invalidation → sell at the BID at the trigger timestamp. PB-0009's invalidation (HY first-published > 344) fired on the 11/5 cell 348, readable 11/6; the row was left OPEN and kept being marked (1.15 at 11/23, −$265). The bid at the trigger was never pulled. **Corrected in `PAPER_BOOK.tsv` this session:** status CLOSED 2026-11-06, close fill = bid UNKNOWN with the nearest recorded mark (2.525 MID, 11/6 17:10 EST) cited, P&L left blank rather than computed from a mid (the fill rule forbids mids). No other open paper row has a fired exit: PB-0010 (UNG; kill = 12/3 CPC test) and PB-0011 (HYG hedge; HY ≤ 330 ×5 reached 4 of 5) checked.

## (b) Conditions that could not be checked, or triggers that fired after the window

| Card | The problem, in one line | What a checkable condition would have been |
|---|---|---|
| ORCL 115/100P | Will's added condition, an Oracle-IR-confirmed FQ2 date, could not be read: Oracle's site refuses automated access (and the card's T1 CDS ≥ 350 rests on sparse DTCC public prints, 5 converted on 11/6) | the date from Oracle's own press release on a wire service or an 8-K, or no date condition and a time stop set before the earliest plausible print (last year's date minus a week) |
| ORCL 115/100P, second line | **T1 also fired AFTER the window:** Oracle 5Y 356 [11/24, secondary, SIG-W-20261125-013] and 364 clean on DTCC [11/25, LIQUID, SIG-W-20261125-041], after the 11/20 lapse (highest read in the window 342). And T2 (ORCL ≥ $120 at the T1 reading) would have failed anyway: ORCL $109.50 [11/24], $103.88 [11/25]. The equity fell first and the credit followed, the opposite order to the card's thesis | a window to the 12/4 time stop, and T2 dropped or re-set to "ORCL above the long strike" so the card can fire when both legs move together |
| HYG 77/74P (credit card) | T1 (HY > 350 on three first-published closes) fired 11/23, ten days after the 11/13 window closed | a window that runs to the thesis horizon (the card's own 1/8 time stop), or a T1 that fires earlier on the same view (the 344 episode peak broke on the 11/5 cell, the line the 11/5 hedge card used) |
| MRNA 200/220C | entry required an issuer-confirmed ESMO presentation date; none was ever issuer-verified before the one-day window | ESMO's own published programme listing the session, or Moderna's press release; failing both, no card |
| CRWV 40/30P (live, approved) | CoreWeave's earnings date is unannounced on its IR page, and leg (b) needs a LIQUID 5Y read no more than two sessions old, which exists only when a desk writes it | a time stop before the earliest plausible print (FY25 Q4 precedent 2/26), and a public credit series named directly so anyone can check leg (b) |
| TLT 82/78P | letter and intent split: T1's letter ("vs the preceding same-tenor auction") would fire on a routine new-issue step-up (+$3B after October reopenings) with no supply surprise | "new-issue size vs the prior new issue, same tenor" |
| UNG 10/12C | the kill ("downward coupling") had no written test from the card's 10/31 date until WQ-642 on 11/6 | the CPC 8-14-day test as written on 11/6, from day one |
| NVDA 155/165C | T1 needed VULCAN to write a judgement (no demand or order impact), and the option chain was never priced; the $4.00 cap sat under the model mid ($4.44) at the card's own spot | a published-number T1 (guidance vs consensus, stated in figures), and a cap set off a priced chain |

**Patterns that are not "uncheckable" but bind the same way** (for Will's question about how conditions are written; no change proposed here, that is his):
1. **Exit fires the day after entry.** RSP and QQQ 670/680 were written on 11/5 during a selloff with HY at 332 [11/4] and an invalidation at "first-published > 344"; the 11/5 cell printed 348. A credit exit set 12 bp from the last print on a selloff day is close to a same-day kill.
2. **Trigger and void fire together.** QQQ 640/650: the panic close that fires T1 is the same stress that fires REG-T-04, the card's void. 
3. **Bearish cards that need strength first.** ORCL needed ORCL ≥ $120 at the CDS reading; CRWV needs a green close ≥ $48 (+12.8% from $42.57 [11/25]).
4. **Caps below the card's own quote.** MRNA (limit $7.70, outer $8.85), CF ($3.30 vs $4.10), NVDA ($4.00 vs model $4.44), QQQ 670/680 (failed by $0.20, $0.35, $1.41 on its three trigger days).

**What a better-written condition would have caught on this window: ORCL only, and only with a longer window AND no T2** (its CDS crossed 350 after 11/20, when ORCL was already under $120). The other approved card (HYG 77/74) would have entered on a longer window and is −$40 to −$155 on today's quotes.

## Excluded (not valued here)

QQQ 690/670P put wall (Will's own hand, +$1,683.92 known, one leg's price UNKNOWN) · HYG 76/73P hedge (approved, fired 11/6, fill UNKNOWN, window to 12/4; PB-0011 paper fill $0.46 vs 11/25 vendor mid $0.61, bid side $0.28) · CRWV 40/30P (approved, NOT-FIRED, to 12/11) · VST shares, IEF 90/92C, FXY 58/60C (reached 10/20, shelved 10/29) and RSP Jan 215/225C (reached 10/20, declined 11/6). Those four can be valued the same way on request.

## (c) The inbox: 21 packets read in full, NO CARD each (`TRY-NOTRADE-DRAIN-NOV26`)

Count reconciled: `boot.py` showed 22 at 16:21 EST = PROME's 21 plus PROME's own launch letter. All 21 committed by their senders. Position-facing first.

| Packet | What it is | Disposition |
|---|---|---|
| DEWEY 11/26 HYG-BDC grade | owner thesis grade: **MIXED** (description right, persistence wrong) | recorded in `POSTMORTEMS.md` grade table: **owner grades now 11 of 12** (owed WAL; PROME ORCL) |
| BOND 11/25 TLT-004 grade + auctions | grade already recorded 11/25 (packet was uncommitted then, committed since); auctions: bid substitution, no add gate | filed; no card. BOND's FR2004 dealer-leg read about 12/3 bears on any new duration-short card |
| VIOLET ×2 (vol fade; view 75%) | VIX 28.29 [11/25]; Dec VX 25.03 already prices a fade to 25; wide credit means a slower fade, not a second spike | no card: the fade is priced, spot VIX not tradeable. **Constructible:** the pending VIX call-spread leg (earliest a VIX-down session from 11/30, a new card to Will), unchanged |
| HENRY 11/25 close check | S&P 7,182.78; odds withdrawn; two-way 7,000–7,450 range; index options did not cheapen on the bounce | no card |
| SHADE 11/26 Athene AI credit | $2.41B par of AI-linked credit bought in Q3, carried at amortized cost; no CoreWeave line | no card: no loss channel before NAIC migration (~10% by the FY2026 annual, SHADE). APO puts would be a proxy of a proxy |
| CARL 11/26 lower-tier credit | borrower-level stress, balance-level losses stable, prime trusts improving | no card today. **Constructible:** CARL's dated trigger, Synchrony's November trust NCO above 4.35% (~mid-December), as a NOT-FIRED put idea; needs live prices, not built on a holiday |
| CARL 11/26 Affirm vs Klarna | one lender's reserve build, contradicted by the other; prints 1–3 weeks old | no card |
| LABOR 11/26 KELYA | thesis side of an 8/21 expiry: macro leg wrong, inferable at entry | recorded in `POSTMORTEMS.md`; construction point noted, no rule added |
| BRENT, FALCON, HAWK (Jazan) | Houthi hit at Jazan Port, minor damage; no barrels lost; a skew toward a Yanbu loading-stop tail (~10% by 12/9, FALCON) | no card. **Fenced, not absent:** a Brent tail call spread on a stated Saudi Red Sea loading stop is constructible, but the energy arm is retired (Will 8/7); reviving it is his word only |
| FERT 11/25 | MAP $1,004 (lagging retail series); Mosaic sells Faustina to CF (~$600M); s.301 proposal with no date | no card (CF was a declined card on 11/4; nothing here re-opens it) |
| HOMER ×3, NEXUS ×2, REGINALD | mortgage distress moving FHA to GSE/VA; mortgage insurers' notices +10.6% but loss ratios 10–20% and capital 158–193% of requirement; apartment losses on Fannie, banks and junior holders before any listed stock; warehouse books secured, no late loans | no card: earnings drag not solvency, horizon Q4 prints (late Jan–Feb 2027), options on the insurers unread and thin (NEXUS). Two of the six are same-day corrections, one a copy |
| CORAL 11/25 DeLand flood | rural single-family reach; Seacoast 10% of the three counties' deposits | no card (nothing observable before the 12/31 call report) |
| CREED 11/25 Q3 QBP | CREED-T-03 NOT FIRED; the bad prints are one private bank | no card |

Small items logged under Will's 11/5 rule: two `combo:` rows in `SIGNALS.tsv` (credit-following; bear-premise erosion, counterevidence included). Logging is not scoring.

**PROME's two unverified claims, tested against what this desk saw (not adopted):**
- **"Flooded":** 21 packets in about 28 hours (11/25 13:2x to 11/26 13:01). They carry about **14 distinct findings**: 3 packets on one Jazan event, 6 on one mortgage channel (2 of them same-day corrections, 1 a copy), 2 VIOLET packets on one view. Each took minutes to read; volume is not what stopped a card in this batch.
- **"Upstream desks filter ideas":** not what this batch shows. Every finding arrived, with its numbers. What arrived pre-judged is the verdict: **19 of 21 carry "no card" wording (grep count, 16:36 EST)**, mostly the sender's own lean or the standard "NO CARD is complete" line (a few only say no card is asked), and none proposes a structure (WQ-696 does not ask for one). I cannot see ideas a desk never sent, so this tests only what reached me.

## (d) Two sentences (labelled)

**Of the 21 packets read, two held an idea this desk could construct on (the pending VIX call-spread leg and a Synchrony trust-print put idea), a third is constructible but fenced by Will's retirement of the energy arm (a Brent tail on a Yanbu loading stop), and the other 18 had no listed vehicle, no edge, or an already-priced move.** ⚠️ *Recollection:* I have no memory across sessions, so I cannot recall how my sessions since 11/6 divided; my own STATUS record for 11/24–11/25 shows three sessions, of which one built a card (CRWV, 11/24) and two went mostly to reading and grading packets (11 and 16 drained, NO CARD each) and encoding Will's ruling, and the repo's record of sessions is the count, not this.
