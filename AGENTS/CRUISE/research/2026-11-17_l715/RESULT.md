# L715 — Norwegian revolver springing-maturity test, Tue 2026-11-17

**Graded:** 2026-11-17, morning (clock 08:3x ET), CRUISE on Claude Code (Opus 5.5), PROME task from prome-19.
**Grade: NOT SPRUNG — PROVISIONAL PASS.** No issuer evidence of a spring; the 9/30 and October issuer figures put Free Liquidity well above the $800M line. Not certified: no issuer document states the 11/17 state yet.

## What the contract says (read at the primary today)

Source: Amendment No. 3 to the Seventh Amended and Restated Credit Agreement, 8-K filed 2026-10-15, acc 0001104659-26-116254, Ex-10.1 (`tm2627514d1_ex10-1.htm`) and the 8-K body (`tm2627514d1_8k.htm`), under sec.gov/Archives/edgar/data/1513761/000110465926116254/.

| Term | Text, as amended 2026-10-15 |
|---|---|
| Springing dates | "1.125% Notes Springing Maturity Date" and "2.500% Notes Springing Maturity Date" each "shall mean November 17, 2026" (91 days before each note's stated maturity) |
| Clause (y) / (z) | Tested **separately per note**: if on that date the note "has not been repaid or refinanced with Indebtedness maturing after April 23, 2030 **and** the Borrower has less than $800,000,000 of Free Liquidity", the revolver matures that day |
| Free Liquidity | Unrestricted Cash plus Available Unused Commitments (and other drawable facilities of the Borrower) that remain undrawn, could be drawn for general purposes, and would not be mandatorily repayable within six months |
| Floor covenant | Section 6.13: Free Liquidity never below $250M |

So Amendment 3 kept the 11/17 date and the $800M line unchanged from the 2025 agreement (KB-CRU-155). Both conditions must hold for a spring.

## Condition 1 — the 2027 exchangeables still outstanding

| Evidence | Reading |
|---|---|
| 10-Q 9/30/26 (acc 0001104659-26-120217) | $192.0M 1.125% + $24.1M 2.5% = **$216.2M outstanding**, current; company expects to repay in cash or refinance before maturity (KB-CRU-225) |
| EDGAR submissions, NCLH CIK 0001513761, retrieved 2026-11-17 08:3x ET | Filings after the 10/30 8-K: **one only**, a Schedule 13G filed 2026-11-16 by Ameriprise / Columbia Management (acc 0001193125-26-462443). No 8-K, no tender or redemption filing |
| Web search, 2026-11-17 | Nothing on a November repurchase of the 2027 notes |

**Treated as still outstanding** (condition live). CONDITIONAL: a small cash repurchase of $216M need not be filed on an 8-K, and NCLH's own press-release page was not read directly.

## Condition 2 — Free Liquidity below $800M

| Figure | $M | Basis |
|---|---:|---|
| 9/30/26 liquidity, issuer-stated | **~1,400** | cash 256.5 + ~1,100 revolver availability, 10-Q Note 2 — the same two components as Free Liquidity |
| After the October notes deal (revolver repaid ~380 from note proceeds) | ~1,731 | CRUISE ESTIMATE, KB-CRU-231; excludes the conditional $315M commitments |
| Harsh case: all of Q4's net need charged before 11/17 | ~1,318 | CRUISE ESTIMATE, KB-CRU-231 |
| Line | 800 | contract |
| Drop needed to spring, from the issuer's own 9/30 figure | **> 600** in 48 days | arithmetic |

On 10/29, NCLH raised full-year guidance and stated covenant compliance with liquidity it expected to cover the next twelve months. Nothing filed since points the other way.

## Grade and its limits

- **NOT SPRUNG, provisional.** Condition 2 fails on every issuer-based figure, so the revolver keeps its January 22, 2030 maturity (subject to clause (x), the >$400M senior-note spring, not live until 2028).
- ⚠️ **Not certified.** The test is the 11/17 state, and no issuer document reports it yet. Free Liquidity counts the **Borrower's** (NCLC's) cash and facilities; the 10-Q figure is consolidated NCLH, so the two are close but not identical. "$1.1B available" is rounded and October to November cash flows are unknown.
- **What would reverse it:** an NCLH 8-K disclosing the revolver maturity moved to 11/17. Four business days after 11/17 runs to **Mon 2026-11-23**. A spring of a ~$2.8B revolver would very likely be disclosed (my reading, not an SEC rule I verified for this case).
- **What certifies it:** the FY2026 10-K (expected late February 2027) debt note stating the revolver maturity. That document already falls inside DOCKET L1074 (the WQ-640 first reading at the Q4 print, due by 2027-03-15), so no new row is needed if PROME folds the confirmation there.

## Trade read (WQ-696)

This finding supports **no new investment implication**. A pass was the base case since the 11/5 10-Q read; it removes a tail (a forced refinancing of the revolver this month) that the desk already rated unlikely, and it adds no information about the surviving Norwegian read (ticket price per day, deposit quality, 5.5x leverage), whose next test is the Q4 print. Horizon: through the Q4 print. Invalidation: an 8-K by 11/23 showing a spring. Unknown: the actual 11/17 Free Liquidity figure. No TERRY packet sent: not a material finding.

## Tape context (prices fetched live 2026-11-17 08:38 ET; 11/16 closes, pre-open)

NCLH $17.90 (−0.33%), RCL $317.82 (−1.69%), CCL $29.03 (−0.68%), FORGE fetch.py (yfinance). CCL is −14.59% against the fixed $33.99 reference: `VX-CRU-01` YELLOW(2), unchanged. No price stress specific to Norwegian on the eve of the test.
