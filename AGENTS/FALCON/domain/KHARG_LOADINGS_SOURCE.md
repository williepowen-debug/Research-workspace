# FALCON — Kharg Export-Loadings Data Source (FROZEN SPEC)
**Built:** 2026-07-18 ~18:00 ET (Sat-eve wave, PROME-tasked) · **Owner:** FALCON · **Consumers:** TERRY (TRY-FIRE-006 / GATE-TERRY-006), PROME (gate arming), BRENT (energy synthesis), RED (reversibility finding A)
> ⛔ **GATE STATUS SUPERSEDED 2026-08-20 — `GATE-TERRY-006` is RETIRED** (PROME `006d32172`, on FALCON's recommendation; consuming card `TRY-FIRE-006` retired by Will 8/18). **This document is now HISTORICAL for its gate purpose.** Two grounds, both instrument-side: door (b) Kpler/Vortexa was the only QUANTITATIVE corroborator and this fleet has no API/credential/fetcher for it; and **the PortWatch veto frozen below FAILED A KNOWN-POSITIVE CONTROL** — it printed 0 t / 0 calls for 8/08–8/14 including **8/12**, the day a NITC VLCC demonstrably loaded ~2M bbl at Kharg (`KB-FALCON-098`). ⛔ **RETIRED ON INSTRUMENT GROUNDS ONLY — this is NOT evidence against the premise.** The Kharg-strand premise is LIVE and demonstrated itself: **Kharg loadings were genuinely halted 25 days, 2026-07-18 → 2026-08-12** (`KB-FALCON-097`). The premise held; the instrumentation failed. **The source freeze and the semantic-gap analysis below remain VALID and worth reading** — they are why the numeric trigger was disqualified in the first place, and that reasoning is preserved as §1 of `AGENTS/TERRY/research/PLAYBOOK_flow-trigger-supply-strand.md`. ⚠️ **Any successor gate must state HOW its quantitative corroborator is pulled BEFORE registration** (PROME's binding note at retirement).
>
> *(Superseded banner retained for provenance:)* **✅ GATE STATUS (7/20):** GATE-TERRY-006 was **REGISTERED LIVE in GATES.tsv (7/18)** on the corroborator-anchored merged condition below — PROME + TERRY confirmed 7/20, trigger inversion applied (corroborator fires; PortWatch/Kpler = refuting VETO only, ≥2 observed days, live-dated-primaries-only). This spec is the frozen source reference behind that VETO. Weekend 7/18-20 corroborator sweep = NEGATIVE → gate correctly unfired.
**Purpose:** Freeze the data source for the **Kharg export-loadings** observable that GATE-TERRY-006 needs — and be brutally honest about the semantic gap between what the gate wants (barrels physically not leaving Kharg) and what the best free/official observable actually measures.

> **⚠️ HEADLINE VERDICT (read before anything below):** A pullable, official, free Kharg export series **exists** (IMF PortWatch `Daily_Ports_Data`, `portid='port2164'`, `export_tanker` field). **But it CANNOT be the gate's fire signal.** It is an **AIS-based series and Iran's crude leaves Kharg on a dark/AIS-off "shadow fleet"** — so PortWatch is **~90%+ blind to Kharg's true throughput and reads literal ZERO for entire NORMAL months.** A naive "≈0 for ≥2 days" test fires on a normal week. Its discriminating power on the strand question is **near-zero — worse than the Hormuz transit count PROME already ruled out.** The series is usable only in the **refuting direction** (a nonzero print proves flow *continues*) and as a weak necessary-condition. **The FIRE evidence must come from a dark-fleet-capable corroborator** (official declaration / Kpler-Vortexa-TankerTrackers / Kharg-specific war-risk notice). Details, numbers, and the operationalized threshold below.

---

## 1. The series that exists — exact recipe (pullable, official, free)

