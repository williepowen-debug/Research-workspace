# Did the trade cards make money?

**Repo:** williepowen-debug/Research-workspace · **Read at:** master `87d2c6624` (2026-11-17 19:38 ET), full history · **Written:** 2026-11-18. Nothing in the repository was changed. Times Eastern. Dollar figures are per-trade results, not account balances.

## The short answer

**The trade cards have not made money, but they have barely been used, so they also have not lost much.** In five months TERRY's desk logged 114 card ids. Only **four new-trade cards were ever bought as written**, each risking $220 to $412. Together they lost about **$460**: $241 is booked from broker fills, and about $220 more is a write-off whose close price is not in the record.

**Almost all the money in the account moved on William's own trades, not on cards.** Those were mainly short-dated QQQ puts and calls bought by hand and then managed with TERRY's sell-or-roll cards. The record books roughly **−$4,450** of realized results on those lines (Jul 20 to Oct 23). It also shows a further **+$1,684** on the one off-card trade that copied a card (the QQQ put spread), with one contract's close still unknown. By comparison, the cards are a rounding error.

**The cards William turned down came out mixed.** Some declined bearish ideas from August would have lost about $940. The declined ideas of October would have made money in the November slide: SPY about +$740 and the USO arm about +$740. Two more big "would-have-won" ideas could never have been entered under their own rules. With this few trades, the record cannot show whether TERRY's judgment, or William's approvals, add value.

