# Closeout checker duplication census — October 21, 2026

**Decision: retain the local checkers. No shared closeout library is justified by this census.** Repeated mechanics exist, but their observable contracts differ. The smallest plausible later extraction is a raw TSV-width diagnostic used by SAM and BROCK, with each caller retaining header selection, expected width, missing-file policy, CR handling and findings text. Even that is a candidate for a separately reviewed change, not a build recommendation today. The stronger immediate follow-through is verifying two existing delegated-error paths, not merging evidence rules.

**Authority and scope:** RED's October 15 packet `inbox/2026-10-15_from-RED_closeout-checker-duplication-census-ASK.md`, read whole, approves audit first and explicitly excludes a library/standard/checker change. The packet calls the population seven desks, but its table names **nine desks and eleven files**, including RED itself. This report accounts for all eleven. STATUS's maintenance lane still correctly calls this audit-only; October 27 was proposed, not a registered deadline. Result is for PROME through DAEDALUS's artifact/closeout; nothing is owed back to RED and no external send occurred.

## Measured population and current invokers

Paths below are relative to `AGENTS/`. “Invoked” means current executable or charter wiring observed, not proof that the most recent operator ran it. Raw search results, including tests and historical research scripts distinguished below, are saved in `runs/2026-10-21_DUPLICATION_CENSUS_evidence/invokers_raw.txt`.

| Desk / file | Lines now | Current production invocation / rc contract |
|---|---:|---|
| SAM `scripts/closeout_check.py` | 676 | CLAUDE:80 manual closeout after final commit, before safe-push; `--pre-commit` explicitly skips ordering/tree checks. Charter still PROVISIONAL. 0/1; exception-to-ERROR joins problems, but ordinary child nonzero is not automatically blocking. |
| CARL `scripts/consistency_check.py` | 1,317 | `scripts/boot.py:46` uses `--quiet --warn-only`; CLAUDE:111 mandatory before commit without that flag. 1 for HARD findings, 0 for SOFT only or warn-only. Current main runs A/B/D/E/F/G: RED's B-unbuilt premise is stale. C remains outside current six-check list. |
| TERRY `scripts/ledger_sweep.py` | 1,603 | `scripts/boot.py:257` advisory; CLAUDE:179 and CLOSEOUT:84 mandatory closeout. 1 for A–H findings; I inbox advisory never blocks. `--selftest` also runs the live sweep afterward. |
| BOND `monitors/closeout_check.py` | 172 | `monitors/closeout_run.py:277` invokes it. Four checks share one cache-busted fetch. 0 clean, 1 finding, 2 fetch failure. |
| BOND `monitors/closeout_run.py` | 448 | CLAUDE:37 / CLOSEOUT:50–53 C12: tiered runner then `--verify`, exact-path commit, safe-push. 0/1 runner; writes transcript and CLOSEOUT_LOG; freeze verification is not push proof. |
| WALTER `tools/closeout_check.py` | 133 | `tools/closeout_run.py:41`; CLAUDE:98 also requires re-run after publication/reconciliation. 0 PASS, 1 REVIEW, 2 UNKNOWN. Checks local origin ancestry; never fetches. |
| WALTER `tools/closeout_run.py` | 183 | CLAUDE:98 tier light/full with explicit condition flags and dated research output. 0/1/2 selected-check state, procedure completion UNVERIFIED. Writes only evidence/draft in its allowed research directory. |
| BROCK `scripts/brock_selfcheck.py` | 123 | CLAUDE:62 closeout 6c ALWAYS. 0 clean, 1 findings, 2 required surface missing. Adoption from CREED is documented; CREED is outside this requested census. |
| HANS `scripts/closeout_check.py` | 191 | CLAUDE:46 / CLOSEOUT:55 mandatory mechanical runner. 0/1, with tool-specific allowed exits plus completion-output signatures; manual duties remain visible. |
| VULCAN `tools/closeout_check.py` | 465 | CLAUDE:38 FIRST and LAST closeout call. 0 mechanical pass, 1 FAIL/LOOK, 2 base/runner crash. Was 424 lines in RED's snapshot. |
| RED `scripts/closeout_check.py` | 586 | CLAUDE:74 W10 gate before commit. 0 scoped pass, 1 FAIL, 2 UNKNOWN/INCOMPLETE; `--at` historical surfaces skip delegated checks explicitly. Was approximately 430 lines in request. |

