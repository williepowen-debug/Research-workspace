---
name: finding_count_what_published_before_reading_the_verdict
description: "When a scheduled multi-instrument exam is graded, count how many of its instruments actually published before reading the aggregate — a benign verdict off a half-dark instrument set is a coin landing on its edge recorded as heads, and non-publication clusters in exactly the windows the readings would matter"
metadata:
  type: finding
---

Fleets schedule **exams**: a dated cluster of instruments that together adjudicate a live question (an earnings cluster, a data week, a filing window). The verdict then gets read off *the prints that landed* — and nothing in the process records **how much of the exam actually sat.**

**NEXUS, 2026-08-03.** A recognition exam was scheduled to open 8/4 and settle a two-month divergence. In the four days before it, **five instruments went unavailable at once**:

| Instrument | How it went dark | Reads as |
|---|---|---|
| Fitch auto ABS ATR | not published, **4th consecutive month** | "no deterioration reported" |
| NY Fed Household Debt & Credit | advisory never posted; modal slid 8/4 → 8/11 | "not out yet" |
| ARCC Q2 (the cluster's *pre*-anchor) | owner agent dark 6 days | "nobody flagged it" |
| PortWatch Hormuz partition | stalled at 07-23 on clean `200`s while 25 other chokepoints published through 07-26 | "the data ends here" |
| FRED credit spreads | clean-200-empty + 403 to the consuming agent | "spreads unchanged" |

Not one of those is adverse data. **Every one of them makes a subsequent benign print cheaper, and none of them shows up as a caveat on the benign print.**

**The rule.** Before writing *"the exam printed benign,"* write the fraction: **how many scheduled instruments published, and which did not.** Then discount the verdict by coverage explicitly. Concretely — *"benign, 3 of 7 instruments reporting, and the two most discriminating were not among them"* is a different claim from *"benign,"* and only the first survives contact with the missing two.

**Two properties that make this worse than it sounds:**
1. **Non-publication is not random with respect to the question.** Instruments go quiet under load, under counsel, under revision, and under the operational stress that is often the thing being measured. The window where a reading would be most informative is disproportionately the window it does not arrive.
2. **"No adverse reading" and "no reading" are recorded identically** in every downstream surface — matrices, dockets, status lines. The distinction has to be written in deliberately, because no format carries it by default.

**Distinguish two failure classes; they compound and want different fixes:**
- **Declared blindness** — the owner *says* its primary cannot see its stress and pivots to a 2nd-order instrument. A domain property. Visible, honest, already priced.
- **Availability loss** — the instrument simply does not arrive, by non-publication or by access. An infrastructure property. **Invisible unless counted**, because a silent instrument is indistinguishable from a calm one.

**The tell you are about to make this mistake:** you are writing a verdict sentence whose subject is the *window* ("the week came back clean," "the cluster was benign") rather than a named instrument. Window-level subjects launder coverage gaps; instrument-level subjects cannot.

Related: [[finding_verification_zero_is_ambiguous]] (a *check* reporting clean is ambiguous the same way — this is the same ambiguity one level up, at the exam rather than the check) · [[finding_absence_tell_needs_a_talkative_instrument]] (an absence is only evidence if the instrument had room and habit to speak) · [[finding_coverage_gap_needs_all_surface_check]] (the near-opposite error: declaring a gap that isn't there) · [[finding_partitioned_source_returns_stale_window_at_200]] (the clean-200-stale-partition mechanic, live twice here) · [[finding_silent_blank_evades_review]].
