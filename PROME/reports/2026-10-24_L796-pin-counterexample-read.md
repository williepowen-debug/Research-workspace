# L796 ❌2 repair — independent counterexample read #1 (perimeter pin)

> Saved verbatim by PROME 2026-10-24 18:1x ET from the reader's scratchpad ledger (Opus, general-purpose, read-only, disposable repos). Spawn: ORCH_LOG 2026-10-24 L796-PIN-READER touch 1. Fixtures: `PROME/reports/2026-10-24_L796-pin-counterexample-read_fixtures/` (ce.py · ac_check.py · old_check.py and their run outputs; scratch paths inside are session-scoped and dead). Verdict NOT RESOLVED at this read; the ❌1/❌2 fixes that followed are recorded in `PROME/tools/tests/ACCEPTANCE_closeout_gate_perimeter_pin_2026-10-24.md` § Results.

---

# L796 ❌2 repair (perimeter pinned at the freeze): independent counterexample read

Reader: independent counterexample reader (Opus). Read-only on the repo. Started Sat 2026-10-24 18:06 EDT (from `date`).

**What I read:**
- the acceptance file `PROME/tools/tests/ACCEPTANCE_closeout_gate_perimeter_pin_2026-10-24.md`;
- the whole uncommitted diff (4 files);
- `PROME/tools/argus_contract.py` in full;
- `argus_scope.py` lines 36-120, 120-240, 395-560, 570-800;
- the prior ledger `PROME/reports/2026-10-24_L796-counterexample-read.md` and its `ce.py`;
- the new `PerimeterPinTests`.

**Fixtures:** all disposable repos live under this directory (`repos/`), built by the scripts here:
- `ce.py`: my counterexamples;
- `ac_check.py`: my own AC1–AC8 checks, plus the pre-fix counterfactual against `HEAD:PROME/tools/argus_contract.py`, copied to `old/`;
- `old_check.py`: confirms pre-existence at HEAD.

Each fixture commits the REAL `AUDIT_PERIMETER.tsv` and the real root `.gitignore`, then patches `sc.ROOT`. I used `python3 -B` throughout.

**Raw output:** `run1.txt`, `run_ac.txt`, `run_old.txt`.

**Repo state:** I wrote nothing to the repo. `git status` was compared before and after the suite run. The only difference was a concurrent NEXUS session staging its own `AGENTS/NEXUS/**` files, which is not my write. I never called `--record-review`, `--freeze`, `--mark-reviewed` or `--record-baseline` against the real repo. The read-only `--verify-review` against the real repo returned `CANNOT-EVALUATE: contract belongs to a different baseline`: the live manifest is from a prior closeout, so the pin change has no live effect right now.

---

## ❌ findings

### ❌1. The committed side lets the perimeter exempt itself at the freeze, and the pin then carries rules nobody reviewed. The belt-and-braces hard-code exists only on the pending side.
- **Claim (VERIFIED):**
  - **Where the hard-code is missing:** `foreign_pending` hard-codes `path == sc.PERIMETER_FILE` as never-advisory (`argus_contract.py:285`). `attributed_by_commit` has no such guard (`:116-126`).
  - **The case:** before the freeze, a commit whose subject does not start with `PROME` changes `PROME/state/AUDIT_PERIMETER.tsv` and adds a row that classifies the perimeter file as non-OWNED.
  - **Why the freeze accepts it:** `freeze()` pins the working-tree rules (`:182`) and passes them to `attributed_by_commit` (`:183`). Those rules call the perimeter SHARED, so the path counts as committed-only, non-OWNED and unevidenced, and is auto-attributed. The freeze succeeds without the perimeter being delivered or observed.
  - **What follows:** every later verify classifies with these unreviewed rules. A post-freeze write that is OWNED under the baseline perimeter (`PROME/state/HANDOFF_X.md`) is then `FOREIGN-PENDING (advisory …)` with rc 0.
  - **Why this is ❌2's class:** this is the committed form of the 12th `finding_instrument_reports_clean_against_the_wrong_reference` instance (the instrument derives its perimeter from a file it never measures). The acceptance puts "the committed side has the same shape" in scope, and AC4 covers only a post-freeze flip.
  - **Not introduced by this diff:** it exists at HEAD with the live read (`old_check.py`, C1 at HEAD code: same `auto=['PROME/state/AUDIT_PERIMETER.tsv']`, rc 0). But the repair now presents the pin as the trusted reference, and this is the path by which an unreviewed perimeter becomes the pin.
  - **Sibling, CE-O (⚠️ grade on its own):** the freeze plan may declare a PENDING perimeter edit as `observed`. `observation()` checks owner ≠ PROME and a quote, never the lane. Freeze then pins the observed and unreviewed rules: rc 0, HANDOFF_X advisory.
  - **Preconditions:** a non-PROME-subject commit to a PROME file whose content reclassifies the perimeter file. Unlikely, but it is the same self-exempting shape as CE8b, which was graded ❌.
