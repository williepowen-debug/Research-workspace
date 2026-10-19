# L721 — four legs graded (LIQ-07 verdict · 069 L4 HY half · discount window · August TIC)

**LIQUID · Fri 2026-10-16 16:1x–16:4x ET · PROME Tier-1 wake on DOCKET L721 (WQ-184 row = the nod).** Claude Code, Opus 5.5. Boot: root `CLAUDE.md`, `AGENTS.md`, `USER.md`, `AGENTS/LIQUID/CLAUDE.md` read explicitly. All figures pulled live this session (pull times 16:16–16:20 ET). **No line, leg, instrument, threshold or consequence moved. $0. No trade view.**

## ① LIQ-07 — FINAL funding-branch verdict: **S2 SPREADING — ORDINARY REPRICING, on BOTH session lists**

Letter: `workbook/PREDICTIONS.tsv` LIQ-07 · `reports/2026-09-25_Q2_first-observation-of-spreading.md` (branches MECE, first event decides). Trigger fired 2026-09-30 (unchanged). S1 needs, within ±10 published sessions of 9/30, one funding leg: `sofr_dispersion.py` z ≥ 4.0 (non-Q-end) · GATE-LIQ-079 ARM (SOFR99−IORB ≥ +30bp ×2 consecutive, date-matched, non-Q-end) · SRF `RPONTTLD` ≥ $50B.

| Date (last needed) | SOFR | SOFR75−IORB | SOFR99−IORB | z (dispersion) | SRF RPONTTLD | Source |
|---|---|---|---|---|---|---|
| 10/14 | 3.88 | +3 | +7 | −0.7 | $0.001B | FRED, read 10/15 + re-pulled 10/16 |
| **10/15** | **3.89** | **+4** | **+7** | **−0.3** (WALTER pure-function −0.337) | **$0.111B** | FRED cache-busted CSV + `transmission_check.py`, pulled 16:17 ET 10/16; IORB 3.90 same date |

| Session list | Window | Max eligible z | Max SOFR99−IORB | Max SRF | Branch |
|---|---|---|---|---|---|
| SOFR list | 9/16 → 10/15 | −0.225 | +9bp | $1.2B (9/30) | **S2** |
| ICE list | 9/16 → 10/14 (incl. 10/12 ICE holiday row) | −0.225 | +9bp | $1.2B (9/30) | **S2** |

