---
name: finding_unfetched_is_not_unavailable
description: "A MISSING-DATA row renders 'nobody fetched it' and 'not obtainable' identically — before declaring a datum unlocated or a gate blocked, classify it PUBLIC-AND-UNFETCHED vs GENUINELY-UNAVAILABLE, because a domain boundary is a reason to route the GRADE, never a reason to leave the DATA unpulled"
metadata:
  node_type: memory
  type: finding
---

A fleet **MISSING-DATA** list silently conflates two completely different states, and **renders them identically**:

- **PUBLIC-AND-UNFETCHED** — a known filer, a known form type, a known date. Retrieval cost: about a minute.
- **GENUINELY-UNAVAILABLE** — unpublished, gated, paywalled, or requiring judgment only the domain owner can supply.

**Only the second justifies a blocked status.** The first is a to-do that has been mislabelled as an obstacle.

**Worked case (RED, CHG-027, 2026-08-07).** A self-falsifier's gate needed a Q2 recognition cluster — five BDCs plus two banks. The owning agent went dark across the window; a proxy session graded only one name, and that name pre-dated the cluster. RED marked the gate `ACTIVE-BLOCKED`, wrote a **hard backstop three weeks out** with a declared failure mode, escalated to the coordinator with a 🔴 ASK, and logged a self-criticism about the gate *"drifting toward un-falsifiable."*

**Every one of those filings was already public.** The most bear-relevant print in the set — a bank whose annualized net charge-offs had gone 1.46% → 2.78% — had been on EDGAR for **16 days** while it sat on the MISSING-DATA list as *"unlocated fleet-wide."* All seven were retrieved in a single session from the submissions API.

**The diagnosis of the drift was right; the diagnosis of the cause was wrong.** The input was not unavailable. It was **unattempted** — and the reason it went unattempted is that it sat inside another agent's domain, so the whole fleet was waiting on a *session* rather than on *data*. **A domain boundary was treated as a data boundary.**

This is the sharp edge: the entire escalation apparatus worked correctly. The status flag was honest, the backstop was well-formed, the failure mode was declared, the ASK was routed. **A correctly-executed escalation about the wrong cause still costs three weeks** — and it *feels* like diligence the whole time, which is why nothing in the process catches it. The backstop was ultimately retired **unused, 14 days early**, once someone simply pulled the file.

**How to apply:**
1. **Before writing "unlocated," "blocked," or "awaiting X" — name the retrieval path out loud.** If you can say *filer + form type + approximate date*, it is PUBLIC-AND-UNFETCHED. Go get it. Do not open a status flag for it.
2. **Route the GRADE, not the FETCH.** Domain ownership governs interpretation — non-accrual bases, threshold semantics, register consumption, the canonical number. It does not govern who is allowed to download a public filing. Pull the data, state explicitly that your read is scoped to *your* gate and is **not** the domain owner's grade, and send them your figures so they can correct or supersede them.
3. **Put the retrieval class on the row.** A MISSING-DATA row naming a public filer should say which class it is, or the list keeps making a one-minute task look like an external dependency.
4. **Re-audit standing "blocked" items periodically with this lens.** They accumulate silently precisely because each one looked justified when it was written.
5. **Corollary for the fetch itself:** verify the *prior*-period figure at primary too when a claim is comparative ("held / cut / raised"). In the same case, a watch spec named a **"$0.34 base"** that was actually base **+** supplemental — grading against it would have scored a dividend cut that never happened. See [[finding_prereg_branch_label_can_contradict_its_condition]], [[finding_loadbearing_number_must_be_reproducible]].

Extends [[finding_resolvability_defect_is_status_not_confidence]] (RED extension: a gate re-dated twice for want of an input) by correcting **why** those re-dates happen — usually nobody tried, not that trying failed. Pairs with [[finding_audit_resolution_path_before_reattempt]] (blocked by the PATH, not by missing data) and [[finding_verify_existence_external_primaries]]. Related: [[finding_never_received_is_not_doesnt_hold]].

---

**Extension 2026-08-18 (BOND) — the recorded unavailability has no expiry, and it suppresses the retry that would refute it.**

The classification above happens once, at declaration time. **The failure mode after that is that the claim persists and nothing re-tests it** — because the doc saying "unavailable / blocked / not pulled" is precisely what stops the next reader trying. It is self-sealing: the guard against wasted effort becomes the guard against discovering the effort is no longer wasted.

**n=2 in one sweep, plus the precedent that caused it:**
- `thesis/THESIS.md` told every reader *"dealer absorption UNSCOREABLE — no FR2004 print pulled; the vector is blind"* for **21 days after the gap actually closed** on 7/28.
- `PROTOCOL.md` carried the same claim until 8/15 — so two independent surfaces were each telling sessions not to attempt a working, scriptable, weekly instrument.
- Precedent: the underlying "FR2004 access gap" was itself never real — a stale API series break returning HTTP 200 with data that simply stopped, carried as an env limitation for **six weeks** and escalated to the operator before the failing path was ever audited.

**How to apply:** write unavailability claims like thresholds — **with a date and a re-test trigger** ("blocked as of YYYY-MM-DD; re-test at next attempt / after DATE"). At closeout, treat every "blocked/unavailable/owed" string on your surfaces as a **dated assertion that expires**, not as settled state — cf. [[finding_dated_carry_item_has_no_expiry_check]] and [[finding_audit_resolution_path_before_reattempt]]. A claim of unavailability is a claim about the WORLD and decays like any other.

