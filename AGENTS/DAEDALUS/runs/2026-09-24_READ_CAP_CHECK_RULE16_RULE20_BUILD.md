# read_cap_check.py — rule 16 class-row expansion + rule 20 charter line (BUILD RECORD)

**Date:** 2026-09-24 · **Builder:** DAEDALUS build subagent (fix-read-cap) · **File:** `scripts/read_cap_check.py` (repo-root fleet tool) — the only file edited besides this record
**State:** built in the working tree, **NOT COMMITTED** (the subagent was barred from mutating git) · md5 before `14f07a92bb67e1c12b95545ef32b3a85` → after `94d81dbb23cbf89fabec7432fd45bc78` · 112,225 B · `git diff --stat`: +213 / −12
**Standard:** CHECK_STANDARD §2 (perimeter stated in output) · §3 (capable + clean cases run and pasted) · §9 (rc 0/1/2 contract unchanged)
**Ruling basis:** rule 20 → `runs/2026-09-19_READ_CAP_CHARTER_RULING.md`; rule 16 class rows → DAEDALUS 2026-09-24, PROME packet `inbox/2026-09-24_from-PROME_NEXUS-perimeter-undeclared-five-briefs-over-cap-read-cap-lane.md`

## ⚠️ Read first — the brief's premises were false, and one decision is still open

| Premise in the brief | What is on disk (measured 2026-09-24) |
|---|---|
| "only declared class rows are DAEDALUS's" | Five desks have class rows. The **`whole`** ones belong to **DAEDALUS** (`inbox/*.md`), **BROCK** (`inbox/WALTER/*.md`) and **WALTER** (`inbox/DEWEY/*`, `RESEARCH-INTAKE/phone_inbox/signal_*.md`, `outbox/REQ-*.md`, `inbox/*.md`). PROME's and WALTER's `AGENTS/*/STATUS.md` rows are summary/scoped. |
| Clean case = BROCK, "no class rows" | BROCK has a `whole` class row, so its output changes (5 members, all under 70%; rc stays 0). **The clean case was moved to RED**, which is declared and attested and has no glob rows. |
| `--fleet` expected verdict change: none | **WALTER changes ✅ → ⛔ (rc 0 → 1, 2 manifest defects).** Its two conditional classes `outbox/REQ-*.md` and `RESEARCH-INTAKE/phone_inbox/signal_*.md` currently match 0 files. The fleet machine line goes `desks_with_manifest_defect=0 → 1`, and `validate_all` D1 goes **ADVISORY → FINDINGS** (verified by calling `classify_read_cap` on both runs). |
| Five briefs over 60 KB (LABOR 94,318; BOND 73,994) | Re-measured: **LABOR is now 12,885 B** (already remedied, so the packet figure is stale) and BOND is 74,232 B. **7 briefs are over budget and 4 over the cap**; ZHAO, RED and BROCK join the list. |

**⮕ RESOLVED — see §Addendum (lead ruling: empty expansions are discriminated by git history; `EMPTY_CLASS_SEVERITY` retired). The paragraph below is the original open item, kept as history.**
**OPEN (at build time) — DAEDALUS/lead to rule:** under the ruling, an empty expansion is a DEFECT. That is correct for a typo'd glob, but it also fires on a legitimately empty *conditional* class, such as a drained inbox or WALTER's REQ outbox (its own row says "Conditional"). So a desk goes red every time it finishes its inbox. The severity is one constant, `EMPTY_CLASS_SEVERITY = P_DEFECT`. Re-ruling it to `P_ADVISORY` is a one-token change plus one selftest leg: K4's rc expectation becomes (0, 0, 0) and it would then assert the advisory count. I shipped it **as ruled** and flagged it to the lead by SendMessage before finishing. No reply had arrived when this record was written.

## Repair (b) — CLASS rows declared `whole`/`programmatic` are cap-bearing per member

