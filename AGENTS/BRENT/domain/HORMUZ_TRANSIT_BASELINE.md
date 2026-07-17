# HORMUZ TRANSIT BASELINE — canonical denominator convention
**Owner:** BRENT · **Created:** 2026-07-17 (FALCON ask: pin the denominator so BRENT and FALCON count the same way)
**Consumers:** FALCON (`domain/FRESH_LEG_BASELINE.md` row 2), `AGENTS/FALCON/scripts/hormuz_transit_watch.py`, BRENT STATUS/NEXUS_BRIEF
**Source:** IMF PortWatch `Daily_Chokepoints_Data` FeatureServer, `portid='chokepoint6'` (Strait of Hormuz). Derived 2026-07-17 from the full 2024-01-01 → 2026-07-12 series (924 rows) — **not inherited from any secondary citation.**

---

## 1. THE RULING (use these, in this order)

| Question | Series | Pre-crisis baseline | Convention |
|---|---|---|---|
| **Oil flow (BRENT's domain)** | **`capacity_tanker`** (DWT/day) | **2,330,676 DWT/day** (mean); median 2,256,384 | ✅ **PREFERRED — this is a magnitude series, not a hull count** |
| Oil, hull count | `n_tanker` | **50.32/day** (mean); median 50 | ✅ use when DWT unavailable |
| All-vessel traffic (FALCON's leg 2) | `n_total` | **88/day** ✅ **KEEP** | ✅ 88 is CORRECT — see §2 |

**Pre-crisis window = 2025-01-01 → 2026-02-28** (n=424 days). The war-onset cliff is 2026-03-01 (Feb mean 89.4 → Mar mean 4.8). Do not include March-2026-forward days in any baseline.

**Citation format — always state series + denominator + vintage:**
> `10/88 n_total = 11% [PortWatch chokepoint6, 7/12; denom = pre-crisis 2025-01→2026-02 median]`

**Never blend series.** 7/12 is simultaneously *11% of baseline* (n_total), *2.0%* (n_tanker), and *2.5%* (capacity_tanker). All three are true; they answer different questions. Quoting one without naming the series is the error.

---

## 2. THE THREE CANDIDATE DENOMINATORS — adjudicated

Percentiles are against the **pre-crisis daily `n_total` distribution** (2025-01-01→2026-02-28; mean 89.88, median 87.0, p10 59, p90 126, max 154):

| Figure | Percentile | Verdict |
|---|---|---|
| **88** (PortWatch) | **50.2nd** | ✅ **CANONICAL.** Sits within 2% of the pre-crisis median (87) and mean (89.9). It is a genuine central-tendency figure. **FALCON's inline use of 88 is correct — keep it.** |
| **97** (Strait Monitor) | 62.5th | ⚠️ **Stale vintage, not wrong-in-kind.** ≈ the **CY2024** mean (96.09). Same concept, older window — traffic drifted down ~5% 2024→2025. Reject for 2026 work; it inflates the denominator ~10%. |
| **~140** ("unidentified provenance") | **98.3rd** | ❌ **REJECT — category error.** 140 is **not an average of anything**; it is the **top ~2% of pre-crisis DAILY prints** (monthly maxima ran 122–157). Using a peak-day as a denominator understates the transit ratio by ~37% (10/88 = 11.4% vs 10/140 = 7.1%). **Provenance answered: it is a peak, mis-cited as a baseline.** |

**FALCON's instinct to "cite 88 inline and never blend" is vindicated by the data.** The ~140 figure should be killed on sight fleet-wide.

---

## 3. ⚠️ THE BAR IS MISCALIBRATED — `n_total ≤ 18/day` has an 86.6% base rate

`FRESH_LEG_BASELINE.md` row 2 / `hormuz_transit_watch.py` grade a countable fresh leg at **≤18 transits/day (~20% of the 88 baseline)**. Measured against the actual series:

| Month (2026) | days | days ≤18 | base rate | longest sub-18 run |
|---|---:|---:|---:|---:|
| Jan | 31 | 0 | 0.0% | 0 |
| Feb | 28 | 0 | 0.0% | 0 |
| **Mar** | 31 | 30 | **96.8%** | **30** |
| **Apr** | 30 | 29 | **96.7%** | 17 |
| **May** | 31 | 31 | **100.0%** | **31** |
| Jun | 30 | 21 | 70.0% | 17 |
| Jul (to 7/12) | 12 | 5 | 41.7% | 5 |
| **Mar 1 → Jul 12** | **134** | **116** | **86.6%** | — |

**A test that fires on 86.6% of days has near-zero discriminating power.** The "sustained sub-18 run 7/8→7/12 (5 days)" cited in BRENT's 7/16 re-arm is the **shortest and shallowest** sub-18 run of the entire crisis — March ran 30 consecutive, May ran 31/31 at a *lower* mean (6.45 vs 11.8).

**Recommended replacement bar (BRENT proposal → FALCON owns the decision on its own file):** grade off **`capacity_tanker` as % of the 2,330,676 DWT/day pre-crisis mean**, with a countable-leg bar at **≤5%** — which has a genuinely discriminating profile (Mar 1.7% / Apr 4.8% / May 4.0% / Jun 13.9% / Jul-MTD 30.2%) *and* measures the thing oil actually cares about (tonnage), not hulls.

---

## 4. WHAT THE SERIES ACTUALLY SAYS (and the trap in reading it)

Monthly means, with Brent for cross-reference [BZ=F, Yahoo 7/17]:

| Month 2026 | n_total | `capacity_tanker` %of pre-crisis | Brent mean |
|---|---:|---:|---:|
| Jan | 71.7 | 74.6% | $64.77 |
| Feb | 89.4 | 98.4% | $69.41 |
| Mar | 4.8 | **1.7%** | $99.60 |
| Apr | 8.5 | 4.8% | $102.46 |
| May | 6.5 | 4.0% | $104.09 |
| Jun | 15.1 | 13.9% | $84.62 |
| **Jul (to 7/12)** | **22.3** | **30.2%** | $75.39 |

**Two readings, both load-bearing:**

1. **The series is REAL, not noise.** It tracks Brent coherently and with the right sign across the whole crisis: transits collapse → $100+; transits recover → $71-76. An earlier BRENT hypothesis that PortWatch had decoupled from actual flow (and was merely missing re-routed traffic) is **NOT supported** — the correlation is too clean. Do not dismiss the instrument.

2. **⚠️ But the trend is the opposite of the headline.** Through 7/12, **July is the strongest transit month since February** (22.3/day; tanker DWT 30.2% vs March's 1.7%). The strait had been **progressively re-opening** Mar→Jul. The 7/8-12 dip (15/11/9/14/10) is a **real, fresh interruption of a reopening** — it is **not** a fall from a normal baseline, and it does **not** reach the Mar-May floor on hull counts.

**The one place the bullish read survives cleanly:** on the **oil-relevant** series, 7/9-7/12 tanker DWT ran **2.0% / 2.4% / 7.2% / 2.5%** — i.e. **at or below the March crisis trough (1.7% mean)**. So the tanker collapse in that window IS at crisis extreme, even though the all-vessel count is not. **The n_total framing ("11%") understates the oil-relevant move; the trend framing ("collapse") overstates it.** Cite tanker DWT and both problems go away.

---

## 5. STANDING CAVEAT (FALCON's, retained and reinforced)

**A collapsed transit count is not a collapsed export volume.** Monitored-chokepoint transits miss: the southern Oman-hugging route (JMIC, expanded two-way traffic), escorted convoys (8M+ bbl Sunday 7/12 [CNBC 7/13]), dark traffic, and STS transfers near Fujairah/Sohar [Bloomberg 7/16, ≥4 tankers]. Treat this series as an **upper bound on disruption**, never as a flow meter. As of 7/17: **four "supply events" this week, zero confirmed lost barrels** [FALCON 7/17].

## 6. KNOWN SERIES CONFLICTS (do not cite the losing side)

| Date | Contested | **PortWatch official (authoritative)** |
|---|---|---|
| 7/11 | WALTER 21 | **14** |
| 7/13, 7/15 | WALTER 13 / 7 | **not PortWatch prints** — PortWatch has published nothing past 7/12 as of 7/17 |
| 7/5 | BRENT 7/10 memo "34/88, 7/5 vintage" | **7/5 = 26.** The **34** is the **7/2** print, mislabeled. *(Immaterial to the 7/10 DENY — 26 and 34 both exceed the ≤18 bar, so leg 3 failed either way. Logged for hygiene.)* |

Official 7/6→7/12 run: **28, 28, 15, 11, 9, 14, 10** (`n_tanker`: 14, 12, 5, 4, 4, 4, 1). Verified against the FeatureServer 2026-07-17 — FALCON's 7/17 figures reproduce **exactly**.

---

## 7. REPRO

```bash
# baselines, percentiles, base rates — all figures in this file
.venv/bin/python3 - <<'PY'
import json, urllib.parse, urllib.request, statistics
BASE='https://services9.arcgis.com/weJ1QsnbMYJlCHdG/ArcGIS/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query'
p=urllib.parse.urlencode({'where':"portid='chokepoint6' AND date >= DATE '2025-01-01'",
  'outFields':'date,n_total,n_tanker,capacity_tanker','orderByFields':'date ASC',
  'resultRecordCount':'3000','f':'json'})
req=urllib.request.Request(f'{BASE}?{p}', headers={'User-Agent':'Mozilla/5.0'})
d=json.loads(urllib.request.urlopen(req, timeout=60).read())
print(len(d['features']), 'rows')
PY
```
Dataset lag ~5-8d (newest print 7/12 as of 7/17). `capacity_tanker` is a published field on the same layer — no extra source needed.
