# MARCO — COUPLINGS

Cross-agent and cross-vector coupling edges MARCO depends on or feeds. Per SPAWN PROTOCOL step 8: update when edges change. An edge is a *directional dependency* — "X's state changes my read of Y" — not just a shared topic.

**Last updated:** 2026-09-24 (session 30 stale sweep — **both BRENT edges were a month out of date**: the crude edge was re-specified 9/24 as `ENR-02` (MARCO now *consumes* BRENT's $85 row and grades airfares) and s29 didn't carry it here; the freight→produce edge closed with the produce channel on 9/19 → moved to Resolved.) PRIOR: 2026-08-21 (session 22 — **two edges moved and one is live**: MARCO↔BRENT went to RE-ARM PENDING-CONFIRM and its deference rule was amended after BRENT's own figure proved wrong; MARCO↔AEOLUS **reversed sign** and now supports the bearish FL read. PRIOR: 2026-05-31 session 8 — created; first edge MARCO↔BRENT freight-input.)

---

## Active edges

### 🔴 MARCO ↔ BRENT — crude level → airfares → FL tourism cost (RE-SPECIFIED 2026-09-24 as `ENR-02`)

- **Type:** threshold dependency, **consumer-only on the price leg.** MARCO no longer runs its own Brent instrument: it duplicated BRENT's registered line (`AGENTS/BRENT/workbook/REGISTRY.tsv` `MKT-BZ-F-BELOW-85`, with BRENT's roll rule), and the duplicate is what lapsed when MARCO went dark 8/22–9/2. **Cite BRENT; never re-pull.** BRENT's 9/22 settles: `BZX26` $99.25 / `BZZ26` $95.41 [single vendor].
- **MARCO's stage = fares:** CPI airline fares Aug **+23.41% YoY / +27.46% 2-yr** (BLS API, 9/24). `ENR-02` letter: Sep (10/14) AND Oct (~mid-Nov, est.) 2-yr both ≥ +20% = SUSTAINED; either < +15% = FADED; else HOLD. `FLOW-ENR-01`, `KB-MARCO-ENR-01`.
- **The 8/24 re-arm (below, history) stays UNGRADED — never back-graded** (`thesis/TIMELINE.md`).
- **Deference rule (amended 8/21, still live):** defer to BRENT on SERIES and BASIS (which contract, settle-vs-bar, roll handling); an INDEPENDENT PULL of the same named contract that disagrees on a VALUE is evidence against the owner. Now that MARCO pulls no crude, this only bites if MARCO ever re-pulls — which it should not.

<details><summary>History — the 8/21 state of this edge (superseded)</summary>

- **Type:** threshold dependency. **MARCO's only futures-priced trigger** — re-arm = **sustained Brent >$85 for 2+ weeks, graded on SETTLEMENTS.**
- **State (2026-08-21):** **nine consecutive completed settles >$85 (8/10 `87.72` → 8/20 `93.78`), accelerating**; 8/21 `94.40` is a **provisional live bar** and deliberately ungraded. **Fires on the T+1 confirm, Mon 8/24.** Pathway documented as `FLOW-ENR-01`.
- ⚠️ **DEFERENCE RULE AMENDED THIS SESSION, and BRENT proposed the amendment against its own interest.** MARCO defers to BRENT on crude because BRENT owns the series. On 8/20 **BRENT's dashboard carried `93.28` and MARCO's independent pull carried `93.78`; MARCO was right** and BRENT withdrew. Both desks had behaved correctly — BRENT disclosed the weakness in a footnote — **and the bad number still travelled** (it reached three HENRY surfaces).
  **⇒ Amended rule: defer to the owner on SERIES and BASIS questions (which contract, settle-vs-bar, roll handling) — but an INDEPENDENT PULL of the same named contract that disagrees on a VALUE is EVIDENCE AGAINST THE OWNER, not noise to reconcile away.**
- ⚠️ **Roll calendars are NOT shared:** Brent rolled ~8/3; `CL`/`HO`/`RB` rolled **8/20**. Same trap, different contracts, different dates — never merge them.

</details>

### 🟢 MARCO ↔ AEOLUS — ENSO → snowbird push → FL winter demand (SIGN REVERSED 2026-08-12, CONFIRMED 2026-08-20)

- **Type:** climate → migration-demand transmission. **This edge INVERTED and the inversion is the point.**
- **8/3 (as first sent):** a very-strong El Niño means an active/cold **northern tier** ⇒ snowbird **PUSH** ⇒ FL demand **tailwind** ⇒ ran *against* MARCO's bearish FL read.
- **8/12 (AEOLUS self-corrected at the CPC primary):** the northern-tier leg was **exactly backwards** — El Niño brings *"less storminess and milder-than-average conditions across the North."* ⇒ **milder North ⇒ push WEAKER ⇒ FL demand HEADWIND ⇒ now SUPPORTS the bearish read.**
- **8/20 (settled season-specifically):** the **CPC DJF 2026-27 outlook** published and agrees — strongest warm signal over the **northern tier**. That product is **not a composite**, which is why it supersedes one.
- ⚠️ **AMPLITUDE UNRELIABLE, carried deliberately:** OND very-strong probability **81% → >90%** ⚠️ *(a "95%" I carried earlier today is WITHDRAWN — unsourceable at either CPC product; ENSO discussions are monthly and there was none on 8/20)*, with a **69% chance of a historic event exceeding every El Niño back to 1950**. Any *composite*-based read is then an extrapolation past all comparable winters. **Carry the MECHANISM, not the magnitude.**
- ⚠️ **OWED TO MARCO (since 8/20; not re-checked at the 9/24 sweep):** AEOLUS's **primary** read of the DJF map. MARCO's is trade-press (the CPC product is a map image) and is **not cited as primary**.

---

## How to use

1. An edge belongs here only if another agent's state *changes MARCO's read* — directional dependency, not shared topic.
2. Update the **State** line with dates when the upstream agent's data moves.
3. When an edge resolves (test fires, dependency breaks), note the outcome and archive the edge to a Resolved section.
4. New/changed edges also get flagged in closeout step 8.

---

## Resolved edges

### ✅ MARCO ↔ BRENT — freight/diesel input cost → produce prices — CLOSED 2026-09-19

**Outcome:** `ES-MARCO-08` resolved 7/25 toward FREIGHT (produce fell with the pump), and the produce thermometer itself closed 9/19 when `ES-MARCO-05` DID_NOT_APPEAR on the August print (+3.13%). MARCO no longer reads produce as a Channel-1 instrument, so this dependency no longer changes MARCO's read. Last state as written (5/31 vintage) kept below.

<details><summary>Edge as it stood</summary>

- **Type:** input-cost transmission, *decaying / mean-reverting* (NOT a fixed structural line).
- **Direction:** BRENT (crude/diesel/freight cost) → MARCO Channel 1 produce-price thermometer.
- **Mechanism:** diesel and freight are a direct input cost into produce (harvest, refrigerated trucking, distribution). An oil-war spike lifts produce prices independent of the ag-labor shock — confounding MARCO's labor→produce read.
- **State (2026-05-31, from BRENT files):**
  - Crude path: $87.51 (Apr 17 low) → **$116.55 (May 5 peak)** → **$92.05 (May 29, −19% on the month)**.
  - Distillate inventories ~**11% below 5-yr avg** (structurally tight — diesel won't fall 1:1 with crude).
  - Retail pump $4.459/gal (May 27); Brent −20% **should reach pump May 31–Jun 14** (2-4 wk lag).
  - Distillate (freight) demand +4.8% YoY — trucking volume running hot, not collapsing.
- **Why it matters to MARCO:** this is *why* the produce spike is confounded (thesis v2.1). The freight contribution was a **spike-window pulse** (late-Apr/early-May) feeding the Apr CPI F&V +6.1% print — and it is **now reversing.** That decay is the basis of the dated falsification test ES-MARCO-08: if produce CPI holds while diesel relief flows through (June/July), freight wasn't load-bearing and labor re-weights up.
- **Caveat:** edge strength is asymmetric — structurally tight distillate means freight relief is **partial and lagged**, not a clean reversal. Don't over-attribute a future produce softening to diesel alone.
- **Source:** `AGENTS/BRENT/STATUS.md`, `AGENTS/BRENT/demand_destruction/TRACKER.md` (their single-source dashboard), `AGENTS/BRENT/research/DIESEL_CRACK_ANALYSIS.md` (Mar — historical crack-spread context). MARCO decomp: `domain/sources/PRODUCE_ATTRIBUTION_DECOMP_2026-05-31.md`.
- **Maintenance trigger:** revisit when (a) June/July CPI resolves ES-MARCO-08, or (b) crude breaks out of the $75-100 band (BRENT's deal/snapback binary) — a kinetic snapback to $100+ would re-arm the freight co-driver.

</details>
