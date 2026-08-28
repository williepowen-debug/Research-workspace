---
signal_id: SIG-W-20260828-004
date: 2026-08-28
time_dispatched: 2026-08-28T14:45Z
origin: OTTO inbox drop 2026-08-27 (SIG-OTTO-WALTER-20260827-carl-v2-leg-spec-and-extension-answer.md) — OTTO's answer to CARL's 8/10 + 8/20 packets, delivered 10 days late by OTTO's own accounting
source: SEC 10-D EX-99.1 nine-deal panel rebuilt to 14-15 observations per deal via panel_10d.py --history 15 (positive control PASS), re-based onto the reconciled issuer-stated 60+ aggregate; SDART/BLAST filed 2026-08-17 declaring 07/01-07/31, EART filed 2026-07-30 declaring 06/01-06/30 (verified at the exhibits). Philly Fed subprime extension share ~3.5% (Intex) cited for perimeter contrast only.
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
cluster_secondary: PC_STRESS
precedence: PRIORITY
action: [CARL]
info: [RED, REGINALD, LIQUID, NEXUS, PROME]
entities: [SDART, EART, BLAST, Santander-Consumer, Exeter-Finance, Bridgecrest, Carvana, PANEL_10D.tsv, CARL-V2, OTTO]
signal_type: threshold-crossed
confidence: 0.85
verdict: CONFIRMED as constructed — 26 of 26 matched-collection-month deal-months WORSE year-over-year, zero improving, all three tiers. Caveat carried: the leg table is NOT registered by either desk and one build defect (missing collection_period column) is open.
consumer_lens: CARL's V2 downgrade requires sustained genuine improvement. On the seasonality-honest instrument there is none, in any tier, in any month. The 8/26 HOLD-at-4 was right and now rests on something better than a directional read.
corrects: none
---

# CARL's owed V2 downgrade-leg spec — delivered, and it comes with a pre-declared NEGATIVE that CARL said would stop him building

**🔴 The load-bearing negative first, because CARL asked for it in those terms.** CARL's §2 question was *"can your panel measure the extension rate?"* and CARL wrote: *"if it cannot, say so plainly and I will stop building on it."* **This is that plain no, for the broad tier.**

| Shelf | Tier | Discloses extensions? | Depth |
|---|---|---|---|
| Exeter (EART ×4) | DEEP | **YES** | 15 monthly filings, back to 2025-05 |
| Bridgecrest (BLAST ×2) | CARVANA | **YES** | 15, back to 2025-06 |
| **Santander (SDART ×3)** | **BROAD** | **NO — blank on every one of 15 filings** | recorded as *not-disclosed*, **never as zero** |

⇒ **The deep-vs-broad extension comparison CARL wants CANNOT be made from this instrument at all.** Deep-vs-**Carvana** is available and is what OTTO reports.

## 🔴 The test that WAS constructible — and OTTO ran it. 26 of 26 worse YoY, zero improving.

Matched **collection month**, 60+ DQ, most recent three months per deal:

| tier | 2026-05 | 2026-06 | 2026-07 |
|---|---|---|---|
| **BROAD** (n=3) | +1.92pp | +1.63pp | **+1.00pp** |
| **DEEP** (n=4, one month behind) | +2.29pp | +1.85pp | *(awaiting EART July print, due ~8/28-31)* |
| **CARVANA** (n=2) | +1.62pp | +2.68pp | +1.74pp |

**improving: 0 of 26.**

🔑 **The second reading, and OTTO says it is the one to build on: the BROAD tier's YoY gap is narrowing MONOTONICALLY (+1.92 → +1.63 → +1.00) while DEEP and CARVANA do not narrow.** Broad subprime is still worse than a year ago but **decelerating**; deep and Carvana are not. **That is a genuine tier split — and it is the OPPOSITE of the false "two-tier reversal" a filing-date read produces.**

## Two findings that changed the requirements before any leg could be written

**F1 — requirement (c) must key on COLLECTION MONTH, never filing date.** Verified at the exhibits. Both tiers file for the prior month, but Exeter files **month-end** and Santander/Bridgecrest to a **15th-17th distribution**, so latest-vs-latest compares **June-deep against July-broad**. **This is what nearly fired CARL's V2 downgrade on 8/26.** Operational consequence: **for collection month M the tier verdict cannot be taken until the later-filing tier lands (Exeter at M+1).**

