# WIRING SWEEP — RUN RECORD, 2026-08-28 (Fri)

**Owner:** DAEDALUS · **Register:** `sweeps/WIRING_SWEEP.md` (input, ㉕→㉘ after today) · **Commitment:** `sweeps/WIRING_SWEEP_CUT_LIST.md` (6 legs named in advance, promised to PROME "before Friday") · **Readers:** 12 read-only sonnet subagents, every report in this directory (`leg17_*`, `leg20_*`, `leg21_*`, `leg01_*`) — evidence lives there, this record synthesizes and does not restate (PAT-100).
**Method inputs absorbed (⑥/⑥b/⑦):** "not named in the protocol ≠ not covered — ask which INSTRUMENT covers it before recording a gap" applied on every leg; timeline-before-blame; row-granularity re-check; anchor-audit uptake treated as a coverage axis, not a leg.
**Brief errors (PAT-128 — a spawn brief is unverified input):** 3 caught by readers, recorded not hidden: GATES.tsv has **29** data rows, not 38 (my `grep -c .` counted 9 comment lines); TERRY's boot does **not** read `FORGE/STATUS.md` and `paper_book_mark.py` is content-derived, not mtime (my ⑯ grep matched the word "touched" in a docstring); ⑰ sample line numbers were off on 3 desks (LABOR +1, LIQUID +2, OSPREY +6 — the sampler skipped comment lines; readers cited verified `file:line`).

---

## 0. The count, reconciled (PAT-132: count by KIND before sizing)

| Kind | Cut-list count | Today |
|---|---|---|
| Already discharged (verify → strike) | 2 (⑤, ⑤b) | **STRUCK, both VERIFIED at artifact** — ⑤ = CHECK_STANDARD §12 + §1 PROXIMITY-NOT-PRESENCE (Batch B, `0416eaa40`); ⑤b = §3 monkeypatched-legs + §6 DECLARED ASYMMETRY + §8 rule 6 GLYPH-VS-COUNT + ZHAO `boot.py:298-301` comment. **+1 more stale carry found today: ⑬②/⑬⑤ (memory-wording → Will) were RULED 8/21 Batch A** — `memory/auto/MEMORY.md` preamble carries both approved lines (`symptoms:`, promotion flag). Struck. *Three discharged rows carried as open in a register I wrote five days ago — same class as PAT-132's own founding instance.* |
| Method inputs | 3 | applied |
| Will-gated deliverables riding the date | 3 (㉑, ⑱, ⑬) | ㉑ **DELIVERED** (memo → PROME) · ⑱ **DECIDED: DECLINE-WITH-TRIGGERS** · ⑬ struck (above) |
| Real work items | 18 → committed 6 | **6 landed** (§1–§6) · 12 deferred with destinations unchanged (§7) |
| New legs registered today | — | ㉖ machine-local untracked (PROME) · ㉗ ruled-kill-never-reached-counterparty (CREED) · ㉘ occasion-vs-artifact carry rows (CREED → PROME lane) |

---

## 1. Leg ⑰ — METRIC-SURFACE AUDIT (audit form, two-leg test, per-leg on conjunctions)

**Sample:** seeded (`random.seed(20260828)`) 8 desks × 5 rows from 22 VX/THRESHOLDS/TRIGGERS registries (MARCO+AEOLUS excluded as base-rate donors, RED live, HANS = leg ㉑) = 39 rows; plus `PROME/GATES.tsv` whole (29 rows). **n = 68. A sample, not a census — generalise the SHAPE, not the rate.** Population: 30 registries / ~1,130 rows + 29 PREDICTIONS ledgers / ~580 rows.

**⚠️ Method finding first:** the sampler did not screen for FROZEN banners — LABOR `VX.tsv` and LIQUID `VX.tsv` are both FROZEN (correctly, 7/11), so 10 of 39 desk rows are point-in-time snapshots by design. **The registry population count overstates the LIVE threshold population; any fleet base rate must exclude frozen ledgers.** Live desk rows below = 29.

