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

### ⏳ One break is OPEN-BY-DESIGN and must not be read as a standing pass — `USO Oct-16 135C`, 2026-08-21
*(Recorded here 2026-08-23 from BRENT's 8/21 ruling packet. **Will deliberately did NOT rule the root-rule-#6 break** — and the non-ruling is itself the decision: the break only bites if a fill is on the table, and once the roll was ruled HOLD, none was. Ruling it would have spent an operator decision on a question the roll decision dissolves.)*

**The test stood as written and was MET** — figures on the card, before any fill, no hard guard relaxed. **The measurement argued the same way:** honest day-colour cost was **~$21 / 2.8%** — vega **+18.58/pt into OVX 50.62 (+1.97%)** — **not** the `$1.99` the delta leg alone implies. **Worth ~$21. Noise.**

⛔ **STATUS: OPEN-BY-DESIGN. If a same-strike calendar roll is proposed again, RE-MEASURE the day-colour cost on THAT day's tape. The 8/21 figures are NOT a standing pass** — they are a `MOMENT` property (#14) and they expired with the session that produced them. ⚠️ **A met-but-unruled break is the easiest thing in this file to mistake for a granted one.**

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

6c. **📏 A FUTURES DAILY BAR IS A QUOTE, NOT A "CLOSE" — fleet rule N5, Will-ratified 2026-08-11, consumed 2026-08-13.** Five clauses, cited not restated (full text + attributions → WALTER `SIG-W-20260811-002`, filed `inbox/WALTER/processed/`): never write a futures daily bar as a "close" without a settlement source or a pull stamp, dime precision · a current-session bar is PROVISIONAL until a T+1 re-pull · refuse a same-day-labelled bar pulled past 18:00 ET · an ETF proxy close is the discriminator · a thin-book mid discharges by DEPTH, never by elapsed time. **This is 6b's price-side sibling: 6b polices the clock you stamp, N5 polices the price you stamp.** Scope: futures bars and thin-book mids ONLY — cash indices, ETF closes and official prints are exempt, and over-applying it is its own defect (WALTER's words, kept). This desk's exposure is low (mostly ETF chains + cash indices) — the bind is any card or gate citing a `CL=F`/`BZ=F`-class level, e.g. a BRENT-gated arm. *(Delivery note: sent as a declared WALTER OVERRIDE — its own T-1/T-2/T-3 tests all fail. TERRY grades the override CORRECT to send: a method rule is in the un-re-pullable class, which is the exemption's own rationale. n=1 against the ≤10% ratio; no gate widened.)*

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

    🔴 **The incident, 2026-08-04.** `TRY-BRENT-USOARM` leg (b) — net debit ≤33.0% of width — was graded **five times in one morning by three agents** while leg (a) could not resolve until the ~~16:15~~ **16:00** close: **27.0 → 34.0 → 38.0 → 26.0 → 31.0**, i.e. **two FAILs and three PASSes on the same structure** *(against the ≤33.0 line: 27.0 PASS · 34.0 FAIL · 38.0 FAIL · 26.0 PASS · 31.0 PASS).* ⚠️ **CORRECTED 2026-08-07** — this read *"three FAILs and two PASSes"* from the day it was written until a **Will-directed review caught it 8/6** by doing the arithmetic nobody else had. **The values were always right; the tally was always wrong**, and it sat inside the rule about grading discipline. ★ **The rule's force is unchanged and arguably sharper: the sequence still flips verdict THREE times, and the point was never the ratio — it was that every grade was correct at its timestamp and not one was actionable.** *(BRENT's 8/5 paraphrase — "graded 5× with **four verdicts**" — inherited the same confusion and is impossible on its own terms: a PASS/FAIL test has exactly two verdicts. Correction routed to BRENT.)* ★ **Had anyone acted on PROME's 11:38 read of `38.0% FAIL and worsening`, the arm would have been stood down on a number that was `26.0%` forty-six minutes later.** Nothing was mis-measured — every grade was correct *at its timestamp*. **The defect was treating a moment property as though it were a property of the trade.**

    **Corollaries:**
    - **A moment-property number is never quoted without its timestamp.** "Leg (b) = 26.0%" is not a fact about the trade; "26.0% on the 12:24 chain" is.
    - **Do not chase it.** If the number moves after you have recorded it, that is the number behaving normally — **re-writing the card to the newest print is the very behaviour that caused the drift.**
    - **A gate spec that tests a moment property must name its measurement moment** (this one does: *"live chain **at fill**"*). If it does not, that is a spec defect to route to its owner, not to resolve by picking a moment.
    - **Empirical half-life at this desk: ~40 minutes.** Leg (b) moved **5.0pp in 37 minutes** on 8/4. Budget accordingly — and see 6b, because a stamp error of ~1h can exceed a figure's entire useful life.

