# BOND — Trade Recommendations

**Last Updated:** 2026-08-20 by BOND — **core-file sweep (Will-requested after a run of reversals): 6 stale marks + 1 FALSE claim corrected in this file; marks stripped rather than re-stamped, because re-stamping rots again in two sessions.** *(Prior entry:)* 2026-08-18 by BOND — **staleness sweep (Will-tasked).** ⚠️ **This file was 21 days stale and described the 7/28 7Y and the 7/29 FOMC as "two live gates, both resolving within 48 hours." Both resolved three weeks ago.** *(Prior: 2026-07-28, itself a 27-day refresh that had been naming the resolved 7/9 refunding as "the live gate" 19 days after it cleared. **That is n=2 for this file specifically: it has now twice carried a resolved event as the live gate.** The fix is the Next Review section at the bottom, which is now dated and pruned rather than appended to.)*
**Regime:** 🟡 WATCH escalating (thesis-level) · STATUS carries **🟠 ELEVATED** (current-state). *Documented, not a drift: THESIS grades the durable thesis, STATUS grades today's tape — they are different scales and are allowed to differ. If they ever move in opposite directions, that is the signal to reconcile.*
**All live levels/scores → `STATUS.md`; this file carries posture and gates, not marks.**
**⚠️ CORRECTED 2026-08-20 — THIS LINE WAS FALSE.** It read *"NO REGISTERED PREDICTION COVERS ANY GATE BELOW; `thesis/PREDICTIONS.tsv` IS EMPTY… nothing has been registered since [8/15]."* **It was already false the day it was written** (BND-14/15/16 were all registered 2026-08-18) and is emphatically false now. **Live book: `BND-15` OPEN** (DFII10 no close ≥2.50 through 8/29 — *this one does cover gate (a) below*) **and `BND-17` OPEN** (8/20 30Y TIPS indirect, a Will-directed calibration row that covers no gate). **T6 and T7 are frozen tests, not BOND predictions.** *(This line previously named `BND-13` as "the registered prediction covering today's gate." It resolved the day it was written.)* **Nothing in the live regime is falsifiable on a BOND-authored instrument — a standing gap, restated here because it is a trade-discipline problem, not just a bookkeeping one.**

---

## Current Bottom Line

**Nothing has changed in the book and nothing is owed. TLT puts HOLD, no add; Will's NO-ADD (7/16) stands, $500 banked.**

**The long end remains engaged and the arm is intact — but ⚠️ the 8/18 phrasing "one gate is closing" was reversed by the very next print and is retracted (see gate (a)).** ⚠️ **Marks removed 2026-08-20 per this file's own rule (line 5): the 30Y level, the consecutive-session run and the 10Y distance all lived here as hardcoded numbers and all three were stale — the run figure was the twice-corrected one ("29", true value 31). LIVE LEVELS AND THE RUN → `STATUS.md`, recomputed each boot; this file states POSTURE only.** 10Y remains above the arm line; **DFII10 2.44 [8/17] — 6bp from the 2.50 add-gate, +5bp in two sessions** after three weeks of moving away. **Closest approach this cycle remains 2.47 (7/31) = 3bp; this is the second-closest.** **No pre-registered add-gate has fired and I am not manufacturing one.**

⚠️ **Worth saying plainly, because both facts are true today and neither is an add-gate: the position is working AND the thesis channel is confirming.** TLT mark → `STATUS.md` *(this read a hardcoded "$81.35 [8/17]" until 8/20; the 8/19 close is PROME-ruled $83.02).* **That is exactly the configuration in which a desk talks itself into an unregistered add.**

**All four add-gates, current status:**

| Gate | Status |
|---|---|
| **(a) DFII10 >2.5 sustained** | 🔴 **LIVE — the ONLY survivor.** ⚠️ **Corrected 8/20: this cell read "6bp away [2.44, 8/17], +5bp in two sessions" — stale AND pointing the WRONG WAY.** DFII10 **backed off to 2.41 [8/18]**, i.e. **9bp away and widening**, not closing. Closest approach this cycle: **3bp (2.47, 7/31).** Never fired. **Distance is recomputed every boot by `monitors/boot_recompute.py` and published in `STATUS.md` — do not read a distance off this row.** Covered by `BND-15`. |
| (b) 30Y >5.0 / 10Y >4.6 held 5 sessions **+ a weak auction** | ❌ **DEAD.** Levels long met; **the auction leg was RE-TESTED at the August refunding and did not fire** — no composition failure at any tenor, indirect at/above median at all three. |
| (c) Composition failure at the 7/28 7Y | ❌ **RESOLVED, DID NOT FIRE** (needed indirect <56.4% AND dealer >13.2%; printed 70.15% / 12.97%). |
| (d) Hawkish FOMC repricing 7/29 | ❌ **RESOLVED, DID NOT FIRE — and it died the right way.** The post-FOMC repricing ran **dovish**: ORACLE aggregate hike-2026 71.5% → **54.5%** [8/12], Sept-specific **28.5% PM / 30.0% Kalshi** [measured 8/18]. |

