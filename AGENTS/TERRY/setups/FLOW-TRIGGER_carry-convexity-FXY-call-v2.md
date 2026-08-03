# FIRE CARD — FXY — Carry-Convexity ENTRY v2 / FXY calls (long-yen convexity)

**Setup ID:** TRY-FIRE-007 · **Date:** 2026-08-03 · **Trigger class:** PRINT/CONFIRM discriminator (weekly CFTC COT release)
**Thesis owner:** SAM (`AGENTS/SAM/thesis/THESIS.md` v1.6.11 — carry-convexity tail **MED-HIGH, provisional on the 8/7 print**; SAM position FLAT)
**Terry verdict:** 🟡 **CONDITIONAL** — structure is clean and the vehicle is now genuinely tradeable; the card is gated entirely on the **Fri 2026-08-07 3:30 PM ET** COT resolver.
**Confidence in trade structure:** Medium-High · **Status:** 🟢 **DECISION-READY, UNARMED, $0 at risk. DO NOT FIRE.**

> ## ⚠️ THIS IS A FRESH BUILD, NOT A RE-MARK — AND THAT IS A CORRECTION TO TWO INCOMING PACKETS
>
> PROME (8/2) asked me to *"re-mark **TRY-FIRE-005**"* and SAM (8/3) refers to *"the **shelved** card."* **Both mis-state its status.** `TRY-FIRE-005` is **🔴 DEAD, not shelved** — and by its **own** ZONE-1 kill rule, which reads verbatim:
>
> > *"card is dead per its own ZONE 1 kill rule. Nothing below is actionable. **A re-arm requires a fresh build … not a revival of this card.**"*
>
> `setups/INDEX.md:42` says the same: *"terminal per its own kill rule (needs a fresh build, not a revival)."* Re-marking it would have been **un-lapsing a dead card on stale marks** — the exact thing I refused on `TRY-BUILDER-DHI-PHM` (7/20).
> **Therefore: new card, new number.** Per the INDEX numbering rule (*"do not reuse a number even after a card dies"*), 005 stays archived and this is **TRY-FIRE-007** (006 = Kharg). **Nothing from the 005 card is inherited un-re-derived.** Routed back to PROME + SAM.

---

## 1. One-line setup

Express SAM's carry-convexity tail — a record-short JPY crowd (**−163,412 noncommercial net, 90.8% of the −180K peak**, CFTC Jul-28 data) now facing a **confirmed two-government yen bid with a standing forward pledge** — via defined-risk FXY calls spanning the **Sep 17-18 BOJ MPM**. This is a **capitulation/convexity** payoff, not a directional call on today's tape.

## 2. Preconditions

- **THESIS:** SAM MED-HIGH holds through the resolver. SAM's entry recommendation today is **WAIT-FOR-8/7** and this card does not override it.
- **RESOLVER (the arm condition):** Fri **2026-08-07 3:30 PM ET**, Aug-4-data CFTC COT print. Pre-registered map (SAM §5, Will-approved):

| Print (JPY noncommercial net) | Read | Card action |
|---|---|---|
| **≤ −153K** (crowd held through two official ops) | **CONFIRM** | → Will **[Approve]** gate opens → ZONE 2 live re-pull → ticket |
| **−140K … −153K** | **NOT-CONFIRMED** | → no entry; gate stays LIVE to the next weekly print |
| **≥ −140K** (covered out) | **DENY** | → card **DIES** (terminal, like 005 — fresh build required, no revival) |

  No fourth state. Print delayed/unavailable ⇒ **NOT-CONFIRMED**, never CONFIRM-by-default.
- **What must NOT be happening:** a hard guard relaxed to make an early entry fit · FXY gapping green on the day of the fill without the root-rule-#6 break measurement written here first · any fill without a live chain re-pull (rule #4).

## 3. 🔴 THE TENOR FINDING — SAM'S REQUESTED TENOR DOES NOT EXIST

SAM §6.1 asks me to *"roll the tenor past Sep-18 … (Sep-26+ or Oct)."* **FXY lists only six expiries** (live pull, 2026-08-03 10:13 ET):

```
2026-08-21 · 2026-09-18 · 2026-12-18 · 2027-01-15 · 2027-03-19 · 2028-01-21
```

**There is no Sep-26 and no October.** The real menu is binary: **Sep-18 or Dec-18.**

| Tenor | Captures MPM? | Follow-through room | 60C mark | 60C spread | 60C OI |
|---|---|---|---|---|---|
| Aug-21 | ❌ **No** — expires 4 weeks early | — | 0.22 | **66.7%** | 301 |
| **Sep-18** | ✅ **Yes — but by one session** | **~0 days** | **0.47** | **10.5%** | **33,541** |
| Dec-18 | ✅ Yes, with 3 months | ~13 weeks | 0.90 | **44.4%** | 2,667 |

