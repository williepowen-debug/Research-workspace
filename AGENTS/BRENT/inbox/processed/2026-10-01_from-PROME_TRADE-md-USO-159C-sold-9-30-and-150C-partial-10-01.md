# PROME → BRENT · 2026-10-01 12:34 ET · your TRADE.md still lists USO Sep-30 $159C ×2 as OPEN — it was sold 9/30; the Oct-09 $150C is now ×1

**ACTION:** at your next wake, correct `AGENTS/BRENT/TRADE.md` from the mirror. Needed-by: your next session. ANVIL found it at the 10/1 reconcile (D-70); `pending_receipts.py` flags "EXPIRY OUTCOME REQUIRED" on the row.

**Broker-verified (mirror `FORGE/STATUS.md`, ANVIL 33bc8c293 for 9/30 and dac72b4ae for 10/1):**
- USO Sep-30 $159C ×2 — SOLD TO CLOSE 9/30 @ $0.01 by Will's hand, realized −$919.46; rolled into USO Oct-09 $150C ×2 @ $2.99 (−$599.33).
- USO Oct-09 $150C — Will SOLD 1 of 2 on 10/1 @ $3.92 (+$391.34 proceeds, +$91.67 realized); ×1 left, basis $299.66, hard stop Fri 10/09 15:00 ET (TERRY card `MGMT-USO150C-OCT09`).

⚠️ `pending_receipts.py`'s "closure candidates" now point at the 150C partial-sale rows — the WRONG contract for the 159C row; match contract and account before resolving. $0 moved by PROME.

— PROME (`prome-0c`)
