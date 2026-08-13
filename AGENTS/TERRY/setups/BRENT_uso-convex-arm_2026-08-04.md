# TRADE CARD — USO — OTM CALL DEBIT SPREAD (BRENT v5.0 main convex arm — DEPLOY GATE v2 leg (b) grade)
**Setup ID:** TRY-BRENT-USOARM · **Trigger class:** GATE (two-leg AND: OVX decay + priced convexity)
**Date:** 2026-08-04 · **Chain pulled:** 10:30 ET live (`chain_fetch.py --no-cache`)
**Thesis owner:** **BRENT** (energy/oil; v5.0 main convex arm, unfired since 7/16). Gate spec is BRENT's; **tenor + size are WILL-RULED 8/3**. TERRY owns construction only.
**Terry verdict:** 🔴 **DEAD (terminal) 2026-08-13 — ARM EXPIRED UNFIRED on day 20 of 20; Will ruled let-expire in session.** Leg (b) is **UNPASSABLE** on the 11:39 ET live chain: USO **126.11**, net debit **37.6% at MID / 58.0% paying the full bid/ask** vs the ≤33.0% gate — intrinsic on the 125/130 alone is **$1.11 = 22.2% of width** before any time value. Legs (a)/(a2) PASS (OVX 50.08, well under 58.6245) — **the death is purely priced-out: the move the arm was built to catch (USO 115.96 → 126.11, +8.8%) arrived 8/5–8/13 while the card sat DECISION-READY with no [Approve].** Not fired late, not chased. `$0` at risk from build to death. **Death record §12; latency finding routed to BRENT same session.** *(was 8/4: 🟡 CONDITIONAL — CLEAN on the TERRY construction axis; recommendation `125/130 ×2` @ limit `$1.50` BRENT-ruled 11:48; leg (b) 26.0% worst-case / 16.6% mid on the 12:24 chain, passing outright — full grading history preserved in §§2–11.)*
**Confidence in trade structure:** High. **Confidence in the thesis: not mine to hold** — and the tape has voted against it twice this week (§7).
**Status:** 🔴 **DEAD (terminal) 2026-08-13 — arm expired unfired, `$0` at risk from build to death.** *(was: DECISION-READY / UNARMED / $0 at risk; Will held [Approve] per root rule #5 — the approval was never granted and the gate-passing window closed under it. See §12.)*

> **Capital:** **~$300 this tranche, ~$200 held back — WILL-RULED 2026-08-03.** Inside the existing `~$300 Tier-1 + ~$200 Tier-2` spec, so a sizing decision, not a spec change. The **~$500 defined max-loss cap is unchanged.**
> **⚠️ Do NOT confuse with the existing USO Sep-18 150/165 spread** (filled 7/24, ~$300 at risk, HOLD). Different position, different premise.

---

## 1. One-line setup

Defined-risk far-OTM USO call spread bought **after** oil vol has decayed (leg a) and **only** at a price that leaves ≥2:1 (leg b) — expressing BRENT's supply-loss gap-and-grind while the market prices de-escalation.

## 2. Preconditions — DEPLOY GATE v2 is a hard `(a) AND (b)` on the SAME session

| Leg | Test | Status @ 10:30 ET 8/4 | Owner |
|---|---|---|---|
| **(a)** | OVX ≤ −15% from the post-arm running peak 68.97 ⇒ **≤ 58.6245**, on the **CLOSE** | **OVX 54.37 (−4.95%) = −21.2% from peak.** Cushion widened from ~2.5% (8/3) to **~7.3%**. ⛔ **NOT GRADED BY TERRY** — BRENT grades at ~~16:15~~ **16:00** on the close. An intraday reading is not the gate. | BRENT |
| **(b)** | Net debit **≤ 33.0% of spread width** (⇔ R:R ≥ 2.0:1), **live chain** | ✅ **PASS.** Graded three times on three live chains: 10:30 wide 27.0% · ~~11:06 narrow 34.0% FAIL worst-case / 25.5% mid~~ · **12:24 (§11.B) narrow `125/130` = 26.0% worst-case / 16.6% mid — PASSES OUTRIGHT, no limit-construction needed to make it pass.** Gate still enforced as a limit price. | **TERRY** |

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

**Vehicle tailwind nobody has written down:** WTI is **backwardated, M1−M3 ~~+$3.77~~ → ✅ CORRECTED 8/4 to +$4.66** (BRENT self-correction 11:35 — his 8/3 curve table was pulled mid-session and written as if it were settles; the Brent leg was roll-exposed on top of it. **The number is BRENT's, not PROME's — PROME relayed it accurately.**). **The error ran in my favour: +$4.66 is MORE positive roll yield than +$3.77, so this tailwind was understated.** USO is a front-month roll vehicle, so backwardation is **positive roll yield** — the usual contango drag on USO runs the *other* way over a 74-day hold. ⚠️ Derived from the M1−M3 figure, **not measured on USO's own roll schedule**; directional, not a number to bank.

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
  1. **M1−M3 backwardation flips to CONTANGO.** ⚠️ **THIS IS A KILL LINE AND IT CARRIED A WRONG NUMBER UNTIL 8/4 — ~~+$3.77, compressed 37.4%~~ → the 8/3 settle was +$4.66, compressed 22.6% from +$6.02.** Corrected by BRENT's own `consumer_check.py --old 3.77` at his closeout, inside the hour, on a card that may be approved today. **The error ran in my favour — the curve sat FURTHER from a contango flip than this card claimed, so the invalidation was further from tripping, not closer.** *(A kill line must carry the true number regardless of which way the error runs: misquoted toward the flip, the trade gets killed early on a figure that was never real. Same class as VIOLET carrying HENRY's stale gamma flip for 5 days.)* **📅 LIVE 8/4 ~11:10, explicitly IN-PROGRESS not a settle: WTI M1−M3 +$3.01, Brent Oct−Dec +$3.09 — cumulative −50.0% / −45.8% across two sessions. STILL BACKWARDATED. NO CONTANGO FLIP. Front/back ≈3.07×, same signature two sessions running.** ⇒ **Test #1 is compressing FAST but has NOT fired.** Re-grade on the close before any ticket — do not bank an intraday figure as a settle, which is the whole lesson of the correction above. Jun-17 *did* flip, and that is the signature of prompt premium genuinely being priced out.
  2. **Hormuz transits recover toward >35/day sustained.** Currently **10/day = 11.4%** of the 88/day baseline, `capacity_tanker` 0 DWT; Lloyd's List Intelligence has the most recent complete week at **39 vs 82 = −52.4% WoW**. ⚠️ Do not convert 39/wk to 5.6/day against the 88/day baseline — different series, blending forbidden by BRENT's own baseline doc. The valid figure is the **WoW ratio**.
  3. ⚠️ **Honest counter BRENT states against himself:** GPS jamming / AIS spoofing / dark transits bias **every** count down, so a dark-led recovery would be **partly invisible** to test 2.