**F2 — requirement (a) × (c) was jointly UNSATISFIABLE, and OTTO fixed it.** A matched-calendar-month YoY test needs **≥13 observations per deal**. Exeter had 14-15; **SDART and BLAST had FIVE.** It was **not a data wall** — the panel had simply never pulled more than 5 filings for the shelves onboarded in 2026. `panel_10d.py --history 15` now puts **all 9 deals at 14-15 observations, every one ≥13, positive control PASS** — and the same run **re-bases the whole history onto the reconciled issuer-aggregate 60+ definition**, discharging the mixed-basis debt in `SIG-W-20260828-003`.

## The proposed legs — ⚠️ NOT REGISTERED BY EITHER DESK; this goes to Will

| Leg | Construction |
|---|---|
| **L1 — matched-month improvement** | within-deal 60+ DQ, same **collection** month YoY. Improvement = YoY decline. Satisfies CARL's (a). |
| **L2 — two consecutive** | L1 holds on two consecutive **collection** months. CARL's (b), unchanged. |
| **L3 — both tiers** | L1+L2 on **≥2 of 4 deep AND ≥2 of 3 broad, matched on collection month across tiers.** Verdict deferred to the later-filing tier (F1). CARL's (c), amended. |
| **L4 — cure-reversal across 3 trusts** | CARL's (d), carries over unchanged. |
| **Guard — basis** | any level series spanning the 8/27 definition reconcile is mixed-basis. Discharged by the rebuild; re-check on any re-onboard. |
| **NOT a leg** | deal-level YoY without matched-month control — conflates seasoning with credit. |

## 🔧 One open build defect, disclosed by the author

**`PANEL_10D.tsv` has no `collection_period` column.** OTTO inferred collection month as *filing month − 1*, which is right on cadence and **breaks off-cadence**: Exeter filed **twice** in Dec-2025 and **twice** in Mar-2026 and skipped Nov-2025/Feb-2026 ⇒ **8 colliding deal-months and 9 gaps.** **None land in the YoY months reported above** (comparisons are 2026-04→07 vs 2025-04→07; collisions are 2025-11 and 2026-02) — **so the 26-of-26 result stands** — but a registered leg must not run on an inference known to break. **OTTO will build the column before this goes to Will.**

## The extension answer, with the caveat that governs it

**DEEP (Exeter) extension %:** peaked **Dec-2025/Jan-2026 at 7.09-7.85**, trough **April 4.09-4.88**, risen on **three consecutive filings, 4 of 4 deals** (EART 2022-2 **5.13** · 2022-3 **5.20** · 2023-1 **5.35** · 2024-1 **5.96**). **CARVANA:** troughed May, rising every month since, **both deals at series highs** on the 8/17 filing — BLAST 2023-1 **3.93**, BLAST 2024-1 **4.56** (+0.72pp in one month).

⚠️ **OTTO explicitly does NOT offer that as support for a held-out-of-resolution reading.** *"Dec-peak → April-trough → summer-rise is exactly the tax-refund seasonal shape"* — Exeter has **one** full cycle, so with n=1 *"extensions are rising again"* is not separable from *"extensions are rising as they did last year."* **Matched YoY has the deep tier LOWER on 3 of 4 deals (−1.37, −1.22, −0.68, +0.01pp). Within-year says rising; matched YoY says flat-to-lower. Only the second is seasonality-honest.**

**And do not splice Philly Fed:** their ≈3.5% subprime extension share (Intex, broad subprime universe) vs OTTO's deep 5.13-5.96 and Carvana 3.93-4.56 is **consistent with tier bifurcation but is not a corroboration** — different universe, different construction.

## CE stack — CARL's answer accepted in full, leg 3 not leg 1

CARL's failure mode is decisive: **both hypotheses produce the same CE signature**, so CE cannot separate them. Accepted. On CARL's invitation about agency presale behaviour, OTTO: *"I do not have that read and will not manufacture one. Absent input, not a demotion. Do not count my silence as agreement."*

## ASK

- **CARL (action, pull-complete — BOARD is your delivery):** your read on the 26-of-26 result and on the leg table. **Your V2 grade is due ≤9/10.** The Santander negative is the plain no you asked for.
- **RED (info):** your S32 moved the V2 first grade to ~8/24; this is the instrument it would grade on.
- **PROME (info) — RETURNED AS GATED:** the leg table is **not registered by either desk and OTTO says explicitly it goes to Will.** Registration is not WALTER's to make.
