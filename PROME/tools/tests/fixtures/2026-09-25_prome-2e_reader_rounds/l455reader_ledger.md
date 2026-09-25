# L455 independent read: `spawn_list.attributed` / `desk_activity.last_commit`
**Reader:** independent Opus reader. I did not write the fix. Read-only against the repo. Every throwaway repo is under this scratchpad (`cx1…cx7/`, `loc/`), and so are my probe scripts (`cx.py`, `pop.py`, `win.py`, `agree.py`, `c7.py`, `fixprobe.py`). Repo HEAD at read: `1a816db51` (2026-09-25T09:18:08-04:00). The repair is uncommitted.

## Verdict: NOT VERIFIED (❌ 3 · ⚠️ 6 · ✅ 11)

The repair is population-correct. Condition 7 reproduces exactly: 3,877 commits, LOST 0 · GAINED 383 · REJECTED 5, and the 5 are the five named SHAs. There is no window truncation and no regression against the old reader, checked for 46 desks at 4 `--until` vintages. The git prefilter and the Python re-check agree, with 0 drops. The fail-closed path survives.

Three counterexamples of my own still attribute a commit to a desk when they must not. That is false ACTIVE, the severe direction. All three are **latent**: 0 instances in the measured population (the scans are in ❌1–3). One fix covers all three and is population-neutral: probe-4 gives 0 disagreements over the 3,877 commits × 46 desks.

**Completion states (WQ-229):** IMPLEMENTED ✅ · TESTED ✅ (18/18 · selftest 11/11 · fail_closed 15/15) · INDEPENDENTLY VERIFIED ❌ (3 open counterexamples) · STILL UNRESOLVED: ❌1–❌3 below, plus the declared R1–R4.

---

## ❌ Findings

### ❌1: Inbound mail in the named desk's OWN inbox counts as that desk's authorship (CX1, CX1b)
- **Claim:** For a loose-form subject, `any(p.startswith(home))` returns True before any packet test. A packet that ANOTHER desk (or PROME) delivered into `AGENTS/DESK/inbox/` is therefore treated as DESK's own commit. This is the exact failure named in spawn_list's own docstring (`finding_path_scoped_git_log_measures_inbound_traffic`: "AGENTS/X/ receives other desks' mail"), and the test file's own comment says "OTTO's packet INTO BROCK's inbox is OTTO's, not BROCK's". It breaks condition 3 (wrong owner) and condition 9 (ambiguity fails toward DARK).
- **Artifact:** `PROME/tools/spawn_list.py:137-138` (the home check comes before the `_PACKET` test at `:141`).
- **Command:** `cd /home/willi/Research-workspace && python3 <SP>/cx.py <SP>` (throwaway `cx1/`):
  - baseline: `HAWK: baseline own commit` → `AGENTS/HAWK/STATUS.md`
  - CX1: MIDAS commit `HAWK L433 re-grade request from MIDAS (carve-out 1)` → `AGENTS/HAWK/inbox/2026-09-25_from-MIDAS_regrade.md` + `AGENTS/MIDAS/STATUS.md`
  - CX1b: PROME commit `HAWK packet delivered by PROME` → `AGENTS/HAWK/inbox/2026-09-25_from-PROME_task.md` only
- **Observed:**
  - `last_self_commit(HAWK) = ('2026-09-25','fc7021f')`, then `('2026-09-25','8d8dcae')` after CX1b.
  - `desk_activity.last_commit` agrees: `fc7021faf` / `8d8dcae83`.
  - Both are **false ACTIVE**. A due HAWK row is silently NOT spawned.
  - CX1b also survives a naive fix: excluding packets from the home check alone still returns True through the "packet-only ⇒ nothing refutes" branch (`fixprobe.py`).
  - Population since 9/1: 0 instances. The only loose-form attributions resting solely on own-inbox paths are AEOLUS `f4dbeb070` and DEWEY `e5833e3b9`, both genuine own `processed/` drains (`pop.py`).
