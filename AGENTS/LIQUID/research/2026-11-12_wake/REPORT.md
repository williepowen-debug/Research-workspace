# LIQUID wake, Thursday 2026-11-12 (PROME prome-e8, WQ-184 due-row class C6, D:L1124)

Written from 09:06 ET (desktop, Claude Code / Opus 5.5). Research only: no trade, card, threshold, letter, band or score moved.

## 1. The ICE cell dated November 11 and the missing November 10 cell

**What FRED shows (API read 09:01 ET, all vintages since October 15):** every ICE series carries a row dated 2026-11-11 and **no row dated 2026-11-10**. 11/9 rows unchanged.

| Tier | 11/9 (first-published) | row dated 11/11 | difference |
|---|---|---|---|
| HY (BAMLH0A0HYM2) | 334 | 330 | −4 |
| IG (BAMLC0A0CM) | 91 | 90 | −1 |
| BBB | 113 | 112 | −1 |
| BB | 200 | 193 | −7 |
| B | 350 | 347 | −3 |
| CCC | 1,311 | 1,330 | +19 |
| HY effective yield (BAMLH0A0HYM2EY) | 8.00% | 8.11% | +11 bp |

HY−IG 240, CCC−BB 1,137 on the 11/11-dated row.

**This row is not a carry.** In the first-published set since 2023-11-14 26 earlier SIFMA full closes carry a row; 21 repeat the prior value exactly and 5 differ by 1 or 2 bp (largest: 2024-01-15, 354 against 356). **There is no earlier case of a missing session row** (scan of every weekday session 2023-11-14 to 2026-11-09: zero missing). So this is new: a valuation that moved on every tier, dated on a bond-market closure, with the session before it absent.

**Likely, not established:** the row is ICE's November 10 valuation under the November 11 date. Supporting: ICE does not price on SIFMA closures (21 of 26 exact carries); the HY yield +11 bp with OAS −4 bp fits the November 10 Treasury sell-off (10-year about 5.00% vendor intraday 11/10, auction high yield 5.020%, against DGS10 4.88 on 11/9), and Treasuries did not trade on 11/11. Against certainty: nothing from ICE or FRED says so; FRED may still post an 11/10 cell or re-date this one.

### 1.1 How my written rule counts it

The rule is D:L342 (ruled November 10, fix 398a946b9a; REPORT `research/2026-11-05_live-catchup/REPORT.md` §19.1; code `scripts/gate069_legs.py` `BOND_CLOSED` and `hy_session()`), plus the GATE-HY-REKILL letter's clause *"non-publication days — weekend, holiday, or a missing/NA print — do not break consecutiveness; a day whose print is not yet published is NOT an observation until it publishes"*.

- **The row dated November 11 is not an observation.** The rule is keyed on the calendar, not on the value: *"A row on any other day is a carry or a month-end weekend valuation: never a counted observation."* The month-end weekend rows already showed a non-session row can hold a distinct value and still not count.
- **November 10 has no observation yet.** It is unpublished; it is not counted, and it does not break a run. If FRED posts it, I grade it at first publication.
- **The readers already do this** (09:00–09:03 ET runs): `transmission_check.py` latest session row 11/9; `gate069_legs.py` marks the 11/10 session UNGRADEABLE-PENDING-PUBLICATION and 11/11 UNGRADEABLE (bond market closed); `boot.py`'s level line prints the newest FRED row (330, obs 11/11), a display, not a count.

**What the rule does not cover:** moving a row to a different date. Counting the 330 as November 10's observation would change how a registered count is taken (every letter takes observations "as first published", and this one was published as 11/11). I do not do it. That would be Will's call. **No grade today depends on it** (§1.2): every line fails under either dating. It would matter only if a later count turned on such a row, for example a sub-260 or over-350 value dated on a closure with the session before it missing. My recommendation: no ruling now. If FRED never posts an 11/10 cell, the 330 stays out of every count, and the >320 run loses one observation (8 instead of 9) and nothing else.

### 1.2 Grades (LIQUID rows only; observation dates in brackets)

