# SAM STATUS — WARM REFERENCE

**Hot/cold split out of `STATUS.md` 2026-09-11**, under the fleet READ-CAP rule
(`AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`). STATUS had reached 13 B of headroom against its 32,550 B
budget — the next session block could not be written without breaching it, and the cheap
prose-compression fix was spent (recorded in MEMORY 2026-09-11).

🟡 **WARM — read ON DEMAND, not at boot.** This is not the cold `STATUS_ARCHIVE.md`: everything here is
**current and citable**. It is split out because SAM's boot protocol reads STATUS's header, top session
block and the `LIVE MARKET DATA` / `KEY THRESHOLDS` / `WHAT TO WATCH` / `PREDICTIONS` sections — these
sections were never in that read, so they consumed budget without being read.

⚠️ **Live state stayed in STATUS.** Each section below leaves a pointer in `STATUS.md` carrying its
one-line current state; what moved here is the accumulated evidence, method and durable reference
detail behind it. Read this file whenever a claim turns on intervention evidence, the carry-unwind
method's vintage, channel/policy interpretation, or a durable reference figure.

⛔ **Verbatim move, no edits to the analytical content.** Checked before moving: no external consumer
cites these section names (the `↪️ MOVED:` redirects that peers DO cite deliberately stayed in STATUS).

---

## 📌 DURABLE REFERENCE ROWS
*(moved from `STATUS.md` § LIVE MARKET DATA — stable, slow-moving figures, not live market data)*

