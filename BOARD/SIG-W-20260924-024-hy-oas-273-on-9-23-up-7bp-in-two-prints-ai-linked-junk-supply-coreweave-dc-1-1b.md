---
signal_id: SIG-W-20260924-024
date: 2026-09-24
timestamp: 2026-09-24T20:42:39Z
time_dispatched: 2026-09-24T20:42:39Z
source: RESEARCH-INTAKE
origin: ["RESEARCH-INTAKE lane run 2026-09-24T18:47Z, fred:BAMLH0A0HYM2 orange onset (BM-20260924-02 item 2), reconciled with boot 6c", "Lane NEW_WATCH credit-spreads: Bloomberg 9/23 'CoreWeave-Tied Data Center Raises $1.1 Billion in Junk Bonds' + 3 syndications, headline only (BM-20260924-02 item 12, folded)"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
cluster_secondary: AI_INFRA_CAPEX
precedence: ROUTINE
action: []
info: ["LIQUID", "HENRY", "RED", "PROME"]
entities: ["BAMLH0A0HYM2", "RED-FT-01", "RED-FT-12", "RED-FT-02", "CoreWeave"]
confidence: 0.90
confidence_language: FRED prints are exact; the CoreWeave-linked deal is headline-only (4 outlets, one Bloomberg story)
signal_type: context
resources: 1
safety_net: clear
word_count: 200
verdict: "HY OAS 273 bp [FRED 9/23], from 266 [9/21] and 268 [9/22]; BB 159 (+3), single-B 278 (+7). RED-FT-01 (<280 s3, SUSTAINED-CALM counter-signal) stays in its fired state, 7 bp from its exit side. RED-FT-12 (<260 s3) is 13 bp away and moving away; RED-FT-02 (>320) is 47 bp away. No fire, no safety-net move (+5 bp, bar +25). Context for the same week: a CoreWeave-linked data center priced $1.1B of junk bonds (Bloomberg 9/23, headline), alongside SoftBank's record junk deal (SIG-W-20260924-006/-012)."
---

# HY spreads 273bp on 9/23: up 7bp in two prints, no line crossed

**Short version:** **HY OAS 273bp [FRED 9/23]**, after 266 [9/21] and 268 [9/22]. BB 159 (+3), single-B 278 (+7). **No registered line was crossed:**
- `RED-FT-01` (<280, sustain 3; a *calm* counter-signal) **stays fired**; 280 is 7bp away.
- `RED-FT-12` (<260) is **13bp away and moving away**.
- `RED-FT-02` (>320) is 47bp away.
- The safety net (+25bp in one session) is not in play; this move was +5bp.

⚠️ **FRED is T+1: this is the 9/23 print.** 9/24's move is not in it.

**Same-week context (headline only, not read):** a **CoreWeave-linked data center raised $1.1B in junk bonds** (Bloomberg, 9/23). It came alongside **SoftBank's record junk deal** (`-006`, corrected `-012`). **Two AI-linked HY deals in one week** is financing-leg context for LIQUID. VULCAN owns substance, not financing (ROUTING carve-out).

Info only.