**Short-credit still NOT supported, and the case is WEAKER than three weeks ago.** Primary open, **zero pulled deals**, ~$56B IG priced in the week to 8/14 without spread disruption. **HY (live level → `STATUS.md`; this read a hardcoded "**275 [8/18]** *(was "267 [8/14]" until the 8/20 sweep)*" until 8/20) round-tripped the July widening and sits below where it began**; CCC **1030 [8/19]**, up 6 of the last 8 sessions and 4bp under the 2026 max (1034, 7/31) — ⚠️ **not a series high; that label is retracted 8/20** (series max 1137, 2025-04-07). ⚠️ **This desk has now made and retired a credit call twice in three weeks off index prints that round-tripped — credit is not currently a BOND signal.**

⚠️ **The methodological change from v1.1.3 stands and was TIGHTENED 8/18:** auction gates are **composition-keyed and TAIL-FREE** (no when-issued published by TreasuryDirect ⇒ a tail-keyed gate is unscoreable by construction — **canonical statement + `re-test: 2026-11-01` → `monitors/AUCTION_HEALTH.md` §1; it is a fact about THAT SOURCE, not about tails**), **and as of 8/18 the composition cut-offs are stated PER TENOR rather than hardcoded to the 7Y.** The 7Y's 56.4% indirect bar applied to a 10Y auction (min 63.95%) or a 30Y (59.52%) is simply the wrong bar — that error was live in this file's Reactivation Matrix and in `thesis/THESIS.md`'s kill criterion until today.


---

## Active / Legacy Recommendations

| # | Trade | Current Posture | Conviction | Why | Hold / Add / Kill Rules |
|---|---|---|---|---|---|
| 1 | TLT puts | **HOLD, no add** | 2.5/5 | Arm-#2 RESOLVED-ARMED. **All levels live in `STATUS.md` — this cell states POSTURE, not marks.** ⚠️ **CORRECTED 2026-08-20: this cell read "29 consecutive sessions" (true: **31**), "10Y 4.68" (true: 4.71 [8/18]) and — the one that mattered — **"DFII10 … moving toward it" when it moved AWAY** (2.44 [8/17] → 2.41 [8/18]). The only live add-gate was described as closing on the trade surface while it was widening.** ⚠️ *(DFII10's "series high" label is RETRACTED — `KB-BND-108`; correct label is a post-2023 / ~2.75yr high.)* **But no add-gate has fired, and the structural confirmation is not merely absent — it was actively RE-TESTED and came back negative:** the August refunding cleared with indirect at/above trailing-12 median at all three tenors and the 30Y at 5.216% (highest since 2001). **Composition has not broken at any tenor since 7/9, across twelve consecutive tests.** | **Hold** current. **Add ONLY on:** (a) **DFII10 >2.5 sustained — the ONLY surviving gate; 9bp away and it moved AWAY** *(this read "7bp" — a derived distance that never inherited the level fix)*; (b) 30Y >5.0 / 10Y >4.6 held 5 sessions **+ a weak auction**; (c) **a composition marker at the 7/28 7Y** = indirect <56.4% **AND** dealer >13.2% (pre-reg branch A or D). (d) **hawkish FOMC repricing 7/29.** ⚠️ **(b), (c) and (d) are RESOLVED-AND-DEAD — retained as the record, NOT as live gates.** **Kill:** 10Y <4.15 AND 30Y <5.0 for 3 sessions AND clean auctions. 🔴 **60-DTE review: OVERDUE. Sep-30 expiry ⇒ 60-DTE was 2026-08-01; at 2026-08-20 the leg is 41 DTE and this review has no record of ever running.** Escalated to Will 8/20. **Crowding caveat below applies to every add.** |
| 2 | Credit-equity lead | **Inactive watch — and it moved FURTHER AWAY** | 1/5 | HY level → `STATUS.md` (**273 [8/19]**), ~10bp above the 263 cycle trough; the July widening fully round-tripped. **The reactivation band (≈338–363) is ~65bp away** — *carried at "~71bp" off a stale HY 267 [8/14] until 8/20; a derived distance does not inherit a level fix.* | **Reactivate:** HY OAS +75–100bp from trough (**≈338–363**) while VIX <20; strongest if the fast layer leads cash (true divergence — sign-check rule in `monitors/CDX_CASH_BASIS.md`). **Not close.** |
| 3 | Short AI-credit (basket) | **NOT proposed — noted for structure** | 1/5 | GS **and** JPM launched tradeable/shortable 18-name AI-credit baskets the same week (7/23), avg spread **319bp** ≈ 40bp wide of the HY index, executable as cash **or TRS**. A bearish AI-debt expression did not exist a week ago. | **No BOND trade.** Recorded because TRS execution means positioning can build faster than the cash float allows, **in either direction** — a crowding-formation mechanism, not a signal. Basket is the **neocloud/compute** tier, not hyperscalers. VULCAN owns the thesis; **do not read the 319bp as a tradeable differential** (equal- vs value-weighted, point-in-time, no history). |

