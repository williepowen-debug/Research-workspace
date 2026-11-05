# L334 predictive leg: does an unread INFO backlog predict corrections?

Owner WALTER. Due November 6, delivered November 5. Script `predictive.py`, data `panel.tsv`, `results.json`.

**Result: no relationship detected, and the study cannot support a stronger statement. No bar earned.** Backlog does not give a leading indicator on this evidence. This is not proof that unread INFO is costless.

| Backlog measure → outcome in next 14 days | Within-desk r | Permutation p |
|---|---:|---:|
| Backlog size → desk named on a correction | 0.118 | 0.463 |
| Backlog age → desk named on a correction | 0.125 | 0.086 |
| Backlog size → named on a WEAKEN or FLIP correction | 0.072 | 0.563 |
| Backlog age → named on a WEAKEN or FLIP correction | 0.072 | 0.310 |

Scope for the null arm: 180 desk-weeks across 30 desks with any backlog (35 desks before that filter, CARL, RED, PROME and TERRY excluded as pull-complete); six Mondays September 14 to October 19; 1,373 INFO rows; 95 correction rows in scope, ALL rows excluded; 10,000 within-desk permutations. Detectable effect at 80% power is about r = 0.23, a rough normal approximation, so effects smaller than that would be missed.

Limits that change how far this travels:
- Outcome is WALTER's own register. A correction names the recipients of the corrected card, so routing volume raises both backlog and outcome. A positive r would not show harm; it could be volume.
- The desk-as-corrector outcome had zero events: the register is WALTER-authored, so a desk's own stale figure is unmeasured here.
- Consumer_check stale flags were named in the row but have no logged history, so that outcome was not run.
- Backlog is concentrated: mean 2.2, maximum 96, HENRY averages 21.5 and HAWK 11.3. HENRY's 96 is the October 19 week.
- Removal from the inbox is read from git, so a desk that moves files without reading counts as consumed.

Recommendation: no bar. WQ-556 C's November 13 remeasurement stands unchanged. If PROME or Will wants a real test of harm, the missing instrument is a logged stale-figure event per desk; that is a new control and needs Will's word, so it is not proposed here.
