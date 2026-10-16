# AUGUST 2026 TIC SESSION — ZHA-18 graded (DOCKET L405)

**Session:** ZHAO, spawned by PROME (8fb641db) at 16:16 ET on Fri 2026-10-16. Tier 1, WQ-184 due row.
**Release:** Treasury's press-release index lists "Treasury International Capital Data for August 2026"; it was seen at 16:19 ET; per LIQUID's read it is **sb0662**. **Pull:** `slt_table3.txt`, `slt_table1.txt` and `slt_table5.txt` from `ticdata.treasury.gov/resource-center/data-chart-center/tic/Documents/`, fetched with curl and a UA header at **16:17 ET 2026-10-16** (HTTP 200 on all three; the August 2026 rows were present).
**Letter graded against:** `reports/2026-09-18_PREREGISTRATION_ZHA-18_august-tic.md`, committed 2026-09-18 21:12 ET in `4c27c1548`. That is 28 days before the print, and the letter was not edited after it was committed.

---

## 1. GRADE — ZHA-18 resolves NO (branch B)

| Field | Value |
|---|---|
| Instrument | TIC Table 3, `for_lt_treas_net`, `China, Mainland`, 2026-08 |
| **Value** | **−$4,828M** |
| Branch | **B** (−$5,000M < LT < +$5,000M) ⇒ **NO**: the run breaks, and June–July was a two-month episode |
| Distance to boundary | **$172M** on the NO side |
| Confidence scored | 40% [2026-09-18] (the only mark; it is also the first call) |
| Brier | (0.40)² = **0.16** |

**The letter's §4 clause applies, recorded as it was written:** *"B is graded NO on a number like −$4.9B: the letter is right and nearly worthless — a 40% call resolving 100 bp from its own boundary says the threshold, not the forecast, did the work."* At −$4.83B this grade is **not banked as skill**. The threshold did the work. The direction (net selling) continued for a **third** month, and the magnitude halved for the second month in a row: −$15.77B → −$7.69B → −$4.83B. That fits the letter's deceleration line, *"a third step of similar proportion lands near −$4B,"* which put the deceleration on the record before the print.

**Base-rate update (n=43):** P(LT ≤ −$5B | prior two ≤ −$5B) moves from 3/9 to **3/10 = 30%**. The mean-reversion reference class was not refuted.

## 2. THE REST OF THE AUGUST PRINT (China, Mainland, $M)

| Cell | Aug-26 | Jul-26 | Jun-26 |
|---|---|---|---|
| Total holdings | **590,729** | 618,011 (unrevised) | 633,381 |
| Total net | −9,605 | −12,622 | −21,962 |
| LT net | **−4,828** | −7,685 | −15,769 |
| LT valuation change | −5,423 | −1,669 | −5,470 |
| ST net | −4,777 | −4,937 | −6,193 |
| Agency holdings (Table 1) | 134,180 | 141,091 | 141,966 |
| Agency net | −1,833 | −733 | −1,128 |

- **Level $590.7B (Table 5)** is the lowest level in the table's span (2020-01 →). It is the third month below the $650B line, already 🔴. **No new threshold fires.** Press "N-year low" framings are not certified here, the same rule as in July.
- **Total (incl. bills) net selling for a third month: −$9.6B.** The perimeter has to be stated: the scored leg is LT only.
- **TTM Sep-25..Aug-26:** total **−$102.1B**, LT **−$58.4B**. Level 699.7 → 590.7 = **−$109.0B**.

### ⚠️ 2a. ANOMALY: $12.3B of the August level drop is NOT explained by transactions or valuation

LT holdings fell **578,345 → 555,840 = −$22,505M**. Net transactions (−4,828) plus valuation change (−5,423) explain −$10,251M, which leaves a **residual of −$12,254M**. ST reconciles exactly (−4,777 = ST net).

- Over 43 months of China residuals, this is **the largest absolute value, by 1.6×** (the next is +$7.6B in 2025-08, then −$3.4B in 2026-03).
- In the same month **Belgium shows a +$19,845M residual** (LT holdings 393.8 → 416.2B on LT net +2.6B and ~0 valuation). Belgium residuals are habitually large, though: this one ranks 5th of 43, below +$30.8B in 2024-02.
- **Cause: UNKNOWN.** Possible candidates are a reporting-custodian reclassification, a benchmark or attribution adjustment, or an entity re-attribution. None was checked at a Treasury methodology note this session.
- ⛔ **NOT a custody-migration finding.** The Belgium proxy stays falsified (§3), and one month of opposite-signed residuals is the exact pattern CLAUDE.md §BELGIUM forbids reading as migration. **What it does change:** the August *level* overstates August *selling*. About 45% of the −$27.3B monthly level fall is non-transaction. Any "China dumped $27B" headline is wrong on the perimeter: the transaction figure is −$9.6B.
- **Open question for the next touch:** does TIC's August release or its FAQ carry an adjustment note? Ask LIQUID and HANS if either saw one.

