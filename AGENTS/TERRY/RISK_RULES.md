# TERRY RISK RULES
**Created:** 2026-06-20

## Prime Directive

A trade is not valid until the loss is defined. A thesis can be right and the trade can still be wrong.

## Non-Negotiables

1. **Approval required:** Terry proposes; Will approves/rejects; no execution.
2. **Defined loss:** every trade card must state max loss budget and invalidation.
3. **No stale data:** live price/level pull required before actionable levels.
4. **No position assumptions:** existing holdings require broker/Will truth.
5. **No chase:** every plan has a do-not-chase level or condition.
6. **No roll-by-hope:** rolls must be pre-registered or explicitly re-approved.
7. **No expiry drift:** option trades need a time stop and catalyst map.
8. **No naked “because thesis”:** trade expression must fit timing, vol, liquidity, and risk/reward.

## Default Trade Quality Checklist

| Check | Pass condition |
|---|---|
| Thesis owner named | NEXUS/domain/Will source cited |
| Entry defined | Trigger + preferred zone + do-not-chase |
| Invalidation defined | Price/thesis/time invalidation named |
| Risk budget defined | Max loss in $/%/R; if unknown, ask Will |
| Reward defined | Target(s) and expected path |
| Time defined | Expiry/time stop/review cadence |
| Structure justified | Why shares/options/spread/ETF is the clean expression |
| Counter-case included | Best reason not to trade |
| Approval gate present | Explicit Will approve/reject line |

## Breaking root rule #6 (day colour) — the adjudication test

> ⚠️ **Naming collision, read this first.** **Root `CLAUDE.md` rule #6** = *"puts on green days, calls on red days."* That is **NOT** the same as **Non-Negotiable #6 above** (*no roll-by-hope*). The two lists are independent and both are cited by number. **This section governs the ROOT rule.** *(Root's numbers are a stable API — fire cards cite "rule #6" by number. Nothing here renumbers, deletes, or weakens anything; it is purely additive.)*

**Adopted 2026-07-27** off the first live break justified this way (`TRY-VIOLET-VIXCS`, filled). Promoted from a MEMORY finding to here **because MEMORY is not read at fire-time and this file is** — a discipline that only exists on a surface nobody opens under pressure is not a discipline.

**Root rule #6 is a PROXY.** It exists to answer exactly one question:

> **Am I paying up for convexity?**

Day colour is a cheap, fast stand-in for that question. It is not the question itself.

**THE TEST — a break is legitimate if and only if you can show the DIRECT MEASUREMENT that refutes the proxy.**

| Justification offered | Verdict |
|---|---|
| "Live chain shows the structure is **cheaper** than on the clean-colour day, and here are the numbers" | ✅ **Legitimate break.** Write it on the card with the figures. |
| "The window is closing / this is the last chance / the catalyst is tomorrow" | 🔴 **NOT a break. That is a CHASE.** |
| "The thesis owner says take it today" | 🔴 **Supporting consideration only — never the reason.** |
| "The tape looks exciting / it's finally moving" | 🔴 **That is price, not measurement.** |

**Two conditions that must ALSO hold, or the break is a rationalization:**

1. **No hard guard may be relaxed to make it fit.** Breaking the day-colour *preference* is not licence to loosen a *guard*. If you find yourself reinterpreting a stand-down — especially one written by another agent, especially on the trade you have just spent an hour arguing *for* — **stop.** Flag the defect to its owner and let it bind as written. *(7/27: the `VIX <20` guard was written on **spot** while the position settled on the **forward**, 19.6 vs 19.85. Reinterpreting it was available and would have been convenient. Flagged, not exploited.)*
2. **The reason must be written on the card, in the figures, before the fill** — not reconstructed afterwards. *(7/27, the worked example: colour said expensive at VIX +6.4% on a flat tape; the chain said the spread marked **$0.68–0.76 vs Friday's $0.84**, with worst-case fill improving **$1.85 → $0.83** as leg widths collapsed **85–160% → 16.7%/19.2%**. Friday's "cheap" mark was fictional — unfillable. The proxy said expensive; the thing being measured said the opposite.)*

