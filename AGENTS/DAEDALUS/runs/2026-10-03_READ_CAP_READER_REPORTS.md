# Independent read-cap review — L530 / L538

2026-10-03 · Reviewer: Codex review_readcap, separate from implementing parent. Scope: root `scripts/read_cap_check.py`, October 2 build record, DOCKET physical rows 530/538, READ_CAP and CHECK_STANDARD. No production or other desk files edited by this reader. Initial reviewed source SHA256: `d7fb97019fd6157d47cd540ce1a1af98d96604a7a235401e71bbdd6e5b914a47`.

## Initial verdict: repair required

The October 2 implementation cannot be accepted as reviewed complete. Independent frozen tests found seven L530 failures and two L538 boundary failures. The existing selftest still passed 112/112, confirming its known heuristic coverage gap. New independent suite: `tests/test_read_cap_catchup_20261003.py`; initial result **16/25 pass, 9 fail**, rc 1. Its capable and quiet check_agent outputs both passed, including an inherited second path above 54,250 B producing `OVER THE CAP` and rc 1.

| Finding | Independently constructed counterexample | Observed failure |
|---|---|---|
| L530 parent negation lost | `Do not read these:` then `1. A.md`; also `Never read these:` | A is counted whole; parent check starts at the read verb, dropping preceding negation |
| L530 leading condition lost | `On demand, read these:` then `1. A.md` | A counted whole |
| L530 parent scope lost | `Read only the headers:` then `1. A.md` | A counted whole rather than scoped |
| L530 sibling omission | `Read these in order:` then `1. A.md`, `2. B.md` | Only A found; the immediate preceding item has no literal read verb |
| L530 long enumeration omission | Explicit parent followed by a child with 184 characters of context before A + B | Both omitted because inherited verb at position 0 still faces the 160-character ceiling |
| L530 unrelated sibling inheritance | `1. Read A.md.` then `2. B.md is the write destination.` | B counted whole without a parent/list relationship |
| L538 malformed mode suppressed | External concrete row, `mode=bogus` | EXTERNAL skips the mode vocabulary defect |
| L538 traversal suppressed | `RESEARCH-INTAKE/../AGENTS/X/B.md` | A local target is silently classified EXTERNAL |

Quiet/boundary controls that passed: no read verb; write parent; child write; child on-demand; parent on-demand after verb; nearest unrelated intervening line; heading boundary; one initial blank; blank after active item; own command reset; ordinary two paths; exact external concrete/glob; prefix lookalike and embedded local `RESEARCH-INTAKE` remain local.

## Real production cases, checked read-only

- **CARL `CLAUDE.md:79`**: `boot.py prints upcoming catalysts from docket/CATALYSTS.tsv` describes a bounded tool output, not whole-file ingestion. The October 2 heuristic nevertheless adds `docket/CATALYSTS.tsv` as whole via neighboring read-verb inheritance. This was listed as a beneficial gain in the build report; it is a real false-positive case.
- **TERRY `CLAUDE.md:156`**: requires `POSITION_INTAKE.md` fields for existing-position triage. The heuristic inherits a neighboring read verb and counts the entire file. This is the same false-positive class.
- **BRENT production acceptance**: boot heuristic includes STATUS and excludes `board_log.tsv`, preserving the original documented read-versus-log distinction. Live STATUS bytes are not frozen at the old docstring's 74,061 B; the historical exact figure is not reasserted.
- **CREED `CLAUDE.md:94`**: original mixed long line still carries a later `read` noun, so `if not reads` does not inherit the parent and the early threshold paths stay absent from the heuristic. CREED's own manifest supersedes it and covers THRESHOLDS; declaration is the effective remedy for this real shape, not proof the heuristic class was fully repaired.
- **HANS**: boot heuristic still discovers only STATUS; THRESHOLDS is outside its charter boot section. This is declaration work, not solvable by line inheritance.
- **WALTER live CLI**: external glob `RESEARCH-INTAKE/data/*/news.json` is visibly EXTERNAL, no manifest defects, rc 1 from **HANS** `registry/THRESHOLDS.tsv` at **33,544 B**. The build record's wording that the remaining rc is WALTER's own file is inaccurate for this run. No demand for rc 0 is appropriate while a real declared read exceeds budget.

## Remedy reviewed before production change

Accept a narrow explicit-list parser, not free nearest-line inheritance:

1. Open inherited context only from a read-bearing, file-token-free explicit colon introducer. Retain the entire parent for negation, on-demand and scope classification, including text before the verb.
2. Inherit across same-indent sibling items. Permit one blank between parent and first item; terminate after an active-list blank, unrelated prose, heading, changed indentation, or an item's own read/write command. A child with its own read verb uses its own command.
3. An inherited enumeration has no artificial 160-character distance from an invented position-zero verb. Continue checking each token for local write/scope/on-demand qualifiers.
4. Validate mode before external exemption. Reject parent traversal inside an external-root declaration; do not broaden recognized external roots or silently turn arbitrary local spellings into exemptions.
5. Preserve ordinary reader-perimeter semantics and stable output/exit contracts. The legacy heuristic remains explicitly partial; declaration is authoritative.

The proposed remedy was sent to the implementing parent before any repair, along with the independent fixture. This reader does not claim final acceptance until the final source and live before/after diff are re-read.

## Consumer and acceptance boundaries

