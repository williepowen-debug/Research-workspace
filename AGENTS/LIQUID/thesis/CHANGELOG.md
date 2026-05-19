# LIQUID — Thesis Changelog

## v2.0 — 2026-05-19
**Major revision after 32-day staleness gap (Apr 16 → May 18) and channel-migration finding.**

### What changed
- **Narrower active scope.** v1.0 implied LIQUID owned the full Treasury-market story (auctions, yields, foreign flows). v2.0 explicitly narrows LIQUID's active monitoring to: repo plumbing, credit spreads, public-BDC mark catch-down, APO co-trigger, basis-trade structural tracking. Yield curve and granular auction mechanics are flagged for BOND-primary (when active).
- **Channel migration as a first-class concept.** New §1 + §4 framing: the bear thesis transmits through whichever channel is currently active, and channel migration is normal (not thesis-abandonment). Operationally grounded in KB-LIQ-052: the Apr→May gap saw PLUMBING resolve mechanical (KB-LIQ-051) and DURATION become the active leg.
- **Bilateral credit framework.** v1.0 had only an escalation ladder upward (320 → 350 → 400). v2.0 adds the kill side: **260 KILL** with a five-rung trigger ladder (workbook/KILL_MEMO_HY_OAS_260.md), plus the **APO >$130 ×3 sessions co-trigger** (HEARTBEAT line 80). Reflects the squeeze-resolution path being a real risk worth its own kill condition.
- **Gamma-suppression caveat added.** New epistemic warning (§5, §9) — positive gamma may suppress VIX / HY OAS even while substance accumulates. Cross-verify too-calm prints during loud-substance windows. Origin: 5/14 Will/Prome signal.
- **BOND interface added.** New cross-agent receive line in §8 for when BOND stands up. Yield curve / term-premium / dealer positioning migrate to BOND-primary; LIQUID retains FOI-flow and basis-trade legs at the thesis level.
- **Channel-kill vs full-thesis-kill distinction.** v1.0 framework was monolithic. v2.0 explicitly: each channel can kill independently; full abandonment requires multiple legs failing concurrently.
- **Stagflation trap reinforced.** Brent $110.57 + 30Y 5.168% concurrent on 5/19 is the textbook configuration. Doc updated to cite current reinforcement, not just Mar 10 + Apr 7–8 double-confirmation.

### What stayed
- "Plumbing fragility — three structural buffers gone" remains the core frame.
- Three failure legs (Fed rate-control / FOI demand hole / basis trade) preserved as the structural setup. Re-labeled A / B / C and given current-transmission status, but the legs themselves are unchanged.
- Stagflation trap as structural finding.
- LIQ-01 (HY OAS 320 confirmation) preserved as the upside trigger.
- Kill condition logic on the macro side (Fed liquidity facilities, FOI resumption, ceasefire + oil) preserved.

### Drivers of the revision
1. **32-day gap (Apr 16 → May 18)** — exposed that LIQUID's primary channels can go dormant while the bear thesis continues firing through outside-domain channels.
2. **30Y broke 5% sustained** (May 5 = 5.046, first since 2007; 5/19 = 5.168 fresh life-high) — duration-channel transmission is real and current, not theoretical.
3. **APO co-trigger fired 5/12, missed for ~6 sessions** — exposed the operational risk of trigger-watch going dormant during agent staleness (new durable finding in §9).
4. **BOND agent scaffold created** (`AGENTS/BOND/`, May 2026) — formalizes the future migration of yield curve / market-structure scope out of LIQUID.
5. **Stage 3 PC narrative recognized** (Mar 25 inflection) + **FSK Q1 NAV -9.9%** (5/18) — moves Stage 3→4 transmission from "thesis projection" to "active watch."

### What this revision did NOT do
- Did not retire `STATUS.md`, `STRATEGY.md`, `MEMORY.md`, `KB.tsv`, or `KILL_MEMO_HY_OAS_260.md`. THESIS.md is the conceptual frame; operational layer untouched.
- Did not hand off any scope to BOND. BOND scaffold exists but is inactive; v2.0 names the interface but LIQUID retains all current active scope until BOND stands up.
- Did not change the position-level playbook in STRATEGY.md. Bilateral 320/260 framework was already there; v2.0 just elevates it from playbook-rule to thesis-doc.

---

## v1.0 — 2026-04-08
**Initial thesis document created.**
- Extracted core thesis from STATUS.md, CREDIT_THRESHOLDS.md, IDENTITY.md
- Triple failure point framework documented
- Transmission channels cataloged with current status
- Stagflation trap DOUBLE CONFIRMED (Mar 10 + Apr 7-8)
- Key thresholds and invalidation conditions defined
