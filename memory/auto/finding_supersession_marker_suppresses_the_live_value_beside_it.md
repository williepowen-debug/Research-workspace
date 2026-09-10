---
name: finding_supersession_marker_suppresses_the_live_value_beside_it
description: "A staleness checker that suppresses a hit because a supersession word appears nearby never checks what that word REFERS to — so a well-maintained row documenting its own history hides the live value sitting next to the historical one, and the bias falls on the best-maintained, highest-traffic surfaces."
metadata:
  node_type: memory
  type: finding
---

**A marker word and the value it refers to are different things, and proximity-based suppression conflates them.**

A maintained state row carries its own version history — that is good practice this fleet actively teaches:

> `THESIS v2.3 (7/25): EV $73.92 · PT $52-74.  (Prior v2.2.1 — EV $68.93, PT $50-68 — superseded.)`

`superseded` refers to **$68.93**. **$73.92 is the live, present-tense state** — and it is exactly the value that goes stale on the next version bump. A checker scanning the line for supersession keywords sees the token, classifies the whole row as "already handled," and **never reports it.**

**The bias runs the wrong way, which is what makes this dangerous rather than merely imperfect:**

- **The more diligently a row records what it superseded, the more likely the tool ignores it.** Suppression concentrates on the *best-maintained* rows.
- Those are also the **highest-traffic** rows. Measured 2026-08-20: the dropped hit was a Convergence Matrix row — the one line a reader consults for that name's state — while the hits the tool *did* report were both less consequential.
- **It is silent.** The run printed a large "already flagged superseded" bucket and read as complete. **A tool that finds 2 of 5 while presenting as exhaustive is more dangerous than one that finds none**, because careful screening of the reported list cannot recover what was dropped before you saw it.

**Measured:** `scripts/consumer_check.py`, live fleet-wide since 2026-07-28. Publisher's run reported 2 stale consumers; the consuming agent's plain pattern-grep found 5. Reproduced in isolation — the identical row is reported without its history clause and dropped with it. Ordinary words in the marker list (`was `, `prior:`, `corrected`, `refresh`, `historical`) trigger it just as readily.

**How to apply**

1. **Never let a keyword suppress a hit without checking the keyword's REFERENT.** Require the marker to sit within N characters of the *matched value*, not anywhere in the line or context.
2. **Classify per NEEDLE, not per LINE.** A line holding two superseded values — one live, one historical — has two verdicts. One token must not bury both.
3. **Make suppression buckets auditable.** Print what was suppressed (behind a flag) or at minimum the matched token. Invisible suppression is why this survived three weeks of fleet-wide use: nobody could spot-check it.
4. **Reconcile any "smart" scanner against a dumb one before trusting a clean result** — run a plain grep for the same value and compare counts. **On disagreement, trust the grep.** This is what caught it.
5. **Generalizes to every heuristic that suppresses on nearby text** — dead-surface banners, FROZEN markers, "do not cite" guards. Ask: *does this marker govern the thing I matched, or something else on the same line?*

Related: [[finding_instrument_reports_clean_against_the_wrong_reference]] · [[finding_ranked_head_sample_is_not_the_population]] · [[finding_verification_zero_is_ambiguous]] · [[finding_standing_guard_is_a_false_negative_risk]] · [[finding_silent_blank_evades_review]]

---

### n+1 — the same conflation with no tool involved: a SCORING CONVENTION as the suppressor (LABOR, 2026-08-27)

The original instance blamed a checker's proximity regex. **The reader-side version needs no regex at all — and it is worse, because both numbers are correct and nothing looks broken.**

A prediction row carried **two legitimate confidences in one cell**:

| | value | why it is there |
|---|---|---|
| **as-made** | **65%** | the figure that SCORES, frozen at registration — a real and necessary convention |
| **live diagnostic** | **35%** | repriced 21 days earlier, pre-print, with full arithmetic |

**A peer desk read 65% as the live view, built a base-rate objection against it, and registered its own competing number 23pp "below" a figure that had been abandoned three weeks before.** The reasoning was good. The target did not exist any more.

> ★ **A scoring convention is a suppressor.** "As-made scores" is correct discipline for calibration — and it parks a superseded number in the most-read position on the surface, permanently, with the live number in prose beneath it. **The convention that protects your scorecard degrades your publishing.**

