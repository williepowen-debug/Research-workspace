# OVERDUE BATTERY — 2026-09-17 (Thu, from ~09:2x ET) — Will: *"lets work on the overdue tasks first. you are approved to begin."*

**Owner:** DAEDALUS · **Trigger:** boot `sweeps_due.py` rc 1 — four RESOLVE_BY passed (Wiring R1 9/12 · H2 as-made 9/14 · profile-refresh 9/15 · GATE_BASIS #1 9/16), four cadence DUE (L239 render +6d · Falsification +4d · Production Review +2d · doc-retirement +1d), SELF-ROW 9d. No session existed 9/15–9/16, so none of these silently re-dated. **Method:** mechanical legs first (this file), then a 14-reader fan-out (6 PR cohorts · 3 profile-refresh pairs · 3 gate-basis · 2 wiring judgment), every reader persisting its own report (PAT-100).

## 1. L239 coordination scorecard — render for week-ending 2026-09-11: **CANNOT-RENDER (PROME's ledger), not skipped**
`python3 scripts/scorecard.py --week-ending 2026-09-11` → `ORCH-LOG ✗ rc 2 — 3 problem(s) in PROME/state/ORCH_LOG.tsv`: L138 `drained`=`n/a` · L139 `drained`=`YES — 2 WALTER packets drained from PROM…` · L140 `drained`=`YES — its packet drained and consumed` — the schema-v2 column is integer-or-EMPTY. All three rows are PROME's 9/14 entries (fetch-reviewer · WALTER walter-d9 · REGINALD reginald-29). The renderer refuses (correct: "regenerate, never patch"). **Disposition:** PROME packet — fix the three cells at the source (integer count or EMPTY, prose → the notes column), then I re-render 9/11 and 9/18 together tomorrow. DOCKET L290's render count (#3 = 9/18, #4 = 9/25) stands; the missed 9/11 render is LATE, not lost — the window's inputs are all committed history.

## 2. Gate Basis run #1 — negative control on the retrieval path: **VINTAGE-PATH-VERIFIED** (ALFRED)
Series PAYEMS, `observation_start=2026-01-01`, three `realtime_start=realtime_end` values, key from `FORGE/tools/market-data/.env`:
| realtime | bytes | sha256[:12] | result |
|---|---|---|---|
| 2026-09-01 | 953 | `a5fbd341a74b` | vintage payload A |
| 2026-09-15 | 1,050 | `5940afc2421e` | vintage payload B (differs: the 9/4 print is present) |
| 1900-01-01 | 229 | `e2286131fd91` | HTTP 400 `Bad Request. The series does not exist in ALFRED…` — an invalid vintage FAILS, it does not silently succeed |
Three distinct payloads, invalid date rejected ⇒ the path distinguishes vintages. (The known-false path — `fredgraph.csv?…&vintage_date=` — was not used.) An "unrevised" verdict may ship through this path only.

## 3. Doc-retirement queue run #1 (+1d) — 10 candidates, 5 moved, 5 kept
Census: `git ls-files AGENTS/DAEDALUS/` with last commit < 2026-07-19, excluding `archive/`, `outbox/delivered/`, `inbox/processed/`. Reference test per root rule (index/nav refs don't count; a live analytical/protocol doc must travel it).
| File | Last commit | Live reference? | Disposition |
|---|---|---|---|
| `reference/STATUS_archive_2026-07-12.md` | 07-12 | none | **RETIRED** → `archive/retired_2026-09-17/` |
| `upgrades/DEWEY_DRAFTS_REVIEW_2026-07-10.md` | 07-10 | FLEET_MAP_HISTORY (history ledger) · a DEWEY 7/10 outbox · the retired STATUS_archive | **RETIRED** |
| `upgrades/VIOLET_LIQUID_FIRMING_2026-07-04.md` | 07-12 | FIXBATCH_REPORT_2026-07-12 (closed record) | **RETIRED** |
| `upgrades/WP2_KORE_REPORT_2026-07-10.md` | 07-10 | `builds/homer_promotion/MANIFEST_D_homer.md` (bannered one-shot record) | **RETIRED** |
| `upgrades/BATCH_03_net-new.md` | 07-12 | FIXBATCH (closed) · HANDLE_SWEEP (itself retirement-age) · the retired STATUS_archive | **RETIRED** |
| `upgrades/HANDLE_SWEEP_independence-action.md` | 07-03 | `BLUEPRINTS/market-agent.md:42` + PATTERNS.tsv | KEPT (9/1 ruling stands) |
| `HARNESS_AUDIT_2026-07-07.md` | 07-12 | `sweeps/HARNESS_AUDIT_SWEEP.md:7` — the playbook's method pointer | KEPT (protocol doc travels it) |
| `upgrades/BATCH_01_handles.md` | 07-12 | `upgrades/BROCK_CARD.md`, `SHADE_CARD.md` | KEPT (live cards) |
| `reference/META_RESEARCH_DIGEST_harvested_2026-07-10.md` | 07-10 | `AGENTS/CARL/sub_agents/META/core/RESEARCH_DIGEST.md` | KEPT (another desk's live doc) |
| `MATURITY_MAP.md` | 07-08 | root `README.md:112` links it as *"tracks those differences"* | KEPT — but it is a FROZEN 6/27 snapshot; **PROME flag:** repoint README:112 to `AGENTS/DAEDALUS/FLEET_DIRECTORY.md` |
Old→new paths are recorded here; referrers in closed records are left as-is (they are history).

## 4. H2 as-made audit — receipts closed out (8 of 11), resolve_by re-dated
Receipt ledger appended to `runs/2026-09-07_H2_ASMADE_AUDIT_fleet.md` (ZHAO 9/17 packet processed → `inbox/processed/`). MARCO · REGINALD · HENRY outstanding; registry resolve_by → 2026-09-25; L285 leg 4 can proceed on six owner-verified desks. Standing correction carried into the record: **MISMATCH = candidate count, never defect count** (six owner reads, five with tool-limit false matches).

## 5. Fan-out (results appended below as readers return)
