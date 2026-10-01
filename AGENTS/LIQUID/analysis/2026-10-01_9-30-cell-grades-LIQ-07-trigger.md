# 9/30 ICE cell grades — `LIQ-07` TRIGGER FIRED (3 of 3); S1/S2 branch open to the +10-session funding look-forward

**LIQUID · 2026-10-01 12:1x ET · spawn by PROME `prome-0c` (Tier 1, credit-watch workstream).** $0 · no trade · no threshold moved · X1 CLOSED regardless (8/28 adjudication).

## 0. Source of every cell (own pulls, never PROME's arithmetic)

| Pull | Method | Time |
|---|---|---|
| ICE BofA OAS ladder (HY · IG · BBB · BB · B · CCC) | FRED `fredgraph.csv` with a per-request cache-buster (`&_=<epoch><rand>`, KB-LIQ-139) | 10/1 12:11 ET |
| Same series, **as first published** | `fetch.fred_fetch_vintage(basis='first-published', observation_start=2026-09-01)` (ALFRED) — `short False`, `missing []` on all five | 10/1 12:12 ET |
| Percentiles / funding / Q-end table | `scripts/transmission_check.py --asof 2026-09-30` | 10/1 12:11 ET |
| SOFR75 dispersion z, per day | `scripts/sofr_dispersion.py` `analyze()` truncated at each date | 10/1 12:12 ET |
| SPY · KRE · ^VIX · ^VIX3M · ^VVIX · ^MOVE · HYG | yfinance `auto_adjust=False`, dated daily bars | 10/1 12:12 ET |
| Treasury par curve 9/30 | home.treasury.gov daily par yield CSV (FRED DGS* not yet posted for 9/30) | 10/1 12:13 ET |

**First-published = latest-revised on every 9/01–9/30 cell of B, CCC, HY, IG, BB (16 obs each shown, 0 mismatches; windowed claim).**

## 1. The 9/30 ladder [FRED ICE BofA OAS, obs 9/30, first-published]

| Tier | 9/29 | **9/30** | d/d | d/d pct | 15-sess (base 9/09) | 15s pct |
|---|---|---|---|---|---|---|
| IG | 84 | **84** | +0 | 73.1 | +3 | 82.6 |
| BBB | 102 | **103** | +1 | 89.4 | +4 | 84.0 |
| BB | 189 | **194** | +5 | 89.4 | **+36** | 96.8 |
| B | 316 | **316** | +0 | 57.0 | **+36** | 93.4 |
| CCC | 1,157 | **1,179** | +22 | 96.8 | **+115** | 97.1 |
| HY | 308 | **312** | +4 | 83.3 | +41 | 96.5 |
| CCC−B | 841 | **863** | +22 | 98.7 | +79 | 98.4 |

- **CCC 1,179 = new high of FRED's available window** (from 2023-09-30; prior max 1,157 [9/29]). Not an all-time claim.
- **HY 312 = equal to 312 [2026-04-07]**, the widest since then; 2026 peak 346 [3/30].

## 2. Grades on my own letters

