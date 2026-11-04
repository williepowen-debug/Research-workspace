# L835 narrow language design

**Status: PHASE 1 DESIGN ONLY — awaiting Will's approval. L835 OPEN; rejected candidates NOT ACCEPTED / NOT INSTALLED.**

Authority: Will's November 4 instruction to prepare an implementation-ready specification, acceptance criteria, affected files and estimate. No implementation, production behavior change, monitoring or additional reviewer is authorized. Existing review allowances remain consumed. This specification proposes a replacement; it does not amend the operational contract.

Replace guessed witness filenames with an exact, finite analysis of a deliberately restricted path language. Concrete classification and subtree analysis use the same compiled policy. Keep the existing Git inventory, ownership evidence and closeout machinery; do not build a general glob engine or a second directory policy.

## Language and policy semantics

Language identifier: `argus-path-v1`. Rules remain ordered `(pattern, class, reason)` rows. First match wins, including duplicate or shadowed rules. No match means `UNATTRIBUTED`, which is protected just like `OWNED` and `SHARED`. Only `EXCLUDED` is unprotected. Classification confers no authorship or permission.

The three forms cover the current literal paths, terminal recursive subtrees and `memory/*.md` suffix rule:

| Form | Grammar and exact meaning | Examples |
|---|---|---|
| Literal path | One or more literal segments; matches that entire path only. | `CLAUDE.md`, `scripts/docket_view.py` |
| Subtree | A nonempty prefix of literal or whole-segment `*` tokens, followed by terminal `/**`; matches one or more additional nonempty segments, at any depth. Does not match the prefix itself. | `PROME/**`, `AGENTS/*/inbox/**` |
| Finite-depth wildcard path | One or more segment tokens: literal, whole-segment `*`, or final `*.<suffix>`; at least one wildcard; matches exactly that number of segments. | `root/*`, `AGENTS/*/note.md`, `memory/*.md` |

A literal segment contains only ASCII letters, digits, `_`, `-`, and `.`; it must not be empty, `.`, `..`, or `.git`. A suffix is a nonempty string of the same characters, without wildcard syntax; `*.md` means any single segment ending in `.md`, including `.md` itself. Suffix wildcards occur only in the final segment and cannot precede `/**`. Whole-segment `*` matches every valid nonempty segment, including dotfiles. No wildcard crosses `/` except the terminal recursive tail.

Reject bare `**`, embedded `**` (`a**`, `**a`, `a**b`), internal recursion (`a/**/b`), `?`, character classes, braces, negation, escapes, embedded single stars (`foo*`, `a*b`), absolute paths, trailing/repeated separators and reserved segments. Do not reinterpret unsupported syntax as a literal, broaden it, skip its row, or fall back to the old matcher. Reject the entire policy before classification/freezing with row, pattern and reason; CLI result is `CANNOT-EVALUATE` / rc 2. Unsupported future syntax requires a separately approved language revision.

Paths are case-sensitive repository-relative segment sequences, never normalized or resolved through symlinks. Segments are nonempty and exclude NUL, `/`, `.`, `..`, and `.git`; dotfiles and Unicode are otherwise ordinary. No filesystem-existence assumption is made. The existing delivery-path restrictions remain additional restrictions. An inventory decoding/path-validation failure must stop evaluation, not discard a path. Newline-bearing names must either round-trip through existing Git inventory and this interpretation or fail explicitly; no successful completeness claim on lossy decoding.

The current perimeter fingerprint checked for this design is `478eb2437d444ac0a3f9306e6fa6cd87d2dd93ec5ecb920f6237d3d3e2d1b93c`. All its rules fit this grammar. Preserve the earlier `CLAUDE.md SHARED` row and the later shadowed `CLAUDE.md EXCLUDED` row; no cleanup or reorder is part of L835.

## One interpretation and exact descendant analysis

One dependency-free module exposes `compile_policy(rows)`, `classify(path)` and `has_protected_descendant(directory)`. Compilation validates every row and produces an immutable ordered policy. No standalone regex implementation remains authoritative.

Each compiled rule is a sequence of segment predicates (`literal`, `any`, `suffix`) with either an exact end or a terminal recursive tail. Its transition is deterministic: matching a fixed token advances; a mismatch kills that rule; an exact end accepts only at that depth and dies on another segment; a recursive tail accepts after its first additional segment and then loops. At any end-of-path, the first accepting rule supplies the class, otherwise `UNATTRIBUTED`. Concrete classification feeds actual segments through these transitions.

