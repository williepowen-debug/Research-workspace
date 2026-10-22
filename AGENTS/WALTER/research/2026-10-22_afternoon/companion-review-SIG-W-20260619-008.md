# Independent companion review: SIG-W-20260619-008

- Date: 2026-10-22
- Reviewer: independent Sonnet reader (read-only except this file)
- SOURCE: `BOARD/SIG-W-20260619-008-south-florida-distress-deep-research-bank-transmission-assessment.md` (174 lines, 39,509 B), sha256 `17e64d21e944e628139719841335f18e059bb3d1c652a7d93b3998d90274ddd9`
- COMPANION: `AGENTS/WALTER/reading/SIG-W-20260619-008.md` (105 lines, 21,889 B), sha256 `5d0b19d81e41aaa5e99672cdc95c4e747e91732a394b09b5713dcf5e7ed30d2d`
- Coverage: SOURCE read whole (lines 1-70, 70-145, 143-174); COMPANION read whole. Source lines 143-174 vs companion lines 74-105 compared with `diff`: IDENTICAL (verbatim tail intact).
- Prior review (2026-09-15) bound a draft of 21,611 B (sha e4b4f974...), not these 21,889 B committed bytes (commit 70a2bc593 holds the current bytes). The prior review's conclusion was not relied on; its census was used only as a criteria checklist, and every item was re-checked here against the source.

## Findings

