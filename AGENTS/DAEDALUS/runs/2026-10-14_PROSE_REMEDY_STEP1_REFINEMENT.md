# Prose-Remedy Census — step-1 refinement for run #2 (built 2026-10-14; slot 10/12, +2d)

**What:** run #1's step-1 refinement list (`runs/2026-10-08_PROSE_REMEDY_CENSUS_01.md` §"Step-1 refinement") is now code: `scripts/prose_remedy_candidates.py`. Before this, step 1 was an inline one-off — the census's own defect class (H-4). Run #2 is due 2026-10-29 (21d after 10/08).

| Fix | Behaviour | Selftest case |
|---|---|---|
| R1 word boundaries | `owed` no longer matches showed/allowed/followed/swallowed/`docket_owed.py`; `needs a` no longer matches "needs attention" | ✓ |
| R2 negation, per occurrence | `no packet owed`, `nothing owed`, `owed none` excluded; a live `owed` elsewhere on the same line still hits | ✓ ×3 |
| R3 resolved text | a line LED by ✅, a token in `~~struck~~`, or a ✅ earlier in the same clause — never a whole mixed line | ✓ ×3 |
| R4 ID ranges | only `rows/IDs/entries ≤N` without a unit, or the `HAW-18+` shape; `≤280`, `≤ 153 cm`, `row ≥60% confidence`, `≤ 32,550 B` stay thresholds | ✓ ×6 |
| R5 widening | `not patched` · `not attempted` | ✓ ×2 |
| R6 perimeter | ROSTER ACTIVE + TIER-2 via `render_directory.parse_roster`, + DAEDALUS, RAV, and PROME at `PROME/`; DORMANT and CATO out | ✓ (40 desks) |

**Selftest:** 21/21, rc 0 read bare. **Fleet run 2026-10-14 20:44 ET (live tree):** v2 = **180** candidate lines over 40 desks / 128 files; v1 on the same tree = 198; v2 **added 4, removed 22**. Desks with 0 candidates: BRENT, HAWK, MIDAS, RAV.

**Run #1's named misses:** ORACLE MAINTENANCE:202 ("not patched") is now caught. FLG STATUS:150 ("Owed by me: …") and MARCO MAINTENANCE:80–81 name no script on the line, so form 1 cannot see them by design — they stay the classifier's to find via form 2 or a by-hand pass. Not claimed as fixed.

