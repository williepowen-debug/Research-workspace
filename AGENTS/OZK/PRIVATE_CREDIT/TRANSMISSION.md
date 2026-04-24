# Transmission Mechanics — How Private Credit Stress Reaches OZK

**Last Updated:** 2026-04-23 (Q1 2026 amplifier added to Channel 3; channel architecture unchanged)

---

## Overview

OZK faces private credit stress through four channels. The first is well-understood by the market. The second is partially visible. The third and fourth are not being modeled by anyone we've seen.

The channels are **correlated, not independent** — the same CRE downturn activates all four simultaneously. This is not diversified risk with four chances of loss; it's concentrated risk with four paths to the same outcome.

**🆕 Q1 2026 refinement:** Jake Munn (CIB President) disclosed on the Q1 2026 earnings call that OZK is pulling back from capital-call subscription facilities and experiencing pricing/structure compression in Lender Finance Group — both due to non-bank lenders + insurance companies entering the market. This does NOT add a fifth channel; it amplifies **Channel 3 (Reflexive)**. See Channel 3 below. Structural analysis (Channels 1, 2, 4) unchanged.

---

## Channel 1: Direct (Construction Loan Defaults)

**Mechanism:** OZK construction borrower can't lease/sell completed property → can't refinance at maturity → nonaccrual → charge-off.

This is the main thesis and the channel the market is partially pricing. The mechanics:

1. **Origination (2021-2022):** OZK originates $13.8B in construction loans at peak valuations, 50% LTC, with 18-24 month interest reserves funded at 4-5% SOFR [KB-OZK-061]
2. **Rate shock (2022-2023):** SOFR rises to 5.3%. Interest reserves burn 25-30% faster than modeled. By month 14-19, original reserves exhausted [KB-OZK-088]
3. **Sponsor replenishment (2023-2025):** OZK extracts $2.6B from sponsors ($1.3B equity + $866M reserves + $429M principal) to keep loans current [KB-OZK-084]. 541 modifications. "You pay, you stay."
4. **Maturity wall (2026):** $3.7B maturing this year [KB-OZK-074], front-loaded in Q1 [KB-OZK-075]. Healthy loans already left — FY2025 repayments hit $7.24B record [KB-OZK-082]. What remains is what couldn't refi.
5. **Recognition:** Loans that fail extension hurdles → mandatory nonaccrual within 90 days [KB-OZK-091]. Already visible: $256.7M noncurrent in CRE (75.2% of all noncurrent) [KB-OZK-012]. Sterling Bay Lincoln Yards seized via deed-in-lieu Mar 2026, 100% vacant since 2023 [KB-OZK-094].

**Current status:** LIVE. Wave 1 in progress. $341M noncurrent, $322M added in last 6 months [KB-OZK-063].

---

## Channel 2: Indirect / NDFI (Private Credit Fund Defaults on OZK Lines)

**Mechanism:** CRE debt fund faces its own stress (redemptions, NAV declines, collateral markdowns) → can't repay OZK warehouse/bridge line → OZK takes loss on its $2.74B NDFI book.

This channel exists because of what Gleason admitted: "a chunk of our NDFI loans are actually RESG loans" — loans to CRE debt funds that OZK manages through RESG, not CIB [KB-OZK-022].

The two sub-variants matter enormously:

**Sub-variant A (Co-lending):** OZK holds senior lien on the property; the fund holds mezz. If the fund fails, OZK still has its property lien. Risk is the same as Channel 1 — property-level, not fund-level. OZK is in a 50-60% LTV senior position with the fund's mezz as first-loss buffer.

**Sub-variant B (Back-leverage / Note-on-note):** The fund pledges its entire loan to OZK as collateral. OZK's exposure is to the **fund**, not the property. If the fund gates or defaults:
- OZK takes possession of the fund's loan (which may itself be impaired CRE)
- The fund's loan may be subordinate, mezzanine, or unitranche — worse collateral than OZK would originate directly
- OZK inherits workout complexity on a loan it didn't underwrite

We don't know the A/B split across the $2.74B book. But Gleason's own words — "they want to hold that whole loan on their books but leverage it with a loan from us" — describe Sub-variant B explicitly.

**Stress transmission sequence:**
1. CRE values decline → fund NAV drops
2. LPs request redemptions → fund gates (already happening: Blue Owl, Bridge, Belpointe)
3. Fund needs liquidity → sells loans at discount or can't roll its own funding
4. If fund has OZK back-leverage line → can't repay → OZK loss
5. OZK takes collateral (impaired CRE loan) → additional workout costs

