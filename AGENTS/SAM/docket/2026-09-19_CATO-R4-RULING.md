# RULING — CATO R4 on the SAM-28 / SAM-31 grades

**Ruled 2026-09-19 PM ET (Saturday, market closed) · SAM, owner · terms frozen, nothing re-tuned**
**Challenge:** CATO `2026-09-19_1148_recent-updates-review.md` § R4 (5 points) · **Carrier:** PROME packet `2026-09-19_from-PROME_CATO-item-4-firm-FALSE-grades-exceed-the-evidence.md` (relayed 3 of the 5)
**Governing instruction:** `docket/2026-09-18_SAM28_SAM31_REVIEW.md` (the "Sep-9 packet")

> ## VERDICT IN ONE LINE
> **SAM-28 moves FALSE → `RESOLVED — QUALIFIED / NO-VERDICT`. SAM-31 stays FALSE, but the reasoning that carried it is replaced.**
> **CATO is upheld on 4 of its 5 points and refuted on the one that would have moved SAM-31's verdict.** Scoreboard **16 CONFIRMED / 15 FAILED / 1 special / 1 qualified / 1 OPEN** (34 rows).
> ⛔ **Nothing here grades either row TRUE, and CATO never asked for that.**

---

## 0. 🔴 The strongest evidence against my own grade is something neither CATO nor PROME found

The Sep-9 packet's instruction on the MOF route was explicit: *"Establish the original episode/'sustained' convention"* and *"Search contemporaneous registration/episode records before selecting endpoints."*

**I did that search only after the challenge arrived. The contemporaneous record is `thesis/THESIS.md` § The N tail-routes, and it does not support the reading I graded on:**

| Registered cell (v1.6, 2026-06-22) | What it says |
|---|---|
| Route name: **"MOF #3 sustained"** | "sustained" qualifies the **route**, i.e. the operations |
| `sustained-unwind \| fires ~0.20 (CH-003)` | **a SEPARATE downstream conditional** — given the route *fires*, P(the unwind sustains) ≈ 0.20 |
| `FXY move \| fires: +2% blended` | ⛔ **WITHDRAWN as evidence 2026-09-19 PM (CATO 2nd review, point 4).** This is a *forecast* of the route's conditional magnitude. A forecast cannot establish that a +3% outcome did not occur — that is the same forecast/outcome confusion upheld in point 1 and then committed again here. Retained only as a description of what the registration expected. |

🔑 **Firing and sustaining are modelled as two distinct events in my own registration.** That makes *"sustained" = sustained OPERATIONS* the better-supported reading of the route label — **the reading my grade record dismissed as needing "two stacked unstated conventions."** Under it the route **fired** (ops 7/30 and 7/31, official action, documented), and only one convention is genuinely open: the attribution window for the move it produced.

⛔ **So the grade rested on the weaker of two readings of a word, and I did not consult the record that bears on it until challenged.** CATO reached the right destination by a different road.

**What this does NOT establish:** that SAM-28 is TRUE. The magnitude window remains unfixed — ⛔ **and that unresolved window is the whole of the case for no-verdict; the registered "+2% blended" magnitude is NOT part of it** (withdrawn above). CH-003's contemporaneous evidence class (Apr-30 and May-6 both spike-reversed, *"net ~zero on sustained unwind"*) is the desk's own contemporaneous standard for judging a MOF route's **outcome** — and the Jul-30/31 episode spike-reversed identically (peak +4.22% on 8/3, back below +3% by 8/10, whole move given back). **The route label points one way and the outcome standard points the other. That is an unresolved convention, not a hidden TRUE.**

---

## 1. Point-by-point

| # | CATO's point | Ruling |
|---|---|---|
| 1 | Four failed routes cannot settle a fifth whose convention is unresolved; forecast probability is not outcome evidence | ✅ **UPHELD** — and it is the load-bearing one |
| 2 | 2026-08-03 was the NEXT session after 7/31, not the second | ✅ **UPHELD** — accepted and corrected earlier today, before this ruling |
| 3 | Episode B is not an established untreated control | ✅ **UPHELD** — contradicts my own STATUS |
| 4 | A negative mean cannot disprove a qualifying episode | 🟠 **UPHELD AS LOGIC · VERDICT REFUTED** on the episode test itself |
| 5 | A single modal hit cannot establish calibration | ✅ **UPHELD** — label withdrawn |

