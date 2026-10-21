# LABOR C2 base rates — PRE-REGISTRATION (definitions written BEFORE any computation)

**Written 2026-10-21 08:57 ET** (stamp from `date`), PROME-spawned LABOR session, DOCKET L720 pickups 2 and 9. **This file is committed before any of the numbers below are computed** (L-15: base-rate a threshold before building it; the 10/14 openings base rate was withdrawn because its definitions were never written down and could not be reproduced). Results go to a separate RESULTS section, appended after this commit; this section is never edited after the commit.

## Common data rules

- Source: FRED, current vintage, pulled 2026-10-21 ~08:57 ET via `FORGE/tools/market-data/fetch.py` (`fred_fetch`, full history). ICSA, CCSA (weekly SA), JTSJOL, JTSHIL, JTSTSL (monthly SA, thousands), USREC (monthly NBER indicator).
- ⚠️ Current vintage, not as-published: seasonal factors are revised every spring, so this measures the shape of the revised series, not what a reader saw on the day.
- Pandemic exclusion: any week/month dated 2020-03-01 through 2021-12-31 is excluded both as a firing point and as an outcome window that touches it (a firing whose forward window overlaps the exclusion is dropped).
- Level bars do not transfer across decades (covered employment roughly doubled since 1967), so every historical letter is RELATIVE: the 4-week average divided by its own minimum over the prior 52 weeks (`rel = MA4_t / min(MA4_{t−52..t−1})`).
- Episode = the first firing week after at least 13 consecutive non-firing weeks (monthly series: first firing month after at least 3 non-firing months).

## Pickup 2 — return letters (what moves v13 back 1 → 2 and v7 back 2 → 3)

**v13 (initial claims) candidates**, on ICSA 4-week average (`MA4`, computed from ICSA):
- **R13-a:** `rel ≥ 1.10` in the week graded.
- **R13-b:** `rel ≥ 1.10` for 2 consecutive weeks.
- **R13-c:** `rel ≥ 1.15` in the week graded.

**v7 (continuing claims) candidates**, on CCSA 4-week average:
- **R7-a:** `rel ≥ 1.10`. **R7-b:** `rel ≥ 1.10` for 2 consecutive weeks. **R7-c:** `rel ≥ 1.15`.