15. **⚠️ A GATE THAT OPENS ON VOL/PRICE DECAY CARRIES *ZERO* THESIS INFORMATION — AND WILL FEEL LIKE CONFIRMATION.** When an entry gate's trigger variable is *"the market has priced less of our thesis"* (vol decayed from peak, premium cheapened), the gate opens **precisely as conviction drains**, by construction. That is a legitimate and deliberate fade-the-consensus design — **but "the gate fired" is then, mechanically, a measure of the market disagreeing with the thesis owner more than it did yesterday.** ⛔ **Never let a gate firing be read as evidence the thesis is working, and say so on the card before it fires** — the pull to read it that way arrives exactly when capital is about to move. *(8/4: USO leg (a)'s cushion widened 2.5% → 7.3% on the same morning BRENT cut his own dip confidence 88% → 85%. Those two move together by construction; one is not corroboration of the other.)*

16. **★ MATCH THE EXPIRY TO THE VIEW'S HORIZON. A STRUCTURAL VIEW IN A SAME-DAY INSTRUMENT IS A DIFFERENT TRADE, AND A FAR WORSE ONE.** In 0–1 DTE options **being early is being wrong** — the instrument makes *timing* the entire trade, so a thesis about the next three weeks cannot survive inside it no matter how right it eventually is. **Before choosing tenor, say out loud how long the view needs to work; if the expiry is shorter than that, the expression is wrong even when the view is right.**

    🔴 **The worked example, and it is this desk's most expensive lesson to date.** The same QQQ view existed in the book twice in July–August 2026:

    | Expression | Max loss | Outcome |
    |---|---|---|
    | `TRY-WILL-QQQ-VFADE` — **Aug-21** put spread, defined risk, kill line pre-registered at 712 | **$452** | **never fired — $0** |
    | 11 tickets at **0–1 DTE**, undefined frequency | uncapped by count | **≈ −$4,341** |

    **The swing card would ALSO have lost** — it died on its own 712 invalidation. **It would have lost $452 on a level named in advance. Same view, same wrongness, 9.6× the cost, entirely from tenor and frequency.** The correct expression was built and sitting unfired while the incorrect one ran eleven times. → `POSTMORTEMS.md` 2026-08-04.

    **Corollary — ⛔ A CONTROL THAT HAS NEVER FIRED NEEDS ITS *FORM* CHANGED, NOT ITS WORDING.** That cluster's hard stop was specified in **four consecutive reviews and executed zero times**, re-written each time instead of re-shaped. **Count the executions, not the specifications.** At zero, replace the manual act with something that executes itself — a resting order, or a structure whose max loss *is* the premium. *(This is the same failure as `NO_HARVEST_RULE` #9, pointed at the loss side: a management spec that only works if someone overrides conviction in the moment does not work.)*