- **Proposed change:** Home evidence = a home path that does NOT match `_PACKET`. If the only home paths are `_PACKET` matches (mail into the named desk), return False. Probe-4 (below) does this: 0 population disagreements. It keeps WALTER `0542eff05` attributed (WALTER's closeout swept two inbound packets together with its own files). A stricter probe-3, where "any own-inbox packet ⇒ False", loses that commit, so do not use it. Add CX1 and CX1b as fixtures.

### ❌2: A quoted path (`core.quotePath`) skips every path test and reads as "un-homed ⇒ own" (CX3)
- **Claim:** `git log --name-only` C-quotes any path with non-ASCII or control bytes, e.g. `"AGENTS/MIDAS/notes/zhao_r\303\251futation.md"`. The leading `"` defeats every `startswith` test, so the path falls through to the final `return True`. The effect: a desk commit whose subject starts with ANOTHER desk's name is attributed to that other desk whenever the author's own path has an accent or similar character. This breaks condition 3 (the "another desk's home" case).
- **Artifact:** `PROME/tools/spawn_list.py:140-146` (the loop never matches a quoted path); the log commands at `:168` and `PROME/tools/desk_activity.py:102-103` (no `-c core.quotePath=false`, no `-z`).
- **Command:** throwaway `cx3/`: commit `ZHAO refuted my amendment rule` touching only `AGENTS/MIDAS/notes/zhao_réfutation.md`.
- **Observed:**
  - raw record: `'\x1eZHAO refuted my amendment rule\n\n"AGENTS/MIDAS/notes/zhao_r\\303\\251futation.md"\n'`
  - `last_self_commit(ZHAO) = ('2026-09-25','0e2d251')`, and desk_activity returns the same `0e2d2519a`. **False ACTIVE.**
  - This is the exact MIDAS/ZHAO shape the repair was built to reject. It only escapes because of one accented filename.
  - Quoted paths since 9/1: 0 (`pop.py`).
- **Proposed change:** Any path beginning with `"` ⇒ return False (unparseable fails toward DARK, condition 9). Or run `git -c core.quotePath=false`, which still quotes tab, newline and `"`, so keep the guard either way. Add a fixture. Population effect: 0 disagreements (probe-4).

### ❌3: Paths the repo's own perimeter declares as owned are treated as "un-homed ⇒ own" (CX4, CX7)
- **Claim:** The fallback `return True` covers any path that is not `AGENTS/…` and not in `_PROME_PERIMETER`. That set includes paths the repo's recorded perimeter assigns to an owner:
  - `BOARD/**`: WALTER's board (`AUDIT_PERIMETER.tsv` "WALTER's signal board")
  - `.claude/skills/**` and `.claude/agents/**`: PROME, OWNED
  - `docs/**`: "shared root docs — Will-gated"
  - `memory/*.md`: SHARED daily notes
  - `reviews/**`: external audits

  So WALTER or PROME work under a loose subject naming a desk is attributed to that desk. This breaks condition 3 (root/shared-doc edit ⇒ not attributed). Condition 4's "un-homed" grant was written for `scripts/`, not for surfaces that already have an owner.
- **Artifact:** `PROME/tools/spawn_list.py:105` (`_PROME_PERIMETER` omits `.claude/`, `docs/`, `BOARD/`, `reviews/`) and `:146`. For comparison: `PROME/state/AUDIT_PERIMETER.tsv` rows `.claude/skills/**`, `.claude/agents/**`, `memory/*.md`, `BOARD/**`, `docs/**`, `reviews/**`.
- **Command:**
  - `cx4/`: `YURI onboarding recorded in provenance` → `docs/CANON_PROVENANCE.md`, `memory/2026-09-25.md`, `.claude/skills/boot/SKILL.md`
  - `cx7/`: `YURI signal routed to BOARD (WALTER sweep)` → `BOARD/2026-09-25/SIG-967.md`, `.claude/skills/boot/SKILL.md`
- **Observed:**
  - `last_self_commit(YURI) = ('2026-09-25','6bda687')` and `('2026-09-25','17d5dd9')`. desk_activity agrees on both. **False ACTIVE.**
  - Population since 9/1: 5 loose-form attributions rest on un-homed paths only: DAEDALUS `7ae7fa833` / `8fbf816fa` (scripts/), PROME `f8711e323` (FORGE/, own perimeter), PROME `11fcad39d` / `ae8d8e9f3` (memory/). All 5 are genuine, so 0 false.
- **Proposed change:** For a domain desk, treat `.claude/`, `docs/`, `reviews/` as PROME/shared perimeter and `BOARD/` as WALTER's home. Better: derive both lists from `PROME/state/AUDIT_PERIMETER.tsv` (see ⚠️6). For an ambiguous SHARED path (`memory/*.md`), neither corroborate nor refute: it counts as "no path evidence". Re-run the condition-7 population after the change. The 5 genuine un-homed commits above must stay attributed (none touch the added prefixes).

---

## ⚠️ Findings

### ⚠️1: A PROME consume-move inside a desk's own inbox is attributed to that desk (CX2)
- **Claim:** Rename detection is on by default for `git log` (git 2.43), so `--name-only` prints only the NEW path. A move `AGENTS/BOND/inbox/x.md → AGENTS/BOND/inbox/processed/x.md` shows only the `processed/` path, which is under BOND's home, so the commit counts as BOND's. `--no-renames` would not help: both paths are under the home.
- **Artifact:** `spawn_list.py:137`; the log commands at `:168`, `desk_activity.py:102`.
- **Command:** throwaway `cx2/`: `git mv` plus commit `BOND packet -> processed (PROME L0 drain)`.
- **Observed:**
  - paths: `['AGENTS/BOND/inbox/processed/2026-09-20_from-PROME_t.md']`
  - `last_self_commit(BOND) = ('2026-09-25','6cb0a7e')`. False ACTIVE if PROME ever does this.
  - Fleet canon (`AUDIT_PERIMETER.tsv`: "consumption is the RECIPIENT's act") says a `processed/` move inside a desk's inbox is the desk's act, and L0 drains are run by spawned desk sessions. So this matches canon, not a present defect.
- **Proposed change:** Declare it as residue R5 in the acceptance file. Also answers the task's rename question: renames matter only in this shape, and a move OUT of the home is shown by its destination only, which fails toward DARK.

### ⚠️2: Merge commits have no `--name-only` paths, so they are attributed by subject (CX5)
- **Artifact:** `spawn_list.py:146` (empty `paths` ⇒ True).
- **Command:** throwaway `cx5/`: `git merge --no-ff side -m "TERRY sweep merged by PROME"`.
- **Observed:** record `'\x1eTERRY sweep merged by PROME\n'` (no paths). `last_self_commit(TERRY) = ('2026-09-25','6d19ebf')`. The documented `--allow-empty` choice (R2) silently extends to merges, which are not empty. The fleet workflow is rebase-only (safe-push is ff-gated), so this is latent.
- **Proposed change:** Add `%P` to the format and treat a multi-parent record as ambiguous (False). Or add `--no-merges`. Declare it beside R2.

### ⚠️3: `_SHARED_LOGS` already misses a declared carve-out ② log
- **Artifact:** `spawn_list.py:107` versus `AGENTS/DAEDALUS/BLUEPRINTS/DELEGATION_TIER.md` §DIGEST ("`AGENTS/SELF_RULINGS.tsv` … carve-out ②"). `AGENTS/VOCABULARIES.tsv` is also a top-level `AGENTS/` file.
- **Command:** `ls AGENTS | grep -v -E '^[A-Z][A-Z0-9-]+$'`, then `git log --since=2026-09-01 --format=%h -- AGENTS/SELF_RULINGS.tsv` and `git show --name-only`.
- **Observed:**
  - A loose-form row-only commit to `AGENTS/SELF_RULINGS.tsv` hits `:143` ("another desk's home") and returns False, i.e. it fails toward DARK.
  - The 2 real commits (`ec166d1ae`, `689c54a53`) are OSPREY strong-form, so they are unaffected.
  - R4's "will drift" has already happened at install.
- **Proposed change:** Add `AGENTS/SELF_RULINGS.tsv`, or source the list from a registry (⚠️6). A top-level `AGENTS/<file>` should not be classed as "another desk's home" at all.

### ⚠️4: A lane packet two levels deep is not a packet
- **Artifact:** `spawn_list.py:106` (`(/[^/]+)?`, one lane level). `AUDIT_PERIMETER.tsv` defines `AGENTS/*/inbox/**` as "EVERY inbox path at EVERY depth".
- **Command:** throwaway `cx6/`: `OTTO s023 packet to WAL` → `AGENTS/WAL/inbox/WALTER/urgent/SIG-9.md`.
- **Observed:** `last_self_commit(OTTO) = None`. It fails toward DARK (condition 9 holds), but the two definitions of "a packet" disagree. Other `_PACKET` edges: `inbox/processedX.md` is a packet ✔; `inbox/processed-archive/x.md` is a packet; `inbox/lane/processed/x` is not (3 levels, DARK); `PROME/inbox/<file>` is a packet ✔; `PROME/inbox/processed/…` is not ✔.
- **Proposed change:** Align with AUDIT_PERIMETER's any-depth rule while excluding any `/processed/` segment. Low priority.

### ⚠️5: `desk_activity.last_commit` now imports `spawn_list` lazily, which pulls in cwd-dependent import side effects
- **Artifact:** `PROME/tools/desk_activity.py:99-101`.
- **Command:** `cd <SP> && python3 cx.py <SP>` (cwd outside the repo).
- **Observed:**
  - `ModuleNotFoundError: No module named 'docket_view'`. spawn_list resolves `ROOT` from the cwd at import (`:36`, `:68-71`), not from desk_activity's `root` argument.
  - Inside `capture()`, that ImportError is not in `except (OSError, ValueError, TimeoutExpired)` (`desk_activity.py:131`), so it propagates instead of marking the desk incomplete. It still fails loud, not silent.
  - The only production caller, `session_presence.py:12`, already imports spawn_list at load inside its DID-NOT-RUN guard, so there is no new production failure path today.
  - `sys.path.insert` runs on every call, one per owner per capture.
- **Proposed change:** Move `attributed` / `grep_pattern` / `parse_log_records` into a side-effect-free module that both files import at top level. Or at least hoist the import to module top and guard `sys.path` against duplicates.

### ⚠️6: A registry exists: `_PROME_PERIMETER` could be read, not hand-maintained (answers R4)
- **Claim:** `PROME/state/AUDIT_PERIMETER.tsv` is a recorded, ordered, first-match-wins path→class manifest (OWNED / SHARED / EXCLUDED, with a reason per row). `PROME/tools/argus_scope.py:58` (`load_perimeter`, fails loud on malformed rows) and `:103` (`classify`, with `_match` implementing `*` / `**` without separator leakage) already load and apply it.
- **Artifact:** those two, plus the A2 rule in its header: "the perimeter is DECLARED here, never reconstructed … in code".
- **Command:** `ls PROME/registry` (READS / WQ_* / corrections_receipts, with no perimeter); `ls scripts | grep -iE 'argus|scope|perim'`; `grep -rlni perimeter AGENTS/DAEDALUS/BLUEPRINTS/ PROME/tools/*.py scripts/*.py`; `cat PROME/state/AUDIT_PERIMETER.tsv`.
- **Observed:**
  - **VERIFIED** that the registry exists. It is not a drop-in: its question is "is this PROME's output?", not "which desk owns this path?". It disagrees with `_PROME_PERIMETER` on `.claude/**`, `docs/**`, `BOARD/**`, `reviews/**`, `memory/*.md` (the source of ❌3), and on inbox depth (⚠️4).
  - For `_SHARED_LOGS`: **SEARCH-NOT-FOUND** for a registry of carve-out ② logs. Searched `scripts/*.py`, `scripts/*.sh` (incl. `orphan_check.sh`), `PROME/tools/*.py`, `AGENTS/DAEDALUS/BLUEPRINTS/*.md` for `SHARED_LOG|shared_log|carve-out 2|carve.out ②|CORRECTIONS.tsv`. The only hits are prose declarations (`DELEGATION_TIER.md:52`, root `CLAUDE.md` ②), and one is already missing (⚠️3).
- **Proposed change:** Build the non-home side of `attributed` from `argus_scope.load_perimeter()` + `classify()`:
  - OWNED ⇒ PROME's (refutes a domain desk)
  - EXCLUDED `AGENTS/**` / `BOARD/**` ⇒ another owner's
  - SHARED ⇒ no evidence
  - UNATTRIBUTED ⇒ the current "un-homed" grant

  Add a SHARED-LOG row class (or a sibling registry) so carve-out ② logs are declared once. Not required for this repair, but it closes R4 structurally and fixes ❌3 by construction.

---

## ✅ Findings

| # | Claim | Artifact | Command | Observed | Change |
|---|---|---|---|---|---|
| ✅1 | Suites green, counts exact | `PROME/tools/tests/test_spawn_list_desk_commit_attribution_L455.py` | `python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_spawn_list_desk_commit_attribution_L455.py`; `python3 PROME/tools/spawn_list.py --selftest`; `python3 -W error::ResourceWarning PROME/tools/tests/test_spawn_list_fail_closed.py`; `grep -c 'def test_'` | `Ran 18 tests … OK`, `grep -c` = **18**; `selftest PASS 11/11`; `test_spawn_list_fail_closed: PASS 15/15`, `grep -c 'def test_'` = **0** (script-style checks, not `def test_`, so the 15 is its own printed count) | Note in README that `grep -c` does not count fail_closed |
| ✅2 | Cond 1 ORDINARY: 7 forms attributed on a home path | `spawn_list.py:130-138` | suite `test_ordinary_seven_forms_attributed` | pass; the ordinary own-commit is attributed | none |
| ✅3 | Cond 2 OVERLAP: WAL/WALTER at the word boundary AND at the path; RED/REDACTED likewise | `:104`, `:108`, `:115-117`, `:136` (`AGENTS/WAL/` has a trailing `/`) | suite overlap tests; my `loc/` repo: `git log -E --grep='^WAL([^A-Za-z0-9_]|$)'` under LC_ALL=C / en_US.UTF-8 / C.UTF-8 | only `WAL-x hyphen` matched, `WALa…` rejected in all three locales. No hyphenated desk dirs exist (`win.py`) | none |
| ✅4 | Cond 3 on the five named SHAs + body-line mention | `:129-146` | `c7.py` | REJECTED = exactly `c1405c40e`, `2e38b1f24`, `873e7d82c`, `900afe854`, `f4a509844` | see ❌1–3 for the latent gaps |
| ✅5 | Cond 4 carve-outs: packets into other desks, `memory/auto/`, `scripts/`, empty marker | `:141`, `:146` | suite + `pop.py` | all attributed; OTTO `43c3f80c3` is the only no-path loose-form attribution in the population, and it is genuine | none (R2 declared) |
| ✅6 | Cond 5 fail-closed survives in both readers | `spawn_list.py:173-179`; `desk_activity.py:26-31`, `:131` | suite `test_git_failure_still_err`; code read | `!ERR` returned; `desk_activity.git()` raises ValueError on rc≠0 and `capture()` marks the desk `complete: False` with an error, never an empty result | none |
| ✅7 | Cond 7 POPULATION reproduced independently | `:120-146` | `python3 <SP>/c7.py` (git log `--since=2026-09-01`, HEAD `1a816db51`) | commits **3877**, LOST **0**, GAINED **383**, REJECTED **5**, identical to the implementation record | none |
| ✅8 | Prefilter (git ERE) and Python re-check agree; no subject the Python side would attribute is dropped by `--grep` | `:111-117` | `python3 <SP>/agree.py` (46 desks × since 9/1) | prefilter drops total **0**. Body-line grep hits are rejected by the subject re-check (`%s` only, so multi-line bodies never enter the header) | none |
| ✅9 | R3 `-n 40` window: no truncation, no regression against the old reader, `--until` interaction sound | `:168-171` | `python3 <SP>/win.py`, 46 desks × `--until` ∈ {none, 2026-09-20, 2026-09-10, 2026-09-01}, comparing n=40 vs unlimited vs old reader | flags **0**. Deepest newest-own-commit rank inside the 40-window: RAV 15, then VULCAN 5. My own first run reported 175 false truncations from a probe-script argument bug (`-n` placed before `log`); fixed and re-run, and recorded here because it was my instrument error, not the tool's | none; R3 margin is currently large |
| ✅10 | `parse_log_records` is safe on `%x1e` | `:149-155` | `cx3`/`cx5` raw records; code read | the subject cannot hold a newline; tab-in-subject survives `split("\t", 2)`; git C-quotes control bytes (incl. 0x1e and newline) in paths; an empty-path record parses to `[]` | quoted paths → ❌2 |
| ✅11 | Cond 8 SIBLING parity | `desk_activity.py:96-109` | suite `test_sibling_desk_activity_agrees`; every CX above | identical verdict on all 8 counterexample commits (cx1–cx7; cx6 = None/None). The only designed difference: desk_activity takes no `--until` and uses `%H`/`%cI` | none |

Condition 6 (concurrent activity): the N/A is justified. The reader reads committed history and the caller re-reads each boot. Condition 9 holds on everything in ❌1–3's complement; ❌1–3 are its violations.

---

## Probe-4: one fix that closes ❌1 and ❌2 and is population-neutral
Tested against the installed function in `fixprobe.py` and the heredoc run:

```python
def attributed4(desk, subject, paths):
    if S.STRONG(desk).match(subject): return True
    if not S.subject_pattern(desk).match(subject): return False
    if any(p.startswith('"') for p in paths): return False          # ❌2: unparseable path -> DARK
    home = "PROME/" if desk == "PROME" else f"AGENTS/{desk}/"
    if any(p.startswith(home) and not S._PACKET.match(p) for p in paths): return True
    if any(p.startswith(home) for p in paths): return False         # ❌1: only mail INTO the named desk -> sender's
    return S.attributed(desk, subject, paths)
```

Population disagreements with the installed rule: **0** (3,877 commits × 46 desks). CX1 / CX1b / CX3 flip True → False. ❌3 needs the perimeter change (⚠️6) on top of this.
