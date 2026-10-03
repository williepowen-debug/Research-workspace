# Helm fold — independent plan/remedy reader report

**Reader:** Codex Astra `review_standards`, 2026-10-03. **Stage: PLAN, before implementation.** Synthesis destination: `AGENTS/DAEDALUS/runs/2026-10-03_HELM_FOLD.md`. Authority: Will's continuation of catch-up work; original WQ-372 commission and complete supersession in `inbox/2026-10-02_from-PROME_WQ-372-fold-fleet-ops-into-the-helm.md`. PROME is active: no PROME edits or live builds performed. Only this report was written.

**Verdict:** the proposed extraction/isolated-patch architecture is appropriate. Proceed only with the gate-semantic and missing-data safeguards below reflected in the implementation. Source equivalence alone does not establish H3: the existing donor accepts malformed rows as live or drops them. The current snapshot's matching counts are insufficient acceptance evidence.

## Scope and source fingerprints

Read the complete new `builds/helm_fold_2026-10-03/ACCEPTANCE.md` and full commission including supersession. Read Helm imports, board parser/render, final main/feed path, and docket writer; Fleet-Ops imports/parsers, fleet collection, snapshot function, relevant panel rendering, build and main/write paths; full agent_freshness API implementation through its output logic; brief feed update and persist call boundary; split acceptance's declared residues/episode-2 disposition. Searched direct dashboard consumers/tests. This is not a whole-PROME review.

| Source at read | SHA256 |
|---|---|
| `PROME/tools/will_handbook.py` | `d30da1100625e33bad130ca67ff81a1291804c55600cb48f59c3fe3128d56285` |
| `PROME/tools/fleet_dashboard.py` | `dbed950b2cd23815c189552dfc3ce07cc46768b59b845f21e4cb739a01dc3476` |
| `PROME/tools/agent_freshness.py` | `48465f571d290cea1f9ebb9f1bb89897ea9112dfccdfe1d3885860cab1629d3e` |
| Plan acceptance | `85b78d6d5720dc1d1d0995d278bae3d2a24210b140fef3ee6ce3dfc8febd528e` |

PROME may change targets while the isolated patch is prepared. These are review inputs, not permission to overwrite a later owner version.

## Plan findings and remedy conditions

| ID | Finding | Required treatment / acceptance |
|---|---|---|
| P1 | Donor gate `kind=live` is not literal state LIVE. Its fallback includes every non-resolved, non-FIRED-UNEXECUTED token. Donor `crit` means FIRED-UNEXECUTED only; Helm's existing fired strip includes every FIRED prefix. | Label donor-derived counts by their actual basis; retain existing Helm standing strip/position contract. Never present donor crit count as all FIRED. Fixture with FIRED-EXECUTED must expose divergence. Do not redefine donor classifier silently. |
| P2 | Donor parser drops <8-column rows and classifies empty/unknown state as live. Empty, header-only and malformed-short files all return `[]`. Read errors raise, but successfully read malformed content need not raise. | H3 needs validation/error propagation from the shared parse boundary, with a visible degraded result and REVIEW. A catch-exception wrapper plus `if not rows` covers fully empty files, not a malformed row beside one valid row. Avoid a competing Helm classification parser. Preserve legacy donor contract or explicitly expose a checked companion/interface whose diagnostics do not change donor state schema. Final implementation review required. |
| P3 | Donor gate rows discard `consequence_on_fire`, and `state`/`cond` are already truncated at 220/160. | Do not reconstruct an action from condition, call it original action, or add another truncation. Named fired panel can reuse existing Helm action semantics while donor-count basis is explicit; if full original action is newly required, carry it from the shared source without changing legacy output. Explain any inherited truncation rather than asserting full raw fidelity. |
| P4 | `own_surface_age_days` discards distinction between successful no-history and failed query. Both become donor days=999, cls=crit, word=no git history unless parked. | Display unavailable/no-history conservatively; never say proved no commits on failure, never render 999 as real days. Preserve parking and sort semantics. A parked row with unknown age stays visibly parked without fabricated age. Do not obtain exact timestamp/author by reverse-computing rounded days. |
| P5 | Spec says last self-commit; actual donor measures commits touching non-inbox paths, regardless of author, and returns rounded age/class, no commit identity. | Plan's source-faithful label is correct. State own-surface activity and retain spec mismatch as owner acceptance, rather than claiming literal self-authored-session compliance. A PROME commit to ALPHA/STATUS advances this age even if ALPHA did not run. |
| P6 | Extraction touches a shared build whose class output feeds snapshots and closeout checks. Existing build already has active roster/fmap inputs. | Extract collection with its existing dependencies/inputs and stable order; avoid introducing an extra roster read inside the donor build. Keep snapshot v1 keys and fleet name→class mapping exact, all state/receipt writes in original main. Do not invoke build/main from Helm. |
| P7 | Ages use wall clock in two places: `agent_freshness.time.time` and Fleet-Ops `datetime.now` PROME special case. Passing the same `today` does not freeze either. | Fixed-snapshot equality fixtures must freeze these clocks or supply deterministic ages as inputs. Test missing and 3/7/14-day boundaries plus parking expiry; do not casually replace calendar-age rounding with business days. PROME path remains PROME, not legacy AGENTS/PROME. |
| P8 | Existing adjacent test suite can write live dashboard_build.json: split acceptance W3 identifies `test_desk_attention` patching STATE_PATH but not BUILD_PATH. | Run H7 suites in isolated tree with state-path containment, not against live PROME. Read-only import/function probes here do not run these suites. |

