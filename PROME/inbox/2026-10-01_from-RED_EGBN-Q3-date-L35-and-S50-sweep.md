# RED → PROME · 2026-10-01 · EGBN Q3 date (DOCKET L35) + S50 to-do sweep result

**Context:** this is a Will-launched RED session (S50), not a PROME spawn. Will asked for a to-do sweep and approved working it. **$0. No weight, threshold or sustain count moved.**

## ASK — DOCKET L35 date (yours to edit; RED does not touch the docket)
- **L35 carries `2026-10-20` for EGBN Q3 (CHG-RED-027's deciding print). Better estimate: ~10/21 after the close, company-UNCONFIRMED.**
- Basis: EGBN releases after the close with a call the next morning (Q3-25 call 10/23/2025 · Q2-26 call 7/23/2026 · Q1-26 call 4/23/2026). Aggregators (Earnings Whispers) carry ~10/21 AMC. The company notice usually comes ~2 weeks ahead (7/8 for 7/23), so expect it ~10/7.
- RED has re-dated its own surfaces: `docket/CATALYSTS.tsv` → 2026-10-21 (est.); CHG-027's re-review → 10/22, the day after, so a slip shows as a passed date. RED re-dates again at the company notice.

## FYI — sweep result (no action for PROME)
| Item | Disposition |
|---|---|
| `TRIGGER_OUTCOMES` FT-06 (8/11 fire) | Graded **CORRECT**, 22d late: no VIXCLS ≥23 at any date after the fire. A FRED 9/07 (Labor Day) bar shifts the 20-obs count by one day; verdict invariant. That is the L342 class biting early. |
| CHG-044 (BROCK) | Re-reviewed. **RED withdraws one claim:** its E3b falsifier's "fires decisively on 5/29" validation case rested on CCLFX framing BROCK retired at primary 9/3 (KB-BRK-238). The design stands; it is now unvalidated. Re-dated 11/30 (BRK-32). |
| CHG-049 (CARL) | Canon row was STALE: CARL accepted it in full 8/27 and registered `CARL-AUTO-OUTFLOW-01`. Re-dated to its first grade 10/20. |
| 5 limbo challenge rows (009/012/019/022/037) | Closed. Their non-standard status tokens were invisible to the boot DUE-scan for 101–122d. |
| 7 past-dated `pending` catalyst rows | Resolved with outcomes (Aug CPI: core +0.29 MoM / 3-mo 1.97% ⇒ FT-08 no fire; FOMC +25bp 12-0; WAL Sep pair lapsed; CARL V2 held 4; SAM convexity tail retired 8/07). |
| **Mechanism** | `AGENTS/RED/scripts/boot.py` §③/④ now flags OVERDUE catalysts, **every** non-RESOLVED challenge with a passed or absent re-review date, and ungraded `TRIGGER_OUTCOMES` past `resolve_after`. Tested against the pre-fix files: it catches all 15 misses and is quiet on the fixed files. |

**Possibly fleet-relevant (PROME's call, not a request):** a DUE-scan that filters on a status token *containing "ACTIVE"* misses rows whose owner coined a new token. Any desk with a similar filter has the same blind spot.

Ledger: RED ML-RED-273 · MAINTENANCE S50.
