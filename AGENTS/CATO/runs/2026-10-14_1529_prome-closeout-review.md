# PROME closeout review — October 14, 2026

## Current assessment — proposal follow-up

PROME’s proposal at3f9db4e15 is a sound design direction, with no runtime repairs installed. Its parse-old/hash-new correction addresses a real race, and the calendar patch precondition is stale. Before implementation, resolve the concrete inventory-versus-reviewed-contract boundary (PC14-5), name the real selection producer/consumer and migration behavior (PC14-6), and distinguish verification of a named commit from later shared-push contents (PC14-7). Add a stable-position/changed-quote control to A5. These are bounded implementation clarifications, not a request for another general planning audit or a new control framework. Existing maintenance authority/order remains unchanged; A/B build authority is not inferred from this CATO review.

## Initial assessment — before PROME’s proposal

Keep ARGUS and the freeze → review → committed-content verification → safe-push sequence. Improve the inputs and the delivery boundary. Today's audit caught an actionable stale-choice defect; reducing review indiscriminately would remove a useful safeguard. PROME's five suggestions are broadly sound, but several are existing duties or approved repairs, not new capabilities. “Finish the backlog first” needs a bounded endpoint: pursue the approved high-value sequence, avoid making every measurement/reporting item a prerequisite to fixing demonstrated errors.

Advice only. No PROME procedure/code, owner state, approval, queue, publication or messaging change. No helper launched. This is a broader protocol/design assessment, not another acceptance round on L678, L488 or today's final economic content. Earlier [ARGUS advice](2026-10-10_1640_argus-efficiency.md) and its hidden-packet counterexample remain relevant.

## Scope and boot

Will asked CATO to boot and review PROME's closeout using the supplied conversation. Start pin `e963d98ceeeed3784a932d0017908fde2b86cf2c`, shared master, cwd AGENTS/CATO. Runtime Codex/OpenAI, native task `/root`; exact model variant/session UUID UNKNOWN. Exposed shell/file tools support this work; native collaboration exists but is unused and proves no fleet presence. Root CLAUDE/USER/AGENTS, local AGENTS/CHARTER/CONTINUITY and COMPLETION_SPEC explicitly read; Codex mechanics selected from ORCHESTRATION_PLAYBOOK. No PROME operational boot or fleet launch. Other desks had dirty files and WALTER a staged rename; no pull or foreign-file changes.

Inspected current CLOSEOUT and its runner's core sequence, PROME charter, relevant completion/writeback contract, audit perimeter, argus_scope build/verification logic, publication-prerequisite function, October14 closeout report/baseline receipt and ARGUS run row; docket L473/L488/L548/L591/L594/L628/L647/L665/L675/L676, earlier CATO advice and selected commit evidence. This is not a full runner execution, full gate rerun, fiscal/source audit or hosted-page inspection.

## Findings and bounded recommendations

### PC14-1 — consequential display drift; remove repeated position facts at their source

Owner record: ARGUS found WQ302/357/360 explainers/options retaining closed TLT puts, ten TBT shares and obsolete sleeve comparisons. Two correction passes were required. CATO inspected the committed explainer diff and report, not external broker truth or every rendered sentence. The root position contract says truth is Will/broker off-repo; FORGE is the accepted structured mirror and can stale.

CLOSEOUT already says ONE HOME PER FACT; COMPLETION_SPEC already requires integrating accepted changes and affected displays. Another reminder is insufficient. Recommend one bounded producer/consumer repair: derive identity, quantity and open/closed status from accepted position records, carry source/as-of/unknown limitations, and tie position-dependent action text to the same instrument/version. Do not automatically rewrite research judgment or treat a fill as approval of a new recommendation. A changed/closed instrument should withhold incompatible current choices pending owner reconciliation; merely replacing a number can preserve an obsolete strategy.

Proposed acceptance: the preserved TLT/TBT case cannot render a live choice for a closed instrument or stale quantity; partial exits, multiple lots/accounts, missing/unknown state, retained historical rationale, and a position change between build/review are considered. Verify meaningful current output and preserve history. Owner PROME with existing FORGE/TERRY responsibility boundaries. Design/implementation not commissioned here.

### PC14-2 — demonstrated delivery coupling to another owner's unfinished packets

VERIFIED at code/artifact level. `argus_scope.build_scope` unions committed and pending paths. The review manifest includes OWNED, SHARED and UNATTRIBUTED paths; `verify_review` compares every manifest entry against the chosen commit before applying the explicit delivery-path additions check. Thus `--paths` does not restrict all content comparisons to PROME's delivery. The reader can list an unevidenced shared file unopened, yet its hash still gates the commit.

