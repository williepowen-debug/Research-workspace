# AEOLUS · WATER — domain workspace

**Created:** 2026-08-13 (Will-directed reorganization) · **Owner:** AEOLUS
**Channel mapping:** **C6 = water ALLOCATION** (core channel) · **C5 = river NAVIGATION → freight** (the shipping/trade leg)

---

## WHY THIS FOLDER EXISTS

Water is the one AEOLUS domain that spans **two channels with different mechanisms**, and the split matters enough that Will named it directly in the standing directive (2026-08-03):

> *Maintain first-class tracking on MAJOR RIVER water shortages — especially where they affect SHIPPING / TRADE.*

| | **C6 — ALLOCATION** | **C5 — NAVIGATION** |
|---|---|---|
| **Mechanism** | reservoir depletion → shortage-tier / compact decision → mandatory delivery cuts + hydropower loss | low river stage → barge draft limits → freight cost ↑ → goods/industrial cost |
| **Instrument** | reservoir **elevation** vs a decision threshold | **gauge level** vs navigable minimum, + freight rate |
| **Repricing** | hydro utilities, SW munis, ag-water, data-center siting | shipping, freight, goods-CPI, European industrials |
| **Speed** | quarters (policy clock) | weeks (physical clock) |
| **Live example** | Colorado: Powell/Mead vs Hoover 1,035 ft, ROD ~10/1 | Rhine at Kaub, 12–13 cm, through its all-time low |

⚠️ **These are SEPARATE ANTECEDENTS and must not be stacked.** The Colorado is driven by the **ENSO / Western-hydrology** root shared with C2/C3; the **Rhine is a European basin with an independent root.** Counting them as convergent evidence is precisely the shared-antecedent error the convergence matrix's Independence column exists to prevent (**L-02**).

## SCOPE — what lands here

**Mine:**
- **Colorado River system** — Powell, Mead, Reclamation shortage tiers, the Post-2026 Operating Guidelines (ROD + 12/31/26 expiry), compact/decree questions.
- **Major navigable trade rivers** (Will's standing watch): **Rhine · Mississippi/Ohio · Yangtze · Danube · Paraná**, + the **Panama** chokepoint.
- **Western snowpack** as the allocation-setting input (Apr-1 % of median).
- **Industrial/municipal water competition** — including **data-center water** as the third AI-siting constraint after credit and power.

**Not mine — route, don't deep-dive:**
- Hydro **generation** economics → **WATT** (I own the water resource, WATT owns the MW).
- Ag/food and SW municipal **cost** consequences → **CARL** / **MARCO**.
- Data-center **capex** consequence → **VULCAN** (I own the resource constraint).
- Ag-lending / muni **credit** → **REGINALD / CREED**.
- **Florida** water → **CORAL**. Do not import Colorado framing to FL.

## THE C6 DISCRIMINATOR (binding — WALTER v0.22)

A signal routes to C6 **only with a dated instrument or an allocation decision** — never on the word "drought." Shortage tiers, the Colorado guidelines, compacts, decrees, levels tied to a decision, supply competition, generation limits. **Still-kills:** no allocation decision + no dated instrument + no priced consequence; advocacy framing; unsourced aggregate volume claims. Long-horizon structural depletion (Ogallala) is a **watch-note with the horizon stated** — not an auto-kill, and not a score-mover until it reaches an acreage / cost / water-rights-pricing decision.

## 🔴 THE SOURCING RULE THIS FOLDER EXISTS TO ENFORCE (L-15)

**Use the issuing agency. Never a tracker.**

On 2026-08-12 I published Lake Powell at **3,524.20 ft, "risen 2.2 ft"** from a `lakepowellwaterlevel`-class tracker. The **USBR primary** said **3,520.37 ft, having fallen every day for 15 days** — wrong by **3.83 ft and wrong on the trend sign**, which made my stated conclusion the exact inverse of the truth. I was grading a prediction against a **0.45 ft** margin using sources that disagreed by **3.83 ft**.

> **Rule: before grading any threshold, ask what the margin is and what the source spread is. If spread ≥ margin, a secondary is not "less precise" — it is UNUSABLE.**

**Also: never cite percent-full.** The 19%-vs-23.1% conflict that cost me a session came from trackers using different capacity bases. **Elevation is the threshold instrument.** The percent figure was a number I never needed.

## FILES

| File | Purpose |
|---|---|
| `README.md` | this charter |
| `DOSSIER.md` | consolidated live state — Colorado system, rivers, the open questions |
| `SOURCES.md` | **verified working pull commands** for every primary. Copy-paste, don't reconstruct. |

⚠️ **The central `workbook/` remains canonical.** KB / VX / FLOW / PREDICTIONS rows live in `AGENTS/AEOLUS/workbook/` with the normal `KB-AEO-NN` / `AEO-NN` IDs. **Do not fork a second ledger in here** — this folder holds synthesis and method, the workbook holds the permanent record. Cite KB IDs from the dossier.
