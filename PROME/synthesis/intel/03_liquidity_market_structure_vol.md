# 03 — Liquidity / Market Structure / Public Credit / Vol Intel Packet

## Current claim
Public-credit contagion is **not confirmed**: HY OAS is tight at ~282bps, VIX is sub-20, SOFR-IORB is calm, and Treasury auctions are weak-but-clearing. The live risk is a **fragile calm**: BDC/private-credit and bank tape are deteriorating underneath a mechanically supported equity tape, with extreme gamma/momentum/call-buying conditions suppressing realized vol until positioning flips. Treat this as **yellow duration/market-structure fragility**, not red liquidity crisis yet. (`HEARTBEAT.md`; `AGENTS/BOND/STATUS.md`; `FORGE/signals/2026-05-14_gamma_momentum_factor_squeeze.md`)

## Confirmed evidence
- **HY cash credit remains benign.** HY OAS is 282bps, below the 300 watch line and far below 320/350 stress levels; BOND explicitly says short-HY thesis is not active and HYG June downside is stale without re-widening. (`HEARTBEAT.md`; `AGENTS/BOND/STATUS.md`; `AGENTS/BOND/TRADE.md`)
- **Vol surface is calm.** VIX ~17.85/17.88 in current dashboard, and VIOLET’s May 3 state had VIX 16.99, VVIX 95.17, VIX3M/VIX 1.1989 — deep contango, no vol stress. (`HEARTBEAT.md`; `AGENTS/VIOLET/STATUS.md`)
- **Credit-to-vol transmission has not fired.** VIOLET’s active framework needs HY OAS widening + VIX lag; instead HY/CCC compressed through late April and the Apr 22 SKEW gate failed. (`AGENTS/VIOLET/STATUS.md`; `AGENTS/VIOLET/TRADE.md`)
- **Funding plumbing is currently calm.** Current SOFR-IORB is about -6bps, green. This reverses LIQUID’s Apr 15 one-day SOFR > IORB breach; the structural-leak confirmation did not persist in the latest dashboard. (`HEARTBEAT.md`; `AGENTS/LIQUID/STATUS.md`)
- **Treasury demand is fatigued, not broken.** May refunding tailed across 3Y/10Y/30Y, but tails were small and demand mix was acceptable: 30Y high yield 5.046%, BTC 2.30, indirect 66.6%, dealer 11.7%, +0.5bp tail. (`AGENTS/BOND/STATUS.md`; `FORGE/signals/2026-05-14_30y_5pct_2007_headline_and_cycle_chart.md`)
- **Duration pressure is real.** 30Y traded/sold above 5%, 10Y near 4.5%, and TLT is weak at ~$84.80. This supports a duration-fatigue watch even without auction failure. (`AGENTS/BOND/STATUS.md`; `AGENTS/BOND/TRADE.md`)

## Suggestive evidence
- **Equity tape may be mechanically supported.** Momentum factors are extreme: 3M momentum +43.75% YTD, 6M momentum +42.76%, broad momentum +37.90%; quality, dividend yield, and growth-pair factors lag badly. (`FORGE/signals/2026-05-14_gamma_momentum_factor_squeeze.md`)
- **Gamma regime can suppress VIX until it doesn’t.** The gamma index reportedly moved from near-record low to near-record high in weeks, >$20B position, fastest move on record, exacerbated by 0DTE volume. This explains low realized vol despite BDC/bank/energy stress and creates air-pocket risk if dealer gamma flips. (`FORGE/signals/2026-05-14_gamma_momentum_factor_squeeze.md`)
- **Prior call-buying evidence rhymes.** A May 9 signal claimed $2.6T in SPX call notional in one day, 60% call share, and “semi-irrational chasing mode,” but methodology still needs verification. (`FORGE/signals/2026-05-09_spx-call-notional-sox-rsi-meltup.md`)
- **Breadth/concentration risk is unresolved.** A May 9 Goepfert screenshot claimed S&P record highs with 5%+ of members at 52-week lows — unverified, but directionally consistent with momentum/gamma concentration. (`FORGE/signals/2026-05-09_spx-record-high-breadth-deterioration.md`)
- **Private-credit/BDC stress is leaking into public proxies unevenly.** HEARTBEAT flags FSK Q1 as Strong Bear / near Max Bear, BIZD red at $12.57, WAL near/below bear line, while HY OAS and VIX stay benign. (`HEARTBEAT.md`)

## Unconfirmed / risks
- **CDX is not wired.** BOND’s key early-warning path is CDX widening while cash HY stays tight for 2+ weeks; current files do not provide fresh CDX confirmation. (`AGENTS/BOND/STATUS.md`; `AGENTS/BOND/TRADE.md`)
- **Gamma data needs primary-source validation.** Current gamma/momentum packet is screenshot-derived; use as high-priority fragility signal, not standalone trade trigger. (`FORGE/signals/2026-05-14_gamma_momentum_factor_squeeze.md`)
- **CCC OAS is elevated but compositionally noisy.** Current CCC OAS is ~937bps/yellow, but prior timing work says CCC/HY was partly distorted by cable/media, PE-healthcare, and software concentration; CCC is a stress clue, not clean systemic proof. (`HEARTBEAT.md`; `FORGE/timing/STATUS.md`; `FORGE/timing/2007_OAS_OVERLAY.md`)
- **Old LIQUID path was invalidated/de-risked.** LIQUID’s Apr 16 status treated SOFR>IORB as a possible structural leak and public-credit Path A as holding; current dashboard shows SOFR-IORB negative and public credit still tight. (`AGENTS/LIQUID/STATUS.md`; `HEARTBEAT.md`)
- **VIX call is lottery now.** VIOLET’s May 19 25C position remains open, but trade-level thesis was invalidated; expected outcome is worthless/near-worthless unless May 13-19 tail catalyst arrives. (`AGENTS/VIOLET/TRADE.md`)

