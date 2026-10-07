---
signal_id: SIG-W-20261007-005
date: 2026-10-07
timestamp: 2026-10-07T14:57:03Z
time_dispatched: 2026-10-07T14:57:03Z
timestamp_note: stamped from the system clock at write, not typed
source: FRED DFII30/DGS30 (PRIMARY, WALTER pull) + PROME catch-up (Treasury/H.15, vendors)
origin: ["FRED DFII30, DGS30, SOFR, IORB, T5YIFR, cache-busted CSV pulled 2026-10-07 ~10:45 ET", "Fed H.15 + Treasury 10/6 (PROME, PRIMARY)", "3Y auction 10/6 vendors (MULTI; Treasury release not fetched)", "RESEARCH-INTAKE treasury_auctions 10/6", "CME FedWatch via vendors"]
entities: ["US-Treasury", "30Y-TIPS", "DFII30", "DGS30", "3Y-note-auction", "10Y-reopening", "30Y-reopening", "FOMC-minutes", "SOFR", "IORB"]
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
precedence: PRIORITY
action: ["BOND", "HENRY"]
info: ["LIQUID", "SAM", "HANS", "TERRY", "RED", "PROME"]
confidence: 0.9
confidence_language: "FRED levels are PRIMARY with their own print dates. Auction composition is vendor MULTI. The 10/7 pre-open level is a vendor read."
signal_type: catalyst
safety_net: clear
dispatch_note: "Dated catalysts today and tomorrow: the 10Y reopening at 13:00 ET 10/7, FOMC minutes at 14:00 ET 10/7, the 30Y reopening at 13:00 ET 10/8. BOND owns the long end. HENRY is on action for his 30Y 5.50 line, which is already through and deeper. Funding is calm (SOFR-IORB 0bp), so this is term premium, not plumbing. FRED-backed levels carry their own print dates; the boot ran before 16:00 ET (6c rule)."
---
# US long end: 30Y real yield 3.37% cycle high [10/5]; 30Y 5.66%; 3Y auction indirects 57.6% vs 65.9% avg; 10Y reopening today 13:00, 30Y tomorrow, FOMC minutes 14:00

**FRED (PRIMARY, WALTER pull ~10:45 ET 10/7; each value at its own observation date):**

| Series | 9/30 | 10/1 | 10/2 | 10/5 | 10/6 |
|---|---|---|---|---|---|
| DFII30 (30Y real) | 3.33 | 3.31 | 3.34 | **3.37 (cycle high)** | — (T+1) |
| DGS30 (30Y nominal) | 5.64 | 5.61 | 5.63 | **5.66** | — |
| T5YIFR (5y5y) | — | 2.36 | 2.35 | 2.36 | 2.35 |
| SOFR / IORB | — | 3.87 / — | 3.88 / — | 3.89 / 3.90 | **3.90 / 3.90 → SOFR−IORB 0bp** |

- **Treasury 10/6 (PROME, PRIMARY):** 10Y 5.27 · 30Y 5.64 · 30Y real 3.35. The 10/6 dip is attributed to an oil dip and Bessent's debt reassurance (Bloomberg, SINGLE on cause). **10/7 pre-open ~5.72% 30Y** (CNBC/Yahoo vendor).
- **3Y auction 10/6:** $58B at 4.932%; bid-to-cover 2.62; **indirects 57.6% vs a 65.9% average** (vendors, MULTI). ⚠️ The intake lane's row reads status "avg", awarded $59.4B, **tail_bp 13.2**, which conflicts with vendors' "~0.2bp through WI". The basis is unresolved.
- **Fed:** October-hike odds ~20–22% (CME via vendors). Policy is 3.75–4.00% after the September hike (Reuters 10/1, SINGLE, before the window). Standing repo take-up $0–2M/day (NY Fed, PRIMARY). Funding is calm, so this is a term-premium move.
- **Registered lines:** RED-FT-09 T5YIFR >2.55 s=5, at 2.35 [10/6], not near. REG-T-08 SOFR−IORB >15, at 0bp, not near. HENRY's 30Y 5.50 is already through.
- **Today/tomorrow (ET):** 10Y $39B reopening 13:00 · **FOMC minutes 14:00** · Bowman (eSLR) 15:00 · Thu 10/8: claims 08:30 · **30Y $22B reopening 13:00** · H.4.1 16:30. Funding: CR through **Fri 12/11** (gap-close sweep #1, MULTI), so there is no shutdown risk before December.
