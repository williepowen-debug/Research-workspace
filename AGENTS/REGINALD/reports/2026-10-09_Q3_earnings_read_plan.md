# Q3-2026 earnings read plan — is regional-bank stress concentrated or spreading, and through which balance-sheet channel?

**Written:** 2026-10-09 Fri, ~21:3x–22:xx ET, REGINALD (Will-directed, Opus 5.5). **Before any cohort bank has printed** (first: CFG Fri 10/16).
**Asked by:** Will, 10/9: *"Is regional-bank stress still concentrated in particular banks, or is it spreading — and through which balance-sheet channel?"* Bounded monitor repair first; then a read plan built on the EXISTING frozen frames and the 10/7 funding baseline, unchanged.
**Bounds:** no baseline redone, no grading rule changed, no score/threshold/trade moved, no agent launched. The only new pre-print lines are §2.3's AMTB non-CRE lines, because no frame covers that leg; they are dated before the print and are observation lines, not triggers.

---

## 0. The answer first

1. **Provisional judgment (pre-print): CONCENTRATED on the balance-sheet evidence — which runs only through 6/30.** Each stressed bank has its own named mechanism: FLG rent-regulated multifamily, EGBN multifamily after its office cleanup, OZK RESG foreclosure and recognition, AMTB non-CRE business/owner-occupied/home loans, WAL single-credit charge-offs. Across the 14-bank cohort the **total-CRE** bad-loan rate **fell** (2.46% → 2.23%, 6/30/25 → 6/30/26, original Call Report basis, §2.0 ②) and H1 CRE charge-offs fell ($528M → $452M). The **multifamily** sub-read also fell year on year (3.88% → 3.58%) but **rose last quarter** (3.23% → 3.58%), all of it at FLG, EGBN and CFG. That is individual-bank deterioration, not a spread. At 6/30 **no bank of six showed cheap-deposit flight**. Non-bank (NDFI) exposure is concentrated at CUBI and CFG, with no attributable loss beyond WAL's single First Brands credit.
2. **If it is spreading, the channel with visible pressure ahead of the banks is multifamily CRE recognition:**
   - Freddie Mac multifamily delinquency 0.64% [Aug], its 4th straight rise.
   - Trepp CMBS multifamily 8.04% [Sept].
   - Funding cost at a cycle-high rate level comes second. Non-bank credit draws come third, with no observed trigger.
   - ⚠️ These are **property-market** series, not bank books. They make multifamily the channel to watch; they are not evidence that any bank's book is deteriorating.
3. **What points the other way, unattributed to any balance sheet:**
   - **Discount-window borrowing:** $9.965B on Wed 10/7, the highest Wednesday since at least Jan 2024. Borrowers are not named.
   - **The equity selloff:** since 9/15 it has been led by size, with the largest banks falling most.
   - **KRE outflows:** KRE shares outstanding −4.6% since 9/29.
   - **Financial stress:** the St. Louis Fed financial stress index (STLFSI4) tightened +0.34 in one week.
   - **What they don't show:** none of these sorts on any of my exposure measures, so they do not yet locate a channel.
4. **Most consequential unresolved question:** **does the TOTAL-CRE bad-loan rate, on its original basis, rise >50% QoQ (or show a new foreclosure build) at ≥3 of the five mid-pack banks (WAL, VLY, SSB, BKU, SBCF)?** That is the DOCKET L180 breadth test, and §2.0 defines it.
   - **Multifamily is reported beside it, never instead of it.** Property data puts the pressure in multifamily, so the multifamily sub-read is where a spread would show first. It cannot by itself decide the breadth verdict.
   - **Why this one:** a "yes" is the only pre-registered observation that turns "concentrated" into "spreading". Deterioration at FLG, EGBN, OZK or AMTB alone is individual-bank deterioration, however severe (§2.0).
   - **Timing:** releases show it only partially. The planned retrieval of the Q3 Call Reports is **11/07**, with completeness checked then. The FFIEC token for that run **expires 11/05** (Will action).

---

## 1. Repair result (bounded pass, committed `8255c2d13`; stopped there)