| Item | Source loc | Companion loc | Verdict | Note |
|---|---|---|---|---|
| Dispatch metadata (23:05Z Jun 19, PRIORITY, conf 0.85, BANK_COLLATERAL / CONSUMER_STAGFLATION, FL_REAL_ESTATE, to CORAL, INFO x5) | 2-14 | 9 | PASS | All values match. |
| Frontmatter "VERIFIED-PRIMARY / none required" overstated | 16-17, 105 | 15 | PASS | Companion explicitly refuses blanket primary-verification and points to the closing "unresolved citation tokens" paragraph. |
| Flag closure of SIG-007 Phase 2.8 is lifecycle only | 18, 24 | 9 | PASS | Companion adds "not proof CORAL integrated the actions"; consistent with source role statement (WALTER routes, does not re-analyze). |
| 70/30 normalization/crash, Q2-Q3, Iran tail dominant | 27, 68, 78 | 11, 26 | PASS | Labeled a dated judgment, not a validated probability. Verbatim bottom line also retained. |
| Five-bank "9-11 bps NCO" all-clear vs bank paragraphs | 68, 76, 119, 123, 125 | 13, 52-56 | PASS | Companion correctly surfaces the source's internal inconsistency: SSB 9bp, SBCF 11bp, BKU ~37bp TTM, AMTB 0.45% avg loans, VLY none. Source calls BKU's rate "elevated"; companion drops the word "elevated" (note only, MINOR below). |
| CORAL ACTION: split insurance mark; commercial +10.4% / +18.8% is blended commercial, not condo-only | 34, 107, 103 | 21, 46 | PASS | Colour codes (green vs orange/red) and "resolves SIG-007 TENSION" wording omitted; non-load-bearing. |
| CORAL: add AMTB; mixed migration; top-six artifact; synchronized diagnostic; Ch7 ~230/100k; Q2 re-test | 35-37 | 21, 56 | PASS | All retained. "Durable mechanism, delayed transmission" and "open-question #1" not quoted; substance retained. |
| REGINALD INFO: BKU ACL 0.87% not 1.21% (AMTB contamination); deposits stable; 6/8 cohort read | 40 | 22 | PASS | Retained. "Multi-decade lows" label sits only in the verbatim tail; acceptable because the tail is whole. |
| CARL INFO: consumer-led; energy >60% of May CPI gain, core 0.2/2.9, spillover forward risk; Snaith no recession | 43, 80, 139-141 | 23, 66, 68 | PASS | Economist quotes (Rupkey, "not bleeding into core") omitted; non-load-bearing. |
| SHADE INFO: wholesale easing vs commercial; liability/umbrella shift; condo-master not disclosed | 46 | 24, 42, 46, 58 | PASS | Retained. |
| MARCO INFO: household cost stack/out-migration; Spirit not FL demand, SDNY, ~$100M fuel | 49, 131 | 25, 62 | PASS | Retained. |
| RED INFO: incentives, realized-data preference, aggregate-only vacancy, 70/30 | 52, 99, 125, 133 | 26, 38, 58, 64 | MINOR | "Miami office vacancy lowest of top-25" dropped; the 12.5% / 15.7% / 17.6% figures survive. |
| Bankruptcy figures: US 591,850 +11.9%; business 25,960 +11.4%; nonbusiness 565,890; MD 27,925 vs 21,927 (#2); SD 16,326 vs 14,387 (#6) | 88-90 | 36 | PASS | Match. |
| FL 44,496 +22.2% from 36,407: "nonbusiness" (Key Findings) vs "total" (Details) | 72, 97 | 36 | PASS | Inconsistency correctly flagged as unresolved. |
| Per-capita FL 190, SD 222, MD 199, US 168-173, AL ~520; SmartAsset/BankruptcyWatch; Dec-2025 proxy; denominators approximate | 64, 95-99, 90 | 38 | PASS | Retained with caveats. Alabama "~520" (TL;DR) vs "exceeding 500" (Details) both consistent. |
| Chapter-level counts (US Ch7 369,702; district Ch7/11/13 pairs) and Maryland 203, "third in growth" | 88, 92-93, 97 | omitted | MINOR | Non-load-bearing for conclusions. Mild gap: the Ch7 ~230/100k tripwire has no Ch7 baseline in the companion (companion does flag the total-vs-Ch7 basis mismatch at line 28). |
| "Chapter 11 is not exclusively consumer" | 72 ("all three consumer chapters"), 88 | 36 | MINOR | Reader caution added by the companion; consistent with the source's own Ch7-fastest framing, not a new fact. |
| Insurance: GC -15/-20, Gallagher 20-25/22.8, Aon/Howden to 25; 2025 ARDC -0.46%; FHCF -9.51%; CR 77 vs 92; surplus +45%; $4.3B cat bonds | 103 | 42 | PASS | Match; incentive/corroboration logic and benign-season condition retained. |
| Citizens personal: -2.6% filed, ~-8.7/-8.8% approved, Jun 1 2026-May 31 2027; 463,096 / 59.2% / -11.5%; Insurify $8,458 vs $2,948 | 105 | 44 | PASS | Match. Companion's note that 463,096 is the filing population, not the June 12 remaining count, is arithmetically sound (463,096 > 293,404), not a new claim. Omitted: first cut since ~2015, county detail, ~43% indicated drop; non-load-bearing. |
| Citizens residual 1.41M -> 336,000 -> 293,404 | 109 | 44 | PASS | Match; "supply relief does not mean resolved" matches source incentive flag. |
| Commercial +10.4/+18.8; multi-peril +9.6/+21.3; wind +10.9/+17.2; property-only 10-20%; SIRS/HB1021-1203; non-renewal | 107 | 46 | PASS | Match; blended-line caveat retained. |
| SSB metrics (NCO 9bp, NPA 0.66%, $10.8M, 1.32%, $2.5B/3.6%, 88%/99%, LTV 56%/98%, loans +7%, dep +5%, watch SBA/consumer) | 115 | 52 | PASS | Match. CEO rate-shock explanation omitted; management optimism is labeled as such. |
| SBCF metrics (NPL $95M/0.75% vs $76.3M, two credits, 2.82% flat, ACL 1.39%, NCO 11bp, $0.8M, CRE 60%, 1.21% C&LD, +7%, +29%, 1.54%) | 117 | 53 | PASS | Match; "collateral/management assurance is not a realized-loss test" correctly framed. |
| BKU metrics (-$146M/-12%, -$98M/-26%, NPA 0.79 vs 1.08, 75.5/109, 175.4/238, ACL 208.8M/0.87 vs 219.8M/0.91, 75.9 vs ~59, NCO $36.1M, prov $25M incl $8M overlay, CRE 6.9B/47%/20%/1.78/64.2%, +277M/+1.4B) | 119 | 54 | PASS | Match. CET1 12.2%, NIM, EPS omitted; non-load-bearing. |
| VLY metrics (50.8B, 52.9B, ACL 1.18 vs 1.19, nonaccrual 0.85%, CRE ~329%, CET1 10.91%) | 121 | 55 | MINOR | Match. "CRE concentration ratio edged down" and "not showing a Florida-driven break" dropped. |
| AMTB metrics (21/23 FL, classified -9.7% to $320.3M from $354.8M; NPA/NPL/SM up; $7.8M from $3.5M; gross CO $9.1M; NCO 0.45%; ACL 1.21 vs 1.20; dep +2%; CET1 11.84%) | 123, 102 | 56 | PASS | Match; "mixed migration, not blanket improvement" faithful. |
| Condo-master not isolated; absence of disclosed shock is not absence of channel; managements structurally optimistic | 125, 95 | 58 | PASS | Retained. |
| Business: SubV +36%, Ch11 -~7% (684 vs 739), Spirit May 2 SDNY ~$100M fuel, Darden 28 | 129-131 | 62 | PASS | Match. |
| Vacancy: Miami office 12.5 vs 15.7, US 17.6, Tampa 15.1; retail 2.8/3.0/3.4 vs 4.2; no segment-level series | 133 | 64 | PASS | Match; aggregate-only caveat retained. |
| Energy/CPI: Hormuz closed since Feb 28; Brent 117/107/77-92; EIA 105 and 79 conditional; May CPI 0.5/4.2, energy 3.9/23.5 (>60%), core 0.2/2.9, core goods -0.1, transport -0.6 | 137-139 | 66 | PASS | Match; marked as June context, not current. "Highest since April 2023" dropped; non-load-bearing. |
| Snaith/UCF: GDP 2.1->1.8->1.7, no recession, housing flattened, no audited scorecard, moderate credibility | 141 | 68 | PASS | Match. |
| Recommendations 1-5, Caveats (6), Verification notes (3 discrepancies), Remaining open item | 143-174 | 74-105 | PASS | Byte-identical to source (diff clean). |
| Source line references (section headings) | n/a | 7, 32-70 | PASS | Ranges map correctly to source content (e.g. 64/72/86-99 bankruptcy; 101-109 insurance; 111-125 banks; 127-142 business/macro). |
| Companion adds claims absent from source | n/a | 13, 28, 36 | MINOR | Added items are reader cautions derived from source text (NCO inconsistency, Ch7-vs-total basis, Ch11 population, "sustained" unspecified). None is a new figure or conclusion. All are flagged as companion observations. |
| "Omitted/summarized" statements | n/a | 5 (full evidence on demand) | PASS | Companion makes no specific "omitted" list; omissions checked above are non-load-bearing. |

## Other observations

- Staleness: header says recheck by Sep 30, 2026. That date has passed (today 2026-10-22); this review is the recheck. The prior review hashes (companion e4b4f974...) do not match the current committed companion, so the 09-15 approval did not bind these bytes. This review binds the hashes above.
- No FAIL items. Minor omissions are limited to color codes, ranking trivia, secondary metrics (CET1/NIM/EPS), and economist quotes.

VERDICT: PASS — companion may substitute for the source

---

WALTER approval (2026-10-22, on the independent Sonnet reader's PASS above; companion bytes unchanged since 70a2bc593, sha256 5d0b19d81e41…; next re-review 2026-11-05):

Verdict: APPROVED
