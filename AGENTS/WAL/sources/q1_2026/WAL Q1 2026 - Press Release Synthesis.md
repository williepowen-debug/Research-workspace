# WAL Q1 2026 — Press Release Synthesis

*Source: `Press-Release-3-31-2026-Final.pdf` (20 pp, 13pp of tables on pp7-19)*
*Synthesized: Apr 24, 2026. Pair-doc to `WAL Q1 2026 - Transcript Synthesis.md`.*
*Rule: Signal-only extraction. Numbers, table cells, and management phrasings preserved with page pins. Cut ledger at end.*

---

## ⚠️ Known gaps in this synthesis (caught on second read — flagged for deck pass)

This document was drafted on a single read and missed or under-weighted the following. Each will be addressed in the deck synthesis pass and integrated back here if the deck doesn't fully cover:

1. **Securities carry-trade signature not called out.** Investment securities avg balance +$4.7B YoY at 4.59% yield vs 1.92% cost of funding = 267bps carry spread on new money. A material share of what §5 frames as operational NIM expansion is in fact a carry/positioning trade — same signature as OZK's $1.44B program but 3-4x the size. §5 and §8 should be reconciled.
2. **Loan servicing revenue $23M YoY swing under-weighted.** Q1-25 +$21.8M → Q1-26 -$1.3M, while MSR on balance sheet grew $275M YoY. Growing MSR book with negative servicing revenue = possible MSR mark-down or hedge losses. A $23M swing is ~12% of Q1 GAAP net income. Listed as "still open" in §9 but deserved investigation-flag treatment.
3. **Gov-guaranteed mortgage HFS magnitude under-reported.** $3.9B HFS book with $288M 90d PD gov-guaranteed residential and $94M 30-89d PD. No credit risk to WAL but demonstrates active warehouse participation. Relevant to V3 warehouse thesis — WAL IS a meaningful warehouse lender, mostly to gov-guaranteed paper. §8 mentions composition but doesn't emphasize.
4. **Provision decomposition not done.** $213M Q1-26 provision decomposes approximately as: $126M LAM + $0 Cantor (utilized existing reserve) + $60M covering ex-fraud NCOs + unfunded build + **~$27M of quiet general ALL build**. The ALL build is not called out anywhere in the synthesis. Small dollar amount but directionally interesting vs cohort.
5. **Juris banking context thin.** First quarter Juris shows up materially in BOTH "other non-interest expense" AND "service charges and fees" — roughly opex-neutral but adds revenue base. No segment-level size disclosed. Referenced in §5 and §10 but not analyzed as a strategic shift.

There may be additional gaps. Second-read caught these; third-read and deck cross-check will catch more.

---

## TL;DR — What this document adds beyond the transcript

Three findings that were NOT surfaced in transcript:

1. **Asset-quality leading indicators worsening while lagging indicators improve.** 30-89d PD still accruing **+$49M QoQ to $157M (+45%)**; Special mention loans **+$78M QoQ to $403M (+24%)**. Meanwhile nonaccrual, classified, and classified-to-Tier-1 all improved. The "core asset quality stable" narrative only holds if you ignore the forward-looking buckets. (p13)
2. **$7.9B credit-linked-note reference pool** — WAL's SSFA/capital-relief program. Declining: $8.5B Mar-25 → $8.1B Dec-25 → $7.9B Mar-26. Allowance on the pool $11.2M (kept in ACL). Adjusted ACL/HFI ex-CLN = 1.00%. **V3 data point, directionally surprising — the program is shrinking.** (p4)
3. **CRE non-owner occupied charge-off $27.7M** — largest in 5 quarters, not labeled fraud. Accounts for half the "ex-fraud" $56M NCO figure. "Ex-fraud underwriting clean" needs this asterisk. (p12)

Plus 11 confirmations / refinements detailed below.

---

## Headline box (p1)

| Metric | GAAP | Adjusted |
|---|---|---|
| Net income | $189.2M | $251.3M |
| EPS | $1.65 | $2.22 |
| PPNR | $444.5M | $394.0M |
| NIM | 3.54% | — |
| Efficiency | 55.8% | 47.5% (adj for deposit costs) |
| BVPS | $67.03 | — |
| TBVPS | — | $61.14 |

