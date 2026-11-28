# United Fidelity failure: WAL read-across (legs 5 and 6)

**Written:** 2026-11-27 23:45 ET (`date`), WAL, Claude Code, Opus 5.5, Will's own WAL window. **Authority:** WQ-759 RULED A (Will 23:40 ET, `PROME/WILL_QUEUE.md` row 759, read at the artifact), plan `PROME/plans/2026-11-27_bank-failure-investigation-PLAN.md` legs 5 and 6, relayed by PROME prome-80. **Facts on United Fidelity Bank (UFB)** are REGINALD's (`PROME/inbox/processed/2026-11-27_from-REGINALD_united-fidelity-failure.md`), cited, not re-derived. Nothing graded; no level, gate, weight or score moved.

**Primaries read tonight:** WAL Q3 2026 10-Q (acc 0001628280-26-068599, `wal-20260930.htm`, fetched from EDGAR 23:4x ET, sha256 e176534539cd1f32…); bank Call Reports 9/30 and 6/30 (`sources/ffiec_2026-11-04_verified/WAL_20260930.sdf`, `WAL_20260630.sdf`, verified 11/04, KB282–287); EDGAR full-text search on CIK 0001212545.

## Leg 6: direct exposure to Pedcor, Birge & Held, or a like book

**Answer: NOT FOUND.** No WAL SEC filing names either sponsor group, UFB or its parent.

| Query (EDGAR FTS, CIK 0001212545) | Window | Hits |
|---|---|---|
| "Pedcor" | 2019-01-01 to 2026-11-27 | 0 |
| "Birge" | same | 0 |
| "United Fidelity" | same | 0 |
| "Fidelity Federal" | same | 0 |
| "Indianapolis" · "Evansville" | 2026-01-01 to 2026-11-27 | 0 · 0 |
| Control: "brokered deposits" | 2019 onward | 38 |
| Control: "multifamily" · "affordable housing" | 2026 | 6 (incl. Q3 10-Q) · 6 (incl. Q3 10-Q) |