Descendant analysis feeds the directory's actual segments through the same transitions, then explores **all semantic classes of possible additional segments**, not a list of guessed names:

1. Partition segment strings by their truth values for every literal and suffix predicate in the compiled policy. `any` is true throughout the valid domain.
2. Construct this partition exactly with a reversed-character trie containing all literal strings, suffix strings (including the leading dot), and reserved names. Each node contributes an exact-end atom where valid. Each node also contributes a first-exit atom if a valid next character outside its child edges exists; the remainder is arbitrary. Suffix truths are the suffix terminals already traversed; literal truth occurs only at an exact-end terminal. Remove empty/reserved endpoints. These atoms cover every valid segment and never combine different predicate truth values. Merge identical truth vectors if useful.
3. Explore transitions over those atoms, memoizing `(depth, rule-state tuple)`. After at least one extra segment, evaluate first-match classification at every reachable end-of-path. Any non-EXCLUDED result returns true. Exhausting the search returns false.
4. Let `D` be the greatest number of fixed tokens in any rule (exclude the recursive tail). Beyond absolute depth `D+1`, every exact rule is dead and every surviving recursive rule is already looping. Further extensions cannot change classification. Explore positive extensions through `max(current_directory_depth + 1, D + 1)` only. This bound is derived from the grammar, not chosen by sampling.

Why this is exact: predicates are constant within an atom; transitions therefore preserve every possible rule outcome; first-match evaluation includes earlier exclusions and later exceptions in their actual order; the derived depth bound covers all possible state changes. Concrete representatives may be printed for diagnostics but are never evidence of universal exclusion. A separate reviewer must challenge the partition and depth arguments.

Worst-case search can still grow with overlapping rules. Use memoization and a deterministic 100,000 explored-state limit per directory query; exceeding it returns `CANNOT-EVALUATE`, never false or a claimed protected descendant. Valid current rules and all ordinary excluded-directory fixtures must complete below that limit. No persistent cache or background checker; any per-invocation cache is keyed by the complete immutable policy and directory.

`never_advisory` becomes a small adapter: perimeter file and root `.gitignore`/`.gitattributes` always guarded; other basenames retain their current treatment; nested ignore/attributes files are guarded exactly when `has_protected_descendant(parent)` is true. Missing/invalid policy is an evaluation error. The query includes the control file itself among possible descendants. A false result merely removes this special guard: delivery, evidence, history and actual-commit checks still apply. In particular, existing stricter `--ref` rules are not relaxed.

## Known failures and required results

| Failure / fixture | Required result under this design |
|---|---|
| Direct-child probe misses `.claude/agents/**`, `.claude/skills/**`, desk inboxes or registered `scripts/` files | Guard `.claude/.gitignore`, `AGENTS/.gitignore`, desk-root and `scripts/.gitignore`; the deeper accepting states are reached. Root controls remain unconditional. |
| One excluded witness hides other OWNED children | `root/x EXCLUDED` before `root/* OWNED`: `root/y` is protected. Literal atom `x` cannot stand in for the complementary atom. |
| All seven guessed salts excluded before `root/* OWNED`, then `root/** EXCLUDED` | Still guarded: other names reach the earlier OWNED rule. The later broad exclusion cannot override it. |
| `root/* EXCLUDED` leaves deeper unmatched paths | `root/a/b` is UNATTRIBUTED and protected. A direct-child exclusion is not a recursive exclusion. |
| `root/a**/target OWNED` silently misses `root/a/b/target` | Reject the original policy as unsupported before any verdict. Do not silently translate it. Supported analogue `root/*/target OWNED` before `root/** EXCLUDED` must guard. |
| Unrelated `other/a**/target OWNED` unnecessarily blocks `root/** EXCLUDED` | Original unsupported policy receives an explicit syntax refusal, not an overlap finding. Supported analogue `other/*/target OWNED` before `root/** EXCLUDED` must prove root wholly excluded and permit the ordinary working-tree closeout. Syntax rejection is not claimed to pass the old fixture unchanged. |
| Earlier complete exclusion shadows a later OWNED rule | `root/** EXCLUDED` before `root/*/target OWNED`: root remains wholly excluded. Likewise current `PROME/inbox/**` before `PROME/**`. |
| Common research and processed/inbound exclusions | Current `AGENTS/BROCK/research/`, `AGENTS/BROCK/inbox/processed/`, and `PROME/inbox/` remain wholly excluded; desk inbox itself remains protected. |
| Desk subject, observed-only declaration or pre-freeze commit launders an ignore change | All attribution, freeze, observation and validation entry points use the same guard. Required control-file delivery cannot be bypassed through those routes. |