**Three defects of my own, caught on the first real-tree runs before shipping (CHECK_STANDARD §3, PAT-146):** (1) the first R4 dropped real thresholds (SHADE's 280bp sustain bar, AEOLUS ≤153 cm, WAL ≤250 ln, LABOR ≥60%); (2) the first R2/R3 dropped whole lines on any negation or ✅ (VULCAN STATUS:103 "④ STILL OWED" vanished); (3) a nested regex `(x+\s*)*` hung on `|---|---|` rows. All three were invisible to the author-written selftest; each now has a case. A first-pass rc was also read through a pager (`tail`) — re-read bare.

**Not a verdict:** a candidate is a line to classify (step 2). Detection read-only; nothing sent.

## Before/after diff (fleet, same tree) — the playbook's no-widening-without-a-diff rule
```
  ADDED-BY-V2	ORACLE	1-script+token	MAINTENANCE.md:188	- **`workbook/LEDGER_GLOB` — NEW.** ORACLE had none, so `ledger_staleness` ran on defaults. ⚠️ **Declaring it did NOT achieve the goal, and 
  ADDED-BY-V2	ORACLE	1-script+token	MAINTENANCE.md:202	- **🔧 NEW TOOL GAP #1 — `polymarket.py history` writes TWO rows stamped with today's date.** `clob_history()` maps every CLOB point to a dat
  ADDED-BY-V2	ORACLE	1-script+token	MAINTENANCE.md:219	## 2026-09-07 — `kalshi.py event <SERIES>` reads a date-stamped series as a delisting (tool gap, logged not patched)
  ADDED-BY-V2	ORACLE	1-script+token	MAINTENANCE.md:230	- **🔧 `polymarket.py pull` reports a RESOLVED market as `PINNED BUT NOT FOUND`, which buries a finding inside a maintenance warning.** Six p
  REMOVED-BY-V2	CREED	1-script+token	CLAUDE.md:85	4c. **🔴 RUN THE THRESHOLD SCAN NOW — `python3 AGENTS/CREED/scripts/threshold_scan.py`** *(built 2026-08-27; ~30ms, read-only, exit 0 clean /
  REMOVED-BY-V2	CREED	1-script+token	LAST_COMPLETION.md:90	`creed_selfcheck.py` **exit 0** *(caught a real KB count drift 19→21 mid-session; fixed by pattern — 5 historical build-record instances del
  REMOVED-BY-V2	DAEDALUS	1-script+token	CLAUDE.md:47	5c. **DOCKET hop check** (gate step B5, added 2026-10-01) — `python3 "$(git rev-parse --show-toplevel)/AGENTS/DAEDALUS/scripts/docket_owed.p
  REMOVED-BY-V2	DAEDALUS	1-script+token	CLAUDE.md:118	- **★ NO GUARD SHIPS UNVERIFIED — adopted 2026-08-03 (Will-approved); canonical text = `BLUEPRINTS/CHECK_STANDARD.md` §3, CITE DON'T RESTATE
  REMOVED-BY-V2	FALCON	1-script+token	CLAUDE.md:339	| `AGENTS/HAWK/scripts/{boot.py,war_monitor.py,thresholds.py,oil_infrastructure.py,sanctions_tracker.py,catalyst_countdown.py,PLAN.md}` | Le
  REMOVED-BY-V2	FALCON	1-script+token	STATUS.md:74	| **DAEDALUS 10/08 asks, DEFERRED with reasons (DONE-WHEN = answered here):** ① leg-2 vintage rule ('grade as first read') and ④ letter clar
  REMOVED-BY-V2	FALCON	1-script+token	STATUS.md:91	**10/10:** `falcon-1010` drained 2 of 2 (WALTER `SIG-W-20261010-002` acted, `SIG-W-20261009-015` noted; board_log rows, `git mv` to processe
  REMOVED-BY-V2	HAWK	2-charter-comparison	CLAUDE.md:69	11. **Workbook / ledgers + predictions** — log new synthesis/dormant facts → `workbook/KB.tsv` (KB-HAWK-224+; pre-split rows ≤223 are frozen
  REMOVED-BY-V2	HAWK	2-charter-comparison	CLAUDE.md:152	| **ID** | KB-HAWK-NNN | Sequential — rows ≤223 are the pre-split, both-theater historical record (frozen, incl. 2 known duplicate IDs 131/1
  REMOVED-BY-V2	LABOR	1-script+token	CLAUDE.md:47	~6s. Runs **five** sub-scripts and feeds B2a/B4/B5/B5b directly: **(a) `labor_data.py`** — live FRED sweep (claims, NFP, U-3/6, JOLTS, temp 
  REMOVED-BY-V2	LABOR	1-script+token	CLAUDE.md:48	> ⚠️ **`--verbose` is MANDATORY, not optional — B2a cannot be run without it.** The default (non-verbose) view **filters to non-🟢 rows**, an
  REMOVED-BY-V2	LABOR	1-script+token	CLAUDE.md:68	> 🔴 **B5b CANNOT SEE A CARD THAT WAS NEVER WRITTEN — this is an inventory check over cards that EXIST.** An empty `docket/` is indistinguish
  REMOVED-BY-V2	LABOR	1-script+token	CLAUDE.md:253	> **Durable home: `STATUS.md` § KEY THRESHOLDS** (re-homed 2026-07-02, DAEDALUS LABOR-10). One source of truth per metric — the live bands/l
  REMOVED-BY-V2	MARCO	1-script+token	STATUS.md:112	| ✅ **DAEDALUS 10/8 sweep answered 10/10:** BDR-01 **graded RESOLVED-CORRECT** (DHS shutdown ran 76 days; twin MAR-27); BORDER/HOUSING/MIGRA
  REMOVED-BY-V2	OSPREY	1-script+token	CLAUDE.md:35	5a-2. **War-risk staleness check at a TIGHT bar (added 2026-07-31).** `python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py
  REMOVED-BY-V2	OSPREY	1-script+token	CLAUDE.md:36	5a-3. **R1 corrections check (fleet-wide — FORUM-6 ruling ①, Will-approved 2026-08-17):** `python3 "$(git rev-parse --show-toplevel)/scripts
  REMOVED-BY-V2	OTTO	1-script+token	MAINTENANCE.md:153	**Trigger:** Boot on 2026-07-25 after a 21-day dark period reported **one** recently-fired catalyst. Running `catalyst_countdown.py` directl
  REMOVED-BY-V2	OTTO	1-script+token	MAINTENANCE.md:324	- **Silent-pass bugs hide in path-rename edits.** `predictions_due.py` returned "ran cleanly, no alerts" when the TSV file didn't exist — a 
  REMOVED-BY-V2	RED	1-script+token	CLAUDE.md:71	9c. **Review-debt check (row-level) — added S33 2026-08-20:** `(cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/RED/scripts/review_d
  REMOVED-BY-V2	RED	1-script+token	MAINTENANCE.md:231	1. **`workbook/PREDICTIONS.tsv` — RED-22 added, and its `Timeframe` cell had to be fixed TWICE.** As registered the cell was prose (*"Resolv
  REMOVED-BY-V2	SHADE	1-script+token	SCRATCH.md:21	**Checks:** canonical `inbox_census.py SHADE`: top-level0 / WALTER0; `corrections_boot_check.py SHADE`: rc0, zero unreceipted NAMED rows; `r
  REMOVED-BY-V2	VULCAN	1-script+token	CLAUDE.md:228	| `tools/test_edgar_watch.py` | **Guard falsification for `edgar_watch.py` (17 checks, offline, no writes).** ⚠️ **NOT decoration — it FAILE
```
