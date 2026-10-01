# FLG — CALENDAR

**Created 2026-08-28** (FLG first live session). Dated events this desk is exposed to. **This file carries DATES, never live values** — the read lives in `STATUS.md`.

> ⚠️ **Anchor types, and why the column exists.** `HARD` = a published, fixed date. `RULE` = derived from a published rule or an observed filing lag. `EVENT` = an expected occurrence that can slip.
>
> 🔴 **An `EVENT`-anchored row on a RECURRING instrument cannot tell you whether the last occurrence already happened.** A due-scan asks *"has the date arrived?"*, never *"has the event occurred?"* — so a fired event renders as pending, in date and correctly formatted. **This desk lost ~10 weeks to exactly that** (`TRIGGERS.tsv` T-06 held the NYC RGB vote as `[EST] 2027-05-03` while the vote had happened in June 2026 and the bank had already provisioned for it). Every recurring `EVENT` row therefore carries **`Last occurrence VERIFIED`**, and that cell — not the next date — is the thing to check.

## Dated events

| Date | Anchor | Event | Instrument / wake row |
|---|---|---|---|
| **2026-10-01** | **HARD** *(date)* · ✅ **FIRED** | 🔴 **NYC rent freeze TOOK EFFECT** — `T-08` FIRED 10/1, graded by FLG: Order #58 (0% one- and two-year, leases commencing 10/1/26–9/30/27) in force at the RGB primary; no stay, appeal or emergency application reported (4 secondary dated 9/30–10/1); court docket unreachable, 403 (KB-FLG-071). Merits ruling still pending, "before the end of the year" | `TRIGGERS.tsv` T-08 (post-fire book read 10/23) · `PROME/GATES.tsv` GATE-FLG-T08 |
| ~~2026-09-30~~ → **2026-10-23** | EVENT *(next FLG wake = PROME DOCKET L522)* | ⚠️ **T-12 — rent-freeze litigation** (Kenilworth Holdings v. NYC RGB; Justice Lantry): 9/30 check consumed 10/1 at the T-08 grade, nothing found. Next dated items ~10/24 full production · merits by year-end (EVENT) · T-07 price backup rides the same wake | Between wakes: intake term only (DOCKET L467, best-effort). Court primaries 403 from this box |
| ~2026-10-23 | EVENT | Q3-2026 earnings release + call *(4th-Friday pattern; not announced as of 9/27)* | T-03, check 10/16. ⚠️ slips; confirm at IR, then re-date and set HARD. Read the 8-K exhibit list (KB-FLG-064) |
| ~2026-11-06 | RULE | Q3-2026 10-Q | T-02. Lag = quarter-end +37d, observed twice (2026-05-07, 2026-08-06). **Grades FLG-02 and FLG-03** |
| **CHECK-BY 2026-11-13** | RULE | Q3 FDM + payoff read, WQ-313 ① (PROME DOCKET L522) | T-13. Will's $29M/$286M question; if insufficient, record as reported, "unreconciled / not cohort-identifiable" |
| ~2026-11-14 | RULE | Q3-2026 Call Report (FFIEC, RSSD 694904) | T-01. Quarter-end +45d |
| ~2027-03-01 | RULE | FY2026 10-K | **Grades FLG-01.** FY2025 10-K filed 2026-02-27. `Resolve_By` carries a 2027-03-15 buffer — a slip is STUCK, never MISS |
| **2027-05-xx** | EVENT | NYC RGB 2027 preliminary vote | T-06. **Last occurrence VERIFIED: June 2026 (rent freeze approved, effective Oct 2026).** Re-verify occurrence before treating this row as pending |
| **2027 (full year)** | **RULE** | 🔴 **$8,503M of multi-family reprices/matures — 31.6% of the book**, into the freeze | T-10 · `workbook/MATURITY_WALL.tsv`. ⛔ **Grade on DOLLARS, not share** — share is arithmetically forced in a shrinking book (KB-FLG-049; corrected here 2026-09-24, this row had kept the pre-correction wording for 27 days) |
| ~2027-03-01 | RULE | FY2026 10-K — refreshes the maturity wall | T-10 re-dates here |
| 2027-08-06 | RULE | Q2-2027 10-Q — EARLY watch point; freeze content near-zero | T-09, demoted (KB-FLG-052). Grade formation for the ORDINARY trend, not for the freeze |
| **2028-08-04** | **RULE** | 🔴 **Q2-2028 10-Q — the DSCR review carrying most of a freeze year (FY2027)** | **T-11. The desk's highest-value scheduled observation.** Instrument is GROSS formation, H1-vs-H1 |

## 🔴 The 2027 convergence — the desk's whole timing in three rows

| when | what |
|---|---|
| **2026-10** | NYC rent freeze takes EFFECT — NOI growth on rent-regulated collateral goes to zero |
| **2027, across the year** | **$8,503M of multi-family reprices or matures — 31.6% of the book** — into that freeze |
| **2028-Q2** | The **DSCR review** carrying most of a freeze year (FY2027 financials) — ⚠️ corrected from Q2-2027, KB-FLG-052 |

⚠️ **The interim prints are quiet BY DESIGN, and the quiet runs LONGER than this desk first said.** RGB Order #58 governs leases **commencing 2026-10-01 → 2027-09-30**, so it phases in as leases renew: FY2026 financials (reviewed Q2-2027) hold at most Oct–Dec 2026 of partial exposure. **The bite is the Q2-2028 review of FY2027 financials** (T-11). Q3/Q4-2026 AND Q2-2027 carry commentary, not formation. ⚠️ And a 0% guideline **caps** revenue rather than cutting it — expect grinding cost-driven DSCR decay, not a cliff.

## Standing cadence

- **Call Report** ≈ quarter-end + 45d · **10-Q** ≈ quarter-end + 37d (observed, re-based from the +40d estimate) · **10-K** ≈ FY-end + 60d.
- ⚠️ **Formation is NOT reliably Q2-seasonal** (KB-FLG-045) — the DSCR-review mechanism is issuer-disclosed but produced a Q2 peak in 2024 only. **Compare H1 to H1; never annualise a quarter.**
- ⚠️ **Roll-forward figures in every filing are YTD from Dec 31**, not quarterly. Differencing is FLG's, and marked `Q-derived` in `NONACCRUAL_FLOW.tsv`.
