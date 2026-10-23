# WATT — Closeout procedure

**ACTIVE — 2026-10-12.** Approved directly by Will: “Okay please implement your proposed improvements and edits.” Implements `proposals/2026-10-12_CLOSEOUT_PROPOSED.md`; supersedes the former five-step CLOSEOUT PROTOCOL block in `CLAUDE.md`.

**Canonical boundaries:** root `CLAUDE.md` owns Git, scope, source and conditional-check rules; `PROME/COMPLETION_SPEC.md` owns delivery and acknowledgment; NEXUS's schema owns brief form/order. This file makes WATT's execution sequence explicit without changing those authorities. A runtime approval rejection remains binding within its stated scope.

## When and how much

Run before ending a window, resetting context or a long pause. State the mode in the dated receipt:

| Mode | Use | Required work |
|---|---|---|
| **checkpoint** | Records-only/status ending or imminent context reset | Reconcile changed records and actual blockers; maintain current STATUS/SCRATCH/brief, applicable checks, persistence and scoped delivery. Preserve real data vintages; do not pull prices merely to change a stamp |
| **standard** | Completed owner research window, grades or inbox work; default at end of day | All nine steps below, with explicit reasons for unchanged surfaces or inapplicable checks |
| **heavy** | Deliberate protocol, tooling or thesis amendment | Standard plus instruction/code agreement and validation of the actual change |

Modes size the work; no mode waives an existing mandatory root or desk duty. For a live event, save evidence and the next action immediately. Session closure does not resolve an unfinished event or promise automatic monitoring. Name the source cutoff, pending window and registered wake/owner.

## Execute in order

**C1 — Reconcile evidence and obligations.** Read current STATUS/SCRATCH, open predictions, inbox and relevant owner/PROME receipts. Evaluate carried warnings against their named artifacts/commits. Distinguish research result, pending future observation, technical blocker and new operator decision. Do not re-present a discharged blocker. Verify actual runtime identity and supported notification tools when needed; do not reuse a previous window's UUID or infer fleet absence from incomplete discovery.

**C2 — Write affected state.** Update STATUS with record-maintenance time separate from market observation date/cutoff. New facts → KB; moved channel state → VX; changed mechanism → FLOW and THESIS; affected trigger/posture → TRADE. Resolve due predictions against original criteria and preserve grade/history. State why unchanged surfaces need no edit; preserve their real vintage. KILL_MEMO is excluded unless a deliberate authorized amendment is separately made. Add a durable desk lesson when warranted; apply root memory checks only if auto-memory was actually written.

**C3 — Reconcile dates and coverage.** Keep STATUS's wake set aligned with actually registered obligations and PROME docket identifiers. Preserve requested versus issued, forecast versus outcome and partial-day versus completed-window distinctions. State the next owner action/date. A registered wake is not a running monitor or a guarantee another session will execute.

**C4 — Current continuity.** Maintain **one current pickup block** in SCRATCH: state at writing, completed work, remaining work, next dated checks, source/approval walls and mail/delivery status. Archive superseded session narrative verbatim when replacing it; name the archive and verify preservation. Keep standing operational constraints readable. Do not append a competing current pickup. Archive links provide history, not instructions to revive resolved work.

**C5 — Mail and delivery.** For each consumed inbox item, reconcile integration/deferred disposition, its board row where applicable and archive move. Integrate, log a KB row and commit before filing (`CLAUDE.md` boot step 6; WALTER signals also per `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` §8.1). Preserve self-authored consumer packets and their commit pointers. A file write/commit is not notification; queue acceptance is not consumption. Confirm acknowledgment at the exact artifact version. PROME's receipt covers PROME, not every other consumer.

**C6 — Check and account.** Run applicable checks from the repository root; save results and their perimeter in the dated receipt. Required mechanics remain those in root `CLAUDE.md`; this is the WATT invocation list:

