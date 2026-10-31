# GATE-BRK-R2 review at review_by 2026-10-31 + DAEDALUS 10/8 asks ①②③

**Desk:** BROCK · **Written:** 2026-10-31 (session start 09:27 EDT, from `date`) · PROME due-row wake (WQ-184, GATES row GATE-BRK-R2 review_by 2026-10-31). $0. No trade, no level, no operator, no population change.
**Primary sources** read this session: EDGAR submissions JSON + filing documents (accessions below), SEC XBRL companyfacts, SEC litigation-release / administrative-proceeding / press-release feeds, EDGAR full-text search (efts). Prices: `FORGE/tools/market-data/fetch.py price`, session 2026-10-30 (Saturday read).

---

## 1. GATE-BRK-R2 — state graded at primary, 2026-10-31

GATES row read whole (12 fields). Letter = `workbook/PC_REDEMPTION_REGISTER.tsv` (P1–P12, plus P13/P14 added today).

| Vehicle (P1) | (a) run / state | (b) latest FINAL | New since 10/28 (primary) |
|---|---|---|---|
| **North Haven PIF LLC** (CIK 0001851322) | **FIRED 9/25** (Q1 47.8 · Q2 41.6 · Q3 43.8 prelim) | **Q3 FINAL 43.7% → (b) NOT FIRED** | 🆕 SC TO-I/A Amendment No. 2, FINAL box ☒, acc 0001193125-26-432196, accepted 2026-10-26T21:29:29Z: *"based on the final count by the Company's transfer agent, the Company accepted for purchase on a pro rata basis approximately 43.7% of the Units validly tendered"*; 8,633,441 units, ~$152,293,899 paid ~10/27 at 9/30 NAV. Prelim 43.8 → final 43.7 = −0.1 pp. |
| North Haven PIF A (0001973476) — not counted (P2) | data only | Q3 FINAL 73.1% (prelim 73.3) | acc 0001193125-26-432189, 758,427 units, ~$14,842,421 |
| **OCIC** (0001812554) | **FIRED 10/2** (22.82 · 26.6 · ~30 prelim) | Q3 FINAL 29.8% → NOT FIRED (graded 10/28) | none since 10/28 bearing on R2 (8-K 10/23 = distributions/offering status) |
| **BCRED** (0001803498) | **2** (Q2 ~50 · Q3 ~50) | n/a (no final-results amendment on this fund; register line 38) | 8-K 10/22 = 9/30 NAV (KB-BRK-359). Next (a) read = Q4 letter ~12/03 (window 11/30–12/07). Q3 10-Q ~11/13 = final dollar value only, CANNOT fire (a) (L270). |
| ADS (0001837532) | 1 (Q3 issuer-stated 9/22) | rate never disclosed | 8-Ks 10/20 (Items 3.02/7.01/8.01) and 10/21 (7.01) — no proration statement found by text scan |
| Monroe (0001742313) | 1 (Q2 pro rata) | rate never disclosed | 🆕 Q4 offer SC TO-I acc 0001104659-26-119625 (10/28): up to 13,493,156 sh = ~5.0% of 9/30 shares. Q3 outcome still unread (Q3 10-Q ~mid-Nov). |
| CCLFX (0001735964) | 0 (not measurable) | — | 🆕 N-23C3A acc 0001213900-26-113636 (10/29): next 5% repurchase offer; **NAV $10.19 on 10/26/26** (issuer-stated) — extends the 10.76→10.72→10.67→10.52→10.39 series (distribution effects not netted). |

**Grade:** (a) FIRED ×2, unchanged · (b) NOT FIRED on both Q3 finals that exist · BCRED the only vehicle at 2 · 0 new fires today · no score move (redemption vector at its 5 ceiling; shared antecedent).