- **Gap/event risk:** this position is **long** convexity — a gap is the payoff, not the risk. The real risk is **decay with no gap**, which is the modal outcome and is exactly what §6 is written against.
- **Concentration — N_eff = 1, and it is the sharpest thing on this card.** ~~The book owns this view **four** ways once this is added: **USO 35 shares** (~$4,200; PROME 8/2 reconcile, *not a live pull*), the **USO Sep-18 150/165 spread**, **STNG**, and this.~~
  🔴 **CORRECTED 2026-08-04 15:50 AGAINST A FULL TWO-ACCOUNT BROKER READ (Will-confirmed) — the count was wrong in BOTH directions: it named a position that is not held and missed two that are.**

  | Oil expression | Value | Cost | On the old list? |
  |---|---|---|---|
  | **USO 35 units** | **$4,057.55** | $4,266.90 | ✅ (est. ~$4,200 — close) |
  | **USO `Oct-16` 135C ×2** | **$910.00** | $1,421.33 | 🔴 **MISSING** |
  | USO Sep-18 150/165 call debit spread ×1 *(Robinhood)* | ~$65 | ~$300 | ✅ |
  | **XLE Sep-30 65C ×2** | **$98.00** | $455.35 | 🔴 **MISSING** |
  | ~~STNG~~ | — | — | 🔴 **NOT IN THE BOOK** |
  | *this card, proposed* | *+$300* | | |

  **⇒ FIVE live oil expressions, not four — `$5,131` at market — and this card would be the sixth.** **Every leg still dies on the same event: a genuine Hormuz reopening.** *(Broker-verified 8/4 across Fidelity + Robinhood; Will confirmed "this is it" — the book is complete. Supersedes the 8/2 PROME reconcile, which was an estimate and is why STNG survived on this line.)*

  ★ **And the proportion belongs on the card: we are debating a `$300` convex tranche sitting on top of `$4,058` of LINEAR USO shares — 11.6% of the account, no defined risk on the largest leg.** That is not mine to rule on (share exposure is Will's/BRENT's), but sizing the convex arm without it stated is sizing against the wrong denominator. **Size to independent views, never to the count of reasons.** Concur with BRENT and PROME.

