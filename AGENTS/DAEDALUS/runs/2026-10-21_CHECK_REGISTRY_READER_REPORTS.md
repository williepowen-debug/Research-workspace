# CHECKS registry reader report — 2026-10-21

Synthesis pair: [2026-10-21_CHECK_REGISTRY.md](2026-10-21_CHECK_REGISTRY.md) (lead-owned).

Read-only helper audit; no CHECKS edits, hook installation, code edits, commits, pushes, or all-tools rerun. Parent synthesizes and owns registry changes. Scope is all 39 existing rows, current root runtime tools/hooks, and newly added local code since October 1. Inspected current source, invocation instructions, Git change history and metadata. This is source/invocation evidence, not a new behavioral test receipt.

## Findings and decision

The registry needs maintenance: several PASS descriptions overclaim, declared invocation sites have changed, and qualifying new checks are absent. Highest priority: position agreement does not establish external positions; session banner now mutates Git metadata/config; explicit read-cap mode grades charters; orch_log has installed L748 timestamp semantics. NEXUS brief_pin is already wired. Local read_cap is legacy. Corrections and pipeline-label gaps contain resolved claims. No automatic wiring or baseline replacement is authorized by this report.

All 39 Invoked_by, Null_meaning and Last_verified_run fields were read. Exact snapshots below preserve dated receipts; today inspection must not overwrite them with an invented run. A retained row means no material metadata contradiction established in this bounded audit, not independent proof every invocation ran.

## Row-by-row disposition

| # | Check | Disposition |
|---|---|---|
| 1 | `scripts/safe-push.sh` | UPDATE: Oct5 bootstrap installs/verifies native hooks before push (also dry-run); refusal is part of current contract. Historical run receipt is not current-source verification. |
| 2 | `scripts/orphan_check.sh` | RETAIN: advisory orphan candidates; global Git-status dependency still matters for candidate-v2 capture. |
| 3 | `scripts/consumer_check.py` | RETAIN with source-date review: Oct1 source change; matches superseded tokens, not semantic consumption or corrected downstream judgment. |
| 4 | `scripts/memory_index_check.py` | RETAIN: index presence/shape is not retrieval quality. |
| 5 | `scripts/ledger_staleness.py` | RETAIN: default/strict/write/abs-floor scans freshly exercised in Staleness report; stale flags are candidates requiring artifact disposition. |
| 6 | `scripts/claim_check.py` | UPDATE verification provenance: Oct5 syntax/runtime change; lexical enumerated claims only, not all correctness. |
| 7 | `scripts/firetime_check.py` | UPDATE: Oct5 artifact-cell parser accepts middle-dot/+ /semicolon and strips locators; gitignored missing paths informational. Parsed-window PASS is not proof every obligation was found. |
| 8 | `scripts/position_agreement_check.py` | UPDATE NULL: compares owner STATUS TRY-* LIVE tokens to trade surfaces. Does not establish broker/external position truth; no matching surface/token can be clean. |
| 9 | `scripts/env_doctor.py` | RETAIN: current-host diagnostics do not establish all runtime/tool permissions. |
| 10 | `scripts/session_banner.sh` | UPDATE NULL: Oct5 now installs Git hooks and may fetch --unshallow (120-second bound), otherwise fetch with 10-second bound; failure ancestry UNKNOWN. Harness wiring is Claude settings, not Codex evidence. |
| 11 | `scripts/check_memory_length.sh` | RETAIN: mechanical size cap only. |
| 12 | `scripts/lane_coverage_check.py` | RETAIN: declared-lane coverage, not evidence quality. |
| 13 | `scripts/gen_automemory_index.py` | RETAIN deliberate manual design; absence of automatic invocation is not defect. |
| 14 | `scripts/link_automemory.sh` | RETAIN setup-only; no invented recurring check. |
| 15 | `scripts/tsv_append.py` | RETAIN NOT-A-CHECK writer classification. |
| 16 | `scripts/market.py` | RETAIN NOT-A-CHECK data tooling classification. |
| 17 | `archive/SENTRY_pipeline/fetch_feeds.py (was scripts/fetch_feeds.py)` | RETAIN retired; no active invocation owed. |
| 18 | `scripts/canon_check.py` | UPDATE NULL/gap: checks enumerated forbidden forms only; known amend/no-pathspec canon omissions remain, no code fix in this audit. |
| 19 | `AGENTS/DAEDALUS/scripts/sweeps_due.py` | RETAIN existing row and owner boot wiring; grandfathered register presence is not precedent to add boot-wired new local checks. |
| 20 | `AGENTS/DAEDALUS/scripts/render_directory.py` | RETAIN generator/check scope; generated navigation agreement is not roster authority. |
| 21 | `AGENTS/DAEDALUS/scripts/falsification_scan.py` | RETAIN manual sweep invocation; candidate extraction is not resolved falsification judgment. |
| 22 | `AGENTS/DAEDALUS/scripts/maturity_scan.py` | RETAIN sweep invocation and maturity-candidate limits. |
| 23 | `AGENTS/DAEDALUS/scripts/complete_check.py` | RETAIN bounded closeout markers, not universal duty proof. |
| 24 | `AGENTS/DAEDALUS/scripts/regen_patterns_hot.py` | RETAIN generated hot-pattern check; source pattern quality not proven. |
| 25 | `AGENTS/DAEDALUS/scripts/verify_push.sh` | UPDATE INVOKED: legacy-only verification under current charter; candidate-v2 uses exact-commit verification. No every-closeout claim and no acceptance inference from subject/ancestry. |
| 26 | `scripts/memory_citation_census.py` | RETAIN WIRED-MANUAL census; prefix/declared-path counting is not actual memory consumption. |
| 27 | `AGENTS/DAEDALUS/scripts/read_cap_check.py` | UPDATE state/invoker/gap: legacy local checker no longer canonical closeout invoker; root read_cap_check is canonical and already covers the prior READS consumer gap. Preserve historical receipt. |
| 28 | `scripts/corrections_boot_check.py` | UPDATE gap/invocation: WALTER tools/closeout_check.py:113 calls --write-compliance; closeout_run.py:41 invokes that checker. Row says 59/59 tests while old gap says no self-tests/no independent read/uninvoked: remove obsolete assertions, preserve dated evidence and live resolver limits. |
| 29 | `AGENTS/DAEDALUS/scripts/profile_clock_check.py` | RETAIN existing boot-wired row (same grandfathering caveat as sweeps_due). |
| 30 | `scripts/docket_view.py` | UPDATE: current write target PROME/state/CALENDAR.md (CLOSEOUT lines51/63/74); Oct16 far rows retain L#/owner/severity beyond detailed 7-day window. Calendar digest is not semantic obligation completeness. |
| 31 | `scripts/orch_log.py` | UPDATE: L748 Oct21 installed after L736 receipt. orch_log check/validate_line grades schema v2, typed nonnegative counts, event class and basic field constraints, NOT structured closeout timestamps. append validates a time_correction_v1 row via orch_time.validate_correction; rotation separately guards correction/target closure. PROME/tools/orch_closeout.py validates lifecycle timestamps. No authentication, original append-time proof, or fleet liveness follows from orch_log check PASS. |
| 32 | `scripts/read_cap_check.py` | UPDATE NULL: explicit charter-loading grades root/local charter bytes; injected/unspecified modes differ. Remove unconditional charter-visible/ungraded statement. L530 implementation present; preserve actual prior test receipts. |
| 33 | `scripts/asmade_audit.py` | RETAIN manual-by-design audit perimeter. |
| 34 | `scripts/wiring_census.py` | RETAIN UNWIRED pending independent evidence; absence of owner boot is not silent permission to wire. |
| 35 | `scripts/validate_all.py` | UPDATE baseline/gap only with exact evidence: saved baseline remains Sep24 C2=1345,D1=2,recheckOct15; lead reports fresh C2=1750 and D1 cannot/AEOLUS unattested. Fresh observation is not installed baseline or D1 pass; no rebaseline here. |
| 36 | `scripts/pipeline_rc_guard.py` | UPDATE gap: settings statusMessage already Pipeline rc advisory (additionalContext; no approval); old blocking-label complaint is resolved. Harness-only/selected-pipeline limits remain. |
| 37 | `AGENTS/DAEDALUS/scripts/walter_route_check.py` | RETAIN MANUAL-BY-DESIGN router audit, not routing-consumption proof. |
| 38 | `scripts/brief_pin_check.py` | UPDATE state/invoker: NEXUS CLAUDE.md:51 executable reader boot instruction adopted Oct8; WIRED-SINGLE-INVOKER, not BUILT-UNWIRED. Pin checks pointer identity, not contents or reader comprehension; independent-reader gap not cleared by this wiring inspection. |
| 39 | `scripts/account_guard.py` | UPDATE verification provenance: Oct20 fixes after initial install. Actual pre-commit condition skips account guard if Python/script absent; narrow known-candidate detection, not whole-hook fail-closed. |

