# TRADE.md — OBLIGATION INVENTORY (P2, tranches 1–2 in progress)

**Started 2026-09-08.** DAEDALUS architecture review P2 / ACTION 13. **One row per binding clause: `clause · from · to · reached by`.** ⛔ **A clause archived without a reader is lost operationally** — so this is built BEFORE any clause moves, not after.

> ## ⛔ THE RULE THIS FILE IS BUILT UNDER
> **`reached by` is a VERIFIED path, never a filled cell.** A pointer records *intended* access; only opening the named step establishes that the obligation is reachable. Every row below was checked by reading the step, not by grepping the filename.
>
> ★ **AND THE CHECK EARNED ITS KEEP ON THE FIRST PASS.** `grep -rl "TRADE.md" scripts/` returns **`boot.py`, `render_calendar.py`, `cot_grade.py`** — and **all three mention it ONLY IN COMMENTS.** No code path reads the file. A `reached-by` column filled from that grep would have recorded three readers that do not exist, with the authority of an audit. `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`

## 🔴 THE FINDING — STATED MORE CAREFULLY THAN IN TRANCHE 1

Of the binding clauses in `TRADE.md`, only the EXECUTION LOG and the two-clock header have a reader that fires without a precondition. Everything else is reached through boot step 1's conditional read — *"read `TRADE.md` … **if** the task touches positions/trades."*

> ⛔ **CORRECTED 2026-09-08 — "NO UNCONDITIONAL READER" IS NOT "NO ADEQUATE READER", AND TRANCHE 1 CONFLATED THEM.** A pre-fill disclosure rule read *before a fill proposal* is adequately read; that is the moment it governs. **The real requirement is RELIABLE ACCESS BEFORE EVERY RELEVANT DECISION** — which includes the case tranche 1 missed: **a session that becomes trade-relevant AFTER boot**, when step 1's condition was already evaluated as false. ⚠️ **And making every clause an unconditional boot read is the WRONG remedy** — it inflates the read burden on the exact surface whose size started this work. The test is per-clause: *is there a step that reaches this clause at or before the decision it governs?*

> ⛔ **THE PROPOSED REPLACEMENT READERS WERE NOT EQUIVALENT, AND TRANCHE 1 OVERSOLD THEM.** `instrument_check` verifies **instrument health** — that a level's data source is reachable and fresh. `Derived Views` verifies **recorded reconciliation timing** — that a standing row was stamped after the newest grade. **NEITHER establishes that the deciding agent READ AND APPLIED the binding clause.** They supervise inputs and bookkeeping, not application. A clause moved under either one is monitored, not read.

⚠️ **Still true and still the point:** on 2026-09-07 the frame-breaker letter was reached because a cloud routine quoted it and a live session went looking — not because a step travels there. And `TRACKER.md:19`'s **non-canonical mirror** is read unconditionally by three cloud routines while the canonical clause is not.

## INVENTORY — tranche 1 (binding clauses; dated narrative not yet inventoried)

| # | clause | from (TRADE.md §) | to (destination) | reached by — **VERIFIED** |
|---|---|---|---|---|
| 1 | **FRAME-BREAKER carve-out** (survives the 8/7 retirement; instance ③ amended 9/7 WQ-189 — cargo/throughput floor) | § DEPLOY GATE v3 HARD RULES, L271–276 | → `setups/SPECS_GATES.md` (P2) | 🟠 **CONDITIONAL ONLY** — boot step 1 `if the task touches positions/trades`. Mirrored (prose, non-canonical) in `demand_destruction/TRACKER.md:19`, which IS read unconditionally by three cloud routines. **The mirror is better-read than the letter.** |
| 2 | **STAGE-A v5 — LIVE ENTRY GATE** (Will-ratified 2026-07-31) | § STAGE-A v5, L527–560 | → `setups/SPECS_GATES.md` | 🔴 **NO UNCONDITIONAL READER.** Conditional boot step 1 only. |
| 3 | **HARVEST RULE** (mandatory, Will-ratified 7/30 Option B) | L692–708 | → `setups/SPECS_TRADE_RULES.md` | 🔴 **NO UNCONDITIONAL READER.** |
| 4 | **OFF-RAMP ROUND-TRIP PLAYBOOK** (pre-registered; re-spec v2 ratified 7/29) | L517–526 | → `setups/SPECS_TRADE_RULES.md` | 🔴 **NO UNCONDITIONAL READER.** |
| 5 | **BINDING WILL RULINGS** — incl. the two 8/3 rulings and the **ROLL scope guard** (*"a scope ruling is broader than an exception and needs one"*) | § BINDING WILL RULINGS, L174–208 | → `RULINGS.md` (dated) + letter stays | 🔴 **NO UNCONDITIONAL READER.** ⚠️ Closeout step 13 now routes NEW rulings to `RULINGS.md`; it does not make the EXISTING ones read. |
| 6 | **MANDATORY PRE-FILL DISCLOSURE** (direction-neutral; adds information, never permission) | L282 | → `setups/SPECS_GATES.md` | 🔴 **NO UNCONDITIONAL READER** — and it binds only AT a fill, which is the moment it must already have been read. |
| 7 | **BINDING CAVEATS** (*"carried ON the spec so they cannot die with a proposal doc"*) | L288 | → travels with clause 2/6 | 🔴 **NO UNCONDITIONAL READER.** ⚠️ The caveat's own text says it was placed to survive a proposal doc dying — it now has the same exposure one level up. |
| 8 | **EXECUTION LOG rows** | L868–880 | stays in `TRADE.md` | ✅ **VERIFIED READER: boot step 6c**, unconditional. ⚠️ **SCOPE-LIMITED: it reaches only rows marked `PENDING`/⏳.** A terminal row that is WRONG is not read by anything. |
| 9 | **`Updated:` / `Last real data refresh:` two-clock header** | L3 | stays | ✅ **VERIFIED READER: `workbook/LEDGER_GLOB` → `ledger_staleness.py`**, unconditional at boot, `--days 7`. ⚠️ Reads the STAMP only, never agreement. |
| 10 | **CURRENT STANCE (v5.0)** · **CONCENTRATION ARITHMETIC** | L18–25 · L52–67 | → STATUS § STANDING STATE? (open) | 🔴 **NO UNCONDITIONAL READER.** Candidate for promotion to STANDING STATE, where the `Derived Views` guard would supervise them. |

