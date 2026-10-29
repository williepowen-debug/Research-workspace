# Helper B: Q3 2026 CRE mREIT census, fixed 11-name cohort

**Pulled 2026-10-28, late evening ET.** Read-only. No repo file was edited.

**Method.** I pulled the EDGAR submissions list for all 11 cohort names plus ABR, ACR, FBRT, CMTG, SACH and LFT, covering filings from 9/20 to 10/28. For each Item 2.02 8-K, I read the EX-99.1 release and the supplement text layer. Q2 comparators come from the Q2 8-Ks and from XBRL companyfacts.

**Tiers.** PRIMARY-READ means I read the filing. DERIVED means my own arithmetic on PRIMARY-READ inputs. SECONDARY means a named outlet.

**Supplement caveat.** The supplements are mostly page images. I read only their HTML text layer, so I did not check chart-only figures (trap #7 shape).

## 1. Who has reported (as of 10/28 evening)

| Ticker | Q3 reported? | Release date / source | Next date if not reported (tier) |
|---|---|---|---|
| LADR | YES | 8-K 10/16 (EX-99.1); 10-Q filed 10/26. PRIMARY-READ | — |
| TRTX | YES | 8-K and 10-Q 10/26. PRIMARY-READ | — |
| BRSP | YES | 8-K 10/27; 10-Q 10/28. PRIMARY-READ | — |
| KREF | YES | 8-K and 10-Q 10/28. PRIMARY-READ | Call 10/29 11:00 ET |
| BXMT | NO | — | **Thu 10/29**: earnings presentation and 10-Q, call 9:00 ET. Date announced by the company 10/7 (SECONDARY, Finviz/BusinessWire repost) |
| STWD | NO | — | **Fri 11/6** before the open, call 10:00 ET. Company release 10/12 (SECONDARY, Finviz repost) |
| ACRE | NO | — | **Fri 11/6** before the open, call 10:00 ET. Company release 10/23 (SECONDARY, Finviz/Placera repost) |
| NREF | NO | — | **~Thu 11/5** before the open, per Earnings Whispers ("confirmed"). No company release found. SECONDARY / UNCONFIRMED |
| RC | NO | — | **NOT ANNOUNCED.** Estimates conflict (EW lists both 11/5 and 11/9 after close). Q3-25 precedent: 11/6. UNCONFIRMED |
| GPMT | NO | — | **NOT ANNOUNCED.** Pattern suggests early Nov (Q3-25: 11/5 after close). UNCONFIRMED |
| ARI | NO (in liquidation) | — | No Q3 release expected. Form 25 filed 10/27; last NYSE day 11/6; SEC deregistration ~11/9; liquidating trust files only 10-K and 8-K (8-K 10/16, PRIMARY-READ) |

**Reporters so far: 4 of 11** (LADR, TRTX, BRSP, KREF). **Non-reporters: 7**, of which ARI will never report on the standard basis.

## 2. Reporters: book value, credit, dividend, actions

### BVPS, 6/30 → 9/30

| Ticker | Basis | 6/30/26 | 9/30/26 | Δ | Tier | Corporate-action check |
|---|---|---|---|---|---|---|
| KREF | GAAP common BVPS (company) | $10.24 | $10.14 | **−$0.10 / −1.0%** | PRIMARY-READ (Q2 and Q3 supplements) | No split or ROC. Buybacks were accretive: 1.6M shares at $7.26 in July. Q3 net loan losses were −$0.11/sh |
| TRTX | GAAP BVPS (company) | $10.95 | $10.85 | **−$0.10 / −0.9%** | PRIMARY-READ | No split or ROC. Bridge: credit loss −$0.11; buybacks +$0.04 (1.16M shares at $8.00) |
| BRSP | GAAP BVPS (company) | $6.81 | $7.08 | **+$0.27 / +4.0%** | PRIMARY-READ | Up because of the GAAP gain on the NNN industrial sale plus buybacks |
| BRSP | **Undepreciated** BVPS (company) | $8.10 | $7.87 | **−$0.23 / −2.8%** | PRIMARY-READ (supplement bridge) | Bridge: buybacks +$0.06; RE impairment −$0.15; change in CECL −$0.12; earnings less dividends −$0.02. **The sign flips with the basis** |
| LADR | GAAP BVPS, **DERIVED** = total shareholders' equity / shares outstanding | $11.27 ($1,429.3M / 126.87M) | $11.61 ($1,463.1M / 125.99M) | **+$0.35 / +3.1%** | DERIVED from PRIMARY-READ balance sheets | Q3 gain on a Jacksonville FL office sale. LADR's own undepreciated BVPS is in the IR supplement, which I did not read |

**Count, per the brief (no cohort verdict):**
- **GAAP basis: 2 of 4 reporters showed BVPS declines**, KREF −1.0% and TRTX −0.9%. Both are about −$0.10/sh.
- BRSP declined **only on its undepreciated basis** (−2.8%); its GAAP BVPS rose 4.0%.
- LADR rose 3.1% (derived GAAP).
- **ARI is excluded from any erosion count.** Its distributions are return of capital (see §3).

### Credit, office, risk ratings, dividend, actions

| Ticker | Q3 provision | Allowance 9/30 (vs 6/30) | Office exposure | Risk-rated 4/5, nonaccrual | Q3 dividend (declared) vs Q2 | Strategic / capital action |
|---|---|---|---|---|---|---|
| KREF | Provision $1.4M, plus a $5.2M loss on a held-for-sale loan. **Realized write-offs $155.9M ($2.70/sh)**, so Distributable loss was −$2.64/sh. The write-offs drew down the reserve: allowance fell, but BVPS barely moved because Q2 had already taken the hit | $187.4M (vs $291.9M 6/30; $201.9M 12/31). XBRL PRIMARY-READ | **24% all-office** (Legacy 18% + Recent 6%) vs **21% at 6/30**. Office outstanding $759.3M of $3,151.5M | **RR5 $329M** principal (Minneapolis office $194M, Chicago office $91M, Carrollton MF $44M); **RR4 $0**. 2Q was RR5 $674M / RR4 $42M. Three resolutions, no downgrades. ⚠️ A chart-layer string reads "15%" at RR5, which does not reconcile to $329M / $3.15B (10.4%); unchecked shape | $0.10, flat vs Q2 $0.10 (that $0.25 → $0.10 cut was in Q2). No October declaration seen | Strategic review (opened 7/21) **ongoing**: $1.46M of review expenses in Q3, no outcome. Redeemed both CLOs ($564M IG). July buyback |
| TRTX | Credit loss expense $8.6M GAAP (−$0.11/sh); $13.0M including REO-related items in the DE bridge | $76.1M total, 147 bp of commitments (vs $80.7M, 179 bp). Balance-sheet allowance $74.0M (vs $77.8M) | **7.9%** office in the property-type mix (supplement text layer; basis not confirmed beyond that) | **RR4 $120.1M** (vs $162.3M 6/30); **RR5 $0** (both quarters). WA risk rating 3.0, unchanged | $0.24 declared **9/17**, flat. No October declaration | **New $50M buyback authorized 10/26**, doubling the prior program. Closed the $1.0B FL8 CRE CLO 10/2 |
| BRSP | Change in CECL ≈ +$7M (general reserve $100M → $107M); no specific reserve. RE impairment −$0.15/sh (undepreciated basis) | $106.3M (XBRL) vs $98.7M; company states $107M ($0.86/sh, 332 bp) | **19% office** of the loan book ($572M of $3,082M) vs 20% at Q2. NNN office is extra: about 16% of net-lease and other RE | **RR4 watch list $187M, 6% of loans** (vs $136M, 5%; +38%). Two office loans downgraded to RR4 (Blue Bell PA, $30M + $30M). No RR5. RR4/5 CECL is $43M of the $107M | $0.16 declared **9/14**, flat. No October declaration | Sold its largest asset (NNN industrial). FL4 CLO closed 10/16. **Activist: CW Investment Advisers / CWRE SSF (Hon Kit Shing, Andrew Freedman), 8.7%, switched 13G → 13D on 9/29** after the board twice refused an ownership-limit waiver. The filing says shares trade at about 57% of undepreciated book (13D PRIMARY-READ) |
| LADR | Provision $13K. **Charge-off $3.5M** (Minneapolis office loan) | $43.6M loans + $0.7M unfunded = $44.3M (vs $47.1M 6/30). PRIMARY-READ 10-Q | **21.7% of HFI loans** ($639.5M office of $2,951.5M). DERIVED from the 10-Q table | **Nonaccrual $60.6M** (one hotel $50.7M, one office $9.9M), vs $129.7M at 12/31. LADR does not publish an RR4/5 table in the release | $0.23, flat | Sold the Jacksonville FL office, adjusting the gain by $34.3M of prior depreciation (a Florida item, so CORAL-relevant) |

## 3. Non-reporters: actions since 9/26 (EDGAR 8-K list, PRIMARY-READ unless marked)

| Ticker | Item |
|---|---|
| ARI | **Initial cash liquidating distribution of $4.10/sh**, declared 10/9, record date 10/20, paid **10/29**. **Ex-date 10/30**, with due bills from the record date through 10/29 (SECONDARY: company release reposted on Finviz; not filed as an 8-K). The proxy range was $3.70–4.00. **⚠️ The ex-date 10/30 price drop of roughly $4.10 is return of capital, not erosion (trap #1).** Form 25 filed 10/27; liquidating trust to follow (8-K 10/16 PRIMARY-READ). Excluded from erosion counts |
| GPMT | 8-K 10/5: amended JPM repo (facility up to $727.0M; assets moved over from the Citi and Morgan Stanley facilities; **Minimum Interest Expense Coverage covenant modified**). 8-K 10/6: reverse-split mechanics (already logged). No review outcome |
| ACRE | 8-K 10/9: **covenant relief.** Minimum tangible net worth cut from $500M to $400M on the Citi, Morgan Stanley and Wells repo facilities (Wells adds 80% of future equity proceeds). 8-K 9/22: sold a North Carolina REO office for $64M (closed 9/18) |
| RC | 8-K 9/28: closed $225M of 10.00% senior secured notes due 2031; redeemed $350M of 4.50% notes due 2026. The 9/18 covenant loosening was already logged |
| BXMT, STWD, NREF | No 8-K 9/20 to 10/28 (Forms 4 and 144 only). **Weak negative:** a dividend can be declared by press release without an 8-K |

**Dividend declarations in October:** none found for any cohort name. Cohort Q3 dividends were declared in mid-September (TRTX 9/17, BRSP 9/14, and per the prior census). ARI's $4.10 is a liquidating distribution, not a regular dividend. **This is the weak form:** EDGAR 8-Ks plus the releases read, with no IR-site check per name.

## 4. Outside the cohort (since 2026-09-26)

| Ticker | Finding | Tier |
|---|---|---|
| FBRT | Reported Q3 on 10/28. Dividend **$0.20, flat** (2026 Q1–Q3 all $0.20; the cut from $0.355 predates the window). Fully converted BVPS $14.26 vs $14.24 (+$0.02); buybacks added $0.55. **Provision $43.1M** (core $37.7M: specific $38.7M, general −$1.0M) vs Q2 $7.2M. Allowance $71.9M vs $54.5M. **Watch list 13 loans, $333.6M: 6 RR4 and 7 RR5.** Buyback extended to 12/31/27 | PRIMARY-READ |
| LFT | 8-K 10/6: regained NYSE $1 minimum-price compliance. **No new dividend action seen** (the 9/18 suspension predates the window) | PRIMARY-READ |
| SACH | 8-K 10/23: annual meeting only (directors, auditor, say-on-pay) | PRIMARY-READ |
| ABR, CMTG, ACR | No 8-K 9/20 to 10/28 (13G/A and Form 4 only). No cut or strategic action found; weak negative. ABR typically declares with Q3 earnings (late Oct / early Nov), which has not happened yet | PRIMARY-READ (absence) |

**Result: no outside-cohort dividend cut or strategic action found since 9/26.** Weak form: 8-K list plus one news search.

## 5. Caveats

1. **The BRSP basis flip** is the main finding to carry forward. GAAP +4.0% and undepreciated −2.8% are both correct, and they point in opposite directions.
2. **LADR BVPS is my own derivation**, not a company figure. LADR's undepreciated BVPS was not read.
3. **KREF write-offs vs book value.** The $155.9M Q3 write-offs are realized recognition of losses reserved earlier, so they barely touch Q3 BVPS. Do not read "−1.0% BVPS" as "light quarter." Distributable loss was −$2.64/sh.
4. **KREF office share rose (21% → 24%) while legacy office was flat at 18%.** The cause is a shrinking book ($1.2B of repayments) plus a new $77.5M Frisco office origination. This is a denominator effect (trap #6).
5. **Cohort read through 10/28 covers only 4 of 11.** BXMT, the largest office-exposed name, reports 10/29.

Sources: EDGAR accessions 0001628280-26-067907 (KREF Q3), 0001628280-26-049023 (KREF Q2), 0001630472-26-000031 (TRTX), 0001717547-26-000072 (BRSP), 0000921895-26-002666 (BRSP 13D), 0001577670-26-000050 / -000055 / -000032 (LADR), 0001562528-26-000035 / -000025 (FBRT), 0001193125-26-424253 (ARI), 0001628280-26-065542 / -063051 (ACRE), 0001703644-26-000038 (GPMT), 0001628280-26-063725 (RC), 0001104659-26-114127 (LFT), 0001682220-26-000067 (SACH); XBRL companyfacts.
Web: https://finviz.com/news/400834/apollo-commercial-real-estate-finance-inc-declares-initial-cash-liquidating-distribution ; https://finviz.com/news/400067/blackstone-mortgage-trust-announces-third-quarter-2026-earnings-release-and-conference-call ; https://finviz.com/news/401414/starwood-property-trust-announces-date-for-third-quarter-2026-earnings-release-and-conference-call ; https://finviz.com/news/407416/ares-commercial-real-estate-corporation-schedules-earnings-release-and-conference-call-for-the-third-quarter-ended-september-30-2026 ; https://www.earningswhispers.com/stocks/nref ; https://www.earningswhispers.com/stocks/rc