- **Lists agree ⇒ no AMBIGUOUS-BY-SESSION-LIST; RED's direction note is moot.** WALTER SIG-W-20261016-020 reached the same maxima independently (evidence, not a grade).
- **Vintage:** 10/14–10/15 funding cells are latest-revised (pulled after NY Fed's ~14:30 ET revision window); first-published equivalence was checked only for dates through 10/13. Margins to every line are wide (z −0.3 vs 4.0; +7 vs +30; $0.111B vs $50B), so no plausible revision changes the branch — INFERRED, not tested.
- **Meaning, narrow:** S2 = *no reserve-channel loop observed*, not *no loop*. Collateral/haircuts, redemptions, term credit and offshore USD channels are outside this test (§5 STATUS).
- **Forecast record:** P(S1 or S2) = 15% — that outcome occurred; P(S1) = 5% did not. A single resolved case does not validate calibration. Status → **RESOLVED-S2** (Date_Resolved 2026-10-16); 11/10 Resolve_By honoured early because the first-event rule has decided.
- Context legs (do not change the branch): VIX 20.16 (+22.5%, yfinance 16:16 ET, intraday-close proxy) · MOVE 101.11 · rates 10Y 5.10 / 30Y 5.43 [FRED 10/15].

## ② GATE-LIQ-069 L4 — HY half

- **10/14 session: FIRED (already graded 10/15 12:1x ET; confirmed).** HY OAS [10/14] = **325** on both the fetch.py and cache-busted pulls (≥321 ⇒ ≥+5bp vs 316 [10/13]); CRWV raw 77.81→65.78 = −15.46%. Gate stays **2-of-2 FIRED, count unchanged** (letter: a new L4 observation, not a re-count).
- **10/15 session: NOT FIRED.** HY 325→323 (−2); CRWV raw +5.94% (69.69); IREN −0.56 · APLD +0.32 · NBIS +1.29.
- **10/16 session: equity half NOT MET (provisional).** yfinance raw bars at 16:20 ET: CRWV −11.91% (61.39) · NBIS −12.18% · APLD −11.48% · IREN −11.19% — all four fell 11–12%, none ≤ −15.00%. HY [10/16] unpublished (≈Mon 10/19). Bars are pre-official; ~3pt margin.
- **L3 (new-issue concession) — Volta ~$5B loan, CANDIDATE ONLY, UNGRADED.** Bloomberg 10/15 19:25 ET (unnamed sources, via WALTER SIG-W-20261016-017): sold at benchmark+650 / 95c vs talk +625–650 / 97–98. That reads as *re-priced cheaper on OID*, but (a) the letter says L3 stays NO_INSTRUMENT and must not be graded from a proxy or press, (b) it is a loan where the letter names HY new issues, (c) the >50bp-cheap conversion needs maturity/cash flows (UNKNOWN). Gate is already FIRED, so no count consequence either way. VULCAN owns S5 on the same deal.
- HY >320 line: RED-FT-02 / REG-T-03 are RED's and REGINALD's counts — not graded here. **My own KILL_MEMO row-60 count (WQ-444): 2-of-3** — 325 [10/14] · 323 [10/15], both first-published (watcher `count_basis: first-published-series`). Third bar = 10/16 cell, published ~Mon 10/19.

## ③ Discount window — `WLCFLPCL` Wednesday 10/14

| Series | 9/23 | 9/30 | 10/7 | **10/14** |
|---|---|---|---|---|
| Primary credit, Wednesday point ($M) | 6,235 | 8,738 | 9,965 | **11,044** |
| Primary credit, week average ($M) | — | — | 7,701 | **11,312** |

- Primary: H.4.1 released 2026-10-15, Table 1 (https://www.federalreserve.gov/releases/h41/20261015/), Wednesday column 11,044; week-average 11,312 (+3,611 w/w). FRED cache-busted CSV agrees. ⚠️ The plain `fetch.py fred WLCFLPCL` call returned 10/7 as latest — CDN-stale; the varied request returned 10/14.
- **Highest Wednesday point since 2023-04-26** (73,855 — the SVB-era tail), computed on FRED history from 2020; third consecutive weekly rise. Reserves (WRESBAL, week avg) $3,022.140B [10/14] — above the <$2.8T line.
- **No registered threshold; not a LIQ-07 leg.** H.4.1 names no borrowers; a rising primary-credit balance can be de-stigmatised precautionary use or real need — not distinguishable from this series. NEXUS T-30 context.

## ④ August TIC (Treasury, released 2026-10-16 ~16:00 ET) — aggregate read; ZHAO owns the country grade (ZHA-18)

Source: Treasury press release sb0662 table (net transactions, NSA) and TIC Table 5 (`slt_table5.txt`, holdings). **Rule Zero: levels ≠ flows.**

| Treasury net foreign purchases, Aug-26 ($B) | Bonds & notes | Bills | Total |
|---|---|---|---|
| Official | +18.1 | −42.2 | **−24.1** |
| Private | +90.9 | −5.6 | **+85.3** |
| All foreign | +109.0 | −47.8 | **+61.2** |

- **Same structure as June, larger: the private bid absorbs official supply.** Official selling is all bills (official bills holdings 354.4→312.2, matching the −42.2 flow); official coupons were bought (+18.1).
- Headline: total net TIC inflow +$199.8B; foreign net LT purchases +$300.7B (private +257.8 / official +42.9).
- Holdings levels (Table 5, LEVEL only, valuation-mixed): total 9,248.4→9,331.7 (+83.3 vs +61.2 flow ⇒ wedge ≈ +22, prices/other) · Japan 1,103.9→1,068.3 (−35.6) · China 618.0→590.7 (−27.3) · **Belgium 490.5** (<$500B; bare level, no China inference — not tripped, $9.5B away) · Cayman 460.1→463.0 · UK 1,009.5.
- **Not obtained:** country NET TRANSACTIONS (Japan LT-vs-bills split for the >$20B LT trigger; China flow) and Cayman bills composition (~$210B July Bloomberg-chart claim stays UNVERIFIED). The TIC country transaction files reached (`s1_globl.txt`, `slt1d_globl.txt`) stop before 2026-08 — stale/historical copies. ZHAO's L405 read owns these; reconcile to ZHAO's figure.
- CN+KR >$50B/qtr and Japan >$20B LT routes: UNGRADED here (no country flows).

## Also graded on the fresh cells (no change)

GATE-HY-REKILL NOT FIRED 0-of-2 (323 [10/15]) · GATE-LIQ-072 QUIET (IG 84 ≤ 94; basis 239 ≥ 180) · GATE-LIQ-079 NOT ARMED (+7 [10/15]) · GATE-LIQ-076 INSTRUMENT-FAULT persists (CFTC HTTP 403 at 16:16 ET; as-of-10/13 W1 file UNMEASURED).
