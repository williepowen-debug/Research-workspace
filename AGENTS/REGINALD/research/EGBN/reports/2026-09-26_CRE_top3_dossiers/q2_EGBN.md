# EGBN loss inputs: office · multifamily · bridge (6/30/2026)
*Built Sat 2026-09-26, read-only. $M. DERIVED = my arithmetic. N/D = not disclosed. Source keys at end. **Integrity:** every SEC figure below was re-extracted from freshly re-fetched `egbn_*` files (CIK 1050441 / Eagle Bancorp confirmed in each; byte-identical to the first fetch) after the shared-scratchpad `q.txt` warning.*

## A. Remaining office ($533.2M amortized cost / $533.9M principal)

**A1. Grade × class × state**
| Cut | $ | Source |
|---|---:|---|
| Pass / SM / Substandard (loans) | 456.1 (44) / 10.8 (1) / 66.3 (5) | D s20 (amortized cost) |
| …substandard on nonaccrual | 34.3 (2 loans: Fairfax $18.5, DC $15.8) | D s20, s25 |
| Substandard accruing | 32.0 | DERIVED 66.3−34.3 |
| Class A / B / C | 304.8 (13 loans, $36.9 criticized) / 219.1 (30, $40.2) / 9.3 (7, $0) | D s18 |
| DC CBD / DC other / MD / VA | 11.19% / 11.14% / 32.21% / 45.45% ≈ 59.7 / 59.4 / 171.7 / 242.3 | D s23; DERIVED ×533.2 |
| Criticized by state | VA ≥40.6 · DC ≥26.6 · $9.9 (2 small loans) N/D; pass by state N/D | D s25; DERIVED |
- DC CBD (~$59.7M) ≈ one loan: top-25 #12, pass, LTV 55% on an **11/8/2022** appraisal, matures 3/31/28. Top-25 #11: Montgomery $60.0M, pass, **LTV 80%** (12/31/24), matures 9/5/28 (D s26).

**A2. Maturities (principal) and appraisal vintage** (D s20)
| | 26Q3 | 26Q4 | 27Q1 | 27Q2 | 27Q3 | 27Q4 | 2028 | 2029+ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Maturing | 89.8 | 46.6 | 32.0 | 26.4 | 46.9 | 39.6 | 160.7 | 91.3 |
| Appraisal after 6/30/25 | 46 | 11 | 0 | 0 | 0 | 0 | 0 | 2 |
- Through 2028: $441.9M (82.9%). Only **~$59M (11%)** has a post-6/30/25 appraisal. ⚠️ The $46/$11/$2 bucket placement is read from the chart; the text layer lists them unlabelled.

**A3. LTV/DSCR as disclosed** (D s20; LTV = "most recently appraised value")
| Maturity yr | $ | Wtd LTV | Wtd DSCR | $/sf |
|---|---:|---:|---:|---:|
| 2026 | 136.4 | 65% | 1.2 | 248 |
| 2027 | 144.8 | 53% | 1.2 | 190 |
| 2028 | 160.7 | 61% | 1.4 | 222 |
| 2029+ | 91.3 | 68% | 1.6 | 245 |
| Total | 533.2 | **61%** | **1.3** | 224 |
- ~89% of these LTVs rest on pre-6/30/25 appraisals (DERIVED). Refresh triggers: maturity, modification, collateral dependency, or downgrade to substandard (D s20).

**A4. Office ACL $39.0M: specific vs collective (DERIVED)**
- Performing-office coverage 7.22% (Q; D s20) × (533.2−34.3 = 498.9) = **$36.0M collective**; 38.98 − 36.0 = **~$3.0M specific** on the 2 NALs. Deck s19 says "$39.8 in reserves" (+$0.8M; unreconciled).

