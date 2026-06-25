# BROCK — Macro-vs-Credit Discriminator + APO Live Mark + Shared-Antecedent Read
**Created:** 2026-06-25 ~noon ET (Desktop Claude Code session; OpenClaw/Codex degraded, Prome coordinating)
**Scope:** Self-contained session memo for the 6/25 alts-selloff read. Three parts: (1) APO Dec $95P live mark, (2) B1 credit-recognition discriminator + daily watch-set, (3) X1 PC-side shared-antecedent test. Pointer in `SCRATCH.md` (watch order + session log) and `STATUS.md`.
**Provenance:** Live marks via `FORGE/tools/market-data/fetch.py` (Yahoo) + FRED (HY/CCC OAS); APO option chain via yfinance read-only pull. All marks intraday 6/25 ~11:45–12:00 ET unless dated otherwise.

---

## CONTEXT — the 6/25 tape (like-for-like flag)

The "today's alts selloff" is the **6/20→6/25 cumulative repricing, not a fresh-today crash.** Intraday 6/25 the bleed has PAUSED and originators are bouncing.

| Ticker | 6/25 live (intraday Δ) | vs prior (6/18/6/20) | Bucket |
|--------|------------------------|----------------------|--------|
| APO | $122.21 (−0.31%) | −11% vs $137.50 [6/20] | Manager |
| ARES | $113.37 (−0.44%) | −12.3% vs $129.34 [6/18] | Manager |
| BX | $115.70 (**+2.40%**) | −6.5% vs $123.79 [6/18] | Manager |
| OWL | $8.60 (+1.5%) | broke further <$9 | Manager |
| ARCC | $18.01 (+0.89%) | flat vs $18.03 [6/18] | Wrapper |
| OBDC | $10.72 (−0.05%) | −1.4% vs $10.87 [6/18] | Wrapper |
| FSK | $10.10 (+0.55%) | −1.7% vs $10.27 [6/18] | Wrapper |
| BIZD | $12.25 (+0.3%) | −0.9% vs $12.36 [6/18] | Wrapper (ETF) |
| BXSL | $23.82 (+0.5%) | — | Wrapper |
| HYG | $79.92 (flat) | flat | Public HY |
| KRE | $74.56 (**+0.8%**) | banks calm/rallying | Bank |
| HY OAS | **271** [FRED 6/23] | 263 [6/17] → +8bp, band 263–271 | Spread |
| CCC OAS | **956** [FRED 6/23] | 939 [6/17] → +17bp | Spread (low-quality) |

**The move landed on high-multiple alt-MANAGERS (APO/ARES/BX), while WRAPPERS held flat and KRE rallied** — the *opposite* composition of the Stage-3 credit-recognition thesis (which wants wrappers/credit leading). Driver: firm May PCE (core 3.4% YoY, 6/25) + hawkish Fed dots (6/17) → higher-for-longer → duration/multiple de-rate on rate-sensitive managers. **This reads MACRO, not credit-substance recognition.**

---

## PART 1 — APO Dec $95P: LIVE MARK (2026-06-25)

**Position status:** LIVE position, **1 contract, HOLD-with-backstop** (Will call 6/15; TRADE.md §4 / Section 4).
**⚠️ LIVE MARK / PENDING broker reconciliation — NOT confirmed cost-basis or booked P&L. Will's broker is the truth source.**

| Field | Value (2026-06-25 intraday) |
|-------|------------------------------|
| Contract | APO **Dec-18-2026 $95 Put** ×1 |
| Bid / Ask / Mid | **$3.00 / $3.70 / ~$3.35** |
| Last trade | $1.82 (STALE — vol=1; ignore, use bid/ask) |
| IV | 44% |
| Open interest | 86 |
| DTE | **176** (6/25 → 12/18/2026) |
| Underlying spot | $122.21 |
| Moneyness | **22.3% OTM** ($95 strike vs $122.21) |
| Per-contract value (mid) | ~$335 |

**HEADLINE — the put recovered ~10–12×.** Will marked it ~$28 ($0.28/sh, "−90%") on 6/15 at APO ~$137; now ~$300–370/contract (mid ~$335) as APO fell to $122 — strike went ~31%→22% OTM with 176 DTE preserving time value. Convexity paying off exactly as the hold-with-backstop rationale anticipated.

**$130 breach = thesis-CONFIRMING, NOT a new actionable kill:**
- The fired exit-rule ("APO reclaims $130 → reassess puts") was the **upside** invalidation. APO dropping back **<$130 un-fires that concern and re-arms the put's value.**
- The **close-reeval** triggers (APO >$145 sustained **OR** HY OAS <260) are **NOT hit** — HY OAS 271 [6/23] has **widened away** from the <260 soft-kill.
- **No forced action.** Position remains HOLD-with-backstop. There is now real recoverable value if Will elects to monetize the (partly macro-driven) bounce — surface as a Will decision, not a BROCK action.

**Vehicle-mismatch flag stands (ORC 6/15):** shorting APO *equity* on a PC-credit thesis captures macro/multiple beta, not the credit leg. The put is working partly for the "wrong" (macro) reason. If/when re-expressing, the channel is wrapper/credit names or AI-collateral, not APO equity. Will's call.

---

## PART 2 — B1: Credit-recognition discriminator + daily watch-set

**Purpose:** separate "macro multiple-compression that re-compresses" from "leading edge of credit-substance recognition." 5 monitorable variables, each with a threshold + current reading.

