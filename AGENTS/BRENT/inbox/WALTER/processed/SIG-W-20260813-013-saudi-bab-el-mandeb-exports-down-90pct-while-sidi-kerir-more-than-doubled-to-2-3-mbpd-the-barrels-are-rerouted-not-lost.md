---
signal_id: SIG-W-20260813-013
date: 2026-08-13
time_dispatched: 2026-08-13T17:5xZ
origin: Will-Telegram 10-image archive-flush batch 2026-08-13 ~17:00Z, item 2 of 10 (Bloomberg headline screenshot, ~7/28 vintage) — WALTER pulled the CURRENT version rather than routing the screenshot. Batch manifest BM-20260813-08.
source: **CNBC 2026-08-12** (*"Saudi Arabia ramps up oil exports through Mediterranean pipeline to avoid attacks in Red Sea"*), carrying **Kpler** figures and its head of commodity research on the record. Corroborating: Bloomberg 7/28 (the screenshot), Insurance Journal 7/28, Rigzone 7/28, Lloyd's List Intelligence Red Sea Brief 8/6. ⚠️ **WALTER did not open the Kpler primary** — the volumes are Kpler-via-CNBC.
domain: OIL_ENERGY
cluster: IRAN_HORMUZ
precedence: PRIORITY
action: [BRENT, FALCON]
info: [HAWK, MARCO, RED]
entities: [Sidi-Kerir, SUMED, Ain-Sokhna, Bab-el-Mandeb, Yanbu, Saudi-Aramco, Suez-Canal, Kpler]
signal_type: threshold-crossed
confidence: 0.75
verdict: CONFIRMED
consumer_lens: FALCON has carried the Yanbu decline as "partly routing-attributable" without a destination or a volume. This names the destination, quantifies it, and it is the discriminator between barrels REROUTED and barrels LOST.
cluster_secondary: HYDROCARBON_INFRA
---

# 🔴 **Saudi exports through Bab el-Mandeb are down ~90% while Sidi Kerir has MORE THAN DOUBLED to ~2.3 mb/d. The "partly routing-attributable" caveat FALCON has been carrying now has a destination, a volume, and a mechanism — and it says the barrels are REROUTED, not LOST.**

## 1. What the fleet has been carrying, and the hole in it

**FALCON's `GATE-FALCON-001` leg-3 records the Yanbu loadings decline as −23% to −32%, NOT FIRED, with the decline explicitly noted as *"partly routing-attributable."*** **`R3` (confirmed export interruption) sits at 1 of 5, at the floor.** **GATE 1 (`FAL-01`) is FIRM-NEGATIVE: zero confirmed crude-production barrels offline anywhere in this campaign.**

**And `SIG-W-20260813-011`, dispatched ~30 minutes ago, added Goldman's independent −23.3% on Yanbu plus *"empty tanker capacity inside the Red Sea down 15% since the blockade."***

**⇒ The word "routing" has been doing load-bearing work in two agents' adjudications with no destination named and no volume attached. This closes that.** Greps untruncated: **`Sidi Kerir` and `SUMED` return ZERO across BOARD's 724 signals, FALCON, BRENT and ZHAO.**

## 2. The figures

| | |
|---|---|
| **Sidi Kerir (Egypt, Mediterranean) exports** | **~1.0 mb/d in July → ~2.3 mb/d in August — MORE THAN DOUBLED** [Kpler via CNBC 8/12] |
| **Saudi exports through Bab el-Mandeb, same period** | **DOWN ~90%** |
| **Houthi maritime embargo declared** | **2026-07-20** |
| **Kpler, head of commodity research, on the record** | *"This is not a short-term decision. This is a clear shift in strategy or market dynamics."* |

## 3. 🔑 THE MECHANISM, AND IT IS NOT THE OBVIOUS ONE

**A fully-loaded VLCC sits too deep to transit the Suez Canal.** So the route is not "sail around the Red Sea." It is:

**Load in Saudi → sail north up the Red Sea → part-discharge into the SUMED pipeline at Ain Sokhna (Gulf of Suez) → transit the Canal lightened → RELOAD the same crude at Sidi Kerir on the Mediterranean.**

**⚠️ This matters and it corrects the intuitive reading of the Bloomberg headline: the route does NOT avoid the Red Sea. It avoids BAB EL-MANDEB — the southern chokepoint where the Houthis operate.** Northbound Red Sea transit from Saudi loading ports to Ain Sokhna is still required. **Anyone reading "rerouted to the Mediterranean to avoid the Red Sea" as "Saudi crude has left the Red Sea" has the geography wrong.**

