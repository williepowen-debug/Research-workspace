# NEXUS — Fleet brief census, 2026-10-24T18:27:40-04:00 (Will-direct: "sweep of all the NEXUS files around the league")

**Method (mechanical, from git and the artifacts — no brief re-read; no brief has been committed since the 10/23 digest read, so the 10/23 content findings in `BRIEFS_MAP.md` stand):** census = `ls AGENTS/*/NEXUS_BRIEF.md`; dates = `git log -1 --format=%cs`; 30-day counts = `git rev-list --count --since=2026-09-24`; first commit = `git log --diff-filter=A --follow`; pin = `python3 scripts/brief_pin_check.py` (run at this stamp); `order` = byte order of `## CROSS-DOMAIN` / `## VIEW` / `## CALIBRATION` (schema §4.1-R); roster class = `PROME/ROSTER.md` tables. `Lag d` = STATUS last-commit date minus brief last-commit date (the owner committed STATUS after the brief). Ages are calendar days to 2026-10-24.

**Headline:** 29 briefs on disk across 46 desk folders. Brief last committed ≤3 days ago: 24 · 4–5 days: 4 · >5 days: 1 (BROCK). Brief behind its own STATUS by ≥2 days: BROCK (8 d), LIQUID (3 d). Pin check: OK-PINNED 11 · OK-SAME-COMMIT 13 · STALE-PIN 1 · UNPINNED 4. Order: A12 15 · pre-A12 6 · n/a 8.

## 1. Census table

