# L796 ❌2 repair — independent counterexample read #2 (the fix pass of read #1)

> Saved verbatim by PROME 2026-10-24 18:2x ET from the reader's scratchpad ledger (Opus, general-purpose, read-only, disposable repos). Spawn: ORCH_LOG 2026-10-24 L796-PIN-READER touch 2. Fixtures: `PROME/reports/2026-10-24_L796-pin-counterexample-read2_fixtures/` (ce2.py, run2.txt). Verdict NOT RESOLVED at this read (❌A committed ignore file attributed by commit · ❌B observe() accepts the perimeter); fix pass 2 and read #3 are recorded in `PROME/tools/tests/ACCEPTANCE_closeout_gate_perimeter_pin_2026-10-24.md` § Results.

---

# L796 perimeter-pin fix pass 1: independent counterexample read #2

**Reader:** independent counterexample reader, round 2 (Opus). Read-only on the repo. Started Sat 2026-10-24 18:18 EDT (from `date`).

**What I read:**
- `git diff` of the four files (argus_contract.py, test_argus_contract.py, CLOSEOUT.md, ARGUS_CONTRACT.md);
- `PROME/tools/argus_contract.py` in full (368 lines);
- `argus_scope.py` lines 55-112, 150-170, 228-260, 405-432 and 575-655;
- the acceptance file, including § Results and its declared residue;
- the round-1 ledger (❌1 and ❌2), and round-1 `ce.py`;
- `PROME/state/AUDIT_PERIMETER.tsv`.

**Fixtures:** my own, at `/tmp/claude-1000/-home-willi-Research-workspace-PROME/21f2c037-44fb-44e2-b95b-80eb222ec9a7/scratchpad/l796-pin-read2/ce2.py`. They reuse the round-1 Fx pattern: the REAL perimeter and root `.gitignore` are committed into the baseline, and `tempfile` is pointed at `l796-pin-read2/repos/`. Raw output is `run2.txt` in the same directory. The ported `test_x*` tests were not used as evidence.

**Repo state:** nothing was written to the repo.
- `git status --porcelain` before and after differs only by `AGENTS/DEWEY/scripts/edgar_doc.py`, `test_edgar_xbrl_compare.py` and `AGENTS/DEWEY/research/edgar_xbrl/`. Those belong to a concurrent DEWEY L834 session: commit 0c0ab27ab landed 2 minutes before the check, and the file mtime is 18:19:53. None of it is mine.
- I never called argus_scope with `--record-review`, `--freeze`, `--mark-reviewed`, `--record-baseline` or `--observe` against the real repo.

**Author suites (run once, as a check only, TMPDIR = my scratch):**

| Suite | Result |
|---|---|
| `test_argus_contract` | 29 OK |
| `test_argus_scope` | 28 OK |
| `test_argus_scope_evidence` | 6 OK |
| `test_argus_r100_consumed_move_WQ289` | 37 OK |

---

## ❌ findings

