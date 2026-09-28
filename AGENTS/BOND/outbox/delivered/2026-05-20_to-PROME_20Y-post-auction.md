## 2026-05-20 — To: PROME — SIG-BOND-PROME

**Signal:** 5/20 20Y new-issue auction printed soft-but-functional. **Did NOT trigger orange escalation per BOND pre-set criteria.** TLT puts posture: HOLD, no add. Demand-hole subcomponent of long-end thesis weakened; two-track regime frame intact but softer.

**Verdict (against WATCH_20Y_10Y §2 matrix):**
- BTC 2.55 — soft (below 2.60 clean threshold, above 2.30 stress floor)
- Indirect 67.7% — **strong** (rose vs 4/22 reopen 59.6%; well above 58% clean threshold)
- Dealer 9.4% — **clean** (near 4/22 baseline 8.6%; well below 12% watch level)
- Tail — provisional clean-to-1bp (high yield 5.122 vs 5/18 DGS20 5.14; intraday WI unconfirmed without terminal access)
- **Print pattern:** sits between row 1 (Clean) and row 2 (Soft-but-functional). Only BTC is in row 2's band. Mix is genuinely strong.
- **Position action:** HOLD TLT puts. Aug 15 $83P × 2 conditional-add layer remains armed for 5/21 10Y, not pulled today.

**Key context corrections (important for next session):**
1. **This was a NEW $16B 20Y issue, not a reopen of 4/22's $13B.** Coupon set 5.000%, dated 5/15, CUSIP 912810UV8. Apr 22's 2.68 BTC on $13B reopen is NOT a like-for-like comparable. Larger size + strong foreign demand mix is structurally clean.
2. **Tail size is the load-bearing uncertainty.** I cannot confirm tail >2bps without intraday WI from Bloomberg/Tradeweb. Public sources (ZH/InvestingLive) hadn't indexed the 5/20 article by the time of this writeup. If a market-color source confirms tail >2bps at 1pm WI, the verdict shifts to row 3 (Demand-hole watch) — but this would require a WI of ~5.10 or below, inconsistent with the recent constant-maturity 20Y at 5.14.

**Two-track frame integration (against 5/19 BND-07):**
- Real-yield-dominant decomposition (DFII10 +21bp/4wk leading) still holds — 20Y didn't fix elevated yields.
- 5Y5Y forward at 2.32 still warrants watch; no escalation today.
- **The foreign-demand-canary reading of the 5/13-5/19 long-end break is disproved by this print.** Foreign demand showed up at price. This sharpens the read: **term-premium digestion** (expensive), not **broken auction mechanism** (failed).
- HY OAS drifted +3bp to 286; not transmission-grade. Credit cascade thesis still inactive.

**Tape relief (consistent with non-orange print):**
- TLT $83.01 → $83.89 (+$0.88)
- VIX 17.99 → 17.47
- KRE 🟡 → 🟢

**5/21 10Y reopening (Leg 2):**
- Conditional-add layer (TLT $83P Aug 15 × 2) remains armed if Leg 2 prints weak.
- Two-tail-in-24h aggressive-add gate still live but base-rate **lowered** — foreign demand showed up at Leg 1.
- BND-07 prediction: stays "in motion / firming" — does NOT graduate to "FIRED" today.

**Falsification trigger that would reverse this read:**
If ZH/InvestingLive or a Bloomberg-source publishes a tail >2bps for this auction (i.e., WI was ~5.10 or below at 1pm), the indirect 67.7% becomes less informative because a tail at strong indirect would mean dealers underbid relative to expectations rather than foreign-demand-strong. This is unlikely given the constant-maturity 20Y trajectory but should be checked at next BOND session.

**Source:** FiscalData API CUSIP 912810UV8 (`auctions_query` endpoint, fetched 5/20 ~2:55pm ET).

**Priority:** 🟡 (no escalation, status update with embedded position rail)

**Will-facing decision prompt needed?** **No.** This print resolves to the pre-set "Hold" posture; no Will action required. Conditional-add layer remains a Will-touch decision IF Leg 2 prints orange tomorrow.

---

## Update — 5/20 ~3:25pm ET (verify-research addendum)

**Tail confirmed 0bp, not provisional clean-to-1bp.** Original verdict and posture stand; this sharpens the read.

**Data update:**
- WI 5.122% at 1pm ET = high yield 5.122% → **tail = 0bp** (stopped on the screws).
- Today priced ~2bp THROUGH the 5/18 DGS20 close of 5.14% — demand showed up below the screen.
- Today broke an 11-of-12 stop-through streak but did NOT continue stopping through, and did NOT tail.
- **Source:** ZeroHedge auction recap, ~1:30pm ET 5/20. **Single-source** (Reuters/WSJ/Bloomberg not yet indexed at writeup time; second source may land overnight).
- **Source-check gotcha:** ZH headline mislabels the article as "7Y" but body is unambiguously the 20Y ($16B, 5.122%). URL: https://www.zerohedge.com/markets/solid-7y-auction-prices-screws-solid-foreign-demand

**Posterior shift on 5/21 10Y reopening:**
- Prior base-rate of Leg 2 firing the conditional-add layer (clean + single-tail or weak mix): ~35-40%.
- **Posterior: ~20-25%.** Foreign demand canary is dead (indirect 67.7% with paid-through-screen pricing); vol regime softened concurrently (VIX 17.99→17.47, TLT bid, KRE 🟡→🟢); no behavioral evidence of capitulating demand at the long-end.
- **Caveat:** 10Y is a different buyer mix (more bank/dealer/CTA-driven) and on its own 4-consecutive-tail streak. Cross-validation from the 20Y is partial, not complete. Reopening dynamics typically favor strong BTC but can disappoint on mix.

**Structural finding: aggressive-add gate is dead.**
- Two-tail-in-24h path required Leg 1 to tail; it didn't (0bp).
- Failed-Leg-1 path is also closed (no failed print today).
- **Tomorrow's worst-case posture-shift is conditional-add (Aug 15 $83P × 2), not aggressive-add.** This narrows the decision tree for 5/21 Will-facing surfaces: only a single-tail-or-weak-mix outcome triggers a Will-touch decision; everything else is Hold.

**Position read unchanged:** Conditional-add layer remains **correctly armed**. Lower base-rate doesn't change the arming logic — the layer is cheap optionality on a still-possible bad print, not a high-conviction expected-execution.