⚠️ **What NOT FOUND does not cover:** WAL does not name individual borrowers or its tax-credit partnerships in filings or Call Reports. NOT FOUND means no disclosed exposure, not a confirmed zero. The securities book was not checked for FFB notes or preferred (the parent's paper), because holdings are not disclosed by name.

**Like book, sized at the primary (9/30/26):**

| Item | WAL | UFB (REGINALD, 9/30) | Source |
|---|---|---|---|
| Multifamily loans | **$581M = 0.94% of HFI loans** ($61,549M); wtd LTV 52.7% | $2,721.6M = 89.0% of loans | 10-Q MD&A CRE-NOO table; bank RCON1460 $581.123M (6/30 $648.717M, −10.4%) |
| LIHTC + renewable energy equity investments | **$597M** (12/31/25 $593M); unfunded commitments $283M; Q3 LIHTC tax credits $28.4M | — | 10-Q income-tax note, "LIHTC and renewable energy projects" |
| Related-party sponsor lending | none disclosed | the defining feature | — |

**Read:** the only affordable-housing contact is a passive tax-credit equity book of about 1% of loans that also includes renewable energy, with partners not named. It is not a lending concentration. Multifamily lending is under 1% of loans, falling, at about 53% LTV. Nothing here resembles UFB's stacked related-party liens.

## Leg 5: does the failure change funding for brokered-reliant banks, WAL included

**Evidence tonight: none in either direction.** The 11/27 half session closed at 13:00 ET, before the announcement (REGINALD claim 15, INFERRED). No brokered-CD rate source was read tonight; the first readable evidence is the Mon 11/30 tape.

**WAL's own funding exposure (primary, 9/30/26):**

| Measure | Value | Source |
|---|---|---|
| Wholesale brokered deposits | **$5.6B** (12/31/25 $5.4B); bank $5,642M = **6.9% of deposits** (UFB 18.7%) | 10-Q deposits note; RCON2365, RCON2200 |
| Brokered maturing within 1 year, ≤$250K | $5,257M = **93% of brokered**; brokered over $250K: $0 | RCONHK06, RCONHK05, RCONK220 |
| Reciprocal deposits (ICS $13.2B, CDARS $2.1B) | $16.6B = 20.1% of deposits (relationship deposits placed through IntraFi; FDIC-insured) | 10-Q; RCONJH83 $16,550M |
| Time deposits maturing in the rest of 2026 | $4,368M of $10,663M (41%) | 10-Q maturity table |
| Q3 average CD cost | 3.71% on $10,088M | 10-Q average-rate table |
| Capital category | well-capitalized: bank CET1 11.4%, total capital 13.3% vs 10.0% | 10-Q capital table |

⚠️ **Call Report basis trap:** bank "total brokered deposits" (RCON2365) reads $15,436M at 6/30 and $5,642M at 9/30. That is **not a $9.8B outflow.** At 6/30 the report counted $10,159M of reciprocal deposits as brokered (RCONG803); at 9/30 that line is absent. Wholesale brokered was about $5,278M at 6/30, so it rose about $0.36B. The reason for the reporting change was not read. Never cite the 2365 drop as a funding flow.

**Mechanism check:** UFB's brokered problem was a rule. An undercapitalized bank may not accept or renew brokered deposits, and at the failure Cede & Co. brokered deposits were excluded from the assumption (REGINALD claims 5 and 7). That rule binds on capital category, and WAL is well-capitalized. The channel that could reach WAL is pricing: brokers and investors asking more of banks that lean on brokered money. At about 6.9% of deposits WAL is a moderate user, not a dependent one. Rough sensitivity: +25bp on the full $5.6B costs about $14M a year pretax, about 0.8% of annualized Q3 PPNR ($419.1M × 4). That is my arithmetic, not an issuer figure, and it assumes the whole book reprices, which 93% does within a year. WAL's larger rate-sensitive cost is the ECR-related deposits (KB-289), and this failure does not touch them.

**Evidence that would show it, and when:**

| Evidence | First readable | State tonight |
|---|---|---|
| KRE and small-bank names against SPY, Mon 11/30 (plan leg 8; >3 points under SPY with deposits as the stated cause) | 11/30 close | none (market closed before the news) |
| New-issue brokered CD rates for mid-size banks against Treasuries of the same term | 11/30 onward | not read (no automated source verified) |
| Fed H.8: small domestic bank deposits, week of 12/2 | ~12/11 | none |
| WAL management deposit commentary (a December conference, if one is scheduled; not verified) | December | none |
| WAL's Q4 10-K/call: brokered balance and CD cost | Q4 print (date not set) | — |

## Forward view (unscored outlook, no row registered)

- **Expect (~85%, through the Q4 print):** no measurable change to WAL's funding from this failure: brokered balance within ±$1B of $5.6B and no deposit-flight commentary. Why: the rule that hurt UFB binds on capital WAL has, UFB's depositors moved whole to a large buyer, and WAL's brokered share is a third of UFB's.
- **Alternative (~15%):** a broader small-bank funding scare (a second failure, or Monday's tape with deposits cited) reprices brokered CDs across the sector. WAL's cost rises in the tens of millions a year, not more. **But the stock would likely fall harder than its funding** (60-day beta to KRE 1.31, STATUS 11/26). The price risk is larger than the earnings risk.
- **Would change my mind:** brokered CD new-issue rates for $50–150B banks widening by more than 25bp against Treasuries; a WAL disclosure of brokered run-off or replacement cost; any filing naming Pedcor or Birge & Held at WAL.

**Tradeability:** nothing here is material to a WAL position (NOT FOUND, small funding sensitivity). TERRY already holds its United Fidelity NO CARD (b521f8025b); no new facts packet is sent.
