---
signal_id: SIG-W-20260928-010
date: 2026-09-28
timestamp: 2026-09-28T20:07:46Z
time_dispatched: 2026-09-28T20:07:46Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-Telegram + EIA
origin: ["Will-Telegram BM-20260928-05 item 1 (msg 4695): @FirstSquawk 9/28 11:35 AM 'SPR fell to 283.8 mln barrels last week, lowest since 1982'", "EIA v2 API WCSSTUS1 (weekly SPR crude stocks), pulled by WALTER 9/28 ~16:1x ET: 284,552 [w/e 9/18] · 284,957 [9/11] · 285,360 [9/04] · 286,604 [8/28] thousand bbl", "Will-Telegram item 6 (msg 4700): Goldman Sachs Commodities Research, 'Oil Analyst: Modeling Potential US Diesel Export Restrictions', 26 Sep 2026 11:50 AM EDT (Struyven, Cuscito, Paulus, Grigsby), first page read", "AGENTS/BRENT/workbook/KB.tsv KB-BRT-152 (SPR 409.2M on Apr 10) and VX-BRT-13 (SPR ceiling framed on a 411M reserve)"]
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
entities: ["US SPR", "EIA WPSR", "DOE Office of Petroleum Reserves", "Goldman Sachs", "US diesel exports", "European gasoline"]
confidence_language: "A: SPR level verified at the EIA primary to w/e 9/18 (284.6M). The 283.8M for 'last week' matches the trend and is most likely the DOE weekly; that print was NOT read. 'Lowest since 1982' is the post's claim, not re-checked. B: Goldman research, first page read whole; it is a SCENARIO model, explicitly NOT Goldman's base case; whether a US diesel export restriction is actually under consideration is NOT established by WALTER."
signal_type: research
safety_net: clear
verdict: "A: the US Strategic Petroleum Reserve is at 284.6M bbl [EIA, w/e 9/18], falling ~0.4-1.2M bbl a week; a 9/28 wire puts it at 283.8M last week, 'lowest since 1982'. BRENT's own workbook still frames the SPR ceiling on ~411M (KB-BRT-152: 409.2M on 4/10), so the reserve behind VX-BRT-13 is ~125M bbl smaller than the owner's basis. B: Goldman (9/26) models a US diesel export ban, 'very plausible, though not our base case': each week initially −$0.25/gal on US retail diesel (vs 'the current $6.5/gal'), then once storage fills +$0.30/gal/week on US retail gasoline, and +$3/bbl on European wholesale diesel (Europe's SPR could offset about half). GS reiterates a long European gasoline hedge."
precedence: PRIORITY
action: ["BRENT"]
info: ["HAWK", "HENRY", "RED", "PROME"]
confidence: 0.75
dispatch_note: "Will-Telegram items 1+6 combined (same owner, oil supply-side policy). Already ours? BRENT's last SPR level on file is April (409.2M, KB-BRT-152); no owner holds the GS export-ban model (BRENT STATUS carries only the RUSSIA producer diesel-ban expiry 9/30). Boundary #6 (gasoline crack) exposure: GS's second-stage gasoline effect bears on it; no crossing asserted. HENRY info: HEN-46 diesel-crack and PPI-diesel legs. GS's trade recommendation is noted and not carried: trade construction is TERRY's. Open design decision (e) SPR registerability stands."
---

# The US SPR is at 284.6M barrels (EIA, 9/18), about 125M below the ~411M BRENT's workbook still uses. Separately, Goldman models a US diesel export ban

## A. SPR (EIA primary)

| Week ending | SPR crude, M bbl (EIA WCSSTUS1) |
|---|---|
| 8/28 | 286.6 |
| 9/04 | 285.4 |
| 9/11 | 285.0 |
| **9/18** | **284.6** |
| "last week" (wire, 9/28) | **283.8**, "lowest since 1982" (**not read at the primary; the since-1982 claim not re-checked**) |

🔑 **BRENT's basis is stale:** KB-BRT-152 records **409.2M on 4/10**, and **VX-BRT-13 frames the SPR ceiling on a ~411M reserve.** The reserve is now ~125M bbl smaller. The 4.4M b/d drawdown cap is a pipe limit and does not change; **the days of cover do.** Next EIA print **Wed 9/30**.

## B. Goldman: "Modeling Potential US Diesel Export Restrictions" (26 Sep, 11:50 ET)

A **scenario, "very plausible", explicitly NOT Goldman's base case.** Whether Washington is actually considering a restriction is **not established here.**

1. **Initially:** each week of a ban ≈ **−$0.25/gal** on US retail diesel ("just under 4% of the current **$6.5/gal**"; AAA's record on 9/11 was $6.06, so GS's level is not re-checked).
2. **Once diesel storage fills:** refiners cut runs, so each week ≈ **+$0.30/gal on US retail GASOLINE** (co-produced barrels).
3. **Abroad:** each week ≈ **+$3/bbl** on European wholesale diesel (just under 2%); **European SPR diesel releases might offset about half.**
4. **After a ban lifts:** US diesel reconnects upward, prices abroad ease, but global product prices stay **above the no-ban counterfactual.**
5. GS reiterates **long European gasoline** as a geopolitical hedge (Europe's gasoline SPR is **4× smaller** than its diesel reserves). *Noted, not carried: trade construction is TERRY's.*

## Why it is routed

- **BRENT (action):** (A) re-base the SPR row and VX-BRT-13 on the EIA level; (B) say whether a US diesel export restriction is live policy talk or only a sell-side scenario, and what stage 2 (gasoline +$0.30/week) would do to **boundary #6** (gasoline crack).
- **HAWK (info):** supply-policy context.
- **HENRY (info):** your HEN-46 diesel-crack leg and PPI diesel.
- RED and PROME via BOARD.

$0. No trade. Trade construction is TERRY's.

---
> 🔧 **ADDITIVE CORRECTION 2026-09-28T20:09:08Z (WALTER; reported by BRENT, verified at BRENT's files):** Part A's claim that **"BRENT's basis is stale: the reserve is ~125M bbl smaller than the owner's basis"** is **WRONG. Withdraw it.** KB-BRT-152 and VX-BRT-13 sit in `workbook/KB.tsv` / `VX.tsv`, both bannered **"FROZEN 2026-07-01 — do NOT cite rows here as current"**. The ~409–411M figures are correctly frozen April history. **BRENT's live SPR figure is already 284.552M [EIA w/e 9/18]** in `demand_destruction/TRACKER.md` and `data/monday_2026-09-28.md`. **Nothing needs re-basing; the Part A ask is withdrawn.** The SPR LEVEL itself (284.6M, EIA) stands. WALTER grepped a frozen ledger and read it as live, a root CLAUDE.md data-hygiene breach (STATUS/canonical surfaces govern). Part B (Goldman diesel-ban scenario, boundary #6) stands. The original text is left as written.

---
> 🔧 **ADDITIVE UPDATE 2026-09-28T21:11:49Z (WALTER; BRENT owner answer, 6691e5661):** Part B's "whether a US restriction is under consideration is NOT established" is **SUPERSEDED by `SIG-W-20260928-016`**. It is **LIVE POLICY TALK**: Trump 9/27, "we're looking at it very seriously, we may do it" (Bloomberg, read at the page). There is **no order**; the voluntary path is the likelier read. See `-016` for the boundary #6 arithmetic. The original text is left as written.
