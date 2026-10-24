# L796 counterexample read: closeout gate FOREIGN-PENDING advisory branch

> Saved verbatim by PROME 2026-10-24 14:5x ET from the reader's scratchpad ledger (Opus counterexample reader, DOCKET L796 owed read). Fixture script: `PROME/reports/2026-10-24_L796-counterexample-read_fixtures/ce.py` (ran against disposable repos only). PROME verified ❌1 and ❌2 at the code before recording them: `argus_contract.py` — the advisory branch is guarded by `target is None` while the inventory loop runs on every verify; `load_perimeter()` reads the live `AUDIT_PERIMETER.tsv` and the manifest records no perimeter digest.

Reader: independent counterexample reader (Opus), read-only on the repo. Started 2026-10-24 14:45 EDT (from `date`).
Code read in full: `PROME/tools/argus_contract.py` (1-320), and in `PROME/tools/argus_scope.py`: perimeter 58-108, content ids 155-252, verify_review 405-470, porcelain/commit/evidence 579-676, main 690-780. Also read: `prome_gate.py:1464-1513`, `PROME/state/AUDIT_PERIMETER.tsv`, `PROME/CLOSEOUT.md:70-118`, `PROME/tools/ARGUS_CONTRACT.md`, the acceptance file, and DOCKET L796.
Fixtures: disposable git repos under this scratchpad (`l796/ce.py`). They use the real `AUDIT_PERIMETER.tsv` text and import the repo tools with `sc.ROOT` patched. No repo file, index or pycache was written (`python3 -B`).
I did not re-run the author's suites (AC5). That is the author's evidence, not mine.

## Ledger (claim → artifact → command → observed → proposed change)

### ❌1. The race moves to step 10. Foreign post-freeze PENDING arrivals still block the push gate, so the fix does not converge with a live fleet.
- **Claim (VERIFIED):** The advisory branch runs only when `target is None` (`argus_contract.py:273`). The working-tree inventory loop (`:224`, `:257-276`) runs on every verify, including `--verify-review --ref <A> --paths …`. That is CLOSEOUT step 10 (`CLOSEOUT.md` step 10 block), and its rc 0 is the precondition for `safe-push`. So any foreign file that arrives after the freeze still returns rc 1 `UNCLASSIFIED` at step 10. The fix only moved the failure from before the commit (step 9) to after the local commit and before the push. Three texts say otherwise:
  - AC4: "foreign pending files are not in the commit and never were checked there" (acceptance `:9`/`:18`).
  - DOCKET L796: "The commit-level control … is unaffected: foreign pending files are not in PROME's commit".
  - `CLOSEOUT.md:86`: "the delivery commit is still verified by its actual paths at step 10".
  `ARGUS_CONTRACT.md:31` itself says the `--ref` verifier "also checks … full inventory".
- **Artifact:** `PROME/tools/argus_contract.py:224,257-276,273`; `PROME/CLOSEOUT.md:86` and step 10; acceptance AC4.
- **Command:** `python3 -B l796/ce.py`, cases CE1 and CE9. Freeze `PROME/result`. A foreign desk writes `AGENTS/REGINALD/decks/img1.png`. Run the working-tree verify, commit the delivery, then run `verify_review(ref=A, paths=['PROME/result'])`.
- **Observed:** Working tree: `(0, ['FOREIGN-PENDING (advisory): AGENTS/REGINALD/decks/img1.png …'])`. Step 10: `(1, ['UNCLASSIFIED: AGENTS/REGINALD/decks/img1.png (new or changed observed version)'])`. CE9: a second arrival between the gate and step 10 gives two `UNCLASSIFIED` lines. The six-round `--observe` loop the row describes is reproduced one step later.
- **Proposed change:** Write the acceptance first (WQ-229). Then decide with Will whether his 12:34 ET word covers the push-gate verify; extending the rule there changes the push control's meaning. A candidate rule for the `--ref` form: a path that is PENDING-only (no commit in `baseline..target`, not in the actual commit paths) gets the same `foreign_pending` test and is advisory. History paths (`:286-296`) and actual commit paths (`:283-284`) stay strict. Until then, correct AC4, the DOCKET cell and `CLOSEOUT.md:86` to say that step 10 still needs `--observe` for post-freeze foreign arrivals. L796 is not RESOLVED while its stated defect ("never converged") persists at the push gate.

