---
name: finding_primary_is_not_one_tier
description: "Two PRIMARY documents can disagree, and the operative contract is often the wrong one — a contract's recital/definition list is weaker evidence about a THIRD-PARTY document than an index that points at that document. A single-source primary pull structurally cannot see this class."
metadata: 
  node_type: memory
  symptoms: "two filings disagree on a trustee/counterparty/date; the credit agreement says one name and the 10-K says another; I cited the contract because it's the operative document; both sources are primary so which wins; sub-agent contradicts my primary-sourced table"
  type: finding
  originSessionId: a75e736a-6335-4ec1-8b6d-bed97781aa4e
  modified: 2026-08-28T02:15:21.231Z
---

**`[PRIMARY]` is a single tag over a stack of very different evidentiary strengths.** When two primary documents disagree about the same fact, "it's in the operative contract" is not a tiebreak — and the contract is frequently the side that is wrong.

**The discriminator is not which document is more authoritative overall. It is which document the fact is ABOUT.**

- A contract is **strongest** about its own terms — what the parties agreed, what the thresholds are, what the definitions mean. Nothing outranks it there.
- A contract is **weak** about *third-party* documents it merely **recites** — a list of "Existing Securitizations," a schedule of prior facilities, a background recital naming other people's agents, trustees, or dates. Those lists are drafted from a data room, often copy-pasted from a prior deal, and **no counterparty proofreads them because nothing turns on them.**
- An **exhibit index that incorporates the actual instrument by reference** is stronger about that instrument than any recital of it, because it points AT the document rather than describing it.

**The case (DEWEY, 2026-08-27, CRMT/DR-6).** A conformed credit agreement's "Existing Securitizations" definition named **Wilmington Trust** as indenture trustee for a live ABS trust. The 10-K exhibit index — incorporating *the actual Indenture dated 10/9/2024* by reference to its own 8-K — named **Deutsche Bank**, as it did for all five live trusts. The credit agreement was wrong. I had already drafted the trustee table and a dated migration narrative off it, and would have shipped both to a desk with an **active Wilmington-Trust-trustee-risk vector** — manufacturing a link that had no live referent.

**⚠️ The half that generalises hardest: a single-source primary pull CANNOT see this class.** There is no internal tell. The contract is well-formed, internally consistent, recent, executed, and load-bearing on every other point. Re-reading it more carefully returns the same wrong answer with more confidence. **It surfaced only because two independent legs read two different primaries and disagreed** — the disagreement was the entire signal. Confidence in a primary-sourced cell is therefore not evidence about that cell; it is evidence about how many sources touched it.

**How to apply:**
1. **Classify each load-bearing fact by what it is ABOUT, not where you found it.** If the fact concerns a *third party* (trustee, agent, servicer, custodian, auditor, counterparty, another deal's date or size), a recital naming it is a **lead**, not a citation.
2. **Deliberately duplicate the source for third-party facts** — the exhibit index, the actual filed instrument, or the third party's own filing. This is the one place where redundant primary pulls pay, and it is cheap relative to shipping a wrong counterparty into someone's risk map.
3. **When two primaries conflict, do not average, defer, or pick the more impressive document.** Ask which one the fact is about, and go to the instrument itself. Then say in the deliverable **that the conflict existed and how it resolved** — the next reader will otherwise re-derive the wrong side from the same contract.
4. **A conflict pointed at a colleague's live thesis is worth a same-session flag**, not a footnote: the wrong version is the one that sounds like corroboration.

Sibling to [[finding_reconcile_mismatch_does_not_say_which_side_is_wrong]] (that one is count-vs-contents *within* one artifact; this one is document-vs-document across two). See also [[finding_owner_of_record_means_authoritative_not_correct]], [[finding_verify_reader_before_source]], [[finding_asymmetric_rigor_counterparty_claims]].
