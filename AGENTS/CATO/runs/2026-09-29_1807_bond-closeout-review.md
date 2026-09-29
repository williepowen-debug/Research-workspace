# BOND closeout review and NEXUS proposals — September 29, 2026

## Current assessment

Keep the separate checklist and consolidated runner, but repair BC1–BC4 before treating the runner as a reliable closeout gate. The strongest defects are missed edits in the freeze and suppressed findings in the runner. No redesign or additional review tier is needed. BOND owns the corrections; CATO has made no owner-file changes or sends.

Will asked for errors and suggested improvements to BOND's `cdcb486ff` closeout restructuring. Reviewed that commit and the current checklist, runner, owner instructions, provenance, cold-read ledger, run log and relevant root tool contracts. The three principal owner files remained identical to `cdcb486ff` at the concluding source check. Initial shared HEAD was `ccd55ffaa`; concurrent agents subsequently advanced it. CREED and PROME had unrelated dirty work, preserved throughout. No pull was performed.

This is an independent review of the procedure and code, not a certification of BOND's market analysis or its earlier closeout execution. The live network-fetching runner was not executed: it writes BOND's log and refreshes data. Tests below ran in temporary repositories or used the existing fixture-only modes.

## Findings

### BC1 — High: the freeze does not bind the checked contents to the commit

Evidence: `AGENTS/BOND/monitors/closeout_run.py:95–123,245–248`; `CLOSEOUT.md:49–54`.

- `tree_digest()` hashes Git status and diffs, not untracked file contents. Rewriting an existing untracked file left the digest unchanged; an edit to a tracked file changed it (positive control). New tools/documents can therefore change after checking without detection.
- The scope is only `AGENTS/BOND`, although C12.4 also commits self-authored packets outside that directory. Editing an outgoing packet left the digest unchanged.
- The digest is first recorded after the checks. A tracked-file mutation after the content checker, simulated during the weekday check, produced runner rc=0 and verify rc=0. This does not enforce the documented freeze starting before the run.
- `verify()` does not inspect the last run's overall result. A matching row marked `FAILED` returned rc=0 and literally printed “FAILED) — commit now.” The checklist still forbids committing after a failed run; the executable instruction contradicts it.

**Correction:** snapshot actual contents for the explicitly intended paths, including untracked files and declared self-authored packets; compare before/after checks and at verification. Keep the automatic log exclusion explicit. Reject failed/incomplete runs and failed Git reads. Verification should authorize only the checked candidate, with any subsequent edit requiring another run. Avoid binding unrelated agents' work merely to widen the scope.

**Closure:** the four counterexamples above fail safely; an unchanged successful candidate still verifies. A clean staging operation should not require redoing expensive research checks solely because bytes moved between the working tree and index.

### BC2 — High: the runner loses the information needed to act on checks

Evidence: runner lines 170–174,183–225,245–248; root `CLAUDE.md` session-end 1b–1e; `scripts/consumer_check.py:1122`.

The consumer check's stdout is captured in `o1/o2` and discarded. Its default exit is **0 even when stale references are found**; `--strict` is required for a finding exit. Thus the runner can print `RAN` and “every mechanical step RAN and passed” without displaying the affected owner, file or line. The saved log does not retain those findings either. A simulated successful consumer check carrying a stale path confirmed that the path appeared in neither output nor log. Execution alone is not a clean result, and the root instruction to repair/notify cannot be carried out from this output.

The failure mapping is also inconsistent: orphan rc=127 and ledger rc=1 both became `RAN`, and the combined runner returned 0 in a controlled probe. Those branches test only `rc is not None`; subprocess crashes usually return integers. Conversely, a weekday advisory rc=1 becomes a hard no-commit failure, with only the final generic advisory line displayed. Root explicitly requires inspecting flags, including legitimate historical quotations, rather than treating every flag as an error. C12 has no disposition path for a reviewed false positive. This last behavior is established from the code/contracts, not a claim that today's BOND run encountered such a flag.

**Correction:** retain actionable output (or save one full transcript and print its pointer), actual rc and reason. Distinguish successful execution with findings, clean execution and execution failure. Keep advisory findings visible and require their appropriate disposition; do not silently pass tool errors or require false-positive prose edits. The log currently stores step labels only, omitting rc, detail and the reason for NOT-APPLICABLE; include those in existing evidence rather than adding another checklist.

**Closure:** a stale consumer path remains accessible; missing/crashed tools cannot yield an all-pass result; a documented false-positive advisory has a legitimate completion path. Exercise these wrapper behaviors, not just the underlying tools.

### BC3 — Medium: optional delivery conflicts with root instructions

Evidence: `CLOSEOUT.md:14–15,20,52–55`; root `CLAUDE.md:84–95`; BOND charter's CLOSEOUT pointer.

