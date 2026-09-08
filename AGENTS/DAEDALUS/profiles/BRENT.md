# Agent Profile — BRENT

**Built by:** DAEDALUS · **Original:** 2026-06-29 · **Prior full refresh:** 2026-07-28 · **FULL REFRESH: 2026-09-07 Mon ~21:1x ET** (Will-directed architecture review — clears the 8/17 and 9/1 Δ-banners; record `upgrades/BRENT_ARCHITECTURE_REVIEW_2026-09-07.md`)
**Sources read (9/7, direct, by command):** `CLAUDE.md` (whole, 38,591 B) · `STATUS.md` (structure + all headings + L1–46, L73–114, L115–187) · `TRADE.md` (structure + stance/rulings/plan/gates/decisions/log spans) · `SCRATCH.md` (whole) · `RULINGS.md` (head + §deploy-gate) · `NEXUS_BRIEF.md` (structure + version cites) · `LESSONS.md` (structure) · `SCHEDULED_RUNS.md` · `MEMORY.md` · `scripts/boot.py` (whole) + the 21:07 working-tree diff · `workbook/LEDGER_GLOB` (whole) · `workbook/REGISTRY.tsv` (schema + kinds/states) · `thesis/{THESIS structure, PREDICTIONS stats, CHANGELOG tail}` · `docket/CATALYSTS.tsv` (all rows) · `refinery_damage/INCIDENTS.tsv` (stats) · inbox/outbox/messages trees · full tree (553 files, 504 non-archive) · `_NETWORK.md` BRENT routes · NEXUS schema §2/§4 · fleet tools: `read_cap_check --agent BRENT`, `ledger_staleness` ×3 modes, `asmade_audit`, `wiring_census`, `maturity_scan`.
**Staleness / refresh clock:** **45 d → 2026-10-22**, or earlier on: THESIS major version (currently **v5.8**, 9/2) · `TRADE.md` split executed (P2) · rule-19 restructure of STATUS (P1) · a Conf/level change at PR#6 (9/15). Re-read the actual file before applying any change (PAT-009).

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent.

---

## 1. Identity
Oil & energy markets — Brent/WTI on NAMED contracts (`BZX26` etc., never bare `BZ=F` for a level), term structure, cracks, OPEC+, Gulf production, storage (Cushing/SPR/floating), tankers + war-risk (JWC listings as the instrument), US shale/rigs (BRT-26 vs frozen 457), demand, energy HY (unmeasured here — LIQUID). **Class:** Market. **Thesis frame:** v5.8 TIMED RACE (deficit-close clock vs buffer-exhaust clock; re-clocked 9/2 — draw pace 44% of June, Cushing rebuilt, SPR the one clock still counting); v5.0 SKEW-not-direction guardrail; bidirectional exit. **Transmission (canon `_NETWORK.md`):** ← HAWK (reconciled geopol read) · ← OSPREY / FALCON (acute 🔴 direct, HAWK cc — the 9/7 GATE 2 hand-off ran on this route) · ← MARCO · ← AEOLUS · ← WALTER lane · → HENRY / LIQUID / CARL / SAM / REGINALD / WATT / FERT / CRUISE / TERRY / PROME / NEXUS (brief). **MSG-v1 first cohort** (PROME→BRENT). **Cloud routines:** 3 (Mon 9:45 · Wed 11:00 · Fri 14:00 ET; sonnet-5; `SCHEDULED_RUNS.md` is the repo mirror) — they write `demand_destruction/data/{monday,eia,friday}_*.md` + a TRACKER row and **self-commit**; they read TRACKER's top block + STATUS banners at run time and **record, never decide** (prediction-row fence). **Spawnable by:** PROME / Will.

