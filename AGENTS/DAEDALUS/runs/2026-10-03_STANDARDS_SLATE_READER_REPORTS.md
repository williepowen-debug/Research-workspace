# Independent reader reports — standards encode and spawn-slate final code

**Reader:** Codex Astra, delegated `review_standards`, 2026-10-03. Independent of the 10/02 authors and original Opus readers. Assignment: catch-up passes 1/2; read only outside this report. No code, registries, ownership state, or external communications changed by this reader. Existing test suite used temporary repositories. Companion synthesis: `AGENTS/DAEDALUS/runs/2026-10-03_CATCHUP.md`; this report preserves the evidence and coverage limits for that synthesis.

## A. SL-6 and ladder A/B — encoded substance PASS, integration residue remains

**Scope actually read:** root/local CLAUDE rules and UPGRADE_PROTOCOL review rule 4/4a/4b; complete `BLUEPRINTS/SPEC_LETTER_STANDARD.md`; local `CLAUDE.md` maturity ladder; primary `PROME/proposals/2026-09-25_wq295-dark-desk-class-PROPOSAL.md` R4 and `2026-09-26_wq-batch-292-296-300-287-257-295-RULED.md`; WQ-354/358 ruled rows in `PROME/WILL_QUEUE.md`; both processed PROME ruling packets dated 9/26 and 10/01; complete `design/2026-10-01_SL6_DISPOSITION_SOURCE_ENCODE.md`; registration checklist row 15; relevant `scripts/maturity_scan.py` scan/floor/gaps implementations.

**Artifact fingerprints read:** SPEC_LETTER_STANDARD sha256 `19a1317e3fb3f708998ee317666237761f6605f6e6175b3ab9272f8f8bee4728`; local CLAUDE sha256 `8c26ecc613126c3fddbae55591e452d11c58cb3095f108da95e2468c7bff9847`. Any edits after this read are POST-REVIEW, except unrelated prose which does not alter the reviewed clauses.

| Tested proposition | Finding at the artifact | Verdict |
|---|---|---|
| Primary R4 letter survives | Names instrument + disposition feed, text-only re-verification is UNVERIFIED for grading, existing >90-day letters reached at next owner boot | PASS |
| Rider overrides proposal test 2 | Both conflicting sources retained, including after adjudication; later publication date alone never governs | PASS |
| WQ-354 adjudicator | PROME names someone other than owner; position or Will-ratified rule conflict goes to Will | PASS |
| WQ-354 recurrence | Every 90 days since last check, not one-shot; absent enumerating instrument explicitly disclosed | PASS |
| Draft overreach removed | No new CONTESTED premise token or blanket disputed-premise gate prohibition imported from withheld draft; unruled gate/lift issues remain declared | PASS |
| WQ-358 A | Proposal route OR explicit flat/frozen re-arm condition OR no-book charter AND demonstrated consumer; frozen/no-condition/no-route fails | PASS |
| WQ-358 B | Current judgment may have any heading; session log fails | PASS |
| Registration consumer | Checklist row 15 links the standard but enumerates only SL-1…SL-5 | RESIDUE A1 |
| Encode record | 10/01 design still begins NOT TRANSPLANTED / standard unchanged and waits on now-partly-answered Q1–Q4 | RESIDUE A2 |

**Reader's own counterexamples, applied manually to the operative text:** a 120-day-old instrument letter has a disposition check 20 days ago: recurring duty does not demand another check merely because registration is old. Two conflicting authoritative sources, newer one declaring in force: date alone cannot settle the conflict, and letter owner cannot name itself final adjudicator. A desk with a frozen trade file, no re-arm condition, a book by charter, and no proposal route fails A. A section titled CURRENT VIEW containing present judgment passes B; a BOTTOM LINE section containing only yesterday's session activity fails B. All results follow the ratified language; none requires inventing a new state token. These are text adjudications, not executions of a grading tool.