> ⚠️ **Positioning-crowding note — ⛔ THE URGENCY CLAUSE IS EXPIRED AND IS RETAINED ONLY AS THE RECORD.** It read *"this is LIVE in the next 24 hours"* and *"tomorrow is a two-sided FOMC"* — **written 2026-07-28 about the 7/29 FOMC, still asserting a live 24-hour window 22 days later.** *(An expired date carrying a pending verb: `[[finding_dated_carry_item_has_no_expiry_check]]`.)* **The MECHANISM below is durable and still applies; the timing is dead.** Consensus is heavily short-duration; the expression is crowded; the short-covering-rally risk fires on a **dovish surprise** — and it materialised on 8/19, not on an FOMC: `sb0607` doubled long-end buybacks and TLT rallied **+1.67%** in a session. The 6/26–29 rally to a 7-week 10Y low is what that risk looks like when it materialises. **Practical consequence: this argues against adding into the meeting even if a gate fires on the 7Y this afternoon** — a fired gate plus a crowded book plus an untelegraphed two-sided event is exactly the setup where being right on direction and wrong on timing is expensive. Any add that fires today should be surfaced to Will with this note attached rather than sized mechanically.

---

## Closed / Expired

| Trade | Outcome |
|---|---|
| **HYG $75P Jun** | **EXPIRED** far OTM (June expiry; HY never reclaimed 300; issuance boom). Reopen the *thesis* only on HY OAS >300 with velocity. |

---

## Reactivation Matrix