**Corollary — the failure mode this prevents.** Every bad break sounds like a good one at the time, because urgency and opportunity feel identical from the inside. The test works precisely because *"show me the number that refutes the proxy"* is something a chase **cannot** produce. If no such number exists, the honest answer is a clean NO — and a clean NO is a good outcome, not a failure to find a way.

✅ **Status: RATIFIED BY WILL 2026-07-27** (in-session, same day it was adopted). **This test now GOVERNS every future break of root rule #6, fleet-wide** — TERRY when constructing, PROME when building proposals, and any agent proposing a break in a packet. A break offered without the refuting measurement is not a break to be argued about; it is a chase to be declined.

*Ratification recorded by PROME on Will's instruction. TERRY remains canonical owner of the rule and of this section — the substance, wording and worked examples above are TERRY's and were ratified as written; PROME changed only this status line. Additive to the numbered list, which is unchanged (stable API preserved).*

---

## Option-Specific Rules

- Do not recommend an option without checking or caveating: bid/ask width, IV/skew, open interest/liquidity, theta/day, event date vs expiry, expected move.
- Prefer spreads when outright IV/theta makes the thesis path too expensive.
- Match expiry to catalyst + confirmation lag; avoid buying too little time for slow-moving credit theses.
- If the trade needs a roll to work, the roll rule must be part of the original plan.

## Durable findings — EMBEDDED FROM AUTO-MEMORY 2026-08-04

*Phase-2 three-tier memory restructure (Will-approved 7/28; PROME embed packet 7/31). These 13 rows no longer auto-load at boot — **they live here because this is the file that gets opened under pressure and `MEMORY.md` is not.** Same reason the root-rule-#6 break test was promoted here on 7/27. `[[slug]]` links point at the memory files, which are unchanged.*

### Capital & deployment

1. **Deploy on a fired trigger, never on the calendar.** Will deploys fresh capital **only** on a fired trigger — never on mechanical book-maintenance. Funds are limited; **preserving dry powder is a position.** `[[feedback_deploy_on_trigger_not_calendar]]`
2. **A cooldown gate is not uniform — MAIN arm vs HEDGE.** A vol/cooldown gate blocks fresh **main-arm** capital (paying vega on a new directional bet). It does **not** automatically block a small **pre-approved, defined-risk hedge** with fixed max loss. Different economics, different gate applicability — say which one you are applying. `[[finding_cooldown_gate_differential_main_vs_hedge]]`
3. **Two-stage fill approval.** Will **[Approve in principle]** unblocks TERRY's live re-mark work; the final Will **[Approve]** on the one-line ticket is the actual execute authorization. Preserves rule #5 at lower Will-attention cost per stage. **Stage one is never permission to fill.** `[[finding_fill_in_principle_vs_final_approve_pattern]]`

### Marks, basis & position truth

4. **Position cost-basis and P/L from a state file are NOT authoritative.** Confirm with Will. Recorded fills can be wrong and have failed to reconcile. `[[feedback_position_cost_basis_not_authoritative]]`
5. **Option marks carried forward in state files go phantom.** Pull the **live chain** (last/bid/ask) at every decision point and sanity-check against moneyness and DTE. This is Non-Negotiable #3 with a named failure mode. `[[finding_option_marks_need_live_chain]]`
6. **Grade execution only against SAME-TIMESTAMP marks.** Comparing a fill to marks pulled at a different time in a moving market **manufactures a fake execution finding.** Establish the fill timestamp **first**, then compare like with like. *(This rule exists because I published a behavioural conclusion about my own limit-setting, n=2, built entirely on a 21-minute timestamp gap. n was actually 0.)* `[[finding_grade_execution_only_against_same_timestamp_marks]]`

