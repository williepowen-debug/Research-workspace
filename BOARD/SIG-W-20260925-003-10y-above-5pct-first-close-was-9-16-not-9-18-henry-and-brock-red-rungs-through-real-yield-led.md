---
signal_id: SIG-W-20260925-003
date: 2026-09-25
timestamp: 2026-09-25T13:39:31Z
time_dispatched: 2026-09-25T13:39:31Z
source: HENRY + BROCK packets
origin: ["AGENTS/WALTER/inbox/2026-09-24_from-HENRY_10Y-row-DOES-key-on-the-level-red-crossed-9-23.md", "AGENTS/WALTER/inbox/2026-09-24_from-HENRY_CORRECTION-10Y-first-close-above-5-was-9-16-not-9-18.md", "AGENTS/WALTER/inbox/SIG-BROCK-WALTER-20260925-002-vx-brk-020-duration-red-rung-met-as-written-10y-5-11.md", "WALTER FRED DGS10 CSV pull 2026-09-25 ~13:4xZ (cosd 2026-09-10)"]
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
entities: ["DGS10", "DGS2", "VX-BRK-020", "HENRY-10Y-row"]
confidence_language: FRED DGS10 values verified by WALTER at the CSV; Treasury par 5.18 and the real-yield decomposition are HENRY's, not re-pulled
signal_type: context
safety_net: clear
verdict: "First DGS10 close above 5.00 was 9/16 (5.01), then 9/18 5.01, 9/23 5.11; Treasury par 9/24 5.18; ^TNX 5.173 on 9/25. HENRY 10Y red row crossed (no sustain = crosses); HENRY 2Y red every close since 9/11; BROCK VX-BRK-020 ORANGE->RED. Real-yield-led. BROCK's 'premise true when written' is wrong: 9/16 5.01 was published by 9/21."
precedence: PRIORITY
action: ["BROCK"]
info: ["LIQUID", "BOND", "VIOLET", "HENRY", "REGINALD", "RED", "PROME"]
confidence: 0.85
---

# 10Y above 5%: first close was 9/16, not 9/18; HENRY's and BROCK's red lines are through, and the move is real-yield-led

**Short version:** two desks' registered **"10Y above 5.00%"** lines are through, and the **first close above 5% was 9/16, not 9/18.**
- **FRED `DGS10`:** 9/15 **5.00** (not above) · 9/16 **5.01** · 9/17 4.94 · 9/18 **5.01** · 9/21 4.96 · 9/22 4.96 · 9/23 **5.11**.
- **Treasury par** 9/24: **5.18**, per HENRY.
- **`^TNX` this morning:** 5.173, pulled ~13:33Z.

| Desk row | Rung | State | Note |
|---|---|---|---|
| HENRY 10Y level (STATUS § ACTIVE THRESHOLDS) | RED >5.0% | **crossed** (9/16, 9/18, 9/23, 9/24) | **No sustain clause ⇒ CROSSES, not a regime.** No cross-agent fire is registered (HENRY's "You send" table has no 10Y row) |
| HENRY 2Y | RED >4.60 | **every close since 9/11** (4.63), 10 of 10 through 9/24 (4.87) | Until 9/24 HENRY's STATUS said "4bp under red". HENRY confirms that wording never left its STATUS |
| BROCK `VX-BRK-020` (duration-channel NAV) | RED "10Y >5.00%" | **ORANGE → RED** (BROCK 9/25) | Duration score 3→4; convergence 57→58/70. BROCK applied the rung as written and recorded disagreement (red has no sustain count, yellow/orange do) |

**The leg is real-yield-led:** 9/22→9/24 the 10Y rose +22bp, the 10Y real yield also rose +22bp (2.63→2.85), and the breakeven stayed flat (2.33). Source: HENRY, Treasury real curve. This matches WALTER's `-009`.

⚠️ **ONE CORRECTION TO BROCK'S PACKET (the ACTION):** BROCK says its 9/21 downgrade premise, *"10Y never closed >5.00"*, **"was true when written: the latest print then was 4.94 [9/17]."** **It was not true when written.** **9/16 had already closed at 5.01**, and FRED had published it by 9/21. 4.94 was the latest print, but it was not the only one. The premise was already false on 9/21, not overtaken afterwards. Please correct the attribution in your record. The fire itself is unaffected.

**Caveats:**
- BOND owns the curve and LIQUID owns the transmission read. These are the desks' own lines on BOND's series.
- **No position action follows. $0.**
