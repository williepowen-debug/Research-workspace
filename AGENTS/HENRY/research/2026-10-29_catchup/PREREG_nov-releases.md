# HENRY pre-registration — October NFP (11/6), October CPI (11/10), October PPI (11/13)

**FROZEN at commit time, 2026-10-29 ~16:5x ET (clock 16:58 at stamp) (Claude Code, Opus 5.5).** Will-directed in session ("lets do … 2": write the expectation down BEFORE the release, the gap Experiment A found at the 10/28 FOMC). Rows HEN-57, HEN-58, HEN-59 in `workbook/PREDICTIONS.tsv` point here. Nothing below changes a standing threshold, a band or a trade. Confidence: **UNASSIGNED** (no calibrated probability; no Brier score). These record what I expect, so the miss can be measured.

**Rules common to all three:**
- **The grade uses the agency's FIRST PRINT, at the published one-decimal (or thousands) figure.** Unrounded figures are recorded beside the grade; they are not graded.
- **NO-VERDICT** if: the release is postponed beyond its stated date plus 5 business days; the series definition changes; or the first print cannot be read at the agency or an agency mirror.
- **Late evaluation is NOT NO-VERDICT.** A grade written after the release day still grades the first print, and the delay is disclosed.
- **Wake:** DOCKET rows proposed to PROME by packet (HENRY does not write DOCKET).

## HEN-57 — October CPI, core m/m (BLS, Tue 11/10 08:30 ET)
| Field | Content |
|---|---|
| Line | `ECON_CALENDAR` § Key Thresholds: Core CPI m/m >0.3% = hot |
| Grading rule | BLS seasonally adjusted "all items less food and energy" m/m, one decimal: **0.4 or higher = FIRED; 0.3 or lower = NOT FIRED** |
| Expectation | **NOT FIRED, at +0.2%** |
| Source of expectation | Cleveland Fed inflation nowcast, October 2026 row, updated 10/29: core CPI **+0.21% m/m**; CPI +0.24% m/m; core CPI y/y 2.48%, CPI y/y 3.74% (page saved `clevelandfed_nowcast_1029.html`) |
| Distance to the edge | The edge for a one-decimal 0.4 is 0.35; the nowcast sits **0.14pp** under it |
| Known bias | On 10/29 the same nowcaster undershot September core PCE by ~0.04pp, in the hot direction (DOCKET L774) |

## HEN-58 — October PPI final demand m/m (BLS, Fri 11/13 08:30 ET)
| Field | Content |
|---|---|
| Line | STATUS § ACTIVE THRESHOLDS: PPI FD m/m >0.4 / >0.5 / >0.6 |
| Grading rule | BLS final demand SA m/m, one decimal. **≤0.4 = NONE · 0.5 = YELLOW · 0.6 = ORANGE · ≥0.7 = RED.** A negative print is NONE. Every one-decimal value maps to exactly one state |
| Expectation | **NONE (≤0.4)** |
| Source of expectation | No nowcast exists for PPI. The expectation rests on one leg: front-month futures, averaged by month, Oct vs Sep. Heating oil −1.67%, RBOB gasoline −4.06%, WTI +0.99%, Brent +5.36%, Henry Hub +1.63% (vendor, pulled 16:5x ET 10/29; Oct = 10/1–10/29). Product prices fell, and September's +1.3% was an energy-goods impulse (KB ML-HEN-179). |
| ⚠️ Weakness, stated before the print | Continuous futures series roll inside each month, so these averages are approximate. **The services leg (+0.8 in September) has no instrument here, and alone could carry a YELLOW or worse.** This is the weakest of the three. |

## HEN-59 — October payrolls headline (BLS Employment Situation, Fri 11/6 08:30 ET)
| Field | Content |
|---|---|
| Line | `ECON_CALENDAR` § Key Thresholds: NFP <100K = labor cracking. LABOR owns the payroll read and its triggers; this row grades only HENRY's line and the market reaction HENRY logs |
| Grading rule | BLS total nonfarm, SA, first-print monthly change: **<+100,000 = FIRED; ≥+100,000 = NOT FIRED** (exactly 100,000 = NOT FIRED) |
| Expectation | **FIRED (under +100K)** |
| Source of expectation | LABOR STATUS (10/29 read): Sep +29K first print; revised run May–Sep 63 / 31 / −10 / 133 / 29 (thousands); 3-month average 50.7K. **4 of the last 5 months printed under 100K.** Base rate only; no consensus panel recovered |
| Reaction note (recorded, not graded) | Per HENRY's 6/6 finding, KRE direction separates a rate story (KRE up) from a credit story (KRE down). Logged on the day |

## Registration discipline checks (LESSONS § Registration)
- **(i) Is any limb already satisfied as written?** No. All three grade future first prints.
- **(ii) Are examples read as exhaustive?** No examples are used. Each rule is a closed numeric partition.
- **(iii) Is there an unnamed region between bands?** None. HEN-57 and HEN-59 are binary at a stated edge; HEN-58 maps every one-decimal value, including negatives.
- **Time basis:** each claim and each grade is the same monthly first print. The only instrument with a time-basis mismatch is HEN-58's futures averages, and that weakness is disclosed above.
