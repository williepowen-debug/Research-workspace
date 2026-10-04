# Harness audit — final primary remainder, reader B

Date: 2026-10-04. Source pin: `68f8b049a5f5bbd19332f1eb6a4e76c80621ec46`. Seven assigned primary charters fully read: HOMER, MIDAS, ORACLE, OSPREY, OTTO, WAL, YURI. This is a bounded independent raw read under the existing audit, not an owner review, runtime audit, domain profile refresh, or authority to implement.

Method: `sweeps/HARNESS_AUDIT_SWEEP.md:5–9` and `HARNESS_AUDIT_2026-07-07.md:13–30`, both fully reread for this portion. Test action versus rationale, existing mechanization at its real invocation and result handling, and canonical ownership. July's repaired classes are counterexamples, not automatically reopened findings. No model-version or hook-liveness inference was made. Charter byte totals are evidence metadata; injected charters are outside READ_CAP rule 20, so this report makes no charter-cap finding.

**Result:** three retained medium instruction conflicts, two low wording/ownership issues, and bounded KEEP dispositions for the remaining examined gates. All proposed remedies are **UNVERIFIED-REMEDY / unapproved**: no owner files, tools, controls, schedules or shared rules changed. Guard-sensitive wording needs the existing owner/approval lane. Parent reports DC6 resolved by `69bffac65`, reserving ONE consumer read of the final fixed commit/manifest/delta including tranche 3; that is coordination evidence, not an executed consumer receipt. These additions remain **CONSUMER-PENDING**. Whole-sweep clock, grade, original October 5 obligation and Helm protection are unchanged by this raw report.

## Ranked retained findings

### B1 — MEDIUM: OSPREY's local packet rule conflicts with mandatory author commit

**Evidence:** `AGENTS/OSPREY/CLAUDE.md:76–79` cites root as owner but then says signals delivered into another agent's inbox stay untracked and should be flagged to Will instead of committed. Root `CLAUDE.md:74–79`, specifically carve-out ① at 77, says the author may and must commit self-authored inbox packets with explicit paths and recipient-named subject. This is an executable contradiction at the delivery boundary; a general canon pointer does not remove the opposing local instruction.

**Disposition:** REWRITE the OSPREY-specific exception into the existing root-canon reference; STRIKE only its contrary untracked requirement, subject to owner approval. Preserve author ownership, explicit-path scope and unrelated shared-file exclusions. No new delivery control is proposed.

**Refuters/limits:** root already controls. A conscientious operator following root can deliver correctly. OTTO's repaired `CLAUDE.md:216–230` expressly supersedes its old untracked instruction and is a positive counterexample, not another occurrence to reopen. This report does not establish an uncommitted OSPREY packet, lost delivery, or a live violation. A newer authoritative OSPREY amendment would supersede this finding; none is present in the pinned charter. Only the two opposing instruction sources are necessary for this verdict; live inbox/history inspection is unnecessary to prove the contradiction and was excluded.

### B2 — MEDIUM: OTTO still instructs replies through its deprecated OUTBOX

**Evidence:** `AGENTS/OTTO/CLAUDE.md:117–123` step 5 directs substantive replies via `OUTBOX.md`; the same full charter at 290 marks that file a deprecated HERMES transport buffer containing nothing live. Current routing at 185–187 and 320–325 uses WALTER, with a specific direct ASK-answer exception and a same-commit WALTER signal when the answer also carries a firing. Those gates distinguish reply classes; the older OUTBOX instruction does not.

**Disposition:** REWRITE the inbox-reply instruction to cite the current routing rule and preserve its ASK-answer/firing distinction; STRIKE the active OUTBOX destination, KEEP its historical deprecation label. This is existing routing residue, to deduplicate against the parent audit's OTTO routing route rather than count as a new implementation package.

**Strong refuters:** the operative routing section was corrected September 2 and clarified September 24. The charter itself refutes a prior DAEDALUS claim of zero WALTER drops: line 325 identifies a filename-pattern mistake and 17 historical drops. That historical count was not independently replayed here and is not used as new runtime evidence. Correct current routing and a deprecated table entry constrain the harm to a conflicting fallback instruction; this is not proof of current bypass or message loss. The July S5 repair is not declared globally undone by this one surviving clause.

### B3 — MEDIUM: ORACLE's numbered closeout can change STATUS after the brief fold