| Test | Live desk rows (n=29) | GATES.tsv (n=29) | Reading |
|---|---|---|---|
| (a) INSTRUMENT: no command returns the number (NONE + PROSE-VALUE) | **17 / 29 = 59%** (15/27 excl. 2 correctly-retired) | 11 / 29 = 38% (+3 PARTIAL-legs, +1 WRONG-SERIES that IS command-named) | The fleet gate registry is materially better instrumented than desk registries |
| (a) PRODUCER-EXISTS-UNCITED (CREED state 2) | 3 | 4 | wiring gap, cheap — but see state-3 trap before wiring |
| (b) BASIS/WINDOW fully STATED | **14 / 29 = 48%** | **24 / 29 = 83%** | MARCO's finding replicates at the desk level: unstated basis/window is the dominant desk-registry defect (PARTIAL 11, UNSTATED 3) |
| CANNOT-FIRE (a dead leg on a conjunction) | 2 | **5** (BRENT-SUSTAIN freshness leg · LIQ-069 2-of-5 · LIQ-076 1-of-3 · LIQ-079 ARM leg wrong basis · TERRY-006 wrong series, retired) | 7 / 58 live rows = 12% render a state indistinguishable from NOT-FIRED |
| POINTER present | ~8 / 29 (NO-POINTER dominant, ~70%) | 28 / 29 | **CREED's falsifying question answered: on rows that HAVE a pointer, wrong-referent hit rate = 2 / ~36 (6%) — GATE-TERRY-006 WRONG-SERIES, GATE-LIQ-079 WRONG-BASIS, both in GATES; no in-repo C3 found. On desk rows the dominant state is NO POINTER AT ALL — a dereference check has nothing to dereference. Verdict: the C-class is real but not concentrated; the bigger desk-side defect is pointer ABSENCE** |
| BOOT-RENDERED | 8 / 29 (FERT 3 flag-only, MIDAS 4, LIQUID successor 1; HAWK/OSPREY/BOND/FLG/LABOR = 0) | ~7 / 29 | LIQUID's severity axis ("renders on a boot surface") applies to <30% of live rows |
| STATIONARITY flag (FIXED-ON-DRIFTING) | 2 (BOND-10 nominal issuance level un-rebased; HAWK-SULPHUR fired on a ~5-month-stale number) | 0 | LIQUID's remediation question ("is the underlying stationary?") is worth asking on every fixed level; n=2/29 here |
| SCANNABLE-AGREES (GATES only) | — | AGREE 24 · **DISAGREE 3** (TERRY-ARM3 mild, FERT-G5, CORAL-MSI-01 — `INSTRUMENT` with no producer) · **CELL-BLANK 1 (GATE-VIO-RV1 is a field-count-mismatched row)** · CANNOT-JUDGE 1 | PROME-owned fixes; the malformed row is the loudest |

**Triage by desk (MARCO's C/D/E form):** CONVENTION-dominant 6/8 (FERT: no fetch scripts by design + flag-only boot; FLG: pre-live, header says so; HAWK: `boot.py` FROZEN and unwired → nothing boot-rendered; LABOR/LIQUID: FROZEN ledgers; OSPREY: no `scripts/` at all, qualitative bands with per-claim not per-band sourcing) · PER-ROW 2/8 (BOND strong with 2 self-flagged rows past their own deadlines; MIDAS strongest-instrumented desk sampled, every gap disclosed on the row). **Do not rewrite rows for a convention defect** — the fix is one header line or one boot wire per desk. Per-desk flags routed (§8); never mass-edited.

**Taxonomy shipped:** `design/2026-08-28_INSTRUMENT_STATE_TAXONOMY.md` — CREED's six states + ORACLE's zeroth (SPECIFIED-BUT-NONEXISTENT) + VULCAN's state 4 (band keyed to the wrong mechanism), with discoverer + the "remedy for 2 creates 3" trap. VULCAN's mechanism question (is the band keyed to the mechanism the evidence arrives through?) was asked on every sampled row: MISMATCH 1 (LIQUID-7.02 superseded framing), CANNOT-JUDGE ~8, MATCH the rest — **VULCAN's class is real (n=3 fleet incl. CREED's self-instance) but not dense in a random sample; it concentrates on desks whose thesis has moved faster than their bands.**

## 2. Leg ② — THE VOCABULARY BLOCK (one sitting, so nothing forks)

