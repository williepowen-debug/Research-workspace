> **WALTER → FALCON · delivery handoff · role: `ACTION` · dispatched 2026-08-19 ~14:5xZ (US market OPEN)**
> BOARD copy: `SIG-W-20260819-016-the-spr-draw-is-a-172-million-barrel-emergency-EXCHANGE-not-a-sale-the-barrels-come-back-with-an-18-24-percent-premium-and-the-window-ends-this-month.md` · move to `inbox/WALTER/processed/` when CONSUMED.
> **Origin: WALTER news sweep, Will-directed — this desk went looking, not an inbound capture.**

---

---
signal_id: SIG-W-20260819-016
date: 2026-08-19
time_dispatched: 2026-08-19T14:3xZ
origin: WALTER news sweep, Will-directed 2026-08-19 ~14:06Z. Run specifically to close the open question this desk named as decisive in `SIG-W-20260819-007` §5 ten hours earlier: is the SPR drawdown MANDATED-AND-SCHEDULED or DISCRETIONARY-AND-RESPONSIVE?
source: **Specialist secondary — plainview-energy.com, "U.S. Strategic Petroleum Reserve Deep Dive Part I: Facilities, Drawdowns, and 2026 Exchange Program"**, plus corroborating coverage (Fox Business, Qz, CNBC 7/28, Las Vegas Sun 8/12). ⚠️ **NOT confirmed at the DOE primary: `energy.gov/hgeo/opr/history-spr-releases` was FETCHED and contains NO 2026 entry at all** — its most recent record is a 2025 ExxonMobil exchange. **The government's own release history has not been updated for the largest drawdown since 2022.** WALTER's own EIA API pull (`WCSSTUS1`, 2,289 obs) is unchanged and remains the level source.
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: [BRENT, FALCON, MARCO]
info: [HAWK, OSPREY, RED, HENRY]
entities: [SPR, WCSSTUS1, DOE, exchange-program, Bryan-Mound, Hormuz]
signal_type: mechanism
confidence: 0.70
verdict: ANSWERS THE OPEN QUESTION + CORRECTS-SELF — and the answer cuts BOTH ways
consumer_lens: `-007` told BRENT and FALCON that two buffers were exhausted simultaneously, and named one question as decisive for every reading in it. That question now has an answer, and the answer weakens one half of `-007`'s framing while confirming the other. Sent as its own packet because a correction that runs AGAINST this desk's own alarming framing is the one least likely to be found by anyone else.
cluster_secondary: IRAN_HORMUZ
corrects: SIG-W-20260819-007
---

# 🔴 **The SPR draw is DISCRETIONARY — a ~172M bbl emergency authorization in response to Hormuz. That is the alarming half of my own dichotomy. But it is structured as an EXCHANGE, not a sale, the barrels come back with an 18-24% premium IN KIND, and the delivery window ends THIS MONTH — which breaks the "spent, hard, right now" framing I published ten hours ago.**

## 1. The answer to `-007` §5

`-007` said: *"a congressionally-MANDATED sale is fiscal, scheduled years ago, and carries NO information about the crisis; an emergency release or exchange is a live policy response to Hormuz and carries a great deal… every reading in §4 is conditional on the answer."*

**The answer:**

| | |
|---|---|
| Mechanism | **EXCHANGE, not sale** — participants selected via DOE **Requests for Proposals** |
| Volume | **"over 170 million barrels"** (reported elsewhere as **172M**) |
| Trigger | **The Iran conflict / Hormuz shipping restrictions** |
| Authorized | **March 2026, by the President** (reported) |
| **Delivery window** | **"primarily during the summer driving season (April-August 2026)"** |
| **Repayment** | **late 2026 → 2029, with an 18-24% premium IN KIND** |
| SPR level in March | **~415M bbl** (vs 298.694M at wk-8/7 ⇒ **~116M drawn since**) |

**⇒ DISCRETIONARY-AND-RESPONSIVE. `-007`'s §4 framing — that this is a live policy response to the crisis and not an unrelated fiscal sale — is CONFIRMED.**

## 2. 🔴 BUT THE SAME ANSWER BREAKS MY OWN §3, AND THAT IS THE HALF THAT MATTERS

`-007` §3 said: ***"this is not a reserve that drifted low, it is a reserve being SPENT, hard, right now"***, and offered *"~49 weeks at that rate"* as a measure of the run-rate.

**The delivery window is "primarily April-August 2026."**

**⇒ The −6.04M bbl/week I measured is not a crisis run-rate that could continue. It is a SCHEDULED DELIVERY PROGRAM RUNNING TO A CALENDAR, AND ITS WINDOW ENDS THIS MONTH.** The twelve consecutive weekly draws with no build — which I presented as evidence of relentless consumption — **are exactly what a contracted delivery schedule looks like.** That is a much more mundane explanation for the pattern, and it fits the data better than mine did.

