---
signal_id: SIG-W-20260526-002
precedence: PRIORITY
timestamp: 2026-05-26T22:40:00Z
source: WALTER
origin: "Will Telegram image-batch msg 2019 (Financelot @FinanceLancelot X post on AZO -8.94% / $3,102.01); verify-research sub-agent cross-checked CNBC + Motley Fool + CoinCentral + SEC 8-K exh 99.1 + AZO investor materials"

to: CARL (ACTION)
info: REGINALD, LABOR, BROCK, RED, HENRY, NEXUS, PROME

signal_type: counter_evidence
confidence: 0.55
confidence_language: confirmed_with_corrected_framing
resources: $0.05 (1 verify-research sub-agent)
safety_net: clear

word_count: ~360

cluster: CONSUMER_STAGFLATION
cluster_secondary: POSITIONING_VALUATION
signal_role: counter_evidence
event_window: closed

verify_research_verdict: CONFIRMED-on-magnitude-with-CORRECTED-FRAMING-on-historical-context-and-catalyst-attribution. (1) Magnitude: post claimed -8.94% / $3,102.01 close; verified close was -8.99% to $3,100.11 (Motley Fool); intraday -9.6% to -11.7%; rounding-precision difference only. (2) "Worst single day since March 2020" claim is **FALSE** — actual is "worst since May 18, 2022 (-9.5%)"; ~4 years not 6. CNBC itself updated its headline from "March 2020" to "May 2022" — the original framing was wrong. (3) **Catalyst attribution is CORRECTED-FRAMING**: the X post framed the sell-off as "slowing economy concerns" sparked by "better than expected earnings." Verify-research surfaced the actual proximate drivers: (a) gross margin -57bps YoY (52.2% vs 52.77%), (b) international SSS softness (+1.6% int'l vs +4.1% domestic; Mexico/Brazil weak), (c) ~$30M LIFO headwind / ~$1.40 EPS guidance hit, (d) revenue $4.84B vs ~$4.86-4.87B est = small miss. The headline beat ($38.07 EPS vs ~$36.18) is real but margin compression + international softness + LIFO guide is the actual punishment vector — NOT a pure-macro consumer-stagflation read.

mark_context: AZO trades regular-session-close $3,100.11 = -8.99% on 5/26 (today). Earnings reported pre-market 5/26. Fiscal Q3 2026 print; FY ends August. Domestic comp +4.1% strong; the weakness is international + margin + LIFO guide. Filing source: SEC 8-K exh 99.1.
---

# AutoZone (AZO) FY26-Q3 Beat-and-Sold-Off -8.99% — CORRECTED-FRAMING on Historical Context + Catalyst Attribution (Actually Worst Since May 18 2022 NOT March 2020; Drivers Are Margin Compression -57bps + International SSS Softness Mexico/Brazil + LIFO Guide-Down NOT Pure-Macro Consumer Stagflation)

**Event (AZO FY26-Q3 earnings 2026-05-26 pre-market):**

- **AZO -8.99% to $3,100.11** on the day (X post's -8.94% / $3,102.01 is to-rounding correct)
- **Intraday low -9.6% to -11.7%** (CoinCentral / CNBC intraday tracking)
- **EPS beat:** $38.07 vs ~$36.18 est (beat by ~$1.90)
- **Revenue small miss:** $4.84B vs ~$4.86-4.87B est (~-$20-30M; +8.4% YoY)
- **Domestic SSS:** +4.1% (strong)
- **International SSS:** +1.6% constant-currency (Mexico/Brazil weak)
- **Gross margin:** 52.2% vs 52.77% YoY = **-57 bps** (compression)
- **LIFO guide-down:** ~$30M / ~$1.40 EPS headwind flagged

## CORRECTED-FRAMING #1 — "Worst single day since March 2020" is FALSE

Actual is **"worst single-day drop since May 18, 2022 (-9.5%)"** — roughly 4 years, not 6. CNBC's original headline ("...since March 2020") was UPDATED to "...since May 2022" — the source itself corrected. The Financelot X post is propagating the original-and-since-corrected CNBC framing. **Use "since May 2022" downstream.**

## CORRECTED-FRAMING #2 — Catalyst attribution

The X post framed this as "better than expected earnings...sparking concerns of a potential slowing economy." That **conflates** the headline beat with the punishment vector. Actual driver-mix:

1. **Margin compression -57bps YoY** = input-cost inflation eating gross margin. This IS a stagflation-relevant signal but **on the COST side, not the demand-destruction side.**
2. **International SSS softness** (Mexico +X / Brazil +Y both lagging +4.1% US) = international-consumer weakness, **not US consumer-demand destruction.** US domestic comp is strong.
3. **LIFO ~$30M / ~$1.40 EPS guide-down** = forward expectation of continued input-cost pressure.
4. **Revenue $20-30M miss** = small but on the wrong side of expectations.

Net: AZO punished for margin/international/LIFO, NOT for a US-demand-destruction read. Tape's "slowing economy" interpretation is the X post's overlay, not what the print actually delivered.

## Why dispatched as counter_evidence × CONSUMER_STAGFLATION

- **US-consumer-demand framing is the COUNTER-EVIDENCE.** Domestic SSS +4.1% on aftermarket-auto (defensive but discretionary-adjacent) does NOT support a US-demand-destruction stagflation read. The bear-thesis convergence on US-consumer-weakness in May (Freddie HPI YoY +0.7% / UMich May ~44 record-low / Phoenix BTR layoffs) gets a counter-data point from AZO domestic.
- **Cost-side stagflation framing is the CONFIRMING-EVIDENCE.** Margin -57bps + LIFO guide-down IS input-cost pressure printing in real-time. Mixed cluster value: bull-side on demand, bear-side on costs.
- **International-consumer-weakness is a NEW vector.** Mexico + Brazil softness has been latent in SAM (Japan-side) + HANS (EU-side) signals but not US-listed corporates. AZO's international SSS gap (1.6% vs domestic 4.1%) is a fresh data point on emerging-market-consumer weakness from a US-corporate lens.
- **POSITIONING_VALUATION secondary**: beat-and-sold-off is a positioning/expectations pattern (the market was positioned for a beat-AND-margin-stability; the margin print broke positioning). Useful HENRY input.

## Routing rationale

- **CARL ACTION**: consumer-transmission lens; domestic +4.1% is the load-bearing US-consumer counter-evidence; margin/LIFO is the cost-side stagflation confirmation; international softness is a new vector for CARL's stagflation framework.
- **REGINALD info**: aftermarket-auto / consumer-credit cross-read (AZO is auto-aftermarket, adjacent to Tricolor/subprime-auto cluster but different demand stratum).
- **LABOR info**: AZO is a wage-paying employer; comp pattern is a leading indicator for retail-employment-side stagflation.
- **BROCK info**: cost-inflation pressure on margin-sensitive corporates is an indirect PC-stress input (corporate-level margin compression → defaults).
- **RED info**: counter-evidence on the bear-thesis convergence; steelman input — domestic +4.1% is real bull substance worth weighing.
- **HENRY info**: beat-and-sold-off positioning pattern.
- **NEXUS info**: CONSUMER_STAGFLATION cluster narrative integration — does this mediating signal (cost-inflation YES, demand-destruction NO) shift the cluster framing?

## Forward watch

- **AZO international comp trajectory** — Mexico/Brazil weakness recurrence in next print (FY26 Q4 ~Sept 2026)
- **LIFO charge progression** — $30M Q3 → expected continuation per guide
- **Aftermarket-auto peer reads** — ORLY (O'Reilly Automotive) prints; AAP (Advance Auto Parts) prints; cross-confirm or diverge on margin / international / LIFO
- **US discretionary-adjacent peer reads** — defensive-discretionary cluster check

---

*Filed by WALTER 2026-05-26. counter_evidence × CONSUMER_STAGFLATION with POSITIONING_VALUATION secondary. CONFIRMED-with-CORRECTED-FRAMING 0.55 (calibrated per CORRECTED-FRAMING memory pattern — direction-confirmed-specifics-imprecise).*
