# CATO — BRENT/WALTER September 15 review

## Scope and assessment

Will asked to examine BRENT/WALTER updates and edits. Snapshot `8f5fa4ed47d66cb9804a5e2d69f9bcce038d3bba`; initial working tree/staging clean. Main scope: BRENT `027609b9c` (receipt/rig repairs and source work), `14d27e552` (five-area evidence review); WALTER `70a2bc593`/`f05cb5b20` (reading companion), `3fe9a55d3`/`68c60ed00` (closeout consistency), and delivery `b7a187129`. Earlier WALTER work is context, not an exhaustive re-audit. CATO did not author these owner implementations; this is independent review within the limits below.

Assessment: useful corrections and better uncertainty reporting, with one reproducible reader defect and two closeout reconciliation issues. No owner files, trades, thresholds, grades or messages changed. Fleet visibility was not established; clean Git state does not prove owner idleness.

## F1 — MEDIUM: missing current rig count can become a neighboring value

Source: `AGENTS/BRENT/scripts/instrument_check.py`, `probe_bhrigs`, lines 674–690; governing BRT-26-RIGS registry locator explicitly requires US Oil / This Week. The reader deletes blank cells, then treats the second surviving cell as the current count. Country and workbook-date validation do not establish column identity.

[Independent reproduction](2026-09-15_1821_brent-walter-probe.py) copies the first 60 rows of the saved September 11 publisher workbook into a small fixture and mocks network delivery. Headers: D=This Week, E=change, F=Last Week. Oil row: D=450, E=1, F=449. Control returns 450. Blank D22 alone and the reader reports **US OIL rig count 1**, success=true, September 11, BELOW/claim holds. A separate fixture with D blank and F=450 also returned the prior count as current.

Consequence: missing data can produce a false below-threshold result instead of failed coverage. The actual saved September 11 D22 is 450: this finding does not invalidate that observation/grade. Blank-cell compression predates the repair, so classify this as an unresolved hole, not a newly introduced regression.

Recommended BRENT repair: bind the count to the validated This Week column without compressing positional blanks; reject missing/non-integer/ambiguous cells. Add blank-current/nonblank-change and blank-current/nonblank-prior regressions. Preserve the frozen 457 line and historical grade. Not implemented by CATO.

## F2 — LOW: BRENT consumed mail remains unfiled with stale sender-state text

Sources: `AGENTS/BRENT/board_log.tsv:361–364`, SCRATCH mail state, and CLAUDE steps 6/13a. September 15 signals 005/006/007 have acted dispositions and substantive evidence but remain in live `inbox/WALTER/`. All five September 15 handoffs were committed in `b7a187129` at 15:25:02 ET. BRENT's 16:29:25 entries for 005/007 still say sender file untracked / archive pending sender commit. Its final report/SCRATCH acknowledge publication during the review but do not complete filing.

Initial deferral while sender files were untracked was legitimate. Later filing and log state disagree with completed consumption, risking misleading inbox scans. This does not mean the underlying research was absent; cargo quantities can remain unresolved after consumption.

Recommended BRENT action: correct the later explanation additively and file exact consumed handoffs under the existing recipient protocol. Keep remaining evidence work in SCRATCH/report. Apply existing triage rules to deferred 001/004 without inventing a resolved outcome. WALTER/CATO should not move recipient-owned processed files. No repair or owner response in this review.

## F3 — LOW: WALTER receipt needs reconciliation after the shared push

Source: `AGENTS/WALTER/LAST_COMPLETION.md` FOLLOW-UP/CLOSEOUT RECEIPT, pending state for `3fe9a55d3`. CATO's preceding confirmed push carried that commit and `68c60ed00`. The current receipt still says publication pending. WALTER's checker now correctly returns rc=1 REVIEW with exactly `3fe9a55d3: claimed pending, origin proves published`. Delivery remains 29/29; owner-evidence hashes match.

This is subsequent shared-push reconciliation, not a false original receipt or checker failure. The observation is explicitly dated. WALTER should refresh its current receipt/follow-up against fresh remote evidence and rerun its checker; historical RESULTS remain dated evidence. Not edited by CATO.

## Verified improvements and known limits

- Independently compared incident CSV revisions: exactly 12 rows changed; status, source tier and operating-evidence dates preserved. Seven obsolete amounts and Bazan's inconsistent typed amount were removed without declaring recovered supply. RF-014's two capacity fields become 346,000; a fresh [KNPC owner-page read](https://www.knpc.com/en/our-business/oil-refining/mina-al-ahmadi-refinery) supports that bpd figure. The undated page does not establish current operating state or historical pre-conflict configuration.
- Independently compared predictions against the pre-workdown revision: only BRT-26/BRT-29 Notes changed; first nine fields, including confidence, timeframe, status and invalidation, remain intact. Airline M stays indeterminate and final prediction OPEN. Evidence review is not a passed milestone.
- Cargo report preserves cancellations versus unknown barrels/duration, tenders versus arrivals, and the buyer's uninterrupted-delivery statement. Chart report retains closed-UNVERIFIED/source-metadata limits. Its displayed-number arithmetic agrees: 124.59492 − 106.36 − 18.25626 = −0.02134, outside its 0.005010 rounding allowance. Source/market-price identity is not established by that arithmetic.
- WALTER's companion guard passes current source/companion/review hashes, the 21,889-byte size and September 30 deadline. An independent preservation receipt exists. CATO reviewed guard code/tests and receipt scope, but did not repeat the complete 11-obligation/13-qualification semantic census or revalidate historical financial claims.
- WALTER's closeout checker detects the actual stale publication state and explicitly limits its verdict to declared evidence/local origin. Owner completion and arbitrary prose remain human judgments.
- Owners disclose remaining incident operating-state, airline dating, cargo-volume, TRADE rotation, remote Friday COT installation, ACTION-completion and primary-source gaps. BRENT also records a FORGE legacy-capacity consumer mismatch in NEXUS. These are not silently cleared or newly assigned here.

## Executed checks and disposition

**40 existing isolated tests passed:** BRENT receipts 12, rig reader 7; WALTER closeout 11, companion 10. Independently devised and executed F1 counterexamples, including the preserved publisher-layout reproduction. Ran current WALTER closeout/companion checks; independently checked CSV structure and unchanged fields. Reviewed selected source reports/receipts and publication lineage against the origin ref freshly fetched in CATO's prior push. This is not a full desk boot, broker reconciliation, exhaustive external-source audit, or rerun of every earlier owner suite. No owner test count substitutes for tests run here.

Findings remain unresolved; recommended fixes are not implemented. No owner response requested or received. Durable delivery is this report and Will's session receipt, without external sends. At closeout commit exact CATO evidence/continuity paths and verify push; final hash is delivered in-session. Next startup: orient and await Will. If follow-up is assigned, begin with F1's reproduction, then F2/F3. Existing publication and CATO/RAV integration boundaries are unchanged.