**Diff summary.** `declared_reads()`: a glob row (`*`/`?`) whose mode is in `CAP_BEARING_MODES` is expanded with `glob.glob(os.path.join(base_root, pth), recursive=True)`, keeping files only (normpath'd). Each member enters `cap_bearing` tagged with its class. A single-file row for the same path takes precedence. An empty expansion appends `(EMPTY_CLASS_SEVERITY, "CLASS row … matched 0 files — cannot certify this row")`. `scoped`/`grep`/`summary` class rows are unchanged: visible, never counted. `cap_bearing` values are now 3-tuples `(mode, src, class_glob|None)`, and `declared_reads.class_rows` is reset on every call. The perimeter note adds "N of the measured are MEMBERS of K cap-bearing CLASS row(s)" **only when K>0**, so desks without class rows print byte-identical output. `check_agent()`: members are counted in `rows` (so `reads`, `over_budget`, `over_cap` and `rotation_due` include them, keeping prome_gate's invariant `over_cap ≤ over_budget ≤ rotation_due ≤ reads`), but they print as one `▣` block per class row. Members ≥70% of budget are listed individually, with the PAT-176 stop-distance line; the rest collapse to `N member(s) all under 70% of budget`. Hidden test-only `--reads-path FILE` points at a manifest copy and announces itself on **stderr**, so the stdout contract is untouched. The heuristic perimeter is unchanged.

**Capable case 1 — `--agent DAEDALUS` (live manifest).** Before:
```
  ◦ AGENTS/DAEDALUS/inbox/*.md                —  declared `whole · CLASS row, not a single file` — not cap-bearing, not counted  (DAEDALUS:CLAUDE.md-SPAWN-3b)
READ-CAP-RESULT v1 mode=agent rc=0 assessed=1 desk=DAEDALUS reads=5 over_budget=0 ...
```
After:
```
  ▣ AGENTS/DAEDALUS/inbox/*.md                   declared `whole` · CLASS row — cap-bearing PER MEMBER (rule 16 ruling 2026-09-24): 30 member(s) measured, 0 over budget, 0 over the CAP, largest 9,711 B (30% of budget)  (DAEDALUS:CLAUDE.md-SPAWN-3b)
      30 member(s) all under 70% of budget (<22,785 B)
READ-CAP-RESULT v1 mode=agent rc=0 assessed=1 desk=DAEDALUS reads=35 over_budget=0 over_cap=0 manifest_defects=0 advisories=0 generated_flagged=0 rotation_due=1 active_decisions_over_budget=0 charter_bytes=31931
```

**Capable case 2 — NEXUS briefs (scratchpad manifest copy, `--reads-path`).** This is the brief's row, plus a **test-fixture** `ATTESTATION NEXUS … manifest-complete` row in the COPY. Without that row the tool correctly failed closed with rc 2 UNATTESTED. That first run was also executed and shows that an attestation is required. It is **not** a NEXUS attestation; the live `PROME/registry/READS.tsv` was never edited (`git diff --quiet` clean). The run exited **rc 1**:
```
  ▣ AGENTS/*/NEXUS_BRIEF.md                      declared `whole` · CLASS row — cap-bearing PER MEMBER (rule 16 ruling 2026-09-24): 26 member(s) measured, 7 over budget, 4 over the CAP, largest 137,282 B (422% of budget)  (NEXUS:CLAUDE.md-Consumes)
      🔴 AGENTS/VULCAN/NEXUS_BRIEF.md        137,282 B   422% of budget  OVER THE CAP (253% of the 54,250 B cap)
      🔴 AGENTS/HOMER/NEXUS_BRIEF.md         109,239 B   336% of budget  OVER THE CAP (201% of the 54,250 B cap)
      🔴 AGENTS/BOND/NEXUS_BRIEF.md           74,232 B   228% of budget  OVER THE CAP (137% of the 54,250 B cap)
      🔴 AGENTS/MIDAS/NEXUS_BRIEF.md          72,126 B   222% of budget  OVER THE CAP (133% of the 54,250 B cap)
      🟠 AGENTS/ZHAO/NEXUS_BRIEF.md           46,446 B   143% of budget  over budget
      🟠 AGENTS/RED/NEXUS_BRIEF.md            40,335 B   124% of budget  over budget
      🟠 AGENTS/BROCK/NEXUS_BRIEF.md          34,501 B   106% of budget  over budget
      🟡 WAL 31,999 · BRENT 31,169 · HENRY 29,796 · AEOLUS 25,166 · OTTO 25,160   (rotate-tier, each printed with its own row)
      + 14 member(s) all under 70% of budget (<22,785 B)
READ-CAP-RESULT v1 mode=agent rc=1 assessed=1 desk=NEXUS reads=26 over_budget=7 over_cap=4 manifest_defects=0 advisories=0 generated_flagged=0 rotation_due=12 active_decisions_over_budget=0
```
*(🟡 rows condensed here for length; the tool prints each one in full.)* LABOR (12,885 B) falls in the collapsed 14.