- 🔴 **THE ALTERNATIVE STRUCTURE `125C/135C ×1` IS UNAVAILABLE — DO NOT FILL IT. (Found 8/4 15:45 from broker truth, Will-confirmed.)** Will is **long `USO Oct-16 135C ×2`**. Selling a 135C does not create a short leg — **it closes half an existing long.**

  | | Intended | What would actually execute |
  |---|---|---|
  | Book after | 125/135 debit spread, defined risk | **long 1× 125C + long 1× 135C** |
  | Risk | capped both ends | more premium at risk, **no short leg** |

  **⇒ The fallback is struck.** ✅ **The RECOMMENDED `125C/130C ×2` is UNAFFECTED** — it never touches the 135 strike, so BRENT's ruling #2 survives intact and this is one more argument for it. ⚠️ **If Will holds the ratified ~12–15% short-leg band, the answer is now NO TRADE, not "fall back to the wide"** — that option no longer exists in this account. *(Rule #6, position truth: this is exactly the failure the rule exists to prevent — a structure that prices correctly and executes into something else.)*
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
**Leg (a): NOT graded here — BRENT grades it on the 16:00 close. The gate has NOT fired.**

**Proposed:** BUY TO OPEN **1× USO Oct-16-2026 125C/135C call debit spread**, limit **$2.50 net debit**, do-not-chase above **$3.30**. Max loss $250–270.
**Named alternative on request:** 2× **125C/130C** @ $1.50 = $300 — lower ceiling, higher probability, and it can harvest partially.

**Nothing here authorizes capital. Re-pull the chain before any ticket — the spec grades leg (b) live at fire, and this is a 10:30 grade.**

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## 9. 🔴 UPDATE 2026-08-04 ~12:20 ET — BRENT RULED BOTH QUESTIONS. **THE RECOMMENDATION FLIPS TO `125/130 ×2`, AND MY §4 RECOMMENDATION WAS WRONG.**

### A. ★ I committed the exact error I had just diagnosed one section earlier

**BRENT's ruling #2, and he is right:** leg (b) scores the wide spread **better** (27.0% vs 30.0%) because it is cheaper per unit of width — **and the wide spread is the worse trade.** My §4 "CONSTRUCTION FINDING" says in the abstract that leg (b) rewards cheapness over quality and must never be read as a ranking. **I then recommended the structure leg (b) scored higher.** That is not an analogy for the pathology; **it is the pathology, live, in the structure I built.**

**His payoff table, at my own debits, settles it:**

| USO | ≈WTI | %move | `125/135 ×1` | `125/130 ×2` | narrow edge |
|---|---|---|---|---|---|
| 126.50 | 82.7 | +8.0% | −$120 | **$0** | +$120 |
| **130.00** | **85.0** | **+10.9%** | **+$230** | **+$700** | **★ +$470** |
| 132.00 | 86.3 | +12.6% | +$430 | +$700 | +$270 |
| **134.70** | 88.1 | +15.0% | +$700 | +$700 | **crossover** |
| 135.00 → 148 | 88.3+ | +15.2%+ | +$730 | +$700 | −$30 |

**⇒ THE WIDE NEVER BEATS THE NARROW BY MORE THAN $30. THE NARROW BEATS THE WIDE BY UP TO $470.**

**And the thesis-shape answer I asked for and got wrong: USO 130 ≈ WTI ~85 ≈ last Friday's close ($84.67).** The narrow structure reaches **maximum value on a simple round-trip back to 7/31** — no new highs, no thesis landing, just this week's two-session gap reversing. The wide needs **USO 135 ≈ WTI ~88.4**, *above* where the week started. **I anchored on the thesis-lands world (Brent $95–100 ⇒ USO 140–148); BRENT's own registered ~85–88% ORDINARY DIP says the modal good outcome is the round-trip — and that is precisely the zone where the narrow pays $700 and the wide pays $230.**

**Ruling #1 also ratified:** leg (b) is a **FLOOR and a VETO, never a ranking** — *"a larger pass means CHEAPER, not BETTER."* BRENT located the defect more precisely than I did: **the spec is not silent on strike selection — the moneyness band selects and leg (b) can only reject. The actual defect is that the band has no LIQUIDITY QUALIFIER**, which is what put 124/134 on OI 144/203. He has proposed a paired amendment to Will (loosening: nearest listed strike meeting a liquidity bar; tightenings: long leg capped at **8.0% OTM**, departure stated in figures = now mandatory). **My +1.8pp departure is accepted for today.**

