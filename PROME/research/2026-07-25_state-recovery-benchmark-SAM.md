# State-Recovery Benchmark v0 — SAM (cold-session recovery cost + fidelity)
**Run:** 2026-07-25 Sat evening (PROME; Will-approved). **Subject:** SAM — the fleet's densest recovery case (STATUS 312 lines / 66.5k chars, >250-line cap, self-flagged 2 sessions running).
**Why:** System report v2 Priority 2 (`AUDITS/2026-07-22_system_analysis_v2.md` §6.3, §12) — "line counts do not measure recovery cost." This run produces the baseline number the P2 state-card protocol needs. DISPOSITIONS row P2.
**Conditions:** weekend-frozen tree (no writers), markets closed. Two independent read-only agents, same model family, launched in parallel with no shared context:
- **Arm K (answer key):** exhaustive extraction, unbounded budget, citations required.
- **Arm C (cold reader):** realistic boot simulation — "read what you need, stop when booted, efficiency is measured."

## Costs

| Arm | Tokens | Tool uses | Wall clock | Files read |
|---|---:|---:|---:|---:|
| K — exhaustive key | 228,166 | 20 | ~4.4 min | 24 |
| C — realistic cold boot | 174,181 | 11 | ~2.5 min | ~18 (10 read steps) |

**Headline: a competent, deliberately-efficient cold recovery of SAM costs ~175k tokens.** The exhaustive sweep costs only ~30% more — the floor is dominated by the mandatory big files (STATUS/THESIS/PREDICTIONS/MEMORY/inbox), not by discretionary reads. Efficiency choices barely move the bill; **file density does.**

## Fidelity (Arm C graded against Arm K; key spot-verified against PROME's independent 7/25 boot reads on 4+ items — GATES SAM rows, HEARTBEAT §4, NEXUS COT relay figure, USD/JPY stamp — all matched)

| Category | Grade | Notes |
|---|---|---|
| 1. Thesis (v1.6.9, MEDIUM tail, mechanism, window) | **FULL** | Version, conviction decomposition, Sep-18 lock, retire conditions all exact |
| 2. Open predictions (5 OPEN + recent resolves) | **FULL** | All IDs, terms, confidences, resolvers exact; scoreboard 12/12/1/5 exact |
| 3. Gates | **FULL−** | SAM-30/ARM3/calendar tripwires exact; HEARTBEAT Near-Gates row unread but self-flagged as the possible gap (it was benign) |
| 4. Domain reads + as-of stamps | **FULL** | COT graded-vs-landed split handled correctly; MOF, USD/JPY, JGB, BOJ OIS, strike watch all exact with stamps |
| 5. Position/trade state | **SUBSTANTIAL** | FLAT + shelved card + no-fabricate caveat exact; missed STRATEGY bands + EWJ/TLT watchlist (skipped TRADE.md deliberately, declared) — low impact on a flat weekend book |
| 6. Pending obligations | **SUBSTANTIAL+** | All 8 unprocessed inbox items enumerated incl. the decision-proximate one; ~85% of MEMORY carried items, tail (insurer tracker anchor, TFF decomposition, tool builds) missed |
| 7. Freshness gaps | **FULL** | Same gap list as the key, incl. the "unpriced is the finding" Jazan read |

**Material errors: zero.** Every gap was self-flagged in the reader's own confidence section — its LOW/MEDIUM marks landed exactly where its real gaps were (well-calibrated self-report). The two arms also converged independently on essentially identical state, which cross-validates both.

## Findings

1. **The cost is the problem; the quality is not.** Recovery fidelity was near-perfect. But ~175k tokens is a large fraction of a session's working context spent before the first unit of new work — on ONE agent. The report's §6.3 claim is confirmed and now quantified. Any P2 card that cuts this 5-10× while preserving categories 1-3+7 pays for itself immediately.
2. **★ The single most decision-relevant fact was NOT on any canonical surface.** The Jul-21 COT rebuild (−152,125, 875 contracts from SAM's −153K re-fire line — the difference between "STALL, nothing pending" and "registered line proximate") lived ONLY in an unprocessed NEXUS inbox packet. Every SAM canonical surface still carries the superseded 68.1% STALL. **Design consequence for the P2 card: a card generated from canonical files alone would have been confidently wrong on the most important number.** The card must carry a pending-inbox/ungraded-inputs section — or equivalently, the P1+P5 exception queue and the P2 card are the same build seen from two sides. (Also live evidence for the report's §6.2 "effective date of current state" distinction, and for keeping inbox-drain in every boot sequence.)
3. **Both arms independently reproduced the key contradictions** (graded-vs-landed COT; TRADE.md one-session drift; THESIS vintage layering) and resolved them by the same ownership rules — the fleet's canonicality conventions are learnable from the files alone, which is a genuine (previously unmeasured) strength.
4. **The stopping-rule behavior was correct:** the reader skipped TIMELINE/CHANGELOG/playbook bodies and lost nothing operational. Boot-doc reading order (THESIS → STATUS → CALENDAR → MEMORY → PREDICTIONS → inbox → gates) is efficient as written; there is no cheap reordering win. The win must come from **surface compression**, not read-order.

## Caveats
n=1 agent-pair on one agent on a frozen weekend; key was agent-built (spot-verified on 4+ items but not line-audited); both arms same model family; the reader knew it was being measured (may bias toward diligence); token counts include tool-result overhead, not just file content.

## Next (for DAEDALUS P2 protocol — packet already routed 7/25)
Repeat on BRENT (mature contrast) + REGINALD or AEOLUS (sprawl/stale contrast) to get a cost range; then spec the card against these numbers with the pending-inbox section mandated by finding #2. Frozen-answer-key + blinded grading per the report's MemProbe-style protocol when it graduates past v0.
