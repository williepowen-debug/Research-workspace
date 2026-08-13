# AEOLUS · WILDFIRE — domain workspace

**Created:** 2026-08-13 (Will-directed reorganization) · **Owner:** AEOLUS
**Channel mapping:** **wildfire is the PHYSICAL PERIL leg of C4 (Property / physical assets).** It is **not** a separate channel.

---

## WHY IT STAYS INSIDE C4 (Will-ruled 2026-08-13)

Wildfire gets its own folder because its evidence was scattered across three KB groups (`WILDFIRE`, `INSURANCE`, `CLIMATE`) and was hard to read as one thing. **It does not get its own convergence-matrix row**, because C4 already carries the transmission it would duplicate:

> `chronic peril (fire/SLR/flood) → insurability loss + property values ↓ → mortgage/CRE/muni credit risk`

Scoring wildfire separately would make a single event score **twice** — in the fire channel and again in C4 property — which is exactly what the matrix's **Independence** column exists to prevent (**L-02**).

## 🔑 THE CENTRAL DISCIPLINE — ACRES ARE NOT LOSSES

**This is the whole C4 thesis and the folder's reason for existing. Get it wrong and the channel mis-scores.**

C4 runs on **two legs that are currently pointing in opposite directions:**

| Leg | Instrument | Current state |
|---|---|---|
| **PERIL** (physical) | NIFC preparedness level, acres burned, fires, potential outlook | **Firing** — PL5 for 26 days, **155% of 10-yr avg acreage** |
| **INSURED LOSS** (financial) | reinsurer cat tallies (Gallagher Re / Munich Re / Aon) | **Soft** — H1 insured nat-cat **~25-28% BELOW** average |

⚠️ **My RED threshold band is a CAT-LOSS instrument (`reinsurer YTD vs 10-yr avg ≥150%`). A 155% ACREAGE print is NOT that band.** They are different rows in the threshold table and different units. **Never let an acreage figure stand in for a loss figure** — it is the single easiest way to manufacture a false 🔴 here.

**The divergence IS the finding, not noise.** Physical peril elevated + insured losses below average means the repricing migrates **DOWN-STACK** — to primary carriers, state residual pools (CA FAIR Plan, Citizens) and munis — rather than into reinsurance, which stays soft. **That down-stack migration is C4's load-bearing claim** (REGINALD's counter, noted and standing: the *softening* leg is the better-evidenced one).

## SCOPE

**Mine:**
- Fire **peril** state: NIFC preparedness level, acres/fire counts vs average, the monthly Significant Wildland Fire Potential Outlook.
- The **climate driver**: drought → fuel state → fire potential, and the **ENSO** signal on it.
- **Insurability** consequences: non-renewal rates, residual-pool enrollment and assessments, carrier exits in peril geographies.
- **WUI structure loss** as the transmission from acres → insured dollars.

**Not mine — route:**
- **Florida** → **CORAL** (FL is a CORAL geography; wind/flood not fire, but the residual-pool mechanics rhyme — reconcile to one figure, don't silo).
- Bank / CRE / **muni credit** exposure → **REGINALD / CREED**.
- **Utility** ignition liability + grid de-energization → **WATT**.
- Reinsurance **pricing** / ROL → C1, and **SHADE** on the capital side.

**Attribution discipline:** a single destructive fire season is **not** a climate trend. Attribution is mine to adjudicate and the honest answer is usually *"one event, insufficient"* — say so rather than letting a dramatic event do the arguing.

## STANDING BANDS (from `../CLAUDE.md` § THRESHOLDS — cite, don't restate)

| Metric | Yellow | Orange | Red |
|---|---|---|---|
| Property insurance non-renewal rate (peril region) | +10% YoY | +25% | +40% / carrier exit |
| Reinsurer cat-loss tally (YTD vs 10-yr avg) | ≥110% | ≥130% | ≥150% |

**C4 upgrade trigger (3 → 4):** **carrier insolvency OR a single >$10B insured cat.** Neither has fired.
**C4 channel-kill:** H1 cat losses <110% of average **AND** non-renewals stable 2+ quarters. **Conjunction — the loss leg currently satisfies it, the non-renewal leg does not.**

## FILES

| File | Purpose |
|---|---|
| `README.md` | this charter |
| `DOSSIER.md` | live peril + insurability state, and the season's open questions |
| `SOURCES.md` | verified pull commands + the discontinued-series warning |

⚠️ **The central `workbook/` remains canonical** — KB / VX / FLOW / PREDICTIONS rows keep their `KB-AEO-NN` IDs in `AGENTS/AEOLUS/workbook/`. **Do not fork a second ledger here.**
