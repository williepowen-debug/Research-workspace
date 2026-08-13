# P1 — STEO VINTAGE LADDER: is the Middle-East recovery being **deferred**, or did I over-read one vintage?

**Built 2026-08-13 · Will-approved slate item 1 · BRENT own pull.**
**Instrument:** EIA STEO archive workbooks `https://www.eia.gov/outlooks/steo/archives/{mar,apr,may,jun,jul,aug}26_base.xlsx`, sheet `3dtab`, series **`cops_opec`** (OPEC total surplus crude oil production capacity, mb/d) and **`cops_opec_r05`** (Middle East).
**Method:** parsed **by series label in column A and by the Jan…Dec header row**, never by cell address — layouts are not guaranteed stable across vintages. Quarterly figures are **simple means of the three monthly values**.
**✅ PARSE VERIFIED:** the Aug-26 vintage reproduces the live v2 API exactly — 2026Q4 `0.020`, 2027Q1 `0.030`, 2027Q2-Q4 `2.380`. *(The v2 API serves only the CURRENT vintage; the archive workbooks are the only public route to prior ones.)*

---

## THE LADDER — OPEC total surplus capacity (mb/d), by forecast vintage

| vintage | forecast date | 26Q2 | 26Q3 | 26Q4 | **27Q1** | 27Q2 | 27Q3 | 27Q4 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| **mar26** | Mon Mar 9 | 3.022 | 2.968 | 3.102 | **3.222** | 3.095 | 3.048 | 3.182 |
| **apr26** | Mon Apr 6 | 0.040 | 0.040 | 2.570 | **3.922** | 3.795 | 3.748 | 3.882 |
| **may26** | Thu May 7 | 0.033 | 0.040 | 0.040 | **2.547** | 2.447 | 2.413 | 2.547 |
| **jun26** | Thu Jun 4 | 0.027 | 0.040 | 0.040 | **1.697** | 2.447 | 2.413 | 2.547 |
| **jul26** | Wed Jul 1 | 0.020 | 0.020 | 0.020 | **1.597** | 2.380 | 2.380 | 2.380 |
| **aug26** | Thu Aug 6 | 0.053 | 0.020 | 0.020 | **0.030** | 2.380 | 2.380 | 2.380 |

---

## ⇒ VERDICT ①: **DEFERRAL PATTERN — CONFIRMED. Not an August outlier.**

**2027Q1 by vintage: 3.222 → 3.922 → 2.547 → 1.697 → 1.597 → 0.030.** After April, **four consecutive downward revisions totalling −3.892 mb/d.**

**But the sharper structure is not "the recovery is shrinking" — it is that THE TROUGH IS MARCHING FORWARD ONE QUARTER AT A TIME.** Read the **first quarter that recovers** in each vintage:

| vintage | trough runs through | first recovering quarter |
|---|---|---|
| mar26 | *(no trough — 3.0+ across the horizon)* | — |
| apr26 | 26Q2–26Q3 | **26Q4** |
| may26 | 26Q4 | **27Q1** ← pushed out one quarter |
| jun26 | 26Q4 | 27Q1 |
| jul26 | 26Q4 | 27Q1 |
| aug26 | **27Q1** | **27Q2** ← pushed out one quarter again |

**The recovery-start date has been deferred TWICE in five vintages — Apr→May and Jul→Aug — roughly one quarter per three-to-four monthly vintages.** ⇒ **my 8/13 morning read (window closes Q2-2027, not Q1-2027) was directionally right, and if anything I saw only the LAST step of a standing pattern.**

## ⇒ VERDICT ②: ⛔ **RETRACTION — my "the assumption HARDENED" framing this morning was WRONG.**

This morning I wrote that the un-audited assumption **"HARDENED rather than softened: 100.0% Middle East (was ~99.6%)."** **The ladder refutes the change, though not the level.** ME share of each vintage's recovery step:

| vintage | mar26 | apr26 | may26 | jun26 | jul26 | aug26 |
|---|---|---|---|---|---|---|
| **ME share of the recovery step** | 100.0% | 100.0% | 100.4% | 100.6% | 99.4% | 100.0% |

**⇒ ME share has been ~100% in EVERY vintage, including March.** It is a **structural constant** of how EIA models OPEC spare capacity (essentially all of it sits in Saudi/UAE/Kuwait/Iraq) — **not a moving assumption that "hardened."** **The 99.6 → 100.0 step I highlighted is NOISE inside a flat series, and I presented it as a change.**
✅ **What survives, and it is the part that actually matters:** the recovery **is** ~100% Middle East, so **EIA's window-closing forecast genuinely is a bet that FALCON's theater de-impairs.** That statement was true this morning and stays true — **it just is not NEW, and I should not have framed a constant as a hardening.** `[[finding_exact_level_authenticates_a_wrong_direction]]` — second instance this week, both mine.

## ⇒ VERDICT ③: **EIA is deferring the START, not writing down the SIZE.**

**27Q2–27Q4 has sat at `2.380` since the July vintage and ~2.4–2.55 since May.** ⇒ **EIA still forecasts the Middle East capacity comes back IN FULL — later.** ⛔ **This is a TIMING edge, not a capacity write-down, and must never be cited as one.**

---

## ⚠️ WHAT THIS CANNOT SUPPORT — carried on the record per PROME's instruction

- ⛔ **This measures EIA's REVISIONS, not barrels. It can support TENOR TOLERANCE. It can NEVER support a supply-loss claim.**
- ⛔ **The vintages are NOT independent** — each is a revision of the last, so deferrals autocorrelate **by construction**. **A monotone slide is weaker evidence than it looks, and n=6 is really n≈2 independent deferral decisions** (Apr→May, Jul→Aug).
- ⚠️ **The series is NOT monotone: April revised 27Q1 UP** (3.222 → 3.922, +0.700). The deferral run starts in May, so it is **4 consecutive down-revisions, not 6.** Reporting it as six would overstate it.
- ⚠️ **Method note, recorded so it does not become a third value for one figure:** my carried July figure was **1.57**; the archive's simple quarterly mean is **1.597**. The gap is an aggregation-method difference (API quarterly weighting vs mean-of-months), **immaterial to every conclusion here** — but the two numbers are not interchangeable and neither should be quoted as the other.
- ⛔ **NO THRESHOLD PROPOSED, NONE REGISTERED.** Observational ladder only.

## 📌 BOOK IMPLICATION — tenor, and only tenor

A no-absorber window running **through Q1-2027** with a **repeatedly deferred** start supports **holding longer-dated oil exposure** — the **USO Oct-16 135C** and the **35 undefended shares**, whose thesis is time. ⛔ **It does nothing for the USO Sep-18 150/165 spread**, which needs **+22.3% Brent in 36 days** and whose risk is already sunk and capped. **It is not a reason to add, and it moved no threshold and no position.**

## 🔁 REFRESH

One workbook pull per month at the STEO release (~the 6th–11th). **Next: sep26 vintage, ~2026-09-08.** The single number to read is **the first recovering quarter** — if it slips to 27Q3, that is a third deferral and the pattern is n≈3 independent decisions.
