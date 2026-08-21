## 2026-08-21 — To: TERRY
**Signal:** ✅ **`COT-FUEL-35B` VINTAGE #2 GRADED 15:30 ET, ZERO LATENCY. `JOINT NO-VERDICT` ⇒ sizing DEFAULTS TO THE BASE CASE. NO SIZING CHANGE — but the two legs now OPPOSE each other for the first time, and you should know why.**
**Priority:** 🟠 · **ASK: none. Nothing to action — this confirms your current sizing basis rather than moving it.**

### The grade
**as-of Tue 2026-08-18.** Two independent raw `f_disagg.txt` pulls, **byte-identical**, `report_date` verified in-row, matched **by MARKET NAME** (the registry forbids contract code `067651` — it spans a 2022 rename).

| | value | vs 8/11 |
|---|---:|---:|
| MM gross shorts | **108,059** | **−2,579** |
| MM gross longs | 195,538 | +4,984 |
| Open interest | 1,888,960 | −3,469 |
| OI-share | **5.7206%** | −0.126 pp |

- **Leg A** — `108,059` is **below** the NO-VERDICT deadband floor `109,165` ⇒ **`SPENT`**. **First SPENT reading this band has ever produced.**
- **Leg B** — OI-share `5.7206%` vs the ≤`4.909%` bar, **GATING** ⇒ **`NOT-SPENT`**.
- ⇒ **`JOINT NO-VERDICT` ⇒ BASE CASE. Same outcome as vintage #1, so your sizing basis is unchanged.**

### ★★ What changed is the SHAPE, and it is the part worth your attention
Vintage #1 (8/11) had **Leg A NO-VERDICT + Leg B NOT-SPENT** — broadly aligned. Vintage #2 has **Leg A SPENT against Leg B NOT-SPENT — direct opposition, first time.**

**This is the band doing precisely what it was built to do.** Defect ⑤ in the N1 build was **leg suppression**: the retired incumbent published only the raw leg and structurally hid the disagreeing normalised one. **On this print the disagreement is visible instead of buried, and the honest answer is a non-call.**

**Why they split — the decomposition is the information:** **shorts fell 2,579, but OPEN INTEREST fell 3,469 alongside**, so OI-share moved only **−0.126pp**. ⇒ **money managers de-grossed in ABSOLUTE terms while positioning INTENSITY relative to the market barely changed.** A raw-count-only band calls that *spent*. **It is not obviously spent at all.**

### ⚠️ Two things that must travel with the verdict if you quote it
1. **RAZOR-THIN.** Leg A cleared the deadband floor by **1,106 contracts = 0.12 median units.** A ~1% move in the short position flips it back to NO-VERDICT. ⛔ **Do not relay "Leg A is SPENT" as a robust reading — it is a hair over a line.**
2. **The retired incumbent was NOT re-graded**, and for spec context only, so nobody argues the retirement suppressed a firing: its arithmetic here is **−21,013 against its own ≤−25,000 bar**, i.e. it would have sat in **IGNITING** and **would not have produced SPENT on this print either.** The retirement is not what changed the answer.

### ⛔ Unchanged and load-bearing
**NO LEVEL MOVED** — base `122,904`, `median_unit 9,160`, Leg-A bar `113,745`, deadband `109,165–118,325`, Leg-B bar `4.909%` were all **read from `REGISTRY.tsv`, not re-derived.** Re-basing remains a NEW N1 build plus a fresh Will ruling. **SIZING MODIFIER ONLY — never an entry trigger without a fresh build.** Non-claims travel: no out-of-sample test, n=0 genuine physical reopenings, no price validation.

⏰ **Next vintage as-of 8/25, releases Fri 8/28 ~15:30 ET. Next Baker Hughes Fri 8/28 ~13:00 ET. Neither should stack.**

**Source:** own grade, 2026-08-21 15:30 ET, `scripts/cot_grade.py` (rebuilt today to the frozen 35b spec; the prior version graded the RETIRED band from a source this spec forbids and could not compute Leg B at all).
