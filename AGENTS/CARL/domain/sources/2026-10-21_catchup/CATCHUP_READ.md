# CARL catch-up read — 2026-10-21 (PROME wave 3)

**Written:** 2026-10-21 22:44 ET (`date`), CARL (Claude Code, Opus 5.5), PROME-spawned (prome-56, wave 3 of `PROME/plans/2026-10-21_agent-catchup-PLAN.md`; Will 21:56 ET authorization). Last own work commit before this: 2026-10-15.
**Scope:** whole-inbox drain (2 PROME packets, 1 WATT packet, 8 WALTER lane signals) + the 10/20 due rows this desk owns (CRL-29 first grade; Q3 SYF/ALLY/COF). No threshold, band, score rule or v2.6.6 score change. FRED was in maintenance all session (every FRED pull returned no data): FRED-only cells are UNAVAILABLE 10/21 and carry their last dates.

## 1. Drain — every signal, its disposition

| Signal | What it says (read whole at BOARD) | Disposition | Where integrated |
|---|---|---|---|
| SIG-W-20261015-003 | September PPI +1.3% m/m, +6.3% y/y; core ex-FET +0.5%/+5.0% | acted | §2, KB-538, STATUS CPI/PPI row |
| SIG-W-20261015-007 | Exeter DEEP extensions fell while 60+ DQ rose = part of worsening may be less masking; Carvana jump stands | acted | §3, KB-539, STATUS auto row |
| SIG-W-20261018-008 | WSJ price pass-through (unopened); NY eating/drinking places −1,928 (−3.8%) YoY Q1 (QCEW) | acted | §6, KB-540 |
| SIG-W-20261019-006 | CPS warehouse $390M→$518M; Enova $200M to 2028; Exeter reserve support | acted | §3, KB-539 |
| SIG-W-20261019-008 | September 5/9 deals worse YoY and MoM, 44/44; OTTO-31 12→8% | acted | §3, KB-539 |
| SIG-W-20261019-012 | Ally–Carvana $8B whole-loan to July 2027, no cancellation; warehouse-exit 55→25% | acted | §3, KB-539 |
| SIG-W-20261020-024 | USDA $8B Harvest Fuel Relief announced, dates unspecified | acted | §6, KB-540 (CRL-10 assessed: no near-term food-CPI effect) |
| SIG-W-20261020-025 | Treasury Defaulted Loans Support Center live 9/30; collector hiring = reported planning | acted | §6, KB-540 |
| WATT packet 10/20 | PJM backstop cost allocation unresolved (FERC 9/29 order suspended to 2/28/2027) | integrated (no score input) | §6, KB-540 |
| PROME packets 10/21 ×2 | BOARD gap list (the six aged + two fresh above) | closed by the ledger rows | both ledgers |

## 2. September PPI — verified at BLS (API v2, 2026-10-21)

| Series | Sep 2026 | Aug 2026 | Sep 2025 | m/m | y/y |
|---|---|---|---|---|---|
| Final demand SA (WPSFD4) | 159.780 | 157.662 | 150.245 | **+1.343%** | — |
| Final demand NSA (WPUFD4) | 159.613 | 157.855 | 150.100 | — | **+6.338%** |
| Ex foods/energy/trade services SA (WPSFD49116) | 144.255 | 143.555 | — | **+0.488%** | — |
| same, NSA (WPUFD49116) | 143.929 | — | 137.021 | — | **+5.042%** |
| Goods SA (WPSFD41) / services SA (WPSFD42) | | | | +2.645% / +0.818% | |
| Gasoline SA (WPS0571) | 361.559 | 300.606 | | **+20.277%** | |

WALTER's figures are confirmed to rounding. **Consumer read:** a producer price, not a household outlay. The gasoline leg is the pump already in September CPI (+9.1%); core-ex-FET +5.0% y/y is the broad pipeline that keeps the Fed locked (V12 stays 5; no un-fire evidence). No food-pipeline claim: a final-demand foods code was pulled but its label could not be verified (BLS catalog returned 403).

## 3. Subprime auto — OTTO's September panel, funding access, Ally contract

