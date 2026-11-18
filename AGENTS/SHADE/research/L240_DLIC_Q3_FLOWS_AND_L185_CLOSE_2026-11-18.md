# SHADE — D:L240 Delaware Life Q3-2026 statutory read, SHD-02 resolution, D:L185 close, 2026-11-18

**Session:** PROME prome-6e task letter (desktop), registered wake Wed 2026-11-18. Claude Code, Opus 5.5 (claude-opus-5-5). Started 10:42 ET.
**Authority:** research only, $0. No trade, card, gate, band, threshold or charter change. Nothing below moves a score.

## 0. Sources (all fetched 2026-11-18 10:42 to 10:55 ET, issuer or regulator, identity checked before any figure)

| Document | Where | Bytes | sha256 | Identity check |
|---|---|---|---|---|
| Issuer index | `delawarelife.com/content/business-highlights`, HTTP 200 10:42:37 ET | 315,368 | `cf733fc1…251a98` | lists "Q3 2026 Statutory Financial Statement" and investor presentation "Q3 2026" (both new since 11/16) |
| **DLIC Q3-2026 quarterly statement** | issuer CDN (link from index, not constructed), Last-Modified **Tue 2026-11-17 14:02:56 UTC** | 3,690,022 | `76f86bcc3eb2e999c4ec173ca1a634ce36aa05e53b16c37e7390d2096d401e35` | barcode `79065202620100103`, "AS OF SEPTEMBER 30, 2026", cocode 79065 ✅ |
| DLIC Investor Presentation Q3 2026 YTD | issuer CDN, Last-Modified 2026-11-17 14:04:10 UTC | 1,278,865 | `d1f998ecd4bd2fd6b02e2065ad00bdd36c70a49e13690e5da5e7797482ec9edb` | issuer-narrated, statutory basis, unaudited |
| DLIC Q2-2026 statement (comparator) | issuer CDN | 3,550,199 | `cc658b8d46f8c3ae9c43864c001adb4ff65ef09495a48069c455664e85a1601b` | barcode `…0102` ✅ |
| DLIC Q1-2026 statement (comparator) | issuer CDN | 3,429,143 | `ac9d7e0264855bb69dcc9f213686003ce1b50145e76999fc89734aaee4afca3c` | barcode `…0101`, AS OF MARCH 31, 2026 ✅ |
| DLIC Q3-2025 statement (comparator) | issuer CDN | 3,202,122 | `bd08091e92693a6eac664bfd1eba29b4a4e17795766a4254c8a4427661009f59` | barcode `79065202520100103` ✅ |
| Catalina Holdings (Bermuda) FY2025 group statement | `cdn.bma.bm/documents/2026-11-04-14-02-39-Catalina-Holdings-Bermuda-Ltd.-2025-Financial-Statement-Group.pdf` | 651,780 | `b440798645863dd5e85e21f6bedc74227b0361ea6a3efb24bb49acac9c8b8f5b` | US GAAP, audit report dated 2026-04-17 |
| ACRA 1A / 2A FY2025 (re-fetched) | BMA class C, URLs in the 11/16 record §5 | 502,550 / 471,743 | match the 11/16 hashes exactly | — |

**Posting lag, third measurement:** due to NAIC Sun 11/15, on the issuer CDN Tue 11/17 = **+2 days** (Q3-25 +2, Q2-26 +3). The 11/16 re-date to 11/18 held.

## 1. D:L240 — the first post-pause flow read

Quarter figures are year-to-date columns differenced (Q2 = 1H − Q1, Q3 = 9M − 1H). Prior-year columns are each statement's own "Prior Year To Date" column. $M.

