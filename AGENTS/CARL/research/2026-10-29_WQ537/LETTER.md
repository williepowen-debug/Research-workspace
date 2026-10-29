# CRL-32 — Household buffer drawdown letter (WQ-537 A)

Registered 2026-10-29 09:35 ET by CARL (session carl-1029-wq537), on Will's ruling WQ-537 A (09:26 ET, verbatim *"A approved"*; his framing 09:23 ET: *"households spending out of savings seems important. Especially as costs continue to climb."*). Relay: `inbox/2026-10-29_from-PROME_WQ537-A-RULED-buffer-drawdown-letter.md`. Canonical row: `thesis/PREDICTIONS.tsv` CRL-32. This file is the full letter; the TSV row carries it in short form and wins on any disagreement.

## 1. Baseline (September, as published by BEA 2026-10-29 08:30 ET; re-pulled FRED 2026-10-29 09:33 ET via `FORGE/tools/market-data/fetch.py`)

| Series | Identifier | Sep 2026 | Aug (rev) | Jul (rev) | Jun | May |
|---|---|---|---|---|---|---|
| Personal saving rate, % of DPI | FRED PSAVERT; BEA NIPA Table 2.6 (monthly personal income and its disposition) | **3.8** | 4.0 | 4.5 | 4.4 | 4.4 |
| Real DPI, $bn chained 2017, SAAR | FRED DSPIC96; Table 2.6 | **18,366** (−0.27% m/m) | 18,416 | 18,414 | 18,358 | — |
| Real PCE, $bn chained 2017, SAAR | FRED PCEC96; Table 2.8.6 / 2.6 | **16,978** (+0.015% m/m) | 16,975 | 16,882 | 16,854 | — |

Source detail and revisions: `research/2026-10-29_GDP_PCE/GRADE.md` (L842, c72a848ac). September 3.8% is the lowest since October 2022 (3.6%).

## 2. Release dates (BEA news schedule, https://www.bea.gov/news/schedule, read 2026-10-29 ~09:30 ET, page last modified 10/29/26, no schedule-change notes)

| Print | Date | Time |
|---|---|---|
| Personal Income and Outlays, **October 2026** | **Wed 2026-11-25** | 08:30 ET |
| Personal Income and Outlays, **November 2026** | **Wed 2026-12-23** | 08:30 ET |

## 3. The letter

**Claim:** the September shape (spending held, real income down, saving drawn down) persists through the next two prints: households keep financing consumption out of their saving while real income does not grow.

| Outcome | Wording in figures |
|---|---|
| **FIRE** | The first-published saving rate is **≤3.8%** in the October print (11/25) **AND ≤3.8%** in the November print (12/23), **AND** real DPI in the 12/23 vintage is **at or below** its September level in that same vintage (DSPIC96 Nov ÷ Sep − 1 ≤ 0.00%). |
| **NOT-FIRED — REBUILD** | Either first-published saving rate prints **≥3.9%**. Resolves early at 11/25 if October prints ≥3.9%. |
| **NOT-FIRED — INCOME-LED** | Both saving rates ≤3.8% but real DPI Nov ÷ Sep − 1 **> 0.00%** in the 12/23 vintage: low saving with rising real income is spending out of income growth, not a squeeze on buffers. |
| **UNGRADEABLE** | Either release is not published by **Fri 2027-01-29** (lapse/postponement); or BEA changes the saving-rate definition or rebases chained dollars between 11/25 and 12/23 such that the Sep and Nov real DPI levels in the 12/23 vintage are not on one basis. A late but published release is graded at publication. |
| **KILL (VOID, retired unscored, not a MISS)** | The 11/25 release revises **September's** saving rate to **≥4.3%** (+0.5 pp): the premise ("3.8%, lowest since Oct 2022") has been revised away (the CRL-11 failure shape). Recorded as VOID-BY-REVISION. |

