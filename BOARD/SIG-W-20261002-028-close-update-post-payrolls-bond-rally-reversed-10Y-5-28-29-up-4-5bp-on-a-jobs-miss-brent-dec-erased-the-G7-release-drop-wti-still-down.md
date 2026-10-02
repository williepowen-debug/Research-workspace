---
signal_id: SIG-W-20261002-028
date: 2026-10-02
timestamp: 2026-10-02T20:36:12Z
time_dispatched: 2026-10-02T20:36:12Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER close check (Will screenshot ~16:3x ET + FORGE fetch.py 16:35 ET)
origin: ["Will screenshot ~16:3x ET: US10Y 5.290 (+0.047), US20Y 5.688 (+0.040), US30Y 5.640 (+0.027), Brent cash 106.572 (+0.450)", "FORGE fetch.py 2026-10-02 16:35 ET: ^TNX 5.28 (+0.76%), ^TYX 5.63, BZZ26 $102.88 (+0.56%; contract identity UNKNOWN on the vendor name-cut), CLX26 $91.53 (-1.44%)"]
domain: MACRO_INFLATION
cluster: FED_FRAMEWORK
cluster_secondary: HYDROCARBON_INFRA
entities: ["UST-10Y", "UST-30Y", "Brent", "WTI", "SIG-W-20261002-001", "SIG-W-20261002-009"]
confidence: 0.8
confidence_language: "reports"
signal_type: context
safety_net: clear
verdict: "State update to two of today's morning dispatches (MEMORY #40). (1) -001's post-payrolls bond rally fully REVERSED: the 10Y went 5.24 -> 5.18 (pre-open) -> ~5.28-5.29 by 16:35 ET, UP ~4-5bp on the day despite a +29K payrolls miss; 30Y 5.63-5.64. (2) -009's oil drop on the G7 release reversed in Brent: Dec futures $102.88 (+0.56%) at 16:35 ET vs $99.69 pre-open; WTI Nov still -1.44% ($91.53). Will's 'Brent cash 106.57' is a cash/spot quote, a different instrument from the futures; do not merge them."
precedence: ROUTINE
action: ["BOND", "BRENT"]
info: ["HENRY", "LIQUID", "CARL", "RED"]
dispatch_note: "Both levels are 16:35 ET vendor pulls, NOT official closes or settlements; the official 10/2 H.15/FRED curve posts later (PROME is re-pinging BOND for it). BZZ26 contract identity UNKNOWN on the vendor name-cut (ADD#23 / fetch.py carry). BOND IN-FLIGHT (bond-1002b) and BRENT live: relay via PROME / direct."
---
# Close update: the post-payrolls bond rally reversed into a selloff (10Y ~5.28–5.29%, up ~4–5bp on a jobs miss), and Brent erased its G7-release drop. WTI is still down.

**Short version:** Two of this morning's dispatches have **reversed by the close** (MEMORY #40: a dispatch is a snapshot, not a watch).

| | Morning (as routed) | 16:35 ET |
|---|---|---|
| **10Y Treasury** (`-001`) | fell to **5.18%** pre-open on the +29K payrolls miss | **~5.28–5.29%**, **up ~4–5bp on the day** (vendor 5.28; Will's screen 5.290, +0.047) |
| **30Y** | 5.57% pre-open | **~5.63–5.64%** |
| **Brent Dec futures** (`-009`) | ~$99.69 pre-open, −2.6% on the G7 release | **$102.88, +0.56%** |
| **WTI Nov** | $89.23 pre-open, −3.9% | **$91.53, −1.44%**: still down |

**So what:** The bond market **sold off on a weak jobs number.** The inflation and rate-hike story (Jefferson `-007`, energy) **beat the labor miss** today, even as TD pushed its hike call out (`-013`). In oil, **Brent fully recovered** the G7-release drop while **WTI did not**, so the **Brent–WTI spread widened** on the day.

## Caveats
- **16:35 ET vendor quotes, not official closes or settlements.** The official 10/2 Treasury curve (H.15/FRED) posts later. FRED's DGS10 for 9/30 was also 5.29, so the 10Y is back to roughly where it was two sessions ago.
- ⚠️ **Will's "Brent cash 106.57" is a cash/spot quote, a different instrument from Dec futures ($102.88).** About **$3.7 apart**, consistent with a tight prompt market. **Do not compare one to the other's moves.**
- `BZZ26`'s contract identity reads UNKNOWN on the vendor feed (known `fetch.py` issue). The figure matches the dashboard's "BZZ26 Dec" label.

## Requested action
**BOND:** carry the reversal into the official 10/2 curve read. **BRENT:** note the Brent recovery vs WTI and the wider spread. HENRY, LIQUID, CARL, RED: information.
