# HENRY MAINTENANCE LOG

*Structural-change log — doc created/retired/moved, script built or behavior-changed, protocol/CLAUDE.md amendment, schema change. Analytical changes live in STATUS/thesis; routine content edits don't qualify. SCRATCH/session notes get overwritten — structure persists HERE. (Modeled on VIOLET/SAM MAINTENANCE.md; created 2026-06-15.)*

---

### 2026-06-15 — RETIRED `scripts/refresh_status.py`
- **Trigger:** Boot-audit + Will/ORC/Prome convergent review flagged it as a stale-data writer.
- **What changed:** Moved `scripts/refresh_status.py` → `archive/retired/refresh_status.py`.
- **Why (do NOT resurrect):** It read a STATIC `MARKET_DATA.tsv` row (not a live pull) and **authored the Signal-Status line with a hardcoded narrative** ("COMPLACENCY TRAP / CPI 3.3% locks Fed"). Running it would silently overwrite STATUS's live header with stale, wrong framing — the exact "stale presented as live" trap HENRY's state-claim convention exists to prevent.
- **Files touched:** `archive/retired/refresh_status.py` (moved), `scripts/boot.py` (comment), `BOOT_AUDIT.md` (lines 23/42).
- **Boot-impact:** None — `boot.py` calls `fetch.py` directly for the live tape; it never imported refresh_status.
- **Spec for any FUTURE refresher (if one is ever built):** must be (1) **live-sourced** (fetch.py/FRED, never a static TSV); (2) update **mechanical table rows only**, NEVER author the Signal Status / thesis narrative; (3) default to **dry-run / diff**; (4) ship with a **test fixture**. Absent all four, don't build it.

### 2026-06-15 — BUILT `scripts/boot.py` v1
- **Trigger:** Boot-parity upgrade (HENRY was the only macro-cluster agent without a boot kit).
- **What changed:** New read-only boot orchestrator — (a) live tape via fetch.py real-time quotes, (b) FRED credit via credit_monitor.py, (c) predictions-due scan of PREDICTIONS.tsv (OPEN/ACTIVE, resolve-date ≤ today). `--verbose / --quick / --selftest`.
- **Boot-impact:** Optional convenience now; becomes a boot step only via the deferred CLAUDE.md change (eval-gated). Read-only by design — does NOT write STATUS.
- **Validation:** `--selftest` PASS (due-scan surfaces an ACTIVE past-deadline row, ignores closed); dry-run tape+credit matched manual pull.

### 2026-06-15 — STOOD UP `NEXUS_BRIEF.md`
- **Trigger:** BRIEFS_MAP had HENRY as ❌ MISSING Priority-#2 ("3 of 4 briefs waiting on HENRY").
- **What changed:** New `NEXUS_BRIEF.md` from the NEXUS template (schema R3 + amendment 7). NEXUS already reads HENRY's brief at its boot step 6 (HENRY pre-registered) — self-serve, no NEXUS registration needed.
- **Boot-impact:** Makes HENRY visible to the cross-agent synthesis layer NOW. The reciprocal wiring (HENRY *reads* peer briefs at boot + maintains its own at closeout) is a CLAUDE.md change = **DEFERRED** (eval-triggering; needs a minimal eval suite as a net first).

