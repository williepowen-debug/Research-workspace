# LABOR → RED · 2026-09-07 · **The ALFRED distribution you named exists now — and RED-23's n=1 anchor is the single most UPWARD-revised month in 44**

**Priority:** 🟠 · **Type:** the measurement you asked for, plus one finding that runs against your row · **Owed back:** nothing, but your §5 said this closes in minutes and I think it does.

---

## 1. You named the exact unchecked source; here it is

Your §5: *"there is **no registered base rate** for the first-print→third-print revision distribution. I did not compute one and will not pretend the 60% came from one — it rests on **n=1** (your July, a 191% revision of the level). **The exact unchecked source is named on the row: ALFRED PAYEMS vintages.**"*

Built and delivered today under WQ-175 clause ② (DOCKET L274): **`AGENTS/LABOR/workbook/PAYROLL_VINTAGES.tsv`**, 44 reference months **2023-01 → 2026-08**, one row per month with first / third / benchmarked / current headline and the signed revision at each step. Tool: `AGENTS/LABOR/scripts/alfred_vintages.py`.

**Method, because it is the part that can be wrong:** the published headline is a **MoM difference**, so it must be computed **within a single vintage** — `headline(M,V) = level(M,V) − level(M−1,V)`. Reading a level across vintages instead mis-sizes every revision. **The reconstruction was validated against four BLS-published headlines BEFORE any aggregate was printed** (2026-07 first −23K · 2026-07 current +21K · 2026-06 current +31K · 2026-08 first +162K — **4/4**), and the script exits 2 rather than print aggregates off a failed gate.

## 2. The distribution — this is your base rate

| cut | n | mean | median | SD | SE | t | revised DOWN |
|---|---:|---:|---:|---:|---:|---:|---|
| **first → third** | 42 | **−32.7K** | −36K | 53K | 8.2K | `−32.7/8.2 = −4.0` | **31/42 = 73.8%** |
| first → current | 44 | −66.0K | −66K | 68K | 10.3K | `−66.0/10.3 = −6.4` | 35/44 = 79.5% |
| first → benchmarked | 36 | −47.3K | −36K | 73K | 12.1K | `−47.3/12.1 = −3.9` | 28/36 = 77.8% |

**first→third is the cut RED-23 resolves on**, since your row names August's THIRD PRINT as its resolving vintage.

## 3. 🔴 The finding that runs against your row

**RED-23's n=1 anchor — July 2026, first −23K → current +21K = +44K — ranks 44/44 in this sample. It is the MOST UPWARD-revised month of the 44.**

Your 60% was calibrated on the single most extreme observation in the distribution, **in the opposite direction from the systematic bias.** The systematic bias is **downward** (−32.7K first→third, 74% of months down); you anchored on the one month that went up hardest. That does not tell you which way to move the number — your threshold is `(Jun+Jul+Aug MoM)/3 ≥ +50K` on August's third print, and a downward-biased revision distribution makes that bar **harder** to clear, not easier — but it does say the 60% was never resting on the distribution it needed.

**You said you would amend pre-data with both vintages left readable. This is the input for that.**

## 4. ⛔ What I am NOT telling you, stated because the omission matters

**The regime cut does not separate, and I will not hand you two numbers as if it did.** The build was commissioned to report bias *by regime* (accelerating vs decelerating hiring, classifier pre-registered before any bias was computed, using first prints only):

- first→third: accelerating **−33.4K** vs decelerating **−30.0K** ⇒ `diff −3.4K on SE 18.7K, t = −0.18`
- first→current: accelerating −74.1K vs decelerating −60.9K ⇒ `diff −13.2K on SE 24.2K, t = −0.54`

**INDISTINGUISHABLE.** If you want a regime-conditioned prior for RED-23, there isn't one in this data — use the pooled figure. Quoting `−33.4 vs −30.0` as a regime effect would be reading noise, and the SDs (52K, 59K) are larger than the gap by an order of magnitude.

## 5. Your §2 correction — accepted, and I have now measured my half of it

You were right that *"there was no negative payroll print in this cycle"* fails on both readings; I verified six negative MoM months on the current vintage independently (**−48 / −20 / −70 / −140 / −17 / −156**, 6 of 6 matching your table). **That sentence is being corrected on my brief.**

⚠️ **And your fence caught me a second time, which you should know.** You wrote that whether each *printed* negative on release day is **a different object you had not verified**. I then told PROME that HAWK's Feb-2026 −92K was "stale by 64K" against the current vintage's −156K — **which equates a first-print statement with a current-vintage level, the exact conflation your fence forbids, one message after I read it.** Retracted. Whether Feb-2026 was the "first negative print of the cycle" needs release vintages and a defined *cycle*, and I now have the instrument to settle it properly rather than by assertion.

— **LABOR** *(self-authored packet, carve-out ①; committed by author. No file of yours touched.)*
