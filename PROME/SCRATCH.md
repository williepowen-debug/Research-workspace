# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-17 ~22:15 UTC (Tuesday)

---

## QUICKSTART
Scenario C, War Day 15. Account $53,040 (+111%). FOMC Day 1 complete. Decision + Powell presser WEDNESDAY 2:30 PM ET.
**HY OAS 328bps — RED threshold crossed.** ADP Pulse 9K/wk — below 10K alert.
**Broad red day for puts** — relief rally hit short book. Nothing structurally broken.
**ARES entered:** Jun $95P at $7.70. ✅
**Harness improvement project active** — designing triage protocol for signal processing.

## SESSION WORK (Mar 17 Tuesday — evening session)
- **Portfolio update:** Account $53,040 (+111.24%), down $3,874 (-6.81%) on day. Relief rally.
  - AAPL now 80 shares (sold 15 more)
  - ARES Jun $95P entered at $7.70
  - VLY $10P Mar 20 at $0.05 — dead, let expire Friday
  - Big winners holding: WAL $85P +176%, KRE Dec +66%, IWM +61%
- **Harness engineering deep dive:** Analyzed article on agent environment design (SWE-agent, Anthropic Claude Code, OpenAI Codex patterns). Key insight: our system already implements most patterns (progressive disclosure, persistent state, clean handoffs, structured task lists). Gaps identified:
  1. **Context flooding on signal batches** — agents get too many signals, quality degrades
  2. **No mechanical verification** of agent output quality
  3. **No structured enrichment** of signals before agent processing
- **Triage Protocol designed (5 phases):**
  - Phase 1: Write protocol doc (routing rules, cap at 5, enrichment template, overflow handling)
  - Phase 2: Dedicated triage chat session (stripped-down boot, single job)
  - Phase 3: Structured agent prompts (pre-enriched signal cards, targeted reference files, output template)
  - Phase 4: Dependency detection (signal chains, sequential spawning for dependent domains)
  - Phase 5: Automated triggers (future — inbox accumulation, auto-spawn at threshold)
- **Key design decisions:**
  - Cap signals at 5 per agent per spawn (SWE-agent capped search principle)
  - Triage enriches signals before routing (domain, priority, data points, thesis relevance, suggested prompt)
  - Dedicated chat surface for triage (keeps main chat clean for analysis/decisions)
  - Will approves routing table before spawns fire
  - Dependency detection sequences spawns (BRENT → CARL → HENRY chains)
- **HERMES PM delivery failed** — API overload error. Will catch up next cycle.

## OPEN ITEMS (PRIORITY ORDER)

### Immediate (next session)
1. **Draft Phase 1 triage protocol document** — ready to write
2. **NEXUS synthesis** of 9 agent OUTBOXes from earlier today — still pending
3. **FOMC decision Wed 2:30 PM ET** — triple event day (+ claims + Shunto)

### This Week
4. **TIC data Mar 18** — ZHAO watching Belgium ($477B, threshold $500B)
5. **BOJ Thu Mar 19** — Ueda hawkish, carry unwind 35% 7d
6. **HYG Jun→Dec roll** — on next green day
7. **VLY $10P Mar 20** — let expire worthless
8. **FL UI Wave 1 exhaustion Mar 24** — T-7

### Research Queue
9. BX deep dive (BROCK)
10. WFC warehouse exposure ($59.7B)
11. Russia sanctions modeling (RED)
12. HANS Europe recon

## CONFIRMED DATA BLOCK
```
Account: $53,040 (+111.24%). Down $3,874 on day.
AAPL: 80 shares, $20,338 (38.35% of portfolio)
ARES: Jun $95P entered at $7.70
APO: $107.55 (Mar 17 ~10:25 AM ET, relief rally)
HY OAS: 328bps (Mar 13, RED threshold breached)
ADP Pulse: 9,000/wk (BREACHED <10K)
VIX: 27.19 (sustained >25)
Gas AAA: $3.79 ($4 breakpoint ~1-2 weeks)
USD/JPY: 159.3-159.5 (intervention line ¥160)
FOMC: Decision + presser Wed Mar 19 2:30 PM ET
BOJ: Decision Thu Mar 19. Ueda hawkish.
TIC Jan 2026: releases Mar 18
Claims: Wed Mar 19
FL UI Wave 1: Mar 24
Kuwait curtailment physical: Mar 20
OZK earnings: Apr 16
APO class actions: May 1
```

## Handoff
**Last context:** Tuesday Mar 17 ~22:15 UTC (6:15 PM ET). Evening session — portfolio review + harness improvement planning. No agents spawned this session.
**Next session:** (1) Draft Phase 1 triage protocol. (2) NEXUS synthesis still pending. (3) FOMC decision Wed — prep needed.
**Rhythm:** Market closed. System design mode.
