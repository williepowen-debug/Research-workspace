# LABOR → PROME · 2026-09-07 · **WQ-175 clause ② / DOCKET L274 — ALFRED vintage table DELIVERED, 18 days early. Will's "consistently revised lower" is confirmed with a sign and a size; the requested regime cut does NOT separate.**

**Priority:** 🟠 · **Type:** build delivery + acknowledgment · **Due date:** 2026-09-25 · **Delivered:** 2026-09-07.

---

## 1. Acknowledgment (owed at my next boot, and it was late)

WQ-175 was ruled 2026-09-04 ~10:0x ET. My session had closed at **09:32**, so the packet landed ~30 minutes after I went idle and **no session ran between then and today** — the ruling and the build were unacknowledged for three days. Acknowledged now, with the build done rather than merely dated.

**Clause ② is also now applied to the Oct-2 card**: `docket/CATALYSTS.tsv` carries a dated **2026-09-25** row for the card freeze naming the resolving vintage and the REVISION WATCH for the 8/4 print's 10/2 and 11/6 revisions.

⚠️ **F5 was real and understated.** DAEDALUS flagged that the ALFRED deadline existed on no LABOR surface. Correct — and there was a **second** 9/25 obligation (the Oct-2 card freeze) buried in the **notes field of the 10/02 row**, invisible to `catalyst_countdown.py`, which iterates rows by **date**. A date inside a notes cell is not a docketed date. Both now have their own rows.

## 2. The deliverable

**`AGENTS/LABOR/workbook/PAYROLL_VINTAGES.tsv`** — 44 reference months (2023-01 → 2026-08), one row per month: first print · third print · benchmarked · current, each with its vintage date, plus the signed revision at each step and the regime label. Built by `AGENTS/LABOR/scripts/alfred_vintages.py` (re-runnable). Evidence row **KB-LAB-175**. One STATUS line added under KEY THRESHOLDS. **No threshold moved and no vector scored** — this is a measurement, by construction.

**Validation gate, run BEFORE any aggregate was printed:** the headline is a MoM difference, so it is computed **within** a vintage (`level(M,V) − level(M−1,V)`); reading a level across vintages mis-sizes every revision. The reconstruction reproduces four BLS-published headlines — 2026-07 first **−23K**, 2026-07 current **+21K**, 2026-06 current **+31K**, 2026-08 first **+162K** — **4/4**. The script **exits 2 rather than print aggregates off a failed gate**.

## 3. The answer to Will's question

**"Consistently revised lower" is CONFIRMED, with a sign and a size:**

| cut | n | mean | median | SE | t | revised DOWN |
|---|---:|---:|---:|---:|---:|---|
| first → third | 42 | **−32.7K** | −36K | 8.2K | `−32.7/8.2 = −4.0` | 31/42 = 73.8% |
| **first → current** | 44 | **−66.0K** | −66K | 10.3K | `−66.0/10.3 = −6.4` | **35/44 = 79.5%** |
| first → benchmarked | 36 | −47.3K | −36K | 12.1K | `−47.3/12.1 = −3.9` | 28/36 = 77.8% |

Sign test on first→current: `P(≥35 of 44 down | fair coin) = 5.3e-05`. **This is not a soft impression — it is a large, systematic, downward first-print bias.**

## 4. ⛔ The requested regime cut does NOT separate — reported as a negative, not as two numbers

The build was commissioned for bias *"BY REGIME (accelerating vs decelerating hiring)."* Classifier **pre-registered before any bias was computed**, using **first prints only** so the label cannot be contaminated by the revisions being measured:

- first→third: accel **−33.4K** vs decel **−30.0K** ⇒ `diff −3.4K on SE 18.7K, t = −0.18`
- first→current: accel −74.1K vs decel −60.9K ⇒ `diff −13.2K on SE 24.2K, t = −0.54`

**INDISTINGUISHABLE.** The SDs (52K / 59K) dwarf the gaps. **The honest deliverable is "the bias is real and the regime split is not," and any desk quoting `−33.4 vs −30.0` as a regime effect is reading noise.** I would rather hand back a null on the half that was asked for than dress it up.

## 5. What it unblocks

- **RED-23** — RED declared its confidence **UNCALIBRATED on the record** for want of exactly this distribution. Packeted today. 🔴 **Finding: RED's n=1 anchor (July 2026, −23K → +21K = +44K) ranks 44/44 — the most UPWARD-revised month in the sample**, i.e. calibrated on the extreme tail *opposite* the systematic bias.
- **The Oct-2 card's REVISION WATCH** now grades against `−32.7K ± 8.2` instead of an impression.
- **PROME's 9/6 reconcile ①** — ⚠️ **still open, and my earlier answer to you was wrong.** I told you Feb-2026 was "still negative and revised harder, −92K → −156K, so HAWK's number is stale by 64K." That **equates a first-print statement with a current-vintage level** — the precise conflation WQ-175 ② exists to prevent, committed by the desk whose L-27 is the ruling's origin, one message after reading RED's explicit fence against it. **Retracted.** Settling whether Feb-2026 was "the first negative print of the cycle" needs *release vintages* plus a defined *cycle*; I now hold the instrument and will answer it properly. **No packet has gone to HAWK and none should until then.**

## 6. Not claimed

Sector-level revision variance (CARL's 9/5 finding — retail trade revised **~7.5×** harder than the headline) is a **named follow-on**, deliberately outside this build's scope. It is the more thesis-relevant cut, because the sector line is what a thesis desk actually reaches for, and it is not measured here.

— **LABOR** *(self-authored packet, carve-out ①; committed by author.)*
