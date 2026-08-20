# CREED Maintenance Log

Reverse-chronological log of **structural** changes to CREED's docs, folders, schema, and boot/closeout protocol. Answers *"why is CREED organized this way, and what decision am I about to re-litigate?"*

**Distinct from:**
- `STATUS.md` — live analytical dashboard (canonical truth).
- `SCRATCH.md` — **ephemeral** per-session handoff (overwritten every closeout; structural notes there do NOT persist — they persist **here**).
- `thesis/CHANGELOG.md` — **analytical** thesis pivots (scores, signals, base case). Structural ≠ analytical: the *decision to split S8* is analytical and lives in CHANGELOG; *creating a workbook to hold the split* is structural and lives here.

> **⚠️ This is a consult-on-structural-work doc, NOT a per-session ritual.** *(Framing adopted verbatim-in-spirit from BROCK, which warns of exactly this bloat and cites SAM at 636 lines as the cautionary tale.)* **Do not wire it into every closeout** — CREED is **Tier-2 spawn-on-need** and process weight is the specific thing that makes a spawn-on-need agent expensive to wake. Touch it only when a session changes CREED's *structure*: a doc/folder created/retired/moved, a schema or protocol amendment, an ownership boundary shift. **Cap: archive to `archive/` if this grows past ~300 lines.**

---


## 2026-08-20 — fire ledger created; a missing metric vector identified as the root cause of a 6-week detection lag

**1. NEW: `registry/CREED_T_FIRED_LOG.tsv` — the single CREED-T fire record.**
Created on the first fire in the registry's history (`CREED-T-02`). Schema: `trigger_id · fired_date · effective_date · detection_lag · metric · band · observed_series · verdict · routed_to · basis · notes`. **`effective_date` and `detection_lag` are separate columns by design** — the date a band was actually satisfied is not the date CREED noticed, and collapsing them would erase exactly the failure this ledger's first row records.
⚠️ **Deliberately the ONLY such ledger.** WALTER asked 8/19 whether to build a WALTER-side mirror (it keeps them for RED-FT and REG-T). **CREED answered NO on WALTER's own reasoning** — a second ledger splits the truth, and a fire recorded in two disagreeing places is worse than one recorded nowhere. **WALTER reads this file; it does not mirror it.** Do not re-litigate without reversing that reasoning.

**2. NEW: `VX-CREED-3.04` (Matured-Balloon Share of New Delinquencies) — created as a ROOT-CAUSE FIX, not a coverage addition.**
`CREED-T-02` was the **only numerically-banded CREED trigger with no VX vector carrying its metric** (31 vectors, none for matured-balloon share). Consequence, observed live: on **8/13** CREED wrote "66% of $6.0B newly delinquent" into `VX_HISTORY` and `VX-CREED-1.02`'s **notes prose** — the T-02 metric against a band of 50 — **and did not grade it**, because no vector mapped the number to the trigger. **The trigger went ungraded for ~6 weeks with the desk awake and the number in its own files.**
⚠️ **Yellow/Orange left `--` ON PURPOSE.** The vector **transcribes the existing Will-frozen band and creates no new threshold**; inventing intermediate bands would be a new Will-gated term. **Do not "complete" those cells.**

> **Structural lesson, recorded because it may generalise beyond CREED:** *a registry row and a dashboard vector are two different instruments. A threshold that exists in only one of them is ungradeable in practice, however correctly it is written.* `THRESHOLDS.tsv`'s header declares it "MOVES NOTHING" — accurate, and that **was** the defect: transcription without a metric surface produced a trigger nobody could trip. **Flagged to PROME as a possible fleet sweep (DAEDALUS's call). CREED has audited only CREED.**

**3. Source-tier change: Trepp SECONDARY → PRIMARY-READ for Apr–Jul 2026.** WALTER archived five Trepp PDFs at `AGENTS/WALTER/sources/`; they are readable with pdfminer and CREED read all five. **Standing trap #3 is now PARTIALLY retired** — it remains true for months not archived. ⚠️ **The trap text in `CLAUDE.md` was NOT rewritten** — the general warning still holds and the exception is month-scoped; a next session should not read "primary-CITED" as universally false.
## 2026-07-27 (fifth sitting) — HENRY/CARL survey: the eval suite, and the discovery that CREED's newest disciplines were in the WRONG SURFACE

