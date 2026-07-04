# CREED Workbook — Design Spec (build-ready)

**Created:** 2026-07-04
**Status:** DESIGN — awaiting Will review, then build (Will chose "design doc first, build next session").
**Author:** CREED (Tier-2). Modeled on the fleet-standard workbook after a 7/4 survey of 46 workbook dirs (REGINALD `VX.tsv` = primary model; canonical `SCHEMA.tsv` from BOND/CARL; legacy CREED `FLOW.tsv` pulled forward).

---

## 1. Purpose & where the workbook sits

A **structured, live, machine-scannable dashboard** for national CRE/CMBS stress — the quantitative spine under CREED's prose rails. Canonical-truth ordering (per fleet data-hygiene rule):

- **`STATUS.md`** = canonical current-state synthesis (narrative). Wins on any conflict.
- **`thesis/THESIS.md`** = mechanism map + 8 Expected Signals + convergence matrix (narrative rails).
- **`research/REFRESH_YYYY-MM-DD.md`** = dated point-in-time source packs.
- **`workbook/`** (this) = the **live metric layer** — one row per monitored number, thresholds, RAG status, cross-agent links, time series. The VX vectors are the 8 Expected Signals expressed as tracked numbers.

The workbook does **not** replace STATUS/THESIS; it operationalizes them. If workbook and STATUS disagree, STATUS is right and the workbook is stale — fix the workbook.

## 2. File manifest (`AGENTS/CREED/workbook/`)

| File | Role | Priority |
|---|---|---|
| `SCHEMA.tsv` | governs KB.tsv columns + controlled vocab | build |
| `VX.tsv` | vector dashboard (the heart) | build |
| `FLOW.tsv` | CRE transmission chains | build |
| `KB.tsv` | Admiralty-scored research memory | build |
| `PREDICTIONS.tsv` | forecasts w/ resolution tracking | build |
| `VX_HISTORY.tsv` | monthly time series of key vectors | build |
| `WORKBOOK_DESIGN.md` | this spec | done |

Legacy workbook (`AGENTS/REGINALD/sub-agents/CREED/workbook/`) stays **frozen archive** (freeze-banner flagged to REGINALD 7/4). This new workbook is the live one. Migration = **seed-from-refresh** (map legacy structure, refresh every value to current), **not** wholesale copy.

## 3. `SCHEMA.tsv` — adopt the canonical KB schema

