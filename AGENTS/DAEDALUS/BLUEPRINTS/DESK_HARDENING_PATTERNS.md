# DESK HARDENING PATTERNS — rules extracted from one desk's hardening day (fleet build standard)

**Owner:** DAEDALUS · **Created:** 2026-09-04 · **Commission:** PROME packet `AGENTS/DAEDALUS/inbox/processed/2026-09-04_from-PROME_Will-directed-extract-VIOLETs-9-4-hardening-into-fleet-blueprint-patterns-six-named.md` (Will, verbatim *"how do we keep VIOLETS approach? Maybe you can tell/direct DAEDALUS"*) · **Status:** RULE FORM, adopted on PROME consume; nothing here moves a threshold or a route. **Scope:** binds NEW desk-local checks and handoff surfaces at build time and existing ones at next material edit, the same scope line as `CHECK_STANDARD.md`. **Self-inclusion (CHECK_STANDARD §10):** DAEDALUS's own surfaces are IN scope.

**Source of record:** VIOLET's 2026-09-04 day is eight commits. The commission packet names three (`1dda98e31` · `ec5d05b69` · `ef3e0be9c`); PROME's doorbell added `95ffa70bc`; this file also reads **`717c8f9a0` (15:28, external review, KB-VIO-242), which neither listed and which corrects two of the mechanisms the others built** — the strongest evidence in this file. Not read here: `756bf3397` (08:47 FT-10 grade), `bc6017fd2` (10:08 SIGNAL_INTAKE re-arm), `f1c8a5f32` (13:42 empty-inbox lesson) — desk-state commits, no new mechanism. The docstrings in `AGENTS/VIOLET/scripts/` are the canon for each mechanism; this file is the index and the RULE. Cite them, do not restate them.

**How to read a rule:** *RULE* (what a desk must do) → *proven on* (the artifact) → *what it removed* (the measured failure) → *cannot see* (the declared blind spot, always present — PAT-084: no guard announces its own scope, so this file does).

---

## H-1. A write-back ORDERING contract is computed at closeout, never remembered