**Evidence:** `AGENTS/ORACLE/CLAUDE.md:46–50` sequences STATUS, workbook, SCRATCH, then mandatory NEXUS_BRIEF step 11, followed by step 12 roll-watch work that writes STATUS flags and the brief's forward catalysts. No final-STATUS ordering constraint appears elsewhere in the fully read charter. Canon `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md:162–165` requires the fold after final STATUS and immediately before commit; refreshed-every-session alone is specifically insufficient.

**Disposition:** REWRITE the closeout ordering/pointer so roll-watch decisions precede the final brief fold. KEEP roll-watch, every-session refresh and the no-change stamp floor. This concerns the existing obligation, not a proposed extra verification task. Amendment 11 at schema 164–165 is an invariant and explicitly must NOT be propagated as a new owner closeout step; this report does not propose doing so.

**Refuters/limits:** step 12 already calls for updating the brief's FORWARD CATALYSTS, so a careful owner could keep content aligned. That does not explicitly refold the full brief or final STATUS pin after all roll-watch changes. HOMER 225–226 deliberately places its final fold after its docket sweep; WAL 86 and OTTO 188 already say LAST. Their repair is retained. No ORACLE content-stale brief, wrong hash, missed roll, or observed closeout breach was sampled. A governing final-fold instruction applicable to ORACLE outside the reviewed charter could constrain execution, but would not erase this local sequence's ambiguity. Schema clauses are sufficient for the instruction finding; live briefs and commit-time replay are excluded runtime coverage.

### B4 — LOW: ORACLE's consumption-proof list mixes producer activity with consumption

**Evidence:** `AGENTS/ORACLE/CLAUDE.md:18–20` names consumer reading/citation and TERRY handoffs, but also lists ODDS_LOG/HISTORY accruing under PROOF OF CONSUMPTION. Accruing producer logs establish production; alone they do not establish another agent used the output.

**Disposition:** REWRITE that label or separate the producer evidence from actual consumer evidence. No telemetry addition or new receipt task is proposed. **Refuter:** the same line explicitly includes a NEXUS read and consumer citation, which can count; this is not a claim that ORACLE lacks consumers or that any maturity decision relied on log accrual. Actual consumption remains outside this pass. Route as optional low wording cleanup if it does not compete with B1–B3.

### B5 — LOW: OTTO's pre-Phase-3 ownership statement survives the canonical thesis migration

**Evidence:** `AGENTS/OTTO/CLAUDE.md:141–149` says STATUS owns the thesis block until Phase 3, while the canonical ownership table at 263–270 says `thesis/THESIS.md` now owns the versioned narrative, STATUS is a live-state mirror, and the changelog moved to `thesis/CHANGELOG.md` June 9. Line 57 onward also presents the thesis directory as established. The explicit migration and ownership table refute treating the older conditional as current ownership.

**Disposition:** REWRITE/demote the obsolete pre-migration assertion; KEEP the live dashboard/mirror action and canonical thesis pointer. Bare CHANGELOG references are not separately counted as missing files because they can be shorthand. **Limit:** this is local ownership residue, not evidence of competing current theses or an owner migration task. Deduplicate with the existing OTTO harness rewrite route. All wording changes remain unapproved.

## Per-file three-leg dispositions

KEEP means retain the examined instruction, not certify every dependency or live execution. No whole-file deletion is proposed.