**Capable case 3 — the zero-match branch, live (WALTER):**
```
  ▣ RESEARCH-INTAKE/phone_inbox/signal_*.md        —  declared `whole` · CLASS row matched 0 files — cannot certify this row (counted as a manifest defect below)  (WALTER:7e-f)
  ▣ AGENTS/WALTER/outbox/REQ-*.md             —  declared `whole` · CLASS row matched 0 files — cannot certify this row (counted as a manifest defect below)  (WALTER:9)
READ-CAP-RESULT v1 mode=agent rc=1 assessed=1 desk=WALTER reads=21 ... manifest_defects=2 ...
```

**Clean case — `--agent RED` and `--agent PROME`, measured after (b) and before (a):** `diff before after` printed **nothing** for both, so their output was byte-identical. After (a), RED's only diff is the added charter line and `charter_bytes=42030` at the end of the machine line. PROME's diff also shows three live-file byte changes (DOCKET.tsv, BOARD/INDEX.md, WALTER LAST_COMPLETION.md). Those come from other sessions writing, not from this tool.

**`--fleet` before → after (per-desk rows diffed by script, 37 desks):**
| Desk | Before | After | Why |
|---|---|---|---|
| BROCK | ✅ reads 2 | ✅ reads 7 | +5 inbox members, all under 70% — verdict unchanged |
| WALTER | ✅ reads 19 | ⛔ reads 21, MANIFEST DEFECT | two empty conditional `whole` classes (see OPEN) |
| (35 others) | — | unchanged | — |

Fleet machine line: `desks_with_manifest_defect 0 → 1`; rc stays 1 (it was already 1 because 2/37 desks are over budget). DAEDALUS is SPECIAL-class and not in `--fleet`.

## Repair (a) — the charter is out of perimeter, and the output now says so (rule 20)

**Diff summary.** New `charter_info(name)` returns (relpath, bytes|None) from `desk_home(name)/CLAUDE.md`, so it covers sub-agents and PROME/. New `charter_line(name)` prints the ruled text. It is printed once per **assessed** desk in `--agent` after the verdict line, as an indented sub-line under each `--fleet` row, and in a fleet summary line: "charters: N/37 measured, X B total, largest D Y B — OUT OF PERIMETER by rule 20 (…). ⛔ The over-BUDGET/over-CAP totals above EXCLUDE every charter by design — they are NOT a clean-charter verdict." The `check_agent` result tuple gains a 9th element (charter bytes); both internal unpack sites were updated. **rc and every existing count are unchanged.** `charter_bytes=<n>` (or `NA` if absent) is **appended at the end** of the `--agent` machine line on both the assessed and the rc-2 paths. The fleet machine line is not changed.

**Capable output (DAEDALUS):** `ℹ️  charter AGENTS/DAEDALUS/CLAUDE.md = 31,931 B — OUT OF PERIMETER by rule 20 (harness-injected, context cost not truncation; not graded here; composite-injection advisory is PROME/Will's)`
**Fleet summary (live):** `charters: 37/37 measured, 1,319,006 B total, largest VULCAN 79,332 B — OUT OF PERIMETER by rule 20 …`
**Selftest falsifier:** a 55,027 B charter (over the CAP) leaves rc **0** and `over_budget=0`, and the machine line ends `charter_bytes=55027`. This shows the charter is stated and never graded.

**READ-CAP-RESULT consumers found (grep of `*.py`/`*.sh`/`*.md` repo-wide):**
| Consumer | How it parses | Safe with an appended key? |
|---|---|---|
| `scripts/validate_all.py` `parse_rc_result` (D1, fleet line) | key=value dict, last line wins | Yes. Verified by running `classify_read_cap` on the after-run |
| `PROME/tools/prome_gate.py` `coverage_result` / `summarize_read_cap` (agent/PROME line) | strict key=value; rejects duplicate/malformed tokens; requires the named counts | Yes. Verified live: `summarize_read_cap(after_PROME, 0)` returns the same result as before, with the new key ignored |
| `AGENTS/HANS/scripts/closeout_check.py:117` | regex `READ-CAP-RESULT v1[^\n]*rc=\d` | Yes |
| `PROME/tools/tests/test_boot_coverage.py` | its own fixture string, not this tool's output | Not affected |
| `.md` hits (DAEDALUS runs/profiles/upgrades, CATO run, PROME inbox/proposals) | prose mentions | Not parsers |
No positional parser exists. prome_gate requires **exactly one** line starting `READ-CAP-RESULT`, and no new human line starts with that prefix.

## Selftest totals and rc contract