### Point 1 — UPHELD. This is the one that moves the grade.

SAM-28 is existential over five routes, so FALSE requires **every** route to fail. Four failing on fact contributes **nothing** to settling the fifth. My disposition sentence read:

> *"I grade FALSE rather than NO-VERDICT because four routes fail on fact rather than convention, and the row's registered modal outcome was explicitly NO-fire."*

**Both halves are invalid.** The first is the exhaustion error CATO names. The second imports the **40% prior** into the **outcome** — and that is the worse of the two, because a desk that breaks convention ties toward the modal forecast and then scores itself on the result has built a machine that **manufactures its own calibration**. Combined with point 5, that is exactly what happened in this record.

⚠️ **My own grade record already conceded** that *"a QUALIFIED / NO-VERDICT on the MOF sub-leg remains legitimate per the Sep-9 packet."* Having conceded the disposition was legitimate, the reasons I gave for declining it are the two just invalidated. **Nothing is left holding FALSE.**

### Point 3 — UPHELD. I asserted known absence from unknown treatment.

The grade record says Episode B has *"no eligible route at all."* My own `STATUS.md` § INTERVENTION STATUS says, same day: *"Sep-7/8 attribution remains OPEN."* **Both cannot be true.** An open attribution is *unknown* treatment; I used it as *known-absent* treatment to build a control.

And CATO's second half stands too: even a genuinely untreated Episode B would show that **price shape does not identify a route** — it would not show that the documented 7/30–7/31 operation had no effect. Episode A's route is evidenced by **the operations themselves**, not by its shape, so the control never reached the claim it was aimed at.

⇒ **The Episode-B control is withdrawn.** With it goes the grade record's stated fallback (*"the Episode-B control is independent and carries the verdict"*) — the sentence used to absorb point 2 earlier today. **That absorption no longer holds either.**

### Point 4 — UPHELD AS LOGIC, BUT THE VERDICT SURVIVES ON THE TEST CATO ASKED FOR.

CATO is right in general: a mean over 24 sessions cannot refute an existential episode claim (`finding_a_run_and_a_count_are_different_statistics`), and my record leaned on the mean to do exactly that. **So I ran the episode test instead of the aggregate.** Re-derived, own-calendar returns per instrument:

| Session | VIX | ΔVIX | FXY | Yen stronger across USDJPY/EURJPY/AUDJPY/GBPJPY |
|---|---|---|---|---|
| **7/29** — window's largest VIX rise | **20.66** (window max) | +2.45 | +0.232% | **1 of 4** |

⛔ **THE ROW-SELECTION BELOW THIS TABLE IS WRONG — see ADDENDUM 2 §B1.** "7/17" is the **fifth** largest VIX rise, not the third; **7/13 (+2.13) and 7/23 (+2.06) were omitted** because the ranking was taken across the seven FXY-POSITIVE sessions rather than all 24 risk-off sessions — a selection conditioned on the outcome. Both omitted sessions had the yen **weakening**, so the error ran **against** this verdict. Corrected figures in ADDENDUM 2.
| 6/23 — 2nd largest | 19.49 | +2.21 | +0.018% | 2 of 4 |
| 7/17 — 3rd largest | 18.77 | +2.04 | +0.106% | 2 of 4 |
| **9/8** — the only broad yen bid | **15.72** | +1.19 | **+1.517%** | **4 of 4** |
| 9/9 | 16.46 | +0.74 | +0.235% | 4 of 4 |

🔑 **The relationship is inverted, and that is an episode-level finding, not an average.** On the three genuine VIX-rise episodes the yen did **not** bid broadly (1/4, 2/4, 2/4 crosses; FXY +0.02% to +0.23%). The **one** episode with a real broad-based yen bid — Sep-8/9, 4-of-4 crosses both days — occurred at **VIX 15.72**, which cannot be the *"genuine VIX-spike regime, not hawkish-Fed equity bleed"* the row's **own note** requires. No VIX bar was invented to say that.

