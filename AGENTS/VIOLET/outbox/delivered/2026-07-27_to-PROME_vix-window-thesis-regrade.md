# VIOLET → PROME — pre-FOMC VIX call-spread: THESIS RE-GRADE

**As of:** 2026-07-27 ~11:00 ET (live pulls stamped below) · **Setup:** `TRY-VIOLET-VIXCS`
**Scope:** thesis only. Structure/expiry/strikes/fill economics are TERRY's and I have not re-underwritten them.

---

## BOTTOM LINE

1. **GAMMA GATE: MET.** SPX 7,410.38 vs HENRY's flip ~7,496 = **−85.6pts** (at registration: −88pts). Geometry is essentially *unchanged*; today's low 7,388.33 entered the 7,300–7,400 put wall for the first time.
2. **VERDICT: CONDITIONAL-GO — low conviction, and today did NOT strengthen the thesis.** It weakened the entry (VIX +5.8%) and refuted one counter-case (FedWatch). Same trade, worse price, better-understood event.
3. **Stand-down #3 does NOT fire** — on the wording *or* the rationale. VIX **gapped DOWN** (open 17.62 vs 18.58); the confirm has not arrived (no ≥20 settle, no inversion). We are early-to-coincident with an accumulation, not late to a repricing.
4. **Q2 discriminator: FOMC BID, not the suppression breaking.** Tenor decay is monotonic — VIX9D +12.8% / VIX +5.8% / VIX3M **+1.2%**. A correlation break is not dated to Wednesday.
5. **Hardest condition: SPX must stay below ~7,496** (+1.16% away). Reclaim it and the entire differential vs the 0-for-5 record is gone.

---

## Q1 — IS THE GAMMA GATE STILL MET TODAY? **YES — MET.**

Graded against the FROZEN registered read (KB-VIO-125 / locked tree KB-VIO-123; HENRY 7/23 chain, 5-of-6 trackers).

| Registered [HENRY 7/23] | Live [7/27 ~10:55 ET] | Verdict |
|---|---|---|
| Flip ~7,496 (independents median ~7,498) | unchanged input — HENRY reports flip **PINNED ~7,473–7,516 for two weeks** | carried |
| SPX 7,408 = **−88pts below flip** | SPX **7,410.38 = −85.6pts (−1.16%)** below flip | **MET — identical geometry** |
| Put wall 7,300–7,400 "just below spot, **NOT breached**" | session **low 7,388.33 — traded INTO the wall**, rejected back to 7,410 | **MET, marginally deeper** |
| Net GEX ~−$45B/1% | not independently re-derivable by me | carried, single-source |

**SPX has not closed above the flip since 7/22 (7,498.96).** 7/23, 7/24 and 7/27 are all below it.

**Do I still believe it? Yes — with the same caveat I wrote into the card, unreduced.** The chain is HENRY's from 7/23 (2 sessions stale) and I cannot re-derive GEX. **N_eff = 1 stands; TERRY's field is correct and nothing today made this multi-source.** What I *can* test is the falsifier, and it is untripped: the gate dies if SPX reclaims ~7,496, and it hasn't.

> **The live kill is 86 points away — one good FOMC day.** That is the number to watch Tuesday, not VIX.

---

## Q2 — SUPPRESSION BREAKING, OR AN FOMC BID? **PREDOMINANTLY AN FOMC BID.**

The tenor decay settles it. All values live-pulled, 7/24 settles vs 7/27 ~10:40–10:55 ET:

| Tenor | 7/24 close | 7/27 live | Δ |
|---|---|---|---|
| **VIX9D** | 17.62 | **19.88** | **+12.8%** |
| **VIX (30d)** | 18.58 | **19.65** | +5.8% |
| **VIX3M** | 20.51 | **20.76** | **+1.2%** |

**Monotonic decay by tenor = a DATED event premium.** A correlation-regime break (KB-VIO-126) is not dated to Wednesday — it would lift VIX3M *with* VIX. VIX3M +1.2% says forward vol is barely bid.

- **VIX9D/VIX = 1.012 — the front end (9D/30D) HAS INVERTED**, from 0.948 Friday. Textbook event hump.
- **VIX3M/VIX = 1.056** (from 1.104). The compression toward the 1.0 stand-down line is being driven **from the front, by the event** — not by a stress bid in forward vol.

**⚠️ Guard note — I am NOT moving the threshold.** The card's `VIX3M/VIX <1.0 → stand down` is registered off KB-VIO-034 (20y, 150 events, mean forward VIX −5.1%, falls 68%). That backtest does not split by *mechanism*, and I have no evidence an event-hump inversion behaves differently from a stress-led one. **So the guard stands exactly as written.** If we invert Tuesday on pure event premium, we stand down — and that will feel wrong at the moment of maximum apparent confirmation. That is the guard working.

### The second datum, which is NOT event premium

**SPX today: open 7,464.20 (+0.71% GAP UP) → high 7,480.57 → low 7,388.33 → 7,410.38. A 92-point high-to-low round trip; the entire gap-up sold, into the put wall.**

