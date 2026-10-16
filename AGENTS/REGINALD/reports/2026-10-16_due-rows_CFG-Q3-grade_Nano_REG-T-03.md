# REGINALD — 2026-10-16 due rows: CFG Q3 WQ-318 grade (D:L620) · Nano P&A (D:L516) · REG-T-03 count · failures count

**Session:** PROME-spawned (prome-ac), WQ-184 L0, Tier 1, $0. Written 2026-10-16 13:41 ET (from `date`). No score, threshold, ladder, gate letter or trade moved. Prices/spreads pulled live this session (FRED API, yfinance via `.venv`), never from STATUS.

---

## 1. D:L620 — CFG Q3-2026, WQ-318 pre-committed observation → **INCONCLUSIVE** (leans DOWN)

**Source (all PRIMARY):** CFG 8-K filed 2026-10-16, acc **0000759944-26-000206** (items 2.02/7.01/9.01): `a3q26earningsrelease.htm`, `q326financialsupplement.htm` (p.6 quarterly average balance sheet), `a3q26earningspresentatio.htm` (slides 3, 5, 9, 10, 13, 16, 27). Downloaded 13:37 ET. **Call transcript NOT read** (Quartr connector requires authentication in this runtime; not attempted) — management's stated motive for the FHLB build is therefore UNKNOWN.

Frame = `reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md` Deliverable 2, CFG row, plus the common leg definitions; checklist `reports/2026-10-11_CFG_Q3_earnings_read-note.md`. Graded on the named lines only.

| Named line | Q2-26 | **Q3-26** | Frame test | Result |
|---|---|---|---|---|
| IB deposit cost (supplement p.6, avg) | 2.08% | **2.13%** (+5bp) | F2/CFG-F: ≥2.18% | not met |
| Total deposit cost | 1.63% | **1.66%** (+3bp) | context | — |
| Avg NIB deposits | $39,881M | **$40,567M** (+1.7%) | F1/CFG-F: <$37.9B (−5%) | not met (rose) |
| NIB share of period-end deposits (company) | 22.05% (40,939/185,620) | **22.09%** (40,916/185,228); deck "NIB 22%" | CFG-F: ≤20% · DOWN: ≥22% | not met; DOWN leg holds |
| FHLB advances, period-end (company) | $5,763M | **$7,613M** (+32%) | borrowed-funds ≥15% / FHLB > $7.32B [CR] | **met on company basis** ([CR] bank-level confirm 11/07) |
| FHLB advances, average | $3,538M | **$4,718M** (+33%) | — | — |
| Total borrowed funds, period-end / avg | $16,349M / $14,101M | **$17,832M (+9%) / $15,668M (+11%)** | — | below 15% on the total |
| Capital call + private-credit finance (drawn) | $14,727M (10-Q Table 9) | **$15.0B** (deck s27: capital call $10.5B + PC finance $4.5B) | N: > $15.46B | not met — **deck basis, INFERRED comparable**; 10-Q Table 9 confirms ~early Nov |
| Unfunded NDFI commitments (the "≈ drawn, $22.5B" line) | $22.48B [CR] | **NOT PRINTED** in release/supplement/deck | separate instrument, never an observed draw | ungradeable until 10-Q / 11/07 Call Report |
| NDFI-book criticized / nonaccrual | [CR] $0.13M | **NOT PRINTED** by book (total nonaccrual $1,461M vs $1,435M, +2%) | N alt. | ungradeable from release |
| NII vs guide | guide Q3 "up 2.5–3.5%" | **$1,675M vs $1,631M = +2.7%** | IB cost rise inside guide, no N ⇒ INCONCLUSIVE | inside guide |

**Classification.** Common legs: F1 no · F2 no (+5bp < 10bp) · **F3 yes (FHLB +32%)** · N no (deck basis). UP needs ≥2 F legs **and** N → fails. DOWN needs no F leg **and** no N → fails on F3 and on IB cost >2.08%. CFG-specific UP needs a cost/NIB condition **plus** the borrowing condition **and** N → the cost/NIB part fails outright. ⇒ **INCONCLUSIVE**, one leg family only (funding, wholesale side), cheap-deposit leg not moving. This is the modal outcome stated in advance on 10/7.