17. **★ THE SIZE-INCREASING BRANCH CARRIES THE HIGHER EVIDENTIAL BURDEN — fleet rule N4, Will-ratified 2026-08-11, consumed 2026-08-13 (PROME forum-4 close packet).** In a claim class whose **sole consumer is a size decision**, the branch that INCREASES size must clear a higher bar than the branch that DECREASES it — **and the spec must show the asymmetry in its own numbers**, not assert it in prose. *(The worked instance is the reason the rule exists: BRENT's crude "FUEL SPENT" fuller-size branch rested on an OI-normalized margin of **477–483 contracts (~5% of a median week), not the 1,512 its label implied** — 68% of the clearance was a denominator artifact — at the **67th percentile** of short-crowding, base rates **1.9:1 against** the claim surviving. Consumption details incl. 35a non-latching revert + 35b band death after its final 8/14 grade → `SIGNALS.tsv` row `FORUM4-35AB-FUELSPENT`.)*

18. **★ A PRINT NEVER JUSTIFIES A DEEP-OTM STRIKE — MATCH THE STRIKE TO THE EVENT'S REALIZED ENVELOPE, OR TAKE THE TENOR PAST THE PRINT.** *(Promoted from `options/IV_CRUSH_PARTB_2026-08-13.md`, Will-approved 2026-08-13 — the `options/` pipeline's first promotion to a numbered rule.)* Measured, not asserted: regional-bank singles (WAL/OZK/HBAN/ZION), 32 prints Oct-24→Jul-26 — realized 1-day reaction-session moves run **median ~2–3%, max 9.7%, 0 of 32 ≥10%**, while the July book held **12.7–15.5% OTM** strikes through prints. **A single ordinary print cannot reach a >10%-OTM strike on these names.**

    - **(a)** A strike **>10% OTM may not cite an upcoming print as its catalyst** — the print cannot pay it. Its real catalyst is multi-quarter transmission, so its tenor must span quarters (#16's horizon test, now with the event's measured size).
    - **(b)** If the print IS the intended catalyst, the strike belongs **inside the realized envelope** (median 2–3%, p95 ≲9%) — and there the crush tax is real (Part A: the event premium concentrates **+10–16 vol pts in front-month deep-OTM strikes**), so prefer a **spread that SELLS the rich deep wing** rather than paying it.
    - **(c)** Size a print-spanning long option against its **post-print mark**, not its pre-print hope.
    - ⚠️ **Regime-conditional, and the rule says so:** the sample contains no crisis print — Mar-2023-class gaps (SVB/FRC; WAL ~−47% intraday 3/13/23) exceeded this envelope. Holding a deep strike through a print is a bet that **the regime break lands ON the scheduled date**; if that is genuinely the trade, write it on the card as that bet, in those words, and size it as a tail-timing lottery.
    - **Scope:** the numbers are name-class-specific (regional-bank singles). Before applying the 10% line to another sector, **re-measure the envelope** — the tool is re-runnable (`options/partb_realized_moves.py`).

    **First consumers:** `TRY-FIRE-002` and `TRY-FIRE-003` (PRINT-class, staged) at build time.

19. **★ A SERIES-DERIVED EXTREME, STREAK OR "HAS X EVER HAPPENED" CLAIM MUST STATE ITS BAR COUNT.** *(Will-approved 2026-08-18. Born from WALTER `SIG-W-20260813-002` + this desk's own reproduction the same day.)* **Coverage is a property of the PULL, not of the instrument, and it varies between two identical calls.**

    🔴 **The measurement, on this box:** two identical `price_history()` calls **seconds apart** returned `^TNX` with **18 bars, then 60** (`IEF`: 59, then 60) for the same 60-day request. ⚠️ **The short pull contains ZERO nulls — the bars are simply ABSENT — so a `close is None` test is blind to it BY CONSTRUCTION.** WALTER's original finding was the *nullity* variant; **absence is the same defect with the detector removed.**

    **Why it is a trading rule and not an infra note:** every stat downstream is an **extreme** or a **window mean**, and a hole corrupts both *silently* — `max`/`min` exclude the extreme, a range-location verdict inherits the wrong range, and an "N-day MA" spans more calendar days than its label. **Concretely: the full 60-bar 10Y series has min `4.37`; the truncated 18-bar window has min `4.60`. `TRY-FIRE-004`'s disarm is a 10Y close `<4.50`** — the short series answers *"has it been below 4.50?"* with a confident **NO**.

    - **(a)** Quote the bar count beside any extreme/streak/percentile: *"11th percentile **of a 120-day window**"*, never a bare percentile.
    - **(b)** ⭐ **THE BATCH IS ITS OWN CONTROL.** Comparing bar counts **across tickers in the same pull** needs **no holiday calendar and no per-symbol expectation** — it catches "one symbol came back short" directly. An absolute floor backstops single-ticker pulls.
    - **(c)** **A short/holed series gets its derived verdicts SUPPRESSED, never interpolated.** An unmarkable series is reported UNMARKED. *(Implemented: `snapshot.py` `coverage_flags()`; regression suite `scripts/test_snapshot_coverage.py`, 12 synthetic-defect assertions including the 18→60 reproduction and a false-positive guard.)*
    - **(d)** **Print coverage on EVERY run, not only on defect** — a check that speaks only on failure teaches the reader to read silence as health.
    - ⚠️ **Cross-window percentiles are NOT like-for-like.** Comparing your 120-day percentile to someone else's differently-windowed one is a basis error; state both windows or compare **levels** instead.

20. **★ THE ENTRY HALF OF A TRADE CARD IS UNRECOVERABLE AFTER THE FILL; THE MANAGEMENT HALF NEVER WAS. A RETROACTIVE WRITE-UP IS MANAGEMENT-ONLY, AND SAYS SO ON ITS FACE.** *(Will-approved 2026-08-18. Forced by `USO $135C Oct-16 ×2` — $1,421.33 basis, in the book on no rail, no card, no owner agent; fill date and price **unobtainable from a positions view**, `FORGE` D-19.)*

    | Card section | After the fill |
    |---|---|
    | preconditions · entry/trigger/do-not-chase · structure rationale | 🔴 **UNRECOVERABLE — do NOT reconstruct.** Writing them retroactively **fabricates a decision record for a decision nobody made.** |
    | risk · target/management · time stop · roll rule | ✅ **NOT retroactive at all — purely forward-looking, and usually ABSENT.** |

    - **(a)** **"Recorded, unowned" is NOT an acceptable terminal state for an option leg.** An option with live theta and no management rule is an **unmanaged decaying asset** — `RISK_RULES` #9 is violated on its face, and it is violated *quietly* while the leg is underwater, which is exactly when nobody looks.
    - **(b)** **Management does not need the entry price.** Max loss from here is the **remaining mark**, whatever was paid. ⚠️ **Do not let a missing fill price block writing the exit** — that is the trap this rule exists to break.
    - **(c)** **Leave the entry fields explicitly marked UNRECOVERABLE, not blank.** *Blank reads as "unrecorded" (someone should go find it); the truth is "unrecoverable" (nobody can).* Mark `[POSITION_STATE_INCOMPLETE]` with the reason.
    - **(d)** Sunk basis is **not** forward risk: state forward max loss as the **remaining mark**, never the original debit. *(8/18: the oil sleeve's three option legs carried `$2,176.68` of sunk basis but only `$1,489.00` of forward exposure.)*

21. **★ A TENOR BAND IS AN *ENTRY-ECONOMICS* TEST, SO IT GOVERNS NEW DEPLOYMENTS AND NOT ROLLS — AND "ROLL" MUST BE DEFINED NARROWLY OR THE BAND DIES BY RELABELLING.** *(Will-ruled 2026-08-21 ~16:3x ET on the `USO Oct-16 135C` pair; recorded by BRENT at `AGENTS/BRENT/TRADE.md § BINDING WILL RULINGS` and on his roll card. **Mirrored here 2026-08-23 at BRENT's explicit ask — the `RISK_RULES` mirror is TERRY's to write; BRENT correctly did not edit this file.** This is a **SCOPE ruling, not an exception** — it says what the band was always about, and it therefore applies to every tenor band on this desk, not just the USO one.)*

    **The ruling:** the **`60–90 DTE`** band governs **NEW STRUCTURAL DEPLOYMENTS.** It does **NOT** govern the **roll of an existing leg.**

    **Why scope and not exception:** the band exists so that a shorter-dated vertical cannot make **leg (b)** — the net-debit-as-%-of-width test — easier to satisfy. That is an **ENTRY-economics** test. **A roll is never leg-(b) gated**, so read for the purpose it was written for, the band was never about rolls at all. *(Precedent for scoping a tenor rule this way is this desk's own: #16's horizon test already distinguishes a structural horizon from an off-ramp one.)*

    ⛔⛔ **THE GUARD IS BINDING AND TRAVELS WITH THE RULE — a scope ruling is broader than an exception, so it needs a tighter definition, not a looser one:**
    > **"ROLL" = SAME underlying · SAME strike · LATER expiry. NOTHING ELSE.**
    > **ANY change of STRIKE or STRUCTURE is a NEW DEPLOYMENT and the tenor band BINDS IN FULL.**

    ⚠️ **Without that guard a genuine new deployment arrives wearing a roll's clothes and the only economic gate on the trade is gone by relabelling.** A "roll" that moves the strike is a **close plus an open**, and the open is gated.

    - **(a)** **Say which you are doing, in those words, before pricing it.** If the answer needs a paragraph, it is a new deployment.
    - **(b)** **The scope exemption is not a recommendation to roll.** A roll pays new capital to keep the same view for longer; it is still subject to **root rule #7** (roll duration, don't trim size) and to the horizon test in #16. *(8/21 worked case: the counter-argument for acting was theta — the leg was ~ATM, 100% extrinsic, decaying ~`$19.61`/day and accelerating. **That argues for CLOSING, never for rolling** — rolling would have paid `$750` to keep the same problem for longer, while the same session's SELL-ONE was a de-risk. **Two decisions pointing in opposite directions is itself the tell.**)*
    - **(c)** **A roll of a filled leg is still a Will-gated proposal.** Scope-exempt from the band ≠ pre-approved. `$0` moves without [Approve].

22. **★ A CONTINUOUS FRONT-MONTH TICKER (`XX=F`) IS SAFE FOR A LEVEL AND UNSAFE FOR A DELTA. NAME THE CONTRACT, OR STATE THE BASIS AND CHECK THE ROLL.** *(BRENT → TERRY 2026-08-20; adopted here 2026-08-23. **I am a first-party casualty: I quoted a `$99.14` diesel crack off exactly this method.** BRENT's own rule ID is `L23`; this is the TERRY mirror.)*

    **`=F` tickers ROLL.** When they do, the symbol silently stops meaning one contract and starts meaning the next — **so a difference taken across the roll measures the CALENDAR SPREAD, not the market.** ⛔ **The print is not wrong. It is an answer to a different question, and nothing in the output says so.**

    🔴 **The worked case, and the scale of it is the point.** On 2026-08-20 `CL`, `HO` and `RB` all rolled in the same session. The rolling-front method printed a **gasoline crack of −$10.71** — read across the fleet as a collapse in refining margin. **Nothing sold off:** `RBU26` closed **+1.4c**, `RBV26` **+3.5c**, `HOU26` **+3.2c**, `CLU26` **+$2.32** — every contract UP on the day. The Sep−Oct RBOB spread was **25.7c/gal = $10.79/bbl**, i.e. **within 8 cents of the entire reported "collapse."** It was the summer→winter RVP grade change.
    **And the same session's diesel read was wrong twice over:** on a consistent Sep-contract CLOSE basis the record is **8/18 at $101.96** (not Monday), and the give-back from the true peak is **−$1.77 over two sessions and DECELERATING** — not the *"−$5.08 and accelerating"* that reached this desk. That figure was **an intraday bar that did not hold to the close.**

    - **(a)** **For a LEVEL, `=F` is fine.** For a **DELTA, a spread, a crack, or any week-on-week / year-on-year comparison**, name the contract (`HOV26`, `CLU26`) or state the basis and verify no roll sits inside the window.
    - **(b)** **Danger dates are structural, not random:** every expiry, and especially **late Aug (RB Sep→Oct)** and **late Nov**. Verify a roll by **close-matching** the continuous series against the named contracts — don't assume the date.
    - **(c)** **A seasonal grade spread is not a signal in EITHER direction.** Sep gasoline $49.14 vs Oct $40.17 is ~$9/bbl of RVP spec, every year. **A comparison straddling that roll is meaningless bullishly and bearishly alike.**
    - **(d)** ⚠️ **Pairs with the intraday trap, because they compound.** BRENT logged the identical error four weeks earlier on the same instrument (a *"gasoline crack −$10.89 in one session"* that was an intraday read; the close was $58.25, not $49.90). **Same instrument, same trap, twice.** `[[finding_ohlc_verify_before_session_claims]]` · `[[finding_continuous_front_ticker_rolls_so_deltas_lie]]`
    - **(e)** **Nothing was retracted upstream and nothing should be:** the earlier signals were **correct on their own dates** — the roll had not happened yet. **This rule is forward-looking. A method finding is not a retraction.**


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
