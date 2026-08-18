---
name: finding_header_edit_is_the_edit_most_mistaken_for_maintenance
description: "Updating a doc's header/version/Last-Updated line is the single edit most likely to be mistaken for maintaining it — the header is what a reader checks for freshness, so a correct header over a stale body is worse than an obviously old file; n=3 in one sweep, each surviving 21+ days"
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