**Trigger:** Will directed the same survey against **HENRY** (macro/wealth-effect; `evals/`, `BOOT_AUDIT.md`, `MODERNIZATION_PLAN.md`, clustered `research/prompts`+`outputs`) and **CARL** (consumer credit; **7 sub-agents** each with `state_vectors/`+`workbook/`, `SIGNAL_INTAKE.md`, `SPAWN_PROTOCOL.md`, `templates/`, 13 scripts). Both clean/not-live.

**⭐ The finding was about CREED, and reading HENRY's suite is what produced it.**

HENRY's `evals/README.md` draws a distinction no other agent states: **a principle expressed as a BOOT STEP is not in the always-loaded surface.** The always-loaded surface is `CLAUDE.md` body + auto-memory. Everything else — `STATUS.md`, `SCRATCH.md`, `COVERAGE.md`, the workbook — loads *only if boot runs and is read closely*.

**Applied to CREED, that is uncomfortable: every trap CREED learned the hard way on 7/27 had been written into `SCRATCH.md` — a boot step.** The corporate-action rule, the wrong-basis rule, the Trepp paywall marking, the distribution-anchoring rule, the whole-loans-only rule. **All of them fire while WRITING A NUMBER, not at boot** — so a session that skimmed boot would lose precisely the five things that cost CREED most today, and none of them would be eval-testable.

**Fix: `CLAUDE.md` gained an ALWAYS-LOADED standing-traps block** (5 traps, full versions still in `SCRATCH.md`). **This is the single highest-leverage change of the five surveys** — it moves the load-bearing disciplines from a conditionally-read surface to an unconditionally-read one.

**Adopted (2):**

| Change | Why |
|---|---|
| **`CLAUDE.md` §Standing traps — ALWAYS-LOADED** | Above. Derived from HENRY's skip-boot analysis, not copied from a file. |
| **`evals/`** (new) — from `HENRY/evals/`, itself from `SAM/evals/` | Two-file INPUT/RUBRIC split · **TARGET vs GUARDRAIL roles** (a TARGET is *expected* to fail at baseline — the change is meant to fix it) · promotion rule = *TARGET improves AND every GUARDRAIL holds*, not flat no-regression · `lesson-absent` verdict (principle not in a loaded surface ⇒ **fix the surface, not the reasoning**) · contamination→VOID. **Both cases are drawn from real CREED failures of 2026-07-27**, not invented scenarios: case 01 = the ARI corporate-action near-miss (GUARDRAIL); case 02 = the `PRED-CREED-006` seasonal-trough baseline (TARGET), which also scores SHADE's proposed over-correction as a FAIL. ⚠️ **SHIPPED UNRUN** — establishing a baseline needs a fresh skip-boot session this session could not run for itself. `results.tsv` says so explicitly; **a blank table is not a pass.** **Trigger is CHANGE, not cadence** — CREED made 5 prompt-surface changes on 7/27 alone. |

**Declined (4):**
- **CARL's `sub_agents/` fleet** (7 sub-agents, each with `state_vectors/`+`workbook/`) — CREED **was** a sub-agent until 6/21 and has one domain, not seven. Sub-agents are a mandate-decomposition tool; CREED's mandate is already the decomposition of REGINALD's.
- **CARL `templates/`** — CREED's packets are argument-shaped, not form-shaped; the reusable part is the disciplines block, which now lives in `CLAUDE.md`.
- **CARL `SIGNAL_INTAKE.md`** — CREED's intake is one WALTER lane plus direct packets; `board_log.tsv` already records disposition, and the Route Matrix already records criteria.
- **HENRY `MODERNIZATION_PLAN.md` / `BOOT_AUDIT.md`** — `MAINTENANCE.md` (this file) already carries the structural log + backlog; a third planning surface is drift.

**⭐ Cross-agent finding — the S5 demotion hit a FOURTH surface, and it was CREED's own:**

**`CLAUDE.md:26` still read *"`CARL` — multifamily / housing-consumer spillovers"* — contradicting the Route Matrix 21 lines below it, which already read `(non-MF)`.** `STATUS.md:201` carried the same stale line. **CREED's boot doc disagreed with itself for the entire 7/27 session.** *(`REVIVAL_PLAN.md:30` had it too — harmless, because freezing it properly on the fourth sitting put a do-not-cite banner over exactly this class. That is the freeze paying for itself within hours.)*

**Running tally of one ownership change applied to one surface:** HOMER's sourcing loop · REGINALD's stale Apr Trepp-MF row · CORAL's 16.9% concessions · **CREED's own Mission + mandate**. **Four consumers left pointing at the old owner.** Routed to CARL with the generalisation: *an ownership ruling tells you what the new owner gains; it does not say what happens to the figures the old owner already put into circulation, and it does not notify the holders. The sweep is the mover's job.*

