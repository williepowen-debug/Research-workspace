---
name: finding_owned_surface_without_a_ledger_destroys_history
description: "A scope grants OWNERSHIP; a ledger grants RETENTION — check they match. A surface you own but never gave a workbook lives only in a capped, rewritten STATUS, so every superseded print is destroyed rather than retained; audit at promotion and scope-change"
metadata:
  node_type: memory
  type: finding
---

**Owning a surface and retaining its history are two different things, and nothing in the boot or closeout sequence checks the second.**

A domain agent's `CLAUDE.md` names the surfaces it owns. Its workbook holds ledgers. **Nobody verifies the two lists match.** When a surface is named in scope but has no ledger, its figures land in `STATUS.md` — which is line-capped and **fully rewritten every session**. The result is not drift or staleness, both of which leave evidence. It is **silent destruction**: each session's number overwrites the last, and the series never existed.

**Live case (HOMER, 2026-07-31, found in a Will-directed documentation audit).** HOMER was promoted 2026-07-12 with a `★` ruling explicitly granting it the mortgage-rate surface — 30Y PMMS, the 10Y-FRM spread, the FHA-vs-Conventional spread — plus HPI/sales/inventory as core signals. **Both ran 19 days with no workbook at all.** Four ledgers existed (pipeline, multifamily, state, builder); the two newest-owned surfaces had none. Every PMMS print, every spread calculation, every superseded HPI figure since promotion had been written to STATUS and erased on the next rewrite. **There was no rate history anywhere in the agent that owned the rate surface.**

**Why it survives normal hygiene checks.** Staleness tooling (`ledger_staleness.py`, two-clock headers) audits **files that exist**. A surface with no file has no header to go stale, so it reports clean forever — the check is structurally incapable of seeing it. Closeout asks "are workbook rows dated and sourced?", which passes trivially when there are no rows. **The absence is invisible to every mechanism designed to catch the presence of rot.**

**The tell that exposed it** was not a missing file — it was a *populated* one. `BUILDER.tsv`'s header still read the prior session's date while carrying current rows, which prompted an audit of what else had been written where. Checking one file's freshness surfaced the fact that two surfaces had nowhere to be written to at all.

**How to apply:**
1. **At promotion, spinout, or any scope change, diff the surfaces named in `CLAUDE.md` §Scope against the ledgers in `workbook/`.** Every owned surface needs a destination. This is a one-time check per scope change, not a recurring ritual — cheap and high-yield ([[finding_mechanize_the_cap_not_the_ritual]]).
2. **Treat STATUS as the *dashboard* and the workbook as the *record*.** Anything written only to a capped, rewritten file is being thrown away. If a figure is worth citing later, it needs a row.
3. **A newly-granted surface is the highest-risk case** — inherited surfaces usually arrive with their ledger; newly-*ruled* ones arrive as a sentence in a review document with no file attached.
4. **Do not read a clean staleness report as coverage.** It only certifies the files that exist ([[finding_verification_zero_is_ambiguous]] — a check reporting nothing is consistent with "found nothing" and with "looked at nothing").
5. **Corollary for reviewers/architects:** when a ruling grants an agent a new surface, the deliverable is a *ledger*, not a sentence. A scope ruling with no file behind it is unexecuted.

Related: [[finding_passive_surface_rot_push_not_dashboard]], [[finding_ledger_drift_behind_narrative]], [[finding_coverage_gap_needs_all_surface_check]], [[finding_mtime_is_corrupted_by_git_sync]], [[finding_derived_surface_fold_is_the_last_writeback]], [[finding_verification_zero_is_ambiguous]].
