---
id: SIG-W-20260511-031
date: 2026-05-11
origin: WALTER image-batch 2026-05-11 — @ALikhodedov X-post citing Reuters (Arathy Somasekhar, 2026-05-08 15:05 ET); verify-research confirmed primary
domain: OIL_ENERGY
cluster: POSITIONING_VALUATION
cluster_secondary: OIL_ENERGY
signal_type: positioning-extreme
precedence: PRIORITY
confidence: 0.70
to: BRENT
info: [RED, HENRY, CARL, HAWK, SAM]
signal_role: cluster_mediating
event_window: closed
verify_research_verdict: CORRECTED-FRAMING
---

# Diamondback (FANG) Buys ~$70M Puts on WTI-Brent Spread — Q2 -$41.67 / Q3 -$42.76, First Basis-Put Since 2022

**Verbatim claim (verified):** Diamondback Energy (top Permian-Basin-only producer; 521 kbpd oil Q1 2026; Midland HQ) bought ~$70M of put options to hedge the WTI-Brent spread: **255,000 bpd at -$41.67/bbl in Q2 2026** + **290,000 bpd at -$42.76/bbl in Q3 2026**. First time FANG has used basis-put hedging since 2022.

**Source primaries:**
- Reuters (Arathy Somasekhar, 2026-05-08 15:05 ET) — https://www.investing.com/news/commodities-news/diamondback-bets-on-wider-wtibrent-gap-amid-us-export-ban-concerns-4673861
- EnergyNow syndication (5/11 repost) — https://energynow.com/2026/05/diamondback-bets-on-wider-wti-brent-gap-amid-us-export-ban-concerns/
- FANG Q1 2026 earnings release (Permian-Basin-only confirmation) — https://www.globenewswire.com/news-release/2026/05/04/3287116/22886/en/Diamondback-Energy-Inc-Announces-First-Quarter-2026-Financial-and-Operating-Results-Increases-Base-Dividend-and-Production-Guidance.html

## Substance

- **Volumes + strikes + premium all confirmed verbatim** vs the Reuters primary. ($70M premium / Q2 255K@-41.67 / Q3 290K@-42.76; spread reference WTI minus Brent.)
- **First basis-put deployment since 2022** — FANG's last analogous hedge predates the post-COVID demand recovery; multi-year regime change in their hedging posture.
- **Top Permian-Basin-only producer** confirmed — FANG operates exclusively in the Permian, third-largest Permian operator after XOM/CVX (both multi-basin).
- **Rationale ATTRIBUTED, not stated:** Reuters explicitly notes: *"Diamondback declined to comment and has not publicly disclosed the reason for the hedge."* The export-ban thesis is provided by Tim Skirrow (Energy Aspects) as analyst-interpretation, not FANG's stated reason.

## Dispatch notes

**CORRECTED-FRAMING on rationale attribution.** The X-author's gloss — "they are hedging against some fairly radical implementation" — is NOT supported by FANG-stated reasoning. The export-ban thesis carrier is Tim Skirrow (Energy Aspects), not FANG. Two thesis branches both fit the data: (a) export-restriction risk hedge (Skirrow), (b) general WTI-discount-widening from Permian glut + pipeline capacity vs Gulf Coast loading; FANG hasn't disclosed which. Trump admin opposes export ban; a Democratic congressman has proposed a bill. Confidence dropped to 0.70 reflecting attribution-uncertainty.

**`cluster_mediating: true`** — positioning-extreme (corporate hedger at $70M-scale basis-put, first since 2022) × oil-market-microstructure (WTI-Brent spread at -$42 strikes is materially wider than recent realized) × policy-risk-vector (export-ban legislative trajectory). Bridges POSITIONING_VALUATION (corporate-hedger-as-sentiment-tell) ↔ OIL_ENERGY (basis spread implies expectations on Permian-to-Gulf-Coast bottlenecks OR export policy) ↔ regulatory-cluster (Democratic legislative initiative + Trump admin pushback on export bans).

**Reuters publication date 5/8, not 5/11** — image is X-amplification 3 days post-primary. The signal is fresh-enough (3d) for dispatch but not breaking; PRIORITY rather than IMMEDIATE.

## Recipient routing

- **BRENT action** — energy primary (HAWK STALE 21d, BRENT acting per backup promotion).
- **RED info** — cluster_mediating + CORRECTED-FRAMING auto-cc per ROUTING_TABLE v0.7 By Tag/By Verdict rules.
- **HENRY info** — positioning-extreme dimension (corporate hedger at $70M-scale = sentiment signal in HENRY domain).
- **CARL info** — export-restriction policy-vector if it materializes is consumer-pump-pass-through downstream.
- **HAWK info** — Permian export-bottleneck context for kinetic-doctrine framing.
- **SAM info** — Brent vs WTI spread mechanics tie to USD strength and Asia-bound flow.