The light tier requires changes to STATUS/SCRATCH but labels commitment optional. The root requires session-end commit and auto-push; its named mechanical exceptions are TERRY, WALTER and YEYOU, not BOND. The local C12 and charter also describe mandatory commit/push, so the document gives conflicting instructions even before consulting root. An intraday light ending can strand changed handoff files. A bounce within the same continuing session can reasonably be a checkpoint, but it must not silently waive delivery at an actual session end.

**Correction/closure:** use tiers to vary write-back depth, while retaining root delivery for every actual ending with changes. Define a same-session bounce separately. No new operator approval is required to conform the local checklist to the standing root rule; a true exception would need explicit authorization.

### BC4 — Medium: the handoff gate forces unnecessary rewrites

Evidence: runner lines 70–92,176–181; `CLOSEOUT.md:42–43,58–60`.

Every non-bounce tier requires NEXUS_BRIEF, SCRATCH and TRADE to have a vintage at least as recent as STATUS. A dirty STATUS is assigned the current time; an unchanged TRADE gets its prior commit time. Consequently, updating only a catalyst or an administrative STATUS line fails the TRADE gate even when its posture/gates are unchanged and C6 correctly requires no edit. The addendum rules likewise allow C11 to be a no-op when no consumed number/date/state changed, but the unconditional gate rejects that case. A Git-backed fixture reproduced the dirty-STATUS/unchanged-TRADE ordering failure.

Dirty surfaces are each assigned a new `time.time()` when inspected, so the check also cannot establish actual write order among them. BOND already discloses that freshness does not prove content; the additional concern here is needless edits and incentives to touch headers to satisfy the gate.

**Correction/closure:** align the gate with changed dependencies and permit an explicit reviewed no-op when a surface's consumed state has not changed. Keep missing/outdated relevant updates visible. A STATUS-only catalyst change must close without rewriting valid TRADE prose; a changed posture must still require its consumers to be reconciled. Do not solve this with filesystem mtime.

## What checked out and test evidence

- The original closeout steps 9–18 are preserved verbatim in the provenance file. Its CRC32 is `4276224127`, matching the checklist. An initial extraction included the subsequent MAIL paragraph and failed comparison; trimming at that section boundary confirmed the actual moved block. Charter sizes are 39,500 bytes before and 32,532 after.
- The saved cold-read ledger contains the four claimed contradictions, and the revised file addresses those specific points. That verifies the recorded edits, not the identity/independence of its reader. The 13-desk survey was not independently repeated.
- Existing run log records an ordering failure followed by successful runs. It does not save diagnostic details, so the claimed 36-minute gap is not independently established by that log.
- `.venv/bin/python3 AGENTS/BOND/monitors/closeout_run.py --selftest`: four ordering fixtures pass. They test the comparison predicate, not the wrapper/freeze counterexamples above.
- `.venv/bin/python3 AGENTS/BOND/monitors/closeout_check.py --selftest`: all pass; its summary counts 63 fixtures, and the numeric output additionally reports four date-alignment fixtures. These are existing checker tests, not fresh market validation.
- [Reproduction probe](2026-09-29_1807_bond-closeout-probe.py): imports the current runner without invoking its production main; uses an isolated Git repository and explicit stubbed check responses. Reproduced all BC1 cases, the BC2 discarded-result/error-mapping cases, and the BC4 vintage predicate case. The probe prints observations rather than claiming they are expected correct behavior. Temporary files are cleaned up; owner artifacts remain untouched.

## NEXUS D-list — additional scope from Will during this review

Will supplied NEXUS's D1–D8 closeout proposals while the BOND review was in progress. Recommendation: retain the direction, with the amendments below. This is proposal/design review plus a bounded read of the developing implementation, not certification of a finished NEXUS commit. `CLAUDE.md` was dirty and being edited concurrently; the latest committed NEXUS charter at first read was `ccd55ffaa`. The working charter and proposals file already recorded Will's separate instruction to encode all D items including D7. That owner record is not CATO granting approval, and this review neither asks for that approval again nor edits the owner files.

**Delivery update:** NEXUS committed the D-list during this review as `6e45b05f9` (18:10 ET). Before delivery CATO inspected that commit's charter and SIGNALS banner: the NC1/NC2 wording and NC3 contradictory lifecycle instruction below are present in the committed version, not merely a superseded draft. The subsequent dirty charter diff only added the LAST_COMPLETION boot-read pointer. No full re-audit of NEXUS's other work is implied.

### NC1 — Required: root controls follow applicability, not tier

