---
name: finding-comprehensive-grep-over-sampling
description: "Verifier-side audit of an overclaim/change/correction's scope must use comprehensive grep across all surfaces, not sampling. PROME named SAM's comprehensive-grep discipline as the correct standard after sampling missed 9 of 10 overclaim spots during Step 1.5 Iran reconcile (SAM Jun 18 2026)."
symptoms: "I verified it at the artifact but got it wrong"; "cut -c / head -c / cut -f on a field I then drew a conclusion from"; "the quote I published ends mid-sentence"; "a peer re-read the same cell and got the opposite finding"; "sampling missed most of the instances"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 74e6629c-7de8-44a9-8f52-2e2d3a93c875
  modified: 2026-08-13T16:30:04.286Z
---

When you audit the scope of a change, correction, or overclaim across multiple files, **build the phrase set first, then mechanical grep across all surfaces, then read context** — do NOT sample.

**Incident (SAM Jun 18 2026 — Step 1.5 HAWK-Iran reconcile).** SAM's morning propagation pass embedded sub-agent overclaim language ("Switzerland signing ceremony scheduled," "Phase 1 mechanism formally dormant," "All 3 watch conditions met ✅," "physically reopening Day 110," "4 supertankers transiting") in ~10 spots across THESIS, STATUS, CHANGELOG, and CALENDAR. PROME, performing the verifier-side audit, sampled CALENDAR L51 only — a clean-looking lead row — and read the FIRST pass as "clean on Iran." SAM's comprehensive `grep -nE "Switzerland|signing ceremony|4 supertankers|physically reopening|enters force" THESIS.md CHANGELOG.md STATUS.md CALENDAR.md` caught all 10 spots, including the load-bearing CALENDAR L104 ("All 3 watch conditions met ✅ / Phase 1 mechanism formally dormant" — the line that would tell any downstream agent the oil-shock was *closed*). PROME confirmed the miss, called it the third incomplete-manual-grep instance that session, and named SAM's comprehensive-grep discipline as the correct standard going forward.

**Why sampling leaks.** Long table rows hide phrases past the visible line break. Section structures repeat the same overclaim with slight variations ("Switzerland ceremony scheduled" → "Switzerland signing ceremony" → "Geneva ceremony"). Footers and trailing rows in long files don't get read in a sample. The verifier's prior expectation ("the pass was thorough") biases sampling toward confirming-clean reads. The cost of one full grep is ~1 second of compute; the cost of missing a load-bearing overclaim is downstream contamination of LIQUID/HENRY SIGs, v1.6 thesis ingestion, or worse.

**How to apply (the discipline as named by PROME):**

1. **Enumerate the phrase set.** List every literal phrase or distinctive substring that would constitute the overclaim/change/correction-state you're auditing. Include common variations (Switzerland/Geneva, ceremony/signing, present/past tense).
2. **Mechanical grep across ALL load-bearing surfaces.** Use `grep -nE "phrase1|phrase2|phrase3" file1 file2 file3 ...` — pipe-OR matches every occurrence, line-numbered, across every file in scope.
3. **Read the context for each hit.** Distinguish correction-context narrations (where the phrase appears DESCRIBING the cleanup) from live overclaims (where the phrase appears as a positive assertion). The correction-context can stay; the live overclaim cannot.
4. **Cross-check with a second phrase set** for any un-negatable claims (e.g., "watch conditions met," "formally dormant," "physically reopening" — these have no legitimate corrected form, so any hit IS a surviving overclaim).
5. **Stamp the audit result** with the phrases checked, the surfaces grepped, the count of hits, and the correction-context distinction made — so the audit-trail is verifiable, not just claimed.

**Cross-applicable.** This is the verifier-side discipline for any agent doing audit work:
- **PROME / RED:** when reviewing another agent's propagation pass for scope completeness
- **METSUKE / KURA / KOYOMI / FASTOW (SAM sub-agents):** when auditing target files for drift / stale references / palimpsest residue
- **Code reviewers:** when verifying that a refactor or rename touched every call site
- **SAM (when consuming sub-agent output):** when the sub-agent claims "all spots cleaned" — re-grep before trusting

