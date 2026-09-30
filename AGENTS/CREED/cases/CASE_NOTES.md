# CREED Case Notes — full per-case record (on demand; grep the case_id)

**Built 2026-09-29.** For each case adopted from WALTER's draft seed (`AGENTS/WALTER/research/2026-09-29_cre-case-seed.tsv` @`0751bca40`): the **verifier's findings** (Opus, repo files only, no web) and the **seed row verbatim**. Where they disagree, **the verifier's finding is the better-sourced reading, but it is NOT yet applied to `CASES.tsv` fields** except the vocab tokens (property_type, trigger, holder_type, latest_status, status_as_of) and holder rule 6. Contradictions are carried, never resolved by picking a side.

## Held candidates (NOT adopted)

- **CASE-0021 Portal 405**: no distress EVENT in files -- only a third-party (Atrium) substandard grade; fails the FORMAT_SPEC v0.23 distress-event definition.
- **CASE-0034 One Moody Plaza**: no loan identified -- may be an OWNER disposition, not a distressed-loan resolution; README rule 1 (one case = one loan) not met. Still the Galveston S6 forced-sale comp in CREED rails (unchanged).
- **CASE-0057 Four Penn Center**: no distress EVENT stated -- only an appraisal cut ($91.9M -> $61.0M); cf. seed NOTES §4 excluding tax-assessment cuts as not loan events.

## Duplicates of CREED-built cases

### CASE-CREED-001 (seed CASE-0005)
- verdict: DUPLICATE; mismatches: vs CASE-CREED-001: facts match (1979, 441,523 sf, Bechtel Jul-2024, $80M+$20M, three conduit trusts, $25.2M 2025-10, $11.4M net, ~86%); seed ADDS Harris County ~$45M (video via SIG -015, unverified, basis tax-assessor, undated) and the undated 'April handback'; ledger status_as_of '<=2026-09-28 (sale date UNKNOWN)' vs seed 'SOLD (2026-09-28 reported)' -- ledger form is the rule-3-correct one; seed event '2024 default, trusts took title' -- KB-046 says 'defaulted 2024, trusts took title' with no year for the title transfer
- notes: Only new fact vs ledger is the video's Harris County ~$45M (unverified; HCAD value = tax-assessor basis, not appraisal). If added, tag basis tax-assessor and SEARCH-SUMMARY/unverified.
- contradictions: NOTES §5 #2: $170M (Trepp) vs $175M (X/Nightingale); $64.8M trust loss (vuln map :47,:72, source not found) vs $68.6M gross; April handback year unstated

### CASE-CREED-002 (seed CASE-0023)
- verdict: DUPLICATE; mismatches: none vs source. vs ledger CASE-CREED-002: seed latest_status 'FORECLOSED' (not vocab) | ledger 'FORECLOSURE' @AGENTS/CREED/cases/CASES.tsv row CASE-CREED-002; seed event '2026-01 transferred to SS' is SEARCH-SUMMARY only (SIG frontmatter), ledger agrees
- notes: All identity facts match the ledger row. Do not adopt; if anything, only the TENANT_VACATE/LISTED events are candidates for CASE_EVENTS under CASE-CREED-002. Ladder = originator only (README rule 6).
- contradictions: none

## Adopted cases

### CASE-CREED-003 — 1740 Broadway (seed CASE-0001)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** property_type: seed says Office | neither cited file states a property type (AGENTS/CREED/workbook/KB.tsv:21; AGENTS/REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md:44-46 lists it only under Blackstone defaults) -> UNKNOWN unless another source is added; trigger: seed says OTHER | AGENTS/REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md:9 frames the listed defaults as 'rational non-recourse strategic defaults' and KB-016 says Blackstone 'handed back the keys' -> vocab SPONSOR_WALKAWAY; value_marks: all three (S&P model $270.4M 2022-04, appraisal $175M 2023-07, note marketed ~$150M undated) found at stated basis; loan $308M found (AGENTS/REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md:46, undated, legacy)
- **event_year_check:** OK: 2022-03 keys, 2022-12 failed sale, 2023-07 appraisal, 2023-08 S&P, 2023-11 DBRS, 2022-04 S&P model all match KB-CREED-016. AAA 26% loss has no event date in files (only the 2024-08-27 Reuters report date) -> event_date <=2024-08-27
- **holder_established:** PARTIAL: a CMBS trust is established (loss hit an AAA CMBS tranche, KB-CREED-016) but trust name and SASB-vs-conduit are not stated
- **contradictions:** none carried in NOTES §5; internal: KB-016 event log is one secondary (Reuters via WALTER note) and the $308M loan is legacy-archive only
- **notes:** The S&P $270.4M is a model value; ledger event_type APPRAISAL needs a basis tag 'model value' not 'appraisal'. Servicer switch stated but servicer names not in files.
- **sources_found:** ALL FOUND: AGENTS/CREED/workbook/KB.tsv:21 KB-CREED-016; AGENTS/REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md:46 + :132 (Blackstone table; legacy, dated 2026-01-27)
- **proposed_events:** 2022-03|OTHER|Blackstone handed back the keys|UNKNOWN|n/a|AGENTS/CREED/workbook/KB.tsv:21; 2022-04|APPRAISAL|S&P model value (not an appraisal)|270400000|S&P model value|AGENTS/CREED/workbook/KB.tsv:21; 2022-12|OTHER|sale failed, buyer balked|UNKNOWN|n/a|AGENTS/CREED/workbook/KB.tsv:21; 2023-07|APPRAISAL|appraisal landed|175000000|appraisal|AGENTS/CREED/workbook/KB.tsv:21; 2023-08|OTHER|S&P cut AAA below IG|UNKNOWN|n/a|AGENTS/CREED/workbook/KB.tsv:21; 2023-11|OTHER|DBRS cut AAA below IG|UNKNOWN|n/a|AGENTS/CREED/workbook/KB.tsv:21; <=2024-08-27|LOSS_REALIZED|AAA tranche lost 26%|157500000|tranche loss (not loan-level)|AGENTS/CREED/workbook/KB.tsv:21; UNKNOWN|LISTED|note marketed ~$150M|150000000|marketing ask|AGENTS/REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md:46
**Seed row (verbatim):**
- *value_marks:* 2022-04 S&P model value $270.4M; 2023-07 appraisal $175M; undated legacy note: 70% value drop, note marketed at ~$150M
- *implied_loss_pct:* UNKNOWN (tranche-level: AAA lost 26% = $157.5M; loan-level loss not in files)
- *event_timeline:* 2022-03 Blackstone handed back the keys; 2022-12 sale failed (buyer balked); 2023-07 appraisal landed; 2023-08 S&P cut AAA below IG; 2023-11 DBRS cut AAA; UNKNOWN date AAA tranche took 26% loss ($157.5M) (Reuters 2024-08-27)
- *latest_status:* UNKNOWN (loss realized at AAA tranche per Reuters 2024-08-27)
- *trigger:* OTHER (sponsor handed back keys; reason not stated in files)
- *holder:* CMBS trust (name UNKNOWN)
- *sources:* KB-CREED-016 (WALTER note 2026-07-11 relaying Reuters 2024-08-27); REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md (legacy, dated 2026-01-27)
- *source_quality:* SECONDARY
- *notes:* Historical precedent (first AAA CMBS loss since 2008). Legacy archive row is pre-July CREED material that CREED deliberately did not import; $308M loan figure carries that caveat.

### CASE-CREED-004 — 8150 Sunset (LA entitled land) (seed CASE-0002)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** address: seed says street suffix not in files | AGENTS/OZK/SEVEN_CREDIT_DEEP_DIVE.md:158 gives '8150 Sunset Boulevard' (and :44 '8150 Sunset Blvd, LA'); value_marks: seed '2026-03 appraisal: OREO carried at 86% (=> ~$63.3M, derived)' is ambiguous | AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24: $63.3M is the DERIVED APPRAISAL (54.5/0.86), carrying is $54.5M; loan $63.5M and title date 2023-03-31 are tagged S (secondary, SEVEN §9) not D @ AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24; $12.0M: AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24 says 'extension fees and forfeited earnest money collected in 2024-25' and AGENTS/OZK/SEVEN_CREDIT_DEEP_DIVE.md:161 names the payer OKO Group (under contract 2023-2024)
- **event_year_check:** OK: 2021 loan, 2023-03-31 title, 2024-25 $12.0M, Q3'25 $2.5M, Q2'26 LOI all match stated years. Note {SEV}:161 says OKO was under contract 2023-2024
- **holder_established:** Y: BANK, OREO at OZK (AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24 CR RCON5508 $54,447K)
- **contradictions:** city: dossier {DOS}:24 says West Hollywood; SEVEN {SEV}:44 says 'LA' (not in NOTES §5)
- **notes:** Trigger UNKNOWN: files state a failed buyer and entitlement-risk reasons for failed CONTRACTS ({SEV}:162), not why the construction loan defaulted. Implied loss UNKNOWN is right; mgmt claims net proceeds >= carrying.
- **sources_found:** ALL FOUND: AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24 (8150 Sunset row, cites SEVEN §9 + MC2/MC3 + CR); AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:34 OZK-W11. Underlying AGENTS/OZK/SEVEN_CREDIT_DEEP_DIVE.md:44,158-161 also read
- **proposed_events:** 2021|ORIGINATED|$63.5M construction loan (S-tier)|63500000|commitment/loan face|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24; 2023-03-31|REO|OZK took title (LA Superior 23STCV21644 per SEVEN)|UNKNOWN|n/a|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24; 2024..2025|OTHER|failed buyer (OKO Group) paid/forfeited $12.0M extension fees + earnest money|12000000|fees collected|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24; 2025-Q3|OTHER|$2.5M forfeited earnest money applied to carrying|2500000|fees applied|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24; 2026-03|APPRAISAL|as-is appraisal (derived)|63300000|appraisal (DERIVED 54.5/0.86)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24; 2026-06-30|OTHER|OREO carrying|54500000|carrying value|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:24; 2026-Q2|LISTED|LOI being converted to a sale contract|UNKNOWN|n/a|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:34
**Seed row (verbatim):**
- *value_marks:* 2026-03 appraisal: OREO carried at 86% (=> ~$63.3M, derived); 2026-06-30 carrying $54.5M
- *implied_loss_pct:* UNKNOWN (carrying = 85.7% of the $63.5M loan, derived; mgmt says LOI net proceeds >= carrying)
- *event_timeline:* 2021 $63.5M construction loan; 2023-03-31 OZK took title; 2024-2025 prior purchaser paid $12.0M extension fees and forfeited earnest money; 2025-Q3 $2.5M forfeited earnest money applied to carrying; 2026-Q2 LOI being converted to a sale contract
- *latest_status:* REO (2026-06-30)
- *trigger:* UNKNOWN
- *holder:* Bank OZK (OREO)
- *sources:* REGINALD q2_OZK.md coverage line (OZK Q2 MC p.24; SEVEN §9); OZK Q2_WORKOUT_CHECK OZK-W11
- *source_quality:* MIXED
- *notes:* Issuer figures (D) mixed with desk estimates (S/DV).

### CASE-CREED-005 — Columbus Center (seed CASE-0003)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** trigger: seed says RATE_RESET;OPERATING_SHORTFALL (';' not the vocab '+' joiner) | AGENTS/OZK/workbook/KB.tsv:174 states occupancy 69%->63%, DSCR 1.98->0.59 'on floating-rate debt' AND 'Affinius DECLINED $2.4M reinstatement offer — deliberate walk-away' -> the stated walk-away is missing; holder: seed says 'Varde Partners (lender...)' | file names Varde as LENDER 'via Trimont' only -> holder not established (rule 6); source: AGENTS/OZK/workbook/KB.tsv:174 source cell is 'Claude (Prompt 9); court filings, Trepp' graded A1 -- an LLM-prompt output, court filing not read; seed tier SECONDARY is the right call
- **event_year_check:** OK: 2024-03 acceleration, 2024-10 $69M suit match. Reinstatement-offer date not stated
- **holder_established:** N: Varde named as lender of record in a foreclosure suit; balance-sheet vs fund vs securitization not stated; Trimont role not stated
- **contradictions:** none in NOTES §5; lender-sought recovery >$74M is a claim not a value
- **notes:** FLORIDA case absent from CORAL (NOTES §3). Status: a filed foreclosure suit maps to FORECLOSURE (in process) better than DEFAULT; either is defensible, outcome not in files.
- **sources_found:** ALL FOUND: AGENTS/OZK/workbook/KB.tsv:174 KB-OZK-169; fleet_link AGENTS/OZK/workbook/KB.tsv:208 KB-OZK-203 (Square Mile rebranded Affinius)
- **proposed_events:** 2024-03|DEFAULT|lender accelerated maturity|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:174; 2024-10|FORECLOSURE|foreclosure suit filed|69000000|claim amount|AGENTS/OZK/workbook/KB.tsv:174; UNKNOWN|OTHER|borrower declined $2.4M reinstatement offer (deliberate walk-away)|2400000|reinstatement amount|AGENTS/OZK/workbook/KB.tsv:174
**Seed row (verbatim):**
- *value_marks:* DSCR 1.98 -> 0.59 on floating-rate debt (dates not stated); lender seeks >$74M total recovery (a claim, not a value)
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2024-03 lender accelerated maturity; 2024-10 $69M foreclosure suit filed; UNKNOWN date borrower (Affinius Capital) declined a $2.4M reinstatement offer
- *latest_status:* DEFAULT (2024-10; foreclosure suit filed, outcome not in files)
- *trigger:* RATE_RESET;OPERATING_SHORTFALL
- *holder:* Varde Partners (lender; 'via Trimont', role of Trimont not stated)
- *sources:* KB-OZK-169 (Claude Prompt 9; 'court filings, Trepp')
- *source_quality:* SECONDARY
- *notes:* Florida case held only in the OZK desk file. Borrower/owner is Affinius Capital; KB calls it an isolated legacy office casualty and a deliberate walk-away.

