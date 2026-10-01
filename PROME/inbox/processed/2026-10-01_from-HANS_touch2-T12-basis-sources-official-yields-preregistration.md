# HANS → PROME · 2026-10-01 13:0x ET · touch 2 (Will 12:49 ET "go for the six"): T-12 sources · official FR/IT 10Y · 10/02 pre-registration

**Full record:** `AGENTS/HANS/research/2026-10-01_T12_BASIS_AND_OFFICIAL_YIELD_SOURCES.md` (each pull named with its endpoint and result).
**LIQUID split:** proposed by SendMessage 10/01 12:3x. HANS takes the T-12 row and the European side (ECB USD ops, ECB Data Portal). LIQUID takes the US side (the Fed swap-line draw by the ECB, SOFR/IORB). Each cites the other. **No LIQUID reply by 13:00 ET, so the split stands as PROPOSED, not agreed.** Nothing was built twice: I pulled no US-side series.

## (1) Dollar-funding sources reachable today
- ✅ **ECB USD 7-day operations, per-tender page (keyless, same day):** allotment, **number of bidders**, rate. Latest: **$207mn, 3 bidders, 4.13%** (tender 9/30, settles 10/01). The last 12 ops ran **$72–378mn with 2–5 bidders. No euro-area bank is paying up for dollars at the backstop.**
- ✅ **ECB full ops history (`tops.zip`):** USD rows only from **2022-11** (220 ops); max **$1,357mn**, max **6 bidders**. In March 2023 the tell was a **switch to DAILY operations** (from 2023-03-21), not size. **March 2020 is out of reach.**
- ✅ **ECB `EMMS`: the exact quantity**, the EUR/USD FX-swap implied rate minus SOFR OIS (1W/1M/3M/O/N, transaction-based). 🔴 **But the last observation is 2025-12-31 (~9 months lag).** Calibration only.
- ✅ ECB `CISS` FX-market contribution, daily D+1 (volatility, not basis). ❌ ECB `FM` has no basis or forwards. ⛔ Vendor CIP (forward points) not tested; no source is wired.
- **⇒ No live market basis is reachable from the European side.** The proposed replacement (§1 of the record, **PROPOSAL, not registered**) is a two-leg T-12: **Leg A** ECB USD ops (WATCH >$1.5bn or ≥8 bidders; ORANGE = the ECB moves to daily ops or a longer tenor) + **Leg B** EMMS (calibration only) + LIQUID's Fed-side leg. Acceptance conditions are written. **Replayed over 220 ops the WATCH fires zero times, so it is shown QUIET but never shown to FIRE (unvalidated against a real squeeze).**

## (2) Official French / Italian 10Y
| Source | Reachable? | Lag |
|---|---|---|
| ECB YC | ✅ euro-area AAA and all-issuers only, **no country curve** | D+1 |
| Bundesbank 10Y | ✅ | same day (fixing time unverified) |
| ECB IRS / Eurostat monthly | ✅ FR 4.000 / IT 3.986 [Aug] | ~1 month; Eurostat **daily** variant 404 |
| Banque de France webstat | ⚠️ the TEC10 daily dataset exists in the catalog but **serves 0 records** | — |
| AFT | ❌ Cloudflare 403 | — |
| Banca d'Italia infostat | ⚠️ JavaScript UI only, no data endpoint found | — |
| **MEF auction PDFs** | ✅ **10Y BTP 9/29: 4.58% gross, bid-to-cover 1.56, €3bn** | per auction |
| **ECB SovCISS (FR/IT/ES/DE)** | ✅ **official daily stress index**: FR 0.260 (86th pct since 2010), IT 0.132 (53rd) [9/30] | D+1 |

**⇒ No official daily FR/IT 10Y yield is reachable.** For tomorrow, T-10 is graded on the vendor screen **whose Bund leg is within 5bp of ECB AAA** for the date. If none qualifies, the level is reported as a range, and the state stands only if all screens agree. This is desk practice inside T-10's existing letter, not a new threshold.

## (3) Pre-registration (written 12:55 ET, committed before the 10/02 close)
"Same direction" = OAT–Bund **and** BTP–Bund each **≥5bp wider** and the Bund **≥3bp lower**. Outcomes: (a) same direction = **day 2 of broad periphery stress with a flight-to-quality bid** · (b) OAT wider, BTP flat = France-specific re-asserts · (c) spreads wider with the Bund **higher** = common-mode fiscal sell-off · (d) ≥5bp tighter = one-day spike. **A same-direction close would NOT mean:** a T-09 fire (Italy is ~80bp from both legs) · a T-10 state change or exit · **dollar-funding stress** (that needs the 10/07 ECB USD op or LIQUID's Fed side) · a cause (the budget stays headline-only) · an HNS-08 re-mark · a regime. Official confirmation: SovCISS for 10/01–10/02, read 10/05.

## COMPLETION — HANS — 2026-10-01 (touch 2)
STATUS: ⚠️ PARTIAL (all three asks answered; the LIQUID split is proposed and not yet agreed; no live basis source exists)
CHANGED: AGENTS/HANS/research/2026-10-01_T12_BASIS_AND_OFFICIAL_YIELD_SOURCES.md (new), AGENTS/HANS/{STATUS, DISPATCH_LOG, SESSION_LOG}, this memo
RESULT: ECB USD ops are reachable with bidders ($207mn, 3 bidders, no stress). The EMMS FX-swap-minus-SOFR series is the right quantity but ~9 months lagged. No official daily FR/IT 10Y exists; official referees are ECB AAA, Bundesbank and SovCISS (FR at the 86th pct since 2010). A two-leg T-12 replacement is proposed with acceptance conditions. The 10/02 periphery test (a)–(d) is pre-registered.
GAPS: No live EUR/USD basis; March-2020 calibration unavailable; BdF/AFT/BdI unreachable; LIQUID has not replied on the split.
WILL_NEEDS: Whether to register the proposed T-12 (Leg A ECB USD ops WATCH >$1.5bn or ≥8 bidders / ORANGE daily ops). Proposal only; record §1.
FOLLOW-UP: 10/02 T-10 re-grade and outcome (a)–(d); 10/05 SovCISS read; 10/07 ECB USD op; LIQUID to confirm the split.
