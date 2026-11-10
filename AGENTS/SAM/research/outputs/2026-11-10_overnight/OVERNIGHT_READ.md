# SAM overnight read, 11/9 evening to 11/10 (ET)

**Commission:** Will, 20:15 ET 11/9 ("yes go ahead"): run tonight's reads in the held-open laptop session rather than at 06:00. **Owner:** SAM. $0. Each item keeps its own source clock.

## 1. BOJ meeting OIS, Totan 11/9 15:15 JST (SAM visual review, SHA `719bd0bd…`)

| Meeting | OIS % | Difference % | Incremental 25bp equivalent | Cumulative count | 11/6 15:15 JST (for reference) |
|---|---|---|---|---|---|
| 2026-12 | 1.4075 | 0.1795 | **72%** | 0.72 | 52% / 0.52 |
| 2027-01 | 1.4600 | 0.0525 | 21% | 0.93 | 27% / 0.79 |
| 2027-03 | 1.5550 | 0.0950 | 38% | 1.31 | 40% / 1.19 |
| 2027-04 | 1.6213 | 0.0663 | 27% | 1.57 | 19% / 1.38 |
| 2027-06 | 1.6913 | 0.0700 | 28% | 1.85 | 29% / 1.67 |

Arithmetic chain checked (difference ÷ 0.25 = column 4 on every row; counts accumulate), `boj_ois.py --no-write` validated live hash, 5 rows ingested to `BOJ_MEETING_OIS.tsv`. Incremental equivalents are not probabilities; counts are not probabilities. JST assumed. Valid to the 12/18 decision, four-day age limit.

**What moved it, 11/6 → 11/9 (REPORTED, no single verified cause):** December went 82% (10/29) → 52% (11/6, the Tokyo −5.96% day) → 72% (11/9). Monday coverage (FXStreet 11/9, European hours) cites the September minutes (released 11/5), former BOJ chief economist Kameda calling a December hike with a path to 2% in 2027, and oil easing after Trump called further action against Iran "highly unlikely". MOF 2Y rose 1.732 → 1.778 (+4.6bp) the same day. Working read: most of the 11/6 drop was risk-off that reversed as Tokyo recovered, not a change in the BOJ's reaction function. ⚠️ The jump **predates** the Summary of Opinions (08:50 JST 11/10), so the summary did not cause it.

## 2. Summary of Opinions, October 29–30 MPM (PRIMARY, `opi261030.pdf`, released 08:50 JST 11/10, read 11/9 ~20:20 ET)

Written before the 11/5–6 selloff. Hawkish in tone:
- "underlying CPI inflation is at a level that is generally consistent with the price stability target of 2 percent".
- "a new phase in which the Bank needs to step up the pace of bringing the policy interest rate to the neutral interest rate".
- "the Bank needs to bring the policy interest rate to the neutral level soon", with "make haste slowly".
- "a regime shift to bring the policy interest rate to the level of the neutral interest rate at an early stage".
- "it is likely that the neutral interest rate is considerably above 1 percent".
- One opinion: core CPI "is projected to exceed 3 percent toward the end of the fiscal year" (the Outlook median for FY2026 is 2.5).
- "decide on the next policy interest rate hike when it is possible without becoming overly cautious".

Counterweights in the same document: two hold opinions ("a little more examination of risks"; "assess the cumulative effects of past rate hikes"); one that the policy rate "has entered the level of the estimated range of the neutral interest rate" and a future hike could push underlying inflation down; one that anchoring holds "even without hastily raising" the rate. Next year's shunto named as the thing to watch.

**Read:** a board with a majority leaning toward hiking again soon and no date. Consistent with December being live, not a commitment. As noted in the plan, hawkish wording against the post-selloff pricing is not a reaction to the selloff. No score, band or prediction moved; SAM-33 concerns long-end capping, not the policy rate.

## 3. MOF quarterly intervention record, July–September 2026 (PRIMARY, `feio/quarter/2026_3Qe.html`, dated 11/9)

| Date | Amount | Pair |
|---|---|---|
| 7/30 | ¥7,975.6B | USD sold, JPY bought |
| 7/31 | ¥5,552.3B | USD sold, JPY bought |
| **8/3** | **¥1,871.4B** | USD sold, JPY bought |
| Total | ¥15,399.3B | sums exactly |