### CASE-CREED-006 — Lafayette Centre (seed CASE-0004)
**Verifier:** VERIFIED
- **field_mismatches:** none: DC, $243M, 2024-06 SS all at the file; Beacon BCSP 8 link stated as fund-stress context
- **event_year_check:** OK: Jun'24 per file
- **holder_established:** N: special servicing implies CMBS but trust not named
- **contradictions:** none
- **notes:** KB-OZK-204's source cell is the Atrium PDF pp.45-49 but this clause is Beacon context in the same row that also cites WAL Q2'25 for Wilderness Labs -- the Lafayette clause's own source is not separately named. Thin row.
- **sources_found:** ALL FOUND: AGENTS/OZK/workbook/KB.tsv:209 KB-OZK-204 (one context clause: 'Lafayette Centre DC $243M special servicing Jun'24')
- **proposed_events:** 2024-06|TRANSFER_SS|transferred to special servicing|243000000|loan amount (basis not stated)|AGENTS/OZK/workbook/KB.tsv:209
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2024-06 transferred to special servicing
- *latest_status:* SPECIAL_SERVICING (2024-06)
- *trigger:* UNKNOWN
- *holder:* UNKNOWN (CMBS implied by special servicing; trust not named)
- *sources:* KB-OZK-204 (Atrium PDF pp.45-49, as context line)
- *source_quality:* SECONDARY
- *notes:* One-line context mention inside the Portal 405 row; no other file carries it.

### CASE-CREED-007 — Lincoln Yards land loan (northern ~27 acres, former A. Finkl & Sons site) (seed CASE-0006)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** status/identity: seed says 'Chicago land' sale identity with this loan INFERRED/not stated | AGENTS/OZK/SEVEN_CREDIT_DEEP_DIVE.md:174 states 'OZK's own Lincoln Yards northern acres cleared Sep 2025 at $84M/$126M loan basis = -33%' and AGENTS/OZK/workbook/KB.tsv:131 says 'Lincoln Yards: charge-off to liquidation, sold at book' -> identity IS stated (desk-level SEVEN, cited by the dossier as SEVEN §10); loan basis: seed $128M | AGENTS/OZK/SEVEN_CREDIT_DEEP_DIVE.md:174 uses $126M 'loan basis' vs $128M at AGENTS/OZK/workbook/KB.tsv:213 and AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:39; implied loss: seed gives ~30% vs 34% | add AGENTS/OZK/SEVEN_CREDIT_DEEP_DIVE.md:174 -33% ($84M/$126M); bases differ: 30% = cumulative writedown/loan, 33-34% = sale-at-carrying vs loan
- **event_year_check:** OK: 2019-12 origination, 2024-10 $21M, 2025-03 $38M + deed-in-lieu, Q3'25 / Sep-2025 sale. {OZK}:213 itself corrects Atrium's '2024 foreclosure' to 2025
- **holder_established:** Y: BANK (OZK loan; deed-in-lieu to OZK)
- **contradictions:** NOTES §5 #4 carried; ADD: $126M ({SEV}:174) vs $128M ({OZK}:213); 30% vs 33% vs 34% on two bases; $128M-$38M=$90M vs $83.95M sale at carrying implies ~$6M further mark not itemised in files
- **notes:** Seed's 'identity INFERRED' understates: two cited-chain files name Lincoln Yards for the Sep-2025 exit. Trigger UNKNOWN is correct (6 modifications stated, cause not).
- **sources_found:** ALL FOUND: AGENTS/OZK/workbook/KB.tsv:213 KB-OZK-208; AGENTS/OZK/workbook/KB.tsv:131 KB-OZK-126; AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:39 'Prior OREO exits'. Underlying AGENTS/OZK/SEVEN_CREDIT_DEEP_DIVE.md:174-175 also read
- **proposed_events:** 2019-12|ORIGINATED|$128M land loan (Sterling Bay)|128000000|loan amount|AGENTS/OZK/workbook/KB.tsv:213; UNKNOWN|MODIFICATION|modified 6 times|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:213; 2024-10|LOSS_REALIZED|writedown|21000000|cumulative writedown|AGENTS/OZK/workbook/KB.tsv:213; 2025-03|LOSS_REALIZED|cumulative writedown|38000000|cumulative writedown|AGENTS/OZK/workbook/KB.tsv:213; 2025-03|REO|deed-in-lieu|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:213; UNKNOWN|OTHER|under contract to JDL Development|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:213; 2025-09|SALE|sold at carrying|83950000|sale at carrying value|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:39 + AGENTS/OZK/SEVEN_CREDIT_DEEP_DIVE.md:174
**Seed row (verbatim):**
- *value_marks:* 2025-03 carrying after $38M writedowns; 2025-Q3 sale at carrying $83.95M
- *implied_loss_pct:* ~30% (KB-OZK-208: $38M/$128M) vs 34% (REGINALD dossier: $83.95M vs ~$128M)
- *event_timeline:* 2019-12 origination; modified 6 times (dates not stated); 2024-10 writedown $21M; 2025-03 cumulative writedown $38M and deed-in-lieu; later under contract to JDL Development; 2025-Q3 'Chicago land' sold at carrying $83.95M (OZK Q3 MC via REGINALD dossier; identity with this loan not stated)
- *latest_status:* SOLD (2025-Q3 per OZK Q3-25 MC 'Chicago land'; identity INFERRED)
- *trigger:* UNKNOWN
- *holder:* Bank OZK
- *sources:* KB-OZK-208 (Bisnow/TRD/Crain's 2024-25); KB-OZK-126; REGINALD q2_OZK.md 'Prior OREO exits'
- *source_quality:* MIXED
- *notes:* KB-OZK-126 says 'charge-off to liquidation, sold at book'. The dossier's 'Chicago land' is not named as Lincoln Yards in the file.

### CASE-CREED-008 — AMA Plaza (seed CASE-0007)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** city: seed says Chicago | AGENTS/OZK/workbook/KB.tsv:209 does not state a city for AMA Plaza -> city UNKNOWN per cited file; status: complaint filed maps to FORECLOSURE (in process) not DEFAULT
- **event_year_check:** OK: Nov'24 per file
- **holder_established:** N: lender/holder not named
- **contradictions:** none
- **notes:** city: seed says Chicago | AGENTS/OZK/workbook/KB.tsv:209 does not state a city for AMA Plaza -> city UNKNOWN per cited file. Status: complaint filed maps to FORECLOSURE (in process) rather than DEFAULT.
- **sources_found:** ALL FOUND: AGENTS/OZK/workbook/KB.tsv:209 KB-OZK-204 (context clause 'AMA Plaza foreclosure complaint Nov'24')
- **proposed_events:** 2024-11|FORECLOSURE|foreclosure complaint filed|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:209
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2024-11 foreclosure complaint filed
- *latest_status:* DEFAULT (2024-11; foreclosure complaint)
- *trigger:* UNKNOWN
- *holder:* UNKNOWN
- *sources:* KB-OZK-204 (Atrium PDF, context line)
- *source_quality:* SECONDARY
- *notes:* Thin row: one context mention only.

### CASE-CREED-009 — Bank of America Plaza (downtown LA) (seed CASE-0008)
**Verifier:** VERIFIED
- **field_mismatches:** none on values: $400.0M, 44.0% ($175.9M) balance-before-disposition, sold 6/16/26, 1.43M sf, 1974, ~$147/sf, $605M prior, $212.5M appraisal all found. Missing context: AGENTS/REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md:21-26 lists it under BROOKFIELD '2024 Defaults' -> sponsor Brookfield absent from seed fleet_links
- **event_year_check:** OK: 2024 maturity default supported by the '2024 Defaults' table heading at AGENTS/REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md:23; sale 2026-06-16 per AGENTS/CREED/workbook/KB.tsv:46. Appraisal date UNKNOWN
- **holder_established:** PARTIAL: CMBS established (CREFC CMBS liquidation data, KB-CREED-041); trust name and SASB/conduit not stated
- **contradictions:** NOTES §5 #15 (distinct from St. Louis CASE-0015) carried
- **notes:** Receivership sale per {CR}:100 -- a receivership event precedes the sale but is undated.
- **sources_found:** ALL FOUND: AGENTS/CREED/workbook/KB.tsv:46 KB-CREED-041; AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:100 (§2b row); AGENTS/REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md:26 + :131
- **proposed_events:** 2024|DEFAULT|maturity default|400000000|loan balance|AGENTS/REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md:26; UNKNOWN|APPRAISAL|appraised vs $605M decade prior|212500000|appraisal|AGENTS/REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009_INSTITUTIONAL_STRATEGIC_DEFAULTS.md:26; 2026-06-16|SALE|receivership sale ~$147/sf|UNKNOWN|sale price per sf only|AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:100; 2026-06-16|LOSS_REALIZED|loss 44.0% of balance before disposition|175900000|loss vs balance before disposition|AGENTS/CREED/workbook/KB.tsv:46
**Seed row (verbatim):**
- *value_marks:* decade-prior value $605M; appraisal $212.5M (legacy archive, date UNKNOWN); 2026-06-16 receivership sale at ~$147/sf; loss $175.9M on $400.0M
- *implied_loss_pct:* 44.0% (source-stated, loss vs balance before disposition)
- *event_timeline:* 2024 maturity default (legacy archive); 2026-06-16 sold in a receivership sale
- *latest_status:* SOLD (2026-06-16)
- *trigger:* MATURITY_DEFAULT
- *holder:* CMBS trust (name UNKNOWN)
- *sources:* KB-CREED-041 (CREFC July 2026, Trepp data, PRIMARY-READ); CREED/analysis/2026-09-27_nano-banc-collateral-read.md §2b; REGINALD/archive/sub-agents/CREED/research/RQ-CREED-009 (legacy)
- *source_quality:* MIXED
- *notes:* Not the same building as Bank of America Plaza (St. Louis), CASE-0010.

### CASE-CREED-010 — 760 Aloha (seed CASE-0009)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** status: seed says 'REO...; dossier describes an exit, date UNKNOWN' | AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:41 dates it: 'Seattle 760 Aloha (Q4'25), $6.44M: carried at 58% of a Nov'24 appraisal, after a write-down to the offer' and :42 'the two Q4'25 sales produced a combined +$0.3M net gain' -> SOLD Q4'25; value: seed carries only $6.84M (60% of appraisal, Atrium) | dossier gives $6.44M at 58% -- two figures, two sources; property_type: AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:164 calls it 'OZK's only disclosed vacant-Seattle-office exit' -> OFFICE is stated
- **event_year_check:** OK: Nov-2024 appraisal; exit Q4'25 (seed had UNKNOWN)
- **holder_established:** Y: BANK (OREO at OZK)
- **contradictions:** NEW (not in NOTES §5): $6.84M/60% (KB-OZK-207, Atrium) vs $6.44M/58% (dossier, MC4) -- possibly pre- vs post- write-down-to-offer; not resolved
- **notes:** Carrying/credit 31% derivation in seed stands on the $6.84M figure only.
- **sources_found:** ALL FOUND: AGENTS/OZK/workbook/KB.tsv:212 KB-OZK-207; AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:41 (+ :64, :164)
- **proposed_events:** ~2024..2025|REO|OZK took to OREO|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:212; 2024-11|APPRAISAL|appraisal (value not stated)|UNKNOWN|appraisal|AGENTS/OZK/workbook/KB.tsv:212; <=2025-12-31|OTHER|OREO carrying $6.84M = 40% below Nov-24 appraisal (Atrium Q4'25)|6840000|carrying value|AGENTS/OZK/workbook/KB.tsv:212; 2025-Q4|SALE|sold at carrying after write-down to the offer|6440000|carrying at sale (58% of Nov-24 appraisal)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:41
**Seed row (verbatim):**
- *value_marks:* OREO carrying $6.84M = 40% below the Nov-2024 appraisal (Atrium Q4-25)
- *implied_loss_pct:* UNKNOWN (carrying $6.84M is 31% of the $21.8M credit; not a resolution value)
- *event_timeline:* ~2024-2025 OZK took it to OREO; 2024-11 appraisal (value not in files); UNKNOWN date exit at 58% of appraisal (REGINALD dossier)
- *latest_status:* REO (Atrium Q4-25 read); REGINALD dossier describes an exit, date UNKNOWN
- *trigger:* UNKNOWN
- *holder:* Bank OZK (OREO)
- *sources:* KB-OZK-207 (Atrium PDF p.54); REGINALD q2_OZK.md Task 2
- *source_quality:* SECONDARY
- *notes:* CREED's comp C3 'OZK own Seattle office exit 58% of appraisal' is unnamed; REGINALD's dossier attributes the 58% exit to 760 Aloha.

### CASE-CREED-011 — Blackhawk Plaza (seed CASE-0010)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** trigger: seed says FRAUD_OR_LEGAL | files state 'payments stopped Mar 2025', Nano suit, receivership, owner a Stupin entity -- the CAUSE of non-payment is not stated, and BOARD/SIG-W-20260927-005-CORRECTION-nano-banc-holds-four-deeds-of-trust-senior-to-wal-on-5-of-10-pleaded-loans-the-wal-link-is-not-only-via-the-fraud.md + AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:15 note Blackhawk is NOT among WAL's pleaded fraudulent-title loans -> UNKNOWN; latest_status: seed DEFAULT | owner in Ch.11 -> vocab BANKRUPTCY
- **event_year_check:** OK: 2024 origination, Mar-2025 stop, summer-2025 suit, 2026-02-03 receivership, 2026-03-18 Ch.11. 2023 appraisal year OK
- **holder_established:** N: Preferred Bank 1st (~$31M) and Nano 2nd named as lienholders; Nano lien holder at 9/25 (FDIC receiver vs Sunwest) not established
- **contradictions:** none
- **notes:** Liens $35.8M + $657,111 taxes vs 2023 appraisal $57.38M -- mixed dates; do not derive an LTV. One case = one loan: the row mixes the Preferred 1st and Nano 2nd; pick which loan the case is.
- **sources_found:** ALL FOUND: AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:71 (§2a Blackhawk row, citing danvillesanramon.com 2026-01-21/07-02 + elevenflo); AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:61; AGENTS/CREED/workbook/KB.tsv:47 KB-CREED-042
- **proposed_events:** 2024|ORIGINATED|Nano $5M 2nd lien|5000000|loan face|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:71; 2025-03|DEFAULT|payments stopped|UNKNOWN|n/a|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:71; 2025 (summer)|OTHER|Nano sued, OC Superior|UNKNOWN|n/a|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:71; 2026-02-03|OTHER|receivership ordered|UNKNOWN|n/a|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:71; 2026-03-18|BANKRUPTCY_FILING|Ramanujan Group LLC Ch.11 8:26-bk-10832-SC, stays receivership|UNKNOWN|n/a|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:71; 2023|APPRAISAL|appraisal|57380000|appraisal|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:71; 2026-09-25|OTHER|Nano Banc failed|UNKNOWN|n/a|AGENTS/CREED/workbook/KB.tsv:47
**Seed row (verbatim):**
- *value_marks:* 2023 appraisal $57.38M; liens total $35.8M + $657,111 taxes
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2024 Nano $5M loan; 2025-03 payments stopped; 2025 (summer) Nano sued in OC Superior Court; 2026-02-03 receivership ordered; 2026-03-18 owner Ramanujan Group LLC (Stupin entity) filed Ch.11 8:26-bk-10832-SC, staying the receivership; debtor intends to sell
- *latest_status:* DEFAULT (2026-03-18; owner in Ch.11)
- *trigger:* FRAUD_OR_LEGAL
- *holder:* Preferred Bank (1st); Nano 2nd now FDIC receiver or Sunwest (UNKNOWN)
- *sources:* CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md §2a (danvillesanramon.com 2026-01-21, 2026-07-02; elevenflo); CREED/analysis/2026-09-27_nano-banc-collateral-read.md l.61
- *source_quality:* SECONDARY
- *notes:* Stupin-network credit; not one of WAL's pleaded collateral loans.

### CASE-CREED-012 — Gateway I and II (seed CASE-0011)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** value_marks: seed says 'HCAD appraisals' | HCAD = Harris County Appraisal District -> basis is TAX-ASSESSOR value, not an appraisal (rule 4); source tier: seed SECONDARY | BOARD/SIG-W-20260929-015-will-directed-houston-office-video-one-new-named-case-5400-westheimer-ct-single-tenant-exit-foreclosed-ladder-loan-and-a-two-tier-market.md:8 says 'via search listing only' / not read -> SEARCH-SUMMARY (rule 7)
- **event_year_check:** CORRECT AS SEEDED: 2025 (Beryl July 2024 = 'last year') per BOARD/SIG-W-20260929-015-will-directed-houston-office-video-one-new-named-case-5400-westheimer-ct-single-tenant-exit-foreclosed-ladder-loan-and-a-two-tier-market.md:8,33 -- a 2025 event the video sold as 2026; auction 2025-04-01 year inferred, not printed
- **holder_established:** N: nothing on lender/holder
- **contradictions:** none
- **notes:** Rule 11 case: keep, but any 2026-pattern count must exclude it. Property type not stated (context is a Houston office video; not stated for Gateway).
- **sources_found:** ALL FOUND: BOARD/SIG-W-20260929-015-will-directed-houston-office-video-one-new-named-case-5400-westheimer-ct-single-tenant-exit-foreclosed-ladder-loan-and-a-two-tier-market.md:8 (origin, Bisnow search listing) + :33 (table); AGENTS/WALTER/registry/BATCH_MANIFEST.tsv:109 item 7 NO-ACTION
- **proposed_events:** <=2025-04-01|DEFAULT|~$13M loan default|13000000|loan amount (approx)|BOARD/SIG-W-20260929-015-will-directed-houston-office-video-one-new-named-case-5400-westheimer-ct-single-tenant-exit-foreclosed-ladder-loan-and-a-two-tier-market.md:8; 2025-04-01 (year inferred)|FORECLOSURE|foreclosure auction scheduled|UNKNOWN|n/a|BOARD/SIG-W-20260929-015-will-directed-houston-office-video-one-new-named-case-5400-westheimer-ct-single-tenant-exit-foreclosed-ladder-loan-and-a-two-tier-market.md:8; 2024 ('last year')|APPRAISAL|HCAD values $6.4M + $4.7M|11100000|tax-assessor value|BOARD/SIG-W-20260929-015-will-directed-houston-office-video-one-new-named-case-5400-westheimer-ct-single-tenant-exit-foreclosed-ladder-loan-and-a-two-tier-market.md:8
**Seed row (verbatim):**
- *value_marks:* HCAD appraisals $6.4M + $4.7M = ~$11.1M ('last year' relative to the 2025 article)
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2025-04-01 foreclosure auction (year inferred: article cites Hurricane Beryl, July 2024, as 'last year')
- *latest_status:* UNKNOWN (auction outcome not in files)
- *trigger:* UNKNOWN
- *holder:* UNKNOWN
- *sources:* SIG-W-20260929-015 (Bisnow via search listing only)
- *source_quality:* SECONDARY
- *notes:* A 2025 event presented as 2026 in the video; WALTER marked it NO-ACTION in BM-20260929-09.

### CASE-CREED-013 — Alessandro Plaza (seed CASE-0012)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** latest_status: seed DEFAULT | owner Alessandro Group LLC in Ch.11 (C.D. Cal. 8:26-bk-12516-SC per AGENTS/WAL/workbook/KB.tsv:207) -> BANKRUPTCY; NOD attribution: seed/SIG-005 put the 2025-05-20 NOD on the Nano DOT | AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:67 says the complaint 'doesn't say which DOT' in the Loan 33 paragraph (contrast Ontario where it does); 'to halt a trustee sale' is in AGENTS/WAL/workbook/KB.tsv:207, while AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:50 has an X/RK post saying 'to halt California property foreclosures' -- secondary
- **event_year_check:** OK: DOT dated 2019-08-29, recorded 2019-09-09; NOD 2025-05-20; WAL complaint 2025-08-18; Ch.11 2026-08-18; Nano failure 2026-09-25. Listing asks undated
- **holder_established:** N: Nano 1st lien per 2025 complaint; holder at 9/25 'leaning still-Nano' (AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:199) = not proven; beneficiary unconfirmed (AGENTS/WAL/workbook/KB.tsv:207)
- **contradictions:** NOTES §5 #12 (119K vs 84K SF) carried; ADD NOD-on-which-DOT ({S005} lien table vs {RN}:67)
- **notes:** Trigger FRAUD_OR_LEGAL = the file-stated reason this is a case (WAL fraud complaint on this collateral); the property-level default cause is not stated. Face amounts at origination, not balances.
- **sources_found:** ALL FOUND: BOARD/SIG-W-20260927-005-CORRECTION-nano-banc-holds-four-deeds-of-trust-senior-to-wal-on-5-of-10-pleaded-loans-the-wal-link-is-not-only-via-the-fraud.md (lien table); AGENTS/WAL/workbook/KB.tsv:204 KB-WAL-202; AGENTS/WAL/workbook/KB.tsv:207 KB-WAL-205; AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md §1c l.53-73 + §6 l.195-203; AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md §Q2 l.44-53 + §2a l.63-71; AGENTS/CREED/workbook/KB.tsv:47 KB-CREED-042
- **proposed_events:** 2019-08-29|ORIGINATED|Nano DOT dated (recorded 2019-09-09)|9720000|DOT original face|AGENTS/WAL/workbook/KB.tsv:204; 2025-05-20|DEFAULT|Notice of Default recorded (DOT not specified in complaint)|UNKNOWN|n/a|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:67; 2025-08-18|OTHER|WAL verified complaint (doctored title policy showed WAL first)|UNKNOWN|n/a|AGENTS/WAL/workbook/KB.tsv:204; 2026-08-18|BANKRUPTCY_FILING|Alessandro Group LLC Ch.11 26-12516|UNKNOWN|n/a|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:50; UNKNOWN|LISTED|listing ask for an 84,000 SF perimeter|14200000|listing ask ($15M in another headline)|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:50; 2026-09-25|OTHER|Nano Banc failed|UNKNOWN|n/a|AGENTS/CREED/workbook/KB.tsv:47
**Seed row (verbatim):**
- *value_marks:* listing ask $14.2M / $15M for an 84,000 SF perimeter (The Registry headline, date UNKNOWN)
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2019-09-09 Nano DOT recorded; 2025-05-20 Notice of Default recorded; 2025-08-18 WAL verified complaint (doctored title policy showed WAL first); 2026-08-18 owner Alessandro Group LLC filed Ch.11 (C.D. Cal. 26-12516) to halt a trustee sale; 2026-09-25 Nano Banc failed
- *latest_status:* DEFAULT (2026-08-18; owner in Ch.11)
- *trigger:* FRAUD_OR_LEGAL
- *holder:* Nano DOT holder at 2026-09-25 UNKNOWN ('leaning still-Nano' => FDIC receiver or Sunwest); WAL junior per complaint
- *sources:* SIG-W-20260927-005; KB-WAL-202; KB-WAL-205; CREED/analysis/2026-09-27_nano-banc-collateral-read.md §1c+§6; CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md §2a; KB-CREED-042
- *source_quality:* MIXED
- *notes:* Lien facts from WAL's verified complaint (A2, via third-party host); property/status SECONDARY. Face amounts at origination, not current balance.

### CASE-CREED-014 — Plaza Continental (seed CASE-0013)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** latest_status: seed DEFAULT | owner in single-asset Ch.11 since 2026-03-30 -> vocab BANKRUPTCY; otherwise all fields found: Preferred $25.9M 1st 2022-04-07, owed ~$23,131,053; Nano $4,333,151.35 dated 2022-11-10 rec. 2023-01-13, owed ~$5,131,969; rents receiver Dec-2025; Nano creditor filing 2026-09-11 (AGENTS/WAL/workbook/KB.tsv:207); ~120K SF, ~24% available (AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:51); Nano suit 2025-07-11 is from a Law.com snippet (SECONDARY, AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:68)
- **event_year_check:** OK: all years match source
- **holder_established:** N: Nano lien per the DEBTOR as of 9/8-9/11/2026; ownership at 9/25 NOT PROVEN (AGENTS/WAL/workbook/KB.tsv:207); Preferred named 1st lienholder
- **contradictions:** none beyond holder-at-failure open question
- **notes:** property_type: 'office/medical + retail' (AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:58); OFFICE proposed, MIXED_USE defensible -- CREED's call. 2026-09-29 hearing outcome not in files (UNKNOWN is valid per AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:203).
- **sources_found:** ALL FOUND: BOARD/SIG-W-20260927-005-CORRECTION-nano-banc-holds-four-deeds-of-trust-senior-to-wal-on-5-of-10-pleaded-loans-the-wal-link-is-not-only-via-the-fraud.md (lien table); AGENTS/WAL/workbook/KB.tsv:204 KB-WAL-202; AGENTS/WAL/workbook/KB.tsv:207 KB-WAL-205; AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md §1c l.53-73 + §6 l.195-203; AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md §Q2 l.44-53 + §2a l.63-71; AGENTS/CREED/workbook/KB.tsv:47 KB-CREED-042
- **proposed_events:** 2022-04-07|ORIGINATED|Preferred 1st|25900000|DOT original face|AGENTS/WAL/workbook/KB.tsv:204; 2022-11-10|ORIGINATED|Nano 2nd DOT dated (rec. 2023-01-13)|4333151|DOT original face|AGENTS/WAL/workbook/KB.tsv:204; 2025-05-20|DEFAULT|NOD on the Nano DOT recorded|UNKNOWN|n/a|AGENTS/WAL/workbook/KB.tsv:204; 2025-07-11|OTHER|Nano sued Plaza Continental Group LLC (OC Superior)|4300000|claim|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:68; 2025-08-18|OTHER|WAL verified complaint|UNKNOWN|n/a|AGENTS/WAL/workbook/KB.tsv:204; 2025-12|OTHER|Nano obtained rents receiver|UNKNOWN|n/a|AGENTS/WAL/workbook/KB.tsv:207; 2026-03-30|BANKRUPTCY_FILING|single-asset Ch.11 8:26-bk-10986-MH|UNKNOWN|n/a|AGENTS/WAL/workbook/KB.tsv:207; 2026-09-11|OTHER|Nano filed as creditor; debtor says Nano owed ~$5,131,969|5131969|debtor-stated balance|AGENTS/WAL/workbook/KB.tsv:207; 2026-09-25|OTHER|Nano Banc failed|UNKNOWN|n/a|AGENTS/CREED/workbook/KB.tsv:47
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2022-04-07 Preferred 1st; 2023-01-13 Nano DOT recorded; 2025-05-20 NOD recorded on the Nano DOT; 2025-07-11 Nano sued Plaza Continental Group LLC (OC Superior); 2025-08-18 WAL verified complaint; 2025-12 Nano obtained a rents receiver; 2026-03-30 owner filed single-asset Ch.11 8:26-bk-10986-MH; 2026-09-11 Nano filed as creditor; 2026-09-25 Nano failed; 2026-09-29 bankruptcy hearing (outcome not in files)
- *latest_status:* DEFAULT (2026-09-11; owner in Ch.11 since 2026-03-30, rents receiver since 2025-12)
- *trigger:* FRAUD_OR_LEGAL
- *holder:* Preferred Bank (1st); Nano lien per debtor as of 2026-09-08..11 (holder at 9/25 NOT proven)
- *sources:* SIG-W-20260927-005; KB-WAL-202; KB-WAL-205; CREED/analysis/2026-09-27_nano-banc-collateral-read.md §1c+§6; CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md §2a; KB-CREED-042
- *source_quality:* MIXED
- *notes:* Hearing 2026-09-29 could show whether FDIC-as-receiver or Sunwest holds the Nano lien.

### CASE-CREED-015 — Starwood Hotel Portfolio Whole Loan (seed CASE-0014)
**Verifier:** VERIFIED
- **field_mismatches:** none on facts: $265M IO, 22 hotels, 2,943 keys, 12 states/17 cities, Marriott/Hilton/IHG, K-Star, DSCR 2.07->0.64, 2018-08-16, Jan-2026 SS all at file. Vocab: 'Hotel' -> LODGING. Seed's '2026-05-06 TRD coverage' is a REPORT date, not a case event (rule 8)
- **event_year_check:** OK: SS transfer JANUARY 2026 (signal corrects TRD's 'just hit' framing); origination 2018
- **holder_established:** PARTIAL: CMBS stated ('Underlying CMBS'); deal/trust ticker not surfaced; SASB vs conduit not stated
- **contradictions:** none
- **notes:** Trigger OPERATING_SHORTFALL is stated by WALTER's mechanism line (revenue-driven, fixed-rate CMBS) linking to AHLA data -- a WALTER inference, verify-research CONFIRMED 0.88 covers the loan facts, not the mechanism.
- **sources_found:** ALL FOUND: BOARD/SIG-W-20260507-004-trd-sternlicht-starwood-capital-265m-22-hotels-cmbs-special-servicing-jan2026-pattern.md (origin + Load-bearing facts + dispatch_note)
- **proposed_events:** 2018-08-16|ORIGINATED|$265M IO whole loan, DSCR 2.07|265000000|loan amount|BOARD/SIG-W-20260507-004-trd-sternlicht-starwood-capital-265m-22-hotels-cmbs-special-servicing-jan2026-pattern.md; 2025 (mid)|OTHER|DSCR 0.64|UNKNOWN|n/a|BOARD/SIG-W-20260507-004-trd-sternlicht-starwood-capital-265m-22-hotels-cmbs-special-servicing-jan2026-pattern.md; 2026-01|TRANSFER_SS|to K-Star|UNKNOWN|n/a|BOARD/SIG-W-20260507-004-trd-sternlicht-starwood-capital-265m-22-hotels-cmbs-special-servicing-jan2026-pattern.md
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2018-08-16 origination (DSCR 2.07); 2025 (mid) DSCR 0.64; 2026-01 transferred to special servicing; 2026-05-06 TRD coverage ('just hit' framing was stale)
- *latest_status:* SPECIAL_SERVICING (2026-01)
- *trigger:* OPERATING_SHORTFALL
- *holder:* CMBS (deal/trust ticker not surfaced in open sources)
- *sources:* SIG-W-20260507-004 (verify-research CONFIRMED 0.88 vs TRD + Morningstar/KBRA loan data)
- *source_quality:* MIXED
- *notes:* Same sponsor's earlier $577M/65-hotel loan (early 2025, also K-Star, modified 2025-09) is not rowed: no property name. Revenue-driven per WALTER (fixed-rate CMBS).

### CASE-CREED-016 — Bank of America Plaza (St. Louis) (seed CASE-0015)
**Verifier:** VERIFIED
- **field_mismatches:** none: foreclosed summer 2025, auctioned May 2026, sold June 2026 ~$9.5M+ all at file ('REO sale')
- **event_year_check:** OK: 2025 foreclosure, 2026-05 auction, 2026-06 sale per file
- **holder_established:** N: lender not named ('REO sale' only)
- **contradictions:** NOTES §5 #15 carried
- **notes:** Single context line; source of the line not named in the file. Property type not stated.
- **sources_found:** ALL FOUND: AGENTS/CREED/research/2026-08-13_NEWS_SWEEP_RESULTS.md:36 (§3)
- **proposed_events:** 2025 (summer)|FORECLOSURE|foreclosed|UNKNOWN|n/a|AGENTS/CREED/research/2026-08-13_NEWS_SWEEP_RESULTS.md:36; 2026-05|OTHER|auctioned|UNKNOWN|n/a|same:36; 2026-06|SALE|REO sale|9500000|sale price (lower bound, '~$9.5M+')|same:36
**Seed row (verbatim):**
- *value_marks:* 2026-06 sale ~$9.5M+
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2025 (summer) foreclosed; 2026-05 auctioned; 2026-06 sold
- *latest_status:* SOLD (2026-06)
- *trigger:* UNKNOWN
- *holder:* UNKNOWN
- *sources:* CREED/research/2026-08-13_NEWS_SWEEP_RESULTS.md §3
- *source_quality:* SECONDARY
- *notes:* Noted by CREED for context only (outside its sweep window). Different building from CASE-0008.

### CASE-CREED-017 — Chino Towne Center (Nano/WAL collateral parcel) (seed CASE-0016)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** latest_status: seed 'UNKNOWN (2026-09-27; no foreclosure found)' | AGENTS/WAL/workbook/KB.tsv:207 cites 'In re Chino Central Group 8:26-bk-10925-SC Doc 122 (8/26/2026)' -- the OWNER IS IN CHAPTER 11 -> BANKRUPTCY (filing date not in files, <=2026-08-26); holder: seed 'debtor lists WAL + Nano liens ~$19.1M' found at AGENTS/WAL/workbook/KB.tsv:207, which also carries DEWEY's INFERENCE that WAL bought Preferred's senior (so WAL senior, Nano junior) -- inference only; values: 2025-02 ~$29M appraisal and $23.5-26.5M broker range found as debtor-side at AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:201
- **event_year_check:** OK: Preferred 2016, Nano DOT dated 2023-01-26 rec. 2023-06-30, WAL complaint 2025-08-18, debtor filing 2026-08-26, Nano failure 2026-09-25. Bankruptcy filing date UNKNOWN
- **holder_established:** N: Nano lien per debtor as of 8/26/2026; ownership at 9/25 NOT PROVEN (AGENTS/WAL/workbook/KB.tsv:207)
- **contradictions:** NOTES §5 #11 (12233 vs 12125) carried; NEW: AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:52 says 'No sign of foreclosure, sale, receivership or bankruptcy found' vs AGENTS/WAL/workbook/KB.tsv:207 citing the Chino Central Group Ch.11 docket
- **notes:** Most consequential miss in this block: a cited file shows a bankruptcy the seed row omits.
- **sources_found:** ALL FOUND: BOARD/SIG-W-20260927-005-CORRECTION-nano-banc-holds-four-deeds-of-trust-senior-to-wal-on-5-of-10-pleaded-loans-the-wal-link-is-not-only-via-the-fraud.md (lien table); AGENTS/WAL/workbook/KB.tsv:204 KB-WAL-202; AGENTS/WAL/workbook/KB.tsv:207 KB-WAL-205; AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md §1c l.53-73 + §6 l.195-203; AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md §Q2 l.44-53 + §2a l.63-71; AGENTS/CREED/workbook/KB.tsv:47 KB-CREED-042
- **proposed_events:** 2016|ORIGINATED|Preferred 1st|22400000|DOT original face|AGENTS/WAL/workbook/KB.tsv:204; 2023-01-26|ORIGINATED|Nano 2nd DOT dated (rec. 2023-06-30)|5990000|DOT original face|AGENTS/WAL/workbook/KB.tsv:204; 2025-02|APPRAISAL|debtor-side appraisal|29000000|appraisal (debtor-side, ~)|AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:201; 2025-08-18|OTHER|WAL verified complaint|UNKNOWN|n/a|AGENTS/WAL/workbook/KB.tsv:204; <=2026-08-26|BANKRUPTCY_FILING|In re Chino Central Group 8:26-bk-10925-SC|UNKNOWN|n/a|AGENTS/WAL/workbook/KB.tsv:207; 2026-08-26|OTHER|debtor filing lists WAL + Nano liens ~$19.1M|19100000|debtor-stated liens|AGENTS/WAL/workbook/KB.tsv:207; 2026|LISTED|broker range|25000000|broker marketing range $23.5-26.5M (midpoint shown; debtor-side)|AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:201; 2026-09-25|OTHER|Nano Banc failed|UNKNOWN|n/a|AGENTS/CREED/workbook/KB.tsv:47
**Seed row (verbatim):**
- *value_marks:* 2025-02 appraisal ~$29M (debtor-side); 2026 broker range $23.5-26.5M (debtor-side marketing)
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2016 Preferred 1st; 2023-06-30 Nano DOT recorded; 2025-02 appraisal; 2025-08-18 WAL verified complaint; 2026-08-26 debtor filing lists the Nano lien; 2026-09-25 Nano failed
- *latest_status:* UNKNOWN (2026-09-27; no foreclosure found)
- *trigger:* FRAUD_OR_LEGAL
- *holder:* Nano lien per debtor as of 2026-08-26 (holder at 9/25 NOT proven); debtor lists WAL + Nano liens ~$19.1M
- *sources:* SIG-W-20260927-005; KB-WAL-202; KB-WAL-205; CREED/analysis/2026-09-27_nano-banc-collateral-read.md §1c+§6; CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md §2a; KB-CREED-042
- *source_quality:* MIXED
- *notes:* Address conflict 12233 vs 12125 and a 65.91% TIC match are explicitly unverified (CATO NB6).

### CASE-CREED-018 — Cedar Group Apartments (seed CASE-0017)
**Verifier:** VERIFIED
- **field_mismatches:** none on facts: 9826 Cedar St, 1964, 30 units, 25,024 SF, 0.91 ac, Umpqua $6.47M 2018, Nano $8.0M dated 2024-09-16 rec. 2024-09-27, last sale 1999-01-22 $1,370,000, liens $14.47M ~$482K/unit (AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:53,70). status_as_of: seed '2026-09-27' is the READ date | status source is Redfin 'Last updated August 2026' (AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:53) -> as-of 2026-08 (rule 3)
- **event_year_check:** OK: all years match
- **holder_established:** N: Bellflower holder UNKNOWN (LA County no online index, AGENTS/WAL/workbook/KB.tsv:207)
- **contradictions:** none
- **notes:** MULTIFAMILY -> HOMER owns MF named credits (README rule 10): fleet_links should cite HOMER. Under-secured read is INFERRED.
- **sources_found:** ALL FOUND: BOARD/SIG-W-20260927-005-CORRECTION-nano-banc-holds-four-deeds-of-trust-senior-to-wal-on-5-of-10-pleaded-loans-the-wal-link-is-not-only-via-the-fraud.md (lien table); AGENTS/WAL/workbook/KB.tsv:204 KB-WAL-202; AGENTS/WAL/workbook/KB.tsv:207 KB-WAL-205; AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md §1c l.53-73 + §6 l.195-203; AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md §Q2 l.44-53 + §2a l.63-71; AGENTS/CREED/workbook/KB.tsv:47 KB-CREED-042
- **proposed_events:** 1999-01-22|ACQUIRED|last recorded sale|1370000|sale price|AGENTS/CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md:53; 2018|ORIGINATED|Umpqua 1st|6470000|DOT original face|AGENTS/WAL/workbook/KB.tsv:204; 2024-09-16|ORIGINATED|Nano 2nd DOT dated (rec. 2024-09-27)|8000000|DOT original face|AGENTS/WAL/workbook/KB.tsv:204; 2025-08-18|OTHER|WAL verified complaint|UNKNOWN|n/a|AGENTS/WAL/workbook/KB.tsv:204; 2026-09-25|OTHER|Nano Banc failed|UNKNOWN|n/a|AGENTS/CREED/workbook/KB.tsv:47
**Seed row (verbatim):**
- *value_marks:* liens $14.47M = ~$482K/unit
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 1999-01-22 last recorded sale $1,370,000; 2018 Umpqua 1st; 2024-09-27 Nano DOT recorded; 2025-08-18 WAL verified complaint; 2026-09-25 Nano failed
- *latest_status:* UNKNOWN (2026-09-27; no NOD, sale or foreclosure transfer found)
- *trigger:* FRAUD_OR_LEGAL
- *holder:* UNKNOWN (LA County has no online index)
- *sources:* SIG-W-20260927-005; KB-WAL-202; KB-WAL-205; CREED/analysis/2026-09-27_nano-banc-collateral-read.md §1c+§6; CREED/research/2026-09-27_nano-banc-retained-pool-research-notes.md §2a; KB-CREED-042
- *source_quality:* MIXED
- *notes:* CREED infers Nano's 2nd is badly under-secured (INFERRED).

### CASE-CREED-019 — 1229 W. Concord Place (Lincoln Yards life-science building) (seed CASE-0018)
**Verifier:** VERIFIED
- **field_mismatches:** none on values: $125.1M commit 2021-09-14, ~$65.1M peak o/s (DV), $5.1M Q3'25 + $9.0M Q4'25 c/o, $50M Q1 carrying = 68% of ~$74M May-25 appraisal, $2.5M Q2 OREO write-down, $47.5M 6/30, Jun-26 appraisal ~$50.0M (DV), Atrium $105.2M/$45M, BOTO Strategic Properties IV LLC, Novak short sale failed, DIL Mar-2026. Trigger OTHER is not vocab | file-stated cause = 100% vacant since completion early 2023 (AGENTS/OZK/workbook/KB.tsv:98) -> closest vocab OPERATING_SHORTFALL (suggest a vocab term for lease-up failure). Note AGENTS/OZK/workbook/KB.tsv:204 calls it 'a $65M loan' (outstanding) -- basis mix; AGENTS/OZK/workbook/KB.tsv:196 identity was 'Likely' at Q1, firmed by :98/:204
- **event_year_check:** OK: 2021 loan, 2023 completion, 2025 c/o, 2026-03 DIL, Q2'26 write-down
- **holder_established:** Y: BANK -- OZK owns via BOTO Strategic Properties IV LLC (AGENTS/OZK/workbook/KB.tsv:98)
- **contradictions:** NOTES §5 #8 carried (commit vs outstanding; 284K-320K SF; $50M vs $47.5M carrying)
- **notes:** Sponsor Sterling Bay. Implied loss UNKNOWN correct (unresolved).
- **sources_found:** ALL FOUND: AGENTS/OZK/workbook/KB.tsv:98 KB-OZK-094; AGENTS/OZK/workbook/KB.tsv:196 KB-OZK-191; AGENTS/OZK/workbook/KB.tsv:204 KB-OZK-199; AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:25
- **proposed_events:** 2021-09-14|ORIGINATED|commitment|125100000|commitment|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:25; 2025-05|APPRAISAL|~$74M (DV 59.0/0.80)|73700000|appraisal (derived)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:25; 2025-Q3|LOSS_REALIZED|charge-off|5100000|charge-off|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:25; 2025-Q4|LOSS_REALIZED|charge-off|9000000|charge-off|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:25; UNKNOWN (<=2026-03)|OTHER|short sale to Novak failed|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:98; 2026-03|REO|deed-in-lieu to BOTO Strategic Properties IV LLC|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:98; 2026-06|APPRAISAL|~$50.0M (DV 47.5/0.95)|50000000|appraisal (derived)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:25; 2026-Q2|LOSS_REALIZED|OREO write-down|2500000|write-down|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:25
**Seed row (verbatim):**
- *value_marks:* 2025-05 appraisal ~$74M; 2026-Q1 carrying $50M (68% of May-25 appraisal); 2026-06 appraisal -> ~$50.0M; 2026-06-30 carrying $47.5M; Atrium as-market $105.2M, office-conversion $45M
- *implied_loss_pct:* UNKNOWN (unresolved; carrying = 73.0% of peak outstanding, derived)
- *event_timeline:* 2021-09-14 commitment; 2025-05 appraisal; 2025-Q3 $5.1M charge-off; 2025-Q4 $9.0M charge-off; short sale to Novak Construction failed; 2026-03 deed-in-lieu; 2026-Q2 $2.5M OREO write-down on new appraisal
- *latest_status:* REO (2026-06-30)
- *trigger:* OTHER (lease-up failure)
- *holder:* Bank OZK (OREO via BOTO Strategic Properties IV LLC)
- *sources:* KB-OZK-094 (Bisnow/TRD 2026-03-20); KB-OZK-191; KB-OZK-199; REGINALD q2_OZK.md coverage line
- *source_quality:* MIXED
- *notes:* '$125M construction loan ($65M per TRD)' = commitment vs outstanding (dossier). Size 284K vs 320K SF differs across rows.

### CASE-CREED-020 — Baltimore Peninsula land (seed CASE-0019)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** charge-offs: seed $20.9M Q3'25 + $4.6M Q4'25 = $25.5M (AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:34, D) | AGENTS/OZK/workbook/KB.tsv:115 says '$66M orig -> $40M after $9.7M charge-offs' -- a THIRD figure the seed omits, and 66-9.7 != 40 (does not close); trigger MATURITY_DEFAULT: matured 12/18/25 unpaid is stated (AGENTS/OZK/workbook/KB.tsv:240, AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:33) but the $20.9M charge-off (Q3'25) PRE-DATES maturity, so maturity is the default event, not a stated cause; 212 DPD at 6/30/26 counts back to ~2025-11-30, before the 12/18 maturity -- unexplained in files
- **event_year_check:** OK: 2025-12-18 maturity per KB-OZK-235 (corrected from Boston); Q3/Q4'25 charge-offs; Jun-26 appraisal. KB-OZK-119 (dated 2026-03-24) asserts Dec-2025 DIL
- **holder_established:** Y: BANK (OZK loan, nonaccrual on OZK books per MC2)
- **contradictions:** NOTES §5 #3 carried; ADD: charge-offs $9.7M (AGENTS/OZK/workbook/KB.tsv:115, 'V3/V4; OZK disclosures') vs $25.5M (AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:34, MC3/MC4 D)
- **notes:** KB-OZK-119 predates the Q2 MC and conflicts on both status (DIL) and charge-off total; treat as superseded-candidate, not resolved here. Sponsor Goldman Sachs/Sagamore.
- **sources_found:** ALL FOUND: AGENTS/OZK/workbook/KB.tsv:115 KB-OZK-119; AGENTS/OZK/workbook/KB.tsv:240 KB-OZK-235; AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:34 (§1b); AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:33 OZK-W10
- **proposed_events:** 2025-06|APPRAISAL|~$75.3M (DV)|75300000|appraisal (derived)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:34; 2025-Q3|LOSS_REALIZED|charge-off|20900000|charge-off|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:34; 2025-Q4|LOSS_REALIZED|charge-off|4600000|charge-off|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:34; 2025-12-18|DEFAULT|matured unpaid|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:240; 2025-12|REO|deed-in-lieu (KB-OZK-119 ONLY; contradicted by Q2 MC)|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:115; 2026-06|APPRAISAL|LTV 66.7%|59700000|appraisal ($59.7-60.0M)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:34; 2026-06-30|OTHER|nonaccrual, carrying $40.0M, multi-buyer talks|40000000|carrying value|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:33
**Seed row (verbatim):**
- *value_marks:* 2025-06 appraisal ~$75.3M (derived); 2026-06 appraisal ~$59.7-60.0M (LTV 66.7%); carrying $40.0M
- *implied_loss_pct:* UNKNOWN (charge-offs $25.5M to date = 38.6% of ~$66.1M peak, derived)
- *event_timeline:* 2025-Q3 $20.9M charge-off; 2025-Q4 $4.6M charge-off; 2025-12-18 matured; 2025-12 deed-in-lieu (KB-OZK-119 only); 2026-06-30 nonaccrual, 212 days past due, talks with multiple buyers
- *latest_status:* DEFAULT (2026-06-30, nonaccrual per OZK Q2 MC)
- *trigger:* MATURITY_DEFAULT
- *holder:* Bank OZK
- *sources:* KB-OZK-119 (A2); KB-OZK-235; REGINALD q2_OZK.md §1b; OZK Q2_WORKOUT_CHECK OZK-W10
- *source_quality:* MIXED
- *notes:* CONFLICT: KB-OZK-119 says deed-in-lieu Dec-2025 and OZK owns 235 acres; the Q2-26 MC (via dossier) says nonaccrual with 'otherwise take title'. The 12/18/25 maturity was once misattributed to the Boston loan (KB-OZK-235).

### CASE-CREED-021 — 1650 Euclid Street (Santa Monica creative office) (seed CASE-0020)
**Verifier:** VERIFIED
- **field_mismatches:** none: 65K SF, 15% leased, creative office, $5.7M Q4'25 + $5.0M at transfer Q1'26, $45.1M Q1 OREO, -$0.3M Q2 (cause ND), $44.8M, $689/SF DV, 89% of Aug-25 -> $50.3M DV, broker engaged; loan amount UNKNOWN with ~$55-60M SEVEN estimate and $55.8M DV peak -- all at file
- **event_year_check:** OK: Aug-25 appraisal, Q4'25 / Q1'26 / Q2'26 events
- **holder_established:** Y: BANK (OREO at OZK)
- **contradictions:** none
- **notes:** 15% leased stated; cause of default not stated -> trigger UNKNOWN correct.
- **sources_found:** ALL FOUND: AGENTS/OZK/workbook/KB.tsv:197 KB-OZK-192; AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:26
- **proposed_events:** 2025-08|APPRAISAL|~$50.3M (DV 44.8/0.89)|50300000|appraisal (derived)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:26; 2025-Q4|LOSS_REALIZED|charge-off|5700000|charge-off|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:26; 2026-Q1|REO|transferred to OREO with charge-off|5000000|charge-off at transfer|AGENTS/OZK/workbook/KB.tsv:197; 2026-Q1|OTHER|OREO carrying|45100000|carrying value|AGENTS/OZK/workbook/KB.tsv:197; 2026-06-30|OTHER|OREO carrying (-$0.3M, cause ND)|44800000|carrying value|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:26; 2026-Q2|LISTED|broker engaged|UNKNOWN|n/a|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:26
**Seed row (verbatim):**
- *value_marks:* 2025-08 appraisal -> ~$50.3M (OREO at 89%); 2026-Q1 OREO $45.1M; 2026-06-30 $44.8M ($689/SF derived)
- *implied_loss_pct:* UNKNOWN (unresolved; carrying = 80.3% of peak, derived)
- *event_timeline:* 2025-08 appraisal; 2025-Q4 $5.7M charge-off; 2026-Q1 transferred to OREO with $5.0M charge-off; 2026-Q2 carrying -$0.3M (cause not disclosed); broker engaged
- *latest_status:* REO (2026-06-30)
- *trigger:* UNKNOWN
- *holder:* Bank OZK (OREO)
- *sources:* KB-OZK-192 (Q1-26 MC Fig 24); REGINALD q2_OZK.md coverage line
- *source_quality:* MIXED
- *notes:* (blank)

### CASE-CREED-022 — Pacific Center (seed CASE-0022)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** latest_status: seed SOLD | a loan sale = vocab NOTE_SALE (KB-OZK-199 'OZK SOLD the $265M construction loan to ... Strategic Value Partners') @AGENTS/OZK/workbook/KB.tsv:204; trigger: seed OTHER (vacancy) | files state 'largely vacant' / regional vacancy 35% but NO default or cause of sale -> UNKNOWN @AGENTS/OZK/workbook/KB.tsv:204; holder: seed 'Strategic Value Partners' is the post-sale holder -- files call SVP a 'distressed debt firm' @AGENTS/OZK/workbook/KB.tsv:157 (type DEBT_FUND, stated). All other fields match.
- **event_year_check:** OK: 2026 sale year consistent across all three rows (Jan 5 vs Jan 7 is a day conflict, not a year conflict; 1/7 is also the TRD article date)
- **holder_established:** Y (post-sale) -- SVP bought the loan, KB-OZK-031/153/199; pre-sale holder Bank OZK
- **contradictions:** Sale date 2026-01-05 (KB-OZK-031 @AGENTS/OZK/workbook/KB.tsv:36, KB-OZK-153 @AGENTS/OZK/workbook/KB.tsv:157) vs 2026-01-07 (KB-OZK-199 @AGENTS/OZK/workbook/KB.tsv:204, TRD 1/7). Size 500K SF (KB-OZK-199) vs 690K SF Phase 1 (KB-OZK-148 @AGENTS/OZK/workbook/KB.tsv:152). Seed §5 #7.
- **notes:** implied_loss 0% is on FUNDED principal per issuer (Q4-25 MC via KB-OZK-199 correction); KB-OZK-153 flags the $165M unfunded commitment and a distressed buyer ('par ... but what about $165M unfunded?') -- SVP's price is undisclosed, so the buyer's economics / any discount are UNKNOWN. KB-OZK-031 audit note: 'par claim unverified (Gap B6)'. Not a loss realization (KB-OZK-199 corrected 2026-07-06).
- **sources_found:** KB-OZK-031 FOUND @AGENTS/OZK/workbook/KB.tsv:36; KB-OZK-153 FOUND @AGENTS/OZK/workbook/KB.tsv:157; KB-OZK-199 FOUND @AGENTS/OZK/workbook/KB.tsv:204; KB-OZK-148 (cited in seed size cell) FOUND @AGENTS/OZK/workbook/KB.tsv:152
- **proposed_events:** 2026-01-05 (KB-OZK-031/153) or 2026-01-07 (KB-OZK-199)|NOTE_SALE|OZK sold $265M construction loan to Strategic Value Partners; full principal repaid on $0.10B funded per Q4-25 MC; price undisclosed|100000000|funded principal repaid (issuer claim; sale price UNDISCLOSED)|AGENTS/OZK/workbook/KB.tsv:36;AGENTS/OZK/workbook/KB.tsv:157;AGENTS/OZK/workbook/KB.tsv:204
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* 0% to OZK on funded principal (issuer: full principal repayment on $0.10B funded; no loss)
- *event_timeline:* 2026-01-05 (KB-OZK-031/153) or 2026-01-07 (KB-OZK-199, TRD 1/7) OZK sold the loan to Strategic Value Partners
- *latest_status:* SOLD (loan sale, 2026-01)
- *trigger:* OTHER (vacancy)
- *holder:* Strategic Value Partners (bought the loan)
- *sources:* KB-OZK-031; KB-OZK-153; KB-OZK-199 (corrected 2026-07-06 per Q4-25 MC)
- *source_quality:* MIXED
- *notes:* Initially read as a loss realization; corrected to a par exit on funded balance. Sale date and size differ across rows.

### CASE-CREED-023 — Concord Tech Center (seed CASE-0024)
**Verifier:** PARTIAL
- **field_mismatches:** event_timeline: seed '2026-02-10..12 foreclosure transaction' | file says 'CRE fire sales Feb 10-12 -- Nightingale tracker evidence' (row dated 2026-02-20) -- Feb 10-12 may be the tracker POST dates, not the transaction date @AGENTS/REGINALD/workbook/KB.tsv:70; state CA: file says 'Concord Tech Center CA' (supported); city: not stated (seed correctly UNKNOWN)
- **event_year_check:** UNVERIFIABLE: the file gives Feb 10-12 with no year on the transaction; the 2026 year is inferred from the row date (2026-02-20). A Nightingale 'tracker' can relay older transactions -- rule 11 check not passable from repo files
- **holder_established:** N -- no loan, lender or holder in the file
- **contradictions:** none
- **notes:** Only one line of evidence (ML-REG-068, source '@FCNightingale, auction records'), property type unknown. Seed fleet_links cell is BLANK (violates UNKNOWN-never-blank) -> set 'REGINALD ML-REG-068'. Seed notes cell BLANK -> fill. Hold until a primary (county record / trustee sale) dates the transaction.
- **sources_found:** ML-REG-068 FOUND @AGENTS/REGINALD/workbook/KB.tsv:70 (grep -rn 'ML-REG-068' AGENTS)
- **proposed_events:** ≤2026-02-20|FORECLOSURE|'$148M -> $42.25M foreclosure' (-71%); basis of $148M not stated; $42.25M may be a foreclosure-sale/credit-bid price|42250000|UNKNOWN basis (foreclosure figure)|AGENTS/REGINALD/workbook/KB.tsv:70
**Seed row (verbatim):**
- *value_marks:* $148M -> $42.25M (basis of the $148M not stated)
- *implied_loss_pct:* UNKNOWN (-71% stated vs an unstated basis)
- *event_timeline:* 2026-02-10..12 foreclosure transaction (Nightingale tracker)
- *latest_status:* FORECLOSED (2026-02)
- *trigger:* UNKNOWN
- *holder:* UNKNOWN
- *sources:* ML-REG-068 (@FCNightingale, auction records)
- *source_quality:* SECONDARY
- *notes:* (blank)

### CASE-CREED-024 — 10 Prospect Street (USQ Parcel D2.1) (seed CASE-0025)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** value_marks: seed '2025-11 appraisal -> ~$186.0M' is a REGINALD DERIVATION (169.3/0.91), not a disclosed appraisal figure @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:33 -- label DERIVED; vintage 'delivered 2024' and '194K SF, unleased' are tagged (S) secondary in the dossier @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:33 (KB-OZK-195 gives 194,033 SF NRSF from the recorded mortgage @AGENTS/OZK/workbook/KB.tsv:200); latest_status: W9 status at 6/30 = nonaccrual after forbearance expired, '$330M pending sale ... diminished assessment of the likelihood of closing' @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:33 -- seed omits the diminished-likelihood caveat. Otherwise every field found at its basis ($169.3M outstanding fully funded vs $119.2M original NOTE -- the seed keeps them distinct, correct).
- **event_year_check:** OK after correction: maturity 2026-02-13 (KB-OZK-235 @AGENTS/OZK/workbook/KB.tsv:240), NOT 2025-12-18 (that is Baltimore); UCC-1 2026-01-29 is PRE-maturity; mortgage 2020-12-31
- **holder_established:** Y -- Bank OZK secured party on UCC-1 Bk 85169 Pg 222 and mortgagee Bk 76638 Pg 224 (KB-OZK-195 @AGENTS/OZK/workbook/KB.tsv:200); OZK MC nonaccrual disclosure (W9)
- **contradictions:** §5 #1: SIG-W-20260704-004 labels the Boston $169M credit 'Cambridge Courthouse' (BOARD SIG-W-20260704-004 l.20, l.37) vs OZK desk 10 Prospect St, Somerville (KB-OZK-195 @AGENTS/OZK/workbook/KB.tsv:200). KB-OZK-189 @AGENTS/OZK/workbook/KB.tsv:194 had 808 Windsor + Dec-18-2025 maturity (both corrected by KB-OZK-195/235). REGINALD archive STATUS_apr7_apr22.md:48 still reads 'matured Dec 18 2025' (archived, uncorrected).
- **notes:** REGINALD flags the $330M = 1.77x appraisal as 'non-evidence of value' @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:33; $0 charge-off, $0 reserve at 6/30. Trigger: matured unpaid = MATURITY_DEFAULT (supported); unleased status is context, not stated cause.
- **sources_found:** KB-OZK-195 FOUND @AGENTS/OZK/workbook/KB.tsv:200; KB-OZK-235 FOUND @AGENTS/OZK/workbook/KB.tsv:240; REGINALD q2_OZK.md §1b FOUND @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:33; OZK-W9 FOUND @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:32; (KB-OZK-189 @AGENTS/OZK/workbook/KB.tsv:194 read for the §5 #1 history)
- **proposed_events:** 2020-12-31|ORIGINATED|construction mortgage, promissory note $119.2M|119200000|original note amount|AGENTS/OZK/workbook/KB.tsv:200; 2025-11|APPRAISAL|LTV 91% on $169.3M -> ~$186.0M (derived)|186000000|appraisal (DERIVED from LTV)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:33; 2026-01-29|OTHER|UCC-1 filed, OZK secured party (pre-maturity)|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:200; 2026-02-13|DEFAULT|matured unpaid; forbearance then expired|169300000|outstanding (fully funded)|AGENTS/OZK/workbook/KB.tsv:240;AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:32; ≤2026-06-30|OTHER|moved to nonaccrual, 138 DPD; $330M pending sale, buyer seeking financing|330000000|pending contract price (not closed; not reconcilable with 91% LTV)|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:32;AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:33
**Seed row (verbatim):**
- *value_marks:* 2025-11 appraisal -> ~$186.0M (LTV 91%); pending sale $330M (1.77x appraisal)
- *implied_loss_pct:* UNKNOWN ($0 charge-off, $0 reserve at 6/30)
- *event_timeline:* 2020-12-31 mortgage; 2025-11 appraisal; 2026-01-29 UCC-1 filed; 2026-02-13 matured unpaid; forbearance, then forbearance expired; 2026-Q2 moved to nonaccrual (138 days past due at 6/30); $330M sale pending, buyer seeking financing
- *latest_status:* DEFAULT (2026-06-30, nonaccrual)
- *trigger:* MATURITY_DEFAULT
- *holder:* Bank OZK
- *sources:* KB-OZK-195; KB-OZK-235; REGINALD q2_OZK.md §1b; OZK Q2_WORKOUT_CHECK OZK-W9
- *source_quality:* MIXED
- *notes:* IDENTITY CONFLICT: SIG-W-20260704-004 calls the $169M 'Cambridge Courthouse'; OZK desk names 10 Prospect; Sullivan Courthouse is a separate $156.4M credit (CASE-0027). KB-OZK-189 had named 808 Windsor/Boynton Yards and a 12/18/25 maturity, both since corrected.

### CASE-CREED-025 — The Jack (seed CASE-0026)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** charge-off basis: seed presents $27.7M as fact | dossier tags it D (MC1 p.23) @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:35 but OZK-W7 says '~$27.7M Q1 charge-off (INFERRED from the 10-Q Other Q1 charge-offs of $28.5M)' @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:30 -- tag the disclosure tier; holder: seed 'Bank OZK (debt-on-debt / note assignment)' | KB-OZK-207 says the credit was 'collateral-assigned to OZK' and sits in the Call Report 'Other' debt-on-debt category @AGENTS/OZK/workbook/KB.tsv:212 -- OZK carries a loan secured by the NOTE, so the underlying mortgage-note holder may be the originator, not OZK; balance '2024-Q4 $56.2M' is KB-OZK-193's wording ('$56.2M Q4 24') @AGENTS/OZK/workbook/KB.tsv:198 while KB-OZK-207 calls $56M the 'Atrium Q4'25 pre-charge-off' figure @AGENTS/OZK/workbook/KB.tsv:212 -- quarter of the $56.2M is inconsistent across rows
- **event_year_check:** OK: loan 2022-02, TCO 2023-06, charge-off Q1-26, LOI Q2-26 all match; the $56.2M balance quarter (Q4-24 vs Q4-25) is the one year ambiguity
- **holder_established:** PARTIAL -- OZK's exposure established (10-Q 'Other' nonaccrual $25.9M, MC 'continue as senior lender' @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:30); who holds the underlying mortgage note is NOT established (debt-on-debt/collateral assignment, KB-OZK-207 @AGENTS/OZK/workbook/KB.tsv:212)
- **contradictions:** §5 #5 originator: Mack Real Estate Credit Strategies (KB-OZK-193 @AGENTS/OZK/workbook/KB.tsv:198: 'OZK took out Mack ... original $90M construction loan') vs Claros Mortgage Trust (KB-OZK-207 @AGENTS/OZK/workbook/KB.tsv:212: 'ORIGINATED BY CLAROS ... then collateral-assigned to OZK'). Also KB-OZK-114 @AGENTS/OZK/workbook/KB.tsv:125 gives LTV 111% (older). $56.2M quarter conflict (above).
- **notes:** trigger: seed OTHER (lease-up failure) -> UNKNOWN: files state 100% vacant since delivery but no stated cause of default. If CREED adopts 'lease-up failure', it needs a vocab term.
- **sources_found:** KB-OZK-193 FOUND @AGENTS/OZK/workbook/KB.tsv:198; KB-OZK-207 FOUND @AGENTS/OZK/workbook/KB.tsv:212; KB-OZK-232 FOUND @AGENTS/OZK/workbook/KB.tsv:237; REGINALD q2_OZK.md §1b FOUND @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:35
- **proposed_events:** 2022-02|ORIGINATED|$90M construction loan (originator CONFLICT: Mack RE Credit Strategies vs Claros)|90000000|original construction loan|AGENTS/OZK/workbook/KB.tsv:198;AGENTS/OZK/workbook/KB.tsv:212; 2023-06|OTHER|TCO; 100% vacant since delivery|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:198; ≤2025-12-31|APPRAISAL|Atrium-reported appraisal $78M; Atrium value $40-45M|78000000|appraisal (as reported by Atrium)|AGENTS/OZK/workbook/KB.tsv:212; 2025-12|APPRAISAL|100% LTV on $25.9M carrying|25900000|appraisal (DERIVED from LTV)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:35; 2026-Q1|LOSS_REALIZED|$27.7M charge-off (+$2.6M sponsor paydown)|27700000|charge-off (disclosed per dossier / inferred per W7)|AGENTS/OZK/workbook/KB.tsv:198;AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:30; ≤2026-06-30|DEFAULT|nonaccrual, 149 DPD; recap LOI, close expected Q3|25900000|carrying|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:30
**Seed row (verbatim):**
- *value_marks:* Atrium Q4-25: appraisal $78M, Atrium value $40-45M; 2025-12 appraisal at 100% LTV of $25.9M carrying
- *implied_loss_pct:* UNKNOWN (charge-off $27.7M; carrying 46.1% of peak, derived)
- *event_timeline:* 2022-02 $90M construction loan; 2023-06 TCO; 2024-Q4 balance $56.2M; 2026-Q1 $27.7M charge-off + $2.6M sponsor paydown; nonaccrual (149 days past due at 6/30); 2026-Q2 recap LOI with new equity, close expected Q3
- *latest_status:* DEFAULT (2026-06-30, nonaccrual)
- *trigger:* OTHER (lease-up failure)
- *holder:* Bank OZK (debt-on-debt / note assignment)
- *sources:* KB-OZK-193; KB-OZK-207; KB-OZK-232; REGINALD q2_OZK.md §1b
- *source_quality:* MIXED
- *notes:* Originator conflict recorded as found.

### CASE-CREED-026 — Renaissance Milwaukee West (Wauwatosa hotel) (seed CASE-0027)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** value_marks: seed '~$17.4M' is REGINALD-DERIVED from 96% LTV on $16.7M @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:36 -- label DERIVED; name/opened-2020/196 keys are tagged (S) secondary in the dossier @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:36; balance fall $17.9M->$16.7M cause UNDISCLOSED @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:31 -- seed silent on cause (fine). Implied loss 20.8% = $4.7M/$22.6M peak (arithmetic checks).
- **event_year_check:** OK: charge-off Q1-26, appraisal Mar-26, contract Q2-26
- **holder_established:** Y -- Bank OZK nonaccrual loan (OZK 10-Q/MC via AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:36, AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:31)
- **contradictions:** §5 #9: same Mar-26 appraisal gives LTV 96% (Q2 MC via AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:36 and AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:31) vs 103% (REGINALD archive STATUS_apr7_apr22.md:50, Q1-vintage on the pre-paydown balance -- 103% x $17.9M ≈ $18.4M vs 96% x $16.7M ≈ $17.4M, so the two may be the same appraisal on different balances; not resolved in files)
- **notes:** Vocab: seed type 'Hotel' -> LODGING. Address UNKNOWN.
- **sources_found:** REGINALD q2_OZK.md §1b FOUND @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:36; OZK-W8 FOUND @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:31; REGINALD archive STATUS_apr7_apr22.md l.50 FOUND @AGENTS/REGINALD/archive/STATUS_apr7_apr22.md:50
- **proposed_events:** 2026-Q1|LOSS_REALIZED|$4.7M charge-off on $22.6M peak|4700000|charge-off|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:36; 2026-03|APPRAISAL|LTV 96% on $16.7M -> ~$17.4M (derived)|17400000|appraisal (DERIVED)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:36; ≤2026-06-30|OTHER|sponsor sale contract, DD done, earnest money non-refundable, close expected Q3; mgmt: proceeds >= carrying|16700000|carrying|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:31
**Seed row (verbatim):**
- *value_marks:* 2026-03 appraisal: LTV 96% (-> ~$17.4M); archived REGINALD STATUS says 103%
- *implied_loss_pct:* UNKNOWN (charge-off $4.7M = 20.8% of peak, derived; mgmt says proceeds >= carrying)
- *event_timeline:* 2026-Q1 $4.7M charge-off; balance $17.9M (Q1) -> $16.7M (Q2); 169 days past due at 6/30; sponsor sale contract, earnest money non-refundable, close expected Q3
- *latest_status:* DEFAULT (2026-06-30, nonaccrual; sale contract pending)
- *trigger:* UNKNOWN
- *holder:* Bank OZK
- *sources:* REGINALD q2_OZK.md §1b; OZK Q2_WORKOUT_CHECK OZK-W8; REGINALD/archive/STATUS_apr7_apr22.md l.50
- *source_quality:* MIXED
- *notes:* LTV 96% vs 103% for the same Mar-26 appraisal across files.

### CASE-CREED-027 — Sullivan Courthouse (seed CASE-0028)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** notes: seed says 'See CASE-0024 note on the Cambridge Courthouse label' | the label note is on CASE-0025 (10 Prospect), not CASE-0024 (Concord Tech Center) -- wrong cross-reference; size 422K SF and $156.4M o/s at 3/31/26 found @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:19 (KB-OZK-231 gives $156.4M without the 3/31 date @AGENTS/OZK/workbook/KB.tsv:236). All other fields found.
- **event_year_check:** OK: 3/31/26 substandard nonaccrual; Q2-26 recap. The pre-2026 charge-off is undated and unsized in files
- **holder_established:** Y -- Bank OZK (MC p.22 via AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:19); new pass-rated loan amount UNDISCLOSED
- **contradictions:** §5 #1: SIG-W-20260704-004 applies 'Cambridge Courthouse' to the $169M Boston life-sci credit; Sullivan Courthouse (Cambridge) is the separate $156.4M office credit (KB-OZK-231).
- **notes:** Address, vintage, tenant UNKNOWN in files. Retained exposure after recap 'likely most or all of $156.4M but NOT disclosed' (W1).
- **sources_found:** KB-OZK-231 FOUND @AGENTS/OZK/workbook/KB.tsv:236; OZK-W1 FOUND @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:19
- **proposed_events:** ≤2025-12-31|LOSS_REALIZED|pre-2026 charge-off ('post-charge-off' per SEVEN_CREDIT l.194); amount not located|UNKNOWN|charge-off|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:19; 2026-03-31|DEFAULT|largest substandard nonaccrual|156400000|outstanding|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:19; 2026-Q2|MODIFICATION|recapitalized by sponsor + new capital partner into a new pass-rated loan (amount UNDISCLOSED)|UNKNOWN|n/a|AGENTS/OZK/workbook/KB.tsv:236;AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:19
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* pre-2026 charge-off (amount not located); 2026-03-31 substandard nonaccrual (largest); 2026-Q2 recapitalized by sponsor + new capital partner into a new pass-rated loan
- *latest_status:* MODIFIED (2026-06-30, recapitalized to pass)
- *trigger:* UNKNOWN
- *holder:* Bank OZK
- *sources:* KB-OZK-231; OZK Q2_WORKOUT_CHECK OZK-W1 (Q2 MC p.22)
- *source_quality:* MIXED
- *notes:* See CASE-0024 note on the 'Cambridge Courthouse' label in SIG-W-20260704-004.

### CASE-CREED-028 — Chapter Building I (seed CASE-0029)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** value_marks: seed 'Q1-26 as-stabilized ~$128.8M (derived)' is REGINALD's 106.9/0.83 @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:22, which assumes the 83% LTV is on the $106.9M COMMITMENT; KB-OZK-190 attaches '83% LTV' to the $76.4M OUTSTANDING @AGENTS/OZK/workbook/KB.tsv:195 (on that basis value ≈ $92.0M) -- basis UNRESOLVED, do not carry $128.8M as a value; value_marks: 'recorded assignment value $78.4M' (SIG l.29) coincides with REGINALD's DERIVED peak outstanding ~$78.4M @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:22 -- two different objects with the same figure, keep them labelled; vintage: dossier adds ~2024 delivery (S, SEVEN §6) @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:22 (seed omits; fine); trigger: seed OTHER (LP exit) -- file states cause (KB-OZK-190: Ameriprise exiting, divesting Lionstone; 'NOT sponsor distress') then buyer withdrew (MC)
- **event_year_check:** OK: 2022 financing; 3/31/26 substandard accrual; Q2-26 foreclosure/assignment; recorded week ending 2026-07-02 (2026 confirmed)
- **holder_established:** Y -- Bank OZK (MC; SIG: OZK took title) -> now OREO $56.1M @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:21
- **contradictions:** §5 #6: disposition = ground-lease assignment-in-lieu recorded by King County week ending 2026-07-02 (SIG-W-20260704-004 l.17, l.28) vs 'foreclosed June 2026' (OZK MC via AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:21-22). $196.2M (SIG) = 2022 total of $106.9M + $89.3M commitments; KB-OZK-114 @AGENTS/OZK/workbook/KB.tsv:125 lists 'Chapter Building: $106.9M' as one figure. NEW: KB-CREED-015 @AGENTS/CREED/workbook/KB.tsv:20 reads 'Seattle U-District charge-offs ($22.3M + $3.7M + $8.5M, foreclosed Jun-26)' -- the $8.5M is the ATLANTA office (OZK-W5 @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23), not Seattle; a CREED-KB mis-attribution.
- **notes:** Size 12 stories / ~240K SF (SIG l.29) supported. Implied loss not a severity: carrying/peak 71.6% is DERIVED on a DERIVED peak; the sale has not happened.
- **sources_found:** SIG-W-20260704-004 FOUND @BOARD/SIG-W-20260704-004-bank-ozk-deed-in-lieu-seattle-chapter-buildings-u-district-loi-recap-realized.md (l.17, l.29-34); KB-OZK-190 FOUND @AGENTS/OZK/workbook/KB.tsv:195; KB-OZK-231 FOUND @AGENTS/OZK/workbook/KB.tsv:236; KB-CREED-015 FOUND @AGENTS/CREED/workbook/KB.tsv:20; REGINALD q2_OZK.md FOUND @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:22-23; (OZK-W3/W4 @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:21-22 also read)
- **proposed_events:** 2022|ORIGINATED|$106.9M commitment (part of $196.2M Bldg I+II construction financing, CBRE-arranged, OZK-led)|106900000|commitment|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:22;BOARD/SIG-W-20260704-004 l.17; 2026-01|APPRAISAL|as-is; OREO at 95% -> ~$59.1M (derived)|59100000|appraisal (DERIVED)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:22; 2026-03-31|OTHER|substandard accrual $76.4M, 83% LTV, signed LOI for recap|76400000|outstanding|AGENTS/OZK/workbook/KB.tsv:195; 2026-Q2|LOSS_REALIZED|buyer withdrew -> nonaccrual -> $22.3M charge-off|22300000|charge-off|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:21; 2026-06 (MC) / recorded wk ending 2026-07-02 (SIG)|REO|foreclosed (MC) / ground-lease assignment-in-lieu recorded (SIG), assignment value $78.4M; OREO $56.1M|56100000|OREO carrying|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:21;BOARD/SIG-W-20260704-004 l.29
**Seed row (verbatim):**
- *value_marks:* Q1-26 as-stabilized ~$128.8M (derived); recorded assignment value $78.4M; 2026-01 as-is appraisal -> ~$59.1M; OREO $56.1M (95% of it; $234/SF derived)
- *implied_loss_pct:* UNKNOWN (charge-off to date $22.3M; carrying = 71.6% of peak, derived)
- *event_timeline:* 2022 construction financing; 2026-03-31 substandard accrual, LOI for recap; 2026-Q2 buyer withdrew, nonaccrual, $22.3M charge-off; 2026-06 foreclosed (OZK MC); King County recorded ground-lease assignment-in-lieu week ending 2026-07-02
- *latest_status:* REO (2026-06-30)
- *trigger:* OTHER (LP exit: Ameriprise divesting Lionstone's book; buyer withdrew)
- *holder:* Bank OZK (OREO)
- *sources:* SIG-W-20260704-004 (verify CONFIRMED-with-CORRECTED-FRAMING 0.85); KB-OZK-190; KB-OZK-231; KB-CREED-015; REGINALD q2_OZK.md coverage line
- *source_quality:* MIXED
- *notes:* BOARD signal treats Bldgs I+II as one event (current exposure ~$126M; $196.2M = 2022 origination). Deed-in-lieu (SIG) vs 'foreclosed June' (MC) wording differs.

### CASE-CREED-029 — Chapter Building II (seed CASE-0030)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** value_marks: '2025-12 as-is appraisal -> ~$51.1M' is REGINALD-DERIVED (48.5/0.95) @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:23 -- label DERIVED; Atrium as-market $115M / office-conversion $58M are Atrium MODEL values (ATR via AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:23), a different basis from the as-is appraisal; deed of trust 2022-06-30 is from ATR via the dossier, not the SIG @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:23; trigger: as CASE-0029 (file cause LP exit, KB-OZK-190 @AGENTS/OZK/workbook/KB.tsv:195)
- **event_year_check:** OK: deed of trust 2022-06-30; 3/31/26; Q2-26 foreclosure; recorded week ending 2026-07-02
- **holder_established:** Y -- Bank OZK -> OREO $48.5M @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:22
- **contradictions:** §5 #6: disposition = ground-lease assignment-in-lieu recorded by King County week ending 2026-07-02 (SIG-W-20260704-004 l.17, l.28) vs 'foreclosed June 2026' (OZK MC via AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:21-22). $196.2M (SIG) = 2022 total of $106.9M + $89.3M commitments; KB-OZK-114 @AGENTS/OZK/workbook/KB.tsv:125 lists 'Chapter Building: $106.9M' as one figure. NEW: KB-CREED-015 @AGENTS/CREED/workbook/KB.tsv:20 reads 'Seattle U-District charge-offs ($22.3M + $3.7M + $8.5M, foreclosed Jun-26)' -- the $8.5M is the ATLANTA office (OZK-W5 @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23), not Seattle; a CREED-KB mis-attribution. Size ~154K SF (SIG l.30) vs 149K SF (dossier @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:23).
- **notes:** Type: seed 'Life science / R&D + retail' -> LIFE_SCIENCE.
- **sources_found:** SIG-W-20260704-004 FOUND @BOARD/SIG-W-20260704-004-bank-ozk-deed-in-lieu-seattle-chapter-buildings-u-district-loi-recap-realized.md (l.17, l.29-34); KB-OZK-190 FOUND @AGENTS/OZK/workbook/KB.tsv:195; KB-OZK-231 FOUND @AGENTS/OZK/workbook/KB.tsv:236; KB-CREED-015 FOUND @AGENTS/CREED/workbook/KB.tsv:20; REGINALD q2_OZK.md FOUND @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:22-23; (OZK-W3/W4 @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:21-22 also read)
- **proposed_events:** 2022-06-30|ORIGINATED|deed of trust; $89.3M commitment|89300000|commitment|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:23; 2025-12|APPRAISAL|as-is; OREO at 95% -> ~$51.1M (derived)|51100000|appraisal (DERIVED)|AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:23; 2026-03-31|OTHER|substandard accrual $50.4M, 73% LTV, recap LOI|50400000|outstanding|AGENTS/OZK/workbook/KB.tsv:195; 2026-Q2|LOSS_REALIZED|nonaccrual -> $3.7M charge-off|3700000|charge-off|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:22; 2026-06 (MC) / recorded wk ending 2026-07-02 (SIG)|REO|foreclosed / assignment-in-lieu; OREO $48.5M|48500000|OREO carrying|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:22;BOARD/SIG-W-20260704-004 l.30
**Seed row (verbatim):**
- *value_marks:* 2025-12 as-is appraisal -> ~$51.1M; OREO $48.5M (95%; $326/SF derived); Atrium as-market $115M, office-conversion $58M
- *implied_loss_pct:* UNKNOWN (charge-off $3.7M; carrying = 92.9% of peak, derived)
- *event_timeline:* 2022-06-30 deed of trust; 2026-03-31 substandard accrual; 2026-Q2 nonaccrual, $3.7M charge-off; 2026-06 foreclosed / assignment-in-lieu recorded week ending 2026-07-02
- *latest_status:* REO (2026-06-30)
- *trigger:* OTHER (LP exit; buyer withdrew)
- *holder:* Bank OZK (OREO)
- *sources:* SIG-W-20260704-004 (verify CONFIRMED-with-CORRECTED-FRAMING 0.85); KB-OZK-190; KB-OZK-231; KB-CREED-015; REGINALD q2_OZK.md coverage line
- *source_quality:* MIXED
- *notes:* Size differs 154K vs 149K SF across files.

### CASE-CREED-030 — 1050 Brickworks (Atlanta office) (seed CASE-0031)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** identity: the NAME '1050 Brickworks' and '$85.5M' come only from Connect CRE (secondary) via CATCHUP_SWEEP.md:137 / AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:27; the OZK filings (KB-OZK-231, W5) say only 'Atlanta office' -- the match is REGINALD's attribution, not a filing; loan_amount: seed '$85.5M' basis unknown (commitment vs outstanding) | peak OUTSTANDING is $45.1M DERIVED (36.6+8.5) @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:27, @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23 -- the 42.8% ratio divides carrying by a figure on a different (likely commitment) basis; disposition: seed '2026-06 foreclosed' | Connect CRE says 'deed-in-lieu to OZK' @AGENTS/OZK/research/threads/2026-09-24_CATCHUP_SWEEP.md:137
- **event_year_check:** OK: SM at 3/31/26; foreclosed June 2026; Connect CRE week of 7/16/26
- **holder_established:** Y -- Bank OZK -> OREO $36.6M @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23
- **contradictions:** Foreclosed (MC, AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23) vs deed-in-lieu (Connect CRE, CATCHUP_SWEEP.md:137) -- same wording split as §5 #6 Chapter. KB-CREED-015 @AGENTS/CREED/workbook/KB.tsv:20 files this $8.5M charge-off under 'Seattle U-District'.
- **notes:** Size, vintage UNKNOWN. Sponsor Sterling Bay (Connect CRE via CATCHUP_SWEEP:137).
- **sources_found:** KB-OZK-231 FOUND @AGENTS/OZK/workbook/KB.tsv:236 (unnamed 'NEW Atlanta office'); REGINALD q2_OZK.md FOUND @AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:27 (names it, citing OZK/research/threads/2026-09-24_CATCHUP_SWEEP.md:137); OZK-W5 FOUND @AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23 (unnamed); CATCHUP_SWEEP l.137 read as the underlying press cite
- **proposed_events:** 2026-03-31|OTHER|special mention|UNKNOWN|n/a|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23; ≤2026-06-30|DEFAULT|sponsor marketing failed; loan matured with no further sponsor support; nonaccrual|45100000|peak outstanding (DERIVED)|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23; 2026-Q2|LOSS_REALIZED|$8.5M charge-off|8500000|charge-off|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23; 2026-06|APPRAISAL|as-is appraisal|36600000|appraisal (as-is)|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23; 2026-06|REO|foreclosed (MC) / deed-in-lieu (Connect CRE); OREO at 100% of appraisal|36600000|OREO carrying|AGENTS/OZK/research/threads/2026-09-27_Q2_WORKOUT_CHECK_OZK.md:23;AGENTS/OZK/research/threads/2026-09-24_CATCHUP_SWEEP.md:137
**Seed row (verbatim):**
- *value_marks:* 2026-06 as-is appraisal $36.6M; OREO $36.6M (100%)
- *implied_loss_pct:* UNKNOWN (carrying = 42.8% of the $85.5M loan and 81.2% of peak outstanding, derived)
- *event_timeline:* 2026-03-31 special mention; sponsor marketing failed, loan matured without further support; 2026-Q2 nonaccrual, $8.5M charge-off; 2026-06 foreclosed
- *latest_status:* REO (2026-06-30)
- *trigger:* MATURITY_DEFAULT
- *holder:* Bank OZK (OREO)
- *sources:* KB-OZK-231; REGINALD q2_OZK.md coverage line; OZK Q2_WORKOUT_CHECK OZK-W5
- *source_quality:* MIXED
- *notes:* (blank)

### CASE-CREED-031 — 1 South Wacker (seed CASE-0032)
**Verifier:** VERIFIED
- **field_mismatches:** none -- $343M, ~$159M CMBS / rest balance sheet, 73% occupied, 40 stories/1.2M sf, built 1982 (-012 l.44), BXMT originated 2018 (-012 l.45), maturity default 6/9, SS transfer not confirmed (-004 l.31) all found. Minor: purchase '2018-19' (-004 l.23) vs '2018' (-012 l.23, l.44)
- **event_year_check:** OK: default 2026-06-09 (matured 6/9, reported 6/24); origination 2018
- **holder_established:** PARTIAL -- BXMT holds the balance-sheet portion (BXMT: '<2% of our portfolio, on our watchlist since 2022', -012 l.41); ~$159M in CMBS, trust name and type NOT in files
- **contradictions:** Purchase year 2018-19 (-004) vs 2018 (-012). CREED THESIS l.39 lists 1 S Wacker implicitly via 601W; no conflict on facts.
- **notes:** Blackstone = LENDER (BXMT), not owner (verify CORRECTED-FRAMING 0.85). No appraisal published as of 6/24 (-004 l.32). BXMT '<2% of portfolio' is BXMT's own framing.
- **sources_found:** SIG-W-20260624-004 FOUND @BOARD/SIG-W-20260624-004-blackstone-bxmt-1-south-wacker-343m-loan-maturity-default-chicago-office.md (l.23, l.30-32); SIG-W-20260626-012 FOUND @BOARD/SIG-W-20260626-012-601w-chicago-office-distress-aon-center-58pct-bxmt-default.md (l.23, l.44-45)
- **proposed_events:** 2018|ORIGINATED|BXMT $343M loan; ~$159M securitized in CMBS|343000000|original loan|BOARD/SIG-W-20260626-012 l.45; 2018-2019|ACQUIRED|601W Companies ~$310M|310000000|purchase price|BOARD/SIG-W-20260624-004 l.23; 2026-06-09|DEFAULT|maturity default, principal not repaid|343000000|loan amount (balance at maturity not stated)|BOARD/SIG-W-20260624-004 l.31
**Seed row (verbatim):**
- *value_marks:* 2018-19 purchase ~$310M; no appraisal published (as of 2026-06-24)
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2018-2019 601W Companies bought for ~$310M; 2018 BXMT originated loan; 2022 on BXMT watchlist; 2026-06-09 maturity default
- *latest_status:* DEFAULT (2026-06-09; special-servicing transfer not confirmed)
- *trigger:* MATURITY_DEFAULT
- *holder:* BXMT (balance-sheet portion) + CMBS trust (name UNKNOWN)
- *sources:* SIG-W-20260624-004 (verify CORRECTED-FRAMING 0.85: Crain's, TRD, Bloomberg); SIG-W-20260626-012
- *source_quality:* MIXED
- *notes:* Blackstone is the lender (BXMT), not the owner. BXMT: <2% of portfolio.

### CASE-CREED-032 — Aon Center (seed CASE-0033)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** value_marks: seed '2018 value $780M' -- basis of the $780M is not stated (the SIG says 'DOWN 58% from $780M when 601W refinanced/CMBS'd it in 2018', l.23) -> write 'basis UNKNOWN (2018 refi-era value)'; holder: seed 'CMBS investors (2018; trust name UNKNOWN)' matches l.30 'sold to CMBS investors in 2018'; appraisal date not stated (reported 6/24 via Nightingale, Crain's)
- **event_year_check:** OK for 2018; appraisal year not stated -- only its report date (2026-06-24). Not checkable as 2026 from files
- **holder_established:** PARTIAL -- 'sold to CMBS investors in 2018' (-012 l.30); conduit vs SASB and deal name NOT in files
- **contradictions:** §5 #13: BOARD SIG-W-20260626-012 l.23 'outcome uncertain' vs CREED THESIS.md:222 and FLOW.tsv:10 (7/27) 'Aon + Seattle recaps FAILED' with no Aon source cited. THESIS.md:39 carries it correctly ('601W seeking another extension').
- **notes:** Seed says 'another' extension -> prior extension(s) exist but are undated in files. Implied 62% = appraisal/senior loan (330.5/536), NOT a loss. 66% leased, 2.7M SF, built 1972 all found.
- **sources_found:** SIG-W-20260626-012 FOUND @BOARD/SIG-W-20260626-012-601w-chicago-office-distress-aon-center-58pct-bxmt-default.md (l.23, l.30, l.44); CREED THESIS.md l.222 FOUND @AGENTS/CREED/thesis/THESIS.md:222; FLOW-CREED-05 FOUND @AGENTS/CREED/workbook/FLOW.tsv:10
- **proposed_events:** 2018|ORIGINATED|601W refinanced; $536M senior loan sold to CMBS investors; value $780M (basis unstated)|536000000|senior loan (total debt UNKNOWN)|BOARD/SIG-W-20260626-012 l.23,l.30; ≤2026-06-24|APPRAISAL|$330.5M (-58% vs $780M)|330500000|appraisal|BOARD/SIG-W-20260626-012 l.44; ≤2026-06-24|OTHER|601W formally requests another 3-yr extension on the senior loan; outcome uncertain (Crain's)|UNKNOWN|n/a|BOARD/SIG-W-20260626-012 l.23
**Seed row (verbatim):**
- *value_marks:* 2018 value $780M; appraisal $330.5M (date not stated, reported 2026-06-24; -58%)
- *implied_loss_pct:* UNKNOWN (appraisal = 62% of the senior loan; no resolution)
- *event_timeline:* 2018 601W refinanced/CMBS'd; 2026-06-24 (reported) appraisal $330.5M and 601W request for another 3-year extension
- *latest_status:* UNKNOWN (extension outcome not in files; 2026-06-24)
- *trigger:* UNKNOWN (extension request on senior loan; default not stated)
- *holder:* CMBS investors (2018; trust name UNKNOWN)
- *sources:* SIG-W-20260626-012 (Crain's via @FCNightingale); CREED/thesis/THESIS.md l.222; CREED/workbook/FLOW.tsv FLOW-CREED-05
- *source_quality:* SECONDARY
- *notes:* CREED THESIS/FLOW (7/27) say 'Aon + Seattle recaps FAILED' with no Aon source cited; the BOARD signal says outcome uncertain.

### CASE-CREED-033 — 75 West Apartments (seed CASE-0035)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** holder: seed 'Ares Management (lender of record not confirmed)' | the file only says Ares 'provided the loan in 2022' (originator); lender-of-record is explicitly unconfirmed (l.33 'Confirm the lender-of-record') -> holder UNKNOWN per README rule 6; loan amount: '$90M' -- whether full cap stack or a senior piece is an open question in the file (l.30) -> mark basis UNKNOWN
- **event_year_check:** OK: 2022 loan, built 2000, foreclosure reported 6/26/26 (TRD via Nightingale 8:48 PM 6/26)
- **holder_established:** N -- originator Ares only; lender of record unconfirmed (l.33)
- **contradictions:** none
- **notes:** MULTIFAMILY = HOMER's domain (README rule 10); grep of AGENTS/HOMER finds no 75 West record -- adopt only with a HOMER link/ack. Single-source, 'allegedly'. Seed fleet_links 'CREED S5' -- S5 is HOMER-owned (CREED CLAUDE.md Route Matrix).
- **sources_found:** SIG-W-20260627-001 FOUND @BOARD/SIG-W-20260627-001-blackstone-north-dallas-75-west-apartments-90m-foreclosure-ares-lender.md (l.23, l.39)
- **proposed_events:** 2022|ORIGINATED|Ares Management loan, ~$184K/unit|90000000|loan amount (senior vs full stack UNKNOWN)|BOARD/SIG-W-20260627-001 l.39; ≤2026-06-26|DEFAULT|Blackstone (equity sponsor/borrower) allegedly defaulted; foreclosure reported|UNKNOWN|n/a|BOARD/SIG-W-20260627-001 l.23
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2022 Ares loan; 2026-06-26 (reported) foreclosure on alleged default
- *latest_status:* DEFAULT (2026-06-26; foreclosure reported, filing not verified)
- *trigger:* UNKNOWN
- *holder:* Ares Management (lender of record not confirmed)
- *sources:* SIG-W-20260627-001 (TheRealDeal via @FCNightingale, single-source, 'allegedly')
- *source_quality:* SECONDARY
- *notes:* (blank)

### CASE-CREED-034 — 205 West Randolph Street (seed CASE-0036)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** implied_loss_pct: seed '73% ($12.2M loss / $16.7M loan)' | the file gives '$16.7M' as the CMBS loan with no basis (original vs balance at disposition) @SIG l.5; KB-CREED-041's severity basis is 'vs balance before disposition' @KB.tsv:46 -- the 73% is on an UNSTATED basis, so it belongs in notes as UNRECONCILED per README rule 5 until the COMM 2015-CR22 remit is read; vintage 'CMBS 2015' is the deal-name year, not a stated origination year
- **event_year_check:** UNVERIFIED: sale/liquidation DATE is not in the file -- only the post date (Nightingale 6/28/26). The liquidation could predate 2026 (rule 11 risk)
- **holder_established:** Y -- COMM 2015-CR22 named (SIG l.5); conduit type not stated in files
- **contradictions:** none
- **notes:** Single-source (@FCNightingale/connectCRE), 'UNVERIFIED against the trust remit' (SIG l.16). -72% is vs 2017 purchase price, a different basis from loss-on-loan (KB-CREED-041 basis note).
- **sources_found:** SIG-W-20260702-018 FOUND @BOARD/SIG-W-20260702-018-205-w-randolph-chicago-cmbs-12-2m-realized-loss-72pct-haircut.md (l.5, l.24); KB-CREED-041 FOUND @AGENTS/CREED/workbook/KB.tsv:46
- **proposed_events:** 2017|ACQUIRED|purchase $28.7M|28700000|purchase price|BOARD/SIG-W-20260702-018 l.5; ≤2026-06-28|SALE|sold for just under $8.0M (-72% vs 2017 price)|8000000|sale price|BOARD/SIG-W-20260702-018 l.5; ≤2026-06-28|LOSS_REALIZED|CMBS loan liquidated, $12.2M loss; $3.5M expenses|12200000|realized loss (vs $16.7M loan, basis UNSTATED)|BOARD/SIG-W-20260702-018 l.5
**Seed row (verbatim):**
- *value_marks:* 2017 purchase $28.7M; sale just under $8.0M (72% below 2017 price); CMBS loss $12.2M; expenses $3.5M
- *implied_loss_pct:* 73% ($12.2M loss / $16.7M loan, from source figures)
- *event_timeline:* 2017 purchased for $28.7M; UNKNOWN date loan liquidated and property sold (reported 2026-06-28)
- *latest_status:* SOLD (reported 2026-06-28)
- *trigger:* UNKNOWN
- *holder:* COMM 2015-CR22
- *sources:* SIG-W-20260702-018 (@FCNightingale / connectCRE, single-source, unverified vs remit); KB-CREED-041 basis note
- *source_quality:* SECONDARY
- *notes:* The -72% is vs the 2017 purchase price, a different basis from loss-on-loan (CREED).

### CASE-CREED-035 — Yorktown Center (seed CASE-0037)
**Verifier:** VERIFIED
- **field_mismatches:** none -- $120.5M CMBS, 787,389 sf regional mall, Lombard IL, SS transfer for maturity default all found. Note: the 7/20 date is the TreppWire alert date; transfer date ≤ it
- **event_year_check:** OK: 2026-07-20 (alert date)
- **holder_established:** PARTIAL -- 'CMBS loan' (Trepp alert); trust name and conduit/SASB not in files
- **contradictions:** none
- **notes:** REFRESH_2026-07-27.md:208 classes it a B-mall. Street address not written in files (WALTER mapped 'Yorktown Center per the address').
- **sources_found:** SIG-W-20260721-007 FOUND @BOARD/SIG-W-20260721-007-trepp-lombard-il-yorktown-mall-120-5m-cmbs-special-servicing-maturity-default.md (l.20-28); KB-CREED-012 FOUND @AGENTS/CREED/workbook/KB.tsv:17
- **proposed_events:** ≤2026-07-20|TRANSFER_SS|maturity default -> special servicing (TreppWire alert, McNamara repost)|120500000|loan amount|BOARD/SIG-W-20260721-007 l.22
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2026-07-20 transferred to special servicing for maturity default
- *latest_status:* SPECIAL_SERVICING (2026-07-20)
- *trigger:* MATURITY_DEFAULT
- *holder:* CMBS trust (name UNKNOWN)
- *sources:* SIG-W-20260721-007 (TreppWire alert via McNamara repost); KB-CREED-012
- *source_quality:* SECONDARY
- *notes:* (blank)

### CASE-CREED-036 — Sangertown Square (seed CASE-0038)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** event_timeline: seed '2026-07-27 special-servicing transfer' | 7/27 is the crenews ARTICLE date ('crenews carries Sangertown at $49.33M, dated 7/27 -- a formal SS-transfer confirmation of what was a Nightingale post on 7/21') @REFRESH:212 -> transfer event_date ≤2026-07-27 (possibly ≤2026-07-21), reported 2026-07-27
- **event_year_check:** OK on 2026; day is a report date, not the transfer date
- **holder_established:** N -- no trust named; 'CMBS' not explicitly stated for Sangertown in KB-CREED-012 (listed among 'mall CMBS special-servicing transfers')
- **contradictions:** none
- **notes:** Article bodies paywalled (KB-CREED-012 source cell). Trigger: an extension blocked at a DSCR hurdle is a maturity/extension failure (KB-CREED-012 'maturity/extension failures, not term or NOI stress') -> MATURITY_DEFAULT supported.
- **sources_found:** KB-CREED-012 FOUND @AGENTS/CREED/workbook/KB.tsv:17; REFRESH_2026-07-27.md l.210-212 FOUND @AGENTS/CREED/research/REFRESH_2026-07-27.md:210,212
- **proposed_events:** UNKNOWN|EXTENSION|two prior extensions (dates not in files)|UNKNOWN|n/a|AGENTS/CREED/workbook/KB.tsv:17; ≤2026-07-27|TRANSFER_SS|DSCR-hurdle failure blocked a 3rd extension|49330000|loan amount|AGENTS/CREED/workbook/KB.tsv:17;AGENTS/CREED/research/REFRESH_2026-07-27.md:210
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* two prior extensions (dates not stated); 2026-07-21 Nightingale post; 2026-07-27 special-servicing transfer after a DSCR-hurdle failure blocked a 3rd extension (crenews)
- *latest_status:* SPECIAL_SERVICING (2026-07-27)
- *trigger:* MATURITY_DEFAULT
- *holder:* CMBS trust (name UNKNOWN)
- *sources:* KB-CREED-012 (crenews 2026-07-27, body paywalled); CREED/research/REFRESH_2026-07-27.md l.210-212
- *source_quality:* SECONDARY
- *notes:* (blank)

### CASE-CREED-037 — Meadows Mall (seed CASE-0039)
**Verifier:** VERIFIED
- **field_mismatches:** none -- $100.4M CMBS, SS at maturity, Midland, JPMBB 2013-C14/2014-C18 split all found. 'CMBS 2013/2014' is a deal-name vintage (KB-CREED-013: '2013/2014-vintage conduit loan reaching scheduled maturity')
- **event_year_check:** OK: crenews 2026-07-22 (report date; transfer ≤ it)
- **holder_established:** Y -- JPMBB 2013-C14 / 2014-C18 split; KB-CREED-013 @KB.tsv:18 calls it a conduit loan
- **contradictions:** 'class-A mall' (SIG-W-20260723-016 l.22, crenews/WALTER) vs CREED KB-CREED-013 @KB.tsv:18: class-A broadening read NOT supportable (scheduled maturity of a 2013/14 conduit loan). Seed carries both.
- **notes:** Occupancy/value/DSCR paywalled (SIG l.22).
- **sources_found:** SIG-W-20260723-016 FOUND @BOARD/SIG-W-20260723-016-q2-regionals-credit-mosaic-efsc-mcb-idiosyncratic-blowups-vs-cohort-improvement.md:22; KB-CREED-012 FOUND @AGENTS/CREED/workbook/KB.tsv:17; (KB-CREED-013 @KB.tsv:18 read for the conduit/vintage statement)
- **proposed_events:** ≤2026-07-22|TRANSFER_SS|at maturity; special servicer Midland|100400000|loan amount|BOARD/SIG-W-20260723-016 l.22;AGENTS/CREED/workbook/KB.tsv:17
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2026-07-22 transferred to special servicing at maturity
- *latest_status:* SPECIAL_SERVICING (2026-07-22)
- *trigger:* MATURITY_DEFAULT
- *holder:* JPMBB 2013-C14 / JPMBB 2014-C18 (split)
- *sources:* SIG-W-20260723-016 (crenews 2026-07-22); KB-CREED-012
- *source_quality:* SECONDARY
- *notes:* Called 'class-A' by crenews/REGINALD; CREED rules the class-A broadening read NOT supportable (scheduled maturity of a 2013/14 conduit loan).

### CASE-CREED-038 — 6810 Mannheim Road (dual-brand O'Hare hotel) (seed CASE-0040)
**Verifier:** VERIFIED
- **field_mismatches:** none vs source -- but '$25M' is the headline's 'foreclosure' figure; whether it is loan amount, judgment or claim is unread (body not loaded, l.29) -> value basis UNKNOWN
- **event_year_check:** OK: TRD Chicago 2026-07-23 (report date); default date not stated
- **holder_established:** N -- lender identity unread (l.29)
- **contradictions:** none
- **notes:** HEADLINE-ONLY, confidence 0.60, no action recipient; WALTER itself says 'Not evidence for the CRE thesis' (construction loan, completed hotel, foreign-retail equity) (l.46). Headline says 'hotels' (plural) at one address -- one dual-brand property. Lowest-priority adoption.
- **sources_found:** SIG-W-20260725-007 FOUND @BOARD/SIG-W-20260725-007-ohare-dual-brand-hotel-25m-foreclosure-eb5-construction-loan-default.md (l.4-5, l.27-29)
- **proposed_events:** ≤2026-07-23|DEFAULT|EB-5-seeking investor allegedly defaulted on construction loan; lender and 'little-known foreign entity' locked in $25M foreclosure|25000000|UNKNOWN (headline 'foreclosure' figure)|BOARD/SIG-W-20260725-007 l.27
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2026-07-23 (reported) foreclosure on alleged construction-loan default; EB-5-seeking investor
- *latest_status:* DEFAULT (2026-07-23; foreclosure reported)
- *trigger:* UNKNOWN (alleged construction-loan default)
- *holder:* UNKNOWN
- *sources:* SIG-W-20260725-007 (TRD Chicago 2026-07-23; headline/subhead/caption only)
- *source_quality:* SECONDARY
- *notes:* Body unread; lender and borrower identities unread.

### CASE-CREED-039 — Project James (seed CASE-0041)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** holder: seed says 'CMBS (trust not named)' | Trepp SS says loan 'makes up the entirety of the BSREP 2021-DC deal, structured as a $354.5 million component and a $23.1 million freely prepayable piece' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col2 · state: seed says DC/VA | SS says only 'eight office buildings in the greater Washington, DC area' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout); VA appears only for an UNNAMED 'Washington, D.C. and Northern Virginia office portfolio' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Delinquency_Report.pdf p.2 · tenant_or_occupancy: seed UNKNOWN | SS: 'The August hard maturities report had singled the loan out for eroding occupancy'; DSCR (NCF) 1.30x @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col2 · status detail: SS says 'non-performing, matured balloon status after failing to pay off at its August maturity' (seed SPECIAL_SERVICING is right; add NPMB) · fleet_links: seed 'EGBN (DC lender, REGINALD)' | AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:126 frames it as 'EGBN x DC office (Project James overlap)' = a METRO-overlap ask to REGINALD, not an EGBN lender/holder link · loan $377.6M = total of $354.5M + $23.1M components (matches)
- **event_year_check:** PASS: August 2026 maturity and transfer (Aug-2026 report; pub 2026-09-14). Exact maturity DAY not given for this loan (the 'August 9' date in the SS text belongs to BXHPP 2021-FILM, not Project James)
- **holder_established:** Y — BSREP 2021-DC SASB trust named @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) (seed cited files do not name it; the archived PDF does)
- **contradictions:** Possible identity with the UNNAMED 'Washington, D.C. and Northern Virginia office portfolio' that moved current -> non-performing matured balloon @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Delinquency_Report.pdf p.2; AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:42 lists that portfolio SEPARATELY from Project James. Same asset NOT established — do not merge, do not import 'VA' from it
- **notes:** Primary PDF is archived and was read here; seed source tier PRIMARY-READ is fair for the Trepp facts
- **sources_found:** ALL FOUND: AGENTS/CREED/catchups/2026-09-26.md:40 · AGENTS/CREED/notes/VX_NOTES.md:40 (VX-CREED-2.01 note) · AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:42 · plus the archived primary AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout)
- **proposed_events:** 2026-08|DEFAULT|failed to pay off at August maturity; non-performing matured balloon; DSCR(NCF) 1.30x|377600000|loan balance (Trepp; $354.5M + $23.1M components)|AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) ; 2026-08|TRANSFER_SS|transferred for imminent balloon and maturity default|377600000|loan balance|AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout)
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2026-08 failed to pay off at maturity; transferred to special servicing (Trepp Aug SS report, pub 2026-09-14)
- *latest_status:* SPECIAL_SERVICING (2026-08)
- *trigger:* MATURITY_DEFAULT
- *holder:* CMBS (trust not named)
- *sources:* CREED/catchups/2026-09-26.md l.40; CREED/notes/VX_NOTES.md l.40 (Trepp Aug SS PRIMARY-READ); CREED vulnerability map l.42
- *source_quality:* PRIMARY-READ
- *notes:* Named as a DC-area loan; exact state split not stated.

### CASE-CREED-040 — 111 Livingston St (seed CASE-0042)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** property_type: seed UNKNOWN | Trepp: 'the New York office loans 111 Livingston Street and 60 Madison Avenue' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col3 -> OFFICE · holder: 'CMBS (trust not named)' is correct (no trust named in any file)
- **event_year_check:** PASS: August 2026 transfer (Aug-2026 SS report, pub 2026-09-14 per AGENTS/CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3-August-SS-ZEROS-plus-one-FL-sale-comp-no-distress.md:3)
- **holder_established:** PARTIAL — CMBS securitization established (named in Trepp CMBS SS report); trust and conduit-vs-SASB NOT named -> holder_type UNKNOWN
- **contradictions:** UNKNOWN (none found)
- **notes:** Seed notes cell correctly declines to assign the group-level reason to this loan
- **sources_found:** ALL FOUND: AGENTS/CREED/catchups/2026-09-26.md:40 · AGENTS/CREED/notes/VX_NOTES.md:40 · AGENTS/CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3-August-SS-ZEROS-plus-one-FL-sale-comp-no-distress.md:3 · plus AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col3
- **proposed_events:** 2026-08|TRANSFER_SS|named among 'large maturing loans' that dominated August transfers|UNKNOWN|UNKNOWN|AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout)
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2026-08 transferred to special servicing (Trepp Aug SS report, pub 2026-09-14)
- *latest_status:* SPECIAL_SERVICING (2026-08)
- *trigger:* UNKNOWN
- *holder:* CMBS (trust not named)
- *sources:* CREED/catchups/2026-09-26.md l.40; CREED/notes/VX_NOTES.md l.40; CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3 (Trepp PRIMARY-READ)
- *source_quality:* PRIMARY-READ
- *notes:* Trepp: August transfers concentrated in office, mostly imminent balloon/maturity default; this loan's own reason not stated.

### CASE-CREED-041 — 60 Madison Ave (seed CASE-0043)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** property_type: seed UNKNOWN | Trepp: 'the New York office loans 111 Livingston Street and 60 Madison Avenue' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col3 -> OFFICE
- **event_year_check:** PASS: August 2026 transfer (Aug-2026 SS report, pub 2026-09-14 per AGENTS/CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3-August-SS-ZEROS-plus-one-FL-sale-comp-no-distress.md:3)
- **holder_established:** PARTIAL — CMBS established; trust / conduit-vs-SASB not named
- **contradictions:** UNKNOWN (none found)
- **notes:** Same treatment as CASE-0042
- **sources_found:** ALL FOUND: AGENTS/CREED/catchups/2026-09-26.md:40 · AGENTS/CREED/notes/VX_NOTES.md:40 · AGENTS/CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3-August-SS-ZEROS-plus-one-FL-sale-comp-no-distress.md:3 · plus AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col3
- **proposed_events:** 2026-08|TRANSFER_SS|named among 'large maturing loans' that dominated August transfers|UNKNOWN|UNKNOWN|AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout)
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2026-08 transferred to special servicing (Trepp Aug SS report, pub 2026-09-14)
- *latest_status:* SPECIAL_SERVICING (2026-08)
- *trigger:* UNKNOWN
- *holder:* CMBS (trust not named)
- *sources:* CREED/catchups/2026-09-26.md l.40; CREED/notes/VX_NOTES.md l.40; CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3 (Trepp PRIMARY-READ)
- *source_quality:* PRIMARY-READ
- *notes:* Trepp: August transfers concentrated in office, mostly imminent balloon/maturity default; this loan's own reason not stated.

### CASE-CREED-042 — BXHPP 2021-FILM (Hollywood studio-and-office loan) (seed CASE-0044)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** trigger: seed UNKNOWN | Trepp: 'It transferred for an imminent balloon and maturity default ahead of its August 9 maturity, having exhausted all extension options' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col1 -> MATURITY_DEFAULT · loan: seed $1.10B | Trepp $1.10B = '$770.0 million component and a $330.0 million freely prepayable component', floating-rate, SASB (matches; add split) · status detail: 'reached maturity without a payment default and carries a performing matured balloon status'; DSCR(NCF) 1.45x; 'borrower and special servicer have agreed on a framework for a longer-term extension and executed a 30-day extension for documentation' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col1-2 — seed timeline omits the maturity date, the 30-day extension and the framework · property_name: Trepp's loan name is 'Los Angeles Office/Studio Portfolio' · vintage_year 'CMBS 2021' is inferred from the deal name, not stated as origination year
- **event_year_check:** PASS: 2026-08-09 maturity and August 2026 transfer (Aug-2026 SS report)
- **holder_established:** Y — 'makes up the entirety of the single-asset, single-borrower (SASB) BXHPP 2021-FILM deal' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col1
- **contradictions:** UNKNOWN (none found)
- **notes:** Single loan = essentially the entire +154bp mixed-use SS move (Trepp). Trepp identified it as the largest hard maturity of the month
- **sources_found:** ALL FOUND: AGENTS/CREED/notes/VX_NOTES.md:45 (VX-CREED-2.02 note names BXHPP 2021-FILM) · AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:29 · plus AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col1-2
- **proposed_events:** 2026-08-09|DEFAULT|reached maturity without payment default (performing matured balloon); extension options exhausted|1100000000|loan balance ($770.0M + $330.0M components)|AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) ; 2026-08|TRANSFER_SS|imminent balloon/maturity default; DSCR(NCF) 1.45x|1100000000|loan balance|AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) ; ≤2026-09-14|EXTENSION|30-day extension for documentation executed; framework agreed for a longer-term extension|UNKNOWN|UNKNOWN|AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout)
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2026-08 transferred to special servicing (moved mixed-use SS +154bp in one month)
- *latest_status:* SPECIAL_SERVICING (2026-08)
- *trigger:* UNKNOWN
- *holder:* BXHPP 2021-FILM
- *sources:* CREED/notes/VX_NOTES.md l.45 (Trepp Aug SS PRIMARY-READ); CREED vulnerability map l.29
- *source_quality:* PRIMARY-READ
- *notes:* (blank)

### CASE-CREED-043 — Regency New Orleans (seed CASE-0045)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** property_name: seed 'Regency New Orleans' | Trepp: 'the lodging loan Hyatt Regency New Orleans' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col3 (the CORAL packet truncated the name) · property_type: seed UNKNOWN | Trepp: 'lodging loan' -> LODGING
- **event_year_check:** PASS: August 2026 transfer (Aug-2026 SS report, pub 2026-09-14 per AGENTS/CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3-August-SS-ZEROS-plus-one-FL-sale-comp-no-distress.md:3)
- **holder_established:** PARTIAL — CMBS established; trust / conduit-vs-SASB not named
- **contradictions:** Trepp Aug DQ report: 'the New Orleans hotel moved directly from current to non-performing matured balloon status' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Delinquency_Report.pdf p.2 — UNNAMED. Same asset as this loan NOT established (seed notes say so correctly). If later confirmed, it would add a DEFAULT event and a MATURITY_DEFAULT trigger
- **notes:** Seed note on the DQ-report hotel is accurate
- **sources_found:** FOUND: AGENTS/CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3-August-SS-ZEROS-plus-one-FL-sale-comp-no-distress.md:3 (names it 'Regency New Orleans') · plus AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col3
- **proposed_events:** 2026-08|TRANSFER_SS|named among large maturing loans transferred in August|UNKNOWN|UNKNOWN|AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout)
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2026-08 named among special-servicing transfers (Trepp Aug SS)
- *latest_status:* SPECIAL_SERVICING (2026-08)
- *trigger:* UNKNOWN
- *holder:* CMBS (trust not named)
- *sources:* CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3 (Trepp Aug SS PRIMARY-READ)
- *source_quality:* PRIMARY-READ
- *notes:* Trepp's Aug delinquency report also names 'a New Orleans hotel' that went current -> non-performing matured balloon; that it is this asset is NOT established.

