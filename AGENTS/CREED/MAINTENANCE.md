# CREED Maintenance Log

Reverse-chronological log of **structural** changes to CREED's docs, folders, schema, and boot/closeout protocol. Answers *"why is CREED organized this way, and what decision am I about to re-litigate?"*

**Distinct from:**
- `STATUS.md` — live analytical dashboard (canonical truth).
- `SCRATCH.md` — **ephemeral** per-session handoff (overwritten every closeout; structural notes there do NOT persist — they persist **here**).
- `thesis/CHANGELOG.md` — **analytical** thesis pivots (scores, signals, base case). Structural ≠ analytical: the *decision to split S8* is analytical and lives in CHANGELOG; *creating a workbook to hold the split* is structural and lives here.

> **⚠️ This is a consult-on-structural-work doc, NOT a per-session ritual.** *(Framing adopted verbatim-in-spirit from BROCK, which warns of exactly this bloat and cites SAM at 636 lines as the cautionary tale.)* **Do not wire it into every closeout** — CREED is **Tier-2 spawn-on-need** and process weight is the specific thing that makes a spawn-on-need agent expensive to wake. Touch it only when a session changes CREED's *structure*: a doc/folder created/retired/moved, a schema or protocol amendment, an ownership boundary shift. **Cap: archive to `archive/` if this grows past ~300 lines.**

---





## 2026-08-20 (Phase 3) — `COVERAGE.md` lanes rebuilt; a REFRESH-TRIGGER column added so a vintage stamp cannot rot silently

**All 12 lanes rebuilt.** Lanes 1–4, 6 and 9 carry new data; the rest re-verified and re-dated. The 8/20 known-stale banner was **removed because the rebuild it promised landed** — not because it aged out.

**⭐ STRUCTURAL CHANGE — every lane now carries a `🔄 Refresh trigger` beside its vintage.** The file's whole premise was that `VX.tsv`'s `Last_Updated` is a **touch date, not a data vintage** — and then **its own vintage column rotted for three weeks across two sessions.** A static stamp records when data ARRIVED and says nothing about when it EXPIRES, so it decays silently and a reader cannot distinguish a fresh-by-design lane (lane 4 is a quarter stale *by construction*) from a neglected one (lane 12 is three cycles stale through failure). **The trigger is the part a next session can act on.** *(Design question raised in the Phase plan and decided by CREED, not deferred — a straight refresh would have restored the file to precisely the state it just failed from.)*

**A live finding surfaced DURING the rebuild, and it is the most consequential thing in Phase 3.** Lane 9 was going to be recorded as "7/27 vintage, stale." Attempting to make it real instead: **⚠️ `FORGE/tools/market-data/fetch.py` has `price` and `fred` only — no history subcommand — so `CREED-T-08a`'s 3-month relative CANNOT be produced by the fleet's standard tool.** Computed via a direct `yfinance` call on **both bases**, because the carried figure stated none:

> **VNQ vs SPY 3mo = −0.34pp (total-return) / −0.98pp (price-only)**, window 5/19→8/20. **Negative on both bases, so the sign is robust to basis choice.**
>
> 🔴 **The 7/27 reading was +2.04pp, described as "12pp away AND RECEDING." That direction is now WRONG** — it has moved **~2.4–3.0pp TOWARD** the trigger. **The counter-signal CREED commits to honouring is decaying, not strengthening.** ⚠️ The old figure states **no basis**, so the delta is directionally solid but **not verified like-for-like**; only the new reading is basis-labelled. **S8a HELD at 2** — a weakening counter-signal is still a counter-signal and 9pp is not close.

**Propagated in the same session to avoid manufacturing a fresh contradiction:** `VX-CREED-7.01`, `VX_HISTORY.tsv` (new row), `thesis/THESIS.md` matrix row 8a. **A doc rebuild that updates the MAP and not the VECTOR OF RECORD would have created exactly the defect this sweep exists to remove.**

