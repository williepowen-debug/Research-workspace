# OZK Data Staleness and Integrity Sweep

**Date:** 2026-11-02  
**Scope:** Live OZK documents, subdomain status files, workbook ledgers, and current research surfaces. Archive and processed-inbox material were treated as historical records, not current-state defects.  
**Mode:** Audit only. No analytical figures, predictions, scenario weights, positions, or inbox states were changed.

## Bottom line

The workbook is structurally healthy, but several live surfaces disagree with canon or have not absorbed available Q3 evidence. The highest-value work is not another broad re-read: it is a bounded propagation pass led by the Q3 Call Report, followed by correction of the scoring-card, position, scenario, geography, insider, and private-credit surfaces.

Six material findings:

1. **Q3 Call Report evidence is available but absent from OZK's workbook.** The local series still ends at Q2 and says the next pull is due 11/10.
2. **Several current-state statements are affirmatively wrong, not merely old.** These include the Q3 card's “PRE-PRINT” and LOW-re-grade “not applied” labels, `POSITIONS.md`'s frozen-trade/v1.5/August-RaDD statements, and `SCENARIOS.md`'s “book is empty” language.
3. **The San Francisco regulatory-district conclusion needs correction.** WAL's correction shows the prior NCO comparison was consumer/card-dominated, not evidence of fast CRE transmission.
4. **`INSIDERS/STATUS.md` and `PRIVATE_CREDIT/STATUS.md` still carry superseded assessments.** Their headlines and next steps can mislead a cold reader despite later Q3 evidence elsewhere.
5. **Workbook mirrors have drifted.** `KB_INDEX.md` says 263 rows versus 269 actual and repeats two retired claims; `INDEX.md` still describes predictions OZK-01–09 rather than OZK-01–12.
6. **160 ACTIVE KB rows have a `Stale_By` date before 11/2.** This is a review backlog, not evidence that 160 facts are wrong; historical rows need disposition, not mechanical rewriting.

## Priority 1 — Missing evidence and decision-risk contradictions

### 1. Q3 Call Report has not been integrated

`workbook/CALL_REPORT_SERIES.tsv` has 18 rows through 2026-06-30 and retains `next_due=2026-11-10`. WALTER's 11/1 report at `AGENTS/WALTER/research/2026-10-31_call-report-read/REPORT.md` already supplies Q3 bank-level observations:

- Bank equity −2.07%; AOCI deterioration $214.631M.
- CET1 11.80% → 11.45%.
- Deposits +2.44% / +$0.831B; loans +$1.574B.
- Borrowings approximately $0.734M → $750M.
- Nonaccruals $300.416M → $89.117M.
- Quarterly NCOs $56.254M → $44.453M.
- Bank income $168.361M versus $167.371M.

Most of the credit data is contrary evidence for the residual bear case; AOCI and funding are incremental risk information. None of it has been used to move a grade in this audit.

**Still missing:** WALTER's report does not provide the exact `RIAD5409` observation required to resolve invalidation 8 / OZK-10. That requires the same-day FFIEC series pull by the pre-registered 11/16 check date.

### 2. Q3 scoring card is stale and incomplete

`workbook/Q3_2026_SCORING_CARD.md` currently says:

- Line 5: `PRE-PRINT — NO Q3 OBSERVATION GRADED`.
- Line 136: the LOW-conviction re-grade was “not applied,” although Will approved it 10/22 under WQ-483.
- Line 122: “public repo,” although repository visibility was checked 10/22 and found PRIVATE.

The card also lacks available Stage-1 workout observations already recorded in `research/threads/2026-10-21_Q3_PRINT_STAGE1_GRADE.md`:

- W3/W4 Seattle OREO: $56.1M / $48.5M, no sale.
- W5 Atlanta: $36.6M, leasing interest only.
- W13 RESG: $1.65B repayments; $25.4B commitments.
- W14: 50 Q3 modifications, 711 over 17 quarters, and $1.5B additional sponsor support ($956M reserves + $581M paydowns).

This is the clearest workbook-completeness gap: the evidence exists locally but has not reached the scoring surface.

### 3. Position and scenario surfaces contradict current canon

`POSITIONS.md`:

- Line 5 says `TRADE.md` remains frozen; `TRADE.md:1` shows it was unfrozen 10/22.
- Line 55 still calls the thesis v1.5 and RaDD's Aug-2026 maturity the unresolved core catalyst. Current canon is v1.7 with an executed extension to Dec-2029.
- Its “LIVE” table is the older 10/7 capture, not the latest 10/22 mirror in `STATUS.md`.
- Minor broker-basis mismatch: $322.66 here versus $322.65 in `STATUS.md`.

