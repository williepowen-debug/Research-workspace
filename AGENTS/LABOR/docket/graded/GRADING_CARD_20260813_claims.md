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

**GRADED 2026-08-20 ~16:50 ET — 7 days late.** The print landed 8/13 08:30 ET and no session ran until 8/20. **The card did its job; the boot that was supposed to consume it did not happen.** Logged as a process defect, not a card defect: B5b catches an unconsumed card *at the next boot*, and the next boot was a week away. This is the summons gap (BD-02), demonstrated live for the second time.

**No enumeration defects.** Every observed outcome fell inside a pre-committed band. §1's derived pivot (209,000 rolling off) and the band arithmetic reproduced the printed 4-wk MA to the dollar.

---

## §8 — GRADE (written 2026-08-20 off this frozen card)

### 8.1 Initial claims, w/e Aug 8 — **X = 212,000 → BAND C**

| Card said | Actual | ✓ |
|---|---|---|
| Band C = 210,000–229,999 | **212,000** [DOL via FRED ICSA, obs 2026-08-08] | ✅ |
| New 4-wk MA 199.0–204.0K | **199,750** [IC4WSA] | ✅ |
| **Vector 13 HOLDS at 2** | held at 2 | ✅ |
| Matrix 32/75 unchanged | unchanged | ✅ |

**Band E — the modal band — did NOT land, so the pre-committed vector-13→1 (floor) move does NOT execute.** Matrix stays **32/75**. This is the pre-commitment working in the direction that costs nothing: it was written so the floor move could not be re-argued, and it equally forbids taking the move when the band missed.

🔴 **§3's inverse fired, and it is the informative half.** The card pre-committed: *"an MA RISE requires X > 209,000 — a +10K jump off the current print. If band C or worse lands, the MA turning up IS information ... Say so with equal prominence."* **X = 212,000 cleared 209,000 by 3K.** The MA rose 199,000 → 199,750 (**+750**), **ending a six-print decline streak.** Reported at equal prominence per the pre-commitment.

**Kill B: X = 212,000, far above 185,000 → count stays 0 of 5.** No leg banked.
**T-01 / T-02: unarmed** (212K vs 250K / 300K).
**`<200K ×4` condition: BROKEN and reset to 0** at X ≥ 200K, per Band D's clause. Banked run was 189 / 198 / 200 — and see 8.3, the third leg was revised out of qualification anyway.

### 8.2 Continuing claims, w/e Aug 1 — **1,781,000 → §5 "falls back below 1,790K"**

Pre-committed: *"⚪ One-week noise; the 5-week grind lower resumes. Vector 7 holds at 3 (one tick either way is not a trend — **stated symmetrically, before the print**)."* **Vector 7 holds at 3.** ✅

The "+24K, first rise in 5 weeks" that §1 flagged was **one tick and it reversed** (1,799 revised → 1,781, **−18K**). The card's symmetric wording is what keeps this from being written up as a reversal-of-a-reversal; it is noise in both directions. **CC drop-to-2 (`<1,750K ×4wk`) stays dead.** Not ≥1,850K, so no CARL/REGINALD break packet.

### 8.3 🔧 VINTAGE — the second consecutive card to catch a revision STATUS had not followed

**w/e Aug 1 revised 199,000 → 200,000.** Consequences, stated because a spine token is a spine token:
- The **"3 of the last 5 prints <200K"** claim carried on STATUS rows 18/49/76 **is now FALSE** — 200,000 is not <200,000. True count is **2 of 5** (189 / 198), and with the two newest prints it is **2 of the last 5** on any window.
- **§1's own frozen table is off by 1K on its last row** — declared, not corrected (a frozen card is not retroactively edited; the band arithmetic is unaffected because the card computed off the same vintage it froze, and (587+212)/4 = 199.75 reproduces FRED exactly).
- **CC w/e Jul 25 revised 1,801 → 1,799K** (−2K), which shrinks the "first rise in 5 weeks" from +24K to +22K. Immaterial to any band; recorded for the spine.

**This is revision-re-grading under L-15** (fleet convention, Will-ruled 8/12, row 36b — LABOR a named co-party): the threshold is re-graded against the **revised** series, not frozen at publication vintage. **The band call is unchanged under either vintage**, so L-15 costs nothing here — but the compliance is recorded, because the first time it costs something is not the time to be deciding the convention.

### 8.4 The NEXT print (w/e Aug 15 = 206,000) — the card pre-warned it and I am obeying that

§3's honest limit: *"the roll-off effect decays after this print — w/e Aug 15 drops the 189K week, which pushes the MA up mechanically. **From next week the sign of the mechanical term flips**, so the 'MA falling' framing expires by construction. Do not carry it."*

**Confirmed exactly.** MA 199,750 → **204,000**, +4,250. Decomposition: (206 − 189)/4 = **+4.25K — 100.0% of the move is the roll-off swap.** ⛔ **So today's MA rise is NOT reported as information either.** The card earned the right to say this by getting the sign-flip right a week early, and the symmetric application is the whole point: I did not report the mechanical falls, and I do not report this mechanical rise.

**What IS information across both prints, stated plainly:** the *level* has moved. **189 → 198 → 200 → 212 → 206.** The two newest prints are the two highest since w/e Jul 4 (217K), and the sub-200K run is over. That is a ~15-20K drift up off the cycle low — **real, small, and nowhere near any threshold** (T-01 250K, T-02 300K). Vector 13 stays at 2 on both prints.

—
*Frozen 2026-08-12 pre-print. Grade off this card band-by-band. `git mv` to `docket/graded/` in the session it is graded, after repointing references.*
