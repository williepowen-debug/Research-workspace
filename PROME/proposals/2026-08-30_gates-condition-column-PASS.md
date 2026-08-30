# GATES `condition` column — row-by-row pass: **EXAMINED, NO EDIT. The scope item's premise was false.**

**Ran:** 2026-08-30 ~15:0x ET Sun, PROME (DESKTOP), on Will's *"Then proceed with the GATES condition pass."*
**Scope item:** SCRATCH structure lane ② — *"GATES `condition` column (16 KB of spec text owners' KBs also hold) — a SEPARATE row-by-row judgement pass, never a sweep."* Held out of the 8/29 slim-down (WQ-134 #7) for its own sitting.
**Verdict: do not slim this column. Zero rows edited, zero bytes cut, and the reason is a finding, not a punt.**

---

## What was measured

| | |
|---|---|
| Rows | **30** (16 LIVE · 14 terminal) |
| `condition` total | **15,678 B = 30% of `GATES.tsv`** — the scope item's "16 KB" was accurate |
| LIVE rows with an unresolvable `definition_surface` | **0 of 16** |
| LIVE rows whose declared letter is **absent** at its declared home | **0 of 16** |
| Largest two rows | both **terminal** (BRENT-DEPLOY-V2 1,717 B · TERRY-006 1,318 B) = 19% of the column |

## Finding 1 — the premise is false: this is not duplicated spec text

The scope item assumed 16 KB *"of spec text owners' KBs also hold."* It is not. **13 of the 16 LIVE rows literally end `FULL LETTER → definition_surface (registry letter archived 8/22)`**, and the remaining three say the equivalent. The 2026-08-22 envelope conversion (PAT-006 two-homes drift) **did its job and is holding twelve days later.**

Every LIVE letter was then verified *present* at its declared home — **under the local id the cell itself declares**, which is the part that matters: `COT-FUEL-35B` in BRENT's `REGISTRY.tsv` · `KB-FERT-006` in FERT's `KB.tsv` · `T4` in FERT's `TRIGGERS.tsv` · `§REG-T-02` in REGINALD's `NOTES.md` · the two FORUM dissent posts carrying their own frozen thresholds (`≥3`, `N≥10`). **Nothing is orphaned and nothing is duplicated.**

## Finding 2 — the volume is standing guards, written at the fire-point

What actually fills the column is anti-error guard text, each clause traceable to a specific incident: CORAL's ⛔⛔ *MSI is **not** months-of-supply* mislabel correction · REG-T02's *re-derive distance from a NAMED DATED CLOSE, kill-on-sight* · LIQ-079's *never log a 079 fire as "X1 MET"* · HY-REKILL's *H-2 counting rule — a joint fire with HENRY's leg is ONE event on ONE series, never two confirmations* · TERRY-007's *OFFICIAL closes ONLY, ^TNX/^TYX count-neutral* · BRENT-COT-35B's frozen-vintage label correction.

**This is the class `ACTIVE_DECISIONS`' own row-weight rule already protects:** *"Standing guards (clauses carrying live directives) never rotate, however old — relief is discharge by ruling."* A guard's value is that it is read **at the moment someone could repeat the error** — which is when they are grading the gate, i.e. in this file. Moving it to an owner KB moves it away from the fire-point. HY-REKILL's counting rule guards exactly the failure HEARTBEAT flags as live (*"convergence-counting fired THREE times 8/28 from three desks; anyone stacking hawkish items is triple-counting"*).

Spot-checked whether these guards are also owner-homed: they are (LIQUID's STATUS + KB carry the H-2 rule; TERRY's card carries the official-closes rule ×7; REGINALD's NOTES carries the kill-on-sight). So the guards are **redundant, deliberately** — which is what a guard should be, and is not the two-homes *drift* PAT-006 was about (that was the full letter in two places, silently diverging; a one-line guard restated at the fire-point is not).

## Finding 3 — the real defect this pass found is in MY instrument, not the file

⛔ **Four times in this pass my scans asserted a defect that did not exist**, every time by testing a **naming form** instead of the thing:

| # | Scan | False claim | Truth |
|---|---|---|---|
| 1 | path-shaped-token scan | 4 LIVE rows "NO PATH" | directory pointers (`AGENTS/FLG`) and owner-relative paths (`reports/…`) are valid forms |
| 2 | guard-phrase grep | CORAL's MSI letter "absent from `STATUS.md`" | present — I grepped the metric name, the file names the **gate id** |
| 3 | gate-id containment | 6 LIVE rows' letters "NOT FOUND" | all present under the **owner's local id**, which each cell declares |
| 4 | H-2 guard grep | "unique-homed, cutting it would delete it" | owner-homed at LIQUID STATUS + KB, and HENRY |

`[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` — **n+4 in a single sitting.** Each false alarm was caught only because the pass is a judgement pass and I opened the artifact. A sweep would have "fixed" four non-defects, and fix passes carry a higher defect rate than the work they correct (`[[finding_a_correction_pass_is_unreviewed_work]]`).

## Recommendation

1. **Close structure item ② as EXAMINED — NO ACTION.** The column is not a slim-down target. Any future byte hunt should route to the two **terminal** rows (3,035 B, 19% of the column) whose letters are already archived verbatim+crc32 at `PROME/archive/GATES_CONDITION_LETTERS_2026-08-22.md` — but note the 8/22 ACTION-2 re-scope **deliberately** let terminal rows keep their letters as dated records, so changing that is a design ruling for Will, not maintenance.
2. **Build `scripts/gates_pointer_check.py`** (proposed, not built — Will's call). It resolves all four pointer forms (repo-relative · owner-relative · bare directory · KB-id) and verifies each LIVE row's letter is present **under the local id the cell declares**. That is the check that took four hand-iterations today and would take <1s at every boot inside `prome_gate.py`. ⚠️ Per `AGENTS/DAEDALUS/BLUEPRINTS/CHECK_STANDARD.md` its own v1 must be falsified before trust (`[[finding_test_the_guard_not_just_the_guarded]]`) — today's four false alarms are the ready-made negative-control set.

**No row edited. No threshold, band, letter or pointer moved. $0.**
