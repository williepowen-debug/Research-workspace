---
name: finding-subagent-escalation-mode-discriminator
description: Propose-only sub-agents (KOYOMI/KURA/METSUKE pattern) should discriminate escalation handling — money/irreversible blocks on Will; low-stakes/reversible structural applies sane default + logs rationale + flags for veto
metadata: 
  node_type: memory
  type: finding
  originSessionId: f7f596c8-aff4-452c-857a-cb95382ad168
---

Propose-only sub-agents (KOYOMI / KURA / METSUKE — the pattern: spawned by a parent agent, returns proposals, parent applies) should NOT escalate every uncertain item to the user. The escalation-mode discriminator:

| Class | Handling | Examples |
|---|---|---|
| **Money / irreversible** | **BLOCK on Will.** Sub-agent surfaces; parent does NOT apply default. Wait for explicit decision. | Position size, stop level, strike/expiry, premium price, dollar amount of intervention/trade, anything that costs money to undo, anything that's user-facing once shipped |
| **Low-stakes / reversible structural** | **APPLY THE SANE DEFAULT, LOG THE RATIONALE, FLAG FOR VETO.** Sub-agent's default-if-undecided fires; parent applies; Will can override on next turn — don't block. | TSV scope decisions, KB routing (which workbook vs auto-memory), workbook column schema, calendar precedent, sub-agent calibration tuning, doc structure changes |

**Why:** The propose-only pattern earns its keep by reducing Will-decision load. If sub-agents block on every borderline call, the pattern devolves into "sub-agent + Will round-trip every run" — at which point sub-agent isn't propose-only, it's just slow-spawn. The right test is **reversibility × stakes**. A wrong KB-routing call can be re-routed next session at zero cost. A wrong stop level can blow up a position. The protocol should match.

**How to apply:**
- Sub-agent specs include the discriminator inline (so the sub-agent self-classifies each escalation).
- Sub-agent surfaces low-stakes calls with: (a) the default-if-undecided action it took, (b) the rationale, (c) explicit "Will-override on next turn if disagrees." Use "ESCALATION-LOG" framing, not "ESCALATION-BLOCK."
- Sub-agent surfaces money/irreversible calls with: (a) the question, (b) the options + tradeoffs, (c) NO default action — block waiting on Will. Use "ESCALATION-BLOCK" framing.
- Parent agent (SAM in this pattern) respects the framing: applies log-mode defaults inline + commits; surfaces block-mode questions to Will + waits.

**Worked example (SAM, Jun 3 2026):** KOYOMI Run 5 hit a TSV-scope question (admit SAM-internal mechanical triggers to CATALYSTS.tsv?). This was **low-stakes/reversible structural** — wrong call costs nothing (revert the rows, narrow the spec, move on). KOYOMI handled it as escalation-block (defaulted-if-undecided to "CALENDAR narrative only, no TSV row") and surfaced to Will. Will applied option (a) — extend scope — with guardrails (type tag + inclusion bar + parser tests + log precedent in spec). The correct handling for next time: KOYOMI applies its sane default inline, logs the rationale, and SAM forwards a log-mode note to Will; Will overrides if needed. Saves one Will-decision round-trip per borderline call.

**Counter-example (money/irreversible — KEEP blocking):** if METSUKE flags a position-card cost-basis discrepancy ("TRADE reads $58.32, source-of-truth unclear") — that stays BLOCK. Will-confirm only, no default applied. Per `[[feedback_position_cost_basis_not_authoritative]]`.

**Where this gets codified:** one line in each sub-agent spec's autonomy/escalation section pointing to this finding; one line in each sub-agent's CALIBRATION clarifying which class of escalations the sub-agent should default-and-log vs block. The discriminator is the protocol, not a per-instance call.

Related: [[finding_subagent_baseline_audit]] (sub-agents need explicit decline-memory to prevent re-nagging); [[finding_subagent_memory_split]] (sub-agent spec vs state file ownership pattern).