### B. 🔴 BUT THE FRESH CHAIN CHANGES THE GATE ANSWER — and I am not relaxing the standard to fit the ruling

**Re-pulled 11:06 ET, USO $117.52** (spot rose from 116.94): `125C 7.10/7.70 (OI 3,737)` · `130C 6.00/6.25 (OI 5,996)` · `135C 4.70/5.35 (OI 4,405)`.

| Structure | Width | Mid | % width | **FULL spread** | **% width** | Leg (b) worst-case |
|---|---|---|---|---|---|---|
| `125/135 ×1` | $10 | 2.38 | 23.8% | **3.00** | **30.0%** | ✅ **PASS**, 3.0pp room |
| `125/130 ×2` | $5 | 1.28 | 25.5% | **1.70** | **34.0%** | ❌ **FAILS by 1.0pp** |

**⇒ The structure BRENT ruled me to build FAILS leg (b) paying the full bid/ask, and passes only at mid (25.5%).** That is PROME's own "coin-flip on execution quality" language for 127/138 yesterday, and PROME graded that MARGINAL.

**I graded the wide at worst-case and called it PASS. Consistency requires grading the narrow the same way — so it fails.** I am not switching to the mid-based reading because it delivers the answer the ruling wants; **that would be relaxing a hard guard to make a preferred structure fit, which the break test forbids by name.**

**⭐ AND THIS IS THE COMPLETED VERSION OF MY §4 FINDING — leg (b) is biased in BOTH directions at once:**
> **It rewards going further OTM (lower probability), AND it penalizes narrowing the width (higher probability) — because a fixed bid/ask friction is a bigger fraction of a smaller width.** The 125C alone quotes $0.60 wide: that is 6% of a $10 structure and **12% of a $5 one.** So leg (b) systematically disfavours exactly the structures BRENT's payoff math prefers. **That is a stronger argument for his ruling-#1 amendment than the one I originally sent him.**

### C. ⇒ RESOLUTION — make the gate the LIMIT PRICE, which is what a veto should be

**The gate stops being an execution gamble the moment it is the limit.**

> ⚠️ **THIS TABLE IS SUPERSEDED — see §11.** The limits below were anchored to the GATE alone; BRENT ruled 11:48 that they also had to clear **Will's ~$300 size ruling**, which ~~`$1.65`~~ × 2 × 100 = ~~`$330`~~ breached. **Operative limit is `$1.50`.** Retained as the reasoning that produced it.

| Structure | ~~Hard limit = the gate~~ | Work from | Risk at the limit | Max value |
|---|---|---|---|---|
| **`125/130 ×2` ← RECOMMENDED (BRENT-ruled)** | ~~**$1.65 net debit** (33.0% of $5)~~ → **`$1.50` (30.0%)** | mid **$1.28** *(11:06; **$0.83** at 12:24)* | ~~**$330**~~ → **$300** | $1,000 |
| `125/135 ×1` (alternative) | **$3.30 net debit** (33.0% of $10) | mid **$2.38** *(11:06; **$1.93** at 12:24)* | $330 | $1,000 |

**If the narrow fills at ≤$1.65, leg (b) is satisfied by construction. If it cannot fill there, there is no trade — and that is a correct outcome, not a miss.** There is genuine room to work between $1.28 and $1.65 on strikes quoting **4.08% (130C)** and **8.11% (125C)** with OI 5,996 / 3,737.

**⚠️ Departure BRENT named against himself and I carry forward: `125/130` puts the short leg at 11.0% OTM against the ratified `~12–15%` band — 1.0pp BELOW it.** The band exists to preserve convexity; moving the short leg closer deliberately trades ceiling for probability. **That is outside a band Will ratified, so neither BRENT nor I may override it. BOTH structures go to Will. If Will holds the short-leg band, `125/135 ×1` stands exactly as built in §4.**

**Secondary but real:** ×2 restores the `NO_HARVEST_RULE` — **sell one at 2×, hold one.** The VIXCS scar should not be re-opened for $30 of ceiling.

### D. Live at 12:20 — nothing here fires anything

**USO $117.52 · WTI $76.95 (−4.22%) · OVX 54.36 (−4.97%).** Still a red day for crude with vol falling — **root rule #6 stays CLEAN.** Leg (a) still ungraded (BRENT's, on the close). **M1−M3 +$3.01 in-progress, still backwardated, no contango flip** — §5 test #1 compressing fast, **not fired.**

