# FIRE CARD — FXY — Carry-Convexity ENTRY v2 / FXY calls (long-yen convexity)

**Setup ID:** TRY-FIRE-007 · **Date:** 2026-08-03 · **Trigger class:** PRINT/CONFIRM discriminator (weekly CFTC COT release)
**Thesis owner:** SAM (`AGENTS/SAM/thesis/THESIS.md` v1.6.11 — carry-convexity tail **MED-HIGH, provisional on the 8/7 print**; SAM position FLAT)
**Terry verdict:** 🔴 **DEAD (terminal)** — the 2026-08-07 15:30 ET COT print resolved the card's own §2 map to **DENY**. ~~🟡 CONDITIONAL — structure is clean and the vehicle is now genuinely tradeable; the card is gated entirely on the Fri 2026-08-07 3:30 PM ET COT resolver.~~ *(verdict moved 2026-08-07 16:3x ET — see §11)*
**Confidence in trade structure:** Medium-High *(construction axis, unchanged — the card died on its THESIS gate, not on its structure)* · **Status:** 🔴 **DEAD — never armed, never fired, `$0` at risk from build to death. ⛔ NO Monday re-mark. Do not arm. A re-arm requires a fresh build, not a revival (§11).**

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
5. **Effective-N:** ~~this is a **genuinely new axis** for the book — the live book is duration-short + energy + banks. **N_eff += 1, no shared falsifier with any existing leg.**~~ **🔴 THIS CLAIM IS WRONG AND IS CORRECTED 2026-08-04 — see §10.B. NEXUS refuted it the same evening I wrote it: 007 and `TRY-FIRE-004` now share the POLICY-AUTHORITY root (the rates leg and the FX leg have distinct instruments and distinct falsifiers, but a single policy reversal moves both). ⇒ `N_eff += ~0.5, NOT +1`, and 004+007 are ~1.5 roots, not 2.** Sizing at $450 is ~1.1% of the ~$39.5k book — **but it was sized against a diversification claim that does not hold** (§10.B).

## 8. Root rule #6 (day colour) at fire

