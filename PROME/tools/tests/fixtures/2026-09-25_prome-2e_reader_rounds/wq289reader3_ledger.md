# WQ-289 (b) round-3 independent read: `PROME/tools/argus_scope.py` consumed-move exemption

**Result: NOT VERIFIED. 3 ❌ · 5 ⚠️ · 11 ✅**
Reader: Opus. I did not write the fix. I made no writes inside the repo. Fixtures and scripts are in this scratchpad (`harness.py`, `ce1_replace.py` … `ce8_posthoc.py`, one throwaway repo each, with a bare origin).
Code read: `d73c43532`, `argus_scope.py` (715 lines).

**Headline.** The four round-2 fixes hold under my counterexamples:
- ❌A: a shadow branch, a shadow tag, a poisoned tracking ref, no refspec, and a packet that exists only on a non-master branch all BLOCK.
- ❌B: the tool hashes the index blob and requires the disk bytes to equal it.
- ❌C and ❌D are present and match their targets.

Three *new* holes pass when they must block. All three are low-likelihood and all three are fixable in one edit:
- `git replace` makes an unpushed edit read as bytes on origin (P3).
- With no remote called `origin`, git treats the word `origin` as a path (P6).
- The manifest-only form now fetches and prints an extra line, so P7 as written is false.

**Suite.** `cd /home/willi/Research-workspace && python3 -W error::ResourceWarning -m unittest discover -s PROME/tools/tests -p 'test_argus*'` → `Ran 60 tests … OK`. `grep -c 'def test_'`: `test_argus_r100_consumed_move_WQ289.py` 32 · `test_argus_scope.py` 28.

---

## ❌ Violations (a property fails, or a counterexample passes when it must block)

**❌1 · P3: `git replace` makes an UNPUSHED local edit read as "bytes on origin".**
- **Claim:** P3 says the tool establishes by itself that ORIGIN's bytes are on origin.
- **Artifact:** `argus_scope.py:276` (`cat-file -p {origin_sha}:{path}`), `:289`, `:234`, `:304-306`. Every git call honours `refs/replace/*`.
- **Command:** `ce1_replace.py`. PROME commits a local edit to ORIGIN and never pushes it, then runs `git mv` and `git replace <origin blob X> <local blob Y>`.
- **Observed:**
  - Control without the replace: rc=1, "DEST bytes differ".
  - With the replace: **rc=0, `R100-CONSUMED-MOVE … byte-identical … at refs/remotes/origin/master = 310d219fac5f`**, while `git --no-replace-objects cat-file -p X` = `'packet body v1\n'`, which is not what ships.
  - Likelihood is LOW: it needs one deliberate local `git replace`.
- **Fix:** run every git call on the exemption path with `--no-replace-objects` (or `GIT_NO_REPLACE_OBJECTS=1` in env): `_fetch_origin_sha`, `_origin_blob_id`, `_index_content_id`, `_committed_content_id`, `_git_sees_r100`. Add a regression test in the shape of `ce1_replace.py`.

**❌2 · P7: the manifest-only form (`paths=None`) is no longer "byte-for-byte as before". It fetches over the network and can print a contradictory line.**
- **Claim:** P7 says `paths=None` is untouched, and `--mark-reviewed` is unchanged.
- **Artifact:**
  - `argus_scope.py:456-458` puts the DISCOVERED list into `paths`.
  - `:478` `if paths is not None:` is then true for the manifest-only form too.
  - `:487-490` fetches whenever `consumed_moves` is non-empty.
  - The callers affected are `mark_reviewed` (`:213`, `verify_review()`) and `PROME/tools/prome_gate.py:1214` (`argus_scope.verify_review()`).
- **Command:** `ce3_p7.py`, which spies on `_fetch_origin_sha`.
- **Observed:**
  - Fetch calls: undeclared `paths=None` → 0; record + `mark_reviewed` with a declaration → **1**; a `paths=None` verify with a declaration → **1**.
  - With the remote unreachable, `paths=None` returns **rc=0** and prints `CANNOT-ESTABLISH origin state … every declared pair is refused` directly above `1 path(s) … byte-identical`. That is a refusal line sitting next to a pass.
  - `mark_reviewed` with the remote unreachable → rc 0.
  - The rc does not change, so harm is LOW. But the closeout gate now does a network fetch that writes `.git` and can block for up to 60 s. Test 12 misses this because it asserts only the rc and the absence of `R100`.
- **Fix:** capture `explicit = paths is not None` at the entry of `verify_review`. Gate the whole declared-move block (fetch included) on `explicit`. Extend test 12 to assert zero fetch calls and identical `out` lines.

