# WALTER workflow — November 23, 2026

## Current assessment

Keep the division of work: WALTER finds, filters, verifies framing and routes; domain desks judge the implications; PROME coordinates; TERRY assesses trades. In the two sampled November 23 handoffs, recipients recorded their own source checks within minutes. The more consequential observed weakness is execution before dispatch: old observations presented as current, skipped source reads and missed threshold coverage. Existing rules already address those cases. Prioritize executing those rules over adding intake, another checker or another general audit. Workload as a cause is plausible but unmeasured; this review does not establish that instruction length caused the misses.

This is a bounded workflow explanation and advice, not a new operational assignment or full WALTER acceptance. No WALTER files, collector settings, signal records or owner workflows were changed. No sends or launches. Next CATO step: discuss this map with Will; any further investigation should start with the particular stage he wants to improve. Forecast pilot remains held; earlier grants survive.

## Scope, revision and concurrency

Will: “Okay PROME is working. While we wait lets look at WALTER's work flow.” Initial review snapshot `34b17c0392e6c497ffa3bf2f022aa2fd2b938362`, shared master. WALTER's delivery log was dirty at entry; during review it produced new cards 010/011 and associated handoffs/log changes. Those are concurrent owner work, not abandoned artifacts. No pull, owner edit or takeover in this task. Initial boot earlier in the session fetched origin and confirmed then-current HEAD; that is not a publication receipt for later work.

Read WALTER's complete charter and November 20 LAST_COMPLETION, targeted FILTER_SPEC and BOARD_CONSUMPTION_SPEC sections, dispatcher validation/usage, current November 23 calendar/threshold records, three complete BOARD cards (001/003/005), and recipient board-log matches. Read late-arriving 011 as uncommitted work in progress at approximately 14:01 ET. Inspected owner roles and relevant prior rulings/previous CATO scanner dispositions. Large checklist/spec files were navigated selectively, not audited whole. No operational boot, intake scan/mark, source pulls, credentials, external truth verification, benchmark or code test was performed.

Market figures and event accounts below are evidence of what the internal records claim and how work moved. They are not independently verified financial facts. Recipient records establish reported owner checks, not CATO reproduction of those checks. No fleet-wide success rate, miss rate or latency estimate follows from this sample.

## Workflow map

| Stage | Intended behavior | Existing machinery / boundary |
|---|---|---|
| Recover context | Read current desk concerns, position mirror vintage, upcoming releases, prior dispositions and corrections before filtering | WALTER charter steps 1–7; FILTER_SPEC Boot Context. Position truth remains Will/broker; mirror can be stale |
| Gather inputs | News/filing collection lane, release calendar catch-up, threshold data, desk corrections/research returns, Will's drops and X bookmarks | Research-Intake collection and intake_scan; calendar reconciliation; four threshold families; dropzone_scan; x_bookmarks_scan. Collection is not continuous WALTER judgment. X intake has its own Will-launched-session restriction |
| Decide what merits attention | Emergency bypass; otherwise novelty and relevance; credibility affects confidence; stronger evidence or changed figures are new information | FILTER_SPEC; uncertain relevant material is not automatically discarded. Date of the underlying event matters, not merely date found |
| Verify and combine | Open required sources, test framing, distinguish source claims from inference, combine repeated themes while preserving new details | SIGNAL_PROCESSING_CHECKLIST and existing bounded verification mechanism. Small items can be recorded without changing a score |
| Route | Choose owner and ACTION versus INFO, precedence and caveats; write shared BOARD signal and required recipient handoffs | dispatch_card.py already consolidates card, handoff and log writing and validates known mechanical failures. Recipient exceptions are already encoded; no replacement dispatcher needed |
| Publish and prove delivery | Commit/push under precedence rules, then reconcile delivery with Git evidence | Written, on-origin delivery and recipient consumption are separate. Publication by itself does not mean someone used the information |
| Recipient judgment and correction | Owner reads, grades or disposes; corrections propagate to affected readers; PROME decides whether a wake is warranted | Recipient board_log and processed handoff; correction registry; current readiness evidence. WALTER does not acquire domain judgment or desk-launch authority merely by routing |
| Reconcile | Light closeout for ordinary midday routing; full closeout for end-of-day/non-routing work and deferred-closeout limit | Existing closeout_run and exact publication/duty receipt. A selected checker pass is not complete coverage |

Primary instruction references: [charter](../../WALTER/CLAUDE.md), [filter](../../WALTER/design/FILTER_SPEC.md), [processing checklist](../../WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md), [delivery spec](../../WALTER/design/BOARD_CONSUMPTION_SPEC.md), [dispatcher](../../WALTER/tools/dispatch_card.py).

## Evidence and advice

### WW23-1 — retain: two handoffs reached substantive owner judgment quickly

BOARD `SIG-W-20261123-001` was stamped 17:17:41Z. VULCAN's board_log row at 12:20:54-05:00 says it opened the SEC filing and exhibit itself, confirmed three statements, retained the unverified pre-filing move caveat, and wrote findings/consumer packets. This is about three minutes from card stamp to recorded disposition, not total news-discovery latency.

