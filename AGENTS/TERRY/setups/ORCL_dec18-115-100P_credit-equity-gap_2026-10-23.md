# TRADE IDEA — ORCL Dec-18 115/100 put spread — Oracle's equity has not followed its credit
**Date:** 2026-10-23 (written 19:0x ET from `date`)
**Setup ID:** `IDEA-ORCL-PUTSPREAD-OCT23`
**Terry verdict:** CONDITIONAL — NOT-FIRED; unapproved proposal. Nothing is approved in advance.
**Confidence in trade structure:** Medium (liquid chain; the trigger reads a credit series this desk does not own)
**Commission:** WQ-499 RULED APPROVE A, Will 2026-10-23 13:38 ET in PROME's window (PROME packet `inbox/2026-10-23_from-PROME_WQ499-WQ509-RULED-two-NOT-FIRED-cards.md`). Preparation only; root rule #5 — the order is Will's.
**Thesis owner (evidence, not TERRY's):** PROME ELLISON theme, `PROME/themes/ellison/reports/2026-10-22_sweep/00-SYNTHESIS.md` § 5 (as relayed in the packet): 5Y CDS **314 bp [10/22, DTCC]** against an S&P **BBB−** rating; 30-day IV ~59.5%, flat skew, put/call 0.71; FCF ≈ −$28.7B over four quarters, $125B debt, $288B of leases off balance sheet, about half of the $664B backlog is OpenAI; Jupiter force majeure 9/24. Oracle is investment grade, so this is an **idiosyncratic credit/equity-gap card, not a credit-cycle card** (outside DEWEY's HY figures).
**Data freshness:** spot = 10/23 close **$126.16** (+0.49%, green; snapshot 18:54 ET). Chain pulled 18:56 ET after the close; quotes are two-sided and tight, but vendor marks are SCREENING marks (durable finding 5b): the order is priced on the broker chain.

## 0. Missing inputs / hard caveats
- [x] Live price checked (10/23 close) · [x] chain checked (after-hours screen) · [ ] broker quote at entry
- [x] Position truth: no ORCL line in the book (FORGE 10/22 capture + 10/23 activity)
- [ ] **Oracle's fiscal Q2 report date UNVERIFIED** (historically the second week of December; a company IR or 8-K check is owed before any order — root canon: earnings dates come from IR, never memory). The time stop below sits before that window
- [ ] The CDS trigger reads a series TERRY does not own or pull; its reading comes from the ELLISON theme (PROME) at its stated source

## 1. One-line setup
If Oracle's credit keeps widening while the stock holds, buy a defined-risk Dec-18 put spread on a green day, so the equity catching down to the credit pays, and the loss is capped if it never does.