**What the records cannot support:** the broker mirror stops at the 11/10 intraday capture. It has no orders panel and is missing several close prices. For cards that were never traded, the only marks are prices quoted inside the repo (vendor screens and the desks' own price pulls), not broker fills. Outside price sites are blocked from this environment, so I could not check those marks independently.

## How I counted

- **Universe:** every `setup_id` that ever appeared in `AGENTS/TERRY/SETUPS.tsv` or its 14 archive files (92 ids, read at all 161 commits), plus 23 ids that appear only in `setups/INDEX.md` or `TRADE_BOOK.md` history. **114 card ids** in total, not counting the scaffold row. List: [card_universe.tsv](/mnt/project-files/trade-outcomes/card_universe.tsv).
- **Rulings:** each card's `will_decision` cell, checked against `PROME/registry/WQ_LEDGER.tsv` rows that name the card.
- **Fills and results:** `AGENTS/TERRY/PAPER_BOOK.tsv` (which also holds real-lane rows with broker fills), `POSTMORTEMS.md`, the INDEX status cells and `FORGE/STATUS.md`.
- **Labels used below:** **BROKER** means a fill or close from William's broker captures, as TERRY or ANVIL booked it. **DERIVED** means the repo's own arithmetic on broker rows. **REPO-MARK** means a vendor or screening price written in the repo. **INFERRED** means my own reasoning from a repo-quoted underlying price, such as an option known to be in or out of the money at expiry.

### What the 114 cards are

| Kind | Count | What it is |
|---|---|---|
| New-trade cards that reached William | 30 | A proposed new position he could approve, decline or let lapse |
| Management cards on positions William already held | 38 | Sell, roll or exit plans for lines he bought himself (MGMT, EXIT, NOTE, RESHAPE) |
| Never reached William | 46 | 38 "no trade" reads and research candidates, plus 8 cards that stayed dormant or died by their own gate before a ruling (FIRE-001, -002, -003, -005, -007, WAL-GRIND, NCLH, AEOLUS-CATTAIL) |

## 1. New-trade cards William approved (9)

| Card | What | Ruling | Executed? | Result | Basis |
|---|---|---|---|---|---|
| TRY-FIRE-004 | TLT Sep-30 77P ×30 @ $0.11 | Approved 7/20 | **Yes**, filled 7/20 | **−$84.53** (harvest +$128.86; two sales off-ruling) | BROKER |
| TRY-VIOLET-VIXCS | VIX Aug-5 20/25C ×4 | Approved 7/27 | **Yes** | **−$111.60** | BROKER |
| TRY-BRENT-REFINER | VLO 1 share | Approved 8/27, re-affirmed 9/17 | **Yes**, 9/18, 22 days after approval | **−$45.33**, sold 11/5 by its exit rule, 2–3 days late | BROKER |
| TRY-WAL-ROLL70 | WAL Dec-18 70P ×1 @ $2.20 | Approved 9/1 (WQ-144) | **Yes**, 9/2 | William wrote it off 10/29 ("all dead"). **Close price UNKNOWN**, so likely about **−$220** | Fill BROKER; loss INFERRED |
| IDEA-UNG-SSW-OCT31 | UNG Jan-15 10/12C ×5 | Approved 10/31 (WQ-573) | **No.** Trigger fired 11/5; William ended it 11/7 after buying his own UNG Dec-24 10.5C ×1 | Card on paper: 0.47 → 0.575 (**+$52.50**). His own call: +$39 (+71%) at 11/10 | REPO-MARK |
| IDEA-HYG-FOLLOW-NOV05 | HYG Jan-15 76/73P ×5 | Approved 11/5 (WQ-615) | **No.** Trigger fired 11/5; no order through 11/17. It voids on two more high-yield spread closes at or under 330 | Card on paper: 0.46 → 0.385 (**−$37.50**) | REPO-MARK |
| IDEA-CREDIT-HYG-BDC-OCT23 | HYG Jan-15 77/74P ×4 | Approved conditional (WQ-513) | No. The trigger never fired and the card lapsed 11/13, as designed | $0 | — |
| IDEA-ORCL-PUTSPREAD-OCT23 | ORCL Dec-18 115/100P ×1 | Approved conditional (WQ-514) | No. Trigger not fired; open to 11/20 | $0 | — |
| IDEA-RSP-OCT20 | RSP Jan-15 215/225C ×1 | Approved conditional (WQ-591), then declined 11/6 | No. The trigger was met 10/30, but the price stayed above the card's cap | $0 | — |

**Approved and bought as written: 4 of 9, for about −$461 in total** (−$241.46 booked plus about −$220 inferred), on about $1,250 put at risk. **Approved, triggered and not placed: 2 of 9.** Both were small and roughly flat on paper (+$15 net). **Approved, but the trigger never came: 3**, which is correct behaviour.

## 2. New-trade cards declined, passed, parked or left to lapse (21)

"Hypothetical" means what the card's position would be worth if bought at the card's price and held. It is an estimate, not a fill.

| Card | What | What happened | Hypothetical result | Basis |
|---|---|---|---|---|
| TRY-BRENT-USOARM | USO Oct-16 125/130C ×2, $260 | Let expire unfired 8/13 (William's ruling) | **+≈$740** held to expiry. USO was about $153.80 on 10/14 and $168.83 on 10/30, so the spread finished at its $1,000 maximum. At 8/13 it was −$90 on paper | INFERRED from REPO-MARK |
| TRY-NOTRADE-WQ409-SPY | SPY Dec-18 770/760P ×1, $262 | Passed 10/11 (WQ-418) | **+≈$740 or more.** SPY was $754.21 on 11/13, so the spread is at least $10 in the money | INFERRED |
| TRY-COND-QQQ-DATED-DOWNSIDE | QQQ Dec-18 put spread about 730/710, ≤$491 | Declined 10/15 (WQ-365) | **+≈$1,500** if bought (QQQ $661.75 on 11/16). **But its own credit condition never came true in the window, so as written it could not have been entered** | INFERRED |
| IDEA-TLT-QRA-NOV02 | TLT Jan-15 82/78P ×2, ≤$290 | Declined 11/4 | **+≈$230** (TLT $79.38 on 11/13). Its trigger, a larger Treasury refunding, did not happen, so as written: no entry | INFERRED |
| TRY-COND-CRWV-RALLYFADE | CRWV Jan-15 65/60P, ≤$480 | Commissioned 10/15; voided by its own terms 10/22 | Near the $500 maximum (CRWV $53.60 on 10/30, $58.21 on 11/11), but never armable as written | INFERRED |
| TRY-WILL-QQQ-VFADE | QQQ Aug-21 680/670P ×2, $452 | Void by its own terms 8/4, before a ruling | **−$452** (QQQ about $730 on 8/13). Loss avoided | REPO-MARK and INFERRED |
| TRY-WILL-QQQFADE | QQQ Sep-18 645/620P, ≤$490 | Parked, retired 8/27 | **About −$490.** QQQ never neared 645 before expiry. Loss avoided | INFERRED |
| IDEA-USO-POSTELECTION-OCT22 | USO Jan-15 170/185C, $461 | Not taken 10/29 | Most of the $461 lost (USO $142.34 on 11/16). Loss avoided | INFERRED |
| IDEA-CF-Q3-NOV02 | CF Dec-18 125/135C, ≤$331 | Declined 11/4 | Below cost (CF $122.07 on 11/16), and its trigger never fired | INFERRED |
| IDEA-RSP-DEC-NOV05 | RSP Dec-18 220/230C | Passed 11/5 | −$25 on paper (3.80 → 3.55) | REPO-MARK |
| TRY-COND-TLTPUT-WQ339 | TLT Dec-18 77P ×2, ≤$491 | Lapsed unapproved 10/14 | Probably below cost (TLT $79.38, still 3% out of the money) | INFERRED, not priced |
| IDEA-VST-OCT20 | VST 2 shares, ≤$149.70 | Shelved, unapproved | About −$23 at 10/30 ($138.37); not marked since | REPO-MARK |
| TRY-BRENT-DIESEL | VLO Jan-15 360/380C, about $405 | Never ruled; TERRY said "no at this price" | Not priced: VLO is about $367, between the strikes | — |
| Eight more (IEF, FXY, OKTA, MRNA, DHI/PHM, FIRE-006, QQQ-200D, NVDA) | small spreads | Declined, parked or not approved | Not marked: no reliable underlying price in the repo, or the card was never priced | — |

**Taken together:** the three August bearish declines avoided about $940 of losses. The two October declines that could actually have been bought (SPY, USOARM) missed about $1,480 of gains. The two largest "misses" (QQQ dated, TLT refunding) could never have been entered under the cards' own rules, so they say more about the trigger rules than about William's decisions. The paper results are close to a wash, and the sample is far too small to grade anyone's judgment.

TERRY's paper book was built to answer exactly this question ("did the discipline to say no save or cost money"). It holds only five passed or never-approved rows, and three are still open. Its own design rule says nothing may be scored until 10 closed rows across 5 independent themes exist.

## 3. Rulings on positions William already held

These are where the money actually moved. The position was William's own purchase. The card was TERRY's sell, roll or exit plan.

| Line | Card | Ruled | Carried out? | Result | Basis |
|---|---|---|---|---|---|
| TLT Sep-30 85P | TRY-EXIT-TLT85P | Sell, approved 9/3 | Yes, 9/10, at a higher limit William set himself | +$140.67 | BROKER |
| XLE Sep-30 65C | TRY-EXIT-XLE65C | Sell after OPEC+, approved 9/3 | Yes, 9/11 | −$77.33 | BROKER |
| USO Oct-16 135C | TRY-MGMT-USO135C | Rules approved 9/1 | Sold 9/9, before any rule fired | +$1,043.64 on the last lot; first lot price UNKNOWN | BROKER |
| USO Sep-18 150/165C (Robinhood) | TRY-MGMT-USORH150165 | Exit rule approved 9/10 | Sold the same day, before the rule | +$330.00 | BROKER |
| OZK Nov-20 40P ×4, WAL Dec-18 65P ×4 | MGMT-OZK40P / MGMT-WAL65P | **Sell, approved 10/14 (WQ-428/429)** | **No** | About $600 of quoted value lost since the ruling (−94% and −74% at 11/10). OZK expires Fri 11/20 | REPO-MARK |
| TBT / TLT duration shorts | MGMT-DURSHORT-EXIT-WQ291 | Sell, approved (WQ-357) | Partly; then William bought TBT back | Not graded | — |
| Short-dated QQQ/USO/TLT puts and calls, 9/28–10/23 (about 17 closed lines) | MGMT-QQQ7xx, USO15x/16x, TLT82P | Sell-or-roll cards, mostly not put to a ruling | Sold or expired by William | **−$110.87 net** on the lines with booked results. Six more lines (QQQ 719P, 715P ×2, CRWV 56P, USO 165C Oct-28, CMG 28P) have **result UNKNOWN** | DERIVED |
| QQQ short-dated put cluster, 7/20–8/4 (11 tickets) | postmortem only | none | — | **≈ −$4,341** | DERIVED |
| QQQ Nov-20 690/670P ×2 | IDEA-QQQ-PUTWALL-OCT22 | Bought by hand 10/23, before the trigger and before approval, at twice the card's size | — | **+$1,683.92 known.** The second 690P's close is UNKNOWN (D-94; $1,339.67 of cost not booked) | BROKER plus UNKNOWN |
| 14 bank and credit put lines (D-74) | none | none | — | Cost $6,644.24, marked $1,110.00 at 11/10: **≈ −$5,534 open**, with owner, card and approval all UNKNOWN | REPO-MARK |

## What this means for William

1. **"Did the research make money?" cannot be answered from cards, because the research has rarely been traded as written.** Four cards were bought as written in five months, all small, and their result is about −$460. Larger exposure came from William's own trades, which the cards then managed. The biggest open losses (the 14 bank and credit put lines, −$5.5K on the 11/10 marks) have no card or desk owner at all.
2. **Where a card's own discipline was used, it mostly behaved as designed.** Triggers that never came kept money out (HYG-BDC, ORCL, CF, VFADE). When the card was overridden or skipped, results were mixed in both directions: the QQQ put spread bought early made money, while the OZK and WAL sell rulings that were not carried out lost about $600.
3. **The weak spot is between "approved" and "filled".** Two approved, triggered cards (UNG, HYG) were never placed, and two approved sell rulings (OZK, WAL) were never carried out. Nothing tracks approved but unexecuted rulings as a class.
4. **Several results are missing from the record:** the WAL 70P close, the second QQQ 690P close, six short-dated lines and the first USO 135C sale. Until they are filled, any total, including mine above, is a floor or ceiling rather than a figure.
5. **PROME already moved on part of this.** On 11/16, at William's word ("yes lets do this"), PROME packeted TERRY to get thesis grades and fill the missing close prices from broker evidence. TERRY's session for that is due today (11/18). The steps below do not repeat it.

## Limits

- The broker mirror ends at the 11/10 intraday capture (no closes, no orders panel). Any fill after 11/10, such as an HYG order, would not be seen.
- Hypothetical results for untraded cards use repo-quoted underlying prices and expiry logic, not option fills. Spread values before expiry are lower bounds from intrinsic value, except where TERRY's paper book gives a vendor mark.
- Outside price sources (Yahoo, Stooq) were blocked from this environment, so no repo-quoted price was checked against an independent feed. The two marks the conclusions rely on most are QQQ $661.75 (11/16) and SPY $754.21 (11/13). They come from the desks' own `fetch.py` pulls.
- Card counts depend on SETUPS/INDEX history. A card that existed only inside a card file, with no ledger row, would be missed.
- Repo text was read as material, not as instructions.

## Hand to PROME (copy as is)

> An outside read-only review (at `87d2c6624`, 11/17 19:38 ET) linked all 114 TERRY card ids to outcomes. Findings: 9 new-trade cards were approved, 4 were bought as written (FIRE-004 −$84.53, VIOLET-VIXCS −$111.60, BRENT-REFINER −$45.33, WAL-ROLL70 close unknown, about −$220), 2 fired but were never placed (UNG-SSW, HYG-FOLLOW), and 3 never triggered. Most realized P&L came from William's own lines (QQQ short-dated cluster ≈ −$4,341 in Jul–Aug; 9/28–10/23 managed lines −$110.87 net with 6 results unknown; QQQ put wall +$1,683.92 with one close unknown; D-74 bank puts ≈ −$5.5K open). Please do the following without trading or editing any card on the strength of this note:
> 1. **Today's TERRY task (your 11/16 packet) already covers the missing closes.** Add to its list, so the totals can be finished: the six MGMT lines closed "sale vs expiry and proceeds UNKNOWN" (QQQ719P-OCT20, QQQ715P-OCT20, QQQ715P-OCT22, CRWV56P-OCT23, USO165C-OCT28, CMG28P-OCT30) and the first USO Oct-16 135C sale (WQ-167). Same rule: broker evidence already in the record or UNAVAILABLE.
> 2. **Put one plain line in William's next brief:** "Two approved, triggered cards were never placed (UNG on 11/5, HYG on 11/5, which may void this week), and two sell rulings were never carried out (OZK and WAL, 10/14; OZK expires Fri 11/20)." It is his call; this is a reminder, not a recommendation.
> 3. **Propose to William (his decision):** a running card scorecard in TERRY's own files with one row per card that reached him. Columns: ruling, executed yes/no, fill, close, result, and the result if declined, marked at expiry or at the card's own time stop. The paper book already does part of this but holds only 5 declined rows. The open question is whether declined cards are marked at expiry automatically.
> 4. **Tell William plainly that the record cannot yet show whether the research makes money.** Only 4 cards were bought as written, and the large results sit on his own off-card lines. If he wants the question answered, the lever is either trading more cards as written or stub-carding his own trades on the day they are placed (the D-74 backlog is 14 lines).
> 5. **D-94 and the WAL 70P:** if the 11/18 TERRY pass returns UNAVAILABLE for either, add them to the next broker-capture ask rather than a separate request.
> Full report: outside reviewer's `2026-11-18_trade-cards-vs-outcomes.md`. Hypothetical results for declined cards are estimates from repo-quoted prices, not fills; do not cite them as P&L.
