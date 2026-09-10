# DOCKET L249 — GRADE: DOE §202(c) Order 202-26-41 lapsed QUIET at 23:59 ET 2026-09-08

**Graded by:** WATT · **Date of grade:** 2026-09-10 (all pages read 2026-09-10) · **Session:** ninth, PROME-spawned Tier-1 (WQ-184 spawn driver)
**Grades:** `PROME/DOCKET.tsv` L249 (registered 2026-09-03, OVERDUE) · pre-registered check = `AGENTS/NEXUS/PREDICTIONS_MONITOR.md` row **L7**
**Outcome: (d) A QUIET LAPSE.** ⚠️ **A quiet lapse is a real finding, not a null** — per NEXUS's own pre-registered disposition it closes M-09's PJM evidence row as evidence AGAINST the power-constraint leg, and the evidence TYPE stays **ARMED at 0pp**. **NEXUS owns that weighing (ARMED→COUNTED); WATT grades the event only.**

---

## The four pre-registered outcomes, each graded at a primary

### (a) An order EXTENDING past 9/8 — **NO. [VERIFIED]**

- **Order's own DOE page** — `https://www.energy.gov/ceser/federal-power-act-section-202c-pjm-interconnection-llc-pjm-order-no-202-26-41` (read 2026-09-10). Effective-period language, quoted: *"The order is in effect beginning on September 1, 2026, and shall expire at 11:59 PM ET on September 8, 2026."* **No extension, amendment or renewal is posted.** The page carries exhibit updates dated 9/2–9/3 — those are **specified-unit lists**, issued while the order was live, **not** duration changes.
- **DOE 2026 202(c) index** — `https://www.energy.gov/ceser/2026-doe-202c-orders` (read 2026-09-10). **202-26-41 is the LAST PJM order of 2026.** The successors go to other entities:
  | order | entity | effective |
  |---|---|---|
  | **202-26-41** | **PJM Interconnection** | **Sep 1–8, 2026** |
  | 202-26-42 | Orlando Utilities Commission | Sep 2 – Nov 30, 2026 |
  | 202-26-43 | Duke Energy Carolinas | Sep 3–8, 2026 |
  - 2026 PJM orders for the record: 02, 06, 17, 23, 24, 25 (+25A), 32, 33, 35, 40, **41**.
- ⚠️ **Scope of this negative:** the index's newest entry is dated **9/3**, so *that page alone* cannot exclude an order issued 9/8–9/10 and not yet posted. **The PJM board and the price tape below carry that leg independently** — and an unposted §202(c) with no EEA and no scarcity pricing behind it is not a state that occurs.

### (b) An EEA-2/EEA-3, voltage reduction or load shed — **NO. [VERIFIED — and the TAPE carries it, not the board]**

