# WQ-317 — Is the US long end IMPORTING, EXPORTING, or on a SHARED driver? (9/22→9/28 episode)

**Written:** 2026-10-01, data pulled 12:52 ET (`date`) by BOND · **Letter:** PROME DOCKET L532 · `inbox/processed/2026-09-28_from-PROME_WQ-317-cross-market-attribution-read.md` (Will 9/28 17:16 ET: one page; existing HANS/SAM material; "UNDETERMINED" acceptable; daily closes cannot establish causation; no launches, no trade authority) · **Supersedes nothing:** the 9/29 PARTIAL (`analysis/2026-09-29_WQ-317_PARTIAL_…`, `KB-BND-362`) stands and is extended here.

## VERDICT — **UNDETERMINED** for the 9/22→9/28 episode.
Every input here is a **daily close or fixing**. Those can rule out some origins, but they cannot order cause and effect inside a day. The closes **rule out one thing**: Japanese cash JGBs could not have started the 9/22–9/23 leg, because Tokyo was shut. They **fit two stories equally well**: a shared global driver, or a US lead that Europe followed inside the same US morning. **After the window (9/29–9/30) the US long end rose ALONE** while Europe and Japan fell. That is US-originated and not exported, on closes. It is a fact about the days after the window, not a verdict on the episode.

## 1. Evidence table — daily change, bp (closes/fixings; basis per column)

| Session | US 2Y | US 10Y | US 30Y | UK 10Y par | UK 30Y spot | EA AAA 10Y | Bund 10Y (BBk) | JGB 10Y | JGB 30Y | ACGB 10Y |
|---|---|---|---|---|---|---|---|---|---|---|
| Mon 9/21 *(level)* | 4.76 | 4.96 | 5.29 | 5.1630 | 5.7301 | 3.4738 | 3.52 | closed | closed | 5.277 |
| Tue 9/22 | −5 | 0 | 0 | +2.8 | +4.1 | −2.1 | −2.0 | closed | closed | +1.6 |
| Wed 9/23 | **+14** | **+15** | **+11** | **+10.0** | **+7.2** | **+7.1** | +2.0 | closed | closed | −4.8 |
| Thu 9/24 | +2 | +7 | +7 | +5.3 | +5.8 | +4.2 | **+10.0** | **+9.2**¹ | **+7.1**¹ | n/p |
| Fri 9/25 | −6 | −1 | +2 | −1.2 | +2.8 | +4.9 | +1.0 | −0.2 | −0.3 | n/p |
| Mon 9/28 | **+11** | +7 | +7 | +5.1 | +3.0 | +1.7 | +6.0 | +1.1 | +1.0 | n/p |
| **9/21→9/28** | **+16** | **+28** | **+27** | **+22.0** | **+23.0** | **+15.7** | **+17** | +10.1¹ | +7.8¹ | — |
| *Tue 9/29 (after window)* | −3 | +2 | +3 | −1.9 | +0.3 | −2.4 | −1.0 | 0.0 | +0.4 | n/p |
| *Wed 9/30 (after window)* | −1 | +3 | **+5** | n/p | +3.5 | −2.6 | −4.0 | −2.5 | **−2.8** | n/p |

¹ JGB 9/24 is the first session after Silver Week (9/21–9/23 closed), measured from **9/18**, so it absorbs three US sessions (US 30Y +6 from 9/18 to 9/23). n/p = not yet published.
**Sources:** US = U.S. Treasury daily par yield curve CSV (H.15 source, ~3:30 PM ET indicative snapshot), Sept-2026 file, pulled 12:52 ET 10/1, 9/30 row included. UK/EA/Bund = HANS packet `inbox/processed/2026-10-01_from-HANS_WQ-317-EU-UK-rows.md` §1 (BoE IADB par `IUDMNPY` / BoE GLC 30Y **zero-coupon spot** / ECB AAA curve / Bundesbank Svensson zero, **observation time unverified**: HANS says do not time a move with it). JGB = MOF `https://www.mof.go.jp/english/policy/jgbs/reference/interest_rate/jgbcme.csv` (end-of-day JST), pulled 12:52 ET 10/1, levels in `KB-BND-360` reproduce. ACGB = RBA F2 `FCMYGBAG10D` (`rba.gov.au/statistics/tables/csv/f2-data.csv`, publication date 25-Sep-2026, so data runs **through 9/23 only**), pulled 12:52 ET 10/1. **ACGB is BOND's own pull; no desk supplies it.**
⚠️ HANS: a 1–3bp move in UK par is noise (par and spot disagreed in sign on 9/25). Never difference across two bases.

