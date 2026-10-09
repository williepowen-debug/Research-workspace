# WALTER → Will: recommendation on the #6 / #8 contract-month basis (ASKED FOR, 2026-09-14 ~22:34 ET, Telegram msg 4599)

**Status:** RECOMMENDATION MADE, **DECISION PENDING WILL.** Nothing re-specced. Interim handling is live and safe in both directions (`ROUTING_OVERLAYS.md` v0.37).

## ⚠️ DECLARED BIAS — stated to Will first, before the advice
**WALTER benefits from `#6` being quieter**: a false fire sends an `IMMEDIATE` to CARL, HENRY and RED about nothing. ⇒ **I am the wrong desk to be trusted on whether to silence it**, and said so. Same structure as HENRY refusing to re-spec `HEN-46` because every fix moved its own line in its favour.

## THE RECOMMENDATION: DO NOT PICK A MONTH YET

🔑 **There is an unanswered question underneath, and its two possible answers imply OPPOSITE fixes:**

1. **CALENDAR ARTIFACT** — the curve re-prices as time passes, nothing actually falls, the number only looks lower further out. ⇒ fix is a **constant-maturity basis** and the problem disappears.
2. **REAL SEASONAL** — gasoline margins genuinely are weaker in winter. ⇒ the January fire is **telling the truth**, and what is wrong is that **a flat \\$30 line was never the right shape for a seasonal business.**

**Same numbers, opposite conclusions.** ⛔ **Choosing a month before settling this is choosing a number to stop an alarm ringing** — the exact thing HENRY, BRENT and WALTER each refused to do on their own rows tonight.

## ⚠️ THE EVIDENCE CURRENTLY POINTS AGAINST THE COMFORTABLE ANSWER
HENRY assumed the roll steps *"roughly cancel over a cycle"*, **checked, could not establish it, and found the only observable window contradicted it** (`HOX26−HOV26` widened −0.1294 [8/25] → −0.2107 [9/14]). It flagged its own assumption UNVERIFIED rather than leaning on it. ⇒ **the reassuring reading (1) is the one currently lacking support.**

## RECOMMENDED ORDER
1. **Nothing tonight.** Interim handling already safe: the alarm **still fires**, carrying the roll decomposition. **No exposure while this sits.**
2. **Settle (1) vs (2).** It is a **MEASUREMENT, not a judgement** — but it needs price history for **EXPIRED contracts, which our data source drops** (HENRY: *"expired legs are delisted"*). **That is the one genuine blocker**, and it is small and concrete enough to be worth buying if not free.
3. **Then fix, with the answer following from step 2 rather than anyone's preference.**

## IF A DIRECTION IS WANTED NOW ANYWAY — offered WITH its cost, not as a free win
**Change what `#6` MEASURES rather than which month it looks at: fire on margins FALLING SHARPLY over a short matched window, not on margins being BELOW a fixed line.** **Structurally immune to axis (iii)** — a slope common to both endpoints differences out (`THRESHOLD_SCAN.md` v0.44). ⚠️ **Still exposed to axis (ii)** (a roll inside the lookback), so it must be computed on matched months; both are then handled.

⛔ **THE COST, STATED PLAINLY AND NOT BURIED: it changes what the alarm MEANS.** Today `#6` means *"margins are low."* That version means *"margins fell fast."* **They catch different things — a slow grind into genuinely distressed levels would never trip the change form.** **That is a substantive change to something Will signed off 2026-05-08, so WALTER is not making it.**

## THE ONE THING PUT TO WILL
**Authorise finding out whether the ~\\$3/month step is real or an illusion.** Everything else follows from it; **until it is answered, any month WALTER picks is a guess wearing a number.**

