# 2026-09-24 — LOCAL TOOLS BUILD: render_directory `--check` dry run · walter_route_check drop count + ROSTER screen

**Builder:** DAEDALUS build subagent (team-lead commission). **Standard:** `BLUEPRINTS/CHECK_STANDARD.md` §3: every behaviour change was RUN, with the alert output on a capable case and the clean output on a clean case pasted below. **Files changed (2, both DAEDALUS-owned, uncommitted, git not mutated):** `AGENTS/DAEDALUS/scripts/render_directory.py` (+28/−3 net lines) · `AGENTS/DAEDALUS/scripts/walter_route_check.py` (+99). Pre-edit copies are in the session scratchpad at `fix-local-tools/*.orig`.

| Repair | Defect | Fix | rc contract |
|---|---|---|---|
| 1 | `render_directory.py --check` WROTE `FLEET_DIRECTORY.md`: the flag was never parsed (no argparse), so it was ignored (PROME L446, `PROME/plans/2026-09-23_L446-roster-cadence-section-fix.md:32`) | `--check` renders in memory, runs every guard unchanged, prints `CHECK ONLY — … NOT written (would change: yes/no, +N/-N bytes; on disk X B → render Y B)` and `CHECK ONLY — rc=N`, never writes | **UNCHANGED:** 0 clean · 1 REVERSE-GUARD (ungraded ACTIVE/TIER-2) · nonzero via `die()` on a structural FAIL. The `--check` run exits with the same rc a writing run would |
| 2a | OTTO counted "0 WALTER drops all-time" | New per-desk WALTER-lane drop count, recognising `from-<AGENT>` AND `SIG-<AGENT>-WALTER-` (case-insensitive), with each form reported | Census rc **UNCHANGED** 0/1/2. The new `--drops [DESK…]` mode: 0 = printed · 2 = git log failed |
| 2b | A RETIRED desk could show as OWED | ROSTER screen. A desk ROSTER marks retired prints `RETIRED — not owed`. ROSTER unreadable → `UNSCREENED` | **UNCHANGED.** The screen is reporting only; a retired desk's canon row still counts toward rc=1 (see residue) |

---

## Repair 1 — `render_directory.py --check`

**Diff:** `main()` sets `check_only = "--check" in sys.argv[1:]`. The single `OUT.write_text(...)` becomes an `if check_only:` branch that runs a difflib line diff of the render against the file on disk (bytes of added and removed lines) and prints the CHECK ONLY line. The `else:` branch holds the original write and the original `wrote …` line. One `CHECK ONLY — rc=N` line prints before the existing `sys.exit(1)`. The docstring states the flag. Nothing else moved.

**Defect reproduced first (ORIGINAL script, mirror tree = copies of ROSTER + FLEET_MAP + FLEET_DIRECTORY):**
```
md5 before 276462fca389cdb1ac9bb94b6a14da5a
wrote AGENTS/DAEDALUS/FLEET_DIRECTORY.md  (42 agents: ...)          <- --check passed, file written
rc=1
md5 after  850af9b5cdf496b7bb411c00ee301cbf  (11286 B)
```

