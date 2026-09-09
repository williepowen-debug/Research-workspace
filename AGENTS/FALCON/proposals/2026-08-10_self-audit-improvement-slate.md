> ⚠️ **HISTORICAL PROPOSAL (2026-08-10) — do not read its items as open or closed from this file.** Execution state lives in `STATUS.md`'s owed-forward list, `PROME/DOCKET.tsv` L300/L301, and `LESSONS.md` FAL-08. As of 2026-09-08: the vessel ledger, WARRISK per-row check and transit-band re-spec were built 8/10; the attacker-identity axis was applied 9/8; the casualty-ratchet instrument is still OPEN.

# FALCON — self-audit improvement slate, 2026-08-10

**Author:** FALCON · **Task:** Will-directed via PROME — read my own tree, produce a ranked proposal list (functionality · stale data · gaps).
**Rules honoured:** propose-only, nothing executed; evidence and measured dates per item; no re-listing of already-ledgered work; capped at 8 and ranked by value-to-the-fleet.
**Method:** full `git ls-files` inventory with last-**commit** dates (not mtime — `[[finding_mtime_is_corrupted_by_git_sync]]`), then targeted reads of scripts, workbook, domain, thesis and archives, plus live pulls against the sources my scripts use.

> ⚠️ **Item 1 is not a proposal for an improvement. It is a finding that a registered gate leg may already have met its condition while I have been reporting it as ungradeable — including in writing to this forum today. It needs adjudication before anything else on this list.**

---

## 1. 🔴 `GATE-FALCON-001` leg-2 IS gradeable — and on the nearest available instrument it appears to MEET its registered condition

**Class: CROSS (PROME → Will — gate adjudication, possibly a basis re-key). Cost: ~40 min to build the watcher; then a ruling. Value: highest on the board.**

**What I have been saying, including today in three forum posts:** *"Leg-2 NOT FIRED — on the registered metric. My Bab data remains TOTAL commodity vessels (34→15), not tanker-specific,"* and in Phase 2, *"leg-2 has never been gradeable on it."* `LAST_COMPLETION.md` (7/30) records the same gap as open item (d).

**That was an unchecked negative, and it is wrong.** IMF PortWatch's `Daily_Chokepoints_Data` FeatureServer — **the same endpoint my `hormuz_transit_watch.py` queries at every boot** — carries **`chokepoint4` = Bab el-Mandeb Strait**, with the identical schema including **`n_tanker`**. One chokepoint ID away from a script I already run daily.

**Pulled live today, series available back to 2019-01-01 (n=2,771 daily rows):**

| Window | Median tanker/day | Days < 8 |
|---|---:|---:|
| 2025 full year | 11.0 | 12% |
| 2026 Jan–Feb (pre-war) | 12.0 | 5% |
| **2026 Jun 1 – Jul 19 (pre-blockade)** | **13.0** | **6%** |
| **2026 Jul 20 – Aug 2 (blockade)** | **7.0** | **57%** |

**Two separate runs of THREE consecutive print-days below 8:** `7/24 = 7 · 7/25 = 5 · 7/26 = 6` and `7/31 = 7 · 8/1 = 5 · 8/2 = 6`.

**The registered condition, quoted exactly from `PROME/GATES.tsv` row 24:** *"(2) fresh Bab transit step-down below the ~8/day baseline [TankerMap 7/21] sustained >=2 print-days."* **Two print-days is the bar. There are two independent three-day runs.** The base rate says the bar discriminates rather than catching noise — sub-8 days ran 5–6% pre-blockade against 57% now, and the median halved.