| Desk | Roster class | Brief | Bytes | First brief | Brief last | Age d | Brief folds 30d | STATUS last | STATUS commits 30d | Lag d | Order | Pin | State |
|---|---|---|---:|---|---|---:|---:|---|---:|---:|---|---|---|
| AEOLUS | PROVISIONAL ACTIVE | Y | 4,837 | 2026-06-28 | 2026-10-21 | 3 | 13 | 2026-10-21 | 17 | 0 | n/a | OK-SAME-COMMIT | ✅ FRESH |
| ATHENA | ARCHIVE SOURCE | — | 0 | — | — | — | — | 2026-03-14 | 0 | — | — | — | — by design / not expected |
| BARON | DORMANT | — | 0 | — | — | — | — | — | 0 | — | — | — | — by design / not expected |
| BOND | DOMAIN ACTIVE | Y | 2,689 | 2026-07-18 | 2026-10-20 | 4 | 31 | 2026-10-20 | 58 | 0 | n/a | UNPINNED | 🟡 UNPINNED |
| BRENT | DOMAIN ACTIVE | Y | 23,010 | 2026-06-07 | 2026-10-23 | 1 | 94 | 2026-10-23 | 109 | 0 | A12 | OK-SAME-COMMIT | ✅ FRESH |
| BROCK | DOMAIN ACTIVE | Y | 9,609 | 2026-06-15 | 2026-10-15 | 9 | 5 | 2026-10-23 | 28 | 8 | pre-A12 | STALE-PIN | 🟠 BEHIND STATUS |
| CARL | DOMAIN ACTIVE | Y | 5,922 | 2026-06-16 | 2026-10-21 | 3 | 18 | 2026-10-21 | 17 | 0 | A12 | OK-PINNED | ✅ FRESH |
| CATO | SPECIAL | — | 0 | — | — | — | — | — | 0 | — | — | — | — by design / not expected |
| CORAL | DOMAIN ACTIVE | Y | 11,897 | 2026-06-19 | 2026-10-21 | 3 | 18 | 2026-10-21 | 20 | 0 | pre-A12 | UNPINNED | 🟡 UNPINNED |
| CREED | TIER-2 | — | 0 | — | — | — | — | 2026-10-22 | 38 | — | — | — | ⏳ MISSING |
| CRUISE | EVENT-DRIVEN SPECIALIST | — | 0 | — | — | — | — | 2026-10-23 | 22 | — | — | — | ⏳ MISSING |
| CYPHER | TIER-2 | Y | 9,067 | 2026-10-22 | 2026-10-23 | 1 | 11 | 2026-10-23 | 14 | 0 | A12 | OK-PINNED | ✅ FRESH |
| DAEDALUS | SPECIAL | — | 0 | — | — | — | — | 2026-10-24 | 88 | — | — | — | — by design / not expected |
| DEWEY | TIER-2 | — | 0 | — | — | — | — | — | 0 | — | — | — | ⏳ MISSING |
| FALCON | PROVISIONAL ACTIVE | Y | 8,454 | 2026-07-12 | 2026-10-23 | 1 | 24 | 2026-10-23 | 26 | 0 | A12 | OK-PINNED | ✅ FRESH |
| FERT | EVENT-DRIVEN SPECIALIST | — | 0 | — | — | — | — | 2026-10-21 | 10 | — | — | — | ⏳ MISSING |
| FLG | EVENT-DRIVEN SPECIALIST | — | 0 | — | — | — | — | 2026-10-23 | 17 | — | — | — | ⏳ MISSING |
| GIBBS | TIER-2 | Y | 3,605 | 2026-10-20 | 2026-10-23 | 1 | 4 | 2026-10-23 | 10 | 0 | A12 | OK-PINNED | ✅ FRESH |
| HANS | TIER-2 | — | 0 | — | — | — | — | 2026-10-22 | 23 | — | — | — | ⏳ MISSING |
| HAWK | DOMAIN ACTIVE | Y | 7,961 | 2026-06-08 | 2026-10-21 | 3 | 13 | 2026-10-21 | 14 | 0 | A12 | OK-SAME-COMMIT | ✅ FRESH |
| HENRY | DOMAIN ACTIVE | Y | 2,171 | 2026-06-15 | 2026-10-22 | 2 | 32 | 2026-10-22 | 35 | 0 | n/a | OK-SAME-COMMIT | ✅ FRESH |
| HOMER | PROVISIONAL ACTIVE | Y | 13,447 | 2026-07-12 | 2026-10-19 | 5 | 15 | 2026-10-19 | 17 | 0 | A12 | OK-SAME-COMMIT | ✅ FRESH |
| ISHM | TIER-2 | — | 0 | — | — | — | — | 2026-10-23 | 4 | — | — | — | ⏳ MISSING |
| LABOR | DOMAIN ACTIVE | Y | 17,448 | 2026-06-16 | 2026-10-22 | 2 | 24 | 2026-10-22 | 26 | 0 | A12 | OK-PINNED | ✅ FRESH |
| LIQUID | DOMAIN ACTIVE | Y | 6,200 | 2026-07-06 | 2026-10-21 | 3 | 9 | 2026-10-24 | 71 | 3 | n/a | UNPINNED | 🟠 BEHIND STATUS |
| MARCO | DOMAIN ACTIVE | Y | 22,213 | 2026-06-08 | 2026-10-21 | 3 | 9 | 2026-10-21 | 7 | 0 | pre-A12 | OK-PINNED | ✅ FRESH |
| MIDAS | PROVISIONAL ACTIVE | Y | 2,630 | 2026-07-11 | 2026-10-23 | 1 | 22 | 2026-10-23 | 31 | 0 | n/a | OK-SAME-COMMIT | ✅ FRESH |
| ORACLE | DOMAIN ACTIVE | Y | 4,059 | 2026-06-19 | 2026-10-21 | 3 | 14 | 2026-10-21 | 10 | 0 | n/a | OK-SAME-COMMIT | ✅ FRESH |
| OSPREY | PROVISIONAL ACTIVE | Y | 21,495 | 2026-07-12 | 2026-10-23 | 1 | 16 | 2026-10-23 | 20 | 0 | A12 | OK-SAME-COMMIT | ✅ FRESH |
| OTTO | TIER-2 | Y | 13,969 | 2026-06-08 | 2026-10-19 | 5 | 15 | 2026-10-19 | 23 | 0 | A12 | OK-PINNED | ✅ FRESH |
| OZK | EVENT-DRIVEN SPECIALIST | — | 0 | — | — | — | — | 2026-10-22 | 21 | — | — | — | ⏳ MISSING |
| RAV | SPECIAL | — | 0 | — | — | — | — | — | 0 | — | — | — | — by design / not expected |
| RED | REVIEW/QC | Y | 12,054 | 2026-07-10 | 2026-10-22 | 2 | 17 | 2026-10-22 | 36 | 0 | pre-A12 | OK-SAME-COMMIT | ✅ FRESH |
| REGINALD | DOMAIN ACTIVE | Y | 18,221 | 2026-07-09 | 2026-10-23 | 1 | 90 | 2026-10-23 | 92 | 0 | A12 | OK-PINNED | ✅ FRESH |
| SAM | DOMAIN ACTIVE | Y | 5,753 | 2026-06-07 | 2026-10-20 | 4 | 16 | 2026-10-20 | 16 | 0 | pre-A12 | OK-PINNED | ✅ FRESH |
| SENTRY | DORMANT | — | 0 | — | — | — | — | 2026-09-24 | 0 | — | — | — | — by design / not expected |
| SHADE | DOMAIN ACTIVE | Y | 8,069 | 2026-08-03 | 2026-10-21 | 3 | 14 | 2026-10-21 | 15 | 0 | n/a | OK-SAME-COMMIT | ✅ FRESH |
| TERRY | DOMAIN ACTIVE | — | 0 | — | — | — | — | 2026-10-24 | 72 | — | — | — | ⏳ MISSING |
| VIOLET | DOMAIN ACTIVE | Y | 3,451 | 2026-06-07 | 2026-10-21 | 3 | 21 | 2026-10-21 | 23 | 0 | A12 | OK-SAME-COMMIT | ✅ FRESH |
| VULCAN | PROVISIONAL ACTIVE | Y | 10,784 | 2026-07-10 | 2026-10-23 | 1 | 31 | 2026-10-23 | 34 | 0 | A12 | OK-PINNED | ✅ FRESH |
| WAL | EVENT-DRIVEN SPECIALIST | Y | 4,628 | 2026-07-25 | 2026-10-22 | 2 | 36 | 2026-10-22 | 33 | 0 | n/a | OK-PINNED | ✅ FRESH |
| WALTER | ORGANIZING | — | 0 | — | — | — | — | 2026-10-23 | 200 | — | — | — | — by design / not expected |
| WATT | PROVISIONAL ACTIVE | Y | 8,315 | 2026-07-10 | 2026-10-23 | 1 | 16 | 2026-10-23 | 13 | 0 | A12 | UNPINNED | 🟡 UNPINNED |
| YEYOU | RETIRED | — | 0 | — | — | — | — | 2026-08-20 | 0 | — | — | — | — by design / not expected |
| YURI | PROVISIONAL ACTIVE | Y | 12,017 | 2026-09-25 | 2026-10-21 | 3 | 17 | 2026-10-21 | 20 | 0 | A12 | OK-SAME-COMMIT | ✅ FRESH |
| ZHAO | DOMAIN ACTIVE | Y | 22,585 | 2026-07-04 | 2026-10-22 | 2 | 6 | 2026-10-22 | 6 | 0 | pre-A12 | OK-SAME-COMMIT | ✅ FRESH |