**Separate facts — reported, NOT classified on:**
- **FHLB +$1.85B in the quarter while deposits were flat** (period-end −$392M) and the LDR is 80% spot. The frame forbids inferring distress from FHLB growth without a disclosed motive; motive not read (no transcript). The system-level REG-T-06 Q3 count is not touched by one bank's balance.
- **TCE ratio 7.2% → 6.7%** (deck s13) with securities duration 4.1 → 4.6 years (release) — an AOCI/rate-mark move, not credit. CET1 10.5% (8.7% AOCI-adjusted). Not a WQ-318 line.
- Credit clean on the quarter: NCO 37bp stable, provision $125M vs $134M, ACL/nonaccrual 149% vs 152%. 4Q26 guide: NII +2.5–3%, NCO "stable to down slightly".
- **DLIC / Group 1001 $450M revolver:** no mention in release, supplement or deck (grep, 0 hits) → **not disclosed; unresolved**, YE25 date retained.
- **BROCK interface:** BROCK's frozen BRK-31 CFG row uses $12.852B (8.756 + 4.096); this desk's Q2 base is $14.727B (Q2 10-Q Table 9, acc 0000759944-26-000148). The Q3 deck's $15.0B is a third basis (rounded slide). Which vintage BROCK's figures come from is UNKNOWN to me (Q1-26 10-Q is a candidate, INFERRED) — packeted to BROCK; no frozen frame edited.

**Next confirmation:** 10-Q Table 9 (~early Nov) for N; 11/07 Call Report run for F1/F3 on [CR] basis (⚠️ FFIEC JWT expires 11/05 — Will action). Grade is provisional in exactly the way the frame said it would be.

---

## 2. D:L516 — FDIC Nano Banc P&A agreement → **NOT POSTED** (as of 2026-10-16 13:38 ET)

| Search run (13:37–13:38 ET) | Result |
|---|---|
| `https://www.fdic.gov/bank-failures/failed-bank-list/nano-banc` | HTTP 200; "Transaction Documentation" section lists **Bid Summary only**; page "Last Updated: October 8, 2026"; no PDF/agreement link in any href |
| `https://www.fdic.gov/bank-failures/nano-banc-irvine-ca` | HTTP 404 |
| FDIC failed-bank list page + `download-data.csv` | Nano Banc, Irvine CA, cert 58590, acquirer Sunwest Bank, closed 25-Sep-26, fund 10555 — no P&A link |

Date basis: posting was a modeled check-by (~10/05–10/09 on the Metropolitan Capital precedent); it is now **21 days after closing** and unposted. Every L516 question stays open and is graded separately when posted (DEWEY 10/14 boundary: schedules may not settle pool sizes, the $97.1M HFS pool, or named loans): retained-pool allocation · $97.1M HFS disposition · discount/premium/loss-share (bid summary: 0.85% deposit premium, no loss-share — that part is already answered by the Bid Summary, not the P&A) · ~$81M deposit gap. The 10/9 retained-pool SCENARIO (≈$70–90M ≈32–42% of ≈$215M; direction VERIFIED, magnitude INFERRED) stands unchanged. Proposed re-check: **Tue 10/20**; DEWEY's 10/27 source-escalation checkpoint stands.

---

## 3. REG-T-03 count → **2-of-3** (letter: HY-OAS > 320 bps, 3 consecutive daily closes, FRED `BAMLH0A0HYM2`)

| FRED date | HY OAS | >320? | Run |
|---|---|---|---|
| 10/09 | 311 | no | — |
| 10/12 (Columbus Day; forward-filled 3.11 = 10/09) | 311 | non-session, excluded (see §5) | — |
| 10/13 | 316 | no | reset |
| **10/14** | **325** | yes | 1 |
| **10/15** | **323** | yes | **2** |
| 10/16 | publishes ~Mon 10/19 AM | — | — |

Vintage: FRED API pull 13:38 ET 10/16; series `last_updated` 2026-10-16 08:59:55 −05. Earlier 10/1 cell 324 was reset by 310 [10/2] (WALTER -022 correction acknowledged; this desk never cited "first ever").

**What fires, in my letter's words:** if the 10/16 daily close prints **> 320**, REG-T-03 reaches 3 consecutive daily closes → state **CREDIT-CANARY-FIRED**, action REGINALD / CARL info. The registered qualification then binds: *a wide HY print is NOT self-evidently bank transmission* — the fire is recorded with the bank-credit cross-check verdict beside it, never as bank transmission by itself. **What resets:** a 10/16 close **≤ 320** (320 exactly does not count) resets the run to 0-of-3. **Exit (only after a fire):** HY ≤ 300 on 5 consecutive daily closes. REG-T-04 (>350) is not in play (35bp away).

**Bank-credit cross-check (method of `reports/2026-07-30_bank-side-HY-attribution.md`), window 10/13 → 10/15:**

