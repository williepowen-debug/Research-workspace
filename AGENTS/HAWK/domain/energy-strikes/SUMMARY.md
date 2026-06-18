# Energy-Infrastructure Strike Ledger — Summary

**Living index for `STRIKES.tsv`.** One row per *material* energy-infrastructure attack, **all theaters in one table** (so cross-theater patterns — e.g. Russia's campaign peaking the week Iran signed its MOU — are queryable). Russia–Ukraine seeded fully; Gulf–Iran backfilled opportunistically.
**Maintainer:** HAWK. **Last updated:** 2026-06-18.

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

## Current sourced aggregate (Russia refining)
- **~1/3 of Russian primary refining capacity offline ≈ 2.14M bpd** | as-of **mid-June 2026** | source: **Energy Intelligence / Kyiv Post**. *(This is their reported aggregate, not my sum.)*
- First-week-June refining runs **< 4M bpd — lowest in 21 years**; fuel shortages in **25+ regions**; May output lowest since 2009; 24 of 33 major refineries hit by end-May.

---

## Patterns (update each pass)
- **Repeat-targeting:** Moscow MNPZ/Kapotnya **3×** (5/17, 6/16, 6/18); Primorsk **2×** (3/22, 3/29); Tuapse **2×** (mid-Apr). Re-hit cadence on MNPZ is *tightening* (2 in 3 days, 6/16→6/18).
- **Channel rotation:** March–April skewed to **crude-export terminals** (Primorsk/Ust-Luga/Novorossiysk — Baltic+Black Sea, ~2/5 of seaborne crude); May–June pivoted to **refineries / product-crack** (domestic fuel + diesel/gasoline exports). The squeeze migrated from *crude flow* to *refined product*.
- **Geographic creep:** strikes now reaching deep interior — **Tatarstan** (Taneko/Taif-NK), **Samara** (Kuibyshev/Syzran/Togliatti), **Moscow** itself — i.e. drone range is no longer a border-belt constraint.
- **Operator exposure:** Rosneft (Tuapse/Ryazan/Saratov/Syzran/Kuibyshev), Lukoil (NORSI/Volgograd), Transneft (all crude terminals), Gazprom Neft (MNPZ). Rosneft is the most-hit operator.
- **Cross-theater (the headline):** RU-UA campaign hit **all-time intensity** the same week (Jun 16–18) the GULF-IRAN cluster **de-escalated into a signed MOU (Jun 17)**. The geopolitical-energy risk regime is **rotating, not resolving** — the unified table is what lets us see this.

## Open verify items
- Volgograd Lukoil (`RU-20260514-VOLGOGRAD`) date LOW-CONF — one source conflated with a later strike.
- Syzran exact May date TBD.
- `RU-20260521-UNSPEC` — Zelensky-confirmed strike, facility unnamed.
- ReturnToService dates are mostly `unk` — fill as repair/restart reporting appears (this is also how we'll watch Gulf facilities come *back* if the ceasefire holds).
- Gulf–Iran theater: only 4 seed rows (Mar 2026) from vetted KB; full backfill pending.

## Cross-refs
KB synthesis rows: **KB-HAWK-185** (May record month), **KB-HAWK-186** (June sequence + cumulative). Originating sweep narrative: `research/RUSSIA_OIL_INFRA_STRIKES_MAY-JUN2026.md`. Price/crack consequence = **BRENT**.
