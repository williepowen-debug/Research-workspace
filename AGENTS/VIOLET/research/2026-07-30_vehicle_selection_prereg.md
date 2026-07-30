# PRE-REGISTRATION — Vehicle selection for a VIOLET vol-spike view

**Written 2026-07-30 ~13:05 ET, BEFORE any computation on `VX_TERM_HISTORY.tsv`.**
**Owner:** VIOLET (instrument response) · **Counterparty:** TERRY (structure, pricing, risk, harvest)
**Trigger:** `TRY-VIOLET-VIXCS` closed −$111.60 (−38.8%) on 7/30 with the directional call **right**.

> **⚠️ WHY THIS IS PRE-REGISTERED RATHER THAN JUST RUN.** This is the exact setup where I would fit the answer I already like. Today gave me two live examples of doing that — a "two-for-two" tally scored against a registered hook that says nothing about tallies, and a beta adopted on relay. **The tables get built only after this file is committed.**

---

## 0. The framing that makes this a falsification test, not a new rule

**TERRY already owns a registered vehicle rule** — `AGENTS/TERRY/RISK_RULES.md:71`: *"Match expiry to catalyst + confirmation lag; avoid buying too little time for slow-moving credit theses."* Plus **"Structure justified"** as a required card field and **`BAD_STRUCTURE`** as a postmortem tag.

**`TRY-VIOLET-VIXCS` COMPLIED with that rule and still failed on the vehicle axis.** 9 DTE against a catalyst 2 days out is "matched." **So the rule is either wrong or underspecified, and that — not the invention of a new rule — is what this tests.**

⚠️ **TERRY has already withdrawn `BAD_STRUCTURE` on this trade in favour of `NO_HARVEST_RULE`.** That withdrawal is a *live competing hypothesis* (H-C below), not settled background, and this pre-registration must be able to find TERRY right and me wrong.

---

## 1. ⚠️ First: my own H5 was CONFUSED, and I am fixing it before testing, not after

**H5 as written in SCRATCH 7/30:** *"If forward beta rises with proximity to expiry, then the optimal tenor for a dated catalyst is LONGER than the catalyst window — you want the event inside the contract's life while beta is still climbing, not expiring into it."*

**That mechanism does not follow from its own premise.** The measured gradient is **0.274 @21–35 DTE · 0.505 @11–20 · 0.591 @≤10** — beta is **HIGHEST at SHORT DTE**. So a *longer* tenor puts the event at a point where beta is **LOWER**, not higher. **The sentence argues for longer tenor using a fact that argues for shorter.**

**What I was actually reaching for is a different and separable claim: you want to still be HOLDING the contract after the event, so the position can be harvested.** That is a **harvest-window** argument, not a beta argument — and it points at the same place TERRY's `NO_HARVEST_RULE` does.

**H5 is therefore split into H-B1 and H-B2 below and tested separately.** Conflating them would have let a win on either read as a win for both.

---

## 2. The competing hypotheses

