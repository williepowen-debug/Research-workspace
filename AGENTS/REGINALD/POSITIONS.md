# REGINALD — Thesis Positions

**Updated:** 2026-05-08 from broker (typed list, Will dispatch — refreshed after KRE $70P May 15 phantom incident). Apr 2 → May 8 = ~5 weeks of broker activity caught up.

**Scope:** Thesis-relevant only — bank puts + credit/convergence. OZK lives in `../OZK/POSITIONS.md` (peer agent). Stocks, macro options (TLT/VIX/USO/XLE), and non-thesis (AAPL/APD/AAL/CCL/CF/DIS/KELYA/FXY/SLV/TBT) live in `FORGE/STATUS.md`.

⚠️ **Contract quantities not in this rewrite** — broker list was strike/expiry rows only. Reference `FORGE/STATUS.md` for current quantities (currently Mar 25 stale — FORGE refresh from this same broker data recommended).

---

## 🔴 MAY 15 EXPIRY CLUSTER (T-5 trading days)

REGINALD-scope positions expiring May 15:

| Ticker | Strike | Tape (May 8) | OTM% | Mechanical decision |
|---|---|---|---|---|
| WAL | $75P | $82.11 | 9.5% OTM | Roll vs let-expire — needs Greek/IV math |
| SSB | $95P | $96.39 | 1.5% OTM (NTM) | Pin risk; closest to actionable |

(Out of REGINALD scope but on the same day: TLT $88P, OZK $42.5P/$47.5P. TLT in FORGE; OZK in `../OZK/POSITIONS.md`.)

Mechanical-before-creative deadline: this week.

---

## Bank Puts

| Ticker | Strike | Expiry | Notes |
|---|---|---|---|
| WAL | $75P | May-15-2026 | NTM/OTM — **May 15 cluster** |
| WAL | $65P | Jun-18-2026 | Aggressive |
| WAL | $67.5P | Jun-18-2026 | |
| WAL | $77.5P | Jun-18-2026 | |
| WAL | $85P | Jun-18-2026 | Deep ITM at last broker check |
| WAL | $65P | Jul-17-2026 | NEW vs Apr 2 baseline |
| WAL | $67.5P | Sep-18-2026 | NEW vs Apr 2 |
| WAL | $70P | Sep-18-2026 | |
| KRE | $60P | Jun-18-2026 | Margin (matched/spread) |
| KRE | $63P | Jun-30-2026 | |
| KRE | $65P | Jun-30-2026 | |
| KRE | $67P | Jun-30-2026 | |
| KRE | $60P | Aug-21-2026 | |
| KRE | $60P | Sep-30-2026 | |
| KRE | $60P | Dec-18-2026 | Margin |
| KRE | $60P | Dec-18-2026 | |
| EGBN | $25P | Jun-18-2026 | Margin |
| FITB | $45P | Jun-18-2026 | **NEW name vs Apr 2** — cohort-fade thesis play? |
| FLG | $13P | Jul-17-2026 | |
| HBAN | $16P | Oct-16-2026 | **NEW name vs Apr 2** — DC corridor / federal layoff exposure? |
| SSB | $95P | May-15-2026 | NTM — **May 15 cluster** |
| ZION | $57.5P | Jul-17-2026 | (expiry confirmed by Will 2026-05-08) |

## Credit / Convergence

| Ticker | Strike | Expiry | Notes |
|---|---|---|---|
| HYG | $75P | Jun-18-2026 | Credit canary |
| APO | $100P | Jun-18-2026 | PC/MFS thesis |
| APO | $95P | Dec-18-2026 | **NEW vs Apr 2** — longer-dated PC short |
| ARES | $95P | Jun-18-2026 | |
| IWM | $257P | Jun-18-2026 | **NEW strike** (was $250 in old POSITIONS) |
| IWM | $250P | Jun-30-2026 | |
| OWL | $9.5P | Jun-05-2026 | **NEW vs Apr 2** — PC stress (paired with OCIC/OTIC redemption-cap thesis) |
| SOFI | $16P | Jun-05-2026 | Consumer credit |

---

## Key Context

- **WAL** is the heaviest single-name (8 positions across 4 expiries: May-15 / Jun-18 / Jul-17 / Sep-18). WAL Q1 print Apr 21 ✅ V2 fraud confirmed in 8-K. THESIS v2.0 May 1 = "compounder with concentrated CRE tail risk." May 15 $75P added since Apr 2 = short-dated tactical layer.
- **KRE** — 8 positions across 5 expiries ($60-$67 strikes, Jun-18 / Jun-30 / Aug-21 / Sep-30 / Dec-18). **Confirmed: NO May 15 expiry on KRE.** The phantom was a Feb position closed/exited and never propagated. Tape $70.05 today = above all strikes (deep OTM); positions are tail-risk insurance, not directional.
- **New bank names since Apr 2:** FITB (mid-cap regional, Q1 cohort-fade pattern candidate) and HBAN (Huntington — Ohio + DC corridor / federal layoff exposure). Both warrant thesis-row updates in STATUS.md if Will wants them tracked.
- **May 15 cluster (T-5) is the real mechanical decision pile** — was hidden by the phantom. WAL $75P (9.5% OTM) and SSB $95P (1.5% OTM) need Greek/IV-vs-roll math this week.
- **OZK positions are in `../OZK/POSITIONS.md`** (peer agent, spun out 2026-04-24). 4 OZK rows in Will's typed list (May-15 $42.5/$47.5, Aug-21 $42.5/$45) need to flow there, not here.
- **FORGE/STATUS.md staleness propagates the same risk** — Mar 25, also 6+ weeks behind broker. Same broker data should refresh FORGE's current-positions table (out of REGINALD scope).