### ❌A. A COMMITTED post-freeze root `.gitignore` edit with a non-PROME subject hides an OWNED file and is silently attributed by its commit, so the gate returns rc 0 on the working tree AND at step 10. CE-G1 is closed only for a pending edit.
- **Claim (VERIFIED):**
  - **Where the guard is missing:** `never_advisory()` is consulted only by `foreign_pending` (pending paths). `attributed_by_commit()` skips the perimeter file but does not skip ignore/attribute files.
  - **The case:** after the freeze, a desk commits `.gitignore` (subject `WALTER: ignore board cache`) with a line `PROME/state/HANDOFF_X.md`, and PROME then writes that OWNED file. The `.gitignore` is committed-only, UNATTRIBUTED (no perimeter row) and unevidenced, so it is auto-attributed at verify (`:285`, `:308-309`). The OWNED file is absent from porcelain.
  - **What the gate shows:** rc 0, with no line at all. This is weaker than round 1's advisory line, which at least named `.gitignore`. Step 10 (`--ref`) is also rc 0, because the `changes()` loop skips `auto` (`:340-341`).
  - **Same class, same bound as CE-G1:** the inventory's visibility is derived from a file whose post-freeze change the gate does not block. The ignored file still cannot be `git add`-ed without `-f`, and a force-add would fail step 10 as `UNREVIEWED ACTUAL COMMIT PATH`. Round 1 graded CE-G1 ❌ under exactly this bound, and the fix pass accepted that grade.
  - **The doc rationale does not hold on the committed side:** CLOSEOUT.md:86 says `.gitignore`/`.gitattributes` are never advisory "since it changes what the inventory can see". A committed edit is not advisory, but it is treated more leniently than advisory.
  - **Real-world precondition (VERIFIED):** non-PROME subjects do commit root `.gitignore`. Examples: `12a437972 2026-08-18 gitignore + MACHINE_LOCAL: …` and `94eb93602 KERNEL: …` (`git log -- .gitignore`).
  - **Siblings:**
    - **N1c (pre-freeze):** the same commit before the freeze is auto-attributed at the freeze (`auto=['.gitignore']`), and an OWNED pending write is never in `inventory`. Freeze OK, gate rc 0.
    - **N1d:** a committed `.gitattributes` after the freeze also gives rc 0. I constructed no hiding effect for `.gitattributes` from the tree alone (INFERRED low impact), but it is the same unguarded path.
  - **Control (N1ctl):** with a `PROME:` subject, the same commit gives rc 1 `UNCLASSIFIED: .gitignore`, so the hole is the non-PROME-subject exemption.
- **Artifact:** `PROME/tools/argus_contract.py:116-128` (loop guards only `PERIMETER_FILE`), `:144-147` (`never_advisory`, used only at `:297`), `:285`, `:308-309`, `:340-341`; `PROME/CLOSEOUT.md:86`; `PROME/tools/ARGUS_CONTRACT.md:3`.
- **Command:** `python3 -B ce2.py N1 N1ctl N1c N1d`.
- **Observed:**
  - N1 working-tree gate: `(0, ['contract e8750ca9… unchanged; verdict FROZEN; … 2 inventory paths retained …'])`.
  - N1 step10 --ref: `(0, [... delivery c64cf97c…])`.
  - porcelain: `'?? PROME/state/argus_baseline.json\n?? PROME/state/argus_review.json'`.
  - `--ignored` under PROME/: `'!! PROME/state/HANDOFF_X.md'`.
  - N1ctl: `(1, ['UNCLASSIFIED: .gitignore …'])`.
  - N1c: `freeze OK; auto=['.gitignore']; HANDOFF_X in inventory? False; gate: (0, …)`.
  - N1d: `(0, …)`.
- **Proposed change:** in `attributed_by_commit`, replace `if p == sc.PERIMETER_FILE: continue` with `if never_advisory(sc, p): continue`. Ignore and attribute files then need delivered/observed at the freeze and block after it, on both sides. Add N1 (post-freeze commit, working tree and `--ref`) and N1c (pre-freeze commit) as tests. Optionally scope the guard by location (see ⚠️C).

