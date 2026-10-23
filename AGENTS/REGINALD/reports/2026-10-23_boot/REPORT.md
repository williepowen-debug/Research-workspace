# REGINALD — 2026-10-23 boot and catch-up (Will: "get your files caught up with live data/news")

**Written:** 2026-10-23 from 15:18 ET Friday (from `date`). Runtime: Claude Code, Opus 5.5, launched by Will in `AGENTS/REGINALD`. PROME (prome-03) asks folded in: its message 15:1x ET.
**Data receipts:** `kre_vs_hy_vs_10y.txt` and `WAL-KRE-settled.txt` in this folder. FRED pulled 15:2x ET with a fresh cache (`FORGE_CACHE_DIR` override; the shared cache was serving 10/21 values). Today's 10/23 bars are vendor quotes, not settled.

---

## 1. Levels (dated)

| Series | Latest | Prior | Note |
|---|---|---|---|
| HY OAS (FRED BAMLH0A0HYM2) | **340bp [10/22]** | 327 [10/21], 333 [10/20] | REG-T-03 fired state continues (7 consecutive >320). **REG-T-04 (>350 ×3) is 10bp away**, run 0 of 3 |
| CCC OAS | **1,340 [10/22]** | 1,307 [10/21] | CCC/HY **3.94×** [10/22] (4.00× [10/21]); hard-fire continues; widening was not CCC-led on 10/22 (ratio fell) |
| B OAS | **346 [10/22]** | 332 [10/21] | Above the 330 ORANGE line for a third print; watch only |
| BB OAS | 210 [10/22] | 198 [10/21] | |
| 10-year | ^TNX **4.95% [10/22 vendor close]**, 4.99% [10/23 15:2x vendor] | FRED DGS10 5.13 [10/21] | FRED 10/22 not yet published at retrieval |
| Claims | 194K [w/e 10/17] | 200K [10/10] | unchanged from STATUS |
| KRE | **$72.41 [10/22 settled]** | $70.62 [10/21] | Yahoo and Nasdaq agree; $72.5 intraday 10/23 |
| WAL | **$76.67 [10/22 settled]** | $75.55 [10/21] | REG-T-02 exit log row 37, run 0 of 3 |
| FLG | $11.44 [10/22 settled]; **$10.38–10.40 [10/23 intraday, −9%]** | $11.07 [10/21] | Ladder RED; 10/23 not graded until settled |
| Discount window primary credit | **$9.17B [Wed 10/21]**, week avg $8.94B | $11.04B [Wed 10/14] | H.4.1 10/22 as read at the Fed by WALTER (SIG-W-20261022-034). Below the descriptive ~$12.9B line |
| RRP | $0.351B [10/22] | $0.237B [10/21] | |
| SOFR − IORB | −2bp [10/21] (3.88 − 3.90) | | |

## 2. Q3 prints since the last session

### 2a. FLG (Flagstar), Fri 10/23 pre-open — graded against my CRE top-3 "weakens if" lines
FLG desk's primary grade: `AGENTS/FLG/reports/2026-10-23_Q3-2026_PRINT_GRADE.md` (8-K acc 0000910073-26-000080). Figures below are FLG's primary reads; the grading against my lines is mine.

| My line (`reports/2026-09-26_CRE_vulnerability_top3.md` §6) | Q3 print | Concern weakens? |
|---|---|---|
| MF special mention ≤ $2,757M | Not in release/deck | UNREAD (10-Q ~11/6) |
| H2 modifications < $556M | Not in release/deck | UNREAD (10-Q) |
| Criticized NYC rent-regulated pool < $4.0B | **$4,402M** (SM+SS $2,723M + NAL $1,679M) | **NO** |
| Nonaccrual back below $2,675M | **$2,817M** (+$17M) | **NO** |
| NYC RR loss ratio ≤ ~17% | **20.7%** derived (20.45% at 6/30) | **NO** |
| Rent freeze stayed or annulled | No ruling | NO |

**Read: none of the four readable lines weakened the concern; two wait for the 10-Q.** Criticized + classified rose **$670M to $12.3B**, the first rise in five quarter-ends. Coverage made a new low (30.85% release basis) because nonaccruals rose while the reserve stayed flat at $869M. Provision guidance went from $90–140M to $160–170M; 2027 provision from $100–150M to $175–225M. The company bought back ~$216M of stock in Q3 in the same quarter. FLG stays #1 on my CRE list. Matrix score unchanged until the 11/07 re-score (price is not an input).

### 2b. AMTB (Amerant), Thu 10/22 after close — Florida frame, FINAL for this name
8-K acc 0001734342-26-000084, EX-99.1 read at EDGAR.