D1/D8 put root session-end checks at Standard and above; the working charter's tier block and step 16 explicitly do so. Light includes packet commits—the case where the orphan check is particularly useful—and can supersede a claim/figure. A `skipped:` line makes a gap visible but does not waive a binding control. Keep the root-required unconditional checks at every actual ending; conditional checks apply whenever their trigger occurs, including Light. Label genuinely inapplicable controls with reasons. The local weekday-check expansion to pages/PREDICTIONS is useful, but should add to the root-required PROME DOCKET/GATES/WILL_QUEUE perimeter, not silently replace it. Preserve the root `--self` consumer scan when NEXUS supersedes its own cited figure.

Closure: one Light packet/changed-claim example shows the applicable checks; no tier or “skipped” receipt grants an exemption. This is the same policy boundary as BOND BC3.

### NC2 — Required: propagate the meaning; preserve historical evidence

D2's perimeter “every surface this session touched” excludes precisely the untouched active copies that can carry a superseded claim. Start with the changed claim and trace all active consumers, touched or not. A literal phrase search is a useful supplement, but synonyms, causal direction and differently worded grading rules need a short semantic read. PROME-owned mirrors remain PROME's to change; record owner-confirmed or independently checked status rather than editing them or implying delivery from a doorbell alone.

The working implementation goes further than the quoted proposal: it says to paste an **empty** grep result into the commit body and fix every nonempty result in that commit. That would treat preserved original letters, labelled corrections and archives as defects. Today's PRED-50 agreement explicitly preserves the original letter verbatim. Keep those records. Record search scope, active matches and their disposition, with labelled history excluded from the live-correction requirement. A report pointer and concise outcome are more useful than dumping raw matches into every commit body.

Closure: the original PRED-50 letter survives; a live paraphrase and a previously untouched active mirror are found; the corrected operative rule agrees across its actual consumers.

### NC3 — Required for D7 completion: retire the obligations as well as the storage

Removing unused transport/archive chores is reasonable. But an idle file is not necessarily an empty analytical queue. At inspection `SIGNALS.md` still described two unresolved rows: **S-26082801**, including an untested funding-link question, and **S-26060701**, whose remaining leg is the El Niño Q4 crop channel. WALTER's delivery lane replaces intake, not necessarily those unresolved analytical obligations.

Before declaring the retirement complete, map each surviving obligation to an active owner/home and resolver, or explicitly resolve/drop it with a reason. This is not a recommendation to revive old research automatically. The freeze banner is present in `6e45b05f9`; reconcile the charter's remaining “Signal lifecycle,” `signals_archive/` ownership and SIGNALS anti-pattern wording, which still instruct use of the retired surfaces. The retirement commit changes the charter, banner and proposal record but supplies no row-by-row disposition. Neither signal ID appears in the inspected live STATUS/PREDICTIONS files; that exact-ID check is not proof that their subject matter is absent elsewhere. Existing direct analysis-packet routing and WALTER's raw-signal boundary can remain as already specified; retirement does not authorize a new fleet transport scheme.

Closure: two row dispositions and consistent active instructions; no archive deletion needed.

### Improvements to keep the work proportional

- **D3/D4:** keep corrections outside the annotation cap and test changed letter logic. Apply the date/magnitude/resolver/exhaustiveness tests when a correction changes those semantics; a spelling/link fix should not force an unrelated letter test or full analytical pass. Never cap repair of a known consequential error.
- **D5:** keep a dated four-week rollup. State an actual due date/wake, rather than only “next ≥10/27,” which establishes an earliest date but no latest obligation. A due rollup must not slip merely because the next session is not labelled Heavy.
- **D6:** keep a short handoff linked to long-form evidence. A ≤6 KB session block does not itself guarantee the **whole file** is below 70%; measure the whole file after writing and preserve live obligations during rotation. The inspected file was 26,819 bytes, consistent with the reported roughly 82% of 32,550 bytes. This was the starting state, not evidence that an in-progress rewrite failed.
- Named tiers and explicit no-ops are useful. Avoid turning every commit into a full session closeout when it is an intermediate checkpoint; apply actual ending requirements at the ending. The D-list's per-commit costs and claimed 11/11 Git execution were not independently audited here.

**Stop condition:** both reviews delivered. Recommend a bounded BOND runner repair and the NEXUS amendments above; no wider survey or new process layer. No owner edits, sends, retirement decisions or new research commissions made by CATO. Future implementation verification is a separate assignment. Delivery checks and receipt are recorded below/in-session.

## CATO delivery checks

The saved probe reproduces the observations above. Weekday check passed across PROME DOCKET/GATES/WILL_QUEUE and CATO report/continuity (five files). Orphan advisory found no CATO-authored external packets; unrelated CREED/NEXUS/PROME work was left untouched. The shared index contained CREED's inbox-processing paths, so CATO's commit uses only its three explicit files. No memory-index or numeric-consumer check was triggered by this review. No publication was requested or performed; commit/push receipt is delivered in-session.
