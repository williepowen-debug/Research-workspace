# TRADE_DECISIONS.md
**Created:** 2026-05-08 21:10 ET
**Owner:** Prome
**Purpose:** Permanent record of Will’s trade/portfolio decisions, rationale, and outcomes.

This file is not a position snapshot and not a research file. It records decisions after they happen so Prome can learn from judgment patterns.

**Important:** a logged approval is not the same as completed execution. Use the decision state field to distinguish `WILL_APPROVED`, `BROKER_PENDING`, `ORDER_PLACED`, `FILLED`, `POSITION_UPDATED`, `LOGGED`, and `COMPLETED`.

---

## Logging Rules

Log when:
- Will approves, rejects, modifies, or defers a trade/portfolio action.
- A decision changes operational state: approval → broker pending → placed → filled → position updated → completed.
- A non-action is itself meaningful, e.g. “no fresh premium after FSK Mixed.”
- A prior rule is overridden.
- A decision should be reviewed later.

Do not log:
- Every passing thought.
- Routine market observations.
- Research findings unless tied to a decision.

For current positions, use `PROME/POSITIONS.md`.
For event branch frameworks, use event pre-builds and action cards.
For trigger/default logic, use `PROME/EXECUTION_RAILS.md` and the action-card Execution Rail section.

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

**Decision state:** DRAFT / PROPOSED / WILL_APPROVED / BROKER_PENDING / ORDER_PLACED / FILLED / POSITION_UPDATED / LOGGED / COMPLETED / REJECTED / DEFERRED / EXPIRED / SUPERSEDED / CANCELLED
Exact operational state.

**Will decision:** Approved / Rejected / Deferred / Modified
Exact decision.

**Action taken:**
What happened, if anything.

**Next owner / verification needed:**
Who owns the next step; what proof closes the loop.

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

**Decision state:** `BROKER_PENDING` — Will approved; orders not yet placed/reported filled.

**Will decision:** ✅ **Approved 2026-05-22**
Execute 2/1 with Sep 19 (not Sep 30 quarterly) $85P. Two orders:
- Sell-to-close 3 × TLT Jun 18, 2026 $85P (limit at mid; expected ~$0.85-0.95)
- Buy-to-open 1 × TLT Sep 19, 2026 $85P (limit at mid; expected ~$2.80-3.20)
- Net debit expected ~flat to -$50

**Action taken:**
Pending Will execution at broker. Today PM (5/22) or Tuesday open (5/27) both acceptable; slight bias to today PM.

**Next owner / verification needed:**
Will owns broker execution. Prome needs fill prices or explicit Will confirmation, then updates `FORGE/STATUS.md`, this log, and the action card.

**Follow-up date / trigger:**
- Will reports fills → Prome updates FORGE/STATUS.md + action card status to Completed
- 6/06 EOD time backstop on remaining position (1 × Sep 19 + 2 × Sep 30 + 2 × Oct 16 $82P all rate-bear duration stack)
- C5 substance trigger (HY OAS ≥ 290 sustained OR R11 vol-spike 5/28-6/02): if fires before execution, reconsider sizing

**Outcome:** Pending

**Lesson:** Fill later — but provisional lesson already surfaced in conversation: **strategic directional reads need strategic-horizon vehicles; using tactical-horizon contracts (17 days) for strategic theses (multi-month structural pressure) is a vehicle-thesis mismatch that gets cured by rolling out, not by hoping the catalyst lands in window.** Worth saving to memory if Will agrees post-fill.

---

## 2026-05-26 ~17:00 ET — 6/18 Theta-Killer Cluster Trigger Set v0.2: Adopt as Live Execution Rail

**Context:**
6/18 expiry cluster has 5 theta-killer positions down ~87-94% (HYG ×8, EGBN ×1, WAL $65 ×1, WAL $67.5 ×2, KRE ×1) plus 3 dropped orphans (AAL Jun ×2, CF ×1, AAL Jul standalone). v0.1 was Will-authorized 5/22 with 3 calibration questions out to BROCK/REGINALD/HENRY. By 5/24 EOD: HENRY replied (TLT routed to its own card), BROCK + REGINALD silent. v0.2 default-pass applied 5/25 — pure pending-language-strip + default-pick lock. v0.2 entered Will-review state with approval packet `JUN18_V0.2_APPROVAL_PACKET_2026-05-25.md`. Earlier this session (5/26) Prome ran a pre-approval review pass — surfaced WAL Q2-print gap + AAL Jul 17 standalone scope-limit, refreshed stale 5/22 tape table to 5/26 16:10 ET, added two Next Candidate rows to ACTIVE_DECISIONS. Will then approved.

