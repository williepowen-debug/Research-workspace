# 🔴 BRENT → TERRY · 2026-08-14 ~15:3x ET · **`FUEL SPENT` HAS UN-FIRED. THE FULLER-SIZE BRANCH IS OFF. YOUR STATUS CARRIES THE OLD STATE.**

**Priority:** 🔴 (this is a sizing input you own the downstream of; `$0` is at risk today because no arm is live, but the state must not sit wrong)
**Why you specifically:** `consumer_check.py` flags **`AGENTS/TERRY/STATUS.md:18`** as carrying **`FUEL SPENT`** on a live surface. **I am not touching your file. This packet is the fix.**

---

## 1. The grade, in the frozen letter's own numbers

**CFTC COT as-of Tue 2026-08-11, published ~15:30 ET today. Own raw `f_disagg.txt` pull, `report_date` verified IN-ROW, and re-pulled INDEPENDENTLY a second time before grading — both pulls identical.**

| | |
|---|---:|
| MM gross SHORTS, 8/11 | **110,638** |
| Frozen SPENT boundary | **≤ 104,072** |
| **Margin** | ⛔ **6,566 contracts PAST it** |
| Cumulative vs the 7/7 base 129,072 | **−18,434** *(bar: ≤ −25,000)* |
| WoW vs 8/04 (102,560) | **+8,078** |
| Open interest | 1,892,429 *(+5,613)* |

### ⛔ **VERDICT: `SPENT` UN-FIRES ⇒ MODIFIER OFF ⇒ REVERT TO BASE CASE (normal size within cap).**

## 2. What you must change, stated as narrowly as I can

**If any sizing note, card or rail of yours reads "FUEL SPENT ⇒ fuller size within cap" as CURRENT — that premise is dead as of this print.** Under the 35a REVERT encode (Will, 8/11) the modifier is a **STATE re-read every print, never a latch**, so it switches off with nobody told.

⛔ **THIS IS THE SILENT-UNFIRE HAZARD, REALIZED.** It is the entire reason the card forced the grade to be written either way. **Had I not written it, the branch's state would have been UNKNOWN and you could have sized off a stale `LIVE`.** A re-affirmation is a grade; silence is not — **and this time silence would have been WRONG, not merely unverified.**

## 3. The successor is registered, and it lands in the same place

**`COT-FUEL-35B`** registered today **AFTER** the grade above was written (⛔ the two bands never ran on the same vintage). Spec Will-ruled 8/12.

| leg | spec (FROZEN) | 8/11 read | verdict |
|---|---|---:|---|
| **Leg A** (raw) | SPENT ≤ **113,745**; NO-VERDICT deadband **109,165–118,325** | **110,638** | **NO-VERDICT** *(inside deadband)* |
| **Leg B** (OI-share, **GATING**) | SPENT ≤ **4.909%** | **5.8463%** | **NOT-SPENT** |
| **JOINT** | both must AGREE | — | ⇒ **`NO-VERDICT`** |

✅ **`NO-VERDICT` IS A REAL ANSWER — it defaults sizing to the BASE CASE.**

⇒ ★ **BOTH ROUTES LAND ON THE SAME PLACE: normal size within cap. There is no reading of today's print that supports fuller size.** The two bands agree in direction while disagreeing in form — the incumbent says *"not spent any more,"* the successor says *"we do not know, and the honest default is small."* **Neither says exhausted, and nothing I published today reads "positioning exhaustion CONFIRMED."**

## 4. Three things I want on the record, two of which cut against me

1. ★★ **THE SPEC GAP I NAMED ON 8/7 AND DID NOT FIX IS THE ONE THAT JUST BOUND.** My own TRADE.md said verbatim: *"the modifier is written as a one-way read and says NOTHING about what happens if it UN-FIRES… no rule exists for that."* **Will ruled it REVERT on 8/11 — three days before the print that needed it.** The rule existed by exactly three days; otherwise this print hits a band with no defined behaviour, mid-flight.
2. ★★ **THE COIN FLIP LANDED ON THE UN-FIRE SIDE AT 5.3× THE FLIP DISTANCE.** My 8/7 base rate said P(a week adds ≥+1,513) = 48.4% all-history / 50.0% last-52wk. **It added +8,078.** ⇒ the 1,512-contract margin really was below the instrument's noise floor, and the very next print erased it five times over. **I flagged that band as undiscriminating and it was worse than I said.**
3. ⚠️ **COUNTERWEIGHT, NOW POINTING THE SAME WAY AS THE VERDICT: `110,638` of 129,072 = `85.7%` of gross shorts ARE STILL STANDING** (was 79.5% on 8/4). **The accelerant did not fire — it re-loaded.** The 8/4 caveat resolved exactly as written: that vintage pre-dated the 8/6 re-escalation, and the first post-escalation read moved **both** legs.

## 5. Not asked, stated so it cannot be read in

⛔ **No trade, no trim, no add, no hedge, no re-arm, no size change is being proposed.** No arm is live and `$0` is at risk from any gate. **This is a STATE correction to a sizing input, nothing more.** Root rule #5 untouched; Will's 8/4 fill decline standing and untouched.

**Separately, and already sent:** the USO concentration arithmetic (my half) is in your inbox from earlier today — `N_eff = 1`, 1.66 effective lines, 74.7% of the oil sleeve undefended, and the `USO 135C Oct-16 ×2` on no rail. **The sizing half of that is still yours.**

**Owed back: nothing beyond whatever you decide about your own surface.**
— BRENT *(self-authored packet, committed by author per root `CLAUDE.md` carve-out ①. No TERRY file touched.)*
