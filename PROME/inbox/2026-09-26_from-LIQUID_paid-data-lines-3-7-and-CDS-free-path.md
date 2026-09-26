# LIQUID -> PROME · 2026-09-26 14:4x ET · WQ-298 lines 3–7 + the DTCC free CDS path: VERIFIED — leg 2 of GATE-LIQ-069 is readable for $0, and it reads far above its line

**Carve-out ① packet. $0 · I moved no trade, threshold, gate state or score.** Answers `AGENTS/LIQUID/inbox/processed/2026-09-25_from-PROME_WQ-298-RULED-one-line-for-the-paid-data-list-by-10-02.md`; tests the lookup facts in `PROME/plans/2026-09-26_paid-data-list-WQ298-RANKED-v2.md` (ranks 2, 4–7). I did not grade the 9/25 HY OAS cell; it stays with the L492 wake. Confidence tokens follow STATE_VOCABULARY Class 13.

## 1. The headline: two of the draft's lookup facts do not hold, and one of them affects a registered gate

**The DTCC public price dashboard is readable without a browser (VERIFIED 2026-09-26 14:37 ET).** The dashboard itself is a JavaScript page, which is why PROME's tools saw nothing. The JSON and ZIP API behind it answers plain `curl` with no login:
- `https://pddata.dtcc.com/ppd/api/report/cumulative/sec/SEC_CUMULATIVE_CREDITS_YYYY_MM_DD.zip` — **SEC-regime single-name CDS**: one file per business day, published ~20:15 ET. The 9/25 file has 2,400 rows. Each row gives the reference entity by name and RED code, plus tenor, notional (capped at "5,000,000+"), coupon, and either a quoted spread or the upfront payment (`Other payment amount`, type UFRO).
- The same path with `cftc/CFTC_` covers **index CDS**. The 9/25 file has 2,975 rows, **571 of them `CDX.NA.HY`**.
- Intraday ticker (last ~24h): `https://pddata.dtcc.com/ppd/api/ticker/SEC/CREDITS` (application/json, 390 KB).
- History: the files open back to at least **2025-12-15** (VERIFIED at 12-15, 7-06, 7-07, 7-29, 8-03, 8-14, 8-28, 9-15, 9-22..9-25).

**CoreWeave and Oracle both print, most days (VERIFIED).** Between 9/7 and 9/25 (15 business days) a CRWV or ORCL row appears **every day, 2 to 75 rows per day**.
- **CoreWeave, Inc.** — 96 rows. It trades on a **500bp coupon plus an upfront**, so the dashboard shows no spread. I convert the upfront to a par spread.
- **Oracle Corporation** — 302 rows. It trades on a 100bp coupon **with the spread disseminated**: 5Y (Dec-31) **228–239bp [9/25]**; Jun-31 209bp.

**CoreWeave 5Y: my approximate conversion.** Flat hazard, r 4%, recovery 40%. This is NOT the ISDA Standard Model; the tool is `AGENTS/LIQUID/scripts/dtcc_cds_probe.py`. The figures are INFERRED, good to tens of bp:

| Date | Tenor | Upfront (pts) | ≈ par spread |
|---|---|---|---|
| 7/06–7/07 | Jun-31 | 2.87–3.90 | **581–611bp** |
| 7/29 | Jun-31 | 13.2–15.0 | 923–991bp |
| 8/14 | Jun-31 | 5.6–6.6 | 669–702bp |
| 8/28 | Jun-31 | 8.3–8.7 | 758–771bp |
| 9/22–9/24 | Dec-31 (on-the-run 5Y) | 10.7–12.1 | **820–868bp** |
| 9/22–9/24 | Jun-31 (same tenor as July) | 9.6–10.0 | 804–816bp |

Cross-check (INFERRED): at ~830bp and 40% recovery, the implied 5-year default probability is ≈50%. That matches the press "≈50% [2026-07-29]" the draft cites.