## WHAT THIS CHANGES ABOUT P2

⛔ **The migration is NOT primarily a byte problem.** `TRADE.md` at 337% of cap is the symptom that got it noticed; **the defect is that 8 of 10 binding clauses have no unconditional reader**, and moving them to `setups/SPECS_*.md` does not fix that — **it changes the address of an unread clause.**

⇒ **Each move must ship WITH a reader**, or it makes things worse. Options per clause: name it in an unconditional boot step · put its live state in STATUS § STANDING STATE under the `Derived Views` guard · or register it in `workbook/REGISTRY.tsv` where `instrument_check` probes it.

## 🔴🔴 TRANCHE 2 — ROTATION IS **NOT** JUSTIFIED. LIVE OBLIGATIONS SIT INSIDE THE "HISTORICAL" SECTIONS.

⛔ **Tranche 1 proposed rotating three dated sections (`70,739` UTF-8 B = 38.7% of the file) as "dated RECORD, not binding clauses." THAT WAS WRONG, and it is the original defect recurring inside its own remedy:** a superseded SECTION HEADING does not establish that every clause inside it is superseded. `[[finding_live_claim_in_a_closed_container_is_invisible]]`

**Measured 2026-09-08: 33 live/binding marker lines across the three ranges.** Named survivors requiring individual reconciliation BEFORE anything moves:

| # | surviving obligation | at | why it is LIVE, not historical |
|---|---|---|---|
| 11 | **The sharpest-limit caveat** — *"this regime has produced ZERO genuine physical reopenings … THIS SPEC IS OPTIMISED AGAINST A PROFITABLE TRADE, NOT A VERIFIED REOPENING"* | L595 | **Will-directed 2026-07-31 to carry VERBATIM into the live spec and to SURVIVE EVERY FUTURE EDIT.** By its own text it binds Stage-A **v5**, not v4. Rotating it would delete a clause whose whole purpose is to outlive edits. |
| 12 | **SIZING — HALF/HALF, Will-ruled 2026-07-31** · TRANCHE 1 (day 0, on (i)+(T)) · TRANCHE 2 (remainder on Leg C resolution, only if Leg C passes AND day-0 close-basis Leg T passes — tightened Will-ruled 2026-08-05) · **fenced ~$500 max-loss UNCHANGED** | L599–604 | Live sizing rules for a gate that can still fire. Not superseded by v5 — v5 changed the ENTRY legs, not the tranche construction. |
| 13 | **UNRESOLVED CLOCK INTERACTION** — H1 says exit ≤8 trading sessions after entry; two tranches = two entries ⇒ tranche 1 stops day+9, tranche 2 day+10 | L604 | **Flagged "so it is not discovered in a live trade" and carries an INTERIM reading, not a ruling.** An open question with a provisional answer is the most dangerous thing to archive. |
| 14 | **§0a UNRESOLVED, NOT EXPLAINED** (7/30 analogue tanker figures do not reconcile) | L597 | Explicitly labelled unresolved. |
| 15 | **STAGE B — PERSISTENCE** (per-leg windows: transits 10 td · war-risk 25 td · P&I 25 td) + **THE KILL TEST** | L668+ | **Post-entry monitoring and exit rules — they grade a position AFTER it is on.** ⚠️ Some instruments have LATER retirement/successor records (the Worldscale/war-risk leg was retired 7/31 for having no feed) ⇒ **each leg needs individual reconciliation against its successor, not a section-level verdict.** |
| 16 | **Harvest-rule interaction** (*"must not be buried"*) · **35a modifier `REVERSE`, Will-ruled 2026-08-11** (governs SIZE-IF-FIRED) | L735 · L743–749 | Dated Will rulings inside the "knowingly-open" block; both still govern a fire. |

⇒ **NOTHING IN THESE RANGES ROTATES UNTIL EACH ROW ABOVE HAS ITS OWN IDENTITY, TRIGGER, DESTINATION AND VERIFIED READER, AND ANYTHING CLASSIFIED RETIRED CARRIES ITS SUPERSEDING EVIDENCE.** A section-level verdict is exactly the instrument that failed here.

## MEASUREMENT CORRECTION

Tranche 1 said the three ranges were **"69,221 B"**. That figure is **CHARACTERS** — it came from `len(line)+1` on `str`, which counts code points, not bytes. **UTF-8 bytes: `70,739`** (share unchanged at 38.7%; this file is emoji-dense, so char≠byte throughout). ⚠️ **Every byte figure this desk quotes must come from `len(s.encode())` or `wc -c`, never `len(s)`.** `[[finding_loadbearing_number_must_be_reproducible]]`