## 2. Who has no brief, and whether one is expected

| Desk | Roster class | STATUS commits 30d | Brief ever committed? | Reading |
|---|---|---:|---|---|
| ATHENA | ARCHIVE SOURCE | 0 | never | ARCHIVE SOURCE — do not launch |
| BARON | DORMANT | 0 | never | DORMANT (no STATUS.md in the tree) |
| CATO | SPECIAL | 0 | never | SPECIAL adviser/reviewer; none expected |
| CREED | TIER-2 | 38 | never | Tier-2, launch only on Will's word; no brief expected |
| CRUISE | EVENT-DRIVEN SPECIALIST | 22 | never | **NOT covered by the brief-less line.** Event-driven specialist, STATUS active; not load-bearing on any matrix row today. |
| DAEDALUS | SPECIAL | 88 | never | SPECIAL meta-agent; none expected |
| DEWEY | TIER-2 | 0 | never | stateless deep-research desk; none expected |
| FERT | EVENT-DRIVEN SPECIALIST | 10 | never | **NOT covered by the brief-less line.** Event-driven specialist; FERT G5 appears only in my NOT CONFIRMING line; POTASH triage-only. |
| FLG | EVENT-DRIVEN SPECIALIST | 17 | never | **NOT covered by the brief-less line.** Event-driven specialist, STATUS active (FLG RED 10/23 enters my M-05 / R10 rows) — read raw every pass. Candidate for a COMPACT brief (amendment 9). |
| HANS | TIER-2 | 23 | never | Tier-2 Europe; ~monthly cadence; none expected (compact brief optional) |
| ISHM | TIER-2 | 4 | never | Tier-2, built this month (4 STATUS commits); no brief yet — expected once it holds a view. |
| OZK | EVENT-DRIVEN SPECIALIST | 21 | never | listed brief-less by design (BRIEFS_MAP live line); single-name, print-driven |
| RAV | SPECIAL | 0 | never |  |
| SENTRY | DORMANT | 0 | never | DORMANT |
| TERRY | DOMAIN ACTIVE | 72 | never | trade construction — utility desk, none expected (BRIEFS_MAP live line); its VIEW reaches NEXUS by packet/STATUS |
| WALTER | ORGANIZING | 200 | never | routing desk — brief-less by design (BRIEFS_MAP live line) |
| YEYOU | RETIRED | 0 | never | RETIRED 9/05 (folder left in place) |

