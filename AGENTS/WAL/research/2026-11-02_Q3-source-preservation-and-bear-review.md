# WAL — Q3 source preservation, bounded hot-state proposal, and bear review

**Date:** 2026-11-02. **Scope:** Will requested durable primary-source preservation, a proposal for a smaller current-state reading path, and a Q3 research synthesis. No archive rotation is implemented here. No thesis weight, score, frozen grade, prediction, position, or historical record changes.

## 1. A retrieved primary document is not the retrieving desk's interpretation

WALTER's `research/2026-10-31_call-report-read/REPORT.md` and `VERIFY-BASIS.md` are WALTER's synthesis and verification judgments. They are not a substitute for WAL's independent FFIEC extraction. `selected-primary-rows.tsv` preserves exact selected source rows, but it is an extract, not the complete filing.

A complete primary document retrieved by another desk would be acceptable input for WAL's independent extraction if WAL can verify the original bytes and parse them itself. The minimum provenance is:

1. The complete, unmodified FFIEC SDF document at a durable, non-temporary path.
2. Source endpoint and facsimile format.
3. Reporting period `20260930` and WAL bank RSSD `3138146`, also validated inside the document rows.
4. Retrieval timestamp and retrieving desk.
5. SHA-256 and row count, so the preserved bytes can be matched to the retrieval receipt.
6. No credentials in the document or receipt.

WALTER's receipt supplies the expected Q3 identity: FFIEC `RetrieveFacsimile`, SDF, RSSD 3138146, period 20260930, retrieved `2026-11-01T02:18:33.515051+00:00`, **1,792 rows**, SHA-256 **`2e04cc7bf1a78e525a68059c358215c8ce9e3c24c3639d84ea74ccb8d69c60a4`**. A recovered document matching that receipt could support WAL's own extraction.

### Survival check and conclusion

- WALTER's recorded raw path `/tmp/walter-call-report-availability-6guvqyx_/WAL_20260930.sdf` is missing.
- No `*20260930*.sdf` copy exists anywhere under the repository, including ignored source paths.
- WAL's `sources/ffiec_2026-11-02/` contains only failed-retrieval receipts.
- The two preserved WAL Q3 selected rows are RCON2746 and RCONJ454. **RCON1766, the MI3 denominator, is absent.** The extract therefore cannot complete the MI3 calculation even for the selected fields.

**Disposition:** Q3 MI3 and the associated bank-level extraction remain **UNCHECKED**. No Q3 MI3 ratio, NDFI integration, or MI3 data row is created. The existing assignment remains a retry of WAL's verified FFIEC retrieval into a dated `sources/ffiec_*` directory, followed by independent extraction. For future cross-desk retrieval, preserve the complete SDF beside a tracked receipt; a narrative summary alone never satisfies this assignment.

## 2. Bounded maintenance proposal — not implemented

The objective is a smaller hot reading path without creating a new queue, checker, cadence, or ownership structure. Move dated material verbatim into dated files under `archive/` and leave one-line pointers. Preserve all live rules and open obligations in the existing hot files.

### `STATUS.md`

Archive verbatim:

- The entire superseded **BOTTOM LINE (2026-10-28)** section.
- The dated 10/22 paragraph beneath **JUDGMENT**; retain the current 10/30 judgment.
- The completed **Q3 FROZEN-FRAME GRADES** table, with a pointer to the unchanged Stage-1, Stage-2, and Q3 10-Q grade artifacts. Current outcomes and open legs must remain in the live bottom line, convergence matrix, exit rules, and next carriers.
- From **LATEST (10/28)**, only completed process/history rows: `Re-score rule Amendment 1`, `10-Q frame dry run`, `Workbook update`, `Market tracker built`, `Core files folded`, `Q3 10-Q`, `L171 10-Q frame`, `Boot kit`, and `Housekeeping`. Their artifacts and current obligations remain linked, not deleted.

Keep live:

- The current bottom line, live price, current judgment, and **FIVE THINGS THAT MATTER** print snapshot.
- Current evidence rows whose facts are not merely session history, including the $99M prior, NDFI, courts, ratings, leadership, and source blocks.
- **OPERATOR DEPENDENCIES**, **CONVERGENCE MATRIX**, **EXIT RULES**, **NEXT CARRIERS**, and **OWNERS / CONTINUITY**.
- The Q3 10-Q NO-VERDICT, final WAL-01/WAL-02 outcomes, Bear-medium kill state, Q3 FFIEC UNCHECKED state, and all delivery/ownership rules.

### `MEMORY.md`

Archive verbatim the entire **Prior session notes — October 30 2026 evening** section through the end of the file, including its nested 10/30-afternoon and 10/28 handoffs. Leave the current November 2 handoff at the top plus a pointer to the archive.

Before that rotation, carry forward by pointer or a concise live line every still-open item: Q3 FFIEC retrieval; score re-judgment; Q4 predictions due 11/15; hotel read; expired KB rows and the queued DEWEY packet; operator dependencies in STATUS; the earnings-reclassification caveat; and the three carried research proposals that still require Will's go. Completed session narratives and superseded next-session lists do not remain hot.

### `CLAUDE.md`

Archive only dated implementation anecdotes, not operating rules:

- The 8/20 KB-expiry origin statistics in boot 4b; retain the command, individual-judgment requirement, and prohibition on bulk re-dating.
- The 8/20 MI3 drift example in boot 4c; retain source-of-truth, scanning, limited-scope, retired-claim, and inbox-lane rules.
- The 126-day prediction-history anecdote in boot 4d; retain the command, OVERDUE-is-not-a-grade rule, blank-cell warning, and anchor-type requirement.
- The session-#1/NEXUS-audit origin story in the close checklist; retain mandatory NEXUS last-write behavior, STATUS-hash pinning, and commit order.
- Promotion history already preserved in the linked promotion review; retain WAL's identity and domain.

Also de-version stale ownership labels such as `v2.4` and replace the completed `L171 awaiting the 10-Q` file description with neutral ownership language. Do not archive or weaken runtime verification, boot commands, inbox distinctions, delivery, exact-path Git, output, document-ownership, domain-scope, cross-agent signal, or closeout obligations.

No rotation is proposed for **THESIS.md**, **POSITIONS.md**, or **NEXUS_BRIEF.md**. Frozen grading/re-score documents and historical evidence remain untouched. THESIS owns thesis/weights, POSITIONS owns broker-backed positions, STATUS owns current state, MEMORY owns the current handoff, and NEXUS remains the mandatory final delivery brief.

## 3. Q3 facts that most weaken the WAL bear case

These are observed favorable or disconfirming facts, not missing evidence:

1. **The two registered near-term credit predictions failed.** Office classified assets were $272.75M against the >$500M WAL-01 test, and the 10-Q cross-check passed exactly ($926M classified loans + $165M OREO = $1,091M). Net charge-offs were $45.8M / **30bps**, below the >40bps WAL-02 test, with no Q3 fraud exclusion identified. Both invalidations are final under the frozen process (`2026-10-30_Q3_10Q_GRADE.md` §0–§3).
2. **No new Office migration was identified while the topic was addressed.** That is the second broadening disconfirmation, not proof that no loan migrated. It weakens the claim that the original life-science event was immediately propagating through the Office book.
3. **Problem-loan stock improved on several bases.** Nonaccrual loans fell $562M → $485M; full NPL fell $781M → $672M; accruing restructured loans fell $164M → $129M. Classified loans fell $1,002M → $926M. Nonaccrual plus OREO still fell $688M → $650M after accounting for foreclosure transfers.
4. **Loss absorption strengthened.** Funded plus unfunded ACL reached $574.4M, **118.4% of nonaccrual**, from 96%. Q3 included a $35.0M loan-reserve build above net charge-offs; the coverage improvement was not produced by a provision release.
5. **The earnings engine did not collapse.** EPS rose $2.36 → $2.45, NII rose $796.9M → $807.6M, NIM rose 3.53% → 3.57%, and reported PPNR rose $412.4M → $419.1M. The consistent visible-gain screen was nearly flat, so this is a modest offset, not a clean acceleration.