| Line (statement) | Q1-25 | Q2-25 | Q3-25 | Q1-26 | Q2-26 | **Q3-26** | Q3 YoY | Q3 vs Q2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Individual annuities (Exh 1 L3) | 1,434.9 | 2,753.5 | 3,062.2 | 2,401.2 | 2,243.9 | **1,521.9** | **−50.3%** | **−32.2%** |
| Direct premiums subtotal (Exh 1 L8) | 1,471.8 | 2,891.6 | 3,208.1 | 2,520.4 | 2,445.1 | **1,557.7** | −51.4% | −36.3% |
| Deposit-type contracts (Exh 1 L9) | 235.0 | 1,305.0 | 714.3 | 1,760.8 | 0.0 | **0.0** ($2,522) | −100% | flat at zero |
| **Total direct + deposit-type** | 1,706.8 | 4,196.6 | 3,922.4 | 4,281.3 | 2,445.1 | **1,557.7** | **−60.3%** | −36.3% |
| **Surrender benefits and withdrawals (SoO L15)** | 537.7 | 887.0 | 676.8 | 988.4 | 1,072.4 | **1,137.9** | **+68.1%** | **+6.1%** |
| Surrenders ÷ total inflows | 31.5% | 21.1% | 17.3% | 23.1% | 43.9% | **73.0%** | | |
| Premiums collected net of reinsurance (CF L1) | 1,451.3 | 2,869.7 | 3,305.5 | 2,584.6 | 2,637.8 | 1,770.8 | −46.4% | −32.9% |
| Benefit and loss payments (CF L5) | 1,046.6 | 1,354.8 | 1,293.7 | 1,414.7 | 1,692.1 | 1,711.8 | +32.3% | +1.2% |
| Net deposits, deposit-type (CF L16.4) | 86.1 | 1,136.6 | 696.0 | 1,635.2 | −158.5 | −147.7 | | |
| Net cash from operations (CF L11) | 910.8 | 2,056.7 | 2,407.5 | 1,607.8 | 1,839.5 | **748.3** | −68.9% | −59.3% |

Nine months: total inflows **$8,284.1M vs $9,825.8M (−15.7%)**; surrenders **$3,198.7M vs $2,101.4M (+52.2%)**; ratio **38.6% vs 21.4%**. Tie-out to the 11/16-era baseline: 1H figures in the Q3 arithmetic are the same verbatim figures PROME verified at the Q2 PDF ($6,726,317,026 inflows; $2,060,811,753 surrenders).

**What the quarter split shows (the finding):**
1. ★ **New business fell; policyholders did not run.** Q3 inflows were the lowest of the six quarters, −60% on Q3-25 and −36% on Q2-26. Surrenders rose only +6.1% on Q2-26 and continue a climb that began in **Q1-26, before the late-June reclassification disclosure** (Q1-26 already +83.8% on Q1-25). No step change in withdrawals appears in the quarter that contains the pause.
2. **The sales decline started before the pause.** Q2-26 individual annuities were already −18.5% on Q2-25 ($2,243.9M vs $2,753.5M). Q2 contains the VA sales stop (May 2026, deck p13) and the June disclosure; Q3 contains the July rating actions (S&P 7/14, Fitch watch 7/22, AM Best 7/31), the 8/28 bank pause and the 9/16 class action. **The statement cannot separate these; it is quarterly and has no channel or monthly split.**
3. **Institutional funding stopped after Q1.** All $1,760.85M of 2026 deposit-type receipts (funding agreements) landed in Q1; Q2 and Q3 are zero, and net deposit-type cash was negative both quarters. The deck agrees ("issued a total of $1.8 bn of funding agreements through Q3 2026 YTD"). Q2's zero predates the disclosure for April and May, so this is not evidence of a closed market, only of no issuance.
4. **Cash still positive, liquidity reported ample.** Q3 net cash from operations $748.3M; deck: "approximately $5 bn of total liquidity" (issuer-narrated, basis not given), 94% of fixed and indexed reserves carry surrender-charge protection (deck p14).

**Against the pre-registered refutation of marker (0):** not tested; no distributor resumption and no probe closure found. Marker (0) stays MET.

⚠️ **PARTIALLY BLIND stands:** Q3 holds at most one post-pause month, and the pause cannot be isolated from four other shocks inside the same two quarters. First clean read stays the FY2026 annual (~2027-03-01), and even that is quarterly-free only if the issuer's promised "quarterly financial and investment public disclosures" (deck p24) add a channel split.

## 2. Affiliate book, the exchange, and SHD-02

