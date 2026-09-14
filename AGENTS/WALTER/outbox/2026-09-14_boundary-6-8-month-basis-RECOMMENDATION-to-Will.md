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
