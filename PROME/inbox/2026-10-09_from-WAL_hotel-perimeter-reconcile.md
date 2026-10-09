# WAL → PROME: hotel perimeter reconcile (WQ-328 follow-up), 2026-10-09 ~11:0x ET

**Session:** WAL session #12, fresh bounded spawn from `prome-75` (Tier 1 inside WQ-328, Will's 10:24 ET word). Model: Opus (claude-opus-5-5), Claude Code, DESKTOP. **Sources:** EDGAR with a neutral contact UA (not Will's email): Q2 2026 10-Q (acc 0001628280-26-051418) and FY2025 10-K (acc 0001628280-26-010336). Quartr was not retried.

## Outcome: GAP, with the cause named in the filings' own words

| Question | Answer (filing words) | Grade |
|---|---|---|
| Why does property-type Hotel ($4,958M) ≠ HFF segment ($4,582M)? | Segments are "pooled into loan segments based on product types, **business lines**, and other risk characteristics". HFF = "loans **originated within this business line**…collateralized by real estate, where the owner is not the primary tenant". Other CRE-NOO = same, "**not originated within the Company's specialty business lines**" (10-K Note 1 p.93-95). Property type is a **collateral** split of loan-type CRE-NOO ("primary source of repayment is rental income generated from the collateral property", 10-K p.6/p.51, 10-Q p.77) | VERIFIED |
| Why do the segments sum $250M ABOVE the property-type total? | The two systems differ by category. The 10-K Item 1 table (p.7) and Note 4 both total **$58,677M** at 12/31/25, but segments minus loan-type: CRE-NOO **+300**, C&I family +141, Other/Consumer +142, CRE-OO −150, C&LD −12, Residential −421 | VERIFIED values; WAL's name-mapping |
| Which hotel loans sit outside HFF? | **At least $376M (≥7.6% of property-type hotel)** by arithmetic. Exactly $376M only if all HFF loans are hotel-type, which the filing does not state. Their segment home is **INFERRED Other CRE-NOO** ($279M nonaccrual, $59.7M H1 gross charge-offs, ACL 2.10%), which carries no hotel-separated credit line | Lower bound VERIFIED; home INFERRED |
| Missing disclosure | **A segment × property-type (or segment × loan-type) crosswalk.** Absent from both the Q2 10-Q and the FY2025 10-K (every "hotel" token read). The Q3 10-Q carries no Item 1 table; the next total-level bridge is the FY2026 10-K | SEARCH-NOT-FOUND at both documents |

- **Stability:** the hotel gap was $352M / $361M / $353M / **$376M** and the segment excess $289M / $300M / $321M / **$250M** (12/31/24 → 6/30/26). This is consistent with a standing classification difference, not a one-off item.
- **So:** the clean stats ($0 nonaccrual, $44M classified, $0 charge-offs, three quarters) cover the **HFF business line, ≤92.4% of the hotel collateral book**. At least $376M of hotel collateral has its credit reported mixed with non-hotel loans, most plausibly in the pool that carries the CRE losses. This is a perimeter caveat on a clean read, not stress evidence.
- **Q3 10-Q frame §8:** new dated non-gating line. O1–O3 now read as the HFF business line. **O6** gap vs $376M / excess vs $250M · **O7** Other CRE-NOO nonaccrual vs $279M, logged only and never attributed to hotels · **O8** any crosswalk or hotel credit figure.
- **No score, weight, EV, PT, gate or card moved.** The Dec-18 $65P ×4 and $70P ×1 are untouched (TERRY's cards).

## COMPLETION
STATUS: ✅ DONE
CHANGED: AGENTS/WAL/research/2026-10-09_hotel-exposure-read-WQ328.md (§6 addendum + §1 pointer), workbook/KB.tsv (KB-WAL-218, KB-216 pointer, data clock), workbook/KB_INDEX.md, Q3_10Q_GRADING_FRAME_2026-09-24.md §8 (O6–O8), STATUS.md, INDEX.md, MEMORY.md, NEXUS_BRIEF.md, board_log.tsv + SIG-W-20261009-007 → processed; this memo
RESULT: Outcome = GAP with the cause named: segments are pooled by originating business line (HFF = "originated within this business line") and property type by collateral. The 10-K ties the two systems only at the $58,677M total (CRE-NOO segments +$300M vs loan-type). ≥$376M (≥7.6%) of hotel collateral sits outside the clean HFF segment, with no hotel-separated credit line.
GAPS: No segment × property-type crosswalk exists in the Q2 10-Q or FY2025 10-K, so the $376M/$250M cannot be assigned to named loans. Earliest new evidence: a management statement at the 10/20 call (A2), or the FY2026 10-K. Q2 deck/call not read (Quartr un-authenticated, not retried per prompt). REGINALD 10/9 Nano packet left in WAL inbox (out of scope; MEMORY N-0).
WILL_NEEDS: None new. Riverside recorder search + FFIEC JWT 11/5 stay as carried in this morning's WQ-328 memo.
FOLLOW-UP: Next WAL session: process REGINALD Nano bid-summary packet; at the 10/20 call log any hotel-outside-HFF comment; at the Q3 10-Q log O6–O8.
