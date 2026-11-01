# Q3 Call Report basis verification — October 31, 2026

VERDICT: **CORRECTED-framing.** Independently recomputed key arithmetic agrees with the parent comparison. The data support measured deterioration in book equity/AOCI and selected credit or composition flags, not an inference that banks lost another 20% of equity or that gross delinquency is wholly unguaranteed credit stress.

CLAIM CHECKED: Definitions, quarterly arithmetic, and economic framing of the September 30, 2026 Call Reports, with focused checks on OZK, WAL, FLG and the AMTB/SBCF equity outliers. This is a WALTER Rule 9 verification helper, not a domain grade, owner-state change or full-universe audit.

EVIDENCE LOCATOR: Parent `retrieval.json` identifies and hashes the raw March/June/September files. Independently read `/tmp/walter-call-report-availability-6guvqyx_/{BANK}_20260930.sdf` and `/tmp/walter-call-report-comparison-eagcicxy/{BANK}_{20260331,20260630}.sdf`; use exact MDRM codes below, Call Date and RSSD together. Parent `comparison.json` and `compare.py` supplied the claims checked. Primary definition reference: [FFIEC September 2026 reporting form](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_202609_f.pdf), RC-B page 21, RC-N pages 48–50, RI-B page 10, RI-A page 9, RC and RC-R. SDF short labels alone omit important column distinctions.

SUPPORTING OBSERVATION:

## Definitions and calculation checks

| Field | Verified interpretation / required framing |
|---|---|
| 1772 / 1773 | RC-B total AFS amortized cost / fair value; subtraction is the pretax net valuation gap, not gross losses or a quarterly realized loss. |
| 1754 / 1771 | RC-B total HTM amortized cost / fair value; keep this valuation gap separate from AFS. |
| 3210 / B530 | Bank equity / accumulated other comprehensive income. Equity already includes AOCI. Do not subtract the AFS valuation gap again from reported equity. AOCI also contains tax and other OCI effects. |
| P793 | Reported bank CET1 ratio. Actual capital prefixes include RCOA and RCFA; RCON/RCFD-only extraction fails. |
| 1403 / 1407 | RC-N9 nonaccrual / 90+ days past due and still accruing, respectively. They are distinct columns and neither alone is the issuer's adjusted NPL definition. |
| 3123 | Loan-and-lease allowance; broader issuer ACL may include unfunded commitments or other assets. |
| RIAD4340 / 4635 / 4605 | YTD bank income / gross charge-offs / recoveries. Q3 = September minus June; Q2 = June minus March. NCO = gross charge-offs minus recoveries. |
| 3190 + B993 + B995 | Other borrowed money plus federal funds purchased plus repos. This selected borrowing total need not equal an issuer's broader borrowed-funds presentation. |

RCFD and RCON scopes must remain consistent for each bank and period; capital prefixes are a separate schema. No automatic substitution of issuer holding-company earnings for bank earnings is valid.

Independent raw-file calculations passed exact Decimal comparisons against the parent values for both quarterly income/NCO and equity/AOCI changes for all five names below. Amounts in $ millions; percentages use June bank equity as denominator.

| Bank | Equity change | AOCI deterioration / June equity | Q2 → Q3 bank income | Q2 → Q3 NCO |
|---|---:|---:|---:|---:|
| OZK | −2.0655% | 3.4187% | 167.371 → 168.361 | 56.254 → 44.453 |
| WAL | −2.9247% | 4.2611% | 387.058 → 298.758 | 55.027 → 45.797 |
| FLG | −6.0950% | 3.5864% | 34.463 → 12.117 | 99.415 → 74.116 |
| AMTB | −8.8333% | 9.7510% | 23.376 → 27.801 | 1.387 → 2.035 |
| SBCF | −7.2450% | 5.7977% | 60.435 → 60.270 | 3.200 → 5.391 |

For these five, Q3 RCOAP838 is 1 (AOCI opt-out). Book-equity damage and regulatory CET1 movement therefore are not interchangeable. A point-in-time securities gap near a large percentage of equity does not establish a new loss of that percentage during Q3.

## Equity bridges: do not attribute the entire decline to securities

The independent RI-A bridge reconciles exactly to the equity change for each of the five names. Selected outliers, Q3 flows in $ millions:

| Bank | Income | OCI | Net capital stock transactions excluding treasury | Net treasury stock transactions | Common / preferred dividends | Equity change |
|---|---:|---:|---:|---:|---:|---:|
| FLG | +12.117 | −291.966 | +11.858 | −215.839 | −4.142 / −8.211 | −496.183 |
| AMTB | +27.801 | −96.173 | +1.250 | 0 | −20.000 / 0 | −87.122 |
| SBCF | +60.270 | −176.097 | +29.205 | 0 | −133.435 / 0 | −220.057 |

Sources: YTD differences in RIAD4340, B511, B509, B510, 4460 and 4470; other RI-A flows are zero for these three. FLG's [October 23 earnings release](https://www.sec.gov/Archives/edgar/data/910073/000091007326000080/q32026earningsrelease.htm) says the $250M repurchase program completed in early October. The September quarter bridge uses the observed net treasury transaction figure, not the entire completed-program amount. SBCF's bank dividend is a bank-equity movement and must not automatically be described as a listed-parent shareholder payout.

## WAL and FLG loan scope

WAL: RCON1407 is $1,385.227M, of which RCONK043 rebooked GNMA loans account for $1,319.025M, **95.22%**. RCONK037 wholly/partly government-guaranteed loans is $1,321.125M. This is not evidence of $1.385B of new unguaranteed defaults. The [Q3 WAL 10-Q](https://www.sec.gov/Archives/edgar/data/1212545/000162828026068599/wal-20260930.htm), Note 4 and asset-quality MD&A, reports $485M HFI nonaccrual and $272M HFI 90+ accruing, including $214M government-guaranteed residential loans excluded from its adjusted NPL presentation. Its HFI and held-for-sale tables must remain separate. Bank RC-N1403 is $487.951M; this helper has not fully bridged that small perimeter difference.

The apparent WAL $485M versus $433M conflict is **corrected**: `AGENTS/WAL/research/2026-10-30_Q3_10Q_GRADE.md` line 38 already reports $485M nonaccrual. The 433 in its line 97 table is a **number of performing special-mention/substandard loans**, not $433M of nonaccrual loans. No owner figure should be replaced on that premise.

FLG: Call Report RCFD1403 is $2,989.320M. Subtracting RCFDK044 GNMA nonaccrual of $167.641M gives $2,821.679M; subtracting RCFDC226 HFS nonaccrual $4.236M gives $2,817.443M. June's same calculation is $2,987.555M − $182.108M − $4.980M = $2,800.467M. These reproduce the issuer's rounded HFI figures ($2,817M/$2,800M); its release separately reports HFS ~$4M/$5M. Treat this as a strongly supported arithmetic scope reconciliation, not a bank-versus-issuer error. The release does not explicitly document every GNMA exclusion; do not infer that the memo categories are always disjoint across other banks.

## FLG M3 / NDFI composition flag

Same RSSD 694904 and identical consolidated RCFD definitions in both quarters:

- RCFD2746, RC-C I memorandum 3: $440.610M → $679.072M, **+54.1209%**, versus total loans $61,194.867M → $62,110.348M (+1.4960%). It covers CRE/construction/land-development financing not secured by real estate, included in RC-C items 4 and 9; it is not another additive balance-sheet asset category.
- RCFDJ454, RC-C I9a NDFI loans: $3,457.706M → $4,511.574M, **+30.4788%**. September domestic RCONJ454 is $4,511.572M, $2,000 smaller, confirming the need to retain the selected consolidated prefix.
- The earnings release describes broad C&I growth, including Specialized Industries; it does not specifically reconcile M3. No cheap primary source establishes that the M3 change represents worsening economic risk rather than growth, mix or classification. Retain the existing MI3 guard and owner authority; do not add M3 to NDFI or secured CRE as though nonoverlapping.

BOUNDED CONCLUSION: The key calculations are confirmed with the scope corrections above. AMTB/SBCF AOCI pressure, FLG's worsening provision/earnings context and its M3 step warrant attention within the existing owner process. Improving headline nonaccruals or NCOs for selected names do not establish an all-clear, and no full banking-system or trade conclusion is supported by this bounded verification. No new grade issued.

Completion: Finished bounded verification. Codex/OpenAI runtime; exact serving model unavailable. Repo root and root CLAUDE/AGENTS/USER plus local WALTER Rule 9/CHECKLIST framing were explicitly read. Only this memo written; no owner files, commits, sends or domain launches. No helper processes left running.