- **PJM emergency board** — `https://emergencyprocedures.pjm.com/` (read 2026-09-10): **12 postings, newest #105510 @ 9/9 16:27 EPT.** Every one is a **local Post-Contingency Load-Relief Warning** (FE-ME, EKPC ×4, DOM ×2, FE-AP) or an **Informational Special Notice** (PJM-RTO). **Zero emergency-class.** No EEA of any level, no voltage reduction, no load shed, no Max Generation Emergency/Alert. **No Hot Weather Alert in effect.**
- ⚠️ **The board is a CURRENT view and cannot prove a historical negative.** Proof it drops rows selectively rather than by age: **#105485 (EEA-1, 9/3 00:01) is gone, while OLDER rows #105474 (9/1) and #105478 (9/2) are still listed.** Closed alerts drop; routine warnings persist. So a hypothetical EEA declared and cleared on 9/8–9/9 would also have dropped off. **The board alone is therefore not sufficient, and I am not resting the grade on it.**
- ✅ **The DM2 5-min tape carries the negative, with complete coverage.** One deliberate `rt_unverified_fivemin_lmps` pull, PJM-RTO pnode, 2026-09-04 → 2026-09-10 (1,874 rows):

  | day | prints | max $/MWh | at | mean $/MWh | ≥$500 | ≥$1,000 |
  |---|---:|---:|---|---:|---:|---:|
  | 2026-09-04 | 288 | 149.05 | 11:40 | 44.55 | **0** | **0** |
  | 2026-09-05 | 288 | 157.68 | 11:45 | 43.81 | **0** | **0** |
  | 2026-09-06 | 288 | 87.03 | 18:35 | 24.59 | **0** | **0** |
  | 2026-09-07 | 288 | 220.29 | 18:35 | 28.55 | **0** | **0** |
  | **2026-09-08** *(lapse day)* | 287 | **283.51** | 18:55 | 35.68 | **0** | **0** |
  | **2026-09-09** *(first day after)* | 288 | **457.28** | 17:50 | 63.27 | **0** | **0** |
  | 2026-09-10 *(to 12:05)* | 147 | 223.88 | 12:00 | 44.81 | **0** | **0** |

  **n=288 on every full day = complete coverage** (192 on-peak + off-peak; no short-window artefact — the L-44 coverage guard's failure mode does not apply). **Zero intervals ≥$500 on ANY day.** The highest print in the window, **$457.28 on 9/9**, sits below WATT's own ORANGE band. **Scarcity pricing of that shape is incompatible with an EEA-2, a voltage reduction or a load shed inside the window.**
- **Demand:** 9/10 **112,674 MW = 82.3%** of a 136,896 MW 24h peak [EIA-930] — nowhere near the ≥97% band.

### (c) A large-load direction actually ISSUED under the clause — **UNKNOWN. [SEARCH-NOT-FOUND — this is NOT a negative]**

- No utilisation record is published on the order's DOE page; its 9/2–9/3 exhibit updates are unit lists. Nothing on the PJM board records a backup-generation direction at a large load.
- 🔑 **The exact unchecked document, named so a peer can close this in hours:** the **paragraph-E utilisation report** PJM owes DOE under Order 202-26-41 (the same reporting clause WATT has been waiting on since 9/1 for the deployment question). Until it is read, the standing decomposition is unchanged: **authority ✅ · deployment ❓UNKNOWN · utilisation record ❌.**
- ⚠️ **Do not upgrade this to "no direction was issued."** SEARCH-NOT-FOUND upgrades to VERIFIED only after the owner-declared path AND the documented fallback are checked; the para-E report is the declared path and it has not been published. `[[finding_a_named_unchecked_fallback_makes_an_absence_closable]]`

### (d) A QUIET LAPSE — **THIS IS THE OUTCOME. [VERIFIED]**

The order ran its stated course and expired on schedule with no extension, no escalation, and no published record of the authority ever having been exercised.

---

## Why the quiet lapse is a finding rather than a non-event

**The emergency authority that permitted PJM to direct backup generation at large loads before an EEA-3 — the same policy IRAS limb (c) proposes to convert into a standing commercial term of service — expired without a single published utilisation record.** The gap between *authorised* and *observed*, which WATT has held open since 9/1 and which CODEX forced it to stop over-claiming on 9/6, **did not close. It expired unmeasured.**

Two consequences, kept separate:
1. **For P2/WATT-10 (the tariff question):** unchanged. A lapsed emergency order neither strengthens nor weakens PJM's filed case; the FERC docket `ER26-3515-000` (requested effective **10/12/2026**, service availability **1 June 2027**) is where that resolves.
2. **For the power-constraint leg NEXUS tracks (M-09):** the quiet lapse is the **evidence-against** branch of its own pre-registered rule. **NEXUS decides, not WATT.**

**And it is corroboration — not confirmation — for `WATT-11`** (zero EEA-class postings + zero new §202(c) orders naming PJM, 9/15→11/30, ~80% quiet, PROVISIONAL). ⚠️ **WATT-11's window does not open until 9/15**, so this week is **NOT** a resolved leg of it; recording it as one would be scoring a prediction on data outside its own window.

---

## Instruments and their limits (stated, not smoothed)

| leg | instrument | limit that matters |
|---|---|---|
| (a) | DOE order page + DOE 2026 202(c) index | index newest entry 9/3 ⇒ cannot exclude an unposted 9/8–9/10 order by itself |
| (b) board | PJM emergency-procedures page | **current view**; closed alerts drop while routine warnings persist (#105485 gone, #105474 present) — cannot prove a historical negative |
| (b) tape | PJM Data Miner 2 `rt_unverified_fivemin_lmps` | **unverified** 5-min (operational, not settlement); ~15-day retention — inside it here, and per-day n=288 confirms full coverage |
| (c) | para-E utilisation report | **not published** ⇒ SEARCH-NOT-FOUND, never a verified negative |

**DM2 spend this session: 3 calls** (2 by `boot.py`, 1 deliberate for the per-day table) against the non-member 6/min tier. Spaced, never bursted.