- **Artifact:** `PROME/tools/argus_contract.py:116-126` (no `PERIMETER_FILE` guard), `:182-185` (pin taken and used before any check of how the perimeter itself was classified), `:285` (the pending-side guard only).
- **Command:** `python3 -B ce.py "CE-C1"` and `python3 -B ce.py "CE-O"`. Control: `CE-C1 control PROME subject`.
- **Observed:**
  - CE-C1: `freeze OK; attributed_by_commit keys: ['PROME/state/AUDIT_PERIMETER.tsv']`, `perimeter delivered? False; observed? False`, `pinned class of perimeter file: ('SHARED', 'x')`, then gate `(0, ['FOREIGN-PENDING (advisory, owner UNVERIFIED — EXCLUDED lane, no PROME evidence): PROME/state/HANDOFF_X.md', …])`.
  - Control: the same commit with a `PROME:` subject gives freeze `ValueError: unclassified inventory … PROME/state/AUDIT_PERIMETER.tsv`, which is the correct block.
  - CE-O: freeze OK, the pinned rules contain the HANDOFF row, gate rc 0 with HANDOFF_X advisory.
- **Proposed change:**
  1. In `attributed_by_commit`, `continue` when `p == sc.PERIMETER_FILE`. This mirrors `:285`.
  2. In `freeze()`, `require(sc.PERIMETER_FILE not in seen or sc.PERIMETER_FILE in delivered, 'perimeter changed since baseline: deliver it (it becomes the pin)')`. Whatever is pinned is then either the baseline perimeter or a delivered version that ARGUS reviews; it is never auto-attributed or observed.
  3. Add CE-C1 and CE-O as tests.

### ❌2. A post-freeze edit of root `.gitignore` hides an OWNED arrival from the inventory, and the `.gitignore` edit is itself advisory. Same class as CE8b; the pin does not cover it.
- **Claim (VERIFIED):**
  - **Mechanism:** the inventory is `git status --porcelain -z -uall` (`argus_scope.py:579-582`), which honours ignore rules. Root `.gitignore` matches no perimeter row, so it is UNATTRIBUTED and goes to the advisory branch.
  - **The case:** after the freeze, appending `PROME/state/HANDOFF_X.md` to `.gitignore` and writing that file makes the OWNED file vanish from the inventory. The only trace is `FOREIGN-PENDING (advisory, owner UNVERIFIED — UNATTRIBUTED lane …): .gitignore` with rc 0.
  - **Why this is the same class as ❌2:** the instrument derives its perimeter, here the set of paths it sees, from a file whose own post-freeze edit it downgrades to advisory. The repair hard-codes only `PERIMETER_FILE` (`argus_contract.py:285`).
  - **Pre-existing:** same result at HEAD (`old_check.py`, G1 at HEAD code rc 0). The hole was opened by the 10/22 advisory branch, not by this diff.
  - **Consequence (bounded, VERIFIED):** `git add` of the ignored file fails (`git add rc 1: The following paths are ignored …`). A PROME commit of `.gitignore` or of a force-added file fails step 10 as `UNREVIEWED ACTUAL COMMIT PATH`. So this weakens the pre-commit gate (the same mitigation as CE8b) and does not ship bytes on its own.
  - **Related, no trace at all (⚠️, pre-existing, no advisory involved):** a new self-ignoring nested `PROME/state/scratch/.gitignore` (`*`) plus a file beside it leaves nothing in porcelain: rc 0 and no line. This is an inventory-design limit that predates 10/22. `.git/info/exclude` has the same effect from outside the tree (INFERRED, not constructed).
