# Current-state improvement review — October11

Requested by Will: investigate duplicated current-state prose, the immediate resume path, approval versus completion, and consuming existing evidence before new machinery. This is a bounded evidence review, not the full WQ411 spine audit or authorization for a new platform. Baseline54748614c.

## Findings and concrete design

| Claim | Exact artifact | Verification | Observed result | Proposed change |
|---|---|---|---|---|
| Current decision prose is copied across multiple homes | STATUS header; SCRATCH next-session block; BRIEF final POSITION; HANDBOOK top priorities; WQ418/420 ruling | Read current four surfaces and ruling side by side | VERIFIED: all carry approval/implementation status separately; latest broker reconcile copied the same account/expiry summary into several surfaces. WQ_EXPLAINERS409 still says eventual decision is Will's although418PASS is recorded. | One task status in its existing ruling/DOCKET; other surfaces point to it. Generate only fields already structured, retain human judgment/caveats in BRIEF. No new ledger. |
| Resume path is crowded by history | SCRATCH next-session section; HANDOFF Resume/dated entries; BOOT steps1,2,4 | Read first section and boot read contracts | VERIFIED: SCRATCH presents two October10 closeout narratives before its first-actions paragraph. HANDOFF requires a whole read, so moving an old entry below the fold alone does not reduce boot context. | Keep SCRATCH first screen to current priorities, blocker, owner, next action and source; move completed-session narrative verbatim to an existing dated archive with a checked pointer. Respect whole-read boot rules; changing those is a separate procedure edit. No obligation discarded. |
| A single progress chain would merge different facts | WQ418/420 ruling; WQ414/409/419 accepted receipts; DOCKET680–687; ORCH_LOG | Compare approval, commit, verification and actual receipt evidence | VERIFIED:414implemented/verified/ownerclosed but peer consumption unknown;420approved, owner has consumed instruction, implementation blocked;418PASS is final operator decision but downstream VIOLET receipt unknown;347/397 evidence asks closed while TERRY booking remains pending. | Display independent fields: decision; owner implementation; independent verification; recipient consumption; closeout. Receipt is not necessarily the final stage. Use existing records, no aggregate DONE unless named obligations complete. |
| Newer owner grades exist while PROME's mirror is old | GATES selected6rows against committed LIQUID STATUS1ac09fc05, HOMER STATUS10d0d1d79, REG_T02_EXIT_LOGf16be8011 | Read exact owner state tables/log rows and committed source diffs | VERIFIED source-to-mirror lag; proposed six rows below. No verdict flips; several observation vintages advance. | Consume those owner grades with original source basis and observation date. Do not regrade, change rule/deadline, or certify fresh market data. |

## Why pointers first, generation second

The existing code already chooses structured owners for queue, dates, holdings and gate state. `will_brief.parse_brief` uses the last repeated named section, so old BRIEF text still burdens source readers even when not displayed. `will_handbook.parse_handbook` discards everything before the first `##`, then renders the entire Top priorities body; its dated old priorities remain on the page. Thus a fresh preamble alone is not a reliable rendered correction. VERIFIED at functions parse_brief, parse_handbook and render Top priorities; redesign must test both file-reader and rendered views.

Proposed ownership: WILL_QUEUE/ruling = operator decision; DOCKET = remaining obligation/owner/date; existing task/ruling receipt = implementation and verification evidence; ORCH_LOG = actual closeout ask/receipt; FORGE = holdings with broker vintage; GATES = attributable owner grade with its vintage. SCRATCH is the immediate resume index. STATUS is system condition/backlog pointers. BRIEF is dated interpretation, not another task ledger. HANDBOOK is stable operating guidance plus links/generated sections. These are proposed writing boundaries, not a new authority rule or root-file edit.

Minimal pilot: replace only SCRATCH's current resume prose with a short index backed by existing records; archive old closeout narrative without losing active obligations or changing generated blocks. Validate from a fresh read and the existing page parsers before expanding to other files. Do not start by building a four-file synchronization engine. Keep approved L675/L628/L676 sequence unless Will deliberately reorders it.

Non-operational example of the first screen:
- Next position action: QQQ Oct12 call; TERRY card pending runtime permission; L685 and committed packet84a43c362.
- Approved but unfinished: WQ420 owner encode/independent result pending; exact ruling pointer.
- Operator decisions: generated WILL_QUEUE view, never a copied list.
- Domain work: generated DOCKET and required direct owner calendars, with one source link per obligation.
- History: last closeout/archive link; prior clock and liveness statements never presented as current.

Independent verification remains N/A where existing policy does not require it; this display does not add a review duty to every action. A delivered file is evidence of delivery, not proof of acceptance; an old closeout receipt does not cover a newly commissioned continuation. Runtime approval is also separate from research authorization.

## Immediate bounded evidence catch-up

Six proposed GATES state/last_checked updates are specified in `PROME/plans/2026-10-11_existing-grade-catchup.json`. No other gate cell, owner file, threshold, consequence, review date or leading state token changes. Preserve each superseded full row verbatim in a dated GATES_STATE_HISTORY archive with measure.py receipts. This is domain-evidence registrar maintenance, not process instrumentation.

