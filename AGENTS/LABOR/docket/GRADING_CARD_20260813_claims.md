# 🔒 FROZEN GRADING CARD — Initial Claims w/e Aug 8, 2026
**Print:** Thu 2026-08-13, 08:30 ET (DOL ETA 539) · **Written:** 2026-08-12 ~18:15 ET, **PRE-PRINT** · **Author:** LABOR

> ⚠️ **CARD-TIMING DEFECT, DECLARED NOT BURIED.** C2a says write the card *"when the catalyst is ~1 week out, not on print morning."* **This one is written the day before.** It is still pre-print and every band below is arithmetic on published data, so it does its job — but the lateness is a real miss against my own rule and is logged rather than quietly satisfied. **Cause:** the weekly-claims row is `RECURRING WEEKLY, re-docketed each closeout`, and a recurring catalyst has no natural "one week out" trigger — the card rule was written for *dated* events. **→ BUILD_DEBT (BD-19): the recurring-claims card needs a standing template written once and re-dated, not composed per print.**

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE (FRED/DOL, pulled 2026-08-12 13:33 ET)

| w/e | Initial claims (SA) | 4-wk MA |
|---|---|---|
| 2026-07-04 | 217,000 | 219,250 |
| 2026-07-11 | **209,000** ← **rolls OFF tomorrow** | 214,750 |
| 2026-07-18 | **189,000** | 208,000 |
| 2026-07-25 | **198,000** | 203,250 |
| **2026-08-01** | **199,000** | **198,750** |

**Continuing claims:** 1,801,000 [w/e Jul 25] — **+24K, first rise in 5 weeks** (1,798 → 1,789 → 1,777 → 1,801). Tomorrow prints CC for **w/e Aug 1**.

🔧 **VINTAGE CORRECTION FOUND WHILE FREEZING THIS CARD — both recent weeks revised UP 1K and STATUS had not followed.** STATUS carries **188K** (w/e Jul 18) and **197K** (w/e Jul 25); FRED/DOL now carry **189K** and **198K**. Consequences, all small but stated because a spine token is a spine token: (a) the "lowest since Sep-1969" print is **189K**, not 188K or the original 187K — **it has now been revised up twice**; (b) Kill B's distance is **4K**, not the 3K STATUS states; (c) the "3 of last 5 <200K" claim **survives** at 189/198/199. **Swept into STATUS this session.**

**Derived, and this is the number the whole card turns on: the week rolling off is 209,000.**

---

## §2 — PRE-COMMITTED BANDS (assignments fixed before the print)

Let **X** = initial claims, w/e Aug 8. New 4-wk MA = **(199 + 198 + 189 + X) / 4 = (586 + X) / 4**.

| Band | X | New 4-wk MA | **Pre-committed assignment** |
|---|---|---|---|
| **A** | **X ≥ 250,000** | ≥209.0K | 🔴 **T-01 provisional ARM** (needs a 2nd consecutive >250K to fire) · **T-02 fires only at >300K single.** LAB-03 (7%) repriced UP materially. Vector 13 → 4. **Same-day escalation to CARL + REGINALD.** |
| **B** | **230,000 – 249,999** | 204.0–209.0K | 🟠 "Accelerating" band per KEY THRESHOLDS → **vector 13 → 3.** Apply the premortem before any action. Packet CARL + REGINALD. |
| **C** | **210,000 – 229,999** | 199.0–204.0K | 🟡 **Drift band, but the FIRST MA RISE since June** — report the direction change as information (it is not roll-off-driven; see §3). Vector 13 **holds at 2**. |
| **D** | **200,000 – 208,999** | 196.5–199.0K | ⚪ MA falls again, **mechanically** (§3). Vector 13 **holds at 2** — the `<200K ×4` condition **breaks** at X ≥ 200K and the count **resets to 0**. |
| **E** | **185,001 – 199,999** | 192.8–196.5K | ⚪ **4th consecutive sub-200K print → the pre-registered `<200K ×4` condition FIRES → VECTOR 13 → 1** (floor). Banked so far: 189 / 198 / 199. Kill B **does not** start (X > 185K). |
| **F** | **X ≤ 185,000** | ≤192.8K | ⚪ Vector 13 → 1 **and** **Kill B count starts: 1 of 5.** ⚠️ Kill B is the **bull-side exit-all** check — a low print here counts *against* my book, and I record it as leg 1 of 5 the same day, not later. |

