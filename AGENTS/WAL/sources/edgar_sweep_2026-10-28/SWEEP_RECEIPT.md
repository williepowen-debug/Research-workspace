# EDGAR + FFIEC sweep receipt — 2026-10-28 (WAL, laptop WilliePOwen, ~22:38–22:50 ET)

## EDGAR, issuer CIK 0001212545, window 2026-09-24 → 2026-10-28
| Route | Result |
|---|---|
| submissions JSON (data.sec.gov) | Newest filings: 10/19 8-K 0001628280-26-066286 + ten 10/19 Form 4s (066303–066315). Nothing after 10/19. |
| browse-edgar atom (owner=include) | Newest 10 entries all 10/19 Form 4s. |
| efts full-text, forms 8-K/10-Q/144/13D/13G/4, phrase "Western Alliance" | Issuer's own: the 10/19 8-K + ten 10/19 Form 4s. Remaining hits are third-party documents naming Western Alliance (see below). |
| efts forms=144, ciks=0001212545, window | 0 hits. **Positive control:** same route 2024-01-01→2026-10-28 returns 12 WAL Form 144s, newest 2026-06-15 (Curley). |

No 10-Q (Q3 10-Q not on EDGAR as of ~22:40 ET 10/28), no 10-K, no 13D/13G, no Form 144.

## Third-party filings naming Western Alliance (same window)
| Filing | Western Alliance role |
|---|---|
| First Eagle Private Credit Fund 8-K 10/5 (0001193125-26-414009) EX-10.1, 4th Amendment dated 10/1/2026 | **Western Alliance Bank joins as "New Lender" (§5.6); Annex A commitment $100,000,000.00** — saved `FirstEagle_PCF_SPV_4thAmend_ex101.htm` sha256 92d98ceaab0d739dcb293ee6aaefb8f9809bb5ba7548b994b060ac2d45c28a44 |
| KKR FS Income Trust 8-K 10/13 EX-10.1; KKR FS Income Trust Select 8-K 10/2 EX-10.1 | Western Alliance TRUST Co., N.A. = collateral custodian (fee role) |
| Fidus 8-K 10/26 EX-4.2 | Western Alliance TRUST Co. = custodian / collateral agent on ING-agented SPV facility (fee role) |
| EverQuote 8-K 10/21 EX-10.1/10.2 | Western Alliance Bank = agent, lender, issuing lender, swingline lender (2nd amendment 10/21) |
| AudioEye 10-Q 10/26 + EX-10.2 | $20M facility lender (since 3/31/2025); 5th loan modification 10/26 |
| Data I/O 8-K 10/22 | Expected Loan and Securities Agreement with Western Alliance Bank |
| CoStar 8-K 10/27 (Vexcel merger) | Vexcel revolver lender (Debt Facilities definition) |
| Dream Finders 8-K 10/20 | L/C issuer in BofA-agented syndicate |
| FHLB San Francisco 8-K 10/1 | WAB CRO Emily Nachlas in director-election vote tally |

## FFIEC CDR (Call Report, RSSD 3138146)
| Call | Result |
|---|---|
| RetrieveFacsimile 9/30/2026 | HTTP 500 |
| RetrieveFacsimile 6/30/2026 (control, scratchpad) | HTTP 200; bytes identical to `sources/ffiec_2026-10-14/WAL_2026-06-30.sdf` (sha256 7c40bbb5154eb84e…) — credential + transport verified on this box |
| RetrieveReportingPeriods | 200; 9/30/2026 listed |
| RetrieveFilersSinceDate (9/30/2026, since 10/01/2026) | 200; 2,643 filers; **3138146 absent** ⇒ the 500 = not yet filed/published, not a credential failure |

Due date 10/30; JWT expires 11/5.
