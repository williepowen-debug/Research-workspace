# ENTRY DEFECT ② — TRANSIT LEG vs LESSONS #11 · **RESPEC DRAFT + JOINT BASE-RATE OF THE FOUR-WAY GATE**
### **DRAFT FOR WILL'S RULING — NOT A RATIFICATION. Every number below is PROPOSED.**

**Author:** BRENT · 2026-07-31 ~12:30 PM ET · **Status:** ⚪ **DRAFT.** The live Stage-A **(ii-A) transits >~35/day on ≥2 consecutive days** stands **as written** until Will rules (`[[finding_outside_this_rail_disclosure]]`).
**Companion:** `outbox/2026-07-31_to-PROME_stage-a-proposal.md` (Stage-A v4, ratified 7/31 — Legs T and C are now live and are assumed live throughout this draft).

---

## 0. ⛔ FIRST — **THE PREMISE OF THIS WHOLE DEFECT WAS WRONG, AND IT WAS MY PREMISE**

**PROME's packet said *"your dark-transit problem is the crux."* It is not. There was no dark-transit problem.**

`TRADE.md` entry defect ② has said since 7/30: *"On Jun-17 transits were **dark** and a crude short still won −9.7% by day 10."* **I pulled the actual series today.** IMF PortWatch `chokepoint6` (the source my own `domain/HORMUZ_TRANSIT_BASELINE.md` pins as canonical), `n_total`, daily:

| | 6/15 | 6/16 | **6/17** | 6/18 | 6/19 | 6/20 | 6/21 | 6/22 | 6/23 | **6/24** | **6/25** | 6/26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| transits | 11 | 12 | **15** | 22 | 13 | 26 | 8 | 14 | 15 | **51** | **50** | 37 |

**Transits were fully observable on and around Jun-17.** The leg did not fail because the instrument was blind. **It failed on the LEVEL — 15 < 35.** And it then **FIRED on 6/24-25 (51, 50 = two consecutive days >35) — FIVE SESSIONS AFTER the announcement.**

**⇒ Defect ② is a LATENCY defect, not an observability defect.** That changes the fix completely: a corroborator-anchored alternative branch solves a blindness problem I do not have. **The metric was never missing. It was late.** *(`[[finding_verify_loadbearing_before_trade]]` — I built a proposed fix on an inherited premise and the premise did not survive one query. Corrected in TRADE.md this session.)*

---

## 1. 💥 WHAT THE LATENCY ACTUALLY COSTS — **it does not shrink the trade, it INVERTS it**

Brent front-month, Jun-17 analogue, crude **short**:

