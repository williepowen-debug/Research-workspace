# Carvana Q3-2026 — OTTO read of the primary filings (s040, 2026-10-28)

**Sources (all `[CONF]`, SEC EDGAR, pulled 2026-10-28 ~22:10 ET):**
- 8-K Items 2.02/9.01, accession `0001690820-26-000066`, accepted 2026-10-28T20:05:55Z — Ex-99.1 shareholder letter, Ex-99.2 press release (saved in `sources/`).
- 10-Q for quarter ended 2026-09-30, accession `0001690820-26-000067`, accepted 2026-10-28T20:11:03Z — HTML hashed, not stored; verbatim excerpts in `sources/10q_excerpts.txt`.
- Hashes: `sources/SHA256SUMS`.

**Not read:** the 17:30 ET earnings call (no primary audio or transcript read this session). Post-close price reaction not captured. Gotham's January 28, 2026 report is not mentioned in the 10-Q (zero hits); nothing below speaks to it directly.

## 1. The new fact: the SEC closed its investigation, with no enforcement recommendation

10-Q Part II Item 1, verbatim: *"In June 2025, we received a subpoena from the SEC requesting information that we believe primarily relates to the allegations raised by the report. In September 2026, the SEC informed us that it had concluded its investigation and did not intend to recommend an enforcement action against us in connection with the matter."* The "report" is the January 2025 short-seller report (the 10-Q calls the firm "now-defunct", which matches Hindenburg).

| What this is | What it is not |
|---|---|
| Carvana's own description of an SEC staff communication, dated September 2026, first seen by OTTO in this 10-Q | A published SEC document. OTTO has not seen the letter itself |
| The end of the only government investigation OTTO had on record for the Carvana carve-out (subpoena June 2025) | An exoneration. Staff closing communications customarily say they are not one; OTTO has not seen this one's wording |
| Scoped to "the allegations raised by the report" (January 2025) | A finding on Gotham's January 2026 report, whose related-party allegations overlap but are a separate document |

First disclosure: this is the first SEC filing OTTO found that discloses it. OTTO did not run a press search, so an earlier press report is not ruled out.

## 2. Related-party lines (Note 6), Q3-2026 vs Q3-2025

| Line | Q3-26 | Q3-25 | Read |
|---|---|---|---|
| VSC commissions + excess-reserve payments, DriveTime-administered | $125M | $91M | Per retail unit **$575 vs $584**, flat. No per-unit acceleration of the related-party revenue line |
| Servicing/admin fees paid to DriveTime (Carvana's held receivables) | $1M | $2M | Carvana's own held book only. Says nothing about the third-party whole-loan servicing fee Gotham estimated (0.117%), which is not a filed document |
| Finance receivables sold to DriveTime or affiliates | none (9M-26 and 9M-25) | none | Direct statement in the filing |
| Limited-warranty admin fee paid to DriveTime | $9M | $7M | Grows with units |
| Profit Sharing Agreement revenue | $4M | $2M | Amended March 2026 to add contracts |
| Other revenue from related parties (income statement) | $129M | $93M | Sum of the above classes |

The filing holds nothing showing that the related-party flows grew faster than the business. That does not test Gotham's specific third-party whole-loan servicing estimate, which no public filing can reach (THESIS § Carvana, 8/27 re-scope).

## 3. The finance line (Other GPU, GAAP basis, the series OTTO tracked)

| Quarter | Other GPU / retail unit |
|---|---|
| Q3-25 | $3,040 |
| Q4-25 | $2,869 |
| Q1-26 | $2,807 (re-derived from 9M totals: matches) |
| Q2-26 | $2,666 |
| **Q3-26** | **$2,733**: **+$67 QoQ, −$307 YoY** |

- The two-quarter **accelerating** compression OTTO recorded (−$62, then −$141) **did not continue**. Q3 rose sequentially. The YoY decline remains.
- Carvana's attribution (Ex-99.1): lower customer rates relative to benchmarks ("over 100 basis points"), rising benchmark rates and fuel, with "~$200 per unit" put on rates and fuel together. MD&A: "lower loan sale spreads."
- `[EST]` 9M gain on loan sales ÷ proceeds from sale: **7.36% (2026) vs 9.16% (2025)**. A rough proxy (proceeds and gains are cash-flow-statement totals, not one matched pool), but its direction agrees with "lower loan sale spreads."
- **Unchanged limit (THESIS → CARL joint item):** OTTO still cannot separate rate-driven from credit-driven sale-spread compression. Carvana's attribution is the issuer's own, not a measurement. No prediction is written off this join.

## 4. Funding access (Ally forward flow)

- Ally MPSA: $2.0B sold in Q3-26 vs $1.2B in Q3-25 (+67%). $5.7B over 9M-26 vs $3.2B, about 39% of 9M sale proceeds vs about 33%. **$6.0B unused capacity at 9/30** under the July 27 amendment ($8.0B through 7/26/2027). Agrees with OTTO's s032 correction (LESSONS row: read both counterparties' amendments).
- Beneficial interests in securitizations: $557M (from $486M at YE). Q3 fair-value change +$7M. Level 3 discount-rate range 5.7–10.0%, weighted 9.2% (9.0% at YE). This is a fair-value mark that moves with rates; it is not a collateral-performance read. The BLAST 10-D panel (V4) remains the collateral instrument.
- Liquidity: cash $3.049B; committed liquidity $5.12B; no going-concern, ICFR-change or restatement language found.

## 5. Disclosure practice change (logged, not graded)

Starting with the Q4-2026 call, Carvana **will stop giving quarterly or annual financial outlooks** and will shift primary reporting from non-GAAP to GAAP. The second change moves toward the more auditable basis. The first leaves outsiders fewer dated management claims to check. OTTO records both and grades neither.

## 6. Against the registered conditions

| Registered condition (canonical home) | Q3 evidence | OTTO read |
|---|---|---|
| THESIS risk row: *"Carvana earnings/disclosure clean + substantive rebuttal of Garcia related-party allegations"* ⇒ sub-thesis −40% | Clean: no auditor change, no ICFR change, no restatement, no 10-Q delay. Rebuttal: the SEC investigation closed with no enforcement recommendation (company-reported), plus the company's reaffirmed counsel review | **Condition appears MET in substance.** The pre-registered consequence applies. Apply it at THESIS v1.6 (10/30), which is the conviction cell's canonical home; STATUS's V5 score moves only when that cell moves |
| CLAUDE trigger: Carvana 10-K delayed or GT resigns ⇒ 🔴 ALL | 10-Q filed on time with earnings | Not fired |
| THESIS: discovery production surfaces manipulation evidence ⇒ re-promote | None | Not fired |

**What survives the downgrade:** the BLAST collateral is weak (V4, scored separately, unchanged), and Gotham's third-party whole-loan servicing estimate remains unverified, not refuted. A −40% move on a LOWER-conviction carve-out takes it toward DORMANT, not to "refuted."

## 7. Not done this session
- Earnings call (primary audio/transcript).
- Wording of the SEC communication itself (not public).
- Any press search for an earlier report of the SEC closure.
