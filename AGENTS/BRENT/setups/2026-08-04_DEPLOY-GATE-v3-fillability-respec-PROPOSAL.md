# 🔴 DEPLOY GATE v3 — FILLABILITY RE-SPEC · **PROPOSAL TO WILL, NOT APPLIED**

**Author:** BRENT · **Written:** 2026-08-04 Tue ~14:10 ET (⏰ `date`-verified — stamps have run +66 min fast on this desk, TERRY 12:31 packet §7) · **Class:** spec proposal, direction-relevant ⇒ **Will ratifies**
**Status:** ⛔ **PROPOSED ONLY. DEPLOY GATE v2 REMAINS THE LIVE RULE UNTIL WILL RULES.** Nothing here authorises a fill.

---

## 1. THE DEFECT, STATED AS AN INSTRUMENT FACT RATHER THAN AN OPINION

**DEPLOY GATE v2 requires `(a) AND (b)` on the SAME SESSION**, where:

- **leg (a)** = OVX **≤ −15.0% from the post-arm running peak**, **CLOSE basis** (Will-frozen 7/31; *intraday readings are NOT the gate*)
- **leg (b)** = net debit **≤33.0% of width on a LIVE CHAIN AT FILL**

⇒ **Leg (a) becomes knowable at exactly the moment leg (b) becomes ungradeable.**

### ✅ VERIFIED THIS SESSION — the window is ZERO, not fifteen minutes

| Instrument | Final intraday bar | Basis |
|---|---|---|
| **`^OVX`** | **16:00** (7/31) · 15:55 (8/3) | ✅ pulled, 5m bars, this session |
| `^VIX` | **16:10** | ✅ pulled — VIX *does* disseminate late; **OVX does not** |
| `USO` **shares** | 19:55 (post-market) | ✅ pulled — ⚠️ **shares, not options** |
| `USO` **options** | **16:00** (standard ETF; USO is not a broad-based ETF with a 16:15 close) | ⚠️ **NOT independently verified this session — flagged, not asserted** |

⛔ **TERRY's 12:31 and 13:35 packets both state leg (a) "could not resolve until 16:15."** **That is wrong for OVX, and it fails in the comforting direction** — it implies a 15-minute execution window that does not exist. Correction owed to TERRY.

**Deferring to the next session's open does not solve it and is circular:** on session N+1 leg (a) is *not banked* (v2: *"leg (a) must fire AGAIN on whatever session actually fills"*), so it would need N+1's close — and so on, forever.

### ⚠️ WHY THIS SURVIVED RATIFICATION, AND IT IMPLICATES MY OWN AUDIT

1. **v2 was ratified 7/30 when leg (a) was −8.0% away.** Nobody had to execute it.
2. **It bit on 8/3 and I recorded the wrong cause.** PROME's 3.5-hour routing delay meant there was no live chain anyway — **a COORDINATION failure masked a STRUCTURAL one, and I logged the former without testing the latter.**
3. ★ **The 8/2 premise-check audit — mine, run at Will's request, verdict "THE GATE IS SOUND" — base-rated the gate on DAILY CLOSE data.** That silently models a gate graded off *a* close and filled in *a* session, i.e. **it base-rated the cadence proposed below, not the spec as written.** **The audit validated a gate nobody could execute, and never asked whether it could be filled.** `[[finding_threshold_spec_fails_before_world]]` — extended: a spec can fail on its *execution window* while passing every test of its *statistical merit*.

### ⚖️ AND IT VIOLATES ITS OWN GOVERNING LESSON

**LESSONS #21(b), ratified:** *"Match every leg's window to its own response time; a mixed-latency basket needs per-leg windows, not one."*
**Leg (a) is a DAILY-cadence instrument. Leg (b) is a MINUTE-cadence instrument. v2 forces both into one session.** I ratified the per-leg-window fix for Stage A/B on 7/29 **and then reproduced the identical defect in Deploy Gate v2 the following day.**

---

## 2. ⭐ RECOMMENDED — **GATE v3: MOST-RECENT-CLOSE + LIVE NON-REVERSAL**

**One-line change: leg (a) tests THE MOST RECENT OFFICIAL OVX CLOSE, not "this session's close."**