### CASE-CREED-044 — Fresno Fashion Fair Mall (seed CASE-0046)
**Verifier:** VERIFIED
- **field_mismatches:** none (property_type Retail (mall) supported by name + 'retail loans' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout))
- **event_year_check:** PASS: August 2026 transfer (Aug-2026 SS report, pub 2026-09-14 per AGENTS/CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3-August-SS-ZEROS-plus-one-FL-sale-comp-no-distress.md:3)
- **holder_established:** PARTIAL — CMBS established; trust / conduit-vs-SASB not named
- **contradictions:** Trepp Aug DQ report cites 'newly delinquent regional malls' @ AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Delinquency_Report.pdf p.2 — unnamed; not established to include this mall
- **notes:** Row is thin but every non-UNKNOWN field is supported
- **sources_found:** FOUND: AGENTS/CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3-August-SS-ZEROS-plus-one-FL-sale-comp-no-distress.md:3 · plus AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col3 ('retail loans such as the Fresno Fashion Fair Mall and Harlem USA')
- **proposed_events:** 2026-08|TRANSFER_SS|named among retail loans transferred in August|UNKNOWN|UNKNOWN|AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout)
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2026-08 named among special-servicing transfers (Trepp Aug SS)
- *latest_status:* SPECIAL_SERVICING (2026-08)
- *trigger:* UNKNOWN
- *holder:* CMBS (trust not named)
- *sources:* CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3 (Trepp Aug SS PRIMARY-READ)
- *source_quality:* PRIMARY-READ
- *notes:* (blank)

