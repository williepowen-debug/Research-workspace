---
id: SIG-W-20260511-040
date: 2026-05-11
origin: WALTER image-batch 2026-05-11 — WSJ X-post (5/10 8:43 PM); verify-research confirmed MFIC 8-K + Reuters wire + Investing.com primaries
domain: PRIVATE_CREDIT
cluster: PC_STRESS
cluster_secondary: BANK_COLLATERAL
signal_type: catalyst
precedence: IMMEDIATE
confidence: 0.85
to: BROCK
info: [REGINALD, RED, LIQUID, Will, SHADE, OTTO]
signal_role: cluster_mediating
event_window: closed
verify_research_verdict: CORRECTED-FRAMING
mark_context: MFIC $11.10 -4.97% / APO $130.46 -2.06% session-close 2026-05-11
---

# Apollo MFIC Q1 2026 — $61M Realized+Unrealized Loss / Defaults 3.9%→5.3% / Apollo Shopping $3B-Portfolio MFIC Itself to Sell

**Verbatim claim (verified — MFIC 8-K + WSJ-derived reporting):**

**Apollo MidCap Financial Investment Corp (NASDAQ: MFIC) Q1 2026 (period ended 3/31/2026):**
- **$61.1M realized+unrealized losses** ($0.67/share — NOT total net P&L; NII of $34.3M / $0.38/sh OFFSET markdowns; net decrease in net assets from operations = $26.9M)
- **NAV/share $14.18 → $13.82 (-2.5% QoQ)**
- **Default rate 5.3% Q1'26 vs 3.9% Dec 2025 = +140bps in one quarter**
- Realized+unrealized loss line: -$0.67/sh Q1'26 vs -$0.05/sh Q1'25 = **13× YoY deterioration on markdown line**
- NII (Net Investment Income) of $34.3M / $0.38/sh **covered the $0.31/sh dividend** — operations stable, capital-account deteriorating

**Apollo separately shopping a "$3B private credit fund":**
- **The $3B fund Apollo is selling IS MFIC itself** (not a separate Apollo PC fund) — Apollo shopping its captive listed BDC at ~$3B portfolio value to another BDC
- **Stock at $0.85/$1 NAV** (current $11.10 vs NAV $13.82 = 80% of NAV)
- **Redemptions equivalent to 11% of shares last quarter**
- **Lending "largely halted"** per WSJ
- Apollo cited "increasingly difficult to operate" as rationale

**Source primaries:**
- MFIC 8-K (Q1'26 release) — https://www.stocktitan.net/sec-filings/MFIC/8-k-mid-cap-financial-investment-corp-reports-material-event-827ca9b67216.html
- Reuters wire (Apollo $3B PC fund sale talks) — https://m.investing.com/news/stock-market-news/apollo-in-talks-to-sell-3-billion-private-credit-fund-wsj-reports-4674888
- InvestingLive WSJ-derived (rising defaults + redemption pressure) — https://investinglive.com/stock-market-update/wsj-rising-defaults-and-redemption-pressure-push-apollo-to-weigh-3bn-credit-fund-sale-20260511/

## Substance

- **$61M FIGURE FRAMING CORRECTION** — WSJ X-post says "$61 million loss" without disclosing this is the realized+unrealized-losses LINE, not total P&L. NII covered the dividend; net decrease was $26.9M (still negative but materially smaller). For dispatch hygiene: cite both numbers.
- **13× YoY deterioration on markdown line** is the more important signal than the absolute $61M — pace-of-acceleration matters more than level.
- **Defaults +140bps in one quarter** — 3.9% → 5.3% acceleration tracks the same direction as FSK (3.4% FV → 4.2% FV) but at a slightly slower base rate.
- **Apollo exiting captive listed BDC during defaults-spiking phase** — Apollo offloading MFIC at $0.85/NAV. This is one stage further along the BDC-stress curve than:
  - OBDC SIG-W-20260511-009 (NAV compression + dividend cut, no parent-exit signal)
  - FSK SIG-W-20260511-038 (NAV -9.9% + sponsor BACKSTOP, not parent-exit — KKR doubled down)
  - **MFIC pattern = Apollo CASHING OUT**, KKR pattern (FSK) = sponsor DOUBLING DOWN. Different strategic responses.
- **vs FSK $300M sponsor backstop:** Apollo *not* injecting capital — instead pursuing portfolio sale. Material divergence in sponsor strategy at the BDC-stress-curve inflection point.

## Dispatch notes

**`cluster_mediating: true`** — bridges PC_STRESS (BDC stress) + BANK_COLLATERAL (default acceleration) + sponsor-strategy bifurcation (Apollo-cash-out vs KKR-double-down) + APO-parent-implication (Apollo offloading captive listed BDC during stress is concerning signal at the parent level too).

**CORRECTED-FRAMING on $61M number framing** — auto-cc RED per By Tag/By Verdict rule (de-duped with cluster_mediating).

**Pattern context — 3 BDC vehicles now in named stress this session:**
1. **OBDC** (SIG-009) — dividend cut, NAV compression
2. **FSK** (SIG-038) — $560M loss + sponsor injection
3. **MFIC** (this signal) — $61M markdowns + Apollo parent-exit signal

**Sponsor-bifurcation pattern broadens beyond just KKR/Starwood — Apollo joining as 3rd named sponsor with active stress signals.** BROCK STAGE 2 PERSISTS framework gets a fresh primary-data input (APO breaching $130 ties to Apollo parent risk from MFIC exit signal, not just APO capital structure).

**Apollo-as-cash-out vs KKR-as-double-down** is the load-bearing finding for sponsor-strategy framework — when stress hits, sponsors choose: inject more capital (KKR vehicles) or exit (Apollo MFIC). The choice tells you the sponsor's read on how-much-more-stress is coming.

**Mark-context at intake:** MFIC closed $11.10 -4.97% TODAY; APO $130.46 -2.06%; both materially down session — market already pricing significant stress.

## Recipient routing

- **BROCK action** — PC_STRESS + BDC + Apollo cohort primary; STAGE 2 PERSISTS framework input.
- **REGINALD info** — bank-NDFI exposure to Apollo-affiliated PC ($128B → $1.4T NDFI framework correction context); BDC default acceleration cross-feed.
- **RED info** — cluster_mediating + CORRECTED-FRAMING auto-cc (de-duped).
- **LIQUID info** — bank-PC-credit-spread context.
- **Will via Telegram** — sponsor-bifurcation expanding beyond KKR; Apollo MFIC exit signal is material new vector.
- **SHADE info** — PE-insurer nexus + Apollo-Athene Apollo-as-parent context.
- **OTTO info** — subprime-auto-ABS PE-credit cross-feed (Apollo is heavy in auto-related ABS).
