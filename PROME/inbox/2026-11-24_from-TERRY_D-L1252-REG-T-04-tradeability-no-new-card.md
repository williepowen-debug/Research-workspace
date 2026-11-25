# TERRY -> PROME: D:L1252 tradeability read on REG-T-04 FIRED — NO NEW CARD; the approved HYG card is the trade · Car-Mart NO CARD

**Row key:** D:L1252 (DOCKET physical line 1252, TERRY leg; LIQUID's leg is separate). **From:** TERRY, Claude Code, Claude Opus 5.5 (claude-opus-5-5), laptop; session terry-desk-agent-2026-11-24; launched by PROME prome-77 on Will's word 22:43 ET. **Written:** 2026-11-24 22:50 EST (`date`). **$0, no order, nothing executed, not pushed (PROME pushes).** Evidence: `AGENTS/TERRY/research/2026-11-24_reg-t-04-fired-tradeability/NOTE.md`.

## For Will, in plain words

**Answer: no new trade. The trade for this signal is the one you already approved.** That is the small junk-bond protection on HYG: a January put spread, 5 contracts, at most $0.60 each, so at most $306.50 can be lost. It was built on 11/5 for exactly this case, junk-bond spreads widening after the stock selloff. Its trigger fired then, and the credit alarm that completed tonight confirms the same idea. Your approval stands to Fri 12/4. Whether you hold it is unknown to me: no HYG line appears in your 11/18 capture. I am stating where it stands, not prompting you.

**Why I am not adding a second credit trade:**
- **It would be the same bet twice.** The October version of this trade (77/74 put spread ×4, max loss $405.20) was keyed to exactly tonight's alarm. It lapsed on 11/13 because the alarm came ten days late. Bringing it back would put **$711.70 on one idea**, 1.4 times your $500-per-idea default, while the X1 sizing gate is closed. That would be your choice to make; I do not recommend it.
- **The alarm adds confirmation, not a new channel.** Banks are not joining in (REGINALD: bank preferred shares up 0.61%, investment-grade spreads up only 0.04 points). The third day of the three was a narrowing, 3.76 to 3.63 points. Stock-market fear has fallen by a quarter (VIX 35.89 to 26.36). Nobody has yet shown that new bond deals are being pulled; that check is LIQUID's and is still pending.
- **The price has already moved.** The approved spread was about $0.44–0.53 earlier in November. Tonight's after-hours screen puts it near $0.52–0.56, close to the $0.60 cap. If the cap is above the market at the open, the order simply does not fill, and the cap stays where it is.

**Dollar risk:** $306.50 at most on the existing approved card, if it is entered at the cap. Nothing new.

**Caveats that could change your decision:**
- ⚠️ **Prices are after-hours screens, not fill prices.** The market closed hours ago. After-hours option bids fall apart (one leg shows a $0.01 bid), so tonight's numbers are a rough guide only. Any order must be priced on your broker's live chain (root rule #4).
- ⚠️ **Thanksgiving week is thin.** Wed 11/25 is a full session, Thu 11/26 is closed, Fri 11/27 closes early. Seven sessions remain before the approval runs out on 12/4, and prices can be wider than normal on the short days.
- ⚠️ **Big buyers are in these exact options.** Open interest in the two strikes is up about 129,000 and 107,000 contracts since 11/5 (vendor figure, not broker-checked). The market is deep, but the protection is no longer cheap or unowned.
- ⚠️ **The base rate is against the payoff.** In 14 earlier episodes like this one, HYG usually dipped and recovered; it ended down 1.4% or more in only 4. The spread loses money unless HYG falls below about $75.39 (it closed $76.43, so about 1.4% lower) before you sell it.
- ⚠️ **Day colour.** Tuesday was a red day for HYG. Your 11/9 waiver (WQ-663 B) lets this one card enter on any day; that waiver covers no other card.
- **My forward view (unscored, my judgment):** about 1 in 4 that the spread is worth more than you paid at some point before its 1/8 sell date. The most likely path is junk spreads holding at 3.3–3.8 points into the Fed meeting on 12/9 while the spread slowly loses value. What pays is an Optimum default (its grace period ends about 12/16) or Nvidia's late quarterly report (about 12/4) restarting the selloff.

**Car-Mart (BROCK's ask): no trade.** The stock closed at $0.33 after the bankruptcy filing. The plan leaves shareholders about $0.30 a share, so there is almost nothing left to gain from betting against it, and a very large loss if it squeezes. No options are listed on my data feed, so no limited-loss trade exists. BROCK reads it as one company's failure, not a wider auto-loan break.

**What I could not check:** the broker chain (markets closed); the 11/24 junk-spread figure (posts Wednesday morning); LIQUID's read on whether new deals are being pulled; the December VIX future's 11/24 settlement; whether you hold the HYG spread.

## Detail (dense)

| Item | Disposition |
|---|---|
| **REG-T-04 fire** | Verified: HY OAS first-published 352 · 376 · 363 [11/19, 11/20, 11/23], 11/24 not posted (`fetch.py fred --first-published`, 22:45 EST). **NO NEW CARD.** Expression = `IDEA-HYG-FOLLOW-NOV05` (GATE-TERRY-HYG-FOLLOW-01): APPROVED FIRED, fill UNKNOWN, reason UNRESOLVED; void run 0 of 5; window to 12/04, 7 sessions. Screen 22:46 EST after-hours: 76P 0.64/0.90 (last 0.69 13:38) · 73P 0.01/0.41 (last 0.17 15:50) ⇒ mid $0.56, last-trade $0.52, outer $0.89 not real; cap $0.60 unchanged. HYG $76.43 −0.12% [11/24], 60-bar low 76.33 [11/20]. Trigger-state block written on the card. |
| Successor to lapsed `IDEA-CREDIT-HYG-BDC-OCT23` | Not proposed: N_eff 1 with the ×5; pair $711.70 vs $500 default, X1 CLOSED; bank leg absent; 77/74 mid $0.87 / last-trade $1.09 vs old $1.00 limit. Shown as Will's choice only. |
| VIOLET vol leg | NOT-FIRED, no card: HY ≥ 370 trigger unmet on 11/23 (363), 11/24 pending. Reference: VIX Dec-16 30/40C ×5 outer $0.89 → max loss $451.50; same falsifier as the HYG card. Built live only if a cell ≥ 370 prints. |
| Bank leg | NO CARD (REGINALD BANK-ABSENT). |
| `TRY-NOTRADE-REGT04-NOV24` | SETUPS row written. Changes on LIQUID deals-pulled evidence, the bank leg joining, or HY ≥ 390 with CCC leading. |
| **Car-Mart** `TRY-NOTRADE-CRMT-NOV24` | NO CARD: $0.33 [11/24], 0 option expiries on the feed, about $0.03 above BROCK's plan-value estimate (INFERRED); idiosyncratic per BROCK. Packet read only; BROCK's records untouched. |
| Root rule #6 | No new card, so no break. The ×5 card's waiver (WQ-663 B) is unchanged. |
| ⛔ USER.md § No expiry nagging | Followed: no held-position reminders or sell-or-roll content. |

Inbox drain (items 3): reported in a second packet after this one is committed.

## COMPLETION — TERRY — 2026-11-24
STATUS: ✅ DONE (item 1 and item 2; item 3 follows in a second packet)
CHANGED: AGENTS/TERRY/research/2026-11-24_reg-t-04-fired-tradeability/NOTE.md, AGENTS/TERRY/setups/HYG_jan15-76-73P_credit-follows-hedge_2026-11-05.md (trigger-state block), AGENTS/TERRY/SETUPS.tsv (2 NO TRADE rows + HYG note), this packet
RESULT: REG-T-04 FIRED (HY 352/376/363) verified at FRED; NO NEW CARD. The approved HYG 76/73P ×5 card ($306.50 max loss, window to 12/04, fill UNKNOWN) is the expression and screens at a mid of $0.56 against its $0.60 cap. A second credit card would put $711.70 on one view and is declined. VIX leg NOT-FIRED (363 < 370). Car-Mart: NO CARD ($0.33, no listed options).
GAPS: Broker chain unavailable (markets closed; after-hours screens only); the HY 11/24 cell is unposted; LIQUID's issuance read is pending; the VX Z6 11/24 settle is unread.
WILL_NEEDS: None new. The HYG card's order, if any, is Will's hand on a live broker quote by 12/04 (root rule #5); not a prompt.
FOLLOW-UP: Re-read at LIQUID's issuance return or at an HY cell ≥ 370 (VIX leg) or ≥ 390 (second credit card).
