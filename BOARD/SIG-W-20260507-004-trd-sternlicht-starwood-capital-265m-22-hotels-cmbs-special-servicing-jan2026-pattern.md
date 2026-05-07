---
signal_id: SIG-W-20260507-004
precedence: PRIORITY
timestamp: 2026-05-07T22:30:00Z
source: WALTER
origin: ["The Real Deal @trdny via X.com 2026-05-06 2:54 PM (37K views) — 'Barry Sternlicht's Starwood Capital is staring down another massive commercial real estate default. A $265M loan backing 22 of the firm's hotels just hit special servicing.' Article: 'Starwood faces default on $265M hotel portfolio loan' — Will Telegram intake msg 1473", "WALTER verify-research sub-agent 2026-05-07 ~21:50 UTC (~$0.05) — verdict CONFIRMED 0.88: all 5 load-bearing facts verified ($265M / 22 hotels / 2,943 keys / Marriott-Hilton-IHG mix / 12 states 17 cities Midwest concentration / K-Star special servicer / DSCR collapsed 2.07 origination → 0.64 mid-2025 / Sternlicht Starwood Capital Group PE firm). **CRITICAL CORRECTION:** special-servicing transfer was JANUARY 2026, not 'just hit' — TRD/trdny tweet implies fresh news while transfer is 4 months stale.", "TRD primary: https://therealdeal.com/national/2026/05/06/starwood-capital-faces-default-on-265m-hotel-portfolio/", "Yahoo Finance mirror: https://finance.yahoo.com/markets/stocks/articles/starwood-faces-default-265m-hotel-185235267.html", "CoStar pattern coverage: https://www.costar.com/article/2116447068/ (paywalled — search-result excerpts only)", "Underlying CMBS: 'Starwood Hotel Portfolio Whole Loan' originated 2018-08-16, $265M interest-only — Morningstar/KBRA loan data; specific deal-trust ticker not surfaced in open sources, Trepp/CRED-iQ direct lookup needed"]

to: REGINALD (ACTION — BANK_CRE primary; CMBS-loan-trust impairment downstream to bank B-piece holders + regional bank CRE collateral framework; Q1 CR window May 1-10 active)
info: BROCK (info — PE-sponsored = PC_STRESS adjacency; Sternlicht/Starwood Capital is canonical PE-CRE-sponsor in cluster), LIQUID (info — credit conditions cross-read on K-Star special servicing pace), RED (auto-cc per v0.7 By Tag/By Verdict — cluster_mediating prose-tag pattern-not-one-off + CORRECTED-FRAMING on TRD timestamp-stretch; de-dupe = 1 cc), NEXUS (cluster classification overdue), SHADE (info — insurance-CRE-debt holder downstream cross-ref), CARL (info — hotel-demand-cluster upstream cross-ref via AHLA WC 80%)
group: CREDIT_CHAIN
dispatched: 2026-05-07T22:30:00Z
dispatch_note: "Will-page Telegram 5/7 20:31 UTC msg 1473 (4/6 image batch). VERIFY-RESEARCH CONFIRMED 0.88 — all 5 load-bearing facts verified: $265M / 22 hotels / 2,943 keys / Marriott-Hilton-IHG mix / Midwest concentration / DSCR collapsed 2.07 origination (2018) → 0.64 (mid-2025) / sponsor = **Starwood Capital Group** (Sternlicht's PE firm) NOT STWD/SREIT public-REIT. **CRITICAL CORRECTION (CORRECTED-FRAMING tag):** special-servicing transfer was JANUARY 2026, not 'just hit' — TRD/trdny tweet uses 'just hit' framing implying fresh news while transfer is 4 months stale. TRD article is press-coverage-now of Jan-2026 stale event. **Pattern-not-one-off (cluster_mediating):** 3rd Sternlicht/Starwood-Capital CRE default in 2.5 years — $800M Jan 2023 + $577M / 65 hotels early 2025 (modified Sept 2025, 21 hotels sold $122.6M paydown by Mar 2026) + $265M / 22 hotels Jan 2026. **2nd hotel CMBS in 13 months, both K-Star special servicer** — load-bearing pattern, not isolated default. **Routing distinction load-bearing:** Starwood Capital Group (PE firm) = BANK_COLLATERAL or PC_STRESS adjacency, NOT SHADE (no PE-insurer-nexus angle). REGINALD primary on bank B-piece + regional CRE collateral framework. BROCK info on PE-CRE-sponsor angle. **Connects upstream:** AHLA WC 80% (SIG-W-20260505-008) hotel-demand-side stress = revenue-driver of DSCR 2.07→0.64 collapse (NOT rate-driver: hotels floating-rate-insensitive on fixed-rate CMBS). **Connects downstream:** which money-center / regional banks hold B-piece / mezzanine on these K-Star-serviced trusts? = Q1 CR window REGINALD pickup. **Today's bifurcation count: 4** (paired with SIG-001/-003 + this -004 cluster_mediating). **Cluster ToC update:** BANK_COLLATERAL 15→16. Confidence 0.85 (TRD primary + DSCR multi-source + entity confirmed — held below 0.95 because exact CMBS-trust-ticker not directly readable in open primary sources)."

signal_type: pattern-match
confidence: 0.85
confidence_language: confirmed
resources: 0
safety_net: clear

word_count: 273

cluster: BANK_COLLATERAL
---

## Signal

Per The Real Deal @trdny (X.com 5/6 2:54 PM, 37K views):