| Leg | Cadence | Test |
|---|---|---|
| **(a) Vol decompression** | **daily** | **The most recent official OVX close ≤ peak × 0.85**, peak = running max of **closes** since arming (re-ratchet unchanged). ⇒ **A STATE, known at 09:30, holding all session.** |
| **(a2) Live non-reversal** 🔻*NEW* | **minute** | **At the moment of the ticket, OVX must print ≤ the SAME frozen line.** Existence form: fill at any moment it holds; never fill when it doesn't. |
| **(b) Structure economics** | **minute** | **UNCHANGED** — net debit ≤33.0% of width, live chain, at fill. |

**⇒ All three legs are gradeable during regular hours. The execution window goes from 0 minutes to 6.5 hours.**

### 🔻 DIRECTION-NEUTRALITY, per the ratified #21(b) rule *(a spec repair is not direction-neutral)*

This **loosens** (it makes the gate fillable at all). It ships with **two tightenings**:

1. **Leg (a2) is new.** v2 required **ONE** reading below the line; v3 requires **TWO INDEPENDENT** readings — an official close **and** a live print at the ticket. **On the evidentiary axis v3 is STRICTER than v2; the only loosening is that a fill becomes possible.**
2. **Clearance expires at the end of the NEXT session.** Leg (a) is banked for **exactly one session** and never accumulates. If unfilled, it must re-qualify off a fresh close.

**Unchanged:** 20-td arm expiry · frame-breaker carve-out · re-ratcheting peak · vehicle/structure/tenor · **~$500 defined max loss** · **Will's [Approve] at fire** · the full pre-fill disclosure clause incl. the v5.4 terms extension.

---

## 3. 📊 BASE RATE — **RUN BEFORE PROPOSING, per LESSONS #21**

`^OVX` + `BZ=F` daily, **2007-07-30 → 2026-08-04, n=4,729 sessions.** Arming proxy **Brent 1d ≥ +3%**; de-overlapped to **113 episodes**; frozen −15% rule incl. re-ratchet; 20-td window.

**Fire rate within 20 td: 68.1%.**

### Cost of moving the fill one session later (v3 vs a v2 that could actually fill)

| Metric | v2 grade-day | v3 fill-day | Δ |
|---|---|---|---|
| Brent entry slippage | — | — | **median −0.04% · mean −0.10%** (nil, marginally favourable) |
| OVX at fill (median) | 41.90 | 43.30 | **+3.3%** (slightly dearer vol) |
| **P(max Brent +15% within 63d)** | **38.2%** | **39.5%** | **+1.3pp** |
| median max forward gain | 12.03% | 12.50% | +0.5pp |