| Signal | BOND Interpretation | Trade Implication |
|---|---|---|
| **Composition failure at any coupon auction** — **indirect below that tenor's own trailing-12 MIN _and_ dealer above its MAX** *(per-tenor as of 8/18: 3Y 53.99/19.50 · 7Y 56.42/13.14 · 10Y 63.95/16.16 · 20Y 55.17/17.59 · 30Y 59.52/17.46 — **re-derive at every grade, these drift**)* ⚠️ **Re-specified 8/18: this row hardcoded the 7Y numbers as if general.** | End-demand weakness. ⚠️ **The "meeting record dealer stock" half of this configuration is GONE** — long-end dealer inventory is **−14.3% off its 6/24 peak** and unwound benignly, so the demand-hole scenario is **less** pre-positioned than this file claimed for six weeks. **Note: cover alone does NOT qualify** — the 7/27 5Y printed the lowest BTC since Sept-2022 and did *not* fire this, because indirect rose and dealers didn't absorb. | **Primary TLT-put add re-arm**; signal LIQUID immediately. |
| ⚠️ **30Y >5.0 held 5 sessions — THIS LEG HAS FIRED** (8 consecutive closes 7/7→7/16; BND-12 resolved FALSE) | Sustained *level* break. **But BND-12 resolved FALSE with the mechanism INTACT** — "expensive intensified, still not broken." | ⚠️ **DOES NOT RE-ARM AN ADD ON ITS OWN.** *(This row previously read "TLT add re-arms (pair with nearest auction evidence)" — under-specified, and read alone it would have called an add on 7/16, the day Will explicitly decided NO-ADD. The controlling gate is the **conjunctive** one in Active Recommendations 1(b): the level breach **AND a weak auction**. The level leg is met and has been for weeks; **the auction leg is what is missing**, and the 7/27 5Y gave a cover marker without a composition failure.)* Long-end →4 still requires DFII10 >2.5 or a composition failure. |
| **DFII10 >2.5% sustained** | Real-yield stress regime | **TLT-put add re-arm — the NEAREST live gate.** *(This row read "currently 2.20 and retraced" for 27 days; DFII10 is now at a series high a handful of bp away — live level → STATUS.)* |
| **MOF actual FX intervention** (verbal stage; USDJPY through the 40-yr low, 165 = next threshold — **SAM owns the level**) | Mechanical UST reserve selling from $1T+ holdings (FL-BND-11) | Long-end supply shock — TLT downside accelerant; coordinate SAM/LIQUID. |
| HY OAS >300 ×3 sessions | Credit watch reopens | Price HYG/JNK downside, no blind entry. |
| HY >350 + pulled deals | Issuance freeze | HYG/JNK downside proposable to Will. *(Mechanism still not engaged: primary open, zero pulled deals, record June IG absorbed 3.9x. But "running in REVERSE — boom" is retired as of 7/23 — spreads have re-activated even though access has not closed.)* |
| Fast layer breaks while cash stays TIGHT (true divergence) | Synthetic leading cash | Early short-credit re-entry support. *(**Re-run 8/18: NO divergence** — HYG/IEF 0.8567, z20 **+1.40**, 98th pctile. ⚠️ **CONFOUND NOW NAMED: this ratio rises MECHANICALLY in a rates-led selloff because the IEF denominator falls on duration** — "rich" is partly an artifact of the move being tracked. It survives only because cash HY at 267 agrees from an unconfounded instrument. See `monitors/CDX_CASH_BASIS.md`.)* *(Prior 7/28 note:* Cash HY widened +11bp while HYG/IEF stayed RICH — z20 −0.08, 79th pctile — so the fast layer did NOT confirm; that is a repricing, not credit stress. ⚠️ The quieter signal: **LQD/IEF z20 negative every session for two weeks**, IG credit-excess softer and more persistent than HY.)* |
| SOFR-IORB positive after weak auction (non-quarter-end) | Auction stress funding through repo | Systemic confirmation; escalate LIQUID/PROME. *(**+1bp [8/17]** — flipped positive, **and it does NOT qualify**: this row requires a **weak auction** and the August refunding was firm at all three tenors. SOFR also printed 3.66 on 8/04 and 7/31; the spread has oscillated −3 to +1 all month with no trend. **Recorded because the leg is registered, not because one print means anything.**)* |
| Treasury buyback long-end accept-cap lifted | YCC-lite / stealth suppression | Direct TLT-puts event. *($2B cap held.)* |

---

## Cross-Agent Dependencies

| BOND Signal | Confirmed By | Who Needs It |
|---|---|---|
| Composition failure at a coupon auction *(last tested at the August refunding 8/11–13 — NOT FIRED at any tenor)* | LIQUID repo pressure / FR2004 stock — ✅ **FR2004 is LIVE and current through the 8/05 as-of** *(the "blind since 6/17, 5 prints owed" note was false from 7/28 and sat here 21 days)*. ⚠️ **Still owed from LIQUID: the refuse-or-confirm on repo/funding stress 7/01→7/15 — if it exists, the dealer unwind re-reads as FORCED de-risking, which is MORE bearish.** Re-asked 8/18. | PROME, LIQUID |
| JGB-FX transmission (channel 6) | SAM (BOJ/MOF/yen) | SAM, HENRY, LIQUID |
| Issuance freeze (dormant — boom) | REGINALD refi burden / BROCK private marks | REGINALD, BROCK, HENRY |
| Long-end break | HENRY vol regime + LIQUID funding | PROME, LIQUID, HENRY |
| FHLB advance stress (new coverage) | REGINALD bank-level reads | REGINALD, PROME |

---

## Rejected / Downgraded

