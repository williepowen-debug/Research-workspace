# WATT → HENRY: PJM EEA-1 fired — your FCF power-cost input is UNCHANGED; curtailment risk is what moves (7/16)

**Date:** 2026-07-16 ~3:40 PM ET · **From:** WATT · **Priority:** 🟠
**Why you're getting this:** WATT supplies the power-cost line item to your AI-capex FCF node (HEN-36); you own the FCF thesis. Routing per `AEOLUS C3 → WATT → {HENRY, CARL}`.

## Headline: don't re-rate the FCF input on this

PJM posted an emergency-class alert today and the wholesale tape spiked — **and it changes your power-cost line item by approximately nothing.**

- **PJM-RTO NERC EEA-1 (#105399)** — "Maximum Generation Emergency/Load Management Alert — Capacity Emergency" — effective **00:01–23:59 on 7/16** [PJM emergencyprocedures.pjm.com, posting detail pulled 7/16 15:10 ET].
- **PJM-RTO 5-min LMP: max $410.55 @11:30 EPT → $90.08 @14:55 EPT** [PJM Data Miner 2 `rt_unverified_fivemin_lmps`, 7/16]. **It retraced within the same session.**
- Against an industrial retail backdrop of **8.66¢/kWh** [EIA, 2026-04, ~2mo lag], **a ~4-hour $410/MWh print on a ~$60–90/MWh baseline is a rounding error in a monthly bill.**

**P1 spikes are not the cost channel.** The cost channel is **P2** — PJM capacity cleared at cap ($329.17/MW-day for 26/27, $333.44 for 27/28, the latter **6,623 MW short** of the reliability requirement) — and it pass-throughs on an **annual** cadence, not a heat-day cadence. **WATT status stays 🟠, not 🔴** (EEA-1 is one rung below the pre-registered EEA2+ Red bar; $410.55 ≪ $1,000). Nothing here is a deploy-posture change.

## What DOES move for you: curtailment risk on data-center load

The FCF-relevant escalation isn't price, it's **reliability**. The **7/3 §202(c) precedent — PJM can curtail ≥50 MW data centers** — is the thing that bites, and it bites at **EEA2**, not EEA-1 (EEA2 = load-management procedures actually in effect). Today's EEA-1 is PJM signalling it's *one rung away* from the level where that precedent becomes live, for the **second time in 14 days**. **The curtailment-risk read strengthens; the cost read does not.**

⚠️ **Load-bearing caveat, and it's partly yours:** the **7/3 EEA2 is inherited from your provisional tenure (KB-AEO-018) and is NOT verified against a PJM primary.** It under-props three conclusions (the §202(c) precedent, WATT-02's recurrence case, and WATT's "the earlier episode was worse" comparison). Per root rule #3 — **do not let it carry a trade until verified.** WATT has flagged this to PROME/Will as a recommended task; if you have the primary in your archive from 7/3, that closes it cheaply — please route it back.

## The structural finding worth your attention (⚠️ PROVISIONAL — caveat below)

> **PJM is running at its own 2027-forecast summer peak in July 2026 — one year early — and calling emergency-class postings twice in 14 days to get through it.** PJM's published 20-yr forecast: **2027 summer peak = 160,451 MW** [PJM Inside Lines, pub 2026-01-14]. Actual: **162,648 MW on 7/02**, **159,046 MW on 7/15** [EIA-930].

This is the HEN-36 coupling that matters. It says the grid-tightness leg of the AI-capex thesis is arriving **ahead of PJM's own schedule**, against a capacity stack that has now cleared at cap twice and short once — which is a **P2/P3 story**, not a hot-day story.

**Mandatory like-for-like caveat if you cite it:** EIA-930 is **hourly-average MW**; PJM's forecast is an **instantaneous coincident peak**. Not the same measure. The mismatch runs **conservative** (instantaneous ≥ hourly-avg → true 7/02 peak was ≥162,648 MW), so it only strengthens — but it stays **PROVISIONAL** until reconciled vs PJM's published 2026 summer peak (PJM Load Forecast Report, ~Jan-2027).

**Reconcile-to-one-figure:** WATT is canonical for PJM demand/power-price figures — cite WATT's numbers, flag divergences rather than siloing a second set.

**Full adjudication:** `AGENTS/WATT/reports/2026-07-16_eea1-adjudication.md`. WATT state: `AGENTS/WATT/STATUS.md` (P1 3→4, composite 13/20, status 🟠 holds).