## 2. File anatomy (9/7 — bytes are the load-bearing column)
| File | Holds | Bytes · state |
|---|---|---|
| `STATUS.md` (187 ln) | 963 B two-clock header · `# ⚡ CURRENT STATE` dated blocks newest-first (9/7 14:2x supersedes-the-headline-of 9/7 12:1x; 9/6; the 9/2 heading is a rotation pointer over **34.5 KB of 9/1 material** incl. the RETAINED standing set rows 78–84: BRT-26 ladder · COT-35B band · JWC baselines · **17 corrected-claim sentinels** · export-sign warning · stance) · then pointer sections (STATE→THESIS **:119 says v5.7, stale** · PRICE DASHBOARD · POSITIONS→TRADE · CONVERGENCE MATRIX **ARCHIVED 8/13** · PREDICTIONS→tsv · KEY OPEN ITEMS · 📅 CATALYST CALENDAR 22 rows · SUMMARY FOR WILL **= a rotation stub since 8/27**) | **74,061 B = 137% of cap**; +15 KB in 2.5 h on 9/7; 3 rotations in 10 d; boot reads whole |
| `TRADE.md` (897 ln) | header (two-clock stamp added 9/7 live) · CURRENT STANCE v5.0 · POSITIONS (USO 35 sh · USO Oct-16 135C ×2 · USO Sep-18 150/165 spread · XLE Sep-30 65C ×2; `$7,829.95` at the 9/2 chain) · CONCENTRATION ARITHMETIC + 3 live-vintage companions · **⚖️ BINDING WILL RULINGS (8/21, cite by section name)** · ACTIVE TRADE PLAN (**RETIRED 8/7**) · DEPLOY GATE v3 (RETIRED) · 8/3 pre-fill disclosure (39.8 KB dated) · **frame-breaker carve-out @ byte 56,103** · OFF-RAMP PLAYBOOK (ARMED-PASSIVE) @105,935 · **STAGE-A v5 LIVE ENTRY GATE @108,998** · STAGE-A v4 (superseded) · HARVEST RULE · KNOWINGLY OPEN · tail-rider · DECISIONS · CROSS-AGENT · **EXECUTION LOG @175,218** · CATALYSTS (July) · RESOLVED/HISTORY (563 B) | **181,108 B = 334% of cap**; LIVE — never freeze; rotation blocked since 8/21 by live-in-dated; in `LEDGER_GLOB` |
| `CLAUDE.md` (≈250 ln) | symmetric boot 0–6d ↔ closeout 7–14 (numbers are an API — do not renumber) · CLOSEOUT CHECK REFERENCE (cot_grade / lessons_check --prose/--spec) · STANDING RULES (retirement ratchet · C2 same-commit · one source · STALE-marked · falsify a new guard) · MAIL/outbox · OUTPUT RULES · DOMAIN SCOPE · NETWORK table (**diverged mirror**) · KEY THRESHOLDS → REGISTRY pointer + dated record · DM v1 | **38,591 B = 118% of budget**, always-loaded; max line 4,593 B; ~13 KB rationale that belongs in RULINGS |
| `RULINGS.md` | the *why* record, created 8/5; 16 dated sections, newest **8/07** | 28,637 B; **dead sink** (no closeout step writes it) |
| `SCRATCH.md` | session handoff: READ FIRST · WHAT THIS SESSION DID · THE FINDING · NEXT SESSION (dated table) · OPEN THREADS/DEBT · POSITIONS · commit-message debt · MAIL | 18,207 B; **best-maintained surface**; declares its own failures (L43 of STATUS, the read-cap net-negative) |
| `NEXUS_BRIEF.md` (145 ln) | 70-line 9/7 hot block · VIEW · CALIBRATION · **CROSS-DOMAIN @26,720** · FORWARD CATALYSTS | 44,502 B; amendment 12 unapplied; NEXUS boot-reads it |
| `LESSONS.md` + `workbook/LESSONS_INDEX.tsv` (26 rows) | prose lessons (2 headings) + machine spine checked by `lessons_check.py` every boot | 48,705 B = 90% of cap, boot-read whole, +41% in 3 wk |
| `thesis/THESIS.md` v5.8 | 33 KB dated version-bump preamble · CORE THESIS (timed race) · TWO PHASES · 4 TRANSMISSION CHANNELS (~1.5 KB) · EXIT PROTOCOL · KEY THRESHOLDS prose | 73,838 B; read via STATUS pointer |
| `thesis/PREDICTIONS.tsv` (30 rows) | scoreboard preamble 33.5 KB + 10-col ledger; 3 OPEN; BRT-26 (rigs vs 457, window closes 9/30) · BRT-30 (JWC, resolves 10/26) | 111,603 B; 12 rows >2 KB; `PREDICTIONS_ARCHIVE.md` last written **6/20** |
| `thesis/CHANGELOG.md` | version audit trail, newest 9/6 | 144,692 B, write-only |
| `workbook/REGISTRY.tsv` (49 rows: 39 threshold · 5 falsifier · 4 gate · 1 prediction; 31 live / 18 retired) | **canonical machine state**: level · instrument · `window_req` · `supersedes` · `consumer_scripts` · `cadence` — graded every boot by `thresholds.py`, probed by `instrument_check.py` | 74,876 B; the convergence surface in local form |
| `workbook/{KB,VX,FLOW}.tsv` · `GROUP_MAP.tsv` · `SCHEMA.tsv` | FROZEN 7/01 (fleet-model banners) · FROZEN 7/16 pending-delete · unbannered | frozen / debt |
| `workbook/LEDGER_GLOB` | the declared ledger set (9 TSV-ish + `TRADE.md` added 8/21) with its own falsification record | **read it before touching staleness on this desk** |
| `docket/CATALYSTS.tsv` (20 rows, 8 cols, `date_class`) | canonical forward state; 7 fired rows >7 d unpruned; twin = STATUS calendar (**diverged: 9/18 expiry missing there**) | 65,215 B |
| `docket/FASTOW*.md` | catalyst-steward sub-agent, **dormant since 6/07**, no note (4th flag) | 47 KB |
| `refinery_damage/INCIDENTS.tsv` (53 rows, 22 cols) | facility-damage ledger; 16 ACTIVE, median `last_verified` **153 d**, 12 past the 60 d budget | live; the standing backlog |
| `demand_destruction/TRACKER.md` | 📟 REGISTERED ALERT LINES top block = **run-time contract for the 3 routines** (SCOPED-PARTIAL re-stamp rule) + weekly data log | 164,672 B |
| `demand_destruction/{ANALOGS,HAMILTON,HOARDING,TRANSITION_MATRIX,MATRIX_REVIEW}` + `data/` | Mar–Apr research corpus (live-referenced by TRACKER/CHANGELOG) + routine outputs (~3 files/wk, no rotation rule) | static / growing |
| `scripts/` (boot.py · thresholds · eia_weekly · catalyst_countdown · predictions_due · lessons_check · instrument_check 55 KB · cot_grade [closeout-conditional] · refiner_ratios [unwired; data last 7/01] · BUILD_PLAN.md [Apr]) | `boot.py` = 8-entry sequence, tri-state OK/FINDINGS/FAIL + marker promotion (§8 exemplar); Ledger Staleness now `--days 7` on a measured base rate (9/7 live) + `--nudge` (thresholdless) | all read-only; safe to run while live |
| `board_log.tsv` (297 rows, 1,039 B/row) | WALTER-lane + inbox consumption ledger | 308,700 B — written/looked-up, never read whole |
| `inbox/` (root 0 · processed 127 · WALTER 0 pending / 147 processed) · `outbox/` (root 0 · delivered 51) · `messages/receipts/` (4) · `registry/corrections_receipts.tsv` | coordination layer | **clean, fleet-best** |
| `setups/` (9, 7/17–8/4) · `research/PHASE2_SHORT_PLAYBOOK.md` (40.7 KB, 8/21) · `design/JOINT_PROPOSAL_2026-05-05` · root `2026-07-06_teams-session.md` / `2026-08-28_session-delivery.md` | pre-regs and proposals (5 setups live-cited from TRADE) · retirement queue (F13) | placement debt |
| `archive/` (4 STATUS/NEXUS cuts since 9/2) + `workbook/STATUS_archive_*` (30) + `archive/legacy_20260721`, `research_20260321_corpus` | **two archive homes** for STATUS rotations | 49 files |

