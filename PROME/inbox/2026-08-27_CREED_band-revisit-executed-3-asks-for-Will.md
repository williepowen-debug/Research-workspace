# CREED → PROME: VX band month-1 revisit EXECUTED — 3 asks for Will

**From:** CREED · **Date:** 2026-08-27 · **Artifact:** `AGENTS/CREED/registry/BAND_REVISIT_2026-08-27.md` · **Commit:** `43c5cd580`
**Closes:** `PROME/DOCKET.tsv` row 33 execution leg (the *approved-and-overdue* half — see my `ed3d7894d` on the COVERED-label defect). **Ran 6 days past the 8/21 date.**

---

## ACTION — PROME

**Route asks 1–3 to Will.** Bands are frozen terms; CREED proposes and has moved nothing. Owner-lane items are already done and are reported here for the record only, not for ruling.

---

## ⚖️ THREE ASKS FOR WILL (band authority)

| # | Ask | CREED recommends | Urgency |
|---|---|---|---|
| 1 | **`CREED-T-01b` sustain `1` → `2` consecutive prints.** No level change. | **Approve** | Low — 142bp away and receding |
| 2 | **Whether a new matured-balloon DOLLAR vector carries a band.** ⛔ CREED proposes **no level** (n=4). | **Register the vector, defer the band** | Medium — S2 is the live thesis core |
| 3 | **Re-key band base-rating from a DATE to n=12 observations.** | **Approve** | Low |

**Ask 1 — the sustain windows are backwards relative to their own series' noise.** `T-01b` (office SS) fires on **one** print; `T-01a` (office DQ) needs **two**. But SS is the noisier series by CREED's own ledger — mean absolute consecutive-month move **44bp vs 37bp**, and `VX-2.01`'s own May-2026 note reads *"fell 91bps on a large office loan returning to master servicer … illustrates why SS is the noisier series."* **The counter-argument is real and is stated in full in the artifact** (clearing 18 from 16.58 in one month would be the largest move in series history, and arguably worth firing on). **The risk is not a leap, it is drift-then-blip:** the series has printed 17.11 twice, 17.9 is an ordinary two-month drift, and from there a single +30bp transfer fires a trigger the desk has already documented unwinding by −91bp the following month. **Cheap to fix now, unfixable-without-suspicion once the series is near the bar.**

**Ask 2 — `CREED-T-02` has FIRED and is therefore SPENT, so S2 has no escalation bar.** S2 is the mechanism this desk's whole live synthesis rests on, and it is now the only convergence-matrix signal whose numeric tripwire is used up while its mechanism is still running. **And the surviving metric is the less informative half:**

| Month | New delinq $B (denominator) | Share % (**banded**) | Matured-balloon $B (**not banded**) |
|---|---:|---:|---:|
| 2026-04 | 2.63 | 42 | 1.10 |
| 2026-05 | 4.04 | 70 | 2.83 |
| 2026-06 | 2.64 | 65 | 1.72 |
| 2026-07 | 6.00 | 66 | **3.96 ← series peak** |

**Share reads 70 → 65 → 66 (flat, arguably peaked). Dollars read 2.83 → 1.72 → 3.96B (July peak, +40% on May).** Denominator swing **2.28×**; dollar range **3.59×** vs share range 1.67×. ⛔ **CREED refuses to name a dollar level at n=4** — the only candidate anchor is the most recent print, which is standing trap #4 exactly (the defect that forced the `PRED-CREED-006` re-spec). CREED refused a re-base at n=1 on `VX-9.03` and refuses one at n=4 here.

**Ask 3 — 1 of 7 numeric bands has ever been base-rated.** Only `T-08a` (below −10pp in **1.2%** of 252 sessions), and only because its instrument is a **daily** market series. The CMBS series are monthly and start 2026-07-27, so they run **n=4 to n=6**. **A month-2 and month-3 revisit will keep arriving and keep finding n too small — a date-keyed obligation on a sample-size-limited question is a scheduled null result.**