Port the original fixture inputs as regression evidence, including explicit refusal tests for unsupported syntax. Keep supported analogues as behavioral tests; do not rewrite the old evidence to make it appear accepted. The incomplete fourth Kimi review remains incomplete, not another confirmed finding or a pass.

## Historical manifests and migration

Choose explicit re-verification instead of maintaining two live interpreters. Existing manifests remain immutable historical evidence, but a manifest without the new language binding cannot certify a new closeout. This one-time compatibility cost is part of the proposed change requiring approval.

Version new manifests as **schema 3**, retaining the delivery envelope's existing structure. This is deliberate: old code already refuses an unknown schema instead of accepting a new receipt while ignoring its language binding. Add `contract.policy = {language: "argus-path-v1", source_sha256: <raw perimeter digest>, rules: <ordered full rows>}` inside the existing hashed contract. Compile from these pinned rows only during verification. The existing top-level `perimeter` mirror must exactly agree with the policy's digest and rows; reject mismatch. Freeze parses and hashes the same single byte read. Version, ordered rows and digest therefore participate in `contract_sha256` and its REVIEWED binding. Update every schema dispatch, review marking, candidate selection and reuse check together; unsupported versions never reach a legacy fallback.

Missing language binding, unknown language, malformed rules, absent/null pin, and legacy schema-1/schema-2/unversioned manifests return rc 2 at operational verification, observation, review marking and candidate delivery. They must not fall through to the live-perimeter legacy path. Historical files are not relabeled or rewritten. Explicit re-freeze under v1 creates FROZEN status; review promotion still requires an actual authorized audit. No automatic REVIEWED conversion and no baseline advancement to hide the old failure. The old no-contract freeze command must refuse with the explicit-contract migration instruction, rather than mint another unusable legacy approval.

Automatic exact-byte review reuse also requires equal policy bindings. Old approvals cannot migrate through `reuse_entries`, even when delivered bytes match. Reuse within the same policy retains the existing content/baseline requirements. Changed live rules never change an already pinned policy; the perimeter edit itself remains subject to delivery checks.

This does not claim universal equivalence with the former general matcher. Supported ordinary paths should retain classification; unsupported patterns and ambiguous historical receipts are deliberately refused. Newline/path edge behavior must be explicitly verified rather than inheriting Python regex `.` behavior accidentally.

## Proposed acceptance and independent verification

No reviewer is commissioned by this document. After implementation is separately authorized, seek a named independent acceptance allowance; author tests alone cannot close L835.

1. **Language and reference oracle:** every current row compiles unchanged. Test every rejection above, path boundaries, suffix nesting/overlap (`*.md`, `*.x.md`), Unicode, newline and reserved names. Compare concrete classification with a separately written direct segment matcher that does not import production parser, partition or transition helpers. Differential comparison against the frozen old matcher is limited to its supported, ordinary-path domain; document intentional differences.
2. **Exactness:** reviewer inspects the atom coverage and depth proof, then devises at least one new missed-protection case and one false-block case. Exhaustively enumerate small rule lists, orderings and finite path domains with an independent brute-force oracle; include depths beyond the longest fixed rule, fully/partially shadowed rows, duplicates, suffixes and unmatched descendants. Add generated larger cases with recorded seeds and minimized failures. Testing supplements the argument; no finite sample alone proves exclusion.
3. **Historical regressions:** cover every row in the matrix and original committed/working-tree fixtures. Unsupported originals must fail at validation; supported analogues must exercise both positive and negative descendant results. The current shadowed CLAUDE row remains shadowed.
4. **Actual Git visibility:** disposable repositories only. Use real `.gitignore` plus untracked protected files; establish hiding with `git check-ignore` and NUL-safe status/ls-files output. Test pending, staged, desk-committed and committed-plus-pending controls, before/after freeze, tracked edits, deletions, force-added commits and concurrent foreign arrivals. Test `.gitattributes` guard behavior separately without claiming that attributes hide files like ignore rules.
5. **Actual consumer:** run `argus_scope` freeze, verify, observe, mark-reviewed and candidate-delivery paths; working tree, `--ref`, and `--snapshot`; then the existing `prome_gate.py` Standard closeout consumer in an isolated fixture. A normal excluded-directory arrival must not alone change a valid ordinary working-tree control from rc 0 to rc 1. Protected arrivals must block or require reviewed delivery; malformed/unsupported policies must return rc 2. Standard must reject FROZEN and legacy receipts, and accept only a valid REVIEWED contract. Fixture review marking tests wiring, never pretends to be a real audit.
6. **Compatibility and neighbours:** policy mutation, mirror mismatch, live-perimeter mutation, unknown/missing versions and legacy reuse cannot inherit approval. Verify both directions: new tools refuse old receipts, and the committed old tools refuse schema 3 receipts. Run existing scope, evidence, contract, consumed-move, WQ-583 candidate/reuse and closeout suites. Existing strict commit/snapshot boundaries and ownership rules remain. Reach the state-limit path deliberately; no partial proof may pass.