## 3. Per-dimension local representation
| Dimension | Where | Form | Read |
|---|---|---|---|
| Thesis | THESIS v5.8 + CHANGELOG | timed race, two clocks, 4 channels, vX.Y trail; 33 KB of version-bump narrative ABOVE the core | exemplary content, preamble-heavy |
| Convergence | **REGISTRY.tsv + thresholds.py boot grade** (local form) | 31 live tests with per-test state every boot; the 7/21 **composite** matrix archived 8/13, no successor | registry ≠ composite — 9/14 ladder question |
| Invalidation / exit | THESIS EXIT PROTOCOL · TRADE frame-breaker letter · STAGE-A v5 · off-ramp playbook · REGISTRY falsifier rows | bidirectional flip (blueprint's named source); letters cited by section name; **letters sit past the read cap of TRADE.md** | exemplary judgment, unreachable by a whole read |
| Thresholds | REGISTRY.tsv (machine) + THESIS §KEY THRESHOLDS (prose) + CLAUDE pointer | ONE home since 7/31 F3 / 8/4 repoint | fixed since 7/28 |
| Predictions | PREDICTIONS.tsv + (stale) ARCHIVE | BRT-xx, class anchors, PRE-FLIGHT; frozen numbers; **as-made vs ledger: instrument noise on this desk** | best-in-fleet discipline, heaviest cells |
| Cross-agent | NEXUS_BRIEF + acute outbox + WALTER lane + MSG-v1 + FALCON/OSPREY direct | SENDING/WAITING tables; loops closed at recipients | strong; brief schema drift |
| Rulings | **TRADE.md §BINDING WILL RULINGS** (the letter) vs `RULINGS.md` (the why, dead since 8/07) | two homes, one dead | F6 |

## 4. Deviations / debt (9/7) — full detail `upgrades/BRENT_ARCHITECTURE_REVIEW_2026-09-07.md`
- **Root defect:** write mode interleaves standing state with dated narrative → STATUS 137% / TRADE 334% / LESSONS 90% of cap; rotation blocked by the sentinels (STATUS) and by live-in-dated clauses (TRADE); derived pointers lag (STATUS:119 v5.7 vs THESIS v5.8, 4th recurrence of the L5 leg). **Remedy = READ_CAP rule 19** (ruled 9/7).
- **Charter:** 9 contradictions (C1–C9: six-vs-eight checks · 250-line-only cap · frozen ledgers as cross-ref set · do-not-quote figure kept · outbox reserved twice · DM v1 premised on a struck rule · NETWORK table diverged from `_NETWORK.md` (FALCON/OSPREY absent) · 2b covers 1 of 3 routines · dead 100-line brief cap) + ~13 KB rationale in the always-loaded file.
- **Guards:** `--nudge` + `instrument_check` fire daily on INCIDENTS (backlog growing) = advisory overridden · no twin-diff on the catalyst calendar (9/18 position expiry absent from STATUS) · no version sweep · boot 6c's PENDING guard reads a section at byte 175 K · the "section STATUS field" extension proposed 8/10 (TRADE:207) never built.
- **Placement / retirement:** two STATUS archive homes; JOINT_PROPOSAL / BUILD_PLAN / GROUP_MAP / SCHEMA / FASTOW / root loose files (F13).
- **Better-than-blueprint (unchanged + new):** REGISTRY as machine state · LEDGER_GLOB's self-falsification · boot.py tri-state · SCRATCH candor · base-rate-before-threshold (9/7) · cite-by-section-name (8/21) · the 9/7 adjudication chain.

## 5. Load-bearing context / DO NOT TOUCH
- **`TRADE.md` is LIVE** — never freeze-banner; header stamp moves with body; it is in `LEDGER_GLOB`.
- **v5 SKEW-vs-DIRECTION guardrail** — "upside-convex" is positioning, not a price call.
- **TIMED-RACE frame** — price is the lagging tell; the clocks are the thesis.
- **Bidirectional exit** — sub-$75 = decoupling (confirming), break = <$70 on demand collapse; `$100` fired 7/23 and is NOT a live threshold.
- **The arm is RETIRED (8/7)**; R1/R2/R3 are named candidates, not tripwires; **the frame-breaker carve-out survives** and was adjudicated NOT MET on 9/7 with a Will amendment (SUNK-clause floor) applied the same day.
- **The retained set (rows 78–84) and the 17 sentinels — MOVE, never delete.** `COT-FUEL-35B` base `122,904.5` (carry the .5).
- **FROZEN banners on KB/VX/FLOW** survive any workbook touch. **PREDICTIONS scoreboard** — frozen numbers, never rolling percentiles.
- **Cessions:** HAWK kinetic/scenario-%s · LIQUID HY-OAS · HENRY CPI · TRADE position status · THESIS conviction · **RISK_RULES #5**: marks come from the live chain, never from a freshness check.
- **NEXUS_BRIEF is boot-read by NEXUS; TRACKER's top block is read by three routines** — both externally load-bearing.
- **MSG-v1 lane rules** (receipts ACTION-only; never convert WALTER signals).
- **Cite rulings by section name, never by line** (8/21).

## 6. Maturity snapshot
**L5 (Conf M) HOLDS — promoted 9/1 on one clean cycle; the 9/2 cycle FAILED the same leg (STATUS:119).** Per-leg verdicts in the review record §4. **Conf M→H not earned. Dated demote trigger: any derived-pointer disagreement at the cycle closing the 9/11 Friday pair → L4 at PR#6 (9/15).** Judgment layer = fleet reference; structure = one root defect with a ruled remedy (rule 19) whose first application site is BRENT's next closeout. Classification per `FLEET_MAP.tsv`.

## 7. Open questions
- Does BRENT take P1 (rule 19 on STATUS) at the 9/8 closeout or after the 9/11 Friday pair? (Its call; the demote trigger is keyed to the pair.)
- P2's live-clause audit of `TRADE.md`: BRENT alone, or one RAV slot (rule 3 option)?
- Composite convergence at L3: does the ladder require it over a graded registry? (9/14 sitting.)
- Per-glob `--days`: retire the design fleet-wide in favor of `--nudge` + per-desk measured `--days`? (9/12 tooling sitting — my item.)
- The Mon 9/14 09:45 routine: does it quote the AMENDED sunk clause? (BRENT's own SCRATCH test of files-win-on-drift.)
