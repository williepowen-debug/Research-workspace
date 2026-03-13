# FLOW Reclassified Rows — Migration Artifact

**Date:** 2026-03-12
**Context:** FLOW.tsv migrated from 6-col channel format to 11-col HENRY pathway format. 5 rows reclassified as KB material (structural observations or point-in-time events, not reusable transmission pathways).

**Action for BROCK (Task 5):** Review these and absorb relevant content into KB.tsv, then delete this file.

---

## Reclassified as KB (structural observations)

| Old ID | Content | Why Not FLOW |
|--------|---------|-------------|
| LEVERAGE_STACK | 4 layers: Co (5x) → Fund (1.5x) → Bank (fund finance) → LP. Single asset supports 4 debt layers. | Structural observation, not a triggerable pathway. |
| CONCENTRATION | Same names across OWL/ARCC/TCPC/NMFC/PSEC. 9.2% overlap (>$5B funds). Diversification across managers is illusory. | Static fact about portfolio overlap. |

## Reclassified as KB/ML (point-in-time events)

| Old ID | Content | Why Not FLOW |
|--------|---------|-------------|
| 13_BLUE_OWL_GATE | Gate → fear → contagion. $1.7B gated Feb 18. BRK-03 CONFIRMED. | Event that already happened. The ongoing mechanism is in FLOW-BRK-003. |
| 14_DENIAL_PHASE | BofA "misinformation" defense. $8.3B outflows Feb 23. | Point-in-time narrative event. |
| 15_REGIONAL_TRANSMISSION | Blue Owl gate → WAL/EGBN -5.5% Feb 23. | Single-day price reaction, not reusable mechanism. The ongoing channel is in FLOW-BRK-014. |

## Already absorbed

| Old ID | Absorbed Into | How |
|--------|--------------|-----|
| 8_Syndicate_Contagion | FLOW-BRK-002 | ARCC 39-lender syndicate risk folded into revolving facility pathway |
| 16_BIG_BANK_EXPOSURE | FLOW-BRK-014 | JPM/BofA/Citi $100B+ now includes DB $30B disclosure |
