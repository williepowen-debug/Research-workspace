# VLY and EGBN Q3 10-Q reads: six asks, MF criticized table, REG-28 checkpoint

**Read:** 2026-11-06. **Owner:** REGINALD. **Authority:** Will "go", 11:23 ET. **Filings read at SEC 11/06:** VLY 10-Q 9/30/26 acc 0000714310-26-000049, VLY Q2 10-Q acc 0000714310-26-000041, EGBN 10-Q 9/30/26 acc 0001050441-26-000113, EGBN Q2 10-Q acc 0001050441-26-000096. **Call Reports:** Valley National Bank (RSSD 229801), FFIEC CDR, fresh pulls 11/06, seven dates, `use_cache=False`.

## 0. Result

| Item | Read |
|---|---|
| VLY, new finding | **The ~$108M Q2 CRE payment-delay block did not pay off. It is still on the books and was very likely modified again in Q3** (strong inference, §1a) |
| VLY six asks | 2 answered, 1 answered by Call Report tie, 2 partial, 1 not disclosed (§1) |
| VLY correction | My 11/01 "new" NOO 30-89 $0 → $61.4M overstated newness: the line was $70.2M at 12/31 and $63.4M at 6/30/25; $0 at 6/30/26 was the outlier (§1b) |
| EGBN MF criticized | **$211.8M [9/30] vs $284.2M [6/30]; 'weakens if' line ≤ $284M MET.** ⚠️ The Q3 deck says $248M. Issuer documents disagree by $36.2M, unresolved (§2a) |
| EGBN MF reserve | $16.1M vs $6.7M [6/30] |
| REG-28 | **h=0, x=0, u=4, unchanged.** The 10-Q has no subsequent-events disclosure on either 10/27 loan |
| EGBN nonaccrual basis gap (open since 11/01) | **Closed:** the gap is nonaccrual held-for-sale loans |

No score, threshold, gate or trade change. REG-30 no probability change.

## 1. VLY

### 1a. Ask 1: modifications and payment defaults. The Q2 block

**Filed figures ($K, CRE class):**

| Filing, period | Payment delay | Rate reduction | Term extension | Total CRE |
|---|---:|---:|---:|---:|
| Q3 10-Q, three months 9/30/25 | 108,104 | — | 30,252 | 138,356 |
| Q2 10-Q, three months 6/30/26 | **108,184** | 74 | 7,713 | 115,971 |
| Q2 10-Q, six months 6/30/26 | **108,639** | 74 | 7,713 | 116,426 |
| Q3 10-Q, three months 9/30/26 | **140,665** | 41,171 | 4,116 | 185,952 |
| Q3 10-Q, nine months 9/30/26 | **141,113** | 41,227 | 11,698 | 194,038 |

Nine-month less three-month leaves **$448K** of payment delay for H1 2026, against the $108,639K the Q2 10-Q reported for H1. So about $108.2M left the H1 row. Term extension barely moved (H1 $7,713K then, $7,582K now).

**Paid off, or modified again? The Call Report answers it.** RC-C Memo 1 (modified, in compliance) plus RC-N Memo 1 (modified and past due or nonaccrual) tie to the 10-Q's 12-month CRE modified pool:

| Date | MF K160 | Non-MF CRE K161+K162 | RC-N CRE memo lines | Sum | 10-Q CRE pool |
|---|---:|---:|---:|---:|---:|
| 6/30/26 | 23,348 | 110,450 | 5,653 | **139,451** | 139,450 |
| 9/30/26 | 96,892 | 110,499 | 7,718 | **215,109** | **215,109** |

Non-MF series: 9/30/25 **$120.4M**, 12/31/25 **$115.1M**, 3/31/26 **$110.5M**, 6/30/26 **$110.5M**, 9/30/26 **$110.5M** (3/31/25 $232.8M, 6/30/25 $213.3M).

MF was only $23.3M at 6/30, so the Q2 block sat in non-MF CRE. Had it paid off, that line would have fallen by about $108M. It moved +$49K. A loan modified in Q2 and modified again in Q3 leaves the H1 row, stays in the pool and lands in Q3's three-month row, which is the observed pattern.

**Reading (INFERENCE, strong, not loan-matched):** about $108M of Q3's $140.7M payment delays is the same block deferred again, one quarter after an 8-month deferral. Q3's new CRE modifications are then ~$77.8M ($186.0M − $108.2M), which agrees with MF K160 +$73.5M: the Q2 MF 30-59 cohort, as the 11/01 checkpoint inferred from category totals. The filing states none of this. A change in table basis cannot be excluded, and I did not ask the issuer. The near-equal Q3-2025 row ($108.1M, 2-month deferral) suggests the block may be older still; that link is weaker and unproven.