## 2. Trigger state, in figures (NOT-FIRED)
| Leg | Line | State at 10/23 | Status |
|---|---|---|---|
| **T1 — credit leads** | ORCL 5Y CDS **≥ 350 bp** (ELLISON theme reading, DTCC basis) | 314 bp [10/22] | **NOT FIRED** (36 bp away) |
| **T2 — equity has not followed** | ORCL **≥ $120.00** at the T1 reading | $126.16 | MET today; re-read at T1 |
| Entry window | first **green ORCL session** after T1 (root rule #6), through Fri 2026-11-20 | — | waits on T1 |
| **Void before entry** | CDS ≤ 280 bp, or ORCL closes ≥ $145.00, or no green day by 11/20 | — | — |

**Why a credit trigger, not a price line:** the thesis is the gap between credit (junk-like 314 bp on a BBB− name) and the equity. A price-break trigger (e.g. a close under $120) would fire after the equity has already moved and would raise the debit past the chase line; a credit trigger fires while the gap is widening. **Construction rule #15 check:** this gate opens on the thesis variable worsening, not on decay, so a fire is information about the thesis, not against it.

## 3. Chart / tape read (10/23 close)
| Item | Read |
|---|---|
| Price | **$126.16**, 30-day **−12.55%**, near its 30-day low (range 125.54–150.04) |
| Vol | Dec puts **61–66% IV**; 115P 62.4%, 100P 65.6% (the wing is a little richer — the spread sells it) |
| Liquidity | Dec 115P OI 13,518 (7.20 ask) · 100P OI 10,705 (2.81 bid); bid-ask 2–8% of mark |
| Dated events in the window | FOMC 10/28 · mega-cap prints 10/28–29 (MSFT/GOOGL/AMZN capex, OpenAI exposure) · ELLISON theme checkpoint 10/29 (DOCKET L811) · Oracle FQ2 (date unverified) |

## 4. Structure
| Item | Figure (18:56 ET screen) |
|---|---|
| Instrument | **ORCL Dec-18-2026 115P long / 100P short, ×1**, one complex order, never legged |
| Debit | worst (ask − bid) **$4.39**; mid 7.08 − 2.93 = $4.15 |
| Order | net debit limit **≤ $4.40** |
| **Max loss** | **$441.30** = $440.00 + $1.30 fees (0.65/contract/side, budget arithmetic) — inside the $500 default |
| Max gain | $1,500 − $441.30 = **$1,058.70** at ORCL ≤ $100 on 12/18 |
| Breakeven at expiry | **$110.60** (−12.3% from $126.16) |
| Payoff ratio | **2.40 : 1** |
| DTE at 10/23 | 56 days |
| **Do not chase** | net debit **> $5.00** (33% of width), or ORCL **< $112** at entry (breakeven mostly gone) |
| Alternative | **Nov-20 115/100P ×1**: worst 3.75 − 0.88 = $2.87 ⇒ max loss **$288.30**, max gain $1,211.70, breakeven $112.13, ratio 4.2 : 1 — cheaper and covers the 10/28–29 catalysts, but only 28 days for a view PROME frames as 1–3 months (construction rule #16) |

**Why this expression:** an outright Dec 115P costs ~$7.20 ($720, over the default) at ~62% IV; the spread sells the richer 100 wing and caps the loss at $441. Dec gives the gap time to close (credit repricing runs over weeks). Strikes 9–21% below spot match a credit-event move, not an ordinary drift.

## 5. Effective-N (RISK_SCORING §2b)
| Field | Entry |
|---|---|
| N_claimed | 5: CDS vs rating gap · negative FCF · off-balance-sheet leases · OpenAI backlog concentration · Jupiter force majeure |
| Shared antecedent | OpenAI / AI-capex financing: one event (OpenAI's funding or contract renegotiation) moves four of the five |
| **N_eff** | **≈ 1.3 → sized as ONE view** |
| Book overlap | the Nasdaq-downside bet (QQQ Oct-26 710P ×1 + 705P ×2 + Nov-20 690/670P ×2) and APO Dec-18 95P share the AI-capex-repricing antecedent; CRWV Oct-23 56P expired today (disposition unknown). Combined AI-financing downside is far larger than this card's $441 — one theme, several lines |

## 6. Management (written before any fill)
- **Harvest (durable finding 9):** sell when the spread marks **≥ $10.00** on the broker bid (≈ 2.3× the debit, 67% of width).
- **Kill:** ORCL closes ≥ $145.00 on two consecutive sessions, or CDS ≤ 280 bp → sell at the bid.
- **Time stop:** sell by the close **Fri 2026-12-04** if neither has fired (ahead of the unverified FQ2 window; holding through it is a separate Will choice once the date is verified). No roll pre-registered (Non-Negotiable #6).
- Forward max loss after a fill is the remaining mark (construction rule #20(d)).

## 7. Why not / counter-case
- Equity already fell 12.6% in 30 days and sits at its range low: some of the gap may have closed from the equity side.
- 62% IV prices large moves; the spread reduces but does not remove the vol cost.
- The trigger depends on a CDS series read by another desk at a weekly-ish cadence; a fire can arrive late.
- A hyperscaler capex RAISE on 10/28–29 or an OpenAI funding round would close the gap from the credit side (CDS tighter) and void the card.
- Positive expectancy is not demonstrated; edge is qualitative.

## 8. Calibration
No probability stated; no Brier row.

## 9. Decision
- [ ] APPROVE Dec-18 115/100P ×1, limit ≤ $4.40, max loss $441.30 — on T1 + T2 and a green ORCL day
- [ ] APPROVE alternative Nov-20 115/100P ×1, max loss $288.30
- [ ] REJECT
- [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.** All lines above are PROPOSED CARD CONDITIONS, not registered fleet gates. Chain evidence: `../research/2026-10-23_WQ509-WQ499-cards/chains.txt`.