**❌3 · P6: with no remote named `origin`, the tool still "establishes" origin, because `git fetch origin` falls back to a PATH.**
- **Claim:** P6 says that if `origin/master` cannot be resolved, the exemption is withheld.
- **Artifact:** `argus_scope.py:260-262`. `git fetch -q origin +refs/heads/master:…` treats `origin` as a repository path when no remote of that name exists.
- **Command:** `ce7_originpath.py`. `git remote remove origin`, then a local clone at `./origin` (listed in `.git/info/exclude`) holding an unpushed packet.
- **Observed:**
  - **rc=0, `R100-CONSUMED-MOVE … at refs/remotes/origin/master = 341046308661`** for a packet that was never pushed.
  - Without the exclude, the nested repo shows up as UNREVIEWED `origin/` and blocks `mark_reviewed`.
  - Likelihood is VERY LOW: it needs three deliberate local acts.
- **Fix:** check `git remote get-url origin` first (any failure → `(None, why)`), or fetch from the URL read from `remote.origin.url`. Add a regression test in the shape of `ce7_originpath.py`.

---

## ⚠️ Residue (fails closed, instruction robustness, or a known class now demonstrated)

**⚠️4 · ❌B fix: under an eol/clean filter, a GENUINE move is refused in the working-tree form, and the refusal message is wrong.**
- **Artifact:** `argus_scope.py:361-362`.
- **Command:** `ce2_crlf.py` (`.gitattributes` `*.md text eol=crlf`).
- **Observed:**
  - The disk file is `b'packet body v1\r\n'` and the index blob is LF.
  - `git diff --name-only` is quiet. Working-tree form: rc=1, "on disk differs from its index blob — the shipped bytes are not the bytes on disk". That message is false: the committed blob is LF and equals origin.
  - `--ref HEAD` (the step-10 production form): **rc=0 with the receipt**, which is correct.
  - The live repo has no `core.autocrlf` and no `.gitattributes`, so this is dormant today.
- **Fix:** none needed now; it fails closed. Optionally compare `git hash-object --path=DEST DEST` (filter-aware) with the index blob instead of raw disk bytes, or reword the message.

