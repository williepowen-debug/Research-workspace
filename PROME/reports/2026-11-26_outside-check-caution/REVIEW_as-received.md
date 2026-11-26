# Is caution costing trades? An outside check of PROME's 11/26 answer

**Written:** 2026-11-26 by the outside reviewer (read only; nothing in the repo was changed).
**Repo read at:** master `bfc2c63125` (11/26 14:59 ET), which is a few minutes before PROME's 3:03 to 3:13 PM conversation.
**Prices:** public daily closes from stockanalysis.com and financialcontent.com (fetched 11/26), checked against closes the desks recorded in the repo (they match where both exist: QQQ $645.04 on 11/19, MRNA $202.63 on 10/22, NVDA $125.53 on 11/20, HYG $77.51 on 11/9). Option prices were **not** available. Every option value below is an **estimate from the move in the stock or fund**, and is labeled that way.

---

## The short version

1. **PROME's count is right in substance.** The ledger has 15 cards that reached you since 10/22. PROME's 14 leaves out the Moderna card, which was a "don't trade this" card that lapsed without a ruling. You approved 5. None of the 5 is a known position today: 2 lapsed, 1 (CoreWeave) is waiting, 1 (natural gas) you ended, and 1 (the high-yield hedge) fired with its fill unknown.
2. **PROME's "the biggest filter is upstream" does not hold up.** Desks are sending TERRY far more, not less. TERRY's inbox took 17 to 44 packets a week in October and **71 a week in each of the last two weeks**, most of them labeled "tradeability read." But cards fell: **16 cards reached you from 10/20 to 11/5, and only 3 from 11/6 to 11/26.** The narrowing happens where findings turn into cards, and in how the cards' entry conditions are written, not in desks hiding findings. A 11/16 independent sample found **0 of 20** cases where a desk failed to hand over an idea it had.
3. **The line PROME blamed on today's briefs is older and is PROME's own wording.** "A reasoned 'no card' is a complete answer" has been in `USER.md` since 11/10, written as PROME's reading of your "yes we should always be looking to see if something is tradeable." It appears in about 38 desk packets this month. Your words did not say it.
4. **What the passed-over cards would have done, roughly:** if every lapsed, declined and voided card since 10/22 had simply been bought at its stated price limit, the most likely total is **a loss of about $400 to $1,500**, not a gain. One card clearly would have paid: **the Oracle put spread, roughly +$560**, and it lapsed because of a condition nobody could check. Your own five declines cost about nothing: three could not have fired on their own terms and the fourth (equal-weight call spread) is about −$265 on TERRY's paper book.
5. **On this evidence, caution has not obviously cost money.** Fifteen cards in five weeks is far too few to say whether the setting is right. With forecast skill still small (+0.016 over baseline last week), the evidence supports "tidy up how conditions are written" more than "trade more" or "size up."

---

## 1. PROME's outcome table against the ledger

Source: `AGENTS/TERRY/CARD_LEDGER.tsv` (refreshed 11/25), rows with `reached_will` on or after 10/22.

| Card | Reached you | What happened | PROME's box | Holds? |
|---|---|---|---|---|
| Moderna Oct-30 200/220 call spread (ESMO) | 10/22 | Lapsed 10/23 with no ruling; TERRY recommended decline | not in PROME's 14 | PROME's first "fifteen" was right by the ledger; "fourteen" holds only if a don't-trade card is left out |
| Okta Nov-20 220/230 call spread | 10/22 | Parked (WQ-492 B), shelved 10/29 | deferred/parked | yes |
| Oil (USO) Jan-15 170/185 call spread | 10/22 | Not taken (WQ-491) | yours | yes |
| Nasdaq (QQQ) put wall | 10/22 | You placed it by hand 10/23 at ×2 | placed by you | yes; +$1,683.92 known, one leg's close unknown |
| High-yield credit put spread (HYG 77/74) | 10/23 | Approved conditional (WQ-513 A); lapsed unfired 11/13 | approved, lapsed | yes |
| Oracle Dec-18 115/100 put spread | 10/23 | Approved conditional (WQ-514 A); lapsed unfired 11/20 | approved, lapsed | yes |
| Natural gas (UNG) Jan-15 10/12 call spread | 10/31 | Approved (WQ-573); ended by you 11/7, never bought | approved then ended | yes |
| Long bond (TLT) Jan-15 82/78 put spread | 11/2 | Declined (WQ-592 B) | yours | yes |
| CF Industries Dec-18 125/135 call spread | 11/2 | Declined (WQ-593 B) | yours | yes |
| High-yield hedge (HYG 76/73) | 11/5 | Approved (WQ-615 A); fired 11/6; fill unknown; approval stands to 12/04 | fired, fill unknown | yes |
| Equal-weight (RSP) Dec-18 220/230 call spread | 11/5 | Passed (WQ-616 B) | yours | yes |
| Nasdaq 200-day Dec-18 670/680 call spread | 11/5 | Not approved, "decide at a fire" (WQ-617 C); lapsed 11/20 | deferred | yes, but see below |
| Nvidia Jan-15 call spread | 11/12 | Voided 11/17 on its own conditions | voided | yes |
| Nasdaq capitulation Dec-18 640/650 call spread | 11/20 | Declined (WQ-724, 11/23) | yours | yes |
| CoreWeave Feb-19 40/30 put spread | 11/24 | Approved, not fired (WQ-745 A) | approved, waiting | yes |