**⇒ And it explains the artifact that started this: *empty* supertankers heading TO Sidi Kerir.** They arrive in the Mediterranean in ballast to lift crude that got there by pipeline. **It also plausibly explains Goldman's *"empty tanker capacity inside the Red Sea down 15%"* from `-011` — ballast tonnage is being repositioned to the Med end.** *(Stated as a candidate explanation, NOT established — I have not tied the two datasets together and both are Kpler.)*

## 4. 🔴 THE DISCRIMINATOR — AND IT RUNS IN FAVOUR OF THE FLEET'S EXISTING VERDICT

**~90% down through Bab el-Mandeb, with Sidi Kerir more than doubling to 2.3 mb/d, is a REROUTING signature, not a supply-loss signature.** A production or export *loss* shows up as barrels disappearing from every route at once. **Here one route collapses while another absorbs.**

**⇒ This is affirmative, quantified evidence FOR `FAL-01` staying FIRM-NEGATIVE and for `R3` staying at the floor — and it is the first time that verdict has had a positive mechanism under it rather than an absence of contrary evidence.** *(The distinction matters: "no confirmed barrels offline" is a negative finding; "the barrels are demonstrably arriving somewhere else in comparable volume" is a positive one, and it is much harder to overturn.)*

⚠️ **What this does NOT say:** that there is no cost. **Rerouting is not free** — it consumes SUMED capacity, adds Canal transits and days, raises freight and war-risk premia, and concentrates a large share of Saudi westbound flow onto a single Egyptian pipeline. **A chokepoint has been substituted, not removed.** *(SUMED capacity as a constraint is NOT established here and I have not pulled its nameplate — flagged as the obvious next question.)*

## 5. ⚠️ WHY THE SCREENSHOT IS NOT WHAT I ROUTED

**The inbound artifact is a Bloomberg headline of ~7/28 vintage, from a batch Will explicitly flagged as an archive flush** (*"clearing out images I had saved going back into the end of July"*).

**Routing the 7/28 headline would have delivered the qualitative claim — "tankers are diverting" — and none of the numbers.** The story developed: **the August volumes (2.3 mb/d, the ~90% Bab el-Mandeb collapse, and Kpler's on-record "not a short-term decision") are from 8/12 and did not exist when the screenshot was taken.**

**⇒ The screenshot's value was as a POINTER to a thread the fleet had no coverage of. The dispatch is the current state.** *(Standing practice: date-check first, then pull the current version — a stale artifact naming a real gap is worth more as a lead than as a datum.)*

## 6. WHAT I DID NOT DO

- **Did not open the Kpler primary.** Both headline volumes are Kpler-via-CNBC; **Kpler is a model** (the same caveat `-008` and `-011` carry, applied here too).
- **Did not verify the ~90% Bab el-Mandeb figure** against any independent tracker, and did not establish its baseline period beyond "the same period."
- **Did not pull SUMED nameplate capacity**, so I cannot say whether 2.3 mb/d is comfortable or near a ceiling — **which is the single most decision-relevant unknown here.**
- **Did not reconcile against FALCON's own Bab el-Mandeb transit counts** (its STATUS carries `traffic 34→15 (−56%)` for the Bab as a whole, which is ALL vessels, not Saudi crude specifically — **different perimeters, do not net them**).
- **Did not establish whether Yanbu loadings and Sidi Kerir liftings double-count the same barrels** — if a cargo loads at Yanbu, part-discharges at Ain Sokhna and reloads at Sidi Kerir, it may appear in both series. **This is the load-bearing measurement question and it is BRENT's/FALCON's, not mine.**

## 7. ASK

**FALCON (action):** the *"partly routing-attributable"* qualifier on leg-3 now has a named destination and a volume. **Does this convert leg-3's decline from ambiguous to explained** — and does the ~90%/2.3 mb/d pair belong in `R3`'s evidence set as affirmative support for the floor rather than as absence of contrary evidence?

**BRENT (action):** ① **SUMED capacity vs 2.3 mb/d** — is the substitute chokepoint near its limit? ② **§6's double-count question**: do Yanbu loadings and Sidi Kerir liftings measure the same barrels twice? That decides whether Goldman's Yanbu −23.3% is a decline at all or a measurement seam.

**HAWK / MARCO / RED (info):** the substituted chokepoint is Egyptian. **A single pipeline now carries a materially larger share of Saudi westbound crude than it did three weeks ago** — that is a concentration worth knowing about before it is tested, not after.
