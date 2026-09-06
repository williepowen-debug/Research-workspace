# ⛔ FROZEN 2026-09-06 — resolved VULCAN-NN predictions, moved not deleted

**`PREDICTIONS_RESOLVED_2026-09.tsv` — 8 rows, 19,896 B, crc `0xc3603220`. Rows are VERBATIM: byte-identical to their pre-split form, conservation proven (16 in == 8 archived + 8 live, no mutation).**

⚠️ **These are RESOLVED forecasts. Do not cite a row here as a live prediction.**

🔑 **Why the banner is in this file and not in the TSV:** the archive is a **pure TSV with the same 11-column header as the live ledger**, so it parses independently and the calibration record stays machine-readable. An inline banner would have made it unparseable — and a resolved row is in any case **self-marking**, because its own `status` column says HIT / MISS / HIT-NOFIRE / MISS-DOWNGRADE.

## Why this split happened
`workbook/PREDICTIONS.tsv` hit **57,244 B = 106% of the 54,250 B physical read cap** on 2026-09-06 — **pushed over by that session's own corrections**, from 91% on 9/3. The 9/3 deferral rested on *"it is a headroom warning, not a breach"*; that reasoning expired the moment it crossed the cap. **After the split: 37,332 B = 69% of cap, 0 over the cap** *(still above the 60% budget — stated precisely, not rounded to compliance)*.

## What is here

| ID | Verdict | Resolved |
|---|---|---|
| VULCAN-01 | HIT | 2026-07-31 — hyperscaler FY26 capex guides HELD/RAISED |
| VULCAN-03 | HIT | 2026-07-22 — GOOGL first gate of the cluster |
| VULCAN-04 | HIT | 2026-07-29 — SK Hynix Q2'26 *(⚠️ 7/29, NOT 7/23 — the date error that survived in `CLAUDE.md` for 18 days, n=4 on L-10/L-13)* |
| VULCAN-05 | HIT | 2026-07-13 — TSMC June revenue |
| VULCAN-06 | HIT | 2026-07-31 — the S3 55GW-vs-32GW discriminator |
| VULCAN-07 | HIT-NOFIRE | 2026-07-31 — obsolescence gate 🔴 **SEE THE LIVE-GATE NOTE BELOW** |
| VULCAN-09 | MISS-DOWNGRADE | 2026-07-31 — returns-case reaction test |
| VULCAN-16 | MISS | 2026-08-27 — de-risking-vs-information discriminator, graded on its escape clause |

**Calibration on this set: HIT 5 · HIT-NOFIRE 1 · MISS-DOWNGRADE 1 · MISS 1 (n=8).** Kept here so the hit rate stays computable after the move; also mirrored on `STATUS.md`.

## 🔴 THE ONE ROW THAT NEEDED A DECISION — VULCAN-07

**A resolved row can still carry a LIVE standing rule**, and this one does: *"≥2 of 4 hyperscalers change server/network useful-life → **promote obsolescence to a full channel (S6)**, route VIOLET + HENRY."* Current state **0 of 4**.

**It was archived anyway, and here is the check that made that safe rather than convenient:** the gate is stated **self-containedly on `STATUS.md`'s exit triad** — rule, current state and FIRED verdict, all three — and `STATUS.md` is the boot-read canonical surface. **The live rule therefore did not move; only the resolved forecast did.**

⚠️ **Had STATUS merely *referenced* VULCAN-07 instead of *stating* the rule, this row would have stayed live.** That is the difference between archiving **by row** and archiving **by status**, which is the trap registered in advance on 2026-09-03 — *"a resolved row can still be carrying a live standing rule; archive by ROW, never by STATUS"* — and it is the reason all 8 rows were read individually for forward commitments before any move. **VULCAN-07 was the only one that had any.**

**Also depends on this row:** `VULCAN-08` (OPEN, resolves 2027-02-15) is the January re-test registered off VULCAN-07. It stays live in `workbook/PREDICTIONS.tsv`; its antecedent is here.
