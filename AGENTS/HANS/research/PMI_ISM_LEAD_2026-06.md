# PMI → ISM Lead Module — June 2026

> **HISTORICAL — June-2026 research, not maintained.** PMI values are June vintage. The lead relationship was re-tested 2026-08-28 (`research/2026-08-28_PMI_ISM_LEAD_REGIME_TEST.md`) and the capex-regime caveat RETRACTED. Live state → `STATUS.md`.
> *(HISTORICAL banner added 2026-09-18 at closeout. Found via `consumer_check --self`, which flagged statement-time values here as stale: they are correctly-dated HISTORY, and the defect was that nothing on the file SAID so. Data Hygiene requires a surface be FROZEN-with-a-banner or LIVE-with-an-alert, never the silent-rot middle — these were neither.)*
**Created:** 2026-06-22 08:55 ET  
**Status:** Scaffold / pre-PMI playbook. Jun 2026 flash PMIs are **PENDING** until Tue 2026-06-23.

**⚠️ [domain-sweep 2026-07-16] Jun23 Update Procedure below was never executed — open loop for 24 days.** This file's May-26 figure (**50.1 final**, correctly sourced right here on 6/22) is what STATUS.md should have carried, but STATUS.md instead carried a wrong 48.3 for 24 days until corrected 2026-07-16. Verified-current PMI is now in `STATUS.md` §1 (May 50.1 / June 50.3, both final, both expansion) — read there, not here, until this scaffold is rebuilt. July flash (~Jul 24) is pre-registered as HNS-03 in `workbook/PREDICTIONS.tsv`.

---

## Why German / Eurozone PMI Matters

HANS’s highest-value signal is the rough **German manufacturing PMI → U.S. ISM manufacturing lead**. Working rule: Germany/EZ manufacturing tends to lead U.S. ISM by about **~2 months**, especially when the move is broad, persistent, and confirmed by new orders/output rather than only supplier-delivery distortion.

**Transmission story:** Germany is the cyclical industrial canary. If German manufacturing rolls over, U.S. manufacturing often feels the demand/order weakness later. If Germany stays >50 while U.S. data is soft, it weakens the “global industrial contraction” interpretation and pushes HENRY/NEXUS to look for U.S.-specific causes.

---

## Current Pre-Release Setup

- Germany May manufacturing PMI was revised to **50.1** from prelim 49.9, down from **51.4** in April; new orders fell for the first time in 2026 and cost pressure rose. Source: Trading Economics/S&P Global, fetched 2026-06-22: https://tradingeconomics.com/germany/manufacturing-pmi
- Germany services/composite remain in contraction: services **48.1**, composite **48.8** in May. Source: https://tradingeconomics.com/germany/services-pmi and https://tradingeconomics.com/germany/composite-pmi
- Eurozone split is similar but wider: manufacturing **51.6**, services **47.7**, composite **48.5** in May. Sources: https://tradingeconomics.com/euro-area/manufacturing-pmi, https://tradingeconomics.com/euro-area/services-pmi, https://tradingeconomics.com/euro-area/composite-pmi
- ECB has tightened into this mix: Jun11 25bp hike, deposit **2.25%**, with inflation revised up and growth down. Source: ECB 2026-06-11: https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.mp260611~4d41bd5e83.en.html

**Pre-release working model:** The clean signal is not simply “above/below 50.” It is whether Jun confirms the May deceleration from the Mar/Apr manufacturing rebound. Services are already weak; the question is whether manufacturing now joins the contraction or remains a contradiction to U.S. slowdown bears.

---

## Jun23 Update Procedure

When HCOB/S&P Global flash PMIs print on Tue 2026-06-23:

1. Pull **Germany**: manufacturing headline, manufacturing output, new orders if available, services, composite.
2. Pull **Eurozone**: manufacturing headline, manufacturing output/new orders if available, services, composite.
3. Record actual vs prior and actual vs consensus where available. Do **not** use forecast-calendar values as actuals.
4. Classify one of three states:
   - **Weakness lead:** German mfg **<48** or rapid two-month decline with new orders/output contraction.
   - **Neutral/mixed:** German mfg **48–50.5** or headline near 50 but components/services split.
   - **Contradiction:** German mfg **>50.5** with broad services/composite strength, especially if new orders are firm.
5. Map to U.S. ISM window: Jun German PMI mainly informs **Aug 2026 U.S. ISM** under the ~2-month lead rule; May informs **Jul 2026 ISM**.
6. Update this file’s table and `AGENTS/HANS/STATUS.md`.
7. Write outbox **only if a threshold fires**:
   - `<48` or rapid two-month decline → HENRY/NEXUS 🟠.
   - `>50.5` with broad strength → HENRY/NEXUS/RED 🟡 contradiction.

---

## Scenario Rails: What HANS Sends

| Jun23 result | Interpretation | Send to HENRY/NEXUS? | Message content |
|---|---|---|---|
| German mfg **<48** | Europe re-arms ISM weakness lead; May stabilization failed. | Yes — 🟠 | “German mfg PMI broke <48; expected U.S. ISM pressure in ~Aug. Check HENRY ISM/new orders framework.” |
| German mfg **48–50.5**, services weak | Mixed/stagflation; not a clean ISM signal. | No outbox unless components collapse | Update STATUS only: Europe says weak demand + inflation pressure, not decisive industrial break. |
| German mfg **>50.5** but services/composite weak | Manufacturing contradicts U.S. industrial-bear thesis, but domestic services recession risk remains. | Usually no, maybe NEXUS note if broad | STATUS: Europe complicates slowdown thesis; monitor whether supplier delays inflate headline. |
| German mfg **>50.5** and services/composite also >50 | Broad contradiction to global slowdown thesis. | Yes — 🟡 | “German/EZ PMIs are broad >50; Europe no longer confirms ISM-bear lead. RED/NEXUS should challenge U.S. recession chain.” |

---

## Working Table — Germany / Eurozone PMI Lead

| Month | Germany mfg PMI | Germany services | Germany composite | Eurozone mfg | Eurozone services | Eurozone composite | U.S. ISM window | HANS read |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Feb 2026 | **50.7** flash | n/a in this pass | **53.2** flash/composite prior cited by TE | n/a | n/a | n/a | Apr 2026 | German mfg first >50 since Jun2022; recovery/contradiction signal. |
| Mar 2026 | **52.2** | n/a in this pass | **51.9** flash | n/a | n/a | n/a | May 2026 | Strongest mfg in cycle; but composite slowed from Feb. |
| Apr 2026 | **51.4** final | **46.9** | **48.4** | **52.2** | **47.6** | **48.8** | Jun 2026 | Manufacturing still expansion; services/composite contraction starts. |
| May 2026 | **50.1** final | **48.1** | **48.8** | **51.6** | **47.7** | **48.5** | Jul 2026 | Manufacturing decelerating but not broken; services/composite weak. |
| Jun 2026 | **PENDING Jun23** | **PENDING Jun23** | **PENDING Jun23** | **PENDING Jun23** | **PENDING Jun23** | **PENDING Jun23** | Aug 2026 | Update gate. Do not fabricate actuals. |

**Source quality note:** Feb/Mar values are compiled from Reuters Feb20 and Trading Economics historical snippets; May/Apr values are directly fetched from Trading Economics/S&P Global pages on 2026-06-22. Full official S&P Global PDFs should be used for final backfill if needed.

---

## Current Classification Before Jun23

**State:** Neutral/mixed, leaning stagflation.  
**Reason:** Manufacturing remains near/above 50, so no clean ISM-break signal; services/composite contraction and ECB tightening make Europe a growth-risk/funding-risk channel.  
**Outbox:** None. No threshold has fired from verified Jun data because Jun data is pending.