| Attribute | Value |
|---|---|
| **Provider** | IMF PortWatch (same org/infra as the working `hormuz_transit_watch.py`) |
| **Dataset** | `Daily_Ports_Data` FeatureServer, layer 0 |
| **Endpoint** | `https://services9.arcgis.com/weJ1QsnbMYJlCHdG/ArcGIS/rest/services/Daily_Ports_Data/FeatureServer/0/query` |
| **Kharg portid** | **`port2164`** (portname `Kharg Island`, country Iran) — *confirmed present 2026-07-18 pull* |
| **Loadings field** | **`export_tanker`** (estimated outbound tanker shipment volume, **metric tons/day**). Companion: `portcalls_tanker` (count of tanker port calls/day), `export` (all-cargo export tons). |
| **Update cadence** | Daily rows, **but published with a ~5–8 day lag** (identical to the chokepoint series). As of the 2026-07-18 pull the **newest Kharg row is 2026-07-10 (8d old)**. |
| **Access** | Public ArcGIS REST, no key. Browser-class UA courtesy header. Same access pattern as the transit script. |
| **Sibling Iran ports** (for context/cross-read) | Bandar Abbas `port107`, Bandar Khomeini `port108`, Bandar-E Pars `port105`, Bushehr `port196`, Abadan `port2477`, Bahregan `port2478`, Lavan `port2165` |
| **Scripted puller** | **`AGENTS/FALCON/scripts/kharg_loadings_watch.py`** (built same session — clone of the transit watcher; see §6) |

**Query template (verbatim, reproducible):**
```
where=portid='port2164'&outFields=date,portcalls_tanker,export_tanker,export
&orderByFields=date DESC&resultRecordCount=60&returnGeometry=false&f=json
```

---

## 2. What it actually measures vs. what the gate wants — THE SEMANTIC GAP

**The gate wants:** *"Kharg crude barrels physically stop leaving"* — a supply-loss event (seizure that halts loadings, blockade, insurance-withdrawal shut-in, Iranian shut-in).

**`export_tanker` actually measures:** *IMF's AIS-derived estimate of tanker-borne export tonnage detected departing the Kharg port polygon.* PortWatch's own methodology (portwatch.imf.org/pages/data-and-methodology): estimates built from **satellite + terrestrial AIS signals** on ~90,000 ships, converted to trade tonnage via load-factor modelling.

**Why that is a near-fatal gap for THIS port specifically — two compounding failures:**

**(a) DARK-FLEET INVISIBILITY (the killer).** Iran exports ~1.577 Mbpd from Kharg (~90–96% of national crude+condensate; Kpler via Reuters/Bloomberg, 2026-07) on a **shadow fleet that spoofs, disables, or gaps AIS by design** to evade sanctions. PortWatch is AIS-based → **it cannot see the vessels that carry the cargo.** Empirically confirmed by direct pull (2026-07-18):

| Kharg `port2164`, 2026 YTD | tanker calls | export_tanker sum (t) | days | avg t/day |
|---|---:|---:|---:|---:|
| Jan | 0 | **0** | 31 | 0 |
| Feb | 2 | **0** | 28 | 0 |
| Mar | 2 | 5,496 | 31 | 177 |
| Apr | 1 | 103,536 | 30 | 3,451 |
| May | 0 | **0** | 31 | 0 |
| Jun | 5 | 424,804 | 30 | 14,160 |
| Jul (→7/10) | 0 | **0** | 10 | 0 |

Iran was **exporting normally in Jan, May, and early Jul** — yet PortWatch shows **literal zero.** Real Kharg throughput ≈ 205,000 t/day (~6M t/month); PortWatch's **best-ever month (June) captured 424,804 t ≈ 7% of reality.** The series is **~90%+ blind and reads zero for whole normal months.**

**(b) LUMPY, NOT A DAILY FLOW (a general PortWatch property, positive-control-verified).** `export_tanker` is **event-driven** (a spike when a departure is detected), not a smoothed daily rate. Even terminals PortWatch *does* see well are zero most days — positive controls, trailing-30d (2026-07-18 pull):

| Terminal (non-dark-fleet control) | export_tanker nonzero-days / 30 | median t/day |
|---|---:|---:|
| Ras Tanura (Saudi Aramco mega-terminal) `port1091` | 9/30 | **0** |
| Juaymah (SAU) `port526` | 6/30 | 0 |
| Basrah Oil Terminal (IRQ) `port2479` | 6/30 | 0 |
| Fujairah (ARE) `port362` | 17/30 | 9,258 |
| **Kharg (IRN)** `port2164` | **4/30** | **0** |

Ras Tanura — one of the busiest oil terminals on earth — shows export on only **9 of 30 days, median 0.** So even ignoring the dark-fleet problem, a "zero today" print carries almost no information: **zero is the modal daily state everywhere.**

