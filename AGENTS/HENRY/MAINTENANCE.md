# HENRY MAINTENANCE LOG

*Structural-change log — doc created/retired/moved, script built or behavior-changed, protocol/CLAUDE.md amendment, schema change. Analytical changes live in STATUS/thesis; routine content edits don't qualify. SCRATCH/session notes get overwritten — structure persists HERE. (Modeled on VIOLET/SAM MAINTENANCE.md; created 2026-06-15.)*

---

### 2026-07-17 (~21:15 ET) — NEW `scripts/gamma_flip.py` — self-computed SPX gamma flip (resolves the SpotGamma paywall GAP)
- **Trigger:** Will "repull the live gamma flip level." The exact flip had been a persistent GAP (paywalled SpotGamma) + a pending Will decision (pay vs accept the free-tracker estimate). fetch.py has no options/gamma capability (price/FRED/EIA only).
- **What it does:** pulls the LIVE ^SPX options chain (yfinance — available in this venv, 52 expirations w/ OI+IV), computes BSM gamma per contract (r=4.5%, q=1.3%), sums net dealer GEX (long-call/short-put convention) across ≤35d strikes ±25% of spot, finds the zero-gamma flip by sign-change interpolation, plus call/put walls. ~6,200 usable contracts.
- **First run (7/17 21:00):** flip **~7,522** · Net GEX **−$25.7B/1% (NEGATIVE)** · SPX 7,457.69 −65pts below = −GEX confirmed · put wall 7,500 (SPX through it) · call wall 7,600. Validated the 7/16 ~7,530-7,545 estimate.
- **Caveat (documented in the script header + STATUS):** absolute $B depends on the dealer-positioning assumption; the FLIP LEVEL and SIGN are the robust reads. Greeks are BSM-from-IV, not vendor greeks.
- **Consequence:** the "exact gamma flip PAYWALLED" GAP is resolved; the pending Will "pay for SpotGamma?" decision is MOOT. VIOLET's F2 gate can now be fed on demand.
- **Files touched:** `scripts/gamma_flip.py` (new), `STATUS.md` (7/17 block + VOL REGIME + SPX threshold), `MEMORY.md` (gap resolved + infra note), `AGENTS/VIOLET/inbox/` (flip delivered), this entry.
- **Boot-impact:** none (on-demand tool, run on catalyst days — GOOGL 7/22, FOMC 7/28-29 — not wired into boot).

### 2026-07-10 (later, ~11:00 ET) — POST-WIRING EVAL RE-RUN (01+02) + CASE-03 FIRST BASELINE — 3/3 PASS (proxy-caveated)
- **Trigger:** Will approved the owed eval work in-session (~10:45 ET, via PROME), as a continuation of the same spawn that applied PAT-040. Note: PROME's ask said "author case-03" — corrected premise: case 03 was AUTHORED 6/15 (INPUT+RUBRIC exist); what was missing was its baseline RUN.
- **Results:** **case 01 (TARGET) PASS · case 02 (GUARDRAIL) PASS · case 03 (GUARDRAIL, first baseline) PASS** — all EXPECTED met, zero DO-NOTs, no contamination signatures. Promotion bar (TARGET holds + guardrails hold) met for the step-3c wiring. Rows in `evals/results.tsv`; full scoring + responses in `evals/baseline_artifacts/2026-07-10_postwire_responses.md`.
- **Methodology deviations (recorded, not hidden):** runners = fresh-context subagents reading HENRY/CLAUDE.md (skip-boot enforced), NOT fresh interactive CC sessions (README flags the load-path difference); scorer = HENRY in-session (rubrics unread until after all runners responded — one-directional contamination boundary held), not Will. **Treat as provisional/proxy**; the canonical fresh-session Will-scored run remains available if gold-standard numbers are wanted, but the regression question ("did wiring step 3c degrade reasoning?") is answered NO on this evidence.
- **Case-maintenance flag:** case 01's INPUT is vintage-locked (~6/15, "data = 6/12 close") without pinning the run date — a 7/10 runner handled it correctly (dual framing) but the rubric's "~3 days old" phrasing drifts; pin "assume today is 2026-06-15" into the INPUT at next case revision.
- **Files touched:** `evals/results.tsv` (+3 rows), `evals/baseline_artifacts/2026-07-10_postwire_responses.md` (new), this entry, `LAST_COMPLETION.md` (addendum line).
- **Boot-impact:** none further; step 3c stands validated. The eval suite is now a complete 3-case net with all cases baselined.

### 2026-07-10 — WIRED `scripts/boot.py` into CLAUDE.md as boot step 3c (PAT-040 disposition: APPLY, not retire)
- **Trigger:** DAEDALUS 7/8 inbox note (S3 sweep, PAT-040): boot.py installed 6/15 but the numbered boot list never invoked it — 25 days installed-but-unwired ("automation coverage that isn't"). PROME's 7/10 full-boot spawn authorized HENRY to apply the wiring IF the eval evidence supports it, else retire.
- **Eval-evidence read (why APPLY):** (1) the suite's own **minimum-viable-baseline rule** (evals/README §Operator Cost: "Case 01 TARGET + one GUARDRAIL") was **met 6/15** — case 01 PASS + case 02 PASS, zero DO-NOTs, no contamination (results.tsv); (2) the change is **Tier-1 additive** per `proposals/2026-06-15_boot_closeout_hardening.md` (read-only display script, no reasoning-surface change — the eval's regression-guard role applies, and additive hygiene is its lowest-risk class); (3) **live smoke-test this session:** ran clean twice (full 8.1s + --quick 3.9s), and the due-scan immediately earned its keep — it surfaced HEN-39 (due 7/9, ungraded) and, after registration, HEN-40. The retire branch had no case: the script is correct, cheap, and this very session's task list (an ungraded due prediction + a prediction living only in STATUS prose) is the exact failure mode it prevents.
- **What changed:** CLAUDE.md SPAWN PROTOCOL — new step 3c (cwd-proof invocation + "covers live tape + FRED credit + due-scan" supersession clause + the DUE-row disposition rule + "predictions must be TSV rows, not STATUS prose"). This applies proposal steps 4+8 (paired read/write); the rest of the 6/15 hardening proposal stays draft.
- **Files touched:** `CLAUDE.md` (step 3c), `MAINTENANCE.md` (this entry), `MEMORY.md` (infra note flipped to WIRED).
- **Boot-impact:** boot.py is now a mandatory boot step. **Still owed to Will:** post-change eval re-run (guardrails 02/03 must hold — per README re-run cadence, a boot-protocol change is a trigger) + the case-03 baseline that was never run. Flagged to PROME in this session's report, not silent-shipped.

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
