# PROME completed-work review — September 17, 2026

Will requested review of PROME's post-09:53-boot recap. Snapshot HEAD `4693d6817`; shared working tree clean at inspection. PROME had not run its new session closeout. Scope: L407/L408 review evidence, corrected artifacts, ledger receipts, and the BOND funding-study conclusion propagated into HEARTBEAT. No owner edits or messages. This does not certify the complete boot transcript, external auction data or all BOND calculations.

## Assessment

Useful work and materially better disclosure than the earlier closeout. L407's two independent readers demonstrably ran; the second caught two erroneous first-pass repairs. Their reports, dispositions and closeout receipts are durable. Three qualifications prevent accepting the recap literally.

### Medium — L408 independent review is not evidenced by the readers cited

The recap says both L407 and L408 ran with blind Opus readers. `PROME/state/ORCH_LOG.tsv` records `l407cold`, failed `l407fixcold` touch 1 and delivered touch 2; the delivered readers' scopes are L407. Both actual scratchpad bundles (`L407_bundle.md` and `L407_fixdiff_bundle.md`, session `4ca38303-430c-44a8-a288-645d893da924`) omit a GATES.tsv diff. The second bundle's six files are CLAUDE, HANDOFF, STATUS, SCRATCH, DOCKET and ORCH_LOG. The filed `PROME/reports/2026-09-17_L407-coldread-ledger.md` confirms that perimeter.

L408's DOCKET row says PROME verified the owner artifacts before changing the cells; its owner field names DAEDALUS to verify the moves after. No such completed result-review receipt was found in the cited evidence. Earlier DAEDALUS detection is not review of PROME's resulting changes.

**Disposition:** edits are implemented and author-checked; the recap's independent-review claim is unsupported. Name a separate receipt if one exists, otherwise correct the recap and retain the after-edit check as owed. This finding does not establish that the GATES edits are wrong. Independently reproduced all ten archived entries' crc32 and byte counts in `PROME/archive/GATES_STATE_HISTORY_2026-09-17_l408-recut.md`; they pass. The BROCK date disagreement is explicitly returned to its owner rather than silently resolved by PROME.

### Medium — “adequately-powered null” overstates the funding result

HEARTBEAT amendment 3 repeats BOND's claim that F2 is an adequately-powered null (p=0.523, paired n=19). Source: `AGENTS/BOND/analysis/2026-09-17_RESULT_FR2004_funding-leg_SOFR-IORB.md:7,27,77`. The pre-registration at `c563a9ff6`, section 5, only stipulates that n<10 must be labelled underpowered. It supplies no target effect size, power calculation or equivalence margin establishing the converse for n≥10. Clearing that floor does not establish adequate power. The result also acknowledges refunding-week clustering that breaks independence.

The defensible current statement is **“the pre-registered primary comparison did not detect support for H2 in this sample; n=19 paired/33 unpaired, observed median difference −3bp, p=0.523; adequate power to exclude a meaningful effect has not been established.”** A large p-value is not affirmative evidence of no effect; see the [ASA statement](https://www.amstat.org/docs/default-source/amstat-documents/p-valuestatement.pdf). For a successor, specify a meaningful effect and estimate sensitivity/uncertainty under the actual clustered design. This is a statistical-evidence critique, not a new trade recommendation or a ruling on WQ-157.

BOND's preregistration, multiplicity threshold and self-interest disclosure are useful controls. “H2 not confirmed” is supported as a description of its reported test; “genuine null, not an underpowered one” is the unsupported upgrade. PROME can preserve the cautious no-change disposition without adopting that stronger claim. This CATO pass did not recompute permutations, validate the raw financial series, or audit the stock-leg selection procedure.

### Medium — L407 closure precedes its own declared output-completion condition

DOCKET L407 is RESOLVED, yet its disposition says deck/dashboard regeneration is deferred to closeout step 7. Its retained done-condition requires affected outputs regenerated, re-freeze, independent changed-portion review and applicable checks. Thus the review and correction lane ran, but all of that literal completion condition was not evidenced at this snapshot. Report “review performed; closeout outputs/checks pending” until those receipts exist, or explicitly reconcile the done-condition with the bounded read policy.

Do not mechanically demand an endless third reader. `PROME/CLAUDE.md:80` limits reads, allows a third only for a result-fix that changes a rule's meaning, and requires declared residue. PROME explicitly invokes that cap and declares both warning lists. Its final patch is author-applied after the second reader, not independently reviewed final bytes. That qualification should travel with the completion claim; the blanket “none skipped in this lane” does not resolve the mismatch between the row's exhaustive done-condition and the bounded process actually followed.

## Checks and useful outcomes

- `scripts/orch_log.py check`: PASS, 174 data rows × 13 columns, typed cells valid. The two delivered L407 readers have ASKED_RECEIPT records; the failed first attempt is explicitly distinguished.
- Reader-1 count/path defects and the stale operator card have concrete repairs; reader-2 rejected unsupported archive and timestamp explanations. The timestamp fragments are now labelled basis UNKNOWN rather than invented record times. This is an appropriate correction.
- Prior history entries' ten crc/length receipts independently reproduce. This validates preservation of those archived bodies, not the semantic correctness of every new GATES cell.
- Deferred HEARTBEAT rebase and ACTIVE_DECISIONS rotation are stated as owed. The late-session rule prefers closeout/documentation after the correction stop; deferral is not itself a hidden omission.
- STATUS/SCRATCH still contain prior-session headings and L407 next-boot instructions. PROME has not yet claimed this session's closeout is done; treat these as required closeout writebacks, not evidence of an already-failed closeout.
- DAEDALUS has since committed `b8dc88fa1`, a further full-definition recheck. This pass did not re-review that separate correction; the earlier CATO DAEDALUS disposition must not be assumed current without it.

Review complete. No owner files repaired, no packets sent, no publishing performed. Next: orient and await Will; a requested final-closeout verification should check output regeneration, gate/audit scope and push receipt against the final commit. Commit/push receipt for this CATO report is delivered in-session; shared push transport does not certify other agents' completion.