Two small slips in PROME's earlier answers:
- Its first answer listed "a Nasdaq call" among **approved** cards that lapsed. The Nasdaq 200-day card was never approved (WQ-617 C). PROME's later table put it in the right box.
- "Approved cards that become a position: about 1 in 5." On the record it is **0 of 5 known**. The one that fired (high-yield hedge) has no fill in any capture through 11/18.

## 2. The rulings PROME cited, against your recorded words

| PROME said | Your recorded words (source) | Verdict |
|---|---|---|
| 10/20: you loosened the rules so TERRY can bring ideas before a trigger fires | "we can loosen rules for trade ideas" (`USER.md`, 10/20 11:50 ET) | Holds. The $500 card default and the closed sizing gate (X1) stayed. |
| 11/10: you said always look for the trade | "yes we should always be looking to see if something is tradeable" (`USER.md`, 11/10 18:03 ET) | The paraphrase is fair. **"A reasoned 'no card' is a complete answer" is PROME's wording of the consequence, labeled as such in `USER.md`, not yours.** |
| 11/19: you asked for forward views | Verbatim in `USER.md` (11/19 12:01 and 13:31 ET), including "Projections do not automatically move scores, gates or trades, but they can motivate preparation and TERRY's prospective, NOT-FIRED proposals" | Holds. |
| 11/16: you looked at changing TERRY's rules after a sample review and held off | "Keep WQ-696's narrow handoff clarification; no TERRY charter or red-day rule change." (`PROME/proposals/2026-11-16_wq696-RULED.md`, 17:51 ET) | Holds, and it matters more than PROME said: **WQ-696 (a), "okay go with option a," already requires a desk that sends a finding for a trade read to say what it implies, over what horizon, and what would prove it wrong.** That is most of PROME's new step 1. |
| 11/23: you retired the paper book | "WQ-730: retire." (`PROME/proposals/2026-11-23_wq730-736-737-RULED.md`) | **Goes too far.** Only the paper book's second stage (a budgeted "salaried" desk and its three counters) was retired. The first stage, TERRY's shadow book that marks passed and approved cards, is still running (`AGENTS/TERRY/PAPER_BOOK_DESIGN.md`, status line). It already marks the equal-weight, natural gas and high-yield hedge cards. |

## 3. Where findings stop

**Desks are sending more, not less.** TERRY inbox packets by week (file dates, read and unread):

| Week of | Packets | Of which titled or framed as a tradeability read |
|---|---:|---:|
| 10/5 | 19 | about 0 |
| 10/12 | 35 | about 0 |
| 10/19 | 44 | 1 |
| 10/26 | 17 | 0 |
| 11/2 | 40 | 1 |
| 11/9 | 43 | 30 |
| 11/16 | 71 | 31 |
| 11/23 (to Thu) | 71 | 44 |

(The "tradeability" label only came into use after your 11/10 word, so the right column understates October. The left column is the safer comparison.) About 85% of the tradeability packets carry "no card" language, mostly the sender saying it suggests no card, or the standard "no card is a complete answer" line. **20 packets sit unread in TERRY's inbox now**, not the 5 PROME named.

**Cards fell while packets rose.** Cards reaching you, by date: 4 on 10/20, 4 on 10/22, 2 on 10/23, 1 on 10/31, 2 on 11/2, 3 on 11/5, then 1 on 11/12, 1 on 11/20, 1 on 11/24. That is **16 in the 17 days to 11/5 and 3 in the 21 days since.** The record does not say why. Plausible causes we can see, none proven: TERRY's sessions since mid-November went largely to grading, ledgers and inbox drains; the 11/5 to 11/20 selloff moved most prices outside card limits; and TERRY's own bar for a card.

