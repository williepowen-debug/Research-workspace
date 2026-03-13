# Fed T-Bill Purchases & Repo Crisis Parallel

**Created:** 2026-03-13
**Author:** Prome + Will
**Status:** Active research thread — LIQUID investigating

---

## The Signal

Fed T-Bill holdings (FRED: WSHOBA) were flat at ~$195B for 18 months (Apr 2024 - Dec 15, 2025). Starting Dec 17, vertical ramp:

| Date | Holdings ($M) | Δ Weekly |
|------|--------------|----------|
| Dec 15, 2025 | 195,493 | — |
| Dec 17 | 200,936 | +5,443 |
| Dec 24 | 224,068 | +23,132 |
| Dec 31 | 233,592 | +9,524 |
| Jan 7 | 234,758 | +1,166 |
| Jan 14 | 248,755 | +13,997 |
| Jan 21 | 251,108 | +2,353 |
| Jan 28 | 266,532 | +15,424 |
| Feb 4 | 282,547 | +16,015 |
| Feb 11 | 298,167 | +15,620 |
| Feb 18 | 306,429 | +8,262 |
| Feb 25 | 321,306 | +14,877 |
| Mar 4 | 337,199 | +15,893 |
| Mar 11 | 351,895 | +14,696 |

**Total: +$156B in 12 weeks.** Exceeds 2020 COVID peak ($326B). Source: FRED WSHOBA series, verified Mar 13.

---

## The 2019 Repo Crisis — What Happened

### Trigger (Sep 17, 2019)
- Quarterly corporate tax payments + $54B Treasury auction settlement hit same day
- Both drained reserves from banking system simultaneously

### What Broke
- Overnight repo rate spiked from ~2% to **10%** (some trades higher)
- Effective fed funds rate breached Fed's own target range — Fed lost control of its rate
- Money market funds dependent on repo started seizing

### Fed Response
- Emergency same-day repo operations: $53B day one, $75B day two
- Scaled to $120B/day in overnight + term repos within weeks
- October 2019: announced T-Bill purchases at $60B/month ("not QE")
- Bill holdings went from near-zero to $326B by March 2020

### Root Cause
- Years of QT had drained reserves below the "minimum comfortable level"
- Nobody knew where the floor was until they hit it
- Reserves were concentrated in large banks — smaller banks were already stretched
- The trigger was mundane; the vulnerability was structural

---

## Why 2026 Setup Is Worse