6b. **⏰ NEVER HAND-WRITE A CLOCK TIME OR A WEEKDAY — READ IT.** Copy it from `date` (the boot card prints it first, every session). **A time you infer is wrong by tens of minutes and reads as measured.** *(2026-08-04: hand-written prose stamps ran **+66 to +69 minutes fast** across TERRY's card headers, `INDEX.md`, `SETUPS.tsv` **and** BRENT's ruling packets simultaneously. Git commit times were correct throughout — only the prose was wrong, so nothing flagged it.)* 🔴 **This is rule 6's supply chain, not a separate concern:** rule 6 grades against same-timestamp marks, and a **69-minute** systematic skew is **3× the 21-minute gap that produced the fake n=2 finding above.** Two artifacts stamped "12:20" and "12:55" were in fact written **37 minutes apart** — reconstruct sequence from those stamps and you get both the order and the spacing wrong. ⚠️ **A grade also decays faster than it gets written up:** the USO leg-(b) debit moved **26.0% → 31.0% in 37 minutes** the same afternoon, so a stamp error of ~1h can exceed the entire life of the number it labels. **Enforcement:** `ledger_sweep.py` **check E** flags any stamp claiming a time that has not happened yet (a future timestamp is *never* legitimate — no threshold, no judgement call). ⚠️ **It is a backstop, not the fix — it can only see a future stamp while that time is still in the future.** The fix is reading the clock.

### Structure & vehicle selection

7. **Match the vehicle to the OPEN transmission channel.** In a regime-suppressed tape (low VIX, tight spreads, gamma damping), single-name equity puts **bleed even when the thesis validates on substance.** A duration expression of the same view (TLT puts when the long-rate channel is open) **compounds** instead. `[[feedback_put_vs_duration_expression]]`
8. **The variance-risk-premium collapse is NOT uniform — long-put tails split by asset class.** Rates (TLT) pay the **full** vol tax; single names (HBAN) are structurally **cheap except into earnings**. Use when pricing or justifying any long-premium tail. `[[finding_vrp_split_rates_vs_singlename]]`

### Management & exits

9. **★ Every profit zone needs its own harvest rule.** Management triggers keyed to the move going **further** leave **no rule that fires when the position is merely profitable.** Add a **P/L-keyed harvest** — and check the trigger variable is one the **profit zone actually reaches.** *(This is `NO_HARVEST_RULE`, Will-ruled fleet-wide 7/31. It is the root cause of the desk's only realized loss: −$111.60 on `TRY-VIOLET-VIXCS`, where every §6 trigger was keyed to spot going further and none to being in profit.)* `[[finding_profit_zone_needs_its_own_harvest_rule]]`
10. **Surface the MARK before recommending a cleanup exit.** When recommending cleanup of near-dated theta-killers, state the execution mark first (vol regime, IV percentile, spot vs recent range). **At an unfavourable mark, propose a pre-registered window-trigger with backstop dates — not a mechanical close-now.** `[[feedback_exit_recommendations_need_mark_context]]`
11. **A collapsed conditional leg means the stop is DISARMED — that is a risk-control gap, not a sizing question.** When a hard trigger's conditional leg goes permanently true/false after a binary event (e.g. an AND-condition leg collapses post-BOJ), the stop is **functionally disarmed** and needs immediate re-spec. ⚠️ **"No sizing recommendation yet" must never quietly mean "ride unprotected."** *(Will, 2026-06-18, on SAM's post-BOJ AND-stop collapse — he distinguished the two explicitly.)* `[[finding_risk_control_separate_from_sizing]]`
12. **A fired kill-switch is held, not re-litigated.** When a pre-registered kill-switch fires against a framework that was paying: **hold the verdict**, log the counterfactual cost as a **datum on the switch**, and queue refinements for the next calibration pass. **Never retro-apply.** `[[finding_registered_killswitch_cost_datum]]`

### Ledger hygiene