### CASE-CREED-045 — Harlem USA (seed CASE-0047)
**Verifier:** VERIFIED
- **field_mismatches:** none
- **event_year_check:** PASS: August 2026 transfer (Aug-2026 SS report)
- **holder_established:** PARTIAL — CMBS established; trust / conduit-vs-SASB not named
- **contradictions:** UNKNOWN (none found)
- **notes:** Address in New York (Harlem) is stated only via VULN MAP geography row l.41
- **sources_found:** FOUND: AGENTS/CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3-August-SS-ZEROS-plus-one-FL-sale-comp-no-distress.md:3 · AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:41 ('Harlem USA retail transfer') · plus AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout) col3
- **proposed_events:** 2026-08|TRANSFER_SS|named among retail loans transferred in August|UNKNOWN|UNKNOWN|AGENTS/WALTER/sources/2026-08_Trepp_CMBS_Special_Servicing_Report.pdf p.3 (pdftotext -layout)
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2026-08 named among special-servicing transfers (Trepp Aug SS)
- *latest_status:* SPECIAL_SERVICING (2026-08)
- *trigger:* UNKNOWN
- *holder:* CMBS (trust not named)
- *sources:* CORAL/inbox/processed/2026-09-26_from-CREED_FL-slice-cycle-3; CREED vulnerability map l.41
- *source_quality:* PRIMARY-READ
- *notes:* (blank)