| Gap found at the 10/9 boot | Fix | Verified |
|---|---|---|
| OZK's 8-K and insider checks queried the **SEC (CIK 1569650)**. OZK has filed nothing there since 2017, so its "no filings" line was guaranteed. | 8-K: **FDIC FLNG cert 110 through the OZK desk's own `flng_watch.evaluate()`** (imported, not copied). Insider: FDIC disclosure list `/api/instdiscl/cert/110`, identity keyed on cert 110 (pre-2017 rows read "Bank of the Ozarks"). | Live: 182 filings, newest 8/5, none in window → CLEAR; 471 disclosures, newest 8/14 → CLEAR |
| **VLY was keyed to CIK 74260 = OLD REPUBLIC INTERNATIONAL** (found during the repair). It would have shown Old Republic's 8-Ks as VLY's. | CIK 714310. Every SEC response must now name the expected issuer, or it is **PARSE**, never "no filings". | Selftest case reproduces the Old Republic feed → PARSE |
| FLG, AMTB, CFG, CUBI not covered | Added to both monitors (CIKs from SEC `company_tickers.json` 10/9). A `PRIORITY` list (CFG CUBI EGBN FLG OZK AMTB WAL) with no route = **UNCOVERED** | Selftest: drop AMTB → rc 2, no all-clear |
| Failure, parse error and uncovered bank could print "✅ no filings" | Per-name **CLEAR / FOUND / FAILED / PARSE / STALE-ROUTE / UNCOVERED**. A route whose newest filing is >120 days old is STALE-ROUTE (the OZK-at-SEC shape). rc 0 read · 1 review · 2 incomplete; `boot.py` now shows OK / ALERT / INCOMPLETE / FAIL and prints its all-clear only when every script is OK | Live run with the network blocked: 8-K rc 2 (9 FAILED), insider rc 2, **no all-clear line**. Selftests 16/16 and 11/11 |
| Earnings countdown held a hand-typed April list | Reads the new canonical table in `CALENDAR.md` (Q3-2026 BANK EARNINGS DATES). Checks each weekday against its date; a malformed table is rc 2, not "no dates" | Selftest 8/8; live table prints 12 names, CUBI + FLG flagged ESTIMATE |
| The FLG price-ladder check read the in-progress daily bar as a close (10:26 ET: $11.25) and a NaN bar at 20:3x ET | `scripts/settled_bars.py`: **today's (ET) bar and any NaN bar are always excluded** and printed as NOT GRADED. The ladder uses it, and the CLI cross-checks Nasdaq historical for the WAL exit log | Selftest 4/4. Live: FLG last settled $11.35 [10/8], 10/9 NOT GRADED; WAL 10/2–10/8 agree on both routes |

**First live findings from the repaired monitors:** CFG filed an 8-K on 10/8 (item 5.03), which retires its already-redeemed Series G preferred. That is routine capital housekeeping. No open-market insider purchase was found at any of 7 names over 14 days.

**Remaining limitations (recorded, not fixed):**
1. **FDIC FLNG carries OZK's filings, not its press releases.** OZK's earnings release, date notices and dividends need a press search (OZK desk MEMORY 10/2), so the monitor cannot see them.
2. **The OZK insider check cannot tell a purchase from an award.** The FDIC gives A/D (acquired/disposed) or a PDF, not the P code. Any OZK Form 4 in the window is therefore **UNREAD** (no verdict) until someone reads the PDF.
3. **Severity is by item number only.** Earnings-week 2.02 filings will raise ALERTs by design, and 5.03 is always 🟠 even when routine (CFG 10/8).
4. **An evening run of the settled filter grades only through yesterday.** Today's close is graded next session.
5. **`thresholds.py` and `market.py` still print live quotes as "breaches".** These are quotes, not settled grades, and they were not changed.
6. **Coverage gaps:** insider coverage is the 7 priority names (ZION and VLY are covered by the 8-K check only). `si_refresh.py` (short interest, 9/14 vintage) was not touched.
7. **CUBI and FLG dates are estimates** until they are announced, and the CALENDAR table is updated by hand.

---

## 2. Earnings-read plan

### 2.0 Three definitions that govern every row below (Will's clarifications, 2026-10-09 21:33 ET, set before any print)