CEO quote pinning language (p1): *"solid first quarter results featuring robust deposit growth, net interest margin expansion, and core earnings momentum, while taking decisive action to resolve two fraud-related credits, partially offset by gains from a series of well-executed security sales."*

Note — "decisive action" framing. Paired with "two fraud-related credits" phrase. Same language Vecchione used on the call.

---

## 1. The Two Fraud Credits — detail not in transcript (p3, p5, p12, p19)

### Non-GAAP reconciliation math (p19 — the authoritative version)

```
Net charge-offs (GAAP):   $208.5M
 less: LAM charge-off     ($126.4M)
 less: Cantor charge-off  ($26.1M)
Net charge-offs adjusted:  $56.0M
Avg HFI loans:             $58,184M
Adjusted NCO ratio:        0.39% annualized
```

### The LAM / Cantor asymmetry (p18)

**Earnings reconciliation adds back LAM only, NOT Cantor:**
- GAAP NI $189.2M + LAM provision $126.4M − Sec gains $50.5M − Tax effect $13.8M = Adj NI $251.3M.
- Cantor does NOT appear in the EPS bridge. Why: Cantor's $26.1M came from a specific reserve previously established in Q4 25 — it was already expensed. Only the utilization (moving from reserve to charge-off) happened this quarter. **LAM was a fresh hit; Cantor was a bookkeeping release.**

### Cantor residual position (p13 footnote)

*"Includes senior liens acquired to protect the Company's position with respect to its Cantor Group V loan of $13 million as of March 31, 2026."*
- $13M senior liens sitting in nonaccrual bucket as of Q1 26.
- Implication: WAL expects to recover via collateral; liens acquired to block other creditors.
- Does NOT disclose explicit residual balance (transcript / Q4 25 math: $98M outstanding − $26.1M charge = ~$72M residual carry).

### What's NOT in the press release (still open for deck / 10-Q)

- Collateral description / appraisal dates for either credit.
- Inventory of other Leucadia-era credits (if any).
- Legal recovery timing / litigation status.

---

## 2. Asset Quality — the mixed-signal story (p13)

**Five-quarter trajectory, ranked by what Vecchione emphasized first to last:**

| Bucket | Q1-25 | Q2-25 | Q3-25 | Q4-25 | Q1-26 | QoQ | YoY |
|---|---|---|---|---|---|---|---|
| Nonaccrual loans ($M) | 451 | 427 | 522 | 500 | **492** | -$8M ✅ | +$41M |
| Nonaccrual / HFI | 0.82% | 0.76% | 0.92% | 0.85% | **0.83%** | -2bps ✅ | +1bp |
| Classified on accrual ($M) | 693 | 615 | 476 | 450 | **455** | +$5M | -$238M ✅ |
| Classified assets ($M) | 1,195 | 1,261 | 1,129 | 1,088 | **1,070** | -$18M ✅ | -$125M ✅ |
| Classified assets / total | 1.44% | 1.45% | 1.24% | 1.17% | **1.08%** | -9bps ✅ | -36bps ✅ |
| Repossessed ($M) | 51 | 218 | 130 | 137 | **123** | -$14M ✅ | +$72M |
| **90d PD still accruing ($M)** | 44 | 51 | 49 | 66 | **56** | -$10M ✅ | +$12M |
| **30-89d PD still accruing ($M)** | 182 | 175 | 196 | 108 | **157** | **+$49M 🔴** | -$25M |
| **Special mention ($M)** | 460 | 444 | 292 | 325 | **403** | **+$78M 🔴** | -$57M |

**The read:** Vecchione led with the *improving* lagging buckets (nonaccrual, classified, ratios). He did NOT address the two *leading* buckets that turned sharply negative this quarter.

- 30-89d still accruing +45% QoQ off a Dec-25 trough.
- Special mention +24% QoQ off a Sep-25 trough.
- Both are the stages BEFORE criticized → classified → nonaccrual → charge-off migration.
- Q4-25 was the best quarter of the last 5 on both metrics. Q1-26 reverses that.
- Nonaccrual cross-check: $492M ex-Cantor-liens ($13M) = $479M true nonaccrual. Nonaccrual/HFI ratio ex-Cantor = 0.81%.

