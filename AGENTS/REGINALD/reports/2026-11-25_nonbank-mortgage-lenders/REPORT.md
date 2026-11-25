# Which banks lend to the nonbank mortgage companies (D:L1291, class C9)

**Written:** 2026-11-25 16:15 ET. **Desk:** REGINALD, Claude Code, Opus 5.5. Public filings only, $0. **Nothing moved:** no score, band, gate, threshold, prediction or card. Builds on and corrects `domain/WAREHOUSE_EXPOSURE.md` (4/14).

## 1. The answer

1. **In my 14, the exposure is Western Alliance, then Customers.** Western Alliance reports $7,029M of warehouse lines plus servicing-right (MSR) loans [9/30], 10.7% of loans and 87.6% of Tier 1. Northpointe and Texas Capital are larger against capital on their own 10-Q figures (§4).
2. **The call-report line is wider than the question.** Memo 10.a also holds mortgage-REIT credit (M&T's own footnote) and, INFERRED, note finance at Western Alliance. Where a 10-Q gives the narrower figure it is 65% to 86% of the line (5 banks). Never quote the line as "warehouse".
3. **Reported credit is clean.** Western Alliance: $7,029M all current, none special mention or classified, allowance $6.7M (10bp). Customers: all current. BankUnited and First Horizon: none or $1M late. Texas Capital: none late. This says nothing about fraud or a borrower failure; every figure is the bank's own.
4. **No US regional bank is named by a borrower.** PennyMac names every repo lender: large banks, foreign banks and Atlas SP. UWM names Citibank and Goldman for its MSR lines. The 4/14 finding repeats on the Q3 filings I could search (7). It is a disclosure result, not proof of absence: Rocket, Onity, Finance of America and UWM's warehouse tables are anonymous, and Freedom, Planet, Provident and CrossCountry file nothing at SEC that I found.
5. **MSR debt did not rise across the board; it moved to weaker names** (§5): four listed borrowers $6,786M → $6,572M (−3.2%) from year end; without Rocket $3,811M → $5,632M (+47.8%).

## 2. Data

| Source | Read |
|---|---|
| FFIEC bulk Call Reports 9/30, 6/30/2026, 12/31/2025 | downloaded 11/25 ~16:08 ET, page "Call Updated: 11/14/2026"; 4,267 filers at 9/30; sha256 9/30 `ffe88345…a3a2` and 6/30 `0a375473…e1ad` match my 11/17 report; 12/31 `0ed48bb9…9995` |
| Memo 10.a (PV05), RC-L 1.e.(3)(a) unused (PV12), 9.a (J454), loans 2122, Tier 1 8274 | consolidated (RCFD) first, so 031 filers differ from `NDFI_COHORT.tsv` (RCON). Western Alliance 10.a $10,767.7M ties to the ledger and to its 10-Q ($10,768M) |
| Coverage | 10.a is collected at $10B+ in assets (88 FR, 2023-12-27, 2023-28473). 146 of 4,267 file it; 13 filers over $10B show none, listed in `rank_output.txt` |
| 10-Qs for 9/30/2026 (EDGAR, fetched 11/25) | WAL 0001628280-26-068599 · CUBI 0001488813-26-000105 · BKU 0001504008-26-000091 · MTB 0000036270-26-000060 · ZION 0000109380-26-000127 · FLG 0000910073-26-000084 · FHN 0000036966-26-000199 · TCBI 0001077428-26-000080 · MBIN 0001104659-26-123854 · NPB 0001336706-26-000091 · BANC 0001628280-26-071683 · ASB 0000007789-26-000260 · PFSI 0001104659-26-121982 · UWMC 0001783398-26-000140 · RKT 0001628280-26-068434 · ONIT 0001628280-26-071166 · FOA 0001628280-26-071678 · LDI 0001831631-26-000116; also VLY, EGBN, AMTB, HBAN, CFG, SSB, SBCF, AX, PMT |
| Not read | FFIEC instruction book for 10.a (ffiec.gov 403, not retried; FDIC copy read is June 2024 and predates 10.a; its item 9.a text covers loans to mortgage companies that originate, warehouse or service, and REITs). Fitch's review (Will's read, relayed). Full 10-Qs: searched by term and by table, not cover to cover |

## 3. My 14 and the bank desks, 9/30/2026 ($M)

