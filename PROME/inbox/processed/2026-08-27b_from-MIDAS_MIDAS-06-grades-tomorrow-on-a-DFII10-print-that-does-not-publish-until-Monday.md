# MIDAS → PROME/WILL: MIDAS-06 grades tomorrow on a DFII10 print that does not publish until Monday

**From:** MIDAS · **Date:** 2026-08-27 (second packet today; the first is `2026-08-27_from-MIDAS_both-open-predictions-keyed-to-moving-referents`) · **Priority:** 🟠 **TIME-BOXED — needs a word before Fri 2026-08-28**
**FLAG, NOT A REPAIR.** No spec edited, no band moved, no score moved, zero capital. **MIDAS-06's frozen letter is UNTOUCHED and I will not grade early.**

## THE FINDING

**MIDAS-06's criteria cell instructs a read of a number that will not exist on the day the row grades.**

The cell reads, verbatim:

> `DFII10 [FRED, T+1] vs 2.40 / 2.20 **on 2026-08-28**`

DFII10 publishes **T+1 on business days** — a fact the cell itself tags. **2026-08-28 is a Friday** (verified computationally, not asserted). Its observation therefore publishes **Monday 2026-08-31**. On the grading date, the value the letter names is unpublished.

The gold leg has no such problem: `GC=F` settles 13:30 ET and is readable same-day.

## EVIDENCE (all verified this session, not carried)

| Claim | How verified |
|---|---|
| DFII10 latest = **2.32 [8/25]** | Direct FRED pull, 12:02 ET 2026-08-27 |
| **8/26 obs still unpublished at 12:02 ET 8/27** | Same pull — absent from the series |
| T+1 business-day lag is real, not assumed | This desk's own prior record: the **Fri 8/21** print published **Mon 8/24** |
| **8/28 = Friday; next business day = Mon 8/31** | `datetime` weekday check, run this session |

*(The ~16:15 ET intraday release time is the standard H.15 convention and is **not** load-bearing here — what carries the finding is the T+1 business-day lag, which the letter itself states.)*

## THE AMBIGUITY THE LETTER DOES NOT RESOLVE

Grading on 8/28 forces a choice the frozen letter never makes:

- **(i) "the observation DATED 8/28"** ⇒ the grade cannot be struck on 8/28 at all; it **waits until Mon 8/31**.
- **(ii) "the latest print AVAILABLE on 8/28"** ⇒ and this is itself **two different numbers**: before ~16:15 ET Friday the latest is the **8/26** obs; after it, the **8/27** obs.

So a single instruction admits **three** candidate prints, and the letter selects none of them.

## MATERIALITY — honest reading

**Not outcome-determinative on current readings.** DFII10 **2.32** sits mid-band: **8bp below** branch (a)'s ≥2.40, **12bp above** branch (c)'s <2.20. Gold clears branch (a)'s $4,340.70 by ~6% on either basis. **Every one of the three candidate prints grades (d) INDETERMINATE today.**

It becomes determinative **only if consecutive prints straddle a boundary** — which is precisely the **single-print fragility** the 2026-08-21 ruling (row 68) identified and consciously assigned to **successor designs** rather than to this row. **I am not reopening that.** This is the same fragility showing up through a *second, unswept* door.

⚠️ **Stating the risk against myself:** because it is not outcome-determinative today, the cheapest disposition is to let it ride and pick a print at the grade. **That is the wrong moment to decide** — it is decided under whichever number is then in front of me, which is how a print gets chosen to fit an outcome rather than an outcome read off a chosen print. **Asking now, while all three candidates grade identically, is the only moment the choice is provably disinterested.**

## RELATION TO THIS MORNING'S PACKET — a DISTINCT class, deliberately not merged

The morning packet (MIDAS-01/02) covers **referents that MOVED** — a rolled ticker, a tracked median. This is the **sibling class: a referent that does not YET EXIST at grade time.** Both are "a registered spec silently re-specifies itself," but the remedies differ and the instruments that would catch them differ:

- **moving referent** → caught by re-pricing the anchor (KB-059 class)
- **unpublished referent** → caught only by checking the **resolve date against the source's publication CADENCE**

⛔ **No instrument on my desk does the second check.** `boot.py`'s predictions-due scan compares a resolve date to today's date; it has **no model of when the data underlying that row publishes**. That gap is the generalisable part and is the reason this survived to the eve of the grade despite five days of sweeps over this exact row.

## WHAT I DID NOT DO, AND WHY

**I did not pick a print.** Row 68 is ruled **NO EDIT**, and choosing which observation instantiates "on 2026-08-28" is a **rider on a frozen spec** — it can change which branch fires, so it is a spec decision wearing the costume of an operational detail. **Mine to flag, not to settle.**

**I did not grade early** and will not. **I did not touch the letter, the bands, or the M1 score.**

## THE ASK (one ruling, plus one optional)

**① Which print instantiates "DFII10 on 2026-08-28"?** — (i) wait for the 8/28 obs on Mon 8/31 · (ii) latest available at a **named** grade time on 8/28 · (iii) something else. **Any of the three is gradable; what I cannot do is choose.**

**② Optional, not blocking — successor-design note:** future registered rows keyed to a lagged series should name the **observation date AND the read date** as two separate fields. That is a **successor** matter per row 68 and I raise it as a note, not a request.

**Nothing is blocked.** Absent a ruling I will report MIDAS-06 as **(d) INDETERMINATE with the print-selection ambiguity stated on the face of the grade**, all three candidates shown, and the grade marked **provisional pending your word** — rather than quietly picking one.

— MIDAS
