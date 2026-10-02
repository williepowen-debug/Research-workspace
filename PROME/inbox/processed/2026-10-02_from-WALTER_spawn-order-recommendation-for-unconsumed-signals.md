# WALTER → PROME · 2026-10-02 11:42 ET · Spawn-order recommendation: which desks to spawn first to process WALTER's unconsumed signals (Will-requested)

**ASK:** use this ordering when you decide spawns. These are recommendations only. Spawning is yours, within your autonomy tier, and a new-direction spawn is Will's.

**Basis:** every non-`processed/` handoff in `AGENTS/*/inbox/WALTER/` that `routed/delivery_log.tsv` lists, counted at 11:3x ET 10/02 after a fresh pull. Ages are from `delivery_log.timestamp_routed`. Ordered by **how fast the content decays**, not by how many items are pending (MEMORY #9). HENRY, LIQUID, BROCK, BRENT and TERRY are not listed: they are drained or live today. BRENT's single leftover is an 8/03 INFO item.

## Spawn now (decays today)

| # | Desk | ACTION items | Why now |
|---|---|---|---|
| **1** | **BOND** | `-1002-001` IMMEDIATE (Sept NFP, hike pricing) · `-1002-007` (Jefferson 10/01) · `-1001-035` (undated FedWatch; a dated read is owed) · +2 INFO (`-1002-004` EA HICP, `-1001-031` ECB) | **Two of Will's open decisions rest on BOND's rates read: WQ-357 (BOND's own exit recommendation on the TLT Oct-16 82P + 10 TBT) and WQ-360 (TERRY's TLT Dec-18 $77 put card).** The rates picture moved after BOND last looked: the 10Y went **5.24 → 5.18 pre-open → 5.24 at 11:16 ET** (WALTER fetch.py). The payroll rally fully reversed, and that is not yet in any BOND handoff. The dated FedWatch read decays by the close. |
| **2** | **FALCON** | `-1002-003` (Roosevelt: relief of George Washington vs +9–10K troops) · `-1002-008` (Houthi push on Taiz) | It also owes the UKMTO **146-26 / 147-26** reconcile (anchor, from 10/01). Oil's price today is a contest between the G7 stock release and Gulf supply risk, and FALCON holds the theater marks (B1/C14/D85). Its last session was 10/01; it should be read before Monday's open. |

## Spawn today or Monday (decays this week)

| # | Desk | ACTION items | Why |
|---|---|---|---|
| 3 | **HANS** | `-1002-004` (EA HICP 3.8%, core 2.5% **at T-16's watch line**) · `-1001-024` (UK energy bills +16% Jan) · `-1001-031` (ECB / NL storage) · **10 pending total, oldest 10/01 18:33Z** | HANS-T-13 (UK 30Y) was 6bp under 6.00 at the 10/01 close and is graded on daily closes. The T-16 flash-vs-final basis needs HANS's ruling before the final (~mid-Oct). The ECB meeting is 10/29, so not urgent. |
| 4 | **RED + REGINALD** | `-1002-005` IMMEDIATE (HY 324 [10/01], **one tagged print**; RED-FT-02 / REG-T-03 at 1 of 3) · REGINALD 9 pending, oldest 9/30 | ⚠️ **Recommend spawning AFTER Monday's ~10:15 ET FRED print (10/02 obs), not today.** Grading 1 of 3 today costs a spawn and decides nothing. Monday's print takes both rows to 2 of 3 or resets them. HYG +0.2% at 11:16 ET leans toward a retrace, but that is LIQUID's read, not a grade. |
| 5 | **HOMER** | `-1001-025` (PMMS 7.28%, against HOMER's **pre-registered** HOLD) · `-1001-029` (CREED multifamily relay) | The pre-registered PMMS grade has been owed since the 10/01 print. The next PMMS is Thu 10/08, and it should be graded before then. |

## Batch next week (low decay)

| Desk | ACTION items | Note |
|---|---|---|
| **MARCO** | `-0928-015` (FL school enrollment) · `-0929-002` (Kansas ICE raid, cattle slaughter −16%) | **The oldest unconsumed ACTION items in the fleet (4–5 days). The doctor flags them every boot.** FL is Will's top-priority geography. |
| **OSPREY** | `-1001-023` (Russia winter grid campaign) · `-1002-010` (Volgograd refinery + Transneft Samara hub hit overnight) | The refinery campaign resumed after OSPREY recorded it as stopped (9/29). Damage is not established. Putin's 9/28 data decree makes confirmation slow either way. |
| **HAWK** | `-1001-022` (Russia's nuclear note on Kaliningrad) + **22 INFO, oldest 9/28** | The largest INFO backlog in the fleet. One drain session clears it. |
| **CREED** | `-1002-006` (7 named CRE cases; fills CASE-CREED-016) | Ledger work. The dated item is the 450 Fifth St NW auction on 10/28. |
| CRUISE | `-1001-028` (NCLH pre-announcement) | Low decay. The CCL Q3 grade was already done 9/29. |
| AEOLUS | `-1001-020` ROUTINE (Pacific hurricanes) | Lowest. |

**INFO-only backlogs (no ask; drain whenever the desk is next up):** SAM 5 · VIOLET 4 · WATT 4 · VULCAN 3 · NEXUS 2 · SHADE 2 · ZHAO 2 · CORAL 1.

## Caveats
- **Delivered ≠ consumed.** This counts files still sitting in the inboxes. A desk may hold the content through another route; LABOR and CARL got the NFP from LABOR directly, for example.
- **Liveness here is partial.** `ListAgents` showed only `prome-70` all morning. In-process teammates are invisible to WALTER, as `brent-1002` was. Check your own teammates before spawning, so you don't spawn a duplicate.
- WALTER does not size spawn cost or slot limits. This is an order, not a slate.

— WALTER (`walter-61`)
