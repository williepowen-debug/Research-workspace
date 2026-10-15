# CHALLENGE: the bank-put book after the OZK extension (CHG-RED-054)

> ⚠️ **ID CORRECTED at closeout 2026-10-14:** first issued as **CHG-RED-052**, an ID already held by a 2026-09-10 challenge (PROME/KERNEL L247), and 053 was also taken. TERRY's cards, PROME's WQ-425/DOCKET records and RED's dated records written tonight cite "CHG-RED-052" for **this** challenge; read them as **CHG-RED-054**. The 9/10 CHG-RED-052 is unchanged.

**Written:** 2026-10-14 ~20:35 EDT (S52, on Will's request: "go ahead with #2"). **RED makes no trade.** TERRY builds trades (root CLAUDE.md), and Will approves under root rule #5. This is the strongest honest case **against** holding, set beside the strongest case **for** holding.

**Live inputs:** option quotes from Yahoo option chains, pulled 2026-10-14 ~20:28 ET (last trades as stamped; the market is closed, so these are indications, not executable prices). Stock closes come from the RED boot tape (10/14). Positions come from the FORGE broker mirror (received 10/14; capture time UNKNOWN); position truth is off-repo. History: daily adjusted closes 2016-01-04 → 2026-10-13. "Base rate" = the share of past windows of the same length in which the stock fell at least as far as the put needs.

---

## 1. The book, measured

| Line | Qty | Cost | Bid / ask [10/14] | Breakeven at expiry | Move needed | Hist. base rate, 5y (ex-2023 crisis) | Option-implied P(below strike) |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **OZK Nov-20 $40P** | 4 | $322.65 | **$0.30 / $0.50** | $39.19 | **−12.8% in 26 sessions** | **7.9% (6.5%)** | **18.4%** (IV 39% vs 1-mo realized 26%) |
| WAL Dec-18 $65P | 4 | $682.65 | $1.70 / $2.25 | $63.29 | −12.4% in 45 | 17.9% (17.3%) | 30.3% (IV 44% vs realized 21%) |
| KRE Nov-27 $67P | 4 | $510.65 | n/a (strike not in feed) | $65.72 | −4.1% in 30 | 31.7% (29.7%) | — |
| KRE Dec-18 $60P | 5 | $878.02 | $0.45 / $0.85 | $57.07 | −16.7% in 45 | 4.8% (2.8%) | 17.9% (IV 34% vs 15%) |
| KRE Dec-31 $65P | 2 | $337.33 | $0.25 / $2.15 | $63.31 | −7.6% in 54 | 16.8% (15.0%) | 35.2% (IV 30% vs 15%) |

Spot [10/14 close]: OZK 44.93 · WAL 72.22 · KRE 68.54.

**What the table says:** every line is priced **above** its own history. ⚠️ *Closeout correction (TERRY, 10/14): the table compares a breakeven base rate with a strike-level implied probability. Like for like, history is ~0.55–0.75× implied on OZK and ~0.70–0.76× on WAL (below strike 22.9% vs 30.3%; below breakeven 17.9% vs ≈25.5%). The direction stands; the size of the gap was overstated.* Implied volatility is 1.5–2.3× realized volatility, so the holder is paying a premium for the tail rather than collecting one. That is normal ahead of bank earnings, and it is also why the marks fall after earnings even with no move (post-earnings volatility drop). The KRE Nov-27 $67P is the best-placed line: it is nearest the money and needs the least move.

## 2. CHALLENGE: OZK Nov-20 $40P ×4 — **STRONG**

**Target:** the case for holding through OZK's Q3 report (release **Tue 10/20 after the close**, call Wed 10/21 08:30 ET, issuer-confirmed per the OZK desk).

**Steelman first, because it is real:** OZK trades at **0.82× book** [Yahoo, 10/14]. It has a **$169.3M nonaccrual** in Boston (10 Prospect), which the OZK desk calls the largest remaining named potential loss event. The RaDD extension's **$121.3M paydown may be re-drawn**, and how much loss it recognizes is UNKNOWN. HY spreads are **4bp** from RED's FT-02 line, and CCC sits at **1,267**. The bank leg can still move with macro credit. And at $0.30–0.50 the line is now a **cheap** tail: $120–200 for four contracts.

**Counter-evidence:**
1. **The catalyst the line was built around is gone.** The near-term event that made OZK puts make sense was a maturity failure on its largest San Diego construction loan. OZK's 8-K (10/12) says that loan was **extended to Dec 2029 with $100M of fresh capital**. RED's own docket wrote "Executed multi-year extension + recap → OZK-09 FALSE immediately" as the bull signal on this event, and two of its legs are now met. The pass-rating and loss legs are still open.
2. **The desk that owns OZK agrees.** OZK's post-extension review (10/12): *"no compelling, specific near-term downside opportunity"* and *"There is no date-certain RaDD default catalyst left in the November-put horizon."*
3. **The earnings print cannot do it alone.** The line needs −12.8%. TERRY's measured regional-bank earnings envelope is a median of 2–3%, with **0 of 32 moves ≥10%** (`RISK_RULES.md` #18). OZK's own largest earnings-window move in eight quarters was **+9.7%** (Jan 2025). The OZK desk's playbook prices an executed extension (Scenario A) at a **0 to +5%** stock reaction, and short interest is **~16% of float** [9/15], which is squeeze fuel if the print is clean.
4. ~~**History prices the payoff at less than half what you are paying.** −12.8% in 26 sessions happened in **7.9%** of 5-year windows (**6.5%** without the 2023 bank crisis). The option is priced for **18.4%**.~~ **CORRECTED at closeout on TERRY's basis note (10/14). The line above compared a *breakeven* base rate with a *strike-level* implied probability, which are different events.** Like for like:
   - **Below the $40 strike:** history **12.5%** (RED) / **13.8%** (TERRY) vs implied **18.4%** (RED) / **17.7–19.2%** (TERRY).
   - **Below the $39.19 breakeven:** history **7.9%** (RED) / **9.2%** (TERRY) vs implied **≈14.3%** (RED, same IV) / **13.6–15.1%** (TERRY).
   - ⇒ History runs about **0.55–0.75×** the implied probability, **not "less than half"**.
   - The point survives: the line is priced above its own history, but by less than first stated. Some gap is expected, because implied odds carry a risk premium.
5. **No recorded reason, no exit rule.** It was bought 10/7, Will-direct. TERRY's note says the entry rationale is *"unrecoverable"*. There is no card, harvest rule or stop. TERRY's card deadline of 11/18 falls **after** the only scheduled catalyst.

**Risk if wrong (holding and it fails):** the remaining **$120–200** goes to zero. **Risk if wrong (exiting and the bear case lands):** a gap below $39 forfeits the payoff. Historically that is the ~8% tail.

**Grade: STRONG.** The specific premise has been removed by the issuer, and the owning desk concurs.

**Action (RED's recommendation; the decision is Will's, and the card is TERRY's):** the decision point is **before the 10/20 close**, not 11/18. After the print, the volatility premium comes out of the price even with no move. Under **root rule #7** ("Trimming = thesis broken"), the OZK-specific thesis, a near-term maturity failure, is broken, so closing is consistent with the rule. If the view being held is really **"regional banks broadly"**, that view already lives in the KRE lines. Re-expressing it through OZK adds single-name squeeze risk without adding a separate view. Rolling would need a fresh card and fresh approval (TERRY Non-Negotiable #6: no roll-by-hope). On timing, puts sell for more on red days, so the mirror of **root rule #6** points to a red day for regionals. That call is TERRY's.

## 3. WAL Dec-18 $65P ×4 — **MODERATE**

- **For holding:** the line is 10% out of the money with **65 days** left, so it is past the 10/19 print rather than riding on it. REGINALD's December estimate is **25%** below $65 (range 20–35%). WAL fell 2.05% on 10/14. Its print (Mon 10/19 after close) includes the $99M appraisal question.
- **Against:** REGINALD finds *"no demonstrated put-pricing advantage"*: his 25% sits below the ~30% the option implies. The WAL desk itself recommends *"bringing TERRY's Fidelity 65P management review forward before earnings"*, because time decay plus the post-earnings volatility drop can offset a favourable move. And the stock has to fall 12.4% to reach breakeven: 17.9% of 5-year windows.
- **Grade MODERATE:** no edge, but the premise is not broken. **Ask:** pull the 12/16 card review forward to **before 10/19**, as the WAL desk asks.

## 4. KRE lines — **WEAK** challenge on the Nov-27 $67P; **MODERATE** on the Dec-18 $60P

- **Nov-27 $67P:** needs only −4.1%, which happened in ~32% of history. It is the line most aligned with what the evidence actually shows: broad, rate-driven weakness (165 of 167 banks down 9/11→10/9, REGINALD). RED has no strong case against it. Its one gap is ownership: no card exists (FORGE D-77).
- **Dec-18 $60P ×5:** needs −16.7%, which happened in 4.8% of history (2.8% without 2023). It is now a lottery ticket worth ~$225–425, and it has **no card**. Will's standing practice is to sell or roll before expiry. That needs a date written down now, not in December.
- **Dec-31 $65P ×2:** it has a time stop (12/31 15:00), and RED raises no new challenge.

## 5. The book as one bet (the point that matters most)

All **21 bank-put contracts are one view** (TERRY: *"six contract lines are not six independent views"*; effective count 1). They pay together only if **credit breaks into bank funding or bank credit**, and so far the desks find the opposite:
- **Basket study (REGINALD 10/12):** *"Rate contribution plausible, credit cause unproved."*
- **Securities screen (REGINALD 10/13):** no hidden-loss cliff in 14 banks.
- **Large banks' Q3:** charge-offs falling (BAC 0.44% vs 0.47%).
- **Funding stress:** LIQUID's funding-stress check was 0 of 3 through 10/13.

**What would flip this challenge against RED:** an FT-02 fire (HY >320 for three days running) **with** funding joining (LIQ-07 S1 on 10/16), or an OZK Q3 that books a large loss on Boston or RaDD. If either lands before 10/20, the OZK grade drops to MODERATE.

## Sources

FORGE/STATUS.md (10/14 broker mirror) · Yahoo option chains and price history (pulled 10/14 20:28 ET) · BOARD/SIG-W-20261012-005 (OZK 8-K Item 7.01) · AGENTS/OZK/research/threads/2026-10-12_POST_EXTENSION_REVIEW.md (lines 5, 51) · …/2026-10-08_BAND_FIRE_CAUSE_RADD_STOPGAP.md:78 · AGENTS/OZK/STATUS.md (short interest, 9/15 FINRA) · AGENTS/TERRY/RISK_RULES.md:137 (#18) · AGENTS/TERRY/setups/WAL65P-OZK40P_new-fidelity-lines_note_2026-10-07.md · AGENTS/TERRY/research/2026-10-13_future-trade-construction.md · AGENTS/REGINALD/reports/2026-10-14_WAL_December_outcome_probabilities.md (line 3) · AGENTS/WAL/research/2026-10-14_relative-weakness-interpretation.json · AGENTS/REGINALD/research/market-technicals/studies/2026-10-12_KRE_whole_basket_study.md · AGENTS/REGINALD/reports/2026-10-13_bounded-securities-funding-screen.md. The quotes in §2–§4 from OZK (lines 5/51/78), TERRY (#18) and REGINALD (line 3) were **checked at the artifact by RED**; the rest were relayed by a read-only evidence agent.


## Disposition (closeout, 2026-10-14)

**WQ-425 RULED B** by Will at 20:49 ET in PROME's session (*"Approve 425, spawn TERRY for the OZK and WAL cards"*). TERRY wrote two cards:
- **`MGMT-OZK40P-NOV20`:** recommends **SELL ×4 before the Tue 10/20 print**, with no roll. RED's flip conditions are on the card as F1/F2.
- **`MGMT-WAL65P-DEC18`:** **leans SELL ×4 before the Mon 10/19 print**, with HOLD priced as the alternative.

The KRE Dec-18 $60P date ask was outside TERRY's commission and has been flagged to PROME. **Orders are Will's**; RED records them and does not grade fills.