---
*Substance and measurements: `ROUTING_OVERLAYS.md` v0.37 boundary block (#6 Oct 39.11 · Nov 35.58 · Dec 32.14 · Jan 30.27; #8 Nov 49.14, \\$0.86 below bar; no live Brent Oct leg). Source: BRENT own pull 2026-09-14 post-close, matched months — BRENT sized the month-DEPENDENCE and explicitly did not claim a grade is wrong.*

---

# 🔴 ADDENDUM 2026-09-14 ~23:0xZ — **THE QUESTION IS ANSWERED. IT IS SEASONAL, NOT A CALENDAR ARTIFACT — AND THAT MAKES THE ALARM WORSE, NOT BETTER.**

**I said settling this needed EXPIRED-contract history we do not have. THAT WAS WRONG — it needed the FORWARD curve, which is live, and which I could not previously pull because I had the symbol format wrong.** *(Working format: `<ROOT><MONTH><YY>.NYM`, e.g. `CLX26.NYM`. See §Instrument below.)*

## THE MEASUREMENT (own pull, 2026-09-14 post-close, matched months, `crack = RB×42 − CL`)

| Month | RB | CL | Crack | Step |
|---|---:|---:|---:|---:|
| Nov26 | 3.1662 | 97.480 | **35.50** | |
| Dec26 | 2.9719 | 92.770 | **32.05** | −3.45 |
| **Jan27** | 2.8360 | 88.680 | **30.43** | −1.62 ← **TROUGH** |
| Feb27 | 2.7757 | 85.330 | **31.25** | +0.82 |
| Mar27 | 2.7712 | 82.730 | **33.66** | +2.41 |
| **Apr27** | 2.9617 | 80.570 | **43.82** | **+10.16** ← **summer-grade changeover** |
| May27 | 2.9300 | 78.680 | **44.38** | +0.56 |
| Jun27 | 2.8708 | 77.180 | **43.39** | −0.99 |
| Jul27 | 2.8004 | 75.850 | **41.77** | −1.63 |
| Aug27 | 2.7408 | 74.710 | **40.40** | −1.36 |

## ⇒ THE VERDICT

⛔ **READING (1), "CALENDAR ARTIFACT", IS REFUTED.** A uniform calendar drift declines monotonically. **This bottoms in January and recovers \\$14 into summer.** It is a **textbook gasoline seasonal V.**

✅ **READING (2), "REAL SEASONAL", IS SUPPORTED** — and the **+\\$10.16 April step** is the tell: that is the **summer-grade gasoline changeover**, a physical/regulatory fact about how gasoline is made, not a data effect. *(The mechanism is WALTER's attribution; the NUMBERS are the measurement.)*

## 🔑 BUT THE CONSEQUENCE INVERTS THE COMFORTABLE CONCLUSION

**"It's real, so the alarm is telling the truth" is WRONG.** ⇒ **A FLAT \\$30 BAR ON A SERIES THAT SEASONALLY TRAVELS ~\\$30–\\$44 WILL BE CROSSED BY THE FRONT MONTH ESSENTIALLY EVERY WINTER, AS ROUTINE.** **`#6` is not mis-calibrated on the wrong month — it is UN-SEASONALISED, and it has an annual false-fire built in.**

📌 **Neither of the two options I put to Will was right.** The fix is not "pick a month" and not "constant maturity" — **it is that a flat bar cannot grade a seasonal series.** ⚠️ **On today's curve the trough (\\$30.43) sits \\$0.43 above the bar** — so the seasonal low is currently near-touching it **without any stress at all.**

## ⚠️ WHAT THIS IS AND IS NOT
- **IS:** the forward curve — **the market's EXPECTED seasonality, priced today.** Strong evidence of SHAPE (nobody prices a +\\$10 April step unless the seasonality is well understood).
- **IS NOT:** a realized-history measurement. **It does not tell us how big the seasonal swing turns out to be in practice**, only what is priced. **HENRY's caveat is therefore NOT discharged** — its unverified "roll steps roughly cancel" question is about REALIZED cycles and still needs expired-contract history.

## §INSTRUMENT — and it upgrades the PROME packet
⛔ **`FORGE/tools/market-data/fetch.py` returns `ERROR 'currentTradingPeriod'` on EVERY dated contract** (`CLX26`, `BZX26`, `HOX26`, all `RB*`) — a KeyError surfaced as an opaque failure. ✅ **But the data EXISTS: `CLX26.NYM` returns 97.480**, corroborating BRENT's 97.52 at a different pull time. ⇒ **the fix is SMALLER than the packet said — accept the `.NYM`-suffixed form and stop crashing — not build a new capability.** 🔑 **And ADD#23 has been telling the fleet to "quote named contracts" for 14 days while the shared tool could not fetch one.**

---

# ADDENDUM 2026-10-09 ~10:2x ET — BRENT's answer (asked on Will's direct instruction; brent-58 by SendMessage), recorded verbatim in substance

**Whose call:** WILL'S. Both letters are Will-signed (5/8); picking a month changes what the alarm reads = a re-spec. BRENT owns the measurement and basis advice only. Neither BRENT nor WALTER can amend the letter. BRENT bias disclosed: held VLO thesis likes wide cracks; neither alarm touches its exit rule (WQ-386 reads the diesel crack).

**#8 (3:2:1 > $50, 2–3 sessions) — BRENT AGREES with "nearest month in which all three legs trade", plus three conditions:**
(a) named-contract identity check on every pull (BZZ26/RBZ26/HOZ26); continuous tickers rejected (today RB=F printed −5.41% labelled RBX26 at 3.1365 vs RBX26.NYM 3.2825 = a different contract);
(b) per-session SETTLE basis for the persistence count; vendor prev_close is NOT a settle (CLX26 prev 90.43 vs 10/8 settle 91.49). Source order: exchange settle → vendor daily row only within $0.15 of → a 14:28–14:30 ET one-minute VWAP labelled ESTIMATE; within ±$0.15 of $50 on the estimate alone = UNKNOWN, not a fire;
(c) name the month switch in the letter: Dec→Jan when BZZ26 expires (~end-Oct) though RBZ/HOZ trade to end-Nov (step ~−$0.61 today).
BRENT holds NO settle-basis #8 level and will not invent one; can produce a 14:28–30 ESTIMATE on request.

**#6 — BRENT AGREES it is a redesign. Split:** SPIKE ≥$50 half stays live on the front MATCHED month (RBX26×42 − CLX26; Nov $46.29 at 10:12 ET, BRENT pull). RE-CROSS ≥$30 half: a flat bar on a seasonal V crosses routinely every winter; precedent = BRENT's own identical "gasoline crack >$30" line RETIRED 2026-07-31 (F4, Will-ruled): "if a crack tripwire is ever wanted again it is a NEW REGISTRATION with base rates — not a re-level." Options for Will: (i) retire the ≥$30 half the same way, or (ii) commission a seasonal/change-rule redesign with base rates (needs realized expired-contract history, not free). Interim fire-plus-decomposition rule stays until Will picks.

**Status:** DECISION PENDING WILL (two asks, below in WALTER's 10/9 brief). Nothing re-specced.

---

# ✅ DECIDED — Will, 2026-10-09 ~10:29 ET, in-session ("okay confirmed go ahead"), after WALTER's two clarifications

Will's ruling text (pasted 10:27 ET, confirmed with WALTER's session-count and month-switch proposals 10:29 ET): *"Approve #8's nearest common named-contract month, with official settlements for the persistence count. Estimates remain provisional. Before activating the revision, make the exact session count and month-switch treatment explicit. For #6, keep the $50 spike trigger and retire the $30 re-cross trigger. Record this as retirement of an insufficiently validated alert—not a proven annual false alarm. Your existing routing correction says the curve did not establish annual crossings. No replacement study is commissioned now; a future proposal needs historical evidence and a clear decision use. Preserve the historical records and existing position exit rules."*
Explicit terms confirmed: #8 fires on the 3rd consecutive official settle strictly > $50.00; 2 = near-trigger watch; estimates never complete a count; a no-settle session neither counts nor resets; switch on the first session after the Brent leg's last trading day; a count spanning a switch restarts at zero.
⚠️ Correction to this memo's own 9/14 addendum: its "crossed essentially every winter, as routine" overstated the evidence (corrected 9/15 in ROUTING_OVERLAYS: the curve did not establish annual crossings). Will's ruling records the retirement on the accurate basis.
Encoded: ROUTING_OVERLAYS/ROUTING_TABLE/ROUTING_CARVEOUTS v0.41, STATE.md; prior text verbatim in design/history/BOUNDARY_6_8_BEFORE_2026-10-09.md (split_verify CONSERVED, 1 adjudicated H1 edit). Owed: BRENT records the Dec→Jan switch date in row #8's record.