| | Legs | rc |
|---|---|---|
| Before | **86/86** ✅ | 0 |
| After | **101/101** ✅ (`EXPECTED_LEGS` 86 → 101 in the same edit) | 0 |

15 new legs: K1 (4, class `whole` with a member over budget → counted, rc 1, listed/collapsed) · K2 (2, clean class → rc 0, collapsed line) · K3 (2, class `grep` → not counted, an over-cap member does not move rc) · K4 (3, empty class → typed `EMPTY_CLASS_SEVERITY`, manifest defect, rc 1, "cannot certify") · R20 (4, over-cap charter leaves rc 0, exact line text, `charter_bytes` last field with over_budget=0, fleet sub-line plus summary).
**Falsified by mutants (scratchpad copies):** m1, class expansion disabled → **9 legs fail** (all of K1/K2/K4); m2, `--agent` charter print removed → R20 text leg fails; m3, `EMPTY_CLASS_SEVERITY = P_ADVISORY` → the K4 rc leg fails. Each mutant was caught.
**rc contract (docstring, unchanged):** "0 clean · 1 FINDINGS (≥1 mandated read over budget, OR ≥1 MANIFEST DEFECT) · 2 CANNOT-EVALUATE (no charter / unknown desk / unreadable)". Class members feed the first leg of 1. An empty cap-bearing class feeds the second, as ruled.

## Residue

1. **OPEN ruling:** empty conditional class, DEFECT vs ADVISORY (above). Until it is ruled, WALTER reads ⛔ and `validate_all` D1 reads FINDINGS. The same will hit DAEDALUS and BROCK the moment their inboxes drain to zero.
2. `validate_all.py`'s FINDINGS message still says "declared read missing, or a mode outside the vocabulary" and does not name "class row matched 0 files". That text lives outside this file, so it is not edited here (DAEDALUS scripts/ lane, a Will-visible batch).
3. A class row with a mode outside the vocabulary is still printed as visible with no defect. This is pre-existing behaviour and out of scope; worth a follow-up leg.
4. The charter line is not printed on the rc-2 `--agent` paths (nothing was assessed there, so no count can be misread). `charter_bytes` is still emitted on that machine line.
5. NEXUS is still undeclared in the live manifest. The capable case used a test-fixture attestation in a scratch copy. Filing NEXUS's real declaration is PROME/NEXUS's job.
6. Not committed. This is a behaviour-changing edit to a shared `scripts/` tool, so it goes to the Will-visible batch per the DAEDALUS GIT lane. The committing session should re-run `--selftest` (expect 101/101) and `--fleet`.

Artifacts: `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-DAEDALUS/23c86d4b-580a-416e-8271-107104870b83/scratchpad/fix-read-cap/` (`before_*`, `midB_*`, `after_*`, `nexus_*`, `READS_nexus.tsv`, `mut/`, `read_cap_check.py.orig`).

## §Addendum — empty CLASS row severity: discriminated by git history (lead ruling, 2026-09-24)

**Ruling (team-lead):** an empty cap-bearing CLASS row is neither flatly a DEFECT nor flatly an ADVISORY.
- If the glob has **ever** matched a committed file, it is a legitimately drained conditional class. It prints as an **ADVISORY** (counted in `advisories=`, rc unchanged).
- If it has **never** matched anything, it stays a **MANIFEST DEFECT** (probable typo; fail closed).

**Diff summary.** The `EMPTY_CLASS_SEVERITY` constant is **retired**. One helper replaces it, `class_history(pattern, root)`. It runs read-only `git -C <root> log --format= --diff-filter=AR --name-only -- ':(glob)<pattern>'` and returns the number of distinct paths, or `None` when history is unavailable. Results are cached per (root, pattern).
- It returns a count > 0 → **ADVISORY** `CLASS row … matched 0 files today (N files matched historically) — correctly quiet, not counted`.
- It returns 0 → **DEFECT** `… has NEVER matched a committed file in git history — probable typo; cannot certify this row`.
- It returns `None` (not a repo, git missing or timed out) → **DEFECT** `… git history is UNAVAILABLE — cannot prove it drained`. This fails closed; it is my addition beyond the ruling's two cases.
- Two deliberate deviations from the brief's literal command. `--diff-filter=AR` instead of `A`, so a file `git mv`'d into the class path counts as a match. `:(glob)` magic, so `*` stops at `/` exactly as `glob.glob` does; plain git pathspec `*` crosses directories.
- Cost: 0.46 s for one pattern over 14,068 commits; the whole `--fleet` run takes 0.81 s.

