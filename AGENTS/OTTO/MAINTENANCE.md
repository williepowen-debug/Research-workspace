# OTTO Maintenance Log

Reverse-chronological log of **structural** changes to OTTO's docs, folders, scripts, and
SPAWN/closeout protocol. Each entry: **Trigger / What changed / Files touched / Boot-impact /
Lessons**. Answers *"why is OTTO organized this way?"*

**Distinct from:**
- `CHANGELOG.md` — **analytical** changes (thesis/POV pivots, conviction shifts, prediction moves).
- `STALE_PUNCHLIST.md` — **forward** to-do (what's stale, needs fixing).

This log is the **structural** record (what infra/protocol changed and why). The CLAUDE.md version
stamp is the one-line index; the full entry lives here. Log material structural changes only — not
routine content edits. Archive to `archive/` if it grows past ~300 lines (SAM cautionary tale: 635).

---

## 2026-08-14 (session 018) — Unobservable catalyst rows re-keyed to observable outputs; STATUS archive #5

**Trigger:** three catalyst rows fired between boots (2026-08-05 Rule 17 subpoena deadline, 2026-08-07 defense privilege log, plus the 8/14 and 8/21 steps of the same chain) and **all of them swept EMPTY** — not because nothing happened, but because **every one was keyed to a party-to-party discovery obligation that structurally cannot produce a docket entry.** Rule 17 applications are routinely ex parte or sealed and service needs no docket entry; privilege logs are exchanged between parties and are never filed. `[CONF CourtListener docket_id 72046761 — zero entries 2026-08-01..08-14]`

**What changed:**
1. **`docket/CATALYSTS.tsv` — the whole 8/7→9/4 privilege chain collapsed into ONE row** at a modeled **2026-09-04**, keyed to *"first DOCKETED output"* (in camera submission, motion to compel, privilege dispute, or an order resolving one) rather than to the private exchanges. The 8/5 Rule 17 row is annotated **unobservable-by-construction** and explicitly **not re-armed on a date**.
2. **Two new rows added:** `2026-08-07` (First Brands trial **Day 4** — closing arguments, matter under advisement; the day OTTO did not know existed) and `2026-09-15` (**First Brands confirmation ruling**, `modeled`, poll-every-session — the row that decides OTTO-32).
3. **`2026-08-06` NY Fed row re-dated to `2026-08-11`** and pinned to the actual publication.
4. **`2026-07-28` trial row corrected** — the trial was four days, not three.
5. **`workbook/STATUS_archive_20260814.md` created** (5th STATUS archive): s017 boot-pointer + the s017 Carvana post-print vector, both with supersession banners naming exactly what in them went stale and what still stands. STATUS **283 → 258 lines**.

**Files touched:** `docket/CATALYSTS.tsv`, `STATUS.md`, `workbook/STATUS_archive_20260814.md`, `docket/WINTERKORN_MEMORY.md` (PENDING item).

**Boot-impact:** boot step 5 stops re-flagging three rows that can never be graded. **This is the point:** a catalyst that cannot be observed through OTTO's only channel is an alert-fatigue generator, and repeated "unswept" flags on it train the operator to skim the section where a real miss would appear.

**Lessons:** **Fifth member of OTTO's measure-design failure family** (OTTO-30's instrument, OTTO-04's metric, OTTO-07's default-zero ledger, s017's panel positive control) — and the **second built AFTER naming the pattern**. The recurring test being failed is `[[finding_executability_is_a_separate_audit_axis]]`: *can this rule be graded with the instruments I actually have, inside the window it quotes?* Ask it **when the row is written**, not when it fires empty. Corollary recorded on the rows themselves: **absence of a docket entry is not evidence of absence** when the underlying obligation never produces one.

---

## 2026-07-25 (session 016, Will-directed) — 10-D performance panel built; Fitch dependency retired

**Trigger:** Fitch's index reached OTTO only through a trade-press mirror that decayed to March-2026 data. Free alternatives were tested the same day and are closed — **S&P's tracker returns HTTP 403; KBRA's full indices spreadsheet requires an ABS Premium subscription** (KBRA's free preview gives tier-separated MoM deltas at a ~2.5-week lag, useful but no levels). Will directed building the panel.

**What changed:** new `scripts/panel_10d.py` + `workbook/PANEL_10D.tsv`. A **fixed panel of 7 named deals** across two tiers — DEEP (EART 2022-2/2022-3/2023-1/2024-1) and BROAD (SDART 2022-6/2023-1/2024-1) — parsed from SEC 10-D Exhibit 99.1. Emits **60+ DQ, CNL, annualized net loss, recovery rate, extension rate** per deal per filing. Supersedes the Fitch dependency and the frozen `EXTENSION_PROXY.tsv` stub.

**Explicitly NOT an index.** A basket whose composition drifts month to month moves for compositional reasons — the exact bias that broke OTTO-04. Deals are fixed and named, seasoning is recorded, tiers never blend. Panel *levels* are also **not comparable to Fitch levels** (different universe and definitions) and must never be spliced onto that series.

