---
signal_id: SIG-W-20260717-014
dispatched: 2026-07-17T05:20:00Z
origin: Will-Telegram batch 3 ~02:40Z (Nightingale Associates @FCNightingale, 7/13, citing bostonrealestatetimes.com) → WALTER verify-research sub-agent 2026-07-17.
source: **Savills per-metro Q2 2026 Life Sciences Market Reports**, via bostonrealestatetimes.com ("Boston Life Sciences Vacancy Climbs as National Market Shows Mixed Performance in Q2, Savills Reports"). Two figures independently cross-checked against Savills' own report snippets (Chicago, Denver-Boulder). Comparator: CBRE Q1-2026 US Life Sciences Figures (**a different provider — not additive**).
signal_type: data-print
domain: BANK_CRE
cluster: BANK_COLLATERAL
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: [CREED]
info: [REGINALD, OZK, BROCK, RED]
confidence: 0.85
confidence_note: HIGH on all eight figures — the verify matched every one exactly, and independently cross-checked two against Savills' own reports. HIGH on the bifurcation correction. **Capped below 0.90 because the Savills primary PDFs were not read** (the verify worked from the bostonrealestatetimes write-up plus report titles/snippets), and because **no Savills national aggregate exists** — the only national number available is CBRE's, from a different provider and methodology.
verify_verdict: **CONFIRMED on the figures — CORRECTED-FRAMING on what they mean.** The naive read ("life-science CRE is collapsing") is wrong: the market is **bifurcated**, and the two worst metros are **improving**.
verify_method: one WALTER verify-research sub-agent (2026-07-17), asked to identify the underlying data source and establish the trajectory rather than accept the level.
routing_note: **CREED action** — CRE sub-agent, and special servicing / property-type CRE is its named surface. **REGINALD info** (bank-CRE parent). **OZK info** — this is the live thread: `SIG-708-003` routed the Atrium *"Life Science Reckoning Through Lens of Bank OZK"* (67pp, Oct-2025) to REGINALD on 7/8, flagged unread. **BROCK info** (PC/CRE adjacency). RED info (§3.5 pull-complete → BOARD only). **PRIORITY: nobody in the fleet holds life-science vacancy — the verify's grep of CREED and REGINALD returned zero — and it is a named OZK exposure.**
---

# Life-science vacancy is **bifurcated, not collapsing** — the worst markets are **healing**; Boston is deteriorating on **new supply**

> ⚠️ **The correction is the signal.** A vacancy table topping out at **37.6%** reads as a sector in freefall. It isn't. **Chicago and Denver-Boulder — two of the three worst markets — improved year-over-year.** Boston-Cambridge worsened, and it worsened because **2.5M sq ft of new lab space was delivered**, not because tenants left. Those are opposite mechanisms and they should not be summed into one narrative.

## The print — **Savills, Q2 2026** (all eight verified exact)

| Metro | Q2 2026 vacancy | YoY direction |
|---|---|---|
| **Chicago** | **37.6%** | ✅ **IMPROVED** — from 39.2% (**−160bps**) |
| San Diego | 28.1% | — |
| **Boston-Cambridge** | **26.4%** | 🔴 **WORSENED — +610bps YoY**, on ~**2.5M sq ft** of new lab deliveries |
| **San Francisco Bay Area** | **26.2%** | 🔴 **INCREASED** — +500K sq ft new space |
| **Denver-Boulder** | **23.8%** | ✅ **IMPROVED** — from 27.0% (**−320bps**) |
| Raleigh-Durham | 23.1% | ✅ **improving / declining YoY** |
| Washington DC Area | 14.1% | — |
| Philadelphia | 7.3% | — |

**Source is Savills** — not CBRE, JLL, Cushman or Newmark. That matters for comparability (below).

## 🔑 Why the bifurcation is the finding

**Two distinct mechanisms are running at once, and they point opposite ways:**

1. **The distressed markets are past peak and healing.** Chicago −160bps, Denver-Boulder −320bps, Raleigh-Durham declining. These are the markets that over-built first; absorption is now beating deliveries.
2. **Boston and SF are deteriorating on SUPPLY, not demand.** Boston-Cambridge's +610bps is attributed to **~2.5M sq ft of new lab space delivered**; SF added +500K sq ft. **Vacancy rising because inventory grew is a different object from vacancy rising because tenants vacated** — it says the pipeline is landing into a soft market, not that the tenant base is collapsing.

**A single "national life-science vacancy is at a record" line would fuse those and lose the entire read.** `[[finding_blended_index_masks_bifurcation]]` / `[[finding_composition_mask_unmask_discriminator]]` — the third instance of this shape in tonight's batches alone.

**⚠️ On "record highs":** CBRE's broader industry series puts the **national aggregate at 23.2–23.3%**, near but just below its **Q3-2025 record of 23.3%**. **But CBRE is a different provider with a different methodology than the Savills metro figures above — do NOT stack them.** Savills published no national aggregate.

## Why this lands where it does

**Nobody in the fleet holds life-science vacancy.** The verify's grep across CREED and REGINALD returned **zero hits** — this is a genuine coverage gap, not a re-report.

**And it is a live OZK thread.** On **7/8** WALTER routed **`SIG-708-003`** — the Atrium *"Life Science Reckoning Through Lens of Bank OZK"* (Oct-2025, 67pp, image-only PDF) — to REGINALD, **flagged unread**, with REGINALD to pull it from `inbox/WILL/processed/`. **That deep-dive is the qualitative case; this is the quarterly quantitative series it needs.** If that PDF is still unread, this is the prompt.

**The question CREED owns, not WALTER:** does a healing Chicago/Denver alongside a supply-driven Boston deterioration change the **collateral** read for a life-science-exposed lender? The naive version ("vacancy near records → collateral impaired") is exactly the read this print refutes for two of the three worst metros — **while Boston, the deepest life-science market, gets worse.** WALTER routes the split and takes no view.

## Explicit negatives

- **Savills' primary PDFs were not read** — the verify worked from the bostonrealestatetimes write-up plus Savills report titles/snippets. Two figures (Chicago, Denver-Boulder) were cross-checked directly; the other six come from the secondary.
- **No Savills national aggregate exists.** CBRE's 23.2–23.3% is the only national figure and it is **not comparable** to these metro numbers.
- **No YoY direction retrieved** for San Diego, DC or Philadelphia — only levels.
- **No OZK-specific exposure figure** is in this print. The link to OZK is via the 7/8 Atrium thread, **not** established here.
