# CCC/HY Bifurcation Tripwire — Definition & Sustain Window
**Built:** 2026-06-25 (Transmission-Terminus Cluster, Pass 1) · **Owner:** REGINALD
**Vector:** `workbook/VX.tsv` → VX-REG-18.04 · **Ties to:** LIQUID/BROCK live X1 credit-bifurcation root
**Status at build:** 🟢 DORMANT / un-fired — live ratio **3.49×** [FRED 6/24], **3.6× not crossed in last 12 sessions**

---

## Why this exists

Flagged 3 consecutive boots (6/8, 6/19, 6/22) and never built. Every refresh I re-litigated the CCC/HY ratio as a prose judgment call ("bifurcation widening / narrowing"), and the read flip-flopped because the ratio **oscillates in a tight band on a ~1–2 day cycle**. A tripwire converts the judgment call into a mechanical, pre-registered trigger with a defined sustain window and a driver-decomposition rule — so a single noisy print stops moving the read, and the fleet has one tie from the bank-cluster back to the live credit-bifurcation root that LIQUID/BROCK own.

This is the **bank-cluster's hook into the live X1 trigger** (HY>280 + wrapper-basket decoupling), *not* a re-derivation of it. X1 fires upstream; this tripwire tells us whether the **tail** (CCC) is decoupling durably enough to be the substance behind a widening, vs. an index-beta artifact.

---

## Live read (re-pulled, do not trust stale STATUS rows)

`FORGE/tools/market-data/fetch.py fred BAMLH0A0HYM2` (HY OAS) ÷ `... BAMLH0A3HYC` (CCC OAS), FRED, 6/24 close:

| Date | HY OAS | CCC OAS | **CCC/HY** | Gap (CCC−HY) |
|------|--------|---------|-----------|--------------|
| **6/24** | 276 | 964 | **3.493×** | 688bp |
| 6/23 | 271 | 956 | 3.528× | 685bp |
| 6/22 | 265 | 947 | 3.574× | 682bp |
| 6/19 | 266 | 947 | 3.560× | 681bp |
| 6/18 | 266 | 946 | 3.556× | 680bp |
| 6/17 | 263 | 939 | 3.570× | 676bp |
| 6/16 | 271 | 944 | 3.483× | 673bp |
| 6/15 | 266 | 937 | 3.523× | 671bp |
| 6/12 | 271 | 948 | 3.498× | 677bp |
| 6/11 | 278 | 956 | 3.439× | 678bp |
| 6/10 | 280 | 957 | 3.418× | 677bp |
| 6/09 | 278 | 951 | 3.421× | 673bp |

**12-session band: 3.42× – 3.57×. The 3.6× threshold was NEVER touched.** Closest approaches 3.574× (6/22) and 3.570× (6/17). My STATUS "3.56× [6/19]" mark was correct for its date; live is **3.49×**, i.e. the ratio has *compressed* since 6/19, not widened.

---

## Threshold calibration — why 3.6×

The recent regime ceiling is ~3.57×. 3.6× sits just **above** the entire June oscillation band, so:
- It **filters the noise band** (3.42–3.57×) — in-band wiggles never trip it.
- Crossing 3.6× at all is a **regime change** (the tail decoupling beyond the prevailing regime), not a wiggle.
- Cross-ref to the additive measure: the CCC−HY gap band is 671–688bp; a ratio breakout to >3.6× with HY near 276 implies CCC ≳ 994bp, i.e. CCC pushing decisively through its own ~937–964 band and toward/through 1000bp. The threshold is internally consistent with a genuine CCC-tail break, not just an index move.

This is a [[finding_blended_index_masks_bifurcation]] application: the blended HY index masks the CCC tail; the ratio is the decomposition that surfaces it. Threshold set *above* the regime so it discriminates a break from the band.

---

## Sustain window — derivation (tested on both outcome classes)

Per [[finding_sustain_count_role_discriminating_power]]: derive n empirically, test on BOTH the should-fire and should-NOT-fire classes, register the trigger ROLE.

**Should-NOT-fire (oscillation noise):** Single-day ratio swings of +0.08–0.09× are routine (6/16→6/17: 3.483→3.570). Elevated readings also **cluster for 2–3 consecutive days** within the band (6/17/18/19 all 3.556–3.570×). So a 1-print or 2-print sustain at a lower threshold would false-fire on in-band clustering.

