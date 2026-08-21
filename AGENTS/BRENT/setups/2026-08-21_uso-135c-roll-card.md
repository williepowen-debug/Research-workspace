# TRADE CARD — ROLL `USO Oct-16 $135C ×2` → `Dec-18 $135C ×2`

**Built:** 2026-08-21 Fri **09:5x ET** (clock read from `date`, not inferred — RISK_RULES 6b)
**Author:** BRENT · **Requested by:** Will, in-session ("let's roll the 135C out")
**Status:** 🔴 **PROPOSAL — AWAITING WILL [Approve]. NOTHING FILLED. `$0` MOVED.**
**Chain pull stamp:** `2026-08-21 09:51:14 EDT`, USO spot **$134.53** — every option figure below is from that one pull (RISK_RULES #6, same-timestamp marks).

---

## ⚠️ READ FIRST — THE POSITION IS NOT WHAT MY OWN SURFACE SAID

`TRADE.md` carries this leg at **`Mkt $910 · cost $1,421.33 · −36.0%`** `[8/4 broker export]`.

**Live chain says it is `+41.7%`.**

| | 8/4 surface | **Live 8/21 09:51 ET** |
|---|---|---|
| Oct-16 135C mid | $4.55/sh | **$10.07/sh** |
| Position (×2) | $910 | **$2,014** |
| vs cost $1,421.33 | −36.0% | **+$592.67 / +41.7%** |

**The leg swung from deeply underwater to solidly profitable and no surface of mine reflected it.** This is `finding_option_marks_need_live_chain` (RISK_RULES #5) realized — and it materially changes what this roll *is*. **This is not a rescue roll of a loser. It is a roll of a winner**, which changes both the risk framing and what the card must contain.

⚠️ **COST BASIS IS NOT AUTHORITATIVE (RISK_RULES #4).** The `$1,421.33` is a state-file figure from the 8/4 broker export (TERRY-reconciled, Will-confirmed complete). **Every P/L number on this card rests on it. Confirm before filling.**

---

## ① THE STRUCTURAL GAP THIS ROLL MUST CLOSE

**`RISK_RULES #9` — "Every profit zone needs its own harvest rule"** — is **violated on this leg right now.** It has no management rule at all: no harvest, no time stop, no invalidation. Your 8/18 HOLD covered **the shares only**; TERRY says so explicitly, and *"hold"* is not a coherent instruction for a dated option.

★ **#9 is the root cause of this desk's only realized loss** (−$111.60, `TRY-VIOLET-VIXCS`, where every trigger was keyed to the move going *further* and none to being *merely profitable*). **This leg is now sitting in exactly that unguarded profit zone.** A roll that extends its life without adding a harvest rule reproduces the known failure on a bigger position. **§⑤ is therefore not optional garnish — it is the reason the card is worth filling.**

---

## ② WHY ROLL AT ALL — root rule #7

> *"Roll duration, don't trim size. Trimming = thesis broken. Rolling = timeline uncertain."*

**Thesis is intact and the tape confirms it** — Brent **$94.04** live (+0.46%), six straight up sessions, highest since 7/24; M1−M3 **+$4.29**, backwardated, no contango flip. **What is uncertain is the clock, not the direction:** Hormuz has no resolution date, and THESIS v5.6 is unresolved on the supply leg.

⇒ **Rolling duration is the rule-#7-correct response.** Trimming would assert a broken thesis I cannot support.

---

## ③ LIVE CHAIN — the candidates

*USO $134.53 · pull `2026-08-21 09:51:14 EDT` · IV/OI/width as quoted*

| Leg | bid | ask | mid | width | IV | OI | vol |
|---|---|---|---|---|---|---|---|
| **Oct-16 135C** *(held)* | 10.05 | 10.10 | **10.07** | **0.5%** | 48.7% | 2,406 | 48 |
| **Dec-18 135C** *(A)* | 13.20 | 14.45 | **13.82** | 9.0% | 47.8% | 5,427 | 214 |
| Dec-18 140C *(B)* | 11.00 | 12.50 | 11.75 | 12.8% | 48.2% | 11,583 | 1,352 |
| Dec-18 145C *(C)* | 9.95 | 11.35 | 10.65 | 13.1% | 50.4% | 7,003 | 6,669 |

### ⛔ A HARD CONSTRAINT, MEASURED FROM THE CHAIN — **USO LISTS NO NOVEMBER EXPIRY**

Available expiries run **… Oct-02 (42d) · Oct-16 (56d) · [GAP] · Dec-18 (119d) · Jan-15 (147d) …**

**There is no listed USO expiry between 56 and 119 DTE.** This is not a preference; it is what the chain contains. Its consequence is §⑦.

---

## ④ RECOMMENDED — **OPTION A: same strike, roll out only**

> **SELL to close `USO Oct-16 $135C ×2` · BUY to open `USO Dec-18 $135C ×2`**
> **Net debit: `$750` at mid · `$880` worst-case (hit bid / pay ask)**
> **Limit order at mid or better — do NOT market it.** The Dec strike is 9.0% wide; mid-vs-ask is **$126** on a 2-lot.

| | Value |
|---|---|
| Days bought | **+63** (56 → 119 DTE) |
| Cost per added day | **$11.90** mid · $13.97 worst |
| **Decay of the leg being retired** | **$19.61/day** (BS theta, ×2 contracts) |
| Decay of the replacement | **$13.53/day** |
| **Decay break-even** | **$750 ÷ $19.61 = 38.2 days** — the roll buys **63**. ✅ |
| Delta | 0.544 → **0.569** (preserved) |
| Net vega | **+18.58** per vol point |

**Why A and not B/C:** the position's entire job is to pay on a crude move. B and C cut delta to 0.517 / 0.473 to save $414 / $634. **Rolling out *and up* is a size reduction wearing a roll's clothes** — root rule #7 says the answer to timeline uncertainty is duration, not less exposure. If the thesis is right, A pays and B/C partially don't.

---

## ⑤ 🔴 HARVEST RULE — MANDATORY, closes the `#9` gap

> **When `Dec-18 135C` mid ≥ `$21.71/share` → SELL 1 of the 2 contracts.**

**Why that number:** cumulative cash into this line = `$1,421.33` (original) + `$750` (roll) = **`$2,171.33`**. One contract at $21.71 returns **$2,171** — **the entire cumulative outlay comes back and the remaining contract runs as free carry.**

✅ **#9's own reachability check PASSES — the trigger variable is one the profit zone actually reaches.** $21.71 needs USO ≈ **$156.71** at expiry for pure intrinsic (less, earlier, with time value). `TRADE.md` anchors **USO ~$153 ≈ Brent ~$110**, so this is **Brent ≈ $112** — inside the Scenario-C target band (~$115–120), not beyond it.

**Second contract:** runs to the time stop in §⑥.

---

## ⑥ TIME STOP, CATALYSTS, INVALIDATION, DO-NOT-CHASE

**⏱️ Time stop (Non-Negotiable #7 — no expiry drift):** **review Fri Nov-13** (35 DTE remaining). If the position is not in profit **and** no thesis catalyst has fired by then → **close.** Do not ride an ATM call into terminal decay.

**📅 Catalyst map — and the honest part:**

| Date | Event | Inside Oct-16? |
|---|---|---|
| Sep 1 | Russia diesel producer-direct carve-out | ✅ already covered |
| Sep 6 | **OPEC+ — the Q4 decision 8/2 deferred** | ✅ already covered |
| Sep 9 | **SPR exchange-window falsifier** | ✅ already covered |
| Sep 30 | BRT-26 window close | ✅ already covered |
| **Oct 1 – Dec 1** | **EU gas storage binding window** (landing zone 77–80%, 90% out of reach) | 🆕 **only in Dec-18** |

⛔ **STATED AGAINST THE ROLL: all four near catalysts already sit inside the Oct-16 expiry.** The roll does **not** buy new catalyst coverage in the Oct→Dec gap — apart from the EU storage window it buys **post-catalyst runway**, i.e. time for those resolutions to *transmit into price*. That is a coherent rule-#7 reason, but it is a weaker one than "it covers a catalyst you'd otherwise miss," and I am not dressing it up as the stronger one.

**🚫 Do-not-chase (Non-Negotiable #5):** **do not pay more than `$4.40/share` net debit** ($880 — today's worst-case). If the calendar widens past that, **stand down and re-quote next session.** Separately, if USO trades **above ~$140** before the fill, the Oct leg goes ITM and the economics change → **re-quote, do not chase.**

**💥 Invalidation (Non-Negotiable #2):**
- **Thesis:** a genuine Hormuz operational resolution / durable de-escalation. ⚠️ **`N_eff = 1` — this kills all four oil legs at once.**
- **Price:** USO < ~$115 (Brent ~$78–80) **with the curve flipping to contango** ⇒ the Phase-1 premium has bled out.

**💰 Defined loss:**

| | Mid | Worst |
|---|---|---|
| Max loss (full Dec position → $0 below $135 at expiry) | **$2,764** | $2,890 |
| Cumulative cash committed to this line | **$2,171.33** | $2,301.33 |
| New cash at risk today | **$750** | $880 |

⚠️ **THE DISCLOSURE THAT MATTERS: rolling re-risks the `$592.67` of unrealized gain *and* adds `$750` of new cash.** Holding Oct-16 to expiry risks the same gain but adds nothing. **The roll is an increase in committed capital, not a neutral maintenance step.**

---

## ⑦ ⛔ TWO RULINGS I NEED FROM YOU — I will not fill without them

### (a) THE TENOR BAND IS UNSATISFIABLE — and "fixing" it is exactly the trap my own file names

**TRADE.md § BINDING WILL RULINGS** (⛔ this card cited `TRADE.md:180`; that line is the pre-fill disclosure and the ruling sat ~18 lines lower — re-pointed 2026-08-21), **ratified: `60–90 DTE` governs the structural trade.**

- **Oct-16 = 56 DTE** — the held leg has **already aged out below the band.**
- **Dec-18 = 119 DTE** — **29 days above it.**
- **Nothing is listed in between** (§③).

⇒ **No available USO expiry satisfies 60–90 today.**

⛔ **I am NOT quietly widening the band, because widening it is what makes this roll possible** — and **TRADE.md § BINDING WILL RULINGS** already records that trap verbatim (⛔ this card cited `TRADE.md:182`, WHICH IS A BLANK LINE — re-pointed 2026-08-21): *"a spec repair is not direction-neutral… 'Clarifying' the tenor would have loosened the only economic gate on this trade, with nobody deciding to loosen it"* (LESSONS #21(b)). **That is this situation exactly, one rule later.**

**Your call, two clean paths:**
1. ✅ **Recommended — SCOPE ruling:** the 60–90 band governs **new structural deployments**, not the roll of an existing leg. *(Consistent with RISK_RULES #15's 7/30 scoping, which already split 60–90 structural from 21–35 off-ramp.)*
2. **One-time exception**, on the measured ground that no listed expiry satisfies the band.

### (b) ROOT RULE #6 — I am proposing a break, and here is the refuting measurement

**Today is GREEN:** USO **+0.27%**, Brent **+0.46%**. Root rule #6 says *calls on red days*. A net-debit roll on a green day **breaks it.**

**The ratified test asks for the direct measurement that refutes the day-colour proxy. Here it is:**

> Root rule #6 is a proxy for one question: **"am I paying up for convexity?"** For a **same-strike calendar** the structure is **near delta-neutral** — so the proxy barely applies.
>
> | | |
> |---|---|
> | Net delta (Dec-18 135C − Oct-16 135C) | **+0.0249/share** = +5.0 share-equivalents on ×2 |
> | Debit move per **1%** in USO | **$6.69** |
> | **Debit move from today's actual +0.27% tape** | **$1.99** on a **$750** debit = **0.27%** |

⚠️ **AND THE HALF THAT CUTS AGAINST ME, stated because a flattering reading of my own work is the one to check:** the roll is **net long vega `+18.58`/vol pt**, and **OVX is `50.62`, UP `+1.97%` today.** The *vega* leg of "am I paying up" **is** unfavourable today and points the same way as the proxy — roughly **~$19** of the debit. **Honest total day-colour cost ≈ `$21` on `$750` ≈ 2.8%.** Small, but not zero, and not $1.99.

✅ **Break conditions met:** measurement produced, in figures, **on the card before the fill**; **no hard guard relaxed** (the tenor question in (a) is escalated to you, *not* reinterpreted).
**Verdict: LEGITIMATE BREAK — the proxy is built for outright long-premium entries and is ~orthogonal to a delta-0.025 calendar.**
⛔ **Your instruction to roll is explicitly NOT the justification** — the ratified test rules *"the thesis owner says take it today"* a supporting consideration only, never the reason.

---

## ⑧ COUNTER-CASE — the best reasons NOT to do this

1. **🔴 It concentrates an already-concentrated book.** `N_eff = 1`; the forward oil sleeve is **95.3% in two USO lines**, and **74.7% of it is the 35 undefended shares**. Adding $750 to the same view buys **zero diversification.**
2. **🟠 The near catalysts are already covered** (§⑥) — the roll buys transmission time, not new events.
3. **🟠 Long vega at middling vol.** OVX 50.62 = 30th pct of 3mo but **54th pct of 1y**. If OVX mean-reverts to its 3mo low (40.33), that is **−10 vol pts × $18.58 ≈ −$186** on the roll.
4. **🟢 The genuine alternative: harvest instead of roll.** The leg is **+41.7%** and unguarded. **Selling 1 of 2 contracts now banks ~$296 of gain and closes half the #9 exposure with no new cash.** Root rule #7 argues against trimming a live thesis — but **#9 argues that an unguarded profit zone is its own risk.** ⇒ offered as **A-split** below.

**A-split (the #9-purist variant):** sell 1 Oct-16 135C (bank ~$1,005, realize ~$296 gain vs the $709 half-basis), roll the other into 1 Dec-18 135C for **~$375 net debit**. Half the new cash, half the forward delta, #9 satisfied immediately by construction.

---

## ⑨ APPROVAL GATE

**Nothing executes without your word. `$0` has moved and no order is staged.**

- [ ] **[Approve A]** — roll both, Dec-18 135C ×2, limit ≤ $4.40/sh net debit, + harvest rule §⑤
- [ ] **[Approve A-split]** — harvest 1, roll 1
- [ ] **[Approve B]** — Dec-18 140C ×2, cheaper ($336 mid), lower delta
- [ ] **[Reject / hold Oct-16]** — and I still need a §⑤ harvest rule on the existing leg
- [ ] **Ruling (a):** tenor scope — ☐ scope-ruling ☐ one-time exception
- [ ] **Ruling (b):** root rule #6 break — ☐ accept as measured ☐ require a red-day fill

---

*Built under: root rules #4 (live prices), #5 (Will approves), #6 (break test, §⑦b), #7 (roll duration); RISK_RULES Non-Negotiables #1–#8, Default Trade Quality Checklist, Option-Specific Rules, findings #4/#5/#6/#6b/#9/#10/#14.*
*Greeks are Black-Scholes off chain IVs; model prices run 3–10% above mids (yfinance IV is last-trade-derived and the Dec strike is 9% wide), so deltas are approximations. **The §⑦b conclusion is robust to that error** — both legs share a strike and sit near ATM, so their delta difference is structurally small regardless of the exact IV.*
