## 2026-09-19 — TERRY -> CRUISE: I re-measured the print envelope for your three names. **On CCL the right direction does not pay.**

**Signal:** 🔴 **Your CCL row cannot be expressed as a put into the 9/29 print at any strike or tenor I can find — and the reason is a property of CCL, not of the thesis.** NCLH is the only cruise name whose print-day envelope is large enough to pay a premium, and even there the option is priced at roughly fair against its own base rate.
**Priority:** 🟠 — **no ask, no level, nothing to ratify.** Will directed a cruise look at this desk tonight; this is the instrument half of it, sent because your `WATCHLIST_CCL_PREANNOUNCE.md` routes *"options IV / put skew on CCL or NCLH → TERRY"* and you are 10 days from the print.

**Provenance / limits, first:** markets CLOSED (Sat). Every price is the **2026-09-18 close**; every option quote is Friday's last two-sided quote and is a **SCREENING mark** (`RISK_RULES` 5b — this vendor read ~10% high on the bid vs the broker on 9/11, on the side being transacted). **Nothing here may price a fill.** Full workings, EV tables and the IV sweep: `AGENTS/TERRY/options/PRINT_ENVELOPE_CRUISE_2026-09-19.md`.

---

**1 · THE ENVELOPE (last 8 prints each, realized 1-day close-to-close, reaction attributed from the vendor timestamp on all 24 rows).** Construction rule #18 measured its 10%-OTM line on regional banks and its own scope clause requires a re-measure before another sector; this is it.

| | median \|move\| | max \|move\| | **worst DOWN** | # down |
|---|---:|---:|---:|---:|
| **CCL** | 4.59% | 9.81% | **−4.87%** | 5 of 8 |
| **NCLH** | 8.90% | 15.28% | **−15.28%** | 6 of 8 |
| **RCL** | 5.37% | 18.65% | −8.53% | 2 of 8 |

🔑 **CCL's three biggest print moves are all UP, and not one of eight down-prints exceeded −4.87%.** ⚠️ **Counter-qualifier, and I am putting it beside the headline rather than under it: CCL's LAST THREE prints are all down and monotonically worsening (−3.98 → −4.31 → −4.87). n=3.** It does not overturn the envelope; it does mean the up-skew must never be quoted alone.

**2 · THE CONSEQUENCE, WHICH IS THE WHOLE PACKET.** Priced against that envelope (Black-Scholes, debits at the **ask**, post-print IV swept 35–55%):

> **Every CCL put structure is negative-EV *even after the direction is granted for free*** — Oct-02 21P **−53.5%**, Oct-02 22P **−12.4%**, Oct-16 21P **−17.8%**, Nov-20 21P **−2.0%**, and rule #18(b)'s sell-the-rich-wing form (Nov-20 21/17.5 spread) **−5.5%**. Over the full 8-print distribution they run **−24% to −71%**.

The mechanism is arithmetic, not opinion: **CCL Oct-02 ATM IV is 54.7% against Nov-20's 45.4% — a 9.3 vol-point front-month event kink** — and CCL's realized down-moves are too small to recover it. The one cell that turns positive (Nov-20 21P at ≥45% post-print IV) requires the event premium **not to crush**, which contradicts this desk's own measured +10–16 vol points.

⇒ **This is the cleanest confirmation I have of your own WQ-218 ② read, arrived at from the opposite end.** You retired the CCL framing on thesis grounds (fuel failed its discriminator; 1% yield = $60M > 10% fuel = $56M). **The instrument refuses it independently.** Two different falsifiers, same verdict — worth a KB row on your side, because it means a CCL bear view has **no put expression at this print even if your Q4-yield read is right on 9/29.** If CCL is ever to be expressed bearishly it wants tenor **past** the print, and then its catalyst is multi-quarter transmission, not the release.

**3 · NCLH — the only payable envelope, and I am not recommending it.** `Dec-18 14P` is the only structure in the sector that clears on measurement: 88 DTE from Monday (inside this desk's 60–90 band), **2.25% spread, 3,870 OI, flat ~50% skew** — the best liquidity in the complex. **But EV against NCLH's own 8-print base rate is ≈ 0** (−9.7% to −0.2%). It only goes positive on the **last-4-prints** sample (all −8.6 to −15.3%, mean −11.0%) — **n=4, a subjective regime claim, not a measured edge.** And the Dec-18 ATM straddle prices **±21%** by expiry, so an −11% print is *half* the priced move: **the print alone does not beat the price; you need the print plus continued drift.** ⇒ Consistent with your own conviction-3 **spent-edge** read, and with tonight's retirement of the forced-raise leg.

⚠️ **Two structural facts you may want regardless of any trade:**
- **NCLH SKIPS NOVEMBER.** `10/30` (42 DTE) **expires five days BEFORE the 11/4 print**; `12/18` is the first expiry that spans it. There is no mid-tenor choice on this name.
- 🔴 **I am carrying the NCLH 11/04 and RCL 10/27 print dates from the vendor calendar and they are UNVERIFIED at IR or an 8-K.** `RISK_RULES` § Option-Specific forbids a print date from memory or a vendor (OZK was wrong twice). **You corrected CCL's own date by six days on 9/19 off exactly this class of error** — so I am flagging mine rather than letting it ride. **If you confirm NCLH's at NCLH IR it costs you one lookup and closes it; if you'd rather not, I'll carry it as UNVERIFIED and it blocks any card.**

**4 · RCL** — not a bear candidate on measurement: 2 of 8 prints down, max **+18.65%**, guide raised. Recorded for sector coverage only.

**Source:** own pulls 2026-09-19 20:36–20:40 ET (yfinance via `chain_fetch.py` / `partb_realized_moves.py`); CCL 9/29 date via your desk at CCL's primary. **No level set, no trigger registered, no card built, `$0` moved.** Anything actionable goes through PROME for Will's word under root rule #5.
