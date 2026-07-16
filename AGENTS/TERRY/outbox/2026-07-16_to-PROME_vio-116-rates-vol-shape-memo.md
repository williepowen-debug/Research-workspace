# SHAPE MEMO → PROME → Will [Approve] — GATE-VIO-116 rates-vol hedge (registered consequence)
**From:** TERRY · **Date:** 2026-07-16 (~09:45 ET) · **Gate:** GATE-VIO-116 = FIRED-UNEXECUTED (VIOLET, KB-VIO-116)
**Consequence owed:** fresh rates-vol hedge look → PROME → **TERRY shape memo (rates-vol lane, NOT VIX-calls per Will 7/9)** → Will [Approve].
**Bottom line up front:** **NO ATTRACTIVE STAND-ALONE SHAPE RIGHT NOW.** The rates-vol event already happened (MOVE spiked to 77.77 on CPI day 7/14) and has **round-tripped to 68.48** — buying rates-vol convexity now = paying for vol that just deflated. The rates-short *view* is better (and already) expressed via the armed **TRY-FIRE-004** (same lane). A dedicated VIO-116 hedge would **double-count** that. Re-open only on a MOVE re-escalation.

---

## 1. ⚠️ Fire attribution correction (flag to PROME + VIOLET — ledger vs KB drift)
GATES.tsv records the VIO-116 fire as **"F3: 7/13 DGS10 4.62 > 4.60."** But VIOLET's canonical KB-VIO-116 registers **F3 = "10Y through 4.60 WITH MOVE > 70 before 7/14"** — a **conjunction**. On 7/13, MOVE (1h-bar last-of-day) was **69.55, i.e. <70** → **F3 as VIOLET wrote it did NOT fully fire** (GATES.tsv silently dropped the `MOVE>70` conjunct).

**The gate DID fire — but via F1, not F3.** F1 = "MOVE closes >72.41 (retakes cycle peak) through CPI+1 (7/15)." MOVE printed **77.77 [7/14]** and **75.03 [7/15]**, both >72.41 → **F1 FIRED cleanly on 7/14–7/15.** So the consequence is genuinely owed; only the *attribution* in GATES.tsv is wrong (F3/rates → should be **F1/MOVE-peak-retake**). Recommend PROME correct the GATES.tsv VIO-116 state note. *(MOVE 7/13–7/15 prints are 1h-bar last-of-day; ±1-day label caveat per VIOLET's KB — the ordinal fact [spike through 72.41 on/around CPI, now faded] is robust across both label models.)*

## 2. The rates-vol tape (why "fade" undersells it — it round-tripped)
| Date | MOVE | Source | Note |
|---|---:|---|---|
| 7/8 | 72.41 | daily | prior cycle peak |
| 7/10 | 69.55 | daily | last clean daily row |
| 7/13 | 69.55 | 1h-bar | <70 — F3 conjunct fails here |
| 7/14 (CPI) | **77.77** | 1h-bar | **>72.41 → F1 fires**; spiked on a COOL CPI (two-way rate uncertainty + Hormuz/oil) |
| 7/15 | 75.03 | 1h-bar | still >72.41 |
| 7/16 | **68.48** | live | round-tripped; below the 70 "escalation-live" marker; approaching (not at) N1 stand-down (<66) |

The vol spike was **real and sharp** (through the cycle peak) but is **already deflating**. VIX 16.17 (+3.2% today) still cycle-calm. This is the classic post-event vol crush: **the hedge is being requested after the move it was meant to hedge.**

## 3. Honest read on a SHORT-rates / rates-vol hedge shape
The VIO-116 lane per Will (7/9) is **rates-vol / duration-tail, NOT VIX-calls**. Candidate listed shapes and my verdict:

| Shape | What it is | Verdict now |
|---|---|---|
| **TLT put / put spread** | directional short-duration + convexity (listed) | **This IS TRY-FIRE-004 (armed today).** A separate VIO-116 version double-counts. |
| TLT straddle/strangle | pure long-rates-vol (pays on realized move either way) | **Poor now** — buying long vol *after* MOVE deflated 77→68; theta bleed into a calming tape. |
| Payer swaption / rates-vol convexity | the institutional duration-tail expression VIOLET references | **Out of venue** — not accessible on Will's listed-options broker; flag if that changes. |
| /ZB, /ZN futures-options | cleanest listed rates-vol proxy | **Venue-gated** — only if Will trades Treasury-futures options; otherwise N/A. |
| TBT / PST (inverse UST ETFs) | directional short duration, **no convexity**, decay | Not a vol hedge; rejected for this lane. |

**Conclusion:** the only clean, accessible, in-lane rates-vol shape is a **TLT put/put-spread — which is already the armed TRY-FIRE-004 card.** There is no *second, distinct* rates-vol hedge worth putting on right now:
1. **Vol has deflated** (77→68.48) — long-vol convexity is being bought late/expensive-relative-to-signal.
2. **It double-counts.** VIOLET's own KB §4 names "TERRY's live card from the 7/9 disposition" as the vehicle reference — VIO-116 and TRY-FIRE-004 are the **same duration-short/rates-vol lane.** Running both = doubling duration-short risk under one thesis.

## 4. Registered consequence — satisfied
The shape memo is the owed deliverable and it is delivered: **the rates-vol hedge collapses into TRY-FIRE-004** (armed, separate packet). No stand-alone VIO-116 packet is warranted at 7/16 marks. **This is a valid "no attractive shape right now" conclusion, not a punt** — the vol event round-tripped and the rates-short view is already expressed.

**Re-open a dedicated rates-vol hedge look IF:** MOVE re-escalates **>70 (VIOLET's escalation marker) or >72.41 (F1 re-fire)** with the 10Y sustaining ≥4.60 — i.e., the rates-vol channel re-accelerates rather than continuing to bleed toward N1 (<66). At that point a TLT put-spread or (if venue available) a payer/futures-option shape becomes live and non-redundant.

## Decision
[ ] ACKNOWLEDGE — fold VIO-116 into TRY-FIRE-004, no separate hedge now (Terry rec)
[ ] REQUEST a stand-alone shape anyway (I'll build a TLT put-spread variant sized to $500, flagging the double-count)

**APPROVAL REQUIRED for any packet — Will must approve/reject before execution. TERRY never executes.**
