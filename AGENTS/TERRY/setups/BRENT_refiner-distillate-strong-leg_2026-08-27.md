# TRADE CARD — REFINER EQUITY (VLO / MPC / PSX / DINO) — LONG, expressing the distillate-crack STRONG leg

**Setup ID:** `TRY-BRENT-REFINER`
**Date:** 2026-08-27 ~12:0x ET (`date` wall clock, copied not inferred) · **market OPEN**
**Thesis owner:** **BRENT** (distillate/crack domain). ⚠️ **TERRY owns construction ONLY** — I do not re-underwrite the crack thesis.
**Tasking:** Will, relayed via BRENT 11:2x ET — verbatim ***"loop TERRY in on a VLO/MPC construction."***
**Terry verdict:** 🟢 **STAGED — Will APPROVED 2026-08-27 ~12:1x ET, in-session, verbatim *"approved"*; route (i), `3 × VLO`. NOT YET FILLED. TERRY does not execute.** *(State token is `STAGED`, not "APPROVED": approval is the DECISION, `STAGED` is the card STATE — approved, gate clean, awaiting only the fill. `APPROVED` is on `ledger_sweep`'s deliberately-excluded list because it doubles as ordinary prose; check F caught this within a minute of the write and the fix was the SURFACE, never the vocabulary.)*
> ✅ **Rule #6 RE-MEASURED AT APPROVAL (12:12 ET), as this card required:** **VLO `345.29` −0.79%** · XLE −0.80% · **USO +0.86%.** **Refiners still RED, crude still GREEN ⇒ the entry gate is CLEAN on the direct measurement at the moment of approval.** ⚠️ **Still intraday — if the fill slips to another day, re-measure again; it is not a standing pass.**
> ⚠️ **Will did NOT name the oil-exposure ceiling.** Approving route (i) settles it *for this `$1,033` add* (the sleeve math holds it inside the 80% undefended-linear ceiling regardless). ⛔ **It remains UNSET for any future add and the alternative route (ii) — trim-USO-first — is NOT approved and is NOT dead; it was simply not chosen here.**
> *Prior verdict (superseded 2026-08-27): 🟡 CONDITIONAL — SHARES, NOT OPTIONS. Small, and smaller than the ask implies.*
**Confidence in trade structure:** High · **Confidence in thesis:** Not mine to grade.

> ⛔ **`$0` MOVED · NO ORDER · NOTHING ARMED. APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## 1. One-line setup

Own the leg of BRENT's oil thesis the book expresses **nowhere** — refining margin / distillate crack — in the **smallest instrument that does not deepen the concentration flag**, and accept that the honest size is ~$1,000, not a position that will change the book.

## 2. THE HEADLINE: I AM RECOMMENDING A **SMALLER, DULLER** TRADE THAN WAS ASKED FOR, AND HERE IS WHY

**Four independent facts, each measured this session, each pointing the same way — away from options.**

### ⛔ (a) THE 60–90 DTE BAND IS **EMPTY** ON BOTH NAMES WILL NAMED. BRENT SAID IT WOULD NOT BE.

His packet §4: *"the 60-90 window in USO didn't have November listings; VLO/MPC have monthly cycles and the 60-90 window is well-populated. **Not the trap it was on USO.**"*

**Measured, live (`chain_fetch.py`, 12:0x):**

| name | listed expiries around the band | 60–90 DTE window (10/26 → 11/25) |
|---|---|---|
| **VLO** | …9/25, 10/2, **10/16**, **12/18**, 1/15… | ⛔ **NOTHING** |
| **MPC** | 9/18, **10/16**, **12/18**, 1/15… | ⛔ **NOTHING** |
| **PSX** | …**11/20** present | ✅ **11/20 = 85 DTE, IN BAND** |

⇒ **VLO and MPC skip November entirely** — they are quarterly beyond October. **`Oct-16` = 50 DTE (below band) · `Dec-18` = 113 DTE (above band).** **It is the same trap, on the two names the ask specified.** *(`[[finding_adoption_is_not_validation]]` — the claim was confident, consumed, and untested. I ran the pull instead of inheriting it.)*

### ⛔ (b) IV IS RICH, AND YOU WOULD BE BUYING IT **AFTER** THE MOVE

**Measured IV, this session:** VLO Oct-16 ≈ **44.9–45.9%** · VLO Dec-18 ≈ **46.6–47.5%** · MPC Dec-18 ≈ **45.5–47.5%** · PSX Nov-20 ≈ **40.1–42.9%**.

**These names have already run +14–17% in 30 days** (BRENT's table). **Long premium at ~47 IV into a completed move is paying up for convexity you are buying late.** ⚠️ **PSX is the cheapest vol on the board by ~5–7 vol points AND owns the only in-band expiry** — if this trade is ever done with options, that is a fact that should decide the name, and it is *not* one of the two names the ask specified.

### ⛔ (c) THE THESIS HAS **NO DATED CATALYST**, SO CONVEXITY BUYS NOTHING

Inventories at a **1996 low for the date**, utilization **97.4%**, crack at a record — these are **stock-and-flow conditions, not events.** There is no print, no meeting, no expiry to be convex *around*. **`RISK_RULES` 71 (match expiry to catalyst + confirmation lag) has no catalyst to match.** An option here pays theta for optionality against a calendar with nothing on it.

### ⛔ (d) THE `$500` CARD CAP MAKES EVEN **ONE** CONTRACT UNBUYABLE

Standing rule (Will 2026-06-26): **max loss `$500` per card.**
- VLO `Dec-18 350C` mark **32.35** ⇒ **`$3,235`/contract = 6.5× the cap.**
- VLO `Oct-16 360/380` call spread ⇒ net debit ≈ **`$680` = 1.36× the cap**, and it sits at 50 DTE, *below* the band.
- ⇒ **There is no options structure on VLO/MPC that fits the cap without going far OTM on a short tenor — a lottery ticket on a slow structural thesis.** ⛔ **Refused.**

> 🔑 **The four are independent and they agree. That is the finding, not my preference.** *(Execution drag confirms it: quoted spreads run **5–10%** across these strips — VLO Dec `360C` at **2.11%** is the single best quote on the board and the exception.)*

## 3. RULE #6 — ✅ **SATISFIED ON ITS OWN TERMS. NO BREAK TEST NEEDED.** *(and BRENT read the wrong tape)*

**Root rule #6: puts on green days, calls on red days.** BRENT wrote (11:20): *"Today is a **GREEN** day (BZV26 +1.4%)… **my read: WAIT FOR A RED DAY on the refiners specifically.**"*

**★ HIS INSTRUCTION IS RIGHT AND HIS PREMISE IS ALREADY FALSE — the refiners ARE red, right now.** Measured 12:04 ET:

| VLO | MPC | PSX | DINO | CRAK | XLE | **USO** |
|---|---|---|---|---|---|---|
| **−1.01%** | **−0.44%** | **−1.08%** | **−0.34%** | **−0.50%** | **−0.79%** | **+0.91%** |

⇒ **Crude is GREEN; every refiner and the refiner ETF are RED.** **The day-colour that binds is the instrument you transact, not its thesis cousin** — BRENT priced the day off `BZV26`. ✅ **A long refiner expression today is rule-#6-CLEAN on the direct measurement, and needs no break argument.** *(This is the day-colour split doing real work: the two legs genuinely decoupled today, which is the same evidence the trade rests on.)*

⚠️ **INTRADAY, NOT A CLOSE.** Re-measure the refiner's own day-colour **on the day of the fill, before the fill** — an intraday red can close green. **The 8/27 figures above are NOT a standing pass.**

## 4. STRUCTURE — **SHARES**

- **Instrument:** ✅ **COMMON SHARES.** No theta, no IV to overpay, no expiry to match to an absent catalyst, no tenor-band violation, and the thesis is structural and slow — shares express *exactly* the view with nothing bolted on.
- **Expiry / tenor:** **N/A — and that is a feature here**, not a dodge. The 60–90 band governs **new structural option deployments** (`RISK_RULES` #21); shares raise no tenor question, which is the cleanest way past a band the listings cannot satisfy. ⛔ **I did not "solve" the empty band by relaxing it.**
- **Rationale vs alternatives:** calls ⇒ (b)+(c)+(d) · call spread ⇒ (d), and still 50 or 113 DTE · **CRAK** ⇒ BRENT's own objection (dilutes with foreign refiners, Reliance) and it is *also* red today · **HO=F / UNL** ⇒ the cleanest leg-expression in theory, **retail-thin and a futures contract is not sized in `$1,000` units** — refused on tradeability, not on merit.

## 5. SIZING — **THE CONCENTRATION CEILING BINDS, NOT THE `$500` CAP**

**BRENT's constraint, arithmetic run:** oil sleeve gross **`$5,831`**, undefended-linear **76.4% = `$4,455`**, ceiling **~80%**. Shares add **fully** to undefended-linear:

> `(4,455 + X) / (5,831 + X) ≤ 0.80` ⇒ **X ≤ `$1,050`** *(check: 5,504/6,880 = 0.8000)*

| name | last | max shares | cost | % of ceiling | trim step |
|---|---:|---:|---:|---:|---:|
| **VLO** | 344.50 | **3** | **`$1,033`** | 98.5% | 33% |
| MPC | 360.67 | 2 | `$721` | 68.7% | 50% |
| PSX | 239.62 | 4 | `$958` | 91.3% | 25% |
| DINO | 96.19 | 10 | `$962` | 91.6% | **10%** |

⇒ **RECOMMENDED: `3 × VLO` ≈ `$1,033`** (or **`4 × PSX` ≈ `$958`** — see §6, and PSX has the better vol and the only in-band expiry if this ever becomes an option).

**On the `$500` cap:** a `$1,033` share position hits `$500` of loss only at **−48%**. **Any sane invalidation keeps this card inside the cap** — so the cap is not the binding constraint here, the concentration ceiling is. **Both are respected; neither was relaxed.**

⚠️ **`[POSITION_STATE_UNKNOWN]` — CASH.** `FORGE/STATUS.md` is a **2026-08-14** reconcile (13 days stale) and I will not size against a stale cash figure. **If Will's intended oil-exposure ceiling as a share of total book is tighter than the sleeve math above, that number is his and it overrides this table.** *(Boundary #6 — I got a holdings fact wrong from an agent packet earlier today and am not repeating it.)*

## 6. ⚠️ THE NAME CHOICE IS **UNDER-DETERMINED**, AND THE DATUM THAT SETTLES IT HAS BEEN OWED FOR 58 DAYS

**`STATUS.md:137`, open since 2026-07-30:** *"Open ask back to BRENT, now **more** load-bearing: **distillate-yield-by-name** (if it isn't VLO, #1 moves to whichever name it is)."* **Never delivered.**

★ **This is the exact question the ask puts to me — "VLO or MPC?" — and the exact number that answers it is the one outstanding.** ⛔ **I will not pick the name on a thesis basis I do not hold, and I will not assert a distillate-lever ranking from reputation** — that is a naked claim, and it is the class this desk has spent the week correcting.

**So the name is chosen on CONSTRUCTION grounds only, and they are weak tie-breakers:** VLO fits the ceiling most closely (98.5%) and carries the deepest options liquidity should it ever matter; **PSX has cheaper vol (−5 to −7 vol pts) and the only in-band expiry; DINO gives 10% trim granularity against VLO's 33%.**

⇒ **If BRENT delivers distillate-yield-by-name and it does not rank VLO first, THE NAME MOVES — and this card says so in advance so the switch is not a post-hoc rationalisation.** *(`[[finding_hypothesis_needs_an_instrument_for_its_defining_mechanism]]` — the thesis is *distillate*; the instrument should be selected on *distillate yield*, not on price convenience.)*

## 6-bis. ✅ **THE 58-DAY-OWED DATUM ARRIVED (BRENT, 12:3x) — VLO IS CONFIRMED. NAME HOLDS. TWO FLAGGED ALTERNATIVES RULED.**

**`distillate-yield-by-name`, Q1-2026 10-Q sourced:** **CVI 41.3% · DK 37.9% · VLO 37.7% · PARR 37.5% · DINO 37.0% · MPC 35.5% · PBF 34.0% · PSX ⛔ not sourceable** (discloses only an aggregate 87% "clean product yield" — no gasoline/distillate split).

✅ **Within the construction set, VLO ranks FIRST — the pre-committed name-move condition did NOT trigger.** §6 said the name moves *"if the yield data does not rank VLO first."* It does. **The commitment was made before the number arrived and is discharged honestly, not quietly.**

⚠️ **BRENT correctly refused to silently drop two names that rank ABOVE VLO. Ruled here, deliberately:**

| | yield edge vs VLO | shares @ ceiling | trim step | ruling |
|---|---:|---:|---:|---|
| **DK** | **+0.2pp** | 14 = `$985` | 7.1% | ⛔ **DISMISSED ON THE NUMBER ITSELF.** 0.2pp on a **five-month-old filing** is inside any honest measurement error. **It is not a ranking, it is a tie.** |
| **CVI** | **+3.6pp** | 26 = `$1,022` | **3.8%** | ⛔ **NOT ADOPTED — but on PROPORTION, not on merit.** The edge is real and the granularity is genuinely better (3.8% trim steps vs VLO's 33%). |

**Why CVI does not displace an already-approved VLO:**
- ⚠️ **BRENT's own vintage caveat binds: Q1-2026 yields, Q2 filings not checked this session, his words *"not high-confidence for a Nov+ decision."* Reopening an approved trade on a 3.6pp edge from a 5-month-old filing inverts the confidence the number can carry.**
- ⛔ **The switch would need work I have NOT done: whether CVI is a PURE refining expression** (business-mix contamination would defeat the point of picking on refining yield) **and its liquidity/asset-concentration profile as a small-cap single name.** ⛔ **I will not assert those from reputation — that is the exact failure this card corrected in BRENT twice today.**
- **Single-asset operational risk is a real cost at 3 shares:** a small-cap refiner's outage is a **total loss driver independent of the thesis**, and a `$1,033` position cannot diversify it. §7 already flags this axis.
- ⇒ **The yield edge does not clear the bar for churning an approved position of this size.** 🔑 **On a LARGER refiner expression — where the 3.6pp and the 3.8% trim granularity would actually pay for the verification work — CVI is the named candidate to check first.** **Recorded so it is a deferred decision, not a forgotten one.**

★ **PSX's black box is now a PRICED trade-off, not an assumption:** it has the cheapest vol, the only in-band expiry, and the 2nd-best ceiling fit — **and an unsourceable distillate split.** ⇒ **Any future OPTIONS version of this leg trades known-first-on-mix (VLO) for cheapest-vol-in-band with an UNKNOWN yield.** Named so it is chosen, never defaulted into.

## 6-ter. ✅ DEBIT-SPREAD RULING RECEIVED — **DEFINED, not undefended-linear**

BRENT ruled the §5 definitional question **in my favour and against his own morning claim**: *"undefended-linear"* means **max downside not bounded by construction** ⇒ long shares and short options qualify; **long calls, long puts and debit spreads do NOT.** ⛔ **He retracted *"a call adds to undefended-linear until it goes ITM"*** — ITM changes **delta**, never the **loss floor** — noting it contradicted his own `TRADE.md` concentration table, which already bucketed the `USO 135C ×2` as *defined*.
⇒ **Moot for this 3-share card. LIVE the instant anyone proposes a refiner spread** — it would count against the DEFINED bucket, and the `$1,050` shares ceiling would NOT bind it.

## 7. RISK

- **Max loss budget:** `$500` per card (standing). **Position notional `$1,033`; the cap binds at −48%, so it is not the operative limit.** ⚠️ **Shares have NO defined loss without a rule** — §8's invalidation is what makes this a defined trade rather than an open-ended long.
- **Invalidation (thesis, BRENT's — carried, not mine to set):** distillate crack rolls over hard; refiner runs destroyed by higher crude or demand destruction.
- **Invalidation (construction, MINE, and it is the one this card adds):** ⭐ **the DECOUPLING is the whole reason this is not a repackaged USO add — so the decoupling failing is what kills it.** Test: **refiner-vs-XLE 30d spread** (now **+8.9pp**: VLO +14.3% vs XLE +5.4%). **If that spread compresses toward zero while distillate holds a record, the "independent view" claim is dead and this becomes correlated oil beta wearing a different ticker.**
- 📌 **CO-BUILD UNDER WAY (BRENT + TERRY, agreed 8/27) — and the WINDOW ANCHOR is already contested.** BRENT's proposed regime window was *"Feb-2026 war start."* ⛔ **His own base rate says otherwise: `n=117` war sessions ending 8/21 ⇒ the window starts `2026-03-06`** (counted on the actual trading calendar, 4 holidays enumerated by the feed, span re-verified at 117). **A February start would give 140 sessions — `+23`, ~20% — and every extra day is a PRE-WAR day misclassified as WAR**, which would widen the war-regime distribution with quiet observations and **bias the threshold toward firing LATE.** ⚠️ **My derivation assumes his window ends 8/21 inclusive; the authoritative answer is the first date in HIS series, which he holds. Build is READY and deliberately NOT RUN until he confirms — a distribution on the wrong sample is worse than none, because it arrives looking finished.** Method agreed: full-window WITH sub-regime overlay; **the 8/17-only subset REJECTED by both of us** (n=8, conditions the test on the motivating evidence — the third time this desk has refused that exact shape today).
- ✅ **CO-BUILD COMPLETE 8/27 — DISTRIBUTION BUILT, BASIS AND CONTROL RULED, AND ⛔ STILL NO THRESHOLD. THE SLOT REMAINS OPEN, DELIBERATELY.**
  **Window `2026-02-27` → present, n=126** (BRENT's stated boundary, verified verbatim at his row-58 L158 — **my `3/06` back-derivation was WRONG and his stated date beat it**). **Artifact: `research/2026-08-27_refiner-XLE-decoupling-distribution.md`; script `scripts/decoupling_series.py`, reproducible.**
  ★ **THE FINDING WAS THE BASIS, NOT THE DISTRIBUTION: "30d" read as CALENDAR days puts VLO at the `71.4th` percentile (healthy); read as SESSIONS it is the `42.9th` (fading). A 28.5-percentile swing from a DEFINITION, not the tape** (`[[finding_normalization_choice_picks_opposite_winners]]`). ⚠️ **My own first build used sessions and would have placed BRENT's `+8.9pp` into a distribution it does not live in** (`[[finding_instrument_reports_clean_against_the_wrong_reference]]`) — caught by reconciling his table against my output rather than assuming they matched.
  **RULED BY BRENT (his half):** **BASIS = calendar-30d** (and he ruled it on the record that switching basis *after* seeing the distribution is a direction-neutrality trap) · **CONTROL = XLE** — so the falsifier tests *refiners-paid-by-ETF-beta*, **not crude beta**; a `USO`/`BZ` control is a **different instrument, deferred**.
  **VERDICT: `+8.55pp` sits at the `71.4th` percentile, INSIDE p25–p75 — the middle of the distribution. NEITHER of his pre-registered decision rules (`< p25` or `> p75`) trips ⇒ NO THRESHOLD NOMINATED.** ⚠️ **Context, not a challenge: it is only `+1.23pp` below p75 and `+5.48pp` above p25 — nearer the upper rule than the lower.**
  ⚠️ **ON THE WATCH LIST, EXPLICITLY NOT A NOMINATION:** today's `+8.55` is the **maximum of its own sub-regime**, whose mean (`+4.52`, 8/18→now) sits **below the war-window mean (`+6.76`)** ⇒ **a strong print inside a softer stretch.** ⛔ **n=8 cannot carry a verdict and neither desk drew one.**
  🔑 **WHAT THIS MEANS FOR THE POSITION, STATED PLAINLY: the entry is approved and the EXIT LEVEL IS STILL UNSET.** **That is the honest outcome of a base-rate that refused to manufacture a number, not an oversight** — and it is the same refusal made on B-1, on row-58's A2, and on the 8/17-only subset. **Re-evaluate at the next material move.**
- ⛔ **THE COMPRESSION THRESHOLD IS A NAMED SLOT, NOT A NUMBER — `RISK_RULES` #19.** I have **one observation** of that spread. **Naming "≤3pp" today off a single reading is precisely the error BRENT's own B-1 refutation exposed**, and I refused it on row 58 six days ago; refusing it here too. **It needs the spread's in-regime distribution with its bar count.** **→ owed by me, or by BRENT if he holds the series.**
- **Gap/event risk:** single-name equity — earnings inside any multi-month hold *(VLO/MPC report late Oct; **date not verified this session — verify before any hold through it**)*. Refinery-specific operational risk (fire/outage) is a **single-asset** risk the ETF would diversify and the single name does not.

## 8. TARGET / MANAGEMENT

- **Driver test — `RISK_RULES` #23, and this card is its first live application.** ⭐ **On any session this position moves materially, name the driver IN FIGURES, IN-SESSION, BEFORE any add: is it the CRACK (the underwritten mechanism) or CRUDE BETA (not underwritten)?** **Discriminator: refiner move vs XLE/USO the same session.** **Crack-led ⇒ mechanism operating. Crude-led ⇒ you were paid by something this card never underwrote ⇒ that is evidence AGAINST it, and it TRIMS rather than adds.** ⛔ **No name ⇒ no add.**
- **Target:** ⛔ **NOT NAMED.** Same reasoning as row 58's A2 — a structural thesis with no dated catalyst has no natural target, and a fixed one caps a winner the thesis says is being paid to run. **Ratchet, don't target** — and the ratchet width needs the same base-rate work as the §7 slot. **Deliberately left OPEN.**
- **Partial exits:** trim step is **1 share = 33%** at VLO (25% at PSX, 10% at DINO). ⚠️ **Coarse — worth knowing before the fill, not after.**
- **Roll rule:** **N/A** (shares).
- **Time stop:** ⛔ **NONE, deliberately.** *(A fresh dated review clause on a card with a live invalidation is the silently-renewed-clause shape refused on `TRY-FIRE-006` and again on 004's 60-DTE review.)*

## 9. WHY NOT / COUNTER-TRADE — *the best case against my own recommendation*

**★ THE STRONGEST OBJECTION: `$1,033` may not be worth the operational weight of a position.** A +20% move on the whole thing makes **~`$207`** — real, but it will not change the book, and it consumes a card slot, a monitoring obligation, and a decision from Will. **If the honest size the constraints permit is too small to matter, the correct answer may be NO TRADE and to fix the CONSTRAINT instead** — i.e. **trim USO to make room**, which is BRENT's own §6 third bullet and is a *sleeve-sizing* decision I own but which needs Will's word on his oil ceiling first.

⇒ **I am putting that on the table as the live alternative, not burying it:** **(i) 3 × VLO now at `$1,033`**, or **(ii) trim USO first, then size the refiner leg properly** — (ii) is strictly better on concentration (it cuts the 77.1% USO-linked share from both ends at once) and strictly worse on execution (two decisions, and it books a loss on USO at −9.5%).

**Second objection, honestly stated:** the +14–17% run has **already happened**. Every fact in §2(b) that argues against options also argues that the *equity* is not cheap. **The counter is that shares carry no vol premium and no clock** — but "the move already happened" is a real risk and this card does not pretend otherwise.

## 10. WHAT I AM SENDING BACK TO BRENT

1. ⛔ **His 60–90 DTE claim is FALSE on both named tickers** (§2a) — measured, not argued.
2. ⛔ **His "today is green" premise is FALSE for the instrument being transacted** (§3) — he priced the day off `BZV26`; the refiners are red. **His instruction was right; his tape was the wrong one.**
3. 📌 **`distillate-yield-by-name` is 58 days owed and it is now the binding open item** (§6) — it decides the ticker.
4. 📌 **A definitional question that is his, not mine:** does a **defined-risk debit spread** count toward *"undefended-linear share"*? He wrote that a call adds to it *"until it goes ITM."* **A debit spread's loss is capped by construction, so I would argue it is defended — but it is HIS metric and I will not redefine it to make my own structure fit.** *(Moot for this card, which is shares; live the moment anyone proposes a spread.)*

## Decision

**Recommended: BUY `3 × VLO` @ market-or-better, ≈ `$1,033`, as the distillate strong-leg starter** — rule-#6-clean on today's refiner tape, inside the 80% undefended-linear ceiling, inside the `$500` cap, no tenor-band violation.
**Live alternative: (ii) trim USO first and size the leg properly** — better on concentration, needs Will's oil-ceiling number.
⛔ **Both are blocked on: Will's intended oil-exposure ceiling, and a re-measured refiner day-colour on the day of the fill.**

**APPROVAL REQUIRED — Will must approve/reject before execution.**