`SCENARIOS.md`:

- Line 172 says “The book is empty,” despite the mirrored Nov-20 $40P ×4 position. This should be scoped only to the dead historical option legs.
- Line 257 still describes the current book as stale/not managed.
- Lines 234–244 retain expired decision gates without a sufficiently clear dead-surface banner.

These are current-state labeling problems; they do not require a new trade view.

### 4. Geography contains a substantive comparison error

`GEOGRAPHY/REGULATORY_DISTRICTS.md:132,161-175` still asserts San Francisco “fast transmission.” The unprocessed WAL correction at `inbox/2026-10-28_from-WAL_SF-district-NCO-is-consumer-card-not-CRE.md` shows:

- SF's 1.13% FY2025 NCO rate was a total-loan measure, approximately 83% individual loans and 61% cards.
- Comparable CRE NCO was 0.14% versus 0.22% nationally.
- Noncurrent CRE was 0.90% versus 1.30% nationally.

The Dallas PDNA-minus-NCO comparison also mixes a stock with an annual flow. This needs analytical correction, not just a date refresh. The inbox item was deliberately left unprocessed during this audit.

`GEOGRAPHY/STATUS.md:46` also points to KB-177 although KB-268/269 superseded it on 10/28.

### 5. Insider and private-credit status files retain superseded judgments

`INSIDERS/STATUS.md` remains a July/pre-Q2 surface with “FULL CONVERGENCE (Score 13) — Maximum bearish signal,” conflicting with the current v1.7 LOW thesis. Its “Next” section still refers to the pre-Q2 window. Root `STATUS.md` has the later 10/22 FDIC EFR read: no filing after 8/14 and zero open-market buys from 7/6 through 10/22.

`PRIVATE_CREDIT/STATUS.md` mixes newer Q3 updates with stale body text:

- Line 17 calls the 10-Q and Call Report “independent filings”; current canon says they report the same classification twice, not independent confirmation.
- Line 21 says the 2025Q3 MI3 step remains unresolved despite the 9/24 adjudication.
- The body emphasizes The Jack as a casualty without local Q3-cured context.
- “NDFI noncurrent only $2.7M,” “9 funds gated,” Q2 catalysts, and “Monitor Q1 10-Q (~May 5)” are stale current-surface content.

## Priority 2 — Live-document drift

### Thesis and invalidation state

`THESIS.md` correctly carries v1.7 LOW in its header, but:

- Invalidation 4 still ends its check at 10/22 rather than recording the completed 11/2 sub-notes sweep.
- Invalidation 8 still treats the Call Report as unavailable.
- Lines 212–220 carry short interest of approximately 16.0% at 8/31, versus current `STATUS.md` at approximately 18.6% at 10/15 with DTC 9.2.

Older narrative sections are not automatically defects where they preserve dated evidence, but the invalidation-state table is an operational surface and should reflect completed checks.

### Index and calendar mirrors

- `INDEX.md:4` says last updated 10/22 while containing 10/28 KB changes.
- `INDEX.md:31,75` describes predictions OZK-01–09 rather than OZK-01–12.
- Its Call Report map says 18 quarters; this becomes 19 after Q3 integration.
- `CALENDAR.md:3` still says Last Updated 10/28 even though its 11/2 sub-notes row was updated.

### Prediction and handoff notes

- `workbook/PREDICTIONS.tsv` OZK-09 notes retain “weighted EL $140M … stands as ULTIMATE/lifetime EL.” Current canon is approximately $129M pre-outcome EL; $140M survives only as OZK-09's recognition threshold.
- The prediction ledger's last re-pull attestation is 8/28 and covers only nine rows. It no longer covers the current 12-row ledger.
- `MEMORY.md:38` still says `boot.py` is blind to `inbox/WALTER/` and T1 is owed; `TODO.md` says T1 was fixed 10/22.

## Priority 3 — Workbook hygiene and refresh backlog

### KB ledger

Structural checks passed:

- 269 rows, 13 columns, no bad-width rows.
- No duplicate IDs or ID gaps; maximum ID 269.
- 37 groups.
- Status counts: 254 ACTIVE, 8 SUPERSEDED, 2 REFUTED, 2 CORRECTED, 1 ACTIVE_PARTIAL, 2 LIVE.

