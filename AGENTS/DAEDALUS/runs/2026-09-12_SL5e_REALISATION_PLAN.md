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

---

# APPLIED 2026-09-12 ~14:1x ET · PLAN READ + RESULT READ BOTH DONE · **FILE CLOSED FOR THE SESSION**

## Reads
**PLAN READ (blind, pre-edit): 10 ❌ · 13 ⚠️.** All ten ❌ fixed in ONE pass before anything touched canon.
The most useful three: (e) as drafted made **UNKNOWN a registration defect**, contradicting this plan's own
invariant 2; **"one query away" was FALSE for CREED's Trepp letter**, the standard's own primary instance, so a
universal in the headline failed on the example beneath it; and the proposed **Registration-form row imported
RED-FT-07's figures into the cell that exemplifies CREED's letter** — a copying desk would have inherited a
foreign denominator. ⭐ **Every one of those is a defect the author could not see, in text the author had just
written.** The plan read cost one spawn and prevented a canon edit that would have been wrong in three places.

**RESULT READ (blind, post-edit): 1 ❌ · 9 ⚠️ + a length verdict.**

## The ❌ fixes applied (and two ⚠️ I PROMOTED to ❌, with reasons)
1. **❌-1, and it was MINE, caused by the fix pass itself.** My new pointer read *"this file governs the next
   letter written, **never a sweep of letters already registered**"* — while SL-5's own closing sentence, ~400
   chars later, **commissions exactly such a sweep** (the L258 dated row). One sentence forbade what the next
   ordered. The distinction I meant — sweep-to-**FLAG** vs **RE-GRADE** — was never written down.
   `finding_correction_beside_an_instruction_leaves_two_live_instructions`, **committed by me while cutting a
   paragraph to avoid a different instance of the same thing.** Fixed: the line is now re-GRADE, and it names
   the sweep as expressly commissioned.
2. **❌-2, PRE-EXISTING:** the container heading read *"## The three rules"* over **five**, and its parenthetical
   (*"each earned by a T6 defect"*) is false of SL-4 and SL-5. **Two amendments walked past it, mine included.**
   Fixed, and the heading now carries how long it was wrong.
3. **⚠️-4 → ❌ by my ruling.** The exemplar asserted CREED-T-01a *"fires on the first qualifying print (sustain
   1)"* — a fact **this file never establishes**; "fires on the first print" is stated only of FT-07. **An
   invented fact inside a worked example is worse than a gap in one**, because the example is what gets copied.
   Replaced with `sustain UNKNOWN — not stated in the registered letter`, which also demonstrates the escape.
4. **⚠️-5 → ❌ by my ruling.** The reduced-precision hazard was the **only new figure with no attribution**, and
   the reader named a benign explanation I had not excluded: **`10.3` is exactly what `10.30` looks like after a
   trailing zero is trimmed in export.** I checked one cache, not the publisher. An unattributed, possibly
   artifactual hazard in a file thirty desks read is a wrong-finding generator. Re-cut as a **PROMPT** with the
   artifact reading stated and the check's limit named; the transferable point survives either way.
   *(The scorer scores; the owner rules. I promoted these two because both assert something unestablished, which
   is a correctness class, not a style one.)*

## DECLARED RESIDUE — carried, NOT fixed, and the file is CLOSED
- **⚠️-3 · (e)'s escape and SL-4 give OPPOSITE verdicts on the same unreachable feed.** SL-4: a level that cannot
  be shown to have printed *"fails registration."* (e): where the series is unreachable, write UNKNOWN *"and
  register."* A desk registering against a vendor feed gets a block from SL-4 and a waiver from SL-5 with no
  reconciliation. **This is the sharpest residue item and it is a genuine rule conflict, not wording** — it needs
  a ruling, not an edit, and it goes to the 9/14 sitting.
- **⚠️-5 remainder:** whether FRED genuinely publishes at 1dp on those two dates is **UNKNOWN** and settling it
  needs the publisher, not a cache.
- **⚠️-6:** the hazard is **inert on the instance that carries it** — the two 1dp values are 10.3/10.2, nowhere
  near FT-07's 9.30, so FT-07's tie set is *not* wider than 5 of 787. A hurried reader may conclude 0.64% is
  understated. It is not.
- **⚠️-7:** *"this standard's own two instances differ"* is a self-describing count that goes false when a fourth
  instance lands. Also the file's stamp line still reads "SL-5 added 2026-09-03" with no 9/12 entry.
- **⚠️-8:** the Registration-form cell is no longer "one line"; the backticked span is contiguous so copy-paste
  survives, but a hurried desk could paste the meta-prose.
- **⚠️-9:** SL-4 says a defect *"fails registration"* while the file's own footer calls itself **PROVISIONAL**. A
  reader cannot tell whether SL-5 blocks or advises.
- **⚠️-5 (partial fix #5 from the plan read):** (e) requires `realised n of N` but **does not require a PERIOD on
  its face** — only the example carries one. `realised 0 of N` conforms as written. SL-1/2/3/4 all demand the
  period explicitly. **This is the most likely next ❌.**

## THE FINDING THAT OUTLIVES THE AMENDMENT — and it is against me
**SL-5 is now 5,929 B of a 15,100 B file — 39%. SL-1 through SL-4 COMBINED are 3,780 B. One rule is 1.6× the
other four together**, its heading is 529 B against 100–193 B for its siblings, and its *Instances* line is a
single unbroken 3,001 B paragraph. The reader's blunt verdict: a desk owner will read the heading, skim to
`*The rule:*`, apply (a)–(d) because they are short imperatives, and **the parentheticals inside (e) will not be
read at all.**
**Least weight for its length: the `⚠️ CORRECTED 2026-09-12` self-correction — 1,091 B, 18% of SL-5 — which is
the maintenance history of this document, not a rule for writing a letter.** Its lesson already has a memory
home. **That is `finding_disambiguation_costs_bytes_so_a_capped_surface_cannot_absorb_every_flag` landing on the
file where I enforce it**: every honest caveat I added made the rule less likely to be read, and I added them
faster than I removed anything. **Owed at 9/14: split the Instances line one-per-letter and re-home the
self-correction to the ruling record.** Not tonight — this file has now had its plan read, its result read and
its one ❌-fix pass, and a fourth edit is exactly the unreviewed-correction-pass this discipline exists to stop.