| Full primary | Action versus rationale | Actual mechanism/callsite disposition | Canonical ownership disposition |
|---|---|---|---|
| HOMER | KEEP source/denominator gates, state retention, ledger write-back and final-fold action. Historical ruling detail may be compressed only with provenance preserved; no blanket model-based deletion. | KEEP byte-check call at 215–218 and rent-breadth invocation/contract at 102/114. `rent_breadth.py` fully read: real main calls load/series, fixed-roster assertion, integer band comparison, incomplete pairs UNGRADED and input SHA output. The byte one-liner actually tests both declared tiers; it prints a verdict, while the owner supplies the action gate. | KEEP repaired 32,550-byte tier and root Git overlap reference at 212/227; final brief follows docket changes at 225–226. Frozen KB versus active KB_LIVE distinction remains explicit. No July/September finding reopened. |
| MIDAS | KEEP four-leg boot, board receipt intake, consumed-vintage judgment and no-force-grade discipline. Closed-question one-shot graders are explicitly excluded by design (35/240), not an unwired-orchestrator defect. | KEEP `boot.py` invocation at 35: actual main 247–282 calls metals watcher, staleness, prediction scan and COT leg. COT leg calls `cot_gold.fetch/extract_gold` at 214–219, compares source/ledger vintage and returns 0/1/2; summary 285–295 distinguishes failure/REVIEW/quiet. Modules' internals and current source/ledger correctness excluded. | KEEP STATUS/open-items split and canonical source pointers. Legacy communication summaries need route-class context before alleging bypass; no broad route violation retained. Unwired future `cot_metals` consumption dependency is acknowledged design scope, not authorization to build. |
| ORACLE | REWRITE B3 ordering; KEEP live-source, roll-watch and metrics invocation gates. REWRITE B4 evidence label. | KEEP existing spread guards as a bounded positive check: CLI main actually calls `_check_leg_live` on both arithmetic legs at 207–208; context closure guard is separately used at 226–229 and displayed/logged at 267–292. Stale-pair guard is active at 232–243. No new automated closeout proposed. | NEXUS owns brief schema, so cite its existing final-fold obligation. Preserve current v5 vintage boundary and PortWatch instrument-label correction. No claim of runtime roll failure. |
| OSPREY | KEEP active-theater in-content freshness/manual disposition gate at 37 and signal conditions at 73–74. REWRITE conflicting local delivery rule B1. | KEEP strike-feed invocation at 37: actual main fetch/parse loop 170–219 produces explicit FETCH_FAILED/EMPTY_FEED/PARSER_STALE evidence; output headers and NOT_READ counts at 223/238–242 preserve unread coverage. It returns 0, so the charter's manual row disposition is significant and is not redundant solely because the script exists. | Root owns author commit; STRIKE only B1's conflicting exception after approval. Charter 210's late historical tail is stale prose, but its dated September 8 withdrawal controls and does not reopen the band decision. |
| OTTO | KEEP real boot/closeout actions and current ASK/firing distinction. REWRITE B2 and B5. Historical incident blocks can be rationale candidates, but deleting operative exceptions without checking scope is not justified. | KEEP real `scripts/boot.py` dispatch: BOOT_SEQUENCE 52–55, subprocess runner 58–77, dispatch 108–115, marker/rc handling 145–156, staleness 158–169 and final exit 186. Existing stderr relay and marker logic refute treating the old rc-only bug as present wholesale. Child emitters and successful live invocations not tested. | KEEP corrected self-authored commit rule 216–230, routing 325, canonical thesis ownership table 263–270 and final brief fold 188. Narrow surviving contradictions rather than reopen already repaired delivery/routing history. |
| WAL | KEEP instrument-light manual boot, stale-claim judgment and board consumption receipt actions; no forced boot.py build. | KEEP explicit `kb_expiry_check.py` and `predictions_due_check.py` invocations. Inspected actual parsing/result sections and main exits: expiry is explicitly advisory/rc0 (charter185); predictions quiet output distinguishes overdue/blank and optional strict rc. These are not runtime pass certificates. `derived_drift_check.py` internals unexamined. | KEEP receipt owner distinction at 71/184, final brief LAST at86, and de-listed mutable inventory counts at180. Legacy outbox prose is not sufficient alone to assert current route bypass; classify against messaging exceptions before a future owner rewrite. |
| YURI | KEEP actor-evidence, no-trade, in-content due-date and manual ledger-resolution gates. Explicit future mechanization at85 is not an installed-but-unwired finding. | Tree metadata showed no tracked YURI scripts at the pin. Shared corrections invocation at87 matches actual CLI normalization/known-agent gate/cmd_check dispatch in `scripts/corrections_boot_check.py:419–428`. This verifies wiring at the read callsite, not complete correction-check semantics or a successful YURI run. | KEEP root Git/canon references and separate spawned versus ordinary closeout contexts. Full overdue-row scan at85 controls over newest-row shortcut at97; no actual forgotten intent row shown. Launch-loading, remote source reachability, model behavior and first-firming completion UNKNOWN. |

## Counterexamples and excluded upgrades