## 3. DECLARED OBSERVATIONS (letter §3, recorded whatever the grade)

1. **Belgium:** level **$490.5B** (+$19.8B m/m, almost all of it the §2a residual). Total net −$47M, LT net +$2,586M. **YoY +8.74%** against the $451.1B Aug-25 base, which is **below 10%**: the first of the two kill-leg prints. **Recorded as SATISFIED-ON-BASE-EFFECT, NOT as evidence** (letter §2). Belgium did not even stay flat. It rose ~4% m/m, and the YoY still crossed under 10% because the base jumped $425.4B → $451.1B. The full thesis-kill still cannot fire, because China must be above $700B on three prints and it is at $590.7B. The re-spec of the leg is still owed and is not done here (letter §2: it does not belong in the grading document).
2. **rho(China, Belgium total net sales), n=43** (2023-02..2026-08): **+0.067** (LT-only +0.057). The rolling 24m is **+0.017** (LT −0.078), the 36m +0.017, and the 12m −0.151. The proxy reinstates only at a 24m rho below −0.5, so it **stays falsified**.
3. **Agency (Table 1):** holdings $141.1B → **$134.2B**, net **−$1.8B**. Agency was **sold again**, so rotation is refuted a third time.
4. **Official vs private (all countries, LT):** Grand Total LT net **+$108.9B**. Foreign Official LT **+$18.1B**, which implies private LT **+$90.9B**. Official bills **−$42.2B**. This is LIQUID's to price, and ZHAO only records it.
5. **Korea:** LT −$0.56B, ST +$2.90B, total **+$2.33B** (level $134.2B). No Korea selling, nowhere near the >$10B/month line. **Japan:** LT **+$11.9B**, ST **−$48.9B**, total −$37.0B (level $1,068.3B). Both are routed to SAM and LIQUID and not scored here.

## 4. SHARED-METRIC RECONCILE (LIQUID, DOCKET L721 leg ④)

The China figures were sent to LIQUID (liquid-1016) by SendMessage at 16:18 ET. **RECONCILED 16:2x ET.** LIQUID's packet (`inbox/2026-10-16_from-LIQUID_august-TIC-aggregate-reconcile.md`) read the aggregate from press release **sb0662**: official +18.1 / −42.2, private +90.9 / −5.6, all-foreign +109.0 / −47.8 / +61.2. These agree with Table 3 Grand Total (LT +108,908M · official LT +18,053M · official bills −42,214M · total +61,129M); the 0.1 gaps are rounding of summed parts. **One figure: the Table 3 $M cells.** LIQUID could not reach country files, so ZHAO supplied the China, Japan and Korea cells by message. LIQUID adopts ZHAO's country grade.

## 5. OWED-AT-THIS-TOUCH ITEMS (DOCKET L405 tail) — already discharged 2026-09-18, VERIFIED at the artifact

| Item | Disposition | Where |
|---|---|---|
| WQ-112 as-made re-marks (ZHA-11 65% · ZHA-12 55%) | **DONE 9/18.** The ledger carries `68% [2026-07-16] (first call 65% [2026-07-09])` and the ZHA-12 first call 55% [2026-07-16] | `reports/2026-09-18_WQ112_ASMADE_LEDGER_WRITE.md` §2; `PREDICTIONS.tsv` |
| Three RESOLVED re-scores (ZHA-03/04/15) | **REFUSED on canon 9/18.** WQ-112(i) says the latest dated pre-resolution mark governs, and all three marks predate resolution by 18–48 days | same report §3 |
| VX-ZHAO-8.01 | **That id is a FROZEN row** (the NPC GDP target, frozen 2026-08-21). The live need is a Vector-8 LNG VX row under the **next free id**, which is still OPEN and not done here: building one sets new thresholds, which this print does not force | `VX.tsv`; STATUS NEXT ACTIONS #9 |

The L405 row text predates the 9/18 discharge (the row was registered 9/17), so PROME can strike the tail.