**RULE.** Every handoff surface a *consumer* reads in place of STATUS (the `SCRATCH` · `LAST_COMPLETION` · `NEXUS_BRIEF` class, and any file another desk's boot names as its read of you) has a mechanical ordering check at closeout: `effective_vintage(surface) ≥ effective_vintage(STATUS)`, where a file dirty in the working tree counts as *now* and a clean file counts as its last commit time. The check is BLOCKING in the closeout guard and ADVISORY at boot (VIOLET `closeout_guard.py` docstring: *boot warns; closeout blocks*). If the closeout rule is already written as an arithmetic comparison, it is the cheapest mechanization on the desk — build that one first.

**Proven on:** `AGENTS/VIOLET/scripts/writeback_order_check.py` + `closeout_guard.py`, commit `1dda98e31`. The rule had sat as a sentence in `AGENTS/VIOLET/CLAUDE.md:53` (NEXUS Amendment 10, *"the brief's commit timestamp ≥ the session's last STATUS commit timestamp"*) for 31 days.

**What it removed:** a 10:0x crash left three surfaces 79 minutes behind STATUS with four boot checks green (`boot.py` 14/14, `ledger_staleness` rc 0, `corrections_boot_check` rc 0, `closeout_guard` red only on a pre-existing contract). A tail step done from memory fails exactly in the population where the handoff matters most: crash, interrupt, context exhaustion. PROME's own 9/4 morning session ended the same way (`PROME/SCRATCH.md:48`: *"crash after the last desk commit at 11:20; no closeout"*).

**Cannot see:** content. A fresh `As of:` over a stale body passes (`[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]`); the check catches the surface LEFT BEHIND, not the surface REFRESHED BADLY. Commit `717c8f9a0` finding #3 landed that exact limitation on the author the same day. The two provenance stamps that ARE checkable (cited STATUS hash = current STATUS head or a verified `same-commit` marker; `As-of` stamp not later than its own commit) were mechanized in the same commit and belong in the same check — **and that checker shipped with three fail-open holes (`f4950fa8b` #4): a citation passed if it matched the brief's own commit even when that commit never touched STATUS; a missing stamp silently skipped validation; and the whole check RETURNED EARLY when the brief was dirty, which at closeout it always is — correct, wired, and inert on its own path. Test a closeout check IN the dirty condition it runs in (`[[finding_guard_correctness_and_wiring_are_independent]]`, PAT-131).**

**Prior art (§13 line):** `[[finding_mechanize_the_cap_not_the_ritual]]` (instance (d) = this crash) · PAT-065 (a principle written as a boot step is not always-loaded) · PAT-055.

## H-2. A twin check REFUSES to nominate a winner

**RULE.** Where a machine-readable source of truth has a human-readable twin (`CATALYSTS.tsv` ⇄ `CALENDAR.md`; `DOCKET.tsv` ⇄ the SCRATCH catalyst block; any TSV ⇄ its rendered table), the consistency check reports divergence and prints, beside each divergent row, the source and the `date_class` / basis token of the record. It says CATALYSTS should win ONLY when that row is `CONFIRMED` with a named primary; a `MODELED` / `ESTIMATED` / `DERIVED` / unlabelled row is declared *not a tiebreaker* and the operator is sent to the primary. Recency is never a tiebreaker. The class token is read from an explicit field, never from prose, because the supersession note contains the superseded token. The check runs in BOTH directions with strict 1:1 claiming and flags past-dated rows under a forward heading on BOTH surfaces.

**Proven on:** `AGENTS/VIOLET/scripts/twin_check.py`, commit `ec5d05b69` (v1) and `717c8f9a0` (bidirectional v2; the review found v1 green over 8-vs-7 inconsistent twins with three fired August rows under ACTIVE FORWARD for 14 days).

**What it removed:** the MU earnings date, ~9/29 (1 day off, `ESTIMATED`) was overwritten by VULCAN's ~9/22 (8 days off, `MODELED`) twice as a "twin fix"; truth 9/30, verified at the Micron release. A check that asks only WHETHER two surfaces agree converts every disagreement into propagation of whichever was touched last (`[[finding_owner_of_record_means_authoritative_not_correct]]`).

**Cannot see:** two twins that agree and are both wrong. Agreement is not correctness in either direction; the primary is the only referee.

**Fleet instances:** every desk carrying `CALENDAR.md` + `CATALYSTS.tsv`; PROME's DOCKET ⇄ SCRATCH view is already generated by `scripts/docket_view.py`, whose `--check` mode is the same rule (report, never rewrite).

**Prior art:** `[[finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it]]` (v1's date_class-from-prose defect) · PAT-059 (recognizer matches FORM, not keyword presence) · `[[finding_verify_recommended_fix_not_just_finding]]` (the v2 fix of one direction left the same defect in the other).

## H-3. Instrument integrity is checked AT THE MOMENT OF USE, and the verdict is recorded beside the claim

**RULE.** A mirror a grade reads (yfinance/FRED/exchange copies of a publisher's series) is checked VALUE-BY-VALUE against the publisher of record for the dates the grade uses, at the moment the value is consumed; the one-line verdict is pasted beside the claim. Bar counts are necessary, never sufficient: a gapped series announces itself, a wrong one does not. The check FAILS CLOSED (rc 2) on an unreachable publisher: an unreachable source is an unknown, and an unknown must not be quoted as agreement. It is deliberately NOT boot-wired when the defect class heals: a check run before the work does not bound the work, and a later re-run can never bound a grade computed during the gap.

**Proven on:** `AGENTS/VIOLET/scripts/skew_integrity.py`, commit `ec5d05b69`; standing rule on `AGENTS/VIOLET/CANARY_MAP.md:48` (KB-VIO-241); base rate RED's 253-session read (KB-VIO-236).

**What it removed:** `^SKEW` mirror 2/253 sessions defective (omitted bar 2026-08-28; wrong value 2025-12-24, CBOE 161.30 vs yfinance 160.53). The bar-count remedy first proposed was blind to the second mode. The 8/28 hole had HEALED by the 9/4 run: same query, three readings, two different mode sets.

**Cannot see:** first-published values. Neither endpoint retains vintages; a vintage question is `UNKNOWN`, not `clean`. It bounds THIS read at THIS instant, nothing earlier.

**Fleet instances:** every mirror a registered gate reads (HY OAS, DGS10, `^SKEW`, USD/JPY basis, MOVE). Pairs with `sweeps/GATE_BASIS_SWEEP.md` §3 (negative control on the retrieval path) and CHECK_STANDARD §8 (fallback visible in output, artifact, rc).

**Prior art:** `[[finding_instrument_cadence_cannot_resolve_the_claims_window]]` · PAT-106 (a fallback invisible in the output is a silent substitution) · PAT-107 (enumerating an instrument's clock is not establishing it).

## H-4. A remedy carried as PROSE for two sessions is a defect of the class it describes — the "prose remedy → code" census

**RULE.** A fix that is already specified on a surface (a CANARY_MAP contract, a SCRATCH "next session" line, a STATUS caveat, a peer's packet) and carried ≥2 sessions is treated as a tool defect in its own right, not as a queue item: the diagnosis is done and the remaining cost is the hour of typing. Each desk's closeout, and the fleet sweep registered below, asks not *"is there a rule?"* but *"is there a line of code that computes it?"* The census is agent-judged off a mechanical candidate list (playbook `sweeps/PROSE_REMEDY_SWEEP.md`; registry row `Prose-Remedy Census`).

**Proven on:** VIOLET `SCRATCH.md:78` + KB-VIO-240 (*"five queued tool defects built — none needed new analysis"*), commit `ec5d05b69`: COT staleness spec written in full on CANARY_MAP; holiday-table gap in SCRATCH; phantom `move.py` leg on STATUS *with its KB id*; both `^SKEW` modes in RED's packet. Carried between 2 days and 7 weeks.

**What it removed:** a holiday-blind trading-day count that called Labor Day a session (the dangerous direction for a sustain counter); a RESOLVED gate printed as a live threshold at every boot for ~7 weeks; a COT rule that fired a guaranteed false DARK every Friday; both SKEW modes.

**Cannot see:** whether the typed remedy is CORRECT. `717c8f9a0` finding #1: the COT remedy typed from CANARY_MAP encoded a false invariant (a fixed Tue/Fri lag that CFTC holidays move at both ends) and was certified "zero free parameters". Typing the prose is the cheap half; H-6 governs the other half.

**Prior art:** `[[finding_dated_carry_item_has_no_expiry_check]]` (a carried remedy self-evaluates never) · `[[finding_mechanize_the_cap_not_the_ritual]]` · PAT-081 (approved-but-unimplemented is not a neutral parked state: the superseded logic keeps firing while the fix sits).

## H-5. A same-day read gets a pre-registration card at proportionate cost

**RULE.** Before reading a tape whose fundamental surprise is already known (a print graded the same session: LABOR NFP, SAM MOF, BRENT COT, VIOLET vol reaction), the desk freezes a short card: baselines with basis, outcomes A–D with NUMERIC bands, the noise floor declared FIRST and every directional band defined strictly outside it, the author's own prior NAMED so it is held to the same evidence bar, and no causal attribution from one session. Grading the card records the card's own defects rather than resolving them quietly. Full registration canon is `FORGE/PREDICTION_DISCIPLINE.md`; this rule only sets the proportionate-cost floor for the same-day case.

**Proven on:** `AGENTS/VIOLET/research/2026-09-04_nfp_vol_reaction_prereg.md` (authored ~09:1x, before the open) graded in commit `ef3e0be9c`.

**What it removed:** narrating a known surprise into the interpretation. The grade found the card's own defect (bands B and D overlapped; the outcome landed in the overlap) and wrote the resolution down as a rule rather than choosing post hoc.

**Cannot see:** a wrong noise floor. The floor is itself a claim; state its basis (VIOLET used 0.3 VIX points without a stated basis, and the grade said so).

**Prior art:** `[[finding_prereg_verdict_boundary_must_be_a_number]]` · `[[finding_confounds_align_with_the_prior_you_brought]]` · PAT-053 (frozen-frame execute-only print grading; extended 9/4 with the same-day form).

## H-6. Falsify the guard before shipping it, and know what the falsification proved

**RULE.** A new or widened check ships only after (a) its selftest REPRODUCES A KNOWN DEFECT — a real prior instance from the desk's own record, to the cent, never a fixture shaped to pass; (b) its clean line was watched on a clean case (CHECK_STANDARD §3); (c) its exit code was read BARE, never through a pipe (`cmd | tail; echo $?` reports tail's rc; use `${PIPESTATUS[0]}` or `set -o pipefail`, CHECK_STANDARD §14(b)); and (d) the PREMISE the check encodes was verified at the publisher, because a selftest proves the cases the author enumerated and the enumeration comes from the same head that wrote the model. A guard whose selftest has never returned red has proven nothing; a guard whose selftest is 24/24 has proven 24 cases.

**Proven on:** KB-VIO-241 (`skew_integrity.py` reproduced RED's 2025-12-24 disagreement, +0.770001, before it was trusted); `twin_check.py` v1 failed its own first run and was fixed pre-commit (`ec5d05b69`); VIOLET `SCRATCH.md:80` (two guards misread as green through a pipe). **And the counter-instance, `717c8f9a0` finding #1:** `canary_staleness.py` passed a 14-check selftest in both directions and still encoded a false invariant (CFTC federal holidays move both the report and release dates) that the author never checked at CFTC's own schedule page. Two of the original 14 assertions were the false invariant itself. **And the holiday-table correction was wrong too (`f4950fa8b`, 17:28, KB-VIO-243): the asserted Monday-holiday slip is contradicted by CFTC's own history AND by four months of Tuesday report dates sitting in the `COT_VIX.tsv` the guard opens on every run.** Three versions, all green on their own selftests, test count rising 14 → 24 while the premise got more wrong. v4 removed every calendar assumption: cadence + grace derived from the ledger's observed dates (0 = nothing owed · 1 = PENDING · 2+ = DARK). **Rule (e): when a guard models an external schedule, the FIRST test is against the observed history in the data it reads, never against the model — and given a precise rule you keep getting wrong versus a loose rule derived from data, the loose one wins on a guard whose miss gets LOUDER over time.**

**What it removed:** guards certifying health they never checked (PAT-074 family, n≥6 fleet-wide), and the specific silent form where a correct selftest certifies a wrong premise.

**Cannot see:** the case nobody imagined. That is why (d) is at the publisher, not in the fixture set, and why the fleet before/after diff ships in the commit body (`[[finding_test_the_guard_not_just_the_guarded]]` n+2: the diff proves the cases the selftest did not).

**Prior art:** PAT-074 · PAT-083 (a check that cannot fail) · `[[finding_crosscheck_with_free_parameter_validates_nothing]]` · `[[finding_guard_correctness_and_wiring_are_independent]]` (correctness and wiring are tested SEPARATELY; `1dda98e31` did both).

## H-7 (coordination layer, recorded against PROME by PROME's own ask). A tool that surfaces an operator decision names its DELIVERY artifact, and the artifact carries the SAME state as the desk

**RULE.** When a desk-local tool's output is *"this is the operator's call"* (VIOLET `cheap_tail.py`: OPEN 4/4 ⇒ *route PROME → TERRY → Will*), the desk names the packet path that carries it, and the packet's state token agrees with the desk's own STATUS. "Surfaced" means the packet exists AND says so.

**Verified at the artifacts (this corrects the commission's wording):** a packet to PROME DOES exist — `PROME/inbox/processed/2026-09-02_from-VIOLET_31-drained-fomc-letter-skew-basis.md:8` — but its `WILL_NEEDS` line reads **"Nothing"** and calls the window *"recorded, deliberately not actioned, and not a recommendation"*, while `AGENTS/VIOLET/STATUS.md:24` and `:137` call the same window *"a live operator-decision surface, routed PROME → TERRY → Will."* No packet to TERRY exists (TERRY inbox, root and processed, searched by name). So the failure is not "no artifact": it is an artifact that reached the coordinator carrying the opposite token from the desk's STATUS, which a completion-contract reader is right to file as nothing-owed. PROME put the window in front of Will 9/4 15:2x; the rule is what would have made that unnecessary.

**Prior art:** `[[finding_record_of_an_action_is_not_the_action]]` · `[[finding_summary_section_merges_what_the_body_separates]]` (the WILL_NEEDS summary merged what the STATUS body separated) · STRICT_TEXT rule on ACTION/ASK lines.

---

## H-8 (RULED 2026-09-07 as part of the harvest batch, Will verbatim "Go ahead with the batch" — desk-wide write mode; canon = `READ_CAP.md` rule 19; PROME closes WQ-179 against it). Hot STATUS carries tokens + pointer; grade narrative goes cold on the day (WQ-179 rec (c))

> ⛔ **Pending Will's word on WQ-179** (`PROME/SCRATCH.md` "Pending Will" list, 9/4; origin `PROME/inbox/2026-09-04_from-LABOR_ESCALATION-read-cap-is-now-the-binding-constraint-BD-25-budget-gone-in-2-days.md`: a 9/2 hot/cold split consumed in 2 days, 4 rotations in one session). **Do not cite as canon.** If ruled: a print-driven desk writes the grade NARRATIVE straight to its cold surface (`STATUS_DETAIL` class) at the moment of grading; the hot file gains only the state token and a pointer. The fleet template lands here as H-8 on the ruling; until then this block is the draft PROME asked for.

---

## Not adopted from the commission, and why (deliverable ③, mirrored in the one-line to PROME)

| Item | Disposition | Why |
|---|---|---|
| Pattern 6 as "selftest must reproduce a known defect" alone | **ADOPTED WITH AMENDMENT (H-6 d)** | `717c8f9a0` shows the reproduction requirement satisfied and the guard still wrong; the premise leg is the half the commission's commit list could not see. |
| Seventh pattern as "no packet exists" | **ADOPTED WITH CORRECTION (H-7)** | The 9/2 packet exists; its `WILL_NEEDS: Nothing` contradicts STATUS. The rule is about state agreement across the hop, not existence. |
| A new `STATE_VOCABULARY` class for mechanization state | **DECLINED** | The census verdicts reuse existing tokens (`BUILT-UNWIRED` from CHECKS.tsv; `SEARCH-NOT-FOUND`/`VERIFIED` Class 13). A new class is a ruling; propose only if run #1 finds the tokens insufficient. |
| Mechanizing the census grep as a fleet script | **DECLINED for now** | Base-rated 9/4 (CHECK_STANDARD §12): 55 candidate lines / 22 desks, majority false on the exemplars read; positive control 3/3 on VIOLET. That precision belongs in a playbook run by a reader, not in a boot-wired check that would train desks to ignore it. |
| Restating VIOLET docstrings | **DECLINED** (per the commission) | Docstrings are the canon; this file cites. |