BOARD `SIG-W-20261123-005` was stamped 17:24:54Z. HANS's board_log at 17:33Z records its own vendor re-pull and the L3 exit grade. WALTER's card reserved the grade to HANS and distinguished the completed close sequence from the subsequent intraday rebound. This is about eight minutes from card to recorded grade. The card also admits the earlier exit check was missed; quick consumption today does not erase that delay.

**Recommendation:** preserve this owner handoff. The sample supports useful downstream operation, not a conclusion that all delivery is reliable or that a trade benefit occurred. No repair assigned for these two handoffs.

### WW23-2 — material priority: improve first-read execution under existing instructions

WALTER's [November 20 closeout](../../WALTER/LAST_COMPLETION.md), still headed November 20 when inspected, explicitly records omitted FILTER_SPEC position/catalyst/trailing-48h reads, unread HANS threshold rows, and errors in primary-source checking. It is a dated closeout, not proof that today's active session has done nothing.

November 23 correction `SIG-W-20261123-003` supplies a stronger concrete counterexample: Friday's VIX threshold had crossed by the 14:20 ET vendor bar, but WALTER answered Will at about 14:43–14:52 using a 13:33 observation as current. It corrects the prior explanation that no WALTER session was watching. The record therefore identifies an active-session freshness failure; increasing collector frequency alone does not resolve it. The same correction says 12 GPU-finance candidates were closed FOLD from titles without opening the required sources. A declared queue disposition did not establish a completed source review.

**Correction disposition:** the misleading explanation and other framing claims are explicitly corrected on card 003; do not report them as still uncorrected. The broader reliability question is whether subsequent ordinary execution uses current observations and opens required source material before making the claim. No historical miss-rate study or new mandatory test is proposed.

**Recommendation/owner/closure:** WALTER should use the existing freshness, context and source-opening instructions in the normal session. When a required read cannot be completed, keep the corresponding conclusion unassessed; a title skim can identify a candidate but cannot stand in for source review. Closure of a particular review item requires its source-based disposition or an explicit access limitation. Sustained improvement remains unmeasured. This is advice, not a new assignment from CATO to WALTER.

### WW23-3 — keep controls proportionate and recognize work already underway

At roughly 14:01 ET, concurrent uncommitted card `SIG-W-20261123-011` reports source reads for six GPU review items, names access limits, distinguishes opinion/scenarios from evidence, and identifies a Microsoft item as old news. Its origin records Will's 13:56 direction. This is encouraging owner follow-through during the review, not evidence that CATO caused it. It does not prove all 12 earlier title-only dispositions have been repaired; no key-by-key reconciliation was done. Publication and owner consumption of 011 were unassessed at that read.

The rule set is extensive, but both dispatcher and tiered closeout already reduce repeated manual work. Inspecting their existence is enough to avoid proposing duplicates; effectiveness and time cost were not benchmarked. Preserve the difference between a source access problem, skipped execution and a missing tool.

Earlier decisions remain applicable: WQ-694's two collection times are approved/live in the owner record, with the existing November 24 observation of actual starts and surviving batches. WQ-684's ordinary-headline skim is approved with a December 14 usefulness review and known title-only coverage limit. Do not recommission either. CATO's prior N14-1 record preserves the during-scan concurrent-write limit and no-pull/write control; the scanner repair/read ceiling is not reopened here. References: [WQ-694 record](../../../PROME/proposals/2026-11-16_wq693-694-697-RULED.md), [WQ-684](../../../PROME/proposals/2026-11-14_wq684-RULED.md), [prior scanner disposition](2026-11-11_1150_morning-work-review.md#november-14--session-closeout-and-owner-follow-through).

**Remaining owners:** WALTER owns current source/threshold coverage and actual routing; recipients own grading/consumption; PROME/WALTER own the already-scheduled collector observation, and PROME owns the December skim review. No new delivery packet, policy edit, tool, watcher, study or launch authorized by this review. Advice delivered at this stopping point; implementation and lasting benefit remain separate.

## Delivery checks

Verified existence and readability of all ten distinct inputs before checking. Weekday check passed on `PROME/DOCKET.tsv`, `PROME/GATES.tsv`, `PROME/WILL_QUEUE.md`, this report and `AGENTS/CATO/CONTINUITY.md` (five files). Optional CATO STATUS/calendar/catalyst files are absent and were omitted. Read-cap check covered exactly `AGENTS/CATO/AGENTS.md`, `AGENTS/CATO/CHARTER.md`, `AGENTS/CATO/CONTINUITY.md`, root `CLAUDE.md`, `USER.md`, `AGENTS.md`: all below the cap; root CLAUDE has the already-recorded 75% rotation advisory, not a cap failure or CATO repair grant. Orphan advisory found only PROME's untracked honest-name-test directory at this check; none CATO-authored. It was preserved, not swept. `git diff --check` passed; staged list was empty before staging this report. No changed financial figure, STATUS/ledger or auto-memory triggers the conditional consumer/ledger/memory checks. No code changed or implementation tests required. Exact-path commit and fresh-fetch publication receipt are delivered in-session.
