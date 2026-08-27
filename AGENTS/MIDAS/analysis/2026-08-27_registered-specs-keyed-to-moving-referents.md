# MIDAS — BOTH REMAINING OPEN PREDICTIONS ARE KEYED TO REFERENTS THAT HAVE MOVED

**Written:** 2026-08-27 (Thu) · **Channels:** M1 (MIDAS-01) + I1 (MIDAS-02) · **Status:** ESCALATION, not a repair. **No band moved. No score moved. No spec edited. Zero capital.**
**Rides with:** the I1 tracked-baseline escalation (`analysis/2026-08-23_i1-tracked-baseline-measured-effect.md`, KB-059) — **same defect class, second and third instances.**
**Trigger:** `ledger_staleness.py --nudge MIDAS` flagged PREDICTIONS.tsv 11 STATUS-writes behind. I initially dismissed it because the one row I looked at (MIDAS-06) is Will-ruled NO-EDIT. **Will asked whether the file could be updated; checking properly is what found this.**

---

## 0. THE FINDING IN ONE LINE

**A registered spec that names a MOVING referent silently re-specifies itself.** The I1 bands do it through a tracked median. **Both remaining open predictions do it too** — MIDAS-01 through a rolled futures contract, MIDAS-02 through *both* mechanisms at once. **Neither is outcome-determinative today. Both resolve 2026-09-30 and both would be graded against a criterion that no longer means what it said.**

---

## 1. 🔴 THE STRUCTURAL POINT — THIS EXACT DEFECT WAS ALREADY FOUND AND RULED, AND THE SIBLINGS WERE NEVER SWEPT

On **2026-08-23** the GC=F roll was caught on **MIDAS-06**, filed as an observation, and Will ruled **NO EDIT / grade on the frozen letter, print both bases at grade time** (row 68). **That was correct and is not reopened here.**

⛔ **But MIDAS-06 was the row about to GRADE. MIDAS-01 and MIDAS-02 carry the identical defect and nobody looked, because they resolve five weeks out.** The registered, imminent, gated item absorbed the whole sweep; the un-gated siblings were invisible — `finding_registered_gate_captures_attention`. **The roll is a property of the TICKER, not of one row: every row citing `GC=F` or `HG=F` inherited it on the same day.**

---

## 2. MIDAS-01 (M1) — CROSS-ROLL RESOLUTION CRITERIA

**Criteria as written:** `gold (GC=F) close vs $4,113.70 [7/10 anchor] while DFII10 >2.0 by 9/30`
**Kill line:** gold `<$3,702.33` (10% below anchor) while DFII10 >2.0.

| Leg | Status today |
|---|---|
| Gold **$4,598.20** [GC=F 8/26 settle] vs anchor **$4,113.70** | **+11.78%** |
| Distance to the kill line | **−19.48%** — nowhere near |
| DFII10 **2.32** > 2.0 | **holds** |

⚠️ **The defect:** the **$4,113.70 anchor is a GCQ26-era price** (7/10); **`GC=F` now resolves to GCZ26** (confirmed: `GC=F -> GCZ26.CMX`). The criterion compares **two different contracts** — the arithmetic I banned fleet-wide in HEARTBEAT §8 this morning as *"cross-roll, never a like-for-like move."* The contango gap at the 8/21 roll was **$56.50 (~1.2%)**.

**Materiality: LOW today, and stated as low.** 1.2% against a **10%** falsification threshold, with the metal **19.5% clear** of the kill line. ⛔ **But the spec is mis-stated regardless of whether it currently binds**, and **there may be a further roll before 9/30** — a defect's current harmlessness is not a reason to leave it unlabelled (`finding_banner_is_a_warning_not_a_fix`).

---

## 3. MIDAS-02 (I1) — BOTH MECHANISMS AT ONCE, AND ONE OF THEM IS THE ESCALATION ALREADY IN FRONT OF WILL

**Criteria as written:** `copper (HG=F) spot QoQ vs $5.75 [4/9 anchor] + LME inventory LIVE w/ DEFINED baseline (round-3): 306,500t [7/10] = +28.0% vs the trailing-2yr rolling median (239,400t) … The '+100%' RED leg now grades vs the 2yr median (=479kt)`

