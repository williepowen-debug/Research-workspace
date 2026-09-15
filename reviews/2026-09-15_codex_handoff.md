# Codex handoff — Will’s independent repo review

**Session:** September 15, 2026. **Last implementation commit:** `f12c6dc94`, confirmed pushed to `origin/master`. This handoff is a snapshot; verify current Git state and owner records before acting.

## Subsequent discussion: CATO / RAV review

Will is considering a persistent independent reviewer running on Astra through Codex and prefers the name **CATO**. He asked us to review RAV’s maturity and identify what to reuse. [RAV assessment and proposed CATO direction](2026-09-15_rav-maturity-and-cato.md) is the latest review: useful methods/history, underbuilt continuity and stale instructions/dispositions; recommend a deliberate successor rather than a wholesale rename. **No CATO creation, RAV retirement or authority migration has been approved or performed.** The PROME work below remains open as recorded.

## Start here

You are continuing Will’s **independent second pair of eyes** on `/home/willi/Research-workspace`, starting with PROME. Will asked for this handoff when closing the session. Resume this review relationship; read the context below before proposing work.

1. Check `git status -sb`, staged paths and recent commits. Several agents share the checkout; dirty files may be active work.
2. Read root `AGENTS.md`, `CLAUDE.md`, and `USER.md`, then relevant PROME instructions for the task. `PROME/CLAUDE.md` owns its process controls; `PROME/CLOSEOUT.md` owns document roles and delivery order.
3. Read the current work table below and the linked record for the task being resumed. Re-check the corresponding DOCKET entry by content as well as physical line number.
4. Give Will a short status and a concrete next step. Do not repeat the original interview or ask again for the already-approved Deck layout.

## What this repo is

A multi-agent research workspace for detecting economic/market stress transmission and developing evidence-backed decisions. Domain agents own their evidence and judgments; PROME coordinates priorities, agent work, follow-through and Will-facing decision surfaces. Will makes capital decisions. TERRY handles trade construction; the broker/Will remain the source of actual execution truth.

Useful map (the referenced owner documents govern details):

| Location | Purpose |
|---|---|
| `AGENTS/<NAME>/` | Domain agent instructions, evidence, state, inbox/outbox and tools |
| `PROME/` | Coordinator instructions, operational records and tools; no `AGENTS/PROME/` |
| `PROME/ROSTER.md` | Agent membership, responsibilities and launch eligibility |
| `PROME/DOCKET.tsv` | Dated obligations and their dispositions; “L393” means physical line 393 |
| `PROME/WILL_QUEUE.md` | Will-owned decisions/actions; “WQ-253” is an identifier |
| `PROME/GATES.tsv` | Registered trigger states |
| `PROME/STATUS.md`, `SCRATCH.md`, `HANDOFF.md` | Operational state and continuity, with roles defined in CLOSEOUT |
| `PROME/tools/`, `PROME/registry/`, `PROME/artifacts/` | Generators/checks, structured records and rendered views |
| `HEARTBEAT.md`, `FORGE/`, `BOARD/` | Shared synthesis, portfolio/tooling area and signal board; respect ownership |
| `reviews/` | Our independent reviews and proposed edits |

The Helm and Decision Deck are private native Claude Artifacts. A generated local HTML file, a committed file, a pushed commit and a published artifact are different completion states.

## How Will wants us to work

- His concern: agents sometimes make mistakes or call work complete before it actually is. Check original obligations, artifacts, owner-state changes and remaining work; do not accept summaries as proof.
- Priorities: **bloat, hidden breakage, staleness, and whether a better procedure exists**. PROME comes first because the workspace’s usefulness depends on it.
- He wants involvement in bigger changes. Make clear, low-risk fixes; prepare concrete text or a working preview before asking about a consequential choice.
- Stay practical. Prefer repairing an existing control or clarifying its owner over adding another policy, scorecard or repeated reminder.
- Give candid findings, including when PROME’s self-criticism overstates what happened. Separate implementation, tests, independent verification and unresolved conditions.
- Carry approved work through without repeated permission requests. Communicate briefly during work. Do not imply a whole-system certification from a bounded review.

This session worked as an external reviewer/editor, rather than taking over the live PROME desk. We did not run operational boot/closeout merely to close our review: those flows can change live state, spawn desks and regenerate unrelated surfaces. Read their rules where applicable; do not mistake this handoff for a request to operate the fleet.

## Completed work

| Commit | Result and verification |
|---|---|
| `24b820577` | Repaired ARGUS test fixtures to patch module ROOT for temporary repositories, including nested cases; moved the gate-test entrypoint below all classes. ARGUS 28 tests, gate seven via direct/discovery, ledger 24, plus ROOT/cwd restoration passed. Corrected STATUS’s stale L247 F4 disposition. These small repairs were self-tested, not independently result-reviewed. |
| `71d554b92` | Revised the **proposed** continuity cleanup sample. Removed a proposed duplicate reminder; preserved the recurring roll-hazard guard and current-host verification. Live cleanup not applied. |
| `2ae76c7c4` | L381 bounded instruction reconciliation: spawn authority pointers, original-obligation/artifact checks, follow-up ownership, WQ-249 closeout-ask evidence and display/publication integration. Independent plan/result reads completed; result had no blockers. |
| `f12c6dc94` | Implemented Will-approved Owed/reference Deck split, tests, generated pair and closeout publication instructions. Seven new fixture tests (including Node UI/store stubs), 23+28 related tests, parser selftest and exact pre/post card HTML/order comparison passed. Independent result read had no blockers. **Not published.** |