## 10. Decision — ~~REVISED~~ **SUPERSEDED BY §11. Do not fill off this section.**

~~**Proposed (BRENT-recommended):** BUY TO OPEN **2× USO Oct-16-2026 `125C/130C` call debit spread**, **limit $1.65 net debit** (work from $1.28), max loss **$330**.~~ → **limit `$1.50`, max loss `$300`** (§11.A).
**Alternative if Will holds the ~12–15% short-leg band:** **1× `125C/135C`**, limit **$3.30**, work from ~~$2.38~~ **$1.93** (12:24).

**Both are conditional on leg (a) firing on the close — BRENT's grade, not mine — and on a leg (b) re-pull at the fill. The gate has NOT fired. Nothing is authorized.**

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## 11. 🔴 UPDATE 2026-08-04 **12:24 ET** (wall clock, `date`-verified) — BRENT'S SIZE RULING APPLIED, AND A FRESH CHAIN CHANGES THE PICTURE IN OUR FAVOUR

### A. ⚖️ BRENT'S RULING ACCEPTED IN FULL — limit is `$1.50`, not ~~`$1.65`~~

BRENT endorsed the §9.C limit-price construction as **the literal spec, not a relaxation** — the graded quantity is the **net debit at fill**, and a limit priced at the gate either fills inside the gate or does not fill. **He then caught a defect neither PROME nor I flagged: ~~`$1.65`~~ × 2 × 100 = ~~`$330`~~ breached Will's `~$300` size ruling by 10%.** I anchored the limit to the **gate** and never checked it against the **size ruling** — two constraints bind this trade and I applied one.

| | ~~$1.65 (mine)~~ | **$1.50 (RULED)** |
|---|---|---|
| Cost | ~~$330~~ ⛔ over `~$300` | **$300** ✅ |
| Leg (b) | ~~33.0%~~ — on the boundary | **30.0%** ✅ 3.0pp inside |
| Max profit | ~~$670~~ | **$700** |
| Breakeven | ~~126.65~~ | **126.50** |

**Accepted without argument — better on every axis.** *One disclosure against the ruling I am accepting: Will's number carries a tilde (`~$300`), so $330 is arguably inside it. I am treating it as hard anyway, because $1.50 is superior on every other axis and needs no tolerance argument to justify it.*

### B. 🔴 THE 12:24 CHAIN — THE STRUCTURE GOT MATERIALLY CHEAPER, AND THE NARROW NOW PASSES OUTRIGHT

`chain_fetch.py USO 2026-10-16 --type call --no-cache`, **three pulls at 12:22 / 12:23 / 12:24**. Spot **USO $115.96** (from $116.94 at 10:30).

| Leg | Bid | Ask | Mark | Sprd% | OI | Last trade |
|---|---|---|---|---|---|---|
| LONG 125C | 6.10 | 6.95 | 6.53 | 13.03 | 3,737 | 11:34 |
| SHORT 130C | 5.65 | 5.75 | 5.70 | **1.75** | 5,996 | 12:06 |
| *(alt)* SHORT 135C | 4.35 | 4.85 | 4.60 | 10.87 | 4,405 | 11:52 |

| `125/130 ×2` | net debit | leg (b) | cost |
|---|---|---|---|
| At mid | **$0.83** | **16.6%** ✅ | $166 |
| **Paying the full bid/ask (worst case)** | **$1.30** | **26.0%** ✅ | **$260** |

**⇒ The narrow no longer needs the limit construction to pass. It passes outright at worst-case — 7.0pp inside the line.** Net debit at mid fell **$1.28 → $0.83 (−35%)** as USO fell a further 0.84%. *(Recorded because it cuts against the story I told at 11:06: I graded the narrow FAIL at worst-case and built an entire resolution mechanism around that. Two hours later the market made the mechanism unnecessary. The mechanism was still right to build — it is what makes the gate binding on execution rather than predictive of it — but the FAIL grade it was built to solve had a shelf life of ~80 minutes.)*

### C. ⚠️ A DEGENERATE QUOTE, CAUGHT AND CLEARED — the reason there are three pulls, not one

The **12:22 and 12:23** pulls both returned **130C bid `5.70` = ask `5.70`, spread `0.00%`**. A locked market cannot persist in a real book, and it also **violated strike monotonicity** (130C bid `5.70` = 129C bid `5.70`; a lower-strike call must bid higher). I refused to compute a net debit off it. **By 12:24 it had resolved to a genuine `5.65 / 5.75` — the tightest two-sided quote on the strip.**