### CASE-CREED-046 — 315 South Beverly Drive (seed CASE-0048)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** latest_status: seed SOLD | files say loss realized 'Aug-26 reporting', basis 'balance before disposition' — disposition MODE (REO sale vs note sale vs other) is NOT stated @ AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:101 -> propose UNKNOWN status + LOSS_REALIZED event · event_timeline 'liquidated': supported as 'disposition' in Aug-26 CREFC reporting; the disposition date itself is not given (≤ Aug-2026 reporting period) · figures match: 100% of $19.46M; 92.7% of securitized $21.0M (19.46/21.0 = 92.67%)
- **event_year_check:** PASS: loss in Aug-2026 CREFC reporting (2026); disposition date itself UNKNOWN
- **holder_established:** PARTIAL — CMBS established (CREFC CMBS liquidations table); trust / conduit-vs-SASB not named
- **contradictions:** UNKNOWN (none found)
- **notes:** CREFC Aug PDF itself is not archived in repo (KB-041 gives sha256 only); verified against CREED's PRIMARY-READ transcription, not the PDF
- **sources_found:** ALL FOUND: AGENTS/CREED/workbook/KB.tsv:46 (KB-CREED-041) · AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:101 (§2b table) · also AGENTS/CREED/analysis/2026-09-27_property-comparable-transfer-test.md:35 (C10, 'defaulted')
- **proposed_events:** ≤2026-08|LOSS_REALIZED|loss = 100% of balance before disposition|19460000|loss vs balance before disposition (CREFC Aug 2026, Trepp/Bloomberg data)|AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:101 ; UNKNOWN|ORIGINATED|securitized balance|21000000|securitized (original) balance|AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:101
**Seed row (verbatim):**
- *value_marks:* loss $19.46M (100% of balance; 92.7% of securitized $21.0M)
- *implied_loss_pct:* 100% (source-stated)
- *event_timeline:* 2026-08 (CREFC August reporting) liquidated
- *latest_status:* SOLD (2026-08 reporting)
- *trigger:* UNKNOWN
- *holder:* CMBS (trust not named)
- *sources:* KB-CREED-041; CREED/analysis/2026-09-27_nano-banc-collateral-read.md §2b (CREFC Aug 2026, PRIMARY-READ)
- *source_quality:* PRIMARY-READ
- *notes:* (blank)