**Classified assets / (Tier 1 + ACL) regulatory ratio** (p5, p8): **13.0% Mar-26 vs 13.3% Dec-25 vs 15.9% Mar-25.** Regulatory-lens improvement confirms lagging indicator direction.

### CRE Non-Owner Occupied charge-offs — the under-narrated line (p12)

| Quarter | CRE-NOO Charge-off | C&I Charge-off | Note |
|---|---|---|---|
| Q1-25 | $14.5M | $13.0M | — |
| Q2-25 | $0.2M | $17.0M | — |
| Q3-25 | $12.9M | $12.4M | — |
| Q4-25 | $10.7M | $28.9M | — |
| **Q1-26** | **$27.7M** | **$181.4M** (LAM+Cantor+$28.9M) | 5-quarter high on CRE-NOO |

- CRE-NOO 5-quarter cumulative charge-offs: **$66.0M on ~$10.3B book = ~64bps annualized TTM**.
- Ex-fraud ($56M) NCO composition Q1-26: **$27.7M CRE-NOO (49%) + $28.9M other C&I (51%)**.
- "Ex-fraud NCO clean at 0.39%" narrative needs this asterisk: CRE-NOO charge-offs are elevated and accelerating.
- Construction + Residential RE charge-offs: **$0 all 5 quarters**. That's the actually-clean book.
- Nothing in press release identifies the CRE-NOO borrower(s). Deck or 10-Q only.

### Allowance detail (p12)

- ALL: **$461.1M** funded + **$53.3M** unfunded commitments = **$514.4M total ACL**. Flat vs $510.2M Q4-25 (funded was $460.6M + unfunded $49.6M).
- ALL / HFI ratio: 0.78% (flat QoQ, up from 0.71% Mar-25 = +7bps YoY build).
- ALL / HFI adjusted (ex CLN reference pool): **1.00%** Mar-26, 1.01% Dec-25, 0.92% Mar-25. Adj numerator includes $11.2M allowance on CLN pools.
- **Coverage ratios**: ALL / nonaccrual = **94%** (vs 86% Mar-25). ACL / nonaccrual = **105%** (vs 94% Mar-25). Coverage has BUILT through 2025 — $46M additional coverage despite elevated NCOs.
- HTM provision $0.5M; HTM ACL $13.4M (footnote, p12).

---

## 3. V3 — The Credit-Linked-Note / SSFA Program (p4)

**The under-the-radar finding.** Press release discloses:

*"The Company is a party to credit linked note transactions which effectively transfer a portion of the risk of losses on reference pools of loans to the purchasers of the notes. The Company is protected from first credit losses on reference pools of loans totaling **$7.9 billion, $8.1 billion, and $8.5 billion as of March 31, 2026, December 31, 2025, and March 31, 2025**, respectively… the allowance for loan and credit losses ratios include an allowance related to these pools of loans of **$11.2 million** as of March 31, 2026."*

**Trajectory — THE PROGRAM IS SHRINKING:**
- Mar-25: $8.5B
- Jun-25: (not disclosed)
- Sep-25: (not disclosed)
- Dec-25: $8.1B
- Mar-26: $7.9B
- **Down $600M (-7%) YoY. Allowance coverage $11.2M = 14bps of pool.**

**Why this matters for V3 thesis:**
- CLN transactions are WAL's primary SSFA / synthetic capital-relief vehicle.
- If WAL were "doubling down" on capital arbitrage, we'd expect the reference pool to GROW.
- Instead: shrinking — possibly running off natural maturities without replacement, or SSFA treatment proving less attractive under AOCI / Basel III changes.
- Disconfirming to "WAL pressing into synthetic structures" narrative.
- **Still open**: composition of the three CLN pools (vintage, tenor, underlying loan types) — requires 10-Q or deck.

**Loss math**: If CLN first-loss covers X% and $7.9B pool has 1% annual loss, that's $79M of losses/year absorbed by note-holders. WAL pays spread for this protection, not a charge-off. $11.2M allowance on pool = what WAL's own models say of residual first-loss retention. Conservative.

---

## 4. $100B Cat III/IV Lever (p4 — balance sheet data)

**$98,853M total assets Mar 31, 2026.** $1,147M from the $100B threshold.