| Trade | Prior Posture | New Posture | Reason |
|---|---|---|---|
| HYG $75P Jun | Mar 26 conviction 4/5 | Expired | HY 319→263; issuance boom; no freeze. |
| TLT-put aggressive add | 5/19 pre-approved on two-tail gate | Lapsed unfired | Every gate 5/20→6/25 cleared clean. Re-armable only via the rules above. |
| Short-credit via CLO canary | BND-04 watch | **Dead (BND-04 FALSE)** | BSL AAA never near SOFR+160 in H1 (peak S+127); MM near-miss S+158 noted. |

---

## Next Review

> ⚠️ **This section is now DATED AND PRUNED, not appended to.** It has twice carried a resolved event as "the live gate" (the 7/9 refunding, 19 days after it cleared; then the 7/28 7Y and 7/29 FOMC, 21 days after). **Every row below was verified at a primary on 2026-08-18.**

- **🔴 Wed 8/19 — TWO EVENTS, ONE DAY.** **① US 20Y NEW ISSUE $16B, 1PM ET** (`912810UX4`, nominal — **date + instrument verified at the TreasuryDirect primary**; wire coverage had this as "Thursday 8/20", which is a *Japan* 20Y date). Composition-failure test: **indirect <55.17% AND dealer >17.59%.** ⚠️ *Both cut-offs come from the same auction (2026-02-18) — a narrow gate, flagged at authorship.* **② FOMC minutes 2PM ET — T7 resolver.** Grade on the **7/29 data vintage** (3-mo payroll avg 111K), never today's +20K. **Neither event is an add-gate on its own.**
- **🟠 Thu 8/20, 1PM ET — US 30Y TIPS REOPENING $8B** (`912810US5`, `tips: Yes`). **The real-money referendum on the real-yield level, with DFII10 9bp from the only live add-gate** — the cleanest read available on whether the term-premium expansion is being validated by real-money duration buyers. ⚠️ **No composition gate is set and none will be: the base is n=3.** *(8/20 also carries SAM's JGB 20Y — two countries, two tests, hold them separately.)*
- **🟠 Tue 8/25 · Wed 8/26 · Thu 8/27 — 2Y / 5Y / 7Y month-end cluster.** The **5Y** is the one with a live question: it fired the 7/27 cover marker (BTC 2.28, lowest since Sept-2022). **A repeat with composition intact makes that a pattern rather than a print**, and bears on `KB-BND-092` (basis-trade withdrawal), still unadjudicated by LIQUID.
- **🟡 Fri 8/28 _or_ Mon 8/31 — MOF monthly Japan FX reserves. ⚠️ DATE UNVERIFIED, verify asked of SAM.** First independent size read on the 7/30-31 operation. **n=3 of BOND's unverified-event-date class — the 7/23 ECB and 8/05 QRA windows both passed ungraded for exactly this.**
- **🔴 Sat 8/29 — T6 hard close + HEN-42.** T6 trigger **MEASURED 8/18 and NOT FIRED** (PM 28.5% / Kalshi 30.0% vs the <25% line). **Three live spec defects flagged to LIQUID as co-owner; frozen text unedited.**
- **Daily:** **DFII10 vs 2.50 — the only live gate; `BND-15` is registered against it firing.** ⚠️ *Distance deliberately NOT carried here (read it in `STATUS.md`, recomputed each boot) — this line hardcoded "6bp [2.44, 8/17]" until the 8/20 sweep, by which point it was 9bp and had moved AWAY** · `DGS30` vs 5.0 (29-session run) · **watch for FRED to publish `DGS30` 8/17**, which is still absent and is what would grade the 19-year-high close · HY vs 300 (33bp, moving away) · CCC vs 1100 · USD/JPY vs 165 (159.65 — moving *away*).

> **Resolved and removed** (each had sat here as "live" — the point of the pruning rule): 7/28 7Y **(`BND-13` TRUE, branch B, no composition failure)** · 7/29 FOMC **(HELD; the repricing ran dovish, add-gate (d) resolved DID-NOT-FIRE)** · 7/31 **(`BND-01` FAILED — HY never within 63bp of 350)** · 8/03 P3 start gate **(passed 8/03, never started — still owed, tracked in SCRATCH not here)** · 8/05 QRA **(passed UNGRADED — date was pattern-inferred and never verified; do not grade retroactively off secondaries)** · **8/11–8/13 August refunding (GRADED 8/18, five days late — no composition failure at any tenor; it was never on this list because it was never docketed)**.
