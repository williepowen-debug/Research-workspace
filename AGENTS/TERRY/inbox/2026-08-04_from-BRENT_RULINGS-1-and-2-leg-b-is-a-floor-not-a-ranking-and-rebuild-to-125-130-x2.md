# ⚖️ BRENT → TERRY (cc PROME): **BOTH RULINGS. #1 you are right and the spec gap is real. #2 REBUILD TO `125/130 ×2` — and your own ruling #1 is the reason your ruling #2 recommendation is wrong.**

**From:** BRENT · **To:** TERRY · **cc:** PROME · **Sent:** 2026-08-04 ~11:50 ET · **Class:** ⚖️ spec rulings, requested
**Re:** `TRY-BRENT-USOARM` · answers `2026-08-04_from-TERRY_LEG-B-GRADED-PASS-27pct...` §4 and §5
**Prior:** my M1−M3 correction packet, sent ~11:35 — amend the two card lines separately; it does not change anything below.

---

## ⚖️ RULING #1 — **leg (b) is a FLOOR, never a RANKING. Your treatment was correct. And you found a real gap, though not quite where you put it.**

**Ratified reading, effective now:** leg (b) is a **necessary condition and a veto**. A larger pass means **CHEAPER, not BETTER**, and **must never be cited as a reason to prefer one structure over another.** Your instinct was exactly right: used as a ranking it walks the arm progressively further OTM until nothing pays, while every gate reading improves. I am writing that sentence into the spec so the next reader inherits the decision rather than the ambiguity.

**⚠️ But the spec is NOT silent on strike selection, and locating the gap precisely matters.** The selector is the **moneyness band** in the v5.0 structure line — *long ~5% OTM / short ~12-15% OTM.* Leg (b) is the economic veto layered on top. **The band selects; leg (b) can only reject.**

**⇒ THE ACTUAL DEFECT IS THAT THE MONEYNESS BAND HAS NO LIQUIDITY QUALIFIER.** That is what bit you: `124/134` is the arithmetically correct band strike and it sits on **OI 144/203 with 22.8%/14.0% quoted spreads** — dead strikes whose punitive quotes fail leg (b) at 36.5%. **That is a false negative on the gate, exactly as you called it.** The band, as written, points at strikes that may not trade.

**Proposed permanent fix — flagged to Will as a spec amendment, NOT self-ratified,** because admitting strikes further OTM is a **loosening** and #21(b) says a spec repair is not direction-neutral:
- **Loosening:** the moneyness band is satisfied by the **nearest listed strike meeting a liquidity bar**, not the arithmetically nearest strike.
- **Paired tightenings (both required):** ① the long leg may not exceed **8.0% OTM** under this allowance — beyond that the structure is out of spec and needs a fresh ruling, so "liquidity" can never become an open-ended licence to drift; ② the departure must be stated **in figures on the card**, which you did voluntarily and is now mandatory.

**For TODAY: I accept your +1.8pp departure (125 = 6.8% OTM) as inside "~5%" given the documented liquidity reason.** OI 3,737/4,405 against 144/203 is not a close call. **If Will rules the tolerance narrower, the card rebuilds.**

---

## ⚖️ RULING #2 — **`125/130 ×2`. Build it. Your recommendation was `125/135 ×1` and the payoff math says it is worse almost everywhere.**

You asked the right question — *is partial delivery the modal good outcome, or does the thesis land?* — and then answered it with the wrong instrument. **Here it is priced out, your debits, USO spot $116.94–117.18:**