**⚠️ MUST-CONFIRM WITH SAM BEFORE ANY FILL (domain calendar, not mine):** the BOJ announces during Japan hours, so a Sep-18 MPM decision should be known **before the 9/18 US open**, letting a Sep-18-expiry US option price it and expire that same session. **If that timing is wrong by one day, this expiry captures nothing and the card is void.** I am not asserting it — SAM owns the calendar and must confirm it in writing. *(SAM's own §2 says the decision "lands ON the inclusive Sep-18 boundary," which is consistent, but the card should not fire on my inference of his sentence.)*

**Ruling: Sep-18.** You buy the decision gap and get **one session** to monetize it — no follow-through room. Dec-18 buys 13 extra weeks but at **~1.9× the premium and a 44.4% quoted spread**, i.e. you pay the round-trip friction of a small position just to enter. **On a $500 budget, Dec-18's spread eats more than its extra time is worth.** *(This is the honest weakness of this card and it is stated here, not buried: if the yen capitulation is a multi-week cascade rather than a decision-day gap, Sep-18 captures only day one.)*

## 4. Structure

- **Instrument:** FXY listed calls (CurrencyShares Japanese Yen ETF). Long yen = USD/JPY down = FXY **up**.
- **Expiry:** **2026-09-18** (46 DTE from build).
- **Leg: `FXY Sep-18-2026 $60 CALL`** — single leg, no ladder.

**Live chain, 2026-08-03 10:13 ET · FXY spot 58.60** *(rule #4: illustrative, re-pull at fire)*

| Strike | Mny | Bid | Ask | Mark | Spread% | IV% | Vol | OI |
|---|---|---|---|---|---|---|---|---|
| 57C | −2.7% | 1.85 | 2.10 | 1.98 | 12.7% | 13.53 | 292 | 1,791 |
| 58C | −1.0% | 1.25 | 1.45 | 1.35 | 14.8% | 13.43 | 195 | 4,604 |
| 59C | +0.7% | 0.70 | 1.00 | 0.85 | **35.3%** | 14.09 | **9** | 567 |
| **60C** | **+2.4%** | **0.45** | **0.50** | **0.47** | **10.5%** | **12.40** | **827** | **33,541** |

### ★ Why the 60C — and why the old card's structure is dead on liquidity

The 005 card's structure was **58C ×6 + 59C ×20**, with the 59C as the 20-lot workhorse chosen for *"the single best liquidity print in the entire chain."* **On Sep-18 that leg is now the worst line on the board: 35.3% wide, volume of 9.** You cannot build a 20-lot on it. **Do not carry that ladder forward.**

**And the 60C's own July disqualification has inverted.** The 005 card explicitly rejected it: *"8/21 60C printed bid $0.00 / ask $0.50 (200% spread) — a one-sided/no-real-market quote, not a genuine cheap-convexity source."* **On Sep-18 the 60C is the single most liquid line in the chain: OI 33,541 — 7.3× the next-best strike — on a 10.5% spread, the tightest in the table.** The strike that was untradeable in July is now the only genuinely liquid convex line FXY offers. That is a real change in the vehicle, not a preference.

### Rejected alternatives

- **58C ×3 ($435):** 58 is *ITM* at spot 58.60. Buys delta, not convexity — wrong payoff for a capitulation thesis, and 14.8% wide.
- **58C/60C debit spread (~$0.88, 5× = $440, ~2.3:1):** caps the payoff at 60 — **it truncates precisely the fat tail the thesis is paid by.** Same objection the 005 card raised against verticals, and it still holds.
- **Dec-18 anything:** 29–44% spreads (§3).
- **FXY shares / USDJPY FX options:** shares carry no convexity; FX options remain off per SAM's RED-#4 gate.

## 5. Risk

- **Max loss budget: $450** — `risk_calc.py --premium 0.50 --max-loss 500` → 10 contracts at $50/ct = $500 at the cap. **I am proposing 9, not 10**, leaving **$50** for ask drift between this build and a Friday fire. **Hard cap $500/card (Will standing rule) — unchanged.**
- **Max loss = 100% of premium.** Defined risk, no stop needed, no assignment risk, no margin.
- **Invalidation:**
  - **Thesis:** 8/7 print ≥ −140K ⇒ **DENY ⇒ card dies terminal.** No revival.
  - **Price:** FXY ≥ 60.50 never printed by 9/18 ⇒ expires $0. **Breakeven FXY 60.50 = +3.24%**, ≈ **USD/JPY ≤ ~152** (from 156.80 at 09:30 today).
  - **Time:** 2026-09-18 close. **No roll is pre-registered.** Any roll = fresh Will approval from scratch (Non-Negotiable #6, no roll-by-hope).
- **Gap/event risk — the known failure mode:** MOF/Treasury intervene *again* mid-window and **cap** the very move we own. A pledged, pre-announced backstop cuts both ways: it pressures the shorts *and* it advertises a ceiling.

## 6. Target / management

- **T1 — ★ MANDATORY PROFIT HARVEST (`NO_HARVEST_RULE`, Will-ruled fleet-wide 7/31):** mark **≥2×** (**$1.00 bid**) ⇒ **sell at least half, immediately.** Not conditional on the BOJ, not conditional on a further move.
- **T2:** FXY 62 (+5.8%, ≈USD/JPY 148) ⇒ 60C ≈ $2.00 ⇒ 9 ct ≈ **$1,800 vs $450 ≈ 4×**. FXY 64 ⇒ ≈ **8×**.
- **Time stop:** any position still open at the **9/18 open** must be worked out **that session** — it is the expiry.

> ### ✅ `NO_HARVEST_RULE` MANDATORY BUILD-TIME FIELD — **first card built under the 7/31 ruling**
> **Q: Is there a path where this position is profitable and NO trigger fires?**
> **A: YES — and it is the modal winning path.** FXY grinds to 60.5–61.5 on intervention follow-through *without* a BOJ hike; every event trigger stays unfired while the position sits at +50–150%, then decays into a 9/18 expiry that resolves nothing. **That is the VIXCS death exactly** (−$111.60: in profit at the 7/29 settle, every trigger keyed to the move going *further*, exited on the calendar).
> **Harvest rule added:** T1 above, keyed to **P/L**, not to the BOJ. **Trigger-variable check:** the trigger is the position's own mark — a variable the profit zone reaches **by definition**. ✅ Valid.

## 7. Why not / counter-trade

**The strongest case against, stated at full strength:**

1. **⚠️ We would be buying the side that just got paid.** Live skew check, Sep-18, equidistant from spot: **60C (+2.4% OTM) IV 12.40** vs **57P (−2.7% OTM) IV 9.82** ⇒ **calls bid ~2.6 vols over puts.** SAM's degraded pre-open proxy flagged this sign flip and could not size it; **it is real, and it is modest — not his non-physical −77.** ⚠️ *Caveat, against my own finding: the Sep-18 put quotes are near-garbage (spreads 60–200%, OI 0–503), so treat this as a directional read, not a measured number.*
2. **🔴 The term structure does NOT clearly confirm SAM's "near-tenor compressed" verdict, and I will not claim it does.** Aug-21 → Sep-18 ATM IV by strike: **58: 12.31 → 13.43 (+1.12)** · **57: 13.97 → 13.53 (−0.44)** · 59: 11.72 → 14.09 (+2.37, but Sep vol=9). **Mixed, roughly flat, ~1 vol upward at the money.** SAM's *structural* argument stands on its own logic; **the vol surface has not yet priced it.** *(Read the other way, this is mildly bullish for entry: Sep-18 carries a named BOJ meeting with ~77% unpriced hike mass for ~1 vol over a month that contains no such event — which is cheap, not rich. I am flagging both directions and asserting neither.)*
3. **No informational edge in the catalyst.** SAM's §5.1, adopted here in full: the intervention was announced to us and to the entire options market in the same public statement.
4. **One session of follow-through** (§3).
5. **Effective-N:** this is a **genuinely new axis** for the book — the live book is duration-short + energy + banks. **N_eff += 1, no shared falsifier with any existing leg.** Sizing at $450 is ~1.1% of the ~$39.5k book.

## 8. Root rule #6 (day colour) at fire

Long FXY is the **call** side ⇒ the clean day is a **RED FXY day**. FXY is **green today (+1.6% vs SAM's 57.66 Friday reference)**, which is exactly the configuration the break test governs.
**⛔ As of this build I do NOT hold a measurement that refutes the proxy** — §7.1 (calls bid over puts) points the *wrong* way, and §7.2 is ambiguous. **Per the Will-ratified 7/27 test, that means: no break, no early fire.** If Friday's print CONFIRMS and FXY is green that day, either wait for a red print or write the refuting number on this card **before** the ticket. *"The window is closing" is a chase, not a break.*

## 9. Decision

**⛔ NOT ACTIONABLE TODAY. NO APPROVAL IS BEING REQUESTED.**

This card is **decision-ready and parked** until **Fri 2026-08-07 3:30 PM ET**. On a CONFIRM print I will re-pull the chain live and bring a one-line ticket:

> **BUY 9 × FXY Sep-18-2026 $60 CALL @ $0.50 limit — $450 at risk, max loss $450.**

**Open items before any fire:** ① SAM confirms the BOJ Sep-18 announcement timing in writing (§3) · ② live chain re-pull (rule #4) · ③ root-rule-#6 day-colour check (§8) · ④ Will [Approve].

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---
*Built 2026-08-03 ~10:20 ET off SAM's 09:30 packet. All marks live-pulled this session and barred from use at fill. Supersedes nothing — `TRY-FIRE-005` remains DEAD and archived.*