**TERRY's own 60-day review (11/16) of 95 "no card" verdicts** (`AGENTS/TERRY/research/2026-11-16_no-card-review/REPORT.md`): evidence judged too thin or already priced, 43; no listed instrument, 14; trigger or gate not met, 14; no desk held a direction, 11; your decision, 6; the hard rules (cost caps, red-day/green-day, $500/X1), only 6. The independent reader then sorted the 20 "no direction" cases and found **0 failed handoffs**.

**Today specifically.** PROME's "every desk today said nothing material for trading" is close but not exact: CARL (two), DEWEY, HAWK and SHADE each sent TERRY a packet on 11/26, while CYPHER, LABOR and ORACLE logged "no TERRY packet, nothing material." We could not find the phrase "'nothing material' is a complete answer" in any committed brief; PROME's briefs go by message, so this cannot be checked from the repo.

**Our read of the bottleneck, in order:**
1. **How entry conditions are written** (next section). This is where approved ideas die.
2. **Turning findings into cards.** Many more findings arrive than ever; very few become cards since 11/6, and a backlog is building.
3. **Size,** which caps the payoff of a right call at roughly 1% to 2% of the Fidelity account.
4. **Your decisions,** which on this record cost about nothing (section 4).
Upstream filtering by desks is real but is the smallest of these on the evidence.

## 4. What the passed-over cards would have done

Two different questions, and they give different answers:
- **On the card's own terms** (trigger, window, day color, cost cap): every lapsed or declined card here comes to $0, because most could not have been entered.
- **If bought straight away at the card's price limit ("enter now")**, then managed by the card's own exits. This is the useful question, and it is what the table estimates.

All option values are estimates from the stock's or fund's move, without option quotes or bid/ask, so treat each as a range, not a figure.

| Card | Could it have entered on its own terms? | Enter now, managed by its own exits (estimate) | Confidence |
|---|---|---|---|
| **Oracle 115/100 put spread** (≤ $4.40) | No. Credit swaps never reached 350 bp (high 342.5 on 10/20), and the condition you added, an Oracle-confirmed earnings date, could never be met because Oracle's site blocks automated reads | Oracle fell from $126.16 (10/23) to $101.19 (11/20). The spread's take-profit at $10 would very likely have been hit around 11/20: **about +$560** | Medium. Direction certain; exact exit uncertain |
| High-yield credit put spread (HYG 77/74 ×4, ≤ $1.00) | No. Its trigger fired on 11/23, 10 days after the card lapsed | TERRY's 11/24 screen puts the spread mid at $0.87: **about −$50 to −$60** | Medium |
| Nasdaq capitulation call spread (640/650, declined) | No. Needed a red day with QQQ ≤ $635; the rebound came on a +7% day | QQQ $608.45 (11/20) to about $651 (11/23): **about +$150 to +$300 at the 11/23 peak**; current value unknown (no QQQ close after 11/20 fetched) | Low |
| Natural gas call spread (ended by you) | It fired; you ended it unbought | Shadow book: +$22.50 at the 11/23 mark; UNG $10.30 on 11/25 vs $9.31 at the card: **about +$50 to +$100** | Medium |
| High-yield hedge (approved, fired, fill unknown) | Yes | Shadow book +$20 (11/23); TERRY's 11/24 screen mid $0.56 vs $0.46: **about +$50** | Medium |
| Equal-weight call spread (passed) | Yes, it fired 11/5 | Shadow book: $3.80 to $1.15, **−$265** at the 11/23 mark | Medium |
| Nasdaq 200-day call spread (670/680) | Trigger met on three sessions, cost cap failed each time | QQQ fell to $608; the card's credit exit (HY above 344) came 11/18 near QQQ $659: **about −$200 to −$450** | Low |
| Nvidia call spread | No; its first condition failed and it voided | Its exit (close below $148.80) fired 11/19 at $145.98: **about −$100 to −$250** | Low |
| Moderna call spread (no ruling) | Possibly; 10/23 was red and below $202.63 | Must sell by Monday 10/26 morning; MRNA $198.85 that day: **about −$400 to −$600** | Low |
| CF Industries call spread (declined) | Probably not; CF $111.68 on 11/4, below its entry band | Its exit (close below $115) would have fired by 11/4: **about −$170 to −$330** | Low |
| Oil call spread (not taken) | No; its trigger (a US strike on Iran) never came | USO $168.09 on 10/29, then $135.43 on 11/24; the card's exit (close below $150) would have fired: **about −$250 to −$350** | Low |
| Long bond put spread (declined) | No; the Treasury auction-size trigger did not fire | TLT $79.38 (11/13), $82.24 (11/25); exit by 11/20, 11/20 close not found: **cannot be priced honestly; somewhere around −$100 to +$200** | Very low |
| Okta call spread (parked) | No; trigger never fired, and Okta was above its $212 "don't chase" line by 10/23 | No public Okta close after 10/27 reached us: **cannot be priced** | — |
| CoreWeave put spread | Still live | Not valued; it needs CoreWeave to rally about 27% to $48 before it can enter | — |

