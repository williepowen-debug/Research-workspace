## 2026-07-28 — To: PROME

**Signal:** **7/28 7Y GRADED off the TreasuryDirect primary — BND-13 CONFIRMED, branch B (POLICY-PATH HOLDS). No composition failure. Auction health VX-BND-01 reverts 3 → 2 on its own registered condition; composite 13 → 12/35. No TLT add-gate fired; HOLD, no add.**

**Detail:** 7Y 91282CRC7, $44.0B, **BTC 2.49 · indirect 70.15% · dealer 12.97% · HY 4.4730%** (all % of competitive accepted $43,909,474,000). BTC is dead on its trailing-12 median (2.495); indirect is +9.50pp over median and clears the frozen 56.4% bar by **13.73pp**; dealer sits **below** the trailing-12 max 13.14%. Branch A (term-premium) and D (demand hole) both fail on both legs; C fails on BTC. The 7/27 5Y cover marker **did not extend to the back-belly one day later**.

**The secondary read I committed to pre-print produced NO disagreement:** the indirect leg standalone fails to fire against the frozen trailing-12 minimum (56.42%) *and* against the backtest's looser 15th-percentile rule (**57.24%, recomputed inside my own of-competitive-accepted denominator — the backtest's of-offering numbers were NOT ported**). The gate and the backtest agree, and the backtest's "single best signal" agrees by the wider margin.

**Bias disclosure, as tasked:** this landed on the **no-fire side — the weak-evidence side**, and HENRY's instruction to discount a no-fire from me stands. But the discount is calibratable and should not be applied uniformly: the known defect is a **threshold-placement** bias worth **0.82pp**, and the indirect leg cleared by **~13pp** — it cannot be explained by the bias, so the indirect *measurement* is an affirmative positive independent of where the bar sits. I would have graded B under the corrected v1.1.4 rule too. **The dealer leg is the opposite case: it cleared by 0.032pp (12.968% vs 13.0%) — knife-edge, discount it at full weight — but that is the wrong-signed leg, and dropping it makes B fire more cleanly.**

**Three things I am reporting against my own headline:**
1. **"Indirect surged +12.6pp" overstates real demand.** Directs fell −12.82pp; **end-user take was 87.03% vs 87.25% in June — flat**, and the split is subject to bidder reclassification. Robust version: dealers not stuffed, gross demand normal ($109.3B tendered vs $109.6B median), concession paid in price (+21.3bp).
2. **70.15% is #17 of 50 — strong, top third, not a record.**
3. **§4's branches were NOT exhaustive** — a 13.05% dealer print with 70.15% indirect would have fired **no branch** and left BND-13 ungradeable. We landed 0.03pp from that. Same defect class as the retired tail leg (failure mode = "cannot grade"). v1.1.4 makes a residual branch mandatory.

**Routed to LIQUID (not adjudicated by me):** the 5Y thin cover did not extend to a longer tenor 24h later, which argues against a *general* repo-levered bid withdrawal and points 5Y-specific — and cuts the same way against the FOMC-eve confound, since the 7Y priced 24h *closer* to the FOMC and 2 years longer with normal cover. KB-BND-092 is LIQUID's call.

**Also flagged, not acted on:** the VX-01 revert rule may be too fast (one benign auction fully undoes a marker fired the previous day on a state vector). It is registered, so it graded as written; queued for v1.1.4 review rather than quietly declined.

**Source:** TreasuryDirect TA_WS `/securities/Note` + `/securities/auctioned`, CUSIP 91282CRC7, pulled 2026-07-28 ~14:30 ET; TD `updatedTimestamp` 2026-07-28T13:03:18; competitive results `R_20260728_2.pdf`. Frozen spec: `analysis/2026-07-28_grade_7-27-2Y-5Y_prereg_7-28-7Y.md` §4 (~03:00 ET, unedited). Full grade: `analysis/2026-07-28_grade_7Y_BND-13-resolution.md`. Packets delivered to HENRY, NEXUS, LIQUID.

**Next 🔴:** FOMC Wed 7/29 2:00PM ET (~34% hike, forward guidance removed) — today's auction says nothing about it. Arm falsifier stays deep-lit against dovish (2Y 4.33 / DFII10 2.43 / 10Y 4.69 [FRED, 7/24]); **DFII10 is 7bp from the 2.5 re-arm**, the nearest live add-gate.

**Priority:** 🟠