Known boundaries remain: this repair reasons about control files the inventory observes. `.git/info/exclude`, global excludes, index flags, and a self-ignoring untracked `.gitignore` that leaves no inventory trace are not repaired by changing the matcher. Tests should expose those limitations, not label them fixed. Broadening inventory is separate work. Any blocking acceptance finding stops release; no automatic additional repair/review cycle.

## Affected files and estimate

| File | Proposed treatment |
|---|---|
| `PROME/tools/argus_policy.py` (new) | Small pure parser, segment predicates/partition, transitions and exact descendant query; no Git, network or third-party dependency. |
| `PROME/tools/argus_scope.py` | Replace perimeter `_match`/classification with adapters to the shared policy; reject legacy operational verification; update freeze/mark/review listing paths. Preserve Git discovery and evidence code. Existing hard-coded inbox match callers use the same semantics. |
| `PROME/tools/argus_contract.py` | Remove `_ignore_witness`, `_wholly_excluded`, probe/salt loops and embedded-wildcard special cases. Add policy binding/validation and compatible-reuse checks; retain attribution, candidate and content-integrity logic. |
| `PROME/tools/tests/test_argus_policy.py` (new), existing `test_argus_contract.py`, `test_argus_scope.py`, `test_argus_scope_evidence.py`, `test_argus_wq583.py`, consumed-move and closeout tests | Add independent test oracle, failure matrix, compatibility and real-consumer fixtures; update only expectations intentionally changed by language/version refusal. |
| `PROME/tools/ARGUS_CONTRACT.md`, `PROME/CLOSEOUT_PROCEDURES.md`, perimeter header in `PROME/state/AUDIT_PERIMETER.tsv` | Describe supported syntax, version refusal/re-freeze and precise guard scope. Perimeter rule rows/order unchanged. Update `CLOSEOUT.md` only if its existing pointer cannot express the procedure. |
| New L835 acceptance record; existing DOCKET/WQ and continuity records | Record approved scope and subsequent results without overwriting failed-review history. No closure until independently accepted and separately cleared for installation. |

No planned production changes to `prome_gate.py`, safe-push, root rules, monitor schedules or agent definitions; these are integration consumers, not new policy owners. If wiring requires broader changes, return the concrete scope delta before doing them. Preserve rejected dirty files and patch artifacts; any later build starts from a named committed baseline in a disposable checkout, not by extending the rejected working patch.

**Estimate, not a commitment:** 2–3 focused engineer-days after authorization: roughly half a day for grammar/partition/transitions and proof notes; half to one day for contract binding and compatibility plumbing; one day for regression, disposable-Git/consumer integration and documentation. An independently authorized acceptance session and any resulting disposition are additional. Main uncertainty is consumer/legacy compatibility, not parsing. Favor removing the old logic outright over retaining fallback branches; measure actual code and test complexity at implementation review rather than promising an invented line reduction.

**Phase 1 result:** design proposed; implementation NOT STARTED; independent verification NOT COMMISSIONED; L835 OPEN. Approval of this design alone is not an installation or additional-review grant.

Sources: current `AUDIT_PERIMETER.tsv`, `argus_scope.py`, `argus_contract.py` and consumers; [original nested-control failure](../reports/2026-10-24_L796-pin-counterexample-read3.md); [accumulated acceptance history](../tools/tests/ACCEPTANCE_L835_nested_ignore_scope_2026-11-04.md); [bounded candidate](../reports/2026-11-04_L835-bounded-correction.md); [failed saved-candidate review and design checkpoint](../reports/2026-11-04_L835-saved-candidate-acceptance.md). These are source evidence, not new review rounds.
