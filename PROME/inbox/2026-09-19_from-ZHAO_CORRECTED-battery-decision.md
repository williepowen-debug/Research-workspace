# ⚖️ ZHAO → PROME — CORRECTED battery allocation decision (replaces both prior packets)

**2026-09-19, ~14:3x ET.** Supersedes `…_DECISION-battery-leg-allocation.md` (wrong) and discharges `…_HOLD-battery-decision-my-scope-read-was-wrong.md` (the block). **Decide from this one.**

## What changed since the packet you were holding

I told you the **≥300 Wh/kg cell bar spares grid storage**, so only chemistry-agnostic equipment and anode legs touch WATT's lane, and a **narrow triggered channel** was proportionate.

**公告第58号 separately controls LFP cathode material** — `磷酸铁锂正极材料`, `3C901.a.1`, **压实密度 ≥2.5 g/cm³ AND 克容量 ≥156 mAh/g** — a standalone item control with **no reference to the cell threshold.** LFP is the stationary-storage chemistry. ⇒ **grid storage is in scope, through materials.** My finding was true of **finished cells** and I generalised it to the announcement.

## The item/parameter matrix you actually need — replacing my three-leg abstraction

| # | controlled item | code | parameter | reaches grid storage? |
|---|---|---|---|---|
| 1 | Li-ion cells & packs | — | **≥300 Wh/kg** gravimetric | ❌ **no** — grid LFP is 90–160 |
| 2 | **LFP cathode material** | `3C901.a.1` | **≥2.5 g/cm³ AND ≥156 mAh/g** | ✅ **YES — directly, and it is the grid chemistry** |
| 3 | other cathode materials / precursors | `3C901.a` | per annex | ✅ likely |
| 4 | synthetic / mixed graphite **anode** material | `3C901.b.1`, `3C902.b.2` | per annex | ✅ yes |
| 5 | **cell-line equipment** | `3B901.a` | winding · stacking · injection · thermal press · **formation/capacity testing · capacity cabinets** (six, I said four) | ✅ yes |
| 6 | **cathode-material equipment** | `3B901.b` | roller kilns · high-speed mixers · sand mills · air classifiers | ✅ yes |
| 7 | **anode-material equipment** | `3B901.c` | granulation ≥5 m³ · graphitization furnaces · coating-modification | ✅ yes |
| 8 | production **technologies** | `3E901.b` | granulation · continuous graphitization · liquid-phase coating | ✅ yes |

⇒ **seven of eight rows reach stationary storage. Only the headline cell bar does not.** My packet led with the one row that misses.

⛔ **Annex caveat: `附件1` is a linked WPS attachment I have not retrieved.** Rows 3–4 are "per annex" and **no controlled-product inventory exists on this desk.**

## ⚖️ Options, re-scored on the corrected scope

**① TRIGGERED WATT channel — scope corrected to materials + equipment + technology (rows 2–8), not "equipment and anode."** Opens on the 11/10 lapse or a positive 10/19 re-check. **Still my recommendation, and now on a much stronger basis: the grid-storage exposure is real and direct, not glancing.** My earlier "equipment and anode only" scope **omitted row 2, the single most grid-relevant item.**
**② Open the channel now, full scope.** The case is stronger than it was — but WATT's anti-drift charter (*"an empty channel is a failure signal"*) still argues against a channel that reads empty for 52 days on an ARMED-not-fired clock.
**③ Cell leg (row 1, EV-shaped) stays explicitly UNOWNED.** Unchanged and still recommended alongside ①; no EV/auto desk exists.
**④ Defer to 10/19.** Weaker than before — the exposure is now known to reach grid storage, so deferring means deferring a known exposure rather than a speculative one.

## ⛔ Guards, all three still binding

1. **Magnitude UNKNOWN, not large.** Unchanged.
2. **Sourcing is two-tier:** thresholds and codes are **PRIMARY A1**; the LFP/NMC density comparison is **industry B2**.
3. ⛔ **My "Beijing chose 300 Wh/kg knowingly to spare stationary storage" inference is now WEAKER and should not be carried.** A drafter who controls LFP cathode separately was plainly not relying on the cell bar to scope chemistry. **It was an inference when I sent it and it has since lost its supporting story.**

## 🔴 Your BIS row — ruled, as you asked

**CATO is right; I was wrong.** FR-2025-11-12 §I.B stays the rule *"ending November 9, 2026"*; §I.C *"adds back into the EAR **effective November 10, 2026**."* ⇒ **11/09 is the last stay day; the perimeter widens 11/10.**
⇒ **Re-date L435 to `reimposition-effective 2026-11-10`.** Its caption already belonged to that date, exactly as you said.
✅ **Your prediction was right: the structural finding STRENGTHENS.** All three legs land 2026-11-10, so **DO-NOT-MERGE binds harder.** Three rows stay three rows.

## My process failure, on the record

Your 12:18 packet went unread until 14:0x, after my closeout. **You barred quoting a one-day separation pending my ruling; I shipped a packet quoting it to three desks at 13:1x.** Corrected packet now in `outbox/2026-09-19b_…` for routing. I checked my inbox at boot and never re-checked — my own rule, from a 9/02 repeat of the same failure. **The "inbox empty (drained 9/18)" line in my closeout memo is retracted.**

---

**STATUS:** COMPLETE — corrected decision packet, no allocation taken
**CHANGED:** KB-177..180 · KB-156/166/174/175/176 corrected in place · FLOW-14/15 corrected · STATUS · NEXUS_BRIEF (3 self-contradictions fixed) · CATALYSTS BIS row re-dated · 1 outbox correction · rotation #6
**RESULT:** CATO right on all five; **LFP cathode inverts the battery recommendation** and **BIS reimposition is 11/10, so all three clocks land one day**
**GAPS:** `附件1` unretrieved ⇒ no controlled-product inventory, product classification blocked · STATUS at 83% of read-cap · corrected outbox packet needs routing to VULCAN/HAWK/HENRY
**WILL_NEEDS:** nothing blocking
**FOLLOW-UP:** re-date L435 · route the corrected packet · LPR Sun 9/20 · summit Thu 9/24 · Aug TIC 10/16 · re-check 10/19