## New-row eligibility and invocation inventory

W2 excludes a newly considered local check already invoked by its owner boot. Existing sweeps_due/profile_clock rows remain unchanged rather than silently reconciling historical scope exceptions. Root setup tools and writers already have classified rows; the suggested additions use those existing categories and do not pretend installers are checks.

| Candidate | State / invocation | PASS limit |
|---|---|---|
| `scripts/orch_time.py` | WIRED; scripts/orch_log.py and PROME/tools/orch_closeout.py:21,58,132,178 | L748 append-only UNKNOWN time invalidation and attributed Git upper-bound audit. Not receipt authentication, original append-time proof, or fleet liveness. invalidate mutates and requires owner authorization. |
| `scripts/install-git-hooks.sh` | SETUP-ONLY; scripts/safe-push.sh; scripts/session_banner.sh | Verifies required executable native hooks and local hooksPath; refuses conflicting hook setups. Installer can mutate Git config, not a read-only checker. |
| `scripts/install-claude-hooks.py` | SETUP-ONLY; Explicit host setup; no recurrent invocation certified | Merges/backs up host settings atomically with locking; defaults write. Installation is not proof Claude hook execution, and not Codex wiring. |
| `scripts/githooks/pre-commit` | WIRED-HARNESS; Native Git; local core.hooksPath currently scripts/githooks | Conditional account guard plus staged docket line-stability and row-cap checks. Account dependency absence skips that leg; docket checks refuse missing dependencies. Not whole repo policy proof. |
| `scripts/githooks/commit-msg` | WIRED-HARNESS; Native Git; local core.hooksPath currently scripts/githooks | Normalizes subject via stripspace/NFC; first paragraph <=100 characters; missing Python refuses. Not correctness or complete Git protocol enforcement. |
| `scripts/githooks/pre-push` | WIRED-HARNESS; Native Git; local core.hooksPath currently scripts/githooks | Existing-remote ancestry check; deletion refused, UNKNOWN/non-FF refused, new-ref zero OID skipped. Does not detect every force flag or authorize publication. |
| `AGENTS/BROCK/scripts/brock_selfcheck.py` | WIRED-SINGLE-INVOKER; AGENTS/BROCK/CLAUDE.md:62 closeout | Three narrow checks: fire/resolution propagation in enumerated phrasings, STATUS matrix arithmetic, KB/VX 13-field shape. Not general claim or financial truth. |
| `AGENTS/DAEDALUS/scripts/calendar_docket_coverage.py` | MANUAL-BY-DESIGN; builds/calendar_coverage_2026-10-20/RESULT.md standalone command; boot integration not approved | Four discovery patterns, supported explicit point dates and lexical candidate correspondence; rc0 nonempty complete assessed population, rc1 unmatched, rc2 cannot dominates. No event identity/schedule/delivery proof. |
| `AGENTS/DAEDALUS/scripts/dark_window_check.py` | MANUAL-BY-DESIGN; No standing boot/sweep invoker located; owner to confirm intended cadence | Descriptive self-prefix commit gap against declared live tests; threshold enforcement opt-in under Will N. Commit activity is not current evidence/attention or liveness. |
| `AGENTS/DAEDALUS/scripts/prose_remedy_candidates.py` | WIRED-SINGLE-INVOKER; sweeps/PROSE_REMEDY_SWEEP.md:13 | Extracts candidate prose remedies; not acceptance, owner obligation, or completed repair. |
| `AGENTS/RED/scripts/closeout_check.py` | WIRED-SINGLE-INVOKER; AGENTS/RED/CLAUDE.md:74 W10 | Enumerated cross-surface checks and delegated checks; rc1/rc2 block. Selected surface consistency and executed children only, not whole session truth. |
| `AGENTS/VULCAN/tools/closeout_check.py` | WIRED-SINGLE-INVOKER; AGENTS/VULCAN/CLAUDE.md:38 closeout FIRST/LAST | Distinguishes CHECKED/DELEGATED/MANUAL; bounded checklist evidence is not whole judgment or independent validation. |
| `AGENTS/WALTER/tools/closeout_run.py` | WIRED-SINGLE-INVOKER; AGENTS/WALTER/CLAUDE.md:98 selected light/full closeout | Runs selected checks and drafts receipt; rc0/1/2 PASS/REVIEW/UNKNOWN grades selected checks only. No source edits/fetch/Git/scheduling/completion judgment. |
| `PROME/tools/docket_line_stability.py` | WIRED-HARNESS; scripts/githooks/pre-commit before row cap | Protects detectable unique unchanged row identities from movement; all moved-and-edited rows blind spot, sanctioned override explicit. Not full semantic identity or merge/rebase validation. |
| `PROME/tools/docket_row_cap.py` | WIRED; PROME/tools/prome_gate.py:1959 closeout; native pre-commit; post-save validator | Changed rows pair by physical line, ratchet existing oversize rows; staged policy from index. Missing policy => dormant rc0, not enforced cap. rc2 cannot is not PASS. |

New local exclusions: DAEDALUS docket_owed (CLAUDE47 / gate B5); RED basis_check (CLAUDE54 step9f); WAL maintenance_state_check (imported scripts/derived_drift_check.py:201, invoked owner boot CLAUDE58); YURI boot; PROME done_rows_check (prome_gate1876 boot and1953 closeout); PROME spawn_slate (prome_gate1896 boot and1934 closeout). These are boot-wired and outside W2 new-row eligibility.

Dependency/generator/research exclusions: root memory_index_paths; PROME argus_contract (argus_scope dependency), active_decisions_digest, gates_step3_pass, nisaba_pull and rotation_bundle (support workflows, not newly discovered standalone assurance claims); RED nonsession and board_log_append (support/writer); TERRY inbox_paths; CARL prepare_auto_outflow_extract; LIQUID usd_swapline; REGINALD kre_basket_study/settled_bars/wq318_funding_baseline; VULCAN crwv_library/kb_catalog; WAL earnings bridge/FFIEC tools; WALTER bookmark tools; retired LIQUID/archive scripts and PROME report/staged-digest code. These are not certified as complete semantic implementations; classification prevents inflating the registry with every new program.

Root fallback/session_start_sync.sh and fallback/stop_sync.sh were read: dormant fallback procedures, not active harness wiring. Their historical pull/autostash/broad memory staging behavior requires current-rule review before activation. No fallback executed. Native core.hooksPath on this workspace is scripts/githooks; that establishes local configuration only. Other hosts, Git bypass switches and Codex hooks were not attested.

RED status_mirrors.py is additionally eligible as a check-capable generator: CLAUDE65/74 wires --write, while documented --check is standalone/manual (rc0 two blocks equal fresh generation ignoring stamp; rc1 drift; rc2 markers/canon unavailable). closeout a/b separately inspect output; do not claim its --check is invoked there. Suggested JSON includes this sixteenth addition.

## Since-October-1 source-change coverage

Read change history and affected contracts: safe-push/session_banner/claim_check and native hook installers (Oct5); firetime artifact parsing (Oct5); consumer_check (Oct1); ledger/read_cap revisions (Oct2/3/5/20); corrections writer/resolver (Oct2/8/20); docket_view far-row rendering (Oct16); brief_pin (Oct8); account_guard install/fixes (Oct18/20); orch_log L736 (Oct20) and L748/orch_time (Oct21); docket line stability hook (Oct21). Current invocation edges inspected in root settings, native hooks, PROME gate/closeout, NEXUS boot, DAEDALUS charter/sweeps, and affected owner closeouts. Source dates newer than Last_verified_run require a separate dated inspection or new owner behavioral receipt, not silent relabeling.

The saved scripts/validate_all_baseline.json remains September24 (C2=1345,D1=2, recheck October15). Lead supplied fresh C2=1750 and D1 cannot with AEOLUS unattested; those are lead observations, not this reader reruns and not a replacement baseline. Preserve unresolved D1 and independently sourced receipts. Canon-check amend/no-pathspec omissions remain known code gaps outside this report.

Corrections resolver residual limits remain: YAML block-list/compound names/unclosed front matter, non-transitive chains and literal ALL handling; D7 remains unbuilt. Hook and account-guard conditional dependency behavior is described above. Merely finding a run site does not close independent-reader or production-test gaps.

## Completion and limits