Read-only historical reproduction: parse `dc1abc44f:PROME/state/argus_review.json`; SHA256 every named blob at `dc1abc44f` and `27a26d1cd`, preserving absent as None. First commit has exactly four mismatches, all absent DEWEY packets:

- AGENTS/HENRY/inbox/2026-10-14_from-DEWEY_ports-pike-power.md
- AGENTS/VULCAN/inbox/2026-10-14_from-DEWEY_ports-pike-power.md
- AGENTS/WALTER/inbox/DEWEY/2026-10-14_ports-pike-power_handoff.md
- AGENTS/WATT/inbox/2026-10-14_from-DEWEY_ports-pike-power.md

Later `27a26d1cd` has zero mismatches. DEWEY's intervening `46299b920` committed the packet set. This corroborates PROME's reported wait; exact wait duration is unmeasured. It conflicts operationally with Pre-closeout item2's intention that foreign uncommitted work not block closeout.

Recommend separate delivery membership, relied-on evidence and merely observed concurrent work in the existing manifest/control. Keep the complete inventory and provenance; no blanket inbox exclusion or filename-based ownership shortcut. Verify delivery bytes against a named commit and dependencies against preserved, reproducible versions. An uncommitted source used to support PROME's conclusion remains a real dependency requiring persistence/disposition; it cannot be relabeled unrelated to obtain a pass. Unrelated owner additions/edits should not invalidate the delivery.

Proposed acceptance: replay today's four-packet case; unrelated work does not block, changed relevant evidence and unreviewed delivered additions do block; omitted/ambiguous authorship stays explicit; reproduce the prior PROME-authored nested inbox/data case from the perimeter; preserve missing-baseline failure and named-commit identity under concurrent HEAD movement. This is a consequential control repair requiring the existing independent review discipline, not a one-line filter or reopening the unrelated consumed-move exemption.

### PC14-3 — approved publication rule still contradicts the manual

VERIFIED: CLOSEOUT step11 says the Helm keeps Standard publication until WQ382(b) is ruled. Docket L665 records Will's October9 B ruling and explicitly says the rule is already in force, with encoding owed. L594 similarly carries applied work and pending manual integration. Finish that approved encoding, including applicable runner/source references and hosted-build-date treatment, within its existing scope/order. No new permission is required for the already-ruled change; CATO does not take over the owner's work.

This does not eliminate today's publication gap: Owed publication remains required and was reported unavailable. `check_publication_prereqs` checks explainer presence as an advisory, not the existence of publishing tools or actual hosted delivery. A passing gate cannot establish PUBLISHED. The correct report remains explicit about saved/committed, pushed and hosted states; distinguish not due by rule from required but unavailable. Today's early disclosure was appropriate. Restoring the supported publisher is separate from rewriting closeout; no migration is proposed or authorized.

### PC14-4 — reduce warning noise without hiding obligations or starting more machinery

L628 already has an apply-ready fix for upcoming catalysts hidden behind older rows; preserve the direct-calendar workaround until accepted. JANUS (L676/WQ416) is an approved boot triage helper using saved gate output, not demonstrated closeout acceleration. Respect its bounded trial; do not broaden it into another routine auditor. L675 records the approved maintenance ordering and retained state/visibility caveats. USER perimeter L591 is known debt; cited preferences were inspected today but full USER coverage was not certified.

Recommend presenting new failures, materially changed conditions and due actions first, with acknowledged unchanged debt compactly linked to its owner/next action. A known warning can still become urgent or block a dependent claim. Existing controls continue running; this advice does not waive any. Complete the high-value approved repairs rather than adding a parallel backlog or duplicate reporting system. Any changed priority across approved slots is a proposal, not accomplished by this review.

Keep accepted state current during work in its authoritative home. HANDOFF remains concise navigation under the existing contract, not a second live holdings/decision ledger. Closeout then checks and packages that state.

## Evidence interpretation and stop condition

PROME reports 17 blocking checks passed and 23 advisory checks evaluated in argus_baseline.delivery_receipt; CATO did not rerun or independently certify those checks. ARGUS run log reports 438 seconds observed, two corrections/two changed-portion checks, and 294 shared unevidenced paths listed unopened. Those are attributed run observations, not CATO timing or token measurements. The user transcript's 37m16s is whole-turn elapsed time; there is insufficient stage accounting to call it ARGUS time or promise a percentage saving.

CATO independently reproduced historical manifest/blob consistency, inspected the resulting commit paths and confirmed the control mechanism statically. Hash identity proves persistence/identity, not independent review of every path or correctness of financial content. `c67a68b12` adds the baseline/delivery receipt; live hosted contents remain UNKNOWN.

Stop this review here: the next useful work is owner implementation of approved maintenance and a bounded proposal for PC14-1/2. Use the existing ARGUS log at the next ordinary closeout to observe correction passes, unrelated-work waits, total effort where available and retained consequential catches. No new audit, monitoring project, savings claim or automatic follow-up is established. Prior CATO approvals remain untriggered.