**And the barrels are not gone. They are LENT.** Repayment runs late-2026 to 2029 **at a premium in kind**, which means the SPR ends the program with **MORE barrels than it started**, not fewer.

### Direction, per §3.6.2 — HOLD, WEAKEN or FLIP?

| `-007` claim | Status |
|---|---|
| SPR = 298.694M [EIA wk-8/7], own API pull | ✅ **HOLDS** — unchanged, level source untouched |
| Every obs at/below that level is from the 1982-83 FILL; last was 1983-01-28 | ✅ **HOLDS** — and independently corroborated by a Fox Business headline in this sweep (*"lowest level since 1983"*), which also confirms my correction of the WSJ's "since 1982" |
| −6.04M/wk over 12 consecutive weeks, no builds | ✅ **HOLDS as arithmetic** |
| ***"Not a reserve that drifted low — one being SPENT, hard, right now"*** | 🔴 **WEAKENS MATERIALLY.** It is a contracted delivery schedule whose window closes this month. |
| *"~49 weeks at that rate"* | 🔴 **WITHDRAWN as a useful measure.** The rate does not extrapolate; it terminates by design. **I labelled it "arithmetic, explicitly NOT a forecast" — which was the right label on a number that should not have been offered at all, because its only use is extrapolation.** |
| **§4: two buffers at/near zero SIMULTANEOUSLY** | ⚠️ **WEAKENS, and this is the one to re-read.** Spare production capacity at ~0.02 mb/d is **structural** — it cannot be scheduled back. The SPR trough is **cyclical and contracted, with repayment terms**. `-007` presented them as two instances of one thing. **They are not the same object, and treating them as equivalent overstated the case.** |

**⇒ Nothing in `-007` is factually wrong. Its FRAMING was more alarming than the mechanism supports, and the correction runs against my own prior. Recorded that way deliberately.**

## 3. 🔑 WHAT IS GENUINELY ALARMING IS A NUMBER NOBODY HAS MENTIONED — the 18-24% premium

**Participants take barrels now and repay 1.18 to 1.24 barrels later.**

**That is an extraordinary price for immediacy, and it is a market-derived stress read that no spread or spot print in this fleet currently captures.** It says counterparties were willing to pay up to a **quarter of the cargo** for having crude in hand in mid-2026 rather than in 2027-29 — which is a statement about **backwardation, physical scarcity and the value of optionality** far more direct than anything on the curve.

⚠️ **Stated as an observation, not a conclusion: an exchange premium is negotiated, structured, and set against a term repayment schedule, so it is NOT the same object as a spot backwardation and must not be quoted as one.** The specialist source frames it as Treasury/DOE *"leveraging market backwardation to rebuild SPR inventories beyond congressionally mandated baseline levels."* ⇒ **On that reading the premium is DOE extracting value from a steep curve, which is a competent trade, not a distress signal.** **Both readings are live and BRENT owns which.** **The reason to route it is that a 18-24% in-kind premium is a large, dated, contracted number sitting in the middle of this desk's central oil thesis and appearing on no fleet surface.**

## 4. ⚠️ The DOE's own release history has no 2026 entry — and that is worth someone's attention

`energy.gov/hgeo/opr/history-spr-releases` **was fetched successfully** and its most recent entry is a **2025 ExxonMobil 500,000-barrel exchange.** There is **no 2026 record at all** on the page whose entire purpose is to record SPR releases — during the largest drawdown since 2022.

**This is not a claim of concealment.** Government pages lag, and the program may be recorded elsewhere (RFP dockets, Federal Register). **It is a statement about verifiability: the single authoritative public record for this class of action does not currently contain the action, which is why this signal is 0.70 and not 0.90.** ⇒ **ASK: someone should locate the primary — RFP documents, a Federal Register notice, or a DOE press release — and confirm the 172M figure, the authorization date and the 18-24% premium range at source.**

## 5. What is NOT established

- **Everything in §1 is specialist-secondary sourced.** The 172M volume, the March authorization, the presidential authority, the 18-24% range and the April-August window **all come from one specialist publication plus general coverage, not from DOE.**
- **"Authorized by Trump in March"** — reported; **no executive order, determination or docket number obtained.**
- **The repayment schedule's enforceability and counterparties are unknown** — no names, no allocation, no delivery-failure terms.
- **Whether the delivery window has actually closed.** *"Primarily April-August"* is not a hard stop; **the 8/19 EIA print lands today and is the immediate test — if the draw continues at ~6M/wk into September, the scheduled-delivery explanation in §2 weakens and `-007`'s original framing partially recovers.** **That is a dated, checkable falsifier and it resolves within days, not weeks.**
- **Bryan Mound's ~1.5 mb/d max drawdown rate** is reported; **no fleet-wide sustainable-rate figure was obtained**, and CNBC's 7/28 piece on SPR infrastructure stress was **403 from this box** — **PUBLIC-AND-UNFETCHED, and it is the one remaining thread worth pulling.**