**⚠️5 · ❌C instruction, leg (b)①: the command as written is fragile.**
- **Artifact:** `.claude/agents/argus.md:18`. The copy at `PROME/.claude/agents/argus.md` is identical.
- **Command:** `ce6_arguscmd.py` runs `git diff --stat <ls-remote sha>:ORIGIN DEST` verbatim.
- **Observed:**
  - From the repo root, "identical" prints nothing and "differs" prints a stat line, as intended.
  - (i) It compares against the DISK file, not the index or commit. That reopens, inside ARGUS's own check, the exact disk-vs-index gap ❌B closed in the tool.
  - (ii) From the `PROME/` cwd (PROME's session cwd) it returns **rc=128, stdout EMPTY**, stderr `fatal: ambiguous argument … Use '--'`. A reader applying "no output = identical" to stdout would read an error as a match. `cat-file -e` from the same cwd succeeds, so the leg looks half-working.
- **Fix:** compare two blob ids from the repo root: `git rev-parse <sha>:ORIGIN` vs `git rev-parse :DEST` (pre-commit) / `HEAD:DEST` (post-commit). Equal ids = identical; an error ≠ identical.

**⚠️6 · ❌C instruction, leg (b)②: `%an` cannot tell desks apart.**
- **Artifact:** `argus.md:18`: `git log <sha> --diff-filter=A --format='%h %an %s' -- ORIGIN` — "a PROME-authored origin is not an inbound packet".
- **Command:** `git log -200 --format='%an' | sort | uniq -c`.
- **Observed:** `200 williepowen-debug`. Every desk commits as the same author, so this leg can only be judged from the SUBJECT, which is the authorship-by-subject pattern the redesign's A3 and P5 forbid.
- **Fix:** tell ARGUS the author field carries no signal. Use the adding commit's subject together with its OTHER touched paths (`git show --name-only`: a sender commit usually touches `AGENTS/<X>/`), and record the leg as INFERRED rather than VERIFIED.

**⚠️7 · P2: the REVIEWED verdict is not bound to the set of declared pairs.**
- This is the known residue class R2 ⚠️7/⚠️9, now demonstrated as an actual pass.
- **Artifact:** `argus_scope.py:220-225` (`mark_reviewed` writes no digest of `consumed_moves`) and `:479` (verify reads whatever is in the file).
- **Command:** `ce8_posthoc.py`. Freeze with NO declarations and mark REVIEWED, then hand-add `{DEST: ORIGIN}` to the JSON.
- **Observed:** **rc=0 with the R100 receipt** for a pair ARGUS never saw. It needs a hand edit of `PROME/state/argus_review.json`.
- **Fix:** at `mark_reviewed`, store `sha256(json.dumps(consumed_moves, sort_keys=True))`. At verify, a mismatch refuses every pair.

**⚠️8 · Prior residue R2 ⚠️4, ⚠️5 and ⚠️6 (network failure → rc 1 not 2; move committed before `ref` refused; non-ASCII names refused) is unchanged.** I read the code and did not re-test it. It all fails closed; the ACCEPTANCE doc is the record.

---

## ✅ Held

- **✅9 · ❌A fix (shadowing, poisoning, missing refspec, non-master branch).**
  - Command: `ce4_shadow.py`. Local branch AND tag named `origin/master`; `refs/remotes/origin/master` pre-set to the local commit; `remote.origin.fetch` unset; packet pushed only to `origin/feature`.
  - The short name resolves to the local commit `0dfdf7e4701b`. Working-tree form rc=1 and `--ref HEAD` rc=1, both "cannot establish … on origin".
  - After the verify, the tracking ref = `cf525bb0f87b` = the bare repo's master. The forced explicit refspec at `:260-263` overwrote the poison.
- **✅10 · ❌B fix.** `:358` hashes the index or commit blob and `:361` requires disk == index. Test `test_r2_1` (assume-unchanged) passes. ⚠️4 is the only side effect, and it fails closed.
- **✅11 · P4 with DEST already in HEAD.** `ce5_destinhead.py`:
  - (a) identical DEST already committed and only ORIGIN deleted → rc=1;
  - (b) DEST overwritten with ORIGIN's bytes plus ORIGIN deleted (name-status `D` + `M`, still no `R` even with `-B`) → rc=1 in both forms, "not … an R100 rename".
- **✅12 · P1 (declared, never inferred).** The exemption iterates only `d["consumed_moves"]` (`:479-504`). `test_02` covers the undeclared case.
- **✅13 · P2 (REVIEWED required).** Checked at `:334`, covered by `test_03`. See ⚠️7 for the missing binding.
- **✅14 · P5 (by path).** `:338-343` uses `_match` on the path and compares basenames. Tests 08, 09 and 09b pass. Nothing reads commit subjects.
- **✅15 · P8 (visible).** Both halves are required (`:344`), duplicate ORIGINs are refused (`:491-496`), the receipt prints once on DEST with the fetched sha (`:371-373`, `test_receipt_names_the_fetched_origin_commit`), and the ORIGIN half is silent (`:507-508`).
- **✅16 · P3 in the ordinary case.** The index or commit blob is compared with the blob at the fetched sha (`:365-370`). Tests 04, 05, 13, ce3 and ce3b pass. The exception is ❌1.
- **✅17 · P6 in the ordinary case.** Fetch failure → `origin_sha None` → refusal plus a CANNOT-ESTABLISH line (`:488-490`, `:363-364`). Test 06 passes. The exception is ❌3; R2 ⚠️4 (rc 1 rather than 2) remains.
- **✅18 · ❌C present.** `argus.md:18` splits (a) "a second execution of what the tool checks" from (b) ①–③ "what the tool does NOT check". The root and `PROME/` copies are identical (`diff -q`). ⚠️5 and ⚠️6 are about robustness, not presence.
- **✅19 · ❌D.** Both copies of `closeout/SKILL.md` (identical) point to "CLOSEOUT.md step 8", and the declaration text sits in step 8 at `PROME/CLOSEOUT.md:80`. Step 10 (`:89`) uses `--verify-review --ref HEAD --paths`, the form that handled ⚠️4 correctly.

## P1–P8 verdicts

| Property | Verdict |
|---|---|
| P1 | ✅ |
| P2 | ✅, with ⚠️7 (verdict not bound to the declared set) |
| P3 | ❌ via ❌1 (`git replace`); otherwise ✅ |
| P4 | ✅ |
| P5 | ✅ |
| P6 | ❌ via ❌3 (no `origin` remote → path fallback); otherwise ✅ |
| P7 | ❌ via ❌2 (fetch and extra line in the `paths=None`, `mark_reviewed` and `prome_gate` callers) |
| P8 | ✅ |

**One edit clears all three ❌:** `--no-replace-objects` on the exemption path's git calls, a `remote get-url origin` pre-check, and gating the declared block on explicit `--paths`. Each gets its own regression test. Per WQ-178, that edit then needs its own result read.
