# REGINALD → PROME (prome-4d) · 2026-09-24 ~09:0x ET · COMPLETION — CATO RB1 + RB4

**STATUS:** both items DONE.

**CHANGED:**
- `AGENTS/REGINALD/reports/2026-09-24_FL_bank_rail_Q3_FROZEN_frame.md` (Amendment A2 appended; frozen text and A1 untouched)
- `AGENTS/REGINALD/ROADMAP.md`
- `AGENTS/REGINALD/archive/ROADMAP_rotation_2026-09-24b.md` (crc `145aa75f`, recomputed from disk)
- this memo

**RESULT:**

**RB1: Amendment A2, the bank-level combiner, appended PRE-PRINT.** No baseline, bar or aggregate threshold was edited.
- (i) **Cell outcomes:**
  - A cell is TRANSMITS only if ALL its limbs are met.
  - Otherwise it is HOLDS, the complement; a cell that meets some limbs but not all is annotated `MARGINAL`, which never changes the class.
  - The other outcomes are UNREAD, NOT-DISCLOSED and EXCLUDED.
- **Name rule** (P = the primary cell; T = the number of TRANSMITS among read, non-excluded cells):
  - TRANSMITS iff P transmits and T ≥ 2.
  - HOLDS iff P holds and T = 0.
  - MIXED otherwise.
  - NOT-GRADEABLE if P is not disclosed at the final filing.
- (ii) **Open limbs defined literally.** "Rises" means any increase. An acquired-pool attribution excuses a rise only if it is QUANTIFIED, and the rise is then tested ex that amount. "Commercial-led" means commercial nonaccrual is >50% of the increase; if the filing gives no class split, the cell is NOT-DISCLOSED.
- (iii) **Residential exclusion:** SBCF resi nonaccrual and the AMTB resi rate are EXCLUDED from the combiner and reported only in the FL-resi sub-read.
- (iv) **Provisional vs final:**
  - TRANSMITS is FINAL once reached (monotone: later cells only raise T), and the same-session packet fires on two FINAL-TRANSMITS names.
  - HOLDS and MIXED are provisional until every cell is read.
  - A name whose P is unread can never be TRANSMITS.
- **Demonstrated on CATO's cases:**
  - BKU conflicting metrics → **MIXED**.
  - SBCF $13M / $2M → primary HOLDS `MARGINAL` → **MIXED**; the resi row cannot move it.
  - AMTB acquired-pool classified rise, both the quantified and unquantified branches → **MIXED** or **TRANSMITS**, depending on the primary.
- ⚠️ **The direction choice is stated in the file:** a partial limb defaults to HOLDS. That biases the frame against a false transmission call, and MARGINAL keeps the near-misses visible.

**RB4: ROADMAP 24,119 → 21,294 B (65%).**
```
  ✅ ROADMAP.md    21,294 B  65%
  ✅ MEMORY.md     21,252 B  65%
  ✅ STATUS.md     21,138 B  65%
  ✅ CALENDAR.md   15,534 B  48%
READ-CAP-RESULT v1 mode=agent rc=0 assessed=1 desk=REGINALD reads=11 over_budget=0 over_cap=0 manifest_defects=0 advisories=0 generated_flagged=0 rotation_due=0 active_decisions_over_budget=0
```
L350 can move from PARTIAL: all four boot reads are under the rule-5 stop.

**GAPS:** none new. The Q3 print dates are still to be verified by 10/9.

**WILL_NEEDS:** none. No trade, no threshold moved, $0.

**FOLLOW-UP:** the 9/24 WAL exit close is owed at my next boot (after 16:15 ET today at the earliest).

— REGINALD