**Four defects caught during the build — every one would have shipped plausible-but-wrong numbers:**
1. **Footnote markers contain digits.** `{93}` sits between label and value; a gap written `[^\d]{0,30}` stops at the brace and matches the wrong field. **Produced an ANL of 111,600%** — caught only because it was absurd. A subtler mismatch would have passed.
2. **Nested capture groups.** `m.group(m.lastindex)` returned the wrong group; replaced with a single named group.
3. **`_source.ciks[0]` is the DEPOSITOR, not the trust.** All Santander trusts share CIK 1383094, so every SDART deal resolved to the *same* filing list and returned **identical metrics for three different vintages**. The per-trust CIK must be parsed out of the matching `display_name`. **This one looked exactly like valid data** — the only tell was that three vintages had identical numbers.
4. **ANL denominator inconsistency.** Exeter states a beginning-of-period balance; Santander states only initial pool + pool factor. Using the initial pool understated seasoned-deal ANL by the amortisation factor (~6×). Now reconstructed as `initial × pool factor`.

**Fail-loud contract (inherited from `shelf_halt_monitor.py`):** every row run-stamped; unparsed fields written EMPTY with the miss named, never 0; positive control (EART 2022-3 CNL must equal 27.58%) gates the whole run; unsupported issuers reported UNSUPPORTED; network/parse errors raise. **New in this tool: a DUPLICATE-METRIC DETECTOR** — if two different deals return identical values, the run is marked INVALID. That is a permanent net for defect 3, kept precisely because that failure mode is indistinguishable from real data by eye.

**Validation:** SDART 2022-6 parsed to **CNL 12.08%** and EART 2022-2 to **26.34%** — both independently reproducing the s015 hand-pull.

**Boot-impact:** none — monthly/on-demand, ~28 EDGAR fetches per 4-filing run. Not wired into `boot.py`.

**Lessons:**
- **The missing instrument was one parser away, inside documents OTTO was already reading** for OTTO-04. Before accepting a data wall, check whether the primary documents in hand already contain the field.
- **Three of the four defects produced plausible output.** Only the 111,600% ANL announced itself. Absurdity is a lucky detector; controls and cross-deal duplicate checks are the reliable ones.
- **Building the instrument produced the finding.** The panel's first real run resolved the summer-re-deterioration watch OTTO had carried unanswered all session (→ CHANGELOG).

---

## 2026-07-25 (session 016, follow-on) — OTTO-07 re-instrumented: `shelf_halt_monitor.py` replaces a default-zero stub

**Trigger:** freezing the stale ledgers surfaced `workbook/ABS_ISSUANCE.tsv` as not merely stale but **inverted** — `0 deals / shelf_halts 0` during a period STATUS documents as robust issuance. Its feeder (`abs_issuance_tracker.py`) was a manual-check stub emitting zeros when unrun, and that ledger was **OTTO-07's nominal instrument**. DAEDALUS graded the class PAT-060 and endorsed rebuilding warm rather than deferring to a Dec-31 backlog line (OTTO is Tier-2; next spawn may be weeks out).

**What changed:** new `scripts/shelf_halt_monitor.py` + `workbook/SHELF_ACTIVITY.tsv`. Probes whether each tracked subprime shelf filed a current-year vintage on EDGAR full-text search. `ABS_ISSUANCE.tsv` + `abs_issuance_tracker.py` remain FROZEN as the cautionary record.

**Design — fail-loud, per DAEDALUS's spec requirement:**
- Every row carries a **run stamp** (timestamp + probe year + per-issuer vintages). A zero is only meaningful attached to a run that provably executed. **No code path writes a bare 0 without one** — if the script never runs, the ledger gains no rows, so "nobody looked" stays visibly distinct from "nothing happened."
- **Per-issuer positive control:** each shelf must show a prior-year vintage before a current-year zero is believed. A stem that resolves in neither year is `INVALID` (config error), **never** "quiet."
- Three statuses: `OK` / `INVALID` (control failed — counts meaningless) / `ERROR` (run failed — no counts written). Network failures **raise**; they never degrade to False.

**Four defects the build itself caught — each one a false-quiet the old design would have shipped:**
1. `forms=FWP,424B5,...` returned 0 for every ABS entity → the global positive control failed and the run self-marked `INVALID` rather than reporting a market-wide halt. **The fail-loud path worked on its first execution.**
2. Relevance-ranked sampling manufactured a false zero for CPS → replaced with deterministic per-vintage existence probes.
3. EDGAR rate-limiting produced errors on CPS/Flagship → reported as `ERR`, explicitly *not counted as quiet*; added pacing (0.15s) + 3× backoff retry.
4. **Shelves use two vintage conventions** — numeric (Exeter 2026-3) and letter (CPS 2026-A). Probing one manufactured a false `INVALID`. Now detects convention once per shelf against the control year.

**Result — first valid run (2026-07-25T13:36:42): NO HALT, 8/8 validated shelves issuing in 2026.** OTTO-07 **55% → 15%**. And a near-miss worth preserving: Flagship Credit Auto Trust showed a textbook halt shape (4 deals 2022 → 3 → 2 → **zero** in 2025 and 2026), but verification found Flagship Credit Acceptance was **acquired by InterVest in Nov 2025** and rebranded — corporate action, not a funding halt. **The instrument surfaced the candidate; the verify-before-resolving rule rejected it.** Flagship retired from the probe set with that rationale inline.

**Boot-impact:** none (not wired into `boot.py` — it is a monthly/on-demand check, ~90s of paced EDGAR calls; wiring it into boot would add latency to every session for a slow-moving signal).