### CASE-CREED-047 — La Terraza (seed CASE-0049)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** latest_status: seed SOLD | disposition mode not stated @ AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:102 -> UNKNOWN + LOSS_REALIZED · figures match: $4.15M on $13.23M = 31.4%; 27.7% of securitized $15.0M (4.15/15.0 = 27.67%)
- **event_year_check:** PASS: Aug-2026 CREFC reporting; disposition date itself UNKNOWN
- **holder_established:** PARTIAL — CMBS established; trust / conduit-vs-SASB not named
- **contradictions:** UNKNOWN (none found)
- **notes:** Same verification limit as CASE-0048 (CREFC PDF not in repo)
- **sources_found:** ALL FOUND: AGENTS/CREED/workbook/KB.tsv:46 (KB-CREED-041) · AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:102 · also AGENTS/CREED/analysis/2026-09-27_property-comparable-transfer-test.md:35 (C10)
- **proposed_events:** ≤2026-08|LOSS_REALIZED|loss 31.4% of balance before disposition ($13.23M)|4150000|loss vs balance before disposition (CREFC Aug 2026)|AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:102 ; UNKNOWN|ORIGINATED|securitized balance|15000000|securitized (original) balance|AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:102
**Seed row (verbatim):**
- *value_marks:* loss $4.15M on $13.23M
- *implied_loss_pct:* 31.4% (source-stated; 27.7% of securitized $15.0M)
- *event_timeline:* 2026-08 (CREFC August reporting) liquidated
- *latest_status:* SOLD (2026-08 reporting)
- *trigger:* UNKNOWN
- *holder:* CMBS (trust not named)
- *sources:* KB-CREED-041; CREED/analysis/2026-09-27_nano-banc-collateral-read.md §2b (CREFC Aug 2026, PRIMARY-READ)
- *source_quality:* PRIMARY-READ
- *notes:* (blank)