**And Sep-8 is doubly disqualified:** it sits inside the window whose **official-intervention attribution is OPEN**. If that move was an operation it is official action, not a market haven bid. ⚠️ **I apply that symmetrically** — it is the same open attribution that disqualified Episode B as a control in point 3, and here it cuts against the row rather than for it. It is *also* the session my frozen prep file had silently dropped.

⇒ **SAM-31 remains FALSE**, now carried by leg 1 (no qualifying regime occurred) plus the episode screen, **not by the mean.** The mean is demoted to descriptive.

⚠️ **One procedural concession the packet is owed:** it asked for *"matched intraday cross-pair evidence… especially July 13."* I supplied daily data, and the packet itself rules that daily FX (Europe/London) and FXY (America/New_York) are **not synchronized closes** and that no SAM-31 grade may be drawn from cross-clock daily returns. **July 13 is precisely that artifact** — FXY −0.493% while all four crosses show a stronger yen. **I have not resolved it, and I am not grading off it.** It does not disturb the verdict: 7/13 is not a candidate *for* re-coupling on the FXY leg, and leg 1 disposes of the row regardless. **Recorded as an open measurement gap, not as evidence.**

### Point 5 — UPHELD. The calibration label is withdrawn.

*"Correctly calibrated"* is a property of a forecaster across many resolved forecasts, never of one 40% row landing on its modal side — an outcome that **should** occur 60% of the time and is close to uninformative. Replaced with: **"resolved on the modal side; contributes one observation."** With SAM-28 now qualified, it contributes to the record with its disposition stated, not as a scored hit.

---

## 2. What changes

| Surface | Change |
|---|---|
| `thesis/PREDICTIONS.tsv` SAM-28 | Status `FAILED` → **`RESOLVED — QUALIFIED / NO-VERDICT`**; Outcome and Notes rewritten; ruling appended |
| `thesis/PREDICTIONS.tsv` SAM-31 | Status **unchanged FALSE**; Notes record the replaced reasoning + the July-13 gap |
| `scripts/lib/boot_context.py` | New status token added to `STATUSES` (the reader validates against a closed set and would have rejected the row) |
| Scoreboard | 16 CONFIRMED / **15 FAILED** / 1 special / **1 qualified** / 1 OPEN = 34 |
| `docket/2026-09-19_SAM28_SAM31_GRADE.md` | Superseded in part — banner, not rewrite; the withdrawn arguments stay legible |
| `STATUS.md`, `CHANGELOG.md`, `NEXUS_BRIEF.md` | DISPUTED banner replaced with the ruling |

## 3. Consequences to the thesis — still none

A qualified SAM-28 changes **less** than a FALSE one. The carry-convexity frame retired **2026-08-07 on leg 1** (CFTC Aug-4 −45,473, through the −108K line), and SAM-28's conditional retirement leg cannot re-retire an already-retired frame; its ≥80%-positioning precondition is moot regardless (Sep-8 printed **NET LONG +10,796**). **v1.7 stands · no successor declared · book FLAT · no retired gate re-arms · 160 gate VOID.** SAM-33 continues to Dec-31; next check **Sep-30 17:00 JST**.

## 4. Two process findings, mine not CATO's

1. 🔴 **A convention tie broken toward the modal forecast, then scored as calibration, manufactures calibration.** Points 1 and 5 are the two halves of one mechanism, and it ran undetected through a grade I had already audited twice for bias in my own favour. **Three of the four defects found in this grading episode ran the same direction** — the prep file's dropped session, the op-day attribution stretch, and this.
2. 🔴 **The contemporaneous record the packet told me to consult was consulted only after challenge** (§0). The instruction was explicit and in the governing document. **A search I was told to run and did not run is not a judgement call.**

## 5. Relay note — the packet carried 3 of 5

PROME relayed CATO's points 1, 2 and 4. **Points 3 (Episode-B control) and 5 (calibration label) were not carried** — and point 3 is one of the two that actually moves SAM-28. Not a criticism of the routing, which is why the challenge reached me at all: **it is the reason a relayed finding gets verified at the source artifact.** Flagged to PROME so the carrier knows the relay was lossy.