| Factor | 2019 | 2026 |
|--------|------|------|
| RRP buffer | Large (excess reserves parked) | $0.278B (effectively zero) |
| UST demand | Stable (foreign buying intact) | Demand hole: $40-72B/mo (Gulf involuntary) |
| Reserve concentration | Moderate | Worse (Big 4 hold most) |
| Rate environment | Cutting (could ease) | Trapped (stagflation — can't cut) |
| External shocks | None | Oil shock, war, Hormuz closed |
| Private credit | Stable | Melting down (6 funds gated in 5 weeks) |
| CRE maturities | Manageable | $875B in 2026 (MBA) |
| Trigger needed | Tax + auction (mundane) | Multiple stress vectors already active |

### The Composition Shift
Fed is buying bills (short duration) while letting notes/bonds/MBS roll off under QT:
- **Headline:** Balance sheet shrinks (QT continues)
- **Reality:** Short-end liquidity increases (stealth easing)
- Bills are the most liquid instrument — can be repo'd out or sold instantly
- This is the Fed building an emergency buffer without announcing emergency

### Pre-Positioning Hypotheses
1. **Bank funding stress** — bills on hand for emergency repo operations
2. **RRP drain replacement** — rebuilding the liquidity buffer through a different channel
3. **Emergency facility prep** — operational flexibility for BTFP-style programs
4. **T-Bill market functioning** — absorbing Treasury short-end issuance to prevent bill yield spikes

---

## Plumbing Dashboard (Verified Mar 13)

| Indicator | Current | Status | Notes |
|-----------|---------|--------|-------|
| SOFR | 3.64 | 🟢 | Stable since Jan. No spikes. |
| EFFR | 3.64 | 🟢 | Within target range |
| EFFR vs IORB | -1bp | 🟢 | Normal (EFFR below IORB) |
| SRF / Repo ops | ~$0 | 🟢 | Near zero mid-month. Calendar spikes only. |
| Discount window | $4.7B | 🟡 | 3x 2024 lows. Peaked $9.9B Dec 2025 — coincides with bill ramp start. |
| SOFR 99th %ile | 3.73 | 🟢 | Only 9bps above median. No tail stress. |
| SOFR 1st %ile | 3.60 | 🟢 | Only 4bps below median. |
| SOFR spread (99-1) | 13bps | 🟢 | Tight. Year-end widened to 30bps (normal). |
| 3M Fin CP rate | 3.68 | 🟢 | Tracking SOFR, no blowout |
| RRP | $0.278B | 🔴 | Buffer effectively zero |
| Fed T-Bill holdings | $352B | 🔴 | +$156B in 12 weeks. Exceeds 2020 peak. |

**Key findings:**
1. Discount window borrowing peaked at $9.9B in Dec 2025 — the exact week Fed began buying bills aggressively. Bill purchases appear to be a direct response to emerging funding stress.
2. All market-facing indicators (SOFR, EFFR, CP, repo) are calm — the intervention is WORKING.
3. This is "successful suppression" — underlying vulnerabilities (RRP drained, Gulf demand hole, private credit gates, $875B CRE maturities) haven't resolved, they're being papered over.
4. Critical question: how long does the buffer hold when FOMC (Mar 17-18), BOJ (Mar 18-19), Taiwan LNG (Mar 15), and private credit stress hit simultaneously?

### Additional Findings (Claude research, Mar 13)

**SRF Stigma — Usage UNDERSTATES Stress:**
- Primary dealers told NY Fed in Nov 2025 meeting they are RELUCTANT to use SRF — borrowing is seen as "visible sign of weakness" the market would interpret as liquidity stress.
- Implication: SRF usage near zero does NOT mean no stress. Banks may be avoiding the facility while funding through other channels (discount window, FHLB, bilateral repos).

**October 31, 2025 — Warning Shot:**
- Fed executed $29.4B overnight repo through SRF — **largest single-day operation since dot-com era**
- Occurred as bank reserves hit $2.8T — **lowest in 4+ years**
- This was 6 weeks BEFORE the bill-buying ramp began in December

**December 2025 FOMC — SRF Limit Removed:**
- Fed quietly removed the aggregate daily SRF limit → moved to **full allotment** (all bids accepted in full)
- Per-counterparty limit remains at $40B
- You don't uncap a backstop facility if you think everything's fine — this is pre-positioning

**December 31, 2025 — SRF Hit $75B:**
- Year-end spike, normalized to zero by early January
- Arbitrage dynamic: borrow SRF at 3.75%, lend to repo market at higher rates

**SOFR Policy Transmission Deteriorating:**
- RMSE of SOFR vs other money market rates has climbed since late 2024
- Accelerated in late 2025 as reserves declined to post-pandemic lows
- Dallas Fed research: policy transmission from fed funds to broader money markets may have deteriorated
- Implication: the Fed's rate target is becoming less effective at controlling actual funding costs

**Timeline of Fed Pre-Positioning:**
1. Oct 31: $29.4B SRF (largest since 2000s). Reserves at $2.8T (4-year low).
2. Nov: Primary dealers tell Fed they won't use SRF (stigma).
3. Dec 11: Rate cut (3.90 → 3.65 IORB).
4. Dec 17: Bill purchases begin ($200B, first move in 18 months).
5. Dec FOMC: SRF aggregate limit removed — full allotment.
6. Dec 31: SRF hits $75B (year-end).
7. Dec 24 → Mar 11: Bill purchases ramp $224B → $352B (+$128B in 11 weeks).
8. Current: $352B in bills (exceeds 2020 peak), plumbing appears calm on surface.

**FHLB Issuance Surge — CONFIRMED (Mar 13):**
Data from FHLB Office of Finance (fhlbanalystdata.xlsx, debt through Feb 2026):

| Metric | 2025 (monthly avg) | 2026 Jan-Feb (monthly avg) | Change |
|--------|-------------------|---------------------------|--------|
| Bond issuance | $83.4B | $105.9B | **+27%** |
| Discount note issuance | $121.5B | $163.6B | **+35%** |
| Total issuance | ~$205B | ~$269B | **+31%** |

Composition shift: 77% of 2026 bonds are Simple Floaters (vs 59% in 2025). Banks taking floating rate = need flexibility or can't commit to fixed.

Average trade size also up: $264M in 2026 vs $167M in 2025 — larger deals = bigger institutions drawing.

This confirms banks are tapping FHLB (no-stigma channel) at elevated pace — consistent with pre-crisis contingency funding behavior.

**Complete Back-Channel Funding Timeline:**
1. Oct 31: SRF $29.4B (largest since 2000s). Reserves $2.8T (4yr low).
2. Nov: Dealers tell Fed they won't use SRF (stigma).
3. Dec 11: Rate cut.
4. Dec 17: Bill purchases begin (first move in 18 months).
5. Dec FOMC: SRF cap removed → full allotment.
6. Dec: Discount window peaks at $9.9B.
7. Dec 31: SRF hits $75B (year-end).
8. Jan-Feb: FHLB issuance surges 31% above 2025 pace.
9. Dec-Mar: Fed buys $156B in bills → $352B (exceeds 2020 peak).
10. Surface indicators (SOFR, EFFR, CP): all calm. Intervention working — for now.

---

## LCLoR — The Invisible Threshold

**Lowest Comfortable Level of Reserves (LCLoR)** = the behavioral threshold where banks stop lending reserves and start hoarding. Not a regulatory minimum — a survival instinct.

**Current state:** Total reserves at $2.8T (4-year low). But distribution is highly unequal:
- G-SIBs (JPM, BofA, Citi, Wells): hold lion's share, comfortably above LCLoR
- Regionals (our KRE targets): running thin — FHLB surge confirms active reserve management
- Community banks: some may already be AT LCLoR

**Richmond Fed research:** "Gini coefficient" of reserves is highly concentrated. Average looks okay. Distribution is dangerous.

**The sequence when regionals hit LCLoR:**
1. Stop lending → credit tightens → economy slows
2. Compete for funding → costs rise → margins compress
3. Sell assets for cash → prices fall → losses materialize
4. CRE/C&I loans can't refinance → defaults → more losses → repeat

**Why this is our KRE edge:** Market prices KRE on aggregate reserves ("$2.8T is plenty"). We price on distribution ("regionals running on fumes, FHLB proves it").

**Reserve drain catalysts ahead:**
- Gulf UST selling ($40-72B/mo) → Treasury issues more → drains reserves
- April 15 tax payments → cash moves bank→Treasury → reserve drop
- Private credit redemptions → forced sales → cash demands spike
- BOJ rate hike / Japan repatriation → Japanese banks pull dollar funding

---

## Consensus vs. Our View

| | Consensus (Gemini/market) | Our View |
|---|---|---|
| **Framework** | Read market indicators → assess health | Read Fed behavior → assess fragility |
| **SOFR/EFFR** | Calm = healthy | Calm = intervention working |
| **CP-OIS 4bps** | All clear | Was fine Aug 2019 too |
| **SRF at zero** | No stress | Stigma means zero ≠ no stress |
| **FHLB** | "Routine" | +31% surge (verified via primary data) |
| **Reserves $2.8T** | Adequate | Distribution dangerously unequal |
| **Conclusion** | System is fine, just lean | System held together by record intervention; margin of safety is thinnest since 2019 |

**Key insight:** In 2019, every surface indicator was fine until Sep 17. Then repo went 2% → 10% in one morning. The plumbing doesn't give slow warnings — it gives binary breaks. The Fed's behavior (not the market's) is the leading indicator.

**Gemini FHLB claim debunked:** Gemini characterized FHLB issuance as "completely routine." Our primary data (fhlbanalystdata.xlsx from FHLB Office of Finance) shows +31% above 2025 pace. Always verify against primary sources.

---

## Stress Escalation Stages

```
Stage 1 (NOW):     FHLB +31%, discount window elevated, Fed buying bills at record pace.
                   Surface: SOFR/EFFR/CP calm. "Everything's fine."

Stage 2 (NEXT):    Catalyst overwhelms buffer (FOMC/BOJ/Taiwan LNG/private credit).
                   FHLB spikes further. Discount window jumps.
                   Someone uses SRF despite stigma. SOFR tails widen.
                   Surface: first cracks visible.

Stage 3 (BREAK):   SOFR tails blow out. CP spreads widen.
                   Money markets seize. Fed announces emergency facility.
                   Market: "how did nobody see this coming?"
                   Us: we saw it in the FHLB data and the Fed's bill purchases.
```

**Watch triggers for Stage 2:**
- SOFR 99th percentile > 25bps above median (currently 9bps)
- SRF usage on non-calendar dates
- FHLB issuance acceleration in March data
- Discount window > $10B sustained
- Cross-currency basis swaps deeply negative (dollar funding stress for foreign banks)

---

## Key Questions (LIQUID investigating)

1. How does this connect to the UST demand hole and upcoming FOMC (Mar 17-18)?
2. Is $352B enough? In 2019 they needed $120B/day in emergency repos at peak.
3. What's the transmission to TLT shorts and rate path?
4. At what point does the bill-buying become visible enough to move markets?
5. What would a 2026 repo event look like — would it be repo, or would stress show up differently (money market funds, commercial paper, private credit NAV)?

---

## Cross-Agent Relevance

| Agent | Connection |
|-------|-----------|
| LIQUID | Primary — funding stress, rate path, plumbing |
| HENRY | Repo stress → VIX regime change, vol event |
| ZHAO | Gulf UST selling forces Treasury to issue more bills → Fed must absorb |
| SAM | Japan repatriation (Apr 1 FY-end) adds to UST selling pressure |
| BROCK | Private credit redemptions → forced asset sales → repo demand |
| REGINALD | CRE maturities → bank funding needs → reserve pressure |

---

## Implications for Positions

- **TLT puts:** Reinforced. Fed can't cut, plumbing stress pushes long yields higher, and if emergency facilities needed → confidence shock
- **HYG puts:** Reinforced. Credit stress + funding stress = amplification loop
- **KRE puts:** Reinforced. Smaller banks most exposed to reserve scarcity

---

*LIQUID research directive spawned Mar 13. Update this doc with findings.*