**Durable reference rows:** 🆕 **AUGUST CGPI — 2026-09-11 08:50 JST, BOJ `cgpi2608.pdf`, own primary: PPI −0.2% m/m / **+7.6% YoY**; Import PI **yen basis −3.0% m/m / +24.8% YoY**, contract-currency **−1.0% m/m / +16.7% YoY**; **petroleum/coal/natural gas contributed −1.18pp** to the contract-currency monthly fall (crude petroleum, naphtha, LPG); FX column −2.4% m/m (yen appreciation).** ⇒ **in August Japan's import prices FELL in both currencies and terms of trade IMPROVED; oil was the largest single DRAG.** The September oil shock reaches none of the 9/11 CGPI, the 9/16 trade balance or the 9/18 National CPI. 🔧 **The same primary shows July PPI +7.7% r and June +7.4% — this file's earlier 7.2%/7.1% pair (8/13 release) is SUPERSEDED; do not cite it.** · BOJ subsidy-stripped trend gauge 2.8% [Apr] vs official core 1.4% · insurer hedge ratio 44.4% [Mar 2025, 14-yr low] · Tankan Q2 +22 [6/30] · **TOKYO AUGUST CPI — 2025 base: headline 1.9 / core 1.8 / core-core 2.0**, latest Tokyo observation in `workbook/CPI.tsv`. **JAPAN JULY CPI — 2025-BASE, canonical: National headline 1.9 / core 1.8 / core-core 1.9 · Tokyo 1.8 / 1.7 / 1.8** [rel 8/21, e-Stat primary]. ⛔ The 2020-base pair is SUPERSEDED — **never compare across bases**. ⛔ The "Tokyo running ABOVE national" read is RETIRED as a BASE ARTIFACT — **the RETIREMENT STANDS** (it died because its 2020-base counter-example reads 0.0pp on the 2025 base). 🔧 **But the count is UPDATED 2026-09-19: n=7, Tokyo ≤ National in 6 of 7, mean −0.10pp** — August completed the paired set at **Tokyo 2.0 vs National 1.9 = +0.1pp, Tokyo ABOVE**, the first 2025-base exception (the "6 of 6, no exception" figure was n=6, Feb–Jul). ⚠️ Read narrowly: +0.1pp is the one-decimal publication floor (true gap inside ~(0.0, 0.2)pp) and n=1 is not a regime — it does NOT revive the retired directional read. ⚠️ **SCOPE: CORE-CORE ONLY.** · **Japan JULY TB −¥638.3B, revised August 28** (imports +27.9%, crude value +87.8% YoY, **crude VOLUME +5.5%**; crude 12,106 kKL ≈ **76.1 M bbl/mo ≈ 2.46 mb/d**, value **¥1,408.9B**) — **August prints Sep-16, and VOLUME is the discriminator.** Earlier −¥634.5B / +27.8% was provisional; [revised source](https://www.customs.go.jp/toukei/shinbun/trade-st/2026/2026075.xml).

---

---


**🔧 Added 2026-09-18 (rotated from `STATUS.md` LIVE MARKET DATA under the read-cap rule — durable published macro/flow figures; current and citable).**

| Row | Figures | Notes |
|---|---|---|
| Japan domestic data | Q2 GDP **+1.4% ann.**; July wages **+4.1% YoY**; **July current account +¥2,988.9B (+15.6% YoY)**, rel Sep-8 | BoP goods −¥399.9B, services −¥512.9B, **primary income +¥4,289.6B** (MOF `bp202607.pdf`). BoP goods ≠ customs (revised −¥638.3B). **The VECTOR-5 denominator: the oil shock is 4.0% of ONE month's CA surplus.** |
| New macro/flow context | July IIP **−0.2% m/m** (METI Sep-14); FY2027 requests **¥143.0656T** (MOF Sep-4); August foreign equity/fund net **+¥1.2983T** (MOF Sep-8) | IIP shipments +2.1%; requests ≠ enacted spending/issuance; flows ≠ NISA-only or measured FX trades. [Sources](reports/2026-09-15_news-sweep.md). |
| 🆕 Sep flash PMI (S&P Global, rel 9/24) | Manufacturing **54.1** (Aug 54.9; cons 55.0) · services **51.6** (52.5) · composite **52.5** (53.5, slowest since May) | Reuters via Investing, 9/24 (REPORTED). Still expansionary but slowing; S&P names the weak yen and Middle-East energy as input-cost drivers. Survey, not hard data — no BOJ-path read from one flash. |

⚠️ Caveats travelling with them: BoP goods ≠ customs (July revised −¥638.3B); IIP shipments +2.1%; budget **requests ≠ enacted** spending or issuance; securities flows are **not** NISA-only and are not measured FX trades. **The VECTOR-5 denominator: the oil shock is 4.0% of ONE month's CA surplus.**

## CARRY UNWIND PROBABILITY (decomposed estimate — method → `thesis/THESIS.md` § CARRY-UNWIND PROBABILITY METHOD)

**Last assessed August 7: 7d ~3 / 30d ~8 / 60d ~13. Historical assessment, not a fresh rolling forecast.** Amplifier and residual OFF at that assessment; no re-pencil this session. Historical drivers and prior marks → `STATUS_ARCHIVE.md`. Future re-pencils must update all changed anchors; >5pp changes require named drivers. The method's intervention-causing-unwind framing omits the countervailing no-cap/overshoot path. Disclose as a decomposed estimate, never "true probability." No retired entry gate re-arms.

---

## INTERVENTION STATUS — MOF posture

**September 14 ET review: Sep-7/8 attribution remains OPEN.** Sep-10 FINAL equals provisional; Sep-11 FINAL fiscal −¥1,060B vs −¥1,040B forecast (−¥20B), Sep-14 FINAL +¥1,450B vs +¥1,360B (+¥90B), both equal provisional. These residuals do not identify an operation. September 15 −¥590B is only a forecast. [Source evidence](reports/2026-09-14_stale-sweep.md). Prior closed evidence: Sep-10 final: fiscal +¥340B vs projection +¥220B (residual +¥120B); balance ¥412.71T — **no yen-buying signature** (an op *drains* yen and prints large NEGATIVE; this is a net supply, wrong direction, residual trivial). **Sep-9 FINAL −¥3,590B = provisional**, +¥10B vs Ueda Yagi's Sep-3 forecast ⇒ closed as anticipated fiscal. **Sep-8 final −¥1,100B vs Ueda +¥100B (−¥1,200B) / BOJ −¥560B (−¥540B) stays unexplained** — a forecast miss is never an operation size. ⚠️ Japan's settlement instrument **cannot exclude a U.S.-only operation**. Official words: Katayama 9/8 stance "hasn't shifted"; Bessent September 8 SMU remarks (reported September 8–9; Reuters secondary corroboration, primary transcript not located). Evidence → `reports/2026-09-10_et-boot.md` §2; **`MOF_INTERVENTION_PLAYBOOK.md` S1/S1-A governs**.

**Funding — unresolved, and the 9/6 Bloomberg story does not resolve it.** MOF officially reported **¥15,399.3B for Jul-30–Aug-26** (rel Aug-28): Japan-side aggregate only, no daily split and no U.S. euro-leg amount. Earlier official windows: Apr-28–May-27 ¥11,734.9B; Jun-29–Jul-29 ¥0. August reserve **securities fell $87.773B** and deposits $6.868B (rel Sep-8) — a securities-funding *hypothesis*, **not identified UST sales**, given valuation/FX effects and mismatched stock/intervention windows. 🆕 **The $87.8B fall is ~$10.8B SHORT of the ~$98.6B intervention** — consistent with a joint US leg AND with mark-to-market on a rising-yield month. The FIMA-funded claim was retracted; the historical H.4.1 test found no foreign-official repo use. FRBNY Q3 (~Nov-13) addresses the U.S. account split; MOF's quarterly per-op disclosure (~Nov-9) gives the Japan-side per-op record. Details: KB-SAM-209. Monthly path uses `reference/feio/monthly/`, not `feint`; BOJ projections `jp`, provisional `jx`, final `jd`.

**2026-09-24:** Sep-21→24 had NO spike to semi-confirm (largest session range 0.98 yen; 9/18 close → 9/24 live +1.3%). T1 (9/18 rate check) window lapsed without a strike; detail → STATUS § INTERVENTION + playbook 2026-09-24.

**Aug-3 detector disagreement remains an ambiguity:** 2.67y range exceeded the >2.5y detector bar while final settlement −¥3.29T read ordinary. Post-operation elevated ranges and the invisible U.S.-only route prevent attribution. Unchanged disorder watch: ≥1.5–2% in a day or ~2–3 yen over 1–2 sessions. **Silence is not a safety signal.** Frozen confirmation ladder and preregistered bands → `thesis/INTERVENTION_2026-07-30_CONFIRMATION.md` (registered before reads, commit `aa3ad1980`); full history → `STATUS_ARCHIVE.md`. Preserve these external citation targets.

---

## CHANNELS · BOJ · FED

Canonical mechanism and policy interpretation → `thesis/THESIS.md` and September 8 assessment. Channel 1 requires direct foreign sales at ≥2 institutions across ≥2 consecutive windows; yields and ESR are co-conditions, never substitutes. Sector aggregates cannot update named company profiles. Carry-convexity/positioning frames remain retired. ⛔ **BOJ policy rate is 1.25% — RAISED 2026-09-18, effective Sep-24** (the "1.00%" that stood here was a pre-decision vintage, corrected same-day). The July hold was 8–1 with Takada favoring 1.25%; he got it in September, 7–2, with both dissents on the DOVISH side. Current pricing belongs only in LIVE MARKET DATA. Political rhetoric, policy surprise and FX transmission remain distinct.

✅ **SEPTEMBER MPM RESOLVED 2026-09-18 — hiked 25bp to 1.25%, vote 7–2, effective Sep-24; BOTH dissents (Asada, Sato) were DOVISH, for HOLD.** Owner grade of SAM's three-leg pre-registration → `STATUS.md` § 2026-09-18 and `reports/2026-09-18_boj-mpm-grade.md`. ⚠️ **Everything in the remainder of this paragraph is PRE-DECISION material, retained as the as-published forward read and superseded as current state.** Masu's "below the estimated range" framing survives as context: the hike moved the rate toward, not into, the 1.1–2.5% neutral band. **Historical pre-decision read (sources Sep-10, report §5–6).** Masu (Sep-10, primary) — policy rate "below the estimated range" of neutral (1.1–2.5%), "the Bank will continue to raise the policy interest rate," pace keyed to **oil**, AI demand and FX; balance sheet halt-the-reduction from FY2027 at ~¥2T/mo (the June-MPM plan). Ueda 9/2, Takata 9/2, Himino 8/26, Aida 9/7 ("narrow window" before the early-Oct Diet), Katayama 9/8; Reuters via FXStreet 9/11 "set to raise by 25bp next week." Fed: Waller 9/3 HOLD-unless-CPI-hot. All secondary press except Masu and the BOJ/MOF primaries named in the report.

---

## USD/JPY MEASUREMENT BASIS (WQ-162 convention)

**Rotated here from `STATUS.md` § KEY THRESHOLDS on 2026-09-18 under the read-cap rule. ⛔ CURRENT AND CITABLE — this is a convention, not an archive. `STATUS.md` carries the one-line live state and points here.** Internal consumers that named § KEY THRESHOLDS as the canonical home (notably the SAM-39 bullet) now point to this section.

🆕 **BASIS (WQ-162 convention, encoded 2026-09-11 — a CONVENTION line, never a revision claim).** Every USD/JPY level and every USD/JPY-derived COUNT on this desk is read on: yfinance `USDJPY=X`, 1-hour bars aggregated to sessions labeled in **Europe/London** (the index's own zone), **COMPLETED sessions only** — the current bar is never scored. Intraday range = session high − session low, in yen. Observations are taken **as LAST REVISED** inside a 30-day upsert window (`usdjpy.py --revise-window`), **not as first published**. ⛔ This is **NOT** the BOJ 17:00 JST reference rate and **NOT** the MOF curve: never blend or difference across bases. `dashboard.py` and `fetch.py price USDJPY=X` read the SAME yfinance series and are basis-compatible; the BOJ 17:00 JST fix is not. ⚠️ **The vintage direction is deliberately OPPOSITE to LIQUID's GATE-HY-REKILL letter ("as FIRST published")** — HY OAS revisions are rare and first-publication protects a closed count, whereas this instrument's revisions **are its bug fix** (it silently under-stated 7/31 as 2.17y against a true 3.655y, so first-publication grading would have resolved SAM-39 FALSE on a known-defective measurement). Declaring the direction is the point of the convention.

---

## CARRIED MARKET CONTEXT — refreshed 2026-09-24 (was "CARRIED SEP-14/15 VINTAGES")

**Refreshed in the 9/24 catch-up session; every figure carries its own date. These are context rows, not thresholds.** ⚠️ yfinance returned **no US daily bar for Tue 9/22** on any equity/ETF/UST ticker — a vendor gap, not a market closure (US markets were open); FRED has 9/22.

| Item | Level / vintage | Note |
|---|---|---|
| Japan bank ADRs | MUFG **22.57** / SMFG **25.51** / MFG **10.56** [9/24 close] | Were 23.89 / 27.24 / 11.33 [Sep-14/15] — down ~5–7% across both hikes while USD/JPY weakened. Confounded by US rates; no mechanism read. |
| DXY / VIX / S&P | **101.31** / **15.67** / **7,704.13** [9/24] | DXY was 99.58 [9/14] — the dollar leg is part of the USD/JPY move, not all of it (EURJPY 178.29 → 180.75, 9/15→9/24). |
| UST 10Y / 30Y | **5.11% / 5.40%** [FRED 9/23]; ^TNX 5.162 / ^TYX 5.461 [9/24 vendor] | Never blend FRED constant-maturity with vendor yields. The 10Y is above 5% — the "two-decade high" wire claim is WALTER's (SIG-012), not verified here. |
| FXY ATM IV (proxy) | **10.99%** Oct-16 expiry / 11.77% Dec-18 [9/24] | Was 16.24% (Oct-16) [Sep-14/15] — the event premium bled out after the 9/18 decision. ⚠️ KB-183: read the proxy's SIGN, not its level; FXY ETF options ≠ CME CVOL/OTC. |
| Japan-ETF tape | EWJ **95.81** / DXJ **179.03** / YCS **54.76** [9/24] | YCS (2× short yen) +5.1% since 9/15 (52.12). |
| MOF Aug lifer / trust | lifer LT −¥137.3B / trust +¥2,332.6B [Aug, published Sep] | Unchanged — monthly; next with the September release. Trust ≠ GPIF; LT debt ≠ UST. |

## FUNDING (U.S. / Japan)

**Refreshed 2026-09-24 (FRED). Current and citable, not boot-read.**

| U.S. / Japan funding | **SOFR 3.87% / IORB 3.90% ⇒ −3bp** [FRED 9/23]; HY OAS **273bp** / IG **77bp** [9/23] | Post-FOMC hike (IORB 3.65 → 3.90). Spread unchanged at −3bp across the hike ⇒ **no U.S. funding stress.** HY 265 → 273bp [9/11 → 9/23], widening 8bp into two-decade-high UST yields; IG 80 → 77bp. Japan O/N / repo last recorded Sep-14 (0.977% / 1.000%) — **pre-hike, stale; not refreshed this session.** |

⚠️ GC T/N ~1.005% (pre-hike) is a separate instrument. **None of these measures offshore FX swaps** — that gap is what RED salvage ④ (a real JPY xccy-basis instrument) is owed for.