- **Artifact:** `PROME/tools/argus_contract.py:282-291`, `:308-310`; `PROME/tools/argus_scope.py:579-582`; `PROME/state/AUDIT_PERIMETER.tsv` (no row for `.gitignore`, so it is UNATTRIBUTED).
- **Command:** `python3 -B ce.py "CE-G1"` and `python3 -B ce.py "CE-G2"`; `python3 -B old_check.py`.
- **Observed:**
  - CE-G1: porcelain `'M .gitignore\n?? PROME/result\n…'` with no HANDOFF_X. Gate `(0, ['FOREIGN-PENDING (advisory, owner UNVERIFIED — UNATTRIBUTED lane, no PROME evidence): .gitignore', 'contract … unchanged; verdict FROZEN; …'])`.
  - CE-G2: gate `(0, ['contract … unchanged …; 1 inventory paths retained …'])`.
- **Proposed change:** treat any path whose basename is `.gitignore` (and arguably `.gitattributes`) as never-advisory, in the same `foreign_pending` guard as `PERIMETER_FILE`. A post-freeze ignore-rule change then blocks with `UNCLASSIFIED`. Alternatively, declare it in the acceptance's residue with the consequence bound above. The nested self-ignoring case cannot be seen through porcelain at all; if it matters, the inventory would also need `git status --ignored` restricted to the OWNED lane. Register that rather than fix it here.

---

## ⚠️ findings

### ⚠️3. The pinned digest is never checked against anything, and the pin is the one manifest field verify trusts without re-deriving it.
- **Claim (VERIFIED):**
  - **What validate checks:** only the digest's format (`argus_contract.py:225`). It accepts `sha256: null` with rules present, and any 64-hex value with untouched rules. Nothing compares the digest to the rules or to any file.
  - **Why the pin is unlike the other fields:** `observed` records are re-proved against their committed evidence quote (`:235-237`, `:304-305`), and `attributed_by_commit` is recomputed at every verify (`:273`). The pin is used as written, and REVIEWED binds only `reviewed_contract_sha256`, not the pin.
  - **Effect:** a hand edit of `perimeter.rules` (e.g. inserting `PROME/state/HANDOFF_X.md EXCLUDED`), with the digest left stale, passes validate and verify with rc 0. A valid-shape pattern with a trailing space (`'PROME/** '`) also validates. It silently matches nothing.
  - **Why this is only ⚠️:** manifest tampering is outside the defect's threat model (`contract_sha256` can be recomputed by an editor too).
  - **The acceptance overclaims:** AC5b says "bad digest ⇒ CANNOT-EVALUATE", but only a malformed digest string is caught.
- **Artifact:** `PROME/tools/argus_contract.py:223-229`, `:142-147`; acceptance AC5b and its Design bullet ("bad digest").
- **Command:** `python3 -B ce.py "CE-T1"`, `"CE-T2"`, `"CE-V"`.
- **Observed:**
  - CE-T1: `(0, ['FOREIGN-PENDING (advisory, owner UNVERIFIED — EXCLUDED lane, …): PROME/state/HANDOFF_X.md', …])`.
  - CE-T2: `sha256=None,rules present: rc 0`; `sha256=aaaa…: rc 0`.
  - CE-V: `pattern with trailing space (valid shape): rc 0`.
- **Proposed change:** at minimum, require `(pin['sha256'] is None) == (pin['rules'] is None)` and strip-equality on each cell. Cheap consistency check: when the live perimeter's sha256 equals `pin.sha256`, require `load_perimeter() == pinned_rules`; a hand-edited pin then becomes rc 2. Reword AC5b to "bad digest FORMAT", or implement the check.