Trajectory (5 quarters, period-end):
- Mar-25: $83,043M
- Jun-25: $86,725M (+$3.7B)
- Sep-25: $90,970M (+$4.2B)
- Dec-25: $92,774M (+$1.8B)
- **Mar-26: $98,853M (+$6.1B, +6.6% QoQ, +19.0% YoY)**

Sequential $-growth has been $1.8–$6.1B / quarter over the last four. **At Q1-26 pace, $100B crosses at ~Jun 30.** Even at average pace ($3.95B/q), Q2-26 crosses.

**Composition of the $6.1B QoQ asset growth (Mar-26 vs Dec-25):**
- Cash: +$5.0B (!) — $3.6B → $8.6B — **the dominant driver**
- Investment securities: +$4.5B (on period-end; avg +$0.07B)
- HFI loans: +$0.5B (muted)
- HFS loans: +$0.4B
- MSR: +$22M

So the Q1 asset surge is **cash + securities accumulation**, not loan growth. Consistent with a carry-trade / liquidity build ahead of possible deposit outflows (or in preparation for known outflows, e.g., tax season). Cross-check: deposits +$5.6B QoQ, so cash+securities absorbed the deposit inflow.

**Implication for Cat III/IV tripwire**: $100B can be managed by letting cash decline (not letting loans shrink). WAL has a ~$5B cash buffer they could use to stay under $100B for 1-2 quarters longer — a tactical choice. Transcript hinted Cat III regulation was something they'd cross naturally; this press release confirms they have the levers to delay if they wanted.

---

## 5. NIM and Core Earnings — the real acceleration (p14-15)

**NIM progression:**
- Q1-25: 3.47%
- Q2-25: (not disclosed in press release)
- Q3-25: (not disclosed)
- Q4-25: 3.51%
- **Q1-26: 3.54% (+7bps YoY, +3bps QoQ)**

**Key drivers — YoY (Q1-26 vs Q1-25):**

| Component | Q1-26 | Q1-25 | Delta |
|---|---|---|---|
| Total HFI loan yield | 5.85% | 6.20% | **-35bps** |
| Total IB deposit cost | 2.75% | 3.26% | **-51bps** |
| ST borrowings cost | 4.05% | 4.89% | -84bps |
| Qualifying debt cost | 4.92% | 4.18% | **+74bps** (new $400M sub debt) |
| Cost of funding | 1.92% | 2.34% | -42bps |

**Translation:** Falling deposit costs outpaced falling loan yields. Liability beta > asset beta this cycle.

**Avg balance growth YoY:**
- HFI loans: $53.5B → $58.2B (+$4.7B, +8.7%)
- Investment securities: $15.3B → $20.0B (+$4.7B, +30.8%) — **securities book growing 3.5x faster than loans**
- NIBD: $22.1B → $27.4B (+$5.3B, +23.8%)
- IB deposits: $47.1B → $53.3B (+$6.2B, +13.1%)

**Deposit mix improving** — NIBD grew faster than IB deposits YoY, reversing the 2023-24 trend.

### PPNR — the engine (p16)

Five-quarter PPNR:
- Q1-25: $277.6M
- Q2-25: $331.2M
- Q3-25: $393.8M
- Q4-25: $428.7M
- **Q1-26: $444.5M (+60% YoY, +3.7% QoQ)**

**Adjusted PPNR Q1-26 (ex $50.5M sec gains): $394.0M.** Still +42% YoY on adjusted basis.

### Efficiency ratio — the operating leverage (p16)

Five-quarter efficiency (tax-equiv, adjusted for deposit costs):
- Q1-25: 55.8%
- Q2-25: 51.8%
- Q3-25: 47.8%
- Q4-25: 46.5%
- **Q1-26: 47.5%** (+100bps QoQ regression, -830bps YoY improvement)

Opex leverage story is real. Core earnings power up materially YoY. This is the bull case.

### Juris Banking (p3)

- Press release calls out **Juris banking driving increases in BOTH "other non-interest expense" AND "service charges and fees"** — comparable growth on both sides, so roughly neutral to operating margin but adds to revenue base and balance-sheet touchpoints.
- No segment-level disclosure of Juris size — would need deck or 10-Q.