Read-only consumer survey: `scripts/validate_all.py` parses the stable `READ-CAP-RESULT v1` reason line; DAEDALUS `daedalus_gate.py` maps the three rc states; TERRY `scripts/boot.py` parses displayed size rows; SAM/BOND/HANS closeout scripts invoke the CLI. WALTER `signal_read_check.py` and PROME `reads_check.py` import constants. A parser/perimeter repair can retain these contracts unchanged; a changed output/rc contract would require a coordinated consumer batch.

**L530 docket discrepancy remains explicit:** physical row 530 requires reads declared whole by *any* reader to be measured for the *owner*. Current `check_agent(owner)` grades the owner's own declaration only. READS.tsv ruling 1 and READ_CAP rule 15 instead assign the cross-agent read to the **reader's perimeter**, with remedy owned by the source owner. Do not silently reassign the perimeter, or claim this acceptance sentence is implemented. Reconcile the request as owner-directed visibility/remedy, or keep that condition open with PROME.

Tests prove these enumerated parser boundaries only. They do not certify arbitrary Markdown/natural language, declaration completeness, external repository bytes, actual agent consumption, or all boot.py internal reads. PROME and WALTER were active; their files were read but not changed.

## Final verification after parent repair

Final reviewed source SHA256: `ff77e3136e36ce474bc5338092afc2b422a32db8bf4d3e14a51ac6720d4e4c03`. Re-read the complete changed inheritance and external-validation branches. **Bounded code repair ACCEPTED**; the unresolved L530 owner/reader acceptance sentence above remains open.

- Re-ran the original 25 independent tests after production change: **25/25 pass**.
- Added four fresh cases after reading the fix: changed indentation terminates inherited scope; a scoped first child does not contaminate the next sibling; an inherited scoped over-cap file remains in the visible scoped-overcap record; malformed external-glob mode still produces a defect. Expanded independent suite: **29/29 pass**, rc 0. These are new reviewer tests, not self-reported author fixtures.
- Existing producer suite: **112/112**, rc 0. The parser suite remains a separate test file; do not imply those 112 now cover the heuristic.
- Original capable/quiet fixture still observes clean `READ-CAP 0 [X]` for two small inherited paths, then `OVER THE CAP` and rc 1 when only the second file grows above the cap. Production fixtures remain untouched.
- L538 concrete and glob external rows stay visible and ungraded; typo modes and parent traversal now produce defects; local prefix lookalikes remain graded. No external-root set widening occurred.

### Live before/after perimeter comparison

Compared all **38** desk heuristic results to the pre-change snapshot, then separately compared actual `check_agent` results using both source versions on the same live files. These are read-only observations at review time, not immutable fleet inventories.

| Surface | Heuristic change | Assessment from the actual charter |
|---|---|---|
| WALTER `design/CLUSTER_TAXONOMY.md` | Removed whole row | Dispatch/archive-time field validation, not a boot whole-read mandate |
| RED `thesis/CHANGELOG.md` | Whole row removed; scoped-overcap row retained from boot line 51 | Boot reads last 2–3 entries; former whole attribution was a write-back step |
| RED `OUTBOX.md` | Removed whole row | Write-back routing target |
| CARL `docket/CATALYSTS.tsv` | Removed whole row | boot.py computes countdown output |
| TERRY `POSITION_INTAKE.md` | Removed whole row | Field requirement for position triage, not whole-file boot instruction |
| CREED `thesis/THESIS.md` | Removed whole row | **Residual real heuristic miss** in a complex parent list; CREED's attested manifest still counts THESIS and THRESHOLDS correctly |

Zero whole rows added. Scoped-overcap entries incidentally inherited in inbox-processing contexts disappeared for BRENT, HENRY, LABOR, CORAL and OZK; RED's cross-reference trigger-registry entry disappeared. Those changes do not turn whole reads into clean readings; they remove incidental partial references from the heuristic.

Actual production `check_agent` outputs changed at **three** desks: CARL 9→8 measured reads, TERRY 8→7, and BRENT retained the same five files with TRADE's attribution corrected from line 54 to its actual read at line 26. **No desk's rc changed.** Manifest precedence protected WALTER/RED/CREED from heuristic-only changes. CREED attestation and THESIS/THRESHOLDS membership were directly verified.

WALTER still prints external news.json as EXTERNAL, `manifest_defects=0`, `rc=1`, `over_budget=1` from HANS THRESHOLDS. BRENT's real STATUS remains included and its write-only board_log remains excluded (STATUS currently 24,163 B, so the docstring's old 74,061 B capable case is historical, not a current capable production input).

### Compatibility and explicit residue

No constants, rc vocabulary, `READ-CAP-RESULT v1` keys, row-size display format or public return shapes changed. The examined consumers therefore need no protocol migration for this repair. Actual production comparison above confirms no unexpected rc transition; that is not a claim every consumer was executed.

The explicit-list implementation intentionally does not interpret arbitrary Markdown nesting or prose. In particular, a child carrying its own read command resets inherited context; mixed whole/scoped files on a single prose line still use local marker windows and can be ambiguous. The CREED long-line shape remains a real demonstration of that limitation. This is acceptable **only with the existing explicitly partial heuristic perimeter and declaration precedence**, not as evidence that L530's every-path or owner-projection acceptance conditions have all been discharged.

Completion delivered to the parent with source hash, tests, live scope changes and unresolved registrar condition. No production changes or external messages were made by this reviewer.