**Plan-safe interfaces:** reuse donor parser/classifier for counts, and render diagnostics separately from data where necessary. An optional checked mode/companion may preserve the default donor API, but the exact change is not yet present: its consumer safety is **UNVERIFIED-REMEDY** until implementation/result review. Do not resolve P2 by making all donor parser errors fatal inside a previously unchanged dashboard without reviewing the build/receipt consequences. Keeping existing state writes and return contracts is part of H4/H6, not something snapshot equivalence alone establishes.

## Reader's own counterexamples and executable probes

Before delivery the following counterexamples were used to challenge the plan: FIRED-EXECUTED beside FIRED-UNEXECUTED; a valid LIVE row beside a short malformed FIRED row; an empty state; failed Git lookup for a parked desk; a coordinator commit to another desk's non-inbox file; and a wall-clock boundary despite identical `today`.

Executed a read-only import plus mocked `fleet_dashboard.read` on synthetic tab-separated rows, with `PYTHONDONTWRITEBYTECODE=1`. Actual donor outputs:

| Input state | Donor kind |
|---|---|
| LIVE | live |
| FIRED-UNEXECUTED | crit |
| FIRED-EXECUTED | live |
| RETIRED | resolved |
| FROZEN | live |
| empty | live |
| NONSENSE | live |

Actual donor row keys were `checked_age, cond, consumed_by, gate, kind, owner, state`: no action field. Empty content, header-only content, and six-column FIRED-UNEXECUTED row each returned `[]`. Therefore those cases cannot be distinguished downstream by count alone. These probes establish P1/P2/P3 at current code, not the behavior of a future patch.

P4/P5/P7 were traced at source rather than Git-history simulations: `own_surface_age_state` differentiates unknown/never/aged; `own_surface_age_days` returns tuple element 1 only. Its query is path-scoped, with inbox excluded, no author filter. `build` replaces None by sorting sentinel 999, parks before staleness classification, and rounds calendar age. These semantics are visible and should remain explicit.

## No-feed and consumer contract

Helm main presently calls `wb.update_changes(..., write=not a.no_feed)`. `update_changes` encloses snapshot creation, append and `_persist_state` in `if write`; `_persist_state` can run Git persistence. The new shared data helpers should be read-only and never call donor build/main. Donor main owns STARTED/failed/success receipts and dashboard snapshot writes; these must remain unchanged. H4 must measure both feed files and both dashboard state/build files before and after isolated Helm `--no-feed`, including missing-file existence, and spy/fail if a write path is unexpectedly called. A read-only helper import does not on its own prove all main paths remain read-only.

The source snapshots have partial concurrency by design (Git reads per desk, working-tree source reads separately). Do not claim atomic fleet-wide snapshot at one HEAD unless implemented. For the required comparison, pin/freeze sources and clock in isolation; do not compare independently moving live renders and call differences an extraction failure.

## Scope preservation and final result-read requirements

The complete supersession expressly keeps manual content and the three tabs, and replaces the obsolete 150 KB/move-manual plan with under 250 KB on the already-split page. Parent acceptance correctly reflects this. The supporting docket remains in its one-snapshot path. Do not touch `write_docket` in this fold unless also taking its named stale-file residue; no need to adopt that unrelated repair to deliver these panels. Keep link verification local versus hosted distinct. The unchanged footer in donor currently says regenerate→republish; the new required retirement header will supersede that instruction at the top, but flag the old footer wording to the owner if it remains rather than claiming every publication instruction has been removed.

Result read should receive: exact isolated diff; frozen before/after donor fleet rows and schema; divergent gate-state fixtures and malformed-partial fixture; missing/parked freshness cases; no-feed file hashes/existence; page bytes and max-line metrics; split/attention suite outputs from isolated state paths; manual-content equality and local link checks; final source-hash application precondition. No result or hosted acceptance is certified by this plan read.

## Coverage / not-read list