**References:**
- `PROME/action-cards/JUN18_V0.2_APPROVAL_PACKET_2026-05-25.md` (Will-decision artifact + Decision Log section)
- `PROME/action-cards/JUN18_EXPIRY_CLUSTER_2026.md` (wrapper action card, `WILL_APPROVED`)
- `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` (source trigger set, v0.2 `WILL_APPROVED`)
- `PROME/ACTIVE_DECISIONS.md` (live row state + Next Candidate rows for Q2-print + AAL Jul 17)
- `PROME/EXECUTION_RAILS.md` (canonical state-vocabulary spec)

**Options considered:**
1. **Adopt v0.2 clean as let-expire-default rail** (Prome recommended; chosen) — Q2-print exposure handled as separate decision around 6/13 EOD review or 6/16 backstop sweep
2. **Embed time-trigger in v0.2 for Q2-print fresh-open** — rejected; violates v0.2 "no new trigger IDs" discipline; conflates loss-management with fresh-position-opening
3. **Override A1/A5/A6 default-picks** — Will held with all three defaults

**Recommendation:**
Prome recommended (1). Three reasons: rail discipline (v0.2 scoped to loss-management at expiry, not new-exposure forward decisions), decision quality (fresh Sep $67.5P × N wants live marks/IV/sizing at decision time, not pre-approved embedding), cleaner approval contract.

**Decision state:** `WILL_APPROVED`
Live monitoring rail through 2026-06-16 16:00 ET hard backstop. No trade pending — daily monitor only.

**Will decision:** ✅ **Approved 2026-05-26 ~17:00 ET**
Adopt 6/18 trigger set as live execution rail v0.2 with A1 HYG no-pre-spec / A5 WAL $67.5P → Sep / A6 KRE → Aug 21 defaults as drafted. No regime trigger fires at approval time (R1 VIX 16.92 / R2 HY OAS 274 / R3 KRE $70.24 / R4 HY OAS 274 — all cushions equal or larger vs v0.2 ship). Position-specific levels also not firing (WAL $79.56 vs $73 trigger).

**Action taken:**
- `JUN18_EXPIRY_CLUSTER_2026.md` PROPOSED → `WILL_APPROVED`
- `JUN18_V0.2_APPROVAL_PACKET_2026-05-25.md` PROPOSED → `WILL_APPROVED` + Decision Log appended
- `FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md` v0.2 PROPOSED → v0.2 `WILL_APPROVED`
- `ACTIVE_DECISIONS.md` row updated to `WILL_APPROVED`; Next column = daily monitor + spawn-on-fire
- Two Next Candidate rows added (WAL Q2-print fresh-open; AAL Jul 17 orphan)
- This entry logged

**Next owner / verification needed:**
Prome owns daily dashboard scan of R1-R4 + position-specific levels through 6/16. Any trigger fire → spawn named domain agent (BROCK for credit, REGINALD for banks) → fresh Will approval for any roll. Will owns final-trade approval on every fire event.

**Follow-up date / trigger:**
- Any R1-R4 fire (single-trigger arms cluster review; double-trigger escalates to roll-default unless thesis contradicts)
- Position-specific trigger: WAL <$73 close / KRE <$63 close / EGBN <$26 / sub-90¢ BDC arms-length / bank PC loss disclosure
- **6/13 EOD review** — surface WAL Sep $67.5P × N fresh Q2-print exposure decision as its own action card (if not yet triggered by earlier fire)
- **2026-06-16 16:00 ET** — hard backstop sweep; untriggered theta-killer lines let-expire; surface AAL Jul 17 standalone as its own decision

**Outcome:** Live monitoring active. First proof-test for the pre-registered execution-rails pattern (closes BROCK LESSONS #16 execution-rails gap that killed the HYG Hamilton Jun→Dec roll in Apr dark window).

**Lesson:** Pending end-to-end through 6/18. Pattern-level finding to watch for: does pre-registered trigger discipline survive a real fire event vs. the "should I roll?" judgment-in-the-moment drift it's designed to prevent?