13. **Demote a dormant ledger by verification, not by assumption.** Before freezing an agent ledger: verify **live consumers** and **cross-agent counterparties** first; triage by **Group, not ID-range**; use `UNVERIFIED-RETIRED` for LLM-sourced rows; and **re-verify your correction's own provenance.** `[[finding_workbook_demote_by_verification]]`

### Gates & grading cadence

14. **★ SEPARATE A STRUCTURE PROPERTY FROM A MOMENT PROPERTY, AND GRADE EACH ON ITS OWN CLOCK.**

    | | Examples | When to grade |
    |---|---|---|
    | **Structure property** — a fact about the trade | strike exists in the expiry · two-sided quotes / OI · quote sanity (no `LOCK`/`XSD`/`DEAD`/`NOBID`) · moneyness band · tenor in spec · max loss | **any time.** Stable. |
    | **Moment property** — a fact about *now* | net debit · debit as % of width · IV · spread% · mark · R:R at the current price | **ONCE, at fire.** |

    **On a multi-leg `AND` gate whose legs resolve at different times, the early leg is assessed for READINESS before fire, and its VALUE is graded once — at the moment the last leg resolves.** A moment-property grade published before the gate can fire has **no decision content** (nothing can be actioned either way) and **real cost** (it lands on N surfaces × M revisions and manufactures drift).

    🔴 **The incident, 2026-08-04.** `TRY-BRENT-USOARM` leg (b) — net debit ≤33.0% of width — was graded **five times in one morning by three agents** while leg (a) could not resolve until the 16:15 close: **27.0 → 34.0 → 38.0 → 26.0 → 31.0**, i.e. **three FAILs and two PASSes on the same structure.** ★ **Had anyone acted on PROME's 11:38 read of `38.0% FAIL and worsening`, the arm would have been stood down on a number that was `26.0%` forty-six minutes later.** Nothing was mis-measured — every grade was correct *at its timestamp*. **The defect was treating a moment property as though it were a property of the trade.**

    **Corollaries:**
    - **A moment-property number is never quoted without its timestamp.** "Leg (b) = 26.0%" is not a fact about the trade; "26.0% on the 12:24 chain" is.
    - **Do not chase it.** If the number moves after you have recorded it, that is the number behaving normally — **re-writing the card to the newest print is the very behaviour that caused the drift.**
    - **A gate spec that tests a moment property must name its measurement moment** (this one does: *"live chain **at fill**"*). If it does not, that is a spec defect to route to its owner, not to resolve by picking a moment.
    - **Empirical half-life at this desk: ~40 minutes.** Leg (b) moved **5.0pp in 37 minutes** on 8/4. Budget accordingly — and see 6b, because a stamp error of ~1h can exceed a figure's entire useful life.

15. **⚠️ A GATE THAT OPENS ON VOL/PRICE DECAY CARRIES *ZERO* THESIS INFORMATION — AND WILL FEEL LIKE CONFIRMATION.** When an entry gate's trigger variable is *"the market has priced less of our thesis"* (vol decayed from peak, premium cheapened), the gate opens **precisely as conviction drains**, by construction. That is a legitimate and deliberate fade-the-consensus design — **but "the gate fired" is then, mechanically, a measure of the market disagreeing with the thesis owner more than it did yesterday.** ⛔ **Never let a gate firing be read as evidence the thesis is working, and say so on the card before it fires** — the pull to read it that way arrives exactly when capital is about to move. *(8/4: USO leg (a)'s cushion widened 2.5% → 7.3% on the same morning BRENT cut his own dip confidence 88% → 85%. Those two move together by construction; one is not corroboration of the other.)*

---

## Postmortem Tags

Use these in `POSTMORTEMS.md`:
- `THESIS_WRONG`
- `THESIS_RIGHT_BAD_TIMING`
- `BAD_STRUCTURE`
- `OVERSIZED`
- `NO_INVALIDATION`
- `ROLL_RULE_MISSING`
- `STALE_DATA`
- `EVENT_MISALIGNED`
- `GOOD_PROCESS_BAD_OUTCOME`
