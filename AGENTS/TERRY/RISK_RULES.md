# TERRY RISK RULES
**Created:** 2026-06-20

> **HOT half of a hot/cold split, 2026-09-03 (read-cap remedy, Will-approved).** Rules **14–23 live in full at `RISK_RULES_CONSTRUCTION.md`**; the index at the foot of this file carries every one of them by number with its *binds-at* trigger. ⛔ **Nothing was retired, weakened or made optional — only relocated.** The numbered list is a **stable API**: cards cite these by number and the numbers did not move.
> ⚠️ **RE-TRIGGER (READ_CAP rule 7 — a remedy names its own, and a leanness claim is exactly what this must not be): re-measure BOTH halves at any append to either, or on 2026-12-03, whichever comes first.** Instrument: `python3 scripts/read_cap_check.py --agent TERRY`. **Do not read this header as "this file is lean" — read it as "this file was cut once, on a date, and is due a re-measure."**
> ✅ **RE-MEASURED 2026-09-11**, on the append of finding **5b** — the re-trigger fired and was honoured rather than deferred. `read_cap_check.py --agent TERRY` rc=**0**: this file **21,165 B (39% of cap)** · `RISK_RULES_CONSTRUCTION.md` **22,584 B (42%)`. **Both halves under budget; no rotation owed.** ⚠️ Same pull flagged three OTHER boot-reads at rotate-tier — `SETUPS.tsv` 58% · `STATUS.md` 56% · `TRADE_BOOK.md` 55% — **advisory, not this file's problem, and recorded here only so the next append does not re-discover it.** Next re-trigger unchanged: **any append to either half, or 2026-12-03.**

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
- **Two expiry frameworks — don't mix them:** dateable single-name catalysts (PC names: APO, ARES, ARCC) → near expiry keyed to the catalyst (BROCK owns the PC catalyst clock); macro/index (HYG, KRE, IWM) → the Hamilton demand-destruction clock → far expiry (BRENT owns it). *(From retired root LESSONS #2, WQ-130 2026-08-29.)*
- **Earnings / event dates come from company IR or the 8-K, never from an agent's memory** (OZK was wrong twice). *(From retired root LESSONS #4, WQ-130 2026-08-29.)*
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
5b. **🔴 "PULL THE LIVE CHAIN" IS NOT ENOUGH — THE VENDOR'S OPTION QUOTE IS NOT PROVEN LIVE, AND IT READS OPTIMISTIC ON THE SIDE YOU TRANSACT.** *(2026-09-11, measured, n=1 live incident + a same-session investigation.)* Rule 5 above says pull the live chain. **This is the failure of that remedy.** `chain_fetch.py` reported the XLE Sep-30 65C at **bid `1.66`**; the **Fidelity** screen at a comparable moment showed **`1.51` × 53** — **~10% high, on the side being SOLD, in the direction that FLATTERS the trade.** ★ **Why no guard caught it, and could not have:** `yfinance`/Yahoo expose **NO bid/ask timestamp and no delay flag for an option leg** — verified against the raw payload, not assumed — while the **underlying** quote *does* carry `exchangeDataDelayedBy: 0` and `regularMarketTime` and tested real-time to ~1 min. **The spot is declared and timestamped; the option quote is neither.** The one freshness check that existed read `lastTradeDate` — **the last EXECUTED TRADE, a different quantity**, which can be fresh while the quote is stale — and compared it to a **DATE**, so it could not see intraday staleness of any magnitude, **by construction**. ⇒ **THE RULE: vendor chain marks are SCREENING marks. The price you transact on comes from the BROKER.** A card may be *built* on vendor marks; a **fill** may not be *priced* on them. ⚠️ **Magnitude discipline:** the lag is **CONFIRMED materially nonzero** — sign violations appear in the tool's *own* successive outputs, needing no external data — but the ~15-minute figure is **PLAUSIBLE on single-session evidence and is NOT a measured constant. Never cite it as one.** Guard shipped the same day (`FLAG_DIRINC`, advisory): it flags a mark that moved *opposite* the printed spot between two `--no-cache` pulls. ⛔ **Deliberately NOT fatal** — an IV move can do this legitimately, and **a flag cannot recover the true bid anyway.** `[[finding_freshness_check_cannot_catch_a_fresh_lie]]`

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

### Construction rules 14–23 — **HOT INDEX over a cold register** (full text: `RISK_RULES_CONSTRUCTION.md`)

⛔ **These are RULES, not history. They are numbered, cited by number, and every one is LIVE.** Only their full text and worked cases moved; nothing here is retired, weakened or optional. **Read `RISK_RULES_CONSTRUCTION.md` in full before producing any actionable trade card** (`CLAUDE.md` BOOT step 7) — and on demand the moment one of the *binds-at* triggers below fires.

| # | rule, in one line | binds at |
|---|---|---|
| **14** | Separate a STRUCTURE property from a MOMENT property; grade each on its own clock. A moment-property number is never quoted without its timestamp. **Empirical half-life at this desk ~40 min.** | any grade of a gate leg |
| **15** | A gate that opens on vol/price DECAY carries **zero** thesis information and will feel like confirmation. | any decay-keyed entry gate |
| **16** | Match the expiry to the view's horizon; a structural view in a same-day instrument is a different, far worse trade. **Corollary: a control that has never fired needs its FORM changed, not its wording — count executions, not specifications.** | tenor choice; any manual control |
| **17** | The SIZE-INCREASING branch carries the higher evidential burden, and the spec must show the asymmetry in its own numbers. | any sizing claim |
| **18** | A print never justifies a deep-OTM strike — match the strike to the event's **measured** envelope (regional banks: median 2–3%, **0 of 32 ≥10%**) or take the tenor past the print. | any print-catalyst card |
| **19** | A series-derived extreme/streak/percentile must state its **bar count**; coverage is a property of the PULL, and absent bars carry no nulls to detect. | any quoted extreme or percentile |
| **20** | The ENTRY half of a card is unrecoverable after the fill; a retroactive write-up is **management-only** and says so. Forward max loss = the remaining mark, never the original debit. | any un-carded held position |
| **21** | A tenor band is an ENTRY-ECONOMICS test: it governs new deployments, not rolls — and **"roll" = same underlying · same strike · later expiry, nothing else.** | any roll or new deployment |
| **22** | A continuous front-month `XX=F` ticker is safe for a LEVEL and unsafe for a DELTA: name the contract or state the basis and check the roll. | any futures-derived delta/spread |
| **23** | Name the driver before you add. Profit from a mechanism you did not underwrite is evidence **against** the card. No name ⇒ no add, and reduce. | any add; any un-catalysed move |

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
