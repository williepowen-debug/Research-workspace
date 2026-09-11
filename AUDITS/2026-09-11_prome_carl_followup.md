# PROME and CARL second-pair-of-eyes review — 2026-09-11

## Scope and disposition

Reviewed CARL commit `6a242eca9` and PROME's September 11 decisions, tools, completion receipts, and outgoing directives. The focused PROME pass included later work through `292882322`; executable fixes use the isolated `review/codex-20260911` branch based on `b1e4b6156`, after the earlier review commit `042e213de`. This is a sampled judgment review plus targeted mechanical tests, not certification of every research claim. The shared checkout remains active and was not edited.

**Assessment:** CARL shipped a useful protective check with working boot integration, but overstated both its historical diagnosis and what a clean result establishes. PROME generally preserved decision boundaries in the sampled closeouts, but made an actionable source-classification error and has another unknown-as-clean guard defect. Corrections and tests are on the review branch; communication and card wording below are reviewable proposals, not messages sent to desks.

## Findings, highest impact first

### 1. CARL can certify an unavailable BOARD, and misses legacy action labels — corrected

`AGENTS/CARL/scripts/board_gap.py` originally returned success when INDEX was missing or empty: its iterator yielded nothing and the final branch printed “no unrecorded ids.” A stale generated INDEX could also hide a newly published or rerouted action signal. This defeats the purpose of a blocking check. These are reproduced failure cases, not a claim that today's live INDEX was absent.

The action parser also compared exact recipient names after splitting on commas/slashes. Actual older rows use labels such as `CARL (action — CONSUMER_CREDIT / LABOR / AG-CREDIT-STRESS primary)`, which do not equal `CARL`. This is a real archive format; the reviewed snapshot has no currently unrecorded CARL action after normalization, so no additional live owed item is alleged.

Fix: unavailable/empty/duplicate or inconsistent inputs return visible UNKNOWN/rc=2; compare signal IDs, normalized action recipients, and precedence against BOARD records using WALTER's publisher parser; recognize parenthetical legacy annotations and info-only routes. Missing receipt ledger also returns UNKNOWN. An action gap still returns rc=1. No ledger is modified. INDEX disagreement requires publisher regeneration rather than a CARL-side rewrite. This intentionally adds a dependency on the publisher parser and may block boot while an index regeneration is pending.

### 2. CARL's new relevance rule sits under an unfed intake lane — card correction proposed

`AGENTS/CARL/CLAUDE.md` step 5b.2 requires checking signals against open predictions before assigning `noted` or `info-only`. But that step iterates `inbox/WALTER/`, which is unfed while CARL is exempt. Step 5, the actual whole-BOARD path, does not explicitly carry the new rule. Fixing the mtime sentence and the “both ledgers are live” sentence alone leaves this ambiguity.

A recorded ID proves a receipt exists. It does not prove the disposition was justified, a deferred action was completed, or a forecast-relevant signal was incorporated. Likewise, “none explicitly routed action:[CARL]” cannot establish “nothing analytically owed.” The revised console wording makes that limit explicit. Keep substantive disposition/relevance review in the live intake path. A counts-only closeout rider adds little; evidence of that substantive review still matters.

### 3. PROME overgeneralized CalculatedRisk's blog closure — correction draft below

Commit `f1a2b36c0` sent HOMER, CREED and DEWEY directives to mark live CalculatedRisk claims `[CalculatedRisk — DEAD since 2026-01-12; not a live feed]`. The blog endpoint stopped, but the publisher continued through newsletters. The blog's own farewell links the continuing publications. DEWEY's listed housing-distress artifact, line 94, already cites a February 9, 2026 article on `calculatedrisk.substack.com`, not the retired blog endpoint.

