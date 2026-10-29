# VIOLET -> PROME — 2026-10-29 — WQ-545 energy-vol leg (VIOLET)

**Commission:** WQ-545 (Will 15:34 ET "ok go", PROME/WILL_QUEUE.md row 545). VIOLET leg only; $0; no band, threshold or letter change; no trade construction (TERRY builds, Will approves under root rule #5). Evidence and scripts: `AGENTS/VIOLET/research/2026-10-29_WQ545/`.

## Headline for the cross-desk read

**The OVX/VIX canary is not a fresh 10/28 shock signal; it is a re-fire inside a regime that has been on since July.** On VIOLET's own ledger (`workbook/OVX.tsv`) the canary has printed **FIRE on 28 days since 2026-07-01** (18 WATCH, 5 CALM). On the Cboe-history basis, 34 fire days since 7/13, with one gap over 20 sessions inside it. Across that whole stretch (7/13 → 10/28) VIX ranged **14.21–20.66** on official closes and SPX rose **+3.04%** (7,515.34 → 7,743.98). **The canary has not transmitted into equity vol in this regime.** Oil vol has run high relative to equity vol for 3½ months. So from VIOLET's side the 10/27–10/28 cluster reads as an energy-local repricing on top of a standing oil-vol premium, **not** evidence of a shock passing into equity vol. Credit agrees with that (HY 314bp [FRED 10/28]). ⚠️ This is a statement about transmission to date, not a forecast that it cannot transmit.

⚠️ **Correction to my 10/29 catch-up memo and KB-VIO-357:** they described 10/28 as the canary's "first FIRE after four WATCH closes". That is locally true (the last FIRE before it was 10/02) but omits the regime context above. It overstated the novelty.

## (1) Prior fires: what followed (n small; read as weak evidence)

Rule = the canary's own: OVX/VIX ≥ p95 of the ratio AND OVX ≥ p75 of OVX. Data: Cboe OVX/VIX daily history 2009-09-18 → 2026-10-28 (n = 4,300 sessions); SPX from yfinance ^GSPC. Episodes = first fire after >20 sessions with none. Two ladders: **A** full-sample (as the live canary computes; look-ahead) and **B** expanding as-of-date (no future data).

| Horizon | A: n | A: VIX median / up-share | A: SPX median / down-share | A: OVX median | B: n | B: VIX median / up-share | B: SPX median / down-share | Unconditional VIX up-share / SPX down-share |
|---|---|---|---|---|---|---|---|---|
| 5 sessions | 14 | +1.5% / 57% | +0.12% / 43% | −8.0% | 13 | +1.6% / 62% | +0.23% / 46% | 46% / 40% |
| 10 sessions | 14 | +8.2% / 64% | −0.61% / 57% | −7.6% | 13 | +3.2% / 62% | −0.44% / 62% | 46% / 36% |
| 20 sessions | 14 | +2.5% / 57% | +1.11% / 43% | −17.1% | 13 | +6.0% / 54% | +0.73% / 46% | 46% / 33% |

**Honest read:**
- With n = 13–14 episodes, a 57–64% VIX up-share against a 46% unconditional base is roughly 1.5–2 extra "up" episodes out of 14. That is **not distinguishable from noise** at this sample size.
- The dispersion is wide: VIX at 20 sessions ranges from −33% (2020-04) to +30% (2022-03).
- The only consistent feature is that **OVX itself mean-reverts**: median −17% at 20 sessions on both ladders.
- The current episode is the July 2026 one (7/13, ratio 3.51). At 20 sessions it gave VIX −9.9% and SPX +3.16%. The 10/28 print continues that episode rather than starting a new one.

Full table: `ovx_fire_study_output.txt`.

## (2) 10/29 official close — PARTIAL (finals not yet published)

**Checked 16:31 ET (from `date`):** the Cboe daily-history CSVs (VIX, VVIX, SKEW, OVX, VIX3M, VIX9D) still end at **10/28**, so there is no official 10/29 final yet. ⚠️ Cboe's CDN now answers these URLs with a 307 redirect; a fetch that doesn't follow redirects reads it as "not published" and keeps waiting (this session's watcher did exactly that; the check was redone with redirects followed).

**Provisional read from Cboe delayed quotes (session closes, not archive finals):**

| Series | 10/29 quote | Quote time | 10/28 final |
|---|---|---|---|
| VIX | 17.20 | 16:15:01 ET | 16.91 |
| VVIX | 98.01 | 16:15:01 ET | 96.61 |
| VIX3M | 19.37 (3M/VIX 1.126) | 16:15:01 ET | 19.22 |
| OVX | 57.16 | 15:02 CT (16:02 ET) | 58.59 |
| SKEW | **no 10/29 bar** — quote still 148.74, last trade 10/28 17:00 | — | 148.74 |

- **Canary: persists, provisionally.** OVX/VIX = 57.16 / 17.20 = **3.32**. That is ≥ p95 on both bases (the ledger's 3.24 and Cboe full-sample 3.31; marginal on the latter), with OVX ≥ p75. It is FIRE on quotes; official grade at the next boot.
- **SKEW bar for RED FT-10:** **not available** at 16:31 ET. FT-10 exit count stays 0 of 4 through 10/28 (148.74). The 10/29 bar is the first leg of VIOLET's next boot.
- **Cheap-tail distance widened slightly** on quotes: L2 VIX 17.20 needs **−1.20** to ≤16 (was −0.91); L1 VVIX 98.01 needs **−8.01** to ≤90 (was −6.61). Still DORMANT 2/4.

## (3) Cheap-tail state

DORMANT 2/4 on every session 10/22–10/28. On 10/28 official:

| Leg | Line | 10/28 value | Distance to arm |
|---|---|---|---|
| L1 VVIX cheap | ≤ 90.0 | 96.61 (p64.8) | **−6.61** |
| L2 VIX complacency | ≤ 16.0 | 16.91 (p47.8) | **−0.91** (closest) |
| L3 SKEW elevated | ≥ 140.0 | 148.74 (p92.2) | met, cushion 8.74 |
| L4 event-boxed | HIGH/MED catalyst ≤ 21d | BOJ 10/30, Election Day 11/03, payrolls 11/06, CPI 11/10 | met |

**What arms it:** a further calm-down in which VIX closes ≤16 *and* VVIX closes ≤90 while SKEW holds ≥140. In the last 60 sessions (8/05–10/28) that joint condition held on **30 of 60 days**, most recently **10/13** (the 4/4 OPEN before CPI, WQ-418 PASSED). So it is not exotic; it is roughly a 1–2 session calm-down away. An OPEN alert goes to PROME by packet for a WQ row (route text corrected 10/29); it is never a trade.

## (4) Event pricing vs the realized FOMC reaction

| Item | Figure (dated) | Read |
|---|---|---|
| FOMC 10/28 realized | SPX +0.28% (7,722.60 → 7,743.98), QQQ +0.60%, VIX −3.48% (17.52 → 16.91) [closes 10/27→10/28] | The market sold vol through a hawkish-dissent hold |
| **AMZN** (reports after 10/29 close) | 10/30 ATM straddle **7.92%** of spot (K 245, spot 245.03, IV ~1.34; yfinance chain 15:35 ET 10/29) vs median absolute 1-day post-earnings move **5.87%** over the last 8 reports (mean 6.23%) | **Rich** vs its own history by ~2 points. A >±7.9% move is needed to beat the straddle; 2 of the last 8 reports cleared it (+15.32%, +9.58%) |
| **AAPL** | ⚠️ **Probably NOT tonight.** The vendor calendar (yfinance) gives **11/02** after the close. The chain agrees: the 10/30 straddle is 1.04% (IV 0.178, no event premium); the 11/04 straddle is **4.03%** (IV ~0.37) | vs median absolute post-earnings move **1.92%** (mean 2.46%, last 8): **rich** by ~2 points if 11/02 is right. ⚠️ Date unverified at Apple IR (page renders by script); verify before anyone keys a decision on "AAPL tonight" |

**Implication for Will's lines (vol facts only; construction is TERRY's):**
- **Energy (USO calls, VLO ×3):** the oil-vol premium they sit in has been high for 3½ months, and in every prior episode OVX mean-reverted (median −17% at 20 sessions). That is a headwind for long-oil-option *premium* whatever the oil direction; BRENT owns direction. No expiry advice (USER.md).
- **VLO (one dated line; VIOLET keeps no single-name vol ledger, so this is a one-off vendor read and HENRY owns equity):** Nov-20 ATM (K 380) call IV **52.8%** at spot 380.42 [yfinance 10/29 15:37 ET, bid/ask 19.40/21.20]. Raw closes 426.76 [10/26] → 387.34 [10/27] (−9.2%) → 388.48 → 380.42 intraday. The vendor calendar dates its Q3 report 10/22 pre-market (EPS 23.90 vs 21.23 est.), so the 10/27 drop was **not** the earnings session. Cause unchecked.
- **Gas leg (per PROME correction 15:37 ET):** read the TTF leg as "traded above €100/MWh intraday 10/28, first time since 2022", not "settled above $100". This does not change VIOLET's leg; the canary is OVX (crude oil vol), not gas.
- **QQQ Nov-20 690/670 put spread:** index vol is not being bid. VIX 16.91 [10/28], COR1M 8.73 (dispersed), and the oil-vol canary has not transmitted since July. Single-name event premium (AMZN) is rich, but index correlation is low, so a single-name miss is more likely to move the stock than the index. QQQ 713.69 [10/29 ~15:35 ET intraday, yfinance — not a close] sits 23.69 above the 690 strike.

## COMPLETION — VIOLET — 2026-10-29 (WQ-545 leg)
STATUS: PARTIAL — legs 1, 3 and 4 are complete; leg 2 is on provisional quotes because the Cboe 10/29 finals were unpublished at 16:31 ET
CHANGED: this packet; AGENTS/VIOLET/research/2026-10-29_WQ545/ (study scripts + outputs); KB-VIO-359 (correction to KB-VIO-357's novelty framing); SCRATCH next-boot first leg
RESULT: canary FIRE on 28 ledger days since 7/1 with VIX 14.21–20.66 and SPX +3.04% (7/13→10/28) — no transmission; prior-fire VIX up-share 57–64% vs 46% unconditional at n=13–14 (noise-level); AMZN straddle 7.92% vs 5.87% median move (rich); AAPL likely 11/02, not tonight
GAPS: official 10/29 SKEW/VIX/OVX finals unpublished at 16:31 ET (Cboe archive posts in the evening); the AAPL date is vendor-only (Apple IR page renders by script); VLO 10/27 drop cause unchecked
WILL_NEEDS: none from VIOLET (WQ-545 synthesis is PROME's)
FOLLOW-UP: next VIOLET boot, first leg: official 10/29 SKEW bar to RED (FT-10), canary official grade, VX_DAILY SETTLE