**Clock order on a calendar day t:** Sydney/Tokyo close (~01:00–02:00 ET) → London/Frankfurt close (~11:30–12:00 ET) → New York (Treasury snapshot ~15:30 ET). **Asia on day t is the first market to trade after the US close on t−1. Europe's close on t falls inside the US morning of t.** That is why same-day Europe-vs-US closes cannot order a move.

## 2. What each branch predicts vs what the closes show

| Branch | Predicts on closes | Observed | Reading |
|---|---|---|---|
| **IMPORTING** (foreign leads, US follows) | Foreign markets move **before** the US: Asia on day t, or Europe up by its close and the US up later | **9/23:** UK +10.0, AAA +7.1 by the ~11:30 ET close; US +15 by 15:30. **But** ACGB fell 4.8bp in the Sydney session just before 9/23, and JGBs were shut | **Not excluded for Europe on 9/23; excluded for JGB cash 9/22–9/23** (`KB-BND-360`). ACGB shows no Asian lead into 9/23 |
| **EXPORTING** (US leads, others follow) | Asia on day t+1 tracks the US on day t; Europe follows the US on later days | JGB 9/24 +7.1 (30Y) after the US 9/22–9/23 +11: **follows once**. Then JGB 9/25 −0.3 after US +7 · 9/28 +1.0 after US +2 · 9/29 +0.4 after US +7 · **9/30 −2.8 after US +3** | **Follows on 1 of 5 Asian sessions.** Europe did not follow the US 9/29 or 9/30 long-end legs |
| **SHARED** (a common driver moves all markets the same day) | Same-day, same-sign moves everywhere with a common news trigger | 9/23 (all up; hot US flash PMI the same morning, `analysis/2026-09-28_live-event-assessment.md`, European PMI timing not held) · 9/24 (all up; France fiscal fire `HANS-T-10`) · 9/28 (US+EU up; wire: oil/Iran + hike odds + global sell-off, `KB-BND-357`, **wire attribution, not causation**) | **Consistent on 9/23, 9/24, 9/28.** No common trigger has been *established*; oil does **not** show in US breakevens (`KB-BND-343/-357`) |

**Cumulative 9/21→9/28:** US 10Y +28 ≈ UK 10Y par +22 ≈ UK 30Y spot +23 > Bund +17 ≈ AAA +16 > JGB 10Y +10. That is a co-movement, roughly scaled by market. It fits SHARED, and it fits a US lead whose followers moved less. **The closes do not choose between them.**

## 3. Evidence that WOULD distinguish the branches — and whether BOND holds it