These facts justify the completed v2.5 rule application. They do not establish a broad credit all-clear or justify another discretionary weight change.

## 4. Observed adverse evidence — distinct from missing evidence

| Observed Q3 fact | How it could hurt earnings or capital | Next observable evidence that distinguishes outcomes |
|---|---|---|
| **Hotel franchise finance criticized $75M → $185M; classified $44M → $75M; special mention $31M → $110M.** HFF grew $4,582M → $4,912M; nonaccrual and charge-offs remain $0. | Migration can become provisions, charge-offs, and capital loss. At present it is an early-warning/building-concentration observation, not a realized hotel loss. | Named loan-level status, HFF nonaccrual and charge-offs, ACL, criticized balance, and collateral/LTV at Q4. Adverse: migration to nonaccrual or losses. Favorable: criticized balances cure or exit without new nonaccrual/loss. |
| **OREO $126M → $165M and 22 → 27 properties; $36M taken, primarily one office property.** Q3 OREO valuation losses were $0. | Foreclosure replaces a loan with an asset whose sale proceeds and carrying value can still deteriorate; future valuation losses hit earnings and capital. | Property-level sale proceeds versus carrying, valuation allowance/losses, new possessions, and OREO count/dollars. Adverse: further possessions plus valuation losses. Favorable: OREO declines through sales at or above carrying. |
| **Special mention $316M → $397M and problem loans $755M → $838M.** | These are larger early-warning stocks that can become future nonaccrual and provisions. They are not themselves charge-offs. | Named migrations among special mention, classified, nonaccrual, and cures. Adverse: continued SM growth plus classified/nonaccrual conversion. Favorable: SM falls through documented cures/payoffs rather than foreclosure. |
| **AOCI −$451.2M → −$785.5M; AFS gross unrealized loss $686M → $1,223M; TCE $6,906M → $6,720M; TBV $63.24 → $62.22; parent CET1 11.0% → 10.9% preliminary.** $92.1M of buybacks also consumed capital. | Further securities marks and distributions can outrun retained earnings and reduce tangible/regulatory capital. AOCI and regulatory CET1 effects must not be treated as interchangeable. | Q4 AFS marks/AOCI, TCE/TBV, CET1, RWA, hedge coverage/duration, and buyback dollars. Adverse: another large mark plus lower CET1/TBV. Favorable: stable or reversing marks with earnings rebuilding capital. |
| **NII growth guide cut 12–14% → 11–12%; operating expense ex deposit costs $404.1M → $429.7M; mortgage banking $84.7M → $79.5M. Preferred reset raises annual dividend cost by about $12.3M.** | Lower NII, weaker servicing, persistent costs, and preferred distributions can reduce common earnings even if credit losses stay low. | Q4 NII versus $807.6M, ex-deposit expense versus the literal ≤$405.1M guide residual, mortgage revenue versus the ~$70M call indication, and a comparable fee/MSR bridge. Adverse: cost persistence plus NII/fee shortfall. Favorable: the stated cost step-down and fee offsets materialize. |
| **NDFI dollars rose $15,812M → $15,832M despite the share falling 25.9% → 25.7%. Mortgage-credit intermediaries were $10,768M.** | Exposure remains large and can transmit borrower stress into provisions/losses. Exposure growth alone is not evidence of stress. | Durable Call Report extraction plus NDFI nonaccrual, charge-offs, modifications, unfunded draws, and borrower attribution. Adverse: rising nonaccrual/losses. Favorable: stable credit performance despite exposure. |

## 5. Missing or unresolved evidence — not adverse evidence by itself