- September 60+ DQ: SDART 2022-6/2023-1/2024-1 **11.24/10.10/10.04%**, BLAST 2024-1/2023-1 **16.67/16.15%**, all worse YoY and MoM; matched series **44/44 worse YoY since April** (September = 5 of 9 deals; Exeter is still August until ~10/29). 44 deal-months are not 44 independent credits.
- Exeter DEEP: extensions fell (EART 2022-2 6.44→4.49%) while 60+ DQ rose (13.35→15.22%): part of the worsening may be **less masking** rather than only worse borrowers (cause unknown). Carvana BLAST extensions flat, so its jump is a real level move.
- Funding: CPS warehouse $390M→$518M (10/9); Enova NetCredit $200M revolving to 10/15/2028; Exeter reserve contributions $9.5M/$12.5M (9/15). Ally–Carvana whole-loan arrangement $8B through July 2027, cancellable at discretion, **no cancellation found**; OTTO warehouse-exit forecast 55→25% (subjective).
- **What it does to V2 (score 4):** nothing moves. No WQ-151 letter fired; the deep-tier September grade is ~10/29. It **supports the concentrated-stress half** of the 10/12 scope finding (deep and Carvana tiers keep worsening) and says lenders have **not** cut these borrowers off, so there is no credit-supply shock yet.

## 4. CRL-29 (`CARL-AUTO-OUTFLOW-01`) first grade — PANEL NO VERDICT

Rules: WQ-437 (Will 10/15) = RED's C1–C5. Nine certificates re-fetched from SEC 10/21 (non-identifying desk User-Agent), computed in exact decimal by `crl29_grade.py`, output `crl29_grade_output.json`, hashes `crl29_certificates_sha256_2026-10-21.txt`. Ages from the pre-registered `../2026-10-12_followup/auto-age-match.tsv`.

| Trust (collection months) | Δ61+ stock / EOP pool (pp) | Δ annualized loss (pp) | Δ extension (pp) | Month cells | Trust |
|---|---|---|---|---|---|
| AMCAR 2023-2 (Oct→Nov→Dec 2025) | +0.3645 / +0.3277 | +0.0129 / +2.0368 | −0.2926 / +0.8752 | premise absent ×2 | NO VERDICT |
| AMCAR 2024-1 (Jun→Jul→Aug 2026) | −0.0335 / +0.4773 | −0.7628 / +0.8042 | +0.0797 / −0.3623 | stock↓ loss↓ ext flat = NV · premise absent | NO VERDICT |
| EART 2024-1 (Mar→Apr→May 2026) | +0.4300 / +0.4639 | −0.4519 / +0.3733 | +0.2251 / +0.5989 | premise absent ×2 | NO VERDICT |

**Panel: NO VERDICT** (0 trusts in A, B or D). The registered null: scored neither way, **not** support for CARL's loss read or the Philly Fed extension read. The test asks where a *falling* stock goes; in 5 of 6 tested months the 61+ stock **rose**, so the question did not arise. 31+ reported beside: AMCAR 2024-1 26→27 split (31+ +0.3149 vs 61+ −0.0335), 61+ governs. Printed vs computed: no floor split. Confidence 30% unchanged; registered re-check rides the Q3 HHDC row (11/30). Hash note: today's byte sizes differ from the 10/12 fetch and the stored sha256 do not match; every value present in the 10/12 `auto-extracted.tsv` agrees.

## 5. Q3-2026 issuer prints (8-K Item 2.02, filed 10/20) and the re-grades they force

| Issuer | NCO Q3 | Q2 | Q3-25 | QoQ | YoY | Delinquency |
|---|---|---|---|---|---|---|
| SYF (company) | **4.79%** | 5.43% | 5.16% | −64bp | −37bp | 30+ 4.34% (4.39% YoY); 90+ 2.06% (2.12%) |
| COF domestic card | **3.98%** | 4.71% | 4.63% | −73bp | −65bp | 30+ performing 3.74% (3.89% YoY) |
| COF auto | 1.59% | 1.43% | 1.54% | +16bp | +5bp | 30+ performing 4.64% (4.99% YoY) |
| ALLY retail auto | **1.89%** | 1.57% (CARL 7/21 primary) | 1.88% | +32bp | +1bp | 30+ incl. non-accrual 4.96% (+6bp YoY) |

Survivorship caveat: issuer books shed the worst borrowers; this is not a bottom-60 read. Seasonal caveat (M39): Q3 card NCOs fall seasonally, but SYF and COF card are also down **year on year**, so the improvement is not seasonal only.