### ❌B. `observe()` accepts the audit perimeter after the freeze. The post-freeze perimeter commit then passes the gate and step 10, and once the baseline advances, the next freeze pins the unreviewed rules with no delivery demanded. CE-O is closed only inside `freeze()`.
- **Claim (VERIFIED):**
  - **Where the guard is missing:** `freeze()` refuses the perimeter as `observed` (`:185`). `observe()` (`:361-365`) checks only `path in seen and not delivered and not current-evidence`, and `validate()` (`:243-249`) has no perimeter check either.
  - **The case:** after the freeze, a desk commits a perimeter row `PROME/state/HANDOFF_X.md EXCLUDED` (subject `WALTER: …`).
    - The gate correctly blocks: `UNCLASSIFIED: PROME/state/AUDIT_PERIMETER.tsv`.
    - CLOSEOUT.md:86 and :98 instruct that a post-freeze arrival at step 10 is classified with `--observe`. `ac.observe()` with a non-PROME owner and a quote is accepted.
    - Then the gate gives rc 0, `--mark-reviewed` promotes to REVIEWED, and step 10 `--ref` gives rc 0.
  - **Next day:** the baseline is recorded at the delivery commit (the CLOSEOUT practice; e.g. "ARGUS baseline recorded at the 10/24 delivery 2509a8823"). The perimeter is then unchanged since the new baseline, so the freeze's delivery `require` does not fire, and the pin carries WALTER's rows. A PROME write that is OWNED under the reviewed perimeter is then `FOREIGN-PENDING (advisory …)` with rc 0.
  - **Why this is ❌1's class:** this is exactly round-1 ❌1's consequence ("the pin then carries rules nobody reviewed"), reached through the one classification door the fix did not shut.
  - **It contradicts both procedure texts the fix pass wrote:**
    - ARGUS_CONTRACT.md:3: "a post-freeze edit of it is an OWNED arrival that blocks until delivered in a re-freeze … never observed-only";
    - CLOSEOUT.md:86: "editing the perimeter after the freeze is itself an OWNED arrival and blocks until re-frozen".
- **Artifact:** `PROME/tools/argus_contract.py:354-368` (observe, no `PERIMETER_FILE` refusal), `:243-249` (validate observed loop), `:185` (the freeze-only refusal); `PROME/CLOSEOUT.md:86`, `:98`; `PROME/tools/ARGUS_CONTRACT.md:3`.
- **Command:** `python3 -B ce2.py N2`.
- **Observed:**
  - `gate before observe: (1, ['UNCLASSIFIED: PROME/state/AUDIT_PERIMETER.tsv …'])`;
  - `observe() ACCEPTED the perimeter`;
  - `gate after observe: (0, …)`;
  - `mark_reviewed: (0, 'verdict REVIEWED over 1 path(s)')`;
  - `step10: (0, … verdict REVIEWED …)`;
  - `next-day freeze pins WALTER rows without delivery: True`;
  - `next-day gate with OWNED-under-old-rules write: (0, ['FOREIGN-PENDING (advisory, owner UNVERIFIED — EXCLUDED lane, no PROME evidence): PROME/state/HANDOFF_X.md', …])`.
- **Proposed change:**
  - In `observe()`, add `require(not never_advisory(sc, path), f'{path}: never observed-only — deliver it in a re-freeze')`. With ❌A's widening this covers ignore files too, and that is a judgment call: an operator-recorded observation of a desk's `.gitignore` may be acceptable, so at minimum refuse `PERIMETER_FILE`.
  - Mirror the same refusal in `validate()`'s observed loop, so a hand-written manifest entry is CANNOT-EVALUATE.
  - Add N2 as a test.

---

## ⚠️ findings

### ⚠️C. The basename rule over-blocks a routine desk action: a desk creating a nested `.gitignore` in its own research directory after the freeze now blocks PROME's working-tree gate. This regresses the 10/22 live-fleet rule's intent (safe direction).
- **Claim (VERIFIED):**
  - **How often (VERIFIED):** `git ls-files` shows about 30 tracked nested `.gitignore` files. Most are desk research dirs created in October (`AGENTS/WALTER/research/2026-10-19_*/.gitignore`, `AGENTS/OTTO/research/2026-10-19_*/.gitignore`, BROCK, HENRY, REGINALD, …).
  - **What changed:** pending creation of one of these after PROME's freeze is now `UNCLASSIFIED` (rc 1) instead of advisory.
  - **Why it is an over-block:** a nested ignore file hides only paths beneath its own directory. Under `AGENTS/<X>/research/…` those are EXCLUDED-lane paths, which the gate never blocks on anyway. So the block buys nothing there.
  - **Why it matters:** this is precisely the "happens almost every time" friction Will ruled against on 10/22. AC6 itself still passes (R1).
