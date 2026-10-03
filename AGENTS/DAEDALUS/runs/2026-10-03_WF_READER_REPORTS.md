# Independent WF directory plan and result review

2026-10-03 · Reader: Codex review_readcap (independent of implementing parent).

## Plan review — conditional acceptance before implementation

Authority read directly: PROME/DOCKET.tsv physical L490; full `PROME/inbox/processed/2026-09-25_from-DAEDALUS_cadence-and-watch-terms.md` (especially §2–3); full `PROME/inbox/processed/2026-09-26_from-DEWEY_cadence-and-watch-terms.md`. These authorize a generated configured-phrase count, with `n`, `—`, owner-declared `n/a`, and unreadable-source `UNKNOWN`; they do not authorize modifying the lane, matcher or terms. Read `builds/2026-10-03_WF_ACCEPTANCE.md`, `scripts/render_directory.py`, UPGRADE_PROTOCOL rules 4/4a/4b, lane WATCH_FOR literal/schema and top-level AST structure.

**Plan accepted subject to the explicit parser and consumer boundaries below.** Static extraction without importing/executing the lane is appropriate. Live lane has one plain `WATCH_FOR` dictionary assignment at line 630, 24 string keys, each mapping to a list of nonempty strings. Snapshot SHA256: `1d5a88fb5e3f8cfa1297764cce79b19a3f711180a35443894349960983cba0b7`. No lane edits or writes occurred.

Independent counterexamples supplied to the parent **before implementation**:

1. `WATCH_FOR = alias = {'SAM': ['x']}` followed by `alias['SAM'].append('y')`: a detector scanning later direct WATCH_FOR references misses the alias mutation. **Remedy:** require the declaration to have one simple WATCH_FOR target; reject chained/aliased targets.
2. `def f(x=WATCH_FOR.pop('SAM')): pass`: the WATCH_FOR use is in a top-level definition's evaluated default, not its deferred body. **Remedy:** do not exempt decorators, defaults or class bodies merely because they occur inside a definition node. A normal function body reading WATCH_FOR, such as live `match_watch_for`, need not invalidate the declaration.
3. Duplicate literal dictionary keys silently overwrite under `ast.literal_eval`. **Remedy:** inspect keys before conversion, reject duplicate/schema/computed/mutated declarations rather than printing a partial count.

Dynamic mutation via `globals()['WATCH_FOR']`, `exec`, or a call into a mutator is a static-analysis limitation. Do not claim arbitrary Python runtime configuration is proved by a literal extractor. Either reject recognizable unsupported dynamic forms or scope output explicitly to the literal declaration. Nothing in this build should execute unknown code to close that gap.

Value semantics reviewed: count list entries, not distinct matched phrases, hits, quality, coverage, desk activity or routing health. A present key, including an empty list (0), wins over an exemption; an absent key is `—`; only DAEDALUS and DEWEY have read-and-verified no-query declarations in this plan. Unreadable/malformed source is `UNKNOWN` for every row, including those two exemptions, since a new declaration cannot be ruled out. Do not manufacture exemptions from desk class or name.

## Consumer/remedy review (rule 4a)

Repository-wide Python/shell reference search found consumers in root `scripts/{canon_check,read_cap_check,corrections_boot_check}.py` and DAEDALUS `scripts/{read_cap_check,sweeps_due,falsification_scan}.py`; `walter_route_check.py` imports the roster-retirement helper. The name/group parsers use the first Agent cell and section headings, not trailing cell counts. The freshness reader uses the `Generated YYYY-MM-DD` header. Keep those stable; append WF without moving the existing cells. Preserve co-registration/reverse/retirement guards and `--check` no-write behavior.

**Freshness boundary:** `sweeps_due.py` currently watches only ROSTER and FLEET_MAP commit dates. It cannot certify the new external lane source has not changed since render. The directory must describe WF as a render-time snapshot with lane path and hash; lane edits require regeneration. Record this limitation instead of implying the existing staleness guard watches all three sources. Extending that guard would be a separate scope change requiring its own checks.

Renderer rc 0 means its established structural rendering contract passed; it must not be described as proof of known WF data if all cells read UNKNOWN. UNKNOWN needs visible source/error provenance. No matcher or other desk process should start consuming WF as a health/launch trigger.

