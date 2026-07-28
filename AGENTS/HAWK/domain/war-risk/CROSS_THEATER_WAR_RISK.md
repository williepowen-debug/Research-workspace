# Cross-Theater War-Risk Aggregate — HAWK standing surface

> **Standing surface, Will-approved 2026-07-25** (the ~8/1 sunset on the market-wide insurer cc lane was cancelled; HAWK keeps the lane). This is the **only** fleet surface that compares war-risk pricing *across* theaters — neither FALCON nor OSPREY can see this from inside its own lane.
>
> **⚠️ CONVENTION — derived, not owned.** Theater legs belong to their owners: **FALCON** = Gulf/Hormuz/Red Sea/Bab + JWC/P&I · **OSPREY** = Black Sea · **BRENT** consumes. HAWK keeps **no competing copy of a theater's number** — where an owner has a canonical print, cite theirs. HAWK's own contribution is (a) the cross-leg comparison, (b) the decomposition below, and (c) catching when an owner's carry has gone stale.
> **⚠️ "Derived" is NOT "self-updating"** — this file is only as current as its `Refreshed` stamp. See `LESSONS.md` 2026-07-25 item 2.
>
> **Refreshed: 2026-07-28.** **Refresh cadence: every HAWK closeout** (CLAUDE.md closeout step 13a). **Staleness bar: flag any leg whose print is >10 days old.**

---

## Live prints

| Leg | Current | Prior | As of | Age at refresh | Source | Owner |
|---|---:|---|---|---|---|---|
| **Strait of Hormuz** (hull) | **7.5 – 10%** | ~5% [7/10-11] — **corrected, see below** | **7/22** | 6d ✅ | Marcus Baker, Marsh global head of marine → Platts | FALCON |
| **Southern Red Sea** (hull) | **>1%** | ~0.75% [7/21]; 0.3% pre-Houthi-announcement | **7/23** | 5d ✅ | Reuters / Insurance Journal / Al Jazeera 7/23 | FALCON |
| **Bab al-Mandab** (AWRP) | **~0.5%** | — | 7/23 | 5d ✅ | Al Jazeera 7/23; FALCON KB-039 | FALCON |
| **West Coast Saudi** (call *without* chokepoint transit) | **0.1%** | — | 7/23 | 5d ✅ | Al Jazeera 7/23 | FALCON |
| **Black Sea** (hull) | **>1%** (one broker ~1.5%) | ~0.6% | **7/21** | **7d ⚠️** | The Insurer 7/21 (OSPREY B-02; absence rows B-03/B-04) | OSPREY |

---

## ✅ STALE-CARRY CATCH #1 — CLOSED (raised 7/25, adopted 7/27)

The lane's first output was a catch on FALCON's canonical Hormuz carry (~5%, KB-FALCON-004, 7/10-11) against a live market print of **7.5–10%** [Marsh → Platts, 7/22] — ~12 days stale and roughly half the level.

**FALCON accepted it in full** and re-marked (their NEXUS_BRIEF 7/27: *"Hormuz 7.5-10%/hull (I was carrying ~5% — 12 days stale, half the market)"*). Per this file's own convention, **HAWK now re-points to FALCON's number and drops its own copy.** They also named a war-risk surface (`workbook/WARRISK.tsv`), scoped deliberately to Hormuz/Gulf/Red Sea theater premia so it does not collide with this synthesis lane — which closes the 🟠 "FALCON has no named war-risk surface" nudge that sat with PROME.

---

## ⚠️ STALE-CARRY CATCH #2 — OPEN (raised 2026-07-28)

**The Black Sea leg is 7 days old (7/21), and the event that should have moved it has already happened.**

The bar on this surface is 10 days, so the leg is **not yet formally stale** — but staleness by clock is the weaker test. The stronger one is *content*: **CPC resumed loadings on 7/27** after a week-long halt, with two SPMs loading and Tengizchevroil-chartered tankers returning. A terminal reopening is a direct input to Black Sea hull premia, and **there is no post-resumption print on the leg.**

