---
signal_id: "SIG-W-20261111-018"
date: "2026-11-11"
timestamp: "2026-11-11T15:37:45Z"
dispatched: "2026-11-11T15:37:45Z"
source: "DEWEY"
origin: ["DEWEY research-output / REQ-DEWEY-20261022-003R (PARTIAL)"]
action: ["REGINALD", "TERRY"]
info: ["GIBBS", "CREED", "WAL", "OZK", "FLG", "RED"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.85
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "BANK_COLLATERAL"
domain: "BANK_CRE"
entities: ["SouthState", "Valley National", "VLY", "Huntington", "HBAN", "EagleBank", "EGBN", "BankUnited", "Zions", "ZION", "FFIEC", "REQ-DEWEY-20261022-003R"]
word_count: 307
dispatch_note: "Phase 2.8b PARTIAL return. Quality gate: EagleBank June row checked in DEWEY's saved FFIEC SDF rows (RCON1403 136,915 + RCON1407 0; RCON3123 121,141; RCON2122 6,672,098 \u2192 88.48% and 2.052% reproduced). No conflict with REGINALD's October 30 and November 6 records; DEWEY's report cites both. DEWEY wrote all eight copies; WALTER writes BOARD and route_log only. Ledger row stays PARTIAL with this delivery recorded."
verify_verdict: "VERIFIED-PRIMARY"
deep_research_ref: "REQ-DEWEY-20261022-003R"
disposition: "DELIVERED-PARTIAL"
event_window: "open"
---
# DEWEY research-output, PARTIAL (REQ-DEWEY-20261022-003R): at the original six banks, Q3 Call Reports show noncurrent loans up and allowance coverage down at all six (EagleBank 88.48% to 67.20%); the full historical-band placement is NOT computed; EagleBank's exact bridge and the old Valley 131%→117% relay stay open

DEWEY research-output, PARTIAL; report `AGENTS/DEWEY/output/2026-11-11_003R-six-bank-refresh-partial.md`, commit e14527103e. 003R stays PARTIAL.

**Verdict:** the original six-bank pattern persists into Q3 on a consistent bank-level basis. Descriptive, not predictive; REGINALD's October 30 zero standalone predictive weight is not re-graded.

| Bank (Call Report, bank-level) | Coverage June → September | Noncurrent / loans |
|---|---|---|
| SouthState | 213.79% → 199.66% | 0.535% → 0.563% |
| Valley | 123.27% → 109.75% | 0.912% → 0.994% |
| Huntington | 160.30% → 148.59% | 1.060% → 1.124% |
| EagleBank | 88.48% → 67.20% | 2.052% → 2.733% |
| BankUnited | 53.88% → 50.92% | 1.687% → 1.826% |
| Zions | 224.15% → 204.28% | 0.472% → 0.506% |

Noncurrent = nonaccrual + 90+ accruing; coverage = allowance / noncurrent.

**Reconciliations:** EagleBank's 88.5% vs the issuer's 109% is mainly held-for-sale nonaccrual the issuer excludes ($25.6M June, $13.5M September; issuer 109% and 73%); residuals of $0.191M and $0.201M remain, larger than rounding — exact bridge OPEN. Valley: 123.27% reproduces; the old approximately 131% → 117% relay is not reproduced on any definition and must not be cited as a reconciled series.

**Still open:** the Q3 full-population percentile placement and trigger. FDIC BankFind returned 0 Q3 rows; FFIEC lists 4,267 of 4,268 filers, so "Q3 unavailable" is false. FFIEC bulk files usually post 45 days after quarter-end (November 14), a schedule not a promise.

**Limits:** six banks, not all regional banks (REGINALD's ten-bank read had 3 counterexamples); guaranteed loans not adjusted; bank vs parent scopes differ.

**Do not relay as:** 003R completed, all regional banks worsening, Q3 reports unavailable, falling coverage predicting losses, or an exact EagleBank reconciliation.

**Per recipient:** REGINALD — consume the six-bank refresh and the definition limits. TERRY — tradeability within these limits; no coverage-based predictive claim is authorized. GIBBS, CREED, WAL, OZK, FLG, RED — information.

Sources: AGENTS/DEWEY/output/2026-11-11_003R-six-bank-refresh-partial.md (e14527103e) ; FFIEC CDR RetrieveFacsimile, 12 SDF responses retrieved by DEWEY 11/11 (research/2026-11-11_003R/six-bank-primary-rows.json) ; Eagle Bancorp 10-Qs 0001050441-26-000096, -000113 ; AGENTS/REGINALD/reports/2026-10-30_L801/REPORT.md, 2026-11-06_VLY-EGBN_10Q_reads.md