| Row | Grade by my rule | Would the other dating change it? |
|---|---|---|
| >320 first-published run | **8 observations, unchanged** (326 [10/29] … 334 [11/9]); 11/11 row not counted; 11/10 pending. Still MET (≥3). DOCKET L1124 expected 9; by rule it is 8 | 9 instead of 8; still MET, no new consequence |
| GATE-HY-REKILL | **NOT FIRED, 0 of 2** through 11/9 (334); no new observation | NOT FIRED (330 is 70 above 260) |
| Tier rule (September 25 order) | **No new grade**: no new session row; last grade STALLS [11/9] | Not computed (that would be the improvised count). Raw differences in §1 table, context only |
| 069 L1 | **NOT FIRED** [11/9]: BB 200, 20 under 220; CCC 5-session −8 | BB 193 on the 11/11-dated row, fails 220 |
| 069 L4, session 11/10 | **UNGRADEABLE-PENDING-PUBLICATION** (HY 11/10 unpublished). Equity half fails by itself: worst name IREN −7.85% (vendor raw close 19.73 against 21.41), CRWV −0.51%, APLD −0.24%, NBIS −5.27%. No fire possible for this session whatever HY prints | HY −4 also fails ≥+5 |
| 069 L4, session 11/11 | **UNGRADEABLE** (bond market shut, D:L342). Equity half fails anyway: all four names rose (CRWV +24.71%, IREN +5.63%, APLD +7.37%, NBIS +15.44%, vendor raw closes) | same |
| 069 L4, session 11/12 | **UNGRADEABLE** by rule (an HY change would span two equity sessions) | — |
| 069 count | **2 of 2 FIRED stands** (L2 and L5; L4 re-observed November 5); no new consequence | — |
| GATE-LIQ-072 price leg | **NOT FIRED** [11/9]: IG 91 fails >94; HY−IG 243 fails <180 | IG 90 and basis 240 fail both |
| GATE-LIQ-079 | **NOT ARMED**: SOFR99 3.97% − IORB 3.90% = **+7 bp [11/10, non-calendar]**, NY Fed primary read 09:05 ET; prior +6 [11/9]. FIRE not graded while unarmed. No SOFR for 11/11 (holiday) | n/a |
| GATE-LIQ-076 | **Not graded today**: W2 as-of 11/4 not yet published (NY Fed API latest as-of 10/28 at 09:05 ET); W1 as-of 11/10 is CFTC's. Window state unchanged, 1 of 3 (W3) | n/a |

Funding 11/10 (NY Fed primary): SOFR 3.89, p1 3.83, p25 3.87, p75 3.95, p99 3.97, volume $3,159B; EFFR 3.88, p75 3.88 (not above IORB 3.90). Standing repo $0.005B, RRP $0.15B [11/10, FRED]. Calm; nothing near any line.

REGINALD's >350 ×3 is REGINALD's letter; 330 is under 350 under any dating, so nothing there turns on this.

## 2. DTCC CDS: late prints after CoreWeave's results