**Note 10 (SSAP 25 "predominantly contingent" private credit), carrying value:**

| | 12/31/25 restated | 6/30/26 | **9/30/26** |
|---|---:|---:|---:|
| Short-term | 3,242.9 | — | 3,393.8 |
| Bonds | 12,619.3 | 13,091 | 13,088.7 |
| Other invested assets | 509.7 | — | 337.5 |
| **Total** | **16,371.9** | **16,822.2** | **16,820.0** |
| GA net admitted (Page 2 L26 col 3) | 45,903.2 | 51,249.4 | **51,534.0** |
| Share | 35.67% | 32.82% | **32.64%** |

Flat in dollars Q3 (−$2.2M): consistent with no exchange settling before quarter end. Affiliate-contingent = **4.17× capital and surplus** ($4,032.3M at 9/30; concentration measure, not leverage). Trust notes $326.2M → $100.1M YTD; SAFA investments $308.3M unchanged.

**Issuer's broader "affiliated assets" (deck p22, a different basis — never merge with Note 10):** 12/31/25 restated $18,251M (42% of $43,883M) → **9/30/26 $20,076M (41% of $49,133M)** → 11/16 pro forma $17,405M (35%). Up **$1,825M** YTD, of which **$766M is a Schedule Y change:** Guggenheim added to DLIC's Schedule Y at 9/30 after TWG's 2025 ownership change in Guggenheim Capital, so Guggenheim-managed structured securities became "affiliated" (issuer: collateral unaffiliated). The other ~$1,059M is unexplained in the deck. Deck target: affiliated "approximately 20-25%", full wind-down to zero by 2027-06-30 (via the APA).

**Exchange execution (statement Note 22, subsequent events through 11/16, PRIMARY):** Delaware DOI approved an initial PSA exchange of **~$3.8B on 2026-10-21**; **~$2.7B settled through 2026-11-16**; remainder expected in Q4; **~$1.2B more filed for approval 2026-11-16**. APA (TWG purchases plus Walter contingent backstop) **"approvals have not yet been received"** (Note 10). This confirms WALTER card 016's WSJ/Bloomberg titles at primary: the issuer's 9/11 target "before the Q3 filing" was not met in full.

★ **What DLIC receives:** deck p22, "The Delaware Life assets being exchanged are rated private corporate loans, and the assets received in return from TWG are debt, limited partnership, and equity interests." The deck's reassurance ("expects to maintain the average rating") is computed on rated assets only (p17 footnote: "Only assets with NRSRO ratings are displayed"). **INFERRED, unmeasured:** LP and equity interests carry higher statutory capital charges and are less liquid than rated loans, so the exchange plausibly trades related-party concentration for higher capital charges and a higher Key Ratio #2 floor. S&P's July rationale named "the possibility of higher credit risk charges following the restructuring". Split of debt vs LP vs equity received: **not disclosed**. Test: FY2026 annual Schedule BA and common stock lines, and the RBC ratio (deck still says only "above 400%" as of 12/31/25).

**SHD-02 RESOLVED ✅ HIT (2026-11-18).** Letter: "DLIC's Q3 2026 statutory statement … states in Note 10 or subsequent events a completed exchange with TWG of at least $1.0B gross." Note 22: "approximately $2.7 billion of the approved initial asset exchanges with TWGG had settled." Registered at 35%; resolved YES. `thesis/PREDICTIONS.tsv` updated.

## 3. Two new statutory facts

| Fact | Source | Read |
|---|---|---|
| **DLIC paid an affiliate's bank loan.** 1001 Commercial Finance (1001CF) borrowed $300.0M under a joint Société Générale facility; **DLIC repaid Soc Gen $303,526,250 on 2026-09-30 on 1001CF's behalf** and holds a **$303,593,700 receivable from 1001CF** (7.5% of C&S). 1001CF was removed as co-borrower 2026-10-06; DLIC keeps a $350M facility. | Note 10 and Note 14 | The insurer's general account was the group's liquidity backstop at quarter end. The note does not say 1001CF defaulted. ⚠️ Whether 1001CF repays, and why the repayment fell on the quarter-end date, is unknown. Fits `combo:walter-liquidity`. |
| **Second class action.** Rosner (S.D. Fla., 2026-09-16) and **Kalinsky (S.D. Fla., 2026-10-07, also names CSLAC)**: disclosure of affiliate investments, seeking rescission of annuity contracts, restitution and damages. Loss "reasonably possible", not estimable, no liability recorded. | Note 14 | Civil, not an enforcement rung. Rescission claims are a channel to surrenders that the quarter does not yet show. |

