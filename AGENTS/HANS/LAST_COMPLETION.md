## COMPLETION — HANS — 2026-09-19, SESSION 4 (owed-board catch-up, then the AGSI arc). Saturday, market closed — structural work by design.

**STATUS:** ✅ DONE — committed and pushed, HEAD `503c65677`. Boot **EXIT 0 CLEAN** (was rc1) · `doc_audit` **0 findings** · **74/74 tests** (was 67) · `closeout_check` **8/8 mechanical RAN, 0 failed** · R1 rc=0 · read-cap rc=0.

**⚖️ WILL NEEDS: NOTHING.** The one ask of this session — the free GIE AGSI+ key — **Will provisioned at 11:33 and it is verified working by live pull.** No open ask.

---

### THE SESSION IN ONE LINE
Read the ESRB report I had been deferring and found my bank-stress alarm was clean over ground its own author calls blind; then the API key Will added exposed a frozen benchmark that had an **open fire sitting on the wrong side of its own threshold.**

### ① ESRB `esrb.report202602` READ AT PRIMARY (owed #4) — embargo discharged
82pp joint ECB/ESRB, full text, not the press release. **Identified bank exposure to private equity / private credit: €4bn** — the report calls it *"far below the figures implied by supervisory intelligence"* and **drops the class from the analysis**; leverage for these entities *"cannot be computed from existing data"*, and the non-EU gap is *"likely to remain"* after reform.
🔴 **`T-14` is NOT fired and this does not fire it** — but leg (b) waits for a supervisor to NAME institutions, which is downstream of that supervisor being able to SEE the exposure. **Band unchanged, deliberately not re-tuned** → `ML-HANS-464`.
🔑 **Cuts against my own alarm:** euro-area banks are **net DEBTORS** to NBFI (~15% of balance sheets); US banks are net lenders. Europe's channel is **losing NBFI funding in a stress, not credit losses on private credit.** `HNS-09` keeps **70%**, **basis swapped** to the structural point. ⚠️ Two perimeters never merged (FSR €62.5bn drawn ≠ ESRB €4bn identified). ⛔ Not claiming it is larger — it is *unquantifiable*.

### ② AGSI KEY → A FROZEN DENOMINATOR WITH AN OPEN FIRE ON THE WRONG SIDE OF IT
| | gap | norm |
|---|---|---|
| carried in STATUS | −19.7pp | 88.0 (GEF) |
| my script printed | **−12.9pp** | **82.0 HARDCODED, frozen 2026-08-28** |
| **AGSI-native truth** | **−15.99pp** | **85.05** (mean of gas day 09-17, 2021–25; median −16.61) |

Band is **−15**. 🔴 **The frozen constant fails toward ALL-CLEAR and does it invisibly:** the true norm *rises* through the injection season, so the gap reads better as time passes while nothing improves — and the numerator keeps updating, so no single run looks wrong → `ML-HANS-467`. Fixed: `agsi_norm()` computes from AGSI history, **fail-closed — no norm ⇒ NO GAP PRINTED**, never a constant fallback.
⛔ **−19.7 → −15.99 is a BASIS CORRECTION, NOT A RECOVERY** (~80% denominator). **FIRE STAYS OPEN by 1.0pp.** Corrections sent to BRENT and HENRY unprompted.
✅ **The morning's fail-closed exit clause earned itself on its first live pull** — the cross-source −12.9 would have looked 2.1pp from an exit.

### ③ DEAD-KEY DISCRIMINATOR (PROME's finding, verified then wired)
A **rejected AGSI key returns HTTP 200 + an empty array** — identical to an unpublished gas day, so silent expiry prints *come back tomorrow* forever. Now that the norm is AGSI-native, a dead key blinds **both legs**. Wired: KEY REJECTED / genuine-no-data / **UNDETERMINED-and-BLIND**, quirk-dependent with **re-check 2026-12-19 in the code**, failing in the safe direction → `KB-HANS-095`.
🔴 **I nearly refuted a correct finding with a probe that never left my machine** — `curl -H "x-key: "` drops the header; I silently re-tested the ABSENT case and got a *reproducible* wrong answer. **Reproducibility did not rescue it; varying the client did.** Tell I missed: two arms that should differ returned identical results → `ML-HANS-468`.
An injection test then found **two key-resolution paths I had created an hour earlier** → `ML-HANS-469`. Swept the class desk-wide: **clean on the dangerous form**, one LOW item graded and left → `ML-HANS-470`.

### ④ THE REST OF THE OWED BOARD
`T-08` **exit condition registered** (owed #9) — inside −12pp × 5 gas days, hysteresis −15/−12, blind day never counts, no exit cross-source. `HNS-07` **pre-committed re-mark rule** (owed #12) — 43 days before the resolver, 3 checkpoints, 4 triggers, **anti-chase clause**. `VX-HANS-5.01` **had measured a broad index for 3 weeks** against SX7E bands — could not fire; C10/C11 both passed correctly because the arithmetic was consistent and the halves named different objects → `ML-HANS-465`. **All 5 stale vectors cleared:** `8.05` German IP **−1.6% YoY** (GREEN→YELLOW), `4.09` UK food — **AHDB partly refutes the claim that created the row** (wheat −12%, spring barley −19%, but winter barley in line, OSR **+19%**) → `ML-HANS-466`, `11.04` frozen out-of-scope → HAWK/BRENT, `4.07` cadence mismatch not rot.

---

### OPEN, DATED, ON THE BOARD
| # | Item | Due |
|---|---|---|
| 21 | **AGSI lag D+1 vs D+2** (`KB-HANS-096`) — PROME raised it, explicitly NOT a defect. Touches `HNS-07`'s **grading date** (11/02 vs 11/03), not its resolver | **Tue 2026-09-22** |
| 3 | **`HNS-06` resolves — German/EA flash PMI. GRADE THE FLASH**, not the final | **2026-09-23** |
| — | **`TTF=F` roll** — `T-07` is a LEVEL ladder with L1+L2 fired; **never grade a rung crossing across a roll** | **2026-09-29** |
| 20 | **STATUS hot/cold split — PROME-ruled as its OWN task, not a session tail** | 🔴 |
| 22 | **Empty-key discriminator is vendor-quirk-dependent** — re-verify the negative control | **2026-12-19** |
| 5 · 5b | **Two basis gaps, one DECIDES `T-10`** (OAT ~10bp); **no free daily-close gilt source** | 🔴 |
| 13 · 14 · 15 · 16 | Re-argue exclusion leg (2) · split `VX-HANS-11.03` · `doc_audit` C2 does not scan STATUS · Germany UST not in TIC Table 5 | 🟠 |

⚠️ **STATUS sits at ~79% of budget after three rotation passes (from 91%).** Rule 5's stop is <70%. **PROME ruled: do not squeeze further, do the split as its own task** — a fourth pass would shave live state to make a number. **It rose because the day produced findings; that is information, not drift.**
🟢 **Self consumer-check 🔴s NOT cleared, deliberately** — they sit on dated 9/18 records correctly quoting what was believed then (closeout 9c).
⚠️ **STANDING PRIOR, now EIGHT sessions: every defect on this desk is found from OUTSIDE or by a script, never by re-reading.** Session 4 holds three times — a deferred primary, a staleness scan, and a new API key.

**NEXT SESSION FIRST:** the **Tuesday lag check** (it is 3 days from `HNS-06`), then **grade `HNS-06` on the FLASH**.
