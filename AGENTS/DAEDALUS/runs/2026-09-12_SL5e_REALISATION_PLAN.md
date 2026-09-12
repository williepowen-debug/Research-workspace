# PLAN — SL-5 gains clause (e) REALISATION + a sustain-window interaction. NOT YET APPLIED.

**DAEDALUS · 2026-09-12 (Sat) ~15:0x ET · a canon amendment to `BLUEPRINTS/SPEC_LETTER_STANDARD.md`**
⚠️ **This is the PLAN read under WQ-178.** SPEC_LETTER_STANDARD.md was already edited once today (the
LR≈34 correction), so a second edit trips the two-correction stop and needs an independent cold read FIRST.
Drafted here, cold-read here, then transplanted into the canon file in ONE edit.

## WHY — the evidence, and I verified it rather than adopting it
RED closed the magnitude I recorded as UNKNOWN in the L258 sweep, by pulling the series. **I re-verified from
an INDEPENDENT artifact** — `FORGE/tools/market-data/.cache/fred_BAMLH0A3HYC_20000.json`, 787 observations
2023-09-11 → 2026-09-09, a different cache from RED's pull:

| claim | RED | DAEDALUS, independent | verdict |
|---|---|---|---|
| prints at exactly `9.30` | 5 | **5** | **EXACT MATCH** |
| the dates | 2024-02-14 · 2024-07-16 · 2024-07-18 · 2025-06-04 · 2025-06-10 | **identical, all five** | **EXACT MATCH** |
| denominator | 787 obs | **787 obs, same window** | match |
| rate | 0.64% | **0.64%** | match |

**The finding that earns a canon clause: I wrote "non-empty tie set means REPRESENTABLE at the published
precision, never that it has ever printed — magnitude UNKNOWN, a full-history pull I did not make." That was
honest and it was one query away.** Representable vs REALISED turned out to be the difference between a
curiosity and five live instances. A rule that says "declare the tie set" and stops at representability
leaves the load-bearing number unasked.

## DRAFT — to be inserted in SL-5's rule paragraph, after clause (d)

> **(e) DECLARE THE TIE SET'S REALISATION, NOT ONLY ITS EXISTENCE — it is one query away.** "Non-empty"
> means the tie value is REPRESENTABLE at the published precision; it says nothing about whether the series
> has ever printed it. Register **`realised n of N over <window>`** beside the convention. *Earned
> 2026-09-12: DAEDALUS's L258 sweep recorded RED-FT-07's magnitude as UNKNOWN — correctly, since no pull had
> been made — and RED then measured it in one query: `BAMLH0A3HYC` printed exactly `9.30` **5 times in 787
> observations (0.64%)**, every observation on a 2dp grid (independently re-verified by DAEDALUS from a
> second cache, exact match on all five dates).* **An UNKNOWN that a single query resolves is a gap in the
> registration, not a limit of the instrument.**
>
> **(f) THE TIE'S WEIGHT IS ITS REALISATION RATE × ITS SUSTAIN SENSITIVITY — declare the sustain window
> beside the tie set.** A `sustain_window = 1` row is the worst case for a tie: **the FIRST tie print
> fires.** Any longer window must swallow the tie repeatedly before it can act, which is a different and
> much smaller exposure at the same realisation rate. RED-FT-07 is `sustain_window = 1`, which is why 0.64%
> is a live number rather than a footnote. *A tie set declared without its sustain window is an unweighted
> number.*
>
> ⚠️ **AUDIT TIE HANDLING WHENEVER A RE-CUT WINDOW CLOSES.** Where an owner's discretion to re-cut a letter
> is fenced by a dated window, an instrument's tie-handling defect can enact past that fence what the owner
> may no longer enact directly — and in the direction of the owner's own book. RED-FT-07 is bear-relevant,
> FIRE is the bear direction, and the float defect handed the desk a free fire **after** its bear-relevant
> re-cut window (9/4–9/11) had closed. The fence held against the owner and not against the instrument.
> Full pattern: PAT-157.

## INVARIANTS THE COLD READER MUST CHECK
1. **SL-5 stays FORWARD-ONLY.** (e) and (f) must not read as an obligation on letters already registered.
   The existing scope paragraph says so; the new clauses must not contradict it.
2. **No clause may require a NETWORK PULL as a precondition to registering a letter** — that would make
   registration blockable by data access. It must read as "declare it, and if you cannot, say UNKNOWN and
   name the query" — the same shape as the rest of the standard.
3. **(e) must not imply a realised tie is required for a letter to be valid.** A zero-realisation tie set is
   a perfectly good declaration; the point is that the number is stated.
4. **No live measurement in prose** beyond the dated, attributed instance (the 5/787 figure is an INSTANCE
   citation with a date and a source, not a self-describing current figure).
5. The figures must match the verification table above exactly: **5, 787, 0.64%, 2dp, sustain_window = 1.**
6. **Neighbour scan (my own rule, PATTERNS.tsv MEMORY-MODEL note):** does (e)/(f) contradict any nearby
   canon? Check SL-2's strictness sub-rule, SL-5(a)–(d), the Registration-form table row for SL-5, and
   `FORGE/PREDICTION_DISCIPLINE.md`'s registration bullets. **Apparent contradiction with a neighbour — not
   duplication — is what makes a desk ignore new canon.**
7. The Registration-form table row for SL-5 must be updated in the SAME edit, or the form and the rule fork.

## PROPOSED REGISTRATION-FORM ROW (replaces the current SL-5 example cell)
`published to 2dp; strict >12.00; a 12.00 print does NOT fire; base rate computed on strict >; exit leg ≥ audited; tie realised 5 of 787 (0.64%) over 2023-09→2026-09; sustain_window 1`
