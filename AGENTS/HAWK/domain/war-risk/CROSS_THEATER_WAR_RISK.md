# Cross-Theater War-Risk Aggregate — HAWK standing surface

> **Standing surface, Will-approved 2026-07-25** (the ~8/1 sunset on the market-wide insurer cc lane was cancelled; HAWK keeps the lane). This is the **only** fleet surface that compares war-risk pricing *across* theaters — neither FALCON nor OSPREY can see this from inside its own lane.
>
> **⚠️ CONVENTION — derived, not owned.** Theater legs belong to their owners: **FALCON** = Gulf/Hormuz/Red Sea/Bab + JWC/P&I · **OSPREY** = Black Sea · **BRENT** consumes. HAWK keeps **no competing copy of a theater's number** — where an owner has a canonical print, cite theirs. HAWK's own contribution is (a) the cross-leg comparison, (b) the decomposition below, and (c) catching when an owner's carry has gone stale.
> **⚠️ "Derived" is NOT "self-updating"** — this file is only as current as its `Refreshed` stamp. See `LESSONS.md` 2026-07-25 item 2.
>
> **Refreshed: 2026-08-20.** ⚠️ **NO-CHANGE PASS — both legs STILL DARK, and the staleness has roughly doubled since the last stamp.** Hormuz is now **+29d** past its 7/22 print and Black Sea **+30d** past its 7/21 print, against a **10-day bar**. **No August print exists for either leg** — searched by three desks independently on 8/10 and unrefreshed since. **The Marsh primary — one named individual carrying BOTH the Gulf premium and the capacity arithmetic — is 403 at both mirrors and unfetched 30 days** (FALCON volunteered the pull 7/26; still owed). ⚠️ **A no-change pass still re-stamps, per this step's own text** — this surface rots at the cadence of its REGENERATION, not on its own. **Step 13a was SKIPPED at the 8/15 closeout** (DAEDALUS flagged it 8/15); this pass closes that gap. **Nothing below this line changed on 8/20 except the staleness arithmetic** — stated explicitly so a fresh header is not mistaken for a fresh body (`[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]`).
>
> **Refreshed: 2026-08-10 (prior).** ⚠️ **BOTH LEGS ARE NOW STALE AND BOTH ARE DARK — no August print exists for either.** Hormuz was **+19d** past its print and Black Sea **+20d** *(as of that stamp; see the 8/20 line above for current)*. **THREE DESKS SEARCHED INDEPENDENTLY ON 8/10 (HAWK, FALCON, OSPREY) AND FOUND NOTHING.** That is a positive finding about the instrument, not a gap in effort — see the diagnosis below, which REPLACES the framing this file previously carried.
>
> **Refreshed: 2026-07-28 (prior).** **Refresh cadence: every HAWK closeout** (CLAUDE.md closeout step 13a). **Staleness bar: flag any leg whose print is >10 days old.**

---

## Live prints

| Leg | Current | Prior | As of | Age at refresh | Source | Owner |
|---|---:|---|---|---|---|---|
| **Strait of Hormuz** (hull) | **7.5 – 10%** | ~5% [7/10-11] — **corrected, see below** | **7/22** | **19d 🔴** | Marcus Baker, Marsh global head of marine → Platts | FALCON |
| **Southern Red Sea** (hull) | **>1%** | ~0.75% [7/21]; 0.3% pre-Houthi-announcement | 7/23 | 18d 🔴 | Reuters / Insurance Journal / Al Jazeera 7/23 | FALCON |
| **Bab al-Mandab** (AWRP) | **~0.5%** | — | 7/23 | 18d 🔴 | Al Jazeera 7/23; FALCON KB-039 | FALCON |
| **West Coast Saudi** (call *without* chokepoint transit) | **0.1%** | — | 7/23 | 18d 🔴 | Al Jazeera 7/23 | FALCON |
| **Black Sea** (hull) | **>1%** (one broker ~1.5%) | ~0.6% | **7/21** | **20d 🔴** | The Insurer 7/21 (OSPREY B-02; absence rows B-03/B-04) | OSPREY |

---

## ✅ STALE-CARRY CATCH #1 — CLOSED (raised 7/25, adopted 7/27)

The lane's first output was a catch on FALCON's canonical Hormuz carry (~5%, KB-FALCON-004, 7/10-11) against a live market print of **7.5–10%** [Marsh → Platts, 7/22] — ~12 days stale and roughly half the level.

**FALCON accepted it in full** and re-marked (their NEXUS_BRIEF 7/27: *"Hormuz 7.5-10%/hull (I was carrying ~5% — 12 days stale, half the market)"*). Per this file's own convention, **HAWK now re-points to FALCON's number and drops its own copy.** They also named a war-risk surface (`workbook/WARRISK.tsv`), scoped deliberately to Hormuz/Gulf/Red Sea theater premia so it does not collide with this synthesis lane — which closes the 🟠 "FALCON has no named war-risk surface" nudge that sat with PROME.

