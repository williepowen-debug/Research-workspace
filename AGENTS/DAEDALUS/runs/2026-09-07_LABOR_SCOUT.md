# LABOR — pre-assessment SCOUT · 2026-09-07 (Mon, market holiday) · DAEDALUS, Will-directed

**Purpose:** boot + context read BEFORE the parity assessment Will asked for. Read-only. No LABOR file touched. Grades NOT moved here — this is the inventory the assessment starts from.

## Boot state (DAEDALUS)
- git clean, HEAD == origin/master (`336f2d027`). `corrections_boot_check DAEDALUS` rc 0.
- `sweeps_due`: ⏰ **PROME judgment-tail sweep DUE** (21d, +0d) → surfaced to Will/PROME, not run today. ⏰ **PROFILE-CLOCK: LABOR 31d > 30d** (header 2026-08-07) — the subject's own profile clock fired at this boot; BROCK 47d, OSPREY 23d also past.
- FLEET_MAP LABOR row: L5 · H · scored **2026-09-01**; Gaps cell still says "STATUS 52,803 B = 162% of the read budget" — **stale** (split 9/2 → 31,630 B). Next_upgrade "byte tier at next closeout" — **done 9/2**. Row re-cut owed at the assessment (step 7).

## LABOR — where it stands (artifact-verified, not from STATUS prose)
| Item | Verified | Source |
|---|---|---|
| Last own session | 2026-09-04 (NFP grade + L-27/L-28 + LAB-18/19; 8 own commits 9/4) | `git log -- AGENTS/LABOR/` |
| Unconsumed inbox (root) | **4** packets 9/4–9/6: PROME WQ-175 (build ALFRED vintage table by **9/25**, DOCKET L274) · CARL (retraction verified 6/6, sector-revision finding, nothing owed) · PROME 9/6 (reconcile "no negative print in cycle" vs HAWK Feb −92K; consumer sweep) · RED 9/6 (weight moved 60→58 net-bear; correction-to-correction on the same sentence) | `ls inbox/` |
| PARKED fold-by 9/5, NOT done | (a) OBLIGATION-DIFF on BD-25 split · (b) route-around fix `CLAUDE.md:121,291` — `walter_route_check` still lists LABOR (3 desks owed) | STATUS PICKUP #5 · check run 9/7 |
| Read-cap | STATUS **31,630 B = 97%** of 32,550 (920 B headroom) · LESSONS **28,944 B = 89%** — both rotate-tier; `read_cap_check` rc 0. **WQ-179 ruling due 9/11** (rec (c): grade narrative straight to `STATUS_DETAIL.md`) | `read_cap_check --agent LABOR` · WQ-179 |
| Ledgers | KB/PREDICTIONS/PUBLISHED ok +0d · VX/FLOW FROZEN · TRADE ok +28d · nudge clean · **KB.tsv has NO two-clock header** (git-time fallback; LABOR self-flagged 9/3) | `ledger_staleness LABOR` |
| Predictions | 19 rows: 12 RESOLVED · 6 OPEN · 1 REHOMED; 0 overdue; scoreboard 12 rows as-made 0.299 (current to 8/7 — no resolution since) | `PREDICTIONS.tsv` |
| Cards | 9 in `docket/graded/`, 0 live at top level (all consumed) | `ls docket/` |
| board_log | current to 9/4 | tail |
| claim_check | clean (3 files) | run 9/7 |
| corrections | rc 0, 0 named; no `registry/` dir yet (fine — created on first receipt) | run 9/7 |
| Outbox | root EMPTY; 15 files all under `outbox/delivered/` — the 9/3 OPEN_ITEMS 'filing lag' row was CLOSED at the 9/3 closeout (`04cb48db2`). *(First cut of this row read `outbox/*` as root files — corrected 12:1x.)* | `find outbox -type f` |

## Candidate findings for the assessment (to VERIFY, not yet findings)
1. **NEXUS_BRIEF.md = 83,994 B** — above the 54,250 B harness single-read cap; NEXUS CLAUDE.md:36 reads Tier-1 briefs "in full" ⇒ **truncated read at NEXUS**. Fleet class (VULCAN 125 KB · SAM 110 KB · HOMER 101 KB · LABOR 4th). Exactly the cross-agent-mandated-read blind spot `read_cap_check` declares. Schema §1 says "trim under cap pressure" but names no byte number.
2. **EXIT RULES Kill A carries the Jul-2 vintage run** (`214/148/129/57`) while KEY THRESHOLDS carries the 9/4 vintage (`31/21/162`); same verdict (0 of 3), split stamps — the **G5 class from the 8/7 profile, recurring** (C1 spine-token sweep still stops one section short). Section header "(recalibrated Jul 2)"; **no in-content kill-rail stamp** → `falsification_scan` puts LABOR in "no surface this scan can see"; blueprint §4 grandfathered EXTRACT-AND-STAMP owed.
3. **Re-mark form (WQ-112, blueprint §5):** LAB-12 Confidence cell `8% (live diagnostic; SCORES AS-MADE 60%)` — no dates; LAB-08 cell `4%` with the as-made 65% only in Notes/scoreboard. Canon machine form = `8% [2026-09-04] (was 60% [2026-05-04])`. Forward-only rule, so a parity gap not a violation.
4. **Non-cwd-proof invocations** (PAT-031): `STATUS.md:7`, `CLAUDE.md:42`, `CLAUDE.md:287` (`python3 scripts/…` bare).
5. **No `LEDGER_GLOB`** (7 of 43 desks have one; 1c-bis nudge runs on the default glob — works, but the declared-ledger set is implicit).
6. **Content, LABOR's lane, noted not adjudicated:** `NEXUS_BRIEF.md:3` headline "THERE WAS NO NEGATIVE PAYROLL PRINT IN THIS CYCLE" — RED (9/6) shows six negative MoM months on the current vintage; STATUS BOTTOM LINE says the narrower, correct thing ("the negative July print did not survive revision"). The WQ-175 class on LABOR's own headline; PROME already asked LABOR to reconcile.

## What HOLDS at parity (verified live today)
frozen cards written before data and consumed · predictions resolving off pre-committed bands, matrix moved against own book (31→29/75) · as-made scoreboard with §C 15 gates · C2-0 sweep re-derived 9/2 · `PUBLISHED.tsv` has the `status` column (G3 closed) · spine gate automated in `boot.py` (a-bis) · corrections leg wired (B5c) · hot/cold split executed 9/2 · every ledger in a valid two-state · board_log drained · NEXUS_BRIEF pin = STATUS HEAD (`ffc693c28`, Amendment-10 ordering) · RECIPIENT PATHS table in CLAUDE.md (G1 closed 8/12).

## Assessment plan (next step, this session)
Delta read 8/7 → 9/7 (≈60 own commits) → per-leg ladder verdict table (blueprint §9 form) → peer-parity table vs BRENT (L5 Market) + TERRY (L5 Utility) on the fleet-wide REQUIRED items (R1 leg · read-cap · two-clock headers · cwd-proof · re-mark form · dated falsification surface · LEDGER_GLOB · corrections receipts) → refresh `profiles/LABOR.md` (clock reset) → re-cut FLEET_MAP row + `render_directory.py` → findings packet to `AGENTS/LABOR/inbox/` (LABOR is DARK since 9/4 — packet, never edit; charter edits are Will-gated regardless).