Copy the fleet-standard 13-column KB schema (BOND/canonical). Columns: `ID, Date, Group, Entity, Fact, Source, Conf, Epistemic, Status, Stale_By, DerivedFrom, Vectors, Notes`.
- `Conf` = Admiralty digraph (A1–F6: letter=source reliability, number=info credibility).
- `Epistemic` = EMPIRICAL / ESTIMATE / ASSUMPTION.
- `Status` = ACTIVE / CONFIRMED / STALE / SUPERSEDED / CORRECTED.
- `Group`/`Entity`/`Source` draw from `AGENTS/VOCABULARIES.tsv` where listed.
- **No** `Delegated_To` column (CARL-only; CREED has no sub-agents). Optionally add `Last_Refreshed` (CARL's 15-col variant) — recommend **yes**, it's cheap and useful for a spawn-on-need agent.

## 4. `VX.tsv` — vector dashboard (BUILD-READY SEED)

**Columns** (REGINALD model): `ID, Name, Category, Current_Value, Yellow, Orange, Red, Status, Confidence, Last_Updated, Source, Cross_Links, Notes`.

**Category taxonomy (CREED):** `1-CMBS_DQ · 2-Special_Servicing · 3-Maturity_Wall · 4-Bank_Transmission · 5-Forced_Sale_NAV · 6-Multifamily · 7-Office_Demand_REIT · 8-Modifications · 9-Mechanism`

**Seed vectors** (values as of the 7/4 refresh; `S#` = maps to THESIS Expected Signal):

| ID | Name | Cat | Current [as-of] | Y | O | R | Status | Conf | Src | X-Links | Signal |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VX-CREED-1.01 | Office CMBS DQ | 1 | 11.57% [Trepp Jun] | >10 | >11 | >12 | 🟠 ORANGE | 90 | Trepp Jun | REGINALD | S1 |
| VX-CREED-1.02 | Overall CMBS DQ | 1 | 7.35% (9.53% mat-adj) [Jun] | >7 | >8 | >9 | 🟠 | 90 | Trepp Jun | — | S1/S2 |
| VX-CREED-1.03 | Multifamily CMBS DQ | 6 | 7.23% [Jun, +28bps] | >6 | >7 | >8 | 🟠 | 90 | Trepp Jun | CARL | S5 |
| VX-CREED-1.04 | Retail CMBS DQ | 1 | 6.91% [Jun] | >6 | >8 | >10 | 🟡 | 85 | Trepp Jun | CARL | — |
| VX-CREED-1.05 | Lodging CMBS DQ | 1 | 5.22% [Jun, −79bps cure] | >6 | >8 | >10 | 🟢 | 85 | Trepp Jun | — | — |
| VX-CREED-2.01 | Office Special Servicing | 2 | 16.75% [May; **Jun owed**] | >15 | >17 | >18 | 🟠 STALE | 85 | Trepp May | REGINALD | S1 |
| VX-CREED-2.02 | Overall Special Servicing | 2 | 10.86% [May; Jun owed] | >9 | >11 | >13 | 🟠 STALE | 85 | Trepp May | — | S1 |
| VX-CREED-3.01 | CMBS Maturity-Adj DQ | 3 | 9.53% [Jun] = multi-yr high | >8 | >9 | >10 | 🟠 | 88 | Trepp Jun | LIQUID | S2 |
| VX-CREED-3.02 | 2026 Hard Maturities | 3 | $76.6B, 39% Q4, 36% DY≤8% | qual | qual | qual | 🟠 | 85 | Trepp | LIQUID | S2 |
| VX-CREED-3.03 | 2026 CMBS Maturities | 3 | >$100B, >50% exp non-repay | qual | qual | qual | 🟠 | 80 | Morningstar DBRS | LIQUID | S2 |
| VX-CREED-4.01 | Bank Non-Owner CRE PDNA (>$250B) | 4 | 3.40% [FDIC Q1] (↓6th qtr) | >4 | >4.5 | >5 | 🟠 | 90 | FDIC Q1 QBP | **REGINALD (shared)** | S3 |
| VX-CREED-4.02 | Community-Bank Reserve Coverage | 4 | 146.6% [FDIC Q1] | <150 | <140 | <130 | 🟠 | 85 | FDIC Q1 QBP | REGINALD | S3 |
| VX-CREED-4.03 | Overall Bank PDNA | 4 | 1.53% [FDIC Q1] | >1.75 | >2 | >2.5 | 🟢 | 90 | FDIC Q1 QBP | REGINALD | S3 |
| VX-CREED-5.01 | Forced-Sale / NAV Recognition | 5 | CLUSTER [realized] | 1 comp | cluster | fund gates | 🟠 | 80 | WALTER/BOARD | REGINALD,LIQUID | S6 |
| VX-CREED-6.01 | Multifamily Term-Default Broadening | 6 | BUILDING [Jun+Sunbelt cluster] | isolated | TX-conc | nat'l | 🟠 | 80 | Trepp+WALTER | **CARL** | S5 |
| VX-CREED-7.01 | Office REIT tape (VNQ vs SPY) | 7 | −2.9pp/3mo, +6.3pp/1mo [7/2] | −5pp | −8pp | −10pp | 🟢 COUNTER | 90 | fetch.py 7/2 | LIQUID,HENRY | S8 |
| VX-CREED-7.02 | Office-Demand / AI Structural | 7 | narrative-only; DC=strength | tape+data | leasing hit | vacancy accel | 🟡 | 75 | — | REGINALD | S7 |
| VX-CREED-8.01 | CRE Modification Exhaustion | 8 | no evidence (E&P still working) | 2nd-mod↑ | re-default↑ | mods↓ | 🟡 | 75 | — | REGINALD | S4 |
| VX-CREED-9.01 | CMBS Book Flow (MBA) | 9 | −$9.6B Q1 (vs banks +$17.5B) | shrinking | −$15B | −$25B | 🟠 | 82 | MBA Q1 | LIQUID,REGINALD | — |
| VX-CREED-9.02 | Office Price Index (Green St CPPI) | 9 | ⚠️ refresh (legacy −24% pk) | >−15 | >−25 | >−35 | GAP | — | Green St | REGINALD | — |
| VX-CREED-9.03 | Office Vacancy | 9 | ⚠️ refresh (legacy ~19–20%) | >15 | >18 | >20 | GAP | — | CBRE/JLL/Yardi | — | S7 |

**Thresholds are directional starters** — reconcile at build; a few (1.02, 2.02) need the analyst's judgment on band placement. **GAP rows** (9.02/9.03) = need a fresh pull at build. **Shared vectors** (4.01 Bank CRE PDNA) must **reconcile to REGINALD's one figure, not fork** — cite REGINALD-canonical, mirror the value (same rule REGINALD uses for LIQUID's HY OAS: "reference, don't fork").

## 5. `FLOW.tsv` — transmission chains (refresh the legacy 6)

Columns: `Flow_ID, Name, Speed, Status, Layer, Trigger, Current, Key_Insight, Sends_To`. Pull forward the legacy 6, refresh `Current`/`Status` to July 2026:

| Flow | Refresh to current |
|---|---|
| FLOW-CREED-01 CRE Doom Loop | Office CMBS 11.57% 🟠 / Bank PDNA 3.40% — still selective, pre-cascade |
| FLOW-CREED-02 Maturity Wall Cascade | ARMED — mat-adj DQ 9.53% multi-yr high; $76.6B hard, 39% Q4 |
| FLOW-CREED-03 Open-End Fund NAV Cascade | realized-comp CLUSTER now (205 W Randolph −72%, Aon −58%, S2 Capital) |
| FLOW-CREED-04 HOA Super-Lien (FL/NV) | **flag CORAL overlap** — FL property-tax burden-shift (SIG-627-027) |
| FLOW-CREED-05 Extend-and-Pretend Collapse | still ABSORBING at aggregate (Jun lodging cure + mods); asset-level recaps FAILING (Aon, Seattle OZK) |
| FLOW-CREED-06 Lease-Expiration Vacancy Ratchet | MONITORING — office vacancy refresh owed |

## 6. `KB.tsv` — seed fresh, don't import stale

Use the §3 schema. **Do not import the 40KB legacy KB** (Jan–Mar 2026, mostly superseded). Seed ~10–15 current Admiralty-scored rows from this session: June Trepp print (B2), the recognition cluster (each comp with its SKIP-VERIFY conf → Admiralty, e.g. single-source connectcre = C3/D3; WALTER-CONFIRMED S2 Capital = B2), 7/2 REIT tape (A2), FDIC Q1 (A1), MBA Q1 flows (B2). Link each to its VX vector via the `Vectors` column.

## 7. `PREDICTIONS.tsv` — seed live forecasts

Columns: `Pred_ID, Date_Made, Prediction, Confidence, Timeframe, Status, Date_Resolved, Outcome, Notes`. Seed candidates (confirm at build):
- PRED-CREED-001: Office CMBS DQ breaks >12% & holds by Q4-2026 — conf? — OPEN
- PRED-CREED-002: June office Special Servicing prints >17% (vs May 16.75%) — conf? — OPEN (resolves on June SS print)
- PRED-CREED-003: OZK Q2 (mid-late July) shows a CRE provision bump tied to the Seattle deed-in-lieu — conf? — OPEN → REGINALD
- PRED-CREED-004: Multifamily term-default S5 "broadens outside NY/NJ/Houston/TX" by Q4-2026 — conf? — OPEN → CARL

## 8. `VX_HISTORY.tsv` — seed the monthly series

Columns: `Vector_ID, Date, Value, Status, Notes`. Seed the two load-bearing series:
- **Office CMBS DQ:** Jan 12.34 · Feb 11.4 · (Mar) · Apr 11.69 · May 11.53 · **Jun 11.57**
- **MF CMBS DQ:** Mar 7.15 · Apr 7.71 (ATH) · May 6.95 (cure) · **Jun 7.23**
- (add SS + maturity-adj DQ as prints accrue)

## 9. Boot / closeout wiring (add at build)

- **CLAUDE.md boot order** — add after THESIS/CHANGELOG: "read `workbook/VX.tsv`; run mtime staleness check."
- **Staleness alert (data-hygiene rule, LIVE-with-alert not FROZEN):** at boot, if `VX.tsv` mtime > ~14d, surface "⚠️ VX stale Nd — refresh the latest monthly CMBS/SS + REIT tape before citing." Calibrated for a **Tier-2 spawn-on-need** agent (staleness *between spawns is expected* — the alert prompts a refresh, doesn't imply neglect).
- **Closeout** — update `Last_Updated` on refreshed vectors; append `VX_HISTORY` rows for new monthly prints; log session findings to `KB.tsv`; update `PREDICTIONS` status on resolution.
- **Cross-links** — REGINALD (4.01 shared, reconcile-not-fork), CARL (1.03/6.01), LIQUID (3.x/9.01), CORAL (FLOW-04 FL). Route only on signal FIRE per the Route Matrix; the workbook doesn't change routing.

## 10. Open decisions for Will (confirm at build)

1. **`Last_Refreshed` column** in SCHEMA — add it (recommend yes)?
2. **Prediction confidences** (§7) — set them, or leave OPEN-unscored until I have conviction?
3. **Threshold bands** on the softer vectors (1.02 overall DQ, 2.02 overall SS, 9.x mechanism) — my starters, or want to set them together?
4. **GAP vectors** (office vacancy 9.03, Green St CPPI 9.02) — pull fresh at build (office vacancy is web-available; Green St CPPI may be paywalled → proxy or leave GAP)?
5. Anything to **add/drop** from the 21-vector seed list.

---

*Build = transcription of this spec + the GAP-vector pulls + confirming §10. Estimated one focused session. Legacy workbook remains frozen archive; this becomes CREED's live dashboard.*