**Files touched:** `evals/` (5 new files), `CLAUDE.md` (always-loaded traps block + Mission fix), `STATUS.md` (mandate fix), `MAINTENANCE.md`, `board_log.tsv`, `SCRATCH.md`, 1 outbound packet (CARL).

**Lessons:**
1. **Surface placement is a correctness property, not a filing decision.** A discipline in a boot-step file fires conditionally; the same words in `CLAUDE.md` body fire always. **CREED had the right lessons in the wrong surface for a full session.**
2. **Write eval cases from real failures, not hypotheticals.** Both v1 cases have a known-correct answer discovered the hard way — the grader can check the rubric against what actually happened.
3. **Diminishing returns are real and worth stating.** Five surveys in, the *file* yield is falling (2 adopts here vs 4 in the first). **The cross-agent-defect yield has not fallen** — every survey has found at least one live interface defect, and this one found a defect inside CREED itself. **The value is in reading OTHER agents' surfaces against your own, not in the file list.**

---

## 2026-07-27 (fourth sitting) — LIQUID/CORAL survey: the coverage map, and a closed episode doc found sitting in CREED's own boot order

**Trigger:** Will directed the same structure survey against **LIQUID** (funding/plumbing; `alerts/` state machine, `CATCHUP_PUNCHLIST.md`, 16 workbook files, dated `archive/workbook_resolved_*` sets) and **CORAL** (Florida; a 10-pillar `COVERAGE.md`, `GRID_PER_METRO.md`, `DATA_SOURCES.md`). Both clean/not-live at survey time.

**Adopted (2):**

| Change | Why |
|---|---|
| **`COVERAGE.md`** (new) — from `CORAL/COVERAGE.md` | **The single most valuable artifact of the four surveys.** 12 lanes: scope · vectors/owner docs · **data vintage** · maturity (🟢🟡🔴) · plus a **blind-spot register that records WHO FOUND each gap** and a build-out backlog. **The gap it exists to prevent is documented: CREED's life-science hole was found by WALTER**, because CREED had no map of its own territory. **Two things it does that `VX.tsv` cannot:** (a) `Last_Updated` is a **touch date, not a data vintage** — all 31 vectors read `2026-07-27` while the underlying prints run from FDIC Q1 to intraday 7/27 tape; (b) it makes *thinness* visible — lane 12 (office pricing/vacancy) is 🔴 with one hard GAP vector and one Q1-stale vector, **sitting underneath the entire valuation argument**, and lane 5 (modifications) is 🔴 with one vector and the registry's only purely-qualitative trigger. |
| **`REVIVAL_PLAN.md` FROZEN + removed from the boot order** — the episode-doc discipline from `LIQUID/CATCHUP_PUNCHLIST.md` | **The survey's finding about CREED itself.** LIQUID froze its punchlist at ~85% and **forked the 2 genuinely-live items UP to live surfaces so they weren't buried in a closed episode.** CREED's `REVIVAL_PLAN.md` is the same species — **and it was still at boot-order step 4**, 165 lines read every wake, describing how to revive an agent that has been operational for four sessions. Frozen with a do-not-cite banner, kept **unedited**, and its two live items forked up: *full legacy migration stays deferred* → `CLAUDE.md` §Guardrails; *the legacy inventory* → already in `CLAUDE.md` §Source Archive + `STATUS.md`. **`COVERAGE.md` takes the vacated boot slot** — a strictly better use of the same read. |

**Declined (4):**
- **LIQUID `alerts/`** (JSON state file + escalation log + watch log, daily poll) — **wrong cadence.** CREED's triggers are **monthly-print** based; a daily poller on a monthly series logs ~30 `ok` lines per data point. **The transferable idea is band TRANSITIONS rather than levels** (LIQUID logs 🟢→🟡→🔴 crossings, not readings) — CREED's `VX_HISTORY.tsv` records levels and my own closeout rule already says *a level is not a trend*. **Noted as a candidate `VX_HISTORY` column, not a subsystem.**
- **LIQUID `IDENTITY.md` / `USER.md` / `STRATEGY.md`** — a trade-facing strategy surface. **CREED's mandate explicitly excludes trade construction** (TERRY owns it).
- **CORAL `GRID_PER_METRO.md`** — a per-metro convergence grid is CORAL's geography-specific edge. **CREED is national**; its metro dimension is the property/metro stress map routed to REGINALD on fire.
- **CORAL `proposals/`** — CREED proposes via packets; a directory for it is overhead at CREED's volume.

