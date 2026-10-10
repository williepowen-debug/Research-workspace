# ARGUS efficiency — preliminary advice, October 10

Will requested help with PROME's latest closeout/efficiency thread and supplied its earlier assessment during this review. This is bounded advice, not another review round on the final corrections or approval to build.

## Assessment

Keep the independent audit; improve its inputs and correction process before adding another general lint system. ARGUS caught omitted operator rulings, a consequential result. That does not establish cost-effectiveness across sittings. Judge total audit-plus-repair effort and retained consequential catches, not findings per run.

1. Repair existing queue validation. `PROME/tools/table_check.py` labels UNDER rows harmless and succeeds absent OVER rows; `decision_deck.py:parse_done_table` skips rows with fewer than three cells. Rendering tolerance is not consumer completeness. Recommend schema-specific malformed-row rejection and source-ID/parsed-ID reconciliation through ledger and generated decision data. Do not reject every short Markdown row globally.
2. Reduce shared-path reading only with evidenced attribution. The recorded run had 36 OWNED and 323 SHARED paths, 318 inbox paths. `AUDIT_PERIMETER.tsv` retains these because earlier filename filtering hid PROME-authored output. Keep a complete inventory, establish authorship of changes and read PROME's changes plus claim dependencies; ambiguous ownership remains explicit. Blanket inbox exclusion or a from-PROME filename filter recreates the documented counterexample. Safe implementation and savings remain unassessed.
3. Bound correction scope. The run log records eleven warning fixes, described as one-token/bookkeeping. The correction reader found wrong-column deadlines, replacements that never landed, premature completion claims and a wrong event date. Some warning fixes may be necessary; this does not establish all were optional or prohibited. Keep consequential corrections, inspect actual resulting fields before claiming completion, and leave lower-impact residue under existing rules.
4. Run relevant structural checks before freezing and rerun affected checks after correction. The current final gate follows ARGUS and already invokes table/parser checks. Short-row handling is a coverage gap, so a wrapper alone cannot cure it. `wq_ledger.py:cmd_check` validates its own rows and seal, not source completeness; `date_of` selects the first ISO date in prose. Explicit ruling-date handling is another relevant boundary; generic lint cannot reliably infer intent from arbitrary prose.

## Evidence and limits

Initial pin `e4134b88a9405c86b632f6420e2c91c1fd99a0f5`, shared master; foreign WALTER, REGINALD and auto-memory changes preserved. No pull, owner changes, messages, launch or operational boot/closeout.

Inspected sources: `.claude/agents/argus.md`; `PROME/state/AUDIT_PERIMETER.tsv`; current run/calibration in `PROME/argus/MEMORY.md`; correction account in `memory/2026-10-10.md`; `PROME/state/argus_review.json`; relevant `PROME/CLAUDE.md`, `CLOSEOUT.md`, `tools/prome_gate.py`, `table_check.py`, `decision_deck.py`, `wq_ledger.py` clauses/functions.

Owner-recorded run: 50 claims, eight errors, twelve warnings, 238,445 tokens, 83 tool uses, 676 seconds. No native transcript or accounting inspection: not independently measured, not a billing/unique-input claim, and no measured inbox share of cost. About eleven minutes covers the initial run; correction and parent effort are additional and unmeasured here.

Final receipt discloses later corrections checked by instruments without a reader. REVIEWED metadata and hash identity do not independently verify those corrections. No final-content certification or additional reader here. Static code inspection supports the checker mismatch; no runtime probe or test suite run. Earlier trial history and overall policy compliance were not re-audited.

## Resume

Recommend a revised bounded proposal repairing existing checks and explaining shared-path attribution, tested against omitted rulings and the historical hidden-packet case. Compare ordinary closeout effort after implementation; no monitoring project or promised savings. No implementation assignment remains; prior approvals survive untriggered. Delivery checks and Git receipt follow below/in-session.

## Supplied earlier assessment — changed advice

PROME proposes OWNED-only reading, owner/count summaries of the rest, five-class pre-freeze lint, compact pass reporting, token/time logging and a later-catches line. Agree with reducing unnecessary input, preventing deterministic defects before review, concise reports and modest reuse of the existing log. Revise these claims before building:

- **AE1, consequential scope advice:** SHARED is unknown authorship, not established other-desk work. The perimeter's recorded FALCON inbox/data counterexample proves the proposed blanket exclusion can hide PROME's own output. No applied finding in prior runs, even if established, does not settle this risk. Keep visibility and evidence-based attribution, not path-name guesses.
- **AE2, automation limits:** the five classes mix structural checks with semantic judgments. A hash/path's existence, schema and explicitly sourced count can be checked; an early claim overtaken by new evidence, or historical pending versus current done, may require contextual judgment. Recommend named inputs and independently expected outputs for each proposed check, and preserve judgment in ARGUS. The malformed ruling-row failure is a particularly valuable concrete first case.
- **AE3, cost inference:** 323 of 359 paths is about 90% of listed paths in this run, not established token share or time share. The morning 160 of 207 is about 77%. No native trace inspected here. Use these as a reason to investigate scope, not a demonstrated 90% saving.
- **AE4, report/calibration:** current `.claude/agents/argus.md` already requests aggregate pass counts, detailed error/warning lines and fewer than 60 lines. Enforce that before assuming a charter rewrite is needed. Its CALIBRATION is for applied/declined finding classes; repairing one instance does not justify suppressing future recurrences of that class. Automate detection or remove the defect source where useful.
- **AE5, later catches:** use the existing column and separate within-scope misses, later edits and out-of-scope reasoning critiques. CATO's critique of a judgment outside ARGUS's remit is not automatically an ARGUS miss. Thirteen-run effectiveness and four truncations are PROME's supplied assessment, not independently re-counted here. One retrospective line without linked evidence cannot establish coverage.

Recommended sequence: repair existing validation and enforce compact output; design safe shared-path reduction; compare one ordinary run's total audit/correction effort and consequential coverage with the recorded baseline. No standing new measurement program. Do not retire ARGUS or promise that lint handles all five classes.

Checks: weekday check passed on five readable files: PROME DOCKET.tsv, GATES.tsv, WILL_QUEUE.md; CATO CONTINUITY.md and this report. Startup direct bytes at first check: CATO AGENTS/CHARTER/CONTINUITY 6,465/9,921/29,970; root CLAUDE/USER/AGENTS 24,961/5,200/5,313, all below 32,550. Generic CATO read-cap returned rc2 CANNOT-EVALUATE for absent local CLAUDE.md, not a pass. Orphan advisory identified foreign WALTER/auto-memory work, preserved; no CATO cross-directory output. No STATUS, memory-auto or superseded financial figure edits, so corresponding conditional checks do not apply. Final text/whitespace checks rerun before exact-path delivery; receipt in-session.