## Transmission links
1. **Private credit/BDC stress → public credit:** FSK/BDC mark and income deterioration can migrate into HY OAS, issuance access, HYG/BIZD, and CDX. Current public HY is not confirming, but BIZD/FSK are pressure points. (`HEARTBEAT.md`; `AGENTS/BOND/STATUS.md`)
2. **Duration fatigue → funding/liquidity:** 30Y >5 and repeated auction tails become systemic only if paired with dealer-take spike, weak indirects, SOFR-IORB positive, or repo stress. Current auctions are yellow only. (`AGENTS/BOND/STATUS.md`; `AGENTS/BOND/TRADE.md`)
3. **Gamma/momentum crowding → vol/liquidity shock:** extreme positive gamma can suppress VIX and pull exposure higher; unwind transmits through momentum reversal, dealer de-hedging, VIX term-structure flattening, HYG/CDX, and KRE/WAL. (`FORGE/signals/2026-05-14_gamma_momentum_factor_squeeze.md`)
4. **Credit → vol lag:** VIOLET’s best long-vol setup is HY widening while VIX remains 15-26; current credit compression blocks the signal, but a HY OAS +75-100bp move with VIX <20 would re-arm it. (`AGENTS/VIOLET/TRADE.md`; `AGENTS/BOND/TRADE.md`)

## Contradictions
- **Stress is visible in BDCs/energy/banks, but absent in HY/VIX/SOFR.** This is the core contradiction: private-market and equity-proxy deterioration vs calm public credit and vol. (`HEARTBEAT.md`; `AGENTS/BOND/STATUS.md`; `AGENTS/VIOLET/STATUS.md`)
- **30Y 5% headline feels crisis-like; auction mechanics do not.** Narrative says 2007, but actual May 13 auction had only +0.5bp tail and acceptable indirect/dealer mix. (`FORGE/signals/2026-05-14_30y_5pct_2007_headline_and_cycle_chart.md`; `AGENTS/BOND/STATUS.md`)
- **VIOLET regime intact, trade invalidated.** Elevated SKEW regime survived, but the Apr 13 SKEW divergence trade failed strict rules; do not confuse durable fragility with current P&L edge. (`AGENTS/VIOLET/STATUS.md`; `AGENTS/VIOLET/TRADE.md`)
- **2007 OAS overlay projected acceleration earlier than current tape delivered.** March/April timing docs projected HY acceleration toward 400 by late Apr/May; actual May HY is ~282. The analog is not dead, but current public-credit timing is delayed/softened. (`FORGE/timing/2007_OAS_OVERLAY.md`; `FORGE/timing/STATUS.md`; `HEARTBEAT.md`)

## Watch items / triggers
- **HY OAS:** >300 for 3 sessions reopens credit watch; >350 + pulled deals supports short-credit proposal; <260 sustained weakens cascade thesis. (`AGENTS/BOND/TRADE.md`; `HEARTBEAT.md`)
- **CDX:** CDX.HY/CDX.IG widening while cash OAS stays tight for 2+ weeks = synthetic-led warning. (`AGENTS/BOND/STATUS.md`)
- **SOFR-IORB:** positive after weak auctions, especially sustained >+5bps, escalates to LIQUID. (`AGENTS/BOND/TRADE.md`; `AGENTS/LIQUID/STATUS.md`)
- **Rates/auctions:** 10Y >4.5 for 5 sessions, 30Y >5 sustained, auction tail >2bps, BTC <2.3 with dealer spike. (`AGENTS/BOND/TRADE.md`)
- **Vol/gamma:** VIX term structure flattening, VIX >20 then >25, SKEW re-ramp >145/155, VVIX >120, or momentum/realized-vol factor reversal. (`AGENTS/VIOLET/STATUS.md`; `AGENTS/VIOLET/TRADE.md`; `FORGE/signals/2026-05-14_gamma_momentum_factor_squeeze.md`)
- **Public-private bridge:** BIZD <$12.50 sustained, WAL/KRE bear-line continuation, FSK/BDC marks spreading into other 10-Qs. (`HEARTBEAT.md`)

## Source files consulted
- `AGENTS/LIQUID/STATUS.md`
- `AGENTS/HENRY/STATUS.md`
- `AGENTS/VIOLET/STATUS.md`
- `AGENTS/VIOLET/TRADE.md`
- `AGENTS/BOND/STATUS.md`
- `AGENTS/BOND/TRADE.md`
- `FORGE/signals/2026-05-14_gamma_momentum_factor_squeeze.md`
- `FORGE/signals/2026-05-14_30y_5pct_2007_headline_and_cycle_chart.md`
- `FORGE/signals/2026-05-09_spx-call-notional-sox-rsi-meltup.md`
- `FORGE/signals/2026-05-09_spx-record-high-breadth-deterioration.md`
- `FORGE/timing/2007_OAS_OVERLAY.md`
- `FORGE/timing/STATUS.md`
- `HEARTBEAT.md`