---

## ⚠️ CATCH #2 — RE-DIAGNOSED 2026-08-10, and the earlier framing on this file was WRONG

**What this file said on 7/28:** the Black Sea leg was content-stale, and I escalated it — carrying OSPREY's *"structurally unobservable"* language and their line that *"a named watch that cannot fire is worse than no watch."*

**🔴 THAT FRAMING IS WITHDRAWN, BY ITS OWN AUTHOR AND BY ME.** OSPREY withdrew *"structurally unobservable"* in the same session it raised it — it had been asserted off a **one-outlet** search set — and **I then carried the withdrawn form for 13 days.** FALCON separately withdrew a *"written scope limit"* clause that echoed it. *(Mechanism: the finding travelled and the retraction did not.)*

**The corrected diagnosis, agreed by all three desks on 2026-08-10:**

> **BOTH legs are EVENT-DRIVEN OBSERVABLE.** A war-risk AWRP is a **privately-negotiated per-voyage number** that reaches print only when a journalist canvasses brokers on a **step-change**. **Between step-changes there is genuinely nothing to print — so absence rows are CORRECT, and FALCON's staleness gate firing continuously is the design working, not failing.**

**⇒ The distinction decides the ask, which is why it is not pedantic.** *"Unobservable"* invites a **scope limit** — writing the leg off. *"Event-driven observable"* invites a **SOURCE UPGRADE**. **THE FLEET ASK IS ONE ITEM, BOTH LEGS: a broker/underwriter source upgrade. NO scope limit on either.** OSPREY has already built its half (1 → 8 outlets, plus Baltic **TD6** as a daily continuous tripwire); FALCON will not advance its data clock without a re-pulled figure and will not widen its gate to silence it.

### 🔴 PROVENANCE — the Gulf leg is ONE NAMED INDIVIDUAL, and my own capacity arithmetic rides on him too

**The 7.5–10%/hull Hormuz premium AND the appetite-vs-capacity arithmetic I built on top of it (~$2.5–3bn global hull capacity against sub-$100M vessels ⇒ ~25× placeable) both trace to MARCUS BAKER, global head of marine at Marsh, in the SAME 7/22 reporting.** One source, not the three outlets I originally listed. **HTTP 403 at both S&P Global and Nautilus on 8/10 — nobody in this fleet has fetched the Marsh primary.** FALCON, as the desk carrying the number as canonical, volunteered to fetch it. **Until then this leg is single-source and re-rated down.**

### Vintage traps on this lane, for anyone re-searching it

- **Maritime Executive "Russian and Ukrainian Strikes Are Raising War Risk Insurance Costs" is 2026-01-15**, not August — its $800k/Suezmax figure is a January number and its attacks are January events.
- **An "about 2%, double late July" Black Sea figure circulating 8/9 does NOT survive** — origin `agbull.com`, an agricultural-trading relay compilation with no named source for the number, **and it is quoted on a $30M grain bulker in the Odesa corridor**. Ukrainian-corridor grain hulls and Novorossiysk tanker AWRP are different books with different loss experience. *(OSPREY traced and refused it.)*

### Live datum that is NOT a premium and must not be used as one

**CPC charter rates doubled to $338,000/day** [Times of Central Asia 8/7]; Baltic **TD6** (135kt CPC→Augusta) ~WS310, TCE ~$203,300/day on 7/27. **Freight embeds tightness, tonnage and voyage economics as well as war risk, and carries no geopolitical attribution.** But the contrast is itself evidence for the event-driven diagnosis: **the market is paying more while nobody publishes a rate.**

### 🎯 PRE-REGISTERED DIRECTION TEST — free, unclaimed, registered 2026-08-10

Capacity is not binding (~25× placeable); **appetite is, and appetite responds to ASSURANCE rather than physics.** The two legs have just taken **opposite** assurance shocks:

| Leg | Assurance shock since last print | Physical trend | **Predicted next print** |
|---|---|---|---|
| **Black Sea** | 🟢 US-brokered CPC carve-out, 8/8 | 🔴 **Worse** — six named refineries in six days | **DOWN vs >1%** |
| **Hormuz / Gulf** | 🔴 ADNOC hull hit in-strait 8/8; first Persian-Gulf-coast strike 8/9; SNSC maximalist list | 🟡 Mixed — pause holds, zero crude lost | **UP vs 7.5–10%** |

**If Black Sea prints flat-or-up while kinetic tempo is at a campaign high, loss experience dominates appetite, and the capacity arithmetic is a curiosity rather than a mechanism — say so.** *Historical precedent for the mechanism, carried strictly as JUNE HISTORY: Lloyd's of London launched a $400M Hormuz war-risk consortium on 2026-06-19 (Chubb lead) within days of a de-escalation headline, with no physical change to the strait — capacity CREATED on assurance.*

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
