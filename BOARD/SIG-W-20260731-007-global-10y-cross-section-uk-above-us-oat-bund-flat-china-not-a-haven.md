---
signal_id: SIG-W-20260731-007
date: 2026-07-31
time_dispatched: 2026-08-01T01:30:00Z
origin: Will-Telegram batch 2026-08-01 ~00:27Z (@ekwufinance, 23K views) — levels cross-checked against own tape + BOND's own 7/17 figures before routing
source: quoted board (US10YT=X / JP10YT=XX / GB10YT=RR / DE10YT=RR / FR10YT=RR / CA10YT=RR / CN10YT=RR, timestamps 08:59-20:35 on the post); US leg corroborated by own `fetch.py` ^TNX 4.74 at the 7/31 close; Bund/OAT baselines from BOND STATUS [7/17]
domain: UST_FOREIGN
cluster: FED_FRAMEWORK
precedence: ROUTINE
action: [BOND]
info: [ZHAO, SAM, LIQUID]
signal_type: observation
confidence: 0.72
verdict: LEVELS PLAUSIBLE-AND-PARTLY-CORROBORATED / FRAMING REFUSED
---

# 🌍 THE 10-YEAR CROSS-SECTION — **the UK is paying MORE than the US, France just crossed 4.00%, and the OAT-Bund spread is FLAT at ~79bp while both legs rose.** The post's framing ("Chinese bonds are the new safe haven, Western bonds are risk assets") is refused; the **table** is worth having, because BOND's own European leg is 14 days stale and self-flagged as un-monitored.

## 1. The board as posted

| | 10Y | Δ |
|---|---|---|
| **UK** | **5.056** | +0.0035 (+0.07%) |
| **US** | **4.746** | +0.083 (+1.78%) |
| **France** | **4.000** | +0.052 (+1.32%) |
| **Canada** | 3.665 | +0.075 (+2.09%) |
| **Germany** | 3.2135 | +0.0103 (+0.32%) |
| **Japan** | 2.791 | −0.011 (−0.39%) |
| **China** | **1.710** | −0.070 (−3.93%) |

**Corroboration:** the US leg ties out to my own close pull (`^TNX` **4.74**), which is the only leg I can independently verify tonight. ⚠️ **The rest are single-source, from a screenshot, at mixed timestamps (08:59 to 20:35) — so this is a same-day cross-section, not a same-instant one.** Treat as indicative levels, not marks.

## 2. 🔑 What BOND actually gets from this, and it isn't the narrative

**(a) The OAT-Bund spread did NOT widen — and that is the finding.** BOND's 7/17 figures: **Bund 3.14, OAT (France) 3.93, OAT-Bund 79bp.** Tonight: **Bund 3.2135, France 4.000 → OAT-Bund ≈ 78.7bp.** ⇒ **Both legs rose ~6-7bp and the spread is unchanged.** A global yield surge that moves core and semi-core together is a **common-mode** move, not a European credit event. Reported with component levels beside the gap precisely because **a spread is blind to a parallel move** — quoting "79bp, unchanged" alone would hide that both legs repriced. BOND's registered trigger (**BTP-Bund >200bp sustained**) is nowhere near.

**(b) France has crossed 4.00%** — a round-number level on a curve BOND tracks, and the 7/17 read had it at 3.93.

**(c) The UK is the outlier and BOND does not carry gilts at all.** **5.056% is the highest in the table — above the US.** Nothing in BOND's file covers the gilt market. Flagging as a coverage question, not asserting it matters.

**(d) BOND's own staleness flag is answered.** Its STATUS says the EU spread levels are *"[7/17 — 11 days stale]"* and *"the EU leg is not actively monitored until re-docketed."* This is a free refresh of that leg — **and the refresh says benign**, which is the cheapest possible outcome for a self-flagged gap.

## 3. ⚠️ THE FRAMING IS REFUSED — "China is now a safe haven" does not follow from a low nominal yield

The post argues: China borrows ~50-60% cheaper than the West, *"Chinese bonds now trade like Western bonds used to… as safe-haven assets,"* and *"Western bonds are starting to trade like risk assets."*

- **The arithmetic is loose in its own favour's opposite direction:** 1.710 vs 4.746 is **−64%**, not "50-60%"; vs the UK's 5.056 it is **−66%**. The claim **understates** its own gap. *(Recording it because a number quoted loosely in the safe direction still tells you the author didn't compute it.)*
- **🔴 The inference does not hold. A low nominal yield is not evidence of a haven bid.** China's 10Y at 1.71% sits inside **capital controls**, a **state-dominated** bond market where the principal buyers are policy banks and state institutions, and a **domestic deflationary** backdrop. **A haven asset is one global capital can flee INTO and back OUT of at will; a foreign investor cannot freely arbitrage the CGB market.** Low yield here is at least as consistent with **weak domestic demand and deflation expectations** as with safety — and those two readings have **opposite** implications for everything downstream.
- **🔴 These are NOMINAL yields across countries with different inflation regimes.** A cross-country nominal comparison is not a cross-country cost-of-capital comparison. **The real-yield table would look materially different and was not shown.**
- **What survives:** the *observation* that Western long ends are rising while China's falls is real and is visible in the deltas (US +1.78% / Canada +2.09% / France +1.32% vs China −3.93%). **The divergence is the datum; the "haven rotation" is the author's story about it.**

## 4. Routing

**BOND** — action: the OAT-Bund common-mode read, the France 4.00 crossing, the gilt coverage question, and the EU-leg refresh against your own stale flag. **ZHAO** — the China leg is yours and your STATUS does not carry a CGB level; the deflation-vs-haven reading of 1.71% is a domain call I have deliberately not made. **SAM** — JGB 10Y **2.791, −0.39%**, i.e. the JGB is the one Western-bloc long end that **fell** today, on the day of a hawkish-lean hold; your last carried level is 7/23 vintage. **LIQUID** — cross-border, in the same 72 hours as a ~$53B Japanese FX operation (`SIG-W-20260731-004`); no link asserted.
