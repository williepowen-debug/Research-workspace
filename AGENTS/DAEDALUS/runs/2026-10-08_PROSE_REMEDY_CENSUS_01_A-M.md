# Prose-Remedy Census #1 — step 2 classification, desks A–M

**Started:** 2026-10-08 16:15 EDT (from `date`) · **Classifier:** non-owner subagent for DAEDALUS (read-only; this file is its one write) · **HEAD:** 46fa6ef4a
**Input:** `runs/2026-10-08_PROSE_REMEDY_CENSUS_01_CANDIDATES.tsv` rows with desk A–M (CARL, CREED, FALCON, FLG, HANS, HAWK, HENRY, LABOR, LIQUID, MARCO, MIDAS) · **Playbook:** `sweeps/PROSE_REMEDY_SWEEP.md` §2 tokens.

## §0 Summary (27 candidate rows · 11 desks · all read)

| Desk | Candidates | PROSE-REMEDY | BUILT | DIAGNOSIS-ONLY | DECLINED | FALSE | Step-1 FP rate (FALSE/cand.) | Desk verdict |
|---|---|---|---|---|---|---|---|---|
| CARL | 2 | 1 | 0 | 0 | 0 | 1 | 1/2 = 50% | PROSE-REMEDY (1: Amendment-10 ordering, 43 sessions) |
| CREED | 2 | 0 | 0 | 0 | 1 | 1 | 1/2 = 50% | `CLEAN (2)` — the DECLINED row is a Will ruling, accepted |
| FALCON | 2 | 2 | 0 | 0 | 0 | 0 | 0/2 = 0% | PROSE-REMEDY (2: ordering 48 · line cap 68 LOW) |
| FLG | 1 | 0 | 0 | 0 | 0 | 1 | 1/1 = 100% | `CLEAN (1)` (one off-list miss noted, §3) |
| HANS | 1 | 0 | 1 | 0 | 0 | 0 | 0/1 = 0% | `CLEAN (1)` — BUILT row routes as an H-1 stale caveat |
| HAWK | 3 | 1 | 0 | 0 | 0 | 2 | 2/3 = 67% | PROSE-REMEDY (1: line target 69 LOW; byte budget at rotation band) |
| HENRY | 4 | 1 | 2 | 0 | 0 | 1 | 1/4 = 25% | PROSE-REMEDY (1: MEMORY line cap 108 LOW) |
| LABOR | 2 | 1 | 1 | 0 | 0 | 0 | 0/2 = 0% | PROSE-REMEDY (1: ordering 33) |
| LIQUID | 2 | 0 | 0 | 0 | 0 | 2 | 2/2 = 100% | `CLEAN (2)` |
| MARCO | 3 | 2 | 1 | 0 | 0 | 0 | 0/3 = 0% | PROSE-REMEDY (2: ordering 32 · line cap 88 LOW; one off-list miss, §3) |
| MIDAS | 5 | 4 | 1 | 0 | 0 | 0 | 0/5 = 0% | PROSE-REMEDY (4 rows = 2 remedies: `cot_metals.py` boot leg 3 · LESSONS hook cap 24 LOW) |
| **Total** | **27** | **12 rows / 10 distinct** | **6** | **0** | **1** | **8** | **8/27 = 30%** | 7 desks with PROSE-REMEDY · 4 `CLEAN` |

**By form:** form 1 (script + token) 14 rows → FALSE 7 (50%), BUILT 3, PROSE-REMEDY 3 (one remedy), DECLINED 1. Form 2 (CLAUDE.md comparison) 13 rows → FALSE 1 (8%), BUILT 3, PROSE-REMEDY 9.
**The 10 distinct remedies, by class:** ① NEXUS Amendment-10 ordering ("brief commit timestamp ≥ last STATUS commit timestamp") ×4 — CARL, FALCON, LABOR, MARCO; uncomputed everywhere except VIOLET-local `AGENTS/VIOLET/scripts/writeback_order_check.py`, so one shared tool would retire all four. ② Line/character caps with no counter ×5, all LOW — FALCON, HAWK, HENRY, MARCO, MIDAS. ③ `cot_metals.py` boot leg ×1 — MIDAS.
**Step-3 sentence:** this is classification only: 0 rows typed; premise-verified at the source for 0 of 0. Nothing here is fixed.
**Severity split:** 5 of the 10 distinct remedies are not-LOW (4 ordering, 1 COT leg). In the ordering class the failure cannot be seen: NEXUS (and HAWK, for FALCON) read the brief in place of STATUS. All 4 ordering desks pass by hand at their latest commits (2026-10-08 check). The remedy is missing; nothing is breached today.

