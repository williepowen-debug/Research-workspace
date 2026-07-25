---
name: finding_read_the_artifacts_own_header_first
description: "Before asserting a defect in a tool, file or figure, read the artifact's OWN header/self-documentation — a known limitation stated in-file, or a basis stated in-file, is the most common false positive. Twice in one session (PROME 7/25)."
metadata:
  type: feedback
---

Before flagging a defect in a tool, file or figure — **read the artifact's own header, banner and inline comments first.** The thing you are about to speculate about is very often documented in the file, and asserting the defect without checking manufactures a false positive that then travels.

**Two PROME instances the same session (2026-07-25):**
1. **The matrix basis.** REGINALD guessed `BANK_EXPOSURE_MATRIX` used a different CRE basis; PROME amplified that unverified guess into "every row's 300%-line comparison is suspect" and propagated it to DAEDALUS. The file *states its basis* (SR 07-1 section header — though its column reads CRE/Tier 1, a real but small internal wrinkle) and carries its own STALE-VINTAGE "do NOT cite" banner. Actual dominant cause: **vintage** (Q3-2025 data in a Feb file). The escalation was withdrawn to both recipients.
2. **`orphan_check.sh`'s "blind spot."** PROME flagged to Will that the detector mislabels PROME's own files `[not yours]` and recommended a scoped fix. The script's header (lines 33-35) **documents exactly this**, scopes it as harmless (PROME is also the flag-to target, domain agents unaffected). Recommendation collapsed to "do nothing."

**Why it matters:** the cost isn't the wrong belief, it's the propagation — a defect claim routed to another agent becomes work, and an escalation built on it becomes *their* stale premise. Both instances were caught within hours only because the counterparty pushed back.

**How to apply:** `head -40` the script / read the file's banner + the section header of the table you're questioning, BEFORE writing the flag. A self-documented limitation is a design decision, not a bug. Cf [[feedback_verify_counts_before_propagating]] and [[finding_verification_correction_downstream_propagation]] (chase a refuted claim to where it landed — both corrections above were routed same-session).
