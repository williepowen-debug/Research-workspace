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

---

## ⚠️⚠️ DECISION TABLE FOR THE ~AUG 31 RELEASE (JULY DATA) — READ THIS, NOT THE TABLE ABOVE

**The table above was built for the June print and its rows are NOT mutually exclusive at the July print.** Ruled 2026-08-22, **before** the print. ⛔ **Definition only — no level moved.**

**Why the rows stopped being exclusive, which is the part worth carrying:** at registration May stood at **+1.9%**, so *"J below M"* and *"J above +1.9%"* **could not both hold** — the middle row (*"J ≥ M but J ≤ +1.9%"*) is the thin strip between them, and the table's whole shape assumes that geometry. **The June vintage revised M down to +1.58% SA and opened a ~16bp band where both rows fire at once.** ⇒ **The spec was not ambiguous when written; a revision beneath it made it ambiguous.** **Any spec pairing a frozen absolute level with a vintage-floating comparator has this property, and nothing announces the day they cross.**

Let **J** = July-2026 YoY **SA**, **M** = June-2026 YoY **SA as revised in that same release** (~+2.06% on the vintage current at drafting — ⚠️ **ACTUAL M = +1.81% SA** in the July release; see ✅ EXECUTED below).

| July print | Grading action |
|---|---|
| **J > +1.9%** | **CLOSE `MISSED (early-kill)`.** Both arms have fired. **This holds even if J < M** — see ruling (A). Do not wait for the Sep print. |
| **J ≤ +1.9% and J < M** | **Leg-1 CONFIRMED.** Kill quiet. Leg 2 rides to the Aug-data print (~Sep 30), which must print **≤ +1.0%** for CONFIRMED. |
| **J ≤ +1.9% and J ≥ M** | Leg 1 **MISSED** (last chance spent, no streak break). Kill quiet — it needs *both* arms. Leg 2 alone cannot CONFIRM; grade leg-by-leg at the Aug-data print. |
| Release delayed / no national headline | Do **NOT** substitute Case-Shiller or FHFA. Wait; note the delay. Unchanged. |

**The four rulings, in force (full text + rejected counter-argument: `thesis/PREDICTIONS.tsv` HOM-01 Notes):**
- **(A) The early-kill OUTRANKS a same-print Leg-1 confirm.** Inside the band both fire; the kill wins.
- **(B) `(both print > +1.9%)` is the OPERATIVE test.** *"ACCELERATES"* is a descriptive label, not a second condition — **a decelerating print above +1.9% still fires the kill.**
- **(C) +1.9% is FROZEN.** It is the May-2026 figure *in the May-data vintage*, since revised to **+1.58% SA**, so it sits ~32bp above the level it was built to represent. ⚠️ **Freezing is the LENIENT direction and it is frozen anyway** — the rule is *do not move the number*, not *move it against yourself*. Re-levelling is a **RETUNE**, Will-gated, not proposed.
- **(D) BASIS = SEASONALLY ADJUSTED (SA).** June was +2.06% SA / +2.02% NSA; at a +1.90% line a 4bp wedge decides the kill. SA matches the applied resolver-1 grade, the spec's named CalculatedRisk mirror, and HOM-02.

⚠️ **(A) and (B) both cut AGAINST this prediction and were chosen on that basis.** The readings that keep it alive were available and were rejected nine days before the resolver, which is when that choice is worth anything.

✅ **STANDING CHECK, adopted from this defect — run it BEFORE grading, every FMHPI print:** re-test whether the kill line and the prior-month comparator still bound **disjoint** regions. Re-reading the spec cannot catch this class; only re-evaluating the clause geometry against the current vintage can.
| Release delayed/missing national headline | Do NOT substitute Case-Shiller or FHFA — different indices. Wait; note the delay. |

## Discipline notes

- **Year-verify** the release date and data month explicitly before grading (LESSONS.md rule — this exact class of error built a bad SV once).
- Case-Shiller (7/28, May data, 2 days earlier) is **context, not a resolver** — different index, deeper lag. It cannot confirm or kill HOM-01.
- New cross-currents logged 7/24 (KB-HOMER-003): DHI aging-spec hoard = timing headwind for the rollover; NAHB price-cut breadth (32→35→37% May→Jul) = mechanism support. Neither changes the pre-registered triggers — **resolve on the numbers, not the narrative** (CRL-03 lesson).
- On ANY resolution (either leg, either direction): push the read to HENRY (wealth-effect edge) + CARL (housing-consumer context) via NEXUS_BRIEF; if MISSED/FALSIFIED, log the Realtor.com list-price lead failure to LESSONS.md per the registration's if-falsified clause.

---

## ✅ EXECUTED 2026-08-31 — SHEET CLOSED

The July-data release posted 2026-08-31 and was graded same-day off the issuer master file (PRIMARY): **J = +2.31% SA** (NSA +2.24%), **M = +1.81% SA as revised in that release**. The standing geometry check ran first: M < +1.90% ⇒ the kill line and the prior-month comparator bound **disjoint** regions on this vintage — the 8/22 overlap band closed itself; ruling (A) not invoked. **Row 1 of the July decision table applies: J > +1.9% ⇒ HOM-01 CLOSED `MISSED (early-kill)`.** (J ≥ M as well, so Leg-1 also failed independently — the outcome is over-determined.) Record of record: `thesis/PREDICTIONS.tsv` HOM-01, 2026-08-31 Notes entry. Discipline notes executed: year-verify (no article used; issuer file + same-day stamp), mirror unavailable (CalculatedRisk front page at Jan-2026 — a successor prediction needs a new named mirror), IF-MISSED clause → `LESSONS.md`, pushes to HENRY + CARL via `NEXUS_BRIEF`. **This sheet is now a historical instrument — do not grade against it again.**
