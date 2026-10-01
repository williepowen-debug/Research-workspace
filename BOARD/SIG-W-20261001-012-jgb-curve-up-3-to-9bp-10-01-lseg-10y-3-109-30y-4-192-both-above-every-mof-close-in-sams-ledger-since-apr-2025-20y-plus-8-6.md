---
signal_id: SIG-W-20261001-012
date: 2026-10-01
timestamp: 2026-10-01T16:46:11Z
time_dispatched: 2026-10-01T16:46:11Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: Will (Telegram) — Will-Telegram 8-image batch 2026-10-01 ~16:42Z (msgs 4805-4812), batch manifest BM-20261001-02
origin: ["Will Telegram photo (msg 4805): LSEG government-bond quote screen, JP02Y-JP40Y, undated screenshot sent 12:42 ET 10/01 (taken as the 10/01 Tokyo close)", "SAM ledger AGENTS/SAM/workbook/JGB_YIELDS.tsv (MOF basis, 2025-04-02 to 2026-09-30, committed 95d11fed8)"]
domain: JAPAN_BOJ
cluster: ASIA_CHINA
entities: ["JGB 2Y", "JGB 10Y", "JGB 20Y", "JGB 30Y", "JGB 40Y", "BOJ"]
confidence: 0.7
confidence_language: "Screenshot levels are LSEG's, undated (assumed 10/01 close). Comparison is to SAM's MOF-basis ledger; the LSEG-MOF gap on 9/30 was ~0.6bp (10Y) and ~2bp (30Y), smaller than the margins claimed. 'Above every close since Apr 2025' is bounded by the ledger's start, not a historical high."
signal_type: pattern-match
safety_net: clear
verdict: "JGB yields rose 3-9bp across the curve on 10/01 (LSEG): 2Y 1.955 (+3.1), 10Y 3.109 (+5.8), 20Y 3.968 (+8.6), 30Y 4.192 (+7.1), 40Y 4.236 (+7.1). The 10Y and 30Y are above every MOF close in SAM's ledger (start 2025-04-02): prior maxima 10Y 3.082 (9/28) and 30Y 4.131 (9/1). Same day as the European flight-to-quality (-011) and US 30Y near highs."
precedence: PRIORITY
action: ["SAM"]
info: ["LIQUID", "HENRY", "RED"]
dispatch_note: "Source: Will-Telegram 8-image batch 2026-10-01 ~16:42Z (msgs 4805-4812), batch manifest BM-20261001-02, item 1. 'Already ours?' SAM's ledger ends 9/30 (MOF posts the 10/01 row later), so the 10/01 move is new to the owner's record. Domain JAPAN_BOJ -> SAM action (IN-FLIGHT as a PROME spawn; no doorbell). LIQUID/RED info per row; HENRY info (global long-end, same-day US/EU moves). PRIORITY: no registered SAM bar named in the screenshot; SAM grades."
---

# Japanese government bond yields rose 3–9bp across the curve on 10/01. The 10-year (3.11%) and 30-year (4.19%) are above every close in SAM's ledger since April 2025.

| Tenor | 10/01 (LSEG) | Change | SAM ledger max (MOF basis, since 2025-04-02) |
|---|---|---|---|
| 2Y | 1.955% | +3.1bp | — |
| 10Y | **3.109%** | +5.8bp | 3.082 (9/28) |
| 20Y | 3.968% | **+8.6bp** | — |
| 30Y | **4.192%** | +7.1bp | 4.131 (9/1) |
| 40Y | 4.236% | +7.1bp | — |

**So what:** the long end led a curve-wide sell-off on the same day Bunds rallied and the euro periphery widened (`-011`). It also lands while SAM's own Japan flow signal shows residents selling foreign bonds (`-004`). **SAM decides whether it bears on its BOJ or carry ladder.**

## Caveats
- The screenshot is **undated**; read as the 10/01 Tokyo close because of when it arrived (12:42 ET).
- **LSEG vs MOF basis:** the gap on 9/30 was ~0.6bp (10Y) and ~2bp (30Y). The margins over the ledger maxima (+2.7bp, +6.1bp) exceed that, but the MOF 10/01 print is the owner's confirmation.
- "Above every close since April 2025" is the **ledger's** limit, not an all-time claim.

Action SAM: confirm on the MOF print and grade it against your ladder. Canon: SAM.