**A5. Realized office severity**
| Measure | Value | Arithmetic / source |
|---|---:|---|
| Office bridge 6/30/23 → 6/30/26 | 976 − CO 205 − HFS 82 − paydowns 156 = 533 | D s19 |
| Loss content of all reductions | **46.3%** | 205/443 (deck's split) |
| CO ÷ (CO + HFS FV) | **71.4%** | 205/287; upper bound (some CO is partial on held loans) |
| Timing (9/25→12/25→3/26→6/26) | CO 187→188→188→205; **HFS flat $82M**; paydowns 106→129→132→156 | D3, D4, D1, D |
| Per-loan | DC NAL $33.2M → $15.8M in Q2 (**−52%** ≈ Q2 office CO +$17M); its value $44.6M → $38.5M (−13.7%) · Fairfax SS value $32.6M (5/29/25) → **$23.0M (4/2/26), −29.4%**, LTV 68→96% · DC SM $27.55M (2021) → $22.95M (3/18/26), −16.7% | D1 s27 vs D s25 |

⚠️ **No office went to HFS after 9/30/25**, so the 2026 transfers ($238.5M FV, $36.7M CO; Q Note 4) were **non-office**, and office was **≤$82M (≤41%) of FY-25's $201.4M transfer FV**. CREED's "FY-25 39.6% haircut was office-dominated" is **not established**; office share of transfer COs N/D.

**A6. Proposed office loss rates (on current carrying value, incremental)**
| Pool | $ | Base | Stress | Reason |
|---|---:|---:|---:|---|
| Pass | 456.1 | 2% | 8% | Stale-appraisal haircut **−20% / −35%**, anchored on EGBN's re-appraisals (−14% to −29%). CREED has no DC/NoVA office price (Project James $377.6M = failed maturity, not a sale; CREED map :42). At 61% LTV + 8% cost, value must fall ~34% before the average loan loses; loss is in the high-LTV tail (80% LTV → ~25% severity at −35%) |
| SM | 10.8 | 5% | 20% | LTV 47% on a fresh 3/18/26 appraisal; DSCR 1.26 |
| SS accruing | 32.0 | 15% | 40% | Fairfax $22.1M, 96% LTV: −10%/−20% value + 8% cost ⇒ 14%/23%; stress nears 46% cycle loss content |
| NAL | 34.3 | 10% | 35% | DC written to 40% LTV; Fairfax $18.5M at 76% (9/5/25) |
| **Total** | 533.2 | **$17.8M** | **$63.5M** | vs office ACL $39.0M: 0.46× / 1.63× (DERIVED) |

## B. Multifamily

**B1. Basis: IPCRE MF $692.8M vs Call Report 1.d MF $806.4M (+$113.6M)**
| Item | Value | Source |
|---|---|---|
| IPCRE MF (9/25→6/26) | 837.3 → 924.7 → 762.0 → 692.8 | Q3q, K, Q1, Q |
| Call MF / gap | 1,051.1 → 1,142.5 → 858.6 → 806.4 / gap 213.8, 217.8, 96.6, 113.6 | CR :15–18; DERIVED |
| Reconciliation | **N/D.** Inference: Call 1.d takes 5+-unit residential regardless of segment, adding mixed-use "predominantly residential" IPCRE (e.g. DC $63.3M, D s26 #9) and OO multifamily (D s24: "OO Multifamily – DC" NAL $7.2M); offset by lease-up/conversion MF that Call files in 1.a (Call construction $924.0M vs company $611.6M) |

**B2. MF by grade (6/30/26)**
| Grade | $ | Named loans (D s25) |
|---|---:|---|
| Pass | 408.6 (deck $408, 59%) | — |
| SM | 79.2 | DC apt $42.9M (LTV 58%, DSCR 0.67) · Other-US apt $36.4M (LTV 70%, 2021 appraisal, DSCR 0.89) |
| Substandard | 204.9 | PG $56.0M · Montgomery $50.5M · DC $35.4M (**paid off post-6/30**) · DC $26.1M (84%, 2021 appr.) · DC $20.5M · DC $10.9M |
| …nonaccrual | **~$7–11M** | s21 "1%"; s24 MF-DC $7.4M vs s25 DC $10.9M flagged NAL (unreconciled) |
| MF ACL / specific | $6.7M; specific N/D, ≤$6.1M (non-office IPCRE specific, C2) | Q |
- **Q2 criticized bridge** 175.1 → 284.2 (Q1: SM 43.0 / SS 132.0): +PG $56.0M (Q1 SM but **not in Q1 MF**, so it moved in from another class; top-25 still says "Construction CRE") +$36.4M +$35.4M +$26.1M − Fairfax apt $48.7M (Q1 SS, 61% LTV; exit route N/D) ≈ 280 (DERIVED; ~$4M sub-$10M residual).
- Call MF nonaccrual **$35.9M** (incl. HFS; CR :18) vs ~$7–11M HFI MF NAL ⇒ ~$18–28M of the **$25.6M nonaccrual HFS** is likely MF (inference; B1 basis caveat).

**B3. MF charge-offs: disposition vs retained** (Call RI-B charge-offs include write-downs on transfer to HFS)
| Qtr | Call MF CO | IPCRE gross CO | IPCRE retained (grid Δ) | MF disposition-linked |
|---|---:|---:|---:|---|
| Q3-25 | 14.7 | 123.4 | N/D (grid restates) | N/D; bank-wide ≥78% |
| Q4-25 | 6.3 | 8.1 | 1.9 (46.3−44.5) | **≥4.4** (6.3−1.9) |
| Q1-26 | 9.2 | 11.6 | **0** (Q1 grid has no IPCRE CO) | **≥6.3** (9.2 − OOCRE retained 2.9); 9.2 if all in IPCRE |
| Q2-26 | 11.1 | 38.0 | 23.7, of which office ~17 | **≥4.4** (11.1 − non-office retained ~6.7) |
| 4Q | **41.3** | | | **≥15.1 ex-Q3; likely most** |
- **Non-office realized haircut:** H1-26 transfers (all non-office, A5): FV $238.5M, CO $36.7M ⇒ **13.3%** = 36.7/275.2 (Q1 9.4%, Q2 16.5%); sales cleared at 101–103% of carrying. MF-only split N/D.
- Loss content of MF net runoff (Call): 41.3/(1,051.1−806.4) = **16.9%**; overstated (reclass-ins shrink net runoff).

**B4. Criticized >$10M maturing Aug–Dec 2026** (D s25; balance $M, value $M)
| # | Type / place | Bal | Grade | Mat | LTV | Value · appraisal | DSCR |
|---|---|---:|---|---|---:|---|---:|
| 1 | Apt, Prince George's | 56.0 | SS (accruing) | 8/21/26 (extended from 4/21) | 88% | 63.7 · 3/9/26 | 0.63 |
| 2 | Storage, Montgomery | 56.2 | SM | 8/10/26 | 72% | 77.7 · **7/27/22** | 0.93 |
| 3 | Office, Fairfax | 22.1 | SS | 9/25/26 | 96% | 23.0 · 4/2/26 | 0.74 |
| 4 | Storage, Anne Arundel | 15.0 | SS | 9/30/26 | 77% | 19.6 · **6/13/22** | 0.26 |
| 5 | Apt, DC | 42.9 | SM | 10/27/26 | 58% | 74.0 · 9/30/25 | 0.67 |
| 6 | Mixed use, Montgomery | 27.7 | SM | 10/27/26 | 53% | 52.6 · **10/18/21** | 0.76 |
| 7 | Office, DC | 10.8 | SM | 11/10/26 | 47% | 22.9 · 3/18/26 | 1.26 |
| 8 | Apt, Other US | 36.4 | SM | 11/30/26 | 70% | 51.9 · **9/29/21** | 0.89 |
| 9 | Apt, DC | 20.5 | SS | 12/30/26 | 84% | 24.5 · 6/13/26 | 0.15 |
- 9 loans $287.6M; DSCR<1: 8, $276.8M (dossier's "7/$249M" omits the $27.7M mixed-use). **MF: 4 loans, $155.8M (#1, 5, 8, 9).**

**B5. MF anchors and proposed rates**
- **LTV 58%:** with 8% cost, value must fall **37%** before an average loan loses (1 − 0.58/0.92).
- **DSCR 1.0 at DY 6.0%** ⇒ debt constant 6.0%; implied appraisal cap rate = DY × LTV = **3.5%** (DERIVED) — values not supported by current NOI. At a 5.0%/5.5% cap (assumption, unsourced) value −30%/−37% ⇒ wtd LTV **83%/92%**. A refi at 7.2–7.6% constant and 1.20–1.25× carries only **63–69%** of balance (DERIVED). Caveat: lease-up NOI (s25 fn 1).

| Pool | $ | Base | Stress | Anchor |
|---|---:|---:|---:|---|
| Pass | 408.6 | 0.5% | 3% | 3.5% implied cap; $404.6M matures H2-26 |
| SM | 79.2 | 5% | 15% | DSCR 0.67–0.89 |
| SS accruing (ex $35.4M paid off) | ~158.6 | **13%** | 30% | Base = H1-26 non-office haircut 13.3%; stress = −35% value on 84–88% LTV |
| NAL | ~10.9 | 20% | 40% | — |
| **Total** | 657.3 | **$28.8M** | **$76.1M** | vs MF ACL $6.7M: 4.3× / 11.4× (DERIVED: 2.04+3.96+20.62+2.18; 12.26+11.88+47.58+4.36) |

## C. Bridge inputs: **HOLDING-COMPANY basis** (the listed security)
| Item | Value | Source |
|---|---:|---|
| CET1 (holdco) | **$1,186.8M, 14.58%** | Q capital table |
| RWA | **$8,140M** | DERIVED 1,186.828/0.1458 (±$3M); bank basis not used |
| CET1 excess over 10% | $372.8M | DERIVED |
| Total capital / leverage | $1,288.8M, 15.84% / 11.22% | Q |
| TCE / TBVPS / shares | $1,150.5M / $37.73 / 30.49M | R p12 |
| PPNR Q3-25 / Q4-25 / Q1-26 / Q2-26 | 28.76 / 10.66 / 27.66 / 29.08 | R trend: NII + nonint inc − nonint exp (e.g. Q4: 68.303+12.192−69.837) |
| PPNR TTM / Q2 ann. | **$96.2M** / $116.3M | DERIVED (Q4-25 has $10M legal + disposition costs) |
| Dividends | $0.01/sh/qtr since Q3-25 → **~$1.2M TTM** | Q3q equity stmt; DERIVED 0.04×30.49M; H1-26 paid $0.608M (Q) |

**C2. Mutually exclusive CRE pools** (amortized cost; Q vintage grid; ACL from Q Note 4; specifics DERIVED)
| Segment | Pass | SM | SS accruing | NAL | Total | ACL | Specific |
|---|---:|---:|---:|---:|---:|---:|---:|
| IPCRE: office | 456.1 | 10.8 | 32.0 | 34.3 | 533.2 | 39.0 | ~3.0 |
| IPCRE: MF (principal) | 408.6 | 79.2 | ~194–198 | ~7–11 | 692.8 | 6.7 | ≤6.1 |
| IPCRE: other types (principal) | 1,328.7 | 92.1 | ~52.7–56.2 | ~29.9–33.4 | 1,507.0 | 23.1 | 0–6.1 (6.1 − MF specific) |
| **IPCRE total** | 2,190.4 | 182.1 | 281.8 | 75.1 | 2,729.4 | 68.8 | **9.1** |
| OOCRE | 1,596.2 | 45.4 | 14.1 | 5.1 | 1,660.7 | 17.2 | ~0 |
| Construction C&R | 461.2 | 27.7 | 29.3 | 5.0 | 523.1 | 4.4 | 0.07 |
| Construction C&I (OO) | 88.5 | — | — | — | 88.5 | 1.1 | 0 |
| **HFS (at FV; exclude from loss pools)** | 24.1 accruing | | | 25.6 NAL | 49.7 | — | — |
- **Specific** (DERIVED) = NAL amortized cost − Level-3 FV of individually assessed (Q Note 11): commercial 24.77−15.89 = 8.88; IPCRE 75.12−66.02 = 9.10; construction 0.07; consumer 0.15; OOCRE ~0 ⇒ $18.2M vs disclosed **$18.5M**. ACL $121.1M = $18.5M specific + **$102.6M collective**. IPCRE NAL: $30.9M no allowance / $44.3M with (Q Note 4).
- **Overlaps:** (1) substandard **includes** all $111.1M NAL (every class); doubtful 0. (2) Deck C&C "incl. HFS" $760M = SM 274.2 + SS 459.8 + **NAL HFS 25.6** — use 10-Q HFI figures. (3) By-type criticized table is **principal** ($539.5M), grid is **amortized cost** ($539.0M). (4) PG apt $56.0M: "Construction" on top-25, reconciles into IPCRE MF — count once, in MF. (5) DC apt $35.4M SS paid off after 6/30.

## BOTTOM LINE
1. **Office:** 85.5% pass at 61% LTV, ~89% on appraisals >12 months old; EGBN re-appraisals run −14% to −29%. Loss **$18M base / $64M stress** vs $39M office ACL (~$36M collective + ~$3M specific).
2. **Office severity:** cycle loss content 46% (71% ex-paydowns, upper bound). **No office to HFS since 9/30/25**; office ≤41% of FY-25 transfer FV.
3. **MF is the reserve gap:** $284M criticized, $6.7M ACL. The appraisals imply a **3.5% cap rate** (6.0% DY × 58% LTV), so the 58% LTV overstates the cushion. Loss **$29M base / $76M stress**, 4–11× MF ACL.
4. **MF charge-offs:** of ~$41M (4Q), **≥$15M provably disposition-linked**, most of the rest likely. Best non-office severity anchor: **13.3% H1-26 HFS haircut**.
5. **Holdco:** CET1 $1,186.8M / RWA ~$8,140M (14.58%), $373M over 10%, PPNR TTM $96.2M, dividend ~$1.2M/yr. Office+MF stress ~$140M pre-tax ≈ 1.45 yrs TTM PPNR (139.6/96.2), before other CRE.

**Sources** (base URL sec.gov/Archives/edgar/data/1050441/). Q = Q2-26 10-Q acc 0001050441-26-000096 …/000105044126000096/egbn-20260630.htm (Note 4, Note 11, MD&A criticized/ACL-by-collateral, maturity, capital tables) · D / R = Q2-26 8-K acc 0001050441-26-000088 deck final-2q2026egbnearnings.htm (s16–s26) / release final-erq2x2026xearnings.htm · D1 / Q1 = Q1-26 deck acc 0001050441-26-000062 a1q2026egbnearningsdeck3.htm / 10-Q acc 0001050441-26-000066 · D3 = Q3-25 deck acc 0001050441-25-000122 s19 · D4 = Q4-25 deck acc 0001050441-26-000006 s19 · Q3q = Q3-25 10-Q acc 0001050441-25-000134 · K = FY-25 10-K acc 0001050441-26-000021 · CR = `AGENTS/REGINALD/workbook/CRE_RCN_COHORT.tsv:15-18` · CREED = `AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:42`, `…_REGINALD_TOP3_PROPERTY_TEST.md:70-100`.
