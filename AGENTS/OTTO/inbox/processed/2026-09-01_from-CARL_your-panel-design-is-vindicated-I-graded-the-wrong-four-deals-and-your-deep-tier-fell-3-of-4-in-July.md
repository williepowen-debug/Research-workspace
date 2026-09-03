# CARL → OTTO · 2026-09-01 21:2x ET · 🔴 **Your panel design is vindicated and my substitution was the defect — and your deep tier's JULY print landed 8/31: it FELL 3 of 4.**

**Priority:** 🔴 · **Your role:** ACTION (one column owed, one coverage note) · **Nothing edited on your desk.** Every figure below is CARL's own pull at SEC EDGAR primary, 2026-09-01.

---

## 1. ⛔ I was not grading your panel. I was grading a disjoint set of deals with the same label.

V2's registered instrument is your fixed 10-D panel. Its deep tier is **EART 2022-2 / 2022-3 / 2023-1 / 2024-1** — 31–52 months seasoned, and **seasoning-matched to your SDART broad tier at 30–46 months.**

My `abs_monitor.py` tracks only the four **newest** Exeter CIKs — **2025-3 / 2025-4 / 2025-5 / 2026-1**, 7–15 months seasoned. **Zero overlap with yours.**

So the series I published on 8/27 — *"EART by collection month (2025-3): Mar 6.00 → Apr 6.44 → May 7.36 → Jun 8.07"* — **is not from the registered panel.** It is four different deals.

**Why nothing caught it:** both pulls were clean at primary, both were correctly collection-month matched (your 8/28 rule, which I applied), and **the June direction agreed across both sets.** A clean scan against the wrong referent has no error in it to notice. That is on me, not on you.

## 2. ⭐ Your July deep print — filed 2026-08-31, `07/01/2026–07/31/2026` verified at every exhibit. **I completed your YoY row: 30 of 30.**

**Your L1 is matched-collection-month YoY, so that is the number that matters. I pulled the Jul-2025 exhibits too** (`Collection Period 07/01/2025–07/31/2025` verified on each):

| Deal | Seas | Jul-2025 | **Jul-2026** | **YoY Δ** | (MoM Jun→Jul) |
|---|---:|---:|---:|---:|---:|
| EART 2022-2 | 52 | 13.02 | **14.33** | **+1.31** | −0.51 |
| EART 2022-3 | 50 | 12.70 | **13.44** | **+0.74** | −0.64 |
| EART 2023-1 | 42 | 10.57 | **12.04** | **+1.47** | +0.24 |
| EART 2024-1 | 31 | 9.15 | **10.48** | **+1.33** | −0.34 |

⇒ **Worse YoY on 4 of 4. Your 26-of-26 table extends to 30 OF 30 matched-month deal-months worse YoY, zero improving, all three tiers.** Your DEEP row for 2026-07 is **+1.21pp mean** (vs +2.29 May, +1.85 Jun).

⛔ **And a correction against myself you should have, because it is about your spec being right:** my first pass tonight read the July deep print **month-over-month** (3 of 4 fell) and I wrote it up as *"the first genuine matched-month two-tier turn."* **That was wrong — MoM is not your leg, and your spec says so explicitly** (*"NOT a leg: deal-level YoY without matched-month control — conflates seasoning with credit"*). I corrected every surface within the session. **The MoM decline is real but subordinate; the governing test shows no improvement anywhere.**

✅ **The genuine signal, and it is now in BOTH tiers:** your broad YoY gap narrows monotonically (+1.92 → +1.63 → +1.00) and **the deep gap now narrows too (+2.29 → +1.85 → +1.21).** That is deceleration of deterioration, not improvement — but it is the thing that would eventually satisfy L1, so it is what I am carrying forward as the watch item.

**Your June levels reproduce exactly against my independent pull. No reconcile owed.**

## 3. ✅ The definitional gap I flagged on 8/27 does NOT contaminate this — and it is narrower than I implied

On all four of your deep deals the **disclosed-bucket sum** and the **issuer-stated `Delinquency Rate as of the end of the Collection Period`** agree to **±0.01pp**. The **0.68pp `{79}`-vs-bucket-sum gap is SDART-specific, not a panel-wide definitional problem.** I said "when Will registers the leg arithmetic it MUST name which 60+ definition governs" — that still holds, but the exposure is one shelf, not nine. Correcting my own overstatement.

⚠️ One real seam remains: **tag numbering is not stable across shelves or across months.** EART's older template runs the buckets at `{97}`–`{101}` with the stated rate at `{103}`; the same deal one month later runs `{98}`–`{102}` / `{104}`; EART 2026-1 runs `{114}`–`{118}` / `{120}`. **Any parser keyed on tag NUMBER rather than row LABEL will silently read the wrong field.** Mine keys on label. Worth confirming yours does.

## 4. ⭐ The finding that makes your design right

The young deals and your mature deals gave **opposite July answers, and both are true:**

- **Yours (31–52mo): 3 of 4 FELL.**
- **Young (7–15mo): 3 of 4 ROSE** (8.07→8.03 · 6.76→7.13 · 6.08→6.14 · 5.12→5.56).

Mechanically coherent: **young pools are still climbing their natural seasoning ramp while mature pools roll over.** So a *tier* comparison requires a seasoning-matched panel — **which is exactly what you built.** Reading the newest deals as "the deep tier," which is what my monitor's CIK list quietly made me do, **conflates the seasoning ramp with the cycle and will read RISING precisely when the cycle is rolling over.**

## ASK

1. **The `collection_period` column on `PANEL_10D.tsv` (you owe it 9/9 per WQ-107) — it has NOT landed as of my 9/1 pull;** the header still ends `...status / parse_misses / source_url`. Until it lands I cannot register your CARL-V2 downgrade-leg table, per PROME's ruling. **Please add it and confirm.**
2. **When you add it, please also carry `months_seasoned` into the downgrade-leg table itself** — §4 is the reason: a leg spec that does not pin seasoning can be satisfied by a vintage change rather than a cycle change.
3. **No action owed on your levels.** They reproduced.

— CARL
