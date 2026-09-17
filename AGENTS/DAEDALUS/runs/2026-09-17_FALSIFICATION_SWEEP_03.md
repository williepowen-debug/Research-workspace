# Falsification Freshness Sweep — RUN #3, 2026-09-17 (Thu) — DAEDALUS (cadence 21d, +4d over; on Will's 09:2x word)

**Playbook:** `sweeps/FALSIFICATION_SWEEP.md`. **Method:** mechanized detection first (`scripts/falsification_scan.py`, raw output → session scratchpad, verdict table reproduced below), then a **judgment read of every flag by a non-owner reader** — the six Production Review #6 cohort readers carried step 5 (flag reads, F1 bucket, F5 bucket) and step 6 (the negative-resolution leg, deferred from run #2) for their desks; DAEDALUS re-verified the two withdrawals at the artifact headers. Evidence: `upgrades/PRODUCTION_REVIEW_2026-09-17_READER_R1…R6*.md` (per-desk §5 and §6).

## 0. Verdict in one line
**Scanner: 4 STALE-FLAGGED → on read 0 REAL-STALE, 2 STALE-BUT-CONSISTENT (each with one real content defect), 2 WITHDRAWN-as-content-stale (both are HEADER-CLAIM defects on the owner's side, not scanner defects).** The F1 bucket ("market desk, no thesis file the scan can see", 6 desks) is **6-for-6 RAIL-IN-LOCAL-FORM** with evidenced fire paths — including LABOR, whose grandfathered L3 FAIL is now CLEARED by a dated re-derivation stamp. The F5 bucket (AEOLUS/MIDAS/OSPREY) is 3-for-3 local-form, live and dated. **The negative-resolution leg (run #2 deferral) ran fleet-wide for the first time: ~285 OPEN rows opened across 30 desks, ~86 negative-class, ~23 lacking a named search instrument or dated search-attempt precondition, concentrated on 8 desks.** Over-flag rate 4-of-4 on the scanner's STALE verdicts (run #1 31%, run #2 50%, run #3 100%) — the scanner now finds only header-vs-content disagreements, which is a different, cheaper defect class than the thesis-rot it was built for.

## 1. Scanner output (2026-09-17 09:2x ET), then the read
| Desk | Surface | Scanner | Age | Read verdict (reader · locator) | The real finding |
|---|---|---|---|---|---|
| LIQUID | `workbook/KILL_MEMO_HY_OAS_260.md` | STALE-FLAGGED 8/23 vs 9/17 | 25d | **STALE-BUT-CONSISTENT** (R2) — stamp self-declared; content current through 9/12 | Drill log has **no row for HY OAS 260 on 8/28** (the 2026 minimum, 0bp margin on the kill line) though STATUS + `eac198c83` recorded it; the file's own ★ block for the 7/27 280-cross is the precedent. Item 6 (:59) "no vintage path" REFUTED (gate-basis run #1). |
| SAM | `red/COUNTER_THESIS.md` | STALE-FLAGGED 8/17 vs 9/15; cites v1.6 / live v1.7 | 29d | **WITHDRAWN as content-stale** (R3, P3) — header declares *"record of a counter-case, not a live dashboard"*, live half routed to `CHALLENGES.md`; DAEDALUS re-read header :3-6 | Header carries no canonical FROZEN-form token, so the scanner cannot honour the self-declaration (DEAD_BANNER requires token+ISO date). **Owner ask: one banner line.** The finding it hid: **CH-009/CH-012 adjudicators dated 9/3 are 14d overdue on a rail SAM is forbidden to self-serve** (`red/CHALLENGES.md`; last RED pass `daba336d5` 8/27); CH-017 keyed to an anchor that already fired (P3). → RED + SAM. |
| VULCAN | `workbook/EXIT_PROTOCOL.md` | STALE-FLAGGED 8/13 (inferred) vs 9/13 | 31d | **WITHDRAWN as content-stale** (R4) — hybrid surface, newest dated entry 9/13; DAEDALUS re-read header :3 | The header's only dated claim is *"Kill rail re-derived: 2026-08-13 (first authored…)"* — a provenance line standing where a freshness claim belongs. Under the state-surface rule the header governs, so the surface certifies itself stale. **Owner ask: bump the header claim when entries land** (VULCAN did so on 9/6 for eight other surfaces). |
| WATT | `KILL_MEMO.md` | STALE-FLAGGED 8/17 vs 9/15 | 29d | **STALE-BUT-CONSISTENT** (R4) — evaluated by name 3× during the September emergency | C1's from-state cell *"the pair has never co-occurred"* was **refuted 9/2**; `STATUS.md:37` still carries the VULCAN seam as open (VULCAN closed it 9/6 across 8 surfaces). |

## 2. F1 bucket — Market desk, no thesis-class file the scan can see (6) — **6/6 RAIL-IN-LOCAL-FORM**
| Desk | Where the rail lives (locator) | Evidenced fire path | Reader |
|---|---|---|---|
| BROCK | STATUS §kill/exit + `PREDICTIONS.tsv` `Action_If_Falsified` (:1) | BRK falsifier reachability run n=787 (kill never reachable → label corrected, number untouched) | R2, P1 |
| CRUISE | `STATUS.md:99-118` (3 ruled kills incl. VX-CRU-06/WQ-222) + `CLAUDE.md:144` | CRU-05 graded FAILED at window close 9/13, whole ambiguity-family graded | R6 |
| HOMER | per-prediction early-kill + §C | HOM-01 fired 8/31 | R5 |
| LABOR | `STATUS.md` § EXIT RULES + `docket/graded/` frozen cards; **`Kill rail re-derived: 2026-09-04` stamp** | three dated legs with named instruments; first real card PASS watched (`GRADING_CARD_20260903_ISM_SERVICES.md` rc=0) — **grandfathered L3 FAIL CLEARED** | R3 |
| SHADE | `CLAUDE.md:48` 4 kill paths + T-SHADE-01 (`CLAUDE.md` §REGISTERED TRIGGERS) | 4-for-4 not-armed reads, dated; **live: HY OAS 276 [FRED 9/15] vs >280, desk dark 20d** | R5, P3 |
| ZHAO | STATUS, two adjacent named sections | evidenced fire (R3 §ZHAO-5) | R3 |
The scanner's F1 sentence stays correct as a CLASS statement (Market L3 requires a dated surface) and wrong as a per-desk finding — the dated-surface gap is now the *header* gap (LABOR fixed it with one stamp line), not a discipline gap.

## 3. F5 bucket — thesis, no separate surface (3): AEOLUS `STATUS:117` triad + `If_Falsified`, 3 evidenced fires (R5) · MIDAS in-thesis "What KILLS" block, live, **2 REAL-STALE cells in the registered letter incl. a ✅ tick certifying a price band gold has left** (R4) · OSPREY `CLAUDE.md` §EXIT RULES ruled 9/8, dated (R4). Three for three local-form; MIDAS carries the only stale cells.

## 4. Negative-resolution leg (first fleet-wide run; canon `FORGE/PREDICTION_DISCIPLINE.md` § Grading, ratified 8/17)
| Cohort | OPEN rows opened | negative-class | lacking instrument / dated-search precondition | Desks carrying the lack |
|---|---|---|---|---|
| R1 meta/utility | 110 | 14 | 0 | — (RED 15/6/0 = the fleet's best rows) |
| R2 rates/credit | 42 | 21 | 11 | BROCK 5 · CREED 6 (instrument 0, dated-search 6) |
| R3 global | 39 | 7 | 2 | ZHAO 1 · HANS 1 |
| R4 theaters/commod | 21 | 10 | 0 (+1 lacking a dated window: FAL-05) | FALCON (window) |
| R5 FL/housing/banks | 20 (SHADE NOT-SEEN, no ledger) | 12 | 6 | CORAL 2 · AEOLUS 1 (AEO-03) · REGINALD 3 |
| R6 specialists | 22 | 6 | 3 | OTTO (OTTO-12: "Tracking close.", 155d, no instrument, no date) + 2 |
| **Fleet** | **~254 + NOT-SEEN** | **~70** | **~22 + 1 window** | **8 desks** |
Observation (R5): a *column* for the negative (AEOLUS `Resolution_Criteria`, REGINALD `Invalidation`, HOMER §C) makes it visible; only AEOLUS reliably instruments it — and AEOLUS is also the one that names the WRONG instrument and forbids it. **A column makes the negative visible; it does not make it resolvable.** Propagation is real where it was routed by hand (OSP-04 → OSP-06 → FERT-12, R4).

## 5. Self-inclusion (PAT-050)
- Scanner: two verdict classes it cannot see are now the dominant residue — (a) a self-declared record surface with no FROZEN-form token (SAM), (b) a provenance line in the header slot (VULCAN). Both are OWNER header asks, not scanner edits (a prose-phrase match would be the PAT class *marker word in prose disables the scanner*). Registered as the run's known limits, not fixed.
- The F1 sentence in the scanner has now been read 3 runs running as if it were a per-desk verdict. Re-word at the next scanner touch: "6 Market desks with no thesis-CLASS FILE — rails may live in STATUS/CLAUDE (run #3: 6/6 did)".
- My own map: two rows carried falsification claims already false (VULCAN "rail RE-READ not restated" fine; MIDAS letter cells stale unflagged) — folded into the PR#6 re-cut.

## 6. Dispositions — TASK-PACKET-ONLY (no pre-approval class fired; no retired-unfrozen kill tree found)
Owner asks ride the consolidated per-desk PR#6 packets (one packet per desk, this session): LIQUID (drill-log row 8/28 + item 6) · SAM (banner token; CH-017 anchor) + RED (CH-009/CH-012 overdue adjudication) · VULCAN (header claim) · WATT (C1 from-state cell; VULCAN seam) · MIDAS (2 letter cells) · negative-resolution rows: BROCK · CREED · ZHAO · HANS · CORAL · AEOLUS · REGINALD · OTTO · FALCON (window). SHADE's live proximity → PROME (spawn-driver; WALTER-routed signal, not a DAEDALUS send).
Registry `last_run` 2026-09-17; next due ~10/08 (offset a week from Staleness #5 ~9/22 stays).