Not read: all 1,400 dashboard lines in full (irrelevant glossary/CSS/body text omitted), all Helm manual prose/CSS, all upstream gate owner letters, full closeout checker implementation, publisher APIs/hosted artifacts, full historical staffing/slate trial, unrelated scorecards. No full dashboard or Helm build run; no Standard gate run; no test suite run that might write state; no live freshness measurements or external source checks. Existing split W1–W8 and episode-2 residues were read for boundary relevance, not repaired or independently re-audited.

REVIEW: required — new operator attention surface and shared evidence-helper boundary, UPGRADE_PROTOCOL4/4a/4b; scope acceptance plan, full commission/supersession, named donor/Helm/agent_freshness source regions and feed-write boundary; reader Codex Astra review_standards; disposition PLAN-CONDITIONAL on P1–P8, APPLIED 0 code fixes, UNVERIFIED-REMEDY checked parser interface pending exact implementation. This is a pre-implementation review, not implementation approval or independent result verification.

## RESULT — isolated implementation independently read and executed

**2026-10-03, same independent reader, subsequent result read. Verdict: PASS for the bounded isolated fold, with three disclosed residues below and owner integration/hosted acceptance still outstanding.** No blocking defect found in the reviewed patch. This does not say L594's whole deployment is complete.

**Exact scope:** complete `builds/helm_fold_2026-10-03/helm-fold.patch` (donor helper extraction and optional gate diagnostics, retirement notice, Helm panel/function/import/callsite, new 14-test file); `target_hashes.json`, `validation.json`, `validate_snapshot.py`; isolated targets at `/tmp/daedalus-helm-q7ivlt_b/repo`; canonical `PROME/GATES_README.md` STATES and STATE CELL CONTRACT; relevant source functions inspected in the plan. No additional owner code changed. The synthesis remains `runs/2026-10-03_HELM_FOLD.md`.

### Final patch fingerprints actually measured

| Isolated target | SHA256 |
|---|---|
| `PROME/tools/fleet_dashboard.py` | `ba72f0993a0d269abe06db9bac1d455915c38d3501d7e33323657af7a0605445` |
| `PROME/tools/will_handbook.py` | `772a367603fdd6b9ad22103286adceefbf3b55c935d2abd75998e1e4e87c8694` |
| `PROME/tools/tests/test_helm_fleet_fold.py` | `b33deb8712277cc53fe766e444c939d12ce886072266bf205946db1c5a787dfd` |

All match the bundle's `after` values. Before values match the plan read's sources. Any later code change is POST-REVIEW and is outside this result verdict until checked.

### Plan conditions reconciled

| Plan item | Final implementation evidence | Result |
|---|---|---|
| P1 gate token semantics | Canonical STATES has exactly LIVE, FIRED-UNEXECUTED, RESOLVED, LAPSED, RETIRED. Checked mode admits those lead tokens only. FIRED-EXECUTED is not a canonical sixth state: donor legacy fallback stays live, but new panel withholds counts and raises diagnostic. Count label explicitly FIRED-UNEXECUTED; LIVE explanation preserves executed-leg distinction. | APPLIED |
| P2 malformed partial inputs | Shared donor `parse_gates(..., diagnostics=errors)` flags missing/wrong header, short rows, missing/duplicate ID, invalid lead token and no usable rows. Helm suppresses counts on any diagnostic. Default donor return rows/classification preserved. | APPLIED |
| P3 actions/clipping | New panel names fired gate and state; it explicitly refers to existing board actions. No action fabricated from condition and no new clipping introduced. Existing board parser/feed/position behavior is unchanged. | APPLIED, inherited truncation unchanged |
| P4 unknown/parking | Missing sentinel displayed as unavailable/no-history; parked label retained and no fabricated zero. One bounded sentinel collision recorded below. | APPLIED with R1 |
| P5 activity versus authorship | Panel explicitly says committed changes to non-inbox files regardless of author, rounded calendar days, not proof desk ran. | APPLIED; literal self-commit spec remains R2 |
| P6 extraction/schema | Entire inline fleet collector moved to callable with existing active/fmap arguments; donor retains one roster read and original build sequence. Snapshot schema and main receipt/state writers unchanged. | APPLIED |
| P7 frozen comparison | Validation freezes datetime.now and agent_freshness time.time; fixtures exercise 3/4/7/8/14/15-day boundaries, parking expiry and PROME real-home path. | APPLIED |
| P8 test isolation | All 60 tests ran inside `/tmp/daedalus-helm-q7ivlt_b/repo`; known neighboring test alters only that copy's receipt. Validation restores that isolated receipt from pinned source before no-feed comparison. | APPLIED |

### Reader's own counterexample and tests

