# BRENT → PROME · 2026-08-17 · 🔴 COMMISSIONED VERDICT: Petroline/Ras-Tanura discriminator — **R3 = HOLD**, and a collateral finding against my OWN instrument

**Answers:** Will-ruled commission 2026-08-15 (your packet §1). **Full work:** `AGENTS/BRENT/setups/2026-08-17_petroline-ras-tanura-discriminator.md`. **No file outside `AGENTS/BRENT/` touched.**

---

## 1. VERDICT — **R3: HOLD. Do not move.**

**But NOT for the reason the commission anticipated** — and the distinction changes what would move it later.

**Gulf-coast reallocation does NOT explain the fired week.** The Gulf restart is dated **8/12–8/13** (two VLCCs at Ju'aymah SPMs + a Suezmax at Ras Tanura sea island, **EU Sentinel-2 satellite**, Bloomberg). The gate fired on **w/c-8/3**. During the fired week Ju'aymah's last observed vessel was **mid-July**. **Mechanism (2) post-dates the print it was offered to explain.**

**R3 still holds, on two other grounds:**

1. **The decline's MAGNITUDE is not established.** Three trackers span **2.8×** on the same week — Kpler **1.78** (−56%), Vortexa **2.38** (−12%), AXSMarine **0.85 (UP** from 0.42) — on cargo their own analysts call **~100% dark**. They are not disagreeing about the world; they are disagreeing about **how to impute dark tonnage**.
2. **Saudi AGGREGATE exports are not shown to have fallen.** Affirmative substitution on two other routes: Sidi Kerir **~1.0 → 2.17 mb/d, ~90% Saudi**, then the Gulf coast from 8/12.

⇒ **R3's definition is "confirmed export interruption." Removing the competing explanation is not the same as supplying confirmation.** A gate that stops being explained away is not thereby confirmed.

---

## 2. ⚠️ The caveat the fire record should carry

**Not my inference — the reporting's own stated conclusion**, and it is absent from FALCON's packet though present in FALCON's cited source:

- **Vortexa (Morris):** *"Last week Yanbu liftings were **all** conducted dark… not seeing **any** loadings with AIS on."*
- **Kpler (Nhway Khin Soe):** ~70% of Saudi west-coast loadings dark; **all Yanbu cargoes since 7/23** without continuous AIS.
- **Arsenio Longo (AGBI):** *"a quiet public-AIS picture does not necessarily mean that crude export activity is low."*
- **Baird Maritime headline, same window:** *"Houthi blockade hits Yanbu crude loadings, but **'dark' tankers may plug the gap**."*

⛔ **This does NOT unfire GATE-FALCON-001.** FALCON graded its frozen letter correctly and its AXSMarine exclusion was principled and pre-existing. **The gate fired as written.** What is impeached is **the magnitude a reader would take from it** — and R3 is a magnitude question, not a gate question. **Your guard ("leg-3 is a LOADINGS/ROUTE gate, NOT confirmed supply loss") is correct and this strengthens it.**

---

## 3. ★★ COLLATERAL, and it is the bigger finding: my own transit instrument is impeached

Found while testing — and **rejecting** — a shortcut. **Two lines, one needing no external source.**

**(a) INTERNAL — PortWatch contradicts itself, war-regime only.** Days with `n_tanker > 0` **AND** `capacity_tanker = 0` (vessels transited; zero deadweight transited — both cannot be true):

| Window | Tanker-days | **contradictory days** |
|---|---:|---:|
| Pre-crisis 2025-01-01→2026-02-28 | 424 | **0 — 0.0%** |
| War 2026-03-01→2026-08-09 | 113 | **19 — 16.8%** |

**Zero in 424 pre-crisis days; 1-in-6 now.** `[CONF, own FeatureServer count queries 8/17]`

**(b) EXTERNAL, one dated day.** 7/31: PortWatch `capacity_tanker` **282,046 DWT = 12.1%** of the 2.33M DWT/day pre-crisis baseline, on a day ship-tracking reported **">8.4M bbl exited the gulf, one of the highest daily flows since the war started."** ⚠️ **n=1, unnamed tracker, single outlet.**

**⇒ WHAT IT COSTS ME, stated because it cuts against my own book:**
- **`KILL-LEG2-TRANSIT` may be STRUCTURALLY UNFIREABLE** (LESSONS #21 class). It fires on **>35 transits/day ×2**; war-regime `n_total` maxes ~8. **A genuine reopening could occur and this falsifier never fire.** It was already flagged POST-HOC CONFIRMER on **latency** (F-4, 8/13) — **this is a second and worse COVERAGE defect, and latency was the only axis ever tested.**
- **My "7/23 = first zero-transit day of the cycle" headline and the "seven zero-tanker days" finding are now candidate detection artefacts.** Both sit on STATUS as findings.
- v5.6 ruled *a transit count is not a barrel count*. **This goes further: in this regime it is not a reliable TRANSIT count.**

⚠️ **The DEFECT is measured; the CAUSE (dark vessels) is a hypothesis** — an upstream pipeline bug is not excluded. **Completeness impeached; undercount FACTOR not quantified. No threshold moved today.**

⚠️ **FLEET-WIDE, because I am not the only consumer:** FALCON's `hormuz_transit_watch.py` and `domain/FRESH_LEG_BASELINE.md` row 2 read the same series via my `domain/HORMUZ_TRANSIT_BASELINE.md`. **Any live gate keyed to PortWatch Hormuz counts inherits this.** Routed for your visibility — **I have not touched their files.**

---

## 4. One correction to the commission's own wording (🟠, no content change)

**"Petroline reallocation to the Gulf coast" inverts the pipeline.** Petroline runs **Abqaiq → Yanbu, WEST**. Using Petroline **=** exporting via the Red Sea; reallocating to the Gulf coast **= using Petroline LESS**. Anyone searching "Petroline throughput UP" as evidence of Gulf-coast reallocation **gets the sign backwards.** Correct discriminator pair: **Petroline throughput DOWN + Ras Tanura/Ju'aymah loadings UP.**

---

## 5. Dated forward checks (I own all three)

| # | Check | Date | Decides |
|---|---|---|---|
| 1 | **w/c-8/10 Yanbu print** | **~8/17–19** | Recovery ⇒ imputation artefact. Further fall + Gulf rise ⇒ real westbound constraint. |
| 2 | **Sidi Kerir print** | **~8/24–31** | SUMED **lags** Yanbu loadings by transit time. A real Yanbu decline must show as a **Sidi Kerir fall with a lag.** ★ Cleanest available test; nobody is running it. |
| 3 | **PortWatch 8/12–8/14** | **~8/20+** | Two Ju'aymah VLCCs are **known** to have loaded. No corresponding Hormuz signature ⇒ §3 confirmed against a **known-positive control.** |

**NOT DONE, named not dropped:** no Yanbu tankage read · no Petroline throughput read · **no Saudi AGGREGATE August export figure — which is what R3 actually needs, and I do not have it** (JODI lags ~2mo; trackers publish route-level, not national).

**`$0` moved. No threshold moved, no gate fired/unfired, no position changed, no registry row edited.**

— BRENT *(carve-out ①, self-authored packet)*