Compounding it: **OSPREY's own STATUS is dated 7/24 and still reads "still HALTED 7/21 AM"** — i.e. the theater owner's canonical surface carries a state that external primaries superseded on 7/27. Routed to OSPREY 7/28 as a correction, not a disagreement. *(This is the same shape as catch #1: neither owner is wrong about their theater, but a number stops being re-checked once it is canonical.)*

---

## HAWK's analytical read — the premium decomposes cleanly, and it decomposes on TRANSIT

The four Gulf-region legs are all exposed to the *same* belligerents and the *same* war. They price **two orders of magnitude apart**:

| Exposure | Premium | What it isolates |
|---|---:|---|
| Saudi cargo, **no chokepoint transit** (West Coast) | **0.1%** | Country/origin risk alone |
| Bab al-Mandab transit | **0.5%** | + one contested chokepoint |
| Southern Red Sea transit | **>1%** | + active kinetic enforcement |
| **Hormuz transit** | **7.5–10%** | + the closure-declared, mined, blockaded chokepoint |

**Read: what the market prices is TRANSIT risk — willingness to sail a hull through a specific piece of water — not production risk, not country risk, and not lost barrels.** The same war, the same region, **75–100× cheaper** once the transit is removed.

This remains the strongest single piece of evidence for the migration thesis (`FLOW-HAWK-19` branch (c), `KB-HAWK-229`), and it is why premium unwinds fast: transit risk reprices the moment transit is judged safe, whereas destroyed capacity does not come back on a broker's revised rate. **Validated on its first test 7/27** — Brent round-tripped ~−11 to −13% in two sessions with a 400 kbpd Aramco refinery still visibly burning (`KB-HAWK-239`).

**Hormuz is 7–10× the Black Sea leg.** Both theaters are elevated; they are not comparable in magnitude. A consumer treating "both theaters carry war-risk pressure" as symmetric is wrong by an order of magnitude — the insurer-side analogue of the barrels-side asymmetry in `KB-HAWK-230`.

---

## 🆕 The channel going STRUCTURAL — a non-price expression of the same thing (2026-07-28)

**This is not a premium and must not be tabled as one.** On 7/27, **MRPL** (India, state-owned ONGC subsidiary) became the **first Indian refiner ever** to write "avoid the Red Sea **or** the Strait of Hormuz" into a spot crude tender — up to 1M bbl, delivery 25 Aug–6 Sep, with MRPL stating **the clause stays in future tenders if the situation does not improve** [Reuters, tender document seen, 7/27 → `KB-HAWK-237`].

**Why it belongs on a war-risk surface even though it carries no rate:** every other avoidance datum in the fleet is a *ship moving* — reroutes, U-turns, AIS-dark hulls, transit counts. Those are tactical and unwind in days. **A tender clause is forward-dated, contractual, sticky by its own terms, and precedent-setting in the world's #3 crude importer.** A premium is a *price* that reverts when transit is judged safe; a contract clause is a *quantity* decision that persists after the premium normalises.

**⚠️ Do not size it off volume** — 1M bbl is a few days of crude for a ~300 kb/d refinery. In barrels it is noise. The datum is the precedent and the contract language.

**Note the buyer bars BOTH chokepoints** — it treats the Red Sea *bypass* as compromised too, which is a live input to the West Coast Saudi falsifier below.

**Adopted test (WALTER's pre-registration, 7/27):** ≥2 further Indian refiners (IOC / BPCL / HPCL / Reliance — Reliance-Jamnagar being the one material in barrels) adopting the clause within **~3–4 weeks (→ ~2026-08-24)** = durable re-contracting. Zero = one cautious buyer, not a trend. Checked 7/27, nothing found yet — recorded as an explicit negative.

---

## Fire / watch conditions

| Condition | Reading |
|---|---|
| **Hormuz premium sustained >10%, or underwriters withdrawing capacity outright** | Transit risk approaching un-insurable → willingness channel saturates → the next increment must come from *physical* supply loss. Watch with `HAW-18`. |
| **Any leg's premium halving without a physical gate firing** | Branch-(c) reversibility CONFIRMED. ✅ **Partially observed 7/27** on the price side (Brent −11 to −13%); the premium legs themselves have not yet reprinted lower. |
| **West Coast Saudi (0.1%) rising materially** | Risk migrating from transit to **origin/country** — would falsify the decomposition above. **Still the single most informative cheap datum on this surface.** ⚠️ Now with a second read-through: MRPL barring the bypass as well as Hormuz is early evidence that buyers are widening the geography of avoidance. |
| **≥2 more Indian refiners adopt the MRPL clause by ~8/24** | Willingness has become **structural** — premium → re-contracting. Would move branch (c) from "fragile in both directions" toward durable. |
| **Black Sea print going >10 days stale** | ⚠️ **7d at this refresh, and content-stale already** (no post-CPC-resumption print). Nudge sent to OSPREY 7/28; formal bar breaches 7/31. |

---

## Provenance

Owners' surfaces: OSPREY `domain/war-risk/BLACK_SEA_WAR_RISK.md` (named 7/22, Will-directed) · FALCON `workbook/WARRISK.tsv` (**named 7/27** — closes the prior nudge; scoped to Hormuz/Gulf/Red Sea so it does not collide with this lane). Assignment origin: PROME 7/22 (Will-directed) + PROME cc 7/23. Sunset cancelled by Will 2026-07-25. HAWK rows: `KB-HAWK-229`, `KB-HAWK-231/232/233`, `KB-HAWK-237`, `KB-HAWK-239`.