## 3. Form of the eight briefs without the schema header set (`order` n/a)

| Desk | Bytes | Form seen at the artifact | Pin line | Note |
|---|---:|---|---|---|
| AEOLUS | 4,837 | declared COMPACT routing-first variant (amendment 9) — `## 🔴 THE ONE THING` … `## ROUTING` … `## CONVERGENCE SNAPSHOT` | none in the first 40 lines; `Last writeback` stamp only; OK-SAME-COMMIT by git | conformant compact; a §4.1 pin line is the owed fix |
| BOND | 2,689 | `# BOND → NEXUS — current owner pointers`: a 2.7 KB pointer stub with an HTML state comment and glued-word bullets | none; `Last refresh` prose date only | UNPINNED; words glued (root Output Canon) — flagged 10/23, unchanged; the pre-cap full brief lives at `domain/sources/2026-09-29_NEXUS_BRIEF_full-snapshot_pre-cap-rotation.md` |
| HENRY | 2,171 | `**Owner fold:**` stamp + `**View:**` prose, no section headers, 2.2 KB | none (the fold line names the spawn, not a hash); OK-SAME-COMMIT by git | content current to 10/22 19:38 ET; no 10/23 read |
| LIQUID | 6,200 | `**Reconciled:**` / `**After-close review**` stamps + own sections (`## Current judgment` · `## Counterevidence and limits` · `## Existing next tests and ownership`) | none; UNPINNED | brief 10/21 vs STATUS 10/24 (71 STATUS commits in 30 d against 9 brief folds) — the chronic case, 7 consecutive passes behind |
| MIDAS | 2,630 | a dated catch-up note addressed to named desks + pointers, 2.6 KB; older sections rotated to `analysis/NEXUS_BRIEF_ARCHIVE_2026-10.md` 10/23 | none in the header; OK-SAME-COMMIT by git | content current to 10/23 |
| ORACLE | 4,059 | `**As of:**` + `**Status**` + `**Domain**` + `## Cross-agent tensions` + `## Forward catalysts` | `STATUS commit: see git log -1` — a pointer, not a value (class C) | OK-SAME-COMMIT by git; as-of 10/21 against its daily L729 cadence |
| SHADE | 8,069 | `**As of:**` + `**STATUS commit:** same commit as this fold` + prose | same-commit phrase (class C) | OK-SAME-COMMIT by git; §4.1 asks for the hash |
| WAL | 4,628 | `**As of:**` + full 40-char STATUS hash + `## What Q3 showed` … `## Delivery` | full hash — OK-PINNED | issuer-shaped brief, conformant on the pin; headers are the desk's own |