**Actionable residues:** A1: update checklist's scope enumeration to include SL-6, preserving forward-only scope and its expressly ruled retrospective reread exception. A2: append a dated current disposition to the historical design record; retain the withheld draft as history. Q1/Q3 were ruled, other gaps remain. `maturity_scan.py:227,279` still uses literal BOTTOM LINE as a conformance flag; `floor_level` does NOT use that flag, so this is not proof that the scanner demotes a conforming alternative heading. Treat it as a structural heuristic pending substantive judgment, not the ruling itself. Do not repair by broadening a regex and claiming it evaluates judgment.

**Limits:** did not re-grade the five desks, repeat the 10/15 review, inspect their full books, verify historical legal-instrument facts externally, or implement an instrument-premise census. Gate-side tokens were not re-audited in this pass; their lack of SL-6 enforcement is declared by the installed standard, not independently certified here. Registration checklist and the stale design banner keep this from being an integration-clean verdict.

REVIEW: required — changes grading and ladder interpretation; scope SPEC_LETTER_STANDARD SL-6/header/form and CLAUDE maturity ladder against primary ruled R4/354/358, plus named immediate consumers; reader Codex Astra review_standards; disposition APPLIED 0 · RESIDUE 2 local continuity/integration items, plus previously declared machine-enforcement limits.

## B. Spawn slate — R11 read completed; whole-tool acceptance is not clean

**Scope actually read:** all 700 lines of `PROME/tools/spawn_slate.py`, all 330 lines of its 37-test suite, complete `ACCEPTANCE_spawn_slate_2026-10-02.md` and DAEDALUS's `design/2026-10-02_SPAWN_SLATE_AND_STAFF_FOR_PROME.md`; Reader A round-2 verdict/residue and Reader B's ledger findings; `spawn_list.py` Liveness implementation; actual boot/closeout wiring in `prome_gate.py:1470–1514`. Exact code sha256 `dbd78561c8764fac9103f2673bea8cfd97e1ca2a208bf9862b96c53769e8b2f6`; original implementation commit `ac9adad26`.

**Counterexample stated for this read:** a gate classified ACTIVE from registration, whose owner last worked in the previous review cycle, must not acquire a false claim of this-cycle activity. Separately, an owner commit arriving after captured HEAD must not affect a slate advertised as reading all evidence at that HEAD. Both cases were exercised in throwaway repositories; results below.

| R11 post-round-2 change | Direct check and result | Disposition |
|---|---|---|
| Gate lookback −6d | Owner commit 3/10 excluded for gate due 3/17 (window starts 3/11); included at 3/16 (window starts 3/10). Counts 0 and 1 respectively | PASS for declared fixed weekly window |
| Dark-this-cycle line | Gate registered 2/1, review 3/20, owner last commit 3/10: stanza prints NO self-commit since 3/14 and says weigh as spawn candidate | PASS in stanza; B1 below |
| Six uncited packets | Eight synthetic owner-carried uncited packets return six names, `(+2 more)`, NO CITING RETURN | PASS; still a hunt, never answers-row verdict |
| Annotation window | Trailing 3/20 stamp includes preceding 'covered by owner return' text; 3/13 stamp is omitted when window opens 3/14 | PASS; bounded excerpt still may omit older annotations |
| Notes-cell timing | Notes-only `Wake after 15:30 ET; before 16:00 ET.` appears in timing output | PASS; regex coverage remains bounded |

**Executable verification:** `PYTHONDONTWRITEBYTECODE=1 python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_spawn_slate.py` → **37/37 PASS** (0.797 s). Independent probes used the suite's throwaway Git fixture, supplemented by direct function probes. No live output file was regenerated and PROME's gate was not run.

### B1 — top-level dark-cycle summary still misstates activity (medium; partial original remedy)

Reproduced output for the gate above:

```text
- **Receipt gap — owner in session since, nothing cites the row:** ... DELTA G:GATE-D-1 (NO CITING RETURN) ...
### DELTA — READ FIRST — spawn_list classes the row ACTIVE (an owner commit since its start date); the row is still open
    - ⚠ the owner has NO self-commit since 2026-03-14 — spawn_list classes the row ACTIVE on an older commit (since the row's start, 2026-02-01); for THIS cycle the owner is dark: weigh it as a spawn candidate
```

The stanza caveat is real and the row is conserved; the top block does not preserve it. PROME's wiring explicitly instructs reading the top block first. This is not a lost row or a return-answers-row classifier, but the broad activity claim persists where attention is allocated. Proposed local remedy for owner: qualify the top receipt-gap label as lack of a citing return, potentially including owners dark this cycle, or surface the cycle-dark distinction without claiming native liveness. This is output wording; do not silently alter inherited spawn_list classes or cap authority.

### B2 — captured-HEAD guarantee does not cover row liveness (medium; reproduced acceptance-14 failure)

`compose` captures `rev` at lines 578–579, then calls `sl.Liveness(until)` at line 580. `spawn_list.Liveness.last_self_commit` runs `git log` without that revision. `Evidence(rev, until)` pins return evidence separately at line 585. A commit landing between them can change row class in this run, contrary to acceptance condition 14.

Independent race probe: intercept the successful `rev-list -1` return, then commit `ALPHA: L2 delivered` in the throwaway repo before allowing compose to continue. Captured/header revision remained `2b1e19c5f`; new owner commit was `115e02b`. The previously DARK ALPHA row became ACTIVE using the new commit, while its pinned precheck printed NO self-commit since the due date and attributed ACTIVE to an older commit. Exact output:

```text
SNAPSHOT_RACE: captured 2b1e19c5f prior 2b1e19c commit after capture 115e02b
### ALPHA — READ FIRST — spawn_list classes the row ACTIVE (an owner commit since its start date); the row is still open
  - `D:L2` [ACTIVE] — due today (Tue 03/10); nothing from the owner cites this row — a receipt gap, an answer that never named the row, or an owner dark this cycle.
    - ⚠ the owner has NO self-commit since 2026-03-10 — spawn_list classes the row ACTIVE on an older commit (since the row's start, 2026-03-10); for THIS cycle the owner is dark: weigh it as a spawn candidate
```

**Fix direction, UNVERIFIED-REMEDY:** PROME should either pin the liveness read to captured revision through a compatible explicit interface or detect and reject an inconsistent generation. Any shared spawn_list interface change needs its existing consumers checked; this read does not authorize or verify that implementation. Add the race fixture and demonstrate failure before/clean behavior after. Working-tree DOCKET/GATES/ROSTER/ORCH_LOG are already disclosed as working-tree sources; B2 concerns committed-history liveness which the acceptance contract says is pinned.

### Wiring and continuity

Actual `prome_gate.py` boot branch calls slate at horizon 0; closeout calls it at horizon 3 on Fri/Sat and 1 otherwise. Both are ADVISE, with pointer-not-grade warning. Thus **WIRED at source**; DAEDALUS design's NOT wired row and acceptance's initial NOT WIRED status are dated historical receipts, not current deployment truth. This pass proves source wiring, not a successful recent full gate run. The tool's `--stdout` behavior and advisory nature do not grant launch authority.

**Where this reader's hypothesis was wrong:** suspected trailing annotation still lost all preceding content; direct probe showed the 14-word lookbehind fixes that example. Suspected gate window might still include prior weekly due day; boundary probe showed it excluded. Retain the original known limitations: six-packet limit can require a hunt, timing regex is incomplete, gate windows assume the declared six-day lookback, and inherited attribution/first-owner limits persist.