### ⚠️4. `ARGUS_CONTRACT.md` says the live perimeter "is never read at verify time", but the legacy (schema-1) verify still reads it and reproduces CE8b with rc 0, after which `--mark-reviewed` promotes.
- **Claim (VERIFIED):**
  - **The legacy read:** `verify_review()` for a manifest without `schema: 2` builds its scope from `load_perimeter()` live (`argus_scope.py:492`) and drops EXCLUDED paths (L367).
  - **The reproduction:** a post-freeze edit adding `AUDIT_PERIMETER.tsv EXCLUDED` and `HANDOFF_X.md EXCLUDED`, plus the HANDOFF write, gives rc 0 and REVIEWED.
  - **Pre-existing and out of the repair's schema-2 scope**, but two procedure texts overclaim it:
    - `ARGUS_CONTRACT.md:3`, new sentence: "The perimeter every verify classifies with is PINNED … never read at verify time";
    - `CLOSEOUT.md:85`: "Legacy manifests retain strict behavior".
  - **Reachability:** the legacy path is reachable through `--record-review` without `--contract`. The legacy consumed-move workflow forces it, because `--contract` refuses `--consumed-move` (`argus_scope.py:720-721`). That workflow is gated off by L488 for now.
- **Artifact:** `PROME/tools/argus_scope.py:492`; `PROME/tools/ARGUS_CONTRACT.md:3`; `PROME/CLOSEOUT.md:85`.
- **Command:** `python3 -B ce.py "CE-L"`.
- **Observed:** `legacy working-tree gate: (0, ['1 path(s) in the working tree byte-identical to the frozen candidate (verdict FROZEN, …)'])`, then `mark_reviewed: (0, 'verdict REVIEWED over 1 path(s)')`.
- **Proposed change:** scope the sentence to "every schema-2 verify". Add the legacy CE8b reproduction to the acceptance's declared residue, or to the L796 / L488 row, so that "legacy = strict" is not read as covering it.

### ⚠️5. Advisory wording in CLOSEOUT.md does not match the code.
- **Claim (VERIFIED):**
  - `CLOSEOUT.md:86` quotes `FOREIGN-PENDING (advisory, owner UNVERIFIED — <lane>, no PROME evidence)`.
  - The code emits `FOREIGN-PENDING (advisory, owner UNVERIFIED — {lane} lane, no PROME evidence): {path}` (`argus_contract.py:310`). The acceptance Design bullet uses `<class> lane`, which matches the code.
  - The common prefix `FOREIGN-PENDING (advisory` still matches, and no code consumer parses the line (grep of `PROME/tools/*.py` and `scripts/*.py`: only `argus_contract.py`).
- **Artifact:** `PROME/CLOSEOUT.md:86`; `PROME/tools/argus_contract.py:310`.
- **Command:** `grep -n "lane, no PROME" PROME/CLOSEOUT.md PROME/tools/ARGUS_CONTRACT.md` returns no hits. `grep -rn FOREIGN-PENDING PROME/tools/*.py scripts/*.py` matches only argus_contract.py.
- **Observed:** as stated.
- **Proposed change:** write `— <lane> lane, no PROME evidence): <path>` in CLOSEOUT.md:86.

### ⚠️6. A manifest frozen before the repair loses its commit attribution as well as the advisory branch.
- **Claim (VERIFIED):**
  - With no `perimeter` key, `rules` is None. `attributed_by_commit` then returns `{}` even though the manifest carries `attributed_by_commit` (`argus_contract.py:112-113`, `:273`).
  - So every committed-only foreign path becomes `UNCLASSIFIED`, on the working tree and at step 10.
  - This is fail-closed and documented ("a manifest without a pin runs strict"). It matters only if a closeout froze with the old code and verifies with the new code; the real manifest belongs to a prior baseline, so there is no live effect today.
- **Artifact:** `argus_contract.py:112-113`, `:272-273`; real manifest `PROME/state/argus_review.json` (schema 2, REVIEWED, 227 `attributed_by_commit` entries, no `perimeter`).
- **Command:** `python3 -B ac_check.py` (AC5a adds a committed `AGENTS/BRENT/c.md`); read-only `python3 -B PROME/tools/argus_scope.py --verify-review` on the real repo.
- **Observed:**
  - AC5a: `(1, ['UNCLASSIFIED: AGENTS/BRENT/c.md …', 'UNCLASSIFIED: AGENTS/BROCK/new.md …'])`.
  - Real repo: `CANNOT-EVALUATE: contract belongs to a different baseline`.
- **Proposed change:** none required. Re-freeze after this code lands, before the next gate. Optionally add one clause to the CLOSEOUT pin sentence: "(including commit attribution)".

