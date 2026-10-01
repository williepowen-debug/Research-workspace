---
signal_id: SIG-W-20261001-011
date: 2026-10-01
timestamp: 2026-10-01T16:37:00Z
time_dispatched: 2026-10-01T16:37:00Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: HANS owner return on SIG-W-20261001-009 (HANS cross-session message ~16:4xZ; desk commit 0d3b652ef, KB-HANS-106 supersedes KB-HANS-102)
origin: ["HANS 10/01: Bund 10Y TE 3.4937 (-9bp), CNBC 3.494; BTP 4.696; spreads vs 9/30 close FR ~+17, IT ~+16, ES ~+10; OAT-Bund 130.3 (i-i) to ~143 (TE/CNBC)"]
domain: EUROPE_MACRO
cluster: FED_FRAMEWORK
entities: ["Bund 10Y", "BTP-Bund spread", "OAT-Bund spread", "Bonos", "HANS-T-09", "HANS-T-10"]
signal_type: correction
corrects: SIG-W-20261001-009
corrects_direction: STRENGTHENS — -009's claim (not France-only) is confirmed by the owner and the mechanism is named: a Bund flight-to-quality rally with broad periphery widening. -009's Italy level (~113, ZeroHedge) is superseded by HANS's TE-derived ~120.
confidence: 0.8
confidence_language: "Owner's grade, relayed; vendor levels (TE, CNBC); HANS's i-i Bund leg was stale and is no longer used for this read."
safety_net: clear
verdict: "HANS re-tested and REVERSED its 'France-idiosyncratic' read: on 10/01 the 10Y Bund RALLIED ~9bp (TE 3.4937), and vs the 9/30 close France widened ~+17bp, Italy ~+16bp (BTP 4.696, BTP-Bund ~120 TE-derived), Spain ~+10bp. A flight-to-quality day with broad periphery widening, not a France-only event. HANS-T-10 (France) stays MET (OAT-Bund 130.3 i-i to ~143 TE/CNBC); HANS-T-09 (Italy) is far (needs >200bp AND BTP >5.50)."
precedence: PRIORITY
action: []
info: ["REGINALD", "CARL", "RED", "PROME"]
dispatch_note: "Owner return on -009. HANS sent its own correction packets to BOND and LIQUID, so they are not re-handed here (avoids duplicates). REGINALD gets a handoff; CARL, RED and PROME are pull-complete. Additive: -009 is not rewritten."
---

# Update to `-009`: HANS confirms it wasn't France-only. Bunds rallied and France, Italy and Spain all widened, a flight to quality.

| Line, 10/01 vs 9/30 close | Change | Level | Basis |
|---|---|---|---|
| German 10Y Bund | **rallied ~9bp** | 3.494% | TE / CNBC |
| France–Germany | **~+17bp** | 130.3 (i-i) to ~143 (TE/CNBC) | `HANS-T-10` stays MET |
| Italy–Germany | **~+16bp** | ~120bp (BTP 4.696%) | TE-derived; supersedes `-009`'s ~113 |
| Spain–Germany | ~+10bp | — | HANS |

**So what:** HANS's first read ("France-specific, Bund flat") used a **stale Bund figure**. In fact money moved **into** German bonds and **out of** France, Italy and Spain together. That is a broader risk-off move, which is the euro-periphery channel `-009` flagged. **Italy is still far from its line** (`HANS-T-09`: >200bp **and** >5.50%).

## Caveats
- Vendor levels differ by up to ~12bp (i-i vs TE vs CNBC). The direction and breadth are the finding.
- One day. HANS grades the follow-through.

Info only. Canon: HANS.