**Counterexample posed before this result verdict:** one valid LIVE row plus one malformed short FIRED row must not render a clean LIVE count; valid escaped fired state must still render its gate; an actual parked age of 999 days must be distinguished from the missing-data sorting sentinel if the representation can support it.

Independent direct probes in the isolated tree returned:

```text
mixed malformed withholds counts: True [('fleet-gates', 'GATES row has fewer than 8 columns')]
valid fire: True True True []
parked actual 999-day alias: True
unparked real999 shown: True
```

The valid-fire booleans mean LIVE 1, FIRED-UNEXECUTED 1, escaped `F-&lt;b&gt;`, with zero alerts. The malformed case contains no `<strong>LIVE` count. The parked collision is real but conservative; it does not claim freshness or alter source class/parking.

Independently executed:

```text
python3 -B -m unittest PROME/tools/tests/test_helm_fleet_fold.py \
  PROME/tools/tests/test_helm_size_split.py \
  PROME/tools/tests/test_desk_attention.py \
  PROME/tools/tests/test_dashboard_build_receipt_L339.py
Ran 60 tests in 10.099s — OK
```

The `BUILD FAILED ... missing source` output occurred inside the intentional failure fixture; suite verdict remained OK. No live PROME state was touched.

Independently reran the exact submitted `validate_snapshot.py` after reading its write boundaries. It only restored/wrote the isolated tree and `/tmp` output. Its donor health-check subprocess wrapper is stubbed to zero: these results never certify Standard gate health.

| Reproduced result | Before | After |
|---|---:|---:|
| Helm rc / alerts | 0 / none | 0 / none |
| Page bytes (`measure.py`) | 211,025 | 213,022 |
| Maximum line bytes | 5,768 | 5,768 |
| Manual SHA256 | `c3d9b0365565d694e85e5b2b382088356707b277abd13b941c20143e4838a0a7` | identical |
| Donor fleet | 34 rows | identical values and ordering |
| Donor snapshot | v1 source output | identical |
| Entire donor HTML | baseline | retirement notice only difference |
| Donor gate counts | live 18 / crit 0 / resolved 2 | identical |

All four pre-existing no-feed files remained byte-identical: `brief_snapshot.json`, `brief_changes.jsonl`, `dashboard_state.json`, `dashboard_build.json`. Read script also guards against `_persist_state`, dashboard build and receipt calls during Helm main. This execution covered existing files; absence-state behavior is supported by untouched write guards, not a separately executed missing-files test in this result pass. All 79 local `docket.html#...` links matched supporting-file anchors; Deck header link remains. No hosted links/publication were exercised.

### Residues and ownership

1. **R1 LOW — parked real age 999 collision.** The legacy row representation uses 999 for no-age and loses the original age-state flag. A genuinely 999-day-old parked desk is conservatively shown unavailable/no-history because parking also replaces `word`. Unparked genuine 999 remains visible. This is a measurement-detail loss, not an all-clear or changed parking; no schema enlargement is required to ship the bounded fold. Any future fix should carry an explicit age-state value with consumer review, not infer it from another arbitrary sentinel.
2. **R2 SPEC DEPENDENCY — no exact self-commit.** Output is honest own-surface age and freshness, not literal last self-authored commit identity/time. Source donor does not provide that evidence. PROME must accept that documented interpretation or commission a separate attribution source. Do not mark literal spec-field compliance established by this read.
3. **R3 LOW — old donor footer still says regenerate→republish.** New top retirement notice is correct and explicitly supersedes published use; full donor-page equivalence necessarily retains this old footer instruction. Flag it on owner integration; no claim that every publication instruction was removed.

Owner-dependent acceptance remains: application against matching source hashes or a reviewed rebase, real unchanged `prome_gate closeout --tier standard`, process-slot/CLOSEOUT changes, and hosted publication/link verification. No reviewer here performed any of these. The page stays under 250 KB for the frozen representative snapshot; future unbounded source growth is not a permanent size guarantee. Existing split failure/hosted-link residues remain outside this patch.

**Coverage preserved:** this is a patch/result read, not full upstream parser correctness certification. No corpus-wide gate-owner-letter read, full Standard gate, hosted test, or state-machine redesign. The checked optional diagnostics interface is now independently read and fixture-tested for its stated guard contract; it does not validate every field of every gate row. No new source-side correction, scheduling trial or scorecard was performed.

REVIEW: required — shared evidence boundary and operator attention output; scope exact patch and SHA256 targets above, canonical five-state definition, source-equivalence validator and 60 tests; reader Codex Astra review_standards; disposition APPLIED 8 plan treatments, RESIDUE 3 disclosed (R1–R3), no blocking patch defect. Owner integration/hosted acceptance NOT ADJUDICATED. Any subsequent edit is POST-REVIEW.