⚠️ **Band E is the modal band and it costs me a vector.** Three of the last three prints land in it. **Vector 13 → 1 means six of fifteen vectors at floor becomes seven**, and the matrix falls **32 → 31/75**. **That is pre-committed here so it cannot be re-argued tomorrow morning**, including by me pointing at the shadow gap — the gap is evidence about the freeze *mechanism*, and **this vector scores realization** (the row says so already).

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED (this is the card's main job)

**The 4-wk MA will decline again for any print below 209,000 — i.e. in bands C, D, E and F — purely because the 209K week rolls off.** It would be the **7th consecutive MA decline**.

> **PRE-COMMITMENT: a 7th straight MA decline in bands D/E/F is NOT reported as new information, in STATUS, in any packet, or to Will.** It is the roll-off arithmetic and nothing else. This is the same trap the 8/7 card caught at decline #6, and it is now two-for-two, which is why it is the first thing on this card rather than a footnote.
> **The inverse is the part that is genuinely informative and is easy to under-report: an MA RISE requires X > 209,000** — a **+10K jump** off the current print. **If band C or worse lands, the MA turning up IS information**, because it clears a roll-off that was working in the other direction. Say so with equal prominence.

**Honest limit, stated now:** the roll-off effect decays after this print — w/e Aug 15 drops the 189K week, which pushes the MA *up* mechanically. **From next week the sign of the mechanical term flips**, so the "MA falling" framing expires by construction. Do not carry it.

---

## §4 — WHAT THIS PRINT DOES **NOT** DO (attribution discipline, both directions)

- ⛔ **It does not resolve the demand-vs-supply attribution.** That is open per my 8/7 grade and stays open until **QCEW 8/28** or **NFP 9/4**. A low claims print is not evidence of supply-shrink, and a high one is not evidence of demand collapse.
- ⛔ **It does not speak to the payroll count.** July printed **−23K with claims at 199K**; the shadow gap is at its cycle-widest. **Another benign claims print widens the gap further and still says nothing about hiring** — firing is not what stopped the count.
- ⛔ **It is not a policy input.** Per the 7/29 FOMC grade, labor is a **satisfied side-constraint** and *"a benign claims print is not hawkish fuel — it is nothing."* **No rate-path read comes off this print from me** (BOND / HENRY / ORACLE own that lane).
- ⛔ **It does not grade CARL's kill rule.** My 4-wk MA is **leg 1 of CARL's full-thesis kill (claims <220K sustained)**, and CARL grades it — **I supply the number and the vintage, not the verdict.** Routed as context.
- ✅ **What it CAN do:** move vector 13, arm/fire T-01/T-02, start Kill B, and reprice LAB-03. Nothing else.

---

## §5 — CONTINUING CLAIMS (separate letter — do not fold into the initial-claims band)

CC printed **1,801K [w/e Jul 25], +24K, first rise in 5 weeks.** Tomorrow prints **w/e Aug 1**.

| CC outcome | Assignment |
|---|---|
| **Rises again (2nd straight)** | 🟠 **The one non-benign thing in this release.** Vector 7 (UI exhaustion / CC grind) **holds at 3** and the drop-to-2 (`<1,750K ×4wk`) is dead for a month+. **Report it as the lead**, not buried under the initial-claims number. |
| **Falls back below 1,790K** | ⚪ One-week noise; the 5-week grind lower resumes. Vector 7 holds at 3 (one tick either way is not a trend — **stated symmetrically, before the print**). |
| **≥1,850K** | 🟠 Genuine break in the CC series → packet CARL + REGINALD; re-examine vector 7 upgrade. |

**Why CC gets its own letter:** it measures *duration of unemployment*, initial claims measure *entry*. They are different layers and a card that grades two instrument types needs a separate baseline for each (**L-09**).

---

## §6 — ROUTING (pre-committed)

- **Bands A/B** → CARL + REGINALD same-day; **A** also HENRY.
- **Band E** → vector 13 floor is an internal move; **no packet** (a vector hitting floor is not a cross-agent signal).
- **CC rising 2nd straight** → CARL (severance/exhaustion timeline).
- **Every band** → the claims figure + vintage to CARL as his kill-rule leg-1 input, **as data, not as a verdict.**

## §7 — DEFECT LOG (fill in at grade time)
*Any outcome this card failed to enumerate gets logged here and moves NO score — the 8/7 temporary-layoff precedent (§6.6 of that card).*

—
*Frozen 2026-08-12 pre-print. Grade off this card band-by-band. `git mv` to `docket/graded/` in the session it is graded, after repointing references.*
