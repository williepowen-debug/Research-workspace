---
id: SIG-W-20260511-038
date: 2026-05-11
origin: WALTER image-batch 2026-05-11 — @kshaughnessy2 X-post citing WSJ; verify-research confirmed CNBC + Bloomberg + Stocktitan + Investing.com primaries
domain: PRIVATE_CREDIT
cluster: PC_STRESS
cluster_secondary: BANK_COLLATERAL
signal_type: catalyst
precedence: IMMEDIATE
confidence: 0.85
to: REGINALD
info: [BROCK, RED, LIQUID, Will, SHADE]
signal_role: cluster_mediating
event_window: closed
verify_research_verdict: CORRECTED-FRAMING
mark_context: FSK $10.76 -0.74% session-close 2026-05-11
---

# FSK (FS KKR Capital) Q1 2026 — $560M Loss / NAV -9.9% / JPM Cut $648M Credit Facility / $300M Sponsor Backstop = 3rd KKR-Vehicle in Concurrent Stress

**Verbatim claim (verified):** FS KKR Capital Corp (NYSE: **FSK**) Q1 2026 (period ended 3/31/2026):
- **$560M ~$2/share realized + unrealized losses**
- **NAV/share $20.89 → $18.83 (-9.9% QoQ)**
- **Nonaccruals 8.1% at amortized cost / 4.2% at fair value** (up from 3.4% FV Q4'25)
- **Moody's downgraded FSK to junk March 2026** (CONFIRMED via Bloomberg 2026-03-23)
- **JPM-led bank group CUT FSK credit facility by $648M (~14%)** + raised borrowing cost, days before sponsor backstop announcement
- **$300M sponsor backstop:** $150M cumulative convertible perpetual preferred (5% cash / 7% PIK, conversion at $18.83 NAV, 3yr redemption) + $150M fixed-price tender at $11.00/share; plus separate $300M board buyback authorization through Jun-2027 + 50% incentive-fee waiver / 4 quarters
- **Share price -23.2% YTD / -35.5% TTM** (premarket $10.57 / 52wk-low $9.72 / current $10.76 -0.74%); **price-to-NAV 44% discount**

**Source primaries:**
- CNBC (JPMorgan reins in FSK credit line 5/11/2026) — https://www.cnbc.com/2026/05/11/kkr-private-credit-fund-fsk-jpmorgan-chase-credit.html
- Stocktitan (FSK Q1 2026 results + $300M buyback) — https://www.stocktitan.net/news/FSK/fs-kkr-capital-corp-announces-first-quarter-2026-results-and-qnjwfrnvim9w.html
- Investing.com (FSK Q1 2026 NAV drops 9.9%) — https://www.investing.com/news/company-news/fs-kkr-capital-q1-2026-slides-nav-drops-99-strategic-actions-unveiled-93CH-4677172
- Bloomberg (FSK junk downgrade 2026-03-23) — https://www.bloomberg.com/news/articles/2026-03-23/private-credit-fund-run-by-future-standard-and-kkr-cut-to-junk-by-moody-s
- WSJ (KKR $560M loss + $300M backstop) — referenced via @kshaughnessy2 image (5/11/2026 11:10 AM)

## Substance

- **Vehicle correction**: kshaughnessy2's "regular investors" framing is technically loose — **FSK is a NYSE-LISTED BDC** (publicly traded), NOT a non-traded interval/tender-offer retail vehicle like KREST/BCRED/BXSL. Retail-accessible via stock market but not the closed-end-redemption-restricted structure.
- **$560M loss CONFIRMED** — Q1 2026 quarter-end 3/31/2026, $2/share realized+unrealized vs ~$12.3B portfolio.
- **8.1% default rate CORRECTED-FRAMING** — that's nonaccruals at amortized cost; **at fair value (cleaner metric) = 4.2%**, up from 3.4% Q4'25. Both moved (5.5%→8.1% cost / 3.4%→4.2% FV). X-post cherry-picks higher cost-basis without disclosure — directionally accurate (deterioration is real) but headline overstates 2× vs FV.
- **"Share price cut in half" CORRECTED-FRAMING** — actual is -23.2% YTD / -35.5% TTM. Closer to "one-third off recent peak." However **price-to-NAV discount 44%** (current price $10.76 vs NAV $18.83) is the "cut in half" framing if conflating price with NAV.
- **JPM credit-facility cut CONFIRMED** — $648M (~14%) reduction days before sponsor injection. Bank-funding-strain in BDC chain confirmed.
- **$300M sponsor backstop is 6× KREST's $50M and structurally deeper** — KKR injecting preferred equity (not just share-purchase) into FSK. Materially more capital commitment vs prior KKR backstop signal.

## Dispatch notes

**3rd KKR-vehicle in concurrent stress this session — sponsor-bifurcation pattern hardens:**
1. **KREST** (SIG-W-20260511-010) — non-traded REIT, Q1 81% proration + $50M sponsor backstop
2. **KREF** (SIG-W-20260511-025) — mREIT, 60% dividend cut + BV -9% + 0.53× BV
3. **FSK** (this signal) — listed BDC, $560M loss + JPM credit cut + $300M sponsor backstop

Blackstone counter-evidence remains clean (BREIT NET INFLOWS Q1 +$1.2B 3-yr high per deep-dive batch). KKR-side concentration of stress vs Blackstone-side calm = **sponsor-bifurcation thesis 3-of-3 KKR vehicles HARDENED.**

**NON_TRADED_REIT_DISTRESS sub-cluster proposal sharpened** — original proposal scoped to KKR + Starwood pair (sub-cluster within BANK_COLLATERAL). FSK addition expands the KKR-side from 2 named vehicles (KREST + KREF) to 3 (KREST + KREF + FSK). Sub-cluster framing should evolve to **KKR-FRANCHISE_STRESS** (not specifically non-traded-REIT) since FSK is a listed BDC, not a non-traded REIT. Possibly: combine into broader **SPONSOR_BIFURCATION** sub-cluster spanning PC_STRESS + BANK_COLLATERAL + PE-credit-stack.

**`cluster_mediating: true`** — sponsor-franchise concurrent stress is the framework-level signal (bridges PC_STRESS + BANK_COLLATERAL + sponsor-affiliated-fund-stress + bank-funding-strain via JPM credit cut). CORRECTED-FRAMING on nonaccrual basis + share-price magnitude — auto-cc RED per By Tag/By Verdict rule.

**Bank-funding-strain transmission alert:** JPM cutting FSK's credit facility by 14% days before KKR was forced to inject $300M is a discrete transmission step on bank-PC-lending fragility — REGINALD primary attention vector (warehouse/credit-line cuts to BDCs flow back into bank NDFI exposure measurement).

## Recipient routing

- **REGINALD action** — bank-funding-strain primary (JPM credit cut to FSK is BANK-CRE-PC-bridge transmission); NDFI 5-cat schema 4/15 CDR pickup.
- **BROCK info** — PC_STRESS primary; sponsor-bifurcation pattern owner; FSK addition to KKR-vehicle count.
- **RED info** — cluster_mediating + CORRECTED-FRAMING auto-cc (de-duped).
- **LIQUID info** — bank-PC-credit-facility-cut → HY OAS forward-pressure context; current OAS 281 near RED-FT-01 floor.
- **Will via Telegram** — bear-thesis-extending material; sponsor-bifurcation now 3-of-3 KKR-side.
- **SHADE info** — PE-insurer nexus + insurance-asset BDC exposure context.