| Instrument | 10/13 → 10/15 | Proportional |
|---|---|---|
| BB OAS | 191 → 197 | **+3.1%** |
| B OAS | 317 → 326 | +2.8% |
| HY OAS | 316 → 323 | +2.2% |
| BBB OAS | 103 → 105 | +1.9% |
| IG OAS | 83 → 84 | +1.2% |
| CCC OAS | 1,267 → 1,278 | **+0.9% (last)** |
| Bank junior-sub/preferred basket, n=10 (ZIONP, HBANM, OZKAP, TFC-PR, WAL-PA, VLYPP, VLYPO, CFG-PE, HBANL, KEY-PI; yfinance closes) | — | **mean +0.06%, median +0.04%; 2 of 10 down** (OZKAP −1.26%, VLYPO −1.02%) |
| KRE / KBWB | 69.06 → 69.75 / 86.77 → 86.61 | +1.00% / −0.18% |
| BKLN / PFF / PGX | — | 0.00% / −0.44% / +0.50% |

**Verdict: BANK-ABSENT on the 10/14–10/15 sustain** — confidence moderate (~0.7; INFERRED). Widening is proportionally led by BB/B, CCC moves least: a rate/duration signature (hot CPI 10/14, PPI +1.3% m/m 10/15), not a tail-credit break; bank credit instruments flat. CCC/HY ratio 3.96× [10/15] (1,278/323), `VX-REG-18.04` HARD-FIRE continuing, not CCC-led re-cross. ⚠️ **OZKAP −1.26% is the one bank-specific mover**, four sessions before OZK's 10/20 print — single-name, not cohort; noted, not graded. ⚠️ **RED's composition caveat is RED's** (AI-levered issuers — the CoreWeave/AI-infra leg, SIG-W-20261014-018 / -20261015-005: CRWV 2032 YTW 15.83% [10/14], CDS ~1,059–1,120bp): cited, not re-derived — it says *which* issuers are widening, which is a further reason the HY level is not a bank read. Preferred closes are thin-volume single-source vendor prints. The 10/16 bars in the vendor pull are intraday and are excluded from the grade.

---

## 4. Bank failures 2026 → **6, unchanged**; SIG-W-20261015-013 DISCARDED

FDIC `download-data.csv` re-pulled 13:38 ET: closing dates in 2026 = **6** — Metropolitan Capital (IL) 1/30 · CB&T West Georgia (GA) 5/1 · Kentland FS&LA (IN) 7/10 · **Small Business Bank (KS) 7/17** · Tioga-Franklin (PA) 8/21 · Nano Banc (CA) 9/25. None after 9/25 (VERIFIED). -013 discarded per WALTER -002 (KBRA article dated 2023-08-01). ⚠️ **One fact worth knowing about why the false item looked right:** the 4th 2026 failure on the FDIC list *is* a Kansas bank (Small Business Bank, 7/17) — so "a Kansas bank = 4th failure of 2026" is literally true of July, but it is not a new failure and not the bank in the 2023 article. Count stays 6.

## 5. REG-T-03/04 non-session rule (WALTER ask 10/14) — owner confirmation

My letter counts "consecutive **daily closes**". A FRED bar dated on a SIFMA full close or NYSE holiday is a forward-fill, not a close: it is **excluded and the run bridges it** (neither counts nor resets). This is a reading of the existing letter — no level, operator, instrument or consequence changes — and matches RED's FT-02 rule so one crossing counts the same on both rows. Recorded in `registry/NOTES.md` §REG-T-03.

## 6. REG-T-06 / FHLB Q3 calendar (WALTER SIG-W-20261016-025) — owner reconciliation

The letter (`registry/THRESHOLDS.tsv` REG-T-06, `grading_instrument`) names the **Combined Financial Report** system advances line → as written, Q3 grades at the **CFR, 11/13** (OF calendar, subject to change). ⚠️ **Basis discrepancy found, not silently fixed:** the Q2 $810.7B leg was graded from the **Q2 Combined Operating Highlights** (pub 7/30; `research/FHLB/sources/SOURCES.md` row 15), not the CFR. So the practice used for legs 1–2 and the letter disagree. Plan, no letter change: record the 10/30 Highlights value as a dated reading; grade leg 3 at the named CFR on 11/13 unless Will rules Highlights eligible; confirm the Q2 CFR advances figure equals $810.7B at the 11/13 read. Whether Highlights may substitute is an instrument question → PROME/Will, not mine to settle by edit.