| Cell | Q2 | Q3 | Grade |
|---|---|---|---|
| CRE non-owner-occupied nonaccrual (primary) | $9,386K | **$4,677K** | HOLDS (≤ $11.2M) |
| Classified $ | $273.1M | **$213.0M** (−22%, "primarily payoffs") | HOLDS (fell) |
| Acquired-pool resi rate | 1.60% | 10-Q | EXCLUDED from the combiner |

**AMTB = HOLDS (P = HOLDS, T = 0; both non-excluded cells read → final).** Also: nonperforming loans $171.1M → $149.5M; special mention +$10.9M to $120.7M (downgrades); ACL $85.5M → $94.8M, so reserve / NPL ≈ 50% → 63% (derived); NCO 0.12% (0.08% Q2). FHLB $715.0M (+1.8%). **Florida aggregate:** AMTB HOLDS final · SSB HOLDS provisional · BKU HOLDS-PENDING-P · SBCF unread (prints Tue 10/27). Three HOLDS = NO TRANSMISSION, so the aggregate is one SBCF/10-Q leg away from final either way; still PROVISIONAL.

### 2c. CUBI (Customers), Thu 10/22 after close — WQ-318 row
8-K acc 0001488813-26-000100, EX-99.1 and deck read at EDGAR.

| Leg | Pre-committed line | Q3 | Met? |
|---|---|---|---|
| F (funding) | NIB average falls >5%, or DA spot < $3.42B; plus FHLB > $2.37B or IB cost ≥ 3.64% | NIB average **$6.53B vs $6.18B (+5.6%, up)**; FHLB **$2.137B** (+3.8%); IB deposit cost **3.55%** (3.54% Q2); DA spot not in text | NO |
| DOWN | IB cost ≤ 3.54%, NIB ≥ 31.8%, FHLB flat/down, specialized ≤ +5% | IB cost 3.55% (misses by 1bp); NIB **31.9%**; FHLB up | NO |
| N (nonbank draws) | specialized lending > $8.03B | Balance not disclosed; deck loan bridge: **fund finance +$456M**, the largest growth line of +$496M total | Ungradeable from release, as pre-stated → 11/07 Call Report |

**CUBI WQ-318 = INCONCLUSIVE.** Credit improved: NPL $56.0M → $53.4M (0.29%), reserves / NPL 293% → 322%, NCO 0.34% → 0.28%. The one live fact for the nonbank lane: fund-finance lending was CUBI's biggest grower in Q3.

### 2d. First Citizens and First Hawaiian (WALTER SIG-W-20261023-012, SECONDARY to me; not read at EDGAR)
First Citizens: reserve release $48M, nonaccruals 0.96% → 0.87%, NCO 0.27%. First Hawaiian: one CRE loan, $12.5M partial charge-off, NCO 0.11% → 0.60%.

### 2e. Cohort descriptive (asked by WALTER 012 / -005)
The 10/22 line was "problem loans up at 6 of 6 read names; coverage down at 5 of 5 computed."

| Adds | Problem loans | Coverage |
|---|---|---|
| FLG | up (NAL +0.6%, criticized +6%) | down (31.04 → 30.85%) |
| AMTB | **down** (NPL −13%, classified −22%; SM +10%) | **up** (~50% → ~63%) |
| CUBI | **down** (NPL −5%) | **up** (293 → 322%) |
| First Citizens (secondary) | **down** (NAL 0.96 → 0.87%) | not computed |
| First Hawaiian (secondary) | not read | not computed |

**Updated: problem loans up at 7 of 10 read names; coverage down at 6 of 8 computed.** The pattern now holds at the CRE-concentrated names (FLG, EGBN, VLY, SSB, BKU, HBAN, ZION) and breaks at the cleaner or more C&I-weighted ones (AMTB, CUBI, First Citizens). That is the concentration claim, not a tier-wide one. DEWEY's base rate still says coverage decline is a weak near-term NCO predictor (2/10 within 4Q). No score, threshold or probability change. REG-29's six names are not touched by these three prints.

## 3. PROME ask (1): what a REG-T-04 fire means for the bank lane, broad vs AI-driven

**Letter (registry/THRESHOLDS.tsv):** HY OAS > 350 on 3 consecutive daily closes → ISSUANCE-FREEZE; chain REGINALD action / LIQUID action / Will; exit ≤ 330 ×5. Earliest fire: closes 10/23, 10/26, 10/27 all > 350, published by FRED ~10/28 (DOCKET L818).

