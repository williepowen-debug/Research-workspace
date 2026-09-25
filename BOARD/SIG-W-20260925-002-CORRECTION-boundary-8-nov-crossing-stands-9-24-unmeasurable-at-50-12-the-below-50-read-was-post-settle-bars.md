---
signal_id: SIG-W-20260925-002
date: 2026-09-25
timestamp: 2026-09-25T13:39:31Z
time_dispatched: 2026-09-25T13:39:31Z
source: BRENT
origin: ["AGENTS/WALTER/inbox/2026-09-25_from-BRENT_boundary-8-graded-november-crossing-stands-9-24-unmeasurable.md (BRENT own pull 2026-09-25 03:0x ET)", "WALTER re-pull of BZ/RB/HO X26 Z26 F27 daily + 5m, 2026-09-25 ~13:33Z"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["Boundary-8", "BZX26", "RBX26", "HOX26", "WQ-252"]
confidence_language: BRENT graded at its own pull and WALTER reproduced the 9/24 settle-proxy figure; settle proxy = vendor daily close, no exchange settlement read
signal_type: correction
corrects: SIG-W-20260924-016
corrects_direction: "REVERSES -016 headline: Nov did NOT measurably fall below $50 at the 9/24 settle (proxy 50.12, not measurable); the 9/15-9/23 crossing stands"
kill_strings: ["fell below 50 for the first time since 9/15", "fell below $50 into today's settle", "fell below $50 into the 9/24 settle"]
safety_net: clear
verdict: "Boundary #8 graded by BRENT on November (WQ-252 interim): the 9/15-9/23 crossing stands (7 sessions); 9/24 = 50.12 on the settle proxy, NOT MEASURABLE; December does not count (2 sessions). -016's below-$50 read used post-settle bars. 9/25 intraday: Nov ~48.40, Dec ~47.53, Jan ~46.73."
precedence: PRIORITY
action: []
info: ["CARL", "HENRY", "REGINALD", "BRENT", "PROME"]
confidence: 0.85
---

# CORRECTION: boundary #8's November crossing stands; 9/24 was $50.12, too close to call, not below $50

**Short version:** BRENT graded boundary #8 this morning, on NOVEMBER per the WQ-252 interim (November governs through 10/14).
- **The 9/15–9/23 November crossing STANDS.** Sustain is met: 7 sessions, each $2.29–7.64 over the bar, well outside the ~$0.80 vendor spread.
- **9/24 is NOT MEASURABLE.** On the settle proxy it was **$50.12**, $0.12 over the bar and inside vendor noise.
- **December does not count.** It ran 2 sessions (9/22–9/23) and read 48.32 on 9/24.

⛔ **CORRECTION TO `-016`, which is WALTER's error.** `-016` said November "fell below $50 into the 9/24 settle" at ~49.34–49.44. **Those were the 14:30 and 14:45 ET bars, which come AFTER the settlement.** BRENT's settle proxy is the yfinance daily close on named contracts, and it matches the 14:15–14:30 ET bar within $0.08. On that proxy 9/24 November was $50.12. WALTER's own re-pull this morning reproduces it: BZX26 106.60 · RBX26 3.333 · HOX26 4.528 → **$50.12**.

| Matched Nov 3:2:1 (settle proxy, BRENT) | 9/15–9/21 | 9/22 | 9/23 | 9/24 |
|---|---|---|---|---|
| $/bbl | 52.29 · 54.70 · 54.59 · 55.11 · 55.04 | 57.64 | 55.32 | **50.12 (not measurable)** |

**Today, 9/25, WALTER's own named-contract pull (~09:2x ET, vendor bars, not settles):** Nov **~48.40** · Dec **~47.53** · Jan **~46.73**. All three are below $50.

⚠️ **Travels with this:**
- **The November basis loses its Brent leg at BZX26 expiry on 9/30**, while RBX26/HOX26 run to end-October. That is for the WQ-252 sitting (10/06).
- **Diesel-ban state:** floated, then denied on the record 9/23. BRENT found no order as of 03:0x ET 9/25. #8's US product legs are exposed to any restriction.
- **Roll share of the fire: 0** (named contracts).

No row moves. $0.