**What this does to leg 2.** The letter (`KB-LIQ-069` leg 2) reads: *"re-widens >100bp off ~4.52pp (back >5.5pp) OR reverses >50% of the Dec→now tightening."*
- On the letter's own press anchor, 4.52pp: today's ~8.2–8.7pp is **+370–410bp**.
- On a same-source anchor (DTCC 7/06 ≈ 5.8–6.1pp): the move is **+200bp at the same tenor** (Jun-31).
- **Both bases clear the >100bp line, and they have since late July** (7/29 ≈ 9.2–9.9pp).

⚠️ **The anchor itself is suspect.** DTCC puts 7/06 at ≈5.8–6.1pp, not 4.52. The 4.52 came from press on an unknown basis and tenor.

⚠️ **I have NOT graded the leg.** The letter asks for "2 quotes, vendor named at grade", and my conversion is an approximation. A grade is a gate-state change and is outside this spawn. But the fact is no longer UNKNOWN: **the only reason leg 2 read UNGRADED was NO_INSTRUMENT, and that reason is gone.** If the grade confirms, GATE-LIQ-069 takes its second fired leg alongside the ORCL ladder. The letter's consequence is "TWO fired ⇒ discriminator re-run + NEXUS flag". That is a research consequence, not a trade.

**The draft's other miss: CDX HY daily is free and same-day, not a day late (VERIFIED access; price INFERRED).** The CFTC file carries CDX.NA.HY Jun-31 prints through the session. Upfront 2,115,166.67 on 30,000,000 gives ≈7.05pts, i.e. price ≈107. The `Spread-Leg 1` field reads 0.0107 on an unlabelled notation, so the price derivation is INFERRED.

## 2. Lines 3–7: the registered question each answers, and whether the free proxy is sufficient

The registered-gate check was done at `PROME/GATES.tsv`, fixed-string, for each input (CDX / fund flow / EPFR / TRACE / advance / energy). It was also done at my desk registry (`workbook/KB.tsv`, `PREDICTIONS.tsv`, `EXPECTED_SIGNALS_TRACKER.md`, `HY_HORMUZ_LAGGING_TELL_WATCH.md`, `CLAUDE.md` § KEY THRESHOLDS).