### ❌2. A pending perimeter edit makes OWNED arrivals advisory, including the perimeter file itself. This defeats AC2.
- **Claim (VERIFIED):** `foreign_pending` classifies with `sc.load_perimeter()` (`argus_contract.py:246`). That reads the LIVE working-tree `PROME/state/AUDIT_PERIMETER.tsv` (`argus_scope.py:60`). The perimeter is never pinned at the freeze: the manifest records no perimeter digest (`argus_contract.py:166-170`). The rules are first-match (`argus_scope.py:103-108`). So a post-freeze edit that adds a more specific EXCLUDED/SHARED row above `PROME/**` turns OWNED arrivals advisory with rc 0, and the perimeter file can exempt itself. Before this fix, every pending arrival was `UNCLASSIFIED` regardless of the perimeter, so this hole is new. The edit is a realistic one: PROME adds perimeter rows at closeouts (the rows dated 2026-10-02 and 2026-10-22 in the TSV are ARGUS-⚠️ follow-ups). This is the same failure as memory finding 12 under `finding_instrument_reports_clean_against_the_wrong_reference`: an instrument that reads a file to derive its own perimeter never measures that file.
- **Artifact:** `PROME/tools/argus_contract.py:245-256`; `PROME/tools/argus_scope.py:58-108`; `PROME/state/AUDIT_PERIMETER.tsv:28` (`PROME/** OWNED`).
- **Command:** CE8b in `l796/ce.py`. Deliver `PROME/state/GATES.tsv` and `PROME/state/DOCKET.tsv`, then freeze. Add rows `PROME/state/AUDIT_PERIMETER.tsv EXCLUDED` and `PROME/state/HANDOFF_X.md EXCLUDED` directly under the header. Write `PROME/state/HANDOFF_X.md`, then run the working-tree verify.
- **Observed:** `(0, ['FOREIGN-PENDING (advisory): PROME/state/AUDIT_PERIMETER.tsv …', 'FOREIGN-PENDING (advisory): PROME/state/HANDOFF_X.md …', 'contract … unchanged; verdict FROZEN …'])`. Both paths are OWNED under the frozen-time perimeter, and the gate line passes. Control case CE8 (an edit that does not cover the perimeter file) still blocks: `UNCLASSIFIED: PROME/state/AUDIT_PERIMETER.tsv`. Mitigation (INFERRED from `:273` and `:283-284`): if PROME commits either path, step 10 still rejects it as `UNREVIEWED ACTUAL COMMIT PATH`. So the defect weakens the pre-commit gate; it does not ship bytes by itself.
- **Proposed change:** Pin the perimeter at the freeze: record `sha256(AUDIT_PERIMETER.tsv)` in the manifest outside the contract, as `attributed_by_commit` is. In `verify()`, set `rules = None` (strict) whenever the live perimeter digest differs from the pinned one or the perimeter path is in the inventory. Hard-code `PERIMETER_FILE` as never-advisory. Add CE8b as a regression test.

### ⚠️3. Wrong owner: PROME's own post-freeze writes in SHARED, EXCLUDED and UNATTRIBUTED lanes pass as "another owner's live file".
- **Claim (behaviour VERIFIED; consequence INFERRED):** For a never-committed path, "PROME-evidenced" reduces to the three filename forms (`from-PROME`, `via-PROME`, `MSG-PROME`; `argus_scope.py:630-648`), because commit-subject evidence needs a commit. PROME's real writes outside those forms are therefore advisory, with text that asserts foreign ownership. Examples:
  - root `CLAUDE.md`, which is SHARED by the first matching row (`AUDIT_PERIMETER.tsv:19`);
  - an `memory/auto/` lesson;
  - an inbox data body, the 888924d2e class named in TSV row 18;
  - a `PROME/inbox/processed/` consume-move (EXCLUDED, `:16`);
  - a stray root file (UNATTRIBUTED; A4 says "never dropped", and here it is listed but downgraded);
  - CE4 overlap: PROME extending a desk-committed `memory/auto/` file after the freeze.
  None of these ships unseen. A PROME commit of them fails step 10 (`:283-284`), and a separate PROME-subject commit gains evidence and blocks at the gate. The residue is an uncommitted PROME write that passes the gate labelled as someone else's. Root step 1b's orphan check runs at CLOSEOUT step 6, before the freeze, so it cannot see a post-freeze write. The ruling text ("not OWNED, not PROME-evidenced") is met by letter.
