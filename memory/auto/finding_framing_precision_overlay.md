---
name: finding-framing-precision-overlay
description: "When a sub-agent's framing is conceptually useful but literally overspecified (a wrong count, a misclassified state), write a framing-precision overlay note in the target inbox rather than re-spawning the subagent or silently editing the output"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 91570747-9099-4d04-8503-dde09643c4f1
---

# Framing-Precision Overlay Pattern

**Earned:** 2026-05-19 (PROME session — HENRY revival proxy)
**Validated by:** Will + Prome review of HENRY proxy output

## The pattern

When a sub-agent (especially a revival proxy or research subagent) produces output where the **concept** is genuinely useful but a **literal claim** is overspecified or wrong (e.g., "2 of 3 firing" when literally only 1 has fired and another is approaching), the right move is **neither** re-spawning **nor** silently editing the subagent's output in place. Instead:

Write a **framing-precision overlay note** as a third artifact in the same inbox, with:
1. PROVENANCE header acknowledging it's a Will + Prome review overlay, not subagent output and not target's self-state
2. Explicit pairing reference to the original packet
3. A section explaining what to keep (the concept) and what to correct (the literal claim, with the actual numbers/state)
4. Operational guidance for how the target agent should integrate both files coherently on its next boot

File naming: `<TARGET>_FRAMING_NOTE_<date>_prome-spawned.md` in `AGENTS/<TARGET>/inbox/`. Sits alongside the revival packet + STATUS draft. Untracked-by-design (target commits on next boot).

## Why this works (and why other approaches don't)

- **Re-spawning is expensive and risks losing the conceptual win.** The subagent might re-derive the wrong literal claim, or might over-correct and lose the useful concept.
- **Silently editing the subagent's output** loses the audit trail of who said what and breaks the PROVENANCE chain. Future-target can't tell which framing is theirs to inherit vs ours to integrate.
- **An overlay note** preserves both signals cleanly: the subagent's conceptual contribution AND the human-reviewed precision correction. Each artifact stays attributable.

## How to apply

Trigger conditions:
- Subagent output is mostly good but contains an overspecified claim (a count, a state classification, a confidence level) that Will or you can identify as wrong on review
- The underlying concept the subagent was reaching for is still defensible and useful
- The downstream consumer is an agent that will integrate this output structurally (so silent edits would obscure attribution)

Steps:
1. Identify the conceptual win vs the overspecified claim — state them separately to Will or in writing
2. Confirm cross-agent inbox write authorization with Will (per `feedback_cross_agent_inbox_writes.md` — default forbidden, per-instance only)
3. Write the overlay note with the structure above
4. Note in your closeout that a framing-precision overlay was authored — it's a state mutation worth tracking

## Generalizes beyond revival proxies

The pattern applies to any sub-agent output where a conceptual layer and a literal-claim layer can be cleanly separated. Examples beyond revival proxies:
- Adversarial-pair team outputs where one challenger's argument is structurally right but the example case is wrong
- NEXUS synthesis where the convergence read is correct but a constituent agent's data is misquoted
- Sub-agent verdicts where the verdict-first conclusion holds but a supporting number is stale

In all cases: keep the structurally-right layer, append a precision overlay, preserve attribution.

## Related

- [[feedback-cross-agent-inbox-writes]] — authorization gate for the cross-agent write the overlay requires
- [[feedback-corrected-framing-calibration]] — the verify-research analog: most-frequent verdict is "concept right, specifics imprecise"; same shape of correction
- [[feedback-verify-counts-before-propagating]] — discipline that often surfaces these overspecification cases
- `PROME/ORCHESTRAL_LAYER_DESIGN.md` §"Revival-proxy v3 brief spec" — codifies this artifact type for the revival-proxy workflow specifically