### Earnings credits (p15-16)

Reduction to interest income, 5-quarter:
- Q1-25: $58.1M → Q2-25: $61.3M → Q3-25: $64.9M → Q4-25: $56.6M → **Q1-26: $48.7M**
- **Declining 5-quarter. Short-rate-sensitive.** Helps NII as Fed cuts proceed.
- Total earnings credit + referral costs Q1-26: **$214.3M** (vs $192.2M Q1-25).

---

## 6. Capital (p4, p8, p17)

**CET1 11.0%** Mar-26 (flat QoQ, down 10bps YoY from 11.1%).
**TCE ratio 6.8%** Mar-26 (down 50bps QoQ from 7.3%, down 40bps YoY from 7.2%).
**Tier 1 12.0%, Total Capital 14.4%.**

**TBV per share: $61.14** (flat QoQ from $61.29; **+13.0% YoY** from $54.10).

**TCE walk QoQ (approx, from 5-quarter balance sheet):**
- Dec-25 TCE net of tax: $6,711M
- + NI attributable to WAL: +$182.1M
- − Dividends (common $46.1M + depositary $3.2M + REIT pref $7.1M): -$56.4M
- − Buybacks: -$50.0M
- − AOCI change: -$112M
- ~ = ~$6,674M ≈ Mar-26 TCE $6,677M ✓

**AOCI trajectory ($M):**
- Mar-25: (478)
- Jun-25: (482)
- Sep-25: (409)
- Dec-25: (344)
- **Mar-26: (456)** — **-$112M QoQ reversal after 2-quarter rally**

AOCI deterioration ate ~60% of net income this quarter. Rate-curve repricing hit AFS book. This is the AOCI-reinclusion bomb REGINALD has flagged for Cat III/IV (Jun 18 comment period). Cross-check with deck for HTM vs AFS composition.

**Capital actions:**
- Common div: $0.42/share × 109.2M shares = $45.9M paid (≈$46.1M reported)
- Buybacks: $50.0M / 0.7M shares = **$71.61 avg price** (stock $79.44 today = +11% paper gain)
- Remaining authorization: $300M program − $50M = $250M (transcript: "not in our models right now")

**Share count trajectory (5-quarter):**
- Mar-25: 110.4M
- Jun-25: 110.4M
- Sep-25: 110.2M
- Dec-25: 109.5M
- **Mar-26: 109.2M** (net -1.2M YoY — buybacks outpaced stock-based comp dilution)

**Payout math Q1-26 (GAAP):** $189.2M NI → $56.4M div + $50M BB = $106.4M return = **56% payout**. On adjusted NI: **42% payout**.

---

## 7. Deposits & Funding (p4, p8, p11)

**Headline: $82.7B total deposits (+$5.6B QoQ, +$13.4B YoY = +19.3%). L/D 71.5% (vs 76.0% QoQ, 79.0% YoY).**

| Type ($M) | Mar-26 | Dec-25 | Mar-25 | YoY delta |
|---|---|---|---|---|
| Non-interest bearing | 28,078 | 24,353 | 22,009 | +$6.1B (+28%) |
| IB demand | 19,385 | 18,416 | 15,507 | +$3.9B (+25%) |
| Savings & MM | 25,414 | 24,586 | 21,728 | +$3.7B (+17%) |
| CDs | 9,846 | 9,804 | 10,078 | -$0.2B (-2%) |
| **Total** | **82,723** | **77,159** | **69,322** | **+$13.4B (+19%)** |

**Mix as % (p4):**

| | Mar-26 | Dec-25 | Mar-25 |
|---|---|---|---|
| Non-interest bearing | 34.0% | 31.5% | 31.8% |
| IB demand | 23.4% | 23.9% | 22.4% |
| Savings & MM | 30.7% | 31.9% | 31.3% |
| CDs | 11.9% | 12.7% | 14.5% |

**Signal:** **CDs falling 260bps of mix YoY (from 14.5% to 11.9%).** Cheapest-acquired highest-stability funding (NIBD) grew fastest. This is deposit quality improvement, not just quantity.