- **Artifact:** `argus_contract.py:250-256,274`; `argus_scope.py:630-648`; `AUDIT_PERIMETER.tsv:16,18,19,31`.
- **Command:** CE2 and CE4 in `l796/ce.py`.
- **Observed:** CE2 rc 0, with five `FOREIGN-PENDING (advisory) … another owner's live file` lines: the FALCON inbox csv, `CLAUDE.md`, `NEWROOTFILE.md`, `PROME/inbox/processed/…`, and `memory/auto/finding_prome_new_lesson.md`. CE4 rc 0, with `memory/auto/finding_desk.md` advisory.
- **Proposed change:** Reword the line to state what was established: `FOREIGN-PENDING (advisory, owner UNVERIFIED — <class> lane, no PROME evidence)`, using `classify()`'s class. Consider keeping UNATTRIBUTED blocking (A4) and root `CLAUDE.md` blocking, since it is Will-gated. Record the rest as declared residue in the acceptance.

### ⚠️4. Fail-closed over-block: routine desk handling of PROME packets still blocks, so convergence is partial.
- **Claim (VERIFIED):** A desk that consumes a PROME packet during the window (`git mv` to `processed/`) blocks the gate in two ways. The delivered origin becomes `CHANGED-SINCE-REVIEW`, and the `from-PROME` destination carries evidence and gets `UNCLASSIFIED`. A desk-written `via-PROME` relay also blocks; `argus_scope.py:641` notes that 4 of those are desk-written. This is the safe direction and matches AC2/AC3 by letter. Still, PROME filed about 30 `from-PROME` packets from 10/21 to 10/24 (`git log` scan), so this is common live-fleet traffic that keeps the race alive.
- **Artifact:** `argus_contract.py:229-232,256`; `argus_scope.py:637-645`.
- **Command:** CE3 and CE3b in `l796/ce.py`.
- **Observed:** CE3 rc 1: `CHANGED-SINCE-REVIEW: delivered AGENTS/CARL/inbox/2026-10-24_from-PROME_gap.md` and `UNCLASSIFIED: AGENTS/CARL/inbox/processed/…`. CE3b rc 1: `UNCLASSIFIED: AGENTS/WALTER/inbox/2026-10-24_relay_via-PROME_note.md`.
- **Proposed change:** No code change is needed for safety. Declare it as residue in the acceptance file so the next "it never converges" report is not read as a regression.

### ⚠️5. The scope of the change is wider than "the gate's manifest line": `--mark-reviewed` now promotes over foreign arrivals.
- **Claim (VERIFIED):** The branch lives in `verify()`, so `mark_reviewed()` (`argus_scope.py:213`, a working-tree verify) now promotes FROZEN to REVIEWED when there are post-freeze foreign arrivals. Before the fix it refused. This is not unsafe: REVIEWED binds the contract digest (`:224`), and `argus_contract.py:299-301` says "unrelated content not certified". But `CLOSEOUT.md:86` and the acceptance describe only the gate line.
- **Artifact:** `argus_scope.py:206-227`; `argus_contract.py:244-276`.
- **Command:** CE6 in `l796/ce.py`.
- **Observed:** `mark_reviewed: (0, 'verdict REVIEWED over 1 path(s)')` with `AGENTS/BROCK/new.md` arriving after the freeze.
- **Proposed change:** Name the `--mark-reviewed` effect in the acceptance's neighbours/residue and in `CLOSEOUT.md:86`.

### ⚠️6. No unit test exercises the FOREIGN-PENDING branch.
- **Claim (VERIFIED):** The `test_argus_contract.py` fixture writes no `AUDIT_PERIMETER.tsv`, so `load_perimeter()` raises `SystemExit`, `rules = None` (`argus_contract.py:248-249`), and every test runs the strict path. A grep of the test `.py` files for `FOREIGN` returns no hits on the advisory branch. AC1–AC3 were live-tree probes only (acceptance `:15-17`). AC5 being "green" therefore says nothing about the new branch.
- **Artifact:** `PROME/tools/tests/test_argus_contract.py:18-36`; `argus_contract.py:245-249`.
- **Command:** `grep -rn "FOREIGN\|foreign" PROME/tools/tests/*.py`. It only matches pre-existing fixtures that use `foreign` as a path name.
- **Observed:** Zero tests reach `:273` with `rules` loaded.
- **Proposed change:** Port CE1, CE2, CE5, CE7, CE8 and CE8b into `test_argus_contract.py` with the real perimeter copied in. This is the WQ-229 "reusable test" for a defect that has recurred.

