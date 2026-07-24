# HOM-01 Grading Sheet — FMHPI June-2026-data release (~Jul 30)

**Prepared 2026-07-24, ahead of the print** (PROME 7/12 ask: "have the as-published grading sheet ready before the print"). Prediction of record: `thesis/PREDICTIONS.tsv` HOM-01 (registered 2026-07-12, 60% PROVISIONAL).

## The prediction (verbatim mechanics)

Freddie Mac FMHPI **national, headline YoY %, as published in each release** (freddiemac.com/research/indices/house-price-index; CalculatedRisk mirrors same-day). FMHPI revises history monthly → **grade ONLY on the release's own as-published figures**, never on remembered prior prints.

- **Leg 1 (direction):** June-data or July-data release prints YoY **below the prior month's YoY as published in that same release** → accel-streak break.
- **Leg 2 (level):** any release covering Jun/Jul/Aug 2026 data prints YoY **≤ +1.0%**.
- **CONFIRMED** = both legs by the Aug-data release (~Sep 30). Otherwise MISSED (grade leg-by-leg).
- **Early-kill:** Jun-data AND Jul-data releases BOTH print > +1.9% (acceleration continues twice) → close MISSED early.

## Baseline going into the print (as-published in the May-data release, verified 7/12)

| Month | YoY (May-release vintage) |
|---|---|
| Jan 2026 | +0.9% (revised trough) |
| Apr 2026 | +1.4% |
| **May 2026** | **+1.9%** (3rd consecutive accel month) |

## Decision table for the ~Jul 30 release (June data)

Read the release's OWN table for May-YoY (call it M) and June-YoY (call it J). The release may revise May away from +1.9% — **M is whatever THIS release says May was.**

| Outcome | Grading action |
|---|---|
| **J < M** | **Leg-1 CONFIRMED** (streak break). Log in PREDICTIONS.tsv Notes with both as-published numbers + release date. Leg 2 stays open (needs ≤ +1.0% by Aug-data print). |
| J ≥ M but J ≤ +1.9% | Leg 1 NOT YET (no break, no accel past May's vintage level). Neither confirm nor kill-arm. Note and wait for Jul-data print (~Aug 31 = Leg-1 last chance). |
| **J > +1.9%** | **Early-kill ARM 1 of 2.** Log armed state. If the Jul-data release (~Aug 31) also prints > +1.9% → close **MISSED (early-kill)**, do not wait for Sep. |
| Release delayed/missing national headline | Do NOT substitute Case-Shiller or FHFA — different indices. Wait; note the delay. |

## Discipline notes

- **Year-verify** the release date and data month explicitly before grading (LESSONS.md rule — this exact class of error built a bad SV once).
- Case-Shiller (7/28, May data, 2 days earlier) is **context, not a resolver** — different index, deeper lag. It cannot confirm or kill HOM-01.
- New cross-currents logged 7/24 (KB-HOMER-003): DHI aging-spec hoard = timing headwind for the rollover; NAHB price-cut breadth (32→35→37% May→Jul) = mechanism support. Neither changes the pre-registered triggers — **resolve on the numbers, not the narrative** (CRL-03 lesson).
- On ANY resolution (either leg, either direction): push the read to HENRY (wealth-effect edge) + CARL (housing-consumer context) via NEXUS_BRIEF; if MISSED/FALSIFIED, log the Realtor.com list-price lead failure to LESSONS.md per the registration's if-falsified clause.
