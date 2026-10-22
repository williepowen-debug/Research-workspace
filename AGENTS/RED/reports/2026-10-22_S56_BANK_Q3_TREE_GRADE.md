# S56 — Bank Q3 tree graded (DOCKET L35): CHG-RED-027 = DETERIORATION · Acute +1 (pre-stated) · CHG-054 OZK leg → MODERATE

**Written:** 2026-10-22 11:30–11:5x ET (clock from `date`). PROME-spawned Tier-1 WQ-184 due-row wake (WQ-481 A). Tree applied as written: `research/2026-10-19_BANK_Q3_DECISION_TREE.md` (pre-data, 10/14). The tree exists to remove discretion on the grading day; every verdict below is the letter, with the composition recorded beside it.

## Sources (read by RED, this session)

| Source | Locator | Basis / limit |
|---|---|---|
| EGBN 8-K EX-99.1 (release, 12 pp) | sec.gov acc 0001050441-26-000110, `finalegbnerq3-2026xearni.htm`, fetched 11:27 ET, sha256 `4eaea72423a1b38fd4651008b8ec50de516526fbbdabe87a530f47d84f7a8c7a` | PRIMARY. Text layer read directly for every decisive figure |
| EGBN deck (31 slides, images) | same accession, `final-3q2026egbnearnings.htm` | Not re-read by RED; loan-level facts cited from REGINALD's extract (`AGENTS/REGINALD/domain/sources/2026-10-22_catchup/egbn_q3_extract.md`, Opus reader, slides 19/20 re-read by REGINALD), labelled as such |
| EGBN Q3 call, 10/22 10:00 ET | Investing.com "Earnings call transcript: Eagle Bancorp tops Q3 2026 profit estimates", https://in.investing.com/news/stock-market-news/earnings-call-transcript-eagle-bancorp-tops-q3-2026-profit-estimates-93CH-5649012 (page stamp "Published 22-10-2026"), read via WebFetch 11:29 ET | SECONDARY, AI-generated and editor-reviewed per the page. **sha256 UNAVAILABLE**: the site refused a direct `curl` (3-byte body), so no byte hash of what was read exists. Short quotes only. Quartr: subscription_required on this account (PROME) |
| OZK owner grades | `AGENTS/OZK/research/threads/2026-10-21_Q3_PRINT_STAGE1_GRADE.md`, `…/2026-10-22_Q3_CALL_STAGE2_READ.md`, `AGENTS/OZK/STATUS.md` (d32d5c6d0) | Owner's letter; RED does not re-grade it |
| WAL owner grade | `AGENTS/WAL/STATUS.md` (e06a65f98 / 42fe5c022), `research/2026-10-21_Q3_STAGE2_CALL_GRADE.md` | Owner's letter |
| Prices | `FORGE/tools/market-data/fetch.py price … --history`, 11:28 ET | vendor closes; 10/22 is intraday |

## (I) CHG-RED-027 — EGBN branches (E1–E6)