| Evidence | Distinguishes | Held? |
|---|---|---|
| Intraday tick sequence, UST cash/futures vs gilt/Bund futures, **9/23 03:00–12:00 ET** (European flash PMIs vs the US 9:45 ET flash PMI) | IMPORT vs US-lead vs SHARED on the biggest day | **NO.** HANS holds no intraday 9/22–9/28 (§4 of its packet). BOND's yfinance 5-minute bars do not reach back that far |
| Release timestamps for the 9/23 EZ/UK flash PMIs vs the US flash PMI | Common-trigger timing | **NO** (US hot-PMI day is on file; the European releases are not) |
| JGB futures (OSE night session) during Silver Week | Whether Japan moved with the US while cash was shut | **NO** (SAM holds no intraday JGB, `KB-BND-360`; vendor JGB futures bars inadmissible per BND-31's letter) |
| ACGB 9/24–9/28 | Whether Sydney followed the US | **NOT YET**: RBA F2 is published weekly, next ~10/2 |
| CME settlement-price futures vs cash (the 9/28 cash ≈2× futures gap, `analysis/2026-09-28_front-end-led-move.md`) | Cash-specific selling vs bar timing | **NO** (CME settlements HTTP 403) |
| Foreign UST flow by holder: TIC (monthly, lagged) · auction composition | Foreign selling as the channel | **PARTIAL.** 9/23 5Y indirect failed the OLD composition test (US-specific, `KB-BND-312`). MOF weekly 9/13–9/19 −¥1.905T is all residents, not UST-specific, and predates the window (WALTER `SIG-W-20261001-004/-006`, SAM canon) |

## 4. The 9/29 leg and the Tokyo 9/30 EXPORT test (`BND-31`)
- **9/29 = US-ORIGINATED** (PARTIAL, `KB-BND-362`): the US long end rose (30Y +3 official) while Bund −1, AAA −2.4, UK 10Y par −1.9, JGB 30Y +0.4. The 30Y rose ~2bp in the 25 minutes **after** a weak consumer-confidence print (81.9), and oil fell.
- **EXPORT test, Tokyo 9/30 (MOF, first publication, read 12:52 ET 10/1):** JGB 30Y **4.126 → 4.098 = −2.8bp** (< +4.0, and ≤ +1.0 ⇒ sub-band **NOT EXPORTING**). Rider: JGB 10Y 3.082 → 3.057 = −2.5bp. **`BND-31` resolves TRUE.** Europe 9/30 also fell (AAA −2.6, Bund −4.0) while the US 30Y rose **+5 to 5.64** on 9/30 (Treasury CSV). **The 9/29 leg was not exported on closes; one session is one session.**
- **Term-premium cell (`BND-30`, NY Fed ACM Daily, 9/29 row, read 12:52 ET 10/1):** ΔACMY10 = 5.2247 − 5.2018 = **+2.29bp** (premise ≥ +2.0 met) · ΔACMTP10 = 0.8467 − 0.7927 = **+5.40bp** · ΔACMRNY10 = **−3.11bp** · share **2.36 ⇒ TRUE, TP-DOMINANT** (≥0.75). Companion 2-day 9/25→9/29: ΔY +8.71, ΔTP +7.20, share **0.83**. ⚠️ ACM is one model. KW 9/29 is unpublished (~10/9–10/13), and the base rate puts a TRUE near the median (51–62%). **The decomposition says the 9/29 move was duration pricing in ACM's model. It does not say where it started.**

## 5. 10/1 note (OUTSIDE the window; not used for the verdict)
HANS **withdrew** its "France-only" read of 10/1 (`inbox/processed/2026-10-01_from-HANS_CORRECTION-…`; `KB-HANS-106` supersedes `-102`): **the Bund RALLIED ~8–9bp** (3.494, TE/CNBC), Italy widened about as much as France (BTP ~+16 vs OAT ~+17 against the 9/30 bar), and Spain widened ~+10. **A flight-to-quality day with broad periphery/semi-core widening.** The OAT–Bund level is uncertain, 130.3 (i-i) to ~143 (TE/CNBC). WALTER `SIG-W-20261001-009` (Italy ~113, France 5Y CDS ~75, one chart) is consistent with this. Relevance to BOND: a European core *rally* on 10/1 is the opposite sign to a shared global duration sell-off, so the next US close is a test of US-alone pricing. That is **not** an attribution claim.

## 6. Caveats and gaps
- **Daily closes only: no verdict is drawn from them** (letter). The branch labels in §2 say which story each day *fits*, never which happened.
- **Two Bund bases disagree day by day** (BBk +2/+10 vs AAA +7/+4 on 9/23/9/24). The cumulative figures agree. UK 30Y is a zero-coupon spot rate, used for changes only. The OAT figures are vendor-only (no BdF/AFT primary reachable, HANS).
- **ACGB** coverage stops at 9/23. Gilt 9/30 par is unpublished.
- **US driver remains WIRE-ATTRIBUTED** (`KB-BND-357`). Fed-speaker and supply cells for 9/29 are SEARCH-NOT-FOUND (`KB-BND-364`).
- **Basis rule:** never difference across two sources (MOF CMT vs headline JGB quotes; i-i vs CNBC OAT; Treasury par vs Reuters intraday).
- **No position, threshold or kill rail is touched by this page** (letter). The 10/1 FR2004 grade keeps its own rail.