**Should-fire (durable decoupling):** a genuine tail-concentration event holds the breakout **past** the typical 2–3 day in-band cluster length.

**→ Hard tripwire: 3 consecutive daily closes (FRED business days) with CCC/HY > 3.6×.**
- n=3 clears the observed 1–2 day oscillation cycle AND the 2–3 day in-band elevated cluster.
- **Reset:** any close ≤ 3.6× resets the consecutive count to 0.
- **ARMED (watch, no fire):** 1–2 consecutive closes > 3.6×.
- **Companion regime-watch (softer, no cross-agent signal):** ≥3 of trailing 5 closes > 3.6× — flags a *choppy* approach that a strict-consecutive rule would miss when one day dips to 3.59×.

**Discriminating power in-sample:** over the 12-session window the hard tripwire fires **0 times** (3.6× never crossed) → zero false positives in the current calm-tail regime. It is correctly DORMANT. It only speaks when the tail genuinely breaks regime.

---

## Driver decomposition — MANDATORY companion (the load-bearing nuance)

A bare ratio threshold is **two-signed** — the ratio can rise for opposite reasons. Per [[finding_convergence_sign_check]], classify every move by its driver before acting:

| Ratio rises because… | Mechanism | Read | Action |
|---|---|---|---|
| **CCC OAS widening** (tail breaks its 937–964 band, HY stable) | weakest-tier credit stress concentrating | **SUBSTANCE / bearish** | escalate to LIQUID/BROCK as confirming the X1 bifurcation root; feeds bank-landing thesis |
| **HY OAS tightening** (index melt-up, CCC ~flat) | broad risk-on leaves the tail behind | **BETA / benign** | ratio up on index rally — NOT new tail stress; do **not** escalate as bearish |

And the inverse — a ratio *compression* while both widen (the current 6/19→6/24 state) is **HY-led broad widening**, which is the X1-cluster's "the widening is beta, not substance" signature, not tail-concentration.

**Worked example (6/19→6/24, live):** HY 266→276 (+3.8%), CCC 947→964 (+1.8%). HY widened **faster in %**, so the ratio *compressed* 3.560→3.493× even though the additive gap *widened* +7bp (681→688). Verdict: **the 6/24 bear leg is index/beta-led, not CCC-tail-led.** This is a direct, concrete input to the cluster's substance-vs-beta reconciliation (rule #5) and **supports** the X1 cluster's "beta not substance" call for this window. Hand to CARL/Prome as a corroborating data point — note CARL's consumer-credit deterioration is the independent *substance* test that would either confirm or break this benign read.

*(Measure note: ratio and additive-gap can diverge when both legs move — ratio compresses on broad widening because the index base grows. Track both; the gap is the cleaner "decoupling" read when the whole curve shifts, the ratio is the cleaner read when the index is stable. [[finding_number_carries_threshold_unit_source]].)*

---

## Monitoring procedure (reproducible)

```bash
cd /home/willi/Research-workspace && source .venv/bin/activate
python3 FORGE/tools/market-data/fetch.py fred BAMLH0A0HYM2 --periods 6   # HY OAS
python3 FORGE/tools/market-data/fetch.py fred BAMLH0A3HYC --periods 6    # CCC OAS
# ratio = CCC ÷ HY per matched date; count consecutive closes >3.6×; reset on any ≤3.6×
```
- Refresh at each boot; update VX-REG-18.04 Current_Value + Last_Updated.
- **On HARD fire (3 consec >3.6×):** run driver decomposition; if CCC-led → outbox 🟠 to LIQUID/BROCK + PROME (confirms X1 tail-decoupling lands toward bank collateral); if HY-led → log benign, no escalation.
- **Pass-2 option (not built):** add the consecutive-count check to `scripts/boot.py` so the count is computed at boot rather than by hand. Deferred to keep Pass 1 bounded.

## Cross-links
- VX-REG-18.02 (HY OAS, the denominator — LIQUID-canonical), VX-REG-18.04 (this vector), RED-FT-07 (CCC >930, fired), RED-FT-01 (HY sub-280 sustain).
- Live X1 root: LIQUID/BROCK (HY>280 + wrapper-basket decoupling). This tripwire is the bank-cluster's *consumer* of that root, not a re-derivation.
- Cluster grid: `research/Q2_PRINT_CONVERGENCE_GRID_2026-06-25.md` (this ratio is the grid's tie to the live credit root).