**Named exposure:** 19 CRE-linked counterparties, 6 under stress. See `COUNTERPARTY_WATCH.md`.

**Current status:** PRE-STRESS. NDFI noncurrent is only $2.7M — but fund defaults are binary events, not gradual deterioration. The channel activates suddenly when a fund gates.

---

## Channel 3: Reflexive (Takeout Disappearance)

**Mechanism:** Private credit funds can't provide takeout financing → OZK construction borrowers can't refinance at maturity → construction loan defaults accelerate → Channel 1 worsens.

This is the channel nobody is modeling. It connects BROCK's domain (private credit deterioration) back to OZK's core construction book through an unexpected dependency.

**How it works:**

OZK's construction loans are designed to be temporary. A developer borrows from OZK to build, then refinances into permanent debt (from a CMBS conduit, insurance company, or — increasingly — a private credit fund providing bridge/mezz financing). The "exit" for OZK's construction loan depends on the availability of takeout capital.

Private credit funds have become a significant source of that takeout. Blue Owl's $335M bridge loan (Mar 2026) that refinanced OZK's $215M Wynwood Plaza construction loan [KB-OZK-026] is the clearest example: Blue Owl literally took OZK out of a maturing construction loan.

**The reflexive loop:**

```
PC fund stress → fund gates/freezes new origination
    → OZK construction borrower can't find takeout
    → loan can't refi at maturity
    → OZK extends (if sponsor pays) or classifies nonaccrual
    → maturity wall gets steeper
    → more construction loans need takeout simultaneously
    → remaining PC funds face larger pipeline, tighten standards
    → fewer takeouts → more OZK nonaccruals
    → [loop continues]
```

**Why this matters now:**

BROCK tracks 9 funds gating in ~7 weeks. Each gating event removes takeout capacity from the market. OZK's maturity wall ($3.7B in 2026) is hitting at the exact moment private credit's ability to provide takeout is contracting.

The $7.24B in FY2025 repayments [KB-OZK-082] proves the takeout market was functioning. The question is whether it continues functioning through the 2026 maturity wave as fund stress deepens. Management's guidance of "a lot of payoffs expecting in Q1" [KB-OZK-081] will be tested against a deteriorating takeout environment.

**Evidence of dependency:**
- Blue Owl took out OZK's $215M Wynwood — now facing redemption gates [KB-OZK-026]
- Bridge Investment Group was a JV partner on $367M Stacks DC — now NAV plunging
- The 23 named NDFI counterparties are the same entities that provide bridge/mezz takeout for OZK construction borrowers
- OZK's own ecosystem is self-referential: it lends to the construction borrower AND to the entities providing takeout. Stress hits both sides.

**🆕 Q1 2026 amplifier — Competitive Displacement:**

Jake Munn (CIB President) disclosed on the Q1 2026 earnings call that OZK is **pulling back** from capital-call subscription facilities (Fund Finance) and experiencing pricing/structure compression in Lender Finance Group — explicitly due to "non-bank lenders and then insurance companies who have really entered that market" [KB-OZK-186, KB-OZK-187].

This refines Channel 3's mechanics in an uncomfortable way:

1. **The takeout providers are now OZK's competitors.** The non-bank lenders and insurance companies that previously functioned mainly as bridge/mezz takeout for OZK construction borrowers are now displacing OZK from Fund Finance origination at the margin. Same cohort, different relationship — counterparty *and* competitor.

2. **If the ecosystem cracks, it cracks on both sides of OZK's position.** Healthy non-bank lenders displace OZK on origination pricing today; stressed non-bank lenders stop providing takeout tomorrow. OZK gains nothing from their health and loses from their stress.

3. **Management is cycling away from the displacement** (pivot to CBSF, NRG, EFG, ABLG) rather than accepting the margin compression. That protects NIM but concentrates CIB growth in remaining lines — narrowing the "diversification" story further.

4. **Asymmetric disclosure.** The pullback appears only in the spoken call, not in the written Management Comments PDF (p.16, Figure 17 shows Fund Finance book growing $210M → $1,275M YoY, with no commentary on the margin erosion). Management is reluctant to formalize the competitive problem in durable documentation.