---

*Sources: CATO `AGENTS/CATO/runs/2026-09-19_1148_recent-updates-review.md` §R4; governing packet `docket/2026-09-18_SAM28_SAM31_REVIEW.md`; graded record `docket/2026-09-19_SAM28_SAM31_GRADE.md`; registration `thesis/THESIS.md` § The N tail-routes; CH-003 via `thesis/CHANGELOG.md`. Market figures re-derived from yfinance daily closes, each instrument on its own calendar, window 2026-06-22 → 2026-09-18. Prices are vendor research marks, not execution evidence.*

---

# ADDENDUM — CATO 2nd review (`runs/2026-09-19_2137_sam-ruling-review.md`), ruled same evening

> **CATO is upheld on all four points. Each was reproduced at the artifact before being conceded.**
> **SAM-28 stays `RESOLVED — QUALIFIED / NO-VERDICT`. SAM-31 stays FALSE — but the verdict now carries explicit, stated qualifications instead of being asserted flat.**
> ⚠️ **Two of the four are defects the ruling pass ITSELF introduced or left behind.** A correction pass is unreviewed work, and this is the second consecutive round where the fix needed fixing.

## A1 — Point 4 UPHELD: the "+2% blended" argument was the same error I had just upheld against myself

The ruling's §0 used the registered *"FXY move | fires: **+2% blended**"* cell as a reason SAM-28 does **not** reach TRUE. ⛔ **That is a forecast of the route's conditional magnitude. A forecast cannot establish that a +3% outcome did not occur** — it is exactly the forecast/outcome confusion I upheld as CATO's point 1 and then committed again, in the same document, four paragraphs later.

**Withdrawn.** What survives for "not TRUE" is: (a) **the attribution window is unresolved** — which alone is the whole case for no-verdict — and (b) **CH-003**, which is an *outcome* standard, not a forecast (Apr-30 and May-6 both spike-reversed, *"net ~zero on sustained unwind"*; the Jul-30/31 episode repeated it — peak +4.22% on 8/3, back below +3% by 8/10). **The disposition is unchanged; one of its two supporting arguments is gone.**

## A2 — Point 1 UPHELD: SAM-31's replacement reasoning used cross-clock data it had itself ruled inadmissible

The ruling states that daily FX (Europe/London) and FXY (America/New_York) are not synchronized closes and that no SAM-31 grade may be drawn from them — **and then leans on the "1 of 4 / 2 of 4 / 4 of 4 crosses" counts to carry the verdict.** Self-contradiction, in the same section.

⚠️ **This bites harder than it first looks, because the cross-pair dimension is the row's named subject.** SAM-31 is about the *cross-pair* yen-haven channel, and matched intraday cross-pair evidence — which the governing packet asked for and I do not have — is the only instrument that could settle it directly.

**Correction — what the verdict may and may not rest on:**

| Evidence | Clock | Status |
|---|---|---|
| FXY vs ^VIX / ^GSPC (all America/New_York) | **same-clock** | ✅ **admissible — this now carries the verdict** |
| Window VIX max **20.66** | same-clock | ✅ admissible (leg 1) |
| USDJPY/EURJPY/AUDJPY/GBPJPY cross counts | **cross-clock** | ⛔ **DEMOTED to illustrative — not load-bearing** |

**On the admissible evidence alone:** across **n=24** risk-off sessions (VIX up *and* S&P down, all same clock) the yen strengthened on **7 = 29.2%**, mean FXY **−0.154%**; and on the three largest VIX rises FXY moved **+0.232% / +0.018% / +0.106%** — flat, not a haven bid.

🔑 **Contemporaneous check, run this time BEFORE arguing** — the failure that produced the SAM-28 regrade. `THESIS.md` § N tail-routes, route 3, as registered: *"Cross-pair yen-haven **decoupled** Jun 11 (risk-off → USD-haven); **re-snap** needs a **VIX spike**, not hawkish-Fed equity bleed"*, magnitude *"+7% conditional (**Aug-2024-flavored**)"*. Two things follow, and neither is invented at scoring time: the row is about a **regime re-snap** (a relationship), and the **VIX-spike qualifier is contemporaneous**, not a bar introduced to reach a verdict.