**Sum of the estimates:** gains about +$810 to +$1,010; losses about −$1,435 to −$2,305 (long bond left out). **Net, most likely a loss of roughly $400 to $1,500** had everything been bought at once. The conditions protected more than they cost, with one clear exception (Oracle).

**What this cannot tell you.** It is one five-week window that contained a sharp selloff and a sharp rebound, the estimates are rough, and 13 trades are too few to judge a strategy. It is consistent with DEWEY's "mixed" grade of the credit card. Treat it as a cross-check on TERRY's numbers tomorrow, not a verdict.

## 5. Are the entry conditions systematically too tight?

Patterns we can see in the cards themselves:
- **Bearish cards that need a rally first.** The CoreWeave put needs a green close at $48 or higher (about +27% from 11/24). The Oracle put needed Oracle at $120 or higher when its credit trigger fired, so when the stock fell first, the card could not fire. The 10/15 CoreWeave "rally fade" card voided the same way. Root rule #6 (puts on green days, calls on red days) adds a day-color condition to every card on top.
- **Triggers that fire after the window closes.** The credit card's trigger (high-yield spreads above 350 bp for three closes) came 10 days after its window ended.
- **Conditions the system cannot satisfy.** The Oracle-confirmed date could not be checked because Oracle's site is blocked to automated reads.
- **Cost caps a few cents below market.** The Nasdaq 200-day card had its trigger met three times and failed its $4.90 cap each time. Earlier, the yen and 7-to-10-year Treasury cards (10/23) missed their caps by 2.5 and 12.5 cents.
- **Several conditions stacked.** Most cards need a trigger, plus a day color, plus a price band, plus a cost cap, within a two-to-four-week window. Each one is reasonable; together they make firing rare.

**On size:** the Fidelity account was $45,338.94 with $32,243.61 (71.12%) in cash on the 11/18 capture (`FORGE/STATUS.md`), so the marks are eight days old as PROME said; Robinhood is separate and older. A $500 card's maximum gain is usually $500 to $1,000, which is 1% to 2% of that account. The closed sizing gate (X1, "don't size") still binds every card. With no proven edge yet, keeping size small is defensible, and nothing in this record argues for raising it.

## 6. PROME's four proposed steps

| Step | Our view |
|---|---|
| 1. Every desk states how it would express a finding and what would prove it wrong, one line | **Mostly already in force** under WQ-696 (a), 11/16, for findings sent for a trade read. Extending it to every finding adds a line to every packet, against your wish for less load. The cheaper fix is the wording: stop repeating "no card is a complete answer" in asks. That line is PROME's text, so PROME can stop using it in its own briefs; changing the `USER.md` line is yours. |
| 2. TERRY gives a card or a reasoned no on the packets, and values the lapsed cards | **Sound, as a one-off.** It should use the shadow book that is still running and the grades DEWEY and others have started, not a new study. The inbox backlog is 20, not 5. Keep it a one-time answer, not a recurring report. |
| 3. Each card shows a conditional entry and an enter-now entry side by side | **Use sparingly.** You can already approve any card for immediate entry, and you placed the put wall card yourself. A standing second entry doubles the pricing work on every card and will often break root rule #6, which you kept on 11/16. A narrower version: TERRY flags, on the card, when the trigger looks likely to arrive after the window (as with the credit card) or when a condition cannot be checked (as with Oracle). |
| 4. Size last, and yours | **Agree.** Nothing here supports changing it now. |

---

## Paste block for PROME (facts and next steps only)