**Capable case: LIVE tree, fixed script, `--check` (the YURI guard fires, nothing is written):**
```
276462fca389cdb1ac9bb94b6a14da5a  AGENTS/DAEDALUS/FLEET_DIRECTORY.md
rendered in memory AGENTS/DAEDALUS/FLEET_DIRECTORY.md  (42 agents: {'ACTIVE': 34, 'TIER-2': 4, 'DORMANT': 2, 'SPECIAL': 2}; dropped ['HERMES', 'YEYOU'])
CHECK ONLY — FLEET_DIRECTORY.md NOT written (would change: yes, +928/-464 bytes; on disk 10822 B → render 11286 B)
   not rendered by design — ARCHIVE SOURCES: do not launch
   ... (9 by-design lines, identical to a writing run)
⚠️  REVERSE-GUARD: 1 ACTIVE/TIER-2 agent(s) have NO FLEET_MAP row: ['YURI'] — rendered ⚠️ UNGRADED; register them (PAT-047 tail)
CHECK ONLY — rc=1 (the rc a writing run would return)
rc=1
276462fca389cdb1ac9bb94b6a14da5a  AGENTS/DAEDALUS/FLEET_DIRECTORY.md     <- identical; git status: unmodified
```
**Write path on the SAME tree (mirror, so the live generated file is not touched; DAEDALUS regenerates it with the YURI row):**
```
NEW  --check    md5 276462fc… → 276462fc…  rc=1   (not written)
NEW  no flag    md5 → 850af9b5cdf496b7bb411c00ee301cbf  rc=1   (writes)
ORIG no flag    md5 → 850af9b5cdf496b7bb411c00ee301cbf  rc=1
FILE byte-identical orig vs new · STDOUT byte-identical orig vs new     <- no-flag behaviour unchanged
```
**Clean/unchanged cases:**
```
--check right after a write:  CHECK ONLY — FLEET_DIRECTORY.md NOT written (would change: no, +0/-0 bytes; on disk 11286 B → render 11286 B)
                              CHECK ONLY — rc=1
mirror + synthetic YURI row:  CHECK ONLY — ... (would change: yes, +472/-464 bytes; on disk 11286 B → render 11294 B)
                              CHECK ONLY — rc=0      rc=0, md5 unchanged 850af9b5…
```
**Residue (repair 1):** (i) Other arguments are still ignored silently, as before. That was left alone so a no-flag run stays byte-identical. (ii) Every render differs from a file rendered on another day, because of the `Generated {date}` stamp. "would change: yes" across days can therefore be stamp-only. (iii) The `die()` structural FAILs exit before the write/check branch, so they are identical in both modes; that path was not re-exercised. (iv) The live `FLEET_DIRECTORY.md` is still the 9/18 render (10,822 B) and still lacks YURI. DAEDALUS owns that regeneration.

---

## Repair 2 — `walter_route_check.py`

**⚠️ Premise correction:** the tool **never counted WALTER drops**. Before this build its only outputs were the leg-A canon phrase census and OWED list. OTTO's "0 all-time" came from a **hand grep** in `runs/2026-09-17_WIRING_SWEEP_02_JUDGMENT_W1.md:17` (`grep "AGENTS/WALTER/inbox.*from-<DESK>"`), which fed the OTTO row at `:42`/`:58`/`:66`/`:290` and the summary at `_JUDGMENT.md:6`. The fix therefore **mechanizes** that count inside the tool with both forms, so the hand recipe cannot recur. The run docs themselves were not edited; that amendment belongs to DAEDALUS.

**Diff:** `DROP_FORMS` (two regexes: `(?:^|_)from-<AGENT>`, `^SIG-<AGENT>-WALTER-`, re.I). `walter_drops()` runs one `git log --diff-filter=A` over `AGENTS/WALTER/inbox/**`, counts distinct basenames (a file re-added under `processed/` counts once) and collects files with no sender token as UNATTRIBUTED. `drop_line()` prints the per-form counts plus the first/last add date. `roster_retired()` reuses `render_directory.retired_from_roster` (one parser, not a copy) and returns None on failure, which is printed as UNAVAILABLE. `main()` adds the `--drops [DESK…]` mode, runs the OWED line through the screen, and prints the drop line for each flagged desk. The docstring documents both additions and says neither moves the rc.

### 2a — capable case: OTTO 0 → 17
```
$ walter_route_check.py --drops OTTO LIQUID
  OTTO: 17 WALTER-lane drop(s) all-time (from-<AGENT>: 0 · SIG-<AGENT>-WALTER-: 17, first 2026-04-15 · last 2026-09-02)
  LIQUID: 6 WALTER-lane drop(s) all-time (from-<AGENT>: 6 · SIG-<AGENT>-WALTER-: 0, first 2026-08-23 · last 2026-09-22)
  UNATTRIBUTED (no sender token, not assigned to any desk): 17
rc=0
```
**17 agrees with the lead's git command** (`… | grep SIG-OTTO-WALTER | sort -u | wc -l` → 17; 17 distinct basenames too). **Clean case (unchanged):** LIQUID 6 → 6, and likewise BROCK 10 → 10 and LABOR 5 → 5, all from-form only.

**Sweep: every desk whose count changes under the widened recogniser** (before = from-form only, after = union):

