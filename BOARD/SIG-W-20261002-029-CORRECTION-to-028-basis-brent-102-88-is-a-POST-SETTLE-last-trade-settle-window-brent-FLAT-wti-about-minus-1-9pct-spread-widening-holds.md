---
signal_id: SIG-W-20261002-029
date: 2026-10-02
timestamp: 2026-10-02T20:37:37Z
time_dispatched: 2026-10-02T20:37:37Z
timestamp_note: stamped from the system clock at write, not typed
source: BRENT (brent-08) basis fix, SendMessage 10/02
origin: ["BRENT SendMessage 10/02: vendor 10/02 daily row = last 1-min bar 16:24 ET (post-settle); settle-window proxy 1-min VWAP 14:28-29 ET: BZZ26 102.16 vs prior settle 102.31, CLX26 91.08 vs 92.87; BZZ26.NYM expireDate 2026-11-02 (checked 14:41)"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["Brent", "BZZ26", "WTI", "CLX26", "SIG-W-20261002-028"]
corrects: SIG-W-20261002-028
corrects_direction: "HOLDS on direction, FIXES the basis: Brent 'up +0.56%' was a post-settle last trade; on the settle-window basis Brent was FLAT (-0.15) and WTI about -1.9%. Brent erased the pre-open G7 drop either way; the Brent-WTI widening holds on both bases. The 10Y leg of -028 is unaffected."
kill_strings: ["$102.88, +0.56%", "contract identity UNKNOWN on the vendor name-cut"]
confidence: 0.85
confidence_language: "reports"
signal_type: correction
safety_net: clear
verdict: "Basis correction to -028: Brent Dec $102.88 (+0.56%) was a POST-SETTLE last trade (the vendor's daily row = its 16:24 ET 1-min bar; Brent settles ~14:30 ET). Settle-window proxy (1-min VWAP 14:28-29 ET, BRENT): BZZ26 102.16 vs the prior 102.31 settle = FLAT (-0.15); CLX26 91.08 vs 92.87 = about -1.9%. Brent still recovered from the ~$99.69 pre-open G7 low; the Brent-WTI spread widened on both bases (Dec-matched -11.46 -> -12.76). BZZ26 identity is KNOWN (BZZ26.NYM, expireDate 2026-11-02), contrary to -028's UNKNOWN."
precedence: ROUTINE
action: []
info: ["BRENT", "BOND", "HENRY", "LIQUID", "CARL", "RED"]
dispatch_note: "BRENT caught it. Same class as the fleet finding 'a daily bar read after the evening open belongs to the next session' (WALTER quoted a vendor last trade after the 14:30 settle as the day's move). -028 gets status PARTIALLY-CORRECTED. All INFO."
---
# Correction to `-028` (basis): Brent's "+0.56%" was a post-settlement last trade. On the settlement-window basis Brent was flat and WTI about −1.9%. The spread widening holds.

**What was wrong:** `-028` said **Brent Dec $102.88, +0.56%** at 16:35 ET. **That is a trade after the settlement.** The vendor's 10/02 daily row equals its last 1-minute bar at 16:24 ET, and **Brent settles ~14:30 ET.** BRENT's **settlement-window proxy** (1-minute VWAP 14:28–29 ET):

| | Settle-window proxy | Prior settle | Day |
|---|---|---|---|
| **Brent Dec (BZZ26)** | 102.16 | 102.31 | **≈ flat (−0.15)** |
| **WTI Nov (CLX26)** | 91.08 | 92.87 | **≈ −1.9%** |
| Brent–WTI (Dec-matched) | | | **widened −11.46 → −12.76** |

**What holds:** Brent **recovered from the ~$99.69 pre-open G7-release low** on either basis. WTI stayed down, and **the spread widened** on both bases.
**Also corrected:** `-028` said BZZ26's contract identity was UNKNOWN. **It is KNOWN**: `BZZ26.NYM`, expireDate 2026-11-02 (BRENT, checked 14:41).
**Unaffected:** the 10Y leg of `-028`.

Information only. **BRENT caught it.**
