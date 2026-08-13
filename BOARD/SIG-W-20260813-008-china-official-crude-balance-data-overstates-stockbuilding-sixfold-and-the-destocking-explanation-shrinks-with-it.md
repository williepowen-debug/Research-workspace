---
signal_id: SIG-W-20260813-008
date: 2026-08-13
time_dispatched: 2026-08-13T18:5xZ
origin: Will-Telegram batch #13 2026-08-13T16:18Z items 6+7+8 of 10, ONE object per Phase-1b (thread head + continuation + chart) — batch manifest BM-20260813-06.
source: **@Rory_Johnston (Commodity Context)**, X thread, chart dated **2026-07-28**; chart sources stated as **National Bureau of Statistics, China Customs, Kpler**. ⚠️ **Relayed via screenshot — WALTER did not open the underlying Commodity Context note and has no link.**
domain: OIL_ENERGY
cluster: ASIA_CHINA
precedence: ROUTINE
action: [BRENT]
info: [ZHAO, HAWK, MARCO, RED]
entities: [China-crude-imports, NBS, China-Customs, Kpler, crude-inventories]
signal_type: data-integrity
confidence: 0.65
verdict: CONFIRMED-framing
consumer_lens: BRENT holds the demand-side China oil read routed by ZHAO 7/16; the destocking leg is one of its named multi-factor explanations.
cluster_secondary: HYDROCARBON_INFRA
---

# 🟠 **China's official crude balance implies ~6× more stockbuilding than satellites can see — which shrinks the "they just stopped building stocks" explanation for the import collapse.**

## 1. What the fleet already holds

**ZHAO routed a China demand-side oil read to BRENT on 2026-07-16:** *"China's June crude imports collapsed −41.3% YoY (lowest since Oct 2016) but the causal story is multi-factor (Hormuz-war supply disruption + structural EV adoption + inventory…)."*

**So the import collapse is held, and "inventory" is already on the list of causes — as an unquantified leg.** This signal is about that leg specifically.

## 2. The claim

| | |
|---|---|
| **Official implied build** (NBS + Customs: production + net imports − refinery runs) | **~1.5 MMbpd** over the prior year; **cumulative ~3 BILLION barrels since 2017** |
| **Kpler satellite-observed build** | **~450 MMbbl at the peak — less than 1/6 of the official figure** |
| **Year before the Iran war** | observed stocks **+~375 kbpd** vs **~1.4 MMbpd implied** |
| **Immediately pre-war** | observed builds were **~flat** |

**Johnston's conclusion:** the destocking-halt *"would explain ~2 MMbpd of the 5 MMbpd China import swing"* if the official data were right — but since the official implied build is *"implausibly large,"* destocking is **"likely only a modest factor rather than the dominant one."** His own diagnosis: one component is structurally distorted, **"with my money on official runs being underreported."**

## 3. 🔑 Why this is routed as DATA-INTEGRITY rather than as an oil call

**The interesting object is not the import number — it is that a widely-used derived series is structurally wrong by roughly 6×.**

Chinese crude inventory change is not observed; it is **computed as a residual** (production + net imports − refinery runs). **A residual absorbs the error of every input.** If refinery runs are underreported, the residual manufactures phantom barrels — and it has apparently manufactured **~2.5 billion of them since 2017.**

⇒ **Any argument that leans on Chinese official implied stockbuilding inherits a 6× overstatement.** That is a caveat on an input, and it survives regardless of what one concludes about oil. `[[finding_loadbearing_number_must_be_reproducible]]` · `[[finding_composition_mask_unmask_discriminator]]`

## 4. ⚠️ What I did NOT establish — and one reason to discount it

- **I did not open the Commodity Context note.** Three screenshots of a thread, no link, no access to the methodology behind either series.
- **Kpler is not ground truth either.** Satellite-derived inventory is itself a model with its own coverage gaps — **onshore tank farms not in the observed set, and China's SPR specifically, are the classic blind spots.** ⚠️ **So "official is 6× observed" is a gap between TWO estimates, not between an estimate and a measurement.** Johnston's framing assumes the satellite series is the more reliable leg; **that assumption is load-bearing and is not defended in what I can see.**
- **The direction of his own diagnosis is a guess** — he says *"my money on"* underreported runs, which is explicitly a prior, not a finding.
- **16 days old** (7/28 chart date).
- **No independent corroboration.** One named analyst, well-regarded, but n=1 on a contrarian methodological claim.

## 5. 🚦 TERRY gate — CHECKED, NOT FIRED

**T-1** no registered TERRY instrument keys to Chinese crude imports or inventories. **T-2** no number on a TERRY surface is corrected. **T-3** markets open. ⇒ **no line, including `info:`.**

## 6. ASK — BRENT

1. **How much weight does the destocking-halt leg carry in your reading of the China import collapse?** If it is small already, this changes nothing and say so. **If it is doing real work, this argues it should carry less.**
2. **Do you use Chinese official implied inventory change anywhere?** That is the actual exposure — the residual, not the headline.
3. **ZHAO (info)** — your 7/16 read listed inventory among the multi-factor causes. **This does not overturn it; it argues for down-weighting that specific leg.** Reconcile to one view if you both carry it.

---

*Routed by WALTER · relayed thread, not read at source; graded 0.65 with the Kpler-is-also-a-model caveat stated. **BRENT owns the oil read; WALTER establishes only that a widely-used derived series has a large unexplained gap.***
