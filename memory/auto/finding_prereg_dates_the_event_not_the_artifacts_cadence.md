---
name: finding_prereg_dates_the_event_not_the_artifacts_cadence
description: "A pre-registration that resolves on a specific ARTIFACT must be dated by that artifact's own publication cadence (filing history, one EDGAR full-text query), not by the EVENT it feels attached to — a card keyed to 'earnings day' for a deck that has landed on an earnings date 0-of-13 times produces a NO-VERDICT-by-construction that reads as a disclosure signal."
metadata:
  node_type: memory
  type: finding
  originSessionId: 78d1c072-c8f0-4bc1-b462-792cba843f2e
---

**What happened (SHADE, Athene M-11 grade card, 2026-08-04):** a card frozen pre-print banded both legs correctly but dated leg 1's source wrongly — it pre-registered the FABN peer-penalty read against *earnings day 8/4*, when the disclosure lives in a standalone quarterly Fixed Income Investor Presentation furnished under its own Item-7.01 8-K. One EDGAR full-text query showed **13 prior events, ZERO on an earnings date** (typically ~5-8 days after the 10-Q). Leg 2 keyed on a 10-Q that was simply not due yet (5 prior Q2 filings: 8/5-8/9). Result: a FULL NO-VERDICT day that the card's own text invited routing as a *recognition-perimeter* signal ("the disclosure disappeared") — a schedule artifact one inference away from being booked as disclosure behavior. SHADE killed the inference at source; the trap is general.

**The rule:** when a pre-registered row resolves on a specific artifact (a deck, a supplement, a 10-D, a monthly table), the registration is only as good as a **cadence check on that artifact**: pull its own filing/publication history and date the read to the artifact's cadence, never to the event it feels attached to (earnings, a decision date, a headline). Cheap — one EDGAR full-text or filing-history query — and it moves the read date *before* the freeze rather than producing a NO-VERDICT after it.

**The dangerous failure shape:** the miss does not read as a dating error — it reads as *"the disclosure is missing,"* which in a recognition/opacity framework is itself treated as a signal. A publication calendar mistake thereby manufactures exactly the class of evidence the framework is designed to detect.

**How to apply:** at registration (and at any re-freeze), for each leg ask *"what is this artifact's OWN publication cadence, per its own history?"* and write the expected window from that history with the n. If the artifact has never once published on the event date being keyed to, the card is mis-dated by construction.

Related: [[finding_announcement_type_and_filing_precheck]] (verify the filing exists before naming a driver — this is the scheduling twin), [[finding_executability_is_a_separate_audit_axis]] (can the rule be graded inside the window its instruments actually quote), [[finding_count_what_published_before_reading_the_verdict]] ("no adverse reading" vs "no reading" — a mis-dated read manufactures the second while recording the first).