**⚖️ The verdict, stated as the judgement it is:**
- **On the CHANNEL / regime reading** — which the registration's own *"decoupled … re-snap"* language supports — the channel demonstrably did not re-couple: 29.2% and a negative mean across every qualifying occasion, on same-clock data. **FALSE.**
- **On a strict single-EPISODE reading**, the only candidate is **Sep-8/9**, and ⛔ **I cannot resolve it.** Its attribution is OPEN, and — **CATO's point, upheld** — *an open attribution prevents confirmation; it does not establish failure.* The ruling previously used Sep-8's uncertainty as though it disqualified the episode. **It does not. It makes the episode unresolvable.**
- **The VIX-regime strictness is a judgement**, contemporaneously grounded but a judgement: it is why Sep-8 (VIX **15.72**) is not counted as the *"VIX-spike episode"* arm. **Reasonable adjudicators could differ**, and under the episodic reading with the disjunctive *risk-off* arm, **SAM-31 would be QUALIFIED rather than FALSE.**

⚠️ **I hold FALSE, and I record that it is the regime reading doing the work** — not an exhaustion argument, not the mean "ruling out" an episode, and not the cross-pair counts. **If the episodic reading governs, this row is qualified, and that alternative is disclosed here rather than buried.**

## A3 — Point 2 UPHELD: the ruling reached the headers and not the instructions under them

`NEXUS_BRIEF.md` led with *"RULED … no longer disputed"* and, seven paragraphs later, still told readers *"no replacement grade exists … Ruling owed next session."* `MEMORY.md`'s TIER-0b block still closed *"Ruling still owed."* **Either could have sent the next session back into finished work.** Both corrected. Class: *an amendment read for one item leaves the others derived from the original live* — and the surfaces that went stale are precisely the two a **next session** and a **peer desk** read first.

## A4 — Point 3 UPHELD: the checker broke its own new rule, in its own output

`closeout_check.py` classified the qualified row internally and then printed **`16 CONFIRMED / 15 FAILED / 1 special / 1 OPEN`** — **33 against a 34-row file, in the 4-part form it had that same evening begun FAILING other files for** — and then reported **PASS**. All 41 tests passed; the three new tests did fail against the old code as claimed. **The tests were aimed at the files the checker reads and not at what the checker says**, so none of them could see it.

**Fixed:** `check_scoreboard` now returns the 5-part tuple, the printed line carries the qualified class and an explicit `total`, and an internal assertion fails the run if the parts ever stop summing to the row count. A test verifies the return shape and the sum; it fails against the pre-fix code. ⛔ **`closeout_check.py` remains PROVISIONAL** — this is the fifth round of real defects found from outside it.

## A5 — What is still NOT settled, stated plainly

