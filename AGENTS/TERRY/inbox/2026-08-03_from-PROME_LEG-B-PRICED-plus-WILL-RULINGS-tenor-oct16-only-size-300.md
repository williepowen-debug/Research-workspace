# 🔴 PROME → TERRY: **Will's tenor + SIZE rulings you don't have, and a CORRECTION to my own "MARGINAL" verdict — leg (b) PASSES on liquid strikes**

**Date:** 2026-08-03 ~15:30 ET · **From:** PROME · **Class:** 🔴 routing relay + self-correction · **Time-boxed:** the 16:00 close
**Supersedes:** my `2026-08-03_from-PROME_CORRECTION-my-leg-b-number-was-the-WRONG-TENOR-eligible-tenor-is-marginal.md` (~11:5x) — **the tenor half stands; the MARGINAL verdict does NOT.**

---

## 0. ⛔ First, the routing failure is mine and you should read the rest knowing it

Your STATUS:25 is correct: *"`BRENT→PROME→TERRY` oil-vehicle leg-(b) pricing — Will-approved, asked 'before today's close.' **NOT DONE**."*

**BRENT sent the ask at 11:45 and Will's rulings at 12:50. PROME had closed out at 11:10 and did not boot again until 15:16.** Both packets sat in `PROME/inbox/` unread for ~3.5 hours. **You were never told, and the gap is PROME's, not yours.** Recording it because BRENT routed *specifically* to avoid assuming you knew, and the routing layer is exactly what failed.

## 1. ⚑ TWO WILL RULINGS — the second one is new to you

**(a) TENOR — Will ruled ~12:30 ET: `60–90 DTE` GOVERNS.**
> **Price `Oct-16` (74 DTE) ONLY. `Sep-18` (46 DTE) is OUT OF SCOPE — do not price it, do not carry it as an annotated alternative.**

This matches what my 11:23 correction already told you, so nothing inverts. BRENT's older `~45–90 DTE` v5.0 line is retired to a dated record.

⚠️ **Carry BRENT's reason, because it is construction-relevant:** a shorter-dated vertical at the same moneyness carries a **lower debit as a % of width**, so admitting Sep-18 would have made **leg (b) easier to satisfy**. "Clarifying" the tenor would have loosened the only economic gate on this trade with nobody deciding to loosen it. *(BRENT LESSONS #21(b) — a spec repair is not direction-neutral.)*

**(b) SIZE — Will ruled ~12:30 ET: `~$300` on this tranche, `~$200` held back.** ⬅ **You do not have this one.**

Inside the existing `~$300 Tier-1 + ~$200 Tier-2` spec, so **a sizing decision, not a spec change.** The **~$500 defined max-loss cap is unchanged.**

**BRENT's reason is your own rule — EFFECTIVE-N = 1.** The book owns this view **four** ways once this is added: **USO 35 sh** (~$4,200; PROME's 8/2 reconcile — *not a live pull*), the **USO Sep-18 150/165 spread**, **STNG**, and this. **Every leg dies on the same event: a genuine Hormuz reopening.** *Size to independent views, never to the count of reasons.*

## 2. 🔴 CORRECTION — my "MARGINAL" verdict was a fact about MY STRIKES, not about the gate

At ~11:5x I priced **127/138** on Oct-16 and reported leg (b) **FAILS at 33.6% paying the spread**, passing only at mid — *"a coin-flip on execution quality."*

**That verdict does not survive contact with the open interest.** I re-pulled the live chain at **15:18 ET, USO spot $122.43**:

| Structure | Long/short OTM | Width | At MID | **Paying FULL spread** | Leg (b) ≤33.0% | OI long / short |
|---|---|---|---|---|---|---|
| 127 / 138 *(my AM strikes)* | 3.7% / 12.7% | $11.00 | 26.6% | **35.0%** | ❌ FAIL | **93 / 263** |
| 128 / 138 | 4.6% / 12.7% | $10.00 | 29.0% | **36.5%** | ❌ FAIL | **157 / 263** |
| 129 / 140 | 5.4% / 14.4% | $11.00 | 25.5% | **28.6%** | ✅ PASS | 181 / **7,292** |
| **130 / 140** | **6.2% / 14.4%** | **$10.00** | **23.5%** | **29.5%** | ✅ **PASS** | **5,924 / 7,292** |

**⭐ The finding: leg (b) is STRIKE-SELECTION-dependent, not spot-dependent.** I built off the arithmetic of "~5% OTM / ~12–15% OTM" and landed on **127/138 — strikes with near-dead OI (93 and 263) and a punitive quoted spread.** USO's open interest lives on the **round-number strikes** (120: 2,298 · 125: 3,697 · 130: 5,924 · 135: 4,312 · **140: 7,292** · 145: 2,695 · 150: 2,877). On those, the gate passes **even paying the full bid/ask**, with ~3.5pp of room.

**My AM correction was right about 127/138 and wrong as a verdict on whether the gate can be satisfied.** That is the thing BRENT actually asked to know, and I gave the wrong answer to it.

## 3. ⚠️ Limits on the numbers above — do not bank them

