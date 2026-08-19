---
signal_id: SIG-W-20260819-025
date: 2026-08-19
time_dispatched: 2026-08-19T18:3xZ
origin: WALTER boot 6c/7e, 2026-08-19 — the wk-8/14 EIA print was the dated falsifier carried out of `SIG-W-20260819-016`. The RESEARCH-INTAKE lane still showed the wk-8/7 period at its 15:26Z run; WALTER pulled the EIA API directly rather than record a not-yet-posted.
source: **EIA API v2 `petroleum/stoc/wstk`, own pull 2026-08-19 ~18:1xZ. Series WCSSTUS1 (SPR), W_EPC0_SAX_YCUOK_MBBL (Cushing), WCESTUS1 (commercial crude). Period 2026-08-14 — PRIMARY, not relayed.**
domain: HYDROCARBON_INFRA
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: [BRENT]
info: [HAWK]
entities: [SPR, Cushing, WCSSTUS1, WCESTUS1, Boundary-3, CL=F, BZ=F]
signal_type: threshold-crossed
confidence: 0.95
verdict: CONFIRMED-AT-PRIMARY
consumer_lens: BRENT rescinded Cushing Boundary #3 on 2026-08-12 after a three-week rebuild. The next print reversed it. This is not a gate fire — the boundary is rescinded and a raw sub-20M print would NOT be an unfired gate — but the evidence BRENT rescinded on has turned, and BRENT is the only desk that can rule on whether that matters.
cluster_secondary: null
---

# 📉 **The SPR drew a fourth straight week (−5.268M, 293.426M). And Cushing's rebuild — the thing BRENT rescinded Boundary #3 on seven days ago — reversed on the very next print.**

## 1. The print

**EIA weekly, period 2026-08-14, own API pull. The lane had not yet picked it up at its 15:26Z run; this is a direct read.**

| Series | wk 7/24 | wk 7/31 | wk 8/07 | **wk 8/14** | WoW |
|---|---|---|---|---|---|
| **SPR** (kbbl) | 307,650 | 304,809 | 298,694 | **293,426** | **−5,268** |
| **Cushing** (kbbl) | 18,599 | 20,955 | 22,566 | **21,252** | **−1,314** |
| Commercial crude (kbbl) | 404,508 | 406,987 | 424,410 | **428,815** | +4,405 |

## 2. ✅ THE `-016` FALSIFIER RESOLVED — and it resolved AGAINST the "it stops" reading

`SIG-W-20260819-016` framed the drawdown as a **172M-bbl emergency EXCHANGE** whose window ends this month, with the falsifier being simply: *does the draw continue?*

**It continued. −5.268M this week.** Four consecutive weekly draws:

**307.650 → 304.809 → 298.694 → 293.426 = −14.224M bbl since 7/24**, averaging **−4.74M/wk**.

⚠️ **What this does NOT settle.** A continuing draw is consistent with the exchange-delivery reading **and** with a discretionary sale — the two are not separated by the drawdown series. `-016`'s claim was about the **instrument** (exchange vs sale), and a stock series cannot grade an instrument. **The exchange framing survives the week; it has not been confirmed by it.** `[[finding_record_of_an_action_is_not_the_action]]`

**The `-016` window claim is now one week from its own test:** if the exchange window genuinely closes this month, the draw should stop within roughly two more prints. That is a real, dated, falsifiable line and BRENT owns it.

## 3. 🔴 THE SHARPER ITEM: Cushing's rebuild reversed the week after it was used to rescind a boundary

**Cushing Boundary #3** (sub-20M → IMMEDIATE, BRENT-primary) fired 2026-06-24, ran ~7 weeks, and was **RESCINDED by BRENT on 2026-08-12**.

The rebuild BRENT rescinded on:

**18.599 [7/24] → 20.955 [7/31] → 22.566 [8/07]**  — three prints, +3.967M, clearing the 20M line decisively.

**The next print: 21.252 [8/14], −1.314M.** The first decline of the rebuild, and it landed **two days after the rescission**.

**🔑 THIS IS NOT A GATE FIRE AND MUST NOT BE WRITTEN AS ONE.** Boundary #3 is rescinded. A raw sub-20M print in this series is **not** an unfired gate, and reading one as a miss is the exact false-MISS this desk nearly published on 8/19 (standing check (p): *a number next to a threshold tells you nothing until you read the gate*). **Consulting the gate's own record is what makes this a note to its owner rather than a fire.**

**What it IS:** the last observation available to BRENT when it rescinded was 22.566. The series has since given back **33% of the rebuild** in one week. **Whether that re-opens the question is BRENT's ruling and nobody else's** — this desk records the reversal and routes it.

Level context: **21.252M is 1.252M above the old 20M line**, i.e. one print of this week's magnitude from re-crossing it.

## 4. The third leg, for completeness

**Commercial crude built again: 428.815M, +4.405M**, on top of last week's +17.423M. Two consecutive large builds totalling **+21.8M bbl**. The lane graded last week's build `orange`. ⚠️ **Note the composition against the SPR draw**: SPR down 5.268M while commercial up 4.405M is close to a **transfer**, not a net national build — but this desk cannot certify that from stock levels alone (imports, runs and exports all move the same week). **Named as a hypothesis for BRENT, not a finding.** `[[finding_composition_mask_unmask_discriminator]]`

## 5. Routing note (dispatch step 10.7)

Axes present: **strategic reserve · midstream storage hub · commercial inventory** — all one domain, and **BRENT owns all three**. **MARCO was deliberately NOT included**: MARCO's REGISTRY Domain is *"Immigration, DHS shutdown, labor supply"*, not general macro — it was on `-007`'s `info:` line for the earlier SPR item and doctor check #27 flagged that line the same day. **HAWK on info** for the Gulf-supply read. **TERRY correctly absent — no registered TERRY instrument is named or moved by this** (§3.5.5: TERRY is never on `info:`).

**Confidence 0.95** — the figures are an own pull at the EIA primary and are reproducible. The uncertainty is entirely in interpretation, and interpretation is BRENT's.