⚠️ **Found late, recorded against myself (trap 4 / LESSONS #30, again):** STATUS and the register carried the North Haven Q3 final at "~11/05", modelled from the Q2 cadence (+54 d from expiry). It was filed **10/26 (+42 d from the 9/14 expiry)**, the same afternoon as OCIC's final — five days before this review and two sessions (10/28, 10/30) that did not look. Grading is unaffected ((b) cannot fire at 43.7), but the modelled date was wrong in the same direction as 9/25's "7 days late". Cadence on this vehicle is NOT stable (+52 d Q1, +54 d Q2, +42 d Q3); the next read is keyed to the filing feed, not a modelled date.

🆕 **North Haven merger (8-K acc 0001193125-26-432017, Item 1.01, 10/26):** PIF A merges into PIF (NAV-for-NAV, PIF A holders get PIF Class I units); expected close **December 2026**; ~99% of PIF A's gross commitments overlap PIF's (press release Ex. 99.1) — independent confirmation of the P2 one-vehicle ruling; PIF base fee cut 1.25% → 1.00% from 1/1/2027. **Gate effect: none today.** After close, the graded registrant (CIK 0001851322) absorbs PIF A's holders, whose satisfaction ran ~26–30 pp higher (Q3 73.1 vs 43.7): a COMPOSITION change that mechanically lifts the graded cell's satisfaction from the first combined offer. Recorded as P14 so a later rise is not read as easing.

### review_by — recommendation to PROME
**Move review_by 2026-10-31 → 2026-11-16** (Mon), keyed to the Q3 10-Q filing deadline for 9/30 quarter-end non-accelerated filers (+45 d = Sat 11/14 → next business day). By then every Q3 primary on the six vehicles exists: BCRED Q3 10-Q ~11/13 (final dollar value; cannot fire (a)), Monroe and ADS Q3 10-Qs (Monroe's run could reach 2; ADS's Q3 table can confirm or not), and any North Haven / OCIC Q4 offer documents. The genuine (a) event after that is the **BCRED Q4 letter ~12/03 (backstop 12/07)**; the 11/16 review sets the next review_by to 12/07. ⚠️ The row's `consumed_by` text "BCRED next ~11/13 final" reads as a gate event; it is a dollar-value read that cannot fire (a) (DOCKET L270) — suggested re-cut below.

### Cell text for PROME (PROME writes GATES; BROCK writes the register)
- **state** (≤220 chars, lead token kept): `LIVE — (a) FIRED ×2 (North Haven 9/25 · OCIC 10/2; post-fire rule P13 PROPOSED); (b) NOT FIRED on both Q3 finals (OCIC 29.8 · NH 43.7); BCRED at 2, Q4 letter ~12/03 · hist→GATES_STATE_HISTORY`
- **last_checked**: `2026-10-31 BROCK review at primary: NH Q3 FINAL 43.7% (SC TO-I/A 0001193125-26-432196, 10/26) (b) NOT FIRED; NH/PIF A merger 8-K 10/26 (P14); P13 post-fire rule proposed`
- **consumed_by** (suggested): `EVENT: each vehicle's quarterly tender result at primary (next (a) read: BCRED Q4 letter ~12/03; BCRED Q3 10-Q ~11/13 = final $ only, cannot fire) | BROCK grades per print`
- **review_by**: `2026-11-16 · BROCK · keyed to the Q3 10-Q deadline (all six vehicles' Q3 primaries in); next → 12/07 (BCRED Q4 letter backstop)`

---

## 2. DAEDALUS 10/8 ask ① — post-fire rule per vehicle (P13, PROPOSED)

Written before any Q4-2026 figure exists (North Haven Q4 offer ~mid-Nov; OCIC Q4 ~late Nov; BCRED Q4 letter ~12/03).

- **(a) LATCH.** A vehicle whose run fires (a) stays FIRED. Each further consecutive sub-100% quarter is recorded (run depth 4, 5, …) and is **not** a new fire: no new packet, no new routing, no new X1 evidence. **Release** on any P9 reset event (a quarter satisfied in full · unmeasured or inferred-only · no offer — a no-offer quarter still routes separately as a red signal under P9(3)). After release the run restarts at 0; a new (a) fire needs three fresh consecutive issuer-stated sub-100% quarters.
- **(b) NOT LATCHED.** (b) is a single-quarter level: each FINAL strictly below 25.00% fires for that vehicle and quarter, whether or not (a) is latched.
- **Why latch (inversion test, trap 7):** in a world where redemption stress is easing but a 5% cap still binds, every quarter stays sub-100%. OCIC is that world on its own figures: requests 21.9 → 18.8 → 16.8% of shares, satisfaction 22.82 → 26.6 → 29.8%. Re-firing every quarter would fire every quarter there — it fails the inversion test. Restart-at-fire (re-fire every third quarter) fails the same test more slowly. Latch fires nothing new on an easing queue; (b) still catches a real deterioration. The letter's own "≥3 CONSECUTIVE" is a state that stays true while the run continues; the fire is the transition into it — latch is the reading closest to the letter.
- **Direction:** latch is the option with the fewest fires — against my book.
- **Panel depth:** release needs an observed 100% quarter; North Haven printed 100% in Q1 and Q2 2025 at primary, so release is reachable.
- **Status:** PROPOSED to PROME as an owner wording clarification. My C1 test: no level, operator, instrument or consequence changes; it settles an unaddressed case. PROME decides C1 vs Will (the gate is Will-ruled, WQ-158). Not in force until recorded; no post-fire quarter exists to grade before ~mid-Nov.
- **Effect today:** none. North Haven and OCIC latched FIRED; BCRED 2; ADS 1; Monroe 1; CCLFX 0.

---

## 3. DAEDALUS 10/8 ask ② — BDC median NAV discount refresh

Table: `NAV_DISCOUNT_39.tsv` (this folder).

| Measure | Value | Basis |
|---|---|---|
| **39 listed BDCs, median discount** | **28.68%** | 1 − close/NAV; closes 2026-10-30 (fetch.py); NAV = latest XBRL `NetAssetValuePerShare` (35 at 6/30, ARCC/HTGC/OFS 9/30, SAR 8/31) |
| 39-name mean | 22.31% | pulled toward premium by MAIN −62.9, CSWC −39.5, HTGC −35.3, TRIN −26.1, TSLX −8.6 |
| Fixed six-name diagnostic (ARCC/FSK/OBDC/BXSL/MAIN/GSBD) | 17.36% | was 17.23% on 10/13 closes (same Q2 NAVs except ARCC now 9/30) |
| Names >35% | 14 of 39 | PSEC 71.8 · PNNT 54.0 · OFS 51.4 · CION 48.5 · CCAP 48.0 · TPVG 47.8 · RWAY 45.3 · FSK 39.7 · … |
| Names <10% | 9 of 39 | incl. 5 at a premium |

**Reading:** exit §2 ("median narrows to <10%") **NOT MET** — 28.68% on this basis. VX-BRK-010 bands (>15 / >20 / >25 = RED): consistent with its RED. Convergence next-level ">35% median sustained": NOT MET; vector stays 🔴(4), no rescore.
⚠️ **Not the registered resolver.** VX-BRK-010's sector reading is the RJ 45-name median (32% at 10/8, paywalled; no fresh reading reachable). Different cohort, different method: no trend is claimed between 32% and 28.68%. ⚠️ Mixed NAV vintages: Q3 NAVs land through ~11/16; ARCC 9/30 NAV moved −0.2% vs 6/30 (19.35 → 19.31), so a 4-month-old NAV is a small error at the median, not at the tail.
Tail datum, not graded: OXSQ −18.6% and OFS −10.5% on 10/30 (OFS's Q3 10-Q was accepted 10/30; NAV $7.38 at 9/30).

---

## 4. DAEDALUS 10/8 ask ③ — DATED search attempts, BRK-11 / 18 / 25 / 26 (2026-10-31)

Each uses the instrument named on its PREDICTIONS row (10/30). EDGAR full-text search = `efts.sec.gov/LATEST/search-index`, exact-phrase terms, forms filter, custom date range; totals as returned.

| Row | Query (forms · window) | Total | Disposition |
|---|---|---|---|
| CONTROL | `"asset coverage"` (10-Q · 10/01–10/31) | 12 | instrument live; returns ARCC, HTGC, OFS, SAR Q3 10-Qs ⇒ most BDC Q3 10-Qs not yet filed |
| BRK-11 | `"asset coverage" "less than 150%"` (10-Q,10-K,8-K · 10/01–10/31) | 6 docs | all covenant/boilerplate: Barings CIC, Vista CSL, BC Partners Lending, Mount Logan credit-agreement covenants; HTGC 10-Q = SBA exemptive-order text (asset coverage 203.2% ex-SBA) |
| BRK-11 | `"asset coverage" "below 150%"` (same) | 2 | ARCC/MFIC merger agreement covenant (8-K 10/27) |
| BRK-11 | `"asset coverage ratio" "fell below"` (same) | 0 | — |
| **BRK-11 result** | | | **SEARCH-NOT-FOUND (10/01–10/31): no BDC breach.** ⚠️ window holds only ~4 Q3 10-Qs; the bulk lands 11/02–11/16 — re-run then. |
| CONTROL | `"GPU"` (10-Q · 10/01–10/31) | 9 | instrument live |
| BRK-18 (i) | `"GPU" "failure rate"` (10-Q,10-K,8-K,ABS-15G · 2/23–10/31) | 3 | Axe Compute (drug-trial failure rate), Penguin ("Zero Failure Rate" memory brand), TSS (equipment warranty) — none a GPU rate |
| BRK-18 (i) | `"GPU" "annualized failure"` (same) | 0 | — |
| BRK-18 (i) | `"GPU" "failure rates"` (same) | 10 | risk-factor / warranty boilerplate: IREN 10-K (climate → "higher equipment failure rates"), Oracle 10-K ("failure rates of certain components may differ from our expectations"), AMD, others — no published rate |
| **BRK-18 result** | | | **SEARCH-NOT-FOUND (2/23–10/31): leg (i) not met** ⇒ leg (ii) not reached. Oracle's 10-K language is mechanism-adjacent, not a rate. |
| CONTROL | `"% of par"` (10-Q · 10/01–10/31) | 93 | instrument live |
| BRK-25 | `"business development company" "sold" "of par"` (8-K · 5/01–10/31) | 77 | earnings-release balance sheets ("paid-in capital in excess of par") — phrase collision |
| BRK-25 | `… "secondary sale" "of par"` (10-Q,8-K) | 1 | TPVG: Revolut EQUITY secondary sale at a gain — not a loan |
| BRK-25 | `… "sold" "at a price of" "of par"` (10-Q,8-K) | 56 | all 56 fetched and scanned by script for "at a price of" within 120 characters of "of par": 2 hits, both note issuance at 100% of par; in the other 54 the terms are scattered across the document — no priced loan sale identified |
| BRK-25 | `… "realized loss" "sale of" "of par"` (8-K · 7/01–10/31) | 4 | PSEC, TCPC, FSK, ARCC — all "capital in excess of par" boilerplate |
| BRK-25 | `… "loan sale" "discount to par"` · `… "sold" "below par"` | 0 · 0 | — |
| **BRK-25 result** | | | **SEARCH-NOT-FOUND, and an instrument finding:** full-text search cannot isolate a priced loan sale — "par" collides with equity par-value boilerplate and the index has no proximity operator. As the row already says, a miss resolves on the invalidation clause by 12/31; this search cannot certify absence. Count stays 2. |
| BRK-26 | SEC litigation releases (feed + list page, ~9/21–10/30), administrative proceedings (same window), press releases (~9/11–10/30) | ~40 LR · ~40 AP · 25 PR titles | one CANDIDATE (below); Meyer Global (9/30, pre-IPO equity funds) and CityVest/TAG/Snowden (conflicts/custody) are not PC valuation. ⚠️ 5/01–9/20 not re-covered by this attempt (prior sweeps 6/8, 7/27, 8/28). |

### BRK-26 CANDIDATE — SEC v. SQN Capital Management LLC and Jeremiah Silkowski (not resolved today)
- **At primary:** LR-26671 (posted 10/9): complaint **filed 2026-09-18**, S.D.N.Y. No. 1:26-cv-08162; **settled — consent judgments entered 2026-10-08**, receiver appointed to liquidate the funds. Allegations: from at least 2019 through 2025 the adviser **inflated the net asset values of four investment funds** — valuations prepared by the CEO alone, not by the independent valuation expert represented to investors; NAVs "unchanged for years regardless of … the actual performance of the assets"; no audited statements; recidivist (custody/compliance-rule APs 2020 and 2023). Charges: Advisers Act 206(1), 206(2), 206(4), Rules 206(4)-2 and 206(4)-7.
- **What the funds held (one fund, one date, primary):** SQN AIF IV, L.P. (CIK 0001560046, SIC 7359 equipment rental & leasing) 10-Q at 9/30/2019: total assets $109.4M, of which collateralized loans receivable $54.1M + equipment notes $11.9M ≈ 60% loans/notes; the rest finance/operating leases, residuals, an SPV. Stopped filing 2020 (NT 10-K). ⚠️ The complaint PDF (comp26671.pdf) downloads but its fonts do not extract — the four funds are NOT named at primary by me; "credit-majority" is INFERRED from one fund's 2019 balance sheet.
- **Letter test:** formal action ✓ (filed complaint, settled judgment); after 5/01 ✓ (L657); size no floor ✓ (my 10/15 statement); **valuation ✓**; **"PC"? — the open question.** An asset-based / equipment-finance retail LP in wind-down is private lending in substance but is not the BDC / direct-lending class the row was written about on 5/01.
- **Why I do not resolve it alone:** a TRUE moves the row in my book's direction, and my 8/28 Tricolor refusal names this exact risk ("resolve my own prediction on a subject it was never written about"). The classification question goes to RED (the L657 co-reader) by packet, with my provisional reading: **letter-TRUE if "private credit" includes asset-based lending funds; on such a grade the mechanism miss is written beside it (idiosyncratic recidivist adviser, no read-across to BDC marks, not a Stage-3 catalyst ⇒ calibration value near zero, as BRK-30).** Confidence unmoved (55%); row stays OPEN; grade at or before RED's reply, latest 12/31.

---

## 5. Not worked this session
- **Radiant court-source gap** (STATUS row 10/31): not in this wake's task list; carried.
- BRK-26 5/01–9/20 enforcement window, BRK-25 named-trade press route (WALTER intake), BRK-11 re-run after the Q3 10-Q cycle (~11/16): carried as dated rows in STATUS.
