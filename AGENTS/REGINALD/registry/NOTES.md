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