**What this adds to the reflexive loop:** the loop no longer requires outright fund failure to start constricting. Ordinary competitive intensity in the non-bank lender/insurance space already forces OZK to retreat from Fund Finance originations (reducing OZK's footprint in a takeout-adjacent business) *while* OZK's construction book remains dependent on that same ecosystem for exits. Stress amplifies; ordinary competition also extracts a cost.

**Current status:** EARLY WARNING. Takeout market still functioning (record repayments in 2025), but the leading indicators — fund gating, redemption queues, NAV markdowns — suggest capacity is contracting. The Q1 2026 competitive displacement disclosure adds a second pressure vector: OZK is ceding some of the adjacent market even before stress hits. If Q1 2026 repayment velocity drops materially vs Q4 2025's $3.0B, the reflexive channel is activating.

---

## Channel 4: Collateral Cascade (JPM Markdowns → Margin Calls → Forced Selling)

**Mechanism:** JPM (or other dealer banks) mark down collateral pledged by private credit funds → margin calls on warehouse lines → forced loan sales at discount → market prices reset lower → further markdowns → cycle.

This channel is systemic, not OZK-specific. But OZK is uniquely exposed because:

1. **OZK's NDFI counterparties use dealer-bank warehouse lines.** If JPM marks down CRE collateral, funds with JPM warehouse lines face margin calls. Those same funds may also have OZK back-leverage (Sub-variant B). A margin call from JPM could trigger a liquidity crisis that cascades to OZK.

2. **Forced selling reprices OZK's own collateral.** When funds dump CRE loans at 70-80 cents, comparable properties in OZK's direct construction book get reappraised lower. The LTV reappraisal data already shows this: two office loans jumped from 52.9% → 98.9% and 93.2% → 111.5% LTV [KB-OZK-015]. Forced selling by distressed funds accelerates this process.

3. **The cascade is non-linear.** Each markdown triggers more margin calls, more forced selling, more markdowns. OZK sits at the intersection of direct CRE exposure (Channel 1) and indirect fund exposure (Channel 2), so the cascade hits both sides simultaneously.

**Trigger conditions:**
- JPM marks down CRE-backed CLO tranches or warehouse collateral
- Partners Group defaults rise above 5% (currently doubling)
- Software maturity wall ($70B in 2028) begins hitting BDC portfolios early
- Any large fund liquidation that forces CRE loan sales

**Current status:** LATENT. The cascade hasn't fired yet. But the components are all present: elevated CRE distress, fund gating, tightening credit conditions. A single large forced-sale event could trigger repricing across the system.

---

## Channel Interaction Map

The channels don't operate independently. They form a reinforcing system:

```
Channel 4 (Collateral Cascade)
    ↓ marks down collateral values
Channel 1 (Direct) ←——————→ Channel 3 (Reflexive)
    ↑ construction defaults          ↓ takeout disappears
    ↑                                ↓
Channel 2 (NDFI) ←—— fund stress ——→ fewer bridge/mezz originations
    ↑                                ↓
    ←————————————————————————————————→
```

**Worst-case sequence:**
1. JPM marks down CRE collateral (Channel 4)
2. Fund faces margin call, gates redemptions (activates Channel 2)
3. Fund stops originating new bridge loans (activates Channel 3)
4. OZK construction borrower can't find takeout, defaults (Channel 1)
5. OZK takes loss on both the construction loan AND the NDFI line to the same stressed fund
6. Charge-off reprices comparable collateral for other OZK loans
7. More reappraisals, more nonaccruals, more extensions eating reserves
8. ACL consumption accelerates (already at 1.6x coverage — lowest in peer group)

**The double-hit:** If OZK financed both the construction project (RESG) and the debt fund on the same project (NDFI), it takes losses twice on the same underlying asset. We don't know the extent of this overlap, but OZK's "long-standing relationships" with CRE debt funds make it structurally likely.

---

## What Would Prove the Thesis Wrong

- Q1 2026 repayment velocity stays at or above Q4 2025's $3.0B → takeout market still open
- Affinius refinances $2.7B bonds before Oct 2026 → largest stressed counterparty stabilizes
- Blue Owl resumes normal bridge origination → key exit counterparty restored
- NDFI noncurrent stays near zero through 2026 → fund-level stress not reaching OZK
- No JPM/GS collateral markdowns on CRE warehouse lines → cascade doesn't fire

---

*NDFI breakdown → `NDFI_EXPOSURE.md` | Counterparty tracker → `COUNTERPARTY_WATCH.md` | Main thesis → `../THESIS.md`*
