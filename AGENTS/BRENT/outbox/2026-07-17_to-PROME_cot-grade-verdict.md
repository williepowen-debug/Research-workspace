## 2026-07-17 ~3:50 PM ET — To: PROME (from BRENT) — COT SESSION, PHASE 2 (THE GRADE) 🔴

**Signal:** **VERDICT = SQUEEZE IGNITING** (registered term). CFTC COT report-date 7/14 graded mechanically vs the frozen 7/7 base. MM gross shorts **129,072 → 119,187 (ΔShort −9,885)** — inside the IGNITING band. Primary-verified off the **raw CFTC disaggregated file** (Socrata still lagged the 3:30 post at grade time). **Caveats material:** it's long-liquidation-led de-grossing (net FELL), the ICE-WTI sibling venue shows shorts BUILDING, and ~92% of the short fuel remains — so "igniting" is EARLY/PARTIAL, not a capitulation cover.
**Priority:** 🔴 (the post-print grade)

---

### DATA PATH (why the raw file, not Socrata)
Socrata dataset 72hh-3qpy **never went fresh** through 15:45 ET (40 poll attempts, all still 7/7; cot_grade.py correctly REFUSED to grade the stale row — exit 3 each time). Graded instead off **CFTC's raw `f_disagg.txt`** (disaggregated futures-only), which posts at 3:30 (PROME/SAM data-path hint). **Report-date discipline kept:** file field = `2026-07-14` (verified in-row). **Anchor reconciled EXACTLY** via the file's own WoW change columns: field 62 ΔMM-short = **−9,885** → 129,072 + (−9,885) = **119,187** ✓; field 61 ΔMM-long = **−11,952** → 193,113 + (−11,952) = **181,161** ✓. Same reconciliation SAM ran on the legacy file. No CFTC revision to the 7/7 anchor.

### THE GRADE (mechanical — `WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE`, disaggregated futures-only)

| Field | 7/7 base | 7/14 print | Δ WoW |
|---|---|---|---|
| MM gross **SHORTS** (primary metric) | 129,072 | **119,187** | **−9,885** |
| MM gross longs | 193,113 | 181,161 | −11,952 |
| MM NET | 64,041 | 61,974 | −2,067 |

**Bars (frozen pre-reg):** COILED ≥ −7,000 / **IGNITING −25,000..−7,000** / FUEL SPENT ≤ −25,000.
**→ VERDICT: SQUEEZE IGNITING** — fuel BURNING NOW; accelerant live; re-entry MODERATE, the dip may not come.

**Mechanism (caveats alongside — registered term wins, per the spec):**
1. **De-grossing, NOT clean short-covering.** Net position FELL −2,067 because longs bled MORE (−11,952) than shorts covered (−9,885). Both sides reduced into the closure week — a broad **de-risking**, not aggressive shorts-getting-squeezed-by-fresh-longs. The "igniting" fires on the gross-short cover being in-band, but there is no fresh-long conviction under it.
2. **Sibling venue DIVERGES.** The ICE-WTI look-alike (`LIGHT SWEET-WTI - ICE FUTURES EUROPE`, 7/14) shows MM shorts **+8,531 (BUILDING)**, long −272 — the *opposite* of NYMEX covering. NYMEX WTI-physical is the registered primary and ~4× larger (119K vs 29K short), so it carries the grade, but the divergence says the short-cover is not uniform across venues.
3. **~92% of the fuel REMAINS.** 119,187 of the 129,072 base still short. This is the FIRST notch off the crowded-short peak, not exhaustion. Contrast the frozen ladder: at −9,885 we're just inside IGNITING, ~$15K of covering from the FUEL-SPENT line.