### ⚠️7. `ARGUS_CONTRACT.md` was not updated for the new rule.
- **Claim (VERIFIED):** `ARGUS_CONTRACT.md:29` still says "If proven unrelated work arrives or changes … No blanket exclusions; ambiguous arrivals fail." The working-tree gate now does the opposite for foreign pending arrivals. CLOSEOUT step 8 tells concurrent closeouts to follow `ARGUS_CONTRACT.md` first, so the two procedure texts disagree.
- **Artifact:** `PROME/tools/ARGUS_CONTRACT.md:29`; `PROME/CLOSEOUT.md:86`.
- **Command:** `grep -n "ambiguous arrivals fail" PROME/tools/ARGUS_CONTRACT.md`
- **Observed:** Line 29 is unchanged.
- **Proposed change:** After ❌1 is decided, add one sentence to `ARGUS_CONTRACT.md:29` pointing to the CLOSEOUT:86 rule and stating its scope (working tree only, or both forms).

### ✅8. A rename out of the OWNED lane still blocks.
- **Claim (VERIFIED):** `porcelain_entries` synthesizes the origin `" D"` for a staged rename (`argus_scope.py:579-596`). An OWNED origin is not foreign, so it is `UNCLASSIFIED`.
- **Command:** CE5, a staged `git mv PROME/old AGENTS/ZED/old` after the freeze.
- **Observed:** rc 1, `UNCLASSIFIED: PROME/old`. The destination is advisory.
- **Proposed change:** None.

### ✅9. Missing information: an unreadable or malformed perimeter falls back to strict.
- **Claim (VERIFIED):** A `SystemExit` from `load_perimeter` sets `rules = None`, so `foreign_pending` returns False (`argus_contract.py:248-251`).
- **Command:** CE7, a perimeter with an invalid class after the freeze.
- **Observed:** rc 1, `UNCLASSIFIED: AGENTS/BROCK/new.md` and `UNCLASSIFIED: PROME/state/AUDIT_PERIMETER.tsv`.
- **Proposed change:** None.

### ✅10. Delivered-content change still blocks, including when a foreign hand causes it.
- **Claim (VERIFIED):** `argus_contract.py:229-232` runs before the inventory loop and is independent of `foreign_pending`.
- **Command:** CE3, where a desk `git mv`s a delivered packet.
- **Observed:** `CHANGED-SINCE-REVIEW: delivered AGENTS/CARL/inbox/…`
- **Proposed change:** None.

### ✅11. Freeze stays strict when an arrival lands inside `freeze()`.
- **Claim (INFERRED, by reading the code):** `freeze()` enforces `set(seen) <= required` at `argus_contract.py:164` before calling `verify()` at `:171`. An arrival between `:136` and `:171` becomes advisory, which is the same thing as a post-freeze arrival. No pre-freeze path escapes classification.
- **Command:** Code read only.
- **Proposed change:** None.

## Neighbour categories (WQ-229)
- **Ordinary:** CE1 (advisory at the gate as designed, still blocks at step 10, ❌1) and CE6 (⚠️5).
- **Overlap:** CE4 (a desk-committed SHARED path with a PROME pending edit is advisory, ⚠️3) and CE3 (a delivered packet consumed by a desk blocks, ✅10/⚠️4). The case of a committed and pending path with PROME commit evidence is safe by code: `:255-256` passes the commits into the evidence check.
- **Wrong owner:** CE2 (⚠️3) and CE8b (❌2).
- **Missing information:** CE7 (✅9) and stale observed records (accepted by the acceptance neighbour line `:11`; ⚠️7 covers the procedure text).
- **Concurrent activity:** CE9 (arrivals between the gate and step 10, ❌1) and the arrival inside `freeze()` (✅11). A file that changes between porcelain and hashing inside a single `inventory()` call was not constructed; it is UNKNOWN, low consequence, because both values come from one read.

## Verdict
NOT RESOLVED — ❌1 (the race reappears at step 10 / the push gate, and AC4, `CLOSEOUT.md:86` and the DOCKET cell say otherwise) · ❌2 (an unpinned live perimeter lets a pending perimeter edit downgrade OWNED arrivals, including the perimeter itself, to advisory with rc 0).
