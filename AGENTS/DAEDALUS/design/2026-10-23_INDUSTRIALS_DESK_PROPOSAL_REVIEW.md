# DAEDALUS review — WALTER's industrials / manufacturing-cycle desk proposal

**Date:** 2026-10-23 09:26 ET (from `date`) · **By:** DAEDALUS (Claude Code, claude-opus-5-5), at Will's request in-terminal ("help with this proposal I am working on with WALTER")
**Subject:** `AGENTS/WALTER/research/2026-10-23_morning/INDUSTRIALS_DESK_PROPOSAL.md` (untracked; mtime 09:21 ET; read whole, 36 lines)
**Status:** 🟡 REVIEW — no build, no scaffold, no edit to any other desk. Job #1 Build, pre-proposal stage.

## 1. Verdict

The gap is real and a desk is a reasonable answer. Before it goes to PROME, the proposal needs four changes. The first is load-bearing.

| # | Finding | Evidence (path:line, read 10/23) | Fix in the proposal |
|---|---|---|---|
| 1 | **HENRY is missing from the boundary table, and HENRY's charter already claims ISM.** Two desks claim ISM today in two different places; the proposal would make it three. | `AGENTS/HENRY/CLAUDE.md:4` "Owns ISM, PPI, PCE"; `:121` ISM Mfg/Services in its data list; `:147` trigger "ISM Mfg <47 → LABOR, PROME". `AGENTS/WALTER/design/ROUTING_TABLE.md:58` `MACRO_INFLATION` (incl. ISM) action = CARL, backup = HENRY. | Add a HENRY row: it keeps the market-positioning read (equities, vol). The new desk owns the manufacturing-cycle read of ISM/PMI as ONE figure; CARL keeps prices-paid/consumer; LABOR keeps employment. HENRY's `ISM <47` trigger needs a named owner after the move. A change to ownership or routes goes to Will through PROME. |
| 2 | **HANS is listed as "keeps Europe", but its core signal is a lead on US ISM.** That makes HANS an inbound edge to the new desk, not just a neighbour. | `AGENTS/HANS/CLAUDE.md:172–178`: German Mfg PMI leads US ISM ~2 months (r=+0.573, lag approximate). The standing caveat says the PMI drivers are defence, data centres and inventory rebuild, not organic demand. | Add the edge HANS → new desk. Check whether the same caveat applies to the US 57.0 September flash print. It was not checked in this review. |
| 3 | **Scope is a list of data, not a question.** CYPHER and GIBBS were each built around one mechanism. Five data families plus ~9 named companies is the shape that overloaded HAWK (HAW-15, split 7/12). | builds/CYPHER_BUILD_2026-10-22.md (event vs consequence); builds/LARGE_BANK_DESK_PROPOSAL_2026-10-14.md ("one question"). | Name the question, e.g. *"Is the US manufacturing upturn real end-demand, or tariff front-running, AI/defence capex and inventory rebuild, and when does it roll over?"* Name where it transmits in this fleet: C&I lending → REGINALD/GIBBS · earnings/equities → HENRY · hiring → LABOR · power demand → WATT. |
| 4 | **The evidence mixes two failures.** Two missed BOARD signals could be a routing miss (CARL is the action desk on that row and did not act), not only a lack of a desk. | Proposal §gap; ROUTING_TABLE.md:58. | Keep the case on ownership of the cycle question, which a routing fix would not supply. Don't rest it on the two missed prints. The kill-log count is already labelled a keyword count, which is correct. |

## 2. Smaller seam calls the build will need

| Seam | Call needed |
|---|---|
| Eaton · GE Vernova | WATT vs new desk: one figure owner (proposal already flags). GE Aerospace is separate from GE Vernova. |
| Deere | Farm-income side touches FERT/CARL. The new desk owns equipment demand only. |
| Defence / aerospace | HAWK's dormant book lists defence (ROSTER). Decide whether defence-capex orders belong to the new desk. |
| Tariff effect | CARL keeps the announcement (ROUTING_TABLE.md:59). HAWK's dormant book also lists trade. The new desk owns the effect on manufacturers' margins and input costs. |
| Freight | BRENT keeps tankers. Trucking/rail volumes also feed CARL's consumer-goods read. One figure, shared. |

## 3. Data reachability (flag before Will spends prompts)

| Source | Reach | Note |
|---|---|---|
| Industrial production, capacity utilization, durable goods, core capex orders, factory orders | Likely reachable via FRED. The FORGE market-data tool already has a `fred` source (`FORGE/tools/market-data/config.py`). | Not fetch-tested in this review. |
| Regional Fed surveys (Philly, Empire, Richmond, KC, Dallas) | Public releases. | |
| ISM manufacturing | Current release is public. **Historical series is paywalled; ISM data was removed from FRED in 2016.** | ⚠️ A desk cannot back-test ISM thresholds from free data. |
| S&P Global flash/final PMI | Headline press release is public; the full dataset is paid. | Same limit. |
| Cass Freight Index · AAR rail carloads | Public (monthly / weekly). | |
| Class 8 orders (ACT/FTR) | Preliminary press-release headlines only. | |

## 4. Tier and cadence

Prints arrive on a fixed monthly calendar: flash PMI around the 3rd–4th week, ISM on the first business day, regional Feds mid-month, IP mid-month, durables late month. That fits **Tier-2 on demand, woken by dated DOCKET rows** (CRUISE/GIBBS precedent) better than an always-on desk. Recommendation, not a decision.

## 5. Decisions that are Will's (PROME registers them when the proposal reaches it)

1. Name the desk.
2. Tier: recommended Tier-2, calendar-woken.
3. Whether the manufacturing read of ISM moves to the new desk from HENRY/CARL. This is a route/ownership change.
4. The question in finding 3. Will's wording outranks the example.

## 6. What this review did not do

No fetch test of any source. No check of the 57.0 / 55.4 / 55.9 figures against S&P Global. No read of CARL's ISM workbook rows. No grep beyond `AGENTS/*/CLAUDE.md`, ROUTING_TABLE, ROSTER and `_NETWORK.md`.
