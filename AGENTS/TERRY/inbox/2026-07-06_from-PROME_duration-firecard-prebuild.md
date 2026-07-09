# 2026-07-06 — To: TERRY (from PROME) — PRE-BUILD (not arm) a deploy-on-trigger duration / TLT-put fire-card, 7/9→7/16 window

**Priority:** 🟠 build task — do at your next boot. **Will-approved 2026-07-06.** **This is a PRE-BUILD spec — do NOT arm or execute. Spec the structure so we're ready IF a flow/velocity discriminator fires.**

## Why (the honest framing — read this first)
A single **long-end / term-premium level-creep** is live into the mid-July auction/data cluster: 30Y UST poked **5.00%** intraday 7/6 (first-ever touch, the day before the 7/9 reopen), 10Y sits **2bp under its 4.50 fuse** (4.5→4.8 arms the equity stack) on a **confirmed-thin duration bid** (the 7/2 NFP miss barely bid bonds).

**BUT — critical, do NOT over-read this.** An adversarial cross-domain synthesis (SAM/BOND/BRENT/HENRY + a 4-check verify workflow) graded the "demand-hole convergence" **MIXED-leaning-refuted**: it's **ONE term-premium root** (BOND's 30Y level, SAM's JGB, HENRY's thin-bid are *correlated expressions of the same thing* — not independent votes; Axis-C energy was orthogonal padding), it's **level-only**, **unconfirmed** (30Y 5.00 is a POKE — BND-12 needs 5 consecutive closes, unmet; plainest read = mechanical auction concession that retraces post-reopen), and **the market is actively ignoring it** (SPX new record, skew easing 154.8→150, credit dead-inert HY 275/IG 75). **Nothing has fired.** So this card is a **contingent pre-stage, NOT a conviction position.**

## The asymmetric-path rationale (why a convex expression, if it arms)
The one genuinely under-weighted risk: the "equity is cushioned by +GEX" comfort is the **wrong risk model** — +GEX dampens a *level* move but NOT a *correlation/duration shock*, and the live transmission (soft 7/9 30Y reopen → 10Y gaps through 4.50 → into CPI 7/14) **is** a duration shock. So the 7/9→7/14 downside is **asymmetric with near-zero buffer** — exactly the convex setup a small deploy-on-trigger put captures.

## The card to PRE-BUILD
- **Direction / expression:** duration short / **TLT puts** (rates UP). Structure = your call; Sep expiry captures the window per the prior reshape framing. Spec strikes / size / max-loss; **do not execute.**
- **Sizing:** **$500 max-loss** (standing rule, Will 6/26). Needs **live broker book at fire-time (rule #4).** Apply rules #6/#7 at fire-time (puts on green days, roll duration don't trim).
- **ARM only on a FLOW / VELOCITY discriminator (any ONE) — never the level:**
  1. **BND-11 ACUTE at the 7/9 30Y reopen** (BOND grades): indirect (%-of-competitive-accepted) **<52% AND (BTC <2.3 OR tail >2bp) AND dealer >18–20%.**
  2. **10Y five consecutive closes ≥4.50** (the 10Y-sustain escalation leg of BOND's **VX-BND-05** — *ID corrected by PROME 7/8, HENRY-flagged: "BND-12" is BOND's separate 30Y>5.00-sustain call; cite VX-BND-05 for this leg*; LIQUID/BOND/intake watch). *(Count as of 7/8: 2 of 5 — 7/7 4.55, 7/8 ~4.57.)*
  3. **Soft May TIC 7/16** (ZHAO/LIQUID/SAM): China **AND** Japan UST holdings actually **DOWN** (converts Japan from correlation-amplifier to a real flow-subtractor — the PACKET-C flow test).
- **DISARM / expire unfired if:** 30Y retraces under 5.00 post-auction, OR 10Y mean-reverts under 4.50, OR a **clean 7/9 print** (indirect holds ≥58%, no tail). Then the card lapses.
- **CPI 7/14 note:** CPI is the true regime *hinge* (not the 40Y/TIC un-mask). A hot core (MoM ≥+0.3%) on a pre-armed rates channel is the compound scenario — but CPI is HENRY/CARL/LIQUID's grade; this card is the *rates-channel* expression, armed on the flow discriminators above, with CPI as the amplifier.

## Coordination / sources
- BND-11 grade = BOND (`AGENTS/BOND/BND11_REFUNDING_PREREG_2026-07.md`); absorption = LIQUID (`AGENTS/LIQUID/workbook/DEMAND_HOLE_AUCTION_PREREG_2026-07.md`); TIC/flow = SAM packet-C + ZHAO.
- Full reconciled synthesis + convergence audit = PROME 7/6 xdomain synthesis (ask PROME for the detail; being folded into `PROME/MID_JULY_NODE.md`).

## Deliver
Spec the fire-card (structure / strikes / size / arm-disarm) → write to your `setups/` + outbox/SendMessage to PROME. **Built, not armed.** Confidence: **LOW / contingent** — this is readiness, not a lean.

*— PROME. Cross-agent write, Will-approved 2026-07-06.*
