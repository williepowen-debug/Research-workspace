# BOND MEMORY — Persistent Learnings

**Created:** 2026-06-15 (durable lessons lifted from STATUS prose + the retired LAST_COMPLETION)

## Genesis
BOND owns the US bond-market-structure transmission layer — Treasury auctions, dealer positioning, corporate issuance, curve shape, the credit→equity lead. Sits between LIQUID (plumbing) and ZHAO (foreign flows). Promoted to Tier-1 peer 2026-06-15.

## Durable Learnings (BOND-local; fleet-wide lessons live in auto-memory, referenced not restated)
- **"Expensive, not broken" (BOND-core):** the long end clearing demand *at price* (term-premium digestion) is categorically different from a *demand hole* (mechanical failure → dealer warehousing → funding stress). Keeping these distinct IS the thesis. Held 4 straight resolutions (BND-05 F · 06 T · 07 T · 08 F).
- **Confirm the instrument before keying a demand gate:** the 5/21 "10Y reopening" was a 10Y *TIPS* reopen (CUSIP 91282CPU9), not nominal — different buyer base; conflating them mis-specified an add-gate. Fleet analog `[[feedback_verify_treasury_security_type]]` (the "term" field collapses TIPS and nominals — check securityType/CUSIP family).
- **Grade auctions against the sentiment backdrop, and escalate sizing — don't auto-execute (Will via Prome, 5/21):** the same print reads differently by backdrop. On a **held-rally / constructive-sentiment** day: a *weak* print = **upweighted** bear signal; a *clean* print = consistent-with-backdrop bull (not new bull). Operational consequence: when a marginal add would fire, on a held-rally day the recap **surfaces the upsize question to Will rather than silently executing a half-add**. Relates to `[[feedback_anchor_prediction_to_surprise_not_priced]]` (grade vs what's priced) and `[[finding_subagent_escalation_mode_discriminator]]` (money/irreversible → block on Will).
- **Dealer-absorption is a STOCK vector, not a FLOW one:** it tracks dealer balance-sheet *capacity* (NY Fed FR2004 inventory), not auction takedown. A benign auction (low dealer take) shows the backstop wasn't *binding* that day — it does NOT refresh the inventory stock. Only the next FR2004 can downgrade the vector. (Caught this session: I downgraded 3→2 on flow; ORC corrected — reverted to 3.)
- **Macro HY OAS is a top-only read:** it can be calm (271) while CCC (948) and energy HY decouple underneath. Always carry the bifurcation caveat. Fleet analog `[[finding_blended_index_masks_bifurcation]]`.
- **Resolve auction predictions from TreasuryDirect primary, not news:** search/news summaries conflate auctions across dates (caught at BND-08, 6/15) — pull the API/PDF. And when the primary source *can't pin* a needed figure (e.g. the auction tail / when-issued isn't published), **flag the inference explicitly rather than stamping a clean verdict** (BND-08 FALSE rested on a tail inferred from the same-day rally, not a confirmed number). Fleet analog `[[feedback_pull_live_primary_not_dashboard]]`.
- Applies fleet auto-memories `[[threshold_vs_mechanism]]` (BND-07 fired the threshold but was an episode, not a break) and `[[feedback_put_vs_duration_expression]]` (TLT puts cleaner than equity puts for a duration short) — see auto-memory, not restated here.

## Process
- **Pending-push discipline:** BOND commits local-only on the shared branch; ORC verifies against committed files only after a coordinated push. Keep the pending-push queue live in SCRATCH.
- **Path-scoped commits when peers are concurrent:** other agents (e.g. BROCK 6/15) commit in the same clone — use `git commit AGENTS/BOND/<file>`, never a plain `git commit` of the index, to avoid sweeping their staged files. Fleet analogs `[[finding_concurrent_commit_index_race]]`, `[[finding_pathspec_commit_race_safety]]`.