- WAL exit: owner log already has settled10/8$75.50 and10/9$74.27, remains0of3; mirror stops10/7.
- HY re-kill: owner10/9 says0of2, HY315 at10/8/latest-revised; mirror312 at9/30/first-published. Carry latest-revised distinction and explicitly do not certify the gate's required first-published vintage anew.
- LIQ072: owner10/8 cell IG82/basis233/latest-revised, NOT FIRED; mirror9/30 IG84/basis228. Unsourced issuer/event legs stay UNGRADED; SpaceX stays CANNOT-FIRE.
- LIQ076: owner10/9 W1 asof10/6 net−2,353,716, week+56,627; W2asof9/30 G10−9,570/G5L10+847;1of3 NOT MET. W3 latest witness intraday, not a certified close; no re-arm/no second write-up. Boot-instrument gap remains.
- LIQ079: owner gate table grades SOFR99−IORB+6bp at10/7, NOT ARMED. Separate funding paragraph has newer+5at10/8; do not silently substitute it for owner's explicit grade. FIRE legs remain CANNOT-FIRE pending bands/base rate10/31.
- HOMER: owner10/2 bounded review carries PMMS10/1 7.28%, A2kill0of4, thesiskill0of5. Other legs lack new prints; formal grade11/20 unchanged. This does not discharge newer overdue housing work.

## Existing work to reuse and work that stays open

L675 already owns orchestration-view regeneration and routed-packet/consumption distinctions. L628 owns hidden summons; L676 JANUS follows it under approved order. L647 already owns approved history/restatement consolidation; L634 owns the unused collector-config mirror; L665 owns hosted build-date visibility; L688 owns unknown broker quote time. Extend or execute the applicable existing item; no new competing backlog for the same defect. This review does not reorder Will's approved build sequence.

Nearest position work remains TERRY QQQOct12/USOOct14 cards and broker booking (L685–687), blocked at the existing owner's runtime permission at the last native read;420also pending. New owner evidence can be consumed while that block persists. VIOLET418receipt unverified. D69+$53.54 and Robinhood require missing broker evidence, not a script. OSPREY's latest STATUS says no new inbox item changes CPC/Tengiz; this is not a new all-leg grade, so9/18grade stays dated. WQ411 full spine audit is not discharged. Old/unobserved is not automatically false or eligible for closure.

## Acceptance and review boundary

Before gate edit: independent plan reader checks source vintages/meaning, proposes its own counterexample and checks no obligation lost. After: exact diff permits only state+last_checked for the six ids; all other cells/rows byte-identical; historical rows recoverable byte-exact; table/leading tokens/read-cap and existing gate parsers checked; source files still committed/unchanged. One plan, one result read; no further work generated by advisory findings.

Ordinary: six source-to-mirror records. Overlap: explicit differing owner-grade/raw-observation vintages. Wrong owner: registrar copies attributable committed owner grade, does not adjudicate. Missing information: first-published, unsourced event legs, intraday W3, unchanged HOMER legs remain disclosed. Concurrent activity: compare current owner bytes to reviewed commits before installation, no owner writes.

Disposition at creation: investigation findings VERIFIED at named local artifacts; operational redesign PROPOSED, not implemented. Six-row catch-up completed; final independent acceptance below. No new approval requested by this review; no trade or root-rule change.

## Plan-read disposition and bounded implementation

Plan read1 by read-only Sol helper `/root/improvement_grade_review`: no consequential blockers. Committed source bytes and proposed cell caps verified. Independent counterexample: substituting the newer raw079+5bp for explicitly owner-graded+6bp would manufacture an owner grade; proposal prevents that. Advisory retained for redesign: where ruling and DOCKET both mention a task, name the exact authoritative field for each instead of saying “one home” loosely.

IMPLEMENTED six state/last_checked pairs only; no other GATES row/cell altered. Previous full rows archived verbatim at `PROME/archive/GATES_STATE_HISTORY_2026-10-11.md`, with measure.py receipts. Author validation PASS: committed owner-byte equality; exact scope/neighbor invariants; archive recovery; table; existing brief/handbook parsers19rows/18LIVE/no fired-unexecuted; original leading state tokens retained. Independent result review ACCEPTED; receipt below.

Read-cap residue: measure.py reports the gate registry remains above the32,550B whole-read budget (baseline62,232B→60,655B, decreased). This pre-existing compaction debt is not repaired or hidden by six shorter cells. Source reads in this review are targeted and complete at each named row. Existing instruments/obligations remain; no new generator/check built. ORCH_INFLIGHT regenerated using the existing tool after recording this helper touch; this refresh is recorded state, not native liveness or implementation of L675's recurring wiring.

## Independent acceptance and final disposition

Result read1 (second total), same read-only Sol helper: ACCEPTED, no consequential defects. Independently rechecked six exact state/last_checked pairs against54748614c, unchanged other cells/rows, byte-exact prior-row recovery and recomputed CRC receipts, source-commit byte equality, caveats and parsers. Explicit helper closeout received: no edits/Git writes or remaining work. Stop at zero consequential defects; advisory on exact task-field ownership remains for redesign.

DONE: six existing owner grades consumed into PROME's mirror; existing orchestration view refreshed from the recorded ledger. IMPLEMENTED/TESTED/INDEPENDENTLY VERIFIED applies to that bounded registrar change. PROPOSED ONLY: reducing duplicated prose, archival resume cleanup and separate status-field presentation. No new instrument or procedure installed, no overdue obligation closed without evidence, no new owner session launched, no rule or deadline changed. This is a scoped continuation, not a Standard closeout or full spine audit.