**Lessons:**
- **The instrument found its own defects only because it was built to fail loud.** Four separate false-quiet conditions surfaced during one build; a silent-zero design would have reported "no halt" for all four and been believed.
- **Ask of every falsifier: what does the feed read when nobody runs it?** If that equals the on-track reading, the falsifier is theater (DAEDALUS PAT-060).
- **A halt-shaped gap is not a halt.** The single most halt-like signal in the data was a corporate action. Build the verification step into the instrument's own output, not into the analyst's memory.

---

## 2026-07-25 (session 016) — Boot past-due-catch was silently priority-filtering fired catalysts; look-back window now auto-sizes

**Trigger:** Boot on 2026-07-25 after a 21-day dark period reported **one** recently-fired catalyst. Running `catalyst_countdown.py` directly showed **four**. A fifth (Jul 14 Q2 banks, an OTTO-30 input) had already aged out of the window entirely. Two independent defects in the same safety net.

**What changed:**
1. **`scripts/boot.py` — section-sticky rendering for RECENTLY FIRED.** The non-verbose path filtered sub-script output by keyword (`🔴 🟠 ⚠️ OVERDUE …`). Fired rows carrying a **🟡** priority matched nothing and were dropped — including the **First Brands creditor-vote deadline**, a direct dependency of the OTTO-32 resolver. Now: once the RECENTLY FIRED header is seen, every date-bearing row prints regardless of glyph, until the next section header. Added `DATE_ROW` regex + `re` import.
2. **`scripts/catalyst_countdown.py` — `PAST_RETENTION` 10 days (fixed) → adaptive.** New `past_retention_days()` sizes the look-back from `STATUS.md`'s mtime (= last closeout) + 3 days grace, floored at 10 and capped at 120. OTTO is Tier-2/spawn-gated and routinely goes dark longer than 10 days; a fixed window ages unswept catalysts out before they are ever seen. Header now reads "last N days = since last closeout".

**Files touched:** `scripts/boot.py`, `scripts/catalyst_countdown.py`.

**Boot-impact:** verified same-session — window auto-widened to **23 days** and all **5** fired rows surfaced, including the three 🟡 rows and the Jul 14 row that had aged out. No change to the imminent/upcoming sections.

**Lessons:**
- **A filter added for readability silently became a filter on correctness.** The keyword list was written for the *forward* sections, where priority glyphs are always present, then applied to the *past-due* section, where they gate whether a fired catalyst is ever swept. The past-due-catch is a safety net; nothing in it should be conditional on severity.
- **Asymmetric costs deserve asymmetric defaults.** Re-showing an already-swept row costs one line of noise. Hiding an unswept one costs a catalyst. The retention window is now deliberately generous and documented as such in the docstring.
- **A fixed constant encoded an assumption about cadence that this agent does not satisfy.** Deriving it from `STATUS.md` mtime makes it self-correcting: the longer OTTO is dark, the further back it looks.
- This is the same failure class WINTERKORN exists to prevent (the Jun-17 → Jun-12 date-keeping miss), re-introduced one layer up in the wrapper. Sub-agent coverage does not protect against the orchestrator dropping its output.

**Also this session (doc-truth, non-structural but logged for the audit trail):** `thesis/CHANGELOG.md` preamble corrected — it still asserted that `thesis/THESIS.md` did not exist and that there was no MAINTENANCE log, both untrue since Jun 9. STATUS § PREDICTIONS header re-pointed from the dead `PREDICTIONS.tsv` to `thesis/PREDICTIONS.tsv` (PROME boot-gate flag; the *other* `workbook/PREDICTIONS.tsv` mention is correct as Jun-9 history and was deliberately left alone).

---

## 2026-07-04 (session 015) — ML.tsv CRLF-merge corruption repaired + EDGAR-via-UA method established

**Trigger:** LAST_COMPLETION-flagged GAP — `workbook/ML.tsv` carried pre-existing CRLF-merge corruption (append-only ledger, not boot-read, so it rotted unfixed across sessions). Repaired as a P2 hygiene item.

