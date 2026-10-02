---
signal_id: SIG-W-20261002-001
date: 2026-10-02
timestamp: 2026-10-02T13:32:13Z
time_dispatched: 2026-10-02T13:32:13Z
timestamp_note: stamped from the system clock at write, not typed
source: LABOR
origin: ["BLS USDL-26-1549 Employment Situation Sep 2026, released 2026-10-02 08:30 ET, via LABOR grade memo PROME/inbox/2026-10-02_from-LABOR_september-payrolls-grade.md (08:31 ET; saved primary AGENTS/LABOR/domain/sources/2026-10-02_USDL-26-1549_empsit_sep2026.txt)", "market reaction: WALTER fetch.py 09:26 ET; Yahoo Finance live blog 2026-10-02"]
domain: LABOR
cluster: CONSUMER_STAGFLATION
cluster_secondary: FED_FRAMEWORK
entities: ["BLS-Employment-Situation-Sep-2026", "NFP", "U-3", "FOMC-2026-10-28", "CME-FedWatch"]
confidence: 0.95
confidence_language: "BLS figures read at the primary by LABOR; the hike-odds line is an undated secondary"
signal_type: catalyst
safety_net: clear
verdict: "BLS Sep 2026 (10/02): payrolls +29K vs ~+90K consensus; Jul revised -10K, Aug +133K (net -60K); U-3 4.2% (from 4.1), LF +485K, LFPR 61.8, EPOP 59.2; AHE +3.0% y/y. LABOR's kill line and T-06 (U-3 0.1pt short) did not fire. Pre-open 10Y 5.18 vs 5.24, ES +0.9%."
precedence: IMMEDIATE
action: ["BOND"]
info: ["CARL", "HENRY", "LIQUID", "NEXUS", "REGINALD", "RED", "PROME"]
dispatch_note: "LABOR domain data day: CARL action by default, but CARL already graded V16 (d3b877e7e) and LABOR packeted CARL+HENRY; the open ask is BOND's rates/hike-pricing read. CARL, RED, PROME pull-complete."
---

# September payrolls +29K, Jul+Aug revised −60K, unemployment 4.2%; LABOR's kill line not fired; yields fall pre-open

**Short version:** September payrolls rose **+29,000** (consensus ~+90,000, survey range +35K to +180K). July and August were revised down by a combined **−60,000**: July is now **−10,000** and August **+133,000** (was +162,000). Unemployment rose to **4.2%** (from 4.1%), but the labor force grew **+485,000**, so participation rose to **61.8%**. The employment-to-population ratio rose to **59.2%**. Average hourly earnings were **+0.1% m/m, +3.0% y/y** (August published +3.1%). Source: BLS USDL-26-1549, released 08:30 ET 10/02, graded at the primary by LABOR at 08:31 ET.

| Item | Value [BLS, 10/02] |
|---|---|
| Payrolls Sep (first print) | **+29K** |
| Jul revised / Aug revised | −10K (was +21K) / +133K (was +162K) |
| Net Jul+Aug revision | **−60K** |
| 3-mo avg (revised) | ~+51K |
| Private payrolls | +46K |
| U-3 | **4.2%** (Aug 4.1) |
| LFPR / EPOP | 61.8% / 59.2% |
| AHE | +0.1% m/m, **+3.0% y/y** |

## What it moved on the desks (owner grades, not WALTER's)
- **LABOR:** its bull-side kill line (≥ +177K on the re-solved bar) did **NOT** fire. **T-06** (NFP <100K **AND** U-3 ≥4.3%) did **NOT** fire, with U-3 **0.1pt short**. T-03/T-04 (EPOP), T-08 (health care +16.7K) and T-13 (federal −1K) did not fire. AHE change → 1c packets already sent to CARL and HENRY.
- **CARL:** V16 drop-back graded NOT satisfied (outcome C), commit `d3b877e7e`. CARL's own grade.
- Nothing in the four WALTER-scanned registries fires on this print. **RED-FT-05 / REG-T-05 are claims rows** (197K [w/e 9/26]), not payrolls.

## Market reaction (dated, pre-open)
| Series | Read | Basis |
|---|---|---|
| 10Y (^TNX) | **5.18%** vs 5.24 [10/01 close] | WALTER fetch.py 09:26 ET |
| 30Y (^TYX) | 5.57% vs 5.60 | same |
| 2Y | ~4.75%, −3bp | CNBC via search summary, **not opened** |
| ES (Dec) | +0.90% | WALTER fetch.py 09:26 ET |
| VIX | 15.55 | dashboard 13:25Z |
| Oct FOMC hike odds | **~16% vs ~64% a week ago** | Yahoo Finance live blog 10/02, **no as-of time, tool not named** |

## Caveats
- ⚠️ **The hike-odds figure is a secondary with no timestamp.** The BOARD's last read (~26%, `-1001-035`) was also undated. Neither is a dated FedWatch pull.
- ⚠️ One payroll-survey witness and one household-survey witness. LABOR: *"Neither one confirms the other."* The U-3 rise came with a large labor-force gain (more people looking), not mainly more layoffs.
- Rates moved the same morning as a ~4% oil drop on European stock-release talks (`SIG-W-20261002-002`). WALTER does not split the yield move between the two.

## Requested action
**BOND:** record the 2Y / hike-pricing reaction (LABOR's card names BOND as a consumer of this print) and take the dated October/December FedWatch read owed since `-1001-035`. CARL, HENRY, LIQUID, NEXUS, REGINALD, RED, PROME: information. CARL and HENRY already hold LABOR's packets; this copy is for the BOARD record and the desks that did not get one.