**Vintage rule (as-published; revisions kept separate):** each month's saving rate is graded at its first print and never re-graded. The real DPI leg is computed inside ONE vintage (12/23), Nov level against Sep level, so no cross-vintage splice. Every revision to Jul–Oct is entered in a separate revisions table in the grade file; a revision never changes an outcome except through the KILL row above. Saving rate is graded on BEA's published one-decimal figure (3.8 exactly counts as ≤3.8; no recomputation from levels). Real DPI ratio is computed from the published levels and rounded to two decimals of a percent; 0.00% counts as ≤0.

**Real PCE** (PCEC96) is reported at each grade as the shape descriptor (held / cut) and is **not** a grading leg: with saving falling and real income flat or down, spending cannot also be cut much, so a third leg would add conjunction risk without adding information.

**Probability: 25% [CONJUNCTION-PRICED].** Saving rate ≤3.8 twice: about 45% (the rate fell 4.5 → 4.0 → 3.8 over three months, and has been revised down 0.1 pp in each of the last two releases; October regular gasoline eased, which helps real income). Real DPI flat-or-down over two months: about 45% (fell in April and September; nominal income +0.2% in September). The legs are positively correlated (weak real income pushes saving down), so the joint sits above the 20% independence product and below the 45% minimum. Failure-pattern preamble read (CRL-11 revision, CRL-24 conjunction, CRL-01 magnitude): the KILL row and the single-vintage DPI rule are the answers to the first, this price to the second.

## 4. Cost leg (pointer, not a restatement)

The "as costs continue to climb" half of Will's question is HENRY's to grade: **HENRY's October CPI card, DOCKET L775 (Tue 2026-11-10 08:30 ET, BLS).** The one figure this letter takes from it: **October CPI-U all-items, seasonally adjusted, m/m %, as HENRY records it.** It labels a FIRE (or a NOT-FIRED) as occurring with costs still climbing or easing; it does not enter the grade. November CPI (Thu 2026-12-10, per HENRY's calendar) is taken the same way for the 12/23 grade. CARL does not grade CPI.

## 5. Cohort leg (who is drawing down): descriptive, not graded

Instrument and first frozen observation: `COHORT_BASELINE.md` (Fed Distributional Financial Accounts, deposits per household by income group; next release with Z.1 on Thu 2026-12-10 12:00 ET). ⚠️ The DFA's 2026 cohort split is a Fed **model allocation** (SCF-based shares forecast beyond the latest survey year), so it can describe but cannot by itself establish who drew down. A FIRE without a cohort read stays an **aggregate** finding.

## 6. What a FIRE changes, and what it does not

| A FIRE changes | A FIRE does NOT change |
|---|---|
| STATUS Savings / real PCE / real DPI row: 🟠 "buffer drawdown" (one month) → 🔴 "sustained buffer drawdown" (three months) | The convergence score 53/70 or any vector score (V-scores move only under their registered THESIS triggers; none is keyed to BEA saving) |
| A dated evidence entry under THESIS's cost-squeeze mechanism (V5/V8 context), with the cohort label from §5 | Any threshold on any CARL letter, or on any other desk's letter, gate or band |
| Obligates CARL to read the next cohort instrument (DFA 12/10, HHDC Q3/Q4) against it at the following session | No card, no trade proposal, no paper-sleeve row, no capital meaning |
| — | The 10/12 scope judgment: a FIRE is aggregate buffer drawdown, not "broad spending collapse" and not "bottom 60% converging" |

A NOT-FIRED changes the same STATUS row the other way (🟠 → 🟡 "one-month drawdown, not sustained") and nothing else.

## 7. Grade obligations (later touches; this session grades nothing)

| Date | Touch |
|---|---|
| Wed 2026-11-25 08:30 ET | October print: saving-rate leg 1, KILL check (September revision), early NOT-FIRED check |
| Thu 2026-12-10 12:00 ET | DFA Q3 cohort read (descriptive) |
| Wed 2026-12-23 08:30 ET | November print: saving-rate leg 2, real DPI single-vintage leg, final outcome |