**Coverage limits / no overclaim:** this was an independent final-code/R11 review, NOT a slate-alone cold-reader replication, staffing trial, 13-vintage backtest, or full review of all upstream spawn_list consumers. Did not reproduce the previous 20-mutant campaign. The original 37 tests passing do not test the new B2 race. Did not run PROME's full boot or modify its live files. R11 can now say its five changes received an independent read; it cannot say the whole tool is independently clean or that the v2 cold read happened. R1–R10 remain as originally declared, with B1/B2 added.

REVIEW: required — changes evidence interpretation and spawn-attention output; scope spawn_slate.py complete, test_spawn_slate.py complete, acceptance contract, prior round-2 findings, spawn_list.Liveness and prome_gate boot/closeout wiring; reader Codex Astra review_standards; disposition APPLIED 0 · RESIDUE 2 (B1/B2) · UNVERIFIED-REMEDY B2 interface/consumers. Later fixes require explicit POST-REVIEW labeling and bounded verification.

## Pointer map for parent synthesis

| Parent claim | Preserved source here |
|---|---|
| SL-6 and ladder encode substance independently checked | A verdict table and manual counterexamples |
| Why standards integration is not wholly complete | A1/A2 and scanner limitation |
| R11 no longer unread | B five-row results and 37/37 execution receipt |
| Why spawn slate cannot be declared clean | B1/B2 reproductions |
| Slate is now source-wired | Wiring section, actual prome_gate callsites |
| What was not reviewed | Each scope/coverage block above; no missing coverage concealed |

## C. Bounded result read of the parent's continuity edits — PASS

**2026-10-03, subsequent read by the same independent reader.** Scope is precisely the parent's POST-REVIEW changes: `builds/REGISTRATION_CHECKLIST.md` row 15; the new CURRENT DISPOSITION paragraphs in the 10/01 SL-6 encode design and 10/02 spawn-slate design; newest `EVOLUTION.md` entry, 2026-10-03 (a). Read the concrete synthesis at `AGENTS/DAEDALUS/runs/2026-10-03_CATCHUP.md` for companion linkage only, not a new whole-synthesis approval. No new code or standards clause review was performed.

| Edited surface | Final artifact result | Verdict |
|---|---|---|
| Registration checklist row 15 | Now SL-1…SL-6; expressly sends the 90-day existing-letter exception back to the standard instead of creating a second rule | PASS; A1 closed |
| SL-6 design current disposition | Separates encoded current state from historical withheld draft; identifies Q1/Q3 as ruled and preserves remaining semantic/machine gaps; no general contested-premise gate block invented | PASS; A2 closed |
| Spawn-slate design current disposition | Says source-wired, keeps initial NOT wired receipt historical, records completed R11 read and both B1/B2, and disclaims cold-read/staffing-trial certification | PASS; B1/B2 remain open |
| EVOLUTION 10/03 entry | Records late pairing honestly, preserves substantive SL-6/ladder changes and grandfathering, and links review evidence; does not claim a historical same-commit pairing | PASS |

**Counterexample used:** a next-session reader must not read the preserved old NOT TRANSPLANTED/NOT wired banners as current, or treat this continuity pass as closure of B1/B2 or a new gate prohibition. Both new leading disposition paragraphs explicitly prevent those readings. Checklist's generic grandfathering sentence cannot erase the 90-day exception because the same row now names that exception directly.

**Provenance cross-check:** read-only `git show --stat` from repo root confirms `0cc007f28` changed the standard and ladder but did not include EVOLUTION; `43a4c3bc2` changed PROME's gate wiring. These support the two commit pointers in the new banners. The historical pairing defect remains a historical fact.

REVIEW: required — bounded result read of checklist enforcement-scope correction; scope the four edited regions enumerated above; reader Codex Astra review_standards; disposition APPLIED 2 (A1/A2 continuity remedies verified), RESIDUE 0 new continuity defects. Previously declared SL-6 gaps and spawn-slate B1/B2 remain. No code test rerun was needed for these prose-only continuity changes. Any subsequent substantive edit is POST-REVIEW.