| # | Variable | Macro look | Credit look | Threshold | Reading NOW (6/25) | Verdict |
|---|----------|-----------|-------------|-----------|--------------------|---------|
| 1 | **Wrapper-vs-manager leadership** *(cleanest)* | Managers (APO/ARES/BX, high-multiple) lead down, wrappers lag | Wrappers (ARCC/FSK/OBDC/BIZD, NAV-linked) lead down, managers lag/hold | Wrappers underperform managers by >2–3% over a multi-day window | Managers −11/−13% (6/20→6/25); wrappers ~flat (ARCC flat, FSK −1.7%, OBDC −1.4%, BIZD −0.9%) | **MACRO, decisively** |
| 2 | **HY OAS level/direction** | Compresses/holds | Widens, esp. >280 break | >280 sustained 2–3 sessions | 271 [6/23], +8bp off 263, inside 263–271 chop band, no breakout | **Neutral** |
| 3 | **Quality-tier dispersion (CCC−HY)** | Moves together | CCC widens faster than HY | CCC widening ≥2× HY / CCC >1000bps | CCC +17bp vs HY +8bp (~2×) over 6/17→6/23 | **Mild credit lean** (small) |
| 4 | **BDC discount-to-NAV** | Stable (equity beta only) | Widens (NAV erosion priced) | Median >35% sustained / fresh widening | ~25% median (stale ~78d); FSK 41%; OBDC 5th decline — elevated but quarterly cadence | **No daily signal** (next read late-July Q2) |
| 5 | **Non-accrual / PIK trajectory** | Untouched | Rising | KBRA DLD >2.5% / Fitch BDC NAs rising further / PIK median >20% | KBRA 2.3% record-match; Fitch BDC NAs up Q1; PIK elevated (denominator effect) | **Bear, but not daily** (weekly/quarterly prints) |

**NET VERDICT (6/25): leaning MACRO.** The dominant tell (var 1, wrapper-vs-manager) is unambiguously macro — managers got hit, wrappers held, banks rallied. Only the faint CCC>HY dispersion (var 3) tilts credit, and it's small.

**SINGLE CLEANEST "now credit, not macro" TRIGGER:**
> The **wrapper basket (ARCC/FSK/OBDC/BIZD) starts LEADING the managers down** — on a down day APO/ARES hold or bounce while ARCC/FSK/OBDC/BIZD make new lows — **CONFIRMED by HY OAS breaking >280 sustained.**

That rotation (wrappers leading + spread breakout) is the credit-recognition signature. Until then it's multiple compression. **Watch vars 1 + 2 daily; vars 4/5 are quarterly anchors (next: late-July Q2 10-Q cycle, the Decision-Tree STEP-2 substance check).**

---

## PART 3 — X1: Shared-antecedent test (PC vantage; answered INDEPENDENTLY, not coordinated with SAM)

**Question:** is the alts/PC-manager multiple-compression (APO/ARES/BX) the SAME underlying trade as SAM's yen-carry-unwind risk — or genuinely independent? If shared, convergence between the PC signal and the carry signal collapses to ONE root, not two confirmations.

**(a) SHARED** — they share a dominant latent antecedent, with a PC-only idiosyncratic remainder.

**(b) Mechanism (if shared):** Both are **long-duration-of-cheap-funding / short-vol** trades.
- Yen carry = borrow cheap JPY → lever into higher-yield assets; unwinds when JGB yields rise / BOJ tightens / USDJPY reverses (funding cost up).
- PC-manager multiples = capitalized expectation of perpetual fee streams on AUM raised in a low-rate, abundant-liquidity world; compress when the discount rate rises and fundraising/realization slows.
- **Common root:** a single *higher-for-longer / real-rate + liquidity-withdrawal* shock (hawkish Fed dots 6/17 + firm PCE 6/25 + BOJ normalization) simultaneously raises carry funding cost AND de-rates high-multiple long-duration equity (alt-managers). **Today's APO/ARES selloff on firm PCE IS this shared antecedent firing.**

**(c) Decoupling test (the real discriminator):**
- **PC fires WITHOUT carry** = an idiosyncratic **credit-substance** event — marquee BDC forced sub-90¢ markdown / dividend-cut cascade / National-Dentex-style PIK→default conversion / bank PC-warehouse loss disclosure — that craters BDC NAVs and PC-wrapper equity WHILE USDJPY/JGBs stay calm.
- **Carry fires WITHOUT PC** = a sharp BOJ hike / USDJPY snap forcing global deleveraging + VIX spike, while PC credit fundamentals (gates, non-accruals) hold — a liquidity mark-down that mean-reverts.

**Convergence implication:** when PC-manager equity and yen-carry move TOGETHER on a macro day (like 6/25), treat as **~1 root — discount the "two-signal" confirmation ~50%.** It is a genuinely independent 2nd confirmation ONLY when PC fires via the credit-substance leg. **B1's "wrapper-leading + HY OAS >280" trigger ≡ the decoupling marker** — it is the same test for whether PC has separated from the macro/carry root.

---

*Cross-refs: TRADE.md §4 (APO position) · SCRATCH.md WATCH ORDER + Tier-4 housekeeping · STATUS.md LIVE TAPE (6/18, now stale vs this 6/25 read) · LESSONS #15 (tape compresses without substance reversal) · [[finding_shared_antecedent_independence_test]] · [[finding_catalyst_path_decoupling]].*