| Entry basis | Entry session | Entry price | Best short move | **H1 8-session exit (the ratified rule)** |
|---|---|---|---|---|
| **Announcement-based** (LESSONS #11) | 6/18 | **$79.85** | **+10.37%** | **✅ +10.37%** |
| **Transit-leg-gated** (live spec) | 6/26 | **$71.99** | +0.58% | **⛔ −5.99% — A LOSS** |

**The transit leg does not merely reduce the profit. It converts a +10.37% winner into a −5.99% loser**, because the gate only opens after the move it was waiting for has already happened — you buy the bottom of the unwind and then ride the round-trip back up ($71.99 was ~the low; the tape was +13.1% by day 20).

**⇒ LESSONS #11 is not a stylistic preference. On the one analogue that exists it is worth ~16 percentage points and it flips the sign of the trade.** This is the single most decision-relevant number in this packet.

---

## 2. 📊 JOINT BASE-RATE OF THE FOUR-WAY AND-GATE (per `[[finding_compound_gate_jointly_unsatisfiable]]`)

### 2a. The transit leg alone — **PortWatch `chokepoint6`, `n_total`, pulled 2026-07-31**

| Regime | n days | mean | **>35/day** | **>35 on 2 consecutive days** |
|---|---|---|---|---|
| **Pre-crisis** (2025-01-01 → 2026-02-28) | 424 | 89.9 | **99.3%** | 417 occurrences |
| **Closure regime** (2026-03-01 → 7/23) | 145 | 9.9 | **2.8%** (4 days) | **2 occurrences** |
| **Since the 7/11-12 FORMAL closure** | 13 | 10.4 | **0.0%** | **0** |

The **entire** closure-regime population of qualifying days is: **6/24 (51) · 6/25 (50) · 6/26 (37) · 7/1 (40).** One cluster, one isolated print. **Since the formal closure the leg has been satisfiable on zero days.**

> **⚠️ Read this correctly, because it is the opposite of a "the bar is too high" argument:** a leg that is open 99.3% of the time pre-crisis and 2.8% in-crisis is **doing exactly what it was designed to do — detecting the strait returning to normal.** The problem is **not** the threshold. It is that **normalisation is the CONSEQUENCE the trade is predicting, so requiring it at ENTRY means requiring the thesis to have already paid out.** That is LESSONS #21 in its purest form: the leg's response time (weeks) is not matched to the window it is asked to report in (~48h).

### 2b. The joint gate — **and the legs are OUT OF PHASE BY CONSTRUCTION**

Stage A = **(i) signature AND (ii-A) transit AND (T) AND (C)**, all inside the ~48h trade window.

| Analogue | (i) signature | (ii-A) transit | (T) liveness | (C) follow-through | **GATE** |
|---|---|---|---|---|---|
| **Apr-17** (rhetorical) | ⛔ FAIL (minister quote) | ⛔ 18 → no 2×>35 | ✅ 5.63% | ⛔ **+8.96%** | ⛔ **BLOCK** ✅ *correct* |
| **Jun-17** (the money-maker) | ✅ MOU signed | ⛔ **15 → fires 5 sessions LATE** | ✅ 1.63% | ✅ **−2.07%** | ⛔ **BLOCK** ❌ *wrong* |

**{(i) AND (ii-A)} inside the 48h window: 0 of 2 analogues — and 0 occurrences in 145 closure-regime days.** The signature is a **day-0** event; transit recovery is a **day+5** event. **They cannot co-occur inside a 48h window, so the conjunction is ~unsatisfiable in the state where it would be used** — the same anti-correlation that killed the old `{2.89 / 44.2}` cooldown gate (open on 0 of 38 escalation days), found the same way.

> **⚠️ HONEST ON n: the conditional base rate is n=2 and I will not manufacture precision from it.** The 145-day figures above are the **unconditional proxy** and are labelled as such. What n=2 *can* support is a **structural** claim — phase mismatch — which does not depend on sample size: transit recovery lags a signature by construction, and that is visible in the one case we have (5 sessions) and in the mechanism (hulls queue, insurers re-rate, charterers re-book).

---

## 3. ✅ CANDIDATES — with what each does on BOTH analogues

### **CANDIDATE 1 — MOVE the transit leg from Stage A (entry) to the Stage-B KILL TEST. ⭐ RECOMMENDED**

> **Stage A becomes: (i) signature/sovereign act AND (T) AND (C).** The transit test is **not deleted** — it moves to where it can actually report:
> **Added to the existing KILL TEST:** *if aggregate Hormuz transits have **not** reached **>35/day on ≥2 consecutive days within 10 trading days** of the announcement — the window it already carries in the Stage-B persistence table — **the de-escalation was not physically real: CUT the position**,* on the same one-line [Approve/No] authority as the fill.

**⚠️ Note the transit leg is ALREADY in Stage B** with a 10-trading-day window matched to its response time. **Its presence in Stage A is a DUPLICATE of a test that already exists in the right place.** Candidate 1 deletes the duplicate, not the test.

| Analogue | Result |
|---|---|
| **Apr-17** | ⛔ **BLOCKS** — on **(i)** (rhetorical, not a signature/sovereign act) **and independently on (C) +8.96%.** ✅ **Two independent blocks — the false-dawn hole stays shut.** |
| **Jun-17** | ✅ **FIRES** — (i)✅ (T) 1.63%✅ (C) −2.07%✅ → entry 6/18 → **+10.37%, H1 exit +10.37%.** And the kill test would have **passed** anyway (transits hit 51/50 on 6/24-25, day+5, inside the 10-td window). |

**Residual-gate base rate (closure regime, n=99 sessions):** Leg T passes 87.9% · Leg C passes 44.4% · **both pass 38.4%.** ⚠️ **That number is NOT the gate's fire rate** — **(i)**, a signature/sovereign act, is the rare binding event (**2 occurrences in 145 days ≈ 1.4%**). The price legs are a *filter on* (i), not a trigger. **Stated plainly so it can't be misread as "the gate now opens 38% of the time."**

**Why this is not a net loosening:** it removes a leg that has never once permitted a correct fire, while (a) **retaining the physical test as a mandatory post-entry kill**, and (b) leaving **Leg C's 2-session confirmation** in place as a real wait. Net: **strictly better-targeted, and tighter after entry than the spec has ever been.**

### **CANDIDATE 2 — CORROBORATOR-ANCHORED OR-BRANCH** (the GATE-TERRY-006 pattern PROME named)

> `(ii-A) transits >35/day ×2d` **OR** `(ii-B)` a **dated, published JWC/Lloyd's Listed-Areas revision narrowing the Hormuz listing` **OR** `(ii-C)` a **P&I club circular restoring cover** — institutional, dated, **non-sovereign** (FALCON's 7/30 addendum: *war-risk LEADS, transit count LAGS*).