**⇒ Filling one session later does NOT degrade the tail this structure depends on.** The vol paid is ~3% higher; on a **vertical spread** that is second-order (v2's own §: at spec moneyness the debit moves only ~+13.5% across a +44% vol move).

### Sizing leg (a2) — the variant table, because my first draft of this guard was mis-specified

| Guard form | Blocks |
|---|---|
| Strict: OVX ≤ line at **every** moment of the session | **66.2%** ⛔ unusable — and it turns the fill into an intraday timing game |
| **⭐ Existence: no moment ≤ line all session** *(the recommended form)* | **7.8%** |
| Existence with ×1.03 tolerance | 2.6% |
| OPEN > line | 24.7% |
| OPEN > line ×1.05 | 7.8% |

**⇒ Leg (a2) in EXISTENCE form leaves a fillable window on 92.2% of fire sessions** while genuinely closing the overnight-gap hole.

### ⛔ THE HONEST COST, STATED BECAUSE THE TABLE ABOVE FLATTERS IT

**On 31.2% of fire sessions, OVX CLOSES BACK ABOVE THE LINE.** So roughly **one fill in three** happens on a day whose *own* close would not have qualified. **That is the real loosening and it is not small.** It is bounded by leg (a2) (you cannot fill while OVX is above the line) and it did not show up as tail damage (+1.3pp) — but Will should rule knowing it, not knowing only the +1.3pp.

---

## 4. ALTERNATIVES CONSIDERED AND **REJECTED** — recorded so they are not re-proposed

| Option | Why rejected |
|---|---|
| **B — Intraday fire on an "unreversible margin," fill 15:45-16:00** | ⛔ Reverses **Will's 7/31 close-basis ruling**. ⛔ Puts the fill in the **least liquid 15 minutes**, directly attacking leg (b) — which TERRY *and* PROME independently showed is **friction-dominated** (~$0.37-0.38 regardless of width). ⛔ **This is the fix I deliberately declined to propose on 8/3 because it would have enabled that same afternoon's fill — the trap TERRY refused.** It trades a grading defect for an execution defect. |
| **D — Accept it cannot fire; let the arm expire 8/13** | A legitimate *outcome*, not a *design*. **LESSONS #21: "a gate that cannot fire in the world it governs is not discipline, it is a dead switch."** If Will prefers no trade, that should be a decision about the trade, not an artefact of a clock. |
| **E — Drop leg (a); keep leg (b) + [Approve]** | Tempting — v2 itself calls leg (b) *"the thing the vol legs were proxying for, measured directly."* But the 8/2 audit measured leg (a)'s tail contribution at **+9.2pp** (63d). Dropping it discards real edge to fix a scheduling problem. |

---

## 5. ⛔⛔ THE DISCLOSURE THAT MATTERS MOST — **THIS RULE WOULD FIRE TODAY**

**I am stating this first and plainly rather than leaving it to be discovered.**

| Leg under v3 | Reading, 8/4 ~14:10 ET | Verdict |
|---|---|---|
| (a) most recent official close | **8/3 close 57.20** ≤ 58.6245 | ✅ MET all session |
| (a2) live non-reversal | **OVX 53.38** ≤ 58.6245 | ✅ MET |
| (b) structure economics | TERRY 12:24 live chain, `125/130 ×2` = **26.0%** worst case | ✅ MET |

**⇒ GATE v3 WOULD HAVE FIRED TODAY AND WOULD HAVE BEEN FILLABLE AT 12:24.**

⚠️ **That is a reason for Will to scrutinise this proposal harder, not a selling point, and I will not present it as one.** On 7/30 I offered *"the proposed rule would NOT fire today"* as evidence a re-spec was not written to fit the tape. **I cannot offer that here — the opposite is true.**

**What I can offer instead:**
- The defect was forced by an **instrument fact** (`^OVX` stops at 16:00) that is **independent of today's tape** and would hold in any regime.
- The proposal **adds an evidentiary requirement** (a2) rather than removing one.
- Its costs are **disclosed in figures including the one that cuts against it** (31.2%).
- ★ **And TERRY's 13:35 finding binds here:** **a firing gate carries ZERO thesis information.** Leg (a) fires because OVX decayed; leg (b) passed because USO fell another 5%. **Both legs opened as the market priced LESS of my thesis, on a third consecutive down session.** **A gate that fires is not evidence the trade is right.**

---

## 6. ⚠️ LIMITS OF THIS ANALYSIS — stated, not buried

1. **My fire rate (68.1%) does NOT match the 8/2 audit's (81.9%).** Different construction — I **de-overlapped** arming days into 113 episodes; the audit used **n=79 arming days** with a different overlap treatment. **I have not reconciled them and am not presenting either as canonical.** The *comparative* results (v2 vs v3 on identical episodes) are unaffected, because both arms use the same sample.
2. **n=0 genuine physical chokepoint reopenings in the entire 19-year sample.** Every limit on the 8/2 audit applies unchanged: **the base rate validates the gate for DIPS and is SILENT on terminal resolution.**
3. **Arming is a PROXY** (Brent 1d ≥ +3%), not the real Tier-1/Tier-2 event conditions, which are not machine-encoded.
4. **`USO` options' 16:00 close is not independently verified this session** (OVX's is). If USO options *do* run to 16:15, the v2 window is 15 minutes rather than zero — **still not a fillable window for a [Approve]-gated discretionary trade, so the recommendation is unchanged**, but the defect statement would need softening.
5. **First-run guard caveat** (`[[finding_test_the_guard_not_just_the_guarded]]`): this analysis's first pass reported the tail delta as **+0.0pp** and leg (a2)'s block rate as **1.3%**. Both were wrong — an object-dtype `.mean()` silently mangled boolean columns. **Caught by disbelieving a 1.3% tail against the audit's known 44.4%, and the corrected block rate (65.8% strict) was 50× the buggy one and materially changed the recommended guard form.** **The first version of this proposal would have shipped a mis-specified tightening.**

---

## 7. ASK

**Will's ruling on ONE question:** adopt **Gate v3** (§2), keep **v2** and accept the arm likely expires un-deployed 8/13, or a variant.

⛔ **Until then v2 is live and unchanged.** **The clock is not evidence** — if this expires un-deployed because the spec could not be fixed in time, **that is a correct outcome**, and I would rather lose the arm than have a fillability fix wave through a fill.

**Also open to Will, unchanged from earlier today:** short-leg band departure (~1.3pp, widens as USO climbs) · leg (b) **liquidity qualifier** · leg (b) **width bias**.
**Open to me from TERRY:** the `limit = MIN($1.50, fire-time worst case)` form — **orthogonal to this proposal**; I rule on it separately.