| Unknown | What Q3 actually establishes | Next observable evidence |
|---|---|---|
| **$99M life-science loan** | It disappeared from the release, deck, call, and 10-Q. NO-VERDICT is mandatory. Other CRE-NOO nonaccrual fell $106M, but that is an unnamed net movement, not a cure. No below-book-appraisal tell appears in the aggregate allowance tables. | At the Q4 call/10-K: named status at 9/30, appraisal value versus carrying, reserve, charge-off, sale/payoff/OREO/cure, and cash proceeds. An at/above-carrying appraisal with a documented benign exit differs fundamentally from a below-carrying appraisal, continued nonaccrual, or an undisclosed pending appraisal. |
| **Cantor residual and recovery** | Q3 states no new charge-off or recovery and drops Q2's sentence saying no additional charge-offs. That is narrowed disclosure, not a new loss. The $64M PCD purchase remains untied to Cantor. | Named residual, allowance, senior-lien facts, charge-off/recovery, and court outcomes. Silence remains unresolved; a disclosed charge-off or lower recovery would be adverse. |
| **Q3 MI3 and bank-level NDFI/capital fields** | WALTER's receipt establishes that a document was retrieved, but no complete durable copy survives. WAL cannot compute or verify the required ratio from the surviving extract. | Retry the existing FFIEC assignment; preserve the full SDF and receipt; independently extract RCON2746/RCON1766, RCONJ454, and the approved fields. Missing is not zero and not a pass. |
| **Securities hedge effectiveness/duration and exact capital bridge** | The 10-Q shows shrinking hedged AFS and terminated Treasury hedges, but no effective-duration figure. Exact RWA and detailed adjustments are not supplied by the rounded parent CET1 ratio. | Detailed Q4 hedge, duration, RWA, and capital reconciliation. Do not infer either protection or incremental loss from missing duration. |
| **Recurring fee, MSR, expense, and tax bases** | Q3 cost growth and servicing decline are observed adverse facts. Guide exclusions, MSR mark/hedge detail, cost reversal, and forward provision/tax/share assumptions remain unknown. | A dollar reconciliation of the fee guide and Q4 actuals; MSR cash/runoff/mark/hedge bridge; quantified temporary costs; provision and tax bridge. Unknown basis is not a guide miss. |
| **Management's $567M NPL basis** | The Q3 filing supplies $485M nonaccrual and $672M full NPL but no definition producing $567M at Q2. | A management definition/reconciliation, if offered. Until then it is an unexplained basis, not evidence of hidden loans. |

## 6. Research judgment

**Q3 materially weakened the near-term credit bear:** the registered Office and charge-off tests failed, broadening received another disconfirmation, problem-loan measures improved, and reserve coverage rose without a provision release. The strongest remaining bear evidence is not those failed predictions; it is the observed hotel/OREO/special-mention build and tangible-capital pressure.

The $99M loan, Cantor residual, MI3, and several earnings bridges remain **missing or unresolved**, not adverse findings. The next decisive evidence is named loan disposition/appraisal data, hotel and OREO flow/loss data, Q4 capital and recurring-earnings reconciliation, and a durable full Call Report. This synthesis changes no registered weight, score, target, frozen grade, prediction, or position.

## Sources

- `research/2026-10-30_Q3_10Q_GRADE.md` — primary Q3 10-Q grade and final frozen-frame outcomes.
- `research/2026-10-19_Q3_FULL_READ.md` and `2026-10-19_Q3-recurring-earnings-bridge.md` — saved issuer release/deck analysis.
- `research/2026-10-21_Q3_STAGE2_CALL_GRADE.md` — B2 call evidence and limitations.
- `AGENTS/WALTER/research/2026-10-31_call-report-read/{REPORT.md,VERIFY-BASIS.md,retrieval.json,selected-primary-rows.tsv}` — other-desk interpretation, provenance receipt, and selected source rows; not WAL's full primary document.
- `sources/ffiec_2026-11-02/retrieval_20261102T161526805643Z.json` — WAL's latest failed direct retrieval.
