# CRE → bank loss transmission — OZK leg (2026-09-27, Sun evening)

**Asked by:** PROME `prome-9b`, for Will's 17:24 ET objective. Brief: `PROME/plans/2026-09-27_cre-to-bank-loss-transmission-PLAN.md` (e614dee5e). **Reconciles to:** REGINALD `reports/2026-09-26_CRE_top3_loss_bridge.md` @ b93e3ac58 plus its dossier `reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md`. ⚠️ The bridge file had one uncommitted working-copy line at read time, in a non-OZK line. I read it as-is.
**Scope rule:** research only. **Zero** scores, thresholds, weights (OZK-09 45% · A30/B45/C8/D17), conviction, tools or trades moved. The only new pull was the Q2'26 8-K bundle's PPNR table, to verify a cited figure.

## Bottom line

**(1) The best-evidenced mechanism is not RaDD. It is the maturity-failure → foreclosure → foreclosed-property route on 2022-vintage construction and transitional loans.** It is already running in the filings: three credits went to foreclosure in Q2 after charge-offs, and 2022-vintage loans account for 82% of H1 gross charge-offs. Recognition happens late, because of how OZK marks collateral.

**(2) Capacity: I agree with REGINALD's arithmetic, and it reproduces.** Where I differ is that $656M is a tail scenario that lands all at once. My desk's probability-weighted RaDD loss is ~$129M, not $361M. Losses also arrive over quarters, against ~$260M a quarter of pre-provision revenue. **For OZK this is an earnings-and-timing question, not a capital question.**

**(3) The case against is strong on capital and track record, and weaker on marks.** Its best single facts:
- the RESG book has a 46% weighted LTV;
- $2.1B of RESG commitments ran off in one quarter, mostly through repayments;
- no foreclosed-property mark has yet been tested by a sale at scale, in either direction.

**Isolated or broader, for PROME:** OZK's losses are mostly **idiosyncratic**: sponsor-level failures on large, single-project loans in lab and office markets. There is **one broader channel**, the ~$430M book of loans to other CRE lenders ("debt-on-debt"), which first charged off in H1-26. That is non-bank CRE-lender stress arriving at a bank.

---

## (1) Strongest evidenced mechanism

### OBSERVED

| # | Fact | Figure | Source (dated) |
|---|---|---|---|
| O1 | Loans that failed at maturity went to nonaccrual | Boston 10 Prospect $169.3M, **matured Feb 2026**, equity declined to extend, forbearance expired → nonaccrual. Baltimore land $40.0M **matured 12/18/25**, 212 days past due | Q2'26 Mgmt Comments (MC) p.23, Fig. 23; 10-Q (FDIC FLNG 11981, filed 8/5/26) |
| O2 | …then foreclosure within the same quarter, after a partial charge-off | Seattle Chapter I/II foreclosed June after the buyer withdrew (charge-offs $22.3M + $3.7M). Atlanta office went special mention → foreclosed June ($8.5M charge-off). San Carlos paid off with a $14.8M charge-off. **Q2 RESG partial charge-offs = $49.3M on 4 loans** | MC p.23-24; 10-Q |
| O3 | The vintage engine | **$85.2M of $103.5M H1-26 gross charge-offs (82%) are 2022-vintage** | 10-Q p.13 |
| O4 | Foreclosed property is piling up, not selling | Foreclosed assets $61.1M (Dec-25) → **$292.7M** (Jun-26). H1 inflows $241.6M, **sales $6.9M**, write-downs $3.0M. Carried at **86–100% of as-is appraisals** | 10-Q p.22; MC p.24 |
| O5 | Late recognition by method | Nonaccrual $300.4M, of which **$257.8M (86%) carries $0 loan-loss reserve**. Only $13.7M reserved. The allowance-to-nonperforming ratio fell from 886% a year earlier to 154% | 10-Q pp.19, 25, 46 |
| O6 | Foreclosed-property losses bypass the provision line | OREO write-downs and holding costs go through non-interest expense ("elevated expenses related to nonperforming assets"; H1 holding cost `Y923` $8.7M) | 10-Q pp.35-36; REGINALD dossier (Call Report) |
| O7 | Aggregate outcome | Annualized NCO **0.69%** in Q2 (Q1 0.56%). Nonperforming assets **$593M / 1.42%** (Q1 $451M / 1.08%). Classified + criticized **$1,282M, up from $1,215M**, while RESG commitments fell $27.8B → $25.7B | Q2 8-K bundle (FLNG 11969, 7/21/26) |
| O8 | The broader channel: loans to CRE lenders | Debt-on-debt book `RCON2746` $1.20B (6/25) → **$430.3M** (6/26). **First charge-offs in 18 quarters: `RIAD5409` $42.4M YTD**, most likely The Jack + San Carlos (a $63K gap) | FFIEC Call Report RSSD 107244; `CALL_REPORT_2026Q2_LOG.md`; `Q2_2026_10Q_READ.md` F3 (INFERRED-HIGH) |

