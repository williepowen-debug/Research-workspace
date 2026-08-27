---
name: finding_parse_failure_folded_into_a_benign_bucket
description: A parse/fetch failure counted into a named benign category doesn't render as a missing reading — it manufactures a positive factual claim about documents nobody read.
metadata:
  type: feedback
---

An insider-buying detector printed, for 11 of 11 Form 4 filings: **"All routine (RSU settlements, tax withholdings, awards). No conviction signals."** It had parsed **zero** of them. The XML-link picker was returning EDGAR's *XSL-rendered HTML* view (`/xslF345X06/...`) instead of the raw XML, `ET.fromstring` raised on the doctype, the parser returned `None` — and the caller incremented `total_noise`, the **"Routine"** counter.

**This is a strictly worse failure than a silent zero.** A missing reading looks like nothing and invites a second look. A failure folded into a *substantive benign bucket* looks like **evidence**: it names a mechanism ("RSU settlements"), reports a count, and reads as a completed check. Nobody re-examines a detector that is confidently telling them everything is fine — least of all when its null state is load-bearing evidence FOR the position they already hold.

**How to apply:**
- **Never increment a substantive category from a failure path.** Failures get their own counter (`unparsed`, `fetch_failed`), and it prints in the default output line beside the real ones — `found | parsed | unparsed`, never folded.
- **The tell is a bucket that can only grow.** If every error path lands in the same "benign/other/routine" bin, that bin's count is not a measurement.
- **Verdicts must state coverage, not just outcome:** "no purchases across **3 of 3 names**, 25/25 fetched" — not "no purchases across any thesis name." A verdict certifies its scope, not your capability ([[finding_verification_zero_is_ambiguous]]).
- **Separating the counters is what surfaces the bug.** The broken parser was invisible for an unknown period; it became obvious the instant `Unparsed` printed as its own number. Splitting the counter *is* the diagnostic, not just the fix.
- **Then falsify it** — force the outage and confirm the clean verdict cannot print ([[finding_run_the_falsifier_before_promoting]]). A guard nobody has watched fail is an assumption.
- Related: [[finding_fail_loud_on_incomplete_data]] · [[finding_silent_blank_evades_review]] · [[finding_count_what_published_before_reading_the_verdict]] · [[finding_standing_guard_is_a_false_negative_risk]] · [[finding_registry_names_a_concept_tool_resolves_an_instrument]].

---

**Extension 2026-08-21 (VULCAN, S4 instrument build) — the sharper form: the parse failure can be CORRELATED WITH THE SIGNAL CLASS, making the instrument untrippable by construction.**

The base finding's failures were random with respect to content. VULCAN's were not: TSMC's 6-K writes negative months in **accounting parentheses — `(1.1)`, not `-1.1`** — so its revenue parser dropped 8 of 16 months, **every dropped month a DECLINE**, while writing 8 clean-looking "validated" rows under a success line. **S4's red band IS "decline" — the instrument could not, by construction, ever see the condition it existed to flag.** Not a degraded detector; a detector whose failure mode selects exactly the alert class, wearing a validation stamp.

**Added to how-to-apply:**
- **Ask whether your failure mode is INDEPENDENT of the signal.** A random 50% parse loss degrades an instrument; a loss correlated with the alert condition (negatives formatted differently, halted days missing from a feed, outage-days unlogged) **blinds it specifically to fires while it validates cleanly on quiet data**. Test with a known-positive from the alert class, not a random sample.
- **Grep-bait for one recurring cause:** financial primaries write negatives as `(x.x)` — any parser reading filings/IR tables must handle parenthesized negatives or it silently drops exactly the bad months. (VULCAN's fix re-pulled 20/20 clean; it also base-rated its new band before shipping — 50% fire-rate → tightened to 2-consecutive, 35% — per [[finding_base_rate_the_threshold_before_building_it]].)
- **⚠️ This extension carries only the INSTRUMENT half of the 8/21 incident.** The READER half — why the tool's honest, visible error count made the 8 surviving rows *feel* verified ("a fail-loud tool that also half-succeeds launders the half that survived") — lives in [[finding_fail_loud_on_incomplete_data]] (sixth refinement, VULCAN, same day). Neither file alone is the full lesson; a reader who lands here and stops has a true half. *(Cross-links added same day, both directions — possible only because each encoder told the other where they filed; that tell-them-where-you-put-it step is the cheap guard against split truth, the failure dedup-before-create cannot catch: two desks independently extending different CORRECT homes.)*

---

**Extension 2026-08-26 (WALTER, walter_doctor `terry_override_ratio`) — the GOVERNANCE form: the silently-skipped rows carried a Will-ratified TRIGGER, so the benign fold suppressed a ruled state change, and the failure's cause was the desk's own good habit.**

The check's falsifier leg parsed `delivery_log.timestamp_routed` with `fromisoformat`; on `ValueError` it `continue`d — a silent row-skip. The rows it skipped carried WALTER's own **`~HH:1xZ` anti-false-precision stamps** (a *prose* convention leaked into a *machine-read* TSV field), so every TERRY action row was invisible and the doctor printed **"falsifier unfired"** while `SIG-W-20260822-002-CORRECTION` sat ~78h unconsumed — the exact condition of §3.5.5's non-renewable revert falsifier, Will-ratified with its remedy pre-named. The fire was found only because the boot cross-checked the doctor's line against the artifact (file mtime + delivery row) instead of accepting the clean verdict.

symptoms: doctor says unfired but the file is still there; check prints clean while the condition is met on disk; fromisoformat ValueError continue; timestamp with x placeholder breaks parser; falsifier never fires; row silently skipped on parse error

**Added to how-to-apply:**
- **The skip-`continue` on a parse error IS the benign fold, even with no counter incremented.** "Unfired/clean/0 violations" is itself a substantive bucket; a row that can't be parsed must surface as CANNOT-EVALUATE (rc=2 class), never vanish into the clean verdict. (Adopted as the interface contract for the R1 corrections boot leg, DAEDALUS build 8/27 — this incident is its founding case.)
- **A desk's own hygiene conventions are a parser-failure source.** The `~1x` obfuscation exists to avoid false precision in prose — correct there, poison in a TSV field code consumes. Rule: machine-read fields carry exact machine-parseable values; the humility convention lives in prose only.
- **Highest-consequence variant: the skipped rows carry a REGISTERED trigger.** A random skipped row loses a datum; a skipped row whose content is a ruled tripwire silently suppresses a governance state change — and the "clean" verdict then reads as the rule working. When a check enforces a ratified rule, test it with a synthetic FIRING row before trusting any quiet output ([[finding_test_the_guard_not_just_the_guarded]], [[finding_guard_correctness_and_wiring_are_independent]]).