**What this settles:**
1. **8/3 was an intervention day.** `STATUS_REFERENCE.md` carried the 8/3 "detector disagreement" (2.67-yen range over the 2.5-yen bar, while the BOJ fiscal-factor settlement read −¥3.29T, ordinary) as unresolved. The range was right; **the fiscal-factor semi-confirm (KB-SAM-211) did not flag an op of about ¥1.9T.** Not determined tonight: whether the check read the wrong settlement day (an 8/3 op settles about 8/5) or the op sat inside its noise. Either way, a "no signature" from that check cannot rule out an op of this size.
2. The earlier per-day split was wrong. The 7/30 Bloomberg estimate (~¥8.45T) was ¥0.47T high; my derived 7/31 residual (~¥6.95T) was ¥1.40T high, because it assumed two days and the third was 8/3.
3. **SAM-39 is unaffected.** Its window started 8/4 (inclusive), so an 8/3 op sits outside it. Its grade (TRUE-IN-LETTER / FALSE-IN-SPIRIT) stands.
4. Still open: the US account split (ESF vs SOMA), due in the FRBNY Q3 report ~11/13.

## 4. Balance of payments, September 2026 (PRIMARY, MOF/BOJ `bp202609.pdf`, released 08:50 JST 11/10)

Current account **+¥2,372.3B** (−45.8% y/y; August +¥3,993.1B revised; Sept-2025 +¥4,375.8B). Goods −¥187.5B, services −¥456.9B, **primary income +¥3,553.5B (−27.1% y/y)**, secondary −¥536.8B. Financial-account columns extracted scrambled from the PDF and are not quoted. Oil channel (VECTOR-5) still waits on the oil-benchmark repair; this is the denominator, not a verdict.

## 5. Market context at the read (vendor, not closes)

Tokyo open 11/10 (~10:20 JST): Nikkei 60,350.94, SoftBank Group (9984.T) ¥3,783 (+11.3% intraday, before results), USD/JPY 157.97. Arm closed 11/9 at $186.30 (+6.69%). Brent BZ=F $92.32 (evening session, not a settle). MOF 11/9 curve: 2Y 1.778 / 5Y 2.115 / 10Y 2.724 / 20Y 3.604 / 30Y 3.911 / 40Y 3.941.

## 6. JGB 30Y auction 11/10, #92 reopening, 4.2% coupon (PRIMARY, MOF `eresul20261110.htm`, read 22:41 ET 11/9)

Competitive bids ¥1,512.6B, accepted ¥450.7B → **BTC 3.356×**. Lowest-price yield 3.871%, average 3.847% → **tail 2.4bp**. Non-price-competitive I ¥148.8B.

**Grade under the frozen bars: SOFT, on both legs** (SOFT = BTC < 3.5 OR tail > 2.0bp): BTC 0.144× below 3.5, tail 0.4bp above 2.0. Trip margin above 0.1bp, so **no PRECISION-LIMITED tag**. `jgb_auctions.py` labels it "Orderly", which is its failure test (BTC < 2.0), not the frozen bars.

| 30Y auction | BTC | Tail bp | Frozen grade |
|---|---|---|---|
| 6/10 | 2.936 | 2.8 | SOFT |
| 9/3 | 3.788 | 2.1 | SOFT (tail) |
| 10/8 | 3.877 | 1.2 | NEITHER |
| **11/10** | **3.356** | **2.4** | **SOFT** |

Weakest 30Y since June; tail second-largest of the 15 in the ledger (since 9/2025). The average yield (3.847%) is 26bp below October's (4.109%): demand was thinner at the lower yield, consistent with insurers treating ~4% as the attractive level (Meiji Yasuda, REPORTED 10/2026), not proven by it. Sold the same morning the hawkish Summary of Opinions came out. **No failure (BTC well above 2.0), no cross-agent signal fires, no gate or prediction moves**; SAM-33 concerns BOJ operations, not auctions. Evidence for THESIS Pillar 2 (mixed super-long sponsorship), descriptive only.

## 7. SoftBank Group Q2 FY2026, graded (read 10:04–10:11 ET 11/10; the 02:47 ET pass fired late, laptop asleep)

**✅ ESTIMATE CONFIRMED.** SoftBank reported **15.9% at 9/30** (net debt ¥11.30T ÷ value ¥71.14T). Rolled to Arm $183.26 (10:06 ET, vendor) that is **22.5%**, against my A figure of 21.6% at the same price (+0.9, inside ±1.5). The SVF2 $10B OpenAI-shares loan is **inside** SoftBank's ratio (I had guessed outside), the OpenAI mark was **unchanged**, and SoftBank's pro forma (11/9 prices) implies **20.2% before the October $10B tranche**, 22.4% after. Arm for 25% on SoftBank's basis: **$145**. Full grade, §6 list and sources → `../2026-11-06_softbank/2026-11-10_RESULTS_GRADE.md`.