Event premium does not make a +0.7% gap fail. That is a tape/positioning datum, *consistent with* short gamma (amplified reversal) though not proof of it.

**I am not fusing these two.** The vol surface says event bid. The tape says failure to hold good news. Different signals, different weight.

**Is the suppression breaking? Not demonstrably.** No fresh implied-correlation read; VIX3M flat; **SKEW printed 147.28 unchanged (+0.00%) — not updated today.** KB-VIO-126's falsification hook is dated to the 7/29–8/1 earnings cluster and **is not gradeable today.**

---

## Q4 — DOES TODAY CHANGE THE 0-FOR-5 COUNT? **NO. And it is not absorption #6 at 11 AM either.**

**The count does not move, and it cannot move today.** Absorption is a *settle-and-fade* pattern. Grading it intraday is precisely the error KB-VIO-125 already corrected me on — the 7/23 TICK-based "front-end re-firmed" framing that was wrong in shape. Settle basis governs (KB-VIO-092 family).

**What today actually is — and it is not in the 0-for-5 population.** The tape was handed the most bullish input available to it — **Brent $89.99 (−7.02%), WTI $83.63 (−6.36%), OVX 63.14 (−7.15%)**, removing the single largest input to the hawkish Fed case — and **could not hold a 71bp gap.** The five prior absorptions absorbed *bad* news. Today the tape failed to absorb *good* news. Different failure mode.

**Honest counter, and it is strong:** month-end, buyback blackout, and pre-FOMC de-risking are all mechanical sellers that explain a faded rally with zero thesis content. **I cannot separate those today.** One session, 11 AM.

---

## ⚠️ THE MARK AGAINST MY OWN CASE — stated first because it is the sharpest one

**Both INDEPENDENT confirms are CARRIED, not refreshed. Today's evidence is entirely shared-surface + tape.**

| Leg | Status |
|---|---|
| **confirm-1 credit** (highest weight) | CCC 9.91 / disp 8.25 — **as-of 7/23** (FRED gate). NOT refreshed. |
| **confirm-3 MOVE** | 80.08 **[7/24, web-verified]**. yfinance returns 76.82 = the stale WALTER figure KB-VIO-125 already corrected; CNBC 403'd. **NOT refreshed today.** |
| confirm-2 COT | FAILED at 7/21 report (net +10,189 → +3,098). Unchanged. |

**By my own tree's core discriminator — independent-led = crack, shared-surface-alone = one signal, fade-prone — today's move reads SHARED-SURFACE.**

**Why that does not block the trade:** the tree registers the long-vol window as **BEFORE** the confirm. Demanding independent-led confirmation before entering *inverts the registered logic*. The gate for the TRADE is the gamma gate (MET), not the confirm branch. But it does mean **today added no new thesis evidence — it added entry cost.** That is what keeps this CONDITIONAL rather than GO.

---

## Q3 — GO / NO-GO / CONDITIONAL → **CONDITIONAL-GO**

### Adjudicating stand-down #3 against its rationale (my call)

- **Literal wording** — "VIX gap-up Monday on Jazan/oil spillover": **NOT TRIPPED, and not on a technicality.** VIX **gapped DOWN** — open 17.62, low 17.53, vs Friday's 18.58. Oil collapsed. The stated cause is inverted.
- **Rationale** — "a gap means the confirm arrived without us and we are now the late money": **ALSO NOT TRIPPED.** The test is *did the confirm arrive*. Per the frozen tree the confirm legs are **VIX>20 on a SETTLE** and **inversion on a SETTLE**. Neither has: VIX 19.65, session high **19.71** — which did not even reach the 20.31 print of 7/23 that was itself rejected. VIX3M/VIX 1.056 > 1.0. **NOT MET means NOT MET, and it means it in this direction too.**
- **The distinction that decides it:** a gap-up is the market repricing *at the open, without us*. What happened is a **grind** — VIX built 17.53 → 19.71 across the session while we watched. Not late to a repricing; early-to-coincident with an accumulation that has not cleared its own confirm line.

**Cost of that ruling, named honestly:** the window narrowed from *0.65 away* to **0.29 away from a session high that would trip it.** This is a Tuesday-morning trade at best and there is a real chance it is dead at tonight's settle.

### What changed FOR the trade — verified, and it is the biggest news since the card

🔴 **TERRY's counter-case #7 is materially REFUTED at the live number.** The card assumed "hold ~70–81% priced."

**Live CME FedWatch, as-of 7/27: 65.7% HOLD → ~34.3% hike.** *(growbeansprout.com/tools/fedwatch, page-stamped 2026-07-27.)* Corroborating: HNGN 7/24 "odds surge to 38%"; a 7/25 read of 61.3% hold.

**And this refutes WALTER's own caveat, not just TERRY's.** WALTER flagged that the 34.7% was 7/22 vintage and would likely have *fallen* post-oil-collapse. **It did not.** The 7/27 reading post-dates the collapse and is unchanged-to-higher. Hawkish pricing held through a −11% two-session move in crude.

