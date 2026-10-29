# TRADE IDEA — ORCL Dec-18 115/100 put spread — Oracle's equity has not followed its credit
**Date:** 2026-10-23 (written 19:0x ET from `date`)
**Setup ID:** `IDEA-ORCL-PUTSPREAD-OCT23`
**Terry verdict:** CONDITIONAL — APPROVED NOT-FIRED (WQ-514 A, Will 2026-10-23 21:15 ET, at the rec: Dec-18 115/100P ×1, limit ≤ $4.40, default size), CONDITIONAL on an Oracle-IR-verified fiscal-Q2 date written on this card before any entry. The order is Will's hand (root rule #5). *(was: unapproved proposal, 10/23 19:0x ET)*

> **TRIGGER STATE 2026-10-29 (TERRY, written ~11:3x ET from `date`): NOT FIRED; entry still BLOCKED by the date condition.** T1 ORCL 5Y CDS: no reading newer than 314 bp [10/22] found in the repo — UNKNOWN since. T2 (ORCL ≥ $120): met, close $144.54 [10/28] (+10.7% that day; cause not established here), $140.34 intraday 10/29. Void line (close ≥ $145.00): not hit, 10/28 close $0.46 short. FQ2 date: Oracle has not announced it (web search 10/29: calendar sites project 12/10, not issuer-verified) — condition unmet; WQ-518 open with Will. No order.
**Confidence in trade structure:** Medium (liquid chain; the trigger reads a credit series this desk does not own)
**Commission:** WQ-499 RULED APPROVE A, Will 2026-10-23 13:38 ET in PROME's window (PROME packet `inbox/2026-10-23_from-PROME_WQ499-WQ509-RULED-two-NOT-FIRED-cards.md`). Preparation only; root rule #5 — the order is Will's.
**Thesis owner (evidence, not TERRY's):** PROME ELLISON theme, `PROME/themes/ellison/reports/2026-10-22_sweep/00-SYNTHESIS.md` § 5 (as relayed in the packet): 5Y CDS **314 bp [10/22, DTCC]** against an S&P **BBB−** rating; 30-day IV ~59.5%, flat skew, put/call 0.71; FCF ≈ −$28.7B over four quarters, $125B debt, $288B of future data-center lease commitments **not yet on the balance sheet** (commencement ~FY27–29 per the 10-Q: REPORTED by an outside reviewer via PROME, not read by TERRY — verify), RPO $664B of which **"OpenAI ≈ half" is S&P's estimate; Oracle's filing does not name the customer** (ELLISON synthesis line 21, restored 2026-10-24 on PROME's packet); Jupiter force majeure 9/24. Oracle is investment grade, so this is an **idiosyncratic credit/equity-gap card, not a credit-cycle card** (outside DEWEY's HY figures).
**Data freshness:** spot = 10/23 close **$126.16** (+0.49%, green; snapshot 18:54 ET). Chain pulled 18:56 ET after the close; quotes are two-sided and tight, but vendor marks are SCREENING marks (durable finding 5b): the order is priced on the broker chain.

## 0. Missing inputs / hard caveats
- [x] Live price checked (10/23 close) · [x] chain checked (after-hours screen) · [ ] broker quote at entry
- [x] Position truth: no ORCL line in the book (FORGE 10/22 capture + 10/23 activity)
- [ ] **Oracle's fiscal Q2 report date UNVERIFIED — checked 2026-10-25:** the search index of [Oracle's official FAQ](https://investor.oracle.com/faq/default.aspx) reports **December 14, 2026**. This is an INDEXED lead, not a verified rendered issuer date: direct web opens of the FAQ and [IR events page](https://investor.oracle.com/events-and-presentations/default.aspx) returned headings/navigation without the date; direct FAQ curl returned HTTP 403 / Cloudflare challenge. The two prior date releases were ~8 days before the print (2025-12-02 → 12/10; 2026-09-02 → 9/10); those lags do not constrain FAQ/events publication. Third-party December 10 remains unconfirmed. **WQ-514 A still requires an Oracle-IR-verified FQ2 date written here before entry; no inference that verification cannot occur by 11/20.** Re-check Oracle IR at every touch. Evidence: `../research/2026-10-25_boot/ORACLE_DATE.md`.
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
| N_claimed | 5: CDS vs rating gap · negative FCF · lease commitments not yet on the balance sheet (company-disclosed) · OpenAI backlog concentration (S&P estimate, not company-disclosed) · Jupiter force majeure |
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
- [x] **APPROVED (WQ-514 A, Will 2026-10-23 21:15 ET, verbatim "lets have you approve with your recs"; record `PROME/proposals/2026-10-23_wq513-516-RULED.md`)** Dec-18 115/100P ×1, limit ≤ $4.40, max loss $441.30 — on T1 + T2 and a green ORCL day, NOT-FIRED, conditional on the verified FQ2 date
- [ ] APPROVE alternative Nov-20 115/100P ×1, max loss $288.30
- [ ] REJECT
- [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.** All lines above are PROPOSED CARD CONDITIONS, not registered fleet gates. Chain evidence: `../research/2026-10-23_WQ509-WQ499-cards/chains.txt`.

## 10. Ruling encoded — 2026-10-24 (TERRY, PROME packet `inbox/processed/2026-10-23_from-PROME_WQ513-514-RULED-A-cards-approved-not-fired.md`)
- **State:** APPROVED NOT-FIRED. T1 (5Y CDS ≥ 350 bp, ELLISON reading) at 314 bp [10/22]: NOT-FIRED. Nothing fills before T1 + T2 + a green ORCL day, by 11/20; time stop 12/4. $0 moved.
- **Day-colour read source (root rule #6):** ORCL regular-session close vs prior close from `FORGE/tools/market-data/fetch.py price ORCL` (stamp from `date`); intraday at order time the same tool's live read, confirmed on the broker screen. A green day = positive change on that read.
- **Earnings-risk reading (provisional, on the IR-verified pattern, NOT a verified date):** if FQ2 lands ~12/8–12/11, it falls **inside** the Dec-18 structure's life, 7–10 days before expiry and **after** the 12/4 time stop. With the time stop kept, the card exits before the print; holding past 12/4 would be a bet through a binary print and is a separate Will choice. The Dec puts' 61–66% IV on the 10/23 screen already carries some of that event premium, so the debit pays for a print the card plans to leave before. The Nov-20 alternative expires before any December print.
- **Condition binding (corrected 2026-10-25, PRD1):** no entry until the FQ2 date is verified at Oracle IR and written here. The last two date press releases came ~8 days before their prints; that sample does not bound other issuer channels or establish when verification becomes possible. The FAQ index reports December 14, 2026, but direct FAQ/events reads did not verify the date (access evidence in § 0). WQ-514 A, the 11/20 entry-window end and the 12/4 time stop remain unchanged; no condition waiver is proposed.
- **Sourcing (PROME packet `inbox/processed/2026-10-23_from-PROME_ORCL-card-two-source-qualifications-restore.md`):** line 7 now separates the company-disclosed lease commitments (not yet on the balance sheet) from S&P's OpenAI estimate. Levels, trigger and approval unchanged.
- Broker re-quote at entry; the 10/23 chain was an after-hours screen (durable finding 5b).