**Why this mechanism and not the others:**
- **RaDD** is the largest dollar exposure, but it has **no observed loss.** It was pass-rated at 6/30 (by elimination), interest is paid from reserves, and extension plus recap are in negotiation (7/22 call).
- **Adverse selection** (runoff concentrating the residual book) is a *pattern* in O7, not a loss route.
- **Foreclosed-office marks** are the *next stage* of the chosen mechanism (O4), not a separate one.

### SCENARIO ASSUMPTIONS
- "Late recognition" assumes appraisals lag market-clearing prices. Basis: O5, plus a mark on OZK's own vacant Seattle office (760 Aloha) at 58% of a Nov-24 appraisal (REGINALD dossier; **n=1, $6.4M, a mark to an offer rather than a completed sale**).

### UNKNOWNS
- Gross flows between buckets. Balances cannot tell cures from migration (kill-§1 is FIRED-LITERAL, mechanism UNDETERMINED).
- Sale prices on the $288M of RESG foreclosed property, since almost none has sold.

---

## (2) Capacity to absorb — reconciled to REGINALD's bridge

### OBSERVED (re-verified today where marked ✔)

| Input | Value | Source | Agree? |
|---|---|---|---|
| Pre-provision revenue (PPNR), trailing 4Q | ✔ **$1,082.6M** (Q3-25 $290.6M · Q4-25 $279.0M · Q1-26 $253.6M · Q2-26 $259.4M) | Q2 8-K bundle, PPNR reconciliation table | ✔ ties to REGINALD's $1,083M |
| PPNR trend | **−10.7%** from Q3-25 to Q2-26. Q2 run-rate ≈ **$1,037M/yr**, and the 10/1 sub-notes reset takes another ≈$11.2M/yr | same; `CALENDAR.md` (SOFR 3.87% FRED 9/22 + 209bp) | **Addition:** use the run-rate, not trailing. 0.6× is unchanged (~0.61×) |
| CET1 / RWA | $5,300.5M / $44,916.2M = **11.80%** (preliminary; the MC figure is an image) | Call Report RC-R per REGINALD dossier; 11.80% matches the dossier arithmetic | ✔ |
| Loans-only reserve | **$461.5M** (+ $156.3M unfunded-commitment reserve = $617.8M total ACL) | Q2 8-K bundle / 10-Q | ✔ loans-only is the right basis |
| Payout, trailing 12 months | Common dividends $203.9M + preferred $16.2M + buybacks $176.6M = **$396.7M (57% of net income)**. **Dividends alone ≈ 32%** of net income ($51.7M/qtr vs $163.3M) | dossier; bundle p.47 | ✔. ⚠️ **Label:** "57%" includes buybacks. The fixed claim (64 straight quarterly dividend increases) is ~32% |
| New buyback | $200M authorized 6/29/26 (7/1/26–7/1/27). **Q3 execution: unknown** | 10-Q p.57; MC p.38 | ✔ ~0.45pp CET1 if fully executed |
| Sub-notes | $350M: Tier 2 counts only 80% from 10/1. Total capital 14.83% → ~14.67% if retained, ~14.05% if redeemed. **CET1 is untouched either way** | 10-Q pp.57-60 (`Q2_2026_10Q_READ.md` F9) | Not in the bridge; immaterial to CET1 |

**Reproduction:** ($656M stress − $19–35M reserves) = $620–636M × (1 − 25% tax) = $465–477M ÷ $44,916M RWA = **1.04–1.06pp** → 10.74–10.76%. Less the $200M buyback (0.45pp) → **~10.3%**. ✔ Matches.

### Where I differ, and why