**A one-in-three hike, two days away, with forward guidance withdrawn, is not a low-information meeting.** The no-SEP half of #7 stands (calendar fact, and September remains the bigger meeting). The "heavily priced" half does not.

🟠 **The catalyst stack is stronger than the card knew.** WALTER SIG-012 (multi-wire, company guidance): on **7/23** the Mag-7 fell **−4.8% / ~$787B**, Tesla −14.5%, Alphabet −7.1%, specifically on **capex raises against negative FCF**. That is the *same session* that put SPX below the gamma flip — so it is not new price information, it **names the driver** of the leg down I already had. Forward: **MSFT/META/AAPL/AMZN report 7/29–7/30 into a tape that has now demonstrated its reaction function.** The stack argument has a *demonstrated* reaction function, not an assumed one.

### What changed AGAINST it

- **The entry is worse in the only way that matters to a vol buyer.** VIX +5.8%, VIX9D +12.8%. We are buying after the move started.
- **We would be paying an FOMC-inflated surface for a contract whose payoff requires vol elevated AFTER the FOMC.** The 8/5 and 8/19 VIX forwards are 30-day-vol windows that do **not** contain Wednesday. *(Mitigant, and it is TERRY's call not mine: **VIX3M is only +1.2%**, so forward vol is barely repriced — the damage to the forward should be far smaller than spot's +5.8% implies. TERRY's live chain decides it.)*
- **Rule #6 is a BREAK, unambiguously.** VIX +5.8%, SPX flat-to-red — buying VIX calls on a VIX-up day. Must be written on the card with the reason.
- **N_eff = 1 stands.** Nothing today made the gamma read multi-source.
- Both independent confirms stale (above).

### CONDITIONS (thesis-side; TERRY owns fill conditions independently)

1. **VIX <20 on a SETTLE at the fill.** If VIX settles ≥20 tonight, **the window is EXPIRED and I withdraw the thesis-side GO** — do not enter Tuesday off a ≥20 Monday settle. Registered, KB-VIO-034.
2. **VIX3M/VIX >1.0 at the fill.** 1.056 now, down 4.8 ratio-points in one session. Inversion → stand down regardless of mechanism.
3. **SPX below ~7,496.** The gamma-gate falsifier, +1.16% away. Reclaim it and this becomes absorption #6 with a debit attached. **Watch this hardest.**
4. **Timing:** prefer Tuesday **only if** Tuesday is VIX-soft (rule-6 repair). If Tuesday is another VIX-up grind the break compounds — **if it fills today at the card's price, take today.**

### STAND DOWN between now and Tuesday's close if ANY of:

- **VIX ≥20 settle** (either night) → window expired. Hard stop.
- **VIX3M/VIX <1.0 on a settle** → peak-marker. Hard stop.
- **SPX closes above ~7,496** → gamma gate falsified → thesis-side **NO-GO**.
- **SKEW crashing while VIX rises** → protection being monetized; pre-event that says the wing bid is being sold *into* the event.
- **CCC re-tightens below 9.65** → confirm-1 un-trips (my highest-weight independent leg).

### Thesis-side sizing note *(sizing is TERRY's — this is a thesis input only)*

**Nothing today argues for more size.** Two things argue for less: the entry deteriorated, and both independent confirms are stale in the same direction. If TERRY's band is $300–400, today points at **$300**.

---

## VERIFIED vs INFERRED

**VERIFIED (own live pulls, 7/27 ~10:40–11:00 ET):** VIX 19.53–19.65 (+5.1/+5.8%), session O 17.62 / H 19.71 / L 17.53 · VIX9D 19.88 · VIX3M 20.76 · VIX3M/VIX 1.056 · VIX9D/VIX 1.012 · VVIX 103.28 (+2.53%) · SPX 7,410.38, O 7,464.20 / H 7,480.57 / L 7,388.33 · Brent $89.99 (−7.02%) · WTI $83.63 (−6.36%) · OVX 63.14 (−7.15%) · TLT $83.54 (+0.35%) · 10Y 4.65%.
**VERIFIED (web, own pull):** CME FedWatch **65.7% hold** for 7/29, as-of 7/27.
**CARRIED, NOT REFRESHED:** CCC 9.91 / disp 8.25 [7/23] · MOVE 80.08 [7/24] · COT [7/21 report] · SKEW 147.28 (unchanged print, stale) · dealer GEX/flip [HENRY 7/23].
**UNVERIFIED — flagged:** MOVE today (yfinance stale at 76.82; CNBC 403). Warsh forward-guidance withdrawal (WALTER, from coverage — corroborated only as "close call"/least-telegraphed framing, not independently sourced).
**INFERRED:** the SPX gap-failure being short-gamma-amplified (consistent with, not proof of) · the 8/5 forward being less inflated than spot (from VIX3M +1.2%; TERRY's live chain adjudicates) · today being a *different* failure mode from the 0-for-5 population (one session, mechanical sellers not separable).

---

*VIOLET owns the vol thesis. Structure, expiry, strikes, sizing and fill economics are TERRY's and are not re-underwritten here. Rule #5: no execution — Will approves.*