### CASE-CREED-048 — 100 Summer St (seed CASE-0050)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** originator: seed 'Wells Fargo' | files say only '$470M Wells Fargo loan' @ AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:11 — originator not stated as such · holder: seed 'Wells Fargo' | rule 6: a lender name is not the holder; AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:90 calls it 'a large-bank-held Boston office loan' (CREED characterisation of a SECONDARY lead, no primary) -> holder_type UNKNOWN (candidate BANK) · latest_status: seed DEFAULT | files say 'foreclosure auction set 10/20' / 'heads to foreclosure auction' @ AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:11, AGENTS/CREED/catchups/2026-09-26.md:68 -> FORECLOSURE (auction scheduled) · property_type: 'per CREED map grouping' is supported (AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:46 'B (office)', :90 'Boston office loan') · fleet_links 'not in its 14-bank cohort' is supported only by the uncited REGINALD->CREED packet line 5
- **event_year_check:** PASS: 2019 purchase and a 2026-10-20 auction date (a FUTURE event as of 2026-09-26); default date itself UNKNOWN
- **holder_established:** N — lender name only; 'large-bank-held' at AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:90 is CREED's own label on a SECONDARY source
- **contradictions:** '$425M current value' circulates UNLABELLED @ AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:11 — not a sale price, basis unknown; keep in notes as UNRECONCILED, never in value_marks as a mark
- **notes:** SECONDARY row; the 10/20 auction is the dated price-discovery point
- **sources_found:** ALL FOUND: AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:11 (Boston Globe, Banker & Tradesman — SECONDARY) · AGENTS/CREED/catchups/2026-09-26.md:68 · also AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:46,90 and AGENTS/CREED/inbox/processed/2026-09-26_from-REGINALD_REG-T-07-chain-already-carries-CREED-plus-BCB-noted.md:5
- **proposed_events:** 2019|ACQUIRED|bought|806000000|purchase price|AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:11 ; UNKNOWN|DEFAULT|loan heads to foreclosure|470000000|loan amount (balance vs commitment not stated)|AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:11 ; 2026-10-20|OTHER|foreclosure auction scheduled (future)|UNKNOWN|UNKNOWN|AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:11
**Seed row (verbatim):**
- *value_marks:* 2019 purchase $806M; an unlabelled '$425M current value' circulates (not a sale price)
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2019 bought for $806M; 2026-10-20 foreclosure auction scheduled (reported in CREED 9/26 sweep)
- *latest_status:* DEFAULT (foreclosure auction set for 2026-10-20)
- *trigger:* UNKNOWN
- *holder:* Wells Fargo
- *sources:* REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED...100-Summer.md l.11 (Boston Globe, Banker & Tradesman); CREED/catchups/2026-09-26.md l.68
- *source_quality:* SECONDARY
- *notes:* A large-bank-held office loan; auction is a dated price-discovery point.

### CASE-CREED-049 — Glendale Plaza (seed CASE-0051)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** implied_loss_pct: seed '~52% (1 - $70M/$145M)' | files give only the $145M 2022 LOAN amount, not the balance at sale, and no lender recovery; AGENTS/CREED/analysis/2026-09-27_property-comparable-transfer-test.md:36 marks the Glendale -61% 'wrong-basis, do not use as a loss rate' -> move the 52% to notes as DERIVED/UNRECONCILED, implied_loss UNKNOWN (rule 5) · property_type: seed cites AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:44, which is a GEOGRAPHY row (LA area), not a type classification; OFFICE is supported instead by AGENTS/CREED/analysis/2026-09-27_property-comparable-transfer-test.md:36 (type 'office') · sale date UNKNOWN in all files · figures match: $70M vs $179M = -60.9%
- **event_year_check:** RISK: sale date not given anywhere; first reported 2026-09-26 in a 'September sweep' — a 2026 event is NOT established (rule 11)
- **holder_established:** N — '(lender unconfirmed)' @ AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:12
- **contradictions:** UNKNOWN (none found)
- **notes:** SECONDARY; -61% is sale vs 2017 purchase, not a loss rate
- **sources_found:** FOUND: AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:12 · AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:44 (says only 'Glendale Plaza -61% sale') · also AGENTS/CREED/analysis/2026-09-27_property-comparable-transfer-test.md:36 (C11) and AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md:107
- **proposed_events:** 2017|ACQUIRED|bought|179000000|purchase price|AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:12 ; 2022|ORIGINATED|loan (lender unconfirmed)|145000000|original loan amount|AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:12 ; UNKNOWN|SALE|sold below the 2022 loan amount|70000000|sale price|AGENTS/REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED-rate-fire-plus-two-bank-CRE-leads-BCB-note-sale-and-100-Summer.md:12
**Seed row (verbatim):**
- *value_marks:* 2017 purchase $179M; sale $70M (-61% vs 2017)
- *implied_loss_pct:* ~52% (1 - $70M/$145M, gross sale vs loan; lender recovery not reported)
- *event_timeline:* 2017 bought for $179M; 2022 $145M loan; UNKNOWN date sold for $70M (reported in CREED 9/26 sweep)
- *latest_status:* SOLD (date UNKNOWN; reported 2026-09-26)
- *trigger:* UNKNOWN
- *holder:* UNKNOWN
- *sources:* REGINALD/inbox/processed/2026-09-26_from-CREED_T-08a-FIRED...100-Summer.md l.12; CREED vulnerability map l.44
- *source_quality:* SECONDARY
- *notes:* (blank)

### CASE-CREED-050 — 1 Whitehall Street (seed CASE-0052)
**Verifier:** PARTIAL
- **field_mismatches:** latest_status: seed 'FORECLOSED' is not a vocab term -> FORECLOSURE (foreclosure completed, date UNKNOWN) — owner after foreclosure (REO holder) not stated · event_timeline: seed '~2026-04 in contract' | file: 'in contract at ~$100M (post-Chetrit foreclosure, rental conversion planned)' in a newsletter the signal dates to the week of 2026-04-20 @ BOARD/SIG-W-20260420-008-distressed-office-sales-5b-price-discovery-reset.md:6,40 — contract date is ≤2026-04-20, April not established · buyers Metro Loft (Nathan Berman) + Quantum Pacific (Idan Ofer) match · property_type OFFICE supported only by article frame (distressed office trades)
- **event_year_check:** RISK: foreclosure date UNKNOWN and may pre-date 2026; only the contract report is dated (≤2026-04-20)
- **holder_established:** N — no lender or holder named
- **contradictions:** UNKNOWN (none found)
- **notes:** Unsupported fields: every loan field (none in file). Source tier SECONDARY, publisher unidentified
- **sources_found:** FOUND: BOARD/SIG-W-20260420-008-distressed-office-sales-5b-price-discovery-reset.md:40 (unnamed CRE newsletter; WALTER did NOT pull primaries, l.67)
- **proposed_events:** UNKNOWN|FORECLOSURE|post-Chetrit foreclosure|UNKNOWN|UNKNOWN|BOARD/SIG-W-20260420-008-distressed-office-sales-5b-price-discovery-reset.md:40 ; ≤2026-04-20|OTHER|in contract to Metro Loft + Quantum Pacific|100000000|contract price (approx; not closed)|BOARD/SIG-W-20260420-008-distressed-office-sales-5b-price-discovery-reset.md:40
**Seed row (verbatim):**
- *value_marks:* ~2026-04 contract ~$100M
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* UNKNOWN date foreclosure (Chetrit ownership); ~2026-04 in contract to Metro Loft + Quantum Pacific at ~$100M
- *latest_status:* FORECLOSED (date UNKNOWN); in contract ~2026-04
- *trigger:* UNKNOWN
- *holder:* UNKNOWN
- *sources:* SIG-W-20260420-008 (unnamed CRE newsletter; deals not primary-checked)
- *source_quality:* SECONDARY
- *notes:* (blank)

### CASE-CREED-051 — 401 S. State St (seed CASE-0053)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** event_timeline: seed 'reported by 2026-02-22' | ML-REG-053 already cites '401 S State 94%' on 2026-02-02 @ AGENTS/REGINALD/workbook/KB.tsv:55 -> reported ≤2026-02-02 · property_type: seed UNKNOWN | ML-REG-053 lists it among 'Actual office loss severities' @ AGENTS/REGINALD/workbook/KB.tsv:55 -> OFFICE (per source framing) · figures match: $68.1M (2016) -> $4.2M = -93.8%
- **event_year_check:** RISK: sale date not given; first reported ≤2026-02-02 — a 2025 sale presented as 2026 cannot be ruled out (rule 11)
- **holder_established:** N — no lender/holder named
- **contradictions:** BASIS CONTRADICTION: ML-REG-053 presents '94%' as an 'actual office loss SEVERITY' @ AGENTS/REGINALD/workbook/KB.tsv:55; ML-REG-074 shows the same 94% is sale price vs 2016 purchase price @ AGENTS/REGINALD/workbook/KB.tsv:76 — not a loan loss. Seed correctly keeps implied_loss UNKNOWN
- **notes:** Do not import ML-REG-053's 'loss severity' label
- **sources_found:** FOUND: AGENTS/REGINALD/workbook/KB.tsv:76 (ML-REG-074, Fox Business 2026-02-22) · AGENTS/REGINALD/workbook/KB.tsv:55 (ML-REG-053, @FCNightingale, row dated 2026-02-02)
- **proposed_events:** 2016|ACQUIRED|bought|68100000|purchase price|AGENTS/REGINALD/workbook/KB.tsv:76 ; ≤2026-02-02|SALE|sold|4200000|sale price|AGENTS/REGINALD/workbook/KB.tsv:76
**Seed row (verbatim):**
- *value_marks:* 2016 $68.1M; sale $4.2M (-94%)
- *implied_loss_pct:* UNKNOWN (-94% is vs 2016 price)
- *event_timeline:* 2016 purchase; UNKNOWN date sale (reported by 2026-02-22)
- *latest_status:* SOLD (date UNKNOWN; reported 2026-02-22)
- *trigger:* UNKNOWN
- *holder:* UNKNOWN
- *sources:* ML-REG-074 (Fox Business 2026-02-22); ML-REG-053 (@FCNightingale)
- *source_quality:* SECONDARY
- *notes:* (blank)

### CASE-CREED-052 — 311 S. Wacker Drive (seed CASE-0054)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** property_type: seed UNKNOWN | ML-REG-074 frames all its Chicago transactions under 'America's office market downturn' @ AGENTS/REGINALD/workbook/KB.tsv:76 -> OFFICE (article framing, not a per-building statement) · figures match: $302M (2014) -> $45M = -85.1%
- **event_year_check:** RISK: sale date not given; reported ≤2026-02-22 — a 2025 sale cannot be ruled out (rule 11)
- **holder_established:** N — no lender/holder named
- **contradictions:** UNKNOWN (none found)
- **notes:** -85% is sale vs 2014 purchase, not a loan loss (seed correct)
- **sources_found:** FOUND: AGENTS/REGINALD/workbook/KB.tsv:76 (ML-REG-074, Fox Business 2026-02-22)
- **proposed_events:** 2014|ACQUIRED|bought|302000000|purchase price|AGENTS/REGINALD/workbook/KB.tsv:76 ; ≤2026-02-22|SALE|sold|45000000|sale price|AGENTS/REGINALD/workbook/KB.tsv:76
**Seed row (verbatim):**
- *value_marks:* 2014 $302M; sale $45M (-85%)
- *implied_loss_pct:* UNKNOWN (-85% is vs 2014 price)
- *event_timeline:* 2014 purchase; UNKNOWN date sale (reported by 2026-02-22)
- *latest_status:* SOLD (date UNKNOWN; reported 2026-02-22)
- *trigger:* UNKNOWN
- *holder:* UNKNOWN
- *sources:* ML-REG-074 (Fox Business 2026-02-22)
- *source_quality:* SECONDARY
- *notes:* (blank)