- **November 11 cumulative file** (513 rows; holiday-thin): **no CoreWeave, Oracle or Paramount rows.** SoftBank rows are the ones already read 11/11 (5Y 08:13Z, 3Y 03:40Z and 06:00Z, 2034 08:10Z).
- **November 12 intraday slices** (207 slices, 1,412 rows, read 09:05 ET): **no CoreWeave, Oracle or Paramount rows yet** (US session barely open). SoftBank 5Y **473** (00:29Z and 00:34Z, 793.7M+ yen and 500M yen), 3Y 457 (01:00Z), 2034 503 (09:22Z), all yen 100 coupon, converted at r = 1%, R = 40%, ±10 bp. Against 475 [11/11 Tokyo]: flat.
- Paramount: latest stays 529 [11/9]; TERRY's 614 re-open line not crossed (no print).
- **First Oracle prints after CoreWeave's results (poll hit, read 10:21 ET; slices 273–274):** three new trades executed 15:08:32–15:08:40Z (10:08 ET), all senior, 100 bp coupon, notional disseminated only as "5,000,000+", upfront-fee rows (`UFRO`), no spread field. December 2026 maturity: upfront $8,026.47, twice (one cleared, one uncleared, same second: most likely one trade and its clearing leg). June 2027 maturity: upfront $9,809.91. **No spread recoverable:** the notional is capped, so the fee cannot be put on a per-cent basis, and the payer side is not disseminated. Neither is the 5-year point. **Moves no row:** 069 is 2 of 2 FIRED already; no LIQUID line keys on short-dated Oracle CDS. Context only: an upfront paid on a 100 coupon fits a short-dated spread above 100 bp, if the protection buyer paid (not established).
- **CoreWeave rows in the same slices (263) are not new trades:** two `CORR` corrections to May and July records on the CoreWeave delayed-draw loan total-return lines (`COREWEAVE FINANCING-DDTL`, `COREWEAVE (7/26) TRS-DDTL`). No CoreWeave CDS trade through slice 278.
- **First CoreWeave CDS after its results (poll hit, read 10:50 ET; slice 306):** one new trade 15:46:42Z (10:46 ET), senior, **4-year (December 2030)**, **$3,000,000 exact** (not capped), 500 bp coupon, cleared-intent, BILT. Cash upfront $427,916.664 = 3,000,000 × (0.15 − 53/360 × 0.05): **quoted 15.00 points upfront**, net of the coupon accrued from September 21. The quote is above zero on a 500 coupon, so the protection buyer paid; a seller-pays reading would need a spread under 100 bp. **Converted (flat hazard, r = 4%, R = 40%, the probe default): about 1,047 bp** (about 1,009 at R = 25%), model-derived, not executable.

  | CoreWeave 4Y (Dec 2030) | Level | Basis |
  |---|---|---|
  | November 10, before results | 1,093 to 1,105 | DTCC 11/10 final file, same method (REPORT 2026-11-11 §4) |
  | **November 12, after results** | **about 1,047 (one trade, 10:46 ET)** | DTCC slice 306 |

  **Read:** about 50 bp tighter at the same tenor on one trade. Credit's first verdict agrees with the equity bounce (CRWV +24.71% on 11/11), modestly. One print is not a level. The 5-year (December 2031; 1,154 median before results) has not traded yet. **Moves no row:** 069 L2 is a re-widening of more than 100 bp on the 5-year from two quotes; the gate is already 2 of 2 FIRED, and this is a tightening on another tenor. KB-LIQ-073 has no numeric line.
- **First Oracle trades with a disseminated spread after CoreWeave's results (poll hit, read 11:58 ET; slices to 386):** 16:47:34Z and 16:47:47Z, **2-year (December 2028) 175 bp** twice (same $66,389 upfront: likely one trade and its clearing leg); 16:47:59Z, **3-year (December 2029) 222 bp**, upfront $161,267. Notional "5,000,000+" (capped). The upfronts are consistent with about $5M at those spreads over the 100 coupon (implied annuity 1.77 and 2.64). Disseminated spreads, no conversion.

  | Oracle | Before results [11/10, REPORT 2026-11-11 §4] | November 12, 11:47 ET |
  |---|---|---|
  | 1Y | 108 | — |
  | 2Y | — (about 163 interpolated, 1Y–3.5Y line) | **175** |
  | 3Y | — (about 218 interpolated) | **222** |
  | 3.5Y / 4Y / 4.5Y / 5Y | 246 / 271 / 288 / 300–302 | — |

  **Read:** against a straight-line interpolation of the pre-results curve, Oracle's 2-year and 3-year are flat to about 10 bp wider. Unlike CoreWeave's 4-year (about 50 bp tighter), Oracle's credit has not joined the relief. The interpolation is mine and crude; no like-for-like pre-results tenor exists. **Moves no row:** no LIQUID line keys on Oracle CDS levels; 069 L5 is the ratings ladder.