Two dated WALTER research scripts also call its checker (`research/2026-10-14_walter-closeout/record_publication.py`, `research/2026-10-14_morning-news/finish_commit.py`). They are historical workflow artifacts, not evidence of a new standing boot hook. Test imports are not production invocation. No fleet hook, cron or external orchestrator census is claimed.

## Eight requested primitives

Legend: **D** direct implementation; **delegate** named downstream implementation inspected at the decisive range; **similar** related task but a different predicate; **—** not implemented in the inspected checker's control flow. These are presence findings, not pass grades on owner state.

| Desk | TSV row width | Raw CR detection | Own tree clean | Child crash not pass | Canon/mirror set | Derived tally | Brief last | Commit/push evidence |
|---|---|---|---|---|---|---|---|---|
| SAM | D, header-relative | D, any raw CR byte | D, own dir | PARTIAL: caught launch/timeout only; see below | D, sidecar keys; docket identity richer than set | D, five status classes | D, committed times | Tree committed; push receipt MANUAL |
| CARL | —; parser tolerates short optional cells | — | — | Not a child runner | D, canon/mirror ID union with HARD/SOFT asymmetry | D, matrix/histogram | — | — |
| TERRY | —; minimum columns plus parse-coverage check | — | — | Not a child checker runner | Similar, compatible state claims across surfaces | D, real-lane contract counts | — | — |
| BOND | delegate `kb_lint.py:375–377`, fixed 13 KB fields | — in inspected validators | Similar, start/end content digest, not clean-tree predicate | D, mode-specific classifiers; no universal guarantee claimed | delegate mirror token/version comparison, not generic set equality | Similar, market series derivations delegated | D, vintage/no-op policy | Log+digest+verify; publication MANUAL |
| WALTER | D, DictReader malformed-row sentinel on selected delivery ledger | — | — | D, tool-kind adapters and UNKNOWN | Similar, unique delivery pairs and origin evidence | D, selected/proven deliveries | — | D, receipt commits vs local origin ancestry and evidence hashes |
| BROCK | D, fixed 13; skips ID/comment lines | — | — | Not a runner | Similar, fire/resolution propagation by live segments | D, matrix sum/denominator | — | — |
| HANS | — here | — | — | D, allowed codes AND terminal signature/no crash text | — | — | — | Judgment/manual |
| VULCAN | delegate `validate_workbook.py:218–221` | — in inspected validator | D, own dir | PARTIAL: some rc ignored; see below | Similar, file-touch/score-change proxies; event-set review MANUAL | delegate workbook score reconciliation | D, exact STATUS commit pin and clean STATUS | D, scoped ahead-of-local-origin plus recorded delegation |
| RED | delegate `schema_check.py:132–141` | No: `tsv` normalizes CRLF | — | D for caught exceptions/Traceback; other nonzero advisory remains advisory | D, CHG IDs plus grade/status/date; trigger state rules | D, CORRECT/WRONG/ACTIVE | No ordering; header value agreement instead | Manual; `--at` is vintage evidence, not publication |

**Interchangeability verdicts:**

- **TSV parsing is not one interchangeable parser.** SAM preserves raw bytes before decoding, uses first non-comment header and diagnoses absent headers. BROCK asserts 13 fields and skips `ID\t`. CARL locates named required columns, tolerates short fields and selects CRL IDs. TERRY finds the first multi-tab header and separately fails zero parsed coverage. RED's local `tsv()` fills missing fields with empty strings while delegated schema catches ragged rows; its schema parser deliberately splits literal tabs because quotes are prose. WALTER uses CSV quoting semantics and `None` sentinels. A generic DictReader swap could change actual evidence.
- **Crash handling is a common concern, not a common policy.** HANS requires tool-specific completion signatures; WALTER's doctor returns a finding count modulo 256 and has a terminal footer contract; BOND permits acknowledgment for cross-agent consumer findings but never self findings; RED gates and advisories differ. Central `rc != 0` would wrongly turn valid findings into crashes or wrongly accept unavailable checks.
- **Mirror equality, history stripping and tally derivation must remain local.** Sets alone lose SAM date multiplicity/tenor identity; CARL intentionally distinguishes missing resolved mirrors from missing OPEN rows; TERRY supports compatible states, first card declaration, last trade-book row and separate live real contracts; RED counts resolved outcomes rather than SAM's five terminal classes; BROCK strips historical cell segments, not whole lines.
- **Brief ordering has three contracts:** SAM committed timestamp order; BOND dirty-is-now vintage plus explicit allowed no-op; VULCAN exact STATUS commit pin with STATUS clean. They cannot substitute for one another without changing the invariant.
- **Publication evidence differs:** clean tree, unchanged content digest, publication ancestry, and a human safe-push receipt prove different things. No common `is_done()` is supported.