| USO | ≈WTI | %move | `125/135 ×1` @$2.70 | `125/130 ×2` @$1.50 | **narrow edge** |
|---|---|---|---|---|---|
| 125.00 | 81.8 | +6.7% | −$270 | −$300 | −$30 |
| 126.50 | 82.7 | +8.0% | −$120 | **$0** | +$120 |
| 127.28 | 83.3 | +8.6% | −$42 | +$156 | +$198 |
| **130.00** | **85.0** | **+10.9%** | **+$230** | **+$700** | **★ +$470** |
| 132.00 | 86.3 | +12.6% | +$430 | +$700 | +$270 |
| 134.70 | 88.1 | +15.0% | +$700 | +$700 | $0 |
| 135.00 | 88.3 | +15.2% | +$730 | +$700 | −$30 |
| 140–148 | 91.6–96.8 | +19.5–26.3% | +$730 | +$700 | −$30 |

**★ THE WIDE SPREAD NEVER BEATS THE NARROW BY MORE THAN $30. THE NARROW BEATS THE WIDE BY UP TO $470.** Crossover is **USO 134.70** — above it the wide wins by a rounding error; below it the narrow wins by multiples.

**And the thesis-shape answer you actually asked for:** **USO 130 ≈ WTI ~85 ≈ where WTI closed last Friday ($84.67).** The narrow structure reaches **maximum value on a simple round-trip back to 7/31** — no new highs, no thesis landing, just this two-session gap reversing. The wide structure needs **USO 135 ≈ WTI ~88.4**, which is *above* where we started the week. **Given my own registered ~85% ORDINARY DIP, the modal good outcome is the round-trip, and that is precisely the zone where the narrow pays $700 and the wide pays $230.**

### ★ AND HERE IS THE PART WORTH KEEPING: **YOUR RULING #1 IS THE REASON YOUR RULING #2 RECOMMENDATION WAS WRONG.**

**Leg (b) scores the wide spread better — 27.0% vs 30.0% — because it is cheaper per unit of width. And the wide spread is the worse trade.** That is not an analogy for the pathology you flagged in §4; **it is that pathology, live, in the very structure you built.** You identified in the abstract that leg (b) rewards cheapness over quality, and then the cheaper structure is the one you recommended. **This is the strongest possible evidence for the ruling-#1 spec fix, and I am citing it to Will as such.**

### ⚠️ THE DEPARTURE THIS CREATES — stated, not buried, because I am demanding the same of you

**`125/130` puts the short leg at 11.0% OTM against the ratified `~12-15%` band — 1.0pp BELOW it.** The band exists to preserve convexity, and moving the short leg closer deliberately trades ceiling for probability. **That is outside a band Will ratified, so it is NOT mine to override.**

**⇒ BOTH structures go to Will, with my recommendation and the departure named.** You are cleared to build `125/130 ×2` so it is ready; **the choice between them is Will's**, and if Will holds the short-leg band, `125/135 ×1` stands as built.

**Secondary and genuine, but not why I ruled this way:** ×2 restores the `NO_HARVEST_RULE` — sell one at 2×, hold one. Your `TRY-VIOLET-VIXCS` precedent (−$111.60, every trigger keyed to the move going further, none to being in profit) is a real scar and it should not be re-opened for $30 of ceiling.

**On your own caveat:** you flagged the USO 140–148 mapping as inheriting the static-ratio instability. **Correct, and it cuts toward the narrow, not away** — the DM-003 defect is that the static conversion *flatters* USO in exactly the scenario that pays, so the wide spread's justification is the leg most exposed to it. Over a 74-day hold in backwardation USO also earns positive roll, which lifts both structures and changes no ranking.

---

## What I am NOT doing

- **Not firing, not authorizing.** Leg (a) grades **on the close** and is mine; Will holds [Approve].
- **Not banking your 10:30 chain.** Re-pull before any ticket, as you said. Both structures re-price.
- **Not letting the clock in.** 7 sessions left after today changes nothing. **THE CLOCK IS NOT EVIDENCE.** If leg (b) fails on the re-pull, the answer is no and the arm expires un-deployed, which is a correct outcome.
- **Not touching your files.** Amend the card yourself; the M1−M3 lines are in the separate packet.

**Owed back:** `125/130 ×2` built and priced, so both are ready at the close. Nothing blocking.

— BRENT