**What changed:**
- **ML.tsv repaired** — 3 overlaid defects fixed programmatically with *validate-before-write*: (a) 11 rows carried a spurious leading integer column (`cat -n`-style line numbers prepended); (b) ML-OTTO-171 was a CRLF-merge of a truncated draft + the complete row — collapsed to the complete copy via `rfind` (no retyping); (c) a stray blank line. Normalized all rows to **CRLF** (matches OTTO/fleet TSV convention — FLOW/VX_HISTORY/CATALYSTS all CRLF; `.gitattributes` absent). Result: **182 contiguous rows (001-182), every row exactly 8 fields**, IDs unique+monotonic — validated before the write executed.
- **EDGAR primary-source access method established** — SEC `data.sec.gov` / `/Archives/` 403 via WebFetch (can't set a UA); works via `curl`/`urllib` with a compliant `User-Agent` header (auto-memory `[[finding_edgar_403_user_agent_header]]`). Now the OTTO path for 10-D / servicer-report pulls — used this session for the 2022-vintage CNL bifurcation.

**Files touched:** `workbook/ML.tsv` (repair + ML-182/-183 appends), `STATUS.md` (dashboard rows), `thesis/PREDICTIONS.tsv` (OTTO-04).

**Boot-impact:** none (ML.tsv is append-only, not boot-read) — but the ledger is now clean-parseable TSV for any future script.

**Lessons:** validate-before-write (tab-count + ID contiguity) is the safety net for programmatic ledger repair; append in **binary CRLF** to avoid the text-mode line-ending flip (`[[finding_crlf_textmode_tsv_flip]]`); match the file's existing ending convention rather than imposing LF.

## 2026-07-04 — Closeout-maturity parity pass (Will-directed vs DAEDALUS exemplars)

**Trigger:** Will asked to check OTTO's closeout condition/maturity vs more-developed agents. Compared against DAEDALUS `MATURITY_MAP.md` + `FLEET_MAP.tsv` + a step-by-step closeout extraction of REGINALD (L4)/LABOR/BROCK/CARL/SHADE/BRENT. Finding: OTTO's closeout **machinery is at/above parity** (only fleet agent with BOTH MAINTENANCE+CHANGELOG; full `boot.py`; WINTERKORN sub-agent = BRENT's FASTOW) — but OTTO sits at **mechanical L2, "Needs read"** while its structural twin BRENT read-verified L2→L4. Closed the three cheap conformance gaps.

**What changed:**
- **STATUS.md — added labeled `## BOTTOM LINE`** (DAEDALUS's #1 fleet conformance flag; was missing). Trailing synthesis: fraud-leg critical / systemic-funding-leg disconfirmed / next resolver Jul 28.
- **`boot.py` — workbook staleness alert wired** (was `--trade`-only). Now runs `ledger_staleness.py OTTO --quiet` (workbook TSVs) + `--trade` under a "Workbook/Trade Staleness" step loop. Parity with REGINALD/BROCK/CARL/BRENT.
- **Froze `workbook/VX.tsv` + `workbook/FLOW.tsv`** (FROZEN banners; no script parses either; VX→STATUS canonical, FLOW→thesis/THESIS.md canonical). Dropped the boot staleness alert from 5→3 stale ledgers.
- **CLAUDE.md — new closeout step 7b: canonical↔mirror consistency check** (CATALYSTS↔TIMELINE, PREDICTIONS↔STATUS-block, THESIS↔mirror). CARL step-15 parity; encodes auto-memory `[[finding_doc_mirror_consistency_check]]` as a protocol step.
- **DAEDALUS read requested** — `AGENTS/DAEDALUS/inbox/2026-07-04_from-OTTO_maturity-read-request.md` (judgment read + re-rate; flags the conv-matrix equivalent-titling question).

**Files touched:** `STATUS.md`, `scripts/boot.py`, `workbook/VX.tsv` + `workbook/FLOW.tsv` (freeze banners), `CLAUDE.md` (step 7b), `MAINTENANCE.md` (this), + DAEDALUS inbox drop (untracked).

**Boot-impact:** boot now surfaces workbook-ledger staleness every run (currently 3 stale: CROSS_AGENT_LOG/EXTENSION_PROXY/KB — a tracked freeze-or-refresh backlog). Closeout gains an explicit pre-commit mirror-consistency gate.

**Lessons:** OTTO's *machinery* was already exemplar-tier; the gap was **conformance handles + a missing judgment read**, not substance — the same pattern DAEDALUS found on BRENT (L2→L4 under-rate). Wire the staleness alert AND freeze the proven-dead ledgers together, else the alert is noise. Remaining backlog: freeze-or-refresh CROSS_AGENT_LOG / EXTENSION_PROXY / KB with per-ledger judgment.

## 2026-07-04 — TRADE.md frozen + `--trade` staleness boot-line (PROME PAT-035)

**Trigger:** PROME task-packet (Jul 4, MEDIUM) routing DAEDALUS's fleet TRADE-staleness sweep (PAT-035). DAEDALUS extended `scripts/ledger_staleness.py` to cover trade/position surfaces; the `--trade` scan flagged `OTTO/TRADE.md` at +138d stale with no banner — a Data Hygiene two-state-rule violation. Routed owner-decides rather than frozen unilaterally.

**What changed:**
- **`TRADE.md` FROZEN** (banner in header, within the first-6-lines window `is_frozen()` reads). Chose freeze over refresh: OTTO holds no active OTTO-originated position; all ideas are Feb-vintage and stale-or-disconfirmed (pre-split CVNA strikes, dead GT trigger, ABS-spread short falsified this session, ALLY thesis undercut). Live auto read stays in STATUS.
- **`scripts/boot.py` — new "Trade Staleness" step.** Added `STALENESS` path constant (repo-root `scripts/ledger_staleness.py`) + a read-only step running `ledger_staleness.py OTTO --trade --quiet` after the catalyst countdown. Read-only alert, never gates the boot. Mirrors the fleet's cwd-proof lazy-sweep pattern.

**Files touched:** `TRADE.md` (freeze banner), `scripts/boot.py` (STALENESS const + step), `workbook/ML.tsv` (ML-180/-181 = the 2 WALTER signals processed same spawn), `STATUS.md` (boot-pointer inbox note), `MAINTENANCE.md` (this).

**Boot-impact:** Every boot now surfaces trade-surface staleness alongside predictions/catalysts (frozen → silent OK). Closes the silent-rot path that let TRADE.md drift 138 days.

**Lessons:** Freeze is the honest state for a Tier-2 spawn-on-need agent with no live position — a "maintained-current" TRADE.md would just repeat "nothing actionable," which STATUS already says. The staleness enforcer respects the FROZEN banner (STATIC_BANNER_MARKERS, first 6 lines) — verify the freeze is recognized (re-run the script) before wiring the boot-line, so the new step doesn't nag about a file you just froze.

## 2026-06-09 (PM) — WINTERKORN docket-steward sub-agent (v2.6 → v2.7)

**Trigger:** Same-session follow-on to thesis/ consolidation (v2.6). Will-directed TIER-1 audit identified the docket-keeper sub-agent as the highest-leverage next move — the Jun-8 First Brands `Jun 17 → Jun 12` catch was precisely the failure mode FASTOW's `[[finding_subagent_pre_fire_date_verification]]` was built to prevent. Planned-before-built: spec sub-agent identity, scope, autonomy gradient, recurring-release universe, spawn cadence, 7 open scope questions answered by Will before any file written.

**What changed:**
- **New `docket/WINTERKORN.md` (spec, ~250 lines).** FASTOW-pattern scoped owner. Mandate: maintain `docket/CATALYSTS.tsv` + verify forward dates against bankruptcy dockets, SEC EDGAR, rating-agency calendars, ABS pricing windows. Busy-work only — no analytical judgment. Owns write to CATALYSTS.tsv + WINTERKORN_MEMORY.md only; never touches STATUS / THESIS / CHANGELOG / PREDICTIONS / workbook / scripts. Pre-fire date verification within 7d window is the load-bearing job step (Jun-17→Jun-12 catch made cadence). Monthly baseline audit + post-miss audit with decline-memory (CALIBRATION is OTTO-owned; WINTERKORN reads but never writes).
- **New `docket/WINTERKORN_MEMORY.md` (state, ~120 lines, seeded blank).** Inaugural — no LAST RUN history. STANDING MONITORS seeded with per-case watches (First Brands highest activity; Tricolor Ch.7 cert-blocked source pattern; SDNY criminal selective; Carvana derivative) + recurring releases (Fitch ABS Index monthly, NY Fed HDC quarterly, S&P/KBRA/Moody's surveillance) + bank-earnings cycle (named-banks subset) + ABS pricing windows (modeled). NEXT RUN HINTS includes bootstrap-specific guidance for the imminent Jun 12 First Brands UST hearing.
- **CLAUDE.md Doc Ownership** — added 2 new rows for WINTERKORN.md + WINTERKORN_MEMORY.md; refactored `docket/CATALYSTS.tsv` row to flag WINTERKORN as maintainer (OTTO doesn't normally edit during session — applies WINTERKORN escalations).
- **CLAUDE.md Coordination** — new `### 2026-08-03 (s017) — panel_10d.py positive control rebuilt; it was guaranteed to fail on new data

**Trigger.** The scheduled monthly panel re-run pulled Exeter's newly-filed 07-30 10-Ds and reported
`POSITIVE CONTROL … **FAIL** → every value in this run is untrustworthy; run marked INVALID`,
condemning **9 rows that were all correct**.

**Diagnosis — the control was broken by construction, not by a bug.** v1 was
`CONTROL = ("EART 2022-3", "cnl_pct", 27.58, "10-D filed 2026-06-30")`, evaluated against
**whatever value the latest filing returned**. That pins a pass/fail gate to a **moving quantity**:
the moment a new 10-D lands — *the exact event the instrument exists to detect* — the control must
fail. A control that fails on correct new data is worse than no control, because it trains the
operator to override it, and the next override will be the one that mattered.

**What changed.** `CONTROL` is now a dict carrying a **frozen archived exhibit URL**, and a new
`run_control()` re-fetches and re-parses **that one fixed document** every run. The control now
tests the **parser** (which must not drift) and never the **world** (which must). Control evaluation
moved out of the per-deal loop into the summary block.

**Files touched.** `scripts/panel_10d.py` (CONTROL constant + `run_control()`; removed the in-loop
comparison), `workbook/PANEL_10D.tsv` (the 9 falsely-INVALID rows from this session's 09:56 batch
were removed and replaced by the clean 09:58 run — same-session output, not history).

**Boot-impact.** None on boot.py. The panel is a manual monthly run; it now exits clean when new
filings arrive instead of demanding a human override.

**Lessons.** (1) This is the **fourth** member of OTTO's measure-design failure family — after
OTTO-30's press-sampling instrument, OTTO-04's blended-index metric, and OTTO-07's default-zero
ledger — and **the first found inside a tool OTTO built *after* naming the pattern.** Naming a
failure mode does not immunise you against it; the check is to ask of every new gate *"what does
this do on the day the thing I am watching for actually happens?"* (2) Generalises to auto-memory
`finding_threshold_level_is_a_measurement_not_a_constant`: a validation gate is a threshold, and
thresholds pinned to moving quantities decay. (3) The failure direction was **loud** (marked good
data invalid) rather than silent, which is the only reason it was caught in one run — cf.
`finding_test_the_guard_not_just_the_guarded`.

---

### Sub-Agents` subsection codifying the sub-agent pattern + WINTERKORN row (pattern / owns / cadence) + spawn protocol pointer. References `[[finding_subagent_naming_identity_over_functional]]` for future sub-agent naming convention.
- **CLAUDE.md File Structure tree** — docket/ subtree expanded from 1 entry to 3 (CATALYSTS.tsv + WINTERKORN.md + WINTERKORN_MEMORY.md).

**Will-decided scope decisions (locked in spec):**
- **Naming = WINTERKORN.** Auto-domain reference (VW Dieselgate executive-knew-and-didn't-disclose archetype) matching OTTO's cockroach pattern. SAM (METSUKE — Tokugawa inspector) + BRENT (FASTOW — Enron CFO) precedent of identity-named people sub-agents preserved.
- **SDNY criminal track = SELECTIVE.** Trial date + cooperator-witness motions only. Routine motion practice excluded (would inflate TSV without driving OTTO action).
- **Bank earnings = NAMED-BANKS SUBSET ONLY.** JPM/5-3/BCS/Regions/MTB/OBK. REGINALD owns sizing; OTTO tracks disclosure escalation (different signal).
- **Spawn cadence = WEEKLY TUE + ON-DEMAND T-3 PRE-HEARING.** Outside that cadence, spawn cost > value.
- **ABS pricing rows = MODELED.** Issuer cadence projectable; revise within 7d via SEC EDGAR FWP search. Without this, OTTO walks into Jun 30 OTTO-05 resolve cold.
- **STATUS divergence rules = FASTOW PATTERN.** STATUS CRITICAL TIMELINE is a curated load-bearing subset of TSV (all 🔴 + position expiries + tracked-case hearings + OTTO-NN prediction resolves). Rolling monthly recurring releases live in countdown only, not in STATUS.
- **Build order = SPEC FIRST, MEMORY SEEDED BLANK.** Spec is the durable contract; first run populates MEMORY organically.

**Files touched:**
- New: `docket/WINTERKORN.md`, `docket/WINTERKORN_MEMORY.md`
- Edits: `CLAUDE.md` (Doc Ownership table + File Structure tree + new Sub-Agents subsection + version footer), `MAINTENANCE.md` (this entry), `STATUS.md` (boot-pointer refresh)

**Boot-impact:**
- No boot script changes — WINTERKORN spawns on demand via Agent tool, not via `scripts/boot.py`.
- OTTO's `scripts/catalyst_countdown.py` still reads `docket/CATALYSTS.tsv` directly; WINTERKORN edits flow through that pipeline unchanged.
- First WINTERKORN spawn is the validation test. Bootstrap NEXT RUN HINTS in MEMORY flag the Jun 12 First Brands UST hearing as the T-3 pre-hearing canonical first-run trigger.

**Lessons:**
- **Pre-fire date verification is the load-bearing argument for a docket-keeper sub-agent.** Not the "save context" framing — that's secondary. The Jun-17→Jun-12 catch costs OTTO real signal credibility when missed; making the verification cadence-driven (every run, every 7d-window row) is the value.
- **Selective scope on adjacent domains (SDNY criminal, bank earnings) prevents TSV inflation.** Without explicit scope decisions, baseline audits would over-propose. Recording Will's scope decisions in the spec (not just in CALIBRATION) makes them durable across future-WINTERKORN spawns who haven't seen the conversation.
- **FASTOW's decline-memory pattern (CALIBRATION as OTTO-owned, sub-agent reads but never writes) prevents the "audit nags monthly" failure mode.** Critical for a propose-only sub-agent that runs on cadence.
- **Inaugural MEMORY seeding is a real design step, not boilerplate.** A blank-MEMORY first run would have no STANDING MONITORS to anchor against; seeding with current OTTO domain state (per-case watches + known cert-blocked sources + bootstrap T-3 flag) gives the first run productive footing without ambiguity. Otherwise first-run quality is poor.

---

## 2026-06-09 — thesis/ subdir + canonical THESIS.md v1.0 (v2.5 → v2.6)

**Trigger:** Will-directed peer-parity audit (post-v2.5) surfaced thesis content scattered across 7 docs (STATUS § THESIS, CLAUDE.md "Current Thesis", top-level CHANGELOG, workbook/PREDICTIONS, MEMORY § Findings, ML.tsv, research/outputs/) with no canonical home. SAM model (`thesis/THESIS.md` + `thesis/CHANGELOG.md` + `thesis/PREDICTIONS.tsv` + `thesis/PREDICTIONS_ARCHIVE.md`) chosen as target. Planned-before-built: thesis content was articulated explicitly (Primary Cockroach + Secondary Invisible Exit + Carvana sub-thesis carve-out + transmission chain + why-now timing) before the folder was created — moving scattered artifacts into a new folder without nailing what the thesis IS would have just relocated the sprawl.

**What changed:**
- **New `thesis/` subdir** with 4 files:
  - **`thesis/THESIS.md` v1.0** — 12-section canonical thesis: header w/ decomposed conviction (Pattern HIGH / Magnitude HIGH / Near-term timing VARIABLE / Carvana LOWER), one-liner, Primary Cockroach (mechanism + 4-case table + falsification), Secondary Invisible Exit (mechanism + Tricolor industrial validation + falsification), **Carvana sub-thesis carved out** (was bundled at equal weight to 4 confirmed → now separate-conviction layer), transmission chain (7-stage end-to-end with current state), why-now timing claim (2022 vintage / Fed-pause / auditor cycle — defensible against "noise" alternative), expanded risk matrix (prob/impact/mitigation per row, was 4-row sketch in CLAUDE.md), position view (acknowledges TRADE.md stale), predictions w/ failure-pattern synthesis, cross-agent links.
  - **`thesis/CHANGELOG.md`** — moved from top-level (`git mv`); anticipated by header note in v2.5.
  - **`thesis/PREDICTIONS.tsv`** — moved from `workbook/` (`git mv`); 9-col schema unchanged.
  - **`thesis/PREDICTIONS_ARCHIVE.md`** *(NEW)* — 5 resolved-row post-mortems (OTTO-01/08/09/26/27) + calibration scoreboard (5/5 substance, 4/5 substance+window) + failure-pattern rules. Knocks STALE_PUNCHLIST items #4-5 (PREDICTIONS_ARCHIVE + calibration scoreboard preamble).
- **STATUS.md § THESIS block** — replaced 5-row case table + 2 prose paragraphs with **3-line summary + case-status mirror table + pointer to `thesis/THESIS.md`**. STATUS retains live case-status visibility (so dashboard remains self-contained for spawns) but the canonical narrative is single-sourced. Mirror-consistency direction: thesis/ canonical, STATUS mirrors live-state only.
- **CLAUDE.md Current Thesis section** — collapsed two ~4-line case mechanism paragraphs to a one-line bullet pointer. Was a "durable framing" home; canonical thesis now owns that. CLAUDE.md still names the two theses for SPAWN-time keyword orientation, then routes to thesis/THESIS.md.
- **CLAUDE.md Doc Ownership table** — added 2 new rows (`thesis/THESIS.md`, `thesis/PREDICTIONS_ARCHIVE.md`); refactored `STATUS.md` row to specify "live thesis-state *mirror*" not owner; refactored `thesis/CHANGELOG.md` and `thesis/PREDICTIONS.tsv` rows for the move; refactored `CLAUDE.md` self-row to drop "durable thesis framing" claim (now thesis/ owns).
- **CLAUDE.md File Structure tree** — top-level CHANGELOG.md removed; new `thesis/` subtree added; `workbook/` lost PREDICTIONS.tsv row.
- **CLAUDE.md Prediction Convention** — path updated `workbook/` → `thesis/`; added pointer to ARCHIVE for post-mortems; failure-pattern *rules* now home in THESIS.md § Predictions.
- **CLAUDE.md INBOX Processing + Closing Protocol** — path updates for PREDICTIONS.tsv (`workbook/` → `thesis/`).
- **CLAUDE.md Trade Flow** — path update for PREDICTIONS.tsv.
- **Scripts** — `scripts/predictions_due.py` PRED_TSV path updated (`workbook/PREDICTIONS.tsv` → `thesis/PREDICTIONS.tsv`); docstring + `scripts/boot.py` header text updated. **Important silent-pass bug found and fixed**: script silently returned "ran cleanly, no alerts" on file-not-found rather than erroring; first edit on the in-flight file-rename caught this. Now verified to read the new path.
- **STATUS boot-pointer** refreshed to summarize the Jun 9 session.

**Files touched:**
- New: `thesis/THESIS.md`, `thesis/PREDICTIONS_ARCHIVE.md`, `thesis/CHANGELOG.md` (via git-mv), `thesis/PREDICTIONS.tsv` (via git-mv)
- Edits: `CLAUDE.md`, `STATUS.md`, `scripts/predictions_due.py`, `scripts/boot.py`, `MAINTENANCE.md` (this entry)
- Deleted: `CHANGELOG.md` (top-level → moved), `workbook/PREDICTIONS.tsv` (→ moved)

**Boot-impact:**
- Boot step 4 (`predictions_due.py`) now reads `thesis/PREDICTIONS.tsv`. Verified clean: 12 OPEN ledger renders correctly.
- Future boot will hit the new layout naturally — boot step 1 (read STATUS) still works; if a spawn reads CLAUDE.md "Current Thesis" they'll be routed to thesis/THESIS.md within 3 lines.
- One-time call: if a spawn pattern-matches the old top-level CHANGELOG.md path, it should auto-recover via the SAM-style `thesis/CHANGELOG.md` find.

**Lessons:**
- **Plan the substance before the folder.** The structural move is the cheap part (5 min of git-mv + Edit). The hard part is articulating what the thesis IS in the form that the canonical doc needs (12 sections worth of synthesis). Doing the planning pass first surfaced the Carvana carve-out as the most important substantive change — without that, this would have been a relocate-and-rename exercise.
- **Silent-pass bugs hide in path-rename edits.** `predictions_due.py` returned "ran cleanly, no alerts" when the TSV file didn't exist — a wrong path produced false success. Caught only because I re-ran the script after the path edit and noticed it claimed clean against a file that no longer existed at that path. Path-renames should always be followed by an end-to-end verify, not just "edit succeeded."
- **STATUS-as-mirror requires explicit direction encoding.** New ownership rows had to specify "live thesis-state MIRROR" not "live thesis state" to signal the canonical-wins direction. Auto-memory `[[finding_doc_mirror_consistency_check]]` pattern applies: encode the direction, then a closeout/boot check can verify the mirror agrees.
- **OTTO's thesis was meaningfully more mature than its STATUS block suggested.** The 5-row case table in STATUS gave a flat view; the actual thesis — once articulated — has structural depth (4 mechanism features, 2 interlocked theses with explicit explanatory link, 7-stage transmission chain, why-now timing claim, decomposed conviction). The lesson: when an agent has been doing the thinking but storing the conclusions in a flat dashboard, the thesis already exists — it just hasn't been written down.

---

## 2026-06-08 — Peer-parity push: boot automation + closeout maturation + MAINTENANCE.md (v2.1 → v2.5)

**Trigger:** Will-directed comparison to the mature agents (SAM, BRENT) across boot, then closeout, then structural logging. Capped with a domain data-refresh. Multi-part, collaborative — Will chose scope at each fork.

**What changed (by version bump):**
- **v2.2 — Boot automation.** Built `scripts/boot.py` orchestrator (price snapshot + predictions-due scan + catalyst countdown, ~2s) + `scripts/predictions_due.py` + `scripts/catalyst_countdown.py`. Created `docket/CATALYSTS.tsv` (8-col machine feed, backfilled from CRITICAL TIMELINE). Boot steps 4-5 rewritten as script-driven (was manual web-sweep that got skipped → staleness). Closed OTTO's long-deferred "Phase 4."
- **v2.3 — Closeout maturation toward SAM/BRENT.** STATUS line-cap (~250) + archive discipline (closeout step 1); created `CHANGELOG.md` thesis-pivot log + closeout step 1a; promotion-scan step (step 5) routing transferable lessons → auto-memory + remove-local; Git section fixed to pathspec pattern + Will-coordinated push (was the forbidden `git reset HEAD`/`git add <dir>`).
- **v2.4 — NEXUS_BRIEF.** Created `NEXUS_BRIEF.md` as a **Tier-2 opt-in** (locked schema is Tier-1-only; OTTO normally brief-exempt — Will approved the opt-in). Closeout step 7a (mandatory write-back). WALTER→NEXUS awareness signal dropped for scope ruling.
- **v2.5 — This log.** Created `MAINTENANCE.md`; trimmed CLAUDE.md version footer to point here; added closeout step 1b. Registered `STALE_PUNCHLIST.md` in CLAUDE.md (File Structure + Doc Ownership) after a Jun-8 re-audit (so the stale-doc plan survives MEMORY rewrites).

**Files touched:** `CLAUDE.md` (v2.1→v2.5), `STATUS.md` (417→163, archived), `MEMORY.md`, `LAST_COMPLETION.md`, `PREDICTIONS.tsv`, `workbook/ML.tsv`; **new:** `scripts/{boot,predictions_due,catalyst_countdown}.py`, `docket/CATALYSTS.tsv`, `CHANGELOG.md`, `NEXUS_BRIEF.md`, `MAINTENANCE.md`, `PEER_PARITY_ROADMAP.md`, `workbook/STATUS_archive_20260608.md`, 4 auto-memory files, WALTER inbox signal.

**Boot-impact:**
- Boot steps 4-5 now run `boot.py` (~2s) instead of manual sweep — the catalyst countdown + predictions-due scan are mechanized; boot read-sequence (STATUS→LAST_COMPLETION→MEMORY) unchanged.
- Closeout gained: 1a (CHANGELOG), 1b (MAINTENANCE), STATUS archive in step 1, promotion-scan in step 5, NEXUS_BRIEF write-back step 7a.
- `STALE_PUNCHLIST.md` now registered as a standing doc — next major session should re-audit it.

**Lessons (transferable — promoted to auto-memory):** date-specificity-weakest-link, forward-discovery-prediction-spirit, subagent-web-tools-not-autoloaded, litigation-allegation-weighting. Parity-audit recipe: compare boot first, then closeout, then structural logging — each pass surfaces a distinct doc-class gap.

---

## 2026-06-02 — Boot/closeout protocol hardening (v2.0 → v2.1, Phases 1-3b)

**Trigger:** Will-directed multi-phase protocol redesign (boot/closeout loop made self-closing).

**What changed:**
- **P1 Startup Protocol:** git-pull step 0 (+blocked-pull fallback); PREDICTIONS scan flags due-in-7d AND passed-but-OPEN; calendar past-due-catch (unswept vs acknowledged-pending); report-last ordering.
- **P2 Closing Protocol:** rewritten as write-back **mirror** of boot (read→write spine); catalyst-sweep BEFORE prediction-resolve (deliberate cross).
- **P3a:** live-state stripped from CLAUDE.md (Current Thesis → framing only; Thresholds drop Current col; STATUS = single source of truth).
- **P3b:** new `## Evidence & Hygiene Conventions` (evidence-grade tags `[CONF]/[PRESS]/[ALLEG]/[EST]`, `[STALE]` marking) + audit-finalized Doc Ownership table.

**Files touched:** `CLAUDE.md` (v2.0→v2.1); **new:** `STALE_PUNCHLIST.md` (9-item cross-doc rot inventory).

**Boot-impact:** boot/closeout became self-closing — boot flags overdue predictions + past-due catalysts; closeout must resolve them. First live catch: the new past-due-catch surfaced 3 unswept First Brands hearings, resolved same session.

**Lessons:** boot/closeout hardening recipe (mirror closeout to boot, strip live-state to single-source, doc-ownership table + deferred stale-punchlist) — auto-memory `[[finding_boot_closeout_hardening_recipe]]`.

---

*Pre-2026-06-02 structural history (Feb-Mar system build) not backfilled — reference root `archive/` graveyard + git log if needed.*