**Net:** the only free/official observable for Kharg loadings is a **false-quiet machine.** "≈0 for ≥2 days" is satisfied by the baseline; it fires (or sits pre-fired) on normal weeks. It fails the exact test PROME applied to kill the transit-count anchor (86.6% crisis-day base rate) — and fails it *harder* (Kharg reads 0 on ~85%+ of all days, war or peace).

---

## 3. False-fire / false-quiet modes & the corroborator that patches each

| Mode | Direction | What happens | Patch (corroborator) |
|---|---|---|---|
| **Dark-fleet zero** | FALSE QUIET | Series reads 0 for a normal export month (Jan/May/Jul all 0) → "strand" that isn't | **Kpler/Vortexa/TankerTracker read** — these firms specialize in dark-fleet inference (satellite imagery + AIS-gap + floating-storage). They see what PortWatch can't. Their Iran-export figure is the true measure. |
| **Lumpy-zero** | FALSE QUIET | Real loadings happened but no departure detected in the 2-day window (median-0 even at Ras Tanura) | Widen the window: trailing-**14d** sum, not daily-zero. Plus corroborator. |
| **Publication lag** | FALSE QUIET (timing) | 5–8d lag → a strand that started today is invisible for a week | **This is why the scripted series can NEVER be the leading fire signal on a fast weekend event.** The declaration / news / war-risk notice leads the data by ~a week. |
| **Seize-but-flow-continues** | FALSE FIRE (of the political headline) | "Seizure" announced but loadings continue | **Series' ONE good direction:** a *nonzero* Kharg print (or Kpler showing flows) **REFUTES** the strand → do NOT fire. PortWatch is trustworthy when it says "a tanker loaded"; untrustworthy when it says "zero." |
| **Bypass/STS replacement** | FALSE FIRE (of a supply-loss read) | Loadings shift to STS off Fujairah/Sohar; barrels still leave | Kpler/Vortexa "restoring flows" language (already cited in STATUS) → hold, don't fire. |
| **Stale-vintage story** | FALSE FIRE | April-vintage "Bandar Abbas refinery" recirculation (FALCON trap register) | Require a **live-dated** primary, not a restatement. |

**The load-bearing inversion:** because PortWatch's zero is uninformative but its *nonzero* is informative, the series' real job in the gate is **anti-false-fire (refutation), not fire.** The FIRE must be carried by a corroborator that can see the dark fleet.

---

## 4. Trailing-30d baseline & threshold — operationalized honestly

**Requested:** operationalize "≈0 or ≤~10% of baseline for ≥2 observed days" against the real series.

**Finding:** the requested formulation is **not usable as written**, because:
- **Trailing-30d baseline (ending 7/10): export_tanker sum = 424,804 t; nonzero on 4/30 days; 26/30 days already read 0.** The "baseline" is itself mostly zeros driven by ~4 lumpy June detections.
- **10% of a 424,804 t/30d baseline ≈ 42,480 t over 30d ≈ 1,416 t/day.** The series is *below* that on 26 of the last 30 days **in a normal regime.** The threshold is pre-tripped by noise.
- **A daily "≈0 for ≥2 days" test is TRUE right now** (7/4–7/10 all zero) with **no strand** — Iran is exporting via the dark fleet.

**Honest operationalization — what CAN be scripted (necessary, not sufficient):**
- Use a **trailing-14-day SUM** of `export_tanker` and `portcalls_tanker`, not a daily-zero test.
- A strand is **consistent-with** (never *proven-by*) `trailing-14d export_tanker sum == 0 AND trailing-14d portcalls_tanker == 0`, sustained as new (lagged) prints land.
- But since whole normal months already satisfy that, **the scripted collapse is a NECESSARY background condition at most — it can never itself arm the gate.**
- **The scripted series' decisive use is the REFUTING print:** *any* nonzero Kharg `export_tanker` or `portcalls_tanker` in the trailing window = flow ongoing = **gate must NOT fire.**

**Bottom line on the numeric bar:** there is **no defensible free-data numeric threshold that fires the gate.** The bar cannot be frozen on PortWatch. It must be frozen on the **corroborator menu** (§5), with PortWatch as the veto/cross-check.

---

## 5. The corroborator menu (this carries the FIRE — ranked)

