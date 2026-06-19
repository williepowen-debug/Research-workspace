---
name: finding-comprehensive-grep-over-sampling
description: "Verifier-side audit of an overclaim/change/correction's scope must use comprehensive grep across all surfaces, not sampling. PROME named SAM's comprehensive-grep discipline as the correct standard after sampling missed 9 of 10 overclaim spots during Step 1.5 Iran reconcile (SAM Jun 18 2026)."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 74e6629c-7de8-44a9-8f52-2e2d3a93c875
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

Related: [[finding_verification_correction_downstream_propagation]] (post-fix grep-audit to catch derivative-section drift); [[finding_doc_mirror_consistency_check]] (canonical→mirror direction encoded in doc-ownership tables); [[finding_schema_conformance_not_clean_text]] (structural self-verify never reads rendered prose; verify the artifact, not a transcription).