**Shipped in `BLUEPRINTS/STATE_VOCABULARY.md`** (+ hot/cold split to `STATE_VOCABULARY_PROVENANCE.md`, because the file sat at 58% of the read cap and the mints would have breached the 60% budget — 5.3 KB of ruling/provenance narrative moved verbatim, 99 table rows conserved, hot file now 60.0%):
- **Class 2:** `CANNOT-FIRE` (a leg has no metric surface; per-leg, never per-gate) · `UNOBSERVABLE` (instrument exists, the world may never emit — DOCKET 188 / FORUM-5 BRK-25) · `CONTESTED` (a leg another desk owns is disputed; adjudicator + review date on the row). **LIQUID's instance re-cut to `CONTESTED`** per PROME's 8/27 correction, verified at LIQUID's retraction. The three Falsification-#2 exemplars promoted to canon (AEOLUS per-leg render · HENRY non-latching AND with per-leg counts · VULCAN dated retrofit rail) + AEOLUS's `total · range · moved · fired` display form.
- **Class 8:** `Cadence: SCHEDULED next_due=YYYY-MM-DD` · `Cadence: EXEMPT-BY-CHARTER — <clause>` · `PINNED` (row-level, READ from the Kernel record, never declared — the THIRD ledger state). **Enforcement LIVE** in `ledger_staleness.py --nudge` (§5).
- **Class 8 extension — DESK cadence class** for the ROSTER column (Will-approved 8/21 item ②): `DAILY · WEEKLY · MONTHLY · EVENT-DRIVEN · ON-DEMAND` — same word, same meaning at two granularities; PROME applies, `fleet_triage.py` reads.
- **Class 8 extension — catalyst `date_class`:** `CONFIRMED · ESTIMATED · MODELED · EXTERNAL` (ZHAO census; VULCAN conforming); schema-case ruling (VULCAN ⑮b): `lower_snake` on NEW files, no renames under graded rows, readers case-tolerant.
- **STRICT_TEXT rule 6:** LABOR's ordering convention (live value in the most-read position; as-made/archival as labelled companion). **Rule 7:** the Will-ruled forward registration bundle (a) exact contract or ticker+roll (b) frozen value + as-of + anchor TYPE (c) observation date + read date for lagged series, **+ (d) CREED's exact-locator rule** (table/column/row-label, never a document name).
- **Class 10** gains the occasion-vs-artifact sentence (§7 ㉘).

## 3. Leg ⑯ + ⑪ — the false-clean generators (one pass, shared root cause)

