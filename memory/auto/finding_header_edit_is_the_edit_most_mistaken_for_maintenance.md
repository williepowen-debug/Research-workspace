---
name: finding_header_edit_is_the_edit_most_mistaken_for_maintenance
description: "Updating a doc's header/version/Last-Updated line is the single edit most likely to be mistaken for maintaining it — the header is what a reader checks for freshness, so a correct header over a stale body is worse than an obviously old file; n=3 in one sweep, each surviving 21+ days"
symptoms: "the header says it was fixed but the body still says the old thing; Last Updated is today and the number is from July; a file I maintain well is the one carrying the stale value; two sections of the same file contradict each other; a re-stamp is not a re-read"
metadata:
  type: feedback
---

**Editing a document's header is not editing the document — and it is the specific edit that makes an unmaintained body invisible.** A reader checks the version line, the `Last Updated:` stamp, or the top banner to decide whether to trust the file. When those are current and the body is not, **the freshness signal actively certifies the stale content.** An obviously old file gets re-derived; a file with a fresh header gets cited.

**Why:** the header is cheap to update and feels like closing the loop, so it gets touched at closeout when the body does not. Worse, the header is usually where a *correction* is announced — so the very act of documenting "X is now retired / re-specified / downgraded" in the header can leave the body still asserting X, with the header serving as evidence the author handled it.

**Measured n=3 in a single BOND staleness sweep (2026-08-18), each having survived 21+ days:**
- `THESIS.md` v1.1.3's version line declared the falsifier apparatus "RE-SPECIFIED from tail-keyed to composition-keyed." Only the header had been changed; three tail-keyed gates were still live in the body. *(Caught 7/28 by the author, who then wrote the correction into — the header.)*
- The same file's status line read *"dealer long-end inventory is at a record"* while **item 1 of the same document** recorded that record as retired and unwound −17.4%. Two paragraphs apart, opposite claims.
- `monitors/DEALER_CAPACITY.md`'s header announced **"✅ GAP CLOSED — the record has unwound"** while its `## Current Read` section three lines below still said *vector 3, fresh record highs, 4-trigger ARMED*.

**How to apply:**
- **When a header announces a change, the same commit must carry the body edit that change implies.** If you write "re-specified" / "retired" / "downgraded" into a header, grep the file for the thing you just retired **before** committing.
- **Read load-bearing docs end-to-end before declaring them clean.** Section-targeted edits leave the untouched sections asserting the old state, and n=3 above are all section-targeted edits.
- **Treat an internal contradiction as a first-class defect, not an untidiness** — two sections of one file disagreeing means at least one is wrong *and* nobody has read it whole.
- **Corollary for reviewers:** never take a `Last Updated` stamp as evidence a body is current. Audit by content vintage — cf. [[finding_mtime_is_corrupted_by_git_sync]] and [[finding_plausible_stale_value_evades_review]].

Distinct from [[finding_banner_is_a_warning_not_a_fix]] (a banner correctly *warns* and merely doesn't fix; a fresh header actively *reassures*) and from [[finding_a_ruling_governs_the_next_write_not_the_existing_state]] (that is a ruling vs. the stock of existing files; this is one file contradicting itself). Related: [[finding_dated_stamp_is_a_trigger_not_a_shield]].

---

**n=6 — three MORE instances, WAL desk, 2026-08-23, and they sharpen the rule in a way the first three did not.** The 8/20 WAL session wrote `STATUS.md` **seven times** in one day and re-stamped its header on each. Three days later a bounded touch found, on that same file:
- The **Price-discipline exit-rule state cell** reading **"🟢 $83.11, buffer +$5.11"** — a **JULY** price — sitting **~100 lines below a header that called the buffer "the tightest in the record."** The two are on the same screen in any reader wide enough, and the header is what everyone quoted.
- **`BOTTOM LINE`** carrying **"12.4% / spot $81.77"** — two thesis versions and several sessions stale — under a header announcing the *current* thesis version.
- **`STATUS.md:5` and the `THESIS.md` version-history footer** both still reading **"v2.3 is CURRENT"** three days after v2.4 shipped. ★ **A thesis has THREE homes for its version — the header, the "what moved" section, and the version-history footer — and a bump reliably touches the first two.** The footer is written once per version and re-read never.
- Same session, same class: **`INDEX.md`, the cold-spawn entry point**, published **`PT $52-74` under a `Thesis v2.4` header.** Of all surfaces to carry a stale value, the one a fresh session reads *first* and trusts *most*.

**★ The sharpening:** the original n=3 read as *authors announce a change in the header and forget the body*. These three are worse — **nobody announced anything.** The header was simply *refreshed*, repeatedly, by a diligent owner, and each refresh **re-certified** everything beneath it. ⇒ **The risk is not proportional to neglect; it is proportional to how OFTEN you re-stamp.** The file you maintain most attentively is the one whose stale cells are hardest to see, because its freshness signal is always true and always about something else.

**Added to "how to apply":** at closeout, **re-read the DERIVED CELLS — state columns, buffer/distance cells, footers, history lines — not just the sections you edited.** A cheap mechanization: list every cell in the file that restates a number owned elsewhere, and check those, not the prose. *(WAL's `scripts/derived_drift_check.py` does exactly this by scanning rather than by an enumerated list.)* And: **never quote a distance/buffer figure without re-deriving it from a named dated observation** — cf. [[finding_distance_to_a_threshold_is_a_claim_about_its_basis]].