- HOMER's September 29 byte tiers supersede the old 150/170KB claim. Its specific final-fold and Git-overlap repairs control; file length alone is not a defect. Rent breadth's integer denominator/roster guards are visibly in its actual computation. This does not validate current rent data or band calibration.
- MIDAS's COT freshness leg is genuinely called and contributes to the final verdict. Its marker contract candidly states that warning markers were inert at build time (`boot.py:81–88`); this is not promoted into evidence that an event occurred. Closed one-shot graders must not be wired simply to satisfy an audit count.
- ORACLE's settled closure context is visibly suppressed in the actual output/log path; the prior unwired guard is a counterexample. The repaired v5 strike/vintage and IMF-print label are retained. A generic older explanatory paragraph does not justify revoking current methodology or making a market recommendation.
- OSPREY's final line in charter210 says the basis-pair audit has not happened, despite the same paragraph's dated September 8 audit/withdrawal. Treat it as an optional historical-tail rewrite only; the current band is expressly unchanged. The feed emits failed/empty/stale coverage as rows and labels it NOT read. No source fetch or precision/recall acceptance rerun was performed.
- OTTO's final-fold instruction governs even though a subsequent consistency check could cause another edit: this warrants obeying LAST, not a second B3 allegation. The active OUTBOX clause remains different because it affirmatively names a deprecated destination. Historical quoted untracked instructions are clearly demoted and are not themselves defects.
- WAL's advisory return code is explicitly described as advisory; no false claim of strict enforcement was inferred. The excerpt shows the expiry quiet branch does not print all blank/bad counts; this report does not certify parser completeness or recommend a guard rewrite without its full contract/caller context. Predictions warning output is not proof of clean input or grading.
- YURI's absent boot script is compatible with an explicitly deferred first-firming increment. No script, model capability, source reachability or hook was invented to fill that gap. The intent self-falsifier's domain adequacy was not graded.

## Dependencies, read limits and delivery

Necessary dependencies for retained findings have been read: B1 root carve-out plus OSPREY clause; B2/B5 the full OTTO charter; B3 canonical schema ordering/scope clauses plus full ORACLE charter; B4 the producer/consumer distinction in its full charter. These verdicts need no current market observations, live boot or owner-session inspection.

Excluded rather than silently satisfied: complete child-script internals, domain ledgers/current state, live/source results, historical execution replay, runtime launch/load behavior, complete messaging exceptions, producer-to-consumer receipt chain and complete deployment/settings/hooks. The script excerpts only support the named path/guard/callsite checks. No recursively referenced design/spec/template was automatically credited as read. Supporting excerpts do not become primary full-file completion. The seven full charters can be added to the parent's primary-read census; support scope below is independent and must be deduplicated against its existing census.

The parent owns synthesis, deduplication, final result review and existing owner handoff. Final additions need the reserved consumer read of the consolidated fixed commit/manifest/delta, then truthful delivery/acceptance write-back. Accepted read capacity is not completed audit delivery or applied repairs. This raw artifact grants no owner-edit authority and schedules no new work.

## Source manifest and exact read depth

All primary and code/canon hashes below are bytes from the source pin, exported under `/tmp/daedalus-harness-final-b-20261004/`. Primary chunks were read in full with no unrecovered truncation. Metadata/hash generation is not content coverage. Prior same-hash canon excerpt reads are identified separately rather than relabelled as new full reads.

| Full primary | Bytes | Lines | SHA-256 | Full-read chunks |
|---|---:|---:|---|---|
| `AGENTS/HOMER/CLAUDE.md` | 38411 | 277 | `31bfe44995c363051e4597771113d486f653a5b125e550e0474e2b65c9b95399` | 1–90; 91–180; 181–230; 231–277 |
| `AGENTS/MIDAS/CLAUDE.md` | 26438 | 250 | `81e70c9bd59a7f0d3d17548bdc7266281e7282e2eb34cb6368b307ec1a1da97a` | 1–85; 86–170; 171–250 |
| `AGENTS/ORACLE/CLAUDE.md` | 26709 | 284 | `6436fad6aba47dca86517f9ca43281cb1379ccc8a0f9e3feee363a0445acfe02` | 1–100; 101–200; 201–284 |
| `AGENTS/OSPREY/CLAUDE.md` | 48339 | 286 | `c2325eebf1bf3f52c4cc9f178fb5138f5b2d39ca742f4685100eed09847e3c92` | 1–70; 71–155; 156–230; 231–286 |
| `AGENTS/OTTO/CLAUDE.md` | 42142 | 560 | `df7f2df6b5bafbfa743dbab15d99f95073aa6395ff2c555bc14e650256c7d048` | 1–140; 141–280; 281–420; 421–560 |
| `AGENTS/WAL/CLAUDE.md` | 24262 | 191 | `5c9748f67abb7e2764941dfbeeeca7dbf689d609e6a8f5c4c3c3e8b576bf10e4` | 1–100; 101–191 |
| `AGENTS/YURI/CLAUDE.md` | 14604 | 103 | `1998964fce79f478e3240e5a4493497a44394250df1b4c459e5a77a3c186e212` | 1–103 |