- **Artifact:** `PROME/tools/argus_contract.py:144-147`; CLOSEOUT.md:86 (live-fleet rule).
- **Command:** `python3 -B ce2.py N5`; `git ls-files | grep -E '(^|/)\.git(ignore|attributes)$'`.
- **Observed:**
  - `pending AGENTS/BROCK/.gitignore (cannot hide PROME files): (1, ['UNCLASSIFIED: AGENTS/BROCK/.gitignore …'])`;
  - `pending memory/auto/.gitignore: (1, …)`;
  - `pending root .gitattributes: (1, …)` (intended).
- **Proposed change:** make an ignore/attribute file never-advisory only when its directory can contain non-EXCLUDED paths under the pinned rules. Simplest form: root-level, or any directory not wholly inside an EXCLUDED pinned lane. Note that `AGENTS/<X>/` contains the SHARED `AGENTS/*/inbox/**`, so take care not to reopen the hole there. Alternatively, declare the over-block as residue with its frequency.

### ⚠️D. The pin's rules are not bound to the bytes that were delivered. `pin_perimeter` parses rules in one read and digests the bytes in a second, and nothing compares the pin to the delivered version or re-parses it.
- **Claim (VERIFIED by simulation; the real trigger is a double race A→B→A inside `freeze()`, INFERRED unlikely):**
  - **The simulation:** with `load_perimeter` patched to return a different rule set during `pin_perimeter`, while the file's bytes stay at the delivered version, the freeze succeeds.
  - **What the manifest then holds:** `perimeter.sha256 == delivered.sha256` (True), while `pinned_rules != rules parsed from the delivered bytes`. The gate is rc 0 with an OWNED write advisory.
  - **Why the in-freeze verify misses it:** it compares only bytes (CHANGED-SINCE-REVIEW), never the parse.
  - **Link to declared residue:** this extends declared residue ⚠️3. The fix pass made the delivered version "the pin" (freeze require message: "the delivered version becomes the pin"), but the code does not establish that equality.
- **Artifact:** `PROME/tools/argus_contract.py:132-141`, `:180-182`, `:194-195`.
- **Command:** `python3 -B ce2.py N8`.
- **Observed:** `freeze OK; pin sha == delivered sha: True; pin rules == rules parsed from delivered bytes: False`, then gate `(0, ['FOREIGN-PENDING (advisory … EXCLUDED lane …): PROME/state/HANDOFF_X.md', …])`.
- **Proposed change:**
  - Read the bytes once, digest them, and parse those same bytes. For example, write them to a temp file and use `load_perimeter(path=)`, or factor out a parser.
  - When the perimeter is delivered, `require(pin['sha256'] == delivered[PERIMETER_FILE]['sha256'])`.
  - Or fold this into residue ⚠️3's "move the pin inside the contract".

### ⚠️E. Index flags (`--assume-unchanged` / `--skip-worktree`) hide a post-freeze edit of a TRACKED OWNED file from porcelain, so the gate returns rc 0. The declared residue names only `.git/info/exclude` and the self-ignoring nested `.gitignore`.
- **Claim (VERIFIED):**
  - **The case:** after the freeze, `git update-index --skip-worktree PROME/tracked.md` (or `--assume-unchanged`) followed by an edit gives empty porcelain and rc 0.
  - **Ship bound (VERIFIED in a scratch repo):**
    - with skip-worktree, `git add` and `git commit -- path` refuse;
    - with assume-unchanged, `git commit -- path` DOES commit the edit, and step 10 would then catch it as `UNREVIEWED ACTUAL COMMIT PATH` (diff-tree based, `:328-332`).
  - So this has the same bound as CE-G1. It is local-only git state, outside the tree, in the same family as `.git/info/exclude`.
