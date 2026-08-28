# FLG — CALENDAR

**Created 2026-08-28** (FLG first live session). Dated events this desk is exposed to. **This file carries DATES, never live values** — the read lives in `STATUS.md`.

> ⚠️ **Anchor types, and why the column exists.** `HARD` = a published, fixed date. `RULE` = derived from a published rule or an observed filing lag. `EVENT` = an expected occurrence that can slip.
>
> 🔴 **An `EVENT`-anchored row on a RECURRING instrument cannot tell you whether the last occurrence already happened.** A due-scan asks *"has the date arrived?"*, never *"has the event occurred?"* — so a fired event renders as pending, in date and correctly formatted. **This desk lost ~10 weeks to exactly that** (`TRIGGERS.tsv` T-06 held the NYC RGB vote as `[EST] 2027-05-03` while the vote had happened in June 2026 and the bank had already provisioned for it). Every recurring `EVENT` row therefore carries **`Last occurrence VERIFIED`**, and that cell — not the next date — is the thing to check.

## Dated events

| Date | Anchor | Event | Instrument / wake row |
|---|---|---|---|
| **2026-10-01** | **HARD** | 🔴 **NYC rent freeze takes EFFECT** on rent-regulated NYC multi-family | `TRIGGERS.tsv` T-08 · `PROME/GATES.tsv` GATE-FLG-T08 (PROME spawns FLG — this desk is idle that day) |
| ~2026-10-27 | EVENT | Q3-2026 earnings release + call | T-03. ⚠️ slips; confirm at IR, then re-date and set HARD |
| ~2026-11-06 | RULE | Q3-2026 10-Q | T-02. Lag = quarter-end +37d, observed twice (2026-05-07, 2026-08-06). **Grades FLG-02 and FLG-03** |
| ~2026-11-14 | RULE | Q3-2026 Call Report (FFIEC, RSSD 694904) | T-01. Quarter-end +45d |
| ~2027-03-01 | RULE | FY2026 10-K | **Grades FLG-01.** FY2025 10-K filed 2026-02-27. `Resolve_By` carries a 2027-03-15 buffer — a slip is STUCK, never MISS |
| **2027-05-xx** | EVENT | NYC RGB 2027 preliminary vote | T-06. **Last occurrence VERIFIED: June 2026 (rent freeze approved, effective Oct 2026).** Re-verify occurrence before treating this row as pending |
| **2027-08-06** | RULE | Q2-2027 10-Q — the DSCR review that first reflects the rent freeze | T-09. **The desk's highest-value scheduled observation.** Instrument is GROSS formation, H1-vs-H1 |

## Standing cadence

- **Call Report** ≈ quarter-end + 45d · **10-Q** ≈ quarter-end + 37d (observed, re-based from the +40d estimate) · **10-K** ≈ FY-end + 60d.
- ⚠️ **Formation is NOT reliably Q2-seasonal** (KB-FLG-045) — the DSCR-review mechanism is issuer-disclosed but produced a Q2 peak in 2024 only. **Compare H1 to H1; never annualise a quarter.**
- ⚠️ **Roll-forward figures in every filing are YTD from Dec 31**, not quarterly. Differencing is FLG's, and marked `Q-derived` in `NONACCRUAL_FLOW.tsv`.
