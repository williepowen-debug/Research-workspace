# Does a Hormuz reopening leave oil "structurally more expensive"? What is priced, and what shape a trade would take

**Asked by:** Will, 2026-10-09 ~11:10 ET (in session). **Status:** research note, not a proposal.
- Trade construction belongs to TERRY.
- Any trade needs Will's [Approve] (root rule #5).
- The WQ-192 stand-down is unchanged; nothing is armed and no $ moves.
- Read path taken before writing: TRADE.md, SPECS_OFFRAMP_ENTRY, SPECS_GATES, SPECS_TRADE_RULES (all complete).

## 1. What the curve already prices

Pulled 2026-10-09 11:11 ET. Single-vendor `last_price` on named NYMEX-listed contracts (`BZ..`, `CL..`, `HO..`). These are **not settles**, and back months are thin, so treat them as screening marks.

| Contract month | Brent | WTI | WTI − Brent | Diesel crack (HO×42 − WTI) |
|---|---:|---:|---:|---:|
| Dec 2026 | 104.82 | 90.98 | **−13.84** | **104.50** |
| Jan 2027 | 101.23 | 89.92 | −11.31 | 101.45 |
| Mar 2027 | 95.72 | 87.36 | −8.36 | 93.66 |
| Jun 2027 | 91.09 | 83.58 | −7.51 | 79.48 |
| Sep 2027 | 86.91 | 80.05 | −6.86 | 73.76 |
| Dec 2027 | 83.70 | 77.24 | **−6.46** | **69.44** |
| **2025 average (pre-war)** | | | **−3.58** (range −6.17…−0.89) | **32.45** |

The pre-war row is FRED/EIA **spot** data (DCOILWTICO, DCOILBRENTEU, DDFUELNYH), 244 matched days in 2025. That is a different basis from futures, so read it as an order-of-magnitude comparison, not a matched spread.

**Reading:**
- **The market already agrees with part of the premise:**
  - About half the freight-driven WTI discount fades within a year: −13.8 → −6.5.
  - The diesel crack falls by a third: 104 → 69.
- **Neither is priced back to normal by Dec 2027:**
  - WTI−Brent sits about **$2.90** wider than the 2025 average.
  - The diesel crack sits about **$37 above** its 2025 level, still roughly double.
- ⇒ **The trade is not "it stays expensive". That is consensus and already in the curve. The trade is "it stays MORE expensive than this curve says".**

## 2. Which cost components are durable

| Component | Expected behaviour after reopening | Evidence |
|---|---|---|
| War-risk insurance | **Fastest to unwind.** 6–10% of hull per voyage now (FT brokers, 10/7–8), against 0.15–0.25% pre-war (Marsh) | Opscon (A-tier relay): about 10% → about 2% within weeks of the June MOU. The SPECS_TRADE_RULES BH-07 letter expects war-risk halving 2–4 weeks after confirmed de-escalation |
| Tanker freight | Falls as Cape detours end and ton-miles shrink | No post-normalisation history exists in this regime (n=0 genuine reopenings, BE-10). L19: the effect of a reopening on tanker equities is **sign-indeterminate** |
| Refining capacity | **Most durable.** A Hormuz reopening restarts no damaged refinery | BE-16 (verbatim): *"A Hormuz de-escalation round-trips the crude premium; it does not restart Ras Laffan or un-shut Jazan."* Dallas Fed 10/8: fuel prices *"will likely remain unusually elevated relative to crude prices"* after Hormuz normalises. Its 6–8 mb/d global estimate is theirs and not adopted here |
| Inventory rebuild | Supports demand for crude and tankers after reopening | US SPR exchange returns are due in 2027 with premium barrels (BE-16; DOE). Global inventories are ~450M bbl below pre-war (Dallas Fed estimate) |

## 3. Shapes (concept only; TERRY constructs)

1. **Refiner leg: the most direct "cost survives normalisation" expression.** US Gulf refiners buy WTI-linked crude and sell into Brent-linked product markets. A durable product deficit **and** a durable WTI discount both widen their margin. **VLO ×1 is already held** under WQ-386 (exit rule `GATE-TERRY-VLO-HELD-01` on the matched diesel crack, below $90.16). Caveats:
   - The equity already discounts the forward crack path in §1.
   - The diesel crack is about $104 now. The curve prices **$69 by Dec 2027**, crossing the held share's **$90.16 exit line between Mar 2027 ($93.66) and Jun 2027 ($79.48) on the curve's own path**. That is an observation about the curve, not a grade. WQ-386 authorises leg-A observations only through 11/19/2026.
2. **Pair on a reopening: long refiner / short crude.** This is the registered off-ramp (USO bear put spread, 21–35 DTE, ~$500 defined risk, BE-14), with the refiner leg kept. BE-16's molecule scope supports holding product-side exposure while shorting crude. The off-ramp's own limits travel with it:
   - n=2 analogues;
   - zero genuine reopenings;
   - a day+2 latency ceiling;
   - the H1 day+9 exit.
3. **WTI−Brent spread: the purest test of the freight view.** If freight stays high, the discount stays wider than −6.46 for Dec 2027. Retail access is poor: there is no listed spread option at Will's brokers, and USO-vs-BNO is a lossy proxy because the two funds roll differently. Flagged for TERRY, not recommended.
4. **Tanker owners (FRO/DHT/STNG) and war-risk insurers: not recommended.**
   - Tankers: sign-indeterminate on a reopening (L19). Equities price forward earnings, and freight is the component that falls.
   - War-risk insurers: the line unwinds fastest, and it sits outside BRENT's domain (SHADE owns reinsurance).

## 4. What would falsify the view

- Dec 2027 WTI−Brent narrowing toward about −$3.6, or the Dec 2027 diesel crack falling toward about $32–35.
- Insurers cutting war-risk premiums by half within about 5 weeks of a confirmed deal (the BH-07 letter).
- Visible VLCC fixtures (about $530–600k/day in late September) diverging further below the >$1M Baltic benchmark, which would mean the benchmark is overstating freight.

## Lessons (`lessons_check`)

| Lesson | How it is handled here |
|---|---|
| L06 | Cracks used, not crude alone |
| L10 | Paper ≠ physical |
| L11/L16/L18/L19 | Announcement versus physical; tanker sign discarded |
| L15 | Off-ramp 21–35 DTE versus structural 60–90 DTE |
| L23 | Named contracts only |
| L21 | No gate drafted. **No threshold, gate or spec was written or amended.** |