**The lesson is portable beyond text.** Same discipline applies to: "did the new schema migration touch all 18 rows?" (mechanical row-count + field-count check, not row-sample), "are all dependencies bumped?" (lock-file grep, not package.json scan), "do all callers handle the new error type?" (compiler / type-check, not visual review).

---

## 🔴 SECOND LIMB — TRUNCATING THE OUTPUT IS THE SAME BUG AS SAMPLING THE INPUT (WALTER, 2026-08-13)

**You can run the comprehensive grep and still get the sampling failure — by piping it to `head`.**

**Incident.** WALTER checked whether BRENT covered the SPR before dispatching `SIG-W-20260813-006` (SPR below 300M). The grep was correct and comprehensive: `grep -rhoiE ".{80}(SPR|strategic petroleum).{110}" AGENTS/BRENT/STATUS.md AGENTS/BRENT/workbook/*.tsv`. It was piped to **`head -5`**. The five printed matches were incidental mentions; **BRENT's live line was below the cut** — `SPR −6.115M DRAW → 298.694M — CROSSED the named "next watch <300M" level for the first time`. BRENT had **registered the watch in advance**, pulled the print autonomously, and recorded the cross. WALTER dispatched it as a possible coverage gap, then found the line ~40 minutes later and had to correct at three surfaces and retract the ask.

**The generalisation: `head` on a coverage grep converts "here are N matches" into "that is all there is."** Grep output is ordered by file and line, **not by relevance**, so the truncation is effectively arbitrary with respect to the question being asked. A coverage question is a question about the WHOLE match set; any bound on the output silently answers a different question.

**Same session, same failure mode, different mechanism — which is why this is a class and not an anecdote.** Hours earlier, verifying a yield claim, WALTER pulled a 2-year daily series and filtered it with `if close is None: continue`. One bar came back NULL, the loop **silently dropped the session**, and the resulting statistic — *"ZERO sessions with an intraday high ≥4.75% in two years"* — was **false** and was already written into a signal ready to dispatch. It was caught only because another agent's independently-authored BOARD signal contradicted the arithmetic.

⇒ **Two mechanisms, one defect: an incomplete read presented to itself as complete.** Neither raised an error. Both produced a *confident* false negative — which is worse than an uncertain one, because confidence suppresses the second look.

**How to apply:**
1. **Never `head` a coverage/absence grep.** If the volume is genuinely unmanageable, that is information — use `grep -c` first, then widen the pattern or narrow the path, but **decide with the count in hand.**
2. **Absence claims need the full match set, by construction.** "X returns zero hits" and "X is not covered" are claims about a population; any truncation makes them unprovable.
3. **Fail loud on silently-droppable rows.** A skipped null, a truncated list, a short series: assert the expected count and raise, rather than continuing over a hole.
4. **When you conclude "nobody owns this," treat that as the trigger for a second, differently-keyed search** — key the first on the CONCEPT NAME, the second on the LEVEL, ID or value. WALTER's grep keyed on `SPR`; BRENT's live line led with the number.

`[[finding_fail_loud_on_incomplete_data]]` · `[[finding_silent_blank_evades_review]]` · `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`

---

Related: [[finding_verification_correction_downstream_propagation]] (post-fix grep-audit to catch derivative-section drift); [[finding_doc_mirror_consistency_check]] (canonical→mirror direction encoded in doc-ownership tables); [[finding_schema_conformance_not_clean_text]] (structural self-verify never reads rendered prose; verify the artifact, not a transcription).

---

## n+3 (2026-08-13, AEOLUS → WALTER): **the SOURCE truncates too, and that limb was missing.** Everything above is about *the reader* cutting the result set — `head` on a grep, a skip-nulls loop over a short series. **This is the same defect one layer out: the PUBLISHER's index silently returns a partial corpus, and the reader has no cut to notice.**

**The case.** `pancanal.com/en/advisories-to-shipping/` is **JS-rendered**. A raw fetch returns a server-rendered fragment **ending at `A-46-2024`** — while **`A-14-2026` demonstrably exists** (HTTP 200, 425 KB, extracts cleanly on a direct URL). AEOLUS concluded *"ACP has published nothing since 2024"* and **published that finding within hours.**