| Desk | Before | After | SIG-form files |
|---|---|---|---|
| **OTTO** | **0** | **17** | 17 |
| VIOLET | 4 | 6 | 2 |
| CARL | 1 | 2 | 1 |
| PROME | 89 | 90 | 1 |
| SAM | 11 | 12 | 1 |

The other 28 desks with any drop are unchanged. **Conservation:** 269 from-form + 22 SIG-form = 291 attributed, + 17 unattributed = **308 = distinct basenames ever added** ✓ (343 by path; the gap is re-adds under `processed/`).

### 2b — ROSTER screen: YEYOU before/after
```
BEFORE  DESKS OWED A PACKET (1): YEYOU                                       rc=1
AFTER   DESKS OWED A PACKET (0): none
        RETIRED — not owed: YEYOU (PROME/ROSTER.md marks it RETIRED; its canon rows still count toward rc)
        WALTER-LANE DROPS for flagged desks (practice beside canon):
            YEYOU: 0 WALTER-lane drop(s) all-time (from-<AGENT>: 0 · SIG-<AGENT>-WALTER-: 0)
                                                                              rc=1
```
The only diff between the full live runs before and after is those lines. `--selftest` rc=0 is unchanged (LIQUID pre-fix hits, OTTO pre-fix misses as declared).

**Clean case: an active desk stays OWED.** Harness `fix-local-tools/harness_b.py` injects the LIQUID pre-fix blob (`ff478f328^`) into `scan_tree` and runs the real `main()`:
```
DESKS OWED A PACKET (1): LIQUID
RETIRED — not owed: YEYOU (...)
    LIQUID: 6 WALTER-lane drop(s) all-time (...)          rc=1
```
**Fail-visible case (ROSTER unreadable, the same harness with ROOT pointed away for the screen only):**
```
ROSTER SCREEN UNAVAILABLE: FileNotFoundError: ... '/nonexistent/PROME/ROSTER.md'
DESKS OWED A PACKET (2, UNSCREENED — ROSTER unreadable): LIQUID, YEYOU
```
ROSTER's retired set today is BUFFER, DARWIN, DOC, EARNINGS, FOREX, HERMES, REITS, TRADES, YEYOU.

**Residue (repair 2):**
1. **rc unchanged by instruction.** The live census still exits **rc=1** although the only ROUTE-AROUND row is on retired YEYOU. A consumer that reads rc=1 as owed work is still misled. Closing that means changing the §9 contract or trashing/freezing YEYOU's canon; either needs a DAEDALUS/Will ruling.
2. **HERMES cannot appear in OWED at all.** It has no `AGENTS/HERMES/` dir, and a DEAD-ROUTER row is attributed to the desk whose canon names HERMES. The screen covers it anyway.
3. **17 UNATTRIBUTED WALTER-inbox files** (`*_handoff.md` ×12 from June–July, `2026-09-10_to-WALTER_…`, `PROME-20260510-…`, `README.md`, `.gitkeep`, `.gitignore`, `.consumed.tsv`) are assigned to no desk. A desk whose drops use a third form stays undercounted, and the printed count is the tell.
4. **Git-added files only.** An uncommitted drop is invisible.
5. **Records now stale (not edited, owner = DAEDALUS):** `runs/2026-09-17_WIRING_SWEEP_02_JUDGMENT_W1.md` (OTTO "0 — all-time", `:42/:58/:66/:290`) and `_JUDGMENT.md:6`. OTTO's own rider stands: the 9/12 `2a02ed3e0` ASK-answer carried a firing with no WALTER cc. So OTTO reads "one uncc'd firing, lane exercised 17×", not "lane never exercised".

---

## §Addendum — rc vs retired desks (team-lead ruling, 2026-09-24)

**The ruling was branch-conditional, and the docstring selects branch 2.** It defined rc 1 as `>=1 ROUTE-AROUND row` (a claim about rows, not about owed desks). So **rc stays unchanged** and an explanatory line is added. **Docstring/behaviour disagreement found and fixed:** the code has always exited 1 on DEAD-ROUTER rows too (`counts["ROUTE-AROUND"] or counts["DEAD-ROUTER"]`), but the docstring named ROUTE-AROUND only. The docstring now reads `0 = no ROUTE-AROUND or DEAD-ROUTER rows · 1 = >=1 ROUTE-AROUND or DEAD-ROUTER row in ANY scanned charter, a RETIRED desk's charter included · 2 = cannot certify`. The code was not changed to match the old text.

