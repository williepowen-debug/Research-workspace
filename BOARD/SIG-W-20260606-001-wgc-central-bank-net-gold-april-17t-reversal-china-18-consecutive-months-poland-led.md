---
id: SIG-W-20260606-001
date: 2026-06-06
origin: Will Telegram 6/6 21:49 UTC msgs 2183+2184 — Kobeissi Letter @KobeissiLetter X post (~3h, "BREAKING: Global central banks acquired +17 tonnes of gold in April, the 2nd monthly purchase this year. Sharp reversal from March -30t driven by Turkey and Russia. Poland led +14t (YTD +45t, 595t reserves). China added +8t (biggest since Dec 2024; record 2,322t / ~9% of total reserves; 18 consecutive months). Central bank demand remains incredibly strong.") with WGC Chart 1 Jan'24 - Apr'26 monthly tonnes (gross purchases / gross sales / net); verify-research $0.05 agent_id ad7b3477992b17b5d — WGC Goldhub primary (Marissa Salim "Central banks resume net buying April" June 2026); WGC China gold update May 2026
domain: UST_FOREIGN
cluster: MISC
cluster_secondary: ASIA_CHINA
signal_type: threshold-crossed
precedence: PRIORITY
confidence: 0.85
to: BOND
info: [Will, LIQUID, ZHAO, NEXUS, RED, PROME]
signal_role: cluster_mediating
event_window: closed
verify_research_verdict: CONFIRMED
narrative_channel: n/a
---

# WGC: Central Banks Resume Net Gold Buying April +17t (2nd monthly purchase YTD); March -30t Reversal; Poland +14t YTD 45t / China +8t 18 Consecutive Months 2,322t Record

**Source:** Kobeissi Letter X post ~3h before dispatch citing IMF / respective central banks / World Gold Council. **Primary:** WGC Goldhub June 2026 post by Marissa Salim ("Central banks resume net buying in April"). Verify-research surfaced primary directly; Kobeissi framing matches WGC's data points but adds editorial overlay.

## Substance — verify verdicts

| Element | Verdict | Note |
|---------|---------|------|
| April 2026 net +17t | CONFIRMED | WGC: "central banks resumed net buying in April, having bought 17t" |
| 2nd monthly purchase YTD 2026 | CONFIRMED | March was a net seller month |
| March -30t | CONFIRMED | WGC primary corroborates |
| Turkey + Russia drove March sales | INDETERMINATE on Turkey attribution | WGC names Russia continuing as net seller (6t in April, 22t YTD); Turkey attribution for March specifically not directly visible in verify; Kobeissi framing is secondhand-on-driver |
| Poland +14t April / YTD +45t / 595t reserves | CONFIRMED | WGC; Poland top buyer April; NBP gold ~30% of reserves |
| China +8t April | CONFIRMED | WGC explicit |
| China "biggest since December 2024" | CONFIRMED | WGC explicit |
| China 2,322t cumulative reserves | CONFIRMED | PBoC official reserves |
| "China 18 consecutive months" | CONFIRMED | WGC explicit |
| "~9% of total reserves" | CONFIRMED-with-framing-precision | This is China-specific composition (gold as share of PBoC's FX+gold reserves), NOT global share — Kobeissi phrasing ambiguous; tighten when downstream agents quote |
| "Central bank demand incredibly strong" | EDITORIAL OVERLAY | WGC's actual characterization: "central banks stay the course" / "resumed net buying" — measured, not breathless. Strip the adjective for BOND read. |

## Why PRIORITY / cluster MISC primary / cluster_secondary ASIA_CHINA

- **De-dollarization-axis signal** at the central-bank-flows layer — distinct from prior gold-cluster dispatch (SIG-W-20260506-003 Gromen US gold-export #1-5-of-6-months CORRECTED-FRAMING, SIG-W-20260521-028 Gromen CIPS/renminbi golden window CORRECTED-FRAMING). Those were US-export and CIPS-volume mechanics; this is CB net-flow direction-confirmation.
- **MISC primary** because de-dollarization-axis doesn't have a dedicated cluster home; **cluster_secondary ASIA_CHINA** captures the China 18-consecutive-month + record-reserves load-bearing sub-story.
- **cluster_mediating**: ties to FED_FRAMEWORK (foreign-CB Treasury allocation declining as gold accumulating — cross-references SIG-W-20260606-002 Treasury rollover dispatched same session) + ASIA_CHINA cluster (China-specific monetary policy / reserve-composition shift).
- **PRIORITY not IMMEDIATE**: incremental monthly data point, not threshold-cross with immediate market impact. The "Russia continuing seller" detail adds nuance — not a clean "all CBs buying" narrative.

## Framing overlays for BOND dispatch

1. **Strip Kobeissi editorial** ("incredibly strong" / "sharp reversal"); use WGC's measured characterization ("resumed net buying" / "stay the course").
2. **Russia + China divergence remains**: Russia continuing net seller (6t April, 22t YTD per WGC) even as China extends 18-month streak — read as Russia-specific (war-financing FX-reserve drawdown) not CB-universe lean.
3. **Turkey-as-March-driver flag INDETERMINATE** — Kobeissi secondhand; BOND can pull WGC March country attribution if it matters for thesis.
4. **9% framing is China-specific composition** not global-CB share — downstream agents should not conflate.
5. **Cross-ref SIG-W-20260606-002 (same session)** — foreign-CB share of UST declining (TIC + Fed custody at lowest since 2016) while CB gold buying resumes; pair as composition-shift evidence not coincidence.

## Signal-role logic

- `signal_role: cluster_mediating` — bridges MISC (de-dollarization-axis) + ASIA_CHINA (China-specific) + FED_FRAMEWORK (UST-foreign-holder composition cross-reference via SIG-002 same session)
- `event_window: closed`
- `narrative_channel: n/a` (not Iran-cluster)

## What survives if specifics tighten

Even if Turkey-attribution proves wrong or "9%" framing gets corrected to global-share, the core load-bearing facts hold: **April net-buying resumed, China 18 consec months + record 2,322t, Poland top monthly + YTD buyer, Russia continuing seller.** These are WGC primary numbers and de-dollarization-axis-supportive regardless of editorial overlay.

Confidence 0.85 (verify-CONFIRMED with editorial-tone strip; minor INDETERMINATE on Turkey-March driver).