- **Artifact:** `PROME/tools/argus_scope.py:579-582` (porcelain inventory); acceptance § Declared residue, last bullet.
- **Command:** `python3 -B ce2.py N7`; the scratch repo `repos/sw` sequence (shell, in the ledger directory).
- **Observed:**
  - `skip-worktree: porcelain '?? PROME/result\n…'; gate (0, …)`;
  - `assume-unchanged: … gate (0, …)`;
  - scratch: `add rc 1` (sparse refusal) under skip-worktree; `add rc 0`, `commit rc 0`, `HEAD:t.md = c` under assume-unchanged.
- **Proposed change:** add "index flags (assume-unchanged / skip-worktree) and `core.excludesFile`" to the declared residue line. If it matters, a cheap check is `git ls-files -v` lower-case / `S` tags over the OWNED lane.

---

## ✅ findings, checked by my own fixtures

| # | Claim (token) | Artifact | Command | Observed |
|---|---|---|---|---|
| 1 | **CE-C1 closed** (VERIFIED). A non-PROME-subject pre-freeze commit that reclassifies the perimeter (rows `AUDIT_PERIMETER.tsv SHARED`, `HANDOFF_X EXCLUDED`) refuses the freeze, and no manifest is written. Declaring it `observed` also refuses. | `argus_contract.py:117-118`, `:180-182` | `ce2.py V-C1` | `freeze REFUSED: PROME/state/AUDIT_PERIMETER.tsv changed since the baseline: deliver it …; manifest written? False` (both legs) |
| 2 | **Control: perimeter untouched** (VERIFIED). The freeze is OK, the ordinary committed-only desk memory file is still auto-attributed, and the pin digest equals the file. | `:194-195` | `V-C1ctl` | `auto=['memory/auto/f.md']; pin sha == file: True` |
| 3 | **CE-O closed at the freeze** (VERIFIED). A pending perimeter declared observed-only refuses. Delivered-and-observed refuses with the specific message. | `:180-185` | `V-O` | `freeze REFUSED: … deliver it …` / `freeze REFUSED: …: the audit perimeter is never observed-only — deliver it` |
| 4 | **CE-G1 closed for a PENDING edit** (VERIFIED). A post-freeze pending root `.gitignore` edit hiding an OWNED file gives rc 1 `UNCLASSIFIED: .gitignore`, with no FOREIGN line. | `:144-147`, `:297` | `V-G1` | `(1, ['UNCLASSIFIED: .gitignore (new or changed observed version)'])` |
| 5 | **Delivered-perimeter happy path** (VERIFIED). The pin carries the delivered row and the pin sha equals the delivered sha. The working-tree gate and step 10 are rc 0 when clean. With arrivals, the NEW pin classifies `AGENTS/BRENT/x.md` OWNED (blocks) and BROCK EXCLUDED (advisory on the working tree, UNCLASSIFIED at step 10 as designed). | `:180-182`, `:194-203`, `:284-303` | `V-D` | `pin has delivered row: True; pin sha == delivered sha: True`; `step10 clean: (0, …)`; `(1, ['UNCLASSIFIED: AGENTS/BRENT/x.md …', 'FOREIGN-PENDING (… EXCLUDED lane …): AGENTS/BROCK/y.md'])` |
| 6 | **New CE N3: a perimeter both committed (BRENT subject) and pending at the freeze** (VERIFIED). Undelivered, the freeze refuses. Delivered, the pin carries BOTH rows (committed and pending) and step 10 is rc 0. | `:170`, `:180-182` | `N3` | `pin has (committed,pending) rows (True, True)`; `step10: (0, …)` |
| 7 | **New CE N4/N4b: perimeter `git rm` / `git mv`** (VERIFIED). `git rm` at the freeze undelivered refuses. Delivered, the rules become None, everything is strict, and a desk committed-only file then refuses the freeze (fail-closed over-block, not a hole). A staged `git mv` after the freeze, and its WALTER commit, give rc 1 with both old and new paths UNCLASSIFIED; verify still classifies by the pin, not by the missing file. | `:132-141`, `:112-113`, `:297` | `N4`, `N4b` | `freeze REFUSED: unclassified inventory …: memory/auto/f.md`; `(1, ['UNCLASSIFIED: …AUDIT_PERIMETER.tsv …', 'UNCLASSIFIED: …AUDIT_PERIMETER_v2.tsv …', 'FOREIGN-PENDING … AGENTS/BROCK/new.md'])` |
| 8 | **New CE N6: case and path-form dodges fail** (VERIFIED). `.GITIGNORE` is not honoured by git here (`core.ignorecase` unset, case-sensitive fs), so the OWNED file stays visible and blocks. A symlinked root `.gitignore` is not followed by git 2.43 (porcelain `T .gitignore`), so it stays visible and the symlink itself blocks. `PROME//.gitignore` → True. `./PROME/…` → False, but porcelain and `diff-tree` never emit `./` or `//` forms (INFERRED unreachable). | `:147`; `argus_scope.py:579-596` | `N6` | `.GITIGNORE: porcelain '?? .GITIGNORE\n…?? PROME/state/HANDOFF_X.md…'; gate (1, ['UNCLASSIFIED: PROME/state/HANDOFF_X.md …', …])`; symlink: `(1, ['UNCLASSIFIED: .gitignore …', 'UNCLASSIFIED: PROME/state/HANDOFF_X.md …', …])` |
| 9 | **A post-freeze committed perimeter is never commit-attributed** (VERIFIED). Before any `--observe`, it blocks. | `:117-118` | `N2` (first line), `N4b` | `(1, ['UNCLASSIFIED: PROME/state/AUDIT_PERIMETER.tsv …'])` |
| 10 | **Regression R1 (AC6): ordinary foreign pending is still advisory** (VERIFIED). | `:294-303` | `R1` | `(0, ['FOREIGN-PENDING (advisory, owner UNVERIFIED — EXCLUDED lane, no PROME evidence): AGENTS/BROCK/new.md', …])` |
| 11 | **Regression R2: a desk's committed-only SHARED file (`memory/auto/…`) and EXCLUDED file (`AGENTS/BRENT/STATUS.md`) after the freeze still pass** (VERIFIED). Both the working tree and step 10 are rc 0. | `:116-128` | `R2` | `(0, … 3 inventory paths retained …)`; `step10: (0, …)` |
| 12 | **Regression R3: an OWNED pending arrival still blocks** (VERIFIED). | `:300-301` | `R3` | `(1, ['UNCLASSIFIED: PROME/state/HANDOFF_X.md …'])` |
| 13 | **No race between `inventory()` and `pin_perimeter()` that the delivery `require` can be satisfied around** (VERIFIED for the single race; see ⚠️D for the double race). A file change between the delivered-sha capture (`:170`) and the in-freeze verify (`:204`) is CHANGED-SINCE-REVIEW, which round-1 CE-R2 also showed. | `:170`, `:204-205` | round-1 `CE-R2`; my `N8` (double race only) | as cited |
| 14 | **The live perimeter is never read on the schema-2 verify path** (VERIFIED). The only `load_perimeter` call in `argus_contract.py` is in `pin_perimeter` (freeze). `argus_scope.py:492` is the legacy schema-1 branch (declared residue ⚠️4). `:770` is the scope listing, not verify. | `argus_contract.py:137`; `argus_scope.py:423-426`, `:492`, `:770` | `grep -n load_perimeter PROME/tools/argus_*.py` | three hits, as stated |

