# Energy-Infrastructure Strike Ledger — Summary

**Living index for `STRIKES.tsv`.** One row per *material* energy-infrastructure attack, **all theaters in one table** (so cross-theater patterns — e.g. Russia's campaign peaking the week Iran signed its MOU — are queryable). Russia–Ukraine seeded fully; Gulf–Iran backfilled opportunistically.
**Maintainer:** HAWK. **Last updated:** 2026-06-20.

---

## Schema (`STRIKES.tsv`, 16 cols)
`strike_id` (THEATER-YYYYMMDD-SLUG, stable KB cross-ref) · `Date` · `Theater` (RU-UA / GULF-IRAN) · `Attacker` (Ukraine / Iran-IRGC / Iran-axis / Houthi / Israel / US) · `Facility` · `Region` (oblast or country) · `FacilityOperator` (who *owns* it — NOT the attacker) · `Type` (refinery / crude-terminal / depot / pipeline / pump / chemical) · `Capacity` (nameplate; unit inline — Mt/yr or kbpd) · `Status` (offline / reduced / halted / fire / hit / contained — **point-in-time**) · `Strike#` (cumulative hits on that facility this campaign) · `Channel` (crude-export / product-crack / petrochem) · `ReturnToService` (date facility resumed, or `unk` / `~est`) · `Conf` (Admiralty) · `Source` · `Notes`

## Materiality bar (what earns a row)
Log if **any** of: (a) named major facility, (b) capacity/throughput impact, (c) escalation marker (record wave / new geography / first-of-kind). **Skip** daily small-depot noise unless it marks a pattern shift. The ledger is a *material subset*, NOT an exhaustive count of every drone — see monthly-total note below.

---

## ⚠️ Metric discipline (read before quoting a number)
1. **"% capacity offline" is an as-of, sourced aggregate — NEVER the sum of the `Capacity` column.** Summing nameplates of every facility ever hit double-counts (a) facilities since repaired and (b) `reduced`-not-`offline` plants. Always cite *currently-offline, as-of date, source*.
2. **`Status` is point-in-time; `ReturnToService` closes the loop.** "Currently offline" = rows where Status∈{offline,halted} AND ReturnToService is empty/future. Most repair dates are `unk` — so *currently-offline* is presently uncomputable from the ledger alone; defer to the sourced aggregate below until repair tracking fills in.
3. **The ledger is a material subset.** May 2026 had ~31 reported attacks; the ledger captures ~10 named-material ones. Don't read row-count as attack-count.

## Current sourced aggregates (EXTERNAL — not ledger outputs)
> ⚠️ These are sweep/agency stats, NOT derived from STRIKES.tsv. The ledger (22 RU rows) is a material subset; do not present these as ledger patterns.

**Refining offline:**
- **~1/3 of Russian primary refining capacity offline ≈ 2.14M bpd** | as-of **mid-June 2026** | Energy Intelligence / Kyiv Post.
- May output lowest since 2009 (≈17yr); first-week-June *runs* <4M bpd "lowest in 21 years" (Energy Intelligence). **Two distinct source-claims (monthly output vs weekly runs) — unreconciled; don't merge.** Fuel shortages 25+ regions; 24 of 33 major refineries hit by end-May; ~31 reported May strikes.

**Crude-export side (PRIMARY-CONFIRMED the channel thesis — see Pattern 1):**
- **Russian crude shipments 3.83M bpd (17 May–14 Jun) = highest of 2026**; floating storage ~120M bbl, **+25% vs April** | Bloomberg/Moscow Times (Jun 2) + Vortexa | ORC-verified Jun 18.
- Product exports **slashed**; Russia **importing gasoline by sea** (Euromaidan Jun 18). Kremlin milblogger acknowledged Jun 17 the crude-export rise is from falling refining.
- Russian crude production already softening: **May ~8.7M bpd, −5% YoY** (tightens the storage-saturation clock — see Watch).

---

## Patterns (re-graded Jun 18 vs ORC adversarial pass; ranked by what survives)

**① Channel sequence: crude-export → product-crack — LEAD SIGNAL, PRIMARY-CONFIRMED.**
Ledger shows the target sequence: Mar–Apr = **crude-export terminals** (Primorsk/Ust-Luga/Novorossiysk, ~2/5 of seaborne crude); May–Jun = **refineries** (product-crack). The falsifiable consequence — refinery hits *free crude for export* — was delivered by primary data: crude shipments at a **2026 high (3.83M bpd)**, floating storage **+25%**, product exports slashed, Russia importing gasoline by sea. **This is THE decoupling explanation:** it's why "⅓ of refining offline" coincides with Brent ~$79, not $109 — the repricing is on *products/cracks*, not crude. **Decision-relevant for BRENT (handed via outbox Jun 18).**

**② Re-strike sequences — observed, but the load-bearing conclusion is NOT ledger-proven.**
Facilities hit >1×: MNPZ (5/17, 6/16, 6/18), Primorsk (3/22, 3/29), Tuapse (mid-Apr ×2). *Caveat (ORC):* "repair never catches up" needs `ReturnToService` — which is blank — so it's borrowed from external output stats, not the ledger. n=3 on one facility; the 6/16→6/18 "2-day" gap is plausibly **one operation**, not a sustainable cadence, and March re-strikes were already ~4–7d, so "tightening over the campaign" is unproven. Mechanism (re-hit to suppress repair) is qualitatively sound; the quantified "accelerating" claim is retracted pending ReturnToService data.

**③ Geographic reach — "range no longer the binding constraint" ✓; "creep" ✗.**
Deep-interior targets (Tatarstan, Samara) and repeated Moscow strikes show European-Russia refining is broadly reachable. But it is **not monotonic outward**: Feb Tatarstan (1,200km) *preceded* the April coastal strikes. Low decision-relevance. *(Air-defense note: the "~194/180 around Moscow, 555 national" intercept counts are a coarse theater-scale saturation proxy — deliberately NOT a ledger column, and NOT a per-facility figure.)*

**④ Under-priced RU product-supply risk (narrow, falsifiable core of the old "rotation" claim).**
Keep: *the Jun 17 MoU did not end geopolitical-energy risk; RU refined-product supply risk is escalating, and a Gulf-focused tape may under-price it.* **Drop** the "regime rotation" framing — two independently-driven conflicts moving opposite in 72h is coincidence + analogy, no shown mechanism. (Zelensky "Moscow will burn" / "time the war ended" rhetoric → coercive-signaling read is plausible but source it before anchoring.)

**CUT — operator concentration.** "Rosneft most-hit = deliberate" is a base-rate artifact (Rosneft is Russia's largest refiner; random targeting hits it most); "Transneft owns every terminal" is tautological (terminal monopoly). Shows nothing without normalizing by capacity share; no decision turns on it.

**External-aggregate (NOT patterns):** "31 May strikes," "⅓ offline," "lowest since 2009/21yr" — sourced stats, kept in the aggregates section above, not credited to the ledger. P① already showed ⅓-offline doesn't move Brent, so the intensity headline is the one the market is correctly discounting.

## Watch — PRODUCT/CRACK → BRENT flip triggers (valve currently OPEN)
The "outages → crude backs up → touches Brent" transmission is the right **tail**, but right now the valve is **open**: crude is being *freed*, exports at a 2026 high. The refinery campaign converts to a *crude / Brent* story only when one of these fires:

| # | Flip trigger | Leading indicator / what to watch | Status Jun 18 |
|---|---|---|---|
| 1 | **Floating-storage saturation** | Floating + onshore storage fills → freed crude can't clear → shut-ins begin. ~120M bbl floating (+25% vs Apr); production already softening (May ~8.7M bpd, −5% YoY) tightens the clock | 🟡 building, not saturated |
| 2 | **Crude-export terminal / pipeline strikes** | A `crude-terminal`/`pipeline` row reappears in STRIKES.tsv after the refinery-dominated stretch (Baltic terminals / Druzhba) — Ukraine re-targets the crude channel | ⚪ **still none — Jun 15-20 all refineries/depots/Crimea-gas** (Tyumen Jun 20 = deepest-range refinery hit, damage disputed; last crude-terminal hit was Apr). **HAW-15 no_change.** |
| 3 | **Russian crude shut-ins** | Producers cut wellhead output (can't store/refine/export it) — the physical realization of #1 | ⚪ not reported; **Ust-Luga loadings +49% m/m May = no shut-in, valve clearing** |
| 4 | **Urals / tanker / export congestion confirmation** | Urals discount widening, tanker queues, loading delays at export ports = freed-crude flow hitting a ceiling | 🟡 **mixed — Urals discount widened to ~25% vs Brent (May; was ~$6.4 Mar)**, but loadings recovered + shadow fleet 48% of seaborne = flow still clears |

**Any of #2–4 firing, or #1 saturating, flips this from a crack story to a Brent story — pre-registered with BRENT.** Highest-information ledger columns: **`Channel`** (rotated back to crude-export?) and **`Strike#`** (re-hit cadence, once `ReturnToService` lets us test repair-lag).

## Open verify items
- Volgograd Lukoil (`RU-20260514-VOLGOGRAD`) date LOW-CONF — one source conflated with a later strike.
- Syzran exact May date TBD.
- `RU-20260521-UNSPEC` — Zelensky-confirmed strike, facility unnamed.
- ReturnToService dates are mostly `unk` — fill as repair/restart reporting appears (this is also how we'll watch Gulf facilities come *back* if the ceasefire holds).
- Gulf–Iran theater: only 4 seed rows (Mar 2026) from vetted KB; full backfill pending.

## Cross-refs
KB synthesis rows: **KB-HAWK-185** (May record month), **KB-HAWK-186** (June sequence + cumulative). Originating sweep narrative: `research/RUSSIA_OIL_INFRA_STRIKES_MAY-JUN2026.md`. Price/crack consequence = **BRENT**.