Evidence: [CalculatedRisk blog and farewell](https://www.calculatedriskblog.com/) and [February ICE Mortgage Monitor article, February 9, 2026](https://calculatedrisk.substack.com/p/february-ice-mortgage-monitor-home). These establish the endpoint/publisher distinction; they do not certify every downstream financial claim.

Proposed correction to the three recipients: “The January 12 retirement applies to calculatedriskblog.com as a regularly updated feed. Do not mark the whole CalculatedRisk publisher dead. Preserve dated citations; inspect each cited URL. Continuing newsletter citations require their own date and evidence checks. Replace a standing monitor only if its actual endpoint stopped or its coverage no longer serves the instrument.” No corrective message has been sent and historical packets remain intact.

### 4. PROME aged-waits advisory silently treats unknown activity as clean — corrected

`PROME/tools/prome_gate.py:check_aged_waits` delegates activity lookup to `decision_deck.days_dark`. That function can return None; the pure helper skips it, then the wrapper reports that no qualifying aged wait exists. Exception handling does not catch a valid None return. A mocked blocked BROCK row reproduced a green result with unknown activity. No claim is made that this happened in today's live output.

Fix: collect unknown activity for relevant, undated blocked rows, show the desk names, and make the advisory non-clean. Unknown still does not establish that a desk is aged or authorize a spawn. Future-dated exclusions continue to bypass activity lookup.

### 5. PROME's proposed ARGUS trial leaves its own final draft outside scope — revise before adoption

`PROME/reports/2026-09-11_sam-subagent-system-assessment.md` scopes review to paths already committed since the previous closeout, but schedules the auditor before the final commit. It also skips changes under three paths. As written, an uncommitted final closeout and a serious single-file error can escape review. This is a proposal defect, not a deployed auditor failure.

Proposed contract: review the prior-closeout-to-candidate diff, including explicitly identified pending PROME changes; record the reviewed candidate and advance the watermark only after findings are dispositioned. Avoid a path-count skip; use a stated low-risk exemption if necessary. In a shared checkout, identify PROME's candidate paths explicitly rather than absorbing other desks' dirty files. Grade the trial with audited exposure, severity, false positives, review cost, and residual defects after a consistent observation interval. “Before versus after” defect counts alone are not a comparable success rate.

## CARL's claims: what holds

- The guard is wired unconditionally in normal, quick, and skip-ABS modes. Offline integration tests verify a gap reaches boot's nonzero result and survives collapsed output. Other boot subprocesses were mocked; this does not independently reproduce the claimed 16.6-second network run.
- Removing two fixture receipts triggers rc=1 with the expected IDs and precedence; restoring them clears the guard and leaves the ledger byte-identical. This reproduces the behavior without disturbing CARL's real ledger.
- The reviewed snapshot contains 939 INDEX IDs, 754 receipt IDs, 185 unrecorded IDs, and zero explicit CARL action gaps. The quoted 181 backlog can reflect an earlier snapshot; it is not evidence of misreporting.
- The historical mtime explanation is too certain. Git can restamp files it rewrites, but does not rewrite every unchanged file. Sparse Date_Logged values show sparse recorded processing, not every historical gate decision or even every no-new-items scan. Neither PROME's “likely silencer” nor CARL's “always RUN” is demonstrated by the available record. The code comments now preserve that uncertainty.
- CARL's distinction between a peer request and Will's standing authorization is understandable. It was reasonable to ship protection while flagging the contradictory card. This review drafts the complete card correction below without impersonating Will's approval.

## Proposed CARL card wording

Replace step 5 with: **BOARD intake — every boot.** Run the unconditional BOARD gap check through boot.py. UNKNOWN or unrecorded action signals prevent a clean closeout. Diff the canonical BOARD records against board/BOARD_LOG.tsv and disposition unrecorded signals. Before noted/info-only, apply the existing open-prediction relevance rule here: a signal bearing on a registered series requires acted or deferred with a date. The script validates explicit action receipts; it does not substitute for this review. Do not gate the scan on filesystem mtime.

Reframe step 5b and the two-ledger sentence: **CARL is currently exempt from WALTER delivery; inbox/WALTER is unfed and an empty lane proves nothing.** board/BOARD_LOG.tsv is the active whole-BOARD disposition ledger. Retain board_log.tsv as the legacy delivery receipt record; use delivery-lane procedures only for actual received files or if the exemption changes. The prediction-relevance rule applies to every intake route.

Also update step 7.0's enumerated script list to include board_gap.py; the old seven-script description predates this addition. Preserve the existing user-approved relevance requirement rather than leaving it attached only to the dormant route.

## What PROME did well

Sampled WATT completion handling reflected the revised probability ladder and owner evidence. NEXUS's no-verdict outcome and exhausted successor gate remained explicit. HENRY's HEN-44 work stayed pending after CARL supplied input, rather than equating input receipt with resolution. OSPREY's completed drain was distinguished from the analytical questions registered for later work. Those are appropriate scope boundaries.

The earlier review's PROME ledger fixes remain on the same branch: preserve full rulings and content-only updates, reject an empty sealed ledger, permit distinct same-day events, and count receipt IDs in the proper column. See `AUDITS/2026-09-11_codex_review.md` for evidence and limits.

## Validation and delivery

PROME tool suite: 46 tests pass. CARL guard suite: 6 tests pass, including offline boot integration across three modes. The revised CARL guard also ran successfully on the real review snapshot. No live market pulls, trade actions, inbox messages, CLAUDE edits, or shared-checkout changes were made. The changes are a local review-branch follow-up to `042e213de`; they have not been pushed or merged.