---

## 8. ⚖️ SPEC-SWEEP RECONCILIATION — `lessons_check.py --spec`, 9 lessons govern

*Run before shipping, per closeout step 8a. Silence about a governing lesson is the failure mode this exists to kill, so every row is dispositioned.*

### ✅ CITED AND LOAD-BEARING

- **L21 — *a threshold fails on its SPEC before it fails on the world; match each leg's window to its own response time.*** **This proposal is L21 applied twice.** §1 shows v2 is a **mixed-latency basket wearing a single window** — the exact defect L21(b) ratified a fix for, which I then reproduced. §3 base-rates the replacement **before** proposing it, per L21's *"base-rate a proposed replacement under the trigger state BEFORE proposing it."* §2 pairs the loosening with two tightenings per **#21(b)**.
- **⭐ L22 — *a spec must name an instrument that actually TRADES in the window it will be graded in, and "I verified it" is a claim that must be RUN.*** **ADDED ON THE SWEEP — it was missing, and it is the lesson this entire defect is an instance of.** L22(b) says the test must be gradeable *on the instrument it names, at the moment it must fire*; **v2's leg (b) names an instrument (a live USO option chain) that is CLOSED at the only moment leg (a) can be graded.** L22's guard was honoured in method: **I pulled `^OVX`, `^VIX` and `USO` 5m bars rather than inheriting TERRY's "16:15"** — and the pull refuted it. ⚠️ **L22 also convicts §6.4:** USO options' 16:00 close is asserted from convention, **not run**, and is flagged as such rather than written as verified.
- **L15 [SCOPED] — *spreads not naked, 60-90 DTE.*** **HONOURED, UNCHANGED.** v3 touches no structure, vehicle or tenor. **It is also load-bearing for §3:** the "+3.3% dearer vol is second-order" claim holds *because* the mandated instrument is a **vertical**, which is near-vega-neutral. Against the naked call L15 bans, a +3.3% vol move would matter far more. **The 7/30 scoping is respected — this is the STRUCTURAL trade (60-90 DTE), not the 21-35 DTE off-ramp round-trip.**

### 🔇 DELIBERATELY SILENT — governing by keyword, not by substance

- **L11 · L16 · L18** *(announcement-vs-delivery, tanker lead, rhetorical-vs-operational)* — these govern **Stage-A entry on the OFF-RAMP SHORT**, a different trade in the opposite direction. **This gate deploys a LONG convex arm on vol decompression; it is not an announcement-triggered entry and has no tanker or signature leg.** They are matched on shared `entry_timing` vocabulary only. **⚠️ Not discarded: L18's descendants are already live in this gate's PRE-FILL DISCLOSURE clause** (item (i) instrument-vs-guidance + the v5.4 terms extension), which v3 leaves untouched.
- **L06 · L08 · L09** *(crack spreads · storage reporting lag · EIA product-supplied masking)* — matched on the `inventory` / `data_latency` tags. **No crack, storage or EIA claim appears anywhere in this proposal.** The only latency at issue is an **exchange dissemination window**, which is a different object from a data-reporting lag. **Silent by substance, and said so rather than skipped.**
- **L10 · L19** *(OPEC+ paper quotas ≠ physical production · a signed deal is not an operational one)* — **recruited only by the vocabulary of §8 itself** (see the note below). Neither bears on when a vol gate can be graded or filled. **L19's substance is live elsewhere in the arm and untouched here** — it sits in THESIS v5.4 and the disclosure clause, not in the gate mechanics.

> ### ⚠️ CHECKER ARTIFACT WORTH RECORDING — **the spec sweep does not necessarily converge.**
> **First run: 9 governing lessons, 8 NOT CITED. After writing the reconciliation: 11 governing lessons** — citing L11/L16/L18 introduced `announcement_vs_physical` and `tanker_equity` vocabulary, which **recruited L10 and L19 as new governors.** **Reconciling a spec can therefore ENLARGE its governing set**, and a naive "drive NOT CITED to zero" loop would chase its own tail.
> **⇒ The sweep is an ATTENTION tool, not a completion criterion.** Judge each row on substance and stop when the substance is dispositioned — **do not treat a zero as the goal**, or the incentive becomes to write *less* about lessons in order to be governed by fewer. *(Sibling of `[[finding_verification_zero_is_ambiguous]]`.)* **Flagging to no one as urgent; noted here because the next person to run `--spec` on a reconciled file will see the count go UP and should know why.**

— BRENT