| Rule | Q3 value (release, $K) | Q2 comparator (Q3 release's own column) | Leg result |
|---|---|---|---|
| E1 NCO annualized to average loans | **0.25%** ("Net charge-offs (recoveries) (annualized) to average total loans 0.25 % 2.78 %") | 2.78% | ≤ 1.75 → CLEARING's NCO leg MET; DETERIORATION's NCO leg (≥ 2.25) NOT MET |
| E2 NPAs strictly below Q2 | **$166,021K** | $113,090K | NPAs ROSE +$52.9M → CLEARING's NPA leg NOT MET |
| E3 inflows > reductions (EGBN's own rollforward) | "non-performing loan inflows totaled $73.7 million … Reductions of $18.8 million" | Q2: inflows $36.0M < reductions $53.7M | **73.7 > 18.8 → DETERIORATION's OR-leg FIRES.** Disclosed, so E3 is available |
| E4 overlap | NPAs did not fall, so no overlap | — | not invoked |
| E5 exhaustive | — | — | the cell is DETERIORATION, not NO VERDICT |
| E6 read order | release ✔ · call ✔ (secondary, above) · then grade | — | satisfied |

**VERDICT (letter): DETERIORATION.** Pre-stated action: the structural leg re-broadens on evidence; **CHG-027 stays ACTIVE, re-review at the EGBN Q4 print (~late Jan 2027).** The capitulation review does NOT run; the RETIRE default is not reached.

**The call** adds nothing that changes a leg: CFO Newell — "The increase was primarily attributable to the $56 million Maryland affordable multifamily relationship"; asked whether a specific reserve exists: "Yes, Justin, there is" (amount not given); a subordinate lienholder existed and the borrower chose not to support a restructuring (per the transcript; paraphrase). CEO Curley: "The affordable housing book is really contained materially in this loan." On Q4: "We have several multifamily maturities in the fourth quarter where we've been actively working with borrowers." Provision/charge-offs: "model something that's lower next year for the full year"; the outlook "doesn't include assumptions for future provision expense, charge-offs".

**Composition — recorded beside the verdict, scores nothing (the counter-case RED owes):**
- **One relationship carries the verdict.** 76.0% × $73.7M = $56.0M = the #1 nonaccrual, Prince George's (MD) affordable multifamily (REGINALD deck extract D-s19/s20; the call confirms "$56 million Maryland affordable multifamily"). Ex-that loan: inflows ≈ $17.7M < reductions $18.8M, and NPAs ≈ $110.0M < $113.1M — **the ex-loan cell is CLEARING** (reader arithmetic).
- **It is migration of a known problem, not fresh formation.** The loan was already substandard at Q2 (DSCR 0.63 Q2 → 0.74 [8/31]); it moved substandard-accruing → nonaccrual and its maturity went to 12/21/2026 with no principal received. E4's stated purpose was "fresh problem formation"; the 8/7 letter, however, is "NPL inflows > reductions" with no ex-single-name clause, and adding one now would be a post-data edit. **Letter governs; disagreement recorded.**
- **Everything else in the print moved toward clearing:** criticized + classified (incl. HFS) $759.6M → $648.4M; criticized inflows $216.1M → $55.7M (−74%); 30–89 DPD $44.1M → $0.357M; OREO $1.966M → $0; CET1 14.58% → 14.99%.
- **And against that (bear):** ACL / NPLs 109.01% → **72.75%** while the office overlay was released (performing office coverage 7.22% → 4.86%); the $56.0M loan's specific reserve is undisclosed; **$265.7M of income-producing multifamily matures in Q4-2026** (deck s16 per REGINALD; book $574.8M, 43.1% criticized, 11% nonaccrual), including a $20.5M DC apartment loan at LTV 152% / DSCR 0.24 due 12/30/2026. Management gives no credit guidance for Q4. The binding test is that December wall — DOCKET L791 (12/21) carries the named loan.

## (II) Acute ±1 — pre-stated, DISCRETIONARY label

| Leg | Owner evidence | Result |
|---|---|---|
| EGBN verdict | (I) | DETERIORATION |
| OZK adverse = any of three | OZK-09: **OPEN/STUCK** (no sourced amount; owner) · provision > PPNR: **NO** (PPNR $261.4M = 5.5× provision; owner) · **W9 Boston 10 Prospect: sale FAILED, OZK took title after a $37.3M charge-off, OREO $132.0M** (owner Stage-1: "TOWARD-STRESS branch fired"; Q2 reserve on the loan was $0, so the charge-off is new) | **OZK adverse MET on W9** |
| Same-day guard | no mechanical bull fire today (FT-01/FT-12 clear, FT-02 exit needs <300, HY 327 [10/21]; FT-10 exit needs <140) | clear |

**→ Acute +1, from Managed: Acute 19 → 20 · Managed 24 → 23 · net-bear 68 → 69 · HOLD 72 unchanged** (the tree states no CONF move). Label: DISCRETIONARY, pre-stated 10/14 (the S52 symmetric counterpart of the S52c −1).

**Reading note on the tree's third row** ("anything else, or OZK-09 still STUCK → none"): RED reads STUCK as "this leg is not evidence", not as a veto over the other two adverse legs. Basis: OZK-09 was already STUCK when the row was written (10/12 8-K), and W9 was written in as an independent "any of" leg the same night; a veto reading would have made the +1 row unreachable by construction. **The ambiguity is RED's drafting defect and is disclosed, not hidden;** a reader who takes the veto reading gets "none" and net-bear 68.

**Composition beside the move:** both qualifying legs are single names — EGBN one legacy loan, OZK one failed sale at $37.3M (below the $85M bridge-stress figure the OZK thread carried) — inside prints the owners grade as net contrary to stress (OZK classified + criticized −22%, conviction re-graded 🔴🔴 → 🟡 LOW, WQ-483 A; EGBN criticized −15%). Count-once: these rest on credit outcomes, distinct from FT-02's spread fire (+3 stands, never netted). **The 10/23 discretionary re-derivation must not reverse this +1 on the composition argument already recorded here** — that would re-litigate a pre-stated move on information known when it fired.

## (III) CHG-RED-054 — bank-put challenge legs (RED makes no trade; grades the reasoning only)

| Leg | Was | Rule hit | Now |
|---|---|---|---|
| OZK Nov-20 $40P | STRONG | "OZK adverse" (II) via W9 | **MODERATE** |
| WAL Dec-18 $65P | MODERATE | owner frame not bear (Bear CONFIRM not fired; "Q3 credit actuals weaken the near-term bear"); $99M **silent** → PENDING-10-Q | **unchanged MODERATE** |
| KRE lines (Nov-67 WEAK · Dec-60 MODERATE) | — | book-level test only: "credit breaking into bank funding or credit" | **unchanged.** The tree's strongest configuration (EGBN DET + OZK adverse) occurred on the letter, but both are single-name; the cohort shows coverage thinning (REGINALD: 5/5 computed fell) yet NCOs low (HBAN 0.31%, SSB 0.09%, ZION 0.02%), funding orderly (LIQ-07 S2), bank instruments outperforming their surroundings (REGINALD 005: BANK-ABSENT, conf ~0.6) |

Challenge lead grade → **MODERATE** (no leg above MODERATE). Re-review **2026-11-09** (OZK 10-Q ~11/5 for OZK-09 / SM −$313M; WAL 10-Q statutory 11/9 for the $99M). Book facts per FORGE ec5a7058b (Will's 11:01 ET capture); RED states no disposition.

## (IV) Market reaction — recorded, scores nothing

| Name | Day | Close | Prior | % |
|---|---|---|---|---|
| WAL | 10/20 | 75.30 | 73.63 | +2.27% |
| KRE | 10/20 | 70.62 | 69.26 | +1.96% |
| OZK | 10/21 | 48.09 | 46.16 | +4.18% |
| KRE | 10/21 | 70.62 | 70.62 | 0.00% |
| EGBN | 10/22 | **31.63 intraday 11:28 ET** | 28.53 | **+10.9% (intraday; close PENDING)** |
| KRE | 10/22 | 71.79 intraday | 70.62 | +1.66% |

**Flag:** EGBN intraday is outside TERRY #18's envelope (0 of 32 regional prints ≥10%). If it closes ≥10%, it is the first in that sample. The market is paying for the NCO collapse and the criticized decline — the opposite reading from the letter's DETERIORATION. Recorded, never netted against the substance verdict.

## CHG-RED-049 (rides along) — CARL CRL-29 first grade

CARL 10/21 (packet `inbox/2026-10-21_from-CARL_crl29-first-grade-no-verdict.md`): **panel NO VERDICT** — the 61+ stock rose in 5 of 6 tested trust-months, so the cure/extension/charge-off split the one-quantity test exists for did not arise. The registered null scores neither way. **CHG-049 stays ACTIVE, re-review 2026-11-15** (Nov HHDC, CARL's re-check, the same resolver class as CHG-045). VX-009 not re-measured (premise absent).

## FT-10 (DOCKET line in PROME's ask)

Publisher of record (Cboe SKEW_History.csv, pulled 11:28 ET): 160.45 [10/15] · 168.59 [10/16] · 161.86 [10/19] · 160.40 [10/20] · **150.36 [10/21]**. State: FIRED 10/14 (executed); **exit leg <140 strict s=4: 0 of 4.** The ≥150 count is not a RED action line after the fire; 150.36 is 10.36 above the exit line. **10/22 bar: PENDING** (publishes after the 16:00 ET close; this session closes before it). Rule for the next reader: grade the 10/22 bar only on the exit leg (<140.00 strict, four consecutive Cboe-published sessions → Acute −2 / Managed +2). FT-10's outcome test (VIXCLS ≥20 within 30 obs to ~11/25): VIX intraday 19.30 at 11:29 ET; VIXCLS 16.68 [10/21] — not met.