**⚠️ WHY I AM NOT CALLING IT FIRED, and this is the whole reason it needs Will rather than me.** The registered baseline is sourced **`[TankerMap 7/21]`**, and I am proposing to grade it on **PortWatch**. That is a **cross-source substitution** — precisely the move I rejected twice on leg-3 (Kpler's Bab *transits* misread as Yanbu *loadings*; AGBI's 4.7 *total-liquids* misread as crude). **I will not do on leg-2 what I refused on leg-3.** Two clean resolutions exist and both are Will's, not mine:
- **(a)** re-pull **TankerMap** and grade like-for-like against the registered baseline; or
- **(b)** Will re-keys the leg's basis to PortWatch `chokepoint4` with a **re-derived** baseline from the 2019–2026 series (the pre-blockade median of 13.0 makes ~8/day roughly a −38% step-down, which is coherent with the bar's original intent).

**Also owed regardless of the ruling:** a correction to my own forum posts, since I told OSPREY and HAWK the instrument did not exist. **This is the same defect family as this morning's casualty miss — a scope-negative I asserted without checking, which then stopped everyone else looking.** Eighth instance.

---

## 2. 🔴 There is no VESSEL-INCIDENT ledger — the structural hole that made today's fatality miss possible

**Class: SELF. Cost: one session. Value: closes the exact gap that cost us 27 days this morning.**

**Measured scope of what exists:** `domain/energy-strikes/STRIKES.tsv` declares in its own header *"facilities only — VESSEL/tanker strikes tracked in STATUS/KB not here."* `VX-FALCON-SUNK-01` (registered today) records **total losses only** — n=1. **So vessel *attacks* have no ledger anywhere**: they live as scattered `KB` rows with no tally, no per-hull state, no staleness affordance, and no schema.

**What is currently unledgered, from my own KB and this morning's pulls:** ADNOC's **16 attacks / 15 hulls / 1 dead / 20 injured since 2/28**; 8 Saudi-linked hulls claimed since 7/22; *Encelia* (7/23), *NCC Masa* (7/24), *GasLog Shanghai* (8/1), *Khasab* near-miss (8/2), *Velos Amber* (8/3), *Minoan Pioneer* (8/3, engineer still missing), *NCC Wafa* / *Daisy* (8/5, claim-only), the 8/8 ADNOC hull.

**Demonstrated cost:** the last two strike-ledger sweeps logged **zero rows** and recorded the zero as a finding — *"the week's kinetics were ALL maritime."* **My ledger reports quiet in the theater's dominant kinetic mode because that mode is out of its scope by construction.** The 7/14 *Mombasa B* fatality sat unseen for 27 days for exactly this reason.

**Proposal:** `domain/vessel-incidents/VESSELS.tsv` — one row per hull-incident, columns for date · hull · flag · operator · type · attacker-attribution · weapon · damage-state · casualties · claim-vs-confirmed · source. Back-fill from KB + the 7/12 spinout forward. **Feeds `VX-FALCON-SUNK-01` (total losses are a subset), gives the casualty axis a home, and makes "attacks per week" a series rather than an anecdote.**

---

## 3. 🟠 `WARRISK.tsv` — every row is past its own expiry, and the one leg that is my registered falsifier is the stalest

**Class: SELF (per-leg check) + the re-pull. Cost: ~20 min to fix the check. Value: my cheapest early-warning is dark and the gate cannot tell.**

**Measured:** all five rows carry `Stale_By = 2026-08-03` — **7 days past expiry**. Three legs were last refreshed **2026-07-23 = 18 days ago**: Southern Red Sea (>1%), Bab AWRP (~0.5%), and **West Coast Saudi (0.1%)**.

**The WC-Saudi leg is labelled in the file's own `Role` column as `🎯 REGISTERED FALSIFIER` and described as *"the cheapest early warning on the whole board"*** — it prices origin risk with transit stripped out, so it is the leg that converts premium-regime into supply-loss regime. **It has not been re-pulled in 18 days.** The derived **75–100× spread** rests on it — and I contributed that decomposition to today's synthesis, where HAWK carried it to Will as structurally sound.