All four commits were confirmed on origin/master. Authoritative details:

- [Initial review](2026-09-15_prome_second_eyes.md)
- [Continuity sample — still proposed](2026-09-15_prome_continuity_sample.md)
- [L381 implementation, review receipts and residue](../PROME/plans/2026-09-15_L381-reconciliation.md)
- [L333 trial evidence and original L393 measurement](../PROME/reports/2026-09-15_L333-L393-followup.md)
- [L393 approved split, verification and publication handoff](../PROME/plans/2026-09-15_L393-deck-split.md)

The earlier L333/L393 report describes the pre-approval design stage; the L393 implementation record supersedes its “awaits Will” status.

## Open work and suggested order

### 1. Finish L393 publication when native tools are available

**Already authorized:** Will explicitly replied “Approve Owed/reference split.” The implementation exists. Do not rebuild the proposal or request this approval again.

- `PROME/artifacts/decision_deck.html`: Owed + Key, with complete explanations and raw fallback. About 62% smaller than the comparable pre-split render at validation time.
- `PROME/artifacts/decision_reference.html`: full Decided/In-flight/Docket, no ruling-store client.
- The pair currently uses **local relative links**. Do not upload it as-is to hosted artifacts.
- Owed must retain the existing private artifact and attached `rulings` store. The generator validates its ID and rejects duplicate hosted IDs; the implementation record has the URL and exact CLI recipe.
- Still needed: native authenticated Artifact access, compliant reading of the existing live artifact, a private reference artifact URL, grounded WQ-253 explainer coverage, generation with paired hosted URLs, normal candidate verification, publication, and hosted link/store checks.
- Native Artifact view/store/publish tools were unavailable here. Sites tools were a different hosting system, not a replacement. Re-discover available capabilities in the new session; absence here is not proof of absence there.
- A smaller replacement does **not** solve the initial full-read/migration requirement by itself. Preserve privacy and real saved rulings; do not manufacture a Will decision to test the store.
- Declared minor residue: Key’s “Docket tab” wording and historical bookmarks to decided cards at the old URL. Local code review did not verify native integration or browser rendering.

### 2. Prepare L333 for the September 19 trial grade

Useful ARGUS catches are recorded, but no defensible aggregate prevention score or routine cost was established. Labels duplicate “run 2”; rechecks overlap; some findings arrived after commit or used a stale/moving scope.

Next useful work: identify the **first four eligible Standard+ closeouts**, map each to its actual returned ledger and delivery timing, deduplicate findings and separate ARGUS-before, ARGUS-after, author catches and later outside catches. Do not select the four cleanest sessions or turn repeated passes into additional sessions. If delivery evidence is missing, say the comparison is unmeasurable. Preserve the existing September 19 sitting; no new scorecard was installed.

The cost report’s 357,663 tokens includes two development reviews. It is not the four-closeout operating cost. See the linked evidence review for exact distinctions and sources.

### 3. Observe L381 behavior; then stop expanding the process

Instruction changes are implemented and independently source-verified. **Two ordinary completed orchestration sessions remain to be observed.** Editorial sessions and mid-session receipts do not count. Use existing task/artifact/ORCH_LOG evidence; no new standing scorecard.

The change preserves authority. It does not discharge **L378**, the separately registered closeout-ask mechanization work. Existing playbook Git wording and Completion Purpose framing remain declared residue in the L381 record.

### 4. Optional continuity cleanup

The sample in `reviews/2026-09-15_prome_continuity_sample.md` was revised at Will’s request, but **not applied** to live STATUS/HANDOFF. If resumed, re-check current source text and continuity routes, then involve Will in applying the concrete sample. Do not infer that approval to revise a proposal was approval to apply it.

Also keep the L247 distinction intact: F4 closed; F3/F8 and RED’s F1 v0.3 recheck remained owed at our review. No authorization to implement Kernel code came from our STATUS correction.

## Practical safeguards for the next session

- Shared checkout: at handoff preparation there was active-looking work in WALTER, BOARD, FORGE tools and `PROME/registry/READS.tsv`, including **staged WALTER inbox renames**. It was not ours. Do not reset, sweep, stage or commit it. Recheck state instead of treating this list as permanent.
- Use exact file pathspecs. Our commits used `python3 PROME/tools/commit_check.py commit --stage -F <message-file> -- <exact files>` and `bash scripts/safe-push.sh`, then confirmed origin ancestry. The wrapper commits only the named paths, preserving unrelated staged work. Follow current root Git rules.
- For canon-class changes, PROME’s WQ-178 requires one independent plan read and one result read. WQ-229 requires acceptance conditions before consequential repairs and a reader’s own counterexample. Consult current canon; warnings have a declared-residue discipline. These rules authorized the bounded read-only reviewers used here.
- Use `PROME/tools/measure.py` for reported byte/line/CRC measurements. Large TSV rows and historical docs can exceed tool output limits; read bounded chunks and never claim to have read truncated output fully.
- Temporary `/tmp/prome-l393/` previews are disposable. Tracked code, artifacts and records above carry the durable result.

**Closing state:** implementation work saved and pushed; hosted publication and the observations/grade above remain open. Will ended the session, rather than asking us to continue those tasks now.