| Class | Instrument | Found | Disposition |
|---|---|---|---|
| ⑪ hardcoded catalyst list in boot | grep literal ISO dates in 23 `boot.py` | **OZK `boot.py:32-40`** — 8 inlined rows, two already past (7/21, 7/31), the file's own comment `:43-45` says it "silently lags"; its 8/7 profile flagged the same. HENRY's 2 literals are self-test fixture dates (benign, and `finding_frozen_fixture_control_is_blind_to_resolution_faults` applies). **n=1 live / 23** (ZHAO's fixed 8/21) | OZK packet: replace with a `docket/CATALYSTS.tsv` read (ZHAO form + VULCAN owner-field fix) |
| ⑯ activity/mtime proxy as the ONLY boot staleness read | grep `st_mtime|getmtime` in boots × cross with `ledger_staleness` invocation | **4 desks — CORAL `:60`, CREED `:47`, LABOR `:113`, OZK `:265` — key ledger age on mtime and never call the content-vintage enforcer**; git sync restamps mtime, so the receiving machine reads every ledger FRESH after a pull (`finding_mtime_is_corrupted_by_git_sync`, n+4). CARL/HENRY/MARCO also use mtime but ALSO run `ledger_staleness` (duplicate display, not a blind guard). AEOLUS's `domain_log_check.py` "touched" proxy = the self-reported instance | 4 owner packets: call `scripts/ledger_staleness.py <X> --quiet` (already content-first) or port the chain |
| ⑯' ORACLE's grep target — "context / not in the arithmetic / informational only" annotations | grep fleet TSV headers + scripts | **22 files** carry such an annotation (population, not defects); ORACLE's n=1 shows the annotation exempts the value from review | Registered as a standing ⑯ sub-leg; no packets on a population count |
| ⑫(a) `catalyst_countdown.py` forks | md5 + grep | **10 forks, 10 distinct hashes.** Fired-row rule (OTTO 7/25) present in 5 (CARL, LABOR, OTTO, VULCAN, ZHAO), **ABSENT in 5 (BRENT, HAWK, MARCO, SAM, VIOLET)** → fired rows age out unswept on those desks. mtime-keyed window in 3 (OTTO, VULCAN, ZHAO) — all three PRINT the basis (`mtime⚠️`) as last resort behind git-commit vintage (ZHAO's reference form; VULCAN confirmed NOT re-porting OTTO's bug). SAM's fork also drops past rows silently when upcoming rows exist (`:116-143`, latent, 0 today) | **Consolidation proposal → Will (§9 P3)**; 5 owner packets meanwhile |
| ㉕ profile self-declared staleness triggers | hand-classified all 34 | **Fully machine-evaluable 11 · mixed 15 · prose-only ("materially changes") 7 · none 1 (PROME).** Day-clock legs (`>Nd`) on 25/34; **7 EXPIRED today** (CORAL 37/30d · HANS 49/45 · MARCO 49/45 · ORACLE 60/45 · OTTO 52/45 · YEYOU 55/45 · ZHAO 52/45) and **0 of 34 are read by any boot step** — the refresh queue hand-tracks 3 of those 7 | Base rate justifies the cheap half: a `profile_clock_check.py` over the day-clock leg only (≥3 desks; build after R1) |
| VULCAN items 6 + 7 (one-directional reconcile; loop membership is per-SECTION, headings assert freshness) | ⑳ VULCAN audit | **Confirmed live** — boot step 8 channel-liveness is SILENT-BY-CONSTRUCTION; score reconcile checks the number beside rotted prose | Blueprint candidates at next market-agent touch (L-17 neighbour); VULCAN packet |

## 4. Leg ㉔ — READ-CAP EXPOSURE, fleet base rate (founding instance mine, discharged 8/23)

**Instrument:** 25,000-tok harness single-read cap × 2.17 B/tok (measured fleet markdown) = **54,250 B = 100% of cap; 32,550 B = the 60% budget**. **Positive control from PROME today:** `INDEX_COLD.md` truncated silently at 58,825 B (108%) — the cap number is confirmed live, not derived.

| Measurement (169 common boot-read surfaces × 39 desks, 2026-08-28) | Result |
|---|---|
| Surfaces ≥100% of cap (cannot be read whole) | **62 / 169** |
| Surfaces ≥60% (over budget) | 94 / 169 |
| **Desks whose `STATUS.md` alone is over the CAP** | **18 / 39** — BOND 295% · LABOR 279 · HOMER 273 · SHADE 231 · LIQUID 221 · VULCAN 217 · BRENT 208 · REGINALD 205 · CARL 180 (after a −49% rotation) · CORAL 175 · BROCK 167 · TERRY 166 · HENRY 163 · SAM 146 · OTTO 128 · MARCO 126 · RED 123 · FALCON 107 |
| Desks with ≥1 surface over the cap | 28 / 39 |
| MIDAS replication (>40 KB files that pass a 250-line cap) | **61 / 90 = 68%** (MIDAS measured 22/38 = 58% on n=75) |
| ⑳ sample (5 desks, boot-MANDATED whole reads) | **5 / 5 desks mandate ≥1 over-cap read**; SAM mandates 4 of 6 (≈385 KB before the market refresh); VULCAN's own `CLAUDE.md` is over the cap (55,864 B) |
| Line caps | LIQUID 218/250 · VULCAN 205/250 · HENRY 249/250 · TERRY budget **150,000 B self-declared = 2.8× the harness cap** — every line/self-set guard passes clean on a file the boot cannot read whole |

**Reading:** the fleet's boot protocols mandate reads the harness cannot perform; the protocol stays written and execution degrades to fragments (PAT-111, n now fleet-wide). The 8/17 "owner sets the byte budget locally" convention produced budgets above the physical cap. **Proposal → Will (§9 P1/P2).** INDEX_COLD TRIM-vs-SHARD read given to PROME (trim now: ~13 KB of hook mass; shard when the trimmed file re-crosses 80% of the 53,819 B hard line).

## 5. Leg ⑳ — BOOT-SEQUENCE AUDIT (5 desks, chosen by boot complexity; RED excluded as live; SAID SO)

**Unit = DELIVERED CONTENT vs the step's CLAIM.** Boots executed where write-free (HENRY, LIQUID, VULCAN, TERRY; SAM static + `--tools` only — its sequence writes TSVs and hits network). Trees clean before and after; no PAT-054 self-mutation found.

| Desk | Most consequential (evidence in `leg20_<DESK>.md`) | Verdict class |
|---|---|---|
| **HENRY** | (1) **put wall == call wall 7,700 printed with NO warning at today's boot** — the tie/near-tie guard exists in `gamma_flip.py:283-309` and in the returned dict, `boot.py:gamma()` never reads it; the exact recurrence the file's own 7/28 comment describes. (2) `boot.py:158-161,:494-496` claim the gamma read auto-publishes to `PUBLISHED.tsv`; `_publish()` runs only from `gamma_flip.py main()` — corroborated: 19/21 ledger rows are 35d while boot only requests 14d. (3) `consumer_check` output hard-cut at `keep[:26]` with no "N more". | SUBSTITUTED · SILENT · DELIVERS-PARTIAL |
| **LIQUID** | (1) `build_domestic()` (`boot.py:179-255`) has no `else` on fetch failure for 8 series incl. headline DGS30 — the row vanishes, only the summary error count moves (static; 0 errors today). (2) CCC yellow `960` hand-typed vs shared `config.py` (900,1000) — a silent fork between two "same-zone" instruments. (3) VX FROZEN correctly, but 3 rows (FTD, auction tail, Japan TIC) have no successor instrument anywhere. Watcher timer verified live. | SILENT (latent) |
| **SAM** | (1) `thresholds.py:53-58,217-220` prints the three JGB thresholds as `⚪ MANUAL CHECK` in the same visual form as live FX/oil rows while `jgb_yields.py` fetches the data in the same run. (2) **Step 6 (scan 70 predictions) has NO instrument** — zero scripts read `thesis/PREDICTIONS.tsv`; the file's own preamble records a 6-day stale-count incident. (3) 8 of 14 boot-wired scripts CANNOT-JUDGE without execution — `rate_differential.py` (built 8/27) is the least-reviewed. | SUBSTITUTED · CANNOT-JUDGE-BY-DESIGN |
| **TERRY** | (1) **21d anti-rot flag SILENT on the rich status vocabulary it was widened for:** `_is_active` (`:253-255`) widened to substring on 7/30, the flag (`:278-281`) still gates on exact `{LIVE, LIVE-WEAK}`/`DECAYING` → 3 of 12 active `SIGNALS.tsv` rows at 36–65d printed with no flag today (`:12,:14,:16`). (2) `RISK_SCORING.md` absent from `boot.py REQUIRED`. (3) Self-declared STATUS budget 150,000 B vs 54,250 cap. | SILENT (split-brain fix) |
| **VULCAN** | (1) Boot step 8 (channel-liveness) SILENT-BY-CONSTRUCTION — no leg reads `## LIVE CHANNEL READS`; the score reconcile (symmetric, well-built) checks the NUMBER beside rotted PROSE; VULCAN's own `STATUS:35` documents the rot. (2) `THESIS.md` in no boot loop — the SPAWNED card says read it third; the numbered sequence never names it; `score_reconcile` never opens it. (3) `docket/CATALYSTS.tsv` excluded from the leg-1 staleness scan (own output says so). **Live cross-desk catch:** MU FQ4 date VULCAN ~9/22 vs VIOLET ~9/29 `ESTIMATED` — surfaced by VULCAN's own countdown, unreconciled. | SILENT-BY-CONSTRUCTION |
| **PROME** (6th datum, self-reported) | `prome_gate.py:556` advisory says "run `agent_freshness.py`" without a directory; the tool exists at `PROME/tools/` — an UNQUALIFIED path, not a dead pointer (PROME's read corrected at artifact) | remedy-not-executable |

**R1 wiring found at 0/5** (expected — coverage is 1/37 fleet-wide). **Every desk's numbered boot sequence passed the naive audit ("does the step name the file?") and every desk failed at least one step on delivered content** — PAT-125 confirmed 5/5, sample named, not fleet coverage.

## 6. Leg ① — R1 GENERIC BOOT-LEG, first tranche + coverage

- **Coverage this morning: 1 / 37 (2.7%)** — DAEDALUS only. Withdrawal test leg (b): ≥80% receipt coverage by **2026-09-26** = 30 desks.
- **Anchor survey complete on all 37 charters** (`leg01_R1_ANCHORS_{A,B,C}.md`): 36 landable (31 verified-unique insert-after anchors + 5 re-cut as insert-BEFORE the unique `### EXECUTE` heading); **RED + PROME live → packets; RAV has no `CLAUDE.md` (not applicable)**. `registry/` exists at 3/37 (CREED, RED, WALTER) — first receipt creates it. 13 charters already ≥32,550 B (VULCAN 55,864, WALTER 67,664) — auto-loaded not Read, so not a cap failure, noted as context cost.
- **Changelist → `design/2026-08-28_R1_BOOT_LINE_CHANGELIST.md`, one identical line per desk, IN FRONT OF WILL** (AUTHORITY rule 1: batched express permission; rule 2: idle-target re-check at apply). **On approval, 36 edits + 36 path-scoped commits in one session → coverage 37/37 wired; receipt coverage then accrues at each desk's next boot.**
- ✅ **APPLIED 2026-08-28 11:2x on Will's in-session word ("Approve — apply to all idle desks now"):** **28 charters wired, one path-scoped commit each** (AEOLUS BRENT CREED CRUISE FALCON FERT HANS HAWK HOMER LIQUID MIDAS ORACLE OSPREY OTTO RED SAM SHADE TERRY VIOLET VULCAN WATT YEYOU ZHAO BOND BROCK CARL CORAL DEWEY); 0 failures; every anchor re-verified unique at edit time. **Skipped under AUTHORITY rule 2, packeted instead:** FLG/REGINALD/WAL/OZK (idle sessions), LABOR/HENRY/MARCO/NEXUS/WALTER (trees dirty = in-flight spawns), PROME (own hand, `BOOT.md`), RAV (no charter). **Coverage 1/37 → 27/37 at the first pass → 29/37 = 78% after (i) PROME wired its own line in `PROME/BOOT.md` step 5b + `prome_gate.py` advisory with first receipt COR-20260828-01 on file (VERIFIED at artifact, check rc=0) and (ii) MARCO applied on a second pass — no MARCO session live, charter clean, the tree's only dirt an untracked WALTER dispatch in `inbox/WALTER/`. ⚠️ `--coverage` scanned CLAUDE.md only and under-counted PROME the hour it wired (its boot lives in BOOT.md by rule) — scan set widened to CLAUDE.md + BOOT.md the same hour (PAT-084: the instrument's own scan set was narrower than the fleet's boot-surface forms). Unwired (8): WALTER, NEXUS, HENRY, LABOR, REGINALD, OZK, WAL, FLG. **The 9/26 checkpoint needs 30/37 — 1 more.**
- **Landing-slip clause honoured:** the build did not slip (8/26); the tranche is the whole fleet pending one word. If Will declines or defers past ~8/31 I name it and row 204 slides.

## 7. Deferred 12 — destinations unchanged, three updates

③ Will-withheld · ④/⑨ PROME decision rows · ⑧ derived-vector predicate → sweep #2 after ⑰ (now has 68-row data) · ⑩ H1-vs-Version → fold into ⑰ #2 · ⑫ re-scoped: countdown half answered today (§3), FORK question → **consolidation proposal P3** · ⑭/⑮ owner packets (VULCAN ⑮a donor defect confirmed at ZHAO `boot.py`? — NOT re-checked today; carried) · **⑲ clause-geometry: NOT scanned today** — PROME's packet is n=1 with a scan-unit rule (row's clause SET across fields; un-assemblable ⇒ UNSCANNED); a field-limited scan would report a clean census and close a real class, so it waits for sweep #2 with the unit built in · ㉒ applied inside ⑳ (HENRY's tied wall feeds a STATUS write, not an escalation; OZK's precedent stands) · ㉓ redaction-for-scope → sweep #2 / soak · **⑬②/⑬⑤ STRUCK (ruled 8/21)**.

**New today:** **㉖** machine-local untracked files (PROME 8/28; PAT-129 extension — the perimeter is one box) · **㉗** a ruled KILL of a cross-desk arrangement produces no artifact, the counterparty's checks pass clean (CREED n=1) — **cheap base-rate query registered for PROME's lane:** grep ruling records for kills/retirements of 2+-desk arrangements; check the NON-deciding desk's `inbox/` + `processed/` · **㉘** a carry row keyed to an OCCASION is discharged by the occasion (CREED row 33; 47 `COVERED:` rows = population, n=1 defect) → Class 10 sentence added + PROME-lane discriminator ("does the row name the ARTIFACT owed?").

## 8. Shipped in-lane today (all §3-watched, all Will-visible in the batch below)

| Change | Evidence |
|---|---|
| `scripts/harness_caps.env` `MEMORY_WARN_PERCENT` 80→**75** + `check_memory_length.sh` message names the flow rule + `memory_index_check.py` default re-keyed | fixtures: 78% WARN rc1 · **76% WARN rc1 (the exact 8/27 value that printed OK)** · 74% OK rc0 · live 71% OK |
| `scripts/ledger_staleness.py --nudge`: `SCHEDULED next_due=` / `EXEMPT-BY-CHARTER —` declarations + **Kernel-pin caveat** read from `AGENTS/*/outbox/kernel/submissions/*.json` + `KERNEL/shadow/events/*/*/*.json` | 9-ledger fixture: future-scheduled ℹ️ · past-scheduled counted behind with date · unparseable `next_due` 🔴 rc2 · exempt-with-clause ℹ️ · bare exempt 🔴 rc2 · bare-prose trap NOT declaring · pinned row ⛔ named · all-quiet rc0 with ℹ️ lines (not the "clean" line) · **real CREED pins: 3 PRED rows named**; OSPREY/MIDAS/`--all --quiet` regressions unchanged |
| `STATE_VOCABULARY.md` hot/cold split + ② mints (§2) | 99 table rows conserved; hot 60.0% of cap; `STATE_VOCABULARY_PROVENANCE.md` 13% |
| `STRICT_TEXT.md` rules 6 + 7 (§2) | 18% of cap |
| `STATUS_TWO_STATE_PILOT.md`: second failure condition re-specified ABSOLUTE (CARL's denominator defect) + HENRY/CARL seat results | three seats: mechanism confirmed 3/3, cap fits 0/3 |

## 9. Proposals → Will (via PROME registration; R1 asked directly)

- **P1 — Fleet byte budget for boot-mandated whole-read surfaces = 32,550 B (60% of the harness cap), derived from the cap, binding ABOVE any owner-set number.** Owners keep choosing HOW (two-state rotation — confirmed on 3 seats — or hot/cold split), never WHETHER. Per-surface caps, not joint (CARL). Evidence: 18/39 STATUS over the CAP today; TERRY's self-set 150,000 B.
- **P2 — `read_cap_check.py --agent <NAME>` fleet mode** (my lane): measures each desk's boot-mandated read set; exact set needs R7-stage-2 `READS.tsv` (~9/14), interim heuristic = STATUS + files a boot step names with "Read". Don't-build-until-≥3-desks: satisfied 18×. Then per-desk boot wiring = a second R1-style batch.
- **P3 — `catalyst_countdown.py` consolidation:** one shared `scripts/catalyst_countdown.py` seeded from ZHAO's form + VULCAN's owner-field fix + OTTO's fired-row rule, desks opt in by deleting their fork; measured: 10/10 distinct, 5/10 lack the fired-row rule. Don't-build stays a real answer if Will prefers 5 owner patches.
- **P4 — Correction-class validation C1–C5** → `design/2026-08-28_CORRECTION_CLASS_VALIDATION_PROPOSAL.md`.
- **P5 — Un-rotatable correction mass (HENRY):** may verbatim-preserved superseded text live in the ARCHIVE half with STATUS carrying the retirement block + pointer? Preservation ≠ position; DELEGATION_TIER rider R2 says "in place" — Will's call.
- **⑱ DECLINE-WITH-TRIGGERS** → `design/2026-08-28_GENERATED_VIEW_BUILD_OR_DECLINE.md` (row 89).
- **㉑ HANS nomination** → `reports/2026-08-28_HANS_EUROPE_MACRO_NOMINATION.md` (BOND triage-depth; HANS stays Tier-2 deep-dive seat by revival-proxy on trigger; no build).
- **R1 batch** → `design/2026-08-28_R1_BOOT_LINE_CHANGELIST.md` — asked in-session.

## 10. Packets routed (flag, never fix) — see `outbox/` + each recipient's `inbox/`
OZK · HENRY · LIQUID · SAM · TERRY · VULCAN · VIOLET · CORAL · CREED · LABOR · BOND · HAWK · FERT · BRENT · MARCO · CARL · ORACLE · RED (live — doorbelled) · PROME (consolidated, live — doorbelled). Each carries file:line, the verdict token, and the reader report path; none carries an edit.

## 11. What this sweep could NOT see
- ⑰ is a 68-row sample over ~1,700 rows; frozen ledgers were sampled by accident; no external primary was fetched (all C3 = UNCHECKED-EXTERNAL).
- ⑳ is 5 desks; SAM's 8 network/writing scripts are CANNOT-JUDGE; disposition steps (does the analyst act on a flag?) are behaviour, not mechanism.
- ⑲ not scanned; ⑭(a) VULCAN's cross-file catalyst count not run; ⑮(a) ZHAO's over-match ratio not re-checked.
- Fan-out reader verdicts were spot-checked, not re-derived; every verdict carries file:line so a second reader can.
- The read-cap constant (2.17 B/tok) is content-dependent; the 58,825 B truncation confirms the order of magnitude, not the digit.

## 12. Next
**Sweep #2 (~9/11–14, ride Falsification #3):** ⑲ with the clause-set unit · ⑧ · ⑩ · ⑰ #2 on the LIVE-only population with FROZEN screened at sampling · ㉓ · ㉗ query. **Before that:** R1 apply on Will's word → coverage % → `profile_clock_check` (㉕ cheap half) → `read_cap_check --agent` (P2 on approval) → CHECKS.tsv rotation (mine, 113%). **Staleness #4 ~9/1** carries the Class-8 declarations as a grading leg.

---

## 13. Post-run write-backs (same day, verified by the owners' own messages — verify at the artifacts before citing as CLOSED-VERIFIED)
- **PROME 11:2x:** row 89 → DECIDED-DECLINE-WITH-TRIGGERS (awaiting Will) · HANS memo → **WILL_QUEUE row 108** (needed-by 9/4) · P1–P5 → **row 109** (PROME rec: P2+P3 approve; P1 as a fleet cap over owner numbers; P4/P5 one sitting each) · **GATES.tsv repaired from `leg17_GATES.md`:** VIO-RV1 field split fixed (12/12 fields), FERT-G5 + CORAL-MSI-01 re-tagged `JUDGEMENT`, LIQ-069/076/079 state cells annotated `CANNOT-FIRE` (079's wrong-basis ARM leg stays LIQUID's repair); TERRY-ARM3 (mild) left · PROME's own R1 line goes in `PROME/BOOT.md` by PROME's hand.
- **RED 11:1x:** "apply when idle" — RED joins the batch (label `9e.`, path-scoped, only when `ListAgents` shows red-96 idle).
- **NEXUS 11:1x (scoped to the pin instrument only; blind-parallel rule held both ways):** its "15 of 26 briefs lack a STATUS pin" figure is RETRACTED and re-cut **16/26 (62%) in three classes** — A pin present+comparable 10 · B field absent 12 · **C field present, value absent 4 (CORAL, HAWK, OSPREY, VIOLET — a pointer is not a pin)**; its own `grep -L 'STATUS commit:'` measured a string, not a pin (3 false positives, 4 false negatives). Not used in this sweep; banked for the 8/29–31 review. Class C is the same shape as three ⑳ findings today (presence-checks certify the wrong thing).
- **consumer_check on the 80%→75% memory-warn tier:** the tool cannot discriminate a bare percentage (985 fleet hits, all unrelated "80%"s; 21 own-surface hits incl. the R1 "≥80% coverage" threshold) — **no packets sent on a bare 2-sig-fig figure, per root 1c.** Hand-verified: the only surfaces that named the tier (the script's own OK line, CHECKS.tsv row, `memory_index_check` default) are all re-keyed; root CLAUDE.md 1d carries no number.
- **Ledger nudge:** `SURFACES.tsv` 2 STATUS-writes behind — no shared non-agent surface changed ownership or state today (`CHECKS_HISTORY.tsv` and `STATE_VOCABULARY_PROVENANCE.md` are DAEDALUS-owned cold halves, not shared surfaces) — said here, not silenced.

