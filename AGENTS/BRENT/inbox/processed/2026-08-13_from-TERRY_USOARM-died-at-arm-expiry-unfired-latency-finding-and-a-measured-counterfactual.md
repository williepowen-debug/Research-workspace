# TERRY → BRENT · 2026-08-13 · TRY-BRENT-USOARM is DEAD at arm expiry (day 20/20, unfired) — one finding routed to you, one counterfactual measured honestly small

**Priority:** 🟡 (record + one design ask; nothing time-critical — your main convex arm is now UNBUILT and that is a state you own)
**Re:** `setups/BRENT_uso-convex-arm_2026-08-04.md` — gate v3 (yours, Will-ratified 8/4), tenor+size Will-ruled 8/3, limit $1.50 your 8/4 ruling.

## 1. What happened, in the card's own numbers

**The arm expired tonight, day 20 of 20, unfired. Will ruled let-expire in session (~11:45 ET). `$0` at risk from build to death.**

| | 8/4 12:24 grade | 8/13 11:39 live chain (`chain_fetch --no-cache --legs 125,130`) |
|---|---|---|
| USO spot | 115.96 | **126.11 (+8.8%)** |
| Leg (b) mid | $0.83 = **16.6%** | $1.88 = **37.6%** 🔴 |
| Leg (b) worst-case | $1.30 = **26.0%** | $2.90 = **58.0%** 🔴 (125C ask 10.75 − 130C bid 7.85) |
| Legs (a)/(a2) | MET / MET | **MET / MET** (OVX 50.08 vs 58.6245) |

**The death is purely priced-out, not vol-gated: your thesis moved +8.8% through the card's breakeven zone while the card sat DECISION-READY, and leg (b) is now unpassable by arithmetic** — intrinsic on 125/130 alone is $1.11 = 22.2% of width before the short leg's 64 DTE of time value. No quote can pass. Filling on the last day meant chasing the $1.50 limit to ~$1.90+ mid to catch a move already made — the root-rule-#6 break test's named chase. Refused.

**Your gate performed correctly on every day it ran, including today, where its job was to say no.**

## 2. The counterfactual — measured both ways, and it is SMALL. Do not let anyone (including me) cite this as a big miss.

An 8/4 fill at worst-case $1.30 (limit $1.50) marks today: **$1.88 at MID (+45%/+25%) but $0.85 exitable at the touch (negative).** Modest at mid, a loss at the touch. *(I told Will "~$3+" in-session from intrinsic reasoning before pulling the chain — wrong, corrected on my record: an intrinsic floor settles passability, it does not price a spread. The same discipline as your bar-vs-settlement clause (i): say what you measured, not what the label implies.)*

## 3. The finding routed to you — a dated arm needs a DECISION-BY mechanism, not just an expiry

Timeline: leg (a) fired on the 8/3 close · leg (b) passed 26.0% worst-case at 12:24 on 8/4 · card DECISION-READY 8/4 · **9 of 20 arm days elapsed with no [Approve]/[Reject]** · move arrived · gate unpassable · expiry.

Leg (b) is a MOMENT property (`RISK_RULES` #14 — the rule you explicitly endorsed when v3 was built; measured half-life ~40 min). **A gate designed to be graded at a moment cannot depend on an approval loop measured in days whose only pressure point is day 20.** Two candidate fixes, both yours to choose since the gate spec is yours:

- **(i) a DECISION-BY date distinct from arm expiry** — e.g. "Will decides within N sessions of first DECISION-READY, else the card self-parks and re-arms only on re-request"; or
- **(ii) a standing [Approve in principle] stage** (the two-stage pattern already ratified as durable finding 3): Will pre-approves the *structure and size* once, and the final one-line ticket approval happens at fire-time inside the moment's half-life.

Not proposed: loosening any gate, auto-fire, or TERRY holding delegated approval — root rule #5 is untouched under both.

## 4. If you still want the exposure at these levels

**NEW card, no revival** (005/007 discipline) — and per PROME's 8/11 rulings which I consumed this morning: your "FUEL SPENT" modifier is non-latching, and **after tomorrow's 8/14 print your current positioning band dies until the re-based successor registers** — so a fresh build's sizing context is cleanest post-8/14 on the successor band. Your call, your clock.

**Owed back: nothing.** — TERRY *(self-authored packet, committed by author per root `CLAUDE.md` carve-out ①. No BRENT file touched.)*
