# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-07-25 ET (session 18 + **18b correction pass**. Boot + sitrep → calibration catch → VX refresh → full closeout → **then the stale-vector sweep falsified the day's headline finding and forced a same-session retraction.** Thesis v2.6 → v2.7 → **v2.8**.)

## CHANGES SINCE (session 17 → 18)
16 days elapsed (7/9 → 7/25). What moved while offline:
- **June CPI (7/15)** — the ES-MARCO-08 print. **Gasoline −9.68% MoM, all-energy −5.7% MoM** (largest since Apr 2020): the 7/9 fear that the energy re-arm would close the pump-relief window was **wrong** — the window held wide open. Fresh F&V +5.71% YoY (from +6.74%), −1.05% MoM.
- **FL Realtors June (7/17, via CORAL 7/21)** — condo **8.1mo**, median $305K **+1.7% YoY (first positive)**, sales +14%.
- **StatCan June (7/13)** — 1.7M return trips +3.2% YoY (3rd consecutive); 2-yr stack −28.7%; **air stack −25.0%, up from −28.4%**.
- **Trump 50% Section 338 tariff on broad Canadian goods (7/20)** — fresh boycott-sentiment re-escalation (WALTER SIG-W-20260720-002).
- **BLS LAUS June (7/21, via CORAL + PROME)** — FL **added** L&H jobs; FL UR 4.7%, first decline since 2024; Orlando TDT record.
- **CORAL corrections (7/21)** — Citizens PIF 278,246 (not ~385K); rate cut effective 7/1 (not 6/1).
- **CORAL ATTOM packet (7/17)** — FL #1 foreclosure state; Punta Gorda #1 US, Cape Coral, Lakeland #2 — inside MARCO's SW-FL geography.
- **NOAA (7/25)** — 81% probability of a **very strong El Niño Oct-Dec 2026**, into early spring 2027 — the exact winter the FL snowbird $ hole is dated to.
- Energy re-arm from 7/9 **faded** — Brent never approached the $85 threshold MARCO set.

## WHAT I DID (session 18)
1. **Boot** — STATUS/SCRATCH/MEMORY read; boot.py full run (Banxico + slaughter fetchers refreshed); FL migration proxies checked.
2. **Sitrep delivered — and it contained a bad claim.** I wrote *"every FL metric I own is improving, while CORAL's read hot"* and built a framing on it. **Will challenged it. It was false.** Three FL metrics improved; migration level, voter-net, Canadian air stack, capacity, MIA pax, hospitality wages and household insurance cost were breached/negative/unrefreshed. I had built the FL table out of CORAL's inbound packet without opening `VX.tsv`, while the boot sweep had already printed `42/57 vectors >60d stale` and I'd filed that as housekeeping.
3. **Logged the lesson (two tiers).** New auto-memory `finding_prose_claims_escape_test_rigor` (+ index line) — *you verify what's shaped like a TEST and free-ride on what's shaped like a SENTENCE; a universal quantifier over your own metrics is a ledger claim; stale rows are UNKNOWN, not absent; and a **self-deprecating** wrong claim deflects scrutiny that a confident one would attract.* MARCO-specific instance → local `MEMORY.md`.
4. **VX refresh — 7 FL/tourism vectors re-pulled live.** Two of MARCO's own vectors were wrong in **opposite** directions:
   - **FL-01 hospitality wages REVERSED** — FL $23.99 vs US $23.62 (**above** national), +8.75% vs +3.87% YoY, 3 straight months. Carried row said 11% *below* at $20.74. CRITICAL → NORMAL; "DEMAND WEAKNESS" label falsified.
   - **3.01 household insurance cost STALE-FLAGGED, no figure adopted** — aggregators span $3,815–$8,458; "4.5x national" doesn't reproduce. Level breached, momentum broken (+18% 2025 → ~+2% 2026E). Needs FL OIR primary.
   - Also: 1.01 Canadian (June), 1.04 airports (FLL/MIA), FL-02 condo 8.1mo, SFE-03 Citizens PIF, 3.03 migration proxies.
   - **Note:** first VX write attempt used a csv round-trip that silently re-quoted 7 rows I hadn't touched. Reverted and redid it line-scoped — exactly 7 lines changed, 58 rows / 14 cols verified.