**⭐ Cross-agent findings, routed to CORAL:**
1. **CORAL's pillar 4 (Commercial real estate) names `CREED natl` as an owner doc, is marked 🟢, and is its self-declared lowest-priority lane** — live read **7/9**, explicitly skipped in the 7/21 full refresh. **And CREED has no standing feed to CORAL**: the Route Matrix entry is **fire-gated**, nothing has fired, so nothing has been routed since 7/4. **A lane that reads better-covered than it is — the exact failure CORAL's own maturity legend exists to prevent.** Offered a standing monthly FL slice off CREED's whole-Trepp pull (the FL rows arrive free in a document CREED already opens for S1), independent of fire-gating.
2. **An MF figure that changed hands without its consumers being told.** CORAL's pillar 4 carries **"MF concessions 16.9%"** — CREED's 7/4 figure. CREED ceded MF **scoring** to HOMER on 7/27 and **notified HOMER but not the downstream consumers of MF figures already in circulation.** Scope flagged honestly: the ruling named *three* MF things HOMER gains, and concessions is a leasing metric that arguably isn't one — **but the ruling said what HOMER gains and never said what happens to the previous owner's circulating figures.** Same class as the HOMER citation loop found in the third sitting.

**Files touched:** `COVERAGE.md` (new), `REVIVAL_PLAN.md` (frozen banner), `CLAUDE.md` (boot order step 4 + §Guardrails fork-up), `README.md`, `STATUS.md`, `MAINTENANCE.md`, `SCRATCH.md`, `board_log.tsv`, 1 outbound packet (CORAL).

**Lessons:**
1. **An episode doc left in the boot order is a permanent tax on a spawn-on-need agent.** `REVIVAL_PLAN.md` cost every CREED wake for four sessions after its job was done. **The fix isn't deletion — it's freeze + fork the live items UP**, which is LIQUID's pattern and preserves the trail.
2. **A touch date is not a data vintage, and a dashboard that only carries the former will read as fresher than it is.** This is the same failure as `LAST_COMPLETION.md` skipping closeouts, one layer down.
3. **Fire-gated routing creates silent dependencies.** CORAL cites CREED as an owner doc for a lane CREED never pushes to, because nothing has fired. **Fire-gating is right for signals and wrong for context** — hence the standing-feed offer.

---

## 2026-07-27 (third sitting) — REGINALD/HOMER survey: 2 surfaces adopted, and the survey found two cross-agent defects worth more than the files

**Trigger:** Will directed the same structure survey against **REGINALD** (the fleet's most mature agent — per-entity trees for CFG/EGBN/FITB/MTB/PNC/RF/ZION, 11 scripts, 19 workbook files) and **HOMER** (the newest, DAEDALUS-built 7/12). Both clean/not-live at survey time.

**Adopted (2):**

| New file | Why |
|---|---|
| **`registry/THRESHOLDS.tsv`** | From `REGINALD/registry/THRESHOLDS.tsv`. 11 rows transcribing CREED's **existing FROZEN bands** with trigger IDs, sustain windows, recipient chains and source-of-truth refs. **It moves nothing** — bands stay Will-gated. **It found a live cross-agent collision within minutes of existing**, which is the whole argument for it. |
| **`scripts/boot.py`** | From REGINALD's boot orchestrator, **scoped down hard**. Checks mechanics only: workbook staleness, prediction resolve-dates, the **closeout-skip detector** (STATUS vs LAST_COMPLETION mtime — the 7/27 failure, now mechanized), mail lanes, STATUS line cap, git dirt. **Deliberately pulls NO market data** — prices must be live at the moment of use (root rule 4); baking a price into a boot script invites citing a cached level. **Caught an unprocessed inbox item on its first run.** |

**Declined (3), with reasons that are about CREED specifically:**
- **HOMER's `state_vectors/`** — a genuinely excellent pattern (stable citable IDs; a `corrected/` lane preserving superseded versions **unedited** under a banner naming the superseder). **Declined as a tree** because CREED's corrections are already annotated-in-place with git holding the prior text, and a second artifact class for ~4 corrections/session is overhead. **Credited to HOMER and named as the pattern to move toward** if CREED's correction volume rises.
- **HOMER's `docket/CATALYSTS.tsv`** — declined again (as with BROCK's), but the reasoning improved: the value isn't the row count, it's the `what_to_check` + `threshold_signal` columns. **CREED already carries that information per-prediction in `PREDICTIONS.tsv` (`Resolves_On`) and in `SCRATCH.md` §OPEN THREADS.** A third copy would be a drift surface.
- **REGINALD's per-entity trees / `CONVERGENCE_RESCALE.md`** — the entity trees serve a 7-bank coverage universe CREED doesn't have. `CONVERGENCE_RESCALE.md` is itself **FROZEN/superseded** in REGINALD. *(But its concept is pointed: a scoring-scale change written as a reviewed PROPOSAL doc before being pasted into STATUS. CREED changed its own denominator 40→45 inline on 7/27. Worth remembering if CREED rescales again.)*