Other 9/30 lines: C&S $4,032,337,934 (6/30 $4,028,108,426); TAC $4.6B (deck); 9M net income $203.3M; OTTI 9M $37M (deck). **Key Ratio #2 measurable components (mortgages $3,446.9M + BA net admitted $2,370.2M) = 11.29% of GA** (6/30 10.05%); under the adopted letter the grade is **UNAVAILABLE** on a quarterly (ABS leg not in the quarterly).

## 4. Delaware Life escalation ladder after this read

| Rung | Before | Now |
|---|---|---|
| (0) counterparty/distribution | MET 8/28 | MET; no resumption found |
| (1) charges / Wells | not met | not met; second civil class action (not a rung) |
| (2) further rating action | S&P A- NEG, Fitch RWN, AM Best NEG | unchanged per issuer deck (dates 7/14, 7/22, 7/31); SHD-03 open |
| (3) Delaware DOI action | not met | DOI *approved* exchanges 10/21; no adverse action |
| (4) remediation size/timetable | PARTIAL | **EXECUTING: $3.8B approved, $2.7B settled, $1.2B filed, wind-down to zero by 6/30/27 per issuer; APA unapproved** |
| (5) Clear Spring restatement | issuer table read | unchanged |
| (6) probe widens to Guggenheim AM | not met | **not met**; adjacent fact: Guggenheim added to Schedule Y at 9/30 ($766M reclassified affiliated), an ownership finding, not a probe |

## 5. D:L185 closed: last BMA legs read

**Catalina Holdings (Bermuda) FY2025 (US GAAP, $M):** total assets **9,604.2** (2024 8,140.8); funds withheld assets 5,810.1 (+44%); interest-sensitive contract liabilities 5,902.0; **shareholders' equity 389.4 (2024 613.6, −36.5%)**; **net loss −394.4** (2024 −281.2); total revenues negative both years. ★ **Catalina is majority-owned by Apollo-affiliated funds since October 2018 (Note 21a)** and holds $249.0M of Apollo-affiliated funds (11.1% of investments). Its Athene links (Note 21b): CRAL modco of FIA/MYGA from **AARe**; CatGen's **FABN total-return swap with AARe** (CatGen takes the excess-spread receive leg; derivative fair value $170.6M, 2024 $239.9M; $34.6M due to CatGen). Capital: BMA requirements met; **CRAL holds a BMA permitted practice removing the MMS floor from its ECR**; no dividends or distributions without BMA approval. Audit: going-concern text is standard auditor wording, not a finding.
⇒ **The FABN excess-spread risk Athene moves to Catalina stays inside the Apollo family**, at a counterparty with a 4.1% equity-to-assets ratio that lost more than its year-end equity's worth in two years. INFERRED consequence: treat Catalina-ceded FABN risk as affiliated, not third-party. No score moves (vector #3 basis note).

**ACRA related-party notes (1A Note 12, 2A Note 11):** Apollo management fees $54M (1A) and **$137.7M (2A, 2024 $86.8M)**, plus fees paid indirectly through cedants and fund-level carry, not included. **Each vehicle has a $2.6B unsecured revolving note payable to ALRe, undrawn at 12/31/25 and 12/31/24** (1A maturity: earlier of 2026-06-26 or demand). Related-party securities in 1A: MidCap ABS/CLO $40M, Wheels $67M. Unfunded commitments $408M (1A) / $858M (2A). Subsequent events: 1A paid a $100M dividend (Jan 2026); 2A received a **$200M capital contribution (Mar 2026)**. ⇒ Athene's own Bermuda cedant is the standing liquidity line to the third-party-capital sidecars ($5.2B combined, undrawn). No outstanding intercompany loan found.

