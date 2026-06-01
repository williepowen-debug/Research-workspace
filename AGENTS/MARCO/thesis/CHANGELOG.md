# MARCO THESIS — CHANGELOG

Version-transition log. Newest first. Each entry: old view → new view, trigger, conviction deltas. Version bump rule: **major (X)** = structural change / conviction reversal / phase transition; **minor (Y)** = refinement.

---

## v2.0 → v2.1 — 2026-05-31 (session 8) — MINOR — "The produce thermometer is confounded"

**Trigger:** Session-8 produce-attribution decomp (deep-research harness + external-primary verification, completed session 7; reviewed against BRENT's diesel/freight files session 8). v2.0 leaned on CPI fresh F&V +6.1% YoY as the clean confirmation that the workforce shock (Channel 1) was transmitting to food prices. The decomp showed the spike is multi-causal.

**Old view (v2.0):** Channel 1 "load-bearing," HIGH conviction, with the produce CPI print read as direct, hardening confirmation of labor→food transmission. "+6.1% produce" carried as strong thesis evidence.

**New view (v2.1):** Channel 1 splits into **mechanism (HIGH, intact)** vs. **thermometer (MEDIUM, demoted).** The ag-labor supply shock (2.2M stock loss + H-2A bottleneck) is undisputed. But the produce CPI is **multi-causal** — labor is one co-driver, not the dominant/measurable one. A slow labor *stock* drift cannot mechanically produce a one-month +4.0%→+6.1% *acceleration*; supply/cost shocks can.

**Three co-drivers — verified, well-timed, magnitude-material:**
- **FL freeze** Dec'25–Feb'26 — $3.17B, USDA disaster declaration, hit exactly the spiking crops (berry/tomato). Fleet-wide blind spot; nobody caught it. (I first called it fabricated on fleet silence — WRONG; Will pushed back, external primaries confirmed it real. Lesson → auto-memory `feedback_verify_existence_external_primaries`.)
- **Mexican tomato tariff** — 17% AD duty (Jul'25) on the most-weighted fresh vegetable.
- **Diesel/freight** — crude spiked to $116 (May 5), distillate ~11% below 5-yr; timed to the April acceleration. Cross-checked against BRENT's files (session 8): the freight co-driver is **transient/mean-reverting** (crude −19% on the month; pump relief May 31–Jun 14), which sets up a dated forward test.

**Why MINOR not MAJOR:** the thesis spine (workforce supply shock) is unchanged and still HIGH. What changed is the *evidentiary status of one indicator* — we can no longer cite produce CPI as clean labor proof. Refinement of conviction-by-indicator, not a structural reversal.

**Conviction deltas:**
| Item | v2.0 | v2.1 |
|---|---|---|
| Channel 1 mechanism (labor shock) | HIGH | **HIGH** (unchanged) |
| Produce CPI as proof of it | (implicit HIGH) | **MEDIUM ↓** — confounded |

**Forward test added:** ES-MARCO-08 (`EXPECTED_SIGNALS.md`) — June 10 / July CPI vs. pump-price decoupling discriminates labor-vs-transient weighting. New coupling logged: `COUPLINGS.md` MARCO↔BRENT (decaying freight-input edge).

**Prediction resolution:** MAR-21 (planting-season raid surge → produce spike) RESOLVED — mechanism largely WRONG (raids eased, H-2A wages cut; spike attributable to freeze/tariff/freight). See `PREDICTIONS.tsv`.

**Discipline note:** v2.1 is the honest correction of a v2.0 over-claim. The "verify via external primaries" lesson was *satisfied* here — freeze, tariff, and crude all verified against primaries before the demotion — which is what licensed the rewrite rather than blocking it.

---

## v1.0 → v2.0 — 2026-05-31 (session 6) — MAJOR — "The thesis narrows to its spine"

**Trigger:** Session-6 full-sweep data refresh (STATUS was 5 weeks cold; last updated Apr 23). Live pulls on every stale board item revealed a **bifurcation** the v1.0 "everything compounding" frame had masked.

**Old view (v1.0, ~Jan–Apr 2026):** Acute, multi-front population-stress crisis. 76% confidence, STRENGTHENING, Phase 2→3. All channels (tourism, workforce, migration, border) treated as compounding simultaneously toward a unified regional-stress event. Dashboard carried ~10 "breached" indicators read as a single hardening crisis.

**New view (v2.0):** The thesis **bifurcated**. Cyclical channels reversed; the structural channel hardened. The thesis did not break — it **narrowed to its durable spine** (Channel 1: workforce displacement → produce prices). Conviction is now **split by channel** — that split is the substance of v2.0.

**What reversed/softened (→ cyclical, conviction cut):**
- DHS shutdown ENDED Apr 30 (76-day record) — acute disruption over.
- FL condo inventory 8.9mo Apr (back below 9.0, tightening) — Channel 3 ↓.
- Canadian visitors +1.4% YoY Apr headline (air still −8.1%) — Channel 2 ↓ to bifurcated.
- NFP rebounded +115K / UE 4.3% — Feb −92K "smoking gun" was a blip.
- Mexico remittance $-value flipped +4.9% Mar (count −3.6%) — Channel 4 residual signal only.
- ICE eased off ag worksite raids — Channel 1 *flow* softened.

**What hardened (→ structural, conviction held/raised):**
- CPI fresh F&V +6.1% YoY (was +4.0% Mar); fresh veg +3.1% MoM — produce spike accelerating.
- ICE/CBP $71.7B reconciliation text (May 4) — enforcement funded & unconstrained through Trump's term; funding no longer a brake.
- H-2A consular bottleneck persists (South Africa→July; Red River Valley potato).
- 2.2M self-deportation stock loss — irreversible; Channel 1's foundation.

**Conviction deltas (channel-level):**
| Channel | v1.0 | v2.0 |
|---|---|---|
| 1 Workforce→Produce | (folded into 76% composite) | **HIGH ↑** load-bearing |
| 2 Visitor Flows→FL CRE | high/compounding | MEDIUM ↓ bifurcated |
| 3 Migration→Sun Belt | high/compounding | MED-LOW ↓ softening |
| 4 Cross-border→muni | strong | MEDIUM → slow grind |
| 5 American emigration | watch 65% | LOW → watch (unchanged) |

**Invalidation note:** Two of v1.0's four invalidation conditions *partially fired* (Canadian headline rebound, FL RE stabilization). Under v1.0's monolithic frame that would read as the thesis weakening broadly; under v2.0 it correctly localizes to Channels 2-3, leaving the spine (Channel 1) intact. This is exactly why the channel-split reframe was necessary.

**Prediction resolutions logged this session:** MAR-08 (FL condo >9mo) CONFIRMED; MAR-27 (DHS >60d) CONFIRMED. Notes refreshed on MAR-14/-18/-26. (`PREDICTIONS.tsv`)

**Structural note:** v2.0 is the first time MARCO's thesis lives in the house `thesis/` format (consolidated from `MARCO_SKELETON.md` v1.0 + `DECK_EVIDENCE.md` + `FINDINGS.md` + `workbook/FLOW.tsv`). SKELETON retained as v1.0 historical artifact.

---

## v1.0 — pre-2026-05-31 (baseline, reconstructed)

Original thesis articulated in `MARCO_SKELETON.md`: "Population movement disruptions create localized economic stress that compounds in regions with multiple exposures; traditional indicators miss or lag." 76% confidence, STRENGTHENING, Phase 2→3 (Stress Emergence → Economic Transmission). Four FLOW cascades (FLOW-REG-01 FL triple-exposure, FLOW-IVF-01, FLOW-WFD-01, FLOW-IMG-01). Detail in that file; not re-versioned here.