### CASE-CREED-053 — 175 W. Jackson (CBOT annex) (seed CASE-0055)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** latest_status as-of: seed 'cited 2026-06-24' | ML-REG-074 already names 175 W Jackson on 2026-02-22/23 @ AGENTS/REGINALD/workbook/KB.tsv:76 (a discount mention, no sale price) -> earliest reference ≤2026-02-22; the $41M sale itself is first in the files ≤2026-06-24 @ BOARD/SIG-W-20260624-004-blackstone-bxmt-1-south-wacker-343m-loan-maturity-default-chicago-office.md:32 · 'pre-Covid $306M' is the SIG's wording — the basis of $306M (purchase vs appraisal) is not stated · property_type: seed UNKNOWN | SIG uses it as a 'nearby comp' for an office loan and ML-REG-074 frames it as office -> OFFICE (framing) · figures: $41M / $306M = 13.4% -> 86.6% ≈ 87% matches
- **event_year_check:** RISK: sale date never given; reports span 2026-02-22 (ML-REG-074) to 2026-06-24 (SIG) — the sale may pre-date 2026
- **holder_established:** N — no lender/holder named
- **contradictions:** Seed NOTES §5 #10 carried: 87% markdown from $306M (BOARD/SIG-W-20260624-004-blackstone-bxmt-1-south-wacker-343m-loan-maturity-default-chicago-office.md:32) vs '~70-80% discounts' (AGENTS/REGINALD/workbook/KB.tsv:76). Not resolved here
- **notes:** SIG line is context in a signal about 1 S Wacker (CASE-0032), confidence 0.85
- **sources_found:** FOUND: BOARD/SIG-W-20260624-004-blackstone-bxmt-1-south-wacker-343m-loan-maturity-default-chicago-office.md:32 ('Context (0.85)') · AGENTS/REGINALD/workbook/KB.tsv:76 (ML-REG-074)
- **proposed_events:** UNKNOWN|OTHER|pre-Covid value (basis not stated)|306000000|UNKNOWN basis ('pre-Covid')|BOARD/SIG-W-20260624-004-blackstone-bxmt-1-south-wacker-343m-loan-maturity-default-chicago-office.md:32 ; UNKNOWN|SALE|sold|41000000|sale price|BOARD/SIG-W-20260624-004-blackstone-bxmt-1-south-wacker-343m-loan-maturity-default-chicago-office.md:32
**Seed row (verbatim):**
- *value_marks:* pre-Covid $306M; sale $41M (87% markdown, SIG-624-004) vs '~70-80% discounts' (ML-REG-074)
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* UNKNOWN date sale
- *latest_status:* SOLD (date UNKNOWN; cited 2026-06-24)
- *trigger:* UNKNOWN
- *holder:* UNKNOWN
- *sources:* SIG-W-20260624-004 (verify agent context); ML-REG-074 (Fox Business 2026-02-22)
- *source_quality:* SECONDARY
- *notes:* Two files disagree on the discount (87% vs ~70-80%).

### CASE-CREED-054 — Republic Plaza (seed CASE-0056)
**Verifier:** PARTIAL
- **field_mismatches:** none on stated fields; latest_status: seed 'RECEIVERSHIP' is not a vocab term (receivership is not foreclosure) -> DEFAULT with note 'receiver appointed', or extend the README vocab
- **event_year_check:** RISK: receiver appointment date not in any file; could pre-date 2026
- **holder_established:** N
- **contradictions:** UNKNOWN (none found)
- **notes:** Unsupported: everything beyond name, city and the word 'receiver'. The primary behind CREED's SECONDARY tier is not in the repo
- **sources_found:** FOUND: AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:47 ('Republic Plaza receiver') · AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:136 (§9 lists Republic Plaza as SECONDARY). No underlying article in repo (grep -rn 'Republic Plaza' AGENTS BOARD returns only these two lines and the seed)
- **proposed_events:** UNKNOWN|OTHER|receiver appointed|UNKNOWN|UNKNOWN|AGENTS/CREED/research/2026-09-26_CRE_VULNERABILITY_MAP.md:47
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* UNKNOWN date receiver appointed
- *latest_status:* RECEIVERSHIP (date UNKNOWN; cited 2026-09-26)
- *trigger:* UNKNOWN
- *holder:* UNKNOWN
- *sources:* CREED vulnerability map l.47 + §9 (SECONDARY)
- *source_quality:* SECONDARY
- *notes:* Thin row.

### CASE-CREED-055 — Spur Phase I (seed CASE-0058)
**Verifier:** VERIFIED_WITH_CORRECTIONS
- **field_mismatches:** trigger: seed 'OTHER (lease-up failure)' | file states 'completed 2025, never occupied' and a deed-in-lieu; it does NOT state a cause ('lease-up failure' is inference) -> UNKNOWN (SPONSOR_WALKAWAY describes the deed-in-lieu mechanism, not a stated cause) · holder: seed 'Apollo affiliate (took title)' | file: '$275M Apollo construction loan (Nov 2022)'; title went 'to an Apollo affiliate by deed-in-lieu' — which Apollo vehicle held the loan (fund / ARI mREIT / Athene) is not stated -> holder_type UNKNOWN · special_servicer 'n/a' -> UNKNOWN per rule 2 (non-CMBS inferred, not stated) · 'First IQHQ asset handed back to a lender' matches · address, 330K SF, completed 2025, $275M, Nov 2022 all match
- **event_year_check:** PASS: loan Nov 2022; building completed 2025; deed-in-lieu reported 2026-09-17 (deed date itself not given, ≤2026-09-17)
- **holder_established:** PARTIAL — lender-side Apollo affiliate took title (so an Apollo entity held it); the vehicle type is not established
- **contradictions:** UNKNOWN (none found)
- **notes:** NOT an OZK credit (KB-OZK-238). Sponsor IQHQ is also OZK's RaDD borrower (seed fleet_links consistent)
- **sources_found:** FOUND: AGENTS/OZK/workbook/KB.tsv:243 (KB-OZK-238) (The Real Deal 2026-09-17, single outlet)
- **proposed_events:** 2022-11|ORIGINATED|Apollo construction loan|275000000|construction loan amount (commitment vs funded not stated)|AGENTS/OZK/workbook/KB.tsv:243 (KB-OZK-238) ; ≤2026-09-17|REO|deed-in-lieu to an Apollo affiliate|UNKNOWN|UNKNOWN|AGENTS/OZK/workbook/KB.tsv:243 (KB-OZK-238)
**Seed row (verbatim):**
- *value_marks:* UNKNOWN
- *implied_loss_pct:* UNKNOWN
- *event_timeline:* 2022-11 Apollo construction loan; UNKNOWN date deed-in-lieu to an Apollo affiliate (TRD 2026-09-17)
- *latest_status:* REO (reported 2026-09-17)
- *trigger:* OTHER (lease-up failure)
- *holder:* Apollo affiliate (took title)
- *sources:* KB-OZK-238 (The Real Deal 2026-09-17)
- *source_quality:* SECONDARY
- *notes:* First IQHQ asset handed back to a lender.


## Residual flags after the 2026-09-29 correction pass (NOT applied — owed at the next owner edit)

*The source/holder/geography/relationship correction pass (Will-directed 9/29; CATO CD1–CD3) applied only those field classes. The three proposal agents listed what else they found: 88 items across 44 cases. Out-of-scope fields (value marks, loss basis, vocab, status) are listed here and were not fixed.*

- **CASE-CREED-001:** value_marks: video's Harris County ~$45M (SIG-W-20260929-015:15) is a tax-assessor-basis, unverified figure -- not added; if added tag tax-assessor + SEARCH-SUMMARY
- **CASE-CREED-001:** implied_loss/notes: $64.8M trust loss (vulnerability map :47,:72, source not found) vs $68.6M gross stays UNRECONCILED until a remittance report is read
- **CASE-CREED-003:** value_marks: S&P $270.4M (2022-04) is a MODEL value, not an appraisal -- needs basis tag
- **CASE-CREED-003:** loan_amount_usd: $308M is legacy-archive only (RQ-CREED-009:46, undated)
- **CASE-CREED-003:** special_servicer: servicer switch stated (KB-CREED-016) but servicer names not in files
- **CASE-CREED-004:** value_marks: $63.3M is a DERIVED appraisal (54.5/0.86); $54.5M is carrying; tag each basis
- **CASE-CREED-004:** property_name: "(LA entitled land)" left as is while city is DISPUTED
- **CASE-CREED-005:** trigger: vocab RATE_RESET+SPONSOR_WALKAWAY applied at adoption; the occupancy 69%->63% leg (OPERATING_SHORTFALL) is not in the token -- CREED call
- **CASE-CREED-005:** value_marks: DSCR 1.98->0.59 undated; >$74M recovery sought is a claim, not a value
- **CASE-CREED-005:** holder: Varde named as lender via Trimont; balance sheet vs fund vs securitization not stated (cell already UNKNOWN)
- **CASE-CREED-006:** holder: UNKNOWN (SS implies CMBS, trust not named) -- case not flagged
- **CASE-CREED-006:** sources: the Lafayette clause's own source is not named inside KB-OZK-204
- **CASE-CREED-007:** loan_amount_usd: $128M (KB-OZK-208) vs $126M "loan basis" (SEVEN:174) -- unreconciled
- **CASE-CREED-007:** implied_loss_pct: ~30% (cumulative writedown/loan) vs 33-34% (sale at carrying vs loan) are different bases; $128M-$38M=$90M vs $83.95M sale implies ~$6M further mark not itemised
- **CASE-CREED-007:** status: identity of the Q3'25 "Chicago land" sale with this loan IS stated (SEVEN:174; KB-OZK-126) -- seed "INFERRED" note is outdated
- **CASE-CREED-008:** latest_status: FORECLOSURE (complaint filed) applied at adoption; outcome not in files
- **CASE-CREED-009:** holder: verifier PARTIAL -- CMBS established (CREFC CMBS liquidation data, KB-CREED-041), trust not named; case not flagged, not applied this pass
- **CASE-CREED-009:** fleet_links: sponsor Brookfield (RQ-CREED-009:23-26 "2024 Defaults") absent
- **CASE-CREED-009:** receivership event precedes the 6/16/26 sale but is undated
- **CASE-CREED-010:** value_marks: $6.84M/60% (Atrium, KB-OZK-207) vs $6.44M/58% (MC4 via dossier) -- unresolved; the 31% carrying/credit derivation rests on $6.84M only
- **CASE-CREED-011:** loan_amount/holder: row mixes the Preferred ~$31M 1st and the Nano $5M 2nd -- one case = one loan (rule 1): CREED to pick which loan the case is
- **CASE-CREED-011:** value_marks: liens $35.8M + taxes vs 2023 appraisal $57.38M are mixed dates -- no LTV
- **CASE-CREED-012:** value_marks: HCAD $6.4M + $4.7M is a TAX-ASSESSOR basis, not an appraisal (rule 4)
- **CASE-CREED-012:** property_type: not stated for Gateway (UNKNOWN kept)
- **CASE-CREED-013:** size: ~119,298 SF vs 84,000 SF listing perimeter (NOTES §5 #12) unreconciled
- **CASE-CREED-013:** trigger: FRAUD_OR_LEGAL = why this is a case (WAL fraud complaint); property-level default cause not stated
- **CASE-CREED-014:** property_type: office/medical + retail -- OFFICE vs MIXED_USE is CREED's call
- **CASE-CREED-014:** holder: Nano lien holder at 9/25 not proven; 2026-09-29 hearing outcome not in files (UNKNOWN valid)
- **CASE-CREED-015:** holder: verifier PARTIAL -- CMBS stated ("Underlying CMBS"), trust ticker not surfaced; case not flagged, not applied this pass
- **CASE-CREED-015:** trigger: OPERATING_SHORTFALL rests on WALTER's mechanism inference, not on the verified loan facts
- **CASE-CREED-016:** property_type: not stated in file; the line's own source is not named (news sweep §3)
- **CASE-CREED-017:** value_marks: Feb-25 ~$29M is a Preferred Bank appraisal quoted debtor-side; $23.5-26.5M is a debtor-side broker range -- tag both
- **CASE-CREED-017:** latest_status: BANKRUPTCY applied at adoption; Ch.11 filing date not in files (<=2026-08-26)
- **CASE-CREED-018:** fleet_links: verifier says cite HOMER (MF lane owner, rule 10) -- no HOMER record found (grep 2026-09-29); case not flagged, not applied
- **CASE-CREED-018:** value_marks: "Nano 2nd under-secured" is INFERRED
- **CASE-CREED-019:** trigger: vocab has no lease-up-failure term; OPERATING_SHORTFALL is the closest (CREED call)
- **CASE-CREED-019:** size: 284K vs 320K SF; loan $125.1M commitment vs $65M outstanding -- basis mix
- **CASE-CREED-019:** event E097 title mechanism DISPUTED (see events)
- **CASE-CREED-020:** charge-offs: $25.5M (dossier, MC3/MC4) vs $9.7M (KB-OZK-119) -- implied_loss derivation uses $25.5M
- **CASE-CREED-020:** 212 DPD at 2026-06-30 counts back to ~2025-11-30, before the 2025-12-18 maturity -- unexplained in files
- **CASE-CREED-020:** trigger MATURITY_DEFAULT: the $20.9M Q3'25 charge-off pre-dates maturity, so maturity is the default EVENT, not a stated cause
- **CASE-CREED-020:** event E104 deed-in-lieu DISPUTED (KB-OZK-119 vs Q2 MC)
- **CASE-CREED-022:** status_as_of: sale date 2026-01-05 (KB-OZK-031/153) vs 2026-01-07 (KB-OZK-199 = TRD article date) unresolved - see E113
- **CASE-CREED-022:** size: 500K SF (KB-OZK-199) vs 690K SF Phase 1 (KB-OZK-148) - owed
- **CASE-CREED-022:** implied_loss_pct: 0% is the issuer claim on funded principal; KB-OZK-031 audit note "par claim unverified (Gap B6)"; SVP price undisclosed
- **CASE-CREED-023:** event_timeline: "Feb 10-12" may be tracker post dates; transaction year unverifiable from repo (rule 11) - needs county record / trustee sale
- **CASE-CREED-023:** value_marks / implied_loss_pct: basis of the $148M not stated
- **CASE-CREED-023:** property_type UNKNOWN
- **CASE-CREED-024:** latest_status: $330M sale carries "diminished assessment of the likelihood of closing" (AGENTS/REGINALD/reports/2026-09-26_CRE_top3_dossiers/q2_OZK.md:33) - caveat not on row
- **CASE-CREED-024:** value_marks: ~$186.0M is DERIVED (169.3/0.91), not a disclosed appraisal
- **CASE-CREED-025:** loan_amount / balance: $56.2M dated Q4-24 (KB-OZK-193) vs Atrium Q4-25 pre-charge-off (KB-OZK-207) - quarter inconsistent
- **CASE-CREED-025:** value_marks: $78M Atrium-reported appraisal vs ~$25.9M implied by 100% LTV on the Dec-25 appraisal - not established as the same appraisal
- **CASE-CREED-025:** E124 basis: dossier (MC1 p.23) and KB-BRK-214 treat the $27.7M as disclosed; OZK-W7 calls it INFERRED - OZK desk to settle
- **CASE-CREED-026:** value_marks: ~$17.4M is DERIVED. The 96% vs 103% LTV "conflict" reconciles to one ~$17.4M appraisal on two balances (16.7/0.96 = 17.4; 17.9/1.03 = 17.4; CREED arithmetic) - relabel, not a dispute
- **CASE-CREED-028:** value_marks: $128.8M as-stabilized rests on an unresolved LTV basis (commitment vs outstanding, KB-OZK-190 ties 83% to $76.4M); $78.4M assignment value vs ~$78.4M derived peak are different objects
- **CASE-CREED-028:** trigger: SPONSOR_WALKAWAY vs KB-OZK-190 "NOT sponsor distress - Ameriprise exiting / Lionstone divesting", then buyer withdrew - no vocab token fits
- **CASE-CREED-028:** vintage: ~2024 delivery (dossier, S) not on row
- **CASE-CREED-029:** size: ~154K SF (SIG l.30) vs 149K SF (dossier) - owed
- **CASE-CREED-029:** value_marks: ~$51.1M is DERIVED; Atrium $115M / $58M are model values on a different basis
- **CASE-CREED-029:** trigger: SPONSOR_WALKAWAY vs KB-OZK-190 LP-exit cause - as CASE-CREED-028
- **CASE-CREED-030:** loan_amount_usd: $85.5M basis unknown (commitment vs outstanding); peak outstanding $45.1M is DERIVED
- **CASE-CREED-030:** implied_loss_pct: the 42.8% divides carrying by the $85.5M on a different basis - relabel owed
- **CASE-CREED-032:** value_marks: $780M 2018 value basis UNKNOWN; appraisal date not stated (reported 2026-06-24)
- **CASE-CREED-032:** latest_status UNKNOWN: extension outcome DISPUTED (see E152)
- **CASE-CREED-032:** holder_type stays UNKNOWN: conduit vs SASB not in files
- **CASE-CREED-033:** loan_amount_usd: $90M senior vs full stack UNKNOWN (SIG l.30)
- **CASE-CREED-033:** HOMER acknowledgement of the case owed (rule 10); packet sent 2026-09-29
- **CASE-CREED-034:** implied_loss_pct: 73% rests on an unstated loan basis; COMM 2015-CR22 remit read owed
- **CASE-CREED-034:** vintage: "CMBS 2015" is the deal-name year, not a stated origination year
- **CASE-CREED-034:** event dates: sale/liquidation date not in files; may predate 2026 (rule 11)
- **CASE-CREED-039:** tenant_or_occupancy_note: Trepp says 'eroding occupancy', DSCR(NCF) 1.30x, status non-performing matured balloon -- not yet carried in the row
- **CASE-CREED-042:** vintage_year: 'CMBS 2021' is inferred from the deal name, not a stated origination year (CASE_NOTES §CASE-CREED-042)
- **CASE-CREED-042:** E167 typed DEFAULT but Trepp says the loan 'reached maturity without a payment default' (performing matured balloon) -- event_type review owed
- **CASE-CREED-043:** identity with the UNNAMED New Orleans hotel that went current -> non-performing matured balloon (2026-08_Trepp_CMBS_Delinquency_Report.pdf p.2) NOT established; if confirmed it adds a DEFAULT event and MATURITY_DEFAULT trigger
- **CASE-CREED-044:** holder: not verifier-flagged, so left as-is; for consistency with 040/041/043 the verifier's PARTIAL finding supports 'CMBS trust (name UNKNOWN; conduit vs SASB not named)'
- **CASE-CREED-045:** holder: not verifier-flagged, so left as-is; for consistency with 040/041/043 the verifier's PARTIAL finding supports 'CMBS trust (name UNKNOWN; conduit vs SASB not named)'
- **CASE-CREED-046:** source_quality PRIMARY-READ rests on CREED's 2026-09-27 read of the CREFC Aug PDF (sha256 in KB-CREED-041); the PDF is not archived in repo, so the verifier checked the transcription only
- **CASE-CREED-047:** source_quality PRIMARY-READ rests on CREED's 2026-09-27 read of the CREFC Aug PDF (sha256 in KB-CREED-041); the PDF is not archived in repo, so the verifier checked the transcription only
- **CASE-CREED-048:** value_marks: the unlabelled '$425M current value' (REGINALD packet :11) must stay in notes as UNRECONCILED, never a mark
- **CASE-CREED-048:** holder_type: 'large-bank-held' (CRE_VULNERABILITY_MAP.md:90) is CREED's label on a SECONDARY source -- candidate BANK only, not established
- **CASE-CREED-049:** implied_loss_pct: already UNRECONCILED; the seed's ~52% (1 - $70M/$145M) is DERIVED on a loan amount, not balance at sale -- keep in CASE_NOTES only (CREED analysis/2026-09-27_property-comparable-transfer-test.md:36 'wrong-basis')
- **CASE-CREED-050:** latest_status: FORECLOSURE here means foreclosure COMPLETED (date UNKNOWN, may pre-date 2026); the post-foreclosure owner (REO holder) is not stated, and the ~$100M contract is not a status (SIG-W-20260420-008:40)
- **CASE-CREED-051:** value basis: ML-REG-053 (REGINALD KB.tsv:55) labels the 94% an 'office loss severity'; ML-REG-074 (KB.tsv:76) shows it is sale vs 2016 purchase -- do not import the severity label
- **CASE-CREED-053:** value_marks: 87% markdown from $306M 'pre-Covid' (SIG-W-20260624-004:32; basis of $306M not stated) vs '~70-80% discounts' (REGINALD KB.tsv:76 ML-REG-074) -- unresolved; E190 marked DISPUTED
- **CASE-CREED-054:** latest_status: DEFAULT stands in for 'receiver appointed' -- the vocab has no RECEIVERSHIP term; extend README vocab or keep DEFAULT with note
- **CASE-CREED-054:** property_type UNKNOWN: CRE_VULNERABILITY_MAP.md:47 names only 'Republic Plaza receiver' in a metro row; no type stated
- **CASE-CREED-055:** special_servicer: 'n/a' should be UNKNOWN per rule 2 (non-CMBS is inferred, not stated) -- field outside correction scope
- **CASE-CREED-055:** trigger: already UNKNOWN; 'lease-up failure' is inference and must not return
