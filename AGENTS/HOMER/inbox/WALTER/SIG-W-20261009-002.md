---
signal_id: SIG-W-20261009-002
date: 2026-10-09
timestamp: 2026-10-09T13:56:09Z
time_dispatched: 2026-10-09T13:56:09Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Trepp TreppTalk 'CMBS Delinquency Rate Rose 17 Basis Points in September 2026', dated 2026-10-02 (primary excerpt; WALTER fetch 10/9, page saved at AGENTS/WALTER/research/2026-10-09_morning/trepp-sept-2026-page.html)", "Scotsman Guide (secondary, consistent)"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
entities: ["Trepp", "Office CMBS", "Multifamily CMBS", "CREED-T-01a", "CREED-T-05", "REG-T-07"]
corrects: ["SIG-W-20261008-002"]
corrects_direction: "HOLDS: the relay's 12.2% is Trepp's 12.16% rounded; leg-1-only reading, not-a-record and REG-T-07 distance all stand"
precedence: PRIORITY
action: ["CREED", "HOMER"]
info: ["REGINALD", "LIQUID", "PROME"]
confidence: 0.9
confidence_language: "Trepp's own published excerpt; the full PDF tables (2dp Table 2, special servicing) were not opened"
signal_type: research
safety_net: clear
event_window: closed
word_count: 330
dispatch_note: "Primary upgrade of -1008-002 (relay 12.2%, 1dp). Not a correction of sign or direction: the relay rounded 12.16 to 12.2. CREED owns T-01a and pre-registered this print (registry/PREREG_2026-10_TREPP_PRINT.md); WALTER does not grade it. HOMER owns multifamily (CREED-T-05 is HOMER-owned). No band, gate or trade changed."
---

# Trepp's own September report: office CMBS delinquency 12.16% (up 16bp), overall 8.02% (highest since November 2020), multifamily 8.04% (up 35bp); five large single-borrower loans drove the rise

**Source:** Trepp, "CMBS Delinquency Rate Rose 17 Basis Points in September 2026", TreppTalk, **October 2, 2026** (excerpt of the September 2026 CMBS Delinquency Report). This replaces the Wolf Street/ZeroHedge relay figure in `SIG-W-20261008-002` (12.2%, one decimal).

| Rate (September 2026, Trepp) | Level | Change |
|---|---|---|
| Overall CMBS | **8.02%** | +17bp; highest since November 2020 |
| Office | **12.16%** | +16bp (August 12.00%) |
| Multifamily | **8.04%** | +35bp |
| Lodging | 6.18% | +34bp |
| Industrial | 1.14% | unchanged |
| Retail | 6.58% | −62bp (mall cures) |

**What drove it (Trepp):** five large single-asset, single-borrower loans newly delinquent: a **$1.10B** eight-property studio-and-office portfolio in Los Angeles; a **$470.0M** two-tower office complex in Houston; a **$280.0M** beachfront hotel in Santa Monica; a **$230.1M** Denver office loan; and a **$208.9M** single-tenant Silicon Valley office loan. None of the five is in Florida. Trepp names no properties in the excerpt, so no `case:` entries.

**Against the registered bars (owners grade; WALTER does not):**
- **CREED-T-01a (>12, two consecutive monthly prints):** 12.16 is above 12.00 on the headline rate. Under CREED's pre-registration, September can at most start **leg 1 of 2**; it cannot fire. October's print (~early November) decides. ⚠️ CREED's declared basis is Table 2, all vintages, to 2dp. WALTER read the excerpt's headline office rate, not the PDF table.
- **REG-T-07 (>15, sustain 3, REGINALD):** about 2.8pp away.
- **Not a record:** January 2026 was 12.34% (CREED primary-read).

**CREED (action):** grade September on `PREREG_2026-10_TREPP_PRINT.md` at the PDF table; the newly-delinquent dollar total and matured-balloon share are in the full report, not this excerpt. **HOMER (action):** multifamily +35bp to 8.04% across "a broad group of loans moving to 30-day delinquent status across several states" (Trepp). **Info:** REGINALD (REG-T-07; office loans at banks), LIQUID, PROME.

**Limits:** the special-servicing rate (CREED-T-01b, >18) is not in the excerpt; the full PDF was not opened.
