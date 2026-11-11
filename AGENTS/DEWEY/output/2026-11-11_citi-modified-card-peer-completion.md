# Citi completes the modified-card peer comparison

**Date:** 2026-11-11 | **Mode:** Thesis | **Confidence:** High on disclosed balances and arithmetic; Medium on cross-issuer comparison; UNKNOWN on the cause of Capital One's move. **Authority:** Will's existing four-lender approval, reaffirmed November 4 at 21:12 ET; PROME DOCKET L923. Continuation of `output/2026-11-04_card-modified-cohort-peer-check.md`.

## Key finding

**Citi does not reproduce Capital One's large increase in the delinquent share of recently modified card loans.** Citi's North America share rose **18.59% to 19.08%, or 0.49 percentage points**, from June to September 2026. Adding Citi leaves all six comparison issuers within approximately one point of their June share, versus Capital One's approximately 7.9-point increase. This completes the outstanding Citi leg; it does not establish why Capital One moved, prove hidden delinquency, or establish a class-wide causal effect. [PRIMARY: Citi Q2/Q3 10-Q, Note 12; prior six-issuer work cited below.]

## Evidence

Amounts are **$ millions**, except percentages. Citi's population is permanently modified consumer loans to borrowers experiencing financial difficulty, including loans modified during the preceding 12 months. North America includes the United States, Canada and Puerto Rico; Mexico is excluded. This is not identical to Capital One's domestic-card perimeter.

| North America credit cards | June 30, 2026 | September 30, 2026 | Change |
|---|---:|---:|---:|
| Modified group outstanding | 1,555 | 1,630 | +4.82% |
| Current | 1,266 | 1,319 | |
| 30–89 days past due | 185 | 210 | |
| 90+ days past due | 104 | 101 | |
| **30+ days past due, derived sum** | **289** | **311** | **+7.61%** |
| **30+ share of modified group, derived** | **18.59%** | **19.08%** | **+0.49 pp** |

The buckets reconcile exactly: 1,266 + 185 + 104 = 1,555; 1,319 + 210 + 101 = 1,630. Share = (30–89 + 90+) / group total. [PRIMARY: both filings, Note 12, “Performance of Modified Consumer Loans,” p.139.]

The smaller **outside-North-America** card group is kept separate: total $36M to $38M, delinquent $6M at both dates, implying 16.67% to 15.79%. It does not reverse the finding and is not pooled with the North America comparison. [Same tables.]

### New modifications and defaults

| North America cards, three-month activity | Q2 2026 | Q3 2026 | Q3 2025 |
|---|---:|---:|---:|
| Modifications outstanding at period end | 452 | 541 | 467 |
| Modified and subsequently defaulted within the stated quarter | 87 | 93 | 92 |

Q3 modifications increased **19.7% sequentially and 15.8% annually**. They are interest-rate reductions in Citi's table. Citi describes programs generally involving reduced rates, fixed payment plans of up to 60 months, and cancellation of available credit. These are not simply loans whose payments disappeared. [PRIMARY: Note 12, “Consumer Loan Modifications,” pp.136–138.]

**Default means 60 days past due at Citi.** The default table counts loans modified and subsequently defaulted within the stated period, outstanding at period end. Its $93M is neither a default rate for the $1,630M rolling group nor directly comparable with other issuers' definitions. Gross credit losses in the separate performance table are also not substituted for these defaults. [PRIMARY: Note 12, “Defaults of Modified Consumer Loans,” pp.139–141.]

## Counter-evidence and limitations

- The $541M modification balance is higher, so this is not evidence that assistance needs are flat. A modest common increase can coexist with Capital One's unusually large delinquent-share move.
- Citi normally re-ages modified loans to current. For certain loans, FFIEC rules require three consecutive minimum monthly payments or the equivalent first. The observed delinquent share is therefore influenced by program mechanics as well as repayment behavior. It cannot measure concealed delinquency or the causal benefit of modification.
- These are changing 12-month groups, not the same borrowers followed through time. Exits, charge-offs and newly modified accounts can change the share.
- Issuer perimeters and default definitions differ. Bank of America includes other consumer loans; Citi includes Canada and Puerto Rico; JPMorgan's first bucket includes under-30-day arrears. **Do not rank their share levels as a credit-quality league table.**
- The other six issuers' figures are carried from the November 4 completed work, not re-pulled today. Capital One's cause remains UNKNOWN. No trade or score is changed by this report.

## Sources and reproduction

1. [Citi Q3 2026 10-Q](https://www.sec.gov/Archives/edgar/data/831001/000083100126000056/c-20260930.htm), filed November 5, accessed November 11; Note 12 pp.136–141.
2. [Citi Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/831001/000083100126000045/c-20260630.htm), filed August 6, accessed November 11; same note and tables.
3. `output/2026-11-04_card-modified-cohort-peer-check.md`, including its cited primary filings and saved `research/2026-11-04_card-peers/PEERS-Q3-2026-tables.json`.

Evidence: `research/2026-11-11_citi/20260630-tables.json` and `20260930-tables.json` record filing URLs, retrieval times, source hashes, byte counts and extracted table rows. Companion `*-consumer-excerpt.txt` files preserve narrative and footnotes. Table indices 165/166 are modification activity; 169 is performance. Reproduction uses `scripts/edgar_doc.py`'s SEC retrieval method and the formulas above.

## Process report

One targeted web search confirmed the filing; the SEC submissions feed and two complete SEC documents were pulled directly. No sub-agents. System Python lacks BeautifulSoup; the existing repository virtual environment supplied it. Required sub-answers—Citi filing availability, cohort balances, delinquency change, activity/default context and comparison limits—are answered. No additional research assignment or monitoring job is created. Primary figures are high confidence; cross-issuer causal interpretation remains limited.

**Do-not-relay-as:** proof that only Capital One has credit stress, a deterioration caused by modification, hidden delinquency, a pooled issuer default rate, or a trade recommendation. The narrower result is that Citi does not reproduce Capital One's Q3 jump in this particular modified-cohort share.

## Recipient actions

- CARL: CARL consumes the Citi completion under the existing peer comparison. CARL retains causal interpretation.
- TERRY: TERRY assesses tradeability under Will’s standing direction. Return a reasoned no-card if the finding supports no construction.