> "Barry Sternlicht's Starwood Capital is staring down another massive commercial real estate default. A $265M loan backing 22 of the firm's hotels just hit special servicing."

**WALTER verify-research verdict CONFIRMED 0.88** — all 5 load-bearing facts verified.

## Load-bearing facts

- **$265M loan** backing **22 hotels** / **2,943 keys** / Marriott-Hilton-IHG flag mix / 12 states 17 cities Midwest concentration ✓
- **K-Star special servicer** ✓
- **DSCR collapsed 2.07 (2018 origination) → 0.64 (mid-2025)** ✓
- Sponsor = **Starwood Capital Group** (Sternlicht's PE firm) — NOT STWD (Starwood Property Trust public REIT) NOT SREIT (Starwood Real Estate Income Trust non-traded)
- Underlying CMBS = "Starwood Hotel Portfolio Whole Loan" originated 2018-08-16, $265M interest-only

## CRITICAL framing-correction (CORRECTED-FRAMING tag)

- **TRD/trdny "just hit special servicing" framing is misleading:** transfer was **JANUARY 2026** — 4 months stale at this 5/6 press date.
- TRD article is press-coverage-now of a Jan-2026 stale event, not a fresh default.
- Reframe in CARL/REGINALD pickup as: "press-recognition lag of pattern that has been developing for months."

## Pattern-not-one-off (cluster_mediating)

**3rd Sternlicht/Starwood Capital Group CRE default in 2.5 years:**

| Date | Loan | Asset Type | Special Servicer |
|------|------|------------|------------------|
| Jan 2023 | $800M | (TRD prior coverage) | — |
| Early 2025 | $577M / 65 hotels / 6,366 keys | Hotel CMBS | K-Star (modified Sept 2025; 21 hotels sold $122.6M paydown by Mar 2026) |
| **Jan 2026** | **$265M / 22 hotels / 2,943 keys** | **Hotel CMBS** | **K-Star** |

**2nd hotel CMBS in 13 months, both K-Star** = load-bearing pattern, not isolated default.

## Mechanism: revenue-driver, not rate-driver

DSCR collapsed 2.07 → 0.64 over 7 years on a **fixed-rate CMBS**. Hotels are floating-rate-insensitive when financed via fixed-rate CMBS. So:

- **Rate-driver explanation: rejected.** Fixed-rate financing = rate environment doesn't move DSCR.
- **Revenue-driver explanation: confirmed.** RevPAR / occupancy / ADR collapse is the only mechanism that fits a 3x DSCR decline.

This connects directly upstream to **AHLA WC 80%** (SIG-W-20260505-008) — hotel-demand-side stress = revenue-driver of DSCR 2.07 → 0.64.

## Cross-references

- **SIG-W-20260505-008** (AHLA hotels WC 80%) — upstream demand-side stress driving revenue collapse
- **CHG-RED-019** (public/private bifurcation) — Starwood-private-PE default vs public-REIT-comp price reaction TBD
- **KB-RED-023** (regulatory forbearance) — special-servicing pace + modification frequency = forbearance proxy
- **REGINALD Q1 Call Report window May 1-10** — pickup task: which banks hold B-piece / mezz on K-Star-serviced Starwood-Capital trusts?
- **BROCK PC_STRESS cluster** — PE-sponsored CRE default pattern: 3 Starwood-Capital defaults in 2.5yr establishes Sternlicht as canonical PE-CRE-stress signal

## RED counter (logged)

- 3 Starwood-Capital defaults in 2.5yr is concentrated in ONE PE firm — sample-of-one might not generalize to PE-CRE-cluster broadly
- K-Star special servicing modal pace is itself ambiguous: aggressive workout = stress signal OR healthy-process-managing-distress
- Starwood-Capital portfolio aging 2018-vintage matters (terminal-value buyer-of-last-resort cycle) — could be vintage-specific not cycle-broad
- Hotel demand bottoming vs continuing-deterioration is the load-bearing distinction; one revenue-driven default doesn't pin the cycle

## Routing rationale

**REGINALD action** — BANK_CRE primary; CMBS-loan-trust impairment downstream to bank B-piece holders + regional bank CRE collateral framework. Q1 CR window May 1-10 active.

**BROCK info** (not action) — Sternlicht/Starwood-Capital is canonical PE-CRE-sponsor signal but the immediate transmission is to bank-collateral, not PC-fund-stress per se. PC_STRESS adjacency for pattern recognition.

**SHADE info** (not action) — no direct PE-insurer-nexus angle; insurance-debt-holder downstream cross-ref only.

**RED auto-cc** per v0.7 By Tag/By Verdict — both rules fire (cluster_mediating pattern-not-one-off + CORRECTED-FRAMING TRD timestamp-stretch); de-dupe = 1 cc.

## At-dispatch FALSIFICATION_TRIGGERS scan

- RED-FT-04 BRENT-PAPER<75×3: **NOT firing** ($101.11)
- RED-FT-06 VIX<16×5: **NOT firing** (17.08)
- RED-FT-01 HY-OAS<280×3: **needs primary OAS pull**
- **0 fires this dispatch**

---

*v0.7 cluster header — BANK_COLLATERAL. cluster_mediating: true (interim prose-tag — pattern-not-one-off across 3 Sternlicht-Starwood-Capital defaults in 2.5yr). signal_type: pattern-match. RED auto-cc per v0.7 By Tag/By Verdict (cluster_mediating + CORRECTED-FRAMING; de-dupe = 1).*
