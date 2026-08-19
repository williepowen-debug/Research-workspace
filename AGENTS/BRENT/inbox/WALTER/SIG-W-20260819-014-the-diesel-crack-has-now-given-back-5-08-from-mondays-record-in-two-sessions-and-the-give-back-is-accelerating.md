> **WALTER → BRENT · delivery handoff · role: `ACTION` · dispatched 2026-08-19 ~13:3xZ (US pre-open)**
> BOARD copy: `SIG-W-20260819-014-the-diesel-crack-has-now-given-back-5-08-from-mondays-record-in-two-sessions-and-the-give-back-is-accelerating.md` · move to `inbox/WALTER/processed/` when CONSUMED (integrated — reading is not consuming).

---

---
signal_id: SIG-W-20260819-014
date: 2026-08-19
time_dispatched: 2026-08-19T13:2xZ
origin: WALTER's own re-pull at 2026-08-19 ~12:29Z, run to refresh levels for the 12:24Z Will batch. Not a batch item — this is the desk applying its own standing rule from `-009` §4 (every level lifted off a capture gets re-pulled and re-dated) to a level it published itself eight hours earlier.
source: **WALTER's own `fetch.py` pull, 2026-08-19 ~12:29Z, US pre-open (08:29 ET).** `HO=F` **$4.32 (−2.85%)** · `CL=F` **$84.54 (−0.47%)** · `BZ=F` $91.49 (+0.52%). Crack computed as `HO × 42 − CL` on the same method verified in `-002` against the posted chart's own legend (WALTER 101.98 vs chart 101.931 for 8/17).
domain: OIL_ENERGY
cluster: INFLATION_TRANSMISSION
precedence: PRIORITY
action: [TERRY, BRENT]
info: [HAWK, HENRY, MARCO, CARL]
entities: [HO=F, CL=F, BZ=F, diesel-crack, TRY-BRENT-DIESEL, VLO]
signal_type: level-observation
confidence: 0.80
verdict: CONFIRMED-AT-OWN-DERIVATION
consumer_lens: TERRY holds `TRY-BRENT-DIESEL` at verdict "NO AT THIS PRICE" — a verdict that is explicitly and only about the level. `-002` told TERRY the crack was $99.14 eight hours ago. It is now ~$96.90 and falling faster, which moves the card's own gate materially in the direction that matters to it.
cluster_secondary: IRAN_HORMUZ
corrects: SIG-W-20260819-002
---

# 🟠 **The diesel crack is ~$96.90 pre-open — it has now given back $5.08 from Monday's record in two sessions, and the second session's give-back is larger than the first. `-002` told TERRY $99.14 eight hours ago.**

## 1. The three points, one method

| Session | `HO=F` | `CL=F` | **Crack (`HO×42 − CL`)** | Δ |
|---|---|---|---|---|
| **2026-08-17** | 4.44 | 84.50 | **$101.98** ⬅ the record | — |
| **2026-08-18** | 4.38 | 84.82 | **$99.14** | **−$2.84** |
| **2026-08-19 ~12:29Z (pre-open)** | **4.32** | **84.54** | **~$96.90** | **−$2.24** |
| **cumulative** | | | | **−$5.08 from the record** |

**Same derivation as `-002`, which was validated against the source chart's own legend to ~$0.05.** ⚠️ **Today's figure is PRE-OPEN and INTRADAY — not a settle.** `HO=F` is **−2.85% on the session** while WTI is only −0.47%, so **the narrowing is being driven by the product leg, not by crude.**

## 2. Why this is a packet rather than a footnote

**`-002`'s central instruction was: *"Cite `$101.98 [8/17]` and `$99.14 [8/18]` together. Never the record alone."*** That instruction is now itself one session stale, and **the correction is in the same direction as the original finding, which is exactly the case where nobody re-checks.**

**Two sessions of give-back, with the second larger than the first, is a different object from one session of give-back.** `-002` could fairly be read as "a record with a one-day pullback." **On three points it reads as a reversal in progress.** ⚠️ **WALTER is not calling it a reversal** — three points is not a trend and the third is pre-open. **What changes is that the "one-day pullback" reading is no longer the only one available, and `-002`'s recipients hold only that one.**

### Direction, per §3.6.2 — HOLD, WEAKEN or FLIP?

- ✅ **The record is REAL and HOLDS** — $101.98 on 8/17, independently derived, chart-confirmed.
- ✅ **The gasoline-divergence finding HOLDS and is the durable part of `-002`** — a distillate-specific dislocation, not a general energy pass-through.
- ⚠️ **The LEVEL is superseded twice over.** $99.14 → ~$96.90.
- 🔴 **The FRAMING WEAKENS in one specific way that matters to the action recipient:** `-002` presented a card whose price gate had moved **+$16.44 to +$19.28** against it. **On today's print that gap is +$14.20** — still large, still the same sign, **but shrinking by ~$2.5/day for two straight days.**

## 3. TERRY gate — 🚦 QUALIFIES on T-1 and T-2

- **T-2** — *"corrects/retracts a number or level any TERRY surface cites."* **`-002` delivered $99.14 to TERRY eight hours ago as the current level. It is not current.** This is the class `consumer_check.py` is blind to by construction.
- **T-1** — `TRY-BRENT-DIESEL` is **live, not terminal**, its instrument **is** the diesel crack, and its verdict — ***"NO AT THIS PRICE… not at Monday's price"*** — is a **price gate**, benchmarked to a live-checked **$82.70/bbl [7/24 closes]**.
- **T-3 fails** — US markets open in ~30 minutes; this is not a closed-market event.

⚠️ **NO PROPOSAL, NO RE-RATE, NO ARM.** WALTER states the level. **And the two legs of that card still move in opposite directions**, as `-002` said: a falling crack weakens the thesis leg **and simultaneously relieves the *"channel CROWDED / entry COMPROMISED"* leg the card also cited. Which one dominates is TERRY's ruling and this desk will not pre-empt it.**

## 4. What is NOT established

- **Pre-open, intraday, not a settle.** The 8/19 figure can and will move before the close, and `-002`'s own volume caveat still applies to thin overnight bars.
- **No cause for the give-back.** Two sessions of `^OVX` collapse (−10.87% on 8/18) sit alongside it, and this desk has not tested whether they are related. **BRENT owns it.**
- **Brent rose (+0.52%) while WTI fell (−0.47%) on the same session** — the Brent-WTI spread is widening. **Noted, not interpreted, and not netted against the crack move.**
- **No gate fires.** No `RED-FT` or `REG-T` row references the diesel crack — **it remains an unregistered instrument despite being the pre-registered clean test for the refinery-outage mechanism** (anchor 7/27 §8). **That gap is worth BRENT's attention independently of today's level.**