### (3) Doc sentences vs code

| Doc sentence (quoted) | Code | Match |
|---|---|---|
| CLOSEOUT.md:86 "is listed by the gate's manifest line as `FOREIGN-PENDING (advisory, owner UNVERIFIED — <lane> lane, no PROME evidence): <path>`" | `:322` `f'FOREIGN-PENDING (advisory, owner UNVERIFIED — {lane} lane, no PROME evidence): {path}'` | ✅ VERIFIED (round-1 ⚠️5 fixed) |
| CLOSEOUT.md:86 "The lane is read from the perimeter PINNED in the manifest at the freeze, never from the live `AUDIT_PERIMETER.tsv`" | `:284` `rules = pinned_rules(manifest)`; `:299` | ✅ VERIFIED |
| CLOSEOUT.md:86 "editing the perimeter after the freeze is itself an OWNED arrival and blocks until re-frozen" | Pending: `:297` never_advisory ✅. Committed: `:117` ✅. But `observe()` `:361-365` clears it with no re-freeze. | ❌ — see ❌B |
| CLOSEOUT.md:86 "a changed perimeter must be DELIVERED at the freeze (never attributed by commit or observed-only)" | `:117-118`, `:180-185` at the freeze ✅; `observe()` after the freeze ✗ | partial — see ❌B |
| CLOSEOUT.md:86 "a `.gitignore`/`.gitattributes` edit is never advisory either, since it changes what the inventory can see" | `:297` (pending only). A committed edit is attributed silently (`:116-128`). | literal ✅, the guarantee the sentence's reason implies ✗ — see ❌A |
| CLOSEOUT.md:86 "Schema-2 contract manifests only: the legacy schema-1 path … still reads the live perimeter and is not used by this closeout" / :85 "Legacy (schema-1) manifests retain the pre-10/22 strict additions check but still classify against the LIVE perimeter" | `argus_scope.py:423-426` dispatches schema 2 to the contract; `:492` legacy uses live `load_perimeter()` | ✅ VERIFIED (round-1 ⚠️4 fixed) |
| ARGUS_CONTRACT.md:3 "the live `PROME/state/AUDIT_PERIMETER.tsv` is never read at verify time, a post-freeze edit of it is an OWNED arrival that blocks until delivered in a re-freeze, and a manifest without a pin runs strict" | First clause ✅ (✅14). "blocks until delivered in a re-freeze" ✗ under `observe()`. "without a pin runs strict" ✅ (`:112-113`, `:297`). | ❌ on the middle clause — see ❌B |
| ARGUS_CONTRACT.md:3 "A perimeter changed since the baseline must be DELIVERED at the freeze (never attributed by commit, never observed-only); `.gitignore`/`.gitattributes` edits after the freeze are never advisory." | as for CLOSEOUT.md:86 | partial — see ❌A/❌B |

