# v3 (ISM survey employment) return letter: base rates, 2026-10-28

**Question:** v3 dropped 2 → 1 on 2026-10-28 (Sep ISM Mfg Emp 52.7, Svs Emp 50.1, both >50 the same month). No rule exists to move it back up. Which candidate rule, if any, should be the return letter?

**⚠️ NOT PRE-REGISTERED.** Unlike the 10/21 C2 batch (`2026-10-21_C2_BASE_RATES_PREREG.md`), these candidates were written down in the same session the numbers were computed, so they are not a clean test. Any letter adopted from this file is post-hoc and is labeled that way.

## Data (with coverage)

| Series | Source | Coverage |
|---|---|---|
| ISM Mfg Employment Index | DBnomics `ISM/employment` series `in` (copy: `2026-10-28_ism_mfg_employment_dbnomics.json`) | 2021-01 … 2025-12, complete |
| ISM Services Employment Index | DBnomics `ISM/nm-employment` series `in` (copy alongside) | 2021-01 … 2025-12, complete |
| 2026 Mfg | ISM Sep PDF (52.7, primary); Aug 51.2 (primary page); Jun 49.7 / Jul 52.8 from LABOR's dated records | **Jan–May 2026 MISSING** (ISM archive pages return ~4 KB login stubs) |
| 2026 Svs | ISM pages Jan 50.3, Mar 45.2, Aug 47.8, Sep 50.1 (primary); Jul 47.4 (records) | **Feb, Apr, May, Jun 2026 MISSING from this set** |
| Outcome | FRED PAYEMS, current vintage, pulled 2026-10-28 | through 2026-09 |

63 months have both indexes. **Outcome:** average monthly payroll change over the NEXT three months < 100K.

## Results

Base rate of the outcome: `19/60 = 0.317`.

| Candidate | Fires | Outcome when fired | Lift |
|---|---|---|---|
| A — both <50 same month | `18/63 = 0.286` | `11/18 = 0.611` | `0.611/0.317 = 1.93` |
| **B — both <50 two months running** | `9/63 = 0.143` | `8/9 = 0.889` | `0.889/0.317 = 2.81` |
| C — both ≤48 same month | `8/63 = 0.127` | `5/8 = 0.625` | `0.625/0.317 = 1.97` |

## Why the lift is weaker than it looks

1. **Back-to-back months are not independent.** B's 9 firings are **3 episodes**: 2022-07 (next-3-month payrolls avg +289K, a **false alarm**), 2024-03/04 (avg +76K / +73K, hit), 2025-04 and 2025-07…11 (avg +19K, −45K, −4K, hit). **2 of 3 episodes hit.**
2. **The outcome's own base rate shifted.** Months under +100K by year: 2021 0/12 · 2022 0/12 · 2023 1/12 · 2024 6/12 · **2025 11/12**. Most of B's firings sit in 2024–25, when weak payrolls were the norm. Inside 2024–25 the base rate is `17/24 = 0.708`, so B's `8/8` there is a lift of about `1.00/0.708 = 1.41`, not 2.81.
3. **Hindsight vintage.** PAYEMS is the current vintage, revised down by benchmarks, so it is not what anyone saw in real time.
4. **No recession in the sample**, so this cannot test whether a rule warns ahead of a downturn. It can only measure how often each rule fires and whether it lines up with weak hiring.

## What it does show

- In the hot regime (2021–2023, 36 months), B fired **once** (2022-07). That is a low false-alarm rate. For comparison, the v7 continuing-claims candidates rejected on 10/21 fired in 21–25% of weeks.
- A fires in 29% of months. That is too noisy to move a score.

## Recommendation (for Will's call)

Adopt **B** as v3's return letter: **both ISM employment indexes <50 in two consecutive months ⇒ v3 1 → 2**. Label it **POST-HOC, weak evidence** (3 episodes, 2 hits, regime-confounded). Re-test it at the first new episode.

The alternative is no letter, which leaves v3 permanently at its floor and turns the survey layer into a record-only display.

## Ruling — 2026-10-28 (Will, AskUserQuestion in the LABOR session)

**"Adopt, labeled weak."** v3 return letter **R3-B**: both ISM employment indexes <50 in two consecutive months ⇒ v3 1 → 2. It is POST-HOC and weak evidence, and it gets re-tested at the first new episode. The Oct prints (11/2, 11/4) can only be leg 1 because Sep was >50 on both. The earliest fire is the Nov pair (~12/1 Mfg, ~12/3 Svs). Card `docket/GRADING_CARD_20261203_ISM.md` is owed by ~11/26.
