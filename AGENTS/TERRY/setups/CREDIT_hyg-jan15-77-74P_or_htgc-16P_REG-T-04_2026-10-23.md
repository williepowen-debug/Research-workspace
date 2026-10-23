# TRADE IDEA — Broad credit into the REG-T-04 window — HYG Jan-15 77/74 put spread (rec) · alt HTGC Jan-15 16P
**Date:** 2026-10-23 (written 19:0x ET from `date`)
**Setup ID:** `IDEA-CREDIT-HYG-BDC-OCT23`
**Terry verdict:** CONDITIONAL — NOT-FIRED; unapproved proposal. Nothing is approved in advance.
**Confidence in trade structure:** Medium (HYG leg) · Low (HTGC leg: thin options, binary print inside the entry window)
**Commission:** WQ-509 RULED APPROVE A, Will 2026-10-23 13:38 ET in PROME's window (PROME packet `inbox/2026-10-23_from-PROME_WQ499-WQ509-RULED-two-NOT-FIRED-cards.md`). Preparation only; root rule #5 — the order is Will's.
**Thesis owners (evidence, not TERRY's):** REGINALD (REG-T-04 letter: HY OAS > 350 bp on 3 consecutive first-published closes; exit ≤ 330 ×5; 340 [10/22], run 0 of 3, packet `012e5c08c`) · DEWEY (REQ-002 HY widening mostly BROAD; REQ-003 CCC bonds ~78% cable/telecom/airline/chemicals, software 5–8%, software stress sits in loans/BDCs: `AGENTS/DEWEY/output/2026-10-23_ccc-and-under-80-loans-three-way-split.md`, `d0d5463a7` + `23209b69f`) · BROCK (BDC pick HTGC, trap FSK: `AGENTS/BROCK/research/2026-10-23_bdc-software-exposure/REPORT.md`, read at the artifact) · WALTER SIG-W-20261023-015/-016 (issuance ≈ $7B Oct vs ≈ $51B Sep).
**Data freshness:** spot = 10/23 closes (snapshot 18:54 ET). Chains pulled 18:56 ET, **after the close**: out-of-the-money HYG strikes show no bid in the vendor feed, so every option figure below is a SCREENING mark (durable finding 5b); the order is priced on the broker chain. Position truth: FORGE mirror of the 10/22 11:01 ET capture plus the 10/23 activity transcription.

## 0. Missing inputs / hard caveats
- [x] Live price checked (10/23 closes) · [x] chain checked, after-hours ⇒ screening only · [ ] broker quote Monday
- [x] Existing position truth: APO Dec-18 95P ×1 (private credit) is the only book line on this falsifier; the 31 bank puts are NOT this trade (REGINALD BANK-ABSENT; the 10-year, not HY, moves KRE)
- [x] Catalyst dates: REG-T-04 earliest fire = the 10/27 close, FRED-published ~10/28 (FOMC day); ARCC Q3 Tue 10/27 before the open; HTGC Q3 Thu 10/29 after the close (BROCK, company-announced)

## 1. One-line setup
Own the broad junk-bond repricing that REGINALD's issuance-freeze gate measures, in the liquid instrument that holds those bonds, with defined risk, entered only once the gate fires.

## 2. Trigger state, in figures (NOT-FIRED)
| Leg | Line | State | Status |
|---|---|---|---|
| **T1 — REG-T-04** (REGINALD letter) | HY OAS > 350 bp on **3 consecutive** first-published closes | **340 [10/22]**, run 0 of 3; 10/23 not yet published | **NOT FIRED** (earliest 10/27 close, published ~10/28) |
| Tier shape (context) | BB / B / CCC | BB 210 · CCC 1,340 [10/22] (PROME packet) | context |
| Entry window | first **green HYG session** after T1 (root rule #6: puts on green days), through Fri 2026-11-13 | — | waits on T1 |
| **Void before entry** | HY OAS ≤ 330 on 5 consecutive closes (REGINALD exit), or the new-issue window reopens (≥ ~$5B priced in one week, PROME/WALTER), or no green HYG day by 11/13 | — | — |

## 3. Chart / tape read (10/23 close)
| Item | Read |
|---|---|
| HYG | **$77.05** (−0.06%, red), 30-day −1.45%, **near its 30-day low** (range 76.81–78.37) |
| HTGC | **$16.41** (−0.49%, red), 30-day −6.66%, mid-range (16.07–17.76); **1.35× its 6/30 NAV of $12.15** (BROCK) |
| Rate leg | HYG carries Treasury duration as well as spread: a falling 10-year cushions HYG while spreads widen. HY OAS went 266 [9/21] → 340 [10/22] (+74 bp) with the 10-year flat over that span (^TNX 4.963 → 4.953, −1 bp; REGINALD's packet agrees). Over the snapshot's 30-day window (from 9/23) HYG fell only 1.45% while the 10-year fell ≈ 16 bp (5.114 → 4.953): the duration leg cushioned part of the spread move. Windows differ; this is an illustration, not a fitted sensitivity |
| Vol | HYG puts ≈ 10.9–12.3% IV (cheap); HTGC ≈ 30–36% IV |

## 4. Structure (both priced; one recommended)
| | **(a) HYG Jan-15-2027 77/74P ×4 — RECOMMENDED** | (b) HTGC Jan-15-2027 16P ×5 — alternative |
|---|---|---|
| Legs (18:56 ET screen) | 77P 1.00 / 1.63 (OI 192,900) · 74P 0.01 / 0.94 (OI 142,933); regular-hours marks ≈ 1.31 / 0.47 | 16P 0.45 / 0.75 (OI 114); Jan 15P 0.20 / 0.35 (OI 369) |
| Order | one complex order, **net debit limit ≤ $1.00** (33% of width) | limit ≤ $0.75 |
| **Max loss** | **$405.20** = 4 × $100 + $5.20 fees (0.65/contract/side, budget arithmetic) | **$378.25** = 5 × $75 + $3.25 fees |
| Max gain | 4 × $300 − $405.20 = **$794.80** at HYG ≤ $74 on 1/15 | to NAV ($12.15): (16 − 12.15) × 500 − 378.25 ≈ **$1,546.75** |
| Breakeven at expiry | HYG **$75.99** (−1.4%) | HTGC **$15.24** (−7.1%) |
| Payoff ratio | **1.96 : 1** | ≈ 4.1 : 1 to NAV (no cap, but no NAV floor either) |
| What it needs | ≈ +35–40 bp of spread widening to breakeven and ≈ +100 bp to max, **with the 10-year flat** (HYG spread duration ≈ 3.2 assumed, not measured) | the premium to NAV compressing and/or a markdown at the 10/29 print |
| Liquidity | deep (OI 140k–190k); after-hours quotes unusable | **thin**: OI 114, spread ~50% of mark — entry and exit each pay a large toll |
| DTE at 10/23 | 84 days; spans T1, FOMC 10/28, election 11/3 | 84 days; spans the 10/29 print |

**Why (a):** the card's thesis is the HY gate (REG-T-04) and DEWEY's finding that the HY-bond widening is broad. HYG holds those bonds, is deep, and its puts are cheap (≈ 11% IV). Tenor matches a credit view that works over weeks (construction rule #16). **Why not (b) as the main expression:** it expresses a *different* stress (software loans inside BDCs, DEWEY/BROCK), its options are thin, and its 10/29 print lands **inside** the entry window, so an entry after a 10/28 fire would pay print volatility. If the print is the catalyst, construction rule #18(b) applies: the 16 strike is only 2.5% out of the money (inside a normal print move), but the BDC print envelope has not been measured (rule #18 scope: re-measure before applying the bank numbers to another sector). Size against the post-print mark (#18(c)). **BROCK's falsifier stands with (b):** HTGC software book marked ≥ 97% of cost, non-accruals ≤ 1.0%, NAV ≥ $12.15 at the 10/29 print ⇒ the AI-disruption-loan case is not showing.

## 5. Effective-N (RISK_SCORING §2b)
| Field | Entry |
|---|---|
| N_claimed | 3: HY OAS gate near its line · issuance freeze on volume · CCC widening |
| Shared antecedent | a broad credit repricing (the cycle); issuance and spreads are two readings of one market |
| **N_eff** | **≈ 1.3 → sized as ONE view** |
| Book overlap | APO Dec-18 95P ×1 (private credit) partly shares it; the Nasdaq-downside bet (QQQ 710P/705P/690-670P) shares a risk-off antecedent; the 31 bank puts do NOT (REGINALD: the 10-year moves KRE, HY does not). Combined risk-off forward exposure is larger than this card's $405 |

## 6. Management (written before any fill)
- **Harvest (durable finding 9):** (a) sell when the spread marks **≥ $2.00** on the broker bid (2× the debit, 67% of width); (b) sell half at a +100% mark.
- **Kill:** HY OAS ≤ 330 on 5 consecutive closes (REGINALD's exit line) or the new-issue window reopens (≥ ~$5B priced in a week) → sell at the bid. (b) also: BROCK's falsifier holds at the 10/29 print → sell.
- **Time stop:** sell by the close **Fri 2027-01-08** if neither has fired. No roll pre-registered (Non-Negotiable #6).
- Forward max loss after a fill is the remaining mark (construction rule #20(d)).

## 7. Why not / counter-case
- REG-T-04 is **10 bp** from its line; a fire can happen on noise and reverse (the exit line is 330 ×5, not 340).
- The 10-year: if it keeps falling (flight to quality), HYG's duration offsets the spread leg — the gate can fire while HYG barely moves (the last 30 days show it).
- DEWEY: the CCC widening is concentrated in a few cable/telecom restructurings (Optimum's Chapter 11 preparation reported 10/22); idiosyncratic defaults can widen the index without a cycle.
- Positive expectancy is not demonstrated; edge is qualitative (cheap vol on a named, dated gate).

## 8. Calibration
No probability stated; no Brier row.

## 9. Decision
- [ ] APPROVE (a) HYG Jan-15 77/74P ×4, limit ≤ $1.00, max loss $405.20 — on T1 and a green HYG day
- [ ] APPROVE (b) HTGC Jan-15 16P ×5, limit ≤ $0.75, max loss $378.25
- [ ] REJECT
- [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.** All lines above are PROPOSED CARD CONDITIONS, not registered fleet gates. Chain evidence: `../research/2026-10-23_WQ509-WQ499-cards/chains.txt`.