Five-quarter NIBD sequence ($M): 22,009 → 22,997 → **26,628** → 24,353 → **28,078**. Note Q3-25 spike then Q4-25 pullback, Q1-26 rebound. Lumpy — large commercial-deposit customer flows. Mortgage warehouse, settlement services, HOA, title business operate with material month-end NIBD volatility.

**Borrowings** ($5.61B Mar-26, +$370M QoQ, +$1.5B YoY):
- Short-term borrowings +$676M QoQ, +$2.0B YoY
- Long-term -$307M QoQ, -$529M YoY
- **Net YoY: $1.5B more reliance on short-term funding**. Watch FHLB Q1 Call Report May 1-10.

Qualifying debt $1.1B Mar-26, flat QoQ, +$175M YoY (Q4-25 issued $400M sub debt, Q2-25 repaid $225M).

---

## 8. Loan Composition (p4, p11)

**HFI loans $59,142M Mar-26 (+$465M QoQ, +$4,381M YoY):**

| ($M) | Mar-26 | Dec-25 | Mar-25 | QoQ | YoY |
|---|---|---|---|---|---|
| Commercial & industrial | 28,223 | 27,928 | 24,117 | +295 | **+4,106 (+17%)** |
| CRE non-owner occ | 10,344 | 10,340 | 10,040 | +4 | +304 (+3%) |
| CRE owner occupied | 1,711 | 1,683 | 1,787 | +28 | -76 (-4%) |
| Construction & land dev | 4,080 | 4,055 | 4,504 | +25 | **-424 (-9%)** |
| Residential real estate | 14,765 | 14,652 | 14,275 | +113 | +490 (+3%) |
| Consumer | 19 | 19 | 38 | 0 | -19 |
| **Total HFI** | **59,142** | **58,677** | **54,761** | **+465** | **+4,381** |

**Signals:**
1. **C&I drove 94% of YoY loan growth.** Warehouse, settlement, Juris — C&I is where NDFI/fund-finance/warehouse all report.
2. **Construction & land development shrinking** (-$424M YoY, -9%). Deliberate pullback. Transcript (Bruckner) confirms.
3. **CRE non-OO flat sequentially** — classified/growth pulled back.
4. **Residential RE growing mildly** (+$490M YoY) — Juris mortgage integration likely part of this.

HFS loans $3,936M Mar-26 (+$438M QoQ, +$698M YoY):
- $345M of QoQ increase = government-insured/guaranteed mortgages
- $113M of QoQ increase = agency-conforming
- $689M of YoY increase = government-insured/guaranteed

