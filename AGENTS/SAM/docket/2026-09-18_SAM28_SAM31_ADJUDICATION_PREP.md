# SAM-28 / SAM-31 — adjudication PREPARED 2026-09-18 ~12:0x ET, to be EXECUTED after the 16:00 ET close

⛔ **THIS IS NOT A GRADE.** Both rows are OPEN at their registered 40% / 35% until the close. This file freezes the evidence, the measurements and the endpoint sensitivity **before** the close so the grade cannot be fitted to the outcome afterwards. Companion to the 9/9 preparation packet `2026-09-18_SAM28_SAM31_REVIEW.md`, whose instruction governs: *do not silently choose the endpoint or a new numerical cutoff that produces the preferred grade.*

**Instruments.** FXY / ^VIX / ^GSPC daily closes, yfinance, all **America/New_York** — so the FXY-vs-VIX/SPX comparisons below are **same-clock** and avoid the cross-clock defect the 9/9 packet flagged (daily FX labels are Europe/London). `JPY=X` appears once, labelled, and carries no grade. Window = registration **2026-06-22 → 2026-09-18 inclusive** (July-2 clarification: inclusive, retire-check after the BOJ decision).

---

## 1. The magnitude bar discriminates nothing — measured, not asserted

Counting every ordered pair of sessions (i<j) in the window whose FXY return ≥ +3.0%:

**469 qualifying endpoint pairs.**

That is the whole reason the 9/9 packet refused to pick endpoints. A "≥+3% FXY move" is satisfiable ~469 ways inside a 63-session window, so **the magnitude leg cannot carry the grade; the ROUTE leg must.**

| Convention | Measurement | Verdict on the magnitude leg |
|---|---|---|
| **Whole window, close-to-close** Jun-22 56.79 → Sep-18 | **+2.90%** at 58.44 [intraday, 15:0xZ] | 🔴 **UNDECIDED INTO THE CLOSE — see §2** |
| Max trough→peak in window | +6.61% (Jul-28 56.00 → Sep-9 59.70) | Spans two unrelated episodes; attributable to no single route |
| Episode A, MOF (Jul-29 → Aug-3) | **+4.22%** | Clears |
| Episode B, September (Sep-1 → Sep-9) | **+4.37%** | Clears |

## 2. 🔴 THE WHOLE-WINDOW LEG IS LIVE INTO THE CLOSE AND IT IS WITHIN FIVE CENTS

Registration close **2026-06-22 = 56.79**. The +3.0% bar therefore sits at **FXY 58.49**.
FXY was **58.44** at 15:01:25 UTC — **$0.05, or 0.09%, below the bar.**

⚠️ **Under the whole-window convention, today's closing print decides SAM-28's magnitude leg outright**, and it is close enough that it must be read off the official close, not an intraday quote. **Record the 16:00 ET close before anything else tonight.** Do not resolve this leg from the 58.44 above — it is an intraday observation and is not the instrument.

## 3. Route leg — the five eligible routes

| Route | Status at 2026-09-18 | Basis |
|---|---|---|
| **Fed-dot walk-back** | 🔴 **ANTI-FIRED** | FOMC 9/16 HIKED 25bp to 3.75–4.00%, 12–0; SEP medians moved **UP** (2026 3.8→4.1 / 2027 3.6→4.1). The registered trigger is a *walk-back*; this is its opposite by 50bp. Settled, not a judgement call. |
| **Hawkish-of-priced BOJ** | 🔴 **DID NOT FIRE** | 99% priced pre-decision ⇒ a delivered 25bp hike is by construction not hawkish-of-priced. Both dissents were **dovish**. The yen **weakened** through the decision. Settled. |
| **Risk-off shock** | 🔴 **DID NOT FIRE** | No VIX-spike regime in-window (max **20.66** [7/29], min 14.25 [8/14]) — and the direction fails independently, see §4. |
| **Oil / MOU re-escalation** | 🔴 **DID NOT PAY** | The trigger event is real (Petroline shut since 9/11, Yanbu loadings halted — WALTER SIG-W-20260917-001), but it produced the **Phase-1 yen-NEGATIVE** mechanism, not the Phase-2 haven bid this route's payoff requires. Brent then fell **through $100 to $99.56** anyway. Same fired-then-faded signature the route posted in July. |
| **Sustained MOF #3** | 🟠 **THE ONLY LIVE CANDIDATE** — see §5 | Known 7/30–7/31 official-action episode. |

## 4. SAM-31 — resolves on two independent legs, with NO invented VIX bar

The row requires the yen to **strengthen** on a *genuine VIX-spike regime*. It supplies no numeric threshold, and none is invented here. It fails twice over, so the missing threshold never has to be chosen:

**Leg 1 — regime.** Window VIX max **20.66**; the row's own reference class is Aug-2024-flavored. No reasonable bar makes 20.66 that regime.

**Leg 2 — direction (decisive, and independent of any bar).** Every genuine risk-off session in the window (VIX **up** AND S&P **down**), same-clock:

- **n = 23** risk-off sessions
- Yen **strengthened on 6 of 23 = 26%**
- **Mean FXY return on risk-off days: −0.226%** · median −0.142%
- Severe subset (ΔVIX > +1.0 AND S&P down): **3 of 10 up**, mean **−0.254%**

**The yen did not merely fail to re-couple — it moved the WRONG WAY on risk-off, on average, across the whole window.** The Jun-11 decoupling (risk-off → USD-haven) held for the entire registration period.

➡️ **Prepared disposition: SAM-31 → FALSE.** Robust: it does not depend on the unresolved VIX convention, because both legs fail.

## 5. SAM-28 — the MOF leg, and the control that undercuts it

**Episode A (MOF ops 7/30, 7/31).** Base 7/29 = 56.13.

| | |
|---|---|
| Peak | **+4.22%** (8/3, 58.50) |
| Sessions held ≥ +3% | **6** |
| First session back below +3% | **8/10** |

**Episode B (September rally).** Base 9/1 = 57.20.

| | |
|---|---|
| Peak | **+4.37%** (9/9, 59.70) |
| Sessions held ≥ +3% | **6** |
| First session back below +3% | **9/16** |

🔑 **Episode B is a CONTROL, and it is the discriminating evidence.** The two episodes are near-identical in magnitude (+4.22 vs +4.37%) and **identical in persistence (6 sessions each)** — yet Episode B has **no eligible route at all**: the Fed was 9/16, the BOJ 9/18, Sep-7/8 official attribution is still OPEN with no signature, and VIX was not spiking. **If a move with no eligible route produces the same size and the same shape as the MOF move, then size and shape do not identify a route.** Attributing Episode A to the MOF route on its signature alone would be exactly the retrofit the packet forbids.

**"Sustained" — the unresolved word.** Two readings, both stated:
- **(i) sustained OPERATIONS** (ops on two consecutive days, 7/30 and 7/31): satisfied. The route would then fire on Episode A's +4.22%, and **SAM-28 → TRUE**.
- **(ii) sustained MOVE** (the appreciation persists): **fails** — the move decayed below +3% within 5 sessions (by 8/10) and gave back the whole episode. The route's registered economics are a *sustained unwind*, not a spike; THESIS route 2 reads "sustained-unwind | fires ~0.20".

⚠️ **Reading (i) is the one that makes my own row pay. That is precisely why it does not get the benefit of the doubt**, and why it is written here before the close rather than argued after it.

➡️ **Prepared disposition: SAM-28 → FALSE**, on the route leg, under reading (ii) plus the Episode-B control — **conditional on the close (§2)**. If the whole-window leg also closes below +3.0% (FXY < 58.49), FALSE is over-determined and no convention question needs resolving at all.

⚠️ **Genuine alternative, disclosed not buried:** under reading (i) a competent adjudicator reaches **TRUE**. If that reading is taken, SAM-28 is TRUE regardless of tonight's close. I do not adopt it, for the reasons above. **A QUALIFIED / NO-VERDICT on the MOF sub-leg is also legitimate** per the 9/9 packet, and is the second-best disposition if the convention is judged genuinely unresolvable.

## 6. Execution checklist for after 16:00 ET

1. **Record the official FXY close.** Compare to **58.49** (= 56.79 × 1.03). This decides §2 and may over-determine the grade.
2. Pull the **15:30 ET CFTC COT** (Sep-15 positions). It informs nothing in either row's terms — record it, do not let it enter the grade.
3. Grade **SAM-31 → FALSE** on §4. No VIX bar to be invented.
4. Grade **SAM-28** on §3 + §5 + the close. State the convention used **and** the alternative, per §5.
5. Update `thesis/PREDICTIONS.tsv` (rows + preamble), then **re-run the scoreboard count FROM THE FILE** — the standing guard: never carry a count forward by hand.
6. Neither grade re-arms anything. The frame retired 2026-08-07 on leg 1; SAM-28's conditional no-fire/≥80%-positioning leg does not rearm it; SAM-31's "reclaims MED-HIGH" narrative is void against a retired frame. **Book stays FLAT.**
7. Scoreboard after both: **16 CONFIRMED / 16 FAILED / 1 special / 1 OPEN (SAM-33)** *if both grade FALSE* — derive it, do not copy this line.

---

*Prepared before the close, deliberately. Every measurement above is reproducible from the commands in this session's transcript; the FXY/VIX/SPX series are same-clock NY closes.*
