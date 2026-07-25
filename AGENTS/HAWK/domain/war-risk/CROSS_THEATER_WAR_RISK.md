# Cross-Theater War-Risk Aggregate — HAWK standing surface

> **Standing surface, Will-approved 2026-07-25** (the ~8/1 sunset on the market-wide insurer cc lane was cancelled; HAWK keeps the lane). This is the **only** fleet surface that compares war-risk pricing *across* theaters — neither FALCON nor OSPREY can see this from inside its own lane.
>
> **⚠️ CONVENTION — derived, not owned.** Theater legs belong to their owners: **FALCON** = Gulf/Hormuz/Red Sea/Bab + JWC/P&I · **OSPREY** = Black Sea · **BRENT** consumes. HAWK keeps **no competing copy of a theater's number** — where an owner has a canonical print, cite theirs. HAWK's own contribution is (a) the cross-leg comparison, (b) the decomposition below, and (c) catching when an owner's carry has gone stale.
> **⚠️ "Derived" is NOT "self-updating"** — this file is only as current as its `Refreshed` stamp. See `LESSONS.md` 2026-07-25 item 2.
>
> **Refreshed: 2026-07-25** (first refresh; fresh external pull). **Refresh cadence: every HAWK closeout** (CLAUDE.md closeout step 13a). **Staleness bar: flag any leg whose print is >10 days old.**

---

## Live prints

| Leg | Current | Prior | As of | Source | Owner |
|---|---:|---|---|---|---|
| **Strait of Hormuz** (hull) | **7.5 – 10%** | 1–3% "several weeks ago"; **~5%** [7/10-11] | **7/22** | **Marcus Baker, Marsh global head of marine/cargo/logistics → Platts** | FALCON |
| **Southern Red Sea** (hull) | **>1%** | ~0.75% [7/21]; **0.3%** the prior week (pre-Houthi announcement) | **7/23** | Reuters / Insurance Journal / Al Jazeera 7/23 | FALCON |
| **Bab al-Mandab** (AWRP) | **~0.5%** | — | 7/23 | Al Jazeera 7/23; FALCON KB-039 | FALCON |
| **West Coast Saudi** (call *without* chokepoint transit) | **0.1%** | — | 7/23 | Al Jazeera 7/23 | FALCON |
| **Black Sea** (hull) | **>1%** (one broker ~1.5%) | ~0.6% | **7/21** ⚠️ 4d, no fresh print 7/22-25 | The Insurer 7/21 (OSPREY B-02; absence rows B-03/B-04) | OSPREY |

---

## 🔴 STALE-CARRY CATCH (2026-07-25 — the lane's first output)

**FALCON's canonical Hormuz war-risk carry is ~5% of hull value** (KB-FALCON-004, 7/10-11, Lloyd's List LL1157799 + Star/Xinhua corroboration). **The live market print is 7.5–10% as of 7/22** — the carried figure is **~12 days stale and roughly half the current level**, attributed to a named executive at a top-tier marine broker.

**Why this matters beyond bookkeeping:** FALCON's entire "premium, not supply-loss" framing is *priced off premium levels*. Understating the premium leg by ~2× understates how much the market has already repriced — and therefore how much of the move is already in the tape. Routed to FALCON as a correction, not a disagreement. Similarly, FALCON's Red Sea carry of ~0.75%/hull is the **7/21** figure, superseded by **>1%** on 7/23.

**This is exactly the case for keeping the lane standing:** neither theater owner is wrong about their own theater — but a number stops being re-checked once it is "canonical," and the cross-theater comparison is what makes a stale leg visible.

---

## HAWK's analytical read — the premium decomposes cleanly, and it decomposes on TRANSIT

The four Gulf-region legs are all exposed to the *same* belligerents and the *same* war. They price **two orders of magnitude apart**:

| Exposure | Premium | What it isolates |
|---|---:|---|
| Saudi cargo, **no chokepoint transit** (West Coast) | **0.1%** | Country/origin risk alone |
| Bab al-Mandab transit | **0.5%** | + one contested chokepoint |
| Southern Red Sea transit | **>1%** | + active kinetic enforcement |
| **Hormuz transit** | **7.5–10%** | + the closure-declared, mined, blockaded chokepoint |

**Read: what the market is pricing is TRANSIT risk — the willingness to sail a hull through a specific piece of water — not production risk, not country risk, and not lost barrels.** A cargo from a belligerent-adjacent country costs **0.1%** if it never enters a chokepoint. The same war, the same region, **75–100× cheaper** once you remove the transit.

This is the **strongest single piece of evidence yet** for the migration thesis (`FLOW-HAWK-19` branch (c), `KB-HAWK-229`): the binding constraint is insurer/owner willingness to *move* hulls, and it is quantified, decomposable, and priced. It is also **why premium unwinds fast** — transit risk reprices the moment transit is judged safe, whereas destroyed capacity does not come back on a broker's revised rate.

**Hormuz is 7–10× the Black Sea leg.** Both theaters are elevated, but they are not comparable in magnitude — a consumer treating "both theaters carry war-risk pressure" as symmetric is wrong by an order of magnitude. This is the insurer-side analogue of the barrels-side asymmetry in `KB-HAWK-230`.

---

## Fire / watch conditions

| Condition | Reading |
|---|---|
| **Hormuz premium sustained >10%, or underwriters withdrawing capacity outright** | Transit risk approaching un-insurable → willingness channel saturates → the next increment must come from *physical* supply loss. Watch with `HAW-18`. |
| **Any leg's premium halving without a physical gate firing** | Branch-(c) reversibility CONFIRMED — the premium regime is unwinding. This is the cleanest early tell of the HAW-18 base case. |
| **West Coast Saudi (0.1%) rising materially** | Risk migrating from transit to **origin/country** — would falsify the decomposition above and mean the market has started pricing production risk. **The single most informative cheap datum on this surface.** |
| **Black Sea print going >10 days stale** | Nudge OSPREY (their leg; no fresh print since 7/21). |

---

## Provenance

Owners' surfaces: OSPREY `domain/war-risk/BLACK_SEA_WAR_RISK.md` (named surface, Will-directed 7/22) · FALCON carries its Gulf/Red Sea legs in `workbook/KB.tsv` + STATUS (**no named surface** — a nudge candidate: the theater with the highest and fastest-moving premiums has the least structured war-risk surface). Assignment origin: PROME 7/22 (Will-directed) + PROME cc 7/23. Sunset cancelled by Will 2026-07-25. HAWK rows: `KB-HAWK-229`, `KB-HAWK-231/232/233`.