**① Individual-bank deterioration ≠ cross-bank spread.**
- **Every per-bank row below grades ONE bank:** "deteriorated at this bank" or "did not".
- **A spread is a COHORT claim, and only two pre-registered aggregates can make it:**
  - **L180 breadth (CRE):** ≥3 of WAL · VLY · SSB · BKU · SBCF → **BROADER**.
  - **FL-rail aggregate:** ≥2 of BKU · SSB · AMTB · SBCF TRANSMITS (frozen frame §3).
- **What does not count as spread:**
  - Deterioration at FLG, EGBN or OZK. Those are the already-named banks, and worse numbers there are **severity at a named bank**.
  - Deterioration at AMTB. No pre-registered aggregate covers non-CRE credit, so a matching pattern at another bank is reported as a co-occurrence, never graded as a spread.
- **The funding list (Q1) has no cross-bank rule.** Its result is reported as a count ("k of 6 UP") with no spread label. No aggregate rule is added here.

**② The bad-loan rate keeps its ORIGINAL basis; total CRE and multifamily are separate evidence.**
- **Basis:** `reports/2026-09-27_cross-bank_CRE_transmission.md` §A3/§E, FFIEC Call Report (`workbook/CRE_RCN_COHORT.tsv`).
  - **Total-CRE bad-loan rate** = (`na_con + na_mf + na_noo` + `pd90_con + pd90_mf + pd90_noo`) ÷ (`bal_con + bal_mf + bal_noo`). That is nonaccrual plus 90+ days past due, over construction + multifamily + non-owner-occupied. Owner-occupied is excluded (SR 07-1).
  - **Foreclosure build** = `oreo_total_k` rising, the §A3 basis. The CRE-only split (`oreo_con + oreo_mf + oreo_nfnr`) is shown beside it, never substituted.
  - ⚠️ **Open limb, flagged and not re-defined:** L180 and §D never quantified "new foreclosure build". I read it literally, as any QoQ rise at reported precision (the reading the FL frame's A2.2 gives "rises QoQ"). On that reading **WAL already met it at Q2** (+$2.9M, +2.3%), so the limb is loose. Every grade prints the size of each rise beside the verdict. A materiality floor would be a rule change, and is Will's to make.
  - **L180 grades on these two only.** (L180 says "CRE bad loans up >50% QoQ"; its source §D says the bad-loan **rate**; the rate is the basis.)
- **Multifamily sub-read, reported separately:** (`na_mf + pd90_mf`) ÷ `bal_mf`, and `oreo_mf`. It locates the channel. **It never enters or replaces the L180 count.**
- **Release figures are provisional** for both. Banks define "CRE", "nonperforming" and "multifamily" on their own bases (e.g. NPLs incl. 90+ accruing, or criticized). A release figure is labelled with its own basis and is never mixed into the Call Report rate.
- **Property-market series** (Freddie, Trepp, CMBS) are a third category: context, never bank evidence.
- **Baseline on this basis, 14 banks, no bank missing** (computed 10/9 from the existing ledger, no new pull):

| Cohort | 6/30/25 | 9/30/25 | 12/31/25 | 3/31/26 | 6/30/26 |
|---|---:|---:|---:|---:|---:|
| Total-CRE bad-loan rate | 2.46% | 2.59% | 2.45% | 2.22% | **2.23%** |
| Multifamily bad-loan rate (sub-read) | 3.88% | 4.02% | 3.73% | 3.23% | **3.58%** |

- **Total CRE** is down year on year and flat last quarter.
- **Multifamily is down year on year but ROSE last quarter** (+0.35pp, Q1 → Q2). The rise sits at FLG (7.27 → 8.06%), EGBN (3.98 → 4.45%) and CFG (1.58 → 2.12%). At the five mid-pack banks, multifamily was flat or falling: BKU 1.61 → 0.34, SSB 1.05 → 0.90, VLY 0.73 → 0.74, WAL 0, SBCF 0.10.
- ⇒ **At 6/30 the multifamily rise was individual-bank deterioration at FLG, EGBN and CFG, not a spread.** CFG is a Q1 (funding) name, and its multifamily rise is recorded for CFG only.
- **L180 on Q1 → Q2 as a dry run:**
  - Rate >50%: **0 of 5** (WAL +11%, VLY +11%, SSB / BKU / SBCF down).
  - Foreclosed property rising: WAL only (+2.3%).
  - So *c* = 1 on the literal reading. The Q3 test starts there.

**③ Missing banks stay UNKNOWN whenever they could change the breadth verdict.**
- **For any breadth count:** let *c* = banks confirmed meeting the test, *m* = banks whose data is missing, *k* = the threshold.
  - **BROADER / TRANSMISSION** if *c* ≥ *k*.
  - **NOT BROADER** only if *c* + *m* < *k*.
  - **Otherwise UNKNOWN**, naming the missing banks.
- **Worked example for L180 (k = 3):** 2 meet, 1 does not, 2 missing → **UNKNOWN**, not "2 of 5".
- **The FL-rail aggregate gets the same overlay:** a NOT-GRADEABLE or UNREAD name that could flip the class makes the aggregate UNKNOWN, not MIXED or NO TRANSMISSION. Recorded as Amendment A3 in that frame; no bar or cell edited.
- **This replaces L180's "name the unavailable banks and grade the rest"** wherever grading the rest would produce a verdict the missing banks could overturn. PROME owns the DOCKET row and is packeted.

**④ 11/07 is the planned RETRIEVAL date, not a completion date.**
- **What happens on 11/07:** retrieve the Q3 Call Reports for all 14 banks. **Check completeness then**: which banks have a Q3 filing in CDR, and whether any is an amendment.
- **What the check feeds:** any bank absent at retrieval is *m* in ③. No breadth verdict is written before that check runs.
- **Prerequisites:** the JWT (expires 11/05) and the cohort-selection question (DOCKET L180 rider) are prerequisites, not part of the check.

**Basis rule for every row:** the **earnings release** (8-K EX-99.1/99.2, deck, call) gives a **provisional** read. The **10-Q** and the **Call Report** (my run **11/07**) confirm or add. A line the release does not print is **INCONCLUSIVE — "line not printed"**, never inferred. Dates are verified at the issuer unless marked ESTIMATE (CALENDAR table, 10/9).

### 2.1 Q1 — funding costs or deposit losses coinciding with increased non-bank credit draws (frame: `reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md` Deliverable 2, frozen 10/7)

The legs are unchanged:
- **F1:** non-interest-bearing (NIB) deposits fall >5%, or NIB share falls ≥2pp.
- **F2:** interest-bearing (IB) deposit cost rises ≥10bp.
- **F3:** brokered deposits or FHLB advances rise ≥15%, or uninsured share rises ≥2pp.
- **N:** NDFI / fund-finance balance up >5%, or a disclosed NDFI criticized or nonaccrual increase.
- **Grading:** **UP** = ≥2 F legs **and** N · **DOWN** = no F leg and no N · otherwise **INCONCLUSIVE**.

| Bank · date | Release line (provisional) | 10-Q / Call Report line (confirming) | Owner | **UP at this bank** (individual; not a spread — §2.0 ①) | **DOWN at this bank** |
|---|---|---|---|---|---|
| **CFG · Fri 10/16** pre-open (time inferred), call 09:00 ET · CONFIRMED | Supplement average-balance table: IB deposit cost (Q2 2.08%), total cost 1.63%, average NIB ($39.88B), NIB share (22% company basis), borrowed funds | 10-Q Table 9: capital call ($9,852M) + secured private-credit finance ($4,875M) → **N grades ~early Nov**. Call Report Memo 10 at 11/07 | REGINALD (no CFG desk). BROCK reads CFG for BRK-31 (F1/F2 attribution) | UP: IB cost ≥2.18% or NIB ≤20% or average NIB <$37.9B, **plus** borrowed funds ≥15% (FHLB >$7.32B [CR]), **and** capital call + PC >$15.46B | DOWN: IB cost ≤2.08%, NIB ≥22%, capital call + PC ≤$15.46B. ⚠️ An IB-cost rise **inside** management's "NII up 2.5–3.5%" guide with no N = INCONCLUSIVE |
| **CUBI · ESTIMATE Thu 10/22 after close (NOT ANNOUNCED, searched 10/9)** | EX-99.1: IB deposit cost (Q2 3.54%), NIB average and share (31.8%), digital-asset vertical spot balances ($3.8B), specialized lending ($7.65B), FHLB advances | **N is ungradeable from the release** (fund finance is not broken out) → Call Report Memo 10b+10c vs $3.60B at 11/07 | REGINALD (no desk) | UP: NIB average −5% or DA <$3.42B, **plus** FHLB ≥15% or IB cost ≥3.64%, **and** specialized lending >$8.03B | DOWN: IB cost ≤3.54%, NIB ≥31.8%, FHLB flat/down, specialized lending ≤+5%. A DA-only move = INCONCLUSIVE (crypto cycle) |
| WAL · Mon 10/19 after close · CONFIRMED | IB cost (2.74%), deposit composition | 10-Q NDFI table ($15,812M / 25.9% of HFI loans), beta assumptions | **WAL desk** (print frame L170); my WQ-318 row is the funding leg only | Per the WQ-318 row | A deposit decline **inside the announced ~$4B optimization** = INCONCLUSIVE. A warehouse-only NDFI rise = INCONCLUSIVE |
| OZK · Tue 10/20 after close · CONFIRMED | Cost of interest-bearing deposits (COIBD, 3.24%), brokered ($2.52B), fund + lender finance ($2,070M) | FDIC 10-Q NDFI ($3.26B) | **OZK desk** (L520); funding leg mine | COIBD ≥3.34% **plus** brokered ≥15% / any FHLB, **and** N | COIBD +1 to +9bp = the pre-announced "inflection" + hike → INCONCLUSIVE |
| EGBN · Wed 10/21 after close · CONFIRMED | IB cost (3.37%), brokered share (32%), uninsured coverage (183%) | — | REGINALD | F only (no NDFI book) | Average-deposit decline inside the −10 to −13% guide = INCONCLUSIVE |

**Expected modal outcome (stated 10/7, unchanged): most rows INCONCLUSIVE.** Two declared deposit programs (WAL, EGBN) and one pre-announced cost inflection (OZK) absorb the likeliest F moves, and N needs a 10-Q or Call Report at four of six. **Q1 most likely cannot be answered UP or DOWN from the releases alone; CUBI's N leg certainly cannot.**

### 2.2 Q2 — CRE deterioration vs genuine cures, sales, foreclosure transfers and loss recognition (frames: `reports/2026-09-26_CRE_vulnerability_top3.md` §6 "weakens if" + the 9/26 loss bridge; `reports/2026-09-27_cross-bank_CRE_transmission.md` §D/§F; WQ-313 DOCKET L35 · L521 · L180 · L514; specialist frames for their names)

**Classify every CRE decline before reading it as improvement**. These are the cross-bank comparison labels this desk owns:

| Label | Means | Evidence that proves it |
|---|---|---|
| **CURE** | the borrower performs again: upgrade to pass, or payoff with **outside** cash | Named upgrade, or a payoff with a stated outside refinancing. ⚠️ Takeout funding is UNDISCLOSED for ~every payoff (§F.4) ⇒ most "payoffs" grade **PAYOFF-UNSOURCED**, never CURE |
| **SALE** | loan sold or moved to held-for-sale | Price vs carrying value (EGBN sold at ~101–103% of marks in Q2). Price vs par is undisclosed everywhere |
| **FORECLOSURE TRANSFER** | loan → foreclosed property (OREO) | OREO build. The loss is deferred until sale (OZK carries OREO at 95–100% of appraisal; WAL books zero OREO valuation loss) |
| **RECOGNITION** | charge-off or write-down at transfer | Net charge-offs (NCOs); held-for-sale (HFS) transfer marks |
| **DETERIORATION** | new problem loans | Inflows into nonaccrual, criticized or special mention, net of the above |

| Bank · date | Release line (provisional) | 10-Q / Call Report (confirming) | Owner | **Deteriorates at this bank** (severity at a named bank, not a spread — §2.0 ①) | **Does not deteriorate** / scenarios overstate |
|---|---|---|---|---|---|
| **EGBN · Wed 10/21 after close · CONFIRMED** (call Thu 10/22 10:00) | NPLs, criticized/classified, NCOs; HFS sales vs post-write-down marks; the Prince George's apartment loan ($56.0M, matured again 8/21) and the Fairfax office loan ($22.1M, matured 9/25): paid, extended, downgraded or nonaccrual (L35) | **Multifamily criticized table is 10-Q only** (~early Nov): ≤$284M; downgrades into criticized <$100M (vs $216M) | REGINALD (no EGBN desk). **RED** grades its CHG-027 branches on the same print. CRE top-3 owner = me | Downgrades ≥$100M; MF criticized >$284M; HFS transfers marked <85% of cost; the Aug–Dec criticized maturities extend at a haircut | Downgrades <$100M; retained-book NCOs <$10M; HFS marks ≥85%; criticized maturities pay off. Insufficient disclosure → record "outcome not disclosed in Q3 deck" (L35) |
| **FLG · ESTIMATE Fri 10/23 before open (NOT ANNOUNCED; Earnings Whispers says Mon 10/26)** | Nonaccrual (back below $2,675M?), NCOs, provision, criticized NYC rent-regulated pool (<$4.0B), rent-regulated provision commentary after the 10/1 rent freeze (T-08 fired) | **10-Q ~11/6:** MF special mention ≤$2,757M, H2 modifications <$556M, risk grades. **Call Report ~11/14** | **FLG desk** (T-03 release · T-02 10-Q · T-13 modification/payoff read L522). I compare only | Special mention >$2,757M with substandard rising; modifications ≥$556M; rent-regulated nonaccrual loss ratio above ~17% as loans resolve | The reverse of each. ⚠️ FLG's "par payoffs" carry an unreconciled $133M between H1 charge-off schedules, so a payoff is not a cure until sourced |
| **OZK · Tue 10/20 after close · CONFIRMED** (call Wed 10/21 08:30) | NPA, OREO ($288M at 6/30) and **any OREO sale price vs carrying value**, special mention ($616M) reversal or migration, NCOs, **RaDD outcome** (bridge matured 10/9; OZK desk reads Mon, L635) | FDIC 10-Q + Call Report ~early Nov (`RCON2746`, `RIAD5409`) | **OZK desk** (L520). I compare only | OREO sold near 58% of appraisal (the offer-mark comparable), not 86–100%; special mention migrates down; new RESG loans to nonaccrual or OREO | OREO sold at or near carrying value; special mention reverses; NPA stops rising |
| WAL · Mon 10/19 after close · CONFIRMED | NPLs vs the ~$500M guide, NCO vs Q2, office-classified slide, the $99M life-science credit, OREO valuation | Q3 10-Q frame (L171) | **WAL desk** (print frame) | The NPL rise continues (WAL is the only name whose CRE problem loans rose every quarter) — then WAL displaces OZK on direction | Management's guide met (NPL ~$500M, ACL >100% of NPLs) |
| **Breadth — mid-pack (THE cross-bank row):** VLY Thu 10/22 before open (L521) · SSB / BKU Wed 10/21 · SBCF Tue 10/27 · WAL Mon 10/19 | Provisional only, each on its own release basis, labelled: CRE nonaccrual/NPL and foreclosed property. VLY: does the Q2 multifamily 30–59 cohort cure or roll; CRE nonaccrual vs $256.1M; re-defaults of the $108M payment-delay loans. FL names: frozen FL-rail cells | **L180 on the Call Report, retrieval planned 11/07 with completeness checked then:** per bank, the total-CRE bad-loan rate up >50% QoQ **or** `oreo_total_k` rising (§2.0 ②). **Multifamily sub-read reported separately; it is not counted** | REGINALD (no desks). CORAL consumes the FL rail. CREED owns the QBP (L514, ~11/25) | *c* ≥ 3 → **BROADER**. This is the only CRE observation that answers Will's question. | *c* + *m* < 3 → **NOT BROADER at Q3**. Anything between → **UNKNOWN**, naming the missing banks (§2.0 ③). The 14 chosen banks are not the population |

### 2.3 Q3 — AMTB's distinct non-CRE credit problem · **Thu 10/22 after close · CONFIRMED** (call Fri 10/23 09:00) · owner REGINALD (no AMTB desk)

**Why it is distinct:** CRE is 5.8% of AMTB's nonaccruals ($9.8M of $168.8M, 6/30/26). The problem is C&I ($79.0M), owner-occupied real estate ($40.5M) and single-family residential ($31.2M). Its reserve covers **51%** of nonaccruals (ACL $85.5M), and 78% of the nonaccruals carry no allowance because they are collateral-dependent at a 47–71% LTV (dossier, Q2 10-Q).

**Frozen frame that applies:** the FL-rail frame (`reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md`, A1/A2), unchanged. Primary cell: CRE non-owner-occupied nonaccrual >$11.2M TRANSMITS. Classified $273.1M rising QoQ, with the rise not attributed in **quantified** form to acquired pools, also TRANSMITS. The resi-rate cell is EXCLUDED (FL-resi sub-read).

**New pre-print observation lines for the non-CRE leg (written 10/9, before the print; not a trigger, no routing).** They use the FL frame's own rule shape, above the prior four-quarter high:

| Line (8-K EX-99.1 NPA and classified tables) | 6/30 baseline | Prior 4Q high | WORSENING if | NOT WORSENING if |
|---|---:|---:|---|---|
| C&I nonaccrual | $79.0M | $85.5M (3/26) | > $85.5M | ≤ $79.0M |
| Owner-occupied nonaccrual | $40.5M | $40.7M (3/26) | > $40.7M | ≤ $40.5M |
| Single-family residential nonaccrual | $31.2M | $31.2M (6/26) | > $31.2M **and** the rise is not attributed, in dollars, to purchased pools (H1 purchases $506.2M) | ≤ $31.2M |
| ACL ÷ total nonaccrual | 51% | — | < 51% | ≥ 51% |

- **How a decline is read:** it is labelled with the §2.2 vocabulary. Q2's declines were sales-driven, which is "realized, not healed".
- **What it answers, and what it doesn't:** this leg answers whether AMTB's problem is healing or worsening, **at AMTB**. A worsening AMTB is individual-bank deterioration (§2.0 ①). If BKU or SSB print the same C&I / owner-occupied pattern, I report it as a co-occurrence. It is not graded as a spread, because no pre-registered aggregate covers non-CRE credit.
- **BRK-31 boundary:** BROCK excludes AMTB residential-growth artifacts from BRK-31 (frame R4).

---

## 3. Counterevidence carried, unchanged (it argues for "concentrated", or against reading the tape as balance-sheet stress)

1. **June baseline:** no cheap-deposit flight at any of the six. NIB share was flat (within 0.5pp) or up year on year. IB deposit costs fell 27–52bp over four quarters. CFG was the only one whose cost rose in Q2 (+4bp). (`2026-10-07` report §1a–1b.)
2. **Negative price attribution:**
   - The 8/14→9/14 leg was small-cap beta with no bank component.
   - The selloff did **not** sort on my private-credit NDFI proxy: rank correlation −0.559 at n=14 collapsed to −0.255 at n=26.
   - The 9/15→9/29 leg sorted on **size** (ρ −0.72). My matrix sorts the wrong way (+0.48). (`2026-09-29` report.)
   - **The market has not priced a channel I can name.** That fits both "absent" and "unseen".
3. **Cohort CRE improved year on year at 6/30:** the bad-loan rate fell 2.46% → 2.23%, NCOs fell $528M → $452M, and only OZK had a sharp new rise (`2026-09-27` cross-bank §A3).
4. **Nano Banc (failed 9/25) is n=1, legal-cost-driven.** No other bank nationally met even three of its four ratios.

**Post-6/30 data that cuts the other way (recorded, not attributed):**
- Discount window $9.965B [10/7], borrowers unnamed (H.4.1 via WALTER).
- Equity: KRE $69.01 [10/9 vendor quote], −6.9% from 74.11 [9/14]. KRE shares −4.6% since 9/29.
- Financial stress: STLFSI4 −0.809 → −0.468 [9/25 → 10/2].
- Credit: high yield 324 peak [10/1] → 315 [10/8]; CCC 1,252 [10/8] = high in FRED's data window.
- Property: Trepp Sept office 12.16% / multifamily 8.04%; Freddie multifamily 0.64% [Aug].
- **None of these names a bank or a balance-sheet line.**

---

## 4. What a missing disclosure prevents me from concluding

| Missing at the release | Prevents | Where it may appear |
|---|---|---|
| CUBI fund-finance balance (inside "specialized lending") | Any N grade for CUBI ⇒ CUBI cannot grade UP from the release, and so Q1's only both-legs name stays open | Call Report Memo 10, 11/07 |
| CFG capital-call + PC finance (10-Q Table 9) | CFG's N leg ⇒ a CFG funding move is F-only, INCONCLUSIVE | CFG 10-Q ~early Nov |
| EGBN multifamily criticized table | The EGBN "weakens if" MF line | 10-Q ~early Nov |
| FLG special mention, modifications, risk grades | Whether FLG's multifamily is migrating or curing | 10-Q ~11/6; T-13 ~11/9–13 |
| OZK OREO sale prices | Whether OZK's foreclosure marks hold ⇒ cannot separate **foreclosure transfer** from **recognition** | Call / 10-Q / any 8-K |
| Takeout funding behind payoffs (every bank) | **CURE vs bank-financed exit** ⇒ payoffs grade PAYOFF-UNSOURCED, so "the refinance market is open" stays an inference | Not observable in aggregate (CREED) |
| Sale price as % of par (every bank) | True loss severity (only % of carrying value is disclosed) | Rarely disclosed |
| Uniform total-CRE bad-loan rate (original basis) at the mid-pack banks | The L180 breadth test ⇒ **"spreading" cannot be graded from releases alone.** A bank still missing at the 11/07 retrieval is *m*, and the verdict is UNKNOWN wherever *m* could flip it (§2.0 ③) | Call Reports, planned retrieval **11/07** with completeness checked then (**FFIEC token expires 11/05**) |
| WAL $99M life-science outcome | WAL's direction leg | Call / 10-Q backstop (absence = PENDING-10-Q, never benign) |

---

## 5. Read schedule (grade each frame within one session of its print; update the conclusion only when evidence changes)

| Date (ET) | Read | Grades |
|---|---|---|
| Tue 10/13 | JPM / WFC / C (context only, not cohort) · Nano P&A re-check (L516) · FRED 10/9 cell for REG-T-03 | none of mine |
| **Fri 10/16** | **CFG** (+ MTB context) | Q1 CFG row (provisional) |
| Mon 10/19 PM → Tue 10/20 | WAL | Q1 WAL funding row; read the WAL desk's grade for Q2 |
| Tue 10/20 PM → Wed 10/21 | OZK | Q1 OZK funding row; read the OZK desk's grade |
| Wed 10/21 | BKU (am) · EGBN + SSB (pm) | Q2 EGBN rows (L35) · FL-rail cells · Q1 EGBN F-only |
| Thu 10/22 | VLY (am) · AMTB + CUBI(est.) (pm) | L521 VLY checkpoint · §2.3 AMTB · FL-rail AMTB · Q1 CUBI (F only) |
| Fri 10/23 (est.) | FLG | read the FLG desk's grade; my cross-bank row |
| Tue 10/27 | SBCF | FL-rail SBCF |
| ~early–mid Nov | 10-Qs | N legs; FLG/EGBN 10-Q-only lines (individual) |
| **Sat 11/07** | **Planned Call Report retrieval; completeness checked then** (which of 14 have a Q3 filing, any amendments) | F1/F3/N confirms; **L180 breadth on the original basis, with the UNKNOWN rule**; multifamily sub-read reported separately; matrix re-score with OREO added |

**Update rule:** the §0 judgment changes only when a graded row moves it:
- **Toward "spreading":** only a cross-bank aggregate can move it, i.e. **L180 = BROADER** or **FL-rail aggregate = TRANSMISSION CONFIRMED** (§2.0 ①).
- **Individual-bank results:** a Q1 UP at one bank, or deterioration at FLG / EGBN / OZK / AMTB, is recorded as **individual-bank deterioration**. It changes that bank's severity, not the concentrated-vs-spreading answer.
- **Ungraded rows do not move it:** an INCONCLUSIVE, "line not printed" or UNKNOWN result moves nothing, and is stated as such in the grade.

---

## 6. What this does NOT do

- Moves no score, threshold, ladder level, trade or REG-T row. A Q1 UP or L180 BROADER produces a dated note to PROME; any threshold idea goes to Will as a proposal.
- Does not grade specialist names (WAL, OZK, FLG). Their desks own those frames; I consume their grades and own the cross-bank comparison.
- Does not re-run the 10/7 baseline or edit any frozen frame. The FL frame, the WQ-318 list and the CRE §6 lines stand verbatim.