| Check | Invocation / trigger | Receipt must state |
|---|---|---|
| Owned changes | `git diff --check -- AGENTS/WATT`; inspect exact paths and TSV column shape for edited ledgers | Paths checked; any findings resolved |
| Orphan advisory | `bash scripts/orphan_check.sh WATT` | Own packets persisted; foreign work excluded |
| Weekday claims | Root 1e: `python3 scripts/claim_check.py --check weekday PROME/DOCKET.tsv PROME/GATES.tsv PROME/WILL_QUEUE.md AGENTS/WATT/STATUS.md` | Findings looked at, corrected or explained; not a blind substitution |
| Read cap | `python3 scripts/read_cap_check.py --agent WATT`; WATT `boot.py` byte-budget leg covers STATUS, SCRATCH, CLOSEOUT and predictions | Detected perimeter, sizes and any unreadable/over-budget surface; heuristic PASS is not fleet-wide coverage |
| Ledger/trade agreement and age | `python3 scripts/ledger_staleness.py WATT --days 7 --quiet` and `--trade --days 7 --quiet`; root ledger nudge when triggered | Actual agreement reviewed; a fresh timestamp alone cannot prove content agrees |
| Superseded number | Root consumer check, cross-agent and `--self`, only when a published figure changed | Series/unit adjudication, relevant packets and own repairs; preserve dated historical captures |
| Auto-memory | Root scoped memory-index/length checks, only if auto-memory was written | Authored slug(s), outcome; never impose another desk's orphan as this desk's failure |
| Protocol/tooling change | Heavy mode: inspect all affected instructions and exercise actual changed behavior | Evidence of the change, failure cases and limits; no code test claimed for a documentation-only edit |

For each check record **ran/result, findings/disposition, failed/UNKNOWN, or not applicable/reason**. A failed or skipped required check is incomplete, never “all checks passed.” Do not rewrite a historical capture solely to clear a lexical consumer hit. Findings require resolution or an explicit bounded disposition under the governing check's contract.

**C7 — Freeze final content and fold the brief.** Stop substantive source edits after C1–C6. Commit final STATUS/affected state with exact paths, then fold NEXUS_BRIEF against that state and **pin its actual STATUS source commit**. The brief is the **last substantive write-back**, immediately before its commit; no source changes afterward without re-folding and repeating affected verification. Confirm with `python3 scripts/brief_pin_check.py WATT` that the pin equals current STATUS HEAD. A newer brief stamp does not freshen its underlying data.

Use compact/full form under NEXUS canon. WATT's compact variant has routing first, no VIEW/CALIBRATION headers, and retains as-of and WAITING-FOR. **Use the full schema when WATT has ≥3 persistent live cross-agent edges or carries a thesis version.** Full form puts CROSS-DOMAIN first. Outbox remains crisis-only; normal owned analysis/coordination delivery follows the canonical file-packet contract.

**C8 — Persist and reconcile publication.** Commit only owned paths and self-authored carve-out packets; use root Git mechanics as authorized. Preserve technical rejection history and honor its scope. Before claiming publication is pending or complete, verify the **actual authored commits** and supporting receipt against a fresh remote observation. An independently authorized push may discharge publication; it does not authorize a denied-command retry or workaround. Do not pull over foreign dirty work or reimplement Git policy here. If required publication remains unavailable, report the actual gap once under the governing approval rules; do not re-present an already discharged approval request.

**C9 — Bounded receipt and close.** Use **one dated receipt per logical owner closeout**, with current disposition above preserved dated history. Update that receipt when later evidence changes publication, notification or consumption. Link exact commits/artifacts and supersede discharged warnings explicitly. Dated PROME delivery and verified notification follow COMPLETION_SPEC. Return the short user-facing result; do not imply that every future event or recipient is complete.

The receipt contains: mode/scope and received closeout instruction; source vintage; changed surfaces and no-op reasons; checks and limits; authored commits; current publication/notification/consumption evidence; pending owner action/date; anything actually requiring Will. Post-commit transport/publication receipts belong in this receipt or its canonical delivery acknowledgment. They are not a new market refresh; do not create a new research closeout merely to record them.

## Source/write-back map

| Read or changed fact | Write-back or explicit no-op |
|---|---|
| Channel score/read | STATUS; VX if state changed; NEXUS; current SCRATCH |
| Mechanism/cost-allocation outcome | STATUS; KB; FLOW/THESIS; TRADE trigger if affected; consumer packet; NEXUS |
| Prediction resolver/deadline | Live/archive prediction row; KB; STATUS wake set; dated PROME packet if coordinator calendar affected |
| Inbox disposition | Integration/deferred artifact; board row where applicable; archive move; continuity if open |
| Recipient acknowledgment / origin ancestry | Current disposition in the same dated receipt/pickup; correct derived pending wording, retain dated history |
| Procedure/tooling amendment | Owning instruction/code and change-specific validation; no implied market refresh |
| CLOSEOUT.md boot read | One-way procedure reference; edit only when a procedure amendment is approved |

**Automation boundary:** this procedure is active; a dedicated closeout runner remains a separate optional implementation. Reuse existing checks first. No new runner, dashboard, approval authority or automatic market grading is introduced by this document.