## Delivery checks

Weekday check passed on five verified-readable inputs: PROME/DOCKET.tsv, PROME/GATES.tsv, PROME/WILL_QUEUE.md, AGENTS/CATO/CONTINUITY.md and this report. Direct startup measurements (bytes): CATO AGENTS 7,092; CHARTER 10,399; CONTINUITY 3,553; root CLAUDE 24,961; USER 6,654; AGENTS 5,313 — each readable and below 32,550. Generic read_cap_check --agent CATO returned rc2 CANNOT-EVALUATE because CATO has no local CLAUDE.md; not a pass. Orphan advisory showed foreign LIQUID/VIOLET/WALTER work, preserved, including WALTER’s staged rename. No superseded financial figure, STATUS, auto-memory or cross-directory output was authored, so associated conditional checks do not apply. Only this report and CONTINUITY are the exact-path delivery; Git receipt in-session. No hosted artifact publication applies to this CATO review.


## October14 — review of PROME’s bounded proposal at 3f9db4e15

Will requested checking the completed proposal and feedback. Start HEAD `7c6b0e2b31acc52ae01a3391462f063ae99b9834`; active WALTER work/staged rename preserved, no pull. This follows the same continuing assignment. Read the complete proposal/readiness evidence, changed-file inventory, handoff/docket links and recorded helper receipt; inspected actual option validation/rendering/store producer, BOOT pickup consumer, ARGUS freeze/promotion/callers, FORGE source headers, calendar patch hash record, and safe-push ref behavior. No owner edits, helper launches, messages, live store access or implementation tests. This is design assessment, not certification of unbuilt software.

### What is verified and worth keeping

- Commit3f9db4e15 changes six documentation/state files, not runtime code. Proposal is byte-unchanged in the current working tree. Handoff and existing L367/L402 plus new display row L702 link it. No software repair completion claimed.
- Same-byte capture for parsing and fingerprinting closes the *described* parse-old/hash-new race: parsing five shares then hashing a newly written three-share file must not certify the displayed five. Subsequent currentness checks remain necessary, and are included. This verifies the design reasoning, not executable behavior.
- The calendar tool currently hashes to10d14d7342a80f9de1f95590230a1509d659e7038efe58240e590bf36de450a8, matching readiness evidence and differing from the bundle’s before hash f84daeda1ac7eb10e85a3b3adee5bbfbbf3f02bb50bdd4d9bbd37ad0a3fd6ed4. Refresh is justified; the mismatch does not prove the underlying patch logic is wrong. Keep VIOLET-behind-VULCAN coverage/direct reads until accepted.
- A correctly distinguishes holdings from approval/order/fill evidence, protects partial exits and combined decision IDs, preserves UNKNOWN/account scope and blocks unsafe PLAIN fallbacks. B preserves full inventory and relevant dependencies rather than excluding all foreign-looking paths. Separate A/B episodes avoid bundling a portfolio feature and an audit-control repair under one ceiling exception.
- Independent review/lifecycle are owner-recorded: two plan reads, first concurrency finding corrected, changed-portion confirmation and explicit closeout receipt. ORCH_LOG/readiness openly retain UNKNOWN precise launch time and lifecycle reader rc1. CATO did not inspect the helper’s native transcript or certify full lifecycle compliance. No need to rediscover the already-reproduced DEWEY failure here.

### PC14-5 — clarify what may change without invalidating review

**Implementation boundary to resolve before B, medium consequence.** B requires changes to manifest membership/roles/hashes to invalidate its verdict, yet B5 requires unrelated packet additions/edits not to block. A new unrelated packet arriving after freeze has no role in the frozen manifest. If adding its observed-only membership invalidates the whole verdict, the repair recreates today’s wait in another form. If all new files are ignored, the unreviewed-addition hole returns.

Define the immutable reviewed delivery/dependency contract separately from the observed inventory, even if both reside in the existing manifest. State how a later file is classified using actual provenance and claim relevance; mere path/name or an unevidenced observed-only label cannot clear it. Changes to delivery/dependency membership or evidence invalidate dependent review; verified unrelated inventory churn does not. Ambiguity about a potentially relevant contribution remains explicit/non-passing.

Acceptance: add a proven unrelated DEWEY packet *after* freeze, then modify it; no rebuild or repeat ARGUS read solely for that churn. Add an otherwise similar PROME-authored nested packet or newly used dependency; it must block until reviewed. This resolves the interaction between two existing acceptance requirements, not a demand for a separate inventory service.

### PC14-6 — the selection consumer can now be named; protect stored operator words