| Supporting source (all PARTIAL except stated) | Bytes / lines | SHA-256 | Read depth |
|---|---:|---|---|
| `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` | 25080 / 57 | `a326afd037cc5e037cd9673a011ad7c21bc5990156f9ae645af6f66576cf90a8` | Same-hash prior 25–57; rule20 used as exclusion; no full read. |
| `AGENTS/HOMER/tools/rent_breadth.py` | 5993 / 145 | `1a46df76c059d4b0073de51e9a2cb8207c9f829203282b58229c1e9c9a8d3509` | FULL1–145; supporting code, not a primary harness document. |
| `AGENTS/MIDAS/boot.py` | 14263 / 299 | `48920985697fb184ab080d0bf29f7b804010eaef0398272bd258e41e61ca5e9f` | 74–103;175–299; function/call inventory search only elsewhere. |
| `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` | 32141 / 290 | `8d8c279c4c56416e5fa34f77b088b6af96d7d34b8269c04c881423526e2f8955` | Fresh155–170; same-hash prior155–180 and201–228 retained; no full read. |
| `AGENTS/ORACLE/tools/disruption_supply_spread.py` | 18895 / 324 | `631ddc5a79ea5cf3dc76f233947f3aa400d06287ed48a9fe53d93193ca491146` | 1–52;144–324. |
| `AGENTS/OSPREY/scripts/strike_feed.py` | 15323 / 245 | `3498203d9d489a3ba25ed57ee8ef88b8fb205ea2ffb050972050c145351b0788` | 155–245; inventory search only elsewhere. |
| `AGENTS/OTTO/scripts/boot.py` | 8852 / 190 | `d10b23952065d79393654613cde3e5a492f1a7f92eda0070825cf3c3bce72209` | 42–77;80–190; inventory search only elsewhere. |
| `AGENTS/WAL/scripts/kb_expiry_check.py` | 5643 / 113 | `db82e414623c94d67ef13b606266fedf98f6ff2e2ea5b92637b577bf0e82d81e` | 55–113. |
| `AGENTS/WAL/scripts/predictions_due_check.py` | 5322 / 117 | `f777540d07d504bbf9d699a06fd7e59abc7b76ed199054ea2f975824cf8cf793` | 45–117. |
| `CLAUDE.md` | 24199 / 133 | `1b176d7b3c619a78dbabe4128f23451fa32a074554f391804707aec7623a3c73` | Fresh 70–79; same-hash prior 80–133 retained. Not a new full-root read. |
| `scripts/corrections_boot_check.py` | 25458 / 432 | `a60120317679154b97390c3e6519d2255e6a43f7753215b08e19c13c820c1110` | 45–95;414–432; unchanged hash from prior tranche. |

| Method reference (live read, not source-pin assertion) | Bytes / lines | SHA-256 | Read depth |
|---|---:|---|---|
| `sweeps/HARNESS_AUDIT_SWEEP.md` | 3381 / 19 | `0f157992d0de488b2933a1ca21c9e2ffa6b0f0c23d6b1743d1b2bb18743385af` | FULL1–19 |
| `HARNESS_AUDIT_2026-07-07.md` | 14096 / 73 | `c41b14421996c461ac3313438e76c1135d3fc7486928a19c6912123763f4612d` | FULL1–73 |

Explicitly not read for this portion: complete MIDAS cot_gold/metals_watch/one-shot graders, OTTO prediction/catalyst children, OSPREY config/load/diff/fetch helpers and acceptance dossier, ORACLE pull/metrics/coverage tools and watchlist data, WAL derived-drift internals, YURI intent ledger and first-firming record, current domain STATUS/THESIS/briefs, messaging canon/BOARD contract beyond prior inherited context, current runtime/settings/hooks, and linked incident/proposal/authority packets. Charter assertions about those sources were not upgraded to independently verified facts.