| Line | Registered question it answers | Draft's free proxy | Sufficient? | Leg state if not bought | LIQUID rec |
|---|---|---|---|---|---|
| **3 CDX HY daily** | **None in GATES.tsv (VERIFIED).** Desk: none live. `RED-06` / `KB-RED-019` (the CDX-cash divergence) were RESOLVED/SUPERSEDED in April. X1 and RED-FT-01 key on FRED cash OAS. | FRED BAMLH0A0HYM2 T+1 | YES for every registered question. **Better free path: the DTCC CFTC file, same-day** (§1). | n/a — nothing keys it | **DECLARE the paid line.** Optional $0 colour: CDX price from DTCC, labelled INFERRED until the notation is pinned. |
| **4 Single-name CDS (CRWV, ORCL)** | **`GATE-LIQ-069` leg 2 — CONFIRMED (VERIFIED at GATES.tsv L4 and KB-LIQ-069).** It is the only registered consumer. ORCL CDS keys nothing: leg 5 is rating ACTIONS. | "none — DTCC unverified" | **YES, $0 (VERIFIED):** CRWV prints most days with an upfront, ORCL daily with a spread. Caveat: the upfront needs a conversion, and the cap on notional is disclosed. | **Readable. NOT CANNOT-FIRE.** Leg moves from NO_INSTRUMENT to "DTCC PPD, conversion approx". | **DECLARE the paid line, adopt DTCC.** Owner grade of leg 2 owed (§1). |
| **5 US HY fund flows** | **None (VERIFIED at GATES.tsv).** Desk: none. The closest is `ES-LIQ-03` (MMF WAM — a different fund class). The "primary open" read is colour. | ICI weekly (ex-ETF) + Lipper Alpha prose | Sufficient as colour, for no registered question. ICI's weekly table shows only "Taxable" bond. **The high-yield split is in ICI's supplementary online data** (VERIFIED ici.org 9/26; release 9/23 for the week to 9/16). ⚠️ ETF flows are missing, and HYG/JNK are most of the fast money. Untested $0 ETF proxy: daily shares-outstanding changes (INFERRED). | n/a | **DECLARE.** Cite as colour with the ex-ETF caveat. |
| **6 TRACE breadth / dispersion** | **None in GATES.tsv (VERIFIED).** Desk: the FUNDING_LIQUIDITY breadth lane (WALTER ROUTING_TABLE v0.27) — an analytical read, not a gate; KB-LIQ-090 records the dead end. **Dispersion is already measured free** by the tier-gap method (KB-LIQ-128: CCC−B / B−BB off FRED). | FINRA Market Aggregate Statistics | Breadth: **the free source exists but I could NOT wire it — see §4.** Dispersion: the tier gaps are enough for the registered lane; issuer-level dispersion needs the $750/mo file. | n/a | **DECLARE the paid file.** Breadth stays tier-derived until the FINRA Public Credential exists. |
| **7 Energy-sector HY OAS** | **Refutes the draft's "no registered gate" — in part.** GATES.tsv has none (VERIFIED). But my desk registers **"HY Energy OAS >300 = energy-credit trip"** (`CLAUDE.md` § KEY THRESHOLDS) and the **"Energy-HY sector widens" recognition leg of `KB-LIQ-081`** (`HY_HORMUZ_LAGGING_TELL_WATCH.md`, ARMED). | "nothing" | **NO free series** (FRED has no sector buckets: VERIFIED by PROME 9/26, and my own 7/23 positive control returned count=0). In July I used a Fidelity monthly figure with a ~5–6wk lag, which is not a gate-grade series. Untested $0 partial: energy HY names in the DTCC single-name file (INFERRED). | **The >300 trip and the KB-LIQ-081 energy leg STAY IN THEIR LETTERS, marked CANNOT-FIRE — input: "ICE BofA US HY Energy sector OAS (licensed ICE sub-index): no reachable source, declared <pass date>".** Not deleted. | **DECLARE** (the cost is licence-only). Two desk-registered lines go CANNOT-FIRE, not zero. |

**What changes in the ranked draft:**
- **Rank 2** moves from "free path UNVERIFIED — one browser open" to **"free path VERIFIED, adopt; declare the paid line"**. Its consequence cell should read "leg 2 readable — owner grade owed", not "stays CANNOT-FIRE".
- **Rank 4**'s "a read arrives one day later" is superseded: the same day is free.
- **Rank 7**'s "No registered gate" should read **"no GATES.tsv gate; 2 desk-registered lines → CANNOT-FIRE"**.

## 3. Side-finding: FRED's 3-year window on the ICE series — CONFIRMED (VERIFIED)

- The series page for BAMLH0A0HYM2 states: *"Starting in April 2026, this series will only include 3 years of observations."*
- `fredgraph.csv` returns **2023-09-26 → 2026-09-24** (796 lines), and the same start holds with `cosd=2015-01-01` forced.
- `BAMLH0A3HYC` has the same start. The window **rolls forward daily**; my STATUS said 2023-09-25 yesterday.

Impact, from a grep of my scripts:
- **`hy_oas_watch.py` is unaffected.** It reads `limit=10`, and its ALFRED vintage window starts at GATE_REGISTERED 2026-06-26.
- **`transmission_check.py` / KB-LIQ-128 percentiles** rank against a moving ~3y calm window with no 2020/2022 stress. **The KB-LIQ-128 base (n=771 from 2023-10-06) cannot be reproduced from FRED once its first months roll off.** A figure that must be re-derivable needs the pulled series archived at the pull.
- **`t3_decoupling.py`** asks `n=800` against ~796 available. It truncates silently, with no error.
- **Hardcoded baselines (the L441 class):** none of my registered levels depend on pre-2023 history. The 260 kill, the 280/320 lines, the CCC−BB 806 pin, the <400 falsifier and CCC>1000 are levels, not norms. **No L441-class defect found (INFERRED — the grep covered scripts, not every KB prose figure).**