**Had I graded off the 12:22 quote I would have published a worst-case of `$1.25 / 25.0%` — right verdict, wrong number, and unreproducible by anyone re-pulling.** The chain-wide scan found exactly one other locked strike (150C), so this is a per-strike feed artifact, not a broken tool. ⇒ **Adopted: a `0.00%` spread is a REJECT, not a tight market — re-pull before grading.** *(Consistent with rule #4 and with `chain_fetch.py` having no safe degraded output.)*

### D. ★ AT EQUAL DEBIT %, THE NARROW STRICTLY DOMINATES — BRENT'S RULING #2 IS STRENGTHENED, AND THE WIDTH BIAS HAS TEMPORARILY VANISHED

Both structures now grade at **exactly 26.0%** worst-case (`$1.30` on a $5 width ×2; `$2.60` on a $10 width ×1). Equal debit-% + equal $1,000 max value ⇒ **identical max loss `$260` and identical max profit `$740`.**

| | `125/130 ×2` | `125/135 ×1` |
|---|---|---|
| Max loss | $260 | $260 |
| Max profit | $740 | $740 |
| **USO needed for max** | **130 = +12.1%** | 135 = +16.4% |

**⇒ The narrow reaches the same ceiling on a 4.3pp smaller move, and is worth ≥ the wide at every price above 125. The crossover BRENT computed at 134.08 does not exist at these prices — the wide's edge came entirely from carrying a lower debit %, and that gap has closed.** The width bias he and PROME measured (friction ~$0.37–0.38 regardless of width) is real but is **currently swamped by the 130C quoting 1.75% wide** — a state of the tape, not a repeal of the finding. **Ruling #2 stands, now with no cost penalty at all.**

### E. ⇒ WHAT I AM AND AM NOT DOING WITH THE LIMIT

**The limit stays `$1.50` as BRENT ruled.** I am **not** unilaterally re-pricing it to the fresh worst case, even though `$1.50` now sits **$0.20 ABOVE the market's own worst case** and is therefore loose rather than tight.

**Proposed to BRENT for his ruling before the close (his gate, his number):** make the limit a **rule instead of a constant** —

> **`limit = MIN( $1.50 , worst-case net debit on the fire-time chain )`**

It is **monotone-tightening by construction** — it can only ever lower the limit below the ruled number, never raise it — so it cannot breach the gate or the size ruling and needs no re-ratification. It also survives a moving tape, which a hardcoded number demonstrably does not: **BRENT's `$1.50` was correct against an input (`mid $1.28`) that was 80 minutes stale by the time he wrote it.** ⚠️ **It does reduce fill probability, and BRENT explicitly reserved "will it fill" as a Will question — which is exactly why I am proposing it rather than applying it.**

### F. Live at 12:24 — nothing here fires anything

**USO `$115.96` (−5.25%)** · leg (a) **still ungraded — BRENT's, on the close ~16:00.** Red day for crude; **root rule #6 stays CLEAN, no break invoked.** **The gate has NOT fired. $0 at risk. Nothing is authorized.**

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## 12. 🔴 TWO GRADING RULES ADOPTED BEFORE THE CLOSE — READ BOTH BEFORE ACTING ON LEG (a)

### A. **LEG (b) WILL NOT BE RE-GRADED BEFORE FIRE. THIS CARD'S 26.0% IS DATED, NOT STALE.**

Leg (b) was graded **five times this morning by three agents**, while leg (a) could not resolve until the 16:00 close:

| Time | Grader | `125/130 ×2` worst case | Verdict |
|---|---|---|---|
| 10:30 | TERRY | *(wide only)* | — |
| 11:06 | TERRY | 34.0% | ⛔ FAIL |
| 11:38 | PROME | 38.0% | ⛔ FAIL "and worsening" |
| **12:24** | **TERRY** | **26.0%** | ✅ **PASS** |
| 13:01 | TERRY *(incidental, `--legs` test)* | 31.0% | ✅ PASS |

**Every one of those was correct at its timestamp. Not one of them could be acted on**, because the gate is `(a) AND (b)` and (a) does not exist until the close.

★ **Had anyone acted on the 11:38 `38.0% FAIL and worsening`, this arm would have been stood down on a number that was `26.0%` forty-six minutes later.** The debit moved **5.0pp in 37 minutes**; its empirical half-life at this desk is **~40 minutes.**

**⇒ `RISK_RULES.md` #14 adopted: net debit is a MOMENT property, not a structure property.** What is stable and *is* graded now — strikes exist, OI 3,737 / 5,996, two-sided quotes, quote sanity clean on both legs, tenor and size in spec — is **READINESS, and it PASSES.** The **value** gets one grade, **at fire**.

⛔ **So: do not "update" this card to the newest print. Chasing the number is the behaviour that caused this morning's drift.** The fire-time invocation is:
```
python3 AGENTS/TERRY/scripts/chain_fetch.py USO 2026-10-16 --type call --no-cache --legs 125,130
```
**It exits 2 if either leg is locked/crossed/dead/no-bid — the guard that did not exist at 12:22 this morning.**

### B. ⚠️ **IF LEG (a) FIRES ON THE CLOSE, THAT IS NOT EVIDENCE THE THESIS IS WORKING. IT IS THE OPPOSITE, BY CONSTRUCTION.**

Leg (a) fires when **OVX has decayed ≥15% from its peak.** Leg (b) got easier because **USO fell another 5%.** Both legs open **as the market prices *less* of BRENT's supply-loss thesis.**

**That is the design, and it is a good one** — this is a deliberate fade of de-escalation, so of course the entry cheapens as conviction drains. **But it means the gate firing carries ZERO thesis information.**

> **On the same morning: leg (a)'s cushion widened `2.5% → 7.3%` while BRENT cut his own dip confidence `88% → 85%`. Those two moved together by construction. One is not corroboration of the other.**

⛔ **Written here BEFORE the close deliberately, because the pull to read a firing gate as confirmation arrives exactly when capital is about to move** — and the tape has now voted against this thesis three consecutive sessions. **The thesis case must stand on BRENT's evidence (the curve refusing to flip to contango, the physical leg, the tolled-corridor reading), never on the fact that his entry got cheap.** *(`RISK_RULES.md` #15. Construction-side observation about the GATE's information content — not a re-underwriting of the oil thesis, which is BRENT's and is not mine to grade.)*

---
*Built by TERRY 2026-08-04 on BRENT's 8/4 ACTION packet (Will-directed: "tell TERRY to price leg (b) first thing tomorrow") + PROME's 8/3 15:30 rulings relay. §9–10 added on BRENT's two rulings + his M1−M3 self-correction; §11 added 12:24 on his size ruling + a fresh chain; §12 added **13:32** (grading cadence + gate-information; time read from `date`, and it was **13:35 as first written** — a future stamp, in the commit that adds the rule against them). Chains: `chain_fetch.py USO 2026-10-16 --type call --no-cache` at 10:30, 11:06 and 12:22/12:23/12:24 ET.*
*⚠️ **Timestamp note:** §9's "12:20" and §10's stamps were written ~11:11 wall-clock and run ~+69 min fast (see STATUS ④). §11's times are `date`-verified. Earlier stamps left as written rather than silently rewritten.*

---

## 13. 🔴 DEPLOY GATE **v3** RATIFIED (BRENT, Will-approved 8/4) — AND MY "16:15" WAS WRONG

### A. ⛔ THE CORRECTION, AND IT IS MINE

**`^OVX`'s final 5m bar is `16:00`. Not 16:15.** *(`^VIX` runs to 16:10; OVX does not. BRENT pulled the bars rather than inherit my figure.)*

**I asserted 16:15 and propagated it to five surfaces** — this card, `INDEX.md`, `SETUPS.tsv`, `TRADE_BOOK.md`, `STATUS.md` — and stated it to Will repeatedly through the session.

★ **The consequence is not cosmetic: under v2 the execution window was ZERO minutes, not fifteen.** Leg (a) needed the OVX **close** and leg (b) needed a **live chain**, both on one session — and the chain dies at the same instant the close prints. **v2 was an unfillable gate and nobody noticed, because a "tight but workable 15 minutes" is exactly the belief that stops you checking.**

⚠️ **It failed in the COMFORTING direction.** BRENT's framing, adopted: *neither of us should carry an exchange-hours fact we have not pulled* — he had it flagged `UNVERIFIED` in his own SCRATCH and could equally have inherited mine. **Corrected on every surface; struck, not silently rewritten.**

### B. ✅ v3 — what actually changed, and it fixes the zero-minute window

| Leg | Cadence | Test |
|---|---|---|
| **(a)** vol decompression | **daily** | **MOST RECENT official OVX close** ≤ peak × 0.85 (**≤ 58.6245**). A **STATE** — known at 09:30, holding all session. *(v2 said "this session's close"; that phrase was the whole defect.)* |
| **(a2)** live non-reversal 🔻**NEW** | **minute** | At the ticket, **OVX must PRINT ≤ the same frozen line.** Fill any moment it holds; **never while it doesn't.** |
| **(b)** structure economics | **minute** | **UNCHANGED — mine.** ≤33.0% of width, live chain, **at fill.** |

**Root cause (BRENT's own):** v2 was a **mixed-latency basket wearing a single window** — leg (a) daily, leg (b) minute. **Base-rated before proposing** (2007→2026, n=4,729, 113 episodes): fire rate 68.1%/20td · slippage from filling a session later **−0.04%** · tail 38.2% → 39.5% · leg (a2) blocks 7.8%. ⛔ **Disclosed cost, ratified with it on the table: on 31.2% of fire sessions OVX closes back ABOVE the line.**

### C. ⇒ WHAT THIS MEANS NOW — the arm did **not** expire tonight

**BRENT's machine-read at 13:57: (a) MET** (8/3 close 57.20 ≤ 58.6245) · **(a2) MET** (OVX 53.20, session high 56.50, line never breached today) · **(b) mine, at the ticket.**

**⇒ Under v3 leg (a) is a daily STATE, so it is known at 09:30 and holds all session.** The "fill it in the last fifteen minutes or lose the day" framing is gone — **and with the market now closed, the live question moves to the next session, not to a missed window.**

✅ **BRENT explicitly confirms `RISK_RULES` #14 and says v3 encodes it: he is NOT asking for a pre-close leg-(b) number and will NOT treat my 12:24 `26.0%` as banked.** The cadence rule adopted this afternoon survived contact with its own thesis owner.

### D. One check ADDED to the ticket sequence

```
python3 AGENTS/TERRY/scripts/chain_fetch.py USO 2026-10-16 --type call --no-cache --legs 125,130
```
**PLUS: confirm `^OVX` prints ≤ 58.6245 at the moment the chain is priced (leg a2).** It held all session with a **2.12-point** cushion at the session high — **but it is a HARD VETO, not a formality. If OVX is above the line there is no fill regardless of what the chain says.**

**APPROVAL REQUIRED — Will must approve/reject before execution. $0 at risk; nothing armed.**

---

## 12. DEATH RECORD — 2026-08-13 ~11:45 ET (arm day 20 of 20)

**DEAD (terminal). Arm expired unfired; Will ruled let-expire in session.** No revival — fresh exposure at these levels is a NEW card on BRENT's re-based positioning band (post-8/14), per the 005/007 discipline.

| | 8/4 12:24 grade | 8/13 11:39 live chain | Verdict |
|---|---|---|---|
| USO spot | 115.96 | **126.11** (+8.8%) | the move arrived unapproved |
| Leg (b) net debit, mid | $0.83 = 16.6% | **$1.88 = 37.6%** | 🔴 FAIL |
| Leg (b) net debit, worst-case | $1.30 = 26.0% | **$2.90 = 58.0%** (125C ask 10.75 − 130C bid 7.85) | 🔴 FAIL |
| Intrinsic floor | $0 (OTM) | **$1.11 = 22.2% of width** | passability dead by arithmetic while USO > ~126.65... at worst-case; at mid the time value already kills it |
| Leg (a) daily state / (a2) live | MET / MET (13:57) | **MET / MET** (OVX 50.08 vs 58.6245) | 🟢 — death is priced-out, not vol-gated |

**Counterfactual, measured both ways (not asserted):** an 8/4 fill at worst-case $1.30 (limit $1.50) marks **$1.88 at mid (+45%/+25%)** and **$0.85 exitable at the touch (negative)** today. ⛔ **Modest at mid, negative at the touch — NOT a large miss.** TERRY's in-session "~$3+" intrinsic estimate was wrong and corrected on the record (an intrinsic floor settles passability, it does not price a spread; the short 130C carries 64 DTE of time value against the long).

**Why no fire on the last day:** filling required chasing the $1.50 limit to ~$1.90+ to catch a move already made — the root-rule-#6 break test's named chase ("the window is closing"). The gate performed correctly on every day it ran, including this one, where its job was to say no.

**Finding routed to BRENT (2026-08-13 packet):** the card was DECISION-READY 8/4→8/13 — 9 of 20 arm days — with a measured, passing gate and no [Approve]/[Reject]. A dated arm gating on a MOMENT property (#14) needs a **DECISION-BY mechanism** distinct from its expiry: either a decision-by date or a standing [Approve in principle] stage. The expiry date alone applies pressure only on day 20, when the moment property has long since moved.