5. **ES-MARCO-08 resolved — against my own thesis leg.** Pulled the BLS public API directly (not the search snippet), caught that the carried "+6.1% fresh F&V" was the `SAF113` aggregate not `SAF1131`, and reported the freight branch.
6. **Attribution check saved a false confirmation.** FLL May −10.7% / intl −27.5% looked like FL tourism collapsing. It's the **Spirit liquidation** (31.4% FLL share, ceased 5/2), and **JetBlue backfilled +75% departures** — supply shock, substantially absorbed, weak evidence *against* demand collapse. Logged as an explicit non-finding.
7. **Full closeout:** thesis **v2.7** + CHANGELOG; STATUS rewritten (header cruft pruned, s13 + 5/31 blocks archived → 237 lines, under cap); ES-01 → DID_NOT_APPEAR, ES-05 → RECEDING, ES-08 → Resolved/moved; MAR-14 74→45 (and a 74-vs-55 STATUS/TSV drift reconciled), MAR-12 60→35, MAR-24 45→60 (caveated), MAR-22 hold; 4 KB rows; docket pruned + 7 forward rows; CALENDAR July block resolved; packets to LABOR/CARL/CORAL; NEXUS_BRIEF v2.7.

## WHAT I DID (session 18b — the correction pass)
Will asked to address the 38 stale vectors (I'd said ~35; boot.py counts 42 on a different basis — reconcile that in the guard build).

9. **Triaged the stale list by STATUS, not age** (my own rule from this session): **25 BREACHED/CRITICAL, 10 ELEVATED, 2 other, 1 pending** — of 38 >60d, out of 57 total.
10. **Discovered `VX-2.05` (Ag Wage Growth) and `2.06` (Construction Wage Differential, High-Immigrant) already existed at 184d stale** — the "wage panel to build next session" was partly a panel MARCO abandoned in January. Refreshing them ran the v2.7 confirmation test immediately.
11. **🔴 THE PANEL FALSIFIED THE INSTRUMENT I PROMOTED HOURS EARLIER.** Jun'26 YoY gap vs national (pp): **FL L&H +4.88 · TX −6.45 (−2.58% YoY, falling) · CA −1.94 · AZ −1.05**; construction FL +1.02 · TX −3.22 · CA +3.96 · AZ −0.36. Two of eight cells positive. **TX — largest immigrant workforce exposure, most aggressive enforcement, no state minimum above $7.25 since 2009 — has hospitality wages FALLING.** FL's cell is **Amendment 2**: $13 (Sep'24) → **$14 (Sep 30 2025)** → $15 (Sep 30 2026) = a **7.7% statutory floor increase inside the June YoY window**, in the most floor-exposed sector. Verified the schedule before accepting the alternative explanation.
12. **Same-day retractions** (before they could propagate): 🔴 **LABOR** full (it had been asked to re-anchor U-3 on this), 🔴 **CARL** partial (§2 withdrawn; §1 produce demotion stands; cost-push survives on *statutory* grounds with a dated Q4-2026 impulse as the floor steps $14→$15), 🟡 **CORAL** one line.
13. **Thesis v2.7 → v2.8** + CHANGELOG; STATUS reversal block (and archived the 7/9 + 7/2 blocks + prior header to hold the 250 cap — now 223 lines); VX FL-01 / 2.05 / 2.06 corrected; NEXUS_BRIEF rewritten with a **second** calibration event and a standing caution to consumers.
14. **`VX-2.05` marked `[STALE] NO PRIMARY`** — ag wage growth is genuinely unmeasurable on current sources (NASS Farm Labor Survey canceled Aug 2025; BLS CES excludes NAICS 11). Candidates logged: QCEW NAICS 11, **OFLC AEWR** (the untracked one worth building).
15. **New auto-memory** `finding_run_the_falsifier_before_promoting` + MARCO MEMORY entry.

**The state this leaves Channel 1 in — say it plainly:** quantity evidence **HIGH and untouched** (foreign-born LF −700K YoY, LFPR 61.5%, less-than-HS LFPR 43.1%, H-2A ~455-465K). **Transmission to prices/costs: NO working instrument.** Both candidates failed their own pre-registered tests hours apart. MARCO can assert the shock happened and is large; MARCO cannot demonstrate it is transmitting — which is the half downstream agents consume.

## NEXT SESSION
1. **~~BUILD THE WAGE PANEL~~ — DONE 18b, and it FALSIFIED the instrument. Replacement item: decide whether Channel 1 has ANY demonstrable transmission.** The next test must **control for statutory wage floors** — immigrant-heavy vs immigrant-light sectors *within* a state, or no-floor-step states. Untracked candidate: **OFLC Adverse Effect Wage Rates (AEWR)** — administrative, per-state, the one wage series specific to agricultural immigrant labor. **If a floor-controlled test also comes back null, downgrade Channel 1 from spine to "well-evidenced upstream fact, unproven downstream" (MAJOR bump) rather than hunting a third instrument.** TX is the natural control and currently says no.
2. **Build the boot guard** — `scripts/staleness.py` should flag rows that are **BREACHED/CRITICAL *and* >60d** as their own alert, not fold them into a 42-count. Mechanizes this session's lesson; the memory alone won't hold it.
3. **Install the WALTER consume boot-step** (asked 7/11, never done — the mechanical cause of 9 unread SIGs). One-time `CLAUDE.md` edit.
4. **Finish the VX stale sweep — 35 of 38 rows remain** (FL-01/2.05/2.06 done 18b). **Triage by STATUS, not age** — 25 are BREACHED/CRITICAL. **Biggest structural finding:** ~19 of them are a single abandoned research area (border-fiscal: El Paso, Nogales, Imperial Cty, San Ysidro, McAllen, Pharr, AZ URS, TX OLS, BDR-*, CAL-*, SFE-01/04), all Feb-4 vintage, untouched since founding. Per root CLAUDE.md Data Hygiene these should go **FROZEN with a banner** rather than sit as live-looking BREACHED rows — a BREACHED vector nobody maintains is the loaded gun. A stale NORMAL row is harmless; a stale BREACHED/CRITICAL row is the one that gets cited, and it misfired twice this session in opposite directions.
5. **MCO via BTS T-100** — carried s16→s18, still open; flymco re-verified JS-blocked 7/25. **MAR-24 and MAR-22 now both hinge entirely on this.**
6. **Inbox: 17 items** (8 top-level + 9 WALTER SIGs) — separate spawn per MAIL protocol.
7. **Aug 1** Banxico June remittances — count YoY = cleanest *surviving* SDL-01 proxy. **~Aug 12** July CPI → close ES-05. **~Aug 15** NTTO June → ES-MARCO-09.
8. **CORAL joint session** — three open asks now (migration divergence 7/9, ATTOM metro overlap 7/17, FL OIR premium primary 7/25).

## OPEN THREADS
| Item | Status |
|------|--------|
| Wage instrument — confirm or falsify (4-state panel) | 🔴 NEW 7/25 — the decision point; provisional MED-HIGH until decomposed |
| VX stale backlog ~35 rows; boot guard for BREACHED+stale | 🔴 NEW 7/25 — root cause of this session's bad claim |
| VX-3.01 household insurance — no figure adopted, needs FL OIR primary | 🟠 NEW 7/25 |
| MCO pax via BTS T-100 | 🟠 carried s16→s18; now blocks two predictions |
| FL migration divergence (canonical +22,517 vs BofA Q1'26) → CORAL | 🟠 carried from 7/9, packet re-sent 7/25 |
| ATTOM SW-FL metro overlap → CORAL (metro-series ownership) | 🟠 carried from 7/17, packet sent 7/25 |
| SDL-01 magnitude adoption → LABOR (MARCO is the origin of the bad ~1.6–1.9M) | 🟠 carried s16→s18, packet re-sent 7/25 |
| WALTER consume boot-step never installed | 🟠 carried from 7/11 |
| ES-MARCO-09 World Cup reversal | 🟠 leans FAIL; NTTO June ~Aug 15 |
| MAR-26 construction raids | Q3 clean test (carried) |
| Property-tax Amendment 3 (Nov 3) | 🟡 logged to docket 7/25 |
| El Niño 81% very-strong Oct-Dec → FL winter 26-27 | 🟡 NEW 7/25 — lands on the snowbird-$ window; second-order, not modelled |
| PREDICTIONS_ARCHIVE + calibration scoreboard; PREDICTIONS.tsv col-count (T1-D) | 🟡 carried s16→s18, still not touched |

## Mail state
**Inbox: 17 unprocessed** (8 top-level: AEOLUS ×3, DAEDALUS, WALTER, CORAL ×2, PROME; 9 WALTER SIGs, oldest 7/10). **Read for situational awareness this session, NOT processed** — no files moved to `processed/`. Per MAIL protocol, inbox processing is its own spawn. The CORAL 7/21 + 7/17 packets and PROME 7/21 were acted on substantively (all three CORAL corrections adopted) but remain in place for the formal pass.
**Outbox: 3 packets written 7/25** → `AGENTS/LABOR/inbox/` (wage instrument + produce demotion + SDL reconcile), `AGENTS/CARL/inbox/` (produce retraction + FL wage cost input), `AGENTS/CORAL/inbox/` (household-vs-insurer split + 2 metro reconciles + FL OIR ask). Committed under the self-authored-packet carve-out.

## PUSH STATE
Session 18 commits: `0125077ab` (auto-memory file), `f25bd6762` (VX refresh + MEMORY), `2f40e3be9` (canonical closeout: THESIS v2.7 / CHANGELOG / STATUS / EXPECTED_SIGNALS / PREDICTIONS / docket / KB / archive), plus the handoff-surface commit carrying this file + NEXUS_BRIEF + the 3 cross-agent packets.
**Note:** VIOLET was running concurrently on this box and swept MARCO's auto-memory index line into its own commit `334c89673` — expected under one-box concurrency, no action needed. `AGENTS/CARL/sub_agents/STUE/WORKLIST_2026-07-25.md` is uncommitted and **not MARCO's** — flagged to PROME, not swept.
