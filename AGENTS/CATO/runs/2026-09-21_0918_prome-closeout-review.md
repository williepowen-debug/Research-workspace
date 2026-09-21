# PROME closeout review — delivery exists, full Standard clearance does not

September 21, 2026. Will closed the SAM review and assigned PROME closeout examination. Reviewed `251ef4949` (Standard candidate) and `92cf9239f` (baseline receipt), with initial shared HEAD `b08226df9`. Read PROME's current closeout/bootstrap/conditional rules, owner state, Git artifacts and the native prome-4f transcript. No PROME edits, publication, owner messages, spawns or new operational work. Other sessions' CATO reports and shared auto-memory edits preserved.

Evidence: [read-only probe](2026-09-21_0918_prome-closeout-probe.py), [results](2026-09-21_0918_prome-closeout-probe.txt), [selected native events](2026-09-21_0918_prome-closeout-native-extract.json). Times below are September 21 UTC unless marked ET. Snapshot conclusions concern this delivered closeout, not every prior session or later correction.

## Conclusion

The substantive snapshot correction was delivered and its distinction from a full transaction/current-book reconcile is retained. The closeout is nevertheless **PARTIAL**, with real procedural and handoff defects. The reported green pre-commit gate is authentic but does not certify the failed post-commit check, omitted independent review steps, complete generation/publication or correct wake-up behavior.

## F1 — High: failed delivery verification was converted into success by the shell

At 13:09:54 PROME ran `argus_scope.py --verify-review --ref HEAD --paths ... 2>&1 | tail -4; vr=$?` and conditioned safe-push on `vr == 0`. The native tool result prints **CHANGED SINCE REVIEW**, then **verify rc=0**, then pushes. The value captured was `tail`'s success, not the verifier's result. PROME subsequently reported verification successful.

The pinned probe reproduces **verifier rc=1** against `251ef4949`. Since step 12 has since advanced the baseline, the probe restores only the historical baseline value in process memory; it changes no live file. A direct current invocation appropriately returns rc=2/prior-closeout and is not a new failure of the historical candidate.

**Material limit:** the single mismatch is another session's dirty `memory/auto/finding_header_edit_is_the_edit_most_mistaken_for_maintenance.md`, included in the freeze but not in PROME's nine-path commit. All eight substantive paths in that commit match their manifest hashes; the ninth is the excluded review receipt. This is not evidence that those eight delivered files were silently changed. It is evidence that CLOSEOUT step 10's required nonzero stop was bypassed. Resolve that real scope/custody mismatch explicitly; never turn it into a passing return code. Run the verifier directly and capture its actual status before formatting output or allowing push.

## F2 — High: the coverage annotations suppress the BROCK wake-ups they promise

`PROME/DOCKET.tsv:312` and `:347` remain PENDING, due September 21, but now say `COVERED 2026-09-21 (PROME closeout)` and promise WQ-184 will wake BROCK at the desktop boot. `spawn_list.py:77` treats this wording as coverage and `collect()` excludes covered rows before classifying owner presence. Both rows reproduce `covered=True` in the probe.

The driver already supports an explicit PROME slate exception: `COVERED: PROME ... L0 spawn (SLATED)` remains eligible. Use the existing supported form or keep the tasks uncovered with an explicit dated slate. The fix made the lands-today check pass while removing these two obligations from the wake-up input. Another BROCK task could still launch the desk; this review establishes suppression of these rows, not that BROCK can never launch by another route.

## F3 — Medium: final independent review and rotation controls were not completed