| # | Point | Effect |
|---|---|---|
| D1 | **The $361M RaDD stress is the D-branch (foreclosure) tail applied with certainty.** On this desk's tree, D is **17%**. B (migration to substandard) is 45%, and under OZK's collateral method (O5) B can book near-$0 reserve if the appraisal holds. Weighted expected loss is **~$129M** (`IQHQ_PLAYBOOK.md` §4, Will-approved 7/23). | A probability-weighted OZK stress is roughly **$656M − $361M + ~$129M ≈ $424M** (my arithmetic, not a bridge rerun) → ~0.4× PPNR |
| D2 | **Severity basis.** 65% comes from Campus at Horton: a **$130M credit bid on a $399M loan** (Sep-25), which is the lender's own bid, not a market sale, on a mall-to-office conversion. ⚠️ **Correction (9/27, after delivery):** the playbook's canonical D-severity band is **50–65% → $275–360M** (§3, l.159-163; adjusted down from Horton's 67% for RaDD's stronger product). The "65–70%" that STATUS, CALENDAR, LIFE_SCI and playbook l.16 carried — and that REGINALD/CREED quoted as "the OZK desk's severity" — was a mislabel that never matched those dollars (65–70% of $555M = $361–389M). REGINALD's 65% = the band's TOP, so its $361M ≈ the playbook's $360M: **the bridge's dollars are unaffected; only the label was wrong.** **Horton's post-foreclosure leasing is unchecked (owed; UNKNOWN after the 9/27 web sweep).** | 50% → RaDD stress ~$278M (−$83M) |
| D3 | **Timing.** v1.5's core claim is that recognition is appraisal-gated and back-loaded. So "no earnings offset" is an instantaneous worst case. Spread over 4 quarters, run-rate PPNR (~$1.03B) less common + preferred dividends (~$220M) leaves ~**$800M pre-tax** before any CET1 erosion, **if the buyback is paused** | CET1 need not fall at all on $656M over a year. It falls only if losses come in one quarter **and** the buyback runs |
| D4 | **OREO stress anchor is small-n.** The 40% office-OREO stress rests on 760 Aloha (58%, $6.4M) and a Boston office (80%, $9.4M). Together that is **~$16M of evidence for a $137.5M pool**, plus external comps (−61% to −72%). The *direction* is sound; the *level* is thinly anchored | Uncertainty on ~$55M of the stress, either way |
| D5 | **Conservative items in the bridge's favor:** tax at 25% vs the H1 effective 22.2% (≈ +0.04pp worse); no relief on risk-weighted assets from charged-off construction loans (HVCRE-weighted up to 150%, so relief ≈ +0.1pp) | Small. They offset in the bridge's favor |
| D6 | **Coverage gaps I agree matter most:** the pass RESG book (~$14.7B), the 2022-vintage source of O3; RaDD's ~$360M unfunded; the debt-on-debt book beyond its nonaccrual | The bridge's number is a floor for these pools, not a ceiling for the bank |

**Net position:** **I agree with the arithmetic and with the conclusion that OZK is "earnings drag, not capital"** (0.6× PPNR vs FLG's 8–11×). I differ on how to read the size: $656M is a tail-at-once. The number I would carry is **~$420M probability-weighted under stress, ≈0.4× a year of PPNR (~1.6 quarters' worth), with CET1 roughly flat if it arrives over several quarters and the buyback is paused.** The live risk is how long recognition is deferred, and the earnings path, not solvency. That is RESERVOIR v1.5.

### SCENARIO ASSUMPTIONS
- PPNR holds at the Q2 run-rate (it has fallen 4 quarters running: margin compression plus expense growth, efficiency ratio 39.2% vs 35.5%).
- The dividend keeps growing (64-quarter streak). The buyback is discretionary.