**Blind-spot register updated: 5 of 7 gaps now found by other agents** (added the `CREED-T-03` unsecured-CRE/C&I scope limit, found by REGINALD via TERRY; and the `CREED-T-02` missing-metric-vector gap, found by CREED's own K5 test — the only one CREED found in its own instrument layer).
## 2026-08-20 (LATE) — `VX-9.03` re-spec: the first CREED vector to change its own instrument

**Will-approved with two riders**, after CREED corrected its own prior claim that the vector carried no band.

**The correction that drove it:** CREED told Will twice that `VX-9.03` had "no band attached." **What it had actually verified was narrower — that no `CREED-T` trigger CITES the vector** (`grep` on `THRESHOLDS.tsv` = 0). **The vector carries bands of its own: >15 / >18 / >20, Will-approved 2026-07-21.** Reported the narrow check as the broad claim. *(`finding_instrument_reports_clean_against_the_wrong_reference` — a clean scan against the wrong referent has no error to notice.)*

**Why the difference mattered enough to re-open the decision:** **a provider swap on a banded vector moves the band state without anyone touching a band.** Moody's 21.0% sits in >20 **RED**; CBRE 18.3% sits in >18 **ORANGE**. The swap would have executed a **RED→ORANGE de-escalation through the instrument** — invisible to any audit that watches band VALUES, which is what every band audit watches.

**Decisions, with reasoning:**
1. **CBRE canonical — chosen for the MECHANISM, not for reachability.** It is the only provider publishing **vacancy and net absorption together**, and absorption is the only thing that distinguished CBRE/JLL's real demand from **C&W's inventory-removal effect** (−360K sf absorption while 33M sf of stock was demolished). **A bare vacancy rate cannot separate those**, and a bare rate is all Moody's ever reached CREED with. `VX-9.03` feeds **S7**, whose trigger requires *direct tenant-demand impairment* — **a level elevated for three years is a stock; absorption answers the question the vector exists to ask.**
2. **Bands NOT re-based — refused at n=1.** Clean overlap is ONE quarter (Moody's Q1 21.0 vs CBRE Q1 18.6 = 2.4pp). **A 2.4–2.7pp spread at n=1 could be a stable offset or one quarter's noise.** Re-base at 3–4 quarters, as a separate Will-gated decision. **CREED applied its own base-rate rule against its own convenience** — re-basing now would have been the comfortable move.
3. **Bands marked UNCALIBRATED-FOR-THIS-PROVIDER rather than edited.** They stay Will-frozen and untouched; the state cell is **indicative only** until re-based. **Grade the leg on absorption direction meanwhile.**
4. **RIDER 1 (Will's): the RED→ORANGE transition is recorded EVERYWHERE as a BASIS CHANGE, never a de-escalation** — `VX_HISTORY` carries a dedicated `BASIS-CHANGE` row that also marks where the Moody's series ends and the CBRE series begins, THESIS S7 carries a basis-change guard, and **S7 stays at 2 on the evidence, not on the band state.**
5. **RIDER 2 (Will's): Moody's and C&W are pulled every quarter as CONTEXT ROWS, not dropped.** **The overlap series that funds the future re-base only exists if the old provider keeps getting recorded** — this folds option C's one virtue in and makes the re-base a lookup instead of an archaeology project.

**Pre-existing defect fixed in passing, and deliberately not claimed as a win:** the state cell read **ORANGE while the value was Moody's 21.0%** — a >20 **RED**-band number — since at least 7/27. **The vector under-stated its own band for three cycles and no check caught it** (`creed_selfcheck` reads fire-state and counts, not band-vs-value). Today's swap made ORANGE correct **by accident**; the coincidence is recorded rather than presented as the fix, and the cell now says *why* it is ORANGE so the next reader can check it.

> **Candidate for the next guard extension:** a **band-vs-value predicate** — does each vector's state cell agree with its own bands and current value? It is mechanical, CREED-scoped, and would have caught a three-cycle-old defect that four staleness sweeps walked past.

## 2026-08-20 (AFTERNOON) — a dead pointer, a re-spec proposal, a third STATUS split, and two Will-frozen-row defects

**Session type:** second session this day, fresh context. Will-directed: fix the COVERAGE lane-9 dead pointer, resolve `VX-CREED-9.03`.

**Created:**
- **`scripts/s8a_relative.py`** — the S8a recompute recipe COVERAGE lane 9 had *promised but never contained*. Prints **series + noise band + base rate** alongside the point, and `--end YYYY-MM-DD` re-derives any past reading. **Deliberately not a FORGE tool:** `fetch.py` has `price`/`fred` only, and this is a CREED-specific instrument.
- **`archive/STATUS_CATCHUPS_2026-08-13.md`** — third enforcement of the 320-line split trigger. ⚠️ **Its banner flags two claims inside the archived text that were refuted on 8/20** (the "not published" July mat-adj DQ, and "no trigger fired") so an archive reader is not misled by correctly-dated-but-false statements.

**Structural decisions, with reasoning:**
1. **`VX-9.03` NOT FROZEN, against the standing escalation's own menu.** The 7/27→8/20 escalation said *"locate a print or propose a freeze."* **Neither happened, and the menu was the problem** — it presumed the vector's fate turned on the specified PROVIDER. Moody's Q2 is **public-but-unreachable** (403), but **three other providers published Q2 and all show the direction reversed.** Freezing would have locked in a stale record-high anchor that was **pointing the wrong way.** *(A closed option menu that omits the right answer reads as a forced choice — `finding_option_menu_omitting_the_owners_choice_reads_as_silence`.)*
2. **Provider re-spec PROPOSED, not executed.** `VX-9.03` carries no band, so nothing is Will-frozen — **but choosing a vector's canonical provider is a methodology call and belongs to Will.**
3. **`CREED-T-08a`'s wrong `source_of_truth` FLAGGED, not fixed.** It names `VX-CREED-8.01` (*CRE Modification Exhaustion*, S4) instead of `VX-CREED-7.01`. **A non-band field of a Will-frozen row, outside the 8/20 ruling's scope.** The correct pointer went into the row's dated annotation so no reader is misled meanwhile. **The band, op, value, sustain window and 10-column width were all verified unchanged** (WALTER's scanner parses the column count).
4. **Ruling #5 executed with CREED's wording, not the ruling's suggested wording.** PROME's suggested stamp embedded the **−0.34pp / "~2.4–3.0pp toward the trigger"** figures that this same session **withdrew**. The ruling said *"Your wording; the requirement is that no reader can consume the refuted direction as current."* **Requirement met with corrected numbers — following the suggested text literally would have date-stamped a figure into a frozen row hours after it was superseded.**

**The finding worth carrying (`KB-CREED-020`):** the 8/20-AM session **did** run a robustness check on S8a — *"negative on BOTH bases, so the sign is robust to basis choice"* — and it **passed and was true.** It was not the binding constraint: **the window, untested, was the larger sensitivity and flipped the sign.** **A robustness check certifies its own scope, exactly like a green guard.** Recorded in SCRATCH §"what the guard cannot see."

**Known state carried forward:** STATUS is **323 lines, 3 over the 320 trigger, with the split already executed this session** — overage came from the header/BOTTOM-LINE rewrite afterward, the same shape as the documented 7/27 precedent (321). **Named remedy: the next catch-up archives the 8/20 MORNING window.** Recorded rather than resolved by raising the number.

## 2026-08-20 (Phase 2) — `scripts/creed_selfcheck.py` built; first CREED-owned tooling

**NEW: `AGENTS/CREED/scripts/creed_selfcheck.py`** (and `scripts/`, CREED's first script directory). Wired into §Closeout Protocol as **step 8b**. ~20ms, exit 0/1.

**Why, precisely:** the 8/20 sweep found 14 defects and **the existing fleet tools were structurally incapable of seeing the worst two.** `consumer_check.py` scans superseded **VALUES**; `#4` was a superseded **STATE** and `#8`–`#13` were superseded **COUNTS**. A clean `consumer_check --self` therefore certified nothing about either — **the scan was correct and its referent was wrong.**

**Two checks, both file-level and enumerable by design:**
1. **Fired-trigger cross-surface consistency** — a trigger FIRED in `registry/CREED_T_FIRED_LOG.tsv` must carry a fire marker on every surface that names it (CORE: `THRESHOLDS.tsv`, `STATUS.md`, `THESIS.md` — always; CONTEXT: `VX.tsv`, `FLOW.tsv`, `COVERAGE.md` — only if they name it). **This is the K5 defect class mechanised.**
2. **Asserted counts vs actual** — VX / KB / PREDICTIONS-open / workbook-file counts claimed in prose, diffed against reality.

⚠️ **Deliberately NOT a general claim-detector.** `claim_check.py` measured 13 decision files → 1 flag vs. the whole tree → 131 flags; a prose-wide staleness scanner would ship alert fatigue and be ignored. **Both checks are file-level, so a flag is always actionable and false positives are ~0 by construction.**

**VALIDATED IN BOTH DIRECTIONS before shipping** — a guard proven only against a broken tree is not proven. Against the live tree: **exit 1, 7 findings.** Against a scratch copy with the corrections applied: **exit 0, CLEAN.** *(A guard that cannot go green is indistinguishable from one that is stuck on red — cf. `finding_instrument_reports_clean_against_the_wrong_reference`, inverted.)*

**On its first run it found a defect the manual sweep missed:** `COVERAGE.md` asserts *"the 31-vector workbook"* — a **15th** count-drift instance not in the catalogued 14. That is the argument for the tool in one line.

⚠️ **Known scope limits, recorded so a future session does not over-trust a green:** check ② matches **known prose phrasings only** (`ASSERTIONS` list) — a new phrasing is invisible, so **extend `ASSERTIONS` in the same edit that introduces one.** Check ① is **file-level, not line-level**: a file containing the word FIRED *anywhere* passes for that trigger, so it detects total absence, not a stale sentence inside an otherwise-updated file.

**⚠️ CHECK 3 ADDED THE SAME DAY, ON A LIVE OBSERVATION — and the observation is the useful part.** Phase 4's fix to `COVERAGE.md` added a *"KNOWN-STALE, rebuild pending"* banner. That banner contains the word **FIRED**, so **check 1 went GREEN on a file whose 12 lanes were still entirely pre-fire.** The check behaved exactly per its documented file-level scope — **and that is precisely the problem: a banner must not be able to silence the guard.** Fixed within minutes by adding **check 3 (open-staleness banners)**, which flags 🟠 while any known-stale banner stands and **clears only when the banner is REMOVED, not when it is written.** `finding_banner_is_a_warning_not_a_fix` says pair every banner with a dated rewrite trigger — **this IS that pairing, mechanised**, and it converts a banner from a silencer into tracked debt.

> **The transferable bit: a documented limitation is not a mitigated one.** This exact limit was written into the file's own docstring *before* it shipped, and it still produced a false green inside the hour. **Writing the caveat down did nothing; the check did.**

⚠️ **Process-weight discipline:** it runs at **CLOSEOUT, not boot.** CREED is Tier-2 spawn-on-need and boot cost is the thing that makes such an agent expensive to wake. **20ms and CREED-scoped — if it ever grows slow or starts reading other agents' files, cut it back.**
## 2026-08-20 (late) — ALWAYS-LOADED traps block: #3 REWRITTEN, #6 and #7 promoted (5 → 7)

**Amends the same-day entry below, which explicitly recorded the opposite decision on #3 and was wrong.**

**1. Trap #3 REWRITTEN, not annotated.** It read *"Trepp PDFs are paywalled ⇒ PRIMARY-CITED, not PRIMARY-READ."* The earlier entry today left it standing, reasoning "the general warning still holds and the exception is month-scoped." **On re-read that was the wrong call and the reason is this session's own headline finding:** an always-loaded instruction saying *you cannot read this source* **is the unfetched-is-not-unavailable defect encoded where every future session sees it, at the highest-authority surface CREED has.** It would have talked the next session out of the exact command that fired `CREED-T-02` and answered W1. Now month-scoped: **check `AGENTS/WALTER/sources/` before assuming either way.**

**2. Traps #6 and #7 PROMOTED from `SCRATCH.md` (where they were 11 and 12).** ⚠️ **The two files number differently — SCRATCH 11 → CLAUDE.md 6, SCRATCH 12 → CLAUDE.md 7** — mapping recorded in SCRATCH's sync note. Both meet the block's own stated criterion (*fires while writing a number*, and *actually cost CREED*): #6 (a share is not a trend when its denominator moves) nearly sent a backwards shape verdict fleet-wide as settled; #7 ("not published" usually means "not fetched") produced a 5-week-late answer to a formally-registered question **and** a mis-priced prediction confidence.

⚠️ **Promotion is not free and this block must stay curated.** It is always-loaded, so every addition is paid at every spawn of a Tier-2 agent whose whole design goal is being cheap to wake. **A trap earns a place here only by having actually bitten CREED while writing a number** — that criterion is now written into the block's header. **Do not promote on the strength of a good idea; promote on the strength of a scar.**

⚠️ **Known interaction, recorded not deferred — this WORSENS the eval-suite contamination defect** (`SCRATCH.md` open thread 12). The suite VOIDs a case when a skip-boot session names an entity from the loaded traps; the block now names **Trepp, HOMER and Connect-CRE** in addition to ARI and MBA. **Net assessment: still worth it** — the traps' job is to protect live analysis, and the eval's contamination rule is the thing that is mis-specified (it cannot distinguish "leaked from live rails" from "correctly cited the text the eval itself loaded"). **The fix belongs in the rubric, not by keeping load-bearing traps out of the always-loaded surface.** Flagged for whoever next touches the suite.
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


---

## 2026-08-27 — the boot-time threshold scan, built at last (`scripts/threshold_scan.py`, boot step 4c)

**Structural change:** one new script, one new boot step. **The oldest un-built item on CREED's work order** — carried unbuilt through three sessions while being named each time as the highest-priority guard.

**What it closes.** `CREED-T-02`'s root cause. On 2026-08-13 CREED wrote **"66% of $6.0B"** into its own workbook — the T-02 metric against a frozen band of **50** — **and did not grade it**; the fire was effective at the June print and went unnoticed **~6 weeks**. The FORUM-5 K5 test **falsified the intuitive explanation**: dark cadence was not the defect. **CREED was awake, holding the number, with the band written down. No boot step read the registry, so nothing ever compared the two.**

**Verified against the real event before shipping, on BOTH wirings** — because "it would have caught it" is a claim, and the flattering version of that claim is the one nobody checks:
- **today's wiring** → `CREED-T-02` reports **🔴🔴 TRIPPED**;
- **the actual 2026-08-13 wiring**, where `VX-CREED-3.04` did not yet exist → reports **UNTRIPPABLE BY CONSTRUCTION**, which is the diagnosis that would have prompted building `3.04` six weeks earlier.
**It catches the event by two different lines, and the second is the more useful one.**

**Design decisions worth keeping (each is a refusal, not a feature):**
1. **It never prints "all clear."** Only rows with **both** a numeric band and a metric vector are comparable — a minority — so the summary states coverage as a fraction and every unscannable row is **enumerated by name and reason on every run.** Silence about them was the failure mode.
2. **`⛔ BLOCKED` ≠ `✅ CLEAR`.** Rows whose comparison is not a valid verdict on the registered basis (`T-03`'s basis defect, `T-08a`'s undeclared basis) are labelled BLOCKED — **but their arithmetic is still printed.** A block downgrades a verdict; it never hides a number. **A hardcoded block that silently swallowed a real crossing would reproduce the exact class the script exists to catch**, so each block entry carries the ruling that deletes it.
3. **It is not an adjudicator.** TRIPPED means *go grade it at primary*. Adjudication stays a CREED act recorded in `CREED_T_FIRED_LOG.tsv`; the script reads state and writes none.
4. **It prints its own parse provenance.** The value cells are prose, not fields, so it shows each parsed number in context — a re-worded cell can silently change what gets extracted, and a wrong-but-plausible parse is this desk's self-declared dominant failure.
5. **No count is hardcoded in the docstring.** The counts move whenever a vector or trigger is added. *(Same-day precedent: README asserted "14 comment lines" for `THRESHOLDS.tsv` when the real count was 25 — a stale number sitting inside the warning against hardcoding one.)*

🔴 **LIVE FINDING FROM THE FIRST RUN — `CREED-T-06` and `CREED-T-06b` carry numeric bands (`>30`, `>=1`) with NO metric vector.** That is the **identical K5 shape, n=2, and it had never been counted** — `README` said "only 5 rows are numerically scannable" without noting that two of the remaining six are *banded but uninstrumented*, which is a different and worse state than *qualitative by design*. **Flagged, deliberately NOT adjudicated here:** whether these two want a vector, or want their numeric bar rewritten as an honestly-qualitative one, is a judgment call — and a band change is Will-gated regardless. Carried to `SCRATCH.md`. *(This is also the first return on SCRATCH deferred item 8 — "evaluate the six non-scannable triggers, never swept; assume they are worse than the scanned ones." They were.)*

⚠️ **The guard's own v1 failed on its first run, in its most load-bearing direction.** A loose `VX-CREED-[\d.]+` regex swallowed the range shorthand `VX-CREED-10.01..10.05` whole and **reported a phantom pointer defect against `CREED-T-08b`** whose five vectors are all present and fine. **A check built to find fabricated referents fabricated one.** Caught only by running it before commit. `[[finding_test_the_guard_not_just_the_guarded]]` — the memory predicts exactly this, and predicting it is not the same as being immune to it.

**Files touched:** `scripts/threshold_scan.py` (new), `CLAUDE.md` (boot step 4c), `README.md` (scripts index), `MAINTENANCE.md`, `SCRATCH.md`.
