# BG-02 — Petroline frame-breaker window grade: PREP (armed, NOT graded)

**Written:** 2026-09-25 03:0x ET by BRENT (PROME Tier-1 due-row spawn, DOCKET L329; prome-fa). **The grade runs at/after 17:00 ET today, not before.** This file is the pre-committed reading so the 17:00 session applies it rather than reconstructs it (`finding_two_phase_spawn_grader_contract`).
**Letter:** [SPECS_GATES.md § BG-02](SPECS_GATES.md#bg-02--frame-breaker-prospective-capacity-floor-and-constraints), WQ-234 C1–C6 (encoded `e360cce14`). **WQ-264 ③ (Will 2026-09-24 08:50 ET):** the window closes on its own letter; NOT extended.

## Evidence state at 03:0x ET 9/25 (every item carried on its own class)

| Item | Source / date | Class under the letter | Weight |
|---|---|---|---|
| Petroline RESTARTED, "pumping at a low rate"; "4 mb/d" = target rate | Reuters, 3 unnamed sources, 9/22 (SIG-W-20260924-002) | wire, unnamed; not Aramco/MoE/SPA; no lost-capacity figure | **Not R1** (C4) |
| Crude flowing to Red Sea refineries; Yanbu tanker loadings NOT resumed as of 9/24; Aramco building "critical mass"; full capacity "six weeks or more" | Reuters via Baird 9/24 18:19 (SIG-W-20260924-021) | wire, unnamed sources; Aramco quote relayed, not on record | **Not R1** (C4) |
| "Three pumping stations damaged" / "3 of 11 pump stations" | Reuters 9/24; Enterprise AM (originator unnamed) (SIG-W-20260924-010/-021) | wire statement, not operator; no throughput figure | **Not R1** |
| Two 9/23 Yanbu liftings missed; ~6 due 9/24–27; "no Yanbu loadings since 9/11" | Kpler (single vendor), relayed | AIS-derived tracker (R2) | **C5 NO-CORROBORATION** — one vendor, no dark-share disclosure ⇒ zero weight, neither confirms nor refutes |
| Aramco "informally signalled" three Asian refiners that Yanbu loadings could resume soon | web search 03:0x ET 9/25 (Zetik/BigGo headlines, unread bodies) | unnamed, informal | **Not R1** |
| Houthi missiles at Yanbu/Taif 9/24 | coalition: INTERCEPTED (SIG-W-20260924-015) | no impact established | none |
| FALCON clean FAL-01 with output-loss figure | none found in the inbox or on the lane | R4 | **R4 absent** |
| Berth occupancy (Sentinel, AIS-independent) 9/22 snapshot: Al Muajjiz est. 476k bbl · North Pt2 1.05m · North Pt1 0 | hormuzstraittracker.com, read 03:01 ET 9/25 | WQ-264 shadow-run leg A — **not an instrument of BG-02**; hulls, not loadings | none (record-only) |
| Brent Nov−Jan (M1−M3) settle-proxy: 9/22 +6.51 · 9/23 +8.05 · 9/24 **+10.18** vs pre-shut +9.27 (9/10) | yfinance daily closes, single vendor | `R-CURVE-VETO` input — applies only to an R1+tracker pair | n/a (no pair exists) |

## Pre-committed decision tree for 17:00 ET

1. **Did Aramco, the MoE or the SPA state, on record before 17:00 ET, a named capacity-offline figure or a Petroline throughput reduction?** (Read at the operator/SPA primary or an owner-grade wire quoting it on record — not unnamed sources.)
   - **No** ⇒ go to 2.
   - **Yes, with a throughput/export figure ≥0.7 mb/d** ⇒ R1 meets its own row (C2): **MET on the letter** ⇒ fresh ask to Will (WQ-192 lift in his words + [Approve] at fill); TERRY re-prices leg (b) from the broker chain; **breach branch $4.95 binds**. Disclose any tracker disagreement in figures.
   - **Yes, capacity figure but no export effect stated** ⇒ C3: needs an ADMISSIBLE tracker pair (both Kpler AND Vortexa ≥0.7 mb/d on the 7-day MA, dark-share disclosed) + `R-CURVE-VETO` (M1−M3 must have widened vs +9.27 — it has on 9/24, +10.18, re-read at the 9/25 settle). Absent an admissible pair ⇒ NOT MET.
   - **Yes, >0 and <0.7 mb/d** ⇒ NO-VERDICT with the figure to Will.
2. **Did FALCON grade a clean FAL-01 with a confirmed output-loss figure?** No ⇒ go to 3. Yes ⇒ as 1 (R4 ≡ R1 under C2).
3. **Default and modal: WINDOW LAPSES — BG-02 instance (4) = NOT MET = premium, not destroyed capacity.** Closed; **not re-opened** on a later relay of the same 9/10 satellite data. Not extended (WQ-264 ③). Successor = the restart resolver, registered only AFTER the 30-day shadow run (window 2026-09-25 → 2026-10-24).
4. **C6 check:** no admissible tracker read exists (Kpler single-vendor fails C5) ⇒ no `NO-VERDICT — CORROBORATION WITHOUT SUPPORT` return is owed.

⚠️ **Honest limit, carried into the grade:** in substance Gulf export throughput through Yanbu **is** reduced — zero crude liftings 9/23–24 on every wire and tracker that speaks. The letter cannot fire on it because no operator has put a number on record and the only quantity is a single AIS vendor's. A NOT MET here is **"not established on the letter"**, not **"no barrels were lost"** — the NO-VERDICT/NOT-MET distinction Will ruled (WQ-234 C) is working as designed, and a lapse is not evidence the outage was small.

**$0. No trade, threshold, floor, MA or window moved. WQ-192 STAND DOWN holds.**