## Counts, with the denominator exposed

The eleven named files contain **5,897 physical lines**. Static AST inventory finds **153 top-level functions/classes**. A comparison of top-level function ASTs after dropping the function name, docstring and source-location attributes found **0 identical cross-file function groups**. It retains variable names, constants and paths; it does not detect renamed/adapted or partial-body clones. Zero exact groups is not zero semantic duplication.

A disjoint, reproducible **selected-range allocation** answers the useful portion of the duplication question without pretending every comment is reusable code:

| Allocation | Physical lines | Meaning |
|---|---:|---|
| Repeated-mechanics candidates | 309 | Selected TSV/CR, subprocess/classifier, tree/order/publication spans across seven desks; includes local policy, diagnostic text and comments. Upper bound on these candidate spans, **not removable code**. |
| Clearly desk-specific evidence bodies | 1,854 | Named rule/parser bodies and BROCK propagation/matrix block; conservative lower bound. |
| Other / unclassified | 3,734 | Remaining prose, CLI/report plumbing, tests/fixtures, local rules and generic helpers; **not assumed to be duplicates or desk-specific**. |
| Total | 5,897 | Exact conservation; ranges and file hashes saved. |

Per-file counts and exact inclusive ranges are `line_counts.json` and `line_allocations.json` in the evidence directory. The classification is intentionally bounded. It does not provide an honest whole-file “duplicate versus specific” binary percentage: that would require assigning all mixed orchestration, fixture and documentation lines an arbitrary semantic label. For example, TERRY's embedded `selftest` alone spans 371 lines; deleting it as overhead would destroy regression protection. Three downstream schema snippets inspected for delegation are outside the eleven-file denominator and are not silently added.

## Lessons a naive merge would lose

| Local implementation | Preserve explicitly |
|---|---|
| SAM `_quoted_spans`/`_is_historical_quote`, `check_docket`, `check_scoreboard` | Quoting AND a history cue required; backticks are formatting; line-start/end empty-character trap; same-date event multiplicity; long-title tenor swaps must compare discriminating tokens directly; five-part scoreboard conservation; declared delegation must actually be called. |
| CARL `check_a/b/d/e/f/g`, `main` | Required mirror is PREDICTIONS_MIRROR, never silent fallback to STATUS; score histogram membership/arithmetic; named resolving instrument; nested threshold monotonicity; position-linked bias versus actual causal proof; tier-1 registration gates versus lower-precision advisory rules; boot warn-only versus blocking closeout. |
| TERRY `state_of`, table readers, read sanity, contract counts, inbox scan | Case-sensitive declaration prefixes and compatible axes; first card verdict versus last trade-book row; zero parsed surface is not quiet; key+value rather than naked number; real versus paper lanes; exact card identity; inbox advisory must not incentivize unread filing. |
| BOND check/runner | One cache-busted fetch for numeric and directional checks; fetch rc 2 means both unrun; self consumer findings cannot be acknowledged away; outgoing packets and untracked content in digest; failed git read is no snapshot; transcripts retain diagnostics. |
| WALTER inspect/classify | Explicit schema receipt; local-origin-only ancestry; delivery cohort uniqueness; hash-bound manually reviewed owner evidence, never automatic semantic completion; doctor count/footer contract; selected checks never certify full procedure. |
| BROCK top-level rules | History removed at cell-segment granularity, not entire line; missing required surface rc 2; narrow named fire/resolution/count checks never general truth. |
| HANS `_crashed`/`_ok` | Valid nonzero findings need their own completed output signature; rc 0 alone and marker substrings alone are insufficient; manual duties remain visible. |
| VULCAN checks/new_ruling_lines | Today ET/base snapshot, current-session ruling versus historical restatement, score-change propagation, first-public time, freeze/dated-deferral scope, exact brief pin, owner-local push delegation. |
| RED Vintage/hold_netbear/checks | Historical `--at` compares commit surfaces with parent and skips present-day delegates; earliest canonical HOLD/net-bear pair beats stray figure and quoted prior; generated mirror comparisons are not owner judgment; unknown differs from failure. |