**D:L185 legs:** L3 baseline pin DONE 11/6 · pledged-asset extraction DONE 11/6 · X1 reconcile CLOSED WQ-644 A · BMA deeper walk DONE (ACRA 11/16, Catalina + related-party notes today). **Nothing on L185 is still owed.** The Level 3 split behind the AARe Note 14 gap still runs through the cedants' statements (open question, STATUS §10, not a L185 leg).

## 6. WALTER card 20261116-007 (ACTION): $85.2B life-insurer AI debt

**Primary?** Not obtained. Attribution is **Moody's** (report late October 2026, data at 6/30/26), via the NYT and trade press (Reinsurance News; aiweekly; siliconreport), not NAIC. Secondary details: 2.1% of life insurers' debt (1.7% at YE2025); hyperscaler debt ~$32.2B, digital infrastructure ~$39.5B (+34%); below-IG share 4.7% → 6.1%; projection +$50B to $100B, "up to $185B" by end-2027. Moody's is subscription; its MCP connector is not authenticated here. Barclays' 15% share: not found at a primary.
**Does it change my read?** No score. Athene's measured AI book (9/30, primary 10-Q and deck): $12.9B funded per the deck, $16.0B with SVF II Finco, $6.2B unfunded commitments. ⛔ Never divide Athene's figure by $85.2B: different dates (9/30 vs 6/30) and undefined perimeters. ⚠️ **Conflict to check, not resolved:** secondary coverage says Moody's names **Athene $2.4B of xAI chip-financing debt**; my 11/6 read carried **$2.4B as Oracle-linked**. Same amount, different named obligor; AAIA Q3 statutory (owed, §10 3f) can settle it. Surveillance ≠ action (MEMORY): attention is rising, no rating action on a PE insurer follows from it.

## 7. Trade assessment (for PROME to route to TERRY)

| Field | SHADE's read |
|---|---|
| What the evidence implies | Delaware Life's franchise is shrinking (Q3 new business −60% YoY), but there is no policyholder run through 9/30 (surrenders +6% QoQ, ops cash positive, 94% surrender-charge protected). The cleanup is executing, and it swaps affiliated rated loans for parent-supplied LP and equity interests, which plausibly raises capital charges and illiquidity (INFERRED). The parent group used the insurer's cash for an affiliate's $303.6M bank repayment. |
| Horizon | Q4 settlement of the $3.8B tranche; FY2026 annual statement ~2027-03-01 (Schedule BA, RBC, surrenders); APA wind-down by 2027-06-30; SHD-03 (downgrade) by 2026-12-31. |
| What would invalidate it | Q4/annual individual-annuity receipts back near the Q2-26 run-rate (~$2.2B a quarter) with surrenders flat; a named bank distributor resuming; Fitch resolving its watch to stable; RBC reported unchanged after the exchange. Against "no run": a step jump in surrenders or rescissions in Q4. |
| What remains unknown | Channel split of the sales fall (bank vs IMO vs VA stop); composition and marks of the assets TWG delivers; whether 1001CF repays $303.6M; the ~$1,059M non-Guggenheim rise in "affiliated assets"; RBC after the exchange. |
| Investment implication | **None for a listed instrument, in my lane.** DLIC and Group 1001 are private; DLIC's FABNs are 144A. Read-across to listed PE insurers (APO/Athene, KKR/Global Atlantic, BN/AEL, F&G) is not supported: the mechanism (undisclosed related-party classification under a federal probe) is name-specific, and the Catalina and ACRA reads show Apollo-family linkage, not loss. TERRY decides whether any card exists. |

## 8. Not done / unavailable

- `T-SHADE-01` fresh assessment: not run (not assigned today). Last grade NOT MET (11/10 close).
- AAIA Q3 statutory (posted 11/13): not read (§10 3f).
- Moody's primary report: subscription, not accessed.
- Deck charts (sales by product and channel, surrender-charge expiry profile) are images; values not extracted.
