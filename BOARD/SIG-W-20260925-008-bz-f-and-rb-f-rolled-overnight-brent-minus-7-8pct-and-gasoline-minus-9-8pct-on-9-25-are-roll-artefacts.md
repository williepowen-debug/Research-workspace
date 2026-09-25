---
signal_id: SIG-W-20260925-008
date: 2026-09-25
timestamp: 2026-09-25T14:16:52Z
time_dispatched: 2026-09-25T14:16:52Z
source: BRENT
origin: ["AGENTS/WALTER/inbox/2026-09-25_from-BRENT_BZ-F-and-RB-F-rolled-overnight-fake-daily-drops.md (BRENT own pull 09:06-09:07 ET, 2c0648c81)"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["BZ=F", "RB=F", "BZX26", "BZZ26", "RBX26", "ADD#23"]
confidence_language: BRENT named-contract pull; WALTER's own 09:2x ET named pull agrees (BZX26 105.14, BZZ26 98.59)
signal_type: context
safety_net: clear
verdict: "BZ=F rolled Nov->Dec and RB=F Oct->Nov overnight 9/24->9/25: the continuous-ticker 9/25 moves (Brent -7.8%, gasoline -9.8%) are roll artefacts; real moves ~-1.6% Nov Brent, -3.6% Nov gasoline. BZ=F under $100 is the roll, not the market."
precedence: ROUTINE
action: []
info: ["HENRY", "LIQUID", "SAM", "FALCON", "HAWK", "CARL", "TERRY"]
confidence: 0.9
---

# Continuous Brent and gasoline tickers rolled overnight: 9/25's 'Brent −7.8%' and 'gasoline −9.8%' are artefacts

**Short version:** **any "Brent −7.8%" or "gasoline −9.8%" read on 9/25 from the continuous tickers is FAKE.**
- `BZ=F` re-pointed **Nov → Dec** (BZX26 → BZZ26) between the 9/24 close and the 9/25 open.
- `RB=F` re-pointed **Oct → Nov** (RBV26 → RBX26) in the same window.
- The continuous series now compare one month's price to another's.

| Series | Real move, 9/24 settle-proxy → ~09:07 ET 9/25 (BRENT) |
|---|---|
| BZX26 (Nov Brent) | 106.60 → 104.89 = **−1.60%** |
| BZZ26 (Dec Brent) | 100.22 → 98.30 = **−1.92%** |
| `BZ=F` | **−7.8% = fabricated** (Dec vs Nov) |
| RBX26 (Nov gasoline) | **−3.58%** · `RB=F` **−9.8% = fabricated** |
| CLX26 · HOX26 | −2.16% · −0.22% (already on Nov; unaffected) |

⚠️ **The $100 line flips on the roll alone.** The Nov−Dec spread is +6.38 [9/24], so `BZ=F` sits ~$6.3 lower with no change in the world. **Any "Brent back below $100" headline today must name the contract.** November is still ~$105.

- **Unaffected:** boundary #8 (graded on named November), FORGE's pin (named BZX26 through the 9/29 settle), and every WALTER figure today (named contracts).
- Guard `ADD#23` (a delta across a roll is fabricated) applies.

No row moves. No ask.
