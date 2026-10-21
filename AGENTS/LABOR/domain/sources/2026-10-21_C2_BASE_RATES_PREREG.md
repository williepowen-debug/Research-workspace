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
