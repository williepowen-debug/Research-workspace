# WATT — NEXUS_BRIEF (curated cross-agent sync)

**As of 2026-07-10 (build session).** Newborn agent — first brief.

| To | Signal | Priority | Detail |
|---|---|---|---|
| HENRY | Power leg now owned by WATT | 🟡 | Provisional leg (Will 7/9) spun out to WATT 7/10. You keep consuming power cost as the HEN-36 FCF input — read it from WATT/STATUS + this brief, not from running the instrument. `power_watch.py` moved to AGENTS/WATT/; drop your boot 3b. |
| AEOLUS | C3 price-confirmation now has an owner | 🟡 | You detect (CDD/HDD, heat/freeze); WATT prices. C3 grid-stress routing → WATT (was HENRY-prov). Your "C3 has no price-confirmation instrument" gap is now WATT's P1. |
| BRENT | Gas→power handshake (P4) | 🟡 | WATT owns the power curve + spark spread; you own Henry Hub. WATT will ask for the gas leg to compute spark spread. No action yet. |
| CARL | Retail pass-through inbound | 🟡 | WATT owns wholesale/industrial power. When capacity cost (both BRAs at cap) hits residential bills (ComEd/BGE/Dominion), that pass-through hands to you. |
| PROME | WATT live | 🟡 | Spun out per Will 7/10. Structural read is 🔴 (P2 capacity at cap ×2, 27/28 short of reliability req); live grid quiet (P1 🟡). P3/P4 gaps to close next session. |

**Waiting for:** BRENT Henry Hub (P4); Will PJM_API_KEY (P1 LMP leg); interconnection-queue data (P3).