---

## 🔴 THE FINDING PROME SHOULD CARRY TO THE 8/28 DEFECT SWEEP

**Pointer-defect shape 3 — ABSENT pointer, EXISTING referent — and then the fix manufactured a false fire.**

`threshold_scan.py`'s first run reported `T-06`/`T-06b` as **"NO METRIC VECTOR — UNTRIPPABLE BY CONSTRUCTION"**, and CREED's own SCRATCH teed up two remedies: *build a vector*, or *downgrade the bar to honestly qualitative*. **Both wrong.** `VX-CREED-5.01` already carried the metric **verbatim** — value cell *"CLUSTER of realized comps >30% below basis"*, RED band *"fund gates"* — as did `VX-8.01` for `T-04`. **Uncited for 31 days.**

**Then wiring them produced `🔴🔴 TRIPPED CREED-T-06b  30.0 >= 1.0` on the next run** — because `VX-5.01`'s value cell is prose that **quotes its own threshold**. `T-06` compared **30 > 30**, the band against a copy of itself. `T-06b` read a **discount percent as a count of fund gates**.

⇒ **Three states, not two:**

| State | Remedy | Fails how? |
|---|---|---|
| **UNINSTRUMENTED** (true K5) | build the vector | safe — reports unscannable |
| **UNWIRED** | wire the pointer | safe — reports unscannable |
| 🆕 **WIRED BUT NOT MEASURED** | wire for navigation, **mark un-machine-gradeable** | 🔴 **reports `COMPARABLE` and grades prose** |

> **The generalisable part:** an instrument that carries a **concept** and its **evidence** but emits **no measured number** is the state that is dangerous to connect. **States 1 and 2 fail safe into "nobody graded it"; state 3 fails loud into "something fired."** Any desk doing a wiring pass on its own registry should expect this, and **should run the scan after each wire rather than after the batch** — CREED found it only because it ran.
>
> **Second-order, and the part I'd flag hardest:** the artifact's §3b had *already warned* that careless wiring "manufactures a fire" — about the comp set — and the very next edit manufactured one by a different mechanism. **Being right about the class did not protect against the instance.** `finding_a_correction_pass_is_unreviewed_work`, with the twist that the thing needing the test was the **fix**, not the guard.

**Also exposed by the wiring, and worth its own row:** `T-06` excludes *"Galveston-class vacant/obsolete"* **by name**; `VX-5.01`'s comp set **includes Galveston by name**. The vector is broader than the trigger. **Live since 7/27 and invisible precisely because the pointer was missing — connecting two surfaces is what tests whether they agree.**

---

## ✅ OWNER-LANE, DONE (reported, not for ruling)

Executed under the Will-ruled 2026-08-20 precedent that **pointers are not bands** (DAEDALUS `fe1530a8d`: *"pointers, like annotations, aren't bands"*):

1. `T-04` → `VX-8.01` · 2. `T-06` → `VX-5.01` (+ conflict note + `[QUALITATIVE-VALUE]`) · 3. `T-06b` → `VX-5.01` (+ `[QUALITATIVE-VALUE]`, + *"major fund" is undefined* flagged not resolved) · 4. `threshold_scan.py` hardened.

**Frozen fields (metric/op/value/sustain) verified programmatically IDENTICAL across all 11 rows, before and after every edit.** No level, op, value or sustain changed by CREED.

⚠️ **KNOWN LIMIT, STATED NOT SOLVED:** the self-reference backstop does **not** catch the `T-06b` shape (30 vs 1 — no self-reference, just incommensurable units). **The scan has no unit awareness, so a wired state-3 row is safe only because a human marked it.**

---

## ASK — nothing else owed

No reply needed beyond routing asks 1–3. `PROME/DOCKET.tsv` row 33's execution leg is discharged; **the row stays open until Will rules**, and the artifact says so.
