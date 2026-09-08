# TRADE.md — OBLIGATION INVENTORY (P2, tranche 1)

**Started 2026-09-08.** DAEDALUS architecture review P2 / ACTION 13. **One row per binding clause: `clause · from · to · reached by`.** ⛔ **A clause archived without a reader is lost operationally** — so this is built BEFORE any clause moves, not after.

> ## ⛔ THE RULE THIS FILE IS BUILT UNDER
> **`reached by` is a VERIFIED path, never a filled cell.** A pointer records *intended* access; only opening the named step establishes that the obligation is reachable. Every row below was checked by reading the step, not by grepping the filename.
>
> ★ **AND THE CHECK EARNED ITS KEEP ON THE FIRST PASS.** `grep -rl "TRADE.md" scripts/` returns **`boot.py`, `render_calendar.py`, `cot_grade.py`** — and **all three mention it ONLY IN COMMENTS.** No code path reads the file. A `reached-by` column filled from that grep would have recorded three readers that do not exist, with the authority of an audit. `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`

## 🔴 THE HEADLINE, AND IT IS A REAL DEFECT — NOT A FILING PROBLEM

**Every binding clause in `TRADE.md` except the EXECUTION LOG is reachable ONLY through boot step 1's CONDITIONAL read** — *"read `TRADE.md` … **if the task touches positions/trades**."*

⇒ **On a session that does not touch positions, NOTHING reads the frame-breaker letter, STAGE-A v5, the harvest rule, the off-ramp playbook, or the binding Will rulings.** They are not archived, not retired, not stale — they are simply not on any unconditional path.

⚠️ **This is not hypothetical.** On 2026-09-07 a scheduled cloud routine flagged the M/T Kylo sinking against the frame-breaker letter. The letter was reached because the ROUTINE quoted it and a live session then went looking — **not because any boot step travels there.** The clause that governs whether capital deploys sits behind an `if`.

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

## NOT YET INVENTORIED (tranche 2)

Dated narrative blocks (LIVE-VINTAGE COMPANIONs 8/21 · 8/27 · 9/2 · the 8/14 broker-vintage table · the frozen behavioral test L428–516 at 20,386 B · STAGE-A v4 L561–691 at 26,716 B · the 7/30 KNOWINGLY-OPEN block L709–817 at 22,119 B). **Those three sections alone are 69,221 B = 39% of the file** and are the rotation candidates — but they are dated RECORD, not binding clauses, so they rotate under rule 19 rather than needing readers.