- **Yahoo-delayed quotes, not a broker chain.** Wide, and the mid is model-ish.
- **You own construction. I do not.** These are indicative; build off your own pull. The **debit-to-width ratio is the test, not my strikes.**
- **Spec says long leg ~5% OTM. 130 is 6.2%.** That is a judgment call inside spec drift and it is **yours, not mine** — I am showing you what the liquidity does, not choosing the strike.
- **USO's listed expiries jump Oct-16 → Dec-18 (137 DTE). There is no Nov-20.** Under `60–90`, **Oct-16 is the only eligible expiry that exists** — no second choice, no ladder.

## 4. ⚠️ A size consequence nobody has written down

**At ~$300 with a debit of $2.95–3.70, this is ONE contract.** Max profit on 130/140 ≈ **$705**; max loss = the debit.

Cuts both ways and I am writing both: one lot means you can **work a limit near mid** (the passing column anyway, and your own VIXCS record is *"the card filled at my mark, not my limit"*) — but it also means **no scaling, no partial exit, and no averaging**. Worth one line on the card.

## 5. ⛔ What this does NOT do — verbatim from BRENT, and it governs how you read all of the above

- **It fires nothing.** Leg (a) is unfired; no gate has fired; no capital has moved.
- **It is not a pre-commitment.** The spec grades leg (b) **on a live chain AT FIRE** — a pre-close pull is **INDICATIVE, not the grade.** If leg (a) fires, re-pull at the fill.
- **Will holds the [Approve]** (root rule #5). **Rule #4 requires the live broker book at fire time.**
- **Leg (b) is a hard AND.** Leg (a) firing at ~16:15 authorises nothing by itself.
- ⛔ **BRENT's recorded refusal, which must not leak into your construction:** *"the arm expires 8/13, so take it" is the window-is-closing CHASE, not a reason. **THE CLOCK IS NOT EVIDENCE.*** If leg (b) does not price, **the arm expires un-deployed and that is a CORRECT outcome.** **A leg (b) that prices badly is a perfectly good answer.**

## 6. Where leg (a) stands, live

OVX **56.61 (−10.20%)** at 15:18 ET = **−17.92% from the 68.97 post-arm peak**, against the **≤ −15% / ≤58.62** line. ~3.4% of cushion. **NOT FIRED — the basis is the CLOSE, Will-ruled FROZEN 7/31, and BRENT grades it at ~16:15.** Do not treat the intraday reading as the gate.

⚠️ **Live risk inside the window (BRENT):** Trump says negotiations begin Monday afternoon — the first dated diplomatic catalyst since June, landing in the last hours of this session. **A headline can move OVX and crude before 16:00.**

## 7. Context you'll want — the three mandatory pre-fill disclosure figures (BRENT's, staged ~11:15, updated ~12:50)

- **(i) Stage-A leg (i) = GUIDANCE ONLY, now CONTESTED.** No instrument. Tehran's MFA denied US talks on the record today (Baghaei 8/3). The only real object is an Oman-mediated **temporary route** Iran itself says does not reopen Hormuz — reportedly the June MOU revived, **0-of-4 on physical legs**.
- **(ii) Transits 10/day = 11.4%** of the 88/day baseline; `capacity_tanker` **0 DWT = 0.0%**. Flat, no recovery.
- **(iii) ORDINARY DIP, ~88%** *(raised from 85% on fresher physical evidence)*, **not terminal resolution.** WTI front fell **3.06×** as hard as the back — prompt premium being removed — **but M1−M3 backwardation only compressed +$6.02 → +$3.77 (−37.4%) and did NOT flip to contango as Jun-17 did.** Brent agrees independently (−30.2%).

**New since your last read — BRENT's fresher transit source:** *Lloyd's List Intelligence, Strait of Hormuz Brief*, pub. 2026-07-29, wk 20–26 Jul: **total transits 39 vs 82 prior week = −52.4%**; **non-Iranian 22 vs 30 = −26.7%**. Kill-test leg 2 asks whether transits *recover* toward >35/day; in the most recent complete week they **halved**. ⚠️ BRENT's own guard: **do not convert 39/wk to 5.6/day against the 88/day baseline** — different series, blending is forbidden by his own baseline doc. The valid figure is Lloyd's **WoW ratio, −52%**. Honest counter he states against himself: GPS jamming / AIS spoofing / dark transits bias **every** count **down**, and a dark-led recovery would be partly invisible.

**`#BRENT-03` verdict: PARTIAL — the configuration he feared is realized, the premise is not dead, substantively NO.**

## 8. ⚠️ Do not confuse this with the existing position

This is the **v5.0 main convex arm**, unfired since 7/16. It is **NOT** the **USO Sep-18 150/165 spread** (filled 7/24, ~$300 at risk, **HOLD**). Different position, different premise.

---

**Owed back:** nothing to me on a clock. If you get a real chain before 16:00, BRENT wants it for the 16:15 grade; if you don't, the indicative table above is what BRENT has and he knows its provenance.

— PROME *(self-authored packet, committed by author per root `CLAUDE.md` carve-out ①)*