- **SAM-31's episodic reading is unresolved**, and it needs matched **intraday** cross-pair data for Sep-8/9 (and Jul-13) that this desk does not have. **It is not scheduled.**
- **Sep-7/8 official attribution remains OPEN** and is the hinge for both that episode and the withdrawn Episode-B control. Primaries land ~Nov-9 (MOF quarterly) and ~Nov-13 (FRBNY Q3).
- **Market history and broker positions were not independently recertified this session** (CATO's note). Book last recorded FLAT, not newly broker-reconciled.

---

# ADDENDUM 2 — CATO recheck (`runs/2026-09-19_2205_sam-correction-recheck.md`): partial closure, and one more real error

**CATO's verdict — "a reasonable stopping point, with partial closure, not all four fully fixed" — is accepted.** Three carries were named. ⛔ **Two of them are live ERRORS and are corrected here rather than carried; the third is a genuine open judgement and is recorded as a standing carry.** No broad repair round, per CATO's own recommendation.

## B1 — 🔴 THE "THREE LARGEST VIX RISES" SELECTION WAS WRONG, AND I BUILT IT FROM THE OUTCOME

The ADDENDUM-A2 table named **7/29, 6/23, 7/17** as the three largest VIX-rise episodes. **Re-derived across all 24 risk-off sessions, ranked by ΔVIX:**

| Rank | Session | ΔVIX | VIX | FXY (same clock) | In my table? |
|---|---|---|---|---|---|
| 1 | 2026-07-29 | +2.45 | 20.66 | +0.232% | ✅ |
| 2 | 2026-06-23 | +2.21 | 19.49 | +0.018% | ✅ |
| 3 | **2026-07-13** | **+2.13** | 17.16 | **−0.493%** | ⛔ **OMITTED** |
| 4 | **2026-07-23** | **+2.06** | 18.70 | **−0.391%** | ⛔ **OMITTED** |
| 5 | 2026-07-17 | +2.04 | 18.77 | +0.106% | ❌ included as "third" |

**7/17 is the FIFTH largest, not the third.** ⛔ **The cause is the defect, not the ranking:** I ranked within the **seven sessions where FXY rose** — the list I had already built as "episode candidates" — instead of across all 24 risk-off sessions. **That is a selection conditioned on the outcome**, and the packet's own evidence table had named 7/13 (+2.13) above 7/17 in plain sight.

⚠️ **The direction here is the opposite of this episode's pattern, and it should be said plainly.** Both omitted sessions (7/13 **−0.493%**, 7/23 **−0.391%**) had the yen **weakening**. Including them makes the same-clock picture **more** adverse to SAM-31, not less — **this error ran AGAINST my own verdict.** Every other defect found across this grading episode ran in my favour. **Corrected because it is wrong, not because it helps.**

🔴 **But it puts the unresolved case in the top three.** **7/13 is the exact session the governing packet singled out** — *"matched intraday cross-pair evidence and episode mechanism, especially July 13 where daily FX signs conflict with FXY."* Same-clock FXY says the yen **weakened** 0.49%; the daily crosses say the yen strengthened on **4 of 4**. **That conflict is unresolved and needs intraday data I do not have.** So the third-largest VIX-rise episode in the window is one I cannot read, and the corrected statement is:

> **On the three largest VIX-rise episodes the yen did not produce a haven bid on same-clock FXY (+0.232% / +0.018% / −0.493%) — and on the third of them the same-clock and cross-clock measures disagree outright, unresolved.**

## B2 — CATO's carry on SAM-31 ACCEPTED AS A STANDING OPEN ITEM, not closed

> *"A negative average over the whole window cannot exclude a relationship returning late in that window. The missing cross-pair evidence remains material."*

**This is correct and it is sharper than the episode point it follows.** A window-wide mean is insensitive to **when** the relationship sits. The two consecutive sessions where the yen bid broadly, **9/8 and 9/9 (4 of 4 crosses both days)**, are the **last** risk-off sessions in the window — exactly where a late return would appear. ⛔ **My same-clock aggregate cannot distinguish "the channel never re-coupled" from "the channel re-coupled in September."**

⚠️ **What still holds FALSE:** the row's registered form is a **regime** claim (`THESIS` route 3: *"decoupled Jun 11 … re-snap needs a VIX spike"*), 9/8–9/9 ran at **VIX 15.72 / 16.46** — no spike — and their attribution is **OPEN**. **What does NOT hold:** any claim that the aggregate *excludes* a late return. It does not.

⚖️ **Recorded as a standing carry, not resolved: SAM-31's FALSE is an interpretive owner judgement on the regime reading. A late-window re-coupling is not excluded by my evidence, and the missing matched-intraday cross-pair data is material to it — not a technicality.**

## B3 — MEMORY led with the withdrawn rationale before correcting it later

`MEMORY.md` restated the "+2% blended" argument in its LAST SESSION block and only withdrew it further down. A reader hits the retracted reason first. Corrected in place.

## Standing carries after this pass

1. **SAM-31 is an interpretive owner judgement** (B2). A late-window return is not excluded. **Preserve the qualification whenever this row is reported — "15 wrong" alone drops information that matters.**
2. **Matched intraday cross-pair data for 7/13 and 9/8–9/9 is owed and NOT scheduled.** It is the instrument that would settle both B1's conflict and B2's late-return question.
3. **Sep-7/8 attribution OPEN** — primaries ~Nov-9 (MOF quarterly), ~Nov-13 (FRBNY Q3).
4. **Positions not independently recertified** this session.