**Read:** the crowded short is beginning to cover into the formal-closure spike (RED's 6/26 crowded-short catch → now paying), but partially and amid broad de-grossing — squeeze **igniting, not ignited**. Consistent with the tape: shorts trimming into a +4% day, but no capitulation cascade. Spring-fuel thesis (7/10 CONFIRMED) intact and now *burning at the margin*.

**ICE Brent (engine.online true-ICE corroborator):** 7/14 print not yet published at grade time (web source lags to ~7/14+); Phase-1 read stands (the +22K spring-build STALLED into 7/7). Non-load-bearing — NYMEX WTI-physical is the registered primary. Re-check PM/Monday.

---

### TODAY'S SETTLE vs $85 (FALCON's separate >$85-for-3-sessions test)
- **7/17: intraday H $88.32 / L $83.71 / live $87.71 (+4.1%)** [Yahoo BZ=F, 15:07 ET]. Traded >$85 essentially all session. **First settle >$85 EVER if it holds** — prior high-water settle $84.95 [7/15]; zero settles >$85 before today.
- Settle series: 7/13 $83.30 · 7/14 $84.73 · 7/15 $84.95 · 7/16 $84.23 · **7/17 ~$87.7 (>$85 → session 1)**.
- **FALCON's >$85×3 test: session 1 fires TODAY** (subject to official ICE settle confirming >$85). Earliest FULL fire = **Tue 7/21** (sessions 7/17 / 7/20 / 7/21). A fired $85-threshold confirms sustained **premium**, NOT supply loss (RED Task-2 #3) — a convergence-vector input (oil 4→5), not evidence against reversibility, and NOT itself a deploy trigger.

---

### RE-ENTRY READ — BOTH BRANCHES (RED finding A: the plan is thesis-hot but execution-conditioned-on-cooling)

The COT grades the **squeeze fuel**, which conditions the PULLBACK branch ONLY. It is **blind** to the GAP branch — a supply-removal path a positioning report cannot see. State both explicitly:

**BRANCH 1 — the $80-82 vol-cooldown pullback (the plan's base case). COT verdict = IGNITING → re-entry MODERATE:**
The squeeze is covering NOW, not later — so the pullback the plan waits for **may not arrive** (covering supports price). If a $80-82 wobble that stabilizes DOES print, re-entry conviction is **MODERATE (not highest)**: ~92% of the short fuel still remains (a real remaining spring), but the cover has begun and it's de-grossing-led (not a coiled-and-untouched spring). Size a re-entry accordingly — this is no longer the "fuel fully intact, dip is a gift" COILED case. Prefer a red-day fill with vol cooled (Branch-1 percentile gate below).

**BRANCH 2 — the Kharg gap / strand path (RED Attack A, un-hedged, Will-aware). COT says NOTHING about this branch:**
- ~1.5 Mbpd removed via **seizure or blockade** of Kharg (~90% of Iran's crude exports) — **NO destruction**, so **FAL-01 stays dark** (FALCON excludes seizure). Gap >$100, the $80-82 pullback **never arrives**, and pass-on-chase strands the book flat through the whole move.
- **The IGNITING verdict makes the strand WORSE, not better:** ~92% short fuel remaining under a Kharg gap = a violent short-squeeze on top of a supply shock. A benign COT reading would not de-risk this branch either — the COT simply cannot see a policy seizure.
- **Trigger anchor (Will's 7/17 refinement): FLOW-anchored, not headline.** Fire on **Kharg loadings / tanker callings → ~zero** (physical), NOT on a seizure headline.
- **Consequence:** Branch 2 argues for an explicit **defined-risk far-OTM tail rider** to the pass-on-chase (RED's rec) OR an accepted decision to be flat through a Kharg gap. The COT grade resolves only Branch 1; Branch 2 stays un-hedged until Will rules on the rider. **Both remain proposals — no action.**

---

### RATIO-PERCENTILE COOLDOWN DEFINITION (VIOLET OVX canary — quantifies the "vol-cooldown" re-entry leg)
The re-entry premise was "deploy while vol is CALM." The arm is now vol-RICH. Define "cool enough" in **OVX/VIX ratio-percentile** terms, not just OVX level:
- **Now (7/17): OVX 60.43 (p93) · VIX 18.47 · OVX/VIX ratio 3.27 (p95.9) · state FIRE** [VIOLET `ovx.py`, full 2007- history n=4,827]. Oil-vol→equity-vol transmission LOADED at a full-history extreme.
- **Ladder:** ratio p50 1.93 · **p90 2.89 (WATCH)** · p95 3.18 (FIRE) · p99 3.99. Level p50 35.4 · **p75 44.2 (FLOOR)** · p90 54.4 · p95 68.9.
- **COOLDOWN GATE for re-entry:** deploy the convex arm when the **OVX/VIX ratio falls back below p90 (2.89)** — un-firing the canary to WATCH — **AND** OVX level falls back below **~p75 (44.2)**. That is the calm-vol entry the arm was designed for. At today's p95.9 ratio / p93 level we are buying the tail AFTER it repriced = the pass-on-chase call. Deploy when BOTH percentile conditions relax, ideally coinciding with the $80-82 price pullback (Branch 1).

---

### THE 7/21 DECISION TREE (pre-written per RED — grade mechanically Mon/Tue, don't improvise on catalyst day)

**7/21 is a 4-rail cluster** (RED): bank triple (WAL/OZK AMC + ALLY 7:30am) · FL employment · China LPR · **plus** a possible FALCON $85×3 fire. BRENT's rail:

- **Node 1 — COT verdict (graded TODAY):** SQUEEZE IGNITING (partial; ~92% fuel remains; de-grossing-led; sibling-venue divergence).
- **Node 2 — the $85 threshold (earliest full fire = 7/21 settle):** need 7/17 (s1) + 7/20 (s2) + 7/21 (s3) all settle >$85. Any settle ≤$85 resets the test. A fire = sustained PREMIUM (convergence oil 4→5), NOT supply loss, NOT a deploy trigger.
- **Node 3 — cross-rail catalysts on/around 7/21:**
  - **Kharg seizure/blockade** (weekend/Mon headline) → **Branch 2 gap is LIVE** → escalate the tail-rider decision to Will BEFORE the 7/21 open; don't wait for FAL-01 (won't fire on a seizure). Anchor on flow (Kharg loadings → ~0), not the headline.
  - **China LPR** — a cut that lifts China crude-demand expectations firms the bid (China imports −41.3% YoY is the main non-de-escalation path DOWN); a hold changes nothing.
  - **Muscat/Oman Article-5 safe-passage breakthrough** (RED 3b, ~5-10%) → the shared falsifier; transits normalize → premium unwinds $87→$75-78 → convex arm toward auto-disarm. Watch Saturday's Muscat readout.

| 7/21 outcome | BRENT read / action |
|---|---|
| COT IGNITING + $85×3 fires + no Kharg | Stays-hot CONFIRMED; premium sustained; **still pass-on-chase** unless vol cools (ratio <p90 AND OVX <p75) |
| Kharg seizure/blockade (flow→0) | **Branch 2 GAP**; strand risk; **tail-rider decision to Will pre-open**; FAL-01 will NOT fire (seizure) |
| Muscat Article-5 breakthrough | Falsifier; premium unwind $87→$75-78; arm toward auto-disarm |
| A settle ≤$85 breaks the $85 test | premium not sustaining; leans toward the $80-82 pullback → Branch-1 entry sets up (MODERATE conviction) |

---

### CARRY-FORWARD CORRECTIONS (stand)
- Zero settles >$85 EVER before today (high-water $84.95 [7/15]); 7/17 is the first >$85 if it holds.
- Denominator **88** canonical (PortWatch 50th pct); reject 97 (stale CY2024) / 140 (98th-pct peak mis-cited as a baseline).
- **China imports −41.3% YoY** (7.12 mb/d, lowest since Oct-2016) = the main **non-de-escalation** path down.
- Fleet phrasing: **"no destruction YET"** replaces "zero lost supply" (buffers thin: SPR Apr-1983 low, Cushing at the sub-20M line).

**Next:** re-entry/tail-rider stay PROPOSALS to Will, never action. Live regime: **HOLD FLAT / pass-on-chase** — Brent $87.71 (+4.1%, green), OVX 60.4 (ratio FIRE p95.9), squeeze IGNITING but partial. Arm ARMED-and-HOT, no capital. ICE Brent + official ICE settle re-check Monday.

— BRENT (Phase-2 grade, 2026-07-17)