Result read is still owed at this plan checkpoint. Tests required at result: independent bad-input counterexamples, actual literal count comparison, present/absent/empty/exempt/UNKNOWN precedence, no source execution, table and consumer compatibility, `--check` no-write and no bytecode, and final generated read-cap measurement. Any fixes after that read need a POST-REVIEW record per rule 4b.

REVIEW: required — rule 4 evidence interpretation (new generated WF figure); scope: authority packets, acceptance plan, render_directory generator and discovered directory consumers, lane WATCH_FOR declaration/top-level AST; reader: Codex review_readcap; disposition: PLAN ACCEPTED WITH BOUNDARIES, result review owed. No implementation reviewed yet.

## Result review — accepted

Reviewed final generator SHA256 `666110836dee09c1ba7b9c3d1ed9fd2490013a5ed3e273978cea33db0e313a00`, `scripts/test_render_directory_wf.py`, and generated `FLEET_DIRECTORY.md`. The lane hash remains `1d5a88fb5e3f8cfa1297764cce79b19a3f711180a35443894349960983cba0b7`. **ACCEPTED for the configured phrase-count snapshot. No blocker found.** This is not an assessment of recall, matching behavior, routing health, declaration completeness or desk activity.

The implementation adopts a stricter whole-module grammar than a WATCH_FOR-only scan: literal assignments; unaliased `import os`; the current simple `os.path.join` expression over known literal strings; inert function definitions with literal defaults and no decorators/annotations. Other executable/computed constructs yield UNKNOWN. The lane is never executed or imported. This directly closes the plan's alias/default/decorator/mutator counterexamples without changing the lane itself.

Independent result checks (temporary fixtures, no production mutation):

| Check | Observed result |
|---|---|
| Fresh counterexample: define a mutator that appends to WATCH_FOR, then call it at top level | UNKNOWN; literal count not reported |
| `globals()['WATCH_FOR']` assignment | UNKNOWN |
| Dictionary unpacking from another binding | UNKNOWN |
| Unhashable literal dictionary key | UNKNOWN rather than uncaught error |
| Class-body mutation | UNKNOWN |
| Keyword-only default calling WATCH_FOR.clear | UNKNOWN |
| Top-level file-writing expression | UNKNOWN; sentinel file not created |
| Invalid UTF-8 source bytes | UNKNOWN |
| Configuration bytecode | No `__pycache__` in the fixture directory |
| Independent AST count versus new parser | Exact equality: **24 keys, 249 phrase-list entries** |
| Generated table counts versus independent counts | All **43** rendered agent rows agree with their expected count/absence/exemption |
| Row conservation against HEAD's prior generated directory | Same **43** agent names; all **seven prior cells** unchanged per row; WF appended as eighth cell |
| Unavailable-source full render | All **43** rows render UNKNOWN, including DAEDALUS and DEWEY; real directory unchanged |
| Real `--check` dry run | `would change: no, +0/-0 bytes`; content and nanosecond mtime unchanged |
| Author regression suite independently rerun | **10/10 pass**, rc 0 |
| Boot read cap | **12,210 B**, displayed **38%** of 32,550 B budget, rc 0 |

Counts were recomputed from individual literal key/value AST pairs, not copied from the parser's result or a previous narrative. Duplicate phrases would count as configured entries; no deduplication or quality scoring is implied. Old-column conservation used `git show HEAD:AGENTS/DAEDALUS/FLEET_DIRECTORY.md` and parsed unescaped table separators; it did not regenerate or overwrite the baseline.

The generated legend explicitly scopes WF to render time, names all value states, displays the lane path/hash, and says the existing directory-age guard watches only ROSTER/FLEET_MAP. The UNKNOWN rendering also says rc describes the structural guards. Source freshness therefore remains a documented limitation, not a falsely expanded guard. Existing Agent-column/heading/date consumers retain their inputs; co-registration, reverse and retirement guard bodies remain unchanged in the reviewed diff.

REVIEW: required — rule 4 evidence interpretation/new generated figure; scope: `scripts/render_directory.py` WATCH_FOR extraction/value/render branches, `scripts/test_render_directory_wf.py`, full generated table and legend, canonical authority/exemptions and directory consumer contracts; reader: Codex review_readcap; disposition: **APPLIED 3 plan remedy classes** (alias and evaluated metadata rejection, strict dynamic-module rejection, consumer/freshness disclosure), **RESIDUE 1** (external-lane freshness not watched automatically; explicitly accepted snapshot boundary). Independent result accepted at the generator hash above. Later changes are POST-REVIEW until separately read.
