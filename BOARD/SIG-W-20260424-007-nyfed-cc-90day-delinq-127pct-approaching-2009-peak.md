---
signal_id: SIG-W-20260424-007
precedence: PRIORITY
timestamp: 2026-04-24T23:02:00Z
source: WALTER
origin: "Will Telegram image 2026-04-24 22:55 UTC (msg 1036). Chart: 'Percent of balance 90+ days delinquent by loan type: credit cards' — time series 2003 through 2025. Y-axis 6% to 14%. Source line at bottom: 'Charles Schwab, New York Fed Consumer Credit Panel/Equifax, as of 12/31/2025.' Chart shows: pre-GFC range ~8-9%, 2009-10 peak ~13.8%, 2014-2016 trough ~7.1-7.3%, grind up 2017-2020 ~8-10%, brief 2020-21 decline during fiscal support, steady rise 2022-2025 reaching ~12.7% at 12/31/2025 endpoint. This is stock-measure (% of balance 90+ days delinquent), not flow-measure (quarterly transition rate)."

to: CARL (ACTION — CONSUMER_CREDIT / credit-card serious delinquency stock-measure approaching GFC peak)
info: REGINALD, BROCK, RED, HENRY, NEXUS, PROME
group: LABOR_DOWNSTREAM
dispatched: 2026-04-24T23:02:00Z
dispatch_note: "NY Fed Consumer Credit Panel / Equifax Q4 2025 data (released mid-Feb 2026): credit card balances 90+ days delinquent at ~12.7%, approaching but not yet at 2009-10 GFC peak ~13.8% = ~92% of peak level. Primary-grade, standard NY Fed series. Ship as PRIORITY — not NEW data (Q4 2025 is 2+ months old) but may not be in CARL's current convergence node count at this chart-level framing. CARL STATUS 2026-04-13 cites 51/55 convergence + student loan 9.2M + CMBS MF ATH 7.15% — the credit-card-90+-approaching-2009-peak frame is either already folded or a new channel. CARL to reconcile against internal count. REGINALD (CC-portfolio exposure at regional banks); BROCK (indirect consumer PC exposure); RED (adversarial — is 12.7% genuinely tracking to 2009-peak or plateauing?); HENRY (macro consumer-stress transmission); NEXUS (cluster integration). Phase 1.5 check: '92% of 2009 peak' framing is stock-level comparison — NOT a FHA-style count-vs-rate misframing; chart is clearly a rate series through time."

signal_type: thesis-confirmation
confidence: 0.85
confidence_language: reports
resources: 0
safety_net: clear — convergent with LABOR and BANK_CRE domains but not 2+ agents same theme in 24h

word_count: 470
---

## Signal

**NY Fed Consumer Credit Panel / Equifax Q4 2025: credit card balances 90+ days delinquent = ~12.7%.** Chart via Charles Schwab reproduction, data labeled "as of 12/31/2025."

Historical context from the series:
- Pre-GFC (2003-2007): ~8-9% range
- **2009-10 peak: ~13.8%**
- Mid-2010s trough (2014-2016): ~7.1-7.3%
- Grind higher 2017-2020: ~8-10%
- 2020-21 fiscal-support decline
- Steady rise 2022-2025 into current ~12.7%

Current level = **~92% of 2009-10 GFC peak**. First time the series has been within striking distance of GFC levels on the stock-measure. Flow-measure (NY Fed quarterly transition-into-serious-delinquency) also elevated; this signal focuses on the stock reading.

## Relevance

- **CARL (ACTION — CONSUMER_CREDIT):** Core domain. CARL STATUS 2026-04-13 enumerated 51/55 convergence nodes + student loans + CMBS MF ATH — the credit-card-90+-approaching-2009-peak stock-measure framing may or may not be in current node count. This signal provides a clean single-chart pillar for the framing. Cross-reference SIG-W-20260419-020 ATTOM Q1 foreclosure +26% YoY and SIG-W-20260419-015 NFIB Sub-V bankruptcies +67% — three stock-measures-at-or-near-GFC-peak on different credit categories.
- **REGINALD (info — BANK_CRE / CC-portfolio exposure):** Regional-bank credit-card books (smaller vs Citi/JPM/BAC but real) face stock-level loss curves if 12.7% holds/extends. Not OZK-specific today, but industry-wide ACL assumption input.
- **BROCK (info — PRIVATE_CREDIT indirect):** Consumer-PC exposure (asset-backed lenders, non-bank CC issuers in PC portfolios, subprime consumer via Marlette/Sofi/Upstart-adjacent) bleeds from industry-wide CC stress. Bridges to SIG-W-20260419-001 Tricolor/MTB auto-subprime.
- **RED (info — adversarial):** Is 12.7% tracking to 13.8% peak or plateauing? Bull case: 12.7% may be cyclical peak absent a recession-catalyst (fiscal support baseline still elevated vs pre-GFC, and 2009-10 peak had unemployment 10% — we're at 4.4%). Bear case: if unemployment rises +1-2pp (see SIG-W-20260424-001 FL-LABOR cracking), 2009-peak is reachable. RED should present the unemployment-level asymmetry directly.
- **HENRY (info — macro):** Consumer stress input for Fed-expectations model. Fed cuts calculus includes employment-side (strong) and consumer-credit-side (stressing) asymmetry. NFP primary > CC secondary in Fed reaction function, but CC shows up in UMich/conference-board consumer-confidence feedback.
- **NEXUS (info — cluster integration):** CONSUMER_CREDIT pillar addition to stress cluster. Pairs with LABOR side + BANK_CRE side. NEXUS classification update pending (stale 11d+).
- **PROME (info):** Coordinator awareness.

## Caveats

- **Stock-measure not flow-measure.** 90+ delinquent balance ratio captures accumulated non-paying balances, which lags flow-level transition-into-serious-delinq rate. Flow is a leading indicator; stock trails. Both elevated, but do not conflate.
- **Q4 2025 data is ~10 weeks old by now (Apr 24 2026).** Q1 2026 NY Fed HHDC release is typically mid-May 2026. Will confirm/extend direction.
- **Unemployment asymmetry vs 2009.** Peak came at unemployment ~10%. Current US 4.4%. Getting to 13.8% CC delinq at 4.4% unemployment would be a structurally different stress signature than 2009-10. May peak lower than GFC even if unemployment rises modestly.
- **Schwab reproduction, not NY Fed direct.** Data is NY Fed; the visual is a Schwab-commentary-style rendering. CARL should check NY Fed HHDC Q4 2025 primary for exact 12.7% figure (primary typically publishes 1-2 decimal points).
- **CC issuer mix matters.** NY Fed balance-weighted rate averages across prime/subprime/retail-card products; industry averages hide subprime stress that's higher than 12.7%.

## Source

- Will Telegram image 2026-04-24 22:55 UTC (msg 1036)
- Charles Schwab commentary (chart reproduction)
- NY Fed Consumer Credit Panel / Equifax primary, data as of 12/31/2025 — https://www.newyorkfed.org/microeconomics/hhdc.html
- Prior BOARD cross-references: SIG-W-20260419-001 (auto-subprime Tricolor/MTB), 015 (NFIB Sub-V), 020 (ATTOM foreclosure); SIG-W-20260424-001 (FL LABOR)
