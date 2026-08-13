# REGINALD registry — row notes

**Created:** 2026-07-30 · **Owner:** REGINALD
**Why this file exists:** `THRESHOLDS.tsv` is a strict 8-column TSV with no notes column, so a row cannot carry its own rationale without breaking the schema. Anything a reader needs *in order to evaluate a row correctly* lives here, keyed by `trigger_id`. **A row with an entry below cannot be read safely from the TSV alone.**

**Rule:** notes record *measurement basis, provenance, and deliberate divergences*. They never restate or modify a level, operator, window, or action — those live in the TSV and move only by an explicit ruling.

---

## `REG-T-07` — OFFICE-CMBS-DQ-TREPP > 15, sustain 3

**⚠️ Evaluation basis is load-bearing and was previously ambiguous. Two providers publish "office CMBS delinquency" and they sit ~8pp apart.**

| Evaluate against | June 2026 | Distance to the >15 fire |
|---|---|---|
| ✅ **Trepp office DQ** — THE basis for this trigger | **11.57%** | **3.4pp** |
| ❌ Fitch *overall* CMBS DQ (different universe **and** different scope) | 3.31% (May) | 11.7pp — reads "nowhere near" |

**History.** Until 2026-07-30 the metric field read the un-provisioned `OFFICE-CMBS-DQ`, while my STATUS dashboard row under the heading "Office CMBS DQ" carried the **Fitch overall** figure. Both numbers are correct for what they measure; the defect was **a wrong denominator under the right label**, which makes the gate look ~3.5× further from firing than it is. Found by **CREED 2026-07-27** (`inbox/processed/2026-07-27_from-CREED_REG-T-07-fires-on-my-series...`) in a Will-directed structure survey. Same provider-stacking class as `[[finding_blended_index_masks_bifurcation]]`.

**Edits made 2026-07-30 (PROME-ruled GO; disambiguation, not level moves — no level, operator, window or action changed):**
1. metric `OFFICE-CMBS-DQ` → **`OFFICE-CMBS-DQ-TREPP`**
2. recipient chain += **`CREED info`** → `REGINALD action / CREED info / BROCK SHADE info`

**★ The divergence from CREED's trigger on the same series is DELIBERATE — recorded here because nothing previously recorded that anyone had compared them.**