**⛔ I CANNOT BACKTEST THIS AND I WILL NOT PRETEND OTHERWISE.** I have no JWC Listed-Areas revision history or P&I circular archive for Apr/Jun-17; those sit behind Lloyd's List / club portals I cannot reach. **A leg I cannot grade on the only two analogues that exist is a leg I cannot recommend today.**
**Also a live design worry:** my own Stage-B table prices war-risk repricing at **2-4 weeks**. A *listing revision* is faster to publish than a *premium* re-rate — but I have not verified that it is fast enough for a 48h window, and asserting it would be exactly the unverified-mechanism error this packet opens by correcting.
**⇒ Recommend: NOT NOW. Worth a scoped research task** (obtain JWC revision dates for Apr/Jun-17 and re-run) **before it is ever ruled on.**

### **CANDIDATE 3 — WAIVE the leg when transit data is dark ("fail-open")**

**⛔ WITHDRAWN BY ME.** Its triggering condition **never occurred** (§0), so it solves nothing; and **fail-open on missing data in a short-arming gate is actively dangerous** — darkness correlates with crisis, so the guard would relax exactly when information is worst (`[[finding_standing_guard_is_a_false_negative_risk]]`). **Recording it as considered-and-rejected so it is not re-proposed later.**

### **CANDIDATE 4 — LOWER the transit bar (>20-25/day ×2d)**

**⛔ DOES NOT WORK — checked, not assumed.** At announcement neither analogue produces 2 consecutive days over any lower bar: **Jun-17** = 15, 22, 13 · **Apr-17** = 18, 22, 7. **A lower bar fires on NEITHER analogue at entry**, and in the closure regime >20/day already has an 11.7% base rate against a regime mean of 9.9 — so it buys noise without buying Jun-17. **The level is not the problem; the phase is.**

---

## 4. ⚠️ THE SIZING SUB-QUESTION — **EXPLICIT OPEN RIDER** (carried per the directive)

**Not ruled 7/31. The strict default stands and is what is written in `TRADE.md`: FULL SIZE ONLY AFTER BOTH LEGS RESOLVE ⇒ entry lands 2 sessions after the announcement.**

**Priced against LESSONS #11 on the one analogue** *(Jun-17, announcement-based entry 6/18 @ $79.85)*:

| Sizing | Entry | Cost vs day-1 entry |
|---|---|---|
| **Strict default** — full size after Leg C resolves | 6/22 (2 sessions later) | Enters after Brent has already fallen; **gives up a material part of the +10.37%** |
| **Half/half** — half on day 0-1, remainder on Leg C pass | 6/18 + 6/22 | Captures the early move on half the risk; **the other half still waits for confirmation** |

**⇒ Will rules this together with §3 or separately, his choice.** My read: **half/half**, because §1 shows the cost of waiting is not linear — it is the difference between a winner and a loser — but **the strict default remains in force until he says otherwise, and I have not pre-applied it.**

---

## 5. ⚠️ HONEST LIMITS (travelling with the draft, as always)

1. **n = 2 analogues.** Everything conditional is n=2. The 145-day figures are an **unconditional proxy**, labelled.
2. **This regime has produced ZERO genuine physical reopenings** (LESSONS #19: Jun-17 was 0-of-4 on physical legs). **Jun-17 is "the one that would have made money," NOT "the one that was real."** Candidate 1 is therefore optimised against a profitable trade, not a verified reopening — **the sharpest limitation in this packet.**
3. **The +10.37% / −5.99% figures are FRONT-MONTH BRENT, not the actual USO put-spread structure.** Direction and sign are robust; the magnitudes are not the P&L of the ratified vehicle.
4. **PortWatch publishes on a 4-6 day lag** — fine for this backtest, and it is precisely why the live spec says grade off real-time AIS. **The lag is a second, independent reason the leg cannot serve as an entry gate**, on top of the phase mismatch.
5. **Series ends 2026-07-23** (latest PortWatch print). The 7/24-7/31 window is not in these base rates.
6. **§0's discrepancy is corrected, not explained** — I know the "dark" claim was wrong; I do not know how it entered my ledger. Same open question as the 7/30 tanker figures.

---

## 6. THE DECISION

| Option | Effect | My read |
|---|---|---|
| **A — Candidate 1** (move transit to the Stage-B kill test; Stage A = (i)+(T)+(C)) | Jun-17 fires (+10.37%); Apr-17 blocks twice over. Physical test retained post-entry. | ✅ **RECOMMENDED** |
| **B — Candidate 1 + half/half sizing** | As A, plus captures the non-linear early move | ✅ **Recommended if ruling both at once** |
| **C — Commission the Candidate-2 research** (JWC/P&I dates for Apr/Jun-17), rule later | Keeps the best-anchored option alive without ruling blind | Sensible parallel step |
| **D — No change** | Entry stays structurally unfireable; playbook stays non-functional end-to-end | Status quo, honestly labelled |

**No threshold is moved by this packet. No capital is requested.**

*BRENT · 2026-07-31*