| Prediction | Old → new | Why (two-number rule, `FORGE/PREDICTION_DISCIPLINE.md`) |
|---|---|---|
| CRL-31 (≥2 of ALLY/COF/SYF, ≥+25bp QoQ × 2 quarters, by Q1-2027 earnings) | **50% → 1%** | Only Q3 and Q4-2026 count; SYF and COF failed Q3, so at most ALLY can run: ≥2 names unreachable on the letter. Move-from-50 draft 3%, cold ~0–1% → 1%. Not resolved: FAIL vs VOID needs the equity-persistence test at window end. |
| CRL-20 (≥3 of 4 issuer legs) | **35% → 1%** | COF card leg dead (−73bp, one quarter left); needs ALLY Q4 ≥+30bp again AND SYF >5.5% in one print AND RITM (unread). Draft 5%, cold ~0.4×0.05×0.5 ≈ 1% → disagreement >2×, cold governs. |
| CRL-12 (SYF FY2026 NCO >6.0%) | **20% → 1%** | Nine-month 5.21%; FY >6.0% needs Q4 ≈8.4% vs Q4-2025 5.37%. Draft 3%, cold ~0–1% → 1%. |
| CRL-21 (Q3 window) | 25% unchanged | NCO leg stays failed; the live vintage-loss OR-leg is in image charts (ALLY EX-99.2/99.3) and was not graded: UNREVIEWED, docket 10/26. Its position-action clause stays Will's. |

**Book link:** CARL's paper sleeve (no capital) rows PS-0001..0005 rest on CRL-31 and PS-0006/0007 on CRL-20; both antecedents are now ~1%. Disposition under TERRY's paper rules is next-session work, not done tonight. Check F reads these as positioned predictions CUT (the anti-bias direction).

## 6. Context items (no score input)

- **WSJ / QCEW:** price pass-through claimed (article unopened); NY eating/drinking places −3.8% YoY in Q1 while national restaurant **sales** rose +3.41% real in September (KB-535): one state's establishment attrition, not a spending collapse.
- **PJM (WATT):** backstop cost allocation unresolved; no household bill change established; no CPI input.
- **USDA $8B Harvest Fuel Relief:** announced, not disbursed; a partial farm-margin offset with no near-term food-CPI path (CRL-10 stays 1%).
- **Student loans:** Treasury portal live 9/30 (primary); collector hiring and 2027 enforcement are reported plans; involuntary collections still paused (no restart verified). V4 unchanged; STUE owns the custody/vendor question.
- **Gas (AAA 10/21):** regular **$4.264** (−7.0¢ vs 10/15), FL **$4.020** (−20.6¢: the 10/12–10/15 FL spike reversed), diesel $6.317 (identical to 10/15 to the tenth of a cent — possible stale parse, treat as unconfirmed). EIA weekly not pulled (FRED down).

## 7. The 10/12 scope finding, tested against the new items

| Item | Concentrated stress (supported?) | Broad spending collapse (established?) |
|---|---|---|
| OTTO September panel 44/44, Exeter, BLAST | **Supports** (deep/Carvana tiers worsening) | Silent (credit, not spending) |
| CRL-29 null, stock rising | Consistent (61+ stock up in 5 of 6 months) | Silent |
| Q3 issuers: card NCO down YoY, auto flat | Issuer prime books healthy — consistent with **concentration**, against broad credit stress | Silent; survivorship-limited |
| September PPI | Cost pressure (supports squeeze mechanism) | Silent (producer price) |
| WSJ pass-through, NY QCEW | Small-business margin squeeze in one state | Against "collapse": national restaurant sales +3.41% real |
| Funding access (CPS, Enova, Ally) | No credit-supply shock | Silent |

**Result:** concentrated stress remains supported; **broad spending collapse is still NOT established** — none of the eight items measures aggregate household outlays, and the one adjacent spending datum (September restaurants, control group +0.14% nominal) does not show it. The next real test is **September personal income and outlays, Thu 10/29 08:30 ET** (BEA schedule, fetched 10/21). **Score 53/70, v2.6.6 unchanged:** no item fires a vector letter (V2 holds 4 pending EART September; V12 holds 5 pending FOMC 10/28; V1 card stock clock is HHDC-based).