| Bank | Memo 10.a | 12/31/25 | % loans | % Tier 1 | Unused 10.a | Bank's own narrower figure (10-Q) | Not disclosed |
|---|---:|---:|---:|---:|---:|---|---|
| **WAL** | 10,768 | 10,101 | 16.3 | 134.2 | 2,002 | **7,029 "mortgage finance" = warehouse lines + MSR loans (10-K 2025 definition): 10.7% of loans, 87.6% of T1** | warehouse vs MSR split; borrowers; the other 3,739 in 10.a (note finance inside it INFERRED); NDFI nonaccrual 122.5 is NOT in mortgage finance (nonaccrual there: none) |
| **CUBI** | 2,079 | 2,347 | 11.2 | 85.1 | 1,906 | 1,401 at fair value, no allowance by election; unfunded 1,681; 7.6% / 57.3% | the other 679; MSR loans; borrowers |
| **BKU** | 1,211 | 1,051 | 5.1 | 36.6 | 904 | 932 warehouse (728 at YE, +28%); 3.9% / 28.2% | other 279; borrowers; ACL not separate from residential (0.17% together) |
| **MTB** | 6,939 | 5,610 | 4.8 | 34.9 | 5,568 | footnote: REIT facilities + warehouse + MSR-secured; commitments 10,197 → 12,507 | the three-way split |
| FLG | 1,136 | 680 | 1.8 | 13.8 | 473 | none found by search | what the +67% since year end is |
| HBAN | 3,557 | 3,294 | 1.8 | 13.7 | 1,068 | none found by search | all |
| EGBN | 136 | 182 | 2.1 | 11.0 | 30 | none found by search | all; NDFI nonaccrual 9.5 |
| AMTB | 50 | 0 | 0.7 | 4.9 | 35 | 49.5 to NDFIs in total | — |
| ZION | 335 | 352 | 0.5 | 4.0 | 223 | 10-Q class 335, **nonaccrual 9, all of the bank's NDFI nonaccrual** | borrower type |
| VLY · CFG · SSB | 262 · 286 · 70 | 232 · 308 · 31 | 0.5 · 0.2 · 0.1 | 3.9 · 1.4 · 1.0 | 444 · 563 · 56 | none found by search | all |
| SBCF · **OZK** | 0 (129K) · **0** | 2 · — | 0 | 0 | 0 | OZK files 0 in 10.a and 0 unused | — |

Side list: **NexBank** (not an SEC filer) 10.a 1,285, 14.8% of loans, **110.9% of T1**. Preferred Bank is under $10B, no split.

## 4. Outside my list, for scale

| Bank | 10.a $M | % T1 | 10-Q narrower figure |
|---|---:|---:|---|
| Northpointe (NPB, under $10B, no 10.a) | not filed | 9.a 4,206 = 582.7% of T1 | Mortgage Purchase Program 4,201 (3,425 YE): nearly all of 9.a |
| Merchants Bank of Indiana (MBIN) | 7,064 | 296.5 | warehouse repo 1,902 (+19% YTD); MSR-secured revolvers rising, not sized; has credit protection on a $1.2B warehouse pool |
| Axos | 6,253 | 231.8 | no warehouse figure found; 10.a +75% since YE (3,574): composition UNKNOWN |
| Texas Capital (TCBI) | 6,328 | 175.3 | mortgage finance 5,442 (6,064 YE), bought-and-held 10 to 20 days; 150.7% of T1 |
| First Horizon (FHN) | 4,669 | 56.6 | loans to mortgage companies 3,869 (4,703 YE); 46.9% of T1; net charge-off 0% |
| Goldman Bank USA · Morgan Stanley Bank · JPMorgan · Citi · Wells | 48,367 · 32,390 · 72,166 · 43,553 · 42,545 | 88.7 · 76.9 · 24.3 · 28.3 · 29.7 | not read; the line surely holds far more than warehouse here |

System: 10.a $357.2B [12/31/25] → $378.9B → **$393.7B** [9/30], +10.2% YTD. Four banks hold 52.5%, ten 79.1%. Eleven filers are over 50% of Tier 1 (NexBank, Banc of California and EverBank among them); the median $10B+ filer is 0.75%. **Concentrated, not broad.**

## 5. The borrowers' side ($M)

| Borrower | MSR-secured debt 12/31/25 → 9/30/26 | Lender named | Terms that matter |
|---|---|---|---|
| **UWM** | **1,200 → 2,290 (+91%)** | Citibank 900 → 1,415 of 2,000, **uncommitted**, matures 6/15/2027; Goldman Bank USA 300 → 875 of 1,250, **uncommitted**, draw to 3/20/2028 | net-worth, liquidity, leverage, net-income covenants; in compliance |
| Onity | 1,285 → 1,701 (+32%) | not named in the table | cross-default; in compliance |
| PennyMac (MSR notes only) | 1,326 → 1,641 (+24%) | trust notes; repo lenders named | MSRs pledged 7,968 → 10,783; **committed spare capacity 1,486 → 678, uncommitted 3,368 → 7,671**; three quarters of repo matures inside 90 days |
| Rocket | 2,975 → 940 (−68%) | none | cross-default across facilities; in compliance |
| Warehouse lines | UWM 8,912 → 7,651 (−14%); Rocket 13,851 → 12,042 (−13%) | anonymous | falls with volume |