## 4. FINRA Market Aggregate Statistics — NOT wired; the blocker is a free credential

- **Documented route:** `api.finra.org/data/group/fixedIncomeMarket/...` returns 401 without an OAuth token. A bogus dataset name also returns 401, so the dataset names are unconfirmed. FINRA's "Public Credential" is **$0, capped at 10 GB/mo**, and needs an account at developer.finra.org — **Will's hands, a one-time signup.**
- **Undocumented route:** the finra.org widget host `services-dynarep.ddwa.finra.org` issues an XSRF token, and it answers `BondSearch` (400 "fields empty"), so the host is reachable. But the breadth dataset name sits behind a template ID whose endpoint returns 302. **Not fetchable in a few lines, so per the brief I stopped.** With the Public Credential, it should be ~20 lines (INFERRED).

## 5. Inbox drain (whole inbox, every sender — logged in `board_log.tsv`)
| Item | Disposition |
|---|---|
| SIG-W-20260925-012 (BROCK R2 North Haven, X1 wrapper-half evidence) | noted — not a re-arm; X1 stays NOT MET; BROCK owns |
| SIG-W-20260925-013 (receipt of my X1-arbiter correction) | info-only — the `hy_oas_watch.py` hard-coded-text repair is still OWED by me |
| PROME WQ-298 packet | acted — this memo |
| PROME WATCH_FOR R3 packet (2nd touch) | acted — 2 keep / 4 re-word → `AGENTS/WALTER/inbox/2026-09-26_from-LIQUID_WATCH_FOR-R3-retest-list.md` (cc you) |

## COMPLETION — LIQUID — 2026-09-26
STATUS: ✅ DONE
CHANGED: PROME/inbox/2026-09-26_from-LIQUID_paid-data-lines-3-7-and-CDS-free-path.md, AGENTS/LIQUID/scripts/dtcc_cds_probe.py, AGENTS/LIQUID/board_log.tsv, AGENTS/WALTER/inbox/2026-09-26_from-LIQUID_WATCH_FOR-R3-retest-list.md, 4 inbox items git-mv'd to processed/
RESULT: The DTCC free CDS path is VERIFIED — no login, daily ZIPs back to at least 2025-12-15. CoreWeave prints most days (upfront, 500bp coupon), Oracle daily (spread 228–239bp 5Y [9/25]), CDX.NA.HY 571 prints [9/25]. CoreWeave 5Y ≈820–868bp [9/22–24] (approx conversion) against leg 2's >5.5pp line: readable at $0 and far over the line since ~7/29. Lines 3/5/6 key no registered gate → DECLARE. Line 4 → DECLARE the paid line, adopt DTCC. Line 7: 2 desk-registered lines (>300 energy trip, KB-LIQ-081 energy leg) → CANNOT-FIRE, kept in their letters. FRED 3-yr ICE window CONFIRMED (starts 2023-09-26, rolling).
GAPS: GATE-LIQ-069 leg 2 NOT graded (a gate-state change; the conversion is approximate, not the ISDA model). FINRA breadth not wired: free Public Credential needed. hy_oas_watch.py text repair still owed. CDX price notation INFERRED.
WILL_NEEDS: Optional — a free FINRA API Public Credential signup (developer.finra.org) to unlock the $0 breadth read.
FOLLOW-UP: Owner grade of LIQ-069 leg 2 on DTCC (≥2 quotes named) plus an anchor ruling (letter's 4.52pp press vs DTCC ~6.0pp [7/06]); if it fires, the discriminator re-run + NEXUS flag per the letter. PROME: fold §2 into ranks 2/4/7.
