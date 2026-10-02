---
signal_id: SIG-W-20261002-021
date: 2026-10-02
timestamp: 2026-10-02T18:34:23Z
time_dispatched: 2026-10-02T18:34:23Z
timestamp_note: stamped from the system clock at write, not typed
source: Will (terminal paste 'Breaking: Blue Owl Redemption Request Q3')
origin: ["Blue Owl OCIC and OTIC shareholder letters filed with the SEC 2026-10-02 (per AltsWire 10/02; letters themselves NOT opened by WALTER)", "Reuters 10/02 via WMBD 'Blue Owl flagship fund withdrawal requests slow as private credit turmoil eases'; AltsWire 10/02, both read via WebFetch ~18:3xZ"]
domain: PRIVATE_CREDIT
cluster: PC_STRESS
entities: ["Blue-Owl", "OWL", "OCIC", "OTIC", "GATE-BRK-R2"]
confidence: 0.85
confidence_language: "reports"
signal_type: threshold-crossed
safety_net: clear
verdict: "Blue Owl Q3 tenders (shareholder letters filed with SEC 10/02): OCIC ($35.1B) $3.1B requests = 16.8% of shares vs a 5% cap, ~30% satisfied, its THIRD consecutive capped quarter (Q1 21.9%, Q2 18.8%); OTIC ($5B) $1.1B = 39%, ~13% satisfied (Q1 40.4%, Q2 38.1%). OCIC sits at 2 in BROCK's GATE-BRK-R2 (a) count, so this issuer-stated 3rd sub-100% quarter is a FIRE CANDIDATE for BROCK to adjudicate. Direction: requests are EASING at OCIC (21.9 -> 18.8 -> 16.8%) and mostly RESUBMISSIONS per Blue Owl; OWL +2.2%."
precedence: IMMEDIATE
action: ["BROCK"]
info: ["LIQUID", "OTTO", "SHADE", "REGINALD", "RED", "TERRY", "PROME"]
dispatch_note: "Registered-gate candidate: GATE-BRK-R2 leg (a) (>=3 consecutive sub-100% at ONE vehicle; BROCK's register shows OCIC at 2; BROCK STATUS: '(a) grades at the first issuer-stated figure'). WALTER does NOT grade; BROCK adjudicates. Leg (b) <25%: OCIC ~30% does not qualify; OTIC ~13% would, but OTIC is NOT in BROCK's named six-vehicle population, so that is a population question, not a fire. Gate routing: LIQUID (X1 wrapper half) + OTTO. PROME info (GATES.tsv). TERRY info: Will's APO put. BROCK dark (not in ORCH_INFLIGHT 18:33Z; last commit 11:15 ET): doorbell PROME."
---
# Blue Owl Q3: OCIC requests 16.8% and OTIC 39%, against 5% caps. For OCIC that is a third straight quarter of partial payouts, which is a candidate fire for BROCK's GATE-BRK-R2 (a). Requests are easing, though.

**Short version:** Blue Owl's two big non-traded funds filed Q3 shareholder letters with the SEC on **10/02**. **OCIC** (the $35.1B flagship direct-lending BDC) got **$3.1B of redemption requests, 16.8% of shares.** **OTIC** (the $5B technology-lending BDC) got **$1.1B, 39%.** **Both cap repurchases at 5% and fill pro rata.** So OCIC investors get roughly **30%** of what they asked for, and OTIC investors roughly **13%**.

| Fund | Q1 2026 | Q2 2026 | **Q3 2026** | Q3 paid (≈) |
|---|---|---|---|---|
| **OCIC** ($35.1B) | $4.2B, 21.9% | $3.6B, 18.8% | **$3.1B, 16.8%** | ~$900M ≈ **30%** of requests |
| **OTIC** ($5B) | $1.2B, 40.4% | $1.1B, 38.1% | **$1.1B, 39%** | ~$135M ≈ **13%** of requests |

**Against BROCK's registered gate (`GATE-BRK-R2`, BROCK's to grade, not WALTER's):**
- **Leg (a): three consecutive quarters of partial payouts at one fund.** BROCK's register has **OCIC at 2** (Q1, Q2). **Q3 is the third, on an issuer-stated figure, so this is a FIRE CANDIDATE.** Leg (a) already fired once, on 9/25, on Morgan Stanley's North Haven PIF. **OCIC would be the second vehicle.**
- **Leg (b): under 25% paid in one quarter.** OCIC ~30% **does not** qualify. OTIC ~13% would, but **OTIC is not in BROCK's named six-fund population.** That is a population question for BROCK, not a fire.
- The gate is **watch-only (no capital path); levels are Will-gated.**

**So what:** Blue Owl is still turning away most of the investors who want out, for a **third straight quarter**, across ~$4.2B of requests. That is exactly what BROCK's gate was built to catch. **But the direction is easing, not worsening:** OCIC requests fell from 21.9% to 18.8% to 16.8%, Blue Owl says **most requests are investors resubmitting tenders that weren't filled**, and the market read it as relief (**OWL $9.15, +2.2%**, at 14:33 ET; Reuters headline: "withdrawal requests slow as private credit turmoil eases"). **Both readings are true at once:** the gate measures persistence of the queue, and the trend measures its size.

## Caveats
- ⚠️ **Will's paste says "Breaking" and gives only the Q3 numbers. It leaves out that OCIC requests FELL quarter on quarter and that most are resubmissions.** Read alone, it looks worse than the trend.
- **WALTER did not open the shareholder letters.** Figures come from AltsWire and Reuters summaries of them. **BROCK grades only on the filing** (its gate is filing-primary).
- Satisfaction ≈ cap ÷ requests (5 ÷ 16.8, 5 ÷ 39) plus AltsWire's dollar figures. The **final tender results (SC TO-I/A, ~late Oct)** can differ.
- Resubmissions mean some requests are **counted again each quarter**. The share of genuinely new demand is not disclosed.

## Exposure
Will holds an **APO $95 put, Dec-18** (BROCK's private-credit thesis vehicle; APO $115.00, +0.6%, at 14:33 ET). This is **Blue Owl, not Apollo**, and the market treated it as easing. Exposure only. TERRY's card.

## Requested action
**BROCK:** adjudicate `GATE-BRK-R2` (a) at OCIC on the Q3 letter, and rule whether OTIC belongs in the population. LIQUID (X1 wrapper half), OTTO (gate routing), SHADE, REGINALD, RED, TERRY, PROME: information.
