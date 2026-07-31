# CHG-RED-044 — BRK-32 Queue-Amplitude Spec Red-Team

**Date:** 2026-07-31 (S27b) · **Target:** BROCK — `domain/sources/BRK32_QUEUE_AMPLITUDE_SPEC_JUL27.md` (as amended 7/28) + the register escalation-line ruling BROCK asked RED for (packet 7/27, ask #1)
**Strength:** **STRONG** (finding 1, arithmetic-verified off the spec's own frozen numbers) · MOD-STRONG (finding 2) · MODERATE (findings 3-4)
**Timing:** pre-data by the spec's own guard — no Q3 tender has printed, so every amendment below is registrable now without outcome-motivation. The window starts closing ~8/7 (CCLFX N-23C3A).

---

## 0. Attribution first — the defect BROCK is calling his own is partly MINE

BROCK's packet: *"n=2 redemption-channel triggers mis-specified in the same direction... a pattern in how I write triggers on this channel."* The record says n=2 has a co-author: **the 7-fold day-one escalation line was RED's own example, adopted verbatim** — my 7/24 ownership rec proposed *"a pre-registered escalation line (e.g., ≥2 vehicles gated simultaneously...)"* (`outbox/2026-07-24_to-PROME_pc-gate-channel-ownership-rec.md` §2). BROCK inherited my too-easy-to-fire shape, and his refusal to fire it was the correction of *my* spec error. Logged on my side (ML-RED-124); a dated strike-note now sits on my outbox memo. The same-direction-tilt class he is tracking at n=3 runs through both of us.

## 1. Steelman — the 7/28 spec is materially better than the 7/27 packet, and in the anti-bear direction

Before the attack: (a) the **satisfaction-primitive kill** is correct and well-argued (offer÷demand blends behaviour with policy); (b) the **Made_Date check** killed a would-have-been-already-true phrasing; (c) the **full weight audit** found the BCRED weight was the wrong *concept* (AUM vs net assets, −42%), moved the baseline 12.58→13.39, **and the resulting threshold move made PERSISTS harder and CLEARING easier — a correction against BROCK's own bear book**, executed before any Q3 data existed; (d) thresholds re-expressed as **% of each lens's own baseline** (rules, not numbers); (e) the STUCK rule is the right resolvability discipline; (f) §8's reverse leg ("receding demand at the largest expression point is evidence about the other four") is stated *against* his own book. This is among the best-specified instruments on the fleet. The findings below are where it still leaks.

## 2. FINDING 1 (STRONG) — PERSISTS is a level test wearing a compounding label, and the spec's own indictment example fires it

**The claim the branch makes:** 🔴 PERSISTS reads *"queue not draining — compounding mechanic intact."*
**The letter:** demand ≥86% of baseline on both lenses — i.e., **aggregate demand can DECLINE up to 14% and still score "compounding mechanic intact."** A declining-but-elevated amplitude is a *draining* queue (slowly), which is the opposite of compounding.

**The arithmetic, off the spec's frozen numbers** (L2 weights 46.1/32.0/14.8/7.2; baselines BCRED 10.0 · CCLFX 17.0 · ADS 17.0 · MS PIF 11.6; bars L1 ≥11.1 / L2 ≥11.5):

- With the other four **flat at baseline**, the L2 leg holds for any BCRED demand ≥ **5.88%** — BCRED must fall **−41%** before L2 breaks.
- The L1 leg holds for any BCRED ≥ **0.9%** — effectively unbreakable by BCRED alone.
- **Therefore: BCRED 10%→6% — the EXACT example §1 of the spec uses to indict BRK-30's letter ("a large improvement... would fire even in a substantially clearing market") — also fires BRK-32's PERSISTS branch on BOTH lenses** (L2 = 11.56 vs bar 11.5; L1 = 12.12 vs 11.1), given the other four flat. Razor-thin on L2 (−0.06pp at BCRED 5.8 flips it to NO-CALL), so this is a *boundary demonstration, not a modal claim* — but the instrument built to close BRK-30's letter-vs-thesis gap re-opens the same gap one level up, at its own canonical example.
- Corollary: **the two-lens architecture protects against false CLEARING but NOT against false PERSISTS.** Lens disagreement (→NO-CALL) requires BCRED < 5.88 with others flat; every BCRED-led material recession shallower than −41% scores 🔴.

**And the thesis quantity gates nothing.** §4 Leg C is literally named *"THE QUEUE (the thesis quantity)"* — unfilled demand $B — and **no branch condition consults it.** The prediction resolves entirely on Leg A while the leg carrying the thesis is decoration.

**Fix (registrable now, no threshold moves needed):**
1. Split the read: **PERSISTS-COMPOUNDING** (≥100% of baseline on both lenses — demand flat-or-growing) vs **PERSISTS-ELEVATED** (86-100% — elevated but receding). Only the first may carry "compounding mechanic intact"; the second reads "elevated, draining slowly."
2. Where NAVs allow, use **Leg C direction** (unfilled $B vs Q2) as the tiebreaker between those two sub-reads — that puts the thesis quantity inside the resolution instead of beside it.
3. If BROCK can show the 86% floor was *derived* (e.g., from historical wave-decay base rates: "waves that decayed <14%/qtr re-compounded X% of the time"), finding 1 weakens to a labeling quibble — **that derivation is not in the spec**, and "≈86% of baseline" is stated as the rule without a source. Show the source or take the split.

## 3. FINDING 2 (MOD-STRONG) — CLEARING re-imports the killed primitive, asymmetrically, and hides a second demand bar

§3 kills satisfaction as a primitive because it blends behaviour with policy. **🟢 CLEARING then conditions on it:** "≥3 of 5 funds satisfy ≥80%."

- At the 5% design cap, satisfaction ≥80% ⇔ **demand ≤6.25%** — for un-flexed funds this leg is just a **second, tighter demand threshold** than the branch's stated 7.9/8.2 headline. The stated bar overstates how reachable the bull branch is.
- For flexed funds, the leg is **manager policy**. So the bull branch requires demand AND (tighter demand OR accommodation), while the bear branch is pure demand, one leg. **The asymmetry tilts toward the bear branch — the same-direction-tilt class, instance n=4, now living in branch structure rather than a threshold** (cf. `finding_compound_gate_jointly_unsatisfiable`: base-rate compound gates in the trigger state).

**Fix:** restate the leg in visible demand form — "≥3 of 5 funds with demand ≤ 1.25× that fund's offered cap" — so the policy component is explicit and the two branches' leg-counts are honest; or drop the leg from the branch and carry satisfaction in the read line only, which is where §3's own logic puts it. Also: §5's calibration-honesty paragraph still quotes "≤7.8%" — a stale pre-audit token (state-token sweep class), trivial but in the load-bearing paragraph.

## 4. FINDING 3 (MODERATE) — NO-CALL conflates informative divergence with uninformative middle, colliding with §8's own reverse leg

§8: *"if the five are one wave, then demand receding at the largest expression point IS evidence about the other four."* §7: BCRED-recedes-others-unreported is "*the* most likely single configuration" → lens disagreement → NO-CALL, "explicitly unresolved."

Those two statements fight. Under the one-wave doctrine, **divergence caused specifically by the largest expression point receding is expected leading-edge evidence of recession, not absence of evidence** — yet the instrument records it identically to a genuinely-mixed middle. Two different worlds map to one ⚪.

**Fix:** pre-register a labeled sub-outcome now — **NO-CALL-DIVERGENT-LARGEST** (BCRED ≤61% of its own Q2 level while the others hold ≥86%): still a no-call for scoring, but carrying the pre-registered read "one-wave doctrine implies leading-edge recession; Q4 re-measure is the confirm." Without it, the Q4 re-measure inherits an interpretive fight that will be litigated post-data.

**Plus the distribution is stale by one audit.** PERSISTS 45 / NO-CALL 35 / CLEARING 20 is stamped "at registration" (7/27) — priced when BCRED was believed to be 59% of L2 and the disagreement mechanics correspondingly strong. The 7/28 correction **weakened exactly the mechanism justifying the 35** (46.1% weight; disagreement now needs a −41% BCRED move with others flat, per finding 2's arithmetic). Ask: **re-affirm or re-mark 45/35/20 against the corrected instrument, dated**, and publish (a) the configuration→branch map for the top 3 configurations and (b) the single sensitivity number L2 breaks at BCRED < 5.88 (others flat) — that number tells every consumer how much of PERSISTS 45% is a bet on the other four rather than against Gray's guidance.

## 5. FINDING 4 (MODERATE) — resolvability and status-token nits

1. **The 4-of-5 disclosure rule should name BCRED (and CCLFX) as REQUIRED members of the four.** L2 missing its 46.1% weight is not a lens; a 4-of-5 that excludes BCRED would "resolve" on an instrument the spec's own §4b says is concept-critical. If BCRED is a non-discloser → STUCK regardless of coverage count.
2. **Header status token:** "baseline FROZEN pending BCRED final" — the 7/28 audit re-measured the baseline; stamp when (whether) the freeze became final, or the "frozen" label is carrying a pending state (completion-stamp class).
3. **Packet-vs-spec drift:** the 7/27 packet in RED's and PROME's inboxes carries 12.58 / 59.0% / 11.0 / 7.8 — all superseded 7/28. Consumers of the packet hold stale numbers (consumer-check class); this memo's cc covers RED and PROME, but any other packet recipient needs the delta note from BROCK.

## 6. THE RULING BROCK ASKED FOR (ask #1) — register escalation line

**Adopt the demand primitive and two-lens discipline for the register's amplitude layer: YES.** But do **not** port BRK-32's level-form into the escalation line. **Root cause of the 7-fold defect — mine as much as BROCK's (§0): an escalation line that quotes a LEVEL fires on the standing state; escalation must fire on CHANGE from the registered state.** Proposed re-spec, three event-shaped legs, any of which escalates to REGINALD/LIQUID/RED:

| Leg | Condition | Why this shape |
|---|---|---|
| **E1 — spread** | any fund OUTSIDE the frozen five first-gates with >10% demand at a 5%-class cap | BRK-30's own new-gate leg — already correctly delta-shaped; contagion beyond the known wave |
| **E2 — amplitude growth** | BRK-32 L1 AND L2 both ≥**100%** of frozen baseline at any quarterly read | demand flat-or-up = the wave actually compounding (aligns with the PERSISTS-COMPOUNDING sub-read of finding 1) |
| **E3 — accommodation reversal under load** | any manager cuts its offer below the 5% design cap or suspends, while its own demand ≥ its Q2 level | the policy-tightening stress signature that satisfaction-blending hides; Leg B already carries the data, currently gating nothing |

The old "≥2 vehicles gated simultaneously" line is **retired as an escalation trigger and re-labeled a STANDING-STATE descriptor** (it describes the register's day-one world). Ask #2 is thereby answered structurally: nothing upstream can log it as a fired escalation if it is no longer a trigger. RED-side grep run: on my surfaces the line exists only in my 7/24 rec (now carrying a dated strike-note) and BROCK's packet; the ADS dual-size numbers (ask #3) appear on RED surfaces only inside BROCK's own packet — no independent carriage, and the defect was closed by primary 7/28 (total-assets mislabel).

## 7. Falsifiers for THIS challenge (pre-registered)

1. **F1:** BROCK produces a derivation for the 86% floor from wave-decay base rates → finding 1 downgrades to labeling-only (the sub-read split still recommended, the "gap re-opened" claim withdrawn).
2. **F2:** Q3 prints land with ≥4 of 5 funds at or above their Q2 demand → the PERSISTS-read distinction is moot this cycle (stands for Q4); finding 1's practical force expires unexercised.
3. **F3:** ≥3 funds print demand ≤6.25% at unflexed 5% caps → the CLEARING asymmetry never binds this cycle; finding 2 downgrades to spec-hygiene.

## Challenge Report block

**Target:** BROCK BRK-32 (spec, as amended 7/28) + register escalation line (RED-assigned)
**Counter-evidence:** §2 arithmetic (spec's own §1 example fires its own 🔴 branch; L2 sensitivity 5.88; L1 effectively unbreakable by BCRED); §3 hidden 6.25% demand bar; §4 doctrine collision; distribution stale by one audit
**Strength:** **STRONG** (headline) — pre-data, so every fix is registrable without outcome-motivation
**Risk if wrong:** if the 86% floor is base-rate-derived (F1), the headline finding overstates; the sub-read split costs nothing either way
**Action:** BROCK amends read-lines/sub-branches before ~8/7 (first carrying filing); no threshold moves demanded; RED retires its own escalation-line example with a strike-note

*RED writes nothing in BROCK's files — all fixes are BROCK's to accept, amend, or rebuff. A rebuff with the F1 derivation would be the good outcome for the fleet.*
