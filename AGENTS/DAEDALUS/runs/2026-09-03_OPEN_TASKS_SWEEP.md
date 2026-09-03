# DAEDALUS — Open / pending task sweep · 2026-09-03 (Thu) 19:4x ET

**Purpose:** Will asked for a catch-up list. This is the register of every open item that names DAEDALUS, swept from: `STATUS.md` (9/2 close) · `inbox/` (10 packets, 9 unread since last close) · `PROME/DOCKET.tsv` · `PROME/GATES.tsv` · `PROME/WILL_QUEUE.md` · `sweeps_due.py` (boot) · `corrections_boot_check.py` (boot) · `read_cap_check.py --agent DAEDALUS` · on-disk existence checks for every artifact STATUS says is owed.

**Boot state:** sweeps none due (15 tracked) · PROFILE-CLOCK rc=1, 11 🔴 · corrections rc=0 · read-cap rc=0 (2 files at rotate-tier) · git: local 1 ahead of origin (PROME's `402cfb922`, not mine), WALTER + PROME + BOARD dirty outside my dir → no pull (none needed).

**Legend:** 🔴 blocking someone or dated today/overdue · 🟠 dated this fortnight or a silent-failure guard · 🟡 small / info · ⏳ watch, not mine to act.

---

## A. Dated / overdue — my builds and rotations

| # | Item | Due | State on disk (verified tonight) | Pri |
|---|---|---|---|---|
| A1 | **`scripts/docket_view.py`** — PROME 8/16 commission, Will-ruled window 9/3–9/5, DOCKET checkpoint row 9/5. `--write` SCRATCH marked block + `--check <prose>` never writes; §5 acceptance (would-have-caught `7ca6b0bdf` Colorado ROD · reproduction · 3 drills · idempotence). | 9/3–9/5 | **NOT STARTED** — no file at `scripts/` or `AGENTS/DAEDALUS/scripts/`. Day 1 of 3 is gone. | 🔴 |
| A2 | **`EVOLUTION.md` rotation** — 38,727 B = 119% of budget; STATUS dated the rotation "9/3, before the docket_view build". Oldest entries verbatim + crc32 → `archive/EVOLUTION_ARCHIVE.md` (un-suffixed container per 9/2 month-container amendment; banner the Aug file's range), until <22,785 B. | 9/3 | **NOT DONE** — still 38,727 B. | 🔴 |
| A3 | **`sweeps/GATE_BASIS_SWEEP.md` playbook** — registry row exists (last_run 9/2, `resolve_by` 9/16); owed before the WQ-162 run. | 9/16 | **FILE DOES NOT EXIST** — `sweeps_due.py` reads the row clean because it checks the row, not the playbook. | 🟠 |
| A4 | **H3 coordination scorecard render #2** (`scripts/coordination_scorecard.py`, DOCKET 9/4 row). Render #1 done 9/2. | 9/4 | script present (7,491 B). | 🟠 |
| A5 | **`CLAUDE.md` over budget** — 33,850 B = **104%** (STATUS said 99.7%; the 9/2 read_cap_check invocation note pushed it over). Charter says next edit net-neutral or trim first. `read_cap_check` does not list it (harness-loaded, not a Read) — the perimeter blindness STATUS already names. | now | 33,850 B | 🟠 |
| A6 | **STATUS.md + PATTERNS_HOT.md at rotate-tier** — 25,029 B (77%) and 27,416 B (84%), both ≥75%. STATUS = rotation per own rule. PATTERNS_HOT is GENERATED — cannot rotate; needs a generator-side decision (shorter hooks or a hot/cold split of PATTERNS itself). | this session | both 🟡 on `read_cap_check` | 🟠 |

## B. Inbox asks awaiting my action (9 packets, all delivered 9/2–9/3)

| # | From · date | Ask | Pri |
|---|---|---|---|
| B1 | **PROME 9/3 15:2x** | `scripts/claim_check.py --check weekday` is blind to weekday-AFTER-date (`9/6 Sat`), parenthetical (`9/6 (Saturday)`), and month-name (`Sep 6 (Sat)`) forms — a root closeout step 1e gate certifying files clean; TERRY STATUS L29 shipped through it. **Fix `RE_WEEKDAY` + add `--selftest` (6 cases + `satisfaction 9/6` negative control) + re-run over `AGENTS/*/STATUS.md` and report NEW flag count.** Reply = commit hash + count → `PROME/inbox/`. | 🔴 |
| B2 | **PROME 9/3 19:4x** | `scripts/ledger_staleness.py` FROZEN marker tripped by header prose ("spec frozen before the data") on BROCK's LIVE `PC_REDEMPTION_REGISTER.tsv` — live ledger silently reclassified, alerts suppressed. Verify at `git show 2fd4b3cfd` + predecessor; **(b) add negative control to selftest (PROME wants this regardless), (a) consider tightening to banner-position tokens.** | 🔴 |
| B3 | **CREED 9/2** | **WQ-100 "major fund" definition for CREED-T-06b — my clean read is Will-ruled second eyes; CREED encodes NOTHING until I reply.** Five attack points supplied: (1) ODCE-membership imports a third party's rules; (2) `$1.0B` is an un-sized round number, trap #4; (3) "gross real-estate assets" basis unpinned (GAV/NAV/total); (4) re-imposition clause untestable at n=1; (5) definition written after the trigger fired cannot be neutral about the next count. | 🔴 |
| B4 | **PROME 9/3 07:2x + CREED 9/2 §3** | **Tie-set canon case, n=2 desks in 4h:** CREED-T-01a `> 12` vs 12.00 print; RED FT-11 `≤ −4bp` strict-vs-non-strict = 1.7× fire rate, tie atom 41% of fires. RED's three clauses (declare strictness AND published precision at registration · base rate on the SAME operator the letter carries · audit EXIT legs too). PROME rec: fold into SPEC_LETTER_STANDARD as **SL-5**, forward-only, + a DATED one-time sweep of registered base rates for operator mismatch. **"Rule the home"** — encode, and deliver before idle. | 🟠 |
| B5 | **OSPREY 9/2 §4** | Registration-time design question, routed not self-ruled: negative-existence prediction's search-attempt guard has a date FLOOR and no CEILING (OSPREY cured 2 days after the window closed, took CONFIRMED legally). Fix = attempt must fall INSIDE the window; second defect = neither limb may key on the author's own activity ("published AND LOGGED"). **Rule or route** — fleet-wide prediction canon ⇒ likely a `FORGE/PREDICTION_DISCIPLINE.md` line via PROME/Will, with the dedup-AND-contradiction scan. Also routed to PROME. | 🟠 |
| B6 | **WAL 9/2** | R1 coverage count 27/37 may UNDER-report: WAL's line was self-applied 8/28 on Will's word, and my instrument's referent is my apply log, not charter presence. **Re-scan the 10 "unwired" desks for the LINE'S PRESENCE.** Rides the 9/26 withdrawal checkpoint (≥80% = 30/37). One command. | 🟠 |
| B7 | **CRUISE 9/2 §3** | `scripts/walter_route_check.py` scores the CORRECT two-lane rule as `[!] MIXED` — a compliant desk moving DEAD-ROUTER → MIXED reads as owed work; BRENT/CARL/CORAL/HANS/HENRY/REGINALD/SAM sit in that bucket. **Add a `TWO-LANE` class (or ordered-pair scoring) BEFORE the next run**; quote text not line numbers in packets. | 🟠 |
| B8 | **CORAL 9/2 §3 + OSPREY 9/2 §1** | **Obligation-audit as a REQUIRED leg of the read-cap remedy** — n=3 in one day (NEXUS dropped 2 owed actions, CORAL dropped the 9/8 Canadian counter-tariff row, OSPREY built a 25→31 OWED REGISTER). Byte checks passed at every point because a size remedy is supposed to shrink the file. **Encode: READ_CAP.md rule + PATTERNS row.** | 🟠 |
| B9 | **PROME 9/2 22:2x** | WQ-163 item 1 RULED as I adjudicated. **Registry line owed:** NEXUS `FLEET_MAP.tsv` L4→L5 re-promote condition = "cure complete" (split landed AND obligation ledger re-homed, verified by me at the artifact), dated to NEXUS's next boot (~9/11). Grep tonight: text NOT yet on the row. | 🟡 |

## C. Write-back tails owed off the same packets (step-7 chain rule: FLEET_MAP row + upgrade card + batch/run doc)

| # | Desk | What closed | Where the chain must close |
|---|---|---|---|
| C1 | CORAL | P1 read-cap EXECUTED (95,195 → 26,730 B, crc verified) · ⑯ mtime flag ENCODED (`boot.py` chain vintage→git→mtime, basis printed) | 8/28 read-cap batch · wiring sweep run doc · FLEET_MAP row |
| C2 | OSPREY | P1 discharged both surfaces (STATUS 164% → 83%, PREDICTIONS post-mortem rotation) · nudge-v2 EVENT-DRIVEN adopted · WQ-87 (d) `LIVE-DEFECTIVE-ESCALATED` cleared, OSP-06 registered | same + note: OSPREY self-declares a SECOND rotation due at its next closeout (83% > 75%) |
| C3 | CRUISE | 3 DEAD-ROUTER rows + a 4th unflagged (line 83) + leg B fixed · Staleness #4 FLOW.tsv REFRESHED + boot line 3d · FL-CRU-06 was 2.7× wrong (stale row ⇒ wrong row — fold into Staleness playbook rationale) | route-around census run doc (9/2) · `runs/2026-09-01_STALENESS_SWEEP_04.md` · FLEET_MAP row |
| C4 | CREED | wiring sweep 3/4 legs closed (② cadence declared + 8/27 nudge complaint WITHDRAWN · ③ `boot.py` RETIRED not wired, mtime-keyed · ① closed by ③); ④ info | `runs/2026-08-28_WIRING_SWEEP` · CREED upgrade card |
| C5 | WAL | R1 line present since 8/28; instrument referent correction | wiring sweep coverage table (feeds B6) |

## D. Sweeps and reviews on the calendar (all mine to run)

| Date | Sweep / event | Notes |
|---|---|---|
| **9/6** | PROME judgment-tail sweep #2 (`sweeps/PROME_SWEEP.md`, last 8/17) | L5 CONFIRM for PROME |
| **9/8** | Profile refreshes NEXUS · RED · PROME (`resolve_by`) · WQ-136 SPEC_LETTER checkpoint (carry forum-4 #11 conditional theater-bracketing residue) · ⏳ WQ-150 root ④ cold read (PROME's) | |
| **~9/9** | ⏳ WQ-155 ③ three-outcome projection spec from PROME → **adversarial review seat = DAEDALUS or RED** (pre-registered lens: half-normalized Brier is the only form byte-identical on binary rows; 4→3 collapse must be a declared mapping) | DOCKET 9/9 |
| **~9/11** | NEXUS next boot — B9 registry line dated to it | |
| **~9/14** | Wiring sweep #2 (⑲ clause-SET · WQ-88 slower-than-window · three 9/2 census legs: BRENT grade→machine-read hop · ZHAO `recheck_by` · LIQUID unattended writers) + **READS.tsv consumer half** of `read_cap_check` (R7-stage-2, DOCKET 9/14) · Falsification #3 (third-copy census PAT-137 (d)) · emphasis-defeats-gate sibling check | |
| **9/15** | Production Review #6 (promotions to confirm: BRENT/RED/VULCAN/WAL/CREED/AEOLUS/FLG conf M→H · TERRY/REGINALD/SHADE/LIQUID/HANS one-leg holds · CRUISE demote trigger · RAV checkpoint) · profile refreshes HANS · ORACLE · ZHAO · OTTO · MARCO · CORAL · YEYOU | 11 🔴 on profile clock tonight |
| **~9/16** | Doc-retirement first sweep (7 docs) · A3 GATE_BASIS playbook `resolve_by` | |
| **9/18** | ⏳ DOCKET: Amendment-12 watch grades (DAEDALUS/NEXUS) | |
| **9/22** | Staleness #5 — with the month-container check leg (`runs/2026-09-02_MONTH_CONTAINER_CENSUS.md` grep B); playbook edit at the run | |
| **9/26** | R1 withdrawal checkpoint (coverage ≥80%) — B6 changes the count | DOCKET row 204 |
| **~10/5** | Harness audit (`sweeps/HARNESS_AUDIT_SWEEP.md`, last 7/7) | |
| **10/6** | ⏳ DOCKET: delegation-tier falsifier grades (PROME/DAEDALUS flag on R3-rider compliance) | |

## E. Build queue behind A1 (undated, in STATUS order)

P2 `read_cap_check --agent` fleet mode + P3 `catalyst_countdown` consolidation (WQ-109 APPROVED) → `registry_chain_check` (Class-7 arm; PortWatch positive control) → `gates_pointer_check` v1 advisory (contract reply sent 9/1) → WAKE-LIST `fleet_triage.py` (approved 8/21) → catalysts_alert · ratification_check (sketch never located) · forum-4 #11 registration-time checklist · WQ-117 A HANS finding_check → shared library · DOCKET "next-DAEDALUS-vocabulary-pass": UNOBSERVABLE state token (FORUM-5 deferral, ratio instrument first) · DOCKET 9/7 FORUM-6 R10 scan_report scope-stating instrument (WALTER+DAEDALUS; build only when a named invocation site exists).

## F. STATUS corrections found by this sweep (my own board was stale in three places)

1. STATUS "NEXT SESSION (9/3)" line lists **CHECK_STANDARD §14 (WQ-117 B)** as owed — **it is encoded** (`CHECK_STANDARD.md` L115). Same line lists WQ-112/WQ-86 lines — both cited in `STRICT_TEXT.md` / `market-agent.md`; confirm at the edit, then strike.
2. STATUS says `CLAUDE.md` = 99.7% — it is **104%** (A5).
3. STATUS names `sweeps/GATE_BASIS_SWEEP.md` as a playbook owed; the registry row points at a file that does not exist (A3) — `sweeps_due.py` cannot see a missing playbook. Candidate guard: registry row whose playbook path is absent ⇒ warn.

## Recommended order for the next working block

1. **A2** EVOLUTION rotation (mechanical, ~15 min, unblocks A1 by the letter of my own board).
2. **B1 + B2** — two `scripts/` guard defects, both SILENT-CERTIFYING, both with reproductions supplied; each is a regex + selftest + one reply packet.
3. **B3** CREED WQ-100 read — a desk is blocked on a Will-ruled encode.
4. **A1** `docket_view.py` — the build; the window is Will-ruled and two-thirds gone.
5. **B4 / B8 / B5** canon encodes (SL-5 tie-set · READ_CAP obligation-audit rule · negative-existence window ceiling), then **B6 / B7 / B9** instrument fixes and the registry line, then **C1–C5** write-back tails.
6. **A3, A4, A5, A6** own-surface hygiene at closeout.

*Sweep author: DAEDALUS. Nothing in this file mutates another desk's surface. Inbox packets stay in `inbox/` until each is actioned; `processed/` moves ride the action commit.*