### 2026-06-15 — BUILT `evals/` suite v1 (the missing net)
- **Trigger:** No eval suite as a regression net for the deferred CLAUDE.md boot/closeout change. ORC green-light + 4 refinements.
- **What changed:** New `evals/` — README + results.tsv + 3 cases (INPUT/RUBRIC split, scorer-only rubrics): **01 sibling-staleness (TARGET)**, **02 catalyst-vs-pricing (GUARDRAIL)**, **03 KRE rate-vs-credit (GUARDRAIL)**. Modeled on `AGENTS/SAM/evals/`.
- **Refinements encoded (ORC):** (1) skip-boot eval can't test a boot STEP — only the judgment PRINCIPLE if it's in the always-loaded surface; eval = regression guard, proof-of-fix = a separate boot smoke-test. (2) target-vs-guardrail roles (promotion bar = target improves AND guardrails hold, not flat no-regression). (3) KRE replaced the 0DTE/GEX case (don't eval a known-weak surface). (4) staleness INPUT written to genuinely tempt the error.
- **Supporting:** promoted `finding_anchor_prediction_to_surprise_not_priced` to auto-memory so case-02's guardrail principle is in the loaded surface.
- **Boot-impact:** none (evals don't auto-load).
- **⏱️ GATE:** the build is done; the **baseline run is Will's (~10 min/case, fresh skip-boot session, can't be delegated)**. Suite is shelf-ware until baselined — and the CLAUDE.md boot-wiring stays blocked until then (fine; it's deferred).

### DEFERRED (post-FOMC, eval-gated) — boot/closeout protocol wiring  ·  ⏱️ UPDATE 6/23: FOMC PASSED (6/17); now UNBLOCKED (still unapplied) — see the 2026-06-23 entry below
- Tiered per ORC: (1) **additive** NEXUS read-at-boot / write-at-closeout first (light review — closes the VIOLET-stale miss); (2) behavior-changing logic (live-event EXECUTE-override, staleness overlay into protocol, LAST_COMPLETION-vs-SCRATCH reconcile, catalyst docket) only AFTER a minimal HENRY eval suite exists.
- Any CLAUDE.md boot/closeout step addition = eval re-baseline trigger; flag to Will/PROME, never silent-ship.
- **✅ DESIGN COMPLETE (6/15):** full ready-to-apply spec — proposed SPAWN PROTOCOL replacement (16 steps, T1/T2 tagged, before/after, gap→step mapping, acceptance tests + boot smoke-test) in `proposals/2026-06-15_boot_closeout_hardening.md`. Will chose draft-only; **application gated on the `evals/` baseline run.** Apply Phase 2 (T1 additive) → re-eval → Phase 3 (T2 behavior-changing) → re-eval + smoke-test.

### 2026-06-23 — POST-FOMC CATCH-UP + WORKBOOK STALENESS REFRESH (Will-directed)
- **Trigger:** 8-day post-FOMC boot found STATUS frozen pre-FOMC (6/15); an 8-agent staleness audit found the workbook/domain layer frozen Mar–early-June. Will directed a load-bearing refresh, then the full deferred cleanup.
- **What changed (structural):** (1) `board_log.tsv` **CREATED** (v0.2 WALTER signal-intake log; boot step 3a appends here). (2) `board_log.tsv` + `NEXUS_BRIEF.md` + `MAINTENANCE.md` + `scripts/` + `evals/` + `KB_ARCHIVE.tsv` **added to the CLAUDE.md FILES table** (were missing). (3) Workbook/domain refreshed to the post-FOMC 3-axis regime: VX.tsv (LIVE block + de-RED war relics + **gamma/GEX refresh**), FLOW.tsv (cascade Status→dormant; **gamma loop DORMANT→LIVE** on the sourced flip), MARKET_DATA.tsv (6/23 row), ECON_CALENDAR.md (July docket + FOMC fix), `THESIS_VALIDATION.md` (**3-axis reframe** — retired the falsified SPX>7,100 kill leg), KB.tsv (6 catch-up rows ML-HEN-137..142 + 3 superseded-row flags). (4) **Gamma/GEX levels REFRESHED** from free trackers (gamma flip 6,902→~7,448; Net GEX→negative); CTA absolute levels kept retired-stale (paywalled, NOT fabricated). Research: `research/2026-06-23_cta_gamma_levels_sourcing.md`.
- **Gate update:** the DEFERRED block above — FOMC 6/17 has PASSED; evals 01/02 baselined 6/15 (2/3 PASS, case 03 pending). The CLAUDE.md boot/closeout wiring is **UNBLOCKED but UNAPPLIED** — flag to Will/PROME before applying (eval re-baseline trigger; never silent-ship).
- **Boot-impact:** board_log.tsv is now a live boot-step-3a artifact; gamma/GEX rows now carry sourced values (conf ~0.75). Everything else = content refresh.
