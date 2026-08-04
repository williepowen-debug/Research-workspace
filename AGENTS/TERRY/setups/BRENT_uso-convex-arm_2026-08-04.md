# TRADE CARD — USO — OTM CALL DEBIT SPREAD (BRENT v5.0 main convex arm — DEPLOY GATE v2 leg (b) grade)
**Setup ID:** TRY-BRENT-USOARM · **Trigger class:** GATE (two-leg AND: OVX decay + priced convexity)
**Date:** 2026-08-04 · **Chain pulled:** 10:30 ET live (`chain_fetch.py --no-cache`)
**Thesis owner:** **BRENT** (energy/oil; v5.0 main convex arm, unfired since 7/16). Gate spec is BRENT's; **tenor + size are WILL-RULED 8/3**. TERRY owns construction only.
**Terry verdict:** 🟡 **CONDITIONAL — CLEAN on the TERRY (construction) axis.** Leg (b) **PASSES**. Conditional on leg (a) at the close, which is BRENT's grade and not mine.
**Confidence in trade structure:** High. **Confidence in the thesis: not mine to hold** — and the tape has voted against it twice this week (§7).
**Status:** DECISION-READY / **UNARMED / $0 at risk.** Will holds [Approve] (root rule #5); live broker book governs at fire (rule #4).

> **Capital:** **~$300 this tranche, ~$200 held back — WILL-RULED 2026-08-03.** Inside the existing `~$300 Tier-1 + ~$200 Tier-2` spec, so a sizing decision, not a spec change. The **~$500 defined max-loss cap is unchanged.**
> **⚠️ Do NOT confuse with the existing USO Sep-18 150/165 spread** (filled 7/24, ~$300 at risk, HOLD). Different position, different premise.

---

## 1. One-line setup

Defined-risk far-OTM USO call spread bought **after** oil vol has decayed (leg a) and **only** at a price that leaves ≥2:1 (leg b) — expressing BRENT's supply-loss gap-and-grind while the market prices de-escalation.

## 2. Preconditions — DEPLOY GATE v2 is a hard `(a) AND (b)` on the SAME session

| Leg | Test | Status @ 10:30 ET 8/4 | Owner |
|---|---|---|---|
| **(a)** | OVX ≤ −15% from the post-arm running peak 68.97 ⇒ **≤ 58.6245**, on the **CLOSE** | **OVX 54.37 (−4.95%) = −21.2% from peak.** Cushion widened from ~2.5% (8/3) to **~7.3%**. ⛔ **NOT GRADED BY TERRY** — BRENT grades at ~16:15 on the close. An intraday reading is not the gate. | BRENT |
| **(b)** | Net debit **≤ 33.0% of spread width** (⇔ R:R ≥ 2.0:1), **live chain** | ✅ **PASS at 27.0%** paying the full bid/ask — see §4. | **TERRY** |

**⚠️ Leg (a) fired on the 8/3 close (57.20) but is NOT banked.** v2 requires both legs on one session; with no chain there was no leg (b), so 8/3 satisfied one leg of a two-leg AND. **The arm is neither deployed nor consumed, and leg (a) must fire AGAIN on whatever session actually fills.** Day 13 of 20; **arm expires Thu 8/13.**

**What must NOT be happening:** a re-escalation that lifts OVX back through 58.62 · a confirmed Hormuz reopening (see §5 invalidation) · any attempt to fill this by legging the spread.

## 3. Entry

- **Trigger:** leg (a) confirmed on the close **AND** leg (b) re-graded ≤33.0% on a live chain **at the fill**. This card's 10:30 grade is the grade *for now* — the spec grades leg (b) at fire, so **re-pull before any ticket.**
- **Preferred entry zone:** net debit **$2.28–2.50** (22.8–25.0% of width). Work one limit order near mid.
- **⛔ DO NOT CHASE above net debit $3.30.** That is not a preference — **$3.30 IS the gate** (33.0% of $10). Between $2.70 and $3.30 the trade still passes but is buying materially worse; above $3.30 there is no trade at any argument.
- **ONE spread ticket, limit at net debit, NEVER legged.** At one contract the fill is workable; legging a 1-lot vertical on a −4.5% tape is how you turn a 27% debit into a 35% one.

### ✅ Root rule #6 — CLEAN, no break required, and the interaction BRENT flagged resolved in our favour

BRENT warned that leg (a) opening and rule #6 being satisfied are *normally* correlated but can decouple on a bounce day — low OVX **and** higher crude — and that if so, the gate opening is **not** a rule-#6 waiver.

**That is not today's tape. The opposite happened, and it is the textbook clean day:**

| Measure | Reading, 8/4 ~10:30 ET | Direction for a long call spread |
|---|---|---|
| USO | **$116.94, −4.50%** (2nd consecutive ~5% down session) | 🟢 RED day = the clean colour for buying calls |
| WTI front | **$76.20, −5.15%** | 🟢 |
| OVX | **54.37, −4.95%** | 🟢 vol cheapening *with* price |

**Price and implied vol are falling together — convexity is on sale on both axes.** No break test is invoked because no break is being made. *(Root rule #6 is TERRY's rule; the ratified break test in `RISK_RULES.md` governs departures and is not needed here.)*

## 4. Structure

**USO `Oct-16-2026` 125C / 135C call debit spread ×1.** Net debit **$2.28 mid / $2.70 paying the full bid/ask** = **$228–270 at risk** against the ~$300 ruling.

**Tenor is not a choice: `60–90 DTE` is Will-ruled, and USO's listed expiries jump Oct-16 (74 DTE) → Dec-18 (137 DTE). Oct-16 is the only eligible expiry that exists.** `Sep-18` is out of scope — not priced, not offered. *(BRENT LESSONS #21(b): a shorter-dated vertical at the same moneyness carries a **lower** debit as a % of width, so admitting Sep-18 would have made leg (b) **easier** to pass. The ruling makes the job harder on purpose.)*

### Live chain — USO Oct-16, spot $116.94, 10:30 ET (both legs printed 10:09, same minute)

| Leg | Strike | OTM | Bid | Ask | Mark | Sprd% | IV% | OI |
|---|---|---|---|---|---|---|---|---|
| LONG | 125C | 6.8% | 6.70 | 7.15 | 6.93 | **6.50** | 49.08 | **3,737** |
| SHORT | 135C | 15.3% | 4.45 | 4.85 | 4.65 | **8.60** | 50.76 | **4,405** |

**Leg (b): net $2.70 / $10.00 width = 27.0% ≤ 33.0% ✅ PASS with 6.0pp of room — paying the full spread, not merely at mid.**

| Fill | Debit | % of width | Max profit | R:R | Breakeven | BE as % move |
|---|---|---|---|---|---|---|
| Mid $2.28 | $228 | 22.8% | $772 | 3.39:1 | 127.28 | +8.8% |
| Target $2.50 | $250 | 25.0% | $750 | 3.00:1 | 127.50 | +9.0% |
| Worst case $2.70 | $270 | 27.0% | $730 | 2.70:1 | 127.70 | +9.2% |

**Skew pays you to spread it:** the short 135 leg sells **IV 50.76** while the long 125 buys **49.08** — you are selling **1.68 vols richer** than you buy. Measured, not asserted.

**Vehicle tailwind nobody has written down:** WTI is **backwardated, M1−M3 +$3.77** (PROME 8/3 15:18). USO is a front-month roll vehicle, so backwardation is **positive roll yield** — the usual contango drag on USO runs the *other* way over a 74-day hold. ⚠️ Derived from the M1−M3 figure, **not measured on USO's own roll schedule**; directional, not a number to bank.

### ⚠️ THE SPEC DEPARTURE, STATED IN FIGURES RATHER THAN CARRIED SILENTLY

**BRENT's spec is long ~5% OTM / short ~12–15% OTM. The long leg here is 125 = 6.8% OTM, a +1.8pp departure. BRENT explicitly handed this judgment to TERRY; here is the reason.**

**The in-spec strike fails the gate, and it fails it on liquidity, not on price:**

| Structure | Long/short OTM | Width | Mid | **Full spread** | ≤33%? | OI long/short | Quoted sprd% |
|---|---|---|---|---|---|---|---|
| **124/134** ← closest to ~5% spec | **5.9% / 14.5%** | $10 | 24.5% | **36.5%** | ❌ **FAIL** | **144 / 203** | 22.8 / 14.0 |
| **125/135** ← **SELECTED** | 6.8% / 15.3% | $10 | 22.8% | **27.0%** | ✅ **PASS** | **3,737 / 4,405** | **6.50 / 8.60** |

**124/134 is PROME's 127/138 trap repeating one day later**, and it reproduces PROME's own finding exactly: **USO's open interest lives on the round-number strikes**, the spec band does not sit on one, and building off the arithmetic of the band lands you on dead strikes with punitive quotes. The departure is +1.8pp of moneyness; the alternative is a gate failure **caused by dead strikes rather than by price** — which would be a false negative on the gate, not a real one.

### ⭐ CONSTRUCTION FINDING — leg (b) cannot select a strike, because it is monotonically easier the further OTM you go

| Structure | OTM | **Full spread as % of width** | BE as % move needed |
|---|---|---|---|
| 120/130 | 2.5% / 11.0% | 31.0% | +6.1% |
| **125/135** | 6.8% / 15.3% | **27.0%** | **+9.2%** |
| 130/140 | 11.0% / 19.6% | **21.5%** | +13.0% |

**The gate scores 130/140 as the *best* trade on the board while requiring a 13% move instead of 9%.** Leg (b) is a **necessary condition, not a quality test** — a big pass means *cheap*, not *good*. Read it that way and it works; read it as a ranking and it will walk the book progressively further OTM until nothing ever pays. Flagged to BRENT as a spec observation, not a request to change the gate.

### Rejected

- **124/134** — in-spec and **fails leg (b) at 36.5%** on OI 144/203. The gate is real; dead strikes are what break it.
- **130/140** — yesterday's structure. **Spot moved $5.49 lower overnight ($122.43 → $116.94), relocating the band: 130 is now 11.0% OTM, not 6.2%.** Out of spec on both legs. This card is a rebuild, not a re-mark.
- **120/130** — long leg 2.5% OTM is buying delta, not convexity, and it leaves only 2.0pp of gate room.
- **125/140** ($15 wide) — passes easily at 22.7%, but short leg 19.6% OTM is outside the band and the $340 debit exceeds the ~$300 ruling.
- **Naked long calls** — never (BRENT LESSONS #15). **BNO** — fails leg (b) at 38.7% on thin chains. **XLE** — captured ~12% of the crude move. *(Both closed on PROME's live 8/3 measurement, not on inheritance.)*

### 🔴 The one real defect in this structure, and it is a consequence of the size ruling

**At ~$300 with a ~$2.50 debit this is ONE contract — and a 1-lot cannot take partial profit.** The harvest rule in §6 therefore has to be all-or-nothing.

**This is a known degradation, not an oversight.** On `TRY-WILL-QQQ-VFADE` (built 8/3) I **rejected a cheaper structure specifically to size 2**, because a 1-lot cannot obey a partial-harvest rule. Here the $10 width and the ~$300 ruling force the 1-lot.

**Named alternative if Will prefers rule-obedience to convexity — `125C/130C ×2`:** full-spread debit **$1.50 each = $300** (30.0% of width, ✅ passes), max value $1,000, **max profit $700 (vs $730), BE 126.50 (+8.2%), and max profit reached at USO 130 (+11.2%) instead of 135 (+15.4%)** — a materially higher-probability payoff for ~the same dollar ceiling, **and it can harvest one and hold one.**

**I am recommending 125/135 ×1 anyway**, on one argument: BRENT's thesis targets **Brent $95–100+**, which maps to roughly **USO 140–148** — a world in which both structures pay their maximum and the narrower one gives up nothing, while the $5-wide spread caps at +11.2% and is simply **less convex than the mandate.** This is billed as "the main convex arm." If Will's read is that partial delivery (USO 128–134) is the modal good outcome rather than the thesis landing, **125/130 ×2 is the better ticket and I will build it on request.**

## 5. Risk

- **Max loss budget:** the debit — **$228–270, capped at $300** by the Will ruling. **0.68% of the ~$39.5k book.** $200 held back. Defined-risk: no stop is required and none is used.
- **Invalidation (thesis, BRENT's own discriminators — measurable, not narrative):**
  1. **M1−M3 backwardation flips to CONTANGO.** Currently **+$3.77**, compressed 37.4% from +$6.02 but **NOT flipped** — Jun-17 flipped, and that is the signature of prompt premium being genuinely priced out. A flip kills the premise.
  2. **Hormuz transits recover toward >35/day sustained.** Currently **10/day = 11.4%** of the 88/day baseline, `capacity_tanker` 0 DWT; Lloyd's List Intelligence has the most recent complete week at **39 vs 82 = −52.4% WoW**. ⚠️ Do not convert 39/wk to 5.6/day against the 88/day baseline — different series, blending forbidden by BRENT's own baseline doc. The valid figure is the **WoW ratio**.
  3. ⚠️ **Honest counter BRENT states against himself:** GPS jamming / AIS spoofing / dark transits bias **every** count down, so a dark-led recovery would be **partly invisible** to test 2.
- **Gap/event risk:** this position is **long** convexity — a gap is the payoff, not the risk. The real risk is **decay with no gap**, which is the modal outcome and is exactly what §6 is written against.
- **Concentration — N_eff = 1, and it is the sharpest thing on this card.** The book owns this view **four** ways once this is added: **USO 35 shares** (~$4,200; PROME 8/2 reconcile, *not a live pull*), the **USO Sep-18 150/165 spread**, **STNG**, and this. **Every leg dies on the same event — a genuine Hormuz reopening.** Size to independent views, never to the count of reasons. Concur with BRENT and PROME.
  - ⚠️ **Live consequence of today's tape:** the same −4.5% session is punishing all three existing legs. With USO at 116.94, the **Sep-18 150 strike is 28% OTM with 45 DTE.** Not this card's problem to solve, but Will should not read a new leg as diversification.

## 6. Target / management

- **Max value $1,000** at USO ≥135 (+15.4%). **Breakeven 127.50** at a $2.50 fill (+9.0%).
- **★ NO_HARVEST_RULE (Will-ruled fleet-wide 7/31) — mandatory check.**
  **Q: is there a profitable path on which NO trigger fires?** **YES, and it is a live path:** USO grinds to 128–133 on partial supply-loss delivery, the spread marks $4–6, it never touches 135, no thesis trigger fires, and it decays into Oct-16. **That is the VIXCS death exactly** — every trigger keyed to the move going *further*, none keyed to being in profit.
  **⇒ HARVEST: net mark ≥ $5.40 (2× the $2.70 debit cap) → SELL THE SPREAD, whole, immediately.** Keyed to the position's own P/L, not to the BOJ-equivalent — i.e. not to any thesis event.
  **Trigger-variable check:** the trigger is the position's own mark, which is reached by definition on the profitable path. **VALID.**
  ⚠️ **At 1 contract this is binary — "sell half" is unavailable.** See §4's alternative if that trade-off is unacceptable.
- **Time stop:** **if USO has not traded ≥$125 by 2026-09-15** (~31 DTE remaining), **exit for residual value.** Rationale: this is a gap-and-grind thesis; a gap that has not arrived in six weeks is not arriving, and the final 30 days is where an OTM long leg is punished hardest. This is a mechanical date, not a judgment call.
- **Roll rule:** **NONE, and none is pre-registered.** Any roll requires fresh Will approval from scratch (Non-Negotiable #6 — no roll-by-hope).
- **Review cadence:** marked at every TERRY boot via `paper_book_mark.py` once filled; invalidation tests 1–2 re-read against BRENT's series weekly.

## 7. Why not / counter-trade — the best case against, at full strength

1. **🔴 The tape has voted against this thesis twice this week.** WTI **−5.07% (8/3), −5.15% (8/4)** — roughly −10% in two sessions. This buys convexity into a market actively repricing de-escalation. The gate is designed to buy *after* vol decays, and it is doing exactly that; the uncomfortable question is whether OVX at 54 is decay **or** the market correctly concluding the event is over.
2. **The de-escalation may be real even though the headline is contested.** Iran's MFA denied US talks on the record 8/3 (Baghaei: *"we currently do not have negotiations with America"*), and the only real object is an Oman-mediated temporary route that Iran says does not reopen Hormuz — **0-of-4 on physical legs.** But price does not need the deal to be real; it only needs the market to keep believing it for 74 days.
3. **N_eff = 1 with three legs already on.** See §5. A fourth expression of a view that just lost ~10% in two sessions is the shape of averaging down, even though this is new capital at a new strike.
4. **BRENT's own probability is against a terminal move:** he grades **ORDINARY DIP ~88%, not terminal resolution.** Read plainly, that is an 88% probability the premise survives — but it is also his statement that the *dip* is the base case, and a dip is what a +9.2% breakeven has to overcome.
5. **⚠️ A stale conversion to not build on:** BRENT's card carries `USO $165 ≈ Brent ~$118` as a **static** figure, and the Brent–WTI basis is not static. He is re-deriving it at fire time (DM-003, due 8/13). **Do not build a payoff narrative off it** — including the USO 140–148 mapping in §4, which is mine, derived off the current USO/WTI ratio (~1.534) and inherits the same instability.

**⛔ THE ARGUMENT THAT IS NOT AN ARGUMENT, carried verbatim from BRENT because it must not leak into construction:**
> **"The arm expires 8/13, so take it" is the window-is-closing CHASE, not a reason. THE CLOCK IS NOT EVIDENCE.**

**An arm expiring un-deployed is a CORRECT outcome, not a miss.** Leg (b) happens to price well today; if it had not, "no" was the right answer and would have been given.

## 8. Decision

**Leg (b) verdict: ✅ PASS — 27.0% of width paying the full bid/ask, 6.0pp inside the 33.0% line, on the two most liquid strikes in the region.**
**Leg (a): NOT graded here — BRENT grades it on the 16:15 close. The gate has NOT fired.**

**Proposed:** BUY TO OPEN **1× USO Oct-16-2026 125C/135C call debit spread**, limit **$2.50 net debit**, do-not-chase above **$3.30**. Max loss $250–270.
**Named alternative on request:** 2× **125C/130C** @ $1.50 = $300 — lower ceiling, higher probability, and it can harvest partially.

**Nothing here authorizes capital. Re-pull the chain before any ticket — the spec grades leg (b) live at fire, and this is a 10:30 grade.**

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---
*Built by TERRY 2026-08-04 on BRENT's 8/4 ACTION packet (Will-directed: "tell TERRY to price leg (b) first thing tomorrow") + PROME's 8/3 15:30 rulings relay. Routed to BRENT and PROME. Chain: `chain_fetch.py USO 2026-10-16 --type call --no-cache`, 10:30 ET.*