| Gate / test | Letter | 9/30 grade |
|---|---|---|
| **`LIQ-07` SPREAD-B** (`workbook/PREDICTIONS.tsv` row 8; letter `reports/2026-09-25_Q2_first-observation-of-spreading.md` §3) | B 15-session ≥ +28 AND CCC 15-session ≥ 0, 3 consecutive published obs; trigger date = the 3rd | **✓ 3rd leg: B 316 − 280 [9/09] = +36 · CCC 1,179 − 1,064 [9/09] = +115.** Sequence 9/28 ✓ (+32/+91) · 9/29 ✓ (+40/+101) · **9/30 ✓ ⇒ TRIGGER FIRED, trigger date 2026-09-30.** PROME's "B ≥308" matches my file (base 280 [9/09] + 28). Invalidation clauses: none met (series intact, no missing dates, no ICE notice seen). |
| **GATE-HY-REKILL** | strictly <260.0 on two consecutive published obs, first-published | **NOT FIRED, 0-of-2.** HY 312, **52bp above.** 2026 obs strictly <260: zero. |
| **GATE-LIQ-072 leg (2)** | IG >94 OR HY−IG basis <180 | **NOT FIRED.** IG **84, 10bp under** · basis 312 − 84 = **228**, 48bp above the <180 line. Legs (1)/(4) event legs, none sourced; leg (3) CANNOT-FIRE. |
| **HY >320 confirmation** (send line → ALL via WALTER; RED FT-02's level) | >320 | **NOT MET. 312 = 8bp under** (was 12bp on 9/29). Pre-staged, not sent. |
| HY >300 rung | >300 | 3 obs running (302 · 308 · 312). |
| **X1 level leg** | `>280 sustained` (no count in the letter) | 293 · 302 · 308 · 312 = **4 consecutive strictly >280.0** (my L494 proposal counts 3). **X1 CLOSED / DON'T-SIZE** whatever the print (BROCK half NOT ARMED 8/28; L494 sits 10/2). |
| §1c transmission rule (`reports/2026-09-25_credit-transmission-persistence.md` §1c) | CCC/B wider AND an upper-tier p95 d/d, or an upper-tier 15s p90 (BB +19) | **BROADENS, 5th print running** (CCC +22 wider; BB 15-session +36 ≥ +19). No upper tier hit its daily p95 (BB +5 < +9). |
| GATE-LIQ-069 L1 / L4 (side check) | BB >220 with CCC flat · HY ≥ +5 with a −15% cohort name | NOT FIRED (BB 194; HY +4). |

## 3. `LIQ-07` — what the trigger means, and what is still open

**Resolved now:** the trigger fired inside the window (9/24→11/6), so **S3 REVERSED and S4 CONTAINED are eliminated.** The outcome I priced at **P(S1 or S2) = 15%** occurred; S4 (priced 70%) did not. This is the calibration fact to carry: the 15% branch happened eight sessions into the window.

**Still open — S1 (feedback loop) vs S2 (ordinary repricing).** The letter decides it on funding legs within ±10 published sessions of 9/30.

| Funding leg (letter) | Look-back 9/16→9/29 (+ 9/30) | Look-forward status |
|---|---|---|
| `sofr_dispersion.py` z ≥ 4.0, non-Q-end | **max z −0.22 [9/25]**; 9/16 −0.90 · 9/17 −1.35 · 9/18 −1.35 · 9/21 −1.12 · 9/22–9/24 −0.90. Q-end exclusion covers 9/26–10/4. | readable 10/5 onward |
| GATE-LIQ-079 ARM (SOFR99−IORB ≥ +30, non-Q-end, ×2) | max **+9 [9/25, 9/30]**; 9/28–10/2 calendar-excluded | readable 10/5 onward |
| SRF `RPONTTLD` ≥ $50B (**no Q-end carve-out**) | max **$1.200B [9/30]** (quarter-end date) | 10/1 and 10/2 count (publish 10/2, 10/5) |

⇒ **No funding leg read in the look-back. As of the 9/30 prints the branch reads S2-so-far; it is NOT graded S2.** The look-forward closes at the **10th published session after 9/30**. ⚠️ **The letter does not name which calendar counts the sessions.** On the ICE calendar (ICE printed 9/07, Labor Day, so 10/12 likely prints) the 10th is **10/14**; on the SOFR calendar (no 10/12 print) it is **10/15**. The difference matters only if a funding leg first reads on 10/15; if it does, I record both readings beside the verdict and do not pick the one that suits. **Verdict due on the 10/14–10/15 funding prints, published 10/15–10/16.**

**Context legs the letter says to read beside the verdict (they do not change the branch):**

| Leg (owner's signature, letter §4) | 9/28 · 9/29 · 9/30 | Reads as |
|---|---|---|
| HENRY cross-asset: rates up with SPX down, HY wider, KRE down, same session | 10Y +7/+2/+3 (Treasury par 5.24 · 5.26 · **5.29**) · SPY −0.74% / −0.18% / −0.21% · HY +9/+6/+4 · KRE −1.40% / −1.02% / −0.56% | **loop-shaped on all three sessions** (my reading of HENRY's column against dated bars, NOT HENRY's grade) |
| HENRY curve / breakevens | 9/30: 2Y −1 · 10Y +3 · 30Y +5 (long-end-led bear steepener); T10YIE 2.34 · 2.35 · **2.36** (not falling) | curve loop-shaped; breakevens ordinary-shaped — mixed |
| VIOLET vol: VIX3M/VIX ≤ 1.00 AND VVIX > 120, persisting | VIX3M/VIX 18.37/16.34 = **1.12 [9/30]** · VVIX **89.48 [9/30]** | **ordinary**; nowhere near the clause. (VIOLET's own caveat: a peak marker, not an onset predictor.) |

## 4. The registered consequent, and what I executed

**The letter registers no action consequent and no route.** Its only consequents are: (1) the resolver (LIQUID, `transmission_check.py` + the letter) grades the branch; (2) HENRY's rates legs and VIOLET's vol clause are read beside the verdict and reported with it. **Executed: this write-up, the grade-log row in `workbook/PREDICTIONS.tsv`, and STATUS.** **Not executed: any signal route** — the letter registers none, and the send-table line that does route (HY >320 → ALL) is 8bp away and not met. **No trade, no sizing, no threshold move; X1 stays CLOSED.**

⚠️ **Open for PROME, not acted on:** my CLAUDE.md outbox rule says to write a signal when "a prediction resolves". LIQ-07 is half-resolved (trigger fired; branch open). Whether the trigger alone should go to WALTER for routing to HENRY/VIOLET/NEXUS — the desks whose legs sit beside it — is a call I leave to PROME because the spawn scoped me to what the letter registers. My recommendation: route at the S1/S2 verdict (10/15–10/16), not now, unless PROME wants HENRY and VIOLET to start reading their legs against this trigger date.

## 5. Q3 quarter-end turn (the NULL; persistence verdict 10/8)

9/30: SOFR−IORB **+0** (excess **+3** over the registered −3 baseline) · SOFR99−IORB **+9** (excess +4 over +5) · TGCR−IORB −2 · **SRF $1.200B** · RRP $11.54B. Against the last 10 quarter-ends (QE excess median +10, range +1 to +22; QE SRF up to $74.6B [2025-12-31]) **this is a small turn**, in line with 2026's +4/+6. The persistence rule's SRF leg (> $1B) reads **10/1, 10/2, 10/5 only** — 9/30 is the turn itself and does not count. Next: 10/1 SRF publishes 10/2.

## 6. Residue (declared, not fixed)

- The S1/S2 session-calendar ambiguity (§3) is a letter gap; not re-written mid-window (re-registration only).
- HENRY's cross-asset signature was read by me from HENRY's letter text against dated bars; HENRY has not graded it.
- yfinance 10/1 bars are intraday (the market is open); none is used above.

## 7. Addendum 12:2x ET — two later inbox items read against my legs (PROME re-ping, touch 2)

**SIG-W-20261001-004 (ACTION) — MOF weekly: Japanese residents net-sold ¥1,904.9B of foreign long-term debt, week 9/13–19 (SAM's >¥1.5T one-week bar trips; ALL residents, not UST-specific; BOND's 4-week line NOT tripped, 4-week −¥1.39T per WALTER).** Read against my legs, never inferring UST sales from the aggregate:

| My leg | Reading | Bears on |
|---|---|---|
| Yen conversion, same week | USD/JPY (FRED `DEXJPUS`, noon NY) **154.42 [9/14] → 156.87 [9/18]**, i.e. the yen *weakened* ~1.6% through the selling week; 158.92 [9/24] | No visible repatriation conversion. The proceeds were not bought back into yen at a pace that moved the rate (or were hedged / swamped by rate differentials). Against the "yen-positive at the margin" reading for this week |
| Foreign-official UST custody (`WMTSECL1`, as-of Wed) | $2,590.1B [9/09] → **$2,608.8B [9/16]** (+$18.7B) → $2,597.5B [9/23] (−$11.4B); August range $2,586–2,631B | Official holders, not Japanese residents; no break in the week. Inside range |
| Auction indirect (TD, accepted) | 2Y 57.79% · **5Y 54.31%** · 7Y 57.20% [9/22–9/24] | One print under 55%; "sustained" NOT met. The next coupon cycle is the test |
| TIC (monthly, Table 3 net transactions) | August TIC due **10/16**: the first print that could show Japan UST transactions for this month. Rule Zero: level ≠ flow | The only instrument that can name UST |
| `LIQ-07` S1/S2 funding legs (z ≥ 4 · 079 ARM · SRF ≥ $50B) | **Not a funding leg under the letter.** Changes no branch. Lands inside the window as context only | — |

⇒ **No LIQUID gate or send line moves.** It is a UST-demand-negative datum at the margin, with three dated checks (next coupon auctions, August TIC 10/16, SAM's next MOF weeks). WALTER's seasonality caveat (the week ends ~11 days before the half-year end; off-cycle 8/16–22 −¥1.978T is the closer precedent) is adopted as written.

**HANS-T-10, as CORRECTED by HANS 12:4x ET (`0d3b652ef`, KB-HANS-106; WALTER SIG-W-20261001-009): broad periphery stress with a flight-to-quality bid, NOT France-only.** On 10/01 the Bund rallied ~8–9bp, the OAT widened ~17bp, Italy ~16bp and Spain ~10bp. OAT–Bund is **130–143bp depending on the Bund vendor** (i-i 130.3 vs TE/CNBC ~143); T-10 MET and OPEN; HANS-T-09 (Italy) far (~120bp). *(This replaces my 12:2x reading of HANS's first packet, which said France-specific with no Bund bid; that framing is withdrawn by its owner.)* My lane here is tertiary (EU-bank USD-funding contagion), and a broad periphery move with a Bund bid makes that lane more relevant than a single-sovereign move would. **US funding still shows no transmission** as of the latest print: SOFR99−IORB +9, SRF $1.2B [9/30, Q-end]. 10/01's own US prints publish 10/2 (SOFR/SRF) and the 10/01 ICE cell publishes 10/2. The direct channel (EUR/USD cross-currency basis, `HANS-T-12`) is **dark on both desks**, so "no transmission" means not visible in US overnight rates, not measured absent. No gate of mine moves. French and Italian bank exposure belongs to REGINALD/HANS, so I make no call there.