### UNKNOWNS
- How much of the $200M buyback ran in Q3 (it prints with Q3).
- Whether the mezzanine lender's recap on RaDD adds new cash equity (the 7/22 call gave no terms).
- The allocation of the general reserve by grade (not disclosed; REGINALD's range assumption).

---

## (3) Strongest evidence AGAINST the stress thesis (stated as strongly as I can)

| # | Argument | Evidence |
|---|---|---|
| A1 | **The collateral cushion is real and large.** RESG weighted LTC 49% and **LTV 46%** (fully funded, 243 credits). Sponsors have 50%+ equity below OZK. A 50% value decline across the book still leaves the average loan whole | Q2 8-K bundle PDF p.31, MC text above Fig. 24 (6/30/26) — ✔ re-read 9/27 |
| A2 | **The book is repaying at par, which is cash, not a mark.** RESG commitments −$2.1B in one quarter. Sullivan Courthouse ($156.4M nonaccrual) was **recapitalized into a pass loan**. The Jack (new-equity LOI) and Wauwatosa (hard-deposit sale, proceeds ≥ carrying) were slated to close in Q3 | 8-K bundle; MC p.23 |
| A3 | **Earnings dwarf the problem.** Q2 NCO $56.3M against PPNR $259.4M = **4.6× coverage** in the worst quarter so far. Even REGINALD's tail is **0.6×** a year of PPNR. TBV/share rose **+$1.26 in Q2** to $48.41 | 8-K bundle |
| A4 | **The central event failed to happen on schedule.** The August RaDD maturity passed **swept-and-empty** (8/31). No specific reserve and no downgrade. Management put "will remain a pass-rated credit" on the record. A third party (the mezz lender) is negotiating to recapitalize, which is someone putting money in | 7/22 call; `IQHQ_AUG_WINDOW_CLOSE_SWEEP.md` |
| A5 | **Leading indicators improved.** Past-due fell $465M → $298M. The 30-89 day bucket fell −88% (Call Report basis $190.9M → $23.3M) | Q2 bundle; Call Report |
| A6 | **One pillar of the stress story is already dead.** The "37.6% hidden CRE" ratio reproduces at no quarter (retracted 8/23; OZK ranks 5th of 14, not worst). The debt-on-debt book it pointed to has **shrunk 64%**, so the risk is running off, not building | `MI3_2025Q3_ADJUDICATION.md`; REGINALD 8/13 |
| A7 | **Stress-period record.** NCO beat the industry in virtually every GFC quarter, and the bank was profitable every quarter of 2008 (WEAKNESSES C6: acknowledged as "the strongest bull argument"). Market evidence also shows performing CRE can clear at par (ARI ~$9B at 99.7%, CREED) | `WEAKNESSES.md` C6; CREED 9/26 |
| A8 | **The market already prices it.** 0.97× TBV at $46.89 (9/25 close). Short interest **16.5M shares ≈ 16.3% of float, 17.6 days to cover** (9/15). Citi Sell $40, MS Underweight. Stress is consensus, not variant | fetch.py; Nasdaq/FINRA; stockanalysis.com 9/27 |

**Where the case against is weakest:**
- A1 is a book-wide average of LTVs against *appraisals*, and O5 shows appraisals are what lags. The loss sits in the tail: the $147M condo at **105.6% LTV**, and Boston at 91% on a Nov-25 appraisal.
- A2's repayments are the healthy loans leaving, which is the adverse-selection tell (O7).
- A7's GFC bank was a ~$2B community lender, not today's $25.7B national RESG book.
- None of these points is disproven. They mean the case against proves **capacity**, not **clean marks**.

---

## Next observations that would change the conclusion

| When | Observation | → Toward stress | → Against stress |
|---|---|---|---|
| **10/1** (read Fri 10/2, `flng_watch.py`) | $350M sub-notes reprice | Reprice as scheduled is **neutral**: ≈$11.2M/yr PPNR drag, CET1 untouched | Redeemed without replacement = management spending capital confidently (Tier 2 −$280M). Mildly against, **not** a credit signal |
| **~mid/late Oct** (date due ~9/30) | **Q3 print + call: the "~92-day" RaDD report-back** | Any RaDD specific reserve, downgrade to substandard, or extension **without** paydown or new equity → D1's weighting shifts toward the bridge's tail | An **executed** extension **with** curtailment or new cash equity → the RaDD stress shrinks toward $0 in the base case |
| same | Foreclosed-property sale prices vs carrying (8150 Sunset LOI → contract; Seattle; Atlanta) | Sales below ~80% of carrying → confirms mechanism (1) and the D4 office-OREO stress | Sales at carrying → the 86–100% marks hold; the OREO stress is overstated |
| same | Boston 10 Prospect ($169.3M, $0 reserve): the $330M sale closes, or OZK takes title | Title + new appraisal → the largest single loss event (bridge stress $85M) | Sale closes → ~$0 loss |
| same | Special mention $616M: reversal or migration into classified | Migration of the 5 RESG credits ($529M) → adverse selection hardens | Reversals to pass → management's "churn" claim holds |
| same | Q3 NCO vs the ≤55bps kill line; the buyback run-rate | NCO > 0.69% and rising | NCO ≤ 55bps → thesis kill-§2 re-opens honestly |
| ~Nov 1-10 | Q3 Call Report: `RIAD5409` (debt-on-debt charge-offs), `RIAD5415` (OREO sale gains or losses) | Continued charge-offs → the broader channel is live | $0 → H1 was two credits, not a trend |