## Concrete disposition and bounded next scope

1. **No library now.** Keep owner scripts and current caller contracts. No code changes, standard, schema replacement or common result enum is proposed for approval. All existing owned tests remain attached to their implementation.
2. **Optional future candidate, only if repeated maintenance cost appears:** raw literal-tab width diagnostics for SAM/BROCK first. Scope would be one pure bytes/line primitive returning row numbers and widths; wrappers keep policy and wording. Before any extraction, compare actual ledger counterexamples including preambles, prose quotes, CRLF, empty/header-only data, missing files and fixed-versus-header width. Do not include CARL/TERRY/RED parsing or market evidence rules by name similarity. This census does not establish net savings.
3. **Higher-value audit residue, SAM:** `run_delegated:553–585` catches Python launch exceptions/timeouts as string ERROR; `main:642–650` joins only ERROR to problems. A launched child process that exits 1 with traceback is an ordinary nonzero and can leave the structural headline PASS. Static path supports the risk; no live owner execution or fixture reproduction done here. Existing “delegated crash not-pass” wording should not be treated as universally verified. Owner-scoped injected regression and fix decision are the bounded follow-up, not a library prerequisite.
4. **Higher-value audit residue, VULCAN:** root orphan branch reads warning text but ignores rc, ledger-staleness branch extracts stale names but ignores rc, and `git()` defaults to returning stdout despite errors. Thus blank failure output can look like no warnings/no dirty paths. Static path only; no claim this happened in a production closeout. Next review should inject unavailable-tool/git responses into those exact branches, preserve valid advisory semantics, and obtain owner acceptance before any change.

These two residues are recommendations for evidence-backed owner follow-up. No packet or owner edit was made by this reader; lead owns routing. They do not establish the other seven desks free of error.

## Coverage and completion

**Completed:** every named file inventoried; all eight requested primitive families accounted for per desk; current charter/executable callers located; selected decisive helper/control-flow bodies read; line denominator and bounded allocations recorded; exact AST clone test performed; local lessons and extraction verdict recorded. Initial broad output truncations were not counted as whole reads; decisive ranges were re-read. Current caller search itself is saved whole even when display was shortened.

**Not completed or claimed:** whole-repo semantic clone detection; all 5,897 lines individually adjudicated; every delegated validator audited; latest operator compliance; live market retrieval; checker/selftest execution; dynamic crash reproductions; owner repair acceptance. BOND checker fetches and mutates cache, BOND runner writes logs, WALTER runner writes research evidence, TERRY selftest continues to live scan. None was run merely to count duplication. AST parsing reads source without importing or executing it.

REVIEW: required for any subsequent implementation, none performed. This census is evidence and a no-extraction recommendation, not acceptance of a changed guard. Independent challenge of the recommendation/line allocation remains the lead's review step.

COMPLETION: bounded duplication census delivered. CHANGED: this report, reader receipt and evidence directory only. WILL_NEEDS: none. FOLLOW-UP: lead records audit delivery to PROME and decides whether the two bounded error-path reviews enter existing tooling follow-through; October 27 is not promoted into a registered deadline.

## Lead challenge and delivery — October21

Counterexample: renamed ASTs can encode a genuinely reusable primitive, so zero exact clones cannot establish “no duplication.” Accepted recommendation rests instead on different header/CR/missing-input and advisory/error policies;309 candidate-span lines are not net savings. Lead independently verified per-file/total conservation5897=309+1854+3734 and reread SAM553–585/633–654 and VULCAN50–54/279–282/315–321/329–331. Static error-path candidates stand, with no production incident or dynamic reproduction claimed. No code changed.

REVIEW: evidence interpretation challenged by DAEDALUS lead after independent census reader; scope allocation arithmetic and decisive SAM/VULCAN control flow; disposition no-extraction recommendation accepted, two source-only regression candidates routed in consolidated PROME packet. Neither author nor lead certifies unclassified3734lines or every delegated validator. Audit obligation delivered; potential fixes remain owner-scoped follow-through, not library prerequisites.
