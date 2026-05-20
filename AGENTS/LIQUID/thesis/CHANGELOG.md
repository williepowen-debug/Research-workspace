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

## POV Pivots (intra-version)

> Reverse-chronological log of significant LIQUID point-of-view shifts that didn't trigger a full thesis-doc revision. Captures the trajectory of reads that would otherwise be lost when STATUS.md is pruned of historical narrative. Each entry: prior view → revised view, with the trigger that forced the update and the durable anchor (KB entry / file) where the finding now lives.

### 2026-05-20 — Foreign-demand-canary refined
- **Prior view:** long-end break 5/13–5/19 (10Y 4.59, 30Y 5.12+ for 4 sessions, TLT fresh lows) was the foreign-buyer-exit canary firing; next leg would be auction-mechanism failure (BTC <2.50, indirect <55%, tail >2bps).
- **Revised view:** demand hole **compresses price** (term-premium digestion, expensive); it does **not break auction mechanism** under current conditions. Foreign demand shows up at the price the macro demands; term premium ratchets higher per absorption.
- **Trigger:** 5/20 20Y NEW issue ($16B, CUSIP 912810UV8) prints indirect 67.7% (strong), tail 0bp (stopped on screws), dealer 9.4% (clean) — under maximally-loaded macro (JPY 159+, Brent $111+, 30Y 5.12+ sustained).
- **Falsification standing:** tail >2bps confirmed by 2nd source would reverse. 5/21 10Y reopening Leg 2 is the corroboration test.
- **Anchored in:** KB-LIQ-057.

### 2026-05-19 — APO co-trigger watch went dormant during agent staleness
- **Prior view:** HEARTBEAT line 80 reassessment triggers (APO >$130 for 3 sessions OR HY OAS <260 sustained) were being watched; agent would notice if either fired.
- **Revised view:** Trigger-watch can go silently dormant during multi-session staleness. APO crossed >$130 on 5/8 and the co-trigger fired on 5/12 (Day 3). LIQUID was stale Apr 16 → May 18 (32 days); the trigger lived for ~6 sessions before live-tape re-verify caught it on 5/19. **Pattern:** on revival, don't trust the proxy's narrative summary alone — pull live values for every named threshold in HEARTBEAT line 80 and verify day-counts. A proxy synthesizing inbox items can cite "APO >$130" as macro context without computing the trigger ladder.
- **Trigger:** 5/19 live tape re-verification + APO 10-day yfinance pull showed Day 7 (now Day 9 as of 5/20).
- **Anchored in:** MEMORY.md Durable Findings; reinforced by 5/19 PM #1 session log.

### 2026-05-18 — Active transmission channel migrated PLUMBING → DURATION
- **Prior view (Apr 16):** SOFR-IORB +7bps breach was the next active channel; structural-vs-mechanical confirmation pending; plumbing dashboard yellow-flashing.
- **Revised view:** SOFR-IORB breach resolved mechanical (tax-day TGA build, not structural leak). The next leg fired through **10Y / TLT / Brent-reflation** instead. Bear thesis transmits through whichever channel is currently active; channel migration is normal, not thesis-abandonment.
- **Trigger:** 32-day gap revival showed 10Y 4.29 → 4.59 (+30bps), TLT $86.28 → $83.56, Brent $98 → $109, while SOFR normalized to 3.55% and SOFR-IORB re-flipped to -10bps.
- **Anchored in:** KB-LIQ-051 (SOFR resolved mechanical), KB-LIQ-052 (Duration regime break May 2026). Elevated to thesis-doc-level concept in v2.0 §1 + §4.

### 2026-04-16 — SOFR-IORB first cycle breach added as plumbing watch
- **Prior view (Apr 10):** Path A (squeeze resolution) winning. LIQ-01 at 290bps, 30bps below 320 trigger. Credit dashboard green. No active plumbing concern.
- **Revised view:** Plumbing dashboard yellow-flashing — SOFR 3.72 vs IORB 3.65 = +7bps positive (first cycle breach). Zero-RRP buffer thesis being tested in real time. Pending structural-vs-mechanical confirmation Apr 17-20.
- **Trigger:** Apr 15 SOFR print; 6-day swing of +11bps on SOFR (Apr 9 3.57 → Apr 15 3.72).
- **Resolution (May 18):** mechanical, not structural. Tax-day TGA build. KB-LIQ-051. The episode generated the now-durable pattern: 1-day SOFR-IORB sign flip on tax-day mechanics is NOT structural confirmation; apply same skepticism to quarter-end / settlement-window single-print breaches.

### 2026-04-10 — Path A (squeeze resolution) confirmation
- **Prior view (Mar/early-Apr):** HY OAS at 346 post-Q-end (Apr 1), bear thesis tracking the LIQ-01 confirmation path toward 320bps. Credit transmission active.
- **Revised view:** Path A (seasonal squeeze unwind) winning. HY OAS reverted 346 → 285 over 2 weeks. Credit/VIX divergence resolved. PC Stage 3 cascade public-equity sentiment decelerating (APO +15.9% over 6 days, BIZD +4.9%).
- **Trigger:** Apr 1 → Apr 10 tape; sustained HY OAS compression below 290.
- **Anchored in:** Durable Signals Log "HY OAS post-Q-end reversion" entry (preserved in KB.tsv lineage). Became the precondition that the *Apr 16 SOFR breach* read against.

---

## v1.0 — 2026-04-08
**Initial thesis document created.**
- Extracted core thesis from STATUS.md, CREDIT_THRESHOLDS.md, IDENTITY.md
- Triple failure point framework documented
- Transmission channels cataloged with current status
- Stagflation trap DOUBLE CONFIRMED (Mar 10 + Apr 7-8)
- Key thresholds and invalidation conditions defined