## 4. Reading

- **Coverage:** every DOMAIN ACTIVE and PROVISIONAL ACTIVE desk except TERRY carries a brief (TERRY is a utility desk by the live line). Of the five EVENT-DRIVEN SPECIALISTS only WAL has one; OZK is excused by the live line; **FLG, CRUISE and FERT are not excused anywhere** — the brief-less line never caught up with the 8/16–8/21 class additions. Tier-2: GIBBS, CYPHER and OTTO hold briefs; ISHM, CREED, DEWEY and HANS do not.
- **Update cadence:** 24 of 29 briefs were committed within 3 days; the fold rides the owner's closeout (amendment 10), so brief age tracks desk activity, not brief discipline. The two weak points are **BROCK** (brief 10/15, STATUS 10/23, pin 5 commits behind — 8 days of CRMT / WQ-511 evidence live only at STATUS) and **LIQUID** (9 folds against 71 STATUS commits; the brief misses the 10/22–10/24 gate grades). HOMER and OTTO sit at 5 days with their 10/20–22 reads listed as future. ZHAO's brief is dated 10/22 but its forward table is still 'refreshed 9/17' and its as-of sentence says 9/25.
- **Conformance:** the pin ruling (10/8 PM: UNPINNED or pointer-valued pins = a §4.1 gap owed at the owner's next fold) has not moved the four UNPINNED desks (BOND, CORAL, LIQUID, WATT) or the two pointer-pins (ORACLE, SHADE) in 16 days. `order` is unchanged from the 10/24 16:19 measurement (15 / 6 / 8).
- **No fallback rows written:** this was a census, not an intake pass (no raw STATUS read for synthesis). The L555 rollup #6 (DOCKET, Tue 10/27) carries the owner asks; the 4-week fallback-log mix as of today: LIQUID stale 8 · BROCK stale 5 · YURI stale 2 · singles (BOND, CARL, CORAL, MIDAS, RED, REGINALD, SHADE, WALTER) · convergence 6 · digest 7 (excluded from rates).
- **Other NEXUS-named files around the fleet (not briefs):** owner-side brief archives (SAM `NEXUS_BRIEF_ARCHIVE.md` 60 KB · MIDAS `analysis/NEXUS_BRIEF_ARCHIVE_2026-{09,10}.md` · BRENT `workbook/NEXUS_BRIEF_archive_*` · RED `reports/*_NEXUS_BRIEF_vS*_rotated.md` ×6 · BOND pre-cap snapshot) — rotation homes, healthy; LIQUID `workbook/DEALER_POSITIONING_NEXUS_WATCH.md` (LIQ-076 letter, live); WAL `FRAUD/AUDITOR_NEXUS.md` (a WAL-internal file whose name collides with this desk — not a NEXUS surface); old outbox packets to NEXUS (CARL 6/16, LIQUID 6/08, BRENT 6/07, TERRY 6/27, ORACLE 7/31, BOND 7/28) — delivered history; PROME task/report files about NEXUS (10/07, 10/08, 10/19 ×4) and the WQ-519 ruling; DAEDALUS profile + the 10/24 L40 packet; CATO run reviews (9/29, 10/24).

**9c late mover, 2026-10-24T18:28:51-04:00:** `AGENTS/DAEDALUS/STATUS.md` committed 18:25 ET during this census (after the table above was computed; DAEDALUS is SPECIAL, brief-less by design) — table row not recomputed, delta-annotated here.