- **Oracle 10-year (poll hit, read 12:58 ET; slice 434):** 17:47:04Z (12:47 ET), December 2035, **$2,000,000 exact**, 100 coupon, cash upfront $294,192.50 = 14.71 points (14.86 if the cash is net of 53 days' accrued). Name disseminated as "Oracle Cop"; RED entity 6EC42L is Oracle Corporation (same entity as the 6EC42LAE4 pair code on the other trades), senior. **Converted about 342 to 345 bp** (r = 4%, R = 40%; 330 to 332 at R = 25%), model-derived. No pre-results 10-year reference, so it shows the curve's shape (5Y 300–302 before results), not a change. Moves no row.
- **No 5-year (December 2031) trade on either name through slice 443 (12:56 ET).** FRED still shows no 11/10 HY cell (latest 2026-11-11, 3.30) at 12:56 ET. Watch ended on the 10-year hit; the final checks are at PROME's 13:15 ET read.

## 3. WALTER cards (six, all consumed)

| Card | Disposition | Read |
|---|---|---|
| 014 SEC FY2026 relief correction | info-only | $1.095B is total relief, penalties $343M; no LIQUID figure carried it |
| 015 ZHAO: China not a forced seller, Japan is the live one | noted | USD/JPY 159.38 [11/11, SAM], 0.62 under 160; boot 159.68 [11/12 vendor]. Logged to KB-LIQ-157. Belgium/TIC rules unchanged; TIC 11/18 |
| 020 Ares CEO on GPU depreciation; Semafor GPU loan portfolios shopped | noted | No price, spread or exposure. Logged to KB-LIQ-153 |
| 021 GPU-backed equipment ABS (Wingspire, Stonebriar); Korean banks | noted | No spread seen (paywall). Logged to KB-LIQ-153 |
| 024 Skydance "almost all secured" correction | acted, NO-OP | Grep of my files finds no "almost all secured" or "$86.6B secured"; nothing to change. About $69.5B secured of about $86.6B total (INFERRED) is the card's figure |
| 030 MSCI deletes Strategy (MSTR) | acted | Read-through in §4 |

## 4. Strategy (MSTR) after the MSCI deletion: does anything reach HY or funding rows?

Primary: Strategy 10-Q for September 30, 2026 (EDGAR 0001050446-26-000060, filed 11/2) and 8-K of 11/9 (0001193125-26-452693).

| Item | Figure [date] |
|---|---|
| Convertible notes | $6.71B principal, six series 2028 to 2032, **senior unsecured**; carrying $6.72B total debt [9/30]. 2028 notes $1.01B classified current |
| Secured debt | $39.8M "other long-term secured debt" only |
| Bitcoin | 847,666 BTC [9/30], **all unencumbered**; 850,364 BTC [11/8] |
| Preferred stock (notional) | STRC $9.10B (12.00%), STRK $1.40B, STRD $1.40B, STRF $1.28B, STRE €775M [9/30] |
| Annual preferred dividends plus interest | about $1.59B; USD Assets cover about 43 months [company figure] |
| Cash and short-term holdings | about $5.91B [9/30] |
| Last week's funding | MSTR ATM $283.8M net, 11/2 to 11/8: $188.3M to buy back STRC, $81.9M to bitcoin, $13.6M to cash; no preferred sold |
| MSCI | the 10-Q already expected the exclusion; deletion effective with the November review (secondary sources: close of November 30) |

**Read:** nothing reaches my HY OAS or funding rows mechanically. The debt is unsecured convertibles, which ICE's US HY index excludes as I understand its rules (not re-read today); there is no margin loan and no bitcoin pledged; no rating or debt clause is tied to an index. The channel that exists is the **cost of equity funding**: Strategy now uses common-stock sales to fund preferred buybacks and dividends, so a thinner passive holder base makes that loop dearer. That is an equity and preferred-market question (HENRY for the November 30 flow), not a credit-market or repo constraint. No gate, no new monitor. Catalyst row resolved.

## 5. What stays open

- November 10 ICE cell: grade at first publication if FRED posts it; if FRED re-dates the 11/11 row, note it on the row (first-published convention), never re-grade a closed count.
- 076: W2 as-of 11/4 (NY Fed, Thursday about 16:15 ET or later if the holiday shifts it); W1 as-of 11/10 (CFTC); PROME review 11/13.
- 30-year auction 13:00 ET (BOND grades; my lines BTC <2.0, indirect <55% sustained).
- First CoreWeave and Oracle CDS prints after CoreWeave's results.