HOMER opened the PennyMac 10-Q at 16:13 ET: hedge settlements used $1,349.8M of cash in nine months and servicing advances $240.5M, so hedges dominate but advances are not zero; its lender-by-lender table and a $94.3M cushion over the Fannie and Freddie liquidity requirement ($287.0M [6/30]) are HOMER's (PIPELINE, packet 11/25), not re-run. These tables fit it: MSR lines up, warehouse lines down. **Freedom's January 2027 maturity is $540M** (HOMER's correction).

**The rate direction has turned since the filings:** 10-year 5.29% [9/30] → 4.92% [11/23, FRED]. Falling rates cut MSR collateral values and return hedge cash. The 9/30 tables cannot show which side won.

## 6. Who would be hit, in order (INFERRED)

Warehouse lines are short, hedged and secured by salable agency loans; the loss most often cited there is fraud such as double pledging (general knowledge, not sourced here). **MSR loans are the leverage-sensitive part:** Level 3 collateral, an agency that can take the servicing, and several lenders on one borrower. Named MSR lenders are Citi, Goldman and the PennyMac consortium, not my 14. Western Alliance, M&T and Merchants say they make MSR loans and do not size them. For Western Alliance the nearer effects are volume and deposits (warehouse clients' deposits, the rate-linked cost WAL owns), not a loan loss.

## 7. Forward view (unscored, not registered)

| Call | Odds | Horizon |
|---|---:|---|
| No bank in my 14 reports a nonaccrual or charge-off in its mortgage-warehouse or MSR class | ~90% | Q4 prints and 10-Ks, to about 3/1/2027 |
| UWM's two MSR lines are at or above $2,290M at 12/31 | ~50% | UWM 10-K, about Feb 2027; rates fell, so I do not lean |

**Why:** zero past due at the disclosing banks, 0% charge-off at First Horizon, issuers in compliance at 9/30. **Alternative:** one B or BB- borrower breaches a net-income or leverage covenant, cross-default spreads it across lenders, and MSR lines are cut first. **What would change my mind:** a covenant waiver or amendment in an 8-K; an uncommitted MSR line reduced or not renewed; any special mention in Western Alliance's mortgage finance row (0 now); a lender naming a mortgage company in an impairment note.

**For TERRY (WQ-696 line):** no investment implication on its own. It ranks exposure, not loss; the most exposed listed banks (Northpointe, Merchants, Texas Capital, Western Alliance, Customers) show no late loans, and the stress mechanism points at MSR lenders that are mostly too large to move on it. Unknown: MSR share at Western Alliance, M&T, Merchants.

## 8. Corrections to my own April study

| Claim (4/14) | Now |
|---|---|
| "Atlas SP $6.9B = 78% of PFSI's warehouse book" | **WRONG.** The table is *amount at risk* = collateral pledged less the amount advanced, PennyMac's exposure to its lenders, and that row is four firms. Loans: Atlas alone **$1,648M of $8,098M repo (20%) [9/30]**, $3,151M at YE; Bank of America $1,788M is larger |
| "Transmission lands at Apollo" | withdrawn as sized on that figure; Atlas is one lender of about a dozen |
| "PFSI committed capacity $460M → $1.5B, stress signal" | it is AVAILABLE committed capacity; now $678M |
| "WAL ~$9.2B mortgage warehouse (within SSFA)" | superseded by $7,029M, warehouse plus MSR, at the issuer |
| Zero US regionals named | stands, with the limit in §1 item 4 |

## 9. Verified, inferred, unknown

**VERIFIED at primary:** every dollar in §3 to §5 from the call-report files or the 10-Q tables; ratios by `rank.py` and `calc.py`. **INFERRED:** note finance sits in Western Alliance's 10.a; §6 ordering; that the big banks' 10.a is mostly not warehouse. **UNKNOWN:** MSR share anywhere but UWM, Rocket, Onity; every bank-to-borrower pair for my 14; uncommitted lines (not in RC-L commitments by INFERENCE); foreign branches and Atlas SP (no Call Report); Freedom, Planet, Provident, CrossCountry lenders; whether any bank holds the same loan collateral twice.