**Complete the proposal’s declared prerequisite before A.** Producer is `decision_deck.py` RULING_JS: it writes one document per tap to `rulings`, with build/decision_id/choice information. Consumer is presently the manual `PROME/BOOT.md` step3b Artifact read_db/write_db pickup, referenced by both boot runner copies; the bounded tools search found no reason to assume an automatic importer. Candidate-file scope must include this consumer contract and any affected runner pointer, not only the renderer.

Specify the stored per-unit position/card basis, and test old stored taps without it as well as a stale tap after a quantity change. Preserve Will’s exact words/history; withholding automatic applicability is not deleting the tap, rewriting it against current options, or declaring his ruling never happened. Missing/obsolete basis needs an explicit reconciliation disposition before dependent action. Current BOOT already preserves stored meanings and unit boundaries; extend that behavior.

One concrete runtime trap: RULING_JS initially disables all `.btn`, then on successful database connection enables them all. A new guard implemented solely as disabled HTML can be undone by that connection step. A6’s runtime test must exercise store connection, card/peek paths and withheld units, not merely inspect static HTML. No assertion that this proposed guard has already been implemented incorrectly.

Hosted publisher/store access remains unavailable in the quoted owner runtime. Local simulated-store tests can verify behavior; actual hosted/store compatibility remains pending until available, rather than certifying end-to-end activation from a local build. This need not hold up independent B work.

### PC14-7 — name the verified commit and keep the shared push’s claim narrower

**Delivery receipt/caller clarification before B.** A full SHA prevents the verifier reading different commits across individual file checks. It does not pin `scripts/safe-push.sh`, which still sends HEAD. Example: verify commitA, then another session advances HEAD toB; B may be unrelated, or may change a reviewed file/dependency. An ancestry receipt proves A reached origin, not that the current remote contents still equal A’s reviewed content.

Keep root shared-push behavior unless separately authorized to change it. Explicitly record A as the reviewed delivery; distinguish later carried commits from that certification. For a claim that the pushed/current artifact is reviewed, reconcile relevant changes through the actual outgoing snapshot and withhold dependent publication/currentness claims if reviewed bytes changed. Unrelated commits should not cause a whole-fleet review. Preserve the named-SHA verification even when a later HEAD differs. Test both an unrelated successor and a successor changing reviewed content between verify and push; an old-commit success must not be relabeled latest-tree certification. No new Git wrapper or cross-owner commit authority is proposed.

### Additional practical refinement and implementation order

A says routine market marks must not invent a new decision, but its provenance includes source versions/hashes and any detected input change requires validation. Make the distinction executable: changed quote/receipt provenance with identical accepted identity/quantity/disposition must be reread/revalidated without automatically demanding owner re-approval of unchanged judgment. Changes to an explicitly price/valuation-dependent recommendation are different and must remain dependencies. Add that negative control to A5 alongside its existing unrelated-holding case; retain hashes for evidence integrity, use relevant semantic facts for recommendation applicability.

Finish relevant authorized maintenance in its existing order. When A/B are eligible and authorized, favor B first: it has a preserved concrete replay and can be validated locally; A requires a holdings adapter, current-unit migration and selection-consumer/hosted compatibility work. That is sequencing advice within the two repairs, not an approved displacement of L675/L628/L676 or L647/L665. The proposal’s initial authority paragraph describes design/readiness; no A/B implementation approval is inferred by CATO.

This Will-directed follow-up must remain in the continuing review history. The proposal records two prior plan reads; do not reset the applicable episode/read count at a fresh session or assume each implementation gets a fresh unused budget. Before proceeding, reconcile the required result-read allowance under the existing rule and actual Will authorization. No extra generic plan audit is commissioned here.

Stop this review after these concrete clarifications; preserve required independent result verification for actual code and its counterexamples, subject to that accounting. Ordinary-use efficiency remains unmeasured. No broader architecture redesign, forecast work, broker research or publishing migration follows from this assessment.

Follow-up delivery checks and exact-path Git receipt follow in-session. No financial figure/STATUS/auto-memory or cross-directory output authored; conditional consumer/ledger/memory checks remain untriggered.

Proposal-follow-up checks: weekday PASS on five verified-readable inputs (PROME DOCKET/GATES/WILL_QUEUE, CATO CONTINUITY and this report); scoped whitespace clean. Direct startup bytes CATO AGENTS7,092/CHARTER10,399/CONTINUITY4,027 and root CLAUDE24,961/USER6,654/AGENTS5,313, all readable/below32,550. Generic CATO read-cap rc2 CANNOT-EVALUATE for absent local CLAUDE remains a disclosed limit. Orphan advisory identified WALTER work/staged rename, preserved. Only this continuing report and CONTINUITY are CATO-authored delivery paths. No hosted publication applies.