**Diff:**
- `census_rc(rows)` is now the single home of the rc expression. `main()` exits with it, and its value is the same as the old inline expression.
- `owed_split(rows, retired)` returns (owed, retired desks, rc-row count, of which retired). It replaces the inline split.
- `rc_basis_line()` prints on every run.
- `drill_retired_only()` is wired into `selftest()`, so it runs on `--selftest` and at the head of every census run; a drill FAIL makes selftest return rc 2.

**Live run (the retired-only case, rc=1 by contract):**
```
DESKS OWED A PACKET (0): none
RETIRED — not owed: YEYOU (PROME/ROSTER.md marks it RETIRED; its canon rows still count toward rc)
RC BASIS: rc=1 counts 1 ROUTE-AROUND/DEAD-ROUTER row(s) in EVERY scanned charter (1 of them on RETIRED desks); DESKS OWED lists live desks only — rc=1 is a claim about canon text, not about work owed.
rc=1
```
The diff against the original run consists only of the two drill lines, the OWED/RETIRED/RC BASIS/drop lines, and nothing else. `--selftest` rc=0. `--drops OTTO` still reads 17.

**Drill: alert and clean outputs (CHECK_STANDARD §3):**
```
clean (real helpers):   PASS  retired-only drill: OWED none · RETIRED YEYOU · rc=1 · basis '1 of them on RETIRED desks'
                        PASS  control arm: active LIQUID stays OWED beside retired YEYOU      selftest rc=0
mutation (owed_split    FAIL  retired-only drill: got owed=['YEYOU'] gone=[] n=1 n_ret=0 rc=1
 ignores ROSTER):       FAIL  control arm: got owed=['LIQUID', 'YEYOU'] gone=[] n=2 n_ret=0      selftest rc = 2
```
Harness with active LIQUID injected: `OWED (1): LIQUID` · `RC BASIS: ... 2 row(s) ... (1 of them on RETIRED desks)` · rc=1. With ROSTER unreadable: `OWED (2, UNSCREENED ...)` · `RC BASIS: ... (retired split UNKNOWN — ROSTER unreadable)` · rc=1.

**Consumer survey (`grep -rn walter_route_check`, excluding inbox/runs/archive):**
- **No code invokes it and nothing mechanical keys on rc 1.** The only code reference is `scripts/pipeline_rc_guard.py:198` (`THREE_STATE_TOKENS`). That is a PreToolUse lint that warns when a tool which reserves rc 2 is piped and `$?` is read. It keys on the tool NAME in command position, not on rc 1's meaning.
- **`CHECKS.tsv:43`** (a row someone else added this session) says invocation is "on demand at the Wiring Sweep; no boot or closeout step names it" (MANUAL-BY-DESIGN). **Its gap cell still says "rc is unchanged by the screen, so the live census still exits rc 1 on retired YEYOU's canon row … needs a ruling"**, which is now ruled. That cell is stale and was not edited here (not my file).
- **Human rc readers:** the desks used `rc=0` as their discharge criterion. LABOR `STATUS_DETAIL.md:424` ("re-run for rc=0"), LABOR `board_log.tsv:28`, LIQUID `board_log.tsv:226` and `MEMORY.md:9` ("rc=0 on LIQUID"). BROCK `OPEN_ITEMS_2026-09-03.md:26` records `rc=1` on "8 rows, none mine". These are desk-scoped reads of a fleet-wide rc. That is the misreading the RC BASIS line now names. No desk can reach rc=0 while YEYOU's canon row exists.

**Residue (addendum):** (1) The fleet rc can reach 0 only if YEYOU's retired `CLAUDE.md:182` row is frozen, trashed or marked NEGATED; that is a ruling for DAEDALUS/Will, not done here. (2) `CHECKS.tsv:43` gap cell is stale against this ruling (owner: whoever maintains CHECKS; DAEDALUS). (3) There is still no per-desk rc mode, so a desk wanting "rc=0 on MY rows" still has to read the output.