| | metric | op | level | sustain | purpose |
|---|---|---|---|---|---|
| **`REG-T-07`** (mine) | OFFICE-CMBS-DQ-TREPP | > | **15** | **3** | **bank-transmission ACCELERATE gate** — the point at which securitized office stress is severe and persistent enough to argue transmission into bank-held CRE |
| **`CREED-T-01a`** (CREED's) | OFFICE-CMBS-DQ-TREPP | > | **12** | **2** | **RECOGNITION gate** — earlier, faster, fires when the market is acknowledging the stress |

Different questions of the same series ⇒ different levels are correct, not a conflict. **Do not "reconcile" them to one number.** CREED owns the series; **CREED had me as `action` on its trigger while I had CREED on none of mine** — that asymmetry is what item 2 fixes.

⚠️ **Bank-HELD ≠ securitized.** This trigger reads a CMBS series and is an *input* to a bank-transmission argument, never direct evidence of bank-held CRE deterioration. The bank-held/CMBS gap is tracked separately (~7.5pp as of the STATUS row).

---

## `REG-T-02` — WAL-PRICE < 78, sustain 1

**Chain provenance.** Reads `REGINALD action / WAL action / Will` as of 2026-07-29. The `WAL action` leg was added post-WAL-promotion by **RAV Codex** (Will's outside continuity tool, commit `383bf581`), WALTER diff-verified 7/30 (`SIG-W-20260730-008`), and **re-verified at source by REGINALD 7/30** rather than accepted on the relay. No further edit is owed; WALTER's 7/25 packets asking for it are **superseded**.

⚠️ **Sustain is 1 — if it fires, it fires SAME-DAY**, with REGINALD + WAL + Will all on `action`. WAL has been oscillating around the ~5% near-trigger band. **WAL-specific analysis belongs to `../WAL/`;** REGINALD keeps the matrix row and cohort context only.

---

## `REG-T-03` / `REG-T-04` — HY-OAS > 320 / > 350

**⚠️ Two standing interpretation caveats — the levels are UNCHANGED by both; carry them when citing either row:**
1. **Composition drift (SIG-723-002, 7/23):** the thresholds are NOMINAL and the HY index has improved since calibration (CCC weight ~10% vs 16%, secured ~37% vs 18%) — the same print now represents MORE stress than at calibration. Flagged as anchor-drift family, not moved.
2. **Blended-index tail-lag (SIG-717-003, WALTER 7/15; promoted from SCRATCH 8/10):** the blended HY index can sit at a benign percentile while the CCC constituent sits at a stressed one (measured 7/15: blended at the 8.3 pctile of its 3-yr range, CCC at 87.8) — so a tail-led credit break may fire late against these blended-level triggers. Companion instrument = the CCC/HY RATIO tripwire `VX-REG-18.04` (spec pinned to the ratio 7/30), which is the tail-sensitive leg; sub-index (BB/B) collection is a fleet gap flagged to PROME by WALTER.

**Downstream-of-bank caveat (7/30 attribution, standing):** HY sits DOWNSTREAM of bank credit in my chain — an HY move without a bank-credit leg is not my chain firing. Before treating any HY level as bank transmission, run the bank-credit cross-check (`reports/2026-07-30_bank-side-HY-attribution.md`).

---

# SCHEMA CHANGE 2026-08-13 — audit-convention encode (8 cols → 13, APPEND-ONLY)

**Authority:** `PROME/proposals/2026-08-12_audit-convention-RULED.md` (Will-approved 2026-08-12, FLEET SCOPE) — *"a stored value must carry its unit and basis; a threshold must name the instrument that grades it (a continuous series is not a contract); and 'zero' must be distinguishable from 'unknown' and from 'not applicable.'"* Encode requested of REGINALD via PROME's 2026-08-13 spawn brief off DAEDALUS's `THRESHOLDS.tsv` findings (**zero exit conditions · zero instrument/basis columns**).

**⚠️ FLAG-BEFORE-ENCODE — the tension I resolved, stated rather than assumed.** DAEDALUS's own REGINALD profile records **"THRESHOLDS 8-col contract"** as a HELD invariant and **"NOTES.md is a companion, never folds into the TSV."** The convention needs machine-readable per-row instrument/basis; NOTES is prose keyed by `trigger_id` and only two rows carry entries. **Resolution: APPEND-ONLY extension.** Columns 1-8 are **byte-identical to `de75ab659`** (verified by `cut -f1-8` diff), so the 8-col contract survives as an exact prefix and any positional reader is unaffected; the five new columns are appended at the end. **No level, operator, sustain window, action, recipient chain or thesis ref moved.** Grep for script consumers before the edit returned **zero** — this file is read by humans and packets only.

| New column | Carries |
|---|---|
| `grading_instrument` | The named series/tool that grades the row. *A continuous series is not a contract* — so the row names FRED `BAMLH0A0HYM2`, not "HY OAS." |
| `value_unit` | Unit of `threshold_value` (USD / bps / percent / thousands of persons / USD billions). |
| `value_basis` | What the number measures — close vs intraday, SA vs NSA, rate vs balance, first-release vs revised. |
| `sustain_unit` | **The defect this closes:** `sustain_window` was a bare integer meaning *daily closes* on REG-T-01/02/03/04/08, *weekly prints* on REG-T-05, *monthly prints* on REG-T-07 and *quarterly prints* on REG-T-06. One column, four different clocks, none written down. |
| `exit_condition` | What un-fires the row. Previously **every row was a one-way auto-fire with no recorded un-fire**, so a fired row could only ever be un-fired by undocumented judgment. |

**Exit conditions are NEW SPEC, pre-registered here, and are deliberately conservative.** Construction rule, applied uniformly: exit requires the metric back on the benign side **by a stated margin** (5% hysteresis on the two price rows; 20bp on HY; a proportionate step on the rest) sustained for a window **≥ the entry window**, graded on the **same instrument** as entry. This is asymmetric by design — harder to un-fire than to fire — because a fired row escalates other agents and an oscillating gate would thrash the whole chain. **These are not levels moved: no entry threshold changed, and before this edit the exit was not "something else," it was *nothing*.** They are gradeable and executable inside the window their instruments quote (`finding_executability_is_a_separate_audit_axis`). If any owner on a recipient chain thinks an exit is mis-set, argue it before it fires, not after.

**Not registered, deliberately.** MI3 / hidden-CRE has **no row in this registry** and I did not add one on the day I re-ran the screen. The cohort re-run (`reports/2026-08-13_MI3_cohort_rerun.md`) found the legacy `>20%` flag catches one name on the legacy basis and **zero on the uniform basis** — so a new MI3 trigger would need its base rate and separation established first, and *"don't build it"* is a real answer (`finding_base_rate_the_threshold_before_building_it`). Recorded as a candidate on ROADMAP, not as a gate.
