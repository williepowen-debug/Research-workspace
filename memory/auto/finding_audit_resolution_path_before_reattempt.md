---
name: finding_audit_resolution_path_before_reattempt
description: "A question open for many sessions with a documented resolution path is usually blocked by the PATH (wrong identifier, stale venue, wrong tool), not by missing data — audit the path before the Nth re-attempt"
metadata: 
  node_type: memory
  type: finding
  originSessionId: ff1c1c39-faa7-4783-a62e-60f9509330da
  modified: 2026-07-26T03:12:26.417Z
---

When a tracked question survives multiple sessions and each session records the *same* resolution path ("needs a court-docket pull", "needs the X API", "check ticker Y"), the recurring failure is far more often a **defect in the path** than an absence of data. Audit the path itself before re-running it.

**Worked case (STUE, 2026-07-25).** "AFT v. MOHELA — what happened at the May 28 status conference?" sat open **46 days** across three sessions, each restating the path as *"CourtListener, docket 1:25-cv-00802 — not web-searchable."* All three failure modes were present at once:
- **Wrong identifier** — `1:25-cv-00802` matched six unrelated cases and no AFT case. It had been carried forward unverified.
- **Stale venue** — the record said D.C. Superior Court (a state court, correctly noted as *not* in RECAP), but the case had been **removed to federal court** long before. The "structurally inaccessible" conclusion was true of the old venue only.
- **Unverified premise** — the May 28 conference itself was never on any docket; it came from an SEO legal-aggregator page. The question was partly asking about an event that did not occur.

Once the actual case was found (`D.D.C. 1:24-cv-02460`), it resolved in one fetch — and the answer *inverted the read*: discovery had been **stayed by court order** for nine months. The parent agent's standing note, "absence of news is non-information," was exactly backwards.

**Apply:**
1. **Verify the identifier before re-spending on the lookup.** One cheap existence check (does this docket/ticker/ID resolve to the thing I mean?) beats another failed pull.
2. **Re-check the venue/owner.** Cases get removed or transferred, series get renamed, endpoints move. "Not accessible" is a claim about a *location*, and locations go stale.
3. **Test the premise.** Before asking "what was the outcome of event E", confirm E happened. A well-formed question about a non-event never resolves.
4. **Silence with a mechanism is information.** A quiet docket, empty queue, or flat series may be quiet *by order or by construction*. Find the mechanism of the silence before scoring it as no-signal — a stay, a pause, or a publication lag each mean something specific and different.

**It recurred in the same session — that is the important part.** Hours after writing this memory, I closed out reporting the stay order's basis as *"PACER-gated, ~$0.30 to resolve."* It was not gated at all: the docket carried **free RECAP PDFs** for neighbouring entries, and the very next filing (a joint status report) quoted the stay's purpose verbatim — *"to allow the parties time to explore a negotiated resolution."* Recovered at **zero cost**, and it materially changed the read: the case was in **settlement talks**, not a procedural freeze, which meant the evidence the prediction depended on was likely to be negotiated out of existence rather than merely delayed.

The failure mode is identical to the first: **declaring a path closed by inspecting only the obvious surface.** First time it was "the docket number I was handed"; second time it was "the button that says Buy on PACER." Neither is the whole access surface. Before recording *anything* as gated/paywalled/unavailable, **enumerate the access surface** — free mirrors and archives (RECAP/CourtListener, SEC full-text, FRED ALFRED vintages), adjacent documents that *quote* the target, and the possibility that the item has no separate document at all (a **minute order** has no PDF and cannot be bought — its text lives in the docket report or in later filings that cite it).

Corollary for aging trackers: a question's **age is itself evidence about the path**, not just about the world. Past ~2–3 failed attempts, stop re-running and start debugging the instrument. And note that "I checked and it's unavailable" is a **claim requiring the same rigor as any other** — it is the one conclusion that stops all further inquiry, so it deserves more scrutiny than a positive finding, not less. Related: [[finding_threshold_spec_fails_before_world]], [[feedback_verify_existence_external_primaries]], [[finding_discovery_tool_wrong_slice_false_zero]], [[finding_premise_residue_survives_date_fix]].
