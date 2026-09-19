---
name: finding_term_hit_absence_check_needs_a_pre_event_baseline
description: A keyword absence-check on any large filer returns hits BY CONSTRUCTION (standing boilerplate) — the positive is the trap, and only a pre-event baseline from the same source separates signal from standing language.
symptoms: "grep found 'breach' so they disclosed it"; "the filing mentions cyber"; term-count hit on a routine disclosure; a silence or absence grade that flips on a keyword; risk-factor language read as an incident; "we searched and found nothing" on a header field
metadata:
  type: reference
---

**A term-based absence check on a large, regularly-filing entity is non-zero every time.** Standard risk-factor and forward-looking-statement language names the hazard in every routine document, so a hit count answers nothing on its own. **The FALSE POSITIVE is the failure mode, not the false negative** — and because it reads as a refutation, it overturns a correct absence claim.

**The discriminator is a PRE-EVENT BASELINE from the same source.** Pull a comparable document filed *before* the event and compare exact language and term counts. Identical text with identical counts ⇒ standing boilerplate, and the absence survives. Only a *delta* against that baseline is a disclosure.

Worked example (CRUISE, 2026-09-19; CCL breach identified 2026-04-14). Claim: *"no 8-K disclosed the breach, tagged or untagged."* The 2026-06-23 earnings exhibit returns **cyber ×1, breach ×1, privacy ×2, incident ×2** — a naive grep reads that as a disclosure. Control: the **identical bullet with identical counts** sits in the **2026-03-27** release, **18 days pre-incident**. Boilerplate established; absence held.

Three compounding traps in the same check, one afternoon:
- **Header vs document.** EDGAR's `items` field is filing-header-derived, so *"no 8-K carries Item 1.05"* ≠ *"no 8-K disclosed it."* An incident can sit untagged under 7.01/8.01 — **or inside an earnings exhibit carrying none of those tags.** Read documents, not the index. Two material facts on the desk's primary name (a redomiciliation; a $500M secured redemption) sat unread in filings already "checked" that way.
- **Perimeter must include amendments.** For an absence claim use forms *starting* `8-K` (incl. `8-K/A`), not the exact form — an amendment can carry a late-tagged item, and excluding them is how a corrected filing goes missing.
- **A 0-byte fetch is not an absence.** A malformed URL returned `NOT FOUND` *inside the control built to fix this very class*. Assert response length before reading any negative.

⚠️ **Path gotcha, and I got it wrong twice while writing this file — which is the point.** The harness memory path `~/.claude/projects/-home-willi-Research-workspace/memory` is a **symlink to `Research-workspace/memory/auto/`**. So `$MEMORY/auto/…` double-nests to `memory/auto/auto/` and the write fails, leaving an index row pointing at nothing. I then concluded *"files live flat in `memory/`, `auto/` doesn't exist"* — **also false**: `memory/auto/` is real, I was simply already inside it. **Both errors were absence claims read off a failed path rather than a resolved one.** `readlink -f` first; a failed `ls` is not a missing directory.

Related: [[finding_scan_keyed_on_naming_reads_local_form_as_absence]] (that one is the NEGATIVE — your pattern set; this is the POSITIVE — their standing language) · [[finding_a_named_unchecked_fallback_makes_an_absence_closable]] · [[finding_crosscheck_with_free_parameter_validates_nothing]] · [[finding_instrument_reports_clean_against_the_wrong_reference]]