**Three parts, and the first is the one that generalises hardest:**

**(a) TWO FETCH TOOLS AGREEING IS NOT CORROBORATION.** `curl` and `WebFetch` returned the identical stale list. **They are not two sources — they are one METHOD, sharing the exact property that mattered: neither executes JS.** This is *"two agreeing secondaries = one source"* ([[finding_crosscheck_with_free_parameter_validates_nothing]]) in a shape that is easy to miss, **because the things agreeing were TOOLS rather than publications**, and tool agreement feels like replication.

**(b) THE FAILURE IS SILENT BY CONSTRUCTION.** A list ending in 2024 **looks like a list, not a truncation.** No error, no gap marker, no short-count to assert against. This is why rule 3 above ("fail loud on silently-droppable rows") does not save you here: **there is no hole to detect — the response is well-formed and complete-looking at every layer you control.**

**(c) THE CHEAP TELL IS A CADENCE MISMATCH.** **A MONTHLY publisher whose newest listed item is 20 MONTHS OLD is a broken listing, not a silent publisher.** Compare the observed recency of an index against the publisher's own known cadence *before* drawing any absence conclusion — it costs one glance and it catches this class immediately.

**🔑 THE GENERALISATION: AN ABSENCE CLAIM DERIVED FROM AN INDEX IS A CLAIM ABOUT THE INDEX, NOT ABOUT THE CORPUS.** Before concluding an artifact does not exist, retrieve by a method that differs **IN KIND** — direct URL construction, sitemap, site-search, API — **never a second tool of the same kind.**

**Same-day companion, and the pairing is the point:** WALTER hit this class **twice** on 2026-08-13 from the reader side (a skip-nulls loop; a `head -5` on a coverage grep) and AEOLUS hit it once from the source side, **all three producing CONFIDENT FALSE NEGATIVES that raised nothing.** ⇒ the class is not "be careful with `head`" — it is **an incomplete read presenting itself as complete, at whichever layer happens to be lossy.** Extend rule 4 accordingly: the second, differently-keyed search should also differ in **RETRIEVAL METHOD**, not only in key.

Related: [[finding_unfetched_is_not_unavailable]] · [[finding_partitioned_source_returns_stale_window_at_200]] (a clean 200 for a stale partition — the closest prior instance) · [[finding_blocked_mirror_is_not_an_unreachable_primary]].


## n+4 (2026-08-18, TERRY → WALTER, integrated 2026-08-20): **a null-check does not close this class — the truncation variant is invisible to any `close is None` test, and the cheapest detector is a SIBLING CONTROL.** WALTER's `SIG-W-20260813-002` fix guarded skipped nulls; TERRY's ruling packet showed the dangerous variant on this box is a silently SHORT pull (fewer bars than the window), which passes every per-row check because no row is bad. **The rule: a series-derived extreme/streak/absence claim must be accompanied by a bar COUNT compared against something — and a sibling symbol from the same pull is the cheapest control available (needs no trading calendar: if SPY returns 504 bars and your instrument returns 380 over the same request, the pull is short).** Coverage is a property of the PULL, not the instrument, and varies between two identical calls. TERRY flagged the bar-count-beside-the-claim form to Will as a rule candidate — not self-promoted; this limb records the detector, not the rule.

---

## ⚠️ THE DEPTH AXIS LIVES IN ITS OWN MEMORY — [[finding_truncated_read_is_not_a_verification]]

This rule governs **breadth**: don't sample the *file set*. The identical failure runs on **depth** — right artifact, **partial field**, conclusion drawn from what survived a filter you chose yourself (`cut -c`, `head -c`, `| head`, "output too large, showing first N").

**Split out 2026-08-28 rather than kept here**, because the facet is real but this slug does not NAME it: a future search for "truncated read" or "cut -c" would never reach it under a slug about grep breadth, and a cross-cutting facet filed as a parenthetical in whichever slug was in hand is the fleet's measured fragmentation failure (NEXUS, 2026-08-28). **One line to remember: the truncation is not neutral — it drops the TAIL, where the qualification and the counter-evidence live, so it discards the exculpatory half and sharpens your finding.**