Long FXY is the **call** side ⇒ the clean day is a **RED FXY day**. FXY is **green today (+1.6% vs SAM's 57.66 Friday reference)**, which is exactly the configuration the break test governs.
**⛔ As of this build I do NOT hold a measurement that refutes the proxy** — §7.1 (calls bid over puts) points the *wrong* way, and §7.2 is ambiguous. **Per the Will-ratified 7/27 test, that means: no break, no early fire.** If Friday's print CONFIRMS and FXY is green that day, either wait for a red print or write the refuting number on this card **before** the ticket. *"The window is closing" is a chase, not a break.*

## 9. Decision

**⛔ NOT ACTIONABLE TODAY. NO APPROVAL IS BEING REQUESTED.**

This card is **decision-ready and parked** until **Fri 2026-08-07 3:30 PM ET**. On a CONFIRM print I will re-pull the chain live and bring a one-line ticket:

> ~~**BUY 9 × FXY Sep-18-2026 $60 CALL @ $0.50 limit — $450 at risk, max loss $450.**~~
> **🔴 SIZE SUPERSEDED 2026-08-04 (§10.C): the recommendation is now `5–6 × @ $0.50 = $250–300`, not 9 × / $450**, because §7.5's `N_eff += 1, no shared falsifier` was refuted by NEXUS (004 and 007 share the policy-authority root ⇒ `+~0.5`) and the modal winning path re-weighted toward *grind-too-slow*. **9 × returns only on an 8/7 print showing the short crowd HELD** (positioning intact ⇒ unwind fuel still loaded).

**Open items before any fire:** ~~① SAM confirms the BOJ Sep-18 announcement timing in writing (§3)~~ **✅ CLOSED 8/3, see §10.E** · ② live chain re-pull (rule #4) · ③ root-rule-#6 day-colour check (§8) · ④ Will [Approve] · **⑤ 🆕 size ruled per §10.C off the 8/7 COT print.**

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## 10. 🔴 RULING — 2026-08-04 ~11:10 ET · SAM's Flag 1 + Flag 2 CLOSED, NEXUS's root count adopted

*My own `STATUS.md` called Flag 1 "the single most important open construction question on the desk" and demanded a ruling before 8/7. Here it is. **Card stays UNARMED, $0 at risk; nothing below fires anything.***

### A. ⚠️ FIRST — SAM and NEXUS are ONE vote, not two, and I am saying so against my own convenience

Both packets say the same thing: the distribution has rotated from gaps toward **escorted, managed appreciation**, so a Sep-18 expiry is exposed to the scenario that became *more* likely. SAM derives it from a character read; NEXUS from a root-map merge, and NEXUS explicitly claims independence (*"corroborating from the root side, not re-reporting"*).

**They share an antecedent: the 7/30 two-sovereign op and Bessent's 8/2 forward commitment. One fact, two framings. Count it as ONE vote.**

**This is the same test I applied to SAM and PROME yesterday** when they both called 005 "shelved" — *"the two of us agreeing was not independent confirmation, it was one stale relay read twice"* (SAM's words, accepted). **Applying it only to evidence I dislike would make it a rhetorical device rather than a rule**, so it gets applied here, where the evidence points somewhere uncomfortable for a card I built.

**⇒ ONE vote — but a strong one**, because the inference is short: a publicly pre-announced, forward-committed two-sovereign put under the yen implies *managed* rather than *violent* appreciation directly. It does not need corroboration to be sound.

### B. 🔴 THE CORRECTION I OWE ON MY OWN CARD — §7.5's "N_eff += 1, no shared falsifier" is WRONG

**NEXUS (8/3 19:30):** the Fed's hawkish hold, the BOJ's hawkish hold and the US Treasury's yen purchase are **one coordinated policy stance expressed through three instruments — 1 vote, never 3.** Break-relevant roots go ~4-5 → ~4, with **R1 (policy-authority) and R6 (FX) now merged on the FX axis.**

**Consequence, stated plainly: `TRY-FIRE-004` (TLT Sep-30 77P) rides the policy-authority root and 007 rides the FX axis of that same root. They are ~1.5 roots, not 2. A single policy reversal moves both.** The merge is *partial* — distinct instruments, distinct falsifiers — so this is not "the same trade twice." But **"no shared falsifier with any existing leg" was false when I wrote it**, and I wrote it as the justification for the size. Corrected at the claim site in §7.5.

### C. ✅ FLAG 1 — RULED: **KEEP Sep-18. But the framing is imprecise, and the honest consequence is a RE-PRICE, not a note.**

**1. "A Sep-18 expiry monetises a GAP and nothing else" is not quite right, and the imprecision matters.** A long call monetises a **LEVEL by a DATE**, not a gap. Escorted appreciation pays this card perfectly well **if it is fast enough to clear BE 60.50 by Sep 18.** The exposure is not to *grind-vs-gap*; it is to **grind-too-slow**. That is a rate question, and it deserves to be priced as one rather than accepted as a binary.

**2. The grind path is ALREADY monetised — by the harvest rule, not by the expiry.** §6 T1 (`NO_HARVEST_RULE`, and this was the first card built under it) sells **at least half at 2× / $1.00 bid, keyed to the position's own mark and explicitly not conditional on the BOJ.** An escorted appreciation that lifts FXY through ~59.5–60 pays that harvest **on the way up, whether or not the BOJ ever delivers.** So the card does **not** read as "captures the September catalyst generally" — SAM's stated worry — because the exit that collects the escorted path is already written and is not event-keyed.

**3. What IS genuinely exposed, and it is unavoidable at this tenor:** a grind that arrives *late* — FXY 59–60.4 on Sep-18 — pays **zero**, having been right about direction for six weeks. The menu is binary (FXY lists 6 expiries; no Sep-26, no October) and **Dec-18's 44.4% quoted spread remains a real and sufficient disqualifier**: on a ~$450 ticket the friction exceeds the value of +13 weeks. **Keeping Sep-18 is therefore choosing a known, bounded, stated weakness over an unbounded execution cost.** That is the trade-off, owned, as SAM asked.

**4. 🔴 THE CONSEQUENCE SAM AND NEXUS ACTUALLY EARN — and it is not a note, it is a number.** If the distribution has rotated toward slower/managed appreciation, then **P(clearing 60.50 by Sep-18) has FALLEN.** The card's §-payoff line (FXY 62 ≈ 4×, FXY 64 ≈ 8×) is unchanged as *arithmetic* but its *probability weighting is now lower than at build*. **⇒ The expected value of this card is lower today than it was yesterday, and it was sized at $450 against a diversification claim (§7.5) that §10.B just refuted.**

> **⇒ SIZING PUT BACK TO WILL, and it is the ruling that matters:** at `N_eff += ~0.5` rather than `+1`, and with the modal winning path re-weighted toward "too slow," **I no longer defend $450 as the right size on this card. My recommendation on 8/7 will be $250–300 (5–6 contracts) unless the COT print materially changes the distribution** — i.e. a print showing the crowd **held** (positioning intact ⇒ the unwind fuel is still loaded ⇒ the violent branch is live), which is exactly the discriminator NEXUS names. **A print showing the crowd covered into the op argues the Break-aligned leg is partly spent and cuts the other way.**

**This is a re-price, not a veto. 007 remains a coherent card and the thesis got *better* while the convexity got *worse* — NEXUS's phrase, and it is the right one.**

### D. ✅ FLAG 2 — PRICED, not dismissed (SAM asked for one or the other in writing)

**Pin risk is REAL and it is ADVERSE, and the reason is arithmetic:** ~33.5K OI at a round strike on a monthly opex is a pin magnet, and **a pin at exactly $60 pays this card $0** — the 60C is worth nothing at 60.00. So the crowding does not merely dampen travel; **it clusters the distribution on the one price where we get nothing.**

**Mitigant, and it is already in the structure:** the **2× harvest at $1.00 exits before expiry day.** Pin risk is an *expiry-day* phenomenon; a plan that collects at 2× on the way up never reaches it. **⇒ If this card is ever relying on expiry-day intrinsic value, the management plan has already been broken** — which makes T1 load-bearing rather than decorative, and is one more reason not to let it be waived under pressure.

**Honest other side, SAM's own:** the crowding is *why the market exists* — the 60C went from "bid $0.00 / ask $0.50, 200% spread, no real market" in July to a 10.5% spread on OI 33,541. **We are buying liquidity that only exists because the strike is crowded.** Both effects are real; they do not cancel, they apply at different times — the liquidity helps at entry and at the harvest, the pin hurts only at expiry.

### E. Blocker — CLOSED ✅

SAM's §1 figures accepted: BOJ MPM Sep 17–18, decision day 2, statement **10.5h** (typical, matching the graded 7/31 precedent of 12:11 JST) to **7.5h** (deliberately pessimistic late case) before the 09:30 ET open; Ueda presser **7.0h**. JST = ET+13 with no DST trap in September. **The expiry captures the event. 007 is NOT void on timing.** Recorded: on the 7/31 evidence **the presser, not the statement, does the repricing** (Oct OIS ~26–40% → ~64%, September named) — and it too is pre-open.

### G. ✅ SAM CONCURS — 2026-08-04 11:30 ET — and supplied the MEASUREMENT, which upgrades §10.C from inference to evidence

I asked SAM to say before Friday 15:30 if he read the escorted path as **fast** rather than slow. **He read it as slow, and he measured it rather than asserting it.**

| Session | USD/JPY intraday range | Close |
|---|---|---|
| Thu 7/30 (op) | **5.82y** | 159.704 |
| Fri 7/31 (op) | **3.73y** | 157.400 |
| Mon 8/3 | **2.67y** | 157.359 |
| Tue 8/4 (~10:33 ET) | — | **157.49** |

**Two things decayed together: velocity (5.82 → 3.73 → 2.67, monotone) and level progression (flat across three sessions after a 6-yen move).** A violent-continuation path looks like neither. **Bessent 8/4 confirms the intent:** the purchases *"could only curb volatility in the short term and would need to be followed by Japanese policies addressing the forces driving the yen lower"* — **the stated objective is countering DISORDERLY movement, i.e. officials are explicitly not trying to produce the move this card needs.**

**⇒ §10.C's "P(clearing 60.50 by Sep-18) has fallen" is no longer my inference — it is measured. The $250–300 size is confirmed, and SAM has put his name to it.**

**⚠️ SAM disclosed two things against his own interest, and both are recorded because they bear on how much weight his input carries:**
1. **His own open prediction SAM-39 (≥1 session with a ≥2.5y range by 9/18, 55%) is under strain from his own concurrence.** His resolution: the two are compatible only if the ≥2.5y sessions are **the official ops themselves, not the trend** (0/60 pre-episode sessions cleared 2.5y). **⇒ SAM-39 is a bet on another official ACTION, not on tape violence — and isolated one-day range spikes around ops do not carry FXY through 60.50. His own prediction, read precisely, does not support the larger size.**
2. **SAM-39's base rate was computed on truncated intraday-range data** (his `usdjpy.py` defect, fixed 8/2–8/3 but not propagated). Repaired: prior-year **3/259 ≈1.16%/session ⇒ naive P ≈32%**, not the registered ~23%. Mark stays 55%; **claimed edge falls ~+32pp → ~+23pp.**

### ★ PRE-REGISTERED FLIP CONDITIONS — SAM, locked 8/4 before the print, so Friday is mechanical

**Size returns to arguable-at-9× on ANY one of:**
1. **8/7 print shows the crowd HELD ≤−153K** — fuel intact ⇒ violent branch live *(my condition and his; the one that matters most)*
2. **A fresh session ≥2.5y range that is NOT an announced op** — velocity without official action = unwind, not escort
3. **A yen-haven re-couple (SAM-31)** — VIX spike with a yen bid. Still unfired; 7/30 is the cleanest counter-evidence available *(VIX **fell 17.3%** on the largest yen move since Dec-2023)*
4. **Sep/Oct BOJ OIS repricing materially higher** on the US rate-pressure channel. ⚠️ **SAM could not source current OIS today and flagged it un-verified rather than re-marking it** — an open input, and he asked whether TERRY or NEXUS can price it.

**Absent one of those: $250–300. SAM scored the 8/7 print as SAM-40 @45%, registered before the outcome and deliberately below even odds against his own long-biased frame** (SAM-22 @65% FAILED is his direct precedent for intervention forcing mass cover).

**⚠️ One branch of Flag 2 survives, and SAM is right to keep it alive:** he withdrew the pin concern as stated on the strength of the T1-exits-before-expiry mitigant — **but only in the branch where T1 triggers. If T1 never fires, the card walks into precisely the expiry it is most exposed to.** And on his slow-path evidence, **T1 is now the PRIMARY payoff path, not a nice-to-have** — expiry-day intrinsic is secondary.

### F. Status after this ruling

**UNCHANGED where it counts: DECISION-READY / UNARMED / $0 at risk / WAIT-FOR-8/7.** No guard relaxed, no gate moved, no entry pulled forward. Changed: §7.5 corrected, the tenor trade-off owned in figures, pin risk priced, and **the size recommendation cut from $450 to $250–300 pending the 8/7 print.**

---

## 11. 🔴 RESOLVER VERDICT — 2026-08-07, after the 15:30 ET CFTC print. **THE CARD IS DEAD. §8 of SAM's skeleton is FILLED.**

*Written 2026-08-07 ~16:3x ET (`boot.py` wall clock 16:24:55, Friday), **after** the US close. Every level below carries its as-of date; nothing here is a live price.*

### A. The print — the number, and the branch it fires on THIS card's map

| Field | Value | Source |
|---|---|---|
| JPY noncommercial net, **Aug-4 data** | **−45,473** | SAM `cftc_jpy.py` + independent hand-parse of raw `cftc.gov/dea/newcot/deafut.txt`, both 2026-08-07 ~15:4x ET |
| % of the −180K peak | **25.3%** (was 90.8% on Jul-28 data) | ditto |
| WoW change | **+117,939** — longs **+45,957**, shorts **−71,982** | ditto |
| Open interest | 419,393 (from 432,366, **−12,973**) | ditto |

**Against §2's pre-registered map, which I do not re-tune at scoring time:**

| Branch | Line | This print | Fired? |
|---|---|---|---|
| CONFIRM | ≤ −153K | −45,473 | ❌ missed by **107,527 contracts** |
| NOT-CONFIRMED | −140K … −153K | −45,473 | ❌ |
| **DENY (terminal)** | **≥ −140K** | **−45,473 — through the line by 94,527** | ✅ **FIRED** |

> **⇒ `TRY-FIRE-007` IS DEAD, TERMINAL, BY ITS OWN PRE-REGISTERED KILL RULE.** §2: *"card **DIES** (terminal, like 005 — fresh build required, no revival)."* §5 invalidation: *"8/7 print ≥ −140K ⇒ **DENY ⇒ card dies terminal.** No revival."*
> **⛔ There is no Monday re-mark. The §2-of-SAM's-packet chain — resolver → TERRY Monday re-mark → Will [Approve] — was conditional on a CONFIRM. It does not run.**

**Two names, one branch — stated so nobody reconciles them later.** SAM's resolver calls this branch **DE-LOAD**; this card calls it **DENY**. Same number, same fire, different consequence by design: DE-LOAD is a *thesis-grade* disposition (revert MEDIUM), DENY is a *card-lifecycle* disposition (terminal). **The card's map governs the card.** They are not in conflict and neither was re-tuned.

### B. What SAM graded — cited, not re-adjudicated

**Thesis truth is SAM's, not mine** (HARD BOUNDARY 3). Recorded here by citation, from `inbox/2026-08-07_from-SAM_RESOLVER-COMPLETE-DE-LOAD-leg1-fired-STAND-DOWN-007.md`:

- A **second registered rule** fired, and it is stricter than the resolver map: **THESIS leg-1 SPF** — *"CFTC covers below −108K / 60% line → frame → LOW."* −45,473 / 25.3% is through it by **62,527 contracts / 34.7pp**. **⇒ the convexity-tail frame is LOW — a thesis-BREAK condition met, not a downgrade of degree.**
- **SAM-40 ❌ FAILED** (the ~25% branch fired; his 45% CONFIRM modal missed). **SAM-29 ❌ RESOLVED FALSE.**
- Mechanism: **position REVERSAL, not liquidation** — OI barely moved (−12,973) while net swung +117,939; shorts covered 71,982 **and** longs added 45,957. **Prior record WoW cover was +31,314 (Jul-7); this is 3.8×.**
- ⛔ **SAM's instruction, adopted verbatim: "007 STANDS DOWN. No Monday re-mark. Do not arm."**

**What this does to the card's own reasoning:** the §10.C ruling said the frame was migrating to *positioning-dominant*. The positioning leg is what evaporated. **A positioning-dominant frame with no positioning is not a thin frame; it is not a frame** (SAM's line, and it is the correct construction read too — there is nothing left for the 60C to be long OF).

### C. ★ THE FLIP CONDITIONS, GRADED — all four, because they were pre-registered

Locked by SAM on 8/4 **before** the print (§10 ★ block), so this is transcription:

| # | Condition | Grade |
|---|---|---|
| **1** | 8/7 print shows crowd **HELD ≤−153K** | ❌ **FALSE, decisively.** −45,473 = 25.3%, not ≥85%. The one that mattered most |
| **2** | fresh session ≥2.5y range that is **not** an announced op | ❌ **UNFIRED** — SAM: 3 sessions in, 0 qualifying (0.75 / 0.58 / 1.01y vs a 2.5y bar) |
| **3** | yen-haven re-couple (SAM-31) | ❌ **UNFIRED.** 8/7 is fresh counter-evidence: **VIX 14.97 (−1.2%) with equities rallying** on a −23K payroll — bad-news-is-good-news, not risk-off |
| **4** | Sep/Oct BOJ OIS repricing materially higher | ⚠️ **AGAINST, not merely unfired.** Sep 17-18 cumulative **39.7% → 45.6%** (as-of 8/6) = **fourth consecutive adverse move.** The route is hawkish-***of-priced***; rising priced probability **destroys** the surprise room it pays on |

**0 of 4. The size question ("does it return to 9×?") is moot — but it is worth recording that it was answered NO on every independent leg, not just by the one that killed the card.**

### D. 🔴 THE COUNTERFACTUAL, IN FIGURES — what an early fire would have cost. **This is my axis, so I measured it rather than accept the assertion.**

SAM's packet says *"had it been acted on, we would be long into this print."* True, and here is the number:

| | At build, 2026-08-03 10:13 ET | **At the 2026-08-07 close (16:26 fetch, freshest trade 15:57)** |
|---|---|---|
| FXY spot | 58.60 | **58.24** (−0.6%) |
| Sep-18 **60C** | bid 0.45 / ask **0.50** / mark 0.47 | **bid 0.20 / ask 0.30 / mid 0.25** |
| Quoted spread | **10.5%** | **40% of mid** |

**A fire at the $0.50 limit would mark ≈ −50% at mid and ≈ −60% at the exitable bid, four sessions in, with the thesis now graded LOW.** At the recommended 5–6× that is ≈ **−$150 to −$180**; at the ~~9× / $450~~ size I originally defended, ≈ **−$270**. **`$0` was at risk instead.**

**⇒ TWO GUARDS DID REAL WORK AND BOTH SHOULD BE NAMED:**
1. **§8, root rule #6's break test** — *"⛔ As of this build I do NOT hold a measurement that refutes the proxy … no break, no early fire. 'The window is closing' is a chase, not a break."* SAM credits this (he cites it as my "§5"; the text is **§8**) as the reason the §5C override that fired **on the letter** on 8/3 was not acted on. **This is the first time the ratified 7/27 break test has demonstrably prevented a loss rather than merely governed one.**
2. **Will's pre-print Monday-gating ruling** (SAM packet §2, recorded 8/7 AM **before the number existed**) plus SAM's WAIT-FOR-8/7. Three independent brakes, all pre-registered, none of them a judgement made after the number landed.

### E. ⚠️ ONE CONSTRUCTION FINDING AGAINST MYSELF — the vehicle argument rested on a MOMENT property

The whole §4 case for the 60C over 005's 58C/59C ladder was liquidity: *"the 60C … is now OI 33,541 (7.3× next strike) at a **10.5% spread** — the vehicle changed underneath the card."* **That spread is 40% today, on a strip `chain_fetch` grades 35% NONMONO = broadly unreliable.**

**`RISK_RULES` #14 lists "two-sided quotes / OI" as a STRUCTURE property (gradable any time) and "spread%" as a MOMENT property (grade once, at fire). I used a moment property — the 10.5% quote — as a structural argument for vehicle SELECTION, four days ahead of any possible fill.** OI (33,541) is genuinely structural and did the honest half of the work; the spread number did not, and I did not separate them.

**Honest other side, stated because it cuts against my own finding:** a strike's liquidity is partly *contingent on the thesis being live* — spreads widen when nobody wants the strike any more, so some of the 10.5% → 40% move is the thesis dying, not a measurement error at build. **Both are true. The rule that survives: when a vehicle is chosen on liquidity, split the claim into the OI half (structural, quotable ahead) and the spread half (moment, re-pull at fire) — and never let the moment half carry the selection argument.** → `RISK_RULES` #14 corollary.

### F. Status, and what is owed

- **CARD: 🔴 DEAD (terminal).** Never armed, never fired. **`$0` at risk from build (8/3) to death (8/7) — the entire life of the card.** Book stays **FLAT** on this axis.
- **No capital moved. No threshold moved. No guard relaxed.** The only thing this session changed is that a resolved gate is now recorded as resolved on every surface that advertised it.
- **A re-arm requires a fresh build and a NEW number** (INDEX rule: never reuse an id). 005 → 007 → the next one is not 007 again.
- ✅ **DELIVERED BY SAM 2026-08-27 — CLOSED after 20 days.** ~~Owed by SAM, still open and NOT closed by this print~~: §6's named branch + exit rule for *"yen strengthens but BOJ does nothing"* — the hole two independent passes found. **Still moot for THIS card (DEAD/terminal since 8/7); live for the next card built on this thesis, which is why it is recorded here rather than archived with the packet.** Full packet: `inbox/processed/2026-08-27_from-SAM_the-owed-branch-yen-strengthens-BOJ-does-nothing-plus-exit-rule.md`.
  - **⚠️ IT IS NO LONGER AN EDGE CASE.** BOJ Sep pricing re-based **~73.5% → ~87.5%** (Polymarket Sep binary, +14pp/10 sessions; wire/OIS ~80–85%; ⛔ `boj_ois.py`'s 55.9% is under a standing do-not-cite). **At ~87.5% priced, a HOLD is yen-NEGATIVE** (CH-004: a fully-priced hike delivered with zero unwind). ⇒ *"BOJ does nothing"* is now a **hawkish disappointment**, so a yen that strengthens anyway is strengthening **against a headwind** — the branch's diagnostic value went UP. ⚠️ **SAM did not sell only the flattering half: the same repricing leaves route 1 (hawkish-of-priced) ~12.5% of surprise room and near-dead, and the bigger yen move now comes from the surprise HOLD — and that move is DOWN.**
  - **THE THREE DRIVERS — name one IN FIGURES, IN-SESSION, before any add:** **(A) DOLLAR-SIDE** — yen **mid-pack** among majors (8/7: CHF +0.62 > JPY +0.59; 8/10 yen the *weakest* major) ⇒ **not our thesis, reduce into it, do not press.** · **(B) HAVEN** — yen the **BEST** major **AND VIX up** ⇒ **the mechanism the card underwrites; hold/add.** ⚠️ **0-for-4 since Jun-11** (8/7, 8/10, 8/19, 8/21 — 8/19 had KOSPI −5.80% limit-down + Nikkei −3.16% and **VIX still FELL**). · **(C) OFFICIAL** — intraday range **≥2.5 yen** + the BOJ settlement-projection tell (7/30: ~¥8.45T est., 163.49→157.92) ⇒ **fade, do not chase.** *(That 7/30 move is now fully given back — 159.38 vs 157.40 on 7/31.)*
  - **⛔ DEFAULT WHEN YOU CANNOT TELL: TREAT AS (A).** Base rates say so — **B has not fired once in four tests**, and A/C produced every yen-strength episode this cycle.
  - 🔑 **AND IT DISAMBIGUATES ROOT RULE #7** (*"Roll duration, don't trim size. Trimming = thesis broken. Rolling = timeline uncertain."*), which is genuinely ambiguous in this exact case: **B ⇒ mechanism operating, timing wrong ⇒ ROLL. A or C ⇒ the yen moved for a reason the card never underwrote ⇒ thesis-broken ON THIS AXIS ⇒ TRIM.** ★ **The trap it closes: under A or C a PROFITABLE move reads as vindication and invites adding — when it is the opposite. Profit from an un-underwritten driver is evidence AGAINST the card, not for it.** → promoted as **`RISK_RULES` #23**; the empirical legs deliberately were NOT promoted (see there).
  - ⚠️ **SAM'S OWN LIMITS, CARRIED NOT STRIPPED** (`[[finding_rederived_signal_loses_the_senders_caveats]]`): spec for the NEXT card, **not a live signal** — SAM's book is FLAT, frame LOW/retired, v2.0 candidate **killed 8/27** after RED's blind pass · the A/B/C partition is a **taxonomy with base-rate support, not a fitted model** · **the 3–5 session decay clock is n=1–2 — "two observations wearing a range", NOT calibrated** · the 87.5% is a **thin traded binary ($60.7K liquidity)** — read as a band.
  - **Open offer from SAM, not taken this session:** he can surface the yen-rank-among-majors discriminator as a named line in his boot sweep (it is already computed there) rather than leaving it a card section.

---
*Built 2026-08-03 ~10:20 ET off SAM's 09:30 packet. All marks live-pulled this session and barred from use at fill. Supersedes nothing — `TRY-FIRE-005` remains DEAD and archived. §10 ruling added 2026-08-04 on SAM's two flags + NEXUS's root count. **§11 resolver verdict added 2026-08-07 after the 15:30 print — card DEAD, terminal.***