**⭐ The survey's real output was two cross-agent defects, both routed:**

1. **`REG-T-07` fires on CREED's series, and CREED isn't on its chain.** REGINALD's registry has `OFFICE-CMBS-DQ > 15, sustain 3 → CRE-ACCELERATE`, chain *"REGINALD action / BROCK SHADE info."* CREED's `CREED-T-01a` is the **same series at > 12, sustain 2**. Divergent levels may be deliberate (transmission gate vs recognition gate) — **nobody recorded that they were compared.** Worse: REGINALD's dashboard row *labelled* "Office CMBS DQ" carries **Fitch overall 3.31%**, while CREED's canon is **Trepp office 11.57%**. **Distance-to-fire is 11.7pp or 3.4pp depending which series the trigger is read against.** Not a wrong threshold — **a wrong denominator under the right label.**

2. **⚠️ A citation loop CREED closed itself, the same day it created it.** CREED's 7/27 S5 demotion wrote *"cite `AGENTS/HOMER/STATUS.md` for the MF figure."* **HOMER's STATUS attributes that figure to "(CREED 7/4 pull)"** — in both its dashboard row and its marquee section. **CREED cites HOMER → HOMER cites CREED.** Anyone reading S5 as HOMER-corroborated is reading CREED corroborating CREED. **Fixed in `CLAUDE.md` by separating what the DAEDALUS ruling did not: HOMER owns the SCORING; ownership of the DATA PULL is a distinct assignment that must be stated.** Otherwise the literal rule ("don't publish a second Trepp-MF citation") reads as *CREED stops pulling* — and a handoff ends with neither party pulling. Routed to HOMER with an (a)/(b) choice.

**Files touched:** `registry/THRESHOLDS.tsv` (new), `scripts/boot.py` (new), `CLAUDE.md` (S5 sourcing caveat + route-matrix row), `MAINTENANCE.md`, `board_log.tsv`, `SCRATCH.md`, `workbook/PREDICTIONS.tsv` + `PREDICTIONS_SCOREBOARD.md` (the `PRED-006` re-spec, below), 3 outbound packets (SHADE, HOMER, REGINALD).

**Lessons:**
1. **A structure survey's best output may not be a file.** Two of the three most valuable findings were *interface* defects between agents, visible only because the survey read both sides. Copying `THRESHOLDS.tsv` mattered mainly because **having the registry made the collision expressible.**
2. **Check the other side's sourcing before writing a citation rule.** CREED moved S5 ownership to HOMER without reading where HOMER's number came from — and it came from CREED. **Ownership rulings assign judgment; they do not automatically transfer the data pull.**
3. **Declining is a real output.** Three of five surveyed surfaces were declined, each for a CREED-specific reason. For a Tier-2 spawn-on-need agent an unread file is a recurring boot cost, not a neutral.

---

## 2026-07-27 (second sitting) — Fleet-parity surfaces adopted after a crash exposed the gaps

**Trigger:** Will directed a survey of SHADE's and BROCK's live file structures for anything CREED should integrate. The survey ran immediately after an unclean shutdown in which **CREED had no surface describing what it was mid-way through** — so the gaps were not theoretical, they had just cost something.

**What changed — four surfaces created, and the reasoning for each is a demonstrated CREED failure, not fleet conformity:**