---

## Neighbour categories (WQ-229)

| Category | Cases |
|---|---|
| Ordinary | R1, R2, R3, V-C1ctl ✅; ⚠️C (over-block of a routine nested `.gitignore`) |
| Overlap | N3 (committed AND pending perimeter) ✅; N1 (committed side of the ignore-file guard) ❌A |
| Wrong owner | V-C1, V-O ✅; N2 (a desk perimeter commit observed after the freeze) ❌B |
| Missing information | N4 (perimeter removed: strict, fail-closed) ✅; ⚠️E (index flags, unseen) |
| Concurrent activity | ✅13 (single race), ⚠️D (double race, pin not bound to bytes) |

## Verdict

**NOT RESOLVED.**
- **Closed as stated:** round-1 ❌1 (CE-C1) and its sibling CE-O are closed AT THE FREEZE. Round-1 ❌2 (CE-G1) is closed for a PENDING `.gitignore` edit. The delivered-perimeter path pins the delivered rules and verifies at step 10. All of this is VERIFIED by my own fixtures.
- **❌A:** a COMMITTED (non-PROME-subject) root `.gitignore` edit, before or after the freeze, is attributed by its commit and hides an OWNED file with rc 0 on the working tree and at step 10. This is CE-G1's class on the committed side, because `attributed_by_commit` guards only `PERIMETER_FILE`, not `never_advisory()`.
- **❌B:** `observe()` (and `validate()`) accept the audit perimeter as observed-only after the freeze. That clears the block without a re-freeze, promotes and ships, and once the baseline advances, the next freeze pins the unreviewed rules. This is CE-O/❌1's class, and it contradicts the new sentences in CLOSEOUT.md:86 and ARGUS_CONTRACT.md:3.
