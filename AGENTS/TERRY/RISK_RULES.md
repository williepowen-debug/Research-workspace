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