**GSE/gov-guaranteed mortgage pipeline dominant in HFS.** Consistent with the RITM / MSR / warehouse adjacency (CARL's non-bank servicer watch).

---

## 9. Non-Interest Income — what's driving the $252.6M (p9)

| ($M) | Q1-26 | Q4-25 | Q1-25 | QoQ delta | YoY delta |
|---|---|---|---|---|---|
| Service charges and fees | 88.5 | 73.6 | 40.5 | +14.9 | **+48.0** |
| Net gain mortgage orig & sale | 72.7 | 91.1 | 49.5 | -18.4 | +23.2 |
| Net loan servicing rev (loss) | (1.3) | (1.4) | 21.8 | +0.1 | -23.1 |
| BOLI income | 10.7 | 11.8 | 11.4 | -1.1 | -0.7 |
| **Gain on sales of invest sec** | **50.5** | 7.4 | 2.1 | **+43.1** | **+48.4** |
| Fair value gain adj | 3.1 | 3.5 | 1.0 | -0.4 | +2.1 |
| Equity investments | 13.3 | 12.2 | (4.8) | +1.1 | +18.1 |
| Other | 15.1 | 16.5 | 5.9 | -1.4 | +9.2 |
| **Total** | **252.6** | **214.7** | **127.4** | **+37.9** | **+125.2** |

**Observations:**
- Total non-interest income **nearly doubled YoY** ($127.4M → $252.6M, +$125.2M).
- Service charges & fees +$48M YoY — Juris banking and deposit-related fees.
- Mortgage gains +$23M YoY despite QoQ decline — mortgage origination recovering modestly from 2024 lows.
- Security gains jumped to $50.5M from $7.4M QoQ — the "mitigation" trade.
- Loan servicing loss (-$1.3M) vs +$21.8M Q1-25 — MSR mark-down or fee pressure, watch for explanation in deck.

---

## 10. Non-Interest Expense (p9)

| ($M) | Q1-26 | Q4-25 | Q1-25 | QoQ | YoY |
|---|---|---|---|---|---|
| Salaries & benefits | 205.5 | 201.7 | 182.4 | +3.8 | +23.1 |
| Deposit costs | 163.3 | 171.2 | 136.8 | -7.9 | +26.5 |
| Data processing | 53.1 | 48.9 | 45.2 | +4.2 | +7.9 |
| Legal / prof / directors | 30.6 | 33.6 | 28.9 | -3.0 | +1.7 |
| Insurance | 24.7 | 17.7 | 37.9 | +7.0 | -13.2 |
| Occupancy | 19.2 | 19.7 | 17.2 | -0.5 | +2.0 |
| Loan servicing | 16.7 | 17.7 | 16.4 | -1.0 | +0.3 |
| Business dev & marketing | 9.5 | 11.1 | 5.9 | -1.6 | +3.6 |
| Loan acq / origination | 7.9 | 7.9 | 5.2 | 0 | +2.7 |
| Other | 43.9 | 22.7 | 24.5 | **+21.2** | +19.4 |
| **Total** | **574.4** | **552.2** | **500.4** | **+22.2** | **+74.0** |

**Anomalies:**
- **"Other" expense +$21.2M QoQ** — largely Juris banking + OREO-related charges (p3). OREO charges suggest more repossessed-asset write-downs this quarter.
- Insurance +$7M QoQ normalization after Q4 FDIC special assessment release.
- Deposit costs -$7.9M QoQ = biggest line-item tailwind.
- Salaries +$23.1M YoY (+13%) — hiring + comp increases. Watch in DEF 14A.

---

## 11. Cohort comparisons — what we can say now

**NCO ratio (annualized, reported):**
| Bank | NCO Q1-26 | Commentary |
|---|---|---|
| ZION | ~3bps | Clean-book outlier |
| CFG | ~40bps retail | NCOs declining YoY |
| FITB | (TBD) | — |
| RF | (improved) | Credit improving |
| MTB | (not broken out) | Building ACL |
| PNC | (TBD) | Building ACL |
| **WAL** | **145bps GAAP / 39bps ex-fraud** | Fraud-specific spike |
| OZK | 57bps | In-line w/ 50bps FY guide |

**NIM Q1-26:**
| Bank | NIM | Direction |
|---|---|---|
| ZION | 3.27% (-4bps QoQ) | Compressing |
| **WAL** | **3.54% (+3bps QoQ, +7bps YoY)** | Expanding |
| OZK | 4.20% | Flat |

**NDFI disclosure spectrum (per REGINALD STATUS):**
- PNC: $73B / 20% of loans
- CFG: $19.6B / 13%
- FITB: $9.5B / 8%
- MTB: $8.9B (partial)
- **WAL: $3B bucket** (via transcript Slide 20+24; lender finance $2.3B = majority)
- RF: ~$3B / <2% (disclosed in Q&A, not in supplement)
- ZION: $2B (cohort floor)

**WAL sits between RF and ZION on NDFI size.** Thematic NDFI bucket is a smaller share of WAL's loan book than cohort. V3 is quality-of-names, not size.

---

## 12. §11 Open Items — status after press release

| # | Item | Status | Source for resolution |
|---|---|---|---|
| 1 | MI3 / RCON2746 ratio | ❌ Open | Call Report May 1-10 |
| 2 | NDFI / fund finance breakdown | 🟡 Partial (transcript Slide 20+24) | Deck, 10-Q |
| 3 | Warehouse book detail | ❌ Open | Deck, 10-Q |
| 4 | Cantor residual balance | ✅ **CLOSED**: $13M senior liens disclosed (p13) | — |
| 5 | Other LAM / Leucadia credits inventory | ❌ Open | Deck, 10-Q |
| 6 | Securities sales composition | 🟡 Partial ($50.5M amount confirmed, portfolio unknown) | Deck, 10-Q |
| 7 | CET1 walk | 🟡 Partial (reconstructed, no formal walk) | Deck |
| 8 | Hormuz / Middle East reserve | ❌ Open | Deck, transcript (none found) |
| 9 | Subsequent-events securities | ✅ **CLOSED**: WAL did $50.5M IN-quarter, not post-Q1 (unlike RF's $40M) | — |
| 10 | Management forward guide | ❌ Open in PR (addressed in transcript) | Deck |

**2 fully closed, 3 partially closed, 5 still need deck / 10-Q / Call Report.**

---

## 13. New items to add to §11 from this read

1. **CRE-NOO $27.7M charge-off composition** — single credit or multiple? Which property type? (deck, 10-Q)
2. **CLN reference pool composition** — three pools at $7.9B total, need vintage / tenor / underlying (10-Q)
3. **Why is CLN pool shrinking?** Running off naturally or strategic pullback? (deck Q&A or 10-Q)
4. **What's behind the 30-89d PD jump (+$49M)?** Categorical or idiosyncratic? (deck, 10-Q)
5. **Special mention surge composition** — which segments? (deck, 10-Q)
6. **Loan servicing revenue swing** — $21.8M to -$1.3M YoY. MSR valuation hit? (10-Q)
7. **Juris banking segment size and margin** — not disclosed (deck)
8. **HFS composition detail** — $3.9B book: gov-guar $2.1B? agency-conforming? non-agency? (deck)

Append to Round 2 / Round 3 deck + 10-Q priorities.

---

## 14. Cut ledger — what was in the press release and deliberately NOT extracted

| Content | Pages | Reason cut |
|---|---|---|
| Cautionary / forward-looking statement boilerplate | p5 | SEC template, no signal |
| About Western Alliance corporate description | p5 | Marketing copy |
| Contact information | p5 | Metadata |
| Conference call dial-in details | p5 | Ephemeral |
| Reclassifications disclosure | p5 | Single-line boilerplate ("no effect on net income") |
| Non-GAAP reconciliation introductory text | p16, p18 | Repeats CEO quote |
| Footnote templating ("See Reconciliation of Non-GAAP…") | all pages | Cross-reference |
| Use of Non-GAAP Financial Information section | p5 | Methodology boilerplate |

None of these would be consulted for any thesis decision. Not re-reading.

---

## 15. What to write back to other REGINALD docs (Wave 1 propagation)

**`WAL/Q1_2026_ANALYSIS.md` additions for Round 2 rewrite:**
- New §4.5: Asset-quality leading vs lagging indicator divergence (30-89d +$49M, special mention +$78M, vs classified/nonaccrual improvements). Elevates the cohort-fade 2% tape response from "adjusted-beat read-through" to "market pricing forward credit deterioration."
- New §3.1: LAM-not-Cantor asymmetry in EPS reconciliation. Sharpens framing — "adjusted EPS adds back the fresh hit, not the bookkeeping release."
- New §5.5: CLN reference pool $7.9B shrinking (V3 data). Disconfirming to "WAL pressing into capital arb."
- Update §4: CRE-NOO $27.7M charge-off — ex-fraud NCO composition asterisk.
- Update §6: Cantor $13M senior liens now confirmed; residual math still rests on $72M inference.

**`WAL/THESIS.md` v2 propagation:**
- V2 CONFIRMED: LAM+Cantor credits resolved mechanically.
- V3 DIRECTIONALLY DISCONFIRMED on the narrow CLN vector: reference pool shrinking, not growing.
- New V5 candidate: Asset-quality leading-indicator reversal (30-89d PD + Special mention). Watch Q2-26 for whether this moves to criticized → classified → nonaccrual.

**`WAL/workbook/KB.tsv` additions:**
- ML-WAL-xxx: CLN reference pool trajectory ($8.5B → $7.9B)
- ML-WAL-xxx: CRE-NOO 5Q charge-off history ($66M cumulative)
- ML-WAL-xxx: 30-89d PD 5Q progression
- ML-WAL-xxx: Special mention 5Q progression
- ML-WAL-xxx: Earnings credit 5Q decline ($58.1M → $48.7M)
- ML-WAL-xxx: Qualifying debt cost +74bps YoY (sub debt repricing micro-signal)

---

*End synthesis. Pair with transcript synthesis for full Round 2 surface. Deck + 10-Q + Call Report remain.*