A Kharg strand is **CONFIRMED for gate purposes** when **≥1 of the following live-dated corroborators fires AND the PortWatch/Kpler cross-check does not refute it** (no detected ongoing loadings):

1. **Official declaration** — Iranian export-suspension statement, OR an official seizure/blockade declaration affecting the Kharg loading complex (state media / IRNA / SHANA / SOMO-equivalent / US CENTCOM interdiction notice naming Kharg). *Live-dated primary, not April-vintage recirculation.*
2. **Dark-fleet tracker collapse** — **Kpler** (Homayoun Falakshahi is the Reuters-quoted Iran analyst) or **Vortexa** ("Iran Crude Situation Report") or **TankerTrackers.com** showing Iran/Kharg crude exports collapsing to ~0. These are the **only sources that actually see the shadow fleet** — they are the true measure the gate wants. *Free access = press citations (Reuters/Bloomberg) + their public posts; not a scripted API.*
3. **Kharg-specific war-risk / P&I withdrawal** — a UKMTO/JWC/Lloyd's/P&I notice naming **Kharg / Bandar-e-Emam specifically** (not the standing generic Gulf JWLA-033 listing). Underwriters pull cover when barrels genuinely can't move.
4. **FALCON Kharg-seizure tripwire** (§ merged condition, routed to PROME this session) — my own escalation-ladder read that a de-facto Kharg stoppage is underway.

**Anti-false-fire on the corroborators (all four apply):**
- Require **live-dated** evidence (traps: April Bandar Abbas refinery story; export-terminal *near*-misses like the 7/16 Iraq drone-near-a-tanker that SOMO explicitly said did NOT target the terminal).
- **Seizure label ≠ strand** — a seizure that maintains loadings does NOT fire (Will's 7/17 "seize-but-flow-continues" branch).
- **Bypass cross-check** — if Kpler/Vortexa show STS/shuttle volumes replacing Kharg loadings, the supply-loss is being absorbed → hold.
- **≥2 observed days** of stoppage (single-day gaps are weather/ops).

---

## 6. Scripted puller — `kharg_loadings_watch.py`

Built this session (clone of `hormuz_transit_watch.py`, same ArcGIS infra). Role, stated in its own docstring: **cross-check / refutation tool, NOT a fire signal.** It reports the newest Kharg print, its age, and the trailing-14d sums; it flags `rc 1` on a **nonzero** print (flow-continuing = REFUTES a strand — the informative direction) and `rc 0` on a quiet/zero window (which is the *uninformative* normal state, explicitly NOT a fire). `rc 2` on fetch failure. State JSON committed for cross-machine continuity.

---

## 7. One-paragraph declaration back to PROME/TERRY (the freeze)

**FROZEN:** The Kharg-loadings observable is **IMF PortWatch `Daily_Ports_Data` port2164 `export_tanker`** (metric tons/day; `portcalls_tanker` companion), pullable via `kharg_loadings_watch.py`, ~5–8d lag. **It is confirmed pullable but is NOT armable as the gate's numeric trigger** — it is AIS-based and ~90%+ blind to Kharg's dark-fleet throughput, reading literal zero for entire normal export months, so no free-data "≈0 for N days" threshold discriminates a strand from a normal week. **Therefore GATE-TERRY-006 must fire on the corroborator menu (§5), with PortWatch/Kpler serving as the refuting cross-check (any detected loading = do-not-fire), not as the primary observable.** This is the honest closure of the open dependency: the gate can go **armable on a corroborator-anchored condition**, but it **cannot** be anchored on a scripted free series. Merged single condition → §merged proposal in the closeout memo.

---
*[2026-07-23 hygiene-sweep footnote — spec FROZEN, tables above unchanged]* Re-ran `kharg_loadings_watch.py` 7/23: PortWatch has since published the **7/11-7/17 window, and it reads literal 0 t across all 7 days** (trailing-14d export_tanker sum = 0, calls = 0). This is exactly the **dark-fleet-blind false-quiet** this spec documents (Jan/May/early-Jul all read 0 during normal exporting) — it is **NOT a strand signal** (rc 0 = UNINFORMATIVE). The positive-control finding stands: the series remains usable only as a refuting veto, never as a fire. No change to GATE-TERRY-006's corroborator-anchored condition.