```
PROME — outside check of your 11/26 caution answer, read at master bfc2c63125.

Facts:
1. CARD_LEDGER has 15 rows reached since 10/22; your 14 omits TRY-NOTRADE-MRNA-ESMO (lapsed 10/23, no ruling). Of the 5 approved, 0 are known positions; the HYG hedge fired 11/6, fill UNKNOWN. The Nasdaq 200-day card was never approved (WQ-617 C), so it is not an "approved card that lapsed."
2. "No card is a complete answer" is your wording of Will's 11/10 word, labeled as yours in USER.md; Will's verbatim is "yes we should always be looking to see if something is tradeable." The line appears in about 38 packets this month.
3. WQ-730 retired only Phase 2 of the paper book. Phase 1, the shadow book, is running and already marks PB-0009 (RSP, -$265 at 11/23), PB-0010 (UNG, +$22.50) and PB-0011 (HYG hedge, +$20).
4. WQ-696 (a), 11/16, already requires a finding sent for a trade read to state its implication, horizon, invalidation and unknowns.
5. TERRY's inbox: 71 packets in each of the weeks of 11/16 and 11/23 (17 to 44 a week in October); 20 unread now. Cards reaching Will: 16 from 10/20 to 11/5, 3 from 11/6 to 11/26.
6. The independent 11/16 sort of 20 no-direction verdicts found 0 failed handoffs.
7. Outside estimate, from public closes, no option quotes: bought straight away at their limits, the lapsed, declined and voided cards since 10/22 net about -$400 to -$1,500. Oracle 115/100P is the clear exception, about +$560 (ORCL $126.16 on 10/23 to $101.19 on 11/20). HYG 77/74P is about -$50 at TERRY's 11/24 mid of $0.87. TLT and Okta cannot be priced honestly. Full table: /mnt/project-files/trade-caution/2026-11-26_is-caution-costing-trades.md (Will can attach it).

Next steps:
a. When TERRY values the lapsed cards tomorrow, ask it to give each card's value two ways, on its own terms and bought at once at its limit, and to use the Phase 1 shadow book rather than a new study. Treat our table as a cross-check only.
b. Ask TERRY to note which lapsed cards had a condition that could not be checked (Oracle's IR date) or a trigger that fired after the window (credit card, 11/23).
c. Correct the inbox count for TERRY's wake: 20 unread, not 5.
d. Drop "no card is a complete answer" from your own briefs. Any change to the USER.md line is Will's.
```

## Decisions that are William's (not in the paste block)

1. **Whether to change the `USER.md` line "a reasoned 'no card' is a complete answer."** Our suggestion: keep the permission but drop it from routine asks, so a desk is not handed the exit in advance.
2. **Whether to adopt PROME's step 3 (an enter-now entry on every card).** Our suggestion: not as a standing rule; ask instead for a flag when a trigger is likely to come after the window or a condition cannot be checked.
3. **Size and the sizing gate.** Our suggestion: no change on this evidence.
4. **The high-yield hedge** (approved, fired, fill unknown, window to 12/04) is yours alone. We make no recommendation on it.

## Sources

- Repo files at `bfc2c63125`: `AGENTS/TERRY/CARD_LEDGER.tsv`, `AGENTS/TERRY/PAPER_BOOK.tsv`, `AGENTS/TERRY/PAPER_BOOK_DESIGN.md`, the card files under `AGENTS/TERRY/setups/`, `AGENTS/TERRY/research/2026-11-16_no-card-review/REPORT.md`, `AGENTS/TERRY/research/2026-11-24_reg-t-04-fired-tradeability/NOTE.md`, `USER.md`, `PROME/proposals/2026-11-16_wq696-RULED.md`, `PROME/proposals/2026-11-23_wq730-736-737-RULED.md`, `PROME/state/ORCH_LOG.tsv`, `FORGE/STATUS.md`, `AGENTS/TERRY/inbox/`.
- Public daily closes: [ORCL](https://stockanalysis.com/stocks/orcl/history/), [HYG](https://stockanalysis.com/etf/hyg/history), [QQQ](https://stockanalysis.com/etf/qqq/history/), [CRWV](https://stockanalysis.com/stocks/crwv/history), [NVDA](https://stockanalysis.com/stocks/nvda/history), [OKTA](https://stockanalysis.com/stocks/okta/history), [CF](https://stockanalysis.com/stocks/cf/history/), [MRNA](https://www.financialcontent.com/quote/NQ:MRNA/historical), [RSP](https://www.financialcontent.com/quote/NY:RSP/historical), [UNG](https://www.financialcontent.com/quote/NY:UNG/historical), [TLT summary](https://stockscan.io/stocks/TLT/price-history). USO, CF after 10/26, Okta after 10/27, and TLT and HYG daily closes after mid-November came from repo records or were unavailable, as noted per card.
