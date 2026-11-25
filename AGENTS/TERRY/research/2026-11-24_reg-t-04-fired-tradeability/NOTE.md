# REG-T-04 FIRED — tradeability read (D:L1252) · Car-Mart · inbox drain

**Written:** 2026-11-24 22:4x–23:xx EST (stamps from `date`), TERRY, Claude Code, Claude Opus 5.5 (claude-opus-5-5), laptop; session terry-desk-agent-2026-11-24; launched by PROME prome-77 on Will's word 22:43 ET ("wake TERRY now for the tradeability read"). **NO ORDER. $0. No new card.**

⚠️ **Every market figure below is after the 11/24 close.** Spot and ETF figures are the 11/24 regular-session closes (vendor, `fetch.py price`, read 22:45 EST). Option figures are the vendor's after-hours chain (`chain_fetch.py --no-cache`, fetched 22:46 EST; last option trades 13:38–15:59 ET): **screening marks, not fill prices** (durable finding 5b). After-hours bids on out-of-the-money strikes collapse (HYG 73P bid $0.01), so the outer debit is not a real price tonight. Everything must be re-priced on the broker chain in the session before any order (root rule #4).

## §1 Verified at the artifact

| Fact | Figure | Source, time |
|---|---|---|
| HY OAS first-published | 347 [11/18] · 352 [11/19] · 376 [11/20] · 363 [11/23]; 11/24 cell not posted | `fetch.py fred BAMLH0A0HYM2 --first-published`, 22:45 EST (my pull shows 11/18 as 347; REGINALD's table agrees) |
| REG-T-04 letter | > 350 on 3 consecutive first-published closes → FIRED on the 11/23 close | REGINALD memo, D:L1235 |
| HYG closes | 77.51 [11/9] · 76.65 [11/18] · 76.53 · 76.33 · 76.52 · **76.43 [11/24], −0.12%** | yfinance history, 22:4x EST; 60-bar closing low 76.33 [11/20] |
| Day colour 11/24 | RED: SPY $718.78 −0.49%, HYG −0.12%, KRE +0.32% | `fetch.py price`, 22:45 EST |
| VIX / VIX3M | 26.36 / 25.47 (ratio 0.966, still inverted) [11/24 close] | `fetch.py price`, 22:45 EST |
| HYG card state | APPROVED FIRED; fill UNKNOWN, reason UNRESOLVED; approval standing, GATES APPROVED, UNFILLED, window to 12/04 | card `setups/HYG_jan15-76-73P_credit-follows-hedge_2026-11-05.md`; `PROME/GATES.tsv` GATE-TERRY-HYG-FOLLOW-01 |
| HYG in the FORGE mirror | no HYG row | `FORGE/STATUS.md`, Fidelity capture 11/18 — six days old, not truth |
| X1 | CLOSED — DON'T-SIZE | `PROME/STATUS.md` § Restrictions |

HYG moved −1.39% from 11/9 to 11/24 while HY OAS widened about 29 bp (334 → 363). The rate leg is cushioning it (card §6). A 29 bp widening has not yet reached the card's $75.39 breakeven.

## §2 The answer: NO NEW CARD. The trade for this fire already exists and is approved.

**Relation to the existing idea.** `IDEA-HYG-FOLLOW-NOV05` (HYG Jan-15-2027 76/73 put spread ×5, limit ≤ $0.60, max loss $306.50) was built for this exact branch, credit following the equity selloff. Its trigger (HY > 344 on one close) fired on 348 [11/5]. REG-T-04 is the stronger version of the same premise. It confirms the premise and changes no term of the card. Void line (HY ≤ 330 on 5 consecutive closes before entry): run 0 (363 is the last cell). Window: through Fri 12/04. Seven sessions remain (11/25, 11/27 short, 11/30, 12/1–12/4). Whether Will holds it is UNKNOWN (no HYG row at the 11/18 capture). This is a statement of the card's state, not a prompt.

**Tonight's screen against the card's $0.60 cap** (after-hours, screening only):

| Leg | Bid / ask | Last (time ET) | OI (vendor) | Vol 11/24 |
|---|---|---|---|---|
| 76P | 0.64 / 0.90 | 0.69 (13:38) | 322,026 (193,230 on 11/5) | 7,502 |
| 73P | 0.01 / 0.41 | 0.17 (15:50) | 190,611 (83,688 on 11/5) | 7,209 |

Mid to mid **$0.56**; last trades, not simultaneous, **$0.52**; after-hours outer $0.89, not a real price. On 11/18 the outer was $0.52 and the mid $0.46. **The spread now prices close to the $0.60 cap, and it may be above it at the open.** If it is, the card does not fill. That is a valid outcome under its own §8, and the cap is not raised. ⚠️ Open interest in these two exact strikes has risen by about 129,000 and 107,000 contracts since 11/5: someone large holds this spread. That means the market is deep, and also that the protection is no longer cheap or unowned. It is vendor OI and I have not checked it with the broker.

**Why not a second credit card (the successor to the lapsed REG-T-04 card):**
1. **Same idea, same thing that kills it.** `IDEA-CREDIT-HYG-BDC-OCT23` (HYG Jan-15 77/74P ×4, ≤ $1.00, max loss $405.20, approved NOT-FIRED under WQ-513 A) was keyed to exactly this fire. It lapsed unfired at the 11/13 close because REG-T-04 came 10 days late. A revival is a new card and needs Will's word. Together with the ×5 it puts **$711.70 on one view**, 1.4× the $500 default, with X1 CLOSED. The ×5 card's own §0 said that second step needs Will's word "at that moment". This is that moment, and the ×4 card no longer exists.
2. **The fire adds confirmation, not a new channel.** Banks are absent (REGINALD: preferred basket +0.61%, IG +4 bp, KRE in line). The third close was a narrowing, 376 → 363. VIX fell 35.89 → 26.36 [11/20 → 11/24]. Nothing yet shows that new issues are shut; that is LIQUID's pending read. My own 11/23 NO TRADE row (`TRY-NOTRADE-HY376-NOV23`) said the read changes on "REG-T-04 completing with bank credit joining". REG-T-04 completed, but bank credit did not join.
3. **The price has moved against a new entry.** The 77/74 now screens at a mid of $0.87, with last trades $1.09 apart (77P traded 14 contracts), against its old $1.00 limit. Entering after the fire pays for the move already made.
4. **Base rate (`research/2026-11-05_selloff-read/NOTE.md`).** After SPY falls 3% or more while HYG holds, HYG touched −3% within 48 sessions in 10 of 14 episodes, but finished ≤ −1.4% in only 4 of 14. It dips and recovers. A second spread doubles the bet on the less common path.

**If Will wants more credit exposure anyway (his choice; I do not recommend it).** HYG Jan-15 77/74P ×4 at a limit ≤ $1.00: max loss $405.20, or $711.70 together with the ×5. It needs his X1 choice on this card and a green HYG day, or a written root-rule-#6 break test, which I have not run for it. Re-price on the broker first.

**Vol leg (VIOLET 11/23): NOT-FIRED, no card built.** VIOLET's dated trigger was HY ≥ 370 on the 11/23 or 11/24 cell. The 11/23 cell is 363, not met. The 11/24 cell posts Wed 11/25 about 10:00 ET. Reference screen: VIX Dec-16 30/40 call spread, 30C 1.50/1.64 · 40C 0.75/0.86 (after-hours) ⇒ outer $0.89, mid $0.77. ×5 at the outer is $445 plus $6.50 fees = **$451.50 max loss**. It settles on the December VIX future (24.08 settle 11/23 per VIOLET; the 11/24 settle is unread), so breakeven is about 30.9, +28%. Reasons it is not a card: the trigger is unmet; VIOLET leans fade at 60–65%; it pays on the same "second leg" branch as the HYG card, so the two count as one view; and the desk's only realised loss was a VIX call spread on a fading vol path (`TRY-VIOLET-VIXCS`, −$111.60). If the 11/24 cell prints ≥ 370, TERRY builds it live on a red day (root rule #6: calls on red days).

**Bank leg:** REGINALD offers no candidate card (BANK-ABSENT). NO CARD.

**Forward view (mine, unscored, nothing registered).** About 1 in 4 that the ×5 spread, if entered at ≤ $0.60, is worth more than its debit at any point before its 1/8 time stop. That needs HYG ≤ about $75.4, roughly HY above 400 with rates flat. The most likely path (about 60%, consistent with REGINALD's 60/40) is that HY stays between 330 and 380 into the FOMC (12/9) and the spread bleeds. The alternative that pays is an Optimum default (grace ends about 12/16) or the Nvidia 10-Q (about 12/04) re-widening CCC first. **What would change my mind toward a second card:** LIQUID showing deals pulled, the bank leg joining (REGINALD's flip data), or HY ≥ 390 with CCC leading.

## §3 Car-Mart (BROCK 11/24): NO CARD

| Check | Read |
|---|---|
| Price | CRMT $0.33, −53.52%, 10,956,700 sh [11/24 close, `fetch.py`, 22:5x EST] |
| Options | **0 listed expiries on the vendor feed** (`chain_fetch.py CRMT`) — no defined-risk structure exists |
| Value left to short | BROCK: equity gets $2.5M plus any residual ≈ $0.30/sh on about 8.26M shares (INFERRED) — the stock already trades at about plan value: about $0.03 of downside to the stated recovery against unbounded squeeze risk on a sub-$1 short with borrow unknown |
| Read-through | BROCK: idiosyncratic (revolver terminated 10/2025, units −81.9% YoY, 2025 restatement); lenders private (Silver Point, Beach Point); ACMAT trusts not debtors; no bonds in HYG (REGINALD rider) |
| Verdict | **NO CARD.** No instrument with a defined loss exists, and short equity has the payoff the wrong way round. Broad subprime auto is OTTO's question; a card needs an OTTO direction and a listed vehicle. Changes on: an ACMAT servicer termination, a missed 12/3 rollover, or a listed lender or ABS holder named. |

## §4 Inbox drain: all 15 packets, every sender (written after §2–§3 were delivered in c91c3beab8)

| Packet | Disposition |
|---|---|
| REGINALD 11/24 REG-T-04 ask · VIOLET 11/23 | §2 (D:L1252). |
| BROCK 11/24 Car-Mart | §3. BROCK's records not touched. |
| CORAL 11/23 flood sweep **+ CORAL CORRECTION** (read together) | NO CARD (CORAL: no supported implication). The correction applies: the uninsured share of the flood loss is a HYPOTHESIS, the line excluding the flood as a cause of insurer stock moves is withdrawn, and USCB's $66.252M is a "Condo commercial" category, not an association book. TERRY carried none of the corrected sentences (grep over TERRY files outside the inbox: 0 hits). The "would create one" lines (a named association assessment, a Citizens forced-flood count that moves policies to UVE or HCI, which is UNESTABLISHED) are not triggers I can key a card to. |
| CREED 11/23 CRE (+ 17:23 correction) | NO CARD. Estates at Palm Bay is Okaloosa, not Brevard; Seacoast is the most concentrated bank, not the only one. Changes on a SE-coast urban flood plus a declaration and an exposure screen, or a REIT disclosing an uninsured loss above its deductible. |
| HOMER 11/23 home values (+ in-place correction) · **HOMER 11/24 correction** | NO CARD. A declaration is now REPORTED for Brevard (FEMA data blank at 03:40Z 11/25; WALTER SIG-W-20261124-019 says six counties). It changes the timing of FHA foreclosures, not values. HOMER's housing-volume read (NAR pending 63.0, −16.7% YoY) has no ticker and no direction: no owner direction, no card. |
| REGINALD 11/23 flood banks (+ correction) | NO CARD (REGINALD: about 80% no nameable Q4 credit effect). Changes on a named flood provision or deferral programme (Seacoast most likely). |
| AEOLUS 11/23 ×3 | NO CARD. FL/CA winter flood: no vehicle. Memphis: the 11/23 15:35Z table replaces the 11/22 one on `TRY-NOTRADE-MISSRIVER-NOV23` (−6.9 ft 12/10, −7.8 ft 12/21). Panama: 55% chance of a 47 ft limit by 4/30; no vehicle named. |
| HANS 11/23 TTF | NO CARD. L3 closed then about €91. Still no listed liquid TTF vehicle (11/20 note). Changes on a named-front close over €100 with a vehicle. |
| VULCAN 11/23 Nvidia 8-K | NO CARD (11/23: the +33% gap was a chase). The dated leg is the 10-Q, deadline about 12/04 (12/09 with a 12b-25). An NT 10-Q or an Item 4.02 is what would re-open it. |
| PROME 11/23 WQ-730 RULED | **DONE.** Stage two marked RETIRED on `PAPER_BOOK_DESIGN.md` (header and §Phase 2). `scripts/paper_book_mark.py` no longer prints the three counters (selftest PASS). The function is kept; ledger rows are not rewritten; the July figures stay as history in the 11/23 note. |

Small items logged (WQ-622): REG-T-04 member plus counterevidence on `COMBO-CREDIT-FOLLOWING` (SIGNALS.tsv). BOARD: SIG-W-20261124-001 (late FLASH, VIX over 30 premarket) logged `noted`.

## §5 Re-read at LIQUID's and HENRY's return (PROME follow-up, written 2026-11-24 23:4x EST)

**Will's question (PROME's relay, 23:12 ET):** what is the high-yield spread leading to downstream? On LIQUID's and HENRY's evidence, **so far it leads to AI-infrastructure financing, not to broad stocks or banks.** LIQUID: not a freeze, selective (mainstream HY and IG cleared 11/16–11/20; refusals sit in AI-infrastructure and CCC; CoreWeave 5Y CDS about 1,314 bp [11/24]). HENRY: RSP $213.96 is flat since 9/21 while HY is +97 bp; the fall is the chip complex.

| Question | Answer |
|---|---|
| **1. AI-infrastructure credit card** | **NOT-FIRED card written: `IDEA-CRWV-AIFIN-NOV24`**, CRWV Feb-19-2027 40/30P ×1, limit ≤ $3.25, **max loss $326.30**. T1: CRWV green close ≥ $48.00 AND LIQUID CDS ≥ 1,200 bp, by 12/11. Screen mid $4.03 [11/24 after hours] > cap: no entry today by design. **A different bet from the HYG card, with correlated but distinct falsifiers** (HY ≤ 330 ×5 kills HYG; CoreWeave's loan clearing kills CRWV). Pair $632.80. X1 CLOSED: needs Will's choice. Root rule #6: green-day entry built in, no break. CoreWeave earnings date NOT VERIFIED (blocks entry until read at IR). Nvidia card stays DEAD. |
| **2. HENRY's two clocks vs the HYG card** | **The HYG card stays the broad-credit expression, but HENRY narrows what it is:** a bet on the 30% broadening branch, not on "credit stress" in general. HENRY's HYG marker ($75.50) sits at the card's $75.39 breakeven, so the card only pays once broadening is visible. **No pre-built broadening card:** an RSP, IWM or KRE put spread keyed to HENRY's markers pays on the same branch as the HYG card (N_eff 1 with it) at equity vol instead of credit vol. Re-read live if two of HENRY's three markers print (HY > 376 on an RSP-down day, KRE < $65, HYG < $75.50). |
| **3. Dated catalysts as triggers** | **No separate cards.** Nvidia 10-Q about 12/04: date not IR-verified (RISK_RULES § Option-Specific forbids keying to it); the Nvidia card is DEAD; it sits inside the CRWV window as event risk. FOMC 12/9: a rates event (HEN-63, BOND/HENRY); no credit edge. Optimum grace about 12/16: idiosyncratic, and a default can tighten the index by rebalance (REGINALD), so a card keyed to it could be paid by bookkeeping. LIQUID's freeze-test week 11/30–12/4: used as the CRWV card's window, not a card of its own. |

**New packets since the 22:55 closeout:** CORAL 11/24 (declaration reported: IA in Brevard, Indian River, Martin, Okeechobee, Palm Beach, St. Lucie; not Seminole or Volusia; no implication) and HOMER 11/24 (same counties; no implication). Both NO CARD. My 11/24 sentence ("delays some foreclosures, not values") HOLDS per CORAL, narrowly.