**Outcome ("hit")** for an episode starting week t:
- **H-claims:** ICSA `rel` reaches ≥ 1.30 in weeks t+1 … t+26 (1.30 is the relative analogue of today's T-01 distance: `250,000 / 198,500 = 1.26`, rounded up).
- **H-rec:** USREC = 1 in any month within 12 months after t (recession already running at t ⇒ episode dropped as not a lead).
- Same two outcomes for v7 episodes (H-claims uses initial claims, so v7 is graded on whether a CC rise leads initial-claims deterioration).

**Base:** the same outcome computed from every eligible week (not just firing weeks) — the unconditional rate.

**Decision rule (fixed now):** a candidate is ADOPTED as the return letter only if ALL hold: (1) ≥ 6 episodes in the sample; (2) episode hit rate on H-claims ≥ 1.5 × the base rate; (3) the candidate fired in ≤ 15% of weeks from 2022-01-01 to the latest observation (a watch letter that fires constantly in the current calm regime is noise). Among passers, adopt the one with the highest H-claims precision; ties → the simpler (single-week) form. **If none passes, the answer is NO RETURN LETTER and the absent cell stays absent, stated as a decision (L-15 permits "don't build it").**
- Effect if adopted: return letter moves the vector ONE step (v13 1 → 2, v7 2 → 3); it enters the 10/22 card only as a dated AMENDMENT block, effective from the w/e Oct 17 print; it is recomputed every print as a formula (L-27), the level shown only as an illustration.

## Pickup 9 — should JOLTS openings carry a registered band? (REGINALD 9/29 (b))

- Series: JTSJOL, 2001-01 → latest (2026-08), ex 2020-03 … 2021-12.
- **Signal:** 3-month % change `JTSJOL_t / JTSJOL_{t−3} − 1 ≤ −5%`. Episode = first such month after ≥ 3 non-firing months. (Current state: Aug 2026 `7,079 / 7,537 − 1 = −6.08%`, first month at or below −5%.)
- **Outcomes**, within months t+1 … t+6:
  - **H-net:** JOLTS NET (`JTSHIL − JTSTSL`) ≤ 0 in two consecutive months.
  - **H-claims:** ICSA weekly `rel ≥ 1.30` in any week of those 6 months (same `rel` as above).
- Base: same outcome from every eligible month.
- **Decision rule (fixed now):** REGISTER an openings band only if (1) ≥ 6 episodes, (2) hit rate ≥ 1.5 × base on BOTH outcomes, (3) the result does not reverse sign between the −5% and −7.5% signal variants (robustness; −7.5% computed as a sensitivity only, never selected). If registered, it is a REPORT-ONLY line: it routes a packet to REGINALD and moves no vector score (v4 grades flows; openings do not measure flows — L-14). Otherwise: NO BAND, with this file as the reproducible basis.

---

## RESULTS — appended 2026-10-21 09:03 ET, after commit `f95654e55` froze the definitions above

**Reproduce:** `python3 -I AGENTS/LABOR/domain/sources/2026-10-21_c2_base_rates.py <dir>` where `<dir>` holds FRED JSON pulls (ICSA, CCSA, USREC, JTSJOL, JTSHIL, JTSTSL; full history, pulled 2026-10-21 08:57–09:00 ET; latest obs ICSA/IC4WSA 2026-10-10, CCSA 2026-10-03, JOLTS 2026-08-01, USREC 2026-09-01).
**Implementation choices the definitions did not spell out (disclosed, not tuned):** the 13-week quiet count runs straight through the excluded 2020–21 weeks (they were firing weeks, so no episode starts there); a continuing-claims week is matched to the initial-claims week with the same end date; JOLTS H-claims counts ICSA weeks ending from the 1st of month t+1 to the end of month t+6; H-rec drops episodes that start inside a recession.

### Pickup 2 — return letters

| Letter | Episodes | H-claims hit | Base | Lift | H-rec hit | Base | Fires in 2022→now | Rule (1)(2)(3) |
|---|---|---|---|---|---|---|---|---|
| R13-a `rel ≥ 1.10` | 35 | `4/35 = 11.4%` | `572/2,917 = 19.6%` | `0.114/0.196 = 0.58` | `4/33 = 12.1%` | `365/2,501 = 14.6%` | `65/250 = 26.0%` | ✓ ✗ ✗ |
| R13-b `≥ 1.10` ×2 | 33 | `4/33 = 12.1%` | 19.6% | `0.62` | `4/31 = 12.9%` | 14.6% | `57/250 = 22.8%` | ✓ ✗ ✗ |
| **R13-c `rel ≥ 1.15`** | **20** | **`7/20 = 35.0%`** | 19.6% | **`0.350/0.196 = 1.78`** | **`6/18 = 33.3%`** | 14.6% | **`28/250 = 11.2%`** | **✓ ✓ ✓ → ADOPTED** |
| R7-a CC `≥ 1.10` | 14 | `5/14 = 35.7%` | 19.6% | `1.82` | `6/13 = 46.2%` | 14.6% | `63/249 = 25.3%` | ✓ ✓ ✗ |
| R7-b CC `≥ 1.10` ×2 | 11 | `5/11 = 45.5%` | 19.6% | `2.32` | `5/9 = 55.6%` | 14.6% | `62/249 = 24.9%` | ✓ ✓ ✗ |
| R7-c CC `≥ 1.15` | 10 | `7/10 = 70.0%` | 19.6% | `3.57` | `5/7 = 71.4%` | 14.6% | `53/249 = 21.3%` | ✓ ✓ ✗ |

**DECISION v13: R13-c ADOPTED** — v13 1 → 2 when the published 4-week average is at least 1.15 × its own minimum over the prior 52 weeks. ⚠️ **Both of its episodes in the current regime (2023-03-25, 2024-06-22) were misses — 0 of 2 since 2022;** the 35% precision is a 1968–2019 property. ⚠️ **On today's inputs it is nearly nested inside band C:** the trailing minimum is 198,250 (IC4WSA w/e Oct 3), so the bar is `1.15 × 198,250 = 227,988`; on the 10/22 print that needs `X ≥ 4 × 227,988 − 596,000 = 315,952`, which is band E. It adds a path only for a slow grind (a run of prints just under 230,000 lifting the average past ~228,000).
**DECISION v7: NO RETURN LETTER.** Every CC candidate carries real lead (lift 1.82–3.57) but fires in 21–25% of weeks since 2022 — the 2022–23 climb of continuing claims off their post-pandemic low kept them firing for a year with no deterioration following. The pre-registered rule (3) says no; I do not re-cut the threshold after seeing the result. The absent cell stays absent as a DECISION (L-15). A fresh pre-registration with a different calm-regime test is possible at a later C2, not owed.

### Pickup 9 — JOLTS openings band (REGINALD 9/29 (b))

| Signal | Episodes | H-net hit | Base | Lift | H-claims hit | Base | Lift |
|---|---|---|---|---|---|---|---|
| **3-mo change ≤ −5%** | 17 | `4/17 = 23.5%` | `74/272 = 27.2%` | **`0.235/0.272 = 0.86`** | `2/17 = 11.8%` | `27/273 = 9.9%` | `1.19` |
| ≤ −7.5% (sensitivity only) | 12 | `4/12 = 33.3%` | 27.2% | `1.23` | `2/12 = 16.7%` | 9.9% | `1.69` |

Episodes (−5%): 2001-03 · 2003-02 · 2003-09 · 2004-06 · 2006-07 · 2008-02 · 2014-11 · 2016-06 · 2016-10 · 2019-02 · 2022-06 · 2023-02 · 2023-07 · 2023-11 · 2024-04 · 2025-08 · 2025-12 (+ 2019-12 and the current 2026-08, no complete outcome window).
**DECISION: NO BAND.** Rule (2) fails on both outcomes at −5% (lift 0.86 and 1.19, both under 1.5); rule (3) fails too — the H-net lift crosses 1.0 between the −5% and −7.5% variants. A 6% three-month fall in openings has, since 2001, been followed by two straight negative NET months a little LESS often than an average month. Openings stay a reported LEVEL with no band. This supersedes the withdrawn 10/14 base rate and the four undocumented 10/15 re-runs; this file + script is the reproducible basis.