**Why it matters.** My 9/27 report said the test comes "when the deferrals end (~Q1-27 for Q2-26 grants)." If this reading holds, the test did not wait for expiry: the deferral was replaced early. Q3 grants carry a 5-month weighted deferral, which puts the next clock at about Q1 2027.

**Performance:** CRE modified in 12 months $215.109M: current $210.655M (includes nonaccrual), 30-89 $0, 90+ $4.454M. Payment defaults of modified loans, nine months: residential only, $939K; **no CRE row.** A payment delay makes this measure quiet by construction, so a zero here is weak evidence.

**Scale:** pool 0.77% of $28.03B CRE; Q3 payment delays 0.50%. Equity $7.9B. This is a recognition question, not a capital one.

### 1b. Ask 2: CRE past due by property type, the $61.4M

The 10-Q has one "Commercial real estate" class; no property split. MD&A: one $10.9M relationship is the whole 60-89 CRE bucket; a $4.0M loan moved to 90+. The Call Report is the split and ties exactly: NOO F179 $61,398K + MF 3499 $21,719K + OO F178 $320K = **$83,437K** = 10-Q 30-59 $72,568K + 60-89 $10,869K.

**Correction to my 11/01 report.** NOO 30-89 history: 3/31/25 $0, 6/30/25 $63.4M, 9/30/25 $21.2M, 12/31/25 $70.2M, 3/31/26 $40.8M, 6/30/26 $0, 9/30/26 $61.4M. The 11/01 line "New: NOO CRE 30–89 $0 → $61.4M … the Q4 roll candidate" read a lumpy line from its low point. It is still a roll candidate; it is not a new stage. Identity of the $50.5M outside the one relationship: UNKNOWN.

### 1c. Ask 3: the $30.1M construction loan
**Partly answered.** Collateral dependent, $30,127K (first appears; $0 at 12/31/25). Construction nonaccrual without allowance $30,127K, so no related allowance. MD&A: "considered well-secured and did not require a specific reserve … based upon the estimated value of the underlying collateral." **Collateral type, location and appraisal date are not disclosed.** The note says values use third-party appraisals that may be discounted, with no loan-level detail. Construction substandard $108.1M vs $91.2M; construction special mention $38.2M vs $99.8M.

### 1d. Ask 4: allowance by segment
**Segment yes, quantitative versus qualitative no.** Q3 roll-forward ($K):

| Segment | Begin | Net charge-offs | Provision | End | % of loans 6/30 → 9/30 |
|---|---:|---:|---:|---:|---:|
| C&I | 198,910 | (16,388) | **28,991** | 211,513 | |
| CRE incl. construction | 319,068 | (18,375) | **(1,300)** | 299,393 | 1.05 → 0.98 |
| Residential | 48,905 | 26 | (1,555) | 47,376 | 0.82 → 0.78 |
| Consumer | 23,717 | (2,341) | 1,142 | 22,518 | 0.57 → 0.55 |
| Total | 590,600 | (37,078) | 27,278 | 580,800 | 1.13 → 1.09 |

**CRE took a negative provision in a quarter with $18.4M of net charge-offs and $186.0M of modifications.** The filing names the mechanism in words and gives no dollar split: economic forecast, qualitative and specific reserves up, "a decline in quantitative reserves largely within certain commercial real estate loan categories, including construction loans." Under L801 a coverage decline alone is not a predictor; this stays a question, not a finding.

### 1e. Ask 5: the $18.5M NDFI nonaccrual
**Not disclosed.** The 10-Q says only "higher levels of non-accrual commercial and industrial loans." No borrower type, and no use of the NDFI, private-equity or capital-call terms anywhere in the text. C&I nonaccrual $168.1M vs $147.7M. Stays Call Report RC-N Memo 9 only.

### 1f. Ask 6: criticized and classified by class ($K)

| Class | SM 6/30 → 9/30 | Substandard | Doubtful | Total |
|---|---|---|---|---|
| C&I | 197,111 → 212,815 | 439,405 → 417,685 | 46,982 → 45,511 | 683,498 → 676,011 |
| CRE | 1,082,114 → 1,041,205 | 1,760,977 → 1,783,590 | 45,757 → 43,666 | 2,888,848 → 2,868,461 |
| Construction | 99,766 → 38,152 | 91,198 → 108,118 | — | 190,964 → 146,270 |
| **Total** | | | | **3,763,310 → 3,690,742** |

7.17% → 6.94% of total loans, same direction as the release's 7.3% → 7.1%; the level difference is not reconciled. **The total fell, but real-estate substandard + doubtful rose $37.4M, $1,897.9M → $1,935.4M.** The improvement is in the mildest bucket.

### 1g. REG-30
Baseline $511,390K confirmed. No probability change; none requested.

## 2. EGBN

### 2a. MF criticized table, the registered 10-Q-only line

