# WAL retirement sweep — 2026-09-28 (session #10 housekeeping)

**Rule (root CLAUDE.md §Data Hygiene):** a file >60 days old AND not boot-read AND not referenced by a live doc → `git mv` to `archive/`. Index/inventory/nav references don't count; KB Source/Notes cells do (the 9/24 sweep's standard). Candidates came from the 9/28 audit (`research/audit_2026-09-28/D_fraud_research.md` §4); each was re-checked 9/28 (git date, grep for full and shortened names across WAL, PROME and every desk).

| File (was `sources/`) | Last commit | Boot-read | Live references | Action |
|---|---|---|---|---|
| `JEFFERIES_Q1_SIGNAL.md` (content 3/21) | 2026-07-25 | no | none | **RETIRED** → `archive/sources/` |
| `RENO_WAL_Nevada_Exposure_2026-02-11.md` | 2026-07-25 | no | KB_INDEX NEVADA row (index — does not count); re-pointed | **RETIRED** |
| `FFIEC_RC-R_Q4_2025.csv` | 2026-07-25 | no | none in WAL (OZK uses its own copy) | **RETIRED** |
| `WAL Q1 2026 - 8-K Extract.md` (content 4/24) | 2026-07-25 | no | `sources/q1_2026/DROPZONE.md` (nav — does not count); annotated | **RETIRED** |
| `FDIC_QBP_Q4_GEOGRAPHIC_ANALYSIS.md` | 2026-07-25 | no | **`AGENTS/OZK/GEOGRAPHY/README.md`** (another desk) + the GEOGRAPHIC cluster's detail file (rows ACTIVE to 11/30) | **HELD** |
| `q1_2026/DROPZONE.md` | 2026-07-25 | no | **`AGENTS/DAEDALUS/profiles/WAL.md`** (another desk's pointer) | **HELD** (moving it would break DAEDALUS's link) |
| `WAL Q1 2026 - Transcript Synthesis.md` + `… Step 1 Fetch Status.md` | 2026-07-25 | no | point at each other and at the q1_2026 synthesis pair, which stay | **HELD** (retire as a set with the pair, later) |

Moved with `git mv` (history preserved). Content untouched.