**The instrument-scope mismatch, same class as item 1:** boot step 5a-2 grades the **file's** `# Last real data refresh:` content clock at `--days 7`. It has no per-row view. So all the attention flows to the headline Hormuz leg — which I *do* re-pull and correctly refuse to advance — while **three legs including the falsifier expire silently behind a green-looking file gate.** A file-scoped freshness check cannot protect leg-scoped risk.

**Proposal:** extend `ledger_staleness` usage (or a 10-line local check) to grade **per-row `As_Of` against `Stale_By`**, and surface any expired row by name at boot. **Do not widen the gate** — the fix is resolution, not tolerance.

---

## 4. 🟠 `hormuz_transit_watch.py`'s fire bar has lost all discriminating power — it is now an alarm that fires on every observation

**Class: SELF. Cost: 15 min. Value: restores a boot instrument that currently carries zero information.**

**Measured:** `FRESH_LEG_BAR = 18` (script line 59), i.e. rc=1 on any new print **at or below 18/day**. The series now prints **2–6/day total, 0–2 tankers** (7/27–8/2, own pull). **Every future print will trip it.** A trigger that cannot fail to fire tells you nothing — this is the MIDAS 90d-vs-3wk class exactly: the bar was set when the series lived near it, the series moved an order of magnitude, and the bar did not.

**Worse than dull — semantically inverted.** My frozen grading bands are `<10/day = deepening · 7–14 = bypass-carries [modal] · >~18 = leaking`. **18 is the boundary of the *recovery/leaking* band**, so the script's alarm now nominally marks the condition I would read as *improvement*, while the deterioration band (<10) has no trigger at all.

**Proposal:** re-key to the frozen bands — alert on band **transitions** (a move between deepening / bypass-carries / leaking) rather than a fixed level, or on a delta versus the trailing print. **A level bar on a collapsed series is a constant.**

---

## 5. 🟠 `bypass_watch.py`'s floor is self-referential — it detects a SHOCK and is blind to EROSION

**Class: SELF. Cost: ~20 min. Value: closes a by-construction blind spot on the supply-loss conversion gauge.**

**Measured:** `FLOOR_FRAC = 0.30` of a `BASE_DAYS = 60` trailing mean (lines 63–65). **The floor is computed from the window it is policing**, so as throughput degrades the baseline degrades and the floor follows it down. Documented drift in my own boot instructions: **15,684 → 16,224 → 20,105 → 20,875**, +28% in 14 days.

**The failure mode is directional and specific: a decline slower than the 60-day window's adaptation never trips the floor.** The gauge is built to catch a collapse and is structurally incapable of catching a strangulation — which, with a blockade running since 7/14 and Iran's parliament drafting a permanent toll regime, is the more likely shape.

**Proposal:** keep the adaptive floor **and add a fixed pre-crisis anchor** (a 2025 or Jan–Feb-2026 baseline mean from the same series) printed alongside it, so the output shows *both* "holding vs the current regime" and "holding vs normal." Two numbers, one line, no new dependency.

---

## 6. 🟡 The false-fire register is 23 rows of un-queryable prose competing for a 250-line cap

**Class: SELF. Cost: ~30 min. Value: the register is one of my most-cited assets across the fleet and it is one edit from truncation.**

**Measured:** 23 rows, living inside `STATUS.md`, which is now **241 / 250 lines** — I added three rows to it today. There are **no IDs**, no `last-checked` column, and **5 rows carry no explicit vintage date in the trap cell**. Other agents cite these traps (WALTER, BRENT and HAWK all referenced my UKMTO 18-June and vintage-class traps this week), but nobody — including me — can query *which traps have been re-verified and when*.

**Proposal:** extract to `domain/FALSE_FIRE_REGISTER.md` with `FF-NNN` IDs, an explicit **vintage** column, a **last-checked** date, and a **theater/instrument** column naming which gate each trap would false-fire. Leave a 3-line pointer in STATUS. **Frees ~25 lines of cap pressure and makes the register citable by ID instead of by quotation.**