| Income-producing MF, principal | 12/31/25 | 6/30/26 | 9/30/26 |
|---|---:|---:|---:|
| Special mention | 43,201 | 79,228 | **42,685** |
| Substandard | 132,419 | 204,942 | **169,123** |
| Criticized | 175,620 | 284,170 | **211,808** |
| MF book | | 692,772 | 575,445 |
| Criticized % of book | | 41.0% | **36.8%** |
| MF allowance | 7,468 | 6,711 | **16,128** |
| Allowance % of criticized | 4.3% | 2.4% | **7.6%** |

`reports/2026-09-26_CRE_vulnerability_top3.md` §6 line "MF criticized ≤ $284M": **MET** on either figure below.

**⚠️ Unresolved issuer disagreement.** Q3 deck slide 16 (10/21, acc 0001050441-26-000110): MF criticized **$248M, 43.1%**, on a $574.8M book, shown rising from 41%. The 10-Q (11/05): **$211.8M, 36.8%**, falling. They agree at Q2 ($284M on both). Gap at 9/30: **$36.2M**, and it changes the direction. Evidence favours the 10-Q: the deck's own >$10M criticized apartment list sums to $195.4M, leaving $16.4M below $10M, against $5.6M at Q2; the deck figure would need $52.6M. The 10-Q's MF special mention is exactly L02 ($42,685K), so L03 ($36.4M, Other US) is out of special mention. $36.2M is close to L03 or L13 ($35.4M), which would fit one loan being counted in one document and not the other. That identity is a guess. Not reconciled. **Cite the 10-Q figure with this caveat.**

**How the decline happened.** MF book −$117.3M (−16.9%) in Q3. No MF charge-off in Q3 (Call Report, 11/01). No new HFS transfer: the $238.5M nine-month figure equals the six-month figure. Q3 loan-sale gain or loss $0; HFS $49.7M → $13.5M. MD&A credits payoffs, sales, migration and "the payoff in full of certain loans", with no loan-level detail. L03, L13 and L21 left the >$10M list; whether by payoff, upgrade or sale stays UNKNOWN at loan level (wall report §101 question).

**What remains.** Q4 MF maturities **$265.7M, 46.2% of the book** (10-Q chart, unchanged from the deck). MF criticized is still 37% of the book. Weighted DSCR 1.0× (deck). Allowance overall 73% of nonperforming, from 149% at 12/31.

### 2b. REG-28 checkpoint
10-Q signed 11/05, nine days after the 10/27 maturities. **No subsequent-events disclosure and no loan-level mention of L02 or L05.** Absence is u, never x. **h=0, x=0, u=4.** 9/30 baselines confirmed: MF SM $42,685K = L02; construction-class SM $27,722K = L05. New: Q3 income-producing "term extension and principal payment delay" $55,963K matches L11 (Prince George's $56.0M, extended to 12/21) within $37K. Identity by amount, no name.

### 2c. Other
- **Basis gap closed.** Deck $111.1M / $166.0M vs Call Report $136.9M / $179.7M (gaps $25.8M, $13.7M). HFS nonaccrual $25.6M [6/30] and $13.5M [9/30]; deck and 10-Q exclude it (10-Q NPA table footnote 1). Residual about $0.2M each date.
- **Modified in 12 months:** 33 loans. 14 performing $93.1M, 19 nonaccrual $94.9M, so 57% of the $166.0M nonaccrual total. None 30-89 or 90+. Income-producing current $76.7M, nonaccrual $85.0M.
- **Valuation language:** "These updated valuations reflect the rapidly changing commercial real estate market in the D.C. metro area." Issuer warns further actions "could continue to result in elevated credit costs."

## 3. What changes the read

**VLY.** Worse: the 12/31 Call Report shows K161+K162 flat again while the 10-K's rows shift again (a third roll); or that block moves to nonaccrual or charge-off. Better: K161+K162 falls with no matching rise in F183 or charge-offs (real cash exit). These are existing Q4 reads, no new monitor.

**EGBN.** REG-28 and L791 at the Q4 print. The Q4 deck's prior-quarter MF criticized comparative may settle $248M vs $211.8M.

## 4. Trade route

No candidate, TRADE.md §2b. No trigger fired. Will holds `VLY $12P Dec-18-2026 ×1` per the 11/5 capture; card owner UNKNOWN on TRADE.md §2. Facts packeted to TERRY; what they mean for that line is TERRY's. EGBN: not on the book; prior read stands (put OI ~2).

## 5. Verification scope

Read: text extraction of the loan notes and MD&A credit sections of all four filings; EGBN chart g5; deck slide 16 from the saved image. VLY Call Report lines as tabled. K161 and K162 are treated together as non-MF CRE; their sum ties to the 10-Q, and the OO versus other split was not checked against the form. Not read: either Q3 call transcript, EGBN's Call Report at FFIEC today (11/01 pull reused and labelled), the other §6 'weakens if' lines for EGBN (graded at the print, 10/22 catch-up §4).