## §1 Per desk, per row

### CARL — 2 candidates · 1 PROSE-REMEDY · 1 FALSE

| # | Surface line (quoted ≤200 chars) | Token | Basis |
|---|---|---|---|
| C1 | `AGENTS/CARL/STATUS.md:107` — "⚠️ `MOHELA complaints` and `Medicare Advantage membership` CANNOT FIRE until PROME adds lane queries for them (owed by PROME)." | `FALSE` | Routing-table cell naming a cross-owner config dependency, not a computation CARL carries. Matched on `newsweep_config.py` + "owed". Still open at the owner: `~/Research-Intake/scripts/newsweep_config.py:715-716` "PROVISIONAL: 0/0 … until a lane query fetches the subject (owed)" (last config commit `62b72b7` 2026-10-08). Outside H-4 (PROME's queue, not a desk prose-check). |
| C2 | `AGENTS/CARL/CLAUDE.md:110` (step 14b) — "the brief fold is the session's LAST write-back … Checkable form: brief commit timestamp ≥ last STATUS commit timestamp." | `PROSE-REMEDY (43)` | Comparison specified (brief commit ts vs last STATUS commit ts; failure = brief older than STATUS). No CARL script computes it: `grep -i brief` over `scripts/consistency_check.py` and `scripts/boot.py` = nothing on ordering; `consistency_check.py` reads NEXUS_BRIEF only for the score total (spec §32). No repo-root `scripts/*.py` names NEXUS_BRIEF. "Checkable form" sentence present since `62a2d27d0` 2026-08-10; **43 distinct CARL commit-days since 2026-08-10** (git log -- AGENTS/CARL/). Prior art to reuse: `AGENTS/VIOLET/scripts/writeback_order_check.py` (same rule, typed 2026-09-04). Current state passes by hand (STATUS and brief both last committed 2026-10-02 11:16:58) — the defect is the absence of the check, not a present breach. |

### CREED — 2 candidates · 1 DECLINED-BY-DESIGN · 1 FALSE

| # | Surface line | Token | Basis |
|---|---|---|---|
| CR1 | `AGENTS/CREED/STATUS.md:3` — "PRIOR: 2026-09-30 (Wed) EVENING … + `scripts/trepptalk_sweep.py` (not wired)." | `DECLINED-BY-DESIGN` | Will ruled 2026-10-01 11:02 ET "okay lets skip that then": sweep stays a manual tool, not a boot step, no WALTER packet (`SCRATCH.md:28`, `README.md:43`, commit `c816d93c4`). Script exists and was hardened (`a52c0da9e`, 13/13 saved cases). Accept, never re-flag. |
| CR2 | `AGENTS/CREED/LAST_COMPLETION.md:90` — "`creed_selfcheck.py` **exit 0** … cross-agent consumer hits **triaged as false positives** (bare 2-sig-fig `-0.34` …) — **no packet owed**" | `FALSE` | A CHECKS receipt line; "owed" = "no packet owed". Note: lines 85–96 are a stale 2026-08-20 block beneath a 2026-10-01 header (H-1 stamp-over-body shape) — not this census's class; mentioned only. |

> **Classifier's note on line-cap rows (applies to FALCON F1, HAWK H2, MARCO M2, HENRY He4).** A STATUS/MEMORY "under N lines" step with no script is the letter of form 2, and no script in any of these desks or repo-root `scripts/` counts lines against a desk cap (grep `250`/`120`/`lines` over desk `scripts/` and root `scripts/*.py`: nothing; root `read_cap_check.py:12` itself records that line caps pass clean over over-cap files). Classified `PROSE-REMEDY` by the letter, **severity LOW**: the failure is visible on any read, and the binding constraint (32,550 B, root Data Hygiene) IS computed by root `scripts/read_cap_check.py --agent <X>`. The cheap remedy is to cite/wire that check at the step (or retire the line cap), not to type a line counter. Ran it read-only 2026-10-08: FALCON/HENRY/MARCO rc=0 rotation_due=0; **HAWK rotation_due=1** (STATUS 70 lines / 22,772 B) — the line target (≤120) passes while the byte budget is at the 70% rotation band, which is the argument in one figure.
>
> **Session counting basis (all desks):** distinct commit dates touching `AGENTS/<DESK>/` from the date the clause entered the file (`git log -S`) to HEAD `46fa6ef4a`. A commit-day is a proxy for a session (over-counts days with only peer-packet commits; under-counts multi-session days). Every count below is ≥2 by a wide margin, so the proxy does not change any verdict.

### FALCON — 2 candidates · 2 PROSE-REMEDY

| # | Surface line | Token | Basis |
|---|---|---|---|
| F1 | `AGENTS/FALCON/CLAUDE.md:96` (closeout 9) — "**`STATUS.md`** — write the dashboard back … Keep under 250 lines (archive overflow to `domain/sources/` — none yet, see FILES note)." | `PROSE-REMEDY (68)` LOW | Clause since `3fb46ebdf` 2026-07-12; 68 FALCON commit-days since. No FALCON script counts lines (`scripts/`: 4 watchers + `warrisk_row_staleness.py`). Currently 92 lines / 16,279 B; FALCON's CLAUDE.md does not invoke root `read_cap_check.py` at closeout (only a mention at :86). |
| F2 | `AGENTS/FALCON/CLAUDE.md:102` (closeout 14) — "ORDERING (NEXUS schema Amendment 10 …): the brief fold is the session's LAST write-back … Checkable form: the brief's commit timestamp ≥ the session's last STATUS commit timestamp." | `PROSE-REMEDY (48)` | Clause since `bbc0718b2` 2026-08-06; 48 FALCON commit-days since. `NEXUS_BRIEF` appears in FALCON `scripts/` only in `bypass_watch.py:12` docstring (where the mark lives) — no ordering comparison anywhere in FALCON or root `scripts/`. Passes by hand now (STATUS 2026-10-07 22:35:13, brief 22:36:12). Prior art: `AGENTS/VIOLET/scripts/writeback_order_check.py`. Consequence named on the same line: HAWK and NEXUS read this brief in place of STATUS. |

### HAWK — 3 candidates · 1 PROSE-REMEDY · 2 FALSE

| # | Surface line | Token | Basis |
|---|---|---|---|
| H1 | `AGENTS/HAWK/SCRATCH.md:9` — "**CLOSEOUT AUDIT 16:25 ET …** That is one session old, so no \">1 session\" flag is owed yet. **Re-check next session; if FALCON still hasn't adopted the quotes, packet it.**" | `FALSE` | Closeout-audit receipt (2026-09-28). Matched on `consumer_check.py` ("Declared, not done: `consumer_check.py` was not run (no numeric threshold superseded …)" — a reasoned skip) + "owed". The ">1 session" divergence test of closeout 12 is a judgment comparison of sibling briefs' content, not an arithmetic one; not this class. |
| H2 | `AGENTS/HAWK/CLAUDE.md:68` (closeout 10) — "**Target ≤120 lines** (this is a thin synthesis surface, not a theater tracker — if it's growing toward 250, you're re-narrating …)" | `PROSE-REMEDY (69)` LOW | Clause since `699c766a5` 2026-07-12; 69 HAWK commit-days since. `scripts/boot.py` has no line count (only `output.splitlines()` at :81/:157 on subprocess output). STATUS 70 lines (passes) / 22,772 B — root `read_cap_check.py --agent HAWK` reports **rotation_due=1**; the uncomputed line target is the wrong instrument for the live risk. |
| H3 | `AGENTS/HAWK/CLAUDE.md:69` (closeout 11) — "log new synthesis/dormant facts → `workbook/KB.tsv` (KB-HAWK-224+; pre-split rows ≤223 are frozen history); … `workbook/VX.tsv` (10 rows …)" | `FALSE` | ID-range descriptors (`≤223`, `HAW-18+`) matched the comparison token; no check is specified. (The literal "10 rows" is a count claim that can rot — an H-1 stamp shape, not H-4; noted only.) |

*HAWK context:* closeout 13a's ">10 days old" leg flag is mechanized in part by `scripts/derived_freshness.py` (`54accb874` 2026-09-08, input-fingerprint drift, rc 0/1/2) — that script certifies input change, not print age; it was not a candidate row and is not classified here.

### FLG — 1 candidate · 1 FALSE · desk `CLEAN (1)`

| # | Surface line | Token | Basis |
|---|---|---|---|
| G1 | `AGENTS/FLG/STATUS.md:152` — "**Owed to me:** … ② ~~PROME/intake: add FLG to `fetch_edgar_8k.py`~~ ✅ LANDED 9/27 (Research-Intake `3129030`, verified at artifact …)" | `FALSE` | A struck DONE line (playbook's named noise class). |

*Step-1 miss on the adjacent line (not a candidate; recorded for the token refinement, not classified):* `AGENTS/FLG/STATUS.md:150` — "**Owed by me:** … ② a numeric comparator for K-4's \"materially above\" leg (DAEDALUS 8/23 §3, carried)". Owed since `37f7afb3a` 2026-08-28 (14 FLG commit-days since). It names no `.py`, so form 1 cannot see it. Whether it is H-4 (code) or a spec edit (a number in `workbook/EXIT_PROTOCOL.md` K-4) is the owner's call — see §3.

### HANS — 1 candidate · 1 BUILT

| # | Surface line | Token | Basis |
|---|---|---|---|
| N1 | `AGENTS/HANS/STATUS.md:122` — "🔴 **FIRST: `python3 scripts/doc_audit.py`** (RULE #1b) — **see owed #15: it reads clean over surfaces it does not scan.**" | `BUILT` | The pointer's target is closed: `STATUS.md:137` "#15 ✅ **DONE 9/19 — `C9` BUILT.** Scans the whole boot-read set, not just STATUS". Code: `scripts/doc_audit.py:217` `C9_SURFACES = ['STATUS.md', 'CLAUDE.md', 'DISPATCH_LOG.md', …]`, built in `036c54267` 2026-09-19. The caveat entered 2026-09-18 (`a3a39f378`) and has ridden 11 HANS commit-days past the fix (STATUS last committed `ae7bf8d27` 2026-10-08). Route as an H-1 stamp-over-body instance: the boot's FIRST instruction carries a caveat its own table retired. |

### HENRY — 4 candidates · 1 PROSE-REMEDY · 2 BUILT · 1 FALSE

| # | Surface line | Token | Basis |
|---|---|---|---|
| He1 | `AGENTS/HENRY/MAINTENANCE.md:108` (entry 2026-07-10, WIRED boot.py) — "**Still owed to Will:** post-change eval re-run (guardrails 02/03 must hold …) + the case-03 baseline that was never run." | `FALSE` | Discharged the same day: the next entry up, `MAINTENANCE.md:95` "2026-07-10 (later, ~11:00 ET) — POST-WIRING EVAL RE-RUN (01+02) + CASE-03 FIRST BASELINE — 3/3 PASS", rows in `evals/results.tsv` (2026-07-10 01/02/03 PASS). An append-only changelog entry superseded below its successor; and an eval run is judgment, not a computation. |
| He2 | `AGENTS/HENRY/CLAUDE.md:66` — "Boot step **(f)** lists `inbox/` **filenames only** … flags a packet if its name carries (a) a date inside the next 14 days … or (e) it has sat ≥10 days unread." | `BUILT` | Computed: `scripts/boot.py:448-509` (`INBOX_WINDOW_DAYS = 14`, `INBOX_STALE_DAYS = 10`, `triage_names()`), built `911fa0c6f` 2026-07-28 ("boot (f) inbox triage"). The line is not stale — the step is code; matched on its thresholds. |
| He3 | `AGENTS/HENRY/CLAUDE.md:230` (FILES) — "`LESSONS.md` | … **≤32,550 B (P1 read-cap budget).**" | `BUILT` | Computed by repo-root `scripts/read_cap_check.py --agent HENRY` (LESSONS.md in its perimeter via boot-step line 28; 2026-10-08 read: 24,342 B = 75% of budget, rc=0, rotation_due=0). **Wiring gap, not an H-4 row:** HENRY's CLAUDE.md never names `read_cap_check` (grep: 0 hits), so the check runs only when someone else sweeps. LESSONS sits at the ≥75% rotation band edge (24,342 vs 24,412 B). |
| He4 | `AGENTS/HENRY/CLAUDE.md:233` (FILES) — "`MEMORY.md` | Cross-session memory … **Boot step 3. Write before finishing.** ≤100 lines." | `PROSE-REMEDY (108)` LOW | Line cap since `b293d676f` 2026-04-17 (108 HENRY commit-days since); no HENRY or root script counts MEMORY.md lines (`boot.py`/`status_figure_manifest.py`: no MEMORY line count). Now 66 lines / 18,156 B (56%) — passing; the byte leg is the computed one (He3's tool). |

### LABOR — 2 candidates · 1 PROSE-REMEDY · 1 BUILT

| # | Surface line | Token | Basis |
|---|---|---|---|
| L1 | `AGENTS/LABOR/CLAUDE.md:81` (C1) — "**ORDERING (NEXUS schema Amendment 10 …; installed here 8/5):** … Checkable form: **your brief's commit timestamp ≥ your session's last STATUS commit timestamp.**" | `PROSE-REMEDY (33)` | Clause since `f5525d857` 2026-08-05; 33 LABOR commit-days since. No LABOR script names NEXUS_BRIEF (`scripts/`: boot, spine_check, card_*_check, predictions_due, …); no root or NEXUS script computes brief-vs-STATUS ordering (NEXUS has no `scripts/`; the only fleet implementation is VIOLET-local `writeback_order_check.py`). The sibling bullet (:82) names NEXUS's "mechanical stale-check (§4.4a)" — that is a schema section, not code found in the repo. Passes by hand now (STATUS 2026-10-08 08:36:43, brief 08:38:23). |
| L2 | `AGENTS/LABOR/CLAUDE.md:88` (C2) — "⚠️ **As-made comes from the earliest `STATUS.md` blob carrying the row's confidence cell — NEVER from `PREDICTIONS.tsv` for any row with `Date_Made` ≤ 2026-03-04** …" | `BUILT` | The matched comparison is computed by repo-root `scripts/asmade_audit.py` (built `d4ffc16ec` 2026-09-07, DAEDALUS harvest H2, Will-ruled; docstring: "runs LABOR's reproducible procedure fleet-wide"; rc 0/1/2). **Wiring gap:** LABOR's C2 does not name the tool (grep `asmade_audit` over LABOR CLAUDE.md + SCOREBOARD: 0 hits), so the procedure still reads as hand work. Separate leg on the same line, not classified (no defect named): "recompute the stats" (mean Brier) has no LABOR script either — CARL's `brier_audit.py` is the fleet precedent. |

### LIQUID — 2 candidates · 2 FALSE · desk `CLEAN (2)`

| # | Surface line | Token | Basis |
|---|---|---|---|
| Q1 | `AGENTS/LIQUID/STATUS.md:14` — "The z ≥4.0 and 079-ARM legs were not run this session (`sofr_dispersion.py` at the verdict). … RED's context rows are still owed beside the verdict (§3)." | `FALSE` | The legs are code (`scripts/sofr_dispersion.py:88` `Z_YELLOW, Z_ORANGE, Z_RED = 3.0, 4.0, 6.0`) deferred to a dated verdict (10/15–10/16) by design; "owed" = RED's context rows, a peer judgment input. No uncomputed remedy. |
| Q2 | `AGENTS/LIQUID/STATUS.md:73` (§5 standing caveats) — "**Vintage:** `fetch.py` sends no `realtime_*`, so figures are **LATEST-REVISED** … For HY OAS, 0 revisions are observed 6/25→9/25 (KB-LIQ-137, windowed claim)." | `FALSE` | **Token noise:** step 1's unanchored `owed` matched inside "wind**owed**". The line is a standing coverage caveat; the exception it names is built (`scripts/hy_oas_watch.py:377` `_first_published`, `realtime_start=` at :383). |

### MARCO — 3 candidates · 2 PROSE-REMEDY · 1 BUILT

| # | Surface line | Token | Basis |
|---|---|---|---|
| M1 | `AGENTS/MARCO/MAINTENANCE.md:88` (✅ T2-D, DONE 2026-07-31) — "**Class lesson: an append-only docket edit needs a dedup pass against existing rows, and a `date+event` uniqueness check is one line — worth adding to `catalyst_countdown.py` so it self-detects.**" | `BUILT` | Built the same session: `scripts/catalyst_countdown.py:58-90` ("Added 2026-07-31 after the docket accumulated three DUPLICATE event pairs" → `LIKELY DUPLICATE` warning), commit `572cad695` 2026-07-31 ("docket deduped, both self-checks mechanized"). The "worth adding" clause inside the ✅ block was never re-cut — H-1 stamp-over-body, cosmetic. |
| M2 | `AGENTS/MARCO/CLAUDE.md:51` (closeout 6) — "**`STATUS.md` write-back** — … Keep under 250 lines (archive overflow to `domain/sources/_archive/`)." | `PROSE-REMEDY (88)` LOW | Clause since `3e6a0ed98` 2026-03-02 (fleet template origin; same commit seeds LABOR's); 88 MARCO commit-days since. No MARCO script counts STATUS lines (`staleness.py:56` reads only the first 5 lines for a header stamp). Now 120 lines / 22,670 B; root `read_cap_check.py --agent MARCO` rc=0. |
| M3 | `AGENTS/MARCO/CLAUDE.md:56` (closeout 11) — "**`NEXUS_BRIEF.md` write-back … THIS IS THE SESSION'S *LAST* WRITE-BACK** … **Checkable form: the brief's commit timestamp ≥ this session's last STATUS commit timestamp.**" | `PROSE-REMEDY (32)` | Clause since `a2fb0f914` 2026-08-11; 32 MARCO commit-days since. MARCO's own guard `scripts/version_drift_check.py` (`59bc9f43a` 2026-08-12) reads NEXUS_BRIEF for classes V/C/B (version drift, duplicated field label, incomplete rename) — **not ordering**; no `git log %ct` comparison anywhere in MARCO `scripts/`. Passes by hand now (both last committed 2026-09-24 19:07:05 — same commit). |

*Step-1 miss on the same surface (not a candidate; recorded for refinement):* `AGENTS/MARCO/MAINTENANCE.md:80-81` — "🟡 **T2-E · Banxico + slaughter fetchers still cadence-skip on mtime — PARTLY DONE (checked 2026-09-24)** … Still on mtime: **CE100 state map** (quarterly, 85d) and **slaughter weekly** (6d). Remaining work = those two `vintage_fn`s." Fully specified (what: a content-vintage `vintage_fn`; against: the header `pulled=/latest_period=`; failure direction: mtime restamped by git sync ⇒ false-negative skip), and `scripts/boot.py:86` still passes `None` for `banxico_destination_states.tsv`. Opened 2026-07-31 (`572cad695`), 38 MARCO commit-days since. Reads as `PROSE-REMEDY (38)` on the classifier's judgment; not counted in §0 because it is off-list. Tokens it carries that the step-1 list lacks: "Remaining work", "still on mtime", "**Action:**".

### MIDAS — 5 candidates · 4 PROSE-REMEDY rows (2 distinct remedies) · 1 BUILT

MIDAS keeps its scripts at the desk root (`AGENTS/MIDAS/*.py`), not under `scripts/` — read there.

| # | Surface line | Token | Basis |
|---|---|---|---|
| Mi1 | `AGENTS/MIDAS/SCRATCH.md:31` (block 2026-10-02) — "> ② `cot_metals.py` boot leg (needs a per-metal consumed-vintages ledger first)." | `PROSE-REMEDY (3)` | Specified: wire `cot_metals.py` as a boot leg the way `cot_gold.py` is leg 3 (`boot.py:23`, `:63` `COT_VINTAGES`, `:216`), graded against a per-metal consumed-vintages ledger; failure direction stated by the gold ledger it mirrors (`sources/cot_vintages_consumed.tsv:3-5`: "STATUS could carry a COT figure that had been superseded at the source with nothing to say so"). `boot.py` imports only `cot_gold`; no per-metal ledger exists (`sources/`: `cot_vintages_consumed.tsv` is gold-only, CFTC 088691). `cot_metals.py` built 2026-09-25 (`1d746010b`); carried in MIDAS's dated blocks 9/25, 10/1, 10/2 = **3 sessions** (no MIDAS-authored commit after 10/2). Silver/Pt/Pd COT is a named THESIS instrument (`THESIS.md:106`, `:171`). |
| Mi2 | `AGENTS/MIDAS/SCRATCH.md:43` (block 2026-10-01) — "③ `cot_metals.py` boot leg (needs a per-metal ledger)." | `PROSE-REMEDY (3)` — same remedy as Mi1 | Earlier carry of Mi1. |
| Mi3 | `AGENTS/MIDAS/SCRATCH.md:61` (block 2026-09-25) — "⑥ Wire `cot_metals.py` as a boot leg: deliberately NOT done yet; needs a consumed-vintages ledger per metal first." | `PROSE-REMEDY (3)` — same remedy as Mi1 | First carry. "Deliberately NOT done yet" is sequencing (ledger first), not a written decline — so not `DECLINED-BY-DESIGN`. |
| Mi4 | `AGENTS/MIDAS/SCRATCH.md:92` (block 2026-09-05) — "**▶ 🔴 NEW INSTRUMENT DEFECT, FOUND AND NOT PATCHED** … All **five** `=F` pointers sat on **dying contracts** … ⛔ **Deliberately unpatched:** the guard needs a volume field `fetch.py` does not return …" | `BUILT` | `metals_watch.py:107` `FRONT_MONTHS` + `:113` `check_contract_identity()` (grades each `=F` pointer on the PRIOR settled session, DYING <5% volume share, rc=1 REVIEW), introduced in `9c31f4923` 2026-09-11 (bundled under a "VECTOR 3" subject); `OPEN_ITEMS.md:21` "✅ **CLOSED 2026-09-11 — the contract-identity guard is BUILT, TESTED and BOOT-WIRED**". The 9/5 block is still on the boot-read SCRATCH, five session blocks deep — MIDAS's own owed list carries "SCRATCH rotation of the 9/11 and 9/5 blocks" (Mi2 line ④). H-1 instance; rotation, not code, is the fix. |
| Mi5 | `AGENTS/MIDAS/CLAUDE.md:230` (FILES) — "`LESSONS.md` | Durable agent-level learning — **INDEX ONLY since 2026-08-27** (one hook per lesson, ≤~170 chars). **Not boot-read** …" | `PROSE-REMEDY (24)` LOW | Clause since `a8148a42b` 2026-08-27; 24 MIDAS commit-days since. No MIDAS script measures hook length. **Live breach:** 12 of 53 hook cells exceed 170 characters (max 293; awk over `^| **L-nn` rows, markup included, 2026-10-08). The "~" makes it a soft cap; owner may prefer to declare it advisory (a written decline would settle it). |

## §2 Per-owner asks (STRICT one-liners for DAEDALUS to packet; the classifier sent nothing)

*Shared prior art for every ordering ask: `AGENTS/VIOLET/scripts/writeback_order_check.py` (VIOLET-local, typed 2026-09-04). DAEDALUS may prefer a single repo-root tool over four desk copies; that is DAEDALUS's design call (it owns root `scripts/`), recorded here as an option, not an ask.*

| Owner | ACTION line | Surface | Carry | Token |
|---|---|---|---|---|
| CARL | CARL types closeout 14b's ordering rule as a check that exits nonzero when `NEXUS_BRIEF.md`'s last commit time is earlier than `STATUS.md`'s. | `AGENTS/CARL/CLAUDE.md:110` | 43 sessions (since 2026-08-10) | `PROSE-REMEDY (43)` |
| FALCON | FALCON types closeout 14's ordering rule as a check that exits nonzero when `NEXUS_BRIEF.md`'s last commit time is earlier than `STATUS.md`'s. | `AGENTS/FALCON/CLAUDE.md:102` | 48 sessions (since 2026-08-06) | `PROSE-REMEDY (48)` |
| FALCON | FALCON replaces closeout 9's "Keep under 250 lines" with a call to `scripts/read_cap_check.py --agent FALCON`, or types the line count. | `AGENTS/FALCON/CLAUDE.md:96` | 68 sessions (since 2026-07-12) | `PROSE-REMEDY (68)` LOW |
| LABOR | LABOR types C1's ordering rule as a check that exits nonzero when `NEXUS_BRIEF.md`'s last commit time is earlier than `STATUS.md`'s. | `AGENTS/LABOR/CLAUDE.md:81` | 33 sessions (since 2026-08-05) | `PROSE-REMEDY (33)` |
| LABOR | LABOR names repo-root `scripts/asmade_audit.py LABOR` in C2 at the as-made procedure. | `AGENTS/LABOR/CLAUDE.md:88` | n/a (wiring) | `BUILT` (unwired at the step) |
| MARCO | MARCO types closeout 11's ordering rule as a check that exits nonzero when `NEXUS_BRIEF.md`'s last commit time is earlier than `STATUS.md`'s. | `AGENTS/MARCO/CLAUDE.md:56` | 32 sessions (since 2026-08-11) | `PROSE-REMEDY (32)` |
| MARCO | MARCO replaces closeout 6's "Keep under 250 lines" with a call to `scripts/read_cap_check.py --agent MARCO`, or types the line count. | `AGENTS/MARCO/CLAUDE.md:51` | 88 sessions (since 2026-03-02) | `PROSE-REMEDY (88)` LOW |
| MARCO | MARCO deletes the "worth adding to `catalyst_countdown.py`" clause from the ✅ T2-D block; `572cad695` built that check on 2026-07-31. | `AGENTS/MARCO/MAINTENANCE.md:88` | n/a | `BUILT` (H-1) |
| HAWK | HAWK replaces closeout 10's "Target ≤120 lines" with a call to `scripts/read_cap_check.py --agent HAWK`, which reported rotation_due=1 on 2026-10-08. | `AGENTS/HAWK/CLAUDE.md:68` | 69 sessions (since 2026-07-12) | `PROSE-REMEDY (69)` LOW |
| HENRY | HENRY replaces the FILES-row "≤100 lines" for `MEMORY.md` with a call to `scripts/read_cap_check.py --agent HENRY`, or types the line count. | `AGENTS/HENRY/CLAUDE.md:233` | 108 sessions (since 2026-04-17) | `PROSE-REMEDY (108)` LOW |
| HENRY | HENRY names `scripts/read_cap_check.py --agent HENRY` at the LESSONS.md "≤32,550 B" row; LESSONS.md measured 24,342 B (75%) on 2026-10-08. | `AGENTS/HENRY/CLAUDE.md:230` | n/a (wiring) | `BUILT` (unwired at the step) |
| HANS | HANS deletes "see owed #15: it reads clean over surfaces it does not scan" from boot line FIRST; owed #15 closed 2026-09-19 (`036c54267`, `C9_SURFACES`). | `AGENTS/HANS/STATUS.md:122` | 11 sessions stale | `BUILT` (H-1) |
| MIDAS | MIDAS builds a per-metal consumed-vintages ledger for Ag/Pt/Pd and wires `cot_metals.py` as a `boot.py` leg graded against it. | `AGENTS/MIDAS/SCRATCH.md:31` (also :43, :61) | 3 sessions (9/25, 10/1, 10/2) | `PROSE-REMEDY (3)` |
| MIDAS | MIDAS rotates the 2026-09-05 SCRATCH block; its "FOUND AND NOT PATCHED" defect closed 2026-09-11 (`metals_watch.py` `check_contract_identity`). | `AGENTS/MIDAS/SCRATCH.md:92` | n/a | `BUILT` (H-1) |
| MIDAS | MIDAS types the LESSONS hook cap "≤~170 chars" as a check, or writes it down as advisory; 12 of 53 hooks exceeded 170 characters on 2026-10-08. | `AGENTS/MIDAS/CLAUDE.md:230` | 24 sessions (since 2026-08-27) | `PROSE-REMEDY (24)` LOW |

No ask for CREED (DECLINED-BY-DESIGN, Will 2026-10-01; never re-flag), FLG, LIQUID (all FALSE). CARL C1 (`newsweep_config.py` lane queries) is PROME's open item at `~/Research-Intake/scripts/newsweep_config.py:715-716`, not a census ask.

## §3 Limits

1. **Session counts are commit-day proxies** (distinct dates with any commit under `AGENTS/<DESK>/`, from the clause's `git log -S` introduction date to HEAD `46fa6ef4a`). They over-count days that held only inbound peer packets and under-count multi-session days. MIDAS's count (3) was taken from its own dated SCRATCH blocks instead, because it is small enough for a proxy error to matter. Every verdict clears the ≥2 bar by a wide margin, so the proxy cannot flip a token. Exact ages are not certified.
2. **"No code computes it" was searched, not proven.** Searched: the desk's `scripts/` (MIDAS: desk-root `*.py`), repo-root `scripts/*.py`, and a fleet grep for `NEXUS_BRIEF` / `STATUS commit` in `*.py`. A check living in a hook, a CI file, `PROME/tools/` or `~/Research-Intake` was not searched (except `newsweep_config.py` for CARL C1). NEXUS has no `scripts/` dir. Its schema's "mechanical stale-check (§4.4a)", cited at `LABOR/CLAUDE.md:82`, was not found as code. The schema file at `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` was not opened.
3. **Ordering "passes by hand now" compares only each desk's latest commits.** It is not a history audit. Sessions where the brief landed before a later STATUS commit were not counted. A typed check would also be the right instrument for that backfill.
4. **Line-cap rows are classified by the letter of form 2 and marked LOW** (see the note above FALCON in §1). If DAEDALUS rules that a line cap superseded by the computed root byte budget is not an H-4 remedy, those 5 rows become `FALSE`. Totals would then be 7 PROSE-REMEDY rows / 5 distinct, and 13 FALSE (48%).
5. **Off-list observations, not counted in §0:** `AGENTS/FLG/STATUS.md:150` (K-4 "numeric comparator", owed since 2026-08-28) and `AGENTS/MARCO/MAINTENANCE.md:80-81` (T2-E two `vintage_fn`s, open since 2026-07-31; classifier reads it as `PROSE-REMEDY (38)`). Both are step-1 misses: no `.py` on the line, or tokens outside the list ("Remaining work", "still on mtime", "**Action:**"). These two come from this classifier's incidental reading of ±10 lines around the candidates. They are not a recall measurement.
6. **Token-list refinement inputs (no widening without a fleet before/after diff, per playbook §5):** (a) `owed` is unanchored and matched "wind**owed**" (LIQUID Q2). Use `\bowed\b`. (b) Negated forms ("no packet owed", "no consume row owed", "no … flag is owed") produced 2 of the 8 FALSE rows (CREED CR2, HAWK H1). (c) Struck/✅ lines (FLG G1) and append-only changelog entries discharged by a later entry (HENRY He1) are DONE-noise. (d) Form 2 matched ID ranges (`≤223`, `HAW-18+`; HAWK H3). Requiring a unit (lines/bytes/chars) or a timestamp noun next to the comparator would remove that class. (e) Form-1 FALSE rate is 50% (7/14) against 8% (1/13) for form 2.
7. **BUILT means the code exists and was read; this pass did not verify that it works.** The cited code was not run, except `read_cap_check.py` (read-only, rc and summary line only). No guard was falsified per CHECK_STANDARD §3.
8. Read-only throughout. The only write is this file. Nothing was committed, no messages were sent and no subagents were used.


**Closed:** 2026-10-08 16:24 EDT (from `date`)