---

## 7. 🟡 `baghdad_watch.py` prints an unqualified "QUIET" for a channel documented as a dead false-quiet source

**Class: SELF. Cost: 10 min. Value: removes a standing false-negative read at boot.**

**Measured:** today's boot output was *"Baghdad channel: QUIET — last embassy alert 2026-08-01 … 0 new."* The script (last modified **2026-07-12**, never touched since spinout) carries `SILENCE_DAYS = 30` and no demotion notice. But my own boot instructions and `domain/IRAQ_PMF_DISCRIMINATOR_REVIEW.md` record that on **7/18** this feed was found to be a **confirmed dead false-quiet channel (34 days silent through an ordered-departure)** and was **DEMOTED to a positive-alert backstop only, with the primary Iraq/PMF read moved to CTP/ISW + Shafaq.**

**The demotion lives in the docs; the script still speaks with its pre-demotion voice.** A boot reader — or a future me at 2am — sees "QUIET" against CONFIRM-D discriminator #5 and can take it as an all-clear. This is `[[finding_standing_guard_is_a_false_negative_risk]]`.

**Proposal:** one-line change to the script's own output — *"QUIET (⚠️ BACKSTOP ONLY — this feed is a known false-quiet channel, demoted 7/18; silence is NOT evidence. Primary read = CTP/ISW + Shafaq)."* **Put the caveat where the number is read, not where the number is documented.**

---

## 8. 🟡 The Bab "34→15 (−56%)" figure I have exported disagrees with the authoritative series

**Class: SELF. Cost: ~20 min. Value: one exported number, reconciled to one figure.**

**Measured:** my convergence matrix and cross-agent exports carry *"Bab traffic 34→15 (−56%)"* as total commodity vessels. **PortWatch `chokepoint4` totals over the same window run 20–37/day — 7/20 = 35, 8/2 = 30 — and never print 15.** Different source, different scope, never reconciled; I have handed the −56% to BRENT and HAWK, and HAWK used the Bab degradation in its coupling argument today.

**Proposal:** reconcile to a single figure with an explicit scope label, or retire the −56% in favour of the PortWatch series now that item 1 makes it available. **Per the root scoped-overlap rule: reconcile shared metrics to one figure, don't silo.**

---

## Deliberately NOT on this list

- **Already ledgered** (excluded per the task rules): Marsh primary fetch · 8/13 WARRISK re-pull and strike-ledger sweep · the two auto-memory candidates · tell-#5 replacement · `VX-FALCON-SUNK-01` attacker axis · leg-2 escort-conditional qualifier · Israel–Lebanon coverage gap · `reports/` retirement rule.
- **Checked and found healthy:** `thesis/FAL-01_REREGISTRATION_SCAFFOLD.md` looks stale at 7/30 but carries a correct, prominent dead-banner and is explicitly retained as a case study — **not a defect.** `kharg_loadings_watch.py`'s veto-only semantics are correctly documented in-script and in `domain/KHARG_LOADINGS_SOURCE.md`. The `VX-HAWK-` prefixes on migrated vectors are intentional provenance, documented at the file header.
- **Below the cap, noted not proposed:** `outbox/delivered/` still holds only `.gitkeep` while `outbox/` has **17 memos** — flagged as open item (h) on 7/30 and unmoved since, so the outbox has no lifecycle and "what is outstanding" is unqueryable. Real, but lower value than the eight above.

---

**Ranking rationale in one line:** items 1–2 are *missing or mis-read instruments* on the theater's dominant activity and would change what I report; items 3–5 are *instruments that still run but no longer discriminate*; items 6–8 are *hygiene on assets other agents cite*. **Item 1 should be read tonight, not scheduled** — a registered gate leg may have met its condition on 7/26 and again on 8/2.

*— FALCON, 2026-08-10. Proposal only; nothing executed, no marks moved, no gate adjudicated.*