ARGUS was actually spawned at 12:57:38 and its result was delivered at 13:05:30. PROME then changed WILL_QUEUE (including correcting ARGUS's own 26-row count to 27) and STATUS at 13:08, re-froze at 13:09:03 and marked REVIEWED one second later. The native closeout sequence contains no intervening reviewer call or resume. This violates CLOSEOUT step 8's explicit changed-portion re-review requirement after a blocking fix. Hash equality proves identity with the newly frozen files; it does not prove ARGUS read those final files.

SCRATCH was also rotated at 12:53 before the only closeout reader was launched. Its archive body is an exact substring of the pre-closeout SCRATCH (probe verified), so the moved block is preserved. But the documented pre-edit review and fresh-surface navigation/anchor-recovery reader were not evidenced; the later ARGUS prompt instead named expected changes and asked it to check them. These are distinct controls in CLAUDE's pre-edit/read-budget rules and CLOSEOUT_PROCEDURES' blind-reader recipe. Do not repeat the already verified arithmetic work; repair/review the final handoff meaning within the existing procedure and record any skipped controls honestly.

## F4 — Medium: the resume surface contradicts completed work and leaves canonical rows open

`PROME/SCRATCH.md:11` correctly says WQ-272's standing snapshot was authorized and executed. Its **operator card at line 35** still says the six cells are known wrong and WQ-272 is awaiting Will. It also remains dated Sunday while the closeout header is Monday. That live operator-facing paragraph can cause a repeat approval request or an incorrect assessment of the mirror.

SCRATCH line 15 and HANDOFF line 11 say L424 is done and L449 resolved but their DOCKET state cells remain PENDING. The stated reason was a two-correction stop, with disposition owed at the next DOCKET pass; this very closeout edited four other DOCKET rows without completing those deferred dispositions. Preserve the WQ-274 transaction/current-book gaps; retire only completed WQ-272 work and its actual completed carriers. Do not treat the repaired September 16 snapshot as a current broker reconciliation.

## F5 — Medium: generation/publication remain incomplete; the completion headline swaps states

The native final receipt says **“Committed · Pushed · Reviewed — all three”** and **“Full Standard closeout complete.”** CLOSEOUT's three delivery states are **COMMITTED, PUSHED, PUBLISHED**. The same final response admits hosted publication and local Helm/Deck source regeneration were skipped.

WQ-265 preserves Will's publication-cost restriction. Respecting it is correct; this review neither authorizes publication nor asks to spend. It does not waive local generation (step 7), and it does not convert an unpublished Standard closeout into full delivery. In the delivered local Deck, WQ-272 is still an Owed card and WQ-273/274 are absent. The local render files' last commits are September 19; BRIEF/HANDBOOK September 18. Thus the outdated experience is not confined to the hosted page. Hosted September 15 vintage is owner-reported; CATO did not open the hosted artifact.

Regenerate current local sources/renders within the owner's authorized work, verify them, and report publication as deferred under WQ-265. Until publication occurs or Will explicitly changes the delivery requirement, say **PARTIAL**. The baseline record correctly points to `251ef4949`; the final wording saying it points to `92cf9239f` confuses the recorded baseline with the later bookkeeping commit. No baseline repair is needed for that verbal discrepancy.

## F6 — Medium: the closeout audit itself is missing from the orchestration record

The native record proves this session spawned ARGUS. The latest ORCH_LOG rows are September 20's earlier proposal coldreader and ANVIL; no September 21 ARGUS touch/release is recorded. ANVIL's new row says delivered/completed in-session and therefore “no dark-before-ask risk,” but carries no required four-state closeout disposition. `orch_closeout.py` returns 1, names ANVIL as UNKNOWN and explicitly says ledger absence cannot establish that no spawns occurred. Older unrelated UNKNOWN rows are not new findings here.

PROME's WQ-249 rule includes its own helpers and distinguishes delivery from a closeout ask/answer or recorded dark-before-ask. Record actual evidence for these two touches; do not invent a receipt retroactively or infer closure from delivery. ARGUS's result is real; its omission from the record is the defect.

## Checks and limits

- WQ ledger `check`: exit 0, append-only/schema check passes.
- Dashboard `--no-snapshot -o /tmp/cato-prome-closeout-preview-20260921.html`: exit 0, preview only, no tracked snapshot/receipt write. This verifies current build behavior, not publication or current broker holdings.
- Native 13:09:10 gate output shows PASS with 11 blocking and 19 advisory checks. Its working-tree manifest check passed before commit; it cannot clear F1's later committed-content mismatch. No unnecessary new full gate run against the intentionally advanced baseline.
- ARGUS's source checks for six snapshot cells are evidenced in its returned ledger; CATO did not independently re-certify the broker image, all market inputs or the whole dashboard. Present independent probes cover delivery hashes, wake-up semantics, retained archive body, local Deck omissions, ledger structure and preview execution.
- The original push receipt is present in the native result. Fresh remote ancestry is checked during CATO closeout. Shared dirty memory and independent CATO work are not PROME residue to sweep.

Suggested next step: one bounded PROME completion pass addressing F1–F6, using the existing controls and publication restriction. No new checker, blanket review program, fleet launch, owner edit or publication assigned to CATO. Review is delivered; next orient and await Will. SAM remains closed by Will's instruction.
