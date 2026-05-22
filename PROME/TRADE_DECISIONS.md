# TRADE_DECISIONS.md
**Created:** 2026-05-08 21:10 ET  
**Owner:** Prome  
**Purpose:** Permanent record of Will’s trade/portfolio decisions, rationale, and outcomes.

This file is not a position snapshot and not a research file. It records decisions after they happen so Prome can learn from judgment patterns.

---

## Logging Rules

Log when:
- Will approves, rejects, modifies, or defers a trade/portfolio action.
- A non-action is itself meaningful, e.g. “no fresh premium after FSK Mixed.”
- A prior rule is overridden.
- A decision should be reviewed later.

Do not log:
- Every passing thought.
- Routine market observations.
- Research findings unless tied to a decision.

For current positions, use `PROME/POSITIONS.md`.  
For event branch frameworks, use event pre-builds and action cards.

---

## Entry Template

```md
## YYYY-MM-DD HH:MM ET — <Decision Title>

**Context:**  
What triggered the decision.

**References:**  
- Pre-build/action card/position snapshot paths.

**Options considered:**  
1. ...
2. ...
3. ...

**Recommendation:**  
Prome recommendation at the time.

**Will decision:** Approved / Rejected / Deferred / Modified  
Exact decision.

**Action taken:**  
What happened, if anything.

**Follow-up date / trigger:**  
When to reassess.

**Outcome:** Pending / Good / Bad / Mixed  
Fill later.

**Lesson:**  
Fill later if there is a reusable lesson.
```

---

## 2026-05-08 — Setup Notes

No trade decision logged here yet.

Architecture created:
- `PROME/DECISION_FLOW.md`
- `PROME/action-cards/FSK_MAY11_ACTION_CARD.md`

Relevant current context:
- `PROME/POSITIONS.md` refreshed from Will screenshots at 2026-05-08 14:17 ET.
- Private-credit option value is now small (~$445 / 1.0%); FSK May 11 mainly decides whether to deploy fresh capital, not whether to save a large existing APO/ARES book.
- Any FSK-related trade after the May 11 print should be logged below.

---

<!-- New decisions below this line -->

## 2026-05-22 ~15:00 ET — TLT Jun 18 $85P × 3: Trim 2 / Roll 1 to Sep 19 $85P

**Context:**
TLT $85P × 3 Jun 18 was +92% at 5/21 close ($83.56 spot). 5/22 intraday bounce to $84.51-54 ate most of the crystallized gain. Final 2 weeks of expiration approaches theta cliff. Decision packet routed to HENRY 5/22 for 4-question validation (split / strike / time trigger / conditional levels). HENRY teammate `a9200162cddd73274` replied verdict-first within ~5 min. Will discussed alternatives (0/3 hold-all) but acknowledged his bearish-bond read is general directional, not catalyst-specific — horizon-mismatch with 17-day Jun expiration. Accepted HENRY's 2/1 + Sep $85P as the horizon-matched expression.

**References:**
- `PROME/action-cards/TLT_JUN18_DECISION_2026-05-22.md` (full action card with execution ticket + conditional triggers)
- `AGENTS/HENRY/outbox/REPLY-PROME-2026-05-22-tlt-decision.md` (HENRY's verdicts)
- `AGENTS/HENRY/inbox/SIG-PROME-HENRY-2026-05-22_tlt-decision-and-vix-trigger-calibration.md` (original packet)
- `FORGE/STATUS.md` (5/21 19:30 ET position state)

**Options considered:**
1. **3/0 (sell all 3)** — naked on R11 vol-spike window 5/28-6/02; HENRY flagged as too aggressive
2. **2/1 trim + roll** — HENRY's pick; horizon-matched to "general directional, no catalyst" read
3. **1/2 (keep more thesis)** — middle-ground; Will declined
4. **0/3 (hold all)** — Will's initial lean; rejected after honest assessment of theta-cliff + horizon mismatch

**Recommendation:**
Prome recommended 2/1 + Sep 19 monthly $85P after HENRY validation. Walked Will through bond-bull evidence (5/20-21 clean auctions, breakeven decomp, HENRY softening R11 trigger #6), then strategic-vs-tactical horizon mismatch. Will agreed.

**Will decision:** ✅ **Approved 2026-05-22**
Execute 2/1 with Sep 19 (not Sep 30 quarterly) $85P. Two orders:
- Sell-to-close 3 × TLT Jun 18, 2026 $85P (limit at mid; expected ~$0.85-0.95)
- Buy-to-open 1 × TLT Sep 19, 2026 $85P (limit at mid; expected ~$2.80-3.20)
- Net debit expected ~flat to -$50

**Action taken:**
Pending Will execution at broker. Today PM (5/22) or Tuesday open (5/27) both acceptable; slight bias to today PM.

**Follow-up date / trigger:**
- Will reports fills → Prome updates FORGE/STATUS.md + action card status to Completed
- 6/06 EOD time backstop on remaining position (1 × Sep 19 + 2 × Sep 30 + 2 × Oct 16 $82P all rate-bear duration stack)
- C5 substance trigger (HY OAS ≥ 290 sustained OR R11 vol-spike 5/28-6/02): if fires before execution, reconsider sizing

**Outcome:** Pending

**Lesson:** Fill later — but provisional lesson already surfaced in conversation: **strategic directional reads need strategic-horizon vehicles; using tactical-horizon contracts (17 days) for strategic theses (multi-month structural pressure) is a vehicle-thesis mismatch that gets cured by rolling out, not by hoping the catalyst lands in window.** Worth saving to memory if Will agrees post-fill.