| Leg | Status today |
|---|---|
| Copper **$6.5945** [HG=F 8/26] vs anchor **$5.75** | **+14.69%** — no 20% roll |
| LME **237,475t** [26 Aug] | vs the row's hardcoded median **239,400t** |
| **The row's median is stale** | today's trailing-2yr median is **238,575t** (−0.345%) |
| **The row's RED leg is hardcoded 479,000t** | on today's median it would be **477,150t** — a **1,650t** shift in a registered trigger |

🔴 **This row hardcodes a TRACKED quantity as if it were frozen — the precise defect of the 8/23 escalation (KB-059), now demonstrated inside a live prediction rather than a band.** The escalation measured the denominator drifting **+45.02% over 180 days** [as-of 8/26; +48.53% as-of 8/23 — see that document's as-of banner]. **A 1,650t discrepancy today is trivial; a denominator capable of moving 45% in six months, wired into a falsification threshold resolving in five weeks, is not.**

⚠️ **AND MIDAS-02 carries the cross-roll defect too** — `HG=F -> HGZ26.CMX`, so its `$5.75 [4/9]` copper anchor is likewise a different contract from what will grade it.

---

## 4. WHY I HAVE NOT FIXED ANY OF IT

**Every available fix moves the difficulty of a live, registered prediction — in one direction or the other — and tier test 4 bars that in either direction (L-20).** Re-anchoring MIDAS-01 to a GCZ26-equivalent price makes the kill line easier or harder by ~1.2% depending on which way it is done; re-basing MIDAS-02's median to today's value moves a registered RED trigger by 1,650t. **These are spec changes to open predictions, which is exactly the class that is Will-gated.** This is the same posture as the 8/23 I1 escalation, which PROME routed as a routing-only decision with **no recommendation owed from me, by design.**

**Options priced. NO recommendation offered.**

| # | Option | What it costs |
|---|---|---|
| **A** | **NO EDIT, observation filed** — the MIDAS-06 precedent (row 68) applied to its siblings: grade on the frozen letter, **print both contract bases and the as-of median at resolution.** | Consistent with a standing ruling; costs nothing now; the grader must remember to do it |
| **B** | **Annotate the criteria in place** — no threshold moves, but each row states its contract basis and that its median is an as-of value. | Documentation only; a reader still has to interpret at grade time |
| **C** | **Re-key the anchors like-for-like** — the MIDAS-06 row-51 precedent, where a boundary was corrected to preserve letter-INTENT after a vendor re-base. | Moves numbers on a live row; needs the same explicit riders row 51 carried |
| **D** | **Nothing until resolution** — accept discovery at the grade. | ⚠️ The failure mode I flagged this morning: the defect is found by the grade itself, when it is least absorbable |

**Not urgent — both resolve 2026-09-30.** ⚠️ **But the wrong time to decide is at the grade**, which is exactly how MIDAS-06's roll was nearly handled before it was caught with five days to spare.

---

## 5. WHAT I AM DOING ON MY OWN AUTHORITY (nothing that moves a spec)

- **Not editing any prediction row.** Not re-anchoring, not re-basing, not annotating criteria.
- **Not touching MIDAS-06** — Will-ruled NO EDIT; it grades tomorrow on the frozen letter.
- **Sweeping the rest of my registered surfaces for the same class** — this document is a flag, and the sweep is the generalisation (`L-32` rule 4: sweep prose and specs, not only code). **Result: MIDAS-03/04/05/07 are all resolved/closed, so the two rows above are the complete live exposure.**

## 6. THE GENERALISATION WORTH BANKING FLEET-WIDE

**A vendor "continuous" ticker is a MOVING REFERENCE, and every registered spec citing it inherited a silent re-specification on the roll date — simultaneously, across all rows, with no event.** Two failure modes compound: the spec is graded against a different instrument than it was written on, **and** nobody re-reads the un-gated rows because attention follows the gated one. **The check is mechanical: on any roll, grep every registered spec for the ticker, not just the row that is about to fire.**