Refresh and mirror issues:

- **160 rows marked ACTIVE have an ISO `Stale_By` earlier than 2026-11-02.** This is a stale-review queue. Historical facts may merit ARCHIVED/SUPERSEDED treatment or a deliberate timeless/refresh disposition; the count must not be read as 160 false claims.
- `workbook/KB_INDEX.md:3` says 263 rows versus 269 actual.
- `KB_INDEX.md:32` repeats the corrected “ACL 1.16% < NCO 1.18% reserve inversion.” Current canon says the like-for-like ACL figure was 1.26%, so there was no inversion.
- `KB_INDEX.md:33` repeats the removed, unverified “$13.8B 2022 vintage.”
- `KB_INDEX.md:26` ends insider coverage at 7/20.
- `KB_INDEX.md:65` still calls the Q3 card pre-print.
- `workbook/README.md:23` lists only nine groups despite 37 actual groups and does not document every status currently used.

### Other workbook files

- `workbook/PREDICTIONS.tsv`: 12 rows, five RESOLVED and seven OPEN, IDs OZK-01 through OZK-12; structural checks passed.
- `workbook/2026-10-12_CASH_RECOVERY_BASELINE.tsv`: 14 rows and 12 columns, structurally clean and intentionally frozen. It is not stale merely because Q3 occurred; actual Q3 observations belong in the scoring card.
- All checked workbook TSVs have consistent column widths and no duplicate first-column IDs.

## Known gaps and intentionally dated material — not new defects

These should remain visible as limitations, but should not be “fixed” by silently rewriting history:

- The Q3 10-Q is not yet in the local raw set as of this sweep; its expected early-November filing remains an upcoming input, not a missed historical integration.
- Exact Q3 `RIAD5409` remains unavailable locally until the direct FFIEC pull.
- RaDD's current lease census, recognition attribution, and some redraw/capital-provider terms remain unknown.
- `IQHQ_PLAYBOOK.md:93` explicitly says its Q1 lab-market severity-comp data have not been refreshed; this is a declared research gap (C4).
- `LIFE_SCI/STATUS.md` is current through Q3, but its lab-vacancy market data are explicitly not refreshed since March 2026.
- `GEOGRAPHY/EXPOSURE_MAP.md` is Q1-vintage and `FL_PARADOX.md` is March-vintage; both are dated limitations rather than hidden current-state claims.
- `SEVEN_CREDIT_DEEP_DIVE.md` points cold readers to the Q3 roster and labels its Q1/Q2 math and old follow-up checklist as historical. Its outstanding R1 re-derivation is a known research obligation, not a newly discovered contradiction.
- `TRADE.md`'s retracted 37.6% and old entry rationale are explicitly bannered historical records.
- `CHANGELOG.md`, `MAINTENANCE.md`, archive documents, and processed-inbox files legitimately preserve old figures and decisions.

## Integrity checks that passed

- Weekday/date validation passed on `CALENDAR.md`, `STATUS.md`, `PREDICTIONS.tsv`, and both Q2/Q3 scoring cards.
- Inline local-link scan over non-archive, non-processed OZK Markdown found **zero missing targets**. Backtick-only references were not validated by that scan.
- Workbook TSV schema and duplicate-ID checks passed.
- `scripts/ledger_staleness.py --nudge OZK` flagged KB behind two STATUS writes, Call Report behind four but scheduled, and PREDICTIONS behind six/event-driven. This audit alone does not earn a KB row.

## Recommended remediation order

1. **Integrate the Q3 Call Report**, then pull exact `RIAD5409` from FFIEC and resolve the OZK-10/invalidation-8 check by 11/16.
2. **Repair current-state contradictions** in the Q3 scoring card, `POSITIONS.md`, `SCENARIOS.md`, and the thesis invalidation-state table; append the already-available Stage-1 observations.
3. **Apply the geography correction and refresh INSIDERS/PRIVATE_CREDIT**, including their headlines and next steps rather than only adding new banners.
4. **Synchronize workbook and entry-point mirrors**: KB_INDEX, INDEX, PREDICTIONS notes/attestation, CALENDAR header, and MEMORY's retired T1 statement.
5. **Triage the 160-row KB stale-review queue by evidence type**, separating timeless historical facts from live claims that genuinely require re-pulling.
6. **Only then schedule optional deep-dive refreshes** such as lab-market comps and the already-logged R1 re-derivation.

No remediation was performed under this audit-only assignment.
