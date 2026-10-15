# MARCO fork — FL pulls (2026-10-14 ~20:30 ET)
Scope: BTS T-100 newest month (MCO/FLL/MIA) · MIA September Traffic Report · FL migration proxies. Nothing written to the repo. `git status -- AGENTS/MARCO/baselines/` shows only `banxico_monthly.tsv` (parent's boot fetch, not this fork). Data: `scratchpad/bts/all.tsv` (carrier=All), `scratchpad/bts/nk.tsv` (carrier=NK), `scratchpad/mia/aug26.pdf` + `aug26.txt`; calc scripts `scratchpad/bts_calc.py`, `scratchpad/voter2022.py`.

## 1. BTS T-100 (enplanements, NOT airport totals; pulled live 2026-10-14)
**Newest month now = JULY 2026** for all three (286 rows each). NK series: MCO/FLL through 2026-07 (zeros post-liquidation); MIA NK = 2021-10 → 2023-02 only (absence re-verified at carrier level).

**Basis check — June reproduces exactly:** FLL −13.22 / MCO −7.27 / MIA −5.48 YoY; 2-yr FLL −23.55 / MCO −8.30 / MIA −2.78; index −11.54. ✅
**Revisions:** NONE. Every 2025 and Jan–Jun 2026 row is byte-identical to the 9/19 repo baseline (June was the newest month on 9/19 and has NOT been revised up — the usual +0.8–2.3% first-print revision did not happen for June this cycle). Only change = July rows added.

Baselines: YoY = Jul-2026 vs Jul-2025; 2-yr = Jul-2026 vs Jul-2024; index = mean of the three 2-yr stacks (same construction that gives June −11.54); ex-Spirit = (total − NK) in BOTH years; offset = other carriers' YoY gain ÷ Spirit's YoY loss.

| Airport | Jul-26 enpl | YoY raw | 2-yr raw | ex-Spirit YoY | Spirit lost | others gained | offset | unabsorbed |
|---|---|---|---|---|---|---|---|---|
| MCO | 2,291,059 | **−5.28%** | −4.10% | **+7.01%** | 277,706 | 150,103 | **54.1%** | 127,603 |
| FLL | 1,204,279 | **−5.97%** | −15.04% | **+31.42%** | 364,367 | 287,891 | **79.0%** | 76,476 |
| MIA | 2,241,035 | **−1.47%** | −2.26% | n/a (no NK) | 0 | — | — | — |
| **Index (2-yr mean)** | | | **−7.13%** (Jun −11.54) | | | | | |

Month-specific offset series (passenger offset, NOT seat capacity — seats never measured): MCO 97.8% May → 35.6% Jun → **54.1% Jul**; FLL 59.0% → 54.5% → **79.0% Jul**.

**Read:**
- **All three FL airports negative YoY on raw BTS for the 2nd straight month (Jun, Jul).** ⛔ **CONFOUNDED / NOT IDENTIFIED** — MCO/FLL are structurally locked negative by the Spirit hole; ex-Spirit both grow (MCO +7.01, FLL +31.42), which fits demand intact AND demand falling while displaced passengers redistribute. Never "not demand".
- **MIA (the unconfounded leg): BTS Jul first print −1.47% vs MIA's OWN airport-reported Jul +0.10% — SIGN DISAGREEMENT** (gap −1.57pp, just outside the Jan–May revised-month gap range −1.17..+1.48pp from `KB-MARCO-APT-45`). Same pattern as June (airport −1.43 / BTS −5.48). Graded basis for the MIA trigger is the airport count (Will-ruled 9/24); BTS shown beside it. First prints are slated for upward revision but June was not revised this cycle — so don't assume the gap closes.
- Index improved −11.54 → −7.13 mostly on FLL's 2-yr (−23.55 → −15.04), a lapping effect as more of the 2025 base is post-Spirit-decline months; not a demand read.
- MAR-24 note: Jul is a Q3 month with all-3-negative on raw first print — but MAR-24 resolver is BTS Q3 on the first pull dated ≥2027-02-01, carrier-adjusted beside raw. Not gradable now.

## 2. MIA September 2026 Traffic Report — **UNPUBLISHED as of 2026-10-14 ~20:25 ET** (not blocked)
**Basis check — August reproduces:** combined passengers 4,289,986 vs Aug-25 4,548,858 = **−5.69%** ✅. Sum identities hold: intl 2,044,562 + dom 2,245,424 = 4,289,986; deplaned 2,152,458 + enplaned 2,137,528 = 4,289,986. Intl −4.44%, Dom −6.80%; dom seats 2,768,256 (−2.07%); dom LF (pax/seats) 81.1% vs 85.2% ✅ (matches carried).
**Index page now lists Jan–Aug 2026** (it lagged at Mar/Apr on 9/24) — no September link.

URLs tried (browser UA, base `https://www.miami-airport.com/library/pdfdoc/Airport%20Stats/`):
| Path | HTTP |
|---|---|
| `FY%202025-2026/August%202026%20Monthly%20%20Calendar%20Yr%20Traffic%20Report.pdf` | 200 (basis check) |
| `FY%202025-2026/September%202026%20Monthly%20%20Calendar%20Yr%20Traffic%20Report.pdf` | 404 |
| `FY%202026-2027/September%202026%20Monthly%20%20Calendar%20Yr%20Traffic%20Report.pdf` | 404 |
| `September%202026%20Monthly%20%20Calendar%20Yr%20Traffic%20Report.pdf` (root) | 404 |
| `FY%202025-2026/September%202026%20Monthly%20Calendar%20Yr%20Traffic%20Report.pdf` (single space) | 404 |
| `FY%202025-2026/Sept%202026%20Monthly%20%20Calendar%20Yr%20Traffic%20Report.pdf` | 404 |
| `FY%202026-2027/September%202026%20Monthly%20Calendar%20Yr%20Traffic%20Report.pdf` | 404 |
MIA-2-consecutive trigger: **NOT decidable yet** — Aug −5.69% stands as 1 of 2; Sep expected ~10/28 (docket).

## 3. FL migration proxies (`fl_migration_proxies.py`, bare run; TSV md5 unchanged before/after; rc=1 = a leg overdue)
- **Newest voter-reg month = SEPTEMBER 2026:** new registrations **66,650**; **+65.7% YoY** (vs Sep-25 40,226); YTD Jan–Sep +26.6% (425,916 vs 336,442). Net +48,279 (purge-noisy).
- **Cycle-matched vs 2022 (midterm) — basis check:** Aug-22 73,723 and Jan–Aug-22 454,701 reproduce `KB-MIG-08` exactly ✅. **Sep-26 vs Sep-22 66,507 = +0.2%** (Aug was −21.0%); **YTD Jan–Sep vs 2022 = −18.3%** (521,208) (Jan–Aug was −21.0%). The cycle-matched monthly gap closed in September; YTD still −18%. ⚠️ 2022 base confounded (FL in-migration peak; SB 7050; Hurricane Ian landfall 2022-09-28 likely touched late-Sep/Oct-22 — unverified). Midterm registration deadline 2026-10-05 pulls registrations into Sep. **Not a clean direction tell either way** (KB-MIG-08 stance holds).
- **Manual legs:** **FLDOE_ENROLLMENT flagged OVERDUE** (newest row 2025-10, 12mo old vs 9mo window; Survey 2 ~Dec–Jan) — the tool's overdue flag fires although FLDOE's next survey isn't out until ~Dec; note `FLDOE_FIRST_DUE` logic only covers an empty leg. **FLHSMV: HINT only** (quarterly window — check MIAMI Realtors for a new license-exchange piece this month; newest row 2026-H1 +3.0%), not overdue.
- Canonical `VX-MARCO-3.03` +22,517/2025 unchanged — direction tells only.

## Summary
| Item | Newest | Reading | Verdict |
|---|---|---|---|
| BTS T-100 | **Jul-2026** (no revisions to May/Jun) | YoY MCO −5.28 / FLL −5.97 / MIA −1.47; index −7.13 (Jun −11.54) | All-3-negative raw, 2nd month · **CONFOUNDED / NOT IDENTIFIED** |
| ex-Spirit Jul | Jul-2026 | MCO +7.01 · FLL +31.42; offset MCO 54.1% / FLL 79.0% | passenger offset, not seats |
| MIA BTS vs airport, Jul | Jul-2026 | BTS −1.47 vs airport +0.10 | sign disagreement (2nd month running) |
| MIA Sep Traffic Report | — | 6 URLs → 404; index lists thru Aug | **UNPUBLISHED** (not blocked); trigger undecided, Aug = 1 of 2 |
| Voter-reg (FL DOS) | **Sep-2026** | new +65.7% YoY · vs Sep-22 **+0.2%** · YTD vs 2022 −18.3% | midterm-cycle; not a clean tell |
| FLDOE | 2025-10 | −2.33% | tool flags OVERDUE (next survey ~Dec) |
| FLHSMV | 2026-H1 | +3.0% | window hint, not overdue |