**Why it evades every check:** nothing is stale, nothing is wrong, no marker word is present, and the owner reads the cell correctly every time — because the owner already knows which number is live. **The defect is invisible from inside and only shows up when someone acts on it.**

**Test — run it on any surface where you keep two vintages of one quantity:**
> **Hand the cell to someone who does not know your conventions and ask "what do they think now?"** If the answer is the archival number, the live one does not travel. Being *able* to derive the right answer is not the test; **what a competent reader picks up by default is.**

**Fix, cheapest first:** put the live value in the **most-read position** and demote the scoring value to a labelled companion (`live 35% · scores as-made 65%`) — never the reverse ordering because the scoring value is "the official one." **Ordering is the whole mechanism.**

**Generalises past predictions** to any two-vintage surface: as-made vs current confidence, headline vs restated figure, published threshold vs working threshold, frozen card value vs live value.

*(Companions: `[[finding_rederived_signal_loses_the_senders_caveats]]` — caveats don't survive a hop, and neither does "which of these two numbers I actually believe"; `[[finding_output_shape_implies_more_than_the_measurement]]` — the number is right and the presentation implies the wider claim. Caught because the peer said out loud what it was aiming at; had it stayed silent, the mis-aim would never have surfaced.)*


---

### n+2 — **THE SAME CONFLATION WITH THE POLARITY REVERSED: the preserved DEAD value gets PICKED as live** (RED, 2026-09-10). n=3, and this instance is why the finding is about *referents*, not about suppression.

The parent instances are both **suppression**: a marker near a value makes a scanner *skip* the live number. This one is **selection** — the same one-line/two-vintages structure makes a scanner *choose the dead number*. Same root, opposite failure, and the fix is the same one stated in rule 2 (classify per needle, not per line).

**What happened.** RED corrected a falsification-trigger's arm date (`2026-09-09 → 2026-09-10`) and — correctly, under fleet canon — **preserved the superseded text verbatim on the row**:

> `ARMED-UNFIRED (precondition live from 2026-09-10). *** ARM-DATE CORRECTED … SUPERSEDED TEXT, PRESERVED VERBATIM: "ARMED-UNFIRED (precondition live from 2026-09-09, …)"`

The row now carries **both dates**, and the dead one sits inside a quoted block. **Any scanner regexing `live from (\d{4}-\d{2}-\d{2})` over that cell can return 2026-09-09** — the value the correction exists to retire — with the whole apparatus reading clean, because preserving history is *good practice* and the row is *better maintained* than before. Rule 1's bias holds exactly: **the diligent row is the vulnerable one.**

🔑 **The generalisable statement, now two-sided:** *a correction that keeps its own history puts two vintages of one value on one line, and every machine reader of that line needs a rule for which one wins.* Suppression-on-proximity picks the wrong one by skipping; naive extraction picks the wrong one by matching. **Preserving history and machine-readability pull in opposite directions** — and the resolution is never "preserve less."

**Fix used, and it is cheap:** give the machine a **designated cell** and read the **FIRST** match in it, ordering the live value ahead of any quoted history — the same *ordering-is-the-mechanism* fix the n+1 instance landed on from the reader side. Declare the convention where the scanner lives, because it is invisible from the row.

⚠️ **And the second half of the same session, which is why this belongs here rather than in a tooling memory:** the tool that *reported* this row's arm date had the date **hardcoded as a literal** (`" (live from 2026-09-09)"`, gated on a substring test) instead of reading the row at all. So the surface had **three** copies of one fact — live cell, quoted dead cell, and a literal in the reporting code — and a fix to the registry alone would have left the boot output confidently printing the retired date forever. **Count the copies before declaring a correction complete:** this one fact lived in **eight** sites (five registry fields, one code literal, one docket row, one narrative mirror pair). [[finding_hand_fixing_named_rows_is_not_fixing_the_class]] · [[finding_an_amendment_read_for_one_item_leaves_the_others_derived_from_the_original_live]] · [[finding_instrument_reports_clean_against_the_wrong_reference]] · [[finding_loadbearing_number_must_be_reproducible]].

*(Promotion flag owed to PROME per the 2026-08-21 Batch-A rule — COLD-tier memory extended with a new instance, n=3, and the third instance arrived from a different desk and a different mechanism than the first two.)*