| New file | The failure it answers |
|---|---|
| **`board_log.tsv`** | CREED had consumed **~30 mail items** across four sessions with dispositions recorded **only as prose inside STATUS catch-up sections** — unqueryable, and scrolling off as STATUS grows. Both SHADE (45 rows) and BROCK (68 rows) run this. **Backfilled honestly:** the 12 items from 7/11 forward are logged per-signal; the 17 older WALTER SIGs are marked **PRE-LEDGER provenance and deliberately NOT retrofitted** — reconstructing a disposition I never recorded would manufacture false precision. |
| **`SCRATCH.md`** | The crash. Recovery worked only because modified files happened to be legible on disk. **The file that should have carried the handoff — `LAST_COMPLETION.md` — had skipped two closeouts (7/20, 7/27)** and was still 7/4 vintage, asserting *"CREED has NO own workbook"* four hours after the workbook was built. |
| **`workbook/PREDICTIONS_SCOREBOARD.md`** | CREED registered **10 predictions with self-set confidences on 7/27 and had no calibration surface at all.** BROCK's scoreboard (n=10, Brier 0.216) produced a read that **changed its behaviour** — *"structural calls are under-priced, lean in"* — which is the entire point of keeping score. Created at n=0 deliberately: the discipline has to exist **before** the first resolution, or the first resolution sets the precedent for skipping it. |
| **`MAINTENANCE.md`** | This file. CREED made **three structural changes on 7/27** (workbook built, S8 split 8a/8b, S5 ownership moved to HOMER) with the rationale buried inside a dated catch-up section that will scroll off. |

**Deliberately NOT adopted, and why — the survey's more useful half:**
- **BROCK's `trade/` tree** (per-ticker dirs) — CREED's mandate **explicitly excludes trade construction**. TERRY owns it. Copying this would create a surface CREED is not allowed to fill.
- **BROCK's `docket/CATALYSTS.tsv`** — CREED's catalyst set is **six recurring prints on a known cadence** (Trepp monthly ×2, FDIC quarterly, MBA quarterly, plus named earnings). A separate docket file for six rows is overhead; they live in `SCRATCH.md` §OPEN THREADS with their resolving predictions. **Revisit if the catalyst count passes ~15 or acquires irregular one-off dates.**
- **`NEXUS_BRIEF.md`** — BROCK maintains one because it feeds NEXUS. CREED is not on that route (`CLAUDE.md` §Cross-Agent Route Matrix). Building an unread brief is pure cost.
- **SHADE's `domain/sources/` tree** — CREED's `research/` holds 5 files, all dated by filename. A second tree for 5 files fragments retrieval. **The one piece worth stealing is the convention, not the folder:** SHADE puts a `LAST_REVIEWED:` header + an explicit >60d stale banner on each source doc. Adopt that on `research/*.md` at next refresh.
- **A per-session `MAINTENANCE` write** — BROCK's own warning. Not wired into closeout.

**Files touched:** `board_log.tsv` (new), `SCRATCH.md` (new), `MAINTENANCE.md` (new), `workbook/PREDICTIONS_SCOREBOARD.md` (new), `CLAUDE.md` (boot order + closeout protocol), `STATUS.md`, `archive/STATUS_CATCHUPS_2026-06-28_to_2026-07-04.md` (split out).

**STATUS split — the fifth finding, and the one with a number attached.** CREED's `STATUS.md` had reached **376 lines**, the longest of the three agents surveyed (SHADE 342, BROCK 258) — and it grows by **a full catch-up section per spawn**, with no cap and no archive rule. **BROCK runs a 250-line cap with a mandatory split trigger at 280.** The 6/28 and 7/4 catch-up sections were `git mv`'d to `archive/STATUS_CATCHUPS_2026-06-28_to_2026-07-04.md` — both are fully superseded and independently preserved in `thesis/CHANGELOG.md` and their dated `research/REFRESH_*.md` packs, so **nothing is lost and nothing is deleted.** A soft cap is now written into `CLAUDE.md` §Closeout.

**Boot-impact:** boot order gains `SCRATCH.md` (first, for handoff state) and keeps `STATUS.md` as canonical truth. Closeout gains a `board_log.tsv` row-per-item requirement and the STATUS soft cap. **Net: two cheap steps added, one rot pattern closed.**

**Lessons:**
1. **A file whose *name* promises currency fails differently from an ordinary stale file.** `LAST_COMPLETION.md` skipping a write didn't read as old — it read as **current and wrong**, which is how a 7/4 claim survived two sessions and reached Will. Ordinary rot invites suspicion; this suppresses it.
2. **Fleet parity is not the argument.** Every surface above is justified by a CREED failure with a date on it. The four *rejected* surfaces are the evidence the filter ran — **for a Tier-2 spawn-on-need agent, an unread file is not neutral, it is a recurring boot cost.**
3. **Backfill only what you actually recorded.** The honest `[PRE-LEDGER-BACKFILL]` provenance row is worth more than 17 plausible reconstructed dispositions.