**Selftest:** 101 → **106/106** ✅ rc 0 (`EXPECTED_LEGS` updated in the same edit). The old K4 (3 legs) is replaced by 8:
- 1 fixture leg: a throwaway git repo built inside the tempdir, never the project repo. It is committed with hooks disabled, and the committed file is then deleted to simulate a drained class.
- **K4a**, never matched (3 legs): DEFECT, rc 1, manifest_defects 1, "probable typo".
- **K4b**, drained (3 legs): ADVISORY with "(1 files matched historically)", rc **0**, advisories 1, defects 0, "correctly quiet, not counted".
- **K4c**, history unavailable (1 leg): DEFECT.

**Falsified by mutants:** m4, `class_history` hard-wired to 0 (flat DEFECT) → **K4b ×3 + K4c fail**. m5, hard-wired to 1 (flat ADVISORY) → **K4a ×3 + K4c fail**.

**`--agent WALTER`: still rc 1. Verified against history, not assumed. Only ONE of its two globs has history:**
```
  ▣ RESEARCH-INTAKE/phone_inbox/signal_*.md        —  declared `whole` · CLASS row matched 0 files, has NEVER matched a committed file — probable typo — cannot certify this row (counted as a manifest defect below)  (WALTER:7e-f)
  ▣ AGENTS/WALTER/outbox/REQ-*.md             —  declared `whole` · CLASS row matched 0 files today (8 files matched historically) — correctly quiet, not counted  (WALTER:9)
READ-CAP-RESULT v1 mode=agent rc=1 assessed=1 desk=WALTER reads=22 over_budget=0 over_cap=0 manifest_defects=1 advisories=1 generated_flagged=0 rotation_due=3 active_decisions_over_budget=0 charter_bytes=63848
```
`RESEARCH-INTAKE/phone_inbox/` **does not exist on disk** and `git log` over the glob returns 0 paths (both `A` and `AR`). Under the ruling this is the right answer: a defect for WALTER to fix. The row is either a wrong path or a gitignored, off-repo intake that git cannot certify. WALTER's row, not this tool, is where the fix goes.

**`--agent DAEDALUS`: a live K4b, arrived unplanned.** The inbox drained to 0 files during this session, so the class row now reads:
```
  ▣ AGENTS/DAEDALUS/inbox/*.md                —  declared `whole` · CLASS row matched 0 files today (294 files matched historically) — correctly quiet, not counted  (DAEDALUS:CLAUDE.md-SPAWN-3b)
READ-CAP-RESULT v1 mode=agent rc=0 assessed=1 desk=DAEDALUS reads=5 over_budget=0 over_cap=0 manifest_defects=0 advisories=1 generated_flagged=0 rotation_due=1 active_decisions_over_budget=0 charter_bytes=31931
```
Under the retired flat-DEFECT constant this run would have been rc 1: exactly the false red the ruling removes.

**`--fleet` original (pre-build) → now:**
| Desk | Original | Now |
|---|---|---|
| BROCK | ✅ reads 2 | ✅ reads 7 (5 inbox members, all under 70%) |
| WALTER | ✅ reads 19 | ⛔ reads 22, 1 MANIFEST DEFECT (phone_inbox) + 1 advisory (REQ drained) |
| YURI | — | ✅ reads 2. **Not this build:** another session regenerated `FLEET_DIRECTORY.md` at 17:10 ET (uncommitted ` M`), which added the desk; `desks` 37 → 38 |

Fleet machine line now: `rc=1 assessed=38 … desks_over_budget=2 desks_over_cap=0 desks_with_manifest_defect=1 desks_with_advisory=1`. `validate_all` D1 → **FINDINGS**. The cause is now WALTER's never-matched phone_inbox row alone, not a drained class. Before this addendum the same verdict came from two empty rows.
RED is unchanged against the prior build (diff, excluding the machine line: empty). The script is **not committed**. md5 is now `11a87f1e7d92b119995ea39c391eba87`; `git diff --stat` is +290 / −12.

**Residue update:**
- Residue 1 is closed by this ruling.
- New: WALTER owes a fix to its `RESEARCH-INTAKE/phone_inbox/signal_*.md` row (wrong path, or re-declare it with a mode/notes that say git cannot certify it). This should go to WALTER as a packet; not sent from here.
- `validate_all` D1's FINDINGS text still doesn't name the "class row never matched" case (residue 2, unchanged).