**Composition now (DEWEY `AGENTS/DEWEY/output/2026-10-23_hy-widening-ai-vs-broad-decomposition.md`):** 65% of the +80bp (260 → 340) came in September's broad selloff; the AI leg is ≈3bp of the ≈+24bp from 10/13 to 10/22 (≈10–15% of October). On 10/22: BB +12, B +14. CCC (+161bp in October, widest since July 2020) has an unknown AI share.

| If REG-T-04 fires on… | What it means for regional banks | What I would look for |
|---|---|---|
| **A broad repricing (the current evidence)** | A cycle signal: the bond window closes for leveraged borrowers, so they lean on bank lines and on lender-finance / fund-finance facilities. **The bank-lane channel is drawn balances (NDFI and C&I), not regional-bank credit losses.** Losses would come later, through NDFI and BDC borrowers (BROCK's lane), not through CRE | Weekly H.8 C&I and NDFI-loan lines for a draw spike; Q4 NDFI balances at CFG (unfunded ≈ 100% of drawn, $22.5B) and CUBI (fund finance +$456M in Q3, already its top grower); bank preferreds vs PFF |
| **An AI-concentrated repricing** | Weaker for regionals: the named AI credits (CoreWeave, SoftBank) borrow from large banks and private credit, not from my cohort. The regional path is second-order, through BDC/private-credit funds that bank lender-finance books lend to | GIBBS (large banks) and BROCK (BDCs) own the first read; my lane moves only if lender-finance draws or marks show up at CFG, CUBI, WAL, OZK |

**Volume vs price (WALTER -016, single Bloomberg secondary):** US junk issuance ≈ $7B in October through 10/21 vs ≈ $51B in September, > $5B of deals delayed. **On volume, the freeze is already under way ahead of the price line.** The registered letter is the price line, and I do not grade it on volume; I record volume as the leading leg.

**Pre-staging before a possible 10/27 fire: nothing new is registered.** On a fire I will run the existing bank cross-check (`reports/2026-07-30_bank-side-HY-attribution.md`) the same session and read the H.8 C&I/NDFI lines. No gate move, no trade.

## 4. PROME ask (2): BANK-ABSENT cross-check at the 10/22 cell, and HY vs the 10-year

**10/22 cell:** HY +13bp (327 → 340) while KRE **+2.53%** ($70.62 → $72.41), KBWB +0.16%, IWM +0.07%, PFF −0.03%, HYG +0.16%, QQQ −2.86%, and the 10-year **−19bp** (^TNX 5.146 → 4.953, vendor). Part of KRE's day was print relief (EGBN +15.6%, VLY +6.1% on 10/22). **The cross-check stays BANK-ABSENT; confidence moves from ~0.6 to ~0.7** because banks rose on the widest HY day of the month.

**Is the 10-year, not HY, the bank-lane transmission? Over 57 trading days (8/4 → 10/22), daily changes:**

| | HY spread | 10-year (vendor ^TNX) |
|---|---|---|
| Correlation with KRE daily return | **+0.07** | **−0.36** |
| KRE move per +10bp (joint regression) | **+0.02%** | **−0.72%** |
| Correlation with KRE minus IWM | +0.37 (KRE beat small caps on HY-wide days) | −0.04 |

Fit is weak (R² 0.13): most KRE variance is neither. Window check: 9/21 → 10/22, KRE +0.6% while HY +74bp and the 10-year −1bp.

**Read:** on this sample the 10-year is the rate that moves regional banks; HY widening has not. That agrees with CREED's 10/22 read (CRE stress is a rate shock, not credit). **So for any regional-bank put, the falsifier to write on the card is a falling 10-year** (rate relief lifts KRE about 0.7% per 10bp on this fit), **not a narrowing of HY.** A wide HY print alone is not confirmation for a bank put. This is a falsifier for TERRY's card, not a trade view; positions are Will's.

## 5. Inbox and BOARD dispositions
WALTER lane: 15 signals logged in `board/BOARD_LOG.tsv` and filed. General inbox: 15 packets read; the cyber set (CYPHER ×3, DEWEY ×8): **no escalation row fired, no named US bank or core-vendor victim, no deposit channel observed** — consequence for my lane: none this session. DAEDALUS WQ-508: lines already applied by DAEDALUS (`d3488e641`); not contested. Correction COR-20261022-48: none of the killed strings appear in my tree (grep 15:3x ET) → NO-OP receipt.

## 6. Trade-idea route
No candidate this print cluster. FLG: no position on this desk's book and the move (−9% intraday) is post-print; EGBN unchanged from 10/22 (no candidate). The rates falsifier in §4 goes to `TRADE.md` §4 for any bank put card.