| | Claim | Predicts |
|---|---|---|
| **H-A** *(TERRY's registered rule)* | Match expiry to catalyst + confirmation lag | Conversion **peaks at matched tenor** and falls off on **both** sides |
| **H-B1** *(beta)* | Shorter tenor at the event converts better, because beta is highest at low DTE | Conversion **rises monotonically as event-DTE falls** |
| **H-B2** *(harvest window)* | Tenor must leave **live days after the event** so the move can be sold | Conversion rises with **post-event days remaining**, roughly independent of event-DTE |
| **H-C** *(TERRY's post-audit position)* | Tenor is second-order; the failure was **no rule keyed to being in profit** | **No tenor** shows materially better conversion once a harvest rule is applied |

**These are genuinely separable and the data can distinguish them.** H-B1 and H-B2 point in *opposite* directions on tenor (H-B1 short, H-B2 long) — so "longer is better" and "shorter is better" cannot both be scored as vindicating me.

---

## 3. What I will measure (VIOLET half only)

**Universe:** VIX spike episodes 2013-05 → 2026-07 from `workbook/VX_TERM_HISTORY.tsv` (28,555 contract-days) + `^VIX`.
**Episode definition (fixed now):** VIX rises **≥20% over ≤5 trading sessions** from a start below 20. *(Chosen to match the setup VIOLET actually trades; ~66 peaks ≥20 exist in the panel and this will select a subset.)*

For each episode and each tenor bucket **(≤5, 6–10, 11–15, 16–20, 21–30, 31+ DTE at the spike)**:
1. **Forward response** — Δforward ÷ Δspot (realized beta), and the *absolute* forward move.
2. **Peak-to-entry** — the maximum favourable forward excursion within the contract's remaining life.
3. **Harvest window** — trading days between the spike peak and expiry.
4. **Decay cost** — forward drift over the waiting period *before* the spike, per day held.

**Output:** two tables (conversion, decay) → `research/2026-08-XX_vehicle_conversion_tables.md`, handed to TERRY.

**I compute NO option prices, no strikes, no P/L.** Those need bid/ask, IV/skew, OI and theta — TERRY's domain and TERRY's data.

---

## 4. Falsification, stated in advance

- **H-A survives** iff conversion is non-monotonic in event-DTE with an interior maximum near the catalyst horizon.
- **H-B1 survives** iff conversion is monotonically decreasing in event-DTE **and** the effect exceeds the decay penalty of holding shorter-dated.
- **H-B2 survives** iff post-event days-remaining predicts conversion **after controlling for event-DTE**. ⚠️ **If it does not survive that control, it is confounded with H-B1 and I report it as such.**
- **H-C survives** iff the tenor spread in conversion is **smaller than the spread between harvest rules** applied to a single tenor.
- **ALL FOUR CAN FAIL.** The honest outcome "tenor does not predict conversion in this sample" is a real result and will be reported as one.

---

## 5. My stated prior, so I can be graded on it

**I expect H-B2 and H-C to be jointly right and H-A to be underspecified rather than wrong** — i.e. matching expiry to the catalyst is fine for *getting the move* and bad for *keeping it*, because it leaves no room to sell. **I expect my own H-B1 to be the weakest of the four**, because our trade sat in the highest-beta bucket (≤10 DTE) and still lost.

⚠️ **Note the incentive and discount accordingly:** H-C is **TERRY's** hypothesis and H-B2 is closest to mine. **I am predicting TERRY is right, which is the direction that costs me nothing** — so treat my prior as weak evidence at best.

---

## 6. Constraints stated before, not discovered after

1. **n is the binding limit, not data access.** ~66 peaks ≥20 across 13 years, and the ≥20%-in-≤5-sessions filter will cut that hard. **Bucketing by six tenors will leave single digits per cell.** This will likely be **directional, not decisive** — and I will say so rather than dress up a thin result.
2. **Base-rate everything** (`finding_base_rate_the_instrument_before_its_event_table`). "Tenor X converts 60%" is meaningless without the unconditional conversion rate.
3. **This is instrument response, NOT a trade backtest.** No assumed fills.
4. **I supply half a tradeoff.** Longer tenor buys harvest room nearly free in *my* half and costs premium in *TERRY's*. **Neither of us can conclude alone, and I will not.**
5. **Weeklies vs monthlies.** The panel is **monthlies only**; VIXCS was a **weekly**. Weekly settles track the monthly closely but are not identical — **stated as a known approximation, not silently absorbed.**

---

## 7. Sequencing

**Runs AFTER the 8/5 SOQ grader.** That grader scores my KB-VIO-144 fade verdict; doing the vehicle work first risks colouring it toward making that verdict look good. Will-approved 7/30.

---

*Pre-registered by VIOLET 2026-07-30 before any computation. Companion packet: `AGENTS/TERRY/inbox/2026-07-30_from-VIOLET_vehicle-selection-scoping.md`. Amendments to this file must be dated and must state what was known when the amendment was made.*