This bounded registry reader leg is complete: every existing requested field has a captured disposition; root additions and new-local W2 decisions recorded. Parent must synthesize the reader report, decide proposed rows/wording, reconcile fresh run receipts, and update CHECKS/sweep logs if appropriate. No claim that registry maintenance or its full sweep clock is complete until those owner actions occur. No all-fleet historical local checker census, no exhaustive dynamic call graph, no proof of remote runtime hook installation, no new functional tests. Root scripts are DAEDALUS surface-owned with PROME integration; orch_time is DAEDALUS-built. PROME-local tools remain PROME-owned. Dark-window no-invoker result is bounded to inspected charter/sweep/search references; classify deliberate manual provisionally, obtain owner cadence confirmation before changing state to a defect.

## Exact existing-field snapshot

### scripts/safe-push.sh

**State:** WIRED

**Invoked_by:** Root CLAUDE.md closeout step 2 + 39 protocol docs

**Null_meaning (what a PASS proves — PAT-074):** Strong: rc 0 only beside the receipt `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch)`; rc 1 NOT confirmed, rc 2 CANNOT-CONFIRM, and every non-receipt line names `safe-push rc=N` separately from the `git push` subcommand's rc, so a killed run (rc 124) or a ref-update line is never a push certificate.

**Last_verified_run:** 2026-09-24 (wording-only edit: `bash -n` OK; non-comment diff = exactly 3 echo lines; 8 exit statements byte-identical; changed lines eval'd at push_rc=0/1; NOT run live — --dry-run fetches; runs/2026-09-24_SAFEPUSH_MARKET_BUILD.md)

**Gap:** The 2026-09-24 wording edit has not yet run end-to-end on a real push (build barred git fetch); there is no --help flag, the usage text is the header comment only.

### scripts/orphan_check.sh

**State:** WIRED

**Invoked_by:** Root CLAUDE.md closeout step 1b

**Null_meaning (what a PASS proves — PAT-074):** Weak-by-design: exit 0 ALWAYS, advisory. ⚠ Classifies by PATH not authorship, so everything under memory/auto/ reads [not yours] regardless of who wrote it — that label is NOT an authorship verdict (documented in root carve-out 3)

**Last_verified_run:** 2026-08-03 (3x)

**Gap:** none — the path-classification limit is documented at the point of use

### scripts/consumer_check.py

**State:** WIRED

**Invoked_by:** Root CLAUDE.md closeout step 1c + 5 protocol docs

**Null_meaning (what a PASS proves — PAT-074):** Partial: 'clean' proves no consumer carries the OLD token unqualified. It does NOT prove the NEW value reached anyone — absence of the stale figure is not presence of the current one ● 2026-08-28 (HENRY via PROME, A): signed needles were TEXT (NUM_RE had no sign) → exempt from every noise gate → '🔴 69 stale, send packets' with ZERO real; now numeric, and the bare floor is ≤4 sig digits ⇒ 🟠 (was ≤2). PASS/🔴 now proves: a context-certified hit, or a bare needle of ≥5 sig digits in ≤4 files. HENRY --from-ledger: 69 🔴 → 0 🔴 / 🟠 only. Known limit: a '%'-suffixed needle ('80%') is still a TEXT needle — pass --old 80 --unit %. ● 2026-08-28 LATE (BROCK via PROME, 2 findings, both fixed+§3-watched): (Q) read_ledger took raw[0] as header — a '#' banner above the header MANUFACTURED a phantom metric 'metric' (witnessed on old code); '#' lines now skipped anywhere. (P) certified-🔴 precision 0/2 — a FROZEN kill line (DOCKET 'CCC/BB ≤5.93 ×2 obs') and a DATED time-series row both read as stale copies; new LINE-CLASS demotion (threshold operator beside the value / '×N obs'|'consecutive'|'kill line' / .tsv row whose first cell is an ISO date) ⇒ 🟠 with reason, DEMOTE-never-suppress. PASS still proves only absence of the old token on LIVE, UNFROZEN, UNDATED lines. ● 2026-08-28 RAV review: tail-word demotion PROXIMITY-SCOPED (THRESH_WINDOW=40 chars of the hit; line-wide form removed escalation from a live value sharing a line with 'consecutive'); COMMITTED FIXTURES scripts/tests/test_consumer_check.py (9 cases incl. the far-tail false-negative shape and the positive control; negative-controlled by breaking the '#'-skip and watching the suite fail).

**Last_verified_run:** 2026-10-01 (DOCKET L457 + HAWK 9/28, n=2: ISO_DATE_RE was bound twice; the anchored L723 form shadowed the loose one, so the PROSE dead-banner branch of file_is_dead() could never clear. FIX: anchored constant renamed ISO_DATE_FULL_RE; DEAD_LINE1_RE tightened to root canon 'MARKER <ISO date>' + ~ excluded + DEAD_REVOKED_RE veto. Tests: scripts/tests/test_consumer_check.py 29/29, fail paths watched (pre-fix 24/29, v1 21/29); --selftest 10/10. Fleet: prose clears 0 -> 91 tracked .md, none live/pending (independent read #2, 15,506 files). Two independent Opus reads: #1 found v1 cleared a LIVE pending LABOR grading card -> v2; #2 PASS-WITH-RESIDUE. Residue R1-R4 (veto list incomplete; canon-shaped PENDING pre-registration would clear; future-dated/list-item banners) = synthetic only, owed as a new episode. Record runs/2026-10-01_L457_CONSUMER_CHECK_PROSE_BANNER_REPAIR.md) [prior cell rotated verbatim 2026-10-01 -> CHECKS_HISTORY.tsv]

**Gap:** CANON RETIREMENT TRIGGER FIRED 8/07: root 1c's interim 'a 🔴 is a CANDIDATE' line says it retires when unit-aware matching ships — it shipped. NEW GAP registered 8/12 (LABOR live instance via PROME): --from-ledger trusts PUBLISHED.tsv as truth and NOTHING valid … [rotated verbatim 2026-08-28 → CHECKS_HISTORY.tsv; the cell states current state only]

### scripts/memory_index_check.py

**State:** WIRED

**Invoked_by:** Root CLAUDE.md closeout step 1d

**Null_meaning (what a PASS proves — PAT-074):** Strong for the slug asked about. ⚠ TRAP: bare --strict gates the WHOLE index and will fail your closeout on ANOTHER agent's orphan, which carve-out 3 forbids you to fix — always --slug ● 2026-08-28: _CAPS_DEFAULTS MEMORY_WARN_PERCENT 80→75 to match harness_caps.env (a default disagreeing with the shared file was the seam itself).

**Last_verified_run:** 2026-08-14 (v3: cap constant now sourced from scripts/harness_caps.env shared with check_memory_length.sh — capable-case verified same-run BOTH readouts agree on the 25600-byte denominator; hook-length warn capable-case: LONG-hook slug 160-chars flagged, no-inline-hook slug silent-skips, unknown --slug prints neither-index warn; missing-caps fallback: py prints ⚠ MISSING with root-canon defaults, sh fails loud rc=2)

**Gap:** none — the trap is documented in root canon at the point of use

### scripts/ledger_staleness.py

**State:** WIRED

**Invoked_by:** 16 protocol docs (per-agent boot lines)

**Null_meaning (what a PASS proves — PAT-074):** Only the declared glob/trade perimeter and selected mode are checked; exclusions are printed. PASS proves vintage, never row completeness. Recent attention prints held without clearing the stale exit code. G1 long-line exemption applies only to the two new aliases immediately after a pipe; legacy keys retain the column cap. G2 only inspects the first eight lines. Declared-quiet and frozen cases retain their existing contract.

**Last_verified_run:** 2026-10-03: selftest 33/33; independent 9/9 tests; 323 declared-glob files compared before/final with zero attention-result changes; five real wrapper contracts (FERT/FLG/WATT/VULCAN/MIDAS) exercised. Fresh independent remedy/result read: runs/2026-10-03_WQ286_READER_REPORTS.md; synthesis runs/2026-10-03_CATCHUP.md.

**Gap:** Pre-existing: future attention dates can yield negative ages; data-clock prose inside eight-line header can contaminate the clock; clocks below that boundary are unseen; no row-completeness proof. Broader fleet sweep was not performed by this repair.

### scripts/claim_check.py

**State:** WIRED

**Invoked_by:** Root CLAUDE.md closeout step 1e (adopted 2026-08-04, canon bundle ③, Will-approved 8/3) + PROME/CLOSEOUT.md:178

**Null_meaning (what a PASS proves — PAT-074):** REPAIRED 8/03: handed a DIRECTORY it read the directory NAME as a file, failed silently, and printed 'clean 2 file(s)' — a whole-fleet pass claimed off zero bytes read. Now recurses; a clean run states the file count it actually read

**Last_verified_run:** 2026-09-03 (weekday ORDER-BLIND: PROME repro of 3 false-cleans [date-then-Sat · date-then-(Saturday) · month-name-then-(Sat)] fixed; --selftest SHIPPED, 29 cases = PROME's 6 + word-boundary/lowercase-month negatives + the 3 documented live regressions + month-name range pairs; fleet re-run 57 files = 0 NEW real flags — the 2 candidates [BRENT Wed–Thu Aug 12-13 · SAM Tue-Wed Sep 15-16] were the extension's OWN range-pair false positives, now guarded and in the set; commit 8fbf816fa) · 2026-08-11 (weekday two-day-range guard shipped [RED 8/7 ML-RED-143, his evaluate-against-range-end form adopted + lead-day-vs-start bonus check]: 8-case capable-case suite — Tue-Wed 9/15-16 passes, Tue-Thu 9/15-16 flags on range end, Wed-Thu flags on range start, no-end-date pair skips trailing half, plain wrong still flags, Satellite-Wed prefix guard holds; RED's live CATALYSTS.tsv:53 now ✓ clean. Prior: 2026-08-03 fleet-wide, 6197 files) || 2026-09-12 (DAEDALUS, TOOLING/WIRING sitting): FIXED: the English verb 'sat' was read as Saturday (DEWEY 9/10 via PROME) — 'on 7/31 sat 5 sessions off a 52wk HIGH' flagged at closeout step 1e, which runs fleet-wide. Scoped to the single lowercase token when NOT bounded as a weekday; 'Sat', '(sat)', 'sat,' and end-of-line all still flag, because the defect is a false POSITIVE and must not be fixed by loosening the check. selftest 29 -> 36 cases, 7 new IN BOTH DIRECTIONS; DEWEY's real file now rc 0.

**Gap:** CLOSED 2026-08-04 — canon step 1e landed the recommended scoped invocation (decision classes). Post-close correction absorbed: the DOCKET:10 flag graded FALSE-POSITIVE on the 'disagrees with itself' e … [rotated verbatim 2026-08-28 → CHECKS_HISTORY.tsv]

### scripts/firetime_check.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** PROME/BOOT.md (--window 7 --quiet)

**Null_meaning (what a PASS proves — PAT-074):** Unverified this session — window-scoped, so a clean run proves nothing about artifacts outside the 7d window

**Last_verified_run:** 2026-08-16 late-3 (--window-90 dead-pointer FP classes fixed — RAV-origin PROME packet, Will "Go on all four", 8-row fixture: class A title-case owner-notation skip [`PROME/Will` ×4] · class B URL-line guard tested only on already-unresolvable backticked token … [rotated verbatim 2026-08-28 → CHECKS_HISTORY.tsv; the cell states current state only]

**Gap:** Single invoker: if PROME does not boot, no fire-path artifact is checked. Off-repo local paths (career-launch class) flag by design — allowlist is their correct home. CANDIDATE (n=1, 8/16, do-not-build until n=2 per PAT-089): m_d tokenizer parses the tail of a slash-RANGE as a date (`~2026-09-10/11` → 'Oct-11' — PROME ASK-3 verification, fixed data-side); fix-form if promoted = digit-range prefix guard beside the existing UPPERCASE-ID guard

### scripts/position_agreement_check.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** PROME/BOOT.md (--all --quiet)

**Null_meaning (what a PASS proves — PAT-074):** Strong and positive: agreement with an external truth source, not freshness. Imports is_frozen from ledger_staleness, so the 7/31 SUPERSEDED token change altered its semantics too — re-run fleet-wide after that change: 38/38 agree, rc=0

**Last_verified_run:** 2026-07-31 (38/38, rc=0)

**Gap:** Single invoker. A SUPERSEDED banner on a live-capital trade surface SHOULD fail it — correct by design going forward

### scripts/env_doctor.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** PROME/BOOT.md

**Null_meaning (what a PASS proves — PAT-074):** Strong: rc=1 means fix-or-flag before citing the affected data source

**Last_verified_run:** 2026-10-01 (PR#7): CLEAN on DESKTOP-BC6EF81, rc 0, clean case WATCHED; perimeter now 8 .env keys — PROME added AGSI_API_KEY 9/19 (d87c26f3b): catches the ABSENT key only — a REJECTED AGSI key returns HTTP 200 + empty data, shape-identical to an unpublished gas day; the rejected case is HANS's point-of-use re-probe (re-verify 2026-12-19). Fire case NOT re-watched this pass. [prior cell → CHECKS_HISTORY.tsv 2026-10-01]

**Gap:** 🟠 SCOPING CALL RULED 8/7 (PROME-routed 8/4, SAM's PyYAML outage — 'CLEAN' printed on a box where DM v1 could not run): DECISION = a health check must STATE ITS OWN PERIMETER in its output ('checked: market-data deps, 4 keys · NOT checked: messaging, agent-loca … [rotated verbatim 2026-08-28 → CHECKS_HISTORY.tsv; the cell states current state only]

### scripts/session_banner.sh

**State:** WIRED-HARNESS

**Invoked_by:** `.claude/settings.json` SessionStart hook — the harness, not a protocol doc

**Null_meaning (what a PASS proves — PAT-074):** Strong for what it claims: it reports, it does not act. Its silence would be visible (no banner at boot)

**Last_verified_run:** 2026-08-03 (fires every session) || 2026-09-12 (DAEDALUS, TOOLING/WIRING sitting): FIXED (DOCKET L294 origin-proof sweep): the dirty-tree leg lost `git status`'s exit code to a pipe, so a FAILED git status yielded DIRTY=0 and the SessionStart hook of EVERY session printed the all-clear 'tree clean' over a dirty tree. rc now captured off the pipe; a failed status prints '[git status FAILED - dirty-tree state UNVERIFIED; do NOT trust tree clean]'. Drilled both directions with a PATH shim. NOTE THE ASYMMETRY: the ORIGIN legs of the same script were already correct (FETCH_RC captured, '? ?' sentinel) - only the leg whose rc travelled through a pipe was wrong.

**Gap:** none — but note this is the ONLY check invoked by the harness rather than by a document, so it is the only one that cannot be skipped by an agent forgetting a step

### scripts/check_memory_length.sh

**State:** WIRED

**Invoked_by:** Root CLAUDE.md closeout step 1d (conditional rider — adopted 2026-08-04, canon bundle ①)

**Null_meaning (what a PASS proves — PAT-074):** REPAIRED 8/03: there was a soft (WARNING) tier for LINES and NONE for BYTES, so the warn tier could not fire on this file's actual growth mode. Measured today: 74% of the BYTE cap vs 12% of the line c … [rotated verbatim 2026-08-28 → CHECKS_HISTORY.tsv]

**Last_verified_run:** 2026-08-14 (constants now sourced from scripts/harness_caps.env via `source`, so this guard and memory_index_check.py can never disagree on the denominator; capable-case verified — MEMORY.md read 61% here + 62% there, rounding-only difference on same source; missing-caps-file capable-case: FAIL LOUD rc=2 as designed) — prior 2026-08-03 verified run: 74% bytes / 11% lines rc=0

**Gap:** CLOSED 2026-08-14 (DEWEY 8/12 flag closed at the ROOT): the same-file-two-readouts defect (this guard 25600 vs memory_index_check.py 24400) is fixed one layer up — both guards read one file (scripts/harness_caps.env), so if the harness cap moves, both move together. PAT-069 fix-shape. Residual is the HEADROOM not the wiring; hook-trim + flow-rule demotion pass already recorded in MEMORY.md header

### scripts/lane_coverage_check.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** sweeps/PRODUCTION_REVIEW.md step 3b (WIRED 2026-08-03 by DAEDALUS — own playbook, no gate); cadence 14d

**Null_meaning (what a PASS proves — PAT-074):** Honest by construction: INFO severity, explicitly 'a coverage FACT to surface, not an alarm'. Reads ROSTER at runtime, so it does NOT rot as the roster changes — verified today at 30 ACTIVE / 6 synthesis-excluded

**Last_verified_run:** 2026-08-07 (rc=1 by findings-count design, 20 covered, 4 INFO — SAME set as 8/3: MARCO/ORACLE/OZK/WAL; already routed 8/3-8/4, WALTER packet sent on OZK/WAL lanes, no new spinouts this period) ● 2026-09-01 PR#5: 20 ✅ · 7 INFO no-lane (CRUISE FERT FLG MARCO ORACLE OZK WAL) — MARCO newly listed vs the 8/3 note (OZK/WAL); relayed to PROME/WALTER in the PR#5 rollup.

**Gap:** 🟡 CLOSED 2026-08-03 — wired into the Production Review (review cadence is correct for an INFO roster-derived check; a boot step would be noise). Was UNWIRED 7/16-8/03, 18 days, during which its 4 INFO findings sat unread — MARCO, ORACLE, and both single-name bank specialists OZK and WAL have no autonomous lane, so intake reaches them only via Will's channel and their own pulls. Routed to PROME 8/03

### scripts/gen_automemory_index.py

**State:** MANUAL-BY-DESIGN

**Invoked_by:** On demand only

**Null_meaning (what a PASS proves — PAT-074):** n/a

**Last_verified_run:** not run

**Gap:** NONE — correctly un-invoked. Its own docstring: 'MANUAL REPAIR TOOL — NOT part of the normal flow', because auto-regeneration would strip Claude's curated index entries every commit

### scripts/link_automemory.sh

**State:** SETUP-ONLY

**Invoked_by:** Machine provisioning, --apply gated

**Null_meaning (what a PASS proves — PAT-074):** n/a — safe by default: prints a plan and changes nothing without --apply; backs up and never overwrites a differing memory file

**Last_verified_run:** not run (per-machine, already applied)

**Gap:** none

### scripts/tsv_append.py

**State:** NOT-A-CHECK

**Invoked_by:** LABOR/CLAUDE.md and other per-agent ledger write steps

**Null_meaning (what a PASS proves — PAT-074):** n/a

**Last_verified_run:** not run

**Gap:** none

### scripts/market.py

**State:** NOT-A-CHECK

**Invoked_by:** 4 protocol docs

**Null_meaning (what a PASS proves — PAT-074):** n/a as a gate; a row with no ⚠ tag means the live regularMarketPrice was present and its regularMarketTime (America/New_York) is today — ⚠prev-close / ⚠stale <date> / ⚠no-asof / ⚠asof-unreadable mark every other row, and --selftest rc 0 proves fmt() only, never the feed.

**Last_verified_run:** 2026-09-24 (--selftest 14/14 PASS rc 0, re-run this pass 14/14; pre-fix fmt() swapped in = 4/14 rc 1; live smoke 16:50 EDT `quote WAL OZK CL=F ^TNX` rc 0, watchlist 40 lines 0 ⚠; runs/2026-09-24_SAFEPUSH_MARKET_BUILD.md)

**Gap:** Weekend/holiday rows all carry ⚠stale (accurate — consumers WAL·OZK·REGINALD·POSITIONS must expect it); a prev-close row carries no as-of date; a genuine 0.00 print reads as absent; the no-yfinance error says 'no repo .venv found' even when the venv exists.

### archive/SENTRY_pipeline/fetch_feeds.py (was scripts/fetch_feeds.py)

**State:** RETIRED

**Invoked_by:** none — SENTRY feed pipeline RETIRED 2026-08-29 (WQ-127, Will); .github/workflows/feeds.yml removed; successor lane = RESEARCH-INTAKE

**Null_meaning (what a PASS proves — PAT-074):** n/a

**Last_verified_run:** not run

**Gap:** none

### scripts/canon_check.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** sweeps/PRODUCTION_REVIEW.md step 3b (cadence 14d). Per-session-closeout upgrade (bundle ④) DECLINED-FOR-NOW 2026-08-04 — own small-bundle argument won; Production-Review cadence stands

**Null_meaning (what a PASS proves — PAT-074):** Says what it searched and what it deliberately skipped, every run: N docs searched, N prohibitions, plus the count of historical/mail hits NOT listed. A clean run means 'no LIVE instruction surface prescribes a forbidden command' — it does NOT mean the canon table is complete (see Gap)

**Last_verified_run:** 2026-08-07 (2515 docs, 4 live flags — the 2 TRUE-POSITIVE incident-memory hits STILL LIVE: the RAV-QC-002 memory fix routed to PROME→WALTER 8/03 has NOT been applied; other 2 = quote-class, need same-line negation wording, author-lane) ● 2026-09-01 PR#5: 2 hits, both memory/auto/ finding files that QUOTE the forbidden recipe to explain a defect (finding_governance_doc_stale_default_drift:11, finding_pathspec_wildcard…:28) — the "forbids it elsewhere in itself" suppression misses a finding file whose whole body is the prohibition's rationale; candidate: exempt memory/auto/finding_* or require the in-line negation there (PROME/owner files, not mine to edit).

**Gap:** ⚠️ The PROHIBITIONS table RESTATES prose canon, because root CLAUDE.md states its git rules in prose and there is no machine-readable source to read instead — so IF CANON ADDS A PROHIBITION THIS TABLE … [rotated verbatim 2026-08-28 → CHECKS_HISTORY.tsv]

### AGENTS/DAEDALUS/scripts/sweeps_due.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** DAEDALUS CLAUDE.md SPAWN step 5 (every boot)

**Null_meaning (what a PASS proves — PAT-074):** rc0 = registry read whole, N tracked + skipped count printed, nothing due, self-row <5d ⚠️⚠️ **AND NOTHING MORE — BOUNDARY MEASURED LIVE 2026-08-23 (PAT-129): a PASS proves nothing in THE REGISTRY is due, NEVER that nothing is OWED.** The clean line states its … [rotated verbatim 2026-08-28 → CHECKS_HISTORY.tsv; the cell states current state only]

**Last_verified_run:** 2026-08-17 (rewrite: §9 rc 0/1/2 + all-stdout + SELF-ROW line; 4 capable cases watched incl. LIVE self-row fire) ● 2026-09-01: DUE ×2 at boot (PR +1d, Staleness +0d), both run; profile_clock_check WIRED as a child (rc 1 on fired clocks, rc 2 on cannot-run) — watched printing 10 fired clocks live.

**Gap:** —

### AGENTS/DAEDALUS/scripts/render_directory.py

**State:** WIRED

**Invoked_by:** SPAWN step 7 on any FLEET_MAP row change + Production Review step 5

**Null_meaning (what a PASS proves — PAT-074):** rc0 = structural directory guards pass; WF may still be UNKNOWN. --check runs guards and renders in memory without writing. External lane currency is NOT watched by the existing directory-age guard.

**Last_verified_run:** 2026-10-03:10 WF tests +8 independent adverse-source probes;43 original seven-cell rows conserved;live24keys/249entries;--check bytes+mtime stable;reader runs/2026-10-03_WF_READER_REPORTS.md.

**Gap:** External WATCH_FOR is render-time snapshot only; regenerate after lane edits. Unsupported computed config is UNKNOWN. Existing unknown argv behavior unchanged.

### AGENTS/DAEDALUS/scripts/falsification_scan.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** sweeps/FALSIFICATION_SWEEP.md step (21d cadence)

**Null_meaning (what a PASS proves — PAT-074):** rc0 = all surfaces scanned, perimeter (4 NOT-looked-at classes) printed in BOTH modes, zero flags ⚠️ 2026-10-08 (Falsification #4): a PASS does NOT cover ledgers registered in `scorecards/LEDGERS.tsv` (YURI) or the blueprint's own `Kill rail re-derived: YYYY-MM-DD` stamp (5 desks print 'no surface' while complying), patch versions (v1.0.2 read as v1.0), or owner-set cadences.

**Last_verified_run:** 2026-08-17 (--tsv perimeter + §9 rc + --agent validation; live rc1 over 4 real flags that previously exited 0)

**Gap:** — · 2026-10-08: scanner gaps F-A..F-E + LEDGERS.tsv + the unbuilt per-leg CANNOT-FIRE render — owed DAEDALUS build (runs/2026-10-08_FALSIFICATION_SWEEP_04.md).

### AGENTS/DAEDALUS/scripts/maturity_scan.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** Production Review §1 Detect (wired 2026-08-17 — was INVOKED-BY-NOTHING, self-audit F10)

**Null_meaning (what a PASS proves — PAT-074):** rc0 = graded from real git data (git-fail now dies CANNOT-CERTIFY, no silent all-L2 collapse); JUDGMENT_ONLY announced in both modes ⚠️ SCOPE-VS-LABEL DEFECT MEASURED 2026-08-20 (FLG build), REGISTERED NOT FIXED: the `session_counts` signal greps the WHOLE dis … [rotated verbatim 2026-08-28 → CHECKS_HISTORY.tsv; the cell states current state only]

**Last_verified_run:** 2026-08-17 (sh()/REPO/epoch guards; git-fail watched via stub-git -> clean CANNOT-CERTIFY rc1; live rc0) ● 2026-09-01 PR#5: 37 graded + RAV NOT GRADED with reason; floor L2 everywhere except DEWEY L0 (no STATUS by design) / YEYOU L1; the "no BOTTOM LINE" hints on BRENT/SAM/MARCO were read-checked (MARCO TRUE, BRENT/SAM local form).

**Gap:** —

### AGENTS/DAEDALUS/scripts/complete_check.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** DAEDALUS CLAUDE.md SPAWN step 9 closeout battery (every closeout)

**Null_meaning (what a PASS proves — PAT-074):** rc0 = all standards commits in range paired, all companions paired-or-pointered, claim list printed w/ full count (display capped, cap stated); leg (i) never gates rc — it enumerates, the closer verifies

**Last_verified_run:** 2026-08-20 (diff-scope fix; capable cases: --since 8/19 printed 2 claims incl. the delivered PROME/inbox packet the 8/19 filter dropped, 483→2 drain measured, inbox-mv range produced 0 false attributions; clean case today 0/0 rc0; bad --since rc2. Prior: 2026-08-17 build — REAL violation 1c0ad78b4 caught + injected bad companion flagged + 3 pointer-pairs pass)

**Gap:** —

### AGENTS/DAEDALUS/scripts/regen_patterns_hot.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** DAEDALUS CLAUDE.md SPAWN step 9 (whenever PATTERNS.tsv changed) + PATTERNS.tsv header canon comment

**Null_meaning (what a PASS proves — PAT-074):** rc0 = hot+cold equals all source rows; not a semantic review or proof of automatic age-trigger invocation

**Last_verified_run:** 2026-10-20: 42 hot +146 cold =188 source rows; nine expired hot entries moved by regeneration; source unchanged.

**Gap:** Age-only drift requires an explicit rerun; source-change boot trigger alone is insufficient.

### AGENTS/DAEDALUS/scripts/verify_push.sh

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** DAEDALUS CLAUDE.md closeout battery step 9 (every closeout, after safe-push)

**Null_meaning (what a PASS proves — PAT-074):** rc0 = a commit with this SUBJECT exists on origin/master AND the ref was read successfully. ⚠️ NOT proof the session shipped — a gitignored deliverable is invisible to it (Job 5 rule 3, the VIRGIL case)

**Last_verified_run:** 2026-08-19 (built; all 3 rc paths watched on capable cases — rc0 real commit, rc1 absent subject, rc2 unreadable ref)

**Gap:** none open

### scripts/memory_citation_census.py

**State:** WIRED-MANUAL

**Invoked_by:** PROME flow passes (MEMORY.md >=75% demotion rule) + DAEDALUS Production Review question 4 (canon-graduation candidates). NOT boot-wired, by design

**Null_meaning (what a PASS proves — PAT-074):** rc0 = both index tiers parsed to non-zero slug sets, window scanned >0 commits, printed queues reflect that scan. NOT proof any memory is valuable/dead (advisory; overrides expected) and CANNOT see the agent who never knew a slug existed — a zero-citation row is 'uncited in window', never 'useless'

**Last_verified_run:** 2026-08-21 (built; all paths watched on real rc: capable 44-demote/42-promote live run reproducing baseline 487-vs-515 cites, clean-case fixture both empty lines, HELD-HOT fixture own-section-not-queued, rc2 zero-slug fixture. First build used DIFF scanning an … [rotated verbatim 2026-08-28 → CHECKS_HISTORY.tsv; the cell states current state only] ● 2026-09-01 PR#5 3c: 40+ PROMOTE-CANDIDATE rows above threshold (head 40 capped; population > list), many `[embedded →]` = duplication evidence for EMBED-THEN-DEMOTE; relayed to PROME flow pass, not actioned here.

**Gap:** QUEUED INCREMENT (PROME 8/21 eve, wave-3 staging; 8/28 register item): HOOK-INTEGRITY assertion — every ·-separated segment in the hot index leads with a slug; slug CONSERVATION is proven every pass, hook integrity never is, and the 8/20 flow-pass-#2 demotion split ragged_row's hook (tail stranded slug-less in the hot line, head truncated mid-paren in the cold row; repaired 941bb346c). §4's silent-truncation class inside the memory index itself

### AGENTS/DAEDALUS/scripts/read_cap_check.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** DAEDALUS CLAUDE.md closeout battery §9 (every closeout)

**Null_meaning (what a PASS proves — PAT-074):** rc0 = THE NAMED FILES are under 60% of the 25,000-token read cap at a MEASURED 2.17 B/token. ⚠️ Does NOT prove: (a) the 25,000 cap is still current — it is OBSERVED from a live truncation, nothing re-derives it; (b) the byte/token ratio holds for this file's c … [rotated verbatim 2026-08-28 → CHECKS_HISTORY.tsv; the cell states current state only]

**Last_verified_run:** 2026-08-23 (built; all THREE rc paths watched on real cases: rc1 on live STATUS+FLEET_MAP, rc0 on REGISTRY.tsv, rc2 on a missing path)

**Gap:** PROME 8/31 ×2 (verified at artifact by PROME): the heuristic perimeter sees 1 of 6 PROME boot reads (BOOT.md pointer, not inline) and is blind BY CONSTRUCTION to a cross-agent mandated read (WALTER 6b → RED FALSIFICATION_TRIGGERS 45,248 B = 139%, in nobody's perimeter). Its PASS line says "this check found" and is quoted as coverage. Fix = consume PROME/registry/READS.tsv (built 8/31) — R7-stage-2 consumer half, mine, ~9/14; every verdict travels with its perimeter until then.

### scripts/corrections_boot_check.py

**State:** WIRED

**Invoked_by:** Boot leg WIRED 38/38 active+tier-2 (--coverage 2026-10-08); DAEDALUS SPAWN step 5b. --write-compliance: NOT YET INVOKED — proposed to WALTER closeout 2026-10-08 (packet AGENTS/WALTER/inbox/2026-10-08_from-DAEDALUS_WQ-393-R1-row-format-spec.md); WALTER picks the site

**Null_meaning (what a PASS proves — PAT-074):** rc 0 means no NAMED correction for this desk lacks a recipient receipt, including RETIRED and DEAD-AT-CAP rows; expiry alone cannot discharge a named target. ALL broadcast expiry remains separate. Receipt existence does not prove the action was correct or applied. Unknown desk or malformed required inputs produce rc 2. --write-compliance rc 0 means every correction-class SIG-W file dated >= --since has its id in a register pointer (or a 'not correction-class' dispatch_note) and every row whose pointer names its original as -to-… targets that original's action+info; it proves nothing about corrections never published to BOARD, originals named another way (counted 'not checkable'), or row content. Zero signals in window = rc 2.

**Last_verified_run:** 2026-10-20 --write-compliance resolver (WALTER 10/16 finding adopted): explicit frontmatter `corrects:` ids first, unambiguous filename forms only, corrected ∪ correcting recipients, BAD-POINTER (rc 1) for an explicit pointer not on BOARD or malformed, `EXTERNAL:` = not checkable; selftest 59/59 (R1a–R1h); live BOARD: old 2 false SHORT-TARGETS → new 0, checked 15→18, none lost (independent Opus read PARTIAL, its ❌ CE1 fixed after the read — UNREVIEWED). Prior: 2026-10-08 (8bf9a3625): selftest 38/38 (17 WQ-399 legs W1–W15 incl. file-unchanged assertions); capable case watched (HEAD writer accepts APPLIED w/o fields rc 0, new refuses rc 2, no file); live DAEDALUS rc 0, coverage 38/38. Independent read ❌1 (CR in a field broke the boot check) fixed at 112ccb908; delta read ACCEPT-WITH-RESIDUE ❌0 ⚠️10; selftest 51/51. Earlier today: --write-compliance watched (b7ec4568a).

**Gap:** Resolver residue (read 10/20): YAML block-list `corrects:` unparsed; `-to-014-and-20261014-018` resolves to 014 only; unclosed frontmatter reads body lines; correction-of-a-correction not transitive; correcting `info: [ALL]` demands literal ALL target. D7 semantic closure tooling remains unbuilt; receipt existence cannot certify application. Cosmetic retired-cap counts and WALTER-owned register/spec wording remain outside this bounded certification. Broad coverage/wiring census not rerun today. --write-compliance has no --selftest cases (verified by watched run only) and no independent read; uninvoked until WALTER wires it. WQ-399 writer guard: residue declared (AC Amendment 3: note tokens after position 1, non-ASCII review digits, W15b test gap), carried into the D7 build; existing 108 receipts not backfilled (ruled ③) — D7 will count them PRE-WORD.

### AGENTS/DAEDALUS/scripts/profile_clock_check.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** sweeps_due.py child at every DAEDALUS boot (SPAWN step 5) — no charter edit (CLAUDE.md at 99.7% of budget)

**Null_meaning (what a PASS proves — PAT-074):** rc0 = evaluated calendar clocks inside declared windows only; content/event/STATUS-relative predicates and truth of refresh work NOT certified. Population and excluded companions named. rc1 = overdue calendar clock; rc2 = unreadable/ambiguous/future metadata or unsupported owner-relative comparison; known alerts still print.

**Last_verified_run:** 2026-09-08 repair: 12/12 tests, six frozen real profiles with source hashes. Real FERT rc0; BROCK rc1 (72>45); OSPREY rc2 (body8/7, owner-relative). Fleet before/after: runs/2026-09-08_PROFILE_CLOCK_{BEFORE,AFTER}.json. sweeps_due rc2 propagation watched retaining six alerts.

**Gap:** HENRY/HOMER/OSPREY require owner STATUS-stamp comparison (rc2, no false wall-clock pass). No assertion that content triggers or declared full-refresh work are verified. Six overdue body reviews remain.

### scripts/docket_view.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** PROME/CLOSEOUT.md:71 (`docket_view.py --write PROME/SCRATCH.md`, generated-block step) · scripts/validate_all.py leg A2 (--selftest)

**Null_meaning (what a PASS proves — PAT-074):** --write PASS = the SCRATCH block is byte-derived from DOCKET at that as-of (crc32 in the stamp) and the ᶜ tag fires only on a whole-word case-sensitive COVERED not preceded by `not `; --check clean = every MATCHED dated claim is covered by a row; neither proves DOCKET's own correctness.

**Last_verified_run:** 2026-09-24 (--selftest 26/26 rc 0, re-run this pass 26/26; old-tag mutant rc 1 on 2 drills; live OVERDUE line 9 ᶜ → 4, all 4 lead `PENDING · COVERED`; runs/2026-09-24_PARSER_FIXES_BUILD.md)

**Gap:** ᵒ (OVERDUE) tag still uses the substring test; the negation guard covers only `not `/`Not `/`NOT ` immediately before the token ('no longer COVERED' would still tag); the quoted prior-state form (L140/L198) would tag if those rows became dated.

### scripts/orch_log.py

**State:** WIRED-SINGLE-INVOKER (PROME closeout; the scorecard is a consumer)

**Invoked_by:** PROME closeout append (`python3 scripts/orch_log.py append --date … --desk … …`, the canonical path per the 9/3 reply) · coordination_scorecard.py imports it as the single owner of COLS and fails closed on its verdict · --selftest 6 drills

**Null_meaning (what a PASS proves — PAT-074):** `check` PASS = every data row is exactly 13 columns and every typed cell is int-or-EMPTY; proves nothing about the VALUES (a wrong integer passes) and nothing about rows PROME never wrote

**Last_verified_run:** 2026-10-20 L736 follow-through:36 existing selftests+7 view tests pass. Independent l736_review verified prior R1/R2/R5/R8 and final public-view refusal/recovery/CLI/concurrency races; SHA e84f5601735ab85a97931d4c2b57f1f62e7d2b81ef9119f1f0ae5d87f1429aac. runs/2026-10-20_L736_FOLLOWTHROUGH.md and reader companion.

**Gap:** Count-only: net-zero hand edits, missing-view baseline and rotate/internal write_view remain provenance limits. Source-path comparison and procedure/test updates belong PROME. Public view no longer absorbs a count rise; legitimate append exact acknowledgment persists evidence. Pre-existing rotate comment-after-header rc1 remains.

### scripts/read_cap_check.py

**State:** WIRED

**Invoked_by:** DAEDALUS closeout battery (CLAUDE.md step 9) · every desk's R1 boot line (36 desks on Will's word) · PROME closeout · sweep #2

**Null_meaning (what a PASS proves — PAT-074):** An attested reader is graded on its own declared whole/programmatic reads; declaration replaces charter heuristic. Class members measured individually; empty classes use history discrimination, not an unconditional defect. An undeclared reader is clean only within discovered heuristic scope. Charter itself is visible/ungraded. Exact external-root concrete/glob rows are visible/ungraded, but invalid mode or parent traversal remains a defect. Consumers use READ-CAP-RESULT, not prose totals.

**Last_verified_run:** 2026-10-20 owner installation receipt: L530 applied b0db526d7; PROME reports 127 selftests. Current cleanup inspected scope/receipt, did not rerun the fleet suite.

**Gap:** L530 installed; READ_CAP rule15 owner-field wording remains separate. CREED complex prose remains heuristic-limited, with affected paths already covered by its attested manifest; HANS outside-boot thresholds require declaration; arbitrary prose and undeclared harness completeness are not certified.

### scripts/asmade_audit.py

**State:** MANUAL-BY-DESIGN

**Invoked_by:** One-time fleet sweep 2026-09-07 (harvest H2; sweeps/REGISTRY.tsv row) + per-desk on demand; candidate for validate_all v1

**Null_meaning (what a PASS proves — PAT-074):** rc0 = every row with a Confidence cell matched the first bare-percentage cell after its ID in the earliest STATUS blob carrying that ID. Does NOT prove the registration predates the ID (limit 2) or that a prose-registered row was read correctly (limit 1); NOT-FOUND rows are unexamined, not clean

**Last_verified_run:** 2026-09-07 (positive control: LABOR ledger @1d17dacfa^ → 9 MISMATCH incl. every row LABOR's own audit found; live LABOR → 6 candidates incl. LAB-03/10/11 real, LAB-02/05/07 limit-2 artifacts; --all-seeded rc1)

**Gap:** Reverse-walk by prediction TEXT for pre-ID rows not implemented; HENRY has no Confidence column (NO-CONF 40)

### scripts/wiring_census.py

**State:** UNWIRED

**Invoked_by:** None yet — fleet run 2026-09-07 filed as runs/2026-09-07_H1_WIRING_CENSUS_fleet.md; target = validate_all v1 (9/10)

**Null_meaning (what a PASS proves — PAT-074):** rc0 = no forward-leg flag and no alias hit on a trigger-shaped STATUS line. Does NOT prove a bar still MENTIONED in STATUS as retired is unwired (presence ≠ wiring — stated in the tool); reverse leg over-fires on prose

**Last_verified_run:** 2026-09-07 (positive control on LABOR @f2558c075^: EMRATIO NOT-FETCHED + TEMPHELPS + 1,900,000 all real; --all rc2, 28 desks, 5 CANNOT-VERIFY; reverse leg judged TOO NOISY to packet)

**Gap:** Reverse leg must be scoped to threshold-table rows before it names a desk; alias table is hand-maintained

### scripts/validate_all.py

**State:** BUILT-UNWIRED

**Invoked_by:** UNWIRED at delivery by design - wiring it into a boot/closeout step is PROME's/Will's call (ASK in the 2026-09-10 delivery memo). Run on demand at any tooling sitting; the intended standing reader is PROME at closeout when a decision ledger was touched

**Null_meaning (what a PASS proves — PAT-074):** rc 0 = the registered instruments pass their OWN selftests AND the three decision ledgers are well-TYPED AND C2/D1 sit at or below the baseline swept 2026-09-24 (C2 1345, D1 2); it proves nothing about whether a finding was ACTED ON, mail read, or external truth, and it is not the retired per-push review seat — rc 2 = a leg could not run.

**Last_verified_run:** 2026-09-24 (--selftest 42/42 rc 0, re-run this pass 42/42; old-parser mutant 40/42 rc 1; live B3 false FINDINGS → PASS; C2 no-col KBs 20 → 9, supervised desks 11 → 22 of 31; baseline re-swept via --rebaseline; runs/2026-09-24_PARSER_FIXES_BUILD.md)

**Gap:** Nothing reads the baseline's recheck_by (2026-10-15) — an inert field until a leg or sweeps_due line alerts on it; C2 counts FROZEN-bannered KBs (BRENT 99 + HOMER 36 of the +688); OTTO KB (uppercase STALE_BY + uncommented banner) stays unsupervised; D1's FINDINGS text does not name 'class row matched 0 files'.

### scripts/pipeline_rc_guard.py

**State:** WIRED-HARNESS

**Invoked_by:** PreToolUse hook via PROME/tools/hooks/pipeline_rc_block.py (.claude/settings.json:31), which imports diagnose(); also `--explain <cmd>` / `--selftest`

**Null_meaning (what a PASS proves — PAT-074):** A WARNING, never a verdict: silence proves only that no NAMED gate in COMMAND position sits left of a status-swallowing pipe (`|`, `|&`) or a two-valued rc idiom without a real PIPESTATUS/pipefail use; the gate list is a curated allowlist, and the hook is ADVISORY since WQ-263 (exit 0 on a hit).

**Last_verified_run:** 2026-09-24 (v4 --selftest 85/85 rc 0, re-run this pass 85/85; v3 diagnose swapped in = 67/85; committed corpus 1,121 lines: v3 6 hits → v4 1, the 1 a true positive; runs/2026-09-24_PIPELINE_RC_GUARD_V4_BUILD.md)

**Gap:** PROME's wrapper --selftest reads 34/36 rc 1 (re-run this pass) — both failures are wrapper drills pinned to v3 behaviour (r5 ❌10 want→2; the suppressed-raw-hit drill needs a new input), PROME's to fix; not covered: `if gate | tail; then`, `gate && ok || FAILED`, process substitution, `sudo -u <user>`, a later command's $?; v4 has no independent read.

### AGENTS/DAEDALUS/scripts/walter_route_check.py

**State:** MANUAL-BY-DESIGN

**Invoked_by:** On demand at the Wiring Sweep route-census leg (sweeps/WIRING_SWEEP.md run sections 2026-08-28 / 09-04 / 09-17); no boot or closeout step names it

**Null_meaning (what a PASS proves — PAT-074):** A clean census proves only that no desk canon carries the LIQUID-form phrase (leg A) — never a clean desk; the --selftest positive control proves LIQUID pre-fix hits and OTTO pre-fix misses (the declared blind spot); drop counts cover git-added WALTER-inbox files in the two recognised forms only.

**Last_verified_run:** 2026-09-24 (--selftest rc 0, re-run this pass; --drops OTTO 0 → 17 matching the lead's git count, LIQUID 6 → 6; conservation 291 attributed + 17 unattributed = 308 distinct basenames; YEYOU moved OWED → RETIRED; runs/2026-09-24_LOCAL_TOOLS_BUILD.md)

**Gap:** rc is unchanged by the screen, so the live census still exits rc 1 on retired YEYOU's canon row (contract change or freezing YEYOU's canon RULED 2026-09-24: rc counts canon rows (RC BASIS line printed); OWED lists live desks; YEYOU row freeze = next-session ruling); 17 WALTER-inbox files carry no sender token and count for no desk; uncommitted drops are invisible; runs/2026-09-17_WIRING_SWEEP_02_JUDGMENT_W1.md (OTTO '0 all-time') and _JUDGMENT.md:6 are stale records.

### scripts/brief_pin_check.py

**State:** BUILT-UNWIRED

**Invoked_by:** NOT YET INVOKED — proposed to NEXUS's reader pin check (NEXUS CLAUDE.md:49); by A11's scope constraint it is never a desk closeout step

**Null_meaning (what a PASS proves — PAT-074):** rc 0 = no brief's header pin names an older STATUS commit or a non-STATUS commit. Does NOT prove brief CONTENT matches STATUS (fresh pin over stale body passes) and does NOT A11-check UNPINNED briefs (9 of 27 on 2026-10-08). Unknown desk or 0 briefs = rc 2.

**Last_verified_run:** 2026-10-08 16:42 EDT: selftest 12/12 (frozen git fixtures, every verdict + rc precedence + empty population); live 27 briefs: OK-PINNED 7 · OK-SAME-COMMIT 9 · STALE-PIN 1 (CORAL) · PIN-UNRESOLVED 1 (BROCK) · UNPINNED 9, both blockers verified at git; first live run produced a false STALE-PIN on BRENT (a line labelled Historical), fixed + test F added before commit.

**Gap:** No independent read yet. Pin parse = first STATUS-commit hash in the first 40 header lines not labelled historical; any other pin form reads UNPINNED.

### scripts/account_guard.py

**State:** WIRED-SINGLE-INVOKER

**Invoked_by:** scripts/githooks/pre-commit; core.hooksPath=scripts/githooks

**Null_meaning (what a PASS proves — PAT-074):** No detected candidates in inspected staged additions; not comprehensive secret detection

**Last_verified_run:** 2026-10-20 code and installed-hook inspection; no fresh behavioral suite claimed

**Gap:** Hook skips this leg if Python/script unavailable; whole hook is not fail-closed


## Lead-review correction — October21

Independent source re-read confirms the initial orch_log wording conflated separate assurance boundaries. scripts/orch_log.py:77 validate_line and :102 check validate schema v2, typed nonnegative counts, event class and basic fields; they do not validate structured closeout timestamps. append at :193–195 validates only marked time-correction rows through orch_time.validate_correction. Rotation at :384 uses orch_time.rotation_problem. Lifecycle timestamps are checked in PROME/tools/orch_closeout.py:70 onward, including original/follow-up ordering. The row disposition and JSON are corrected; never infer lifecycle timestamp validity from orch_log check PASS.

All suggested root-script/hook/installer Owner fields now say DAEDALUS (surface); PROME integration. orch_time was DAEDALUS-built. This corrects initial provisional PROME ownership, which confused integration with surface ownership.

WALTER tools/closeout_check.py was created September15, commit 3fe9a55d3, so it was outside the newly-added-since-October1 local census, not excluded by W2. It has direct closeout invocation in CLAUDE98 after publication/reconciliation and indirect invocation in closeout_run.py:41; no boot invocation found. Because it was directly inspected as a dependency, the historical register omission is now an additional suggested row (17 additions total). PASS is explicit receipt/status consistency, local-origin publication/delivery evidence, hash-bound manually reviewed evidence and delegated corrections write-compliance. It is not remote freshness or semantic/full-duty completion. No behavioral rerun.

## Independent applied-field review — October21

Compared live CHECKS.tsv against HEAD and this reader's final recommendations: 56 rows = 39 prior +17 additions; all17 addition State/Invoked_by/Null/Last_verified fields match the proposed scoped wording. Compared all32 changed existing cells. All32 old cells are retained exactly as parsed TSV values in CHECKS_HISTORY (quoted TSV serialization differs for3 cells; parsed values equal, no data loss). Root ownership correction is present.

PASS-meaning review: ACCEPT changed position-agreement, session-banner, firetime, canon, docket-view, orch_log and explicit read-cap wording within their stated perimeters. orch_log check is schema/typed fields; marked correction validation is append-specific; general lifecycle timestamp checks belong to PROME orch_closeout/orch_time. No global timestamp validity, authentication or liveness inferred. New rows consistently say source/invocation inspection only; no invented behavioral reruns. Lead-only live observations on lane coverage/canon/maturity/memory census/validate_all are explicitly recorded as lead receipts, not this reader's reruns; this bounded review did not independently reproduce those runs. L748 test counts are attributed to PROME and explicitly not rerun.

ACCEPT WITH TWO RESIDUAL WORDING CORRECTIONS (both preexisting cells outside the32 applied edits):

1. scripts/corrections_boot_check.py Null write-compliance clause still limits resolution to filename `-to-…` and original recipients, contradicting the October20 implementation and Last_verified cell. Exact replacement clause: “--write-compliance rc0 means every correction-class signal in the selected window is registered or explicitly dispatched not correction-class, and checkable registered corrections cover corrected ∪ correcting action+info recipients. Resolver uses explicit corrects frontmatter first, then unambiguous filename forms; bad/missing explicit pointers are findings. EXTERNAL/unresolvable originals remain reported not-checkable; no proof of unpublished corrections, recipient semantic action or row correctness. Zero signals in window = rc2.” Source: scripts/corrections_boot_check.py resolver and union at lines467–497. Retain boot-mode receipt limits before this clause.

2. scripts/session_banner.sh Gap still says ONLY harness-invoked check and cannot be skipped. Exact replacement: “Claude SessionStart hook configured; native Git hooks and pipeline guard are separate harness mechanisms. This inspection does not attest execution on every runtime/host or make the banner unskippable.” The new Null correctly limits Codex claims; this gap should agree.

No register edits by reader. Final acceptance of these two remaining wording changes can be closed by a bounded delta read; no functional tests are needed for metadata-only correction.

## Final two-cell delta acceptance — October21

ACCEPTED. Re-read only corrections_boot_check Null and session_banner Gap after lead correction. Corrections now states explicit metadata precedence, corrected union correcting recipients, not-checkable and rc2 limits; banner now limits wiring to Claude, disclaims Codex/other-host attestation, and acknowledges native hooks/pipeline. Both requested residual wording corrections are resolved. Synthesis pair runs/2026-10-21_CHECK_REGISTRY.md exists. This closes the bounded metadata review; no broader source review, functional test or runtime execution claim is added.
