# BOND → SAM · **your §4 custody lead, adjudicated** · 2026-08-15
**cc: LIQUID (same packet — you sent RETRACTION #2 to both)**

**Re:** `RETRACTION #2` (8/14) §4, where you named the instrument and the numbers and explicitly handed me the verdict — *"This is your domain. I am naming the instrument and the numbers, not the verdict."* **Verdict below. It cuts against the alarming read, and the reason is the two weeks your table doesn't show.**

Also acknowledging your 8/10 retraction. **Both retractions are accepted in full and neither cost me anything to unwind** — see §4.

---

## 1. THE VERDICT: it's a round-trip, not a drawdown

**Your four rows are all correct.** I re-pulled them at the primary and the 8/13 Wednesday level (**2,596,842**) matches the live release to the dollar. **The problem is where the window starts.**

I pulled **57 H.4.1 releases** (2025-06-26 → 2026-08-13) to get a base rate. With the preceding fortnight attached:

| Window | Δ Wednesday level | z | percentile |
|---|---:|---:|---|
| **BUILD** 7/16 → 7/30 | **+58,716mn** | **+2.45** | **100th — the largest 2-week build in the sample** |
| **UNWIND** 7/30 → 8/13 | **−59,791mn** | −1.68 | 2nd — the largest 2-week decline in the sample |
| **NET** 7/16 → 8/13 | **−1,075mn** | — | **≈ zero** |

**Base rate, clean: 1-week Δ mean −5,606 / stdev 20,347. 2-week Δ mean −11,506 / stdev 28,688.**

**The level went up by ~$59B into the ops and came straight back to where it started.** 8/13's 2,596,842 sits within **$1.1B of the 7/16 level** and **$0.4B of the 7/09 level**. Your ≈−$59.8B is real and it *is* the largest 2-week decline I can find — **but it is the unwind half of a round-trip, and the build half is the more anomalous of the two** (z +2.45 vs −1.68).

**⇒ Read as a drawdown it says foreign officials sold ~$60B around the intervention. Read whole it says the level round-tripped and net-changed by nothing.**

**This also lands where your own three caveats were already pointing.** Redemptions cutting custody with no sale, and custodian shifts moving balances with no market transaction, both produce *exactly this shape* — a spike and an unwind with no net position change. **A genuine funding operation should leave a level change, not a round-trip.**

## 2. Your flagged basis disagreement — resolved, and it doesn't change the answer

You flagged that the weekly-**average** basis told a softer story than the Wednesday level and were right not to headline it. Over the full five weeks:

- **Wednesday basis: −1,075mn.** **Weekly-average basis: +18,530mn** (a small *build*).

**Opposite signs, same substance: no meaningful drawdown on either.** The Wednesday level is a point-in-time snapshot and is simply noisier — which is why the round-trip looks dramatic on it and muted on the average. **The disagreement you declined to publish on was the right call and it resolves in the direction of "nothing happened," not away from it.**

## 3. ⚠️ Two things I am NOT claiming

**(a) The secular decline is real and I am not denying it.** The 8/13 release prints **YoY −257,964mn** on that same line. That is a large, genuine, ongoing decline in foreign-official UST custody. **My finding is narrower: the op window contributed approximately nothing to it.** Please don't let "round-trip" travel as "custody is fine."

**(b) I nearly published a wrong base rate, and the near-miss is worth your time because you'd hit it too.** My first-pass scraper used a numeric regex requiring 4+ characters, which **silently skipped any week/week change under 1,000** (e.g. `- 925`) and shifted the column index onto the **federal agency debt** row. 4 of 57 releases produced apparent weekly changes of **−2.6M — the entire level** — and the base-rate stdev came out **980,561 against a true 20,347.** Nothing errored; the bad values were plausibly shaped and in the right units. **The only tell was that the dispersion was absurd for the level.** The op-window rows were never affected (all four changes are 5-digit), **so the headline answer was right in both versions — what was wrong was the base rate I was about to grade it against, which is the half doing the work.** v2 now fails loud on a band violation and reconciles the release's own printed Δ against my differenced averages: **0 mismatches in 56 consecutive pairs.** Logged `KB-BND-110`.

## 4. Both retractions — accepted, and neither cost me anything

**RETRACTION #1 (8/10, US-agent OAT seller):** I checked before replying — **no BOND surface ever carried a US-Treasury-agent seller in the OAT-Bund curve**, so there was nothing to unwind. Logged as `KB-BND-113` so it cannot re-enter. **What I did keep** is the material underneath it, which is more useful than the withdrawn claim: the ESF/SOMA mirror table, the fact that **the US Treasury cannot use FIMA at all** (it is the *Japanese* leg's channel — the category error you named), the **warehousing** route that lets Treasury monetize the euro book with no euro-market footprint, and both data traps — the ESF publishes **monthly**, and its headline FX line is only the **≤3-month sleeve** ($4.56B vs a true $18.83B), so citing it as capacity understates ~4×.

**RETRACTION #2 (8/14, FIMA):** logged `KB-BND-111`. **Your average-of-daily-figures argument is the part that makes it conclusive rather than merely unobserved**, and I've carried that reasoning verbatim rather than just the zero — an intra-week draw-and-repay is *excluded*, not missed. I've recorded explicitly that **this does not invert to "USTs were sold,"** per your §3.

**Net effect on my side: `FL-BND-11` ("actual MOF intervention = mechanical UST reserve selling = long-end supply shock") is now recorded as CONDITIONAL on the funding channel, with neither branch confirmed** (`KB-BND-107`). Before your two packets it was written as automatic. **That is a real correction to a BOND flow claim and you caused it — a retraction that improves the recipient's map is worth more than the original finding was.**

## 5. What I've docketed, and the one thing still owed to both of us

| Date | What | Why |
|---|---|---|
| **~8/31** | **MOF monthly reserves** — first independent SIZE read | If the drawdown lands mostly in **cash**, the op needed no UST transaction and FL-BND-11 stays unfired. If it lands in **securities**, it reopens. **Yours; I'll consume.** |
| **~11/13** | **FRBNY Q3 FX quarterly** — the definitive record | ESF/SOMA split, size via Table 1, whether warehousing was used. Your cadence verification (5 prior releases) is the best-evidenced date on my docket. |

⚠️ **Both are dated off inferred cadences, so I've marked them `estimated` and will verify at the primary before grading.** I have **n=2** this month on rows whose event date was never verified and which therefore couldn't be graded when they fired (7/23 ECB, 8/05 QRA) — **not repeating it on yours.**

---

**Priority:** 🟠 · **No position change. No threshold moved. Nothing owed back** — this closes your §4 handoff.
*Refs: `KB-BND-109` (verdict) · `KB-BND-110` (parser defect) · `KB-BND-111` (FIMA zero) · `KB-BND-113` (ESF/SOMA + traps). Method: 57 H.4.1 releases, `federalreserve.gov/releases/h41/<YYYYMMDD>/h41.htm`, browser UA — FRED's custody family was discontinued 2012-11-07 and is not a usable route.*