### ⚠️7. The new tests leave the step-10 `--ref` form and the freeze-side perimeter classification uncovered.
- **Claim (VERIFIED):** `PerimeterPinTests` exercises only the working-tree verify. My CE-S10 shows the pinned rules do govern step 10's committed side correctly: `FORGE/x.md` is UNCLASSIFIED where HEAD code reported only the perimeter. No test locks that in. ❌1 (CE-C1, CE-O) is also untested.
- **Artifact:** `PROME/tools/tests/test_argus_contract.py`, class PerimeterPinTests.
- **Command:** `python3 -B ce.py "CE-S10"`.
- **Observed:** `step10, + FORGE commit + live perimeter edit: (1, ['UNCLASSIFIED: FORGE/x.md …', 'UNCLASSIFIED: PROME/state/AUDIT_PERIMETER.tsv …'])`.
- **Proposed change:** port CE-S10, CE-C1 and CE-O into PerimeterPinTests.

---

## ✅ findings, including AC1–AC9 checked at the code by my own fixtures (not the author's suite)

| AC | Token | Command | Observed |
|---|---|---|---|
| AC1 pin recorded | VERIFIED | `ac_check.py` AC1 | `rules==loaded: True; sha==file: True; perimeter not in contract: True; contract_sha ok: True; contract keys ['anchor','baseline','delivered','evidence']` (`argus_contract.py:130-139,182,186-191`) |
| AC2 CE8b | VERIFIED | AC2, NEW vs OLD(HEAD) | NEW `(1, ['UNCLASSIFIED: PROME/state/AUDIT_PERIMETER.tsv …', 'UNCLASSIFIED: PROME/state/HANDOFF_X.md …'])`, no FOREIGN line. OLD `(0, [FOREIGN-PENDING … ×2, contract … unchanged])`. The defect is reproduced at HEAD and closed by the diff. |
| AC3 CE8 control | VERIFIED | AC3 | rc 1 `UNCLASSIFIED: …AUDIT_PERIMETER.tsv` + `FOREIGN-PENDING (… SHARED lane …): memory/auto/x.md`. memory/auto/x.md is classified by the pinned rules (SHARED), not the live EXCLUDED. |
| AC4 committed overlap | VERIFIED | AC4, NEW vs OLD | NEW rc 1 lists `UNCLASSIFIED: FORGE/x.md` and the perimeter. OLD rc 1 lists only the perimeter, which confirms the pre-fix live attribution the acceptance describes. |
| AC5a legacy strict | VERIFIED | AC5a | rc 1, foreign arrival UNCLASSIFIED, no advisory (see ⚠️6 for the committed-attribution consequence). |
| AC5b malformed pin | VERIFIED for class and shape, NOT ESTABLISHED for "bad digest" beyond format (⚠️3) | AC5b, CE-V | `(2, ['CANNOT-EVALUATE: malformed perimeter pin rules'])`. Empty list, 4 cells, non-str pattern, UNATTRIBUTED class, extra key, `[]`, `false`, `{}` and dict rules all give rc 2. A JSON `null` pin or `rules: null` gives strict rc 1. |
| AC6 ordinary | VERIFIED | AC6 | rc 0, `FOREIGN-PENDING (advisory, owner UNVERIFIED — EXCLUDED lane, no PROME evidence): AGENTS/BROCK/new.md`. |
| AC6b CE7 | VERIFIED | AC6b, NEW vs OLD | NEW rc 1 with the perimeter UNCLASSIFIED and BROCK advisory by the pinned rules. OLD rc 1 with both UNCLASSIFIED. Changed as designed. |
| AC7 CE5 | VERIFIED | AC7 | rc 1 `UNCLASSIFIED: PROME/old`, destination advisory. |
| AC8 CE2 wording | VERIFIED | AC8 | rc 0 with five advisory lines, each naming its lane (SHARED ×3, UNATTRIBUTED, EXCLUDED; root `CLAUDE.md` is SHARED by first match). This is declared residue ⚠️3 of the acceptance. |
| AC9 suites | VERIFIED (author's suites, run once as a check only) | `TMPDIR=<scratch>/repos python3 -B PROME/tools/tests/test_argus_*.py` | contract 25 OK · r100 37 OK · scope 28 OK · evidence 6 OK. |

- **✅ Concurrent: a race inside `pin_perimeter` / `freeze()` is caught (VERIFIED).**
  - `pin_perimeter` reads the file twice: `load_perimeter`, then `read_bytes` (`:135`, `:138`), so the digest and rules can disagree under a race. The in-freeze `verify()` (`:192-193`) still refuses: the perimeter is UNCLASSIFIED (hard-code `:285`) or CHANGED-SINCE-REVIEW if delivered.
  - Commands: `ce.py "CE-R"` and `"CE-R2"`.
  - Observed: `freeze REFUSED: UNCLASSIFIED: PROME/state/AUDIT_PERIMETER.tsv …; manifest written? False` and `freeze REFUSED: CHANGED-SINCE-REVIEW: delivered PROME/state/AUDIT_PERIMETER.tsv`.
  - `pin_perimeter`'s `sc.ROOT / sc.PERIMETER_FILE` and `load_perimeter()`'s default path are the same expression read at call time (`argus_scope.py:60`). `path=` is never passed, so the two cannot name different files except under this race.
- **✅ A perimeter delivered in the same freeze pins the new rules, consistent at step 10 (VERIFIED).** `ce.py "CE-D"`: `pin has new row: True`. The working-tree gate and step 10 both give `UNCLASSIFIED: AGENTS/BRENT/x.md` under the delivered row `AGENTS/BRENT/** OWNED`.
- **✅ Step 10 committed side uses the pin (VERIFIED).**
  - `ce.py "CE-S10"`: an EXCLUDED desk commit after the delivery gives rc 0, which is the ordinary case preserved. A FORGE commit plus a live perimeter edit gives rc 1 naming `FORGE/x.md`.
  - The step-10 rc can only get stricter: a live perimeter edit already forces `UNCLASSIFIED` on the perimeter file. The advisory branch stays OFF under `--ref`, so WQ-517 is unaffected.
- **✅ `--mark-reviewed` and `--observe` preserve the pin; a post-freeze perimeter edit refuses promotion (VERIFIED).** `ce.py "CE-M"`: `pin kept after mark: REVIEWED; pin kept after observe: True`; `mark_reviewed now: (1, 'REFUSED: … UNCLASSIFIED: PROME/state/AUDIT_PERIMETER.tsv …')`.
- **✅ Ordinary committed side (VERIFIED).** `ce.py "CE-X"`: a desk's post-freeze committed-only `memory/auto/finding_x.md` (SHARED by the pinned rules, BRENT subject) is attributed by its commit and gives rc 0.

## Neighbour categories (WQ-229)

| Category | Cases |
|---|---|
| Ordinary | AC6, CE-X, CE-S10 (first leg) ✅ |
| Overlap | AC4 ✅ and CE-S10 ✅ (a committed-only path whose live class flips is held by the pin). CE-C1 ❌1 (a committed perimeter that self-exempts before the freeze). |
| Wrong owner | AC2, AC3 ✅; AC8 (declared residue); CE-O (⚠️ sibling of ❌1); CE-G1 ❌2 |
| Missing information | AC5a, AC5b, AC6b ✅; legacy manifest strict for commit attribution too (⚠️6); unverified digest (⚠️3) |
| Concurrent activity | CE-R and CE-R2 ✅ (a race inside the freeze is caught); CE-M ✅. A perimeter edit between the gate and step 10 is held by the shared pin ✅ (CE-S10). |

## Verdict

**NOT RESOLVED.**
- **The defect as stated is closed:** CE8b (a pending, post-freeze, self-exempting perimeter edit) now blocks. VERIFIED by my own fixture against both the new code and HEAD.
- **❌1:** `attributed_by_commit` lacks the perimeter-file guard, so a non-PROME-subject perimeter commit before the freeze self-exempts and becomes the pin unreviewed. This is in the repair's own declared committed-side scope; the fix is one line plus a freeze `require`.
- **❌2:** a post-freeze root `.gitignore` edit is advisory and hides an OWNED arrival from the inventory. It is the same class and pre-existing since 10/22. Either fix it (never-advisory, like the perimeter) or declare it as residue with its bound: it cannot ship without `git add -f`, and step 10 catches a commit.
