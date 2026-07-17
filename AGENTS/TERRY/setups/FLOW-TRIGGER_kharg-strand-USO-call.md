# FIRE CARD — USO — Kharg-strand supply-loss / OTM call spread (deploy-on-flow-trigger)
**Setup ID:** TRY-FIRE-006 · **Trigger class:** FLOW (physical supply-interruption discriminator — explicitly NOT a price level, NOT a headline, NOT a Hormuz transit count)
**Thesis owner:** RED (reversibility red-team, finding A — `AGENTS/RED/outbox/2026-07-17_to-PROME_reversibility-consensus-redteam.md`) + BRENT (energy/oil, Scenario-C / $200 Tier-2) + FALCON (Kharg flow tripwire + `domain/FRESH_LEG_BASELINE.md`). Routed by PROME 2026-07-17 (Will-approved PRE-BUILD, "build it flow-anchored").
**Card pre-built:** 2026-07-17 ~15:40 ET
**Fired:** ____ (fill at fire)
**Status:** PRE-BUILT / SHELVED — **built ≠ armed ≠ deployed.** Will [Approve] + live broker book required (rule #4/#5). Confidence in structure: **Medium** (thesis owner-held; the trade's job is to survive the vol-rich entry, which the spread does).

> **Capital note (do NOT conflate reserves):** this card draws on a **NEW ~$200 max-loss tranche** (BRENT 7/16 Tier-2 sizing language). It is **separate** from the **$500 banked for TRY-FIRE-004** re-fire. Firing this does not touch 004's budget and vice-versa.

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (written in advance; do NOT re-derive at fire)
══════════════════════════════════════════════════════════════

### The thesis this card serves
The book's oil posture is **pass-on-chase**: no new convexity at Brent ~$87, re-entry deferred to a ~$80–82 stabilized pullback "with the closure still in force." That plan is optimized for the **reversible-premium** world (RED steelman: six strike nights → zero capacity destroyed → premium reverses). **A Kharg flow interruption breaks that plan.** Kharg Island handles **~1.5 Mbpd ≈ 90% of Iran's crude exports**; a de facto stoppage (seizure, blockade, insurance withdrawal, or Iranian shut-in) is a **supply-loss** event — oil gaps toward **$95–100+ and grinds higher on inventory draw**, never revisiting the $80–82 entry band, so the pass-on-chase strands the book flat through the whole move. Critically, **FAL-01 (FALCON's oil-infra-HIT kill-switch) stays DARK on the strand path** — a seizure removes barrels *without destroying capacity*, so the fleet's "no capacity destroyed" anchor would read a seized Kharg as a non-event while 1.5 Mbpd leaves the market. **That mis-read IS the edge:** the reversible-premium market systematically under-prices the non-destruction supply-loss path because its tripwires are destruction-specific. This card is the pre-built response — it forgoes the initial gap **by design** (Will chose pre-build over pre-buy) and captures the **post-trigger continuation** as 43-year-low buffers (SPR 319.5M = Apr-1983 low; Cushing 20.04M = at the sub-20M line) draw down.

### Trigger condition (exact) — FLOW-ANCHORED, Kharg-EXPORT-specific
**ARM only on the observable FLOW state of Kharg crude exports — never the political act, the headline, or a Hormuz chokepoint transit count.** "Seizure" that maintains loadings does NOT fire; a de facto stoppage never labeled "seizure" DOES.

- **Candidate condition (semantics to be FROZEN with FALCON before ARM — see open dependency below):**
  **Kharg terminal crude loadings / tanker callings ≈ ZERO (or ≤~10% of the trailing-30d baseline) for ≥2 consecutive observed days**, **AND** at least ONE corroborating notice:
  - UKMTO / JWC / P&I war-risk withdrawal or listing **specific to Kharg / Bandar-e-Emam** (not the generic Gulf listing already standing since JWLA-033), **OR**
  - an official Iranian export-suspension statement or an official seizure/blockade declaration affecting the Kharg loading complex, **OR**
  - **FALCON's Kharg-seizure tripwire fires** (registration ask already in FALCON's inbox: `AGENTS/FALCON/inbox/2026-07-17_from-PROME_red-kharg-seizure-tripwire-ask.md`). **Coordinate so this card's condition and FALCON's tripwire are ONE condition, not two near-duplicates.**

- **⚠️ CONSTRUCTION-CRITICAL — do NOT anchor the trigger on the Hormuz transit count.** Per PROME's denominator ruling (7/17, `AGENTS/BRENT/domain/HORMUZ_TRANSIT_BASELINE.md`): a ≤18/day transit print fires on **86.6% of ALL crisis days** (near-zero discriminating power), and **a collapsed transit count is NOT a collapsed export volume** — the Oman-hugging bypass + STS transfers move crude *without* showing up in chokepoint counts (this is the exact reconciler between an 11% transit print and ZERO lost barrels). The whole reversibility frame rests on that bypass working. **This card fires on Kharg EXPORT-loadings stopping (barrels genuinely not leaving), which is a different measurement than Hormuz through-traffic.** Anchoring on transits would re-buy already-priced reversible premium — the precise mistake this card exists to avoid.

- **Anti-false-fire guards (encode all four):**
  1. **Single-day loading gaps** happen for weather/ops → require **≥2 consecutive** observed days.
  2. **"Seize-but-flow-continues" branch** (Will's 7/17 question — unlikely per incentives/insurance, but handled for free): if loadings continue, the flow anchor does NOT fire regardless of the political label.
  3. **April-vintage recirculated stories** (FALCON's trap register — Bandar Abbas refinery stories, export-terminal near-misses) → require a **live-dated** print, not a restatement.
  4. **Bypass-still-running** cross-check: if Vortexa/Kpler show STS/shuttle volumes replacing Kharg loadings ("restoring flows"), the supply-loss is being absorbed → **hold, do not fire** on the transit optics alone.

- **Sourcing caveat:** the "Trump weighing a Kharg seizure THIS WEEK" report is **techtimes-grade, UNVERIFIED** (corroborated only by Wikipedia/straits.live). The card's existence does not depend on it — note it as **unconfirmed context, not evidence.** The trigger is the flow state, whatever the political route.

### One-line setup
Defined-risk far-OTM USO call spread expressing a **supply-loss gap-continuation** — entered AFTER a confirmed Kharg export strand, riding the inventory-draw grind that the reversible-premium market under-prices because its tripwires are destruction-specific.

### Structure
- **Instrument:** USO **call spread** (long lower-strike OTM call / short higher-strike OTM call).
- **Expiry / tenor:** **~45–60 DTE from the FIRE date**, nearest liquid monthly. *(Pre-build reference: the Sep-19-2026 monthly ≈ 64 DTE from today; re-anchor at fire.)* Tenor matches the **mechanism, not a scalp** — a Kharg strand against 43-yr-low buffers is a weeks-long inventory-draw grind, not a one-print gap, so the trade needs time for the draw story to compound.
- **Strike ladder (LOGIC, not locked — pick from the live POST-GAP chain at fire):** long leg ~**ATM-to-5% OTM of the post-gap USO print**; short leg ~**10–15% further OTM** (caps the vol-rich premium you're paying). Width set so **total net debit ≤ $200**.
- **Spread is MANDATORY, not optional.** Fire-day vol will be extreme — OVX already **p93** and **OVX/VIX ratio p96.8** (VIOLET KB-VIO-120; live OVX ~61 / VIX ~18 per RED 7/17 13:09 ET), and a strand gaps it higher. A naked far-OTM USO call at that vol is nearly all extrinsic and bleeds hard; selling the further-OTM leg recovers the vol premium and is what keeps a $200 tranche meaningful. *(Consistent with TERRY's own options research: buying oil-vol at p93 pays the full vol tax — the spread is the only way to pay it and still have convexity.)*

### Why this expression beats alternatives
- **USO shares** — no convexity; captures the grind but not the gap-continuation asymmetry, and Will already holds USO shares (the flat exposure is covered).
- **Naked USO calls** — pays peak vol (OVX p93) as pure extrinsic; a $200 tranche buys almost nothing survivable.
- **Longer-dated (Dec/Jan) calls** — over-pays for time the inventory-draw thesis doesn't need and dilutes the gap-continuation delta.
- **Waiting for the $80–82 pullback (the book's base plan)** — the strand path *has no pullback*; that plan strands the book flat through a $100+ move. This card IS the gap-risk rider RED's finding A calls for.

### Max-loss budget
**$200 HARD cap** (new Tier-2 tranche, BRENT 7/16). Separate from 004's $500. Defined-risk by construction (debit spread = max loss is the debit paid).

### Rule #6 pre-documentation (PRE-AUTHORIZED break — do NOT relitigate at fire)
The fire day will almost certainly be a **violent GREEN day** (oil gapping up = USO green). **Calls-on-a-green-day is a rule #6 break.** Rule #6 (puts-on-green / calls-on-red) is a **mean-reversion entry-timing** rule — it exists to stop chasing extended moves. A supply-loss gap-continuation is **explicitly NOT a mean-reversion setup**: it is a regime-break momentum entry where the thesis is "no pullback comes." **Waiting for a red day = missing the move by design.** Per the rule text ("note when breaking and why"), the break is **pre-documented and pre-authorized here** as the exception class. *(The vol axis partially self-corrects the chase: OVX at p93+ means you're buying rich — which is exactly why the structure is a SPREAD, not outright.)*

### Invalidation / kill / confirm
- **Invalidation (thesis):** de-escalation confirmed — the Muscat/Oman Article-5 safe-passage mechanism executes (RED estimates this branch **~5–10%**) → Kharg loadings resume, the supply-loss premise dies → **RETIRE the card.**
- **Kill line (post-fill):** a confirmed resumption of Kharg loadings to normal (bypass absorbs / seizure reversed) → exit; and standard time-stop — the inventory-draw grind should be visible within the tenor, no draw-through-buffers by ~half the DTE = thesis not confirming.
- **Confirm line (go/hold):** loadings stay stranded AND Cushing/SPR buffers visibly draw (HEARTBEAT dashboard) AND war-risk-freight stays elevated → the supply-loss is real and compounding, hold to target.
- **Retire if unfired at ~30d** → re-underwrite (don't let a pre-built tail rot on a stale premise).

### §9 Concentration (aggregate the shared-falsifier book — REQUIRED read before ARM)
This deepens the **one-Mideast-bet**. The shared falsifier is a **Hormuz de-escalation** (Muscat/Article-5, ~5–10%), which fires on multiple book legs at once. Honest split of what dies vs survives on that falsifier:
- **Dies on de-escalation:** USO oil-long (20 sh) **+ this ~$200 tail** — the pure oil-premium legs.
- **Survives de-escalation:** TRY-FIRE-004's **real-yield / term-premium leg** — NEXUS/RED grade it independent of oil (10Y held ≥4.50 *through* a deflationary June print). So the ~$1,150 duration grind is only **partially** shared.
- **Aggregate Mideast-de-escalation-falsifiable oil cluster = USO shares + this $200 tail** (small, defined-risk). Total thesis-adjacent exposure with the rates grind ≈ **$1,350**, but do not double-count 004's surviving real-yield leg as "shared." **This card is the smallest, most defined-risk leg of the cluster and the only one built to pay off ON the strand path the others miss.**

### Alternatives rejected (named once)
Naked calls (vol tax) · shares (no convexity, already held) · long-dated calls (wrong tenor) · Hormuz-transit-anchored trigger (86.6% base rate, transit≠volume) · pre-buy now (Will chose pre-build; the $87/OVX-61 tape is a chase per BRENT's valid vol-rich argument).

### ⚠️ OPEN DEPENDENCY — must resolve with FALCON before this card can ARM
The trigger needs a **Kharg-EXPORT-loadings data source** (tanker callings / loaded DWT at the Kharg terminal), which is **NOT** FALCON's current `hormuz_transit_watch.py` (that pulls the Hormuz *chokepoint*, port-agnostic). Candidate sources: PortWatch **port-level** series for Kharg/Bandar-e-Emam, or Vortexa/Kpler tanker-tracking (FALCON has cited Vortexa "restoring flows"). **Until a Kharg-loadings series is confirmed pullable and its "≈ZERO for ≥2 days" bar is numerically frozen, this card is CONDITIONAL on that freeze** — do not ARM on the Hormuz transit proxy. This is flagged to PROME/FALCON in the outbox note.

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (fill ONLY at actual fire — rule #4)
══════════════════════════════════════════════════════════════
- **Timestamp (ET):** ____
- **Flow-trigger confirm:** Kharg loadings ≈ ZERO for ≥2 obs days? [Y/N] · corroborating notice (which)? ____ · bypass-still-running cross-check clear? [Y/N] · NOT anchored on transit count? [confirm]
- **Spot(s):** USO ____ (post-gap, `fetch.py price USO` via `.venv`) · Brent ____ · OVX ____ / VIX ____ (ratio percentile) — as-of ____
- **Green/red day check (rule #6):** GREEN expected → **BREAK PRE-AUTHORIZED** (gap-continuation exception, ZONE 1). Confirm vol regime for spread-width sizing.
- **Chain marks (POST-GAP, live):** `chain_fetch.py USO <EXPIRY> --type call --no-cache`
  | Strike | Mark | Spread% | IV% | OI | Moneyness% |
  |---|---|---|---|---|---|
  | (long leg) | | | | | |
  | (short leg) | | | | | |
- **Liquidity OK?** [spread/OI acceptable at $200 scale — Y/N]
- **Broker position truth:** existing USO exposure (20 sh + any calls)? [POSITION_INTAKE or `[POSITION_STATE_UNKNOWN]`]
- **Sizing (`risk_calc.py --premium <net-debit> --max-loss 200`):** ____ spread(s), net debit $____ ≤ $200, max value $____, ratio ____:1

══════════════════════════════════════════════════════════════
ZONE 3 — TRIGGER CONFIRM + DECISION
══════════════════════════════════════════════════════════════
- [ ] FLOW trigger actually fired — Kharg loadings stranded ≥2 days + corroborator (NOT a transit-count read, NOT a headline)
- [ ] Bypass cross-check clear (Vortexa/Kpler not showing STS replacement)
- [ ] Live POST-GAP marks pulled (< 15 min old)
- [ ] Structure = SPREAD (vol-rich confirmed); net debit ≤ $200
- [ ] Rule #6 break noted (pre-authorized gap-continuation exception)
- [ ] Liquidity acceptable · Position truth known · §9 aggregate stated

**Terry verdict:** CLEAN / CONDITIONAL / NO TRADE
**Decision:**  [ ] APPROVE   [ ] REJECT   [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

---
### FIRE RUNBOOK (the commands behind ZONE 2)
```
1. source .venv/bin/activate && python3 FORGE/tools/market-data/fetch.py price USO --json
2. python3 AGENTS/TERRY/scripts/chain_fetch.py USO <EXPIRY> --type call --no-cache
3. python3 AGENTS/TERRY/scripts/risk_calc.py --premium <net-debit> --max-loss 200
```
Cross-refs: RED memo (findings A + 3a) · FALCON Kharg-seizure tripwire ask + `FRESH_LEG_BASELINE.md` + `HORMUZ_TRANSIT_BASELINE.md` (denominator ruling) · VIOLET KB-VIO-120 (OVX canary) · BRENT 7/16 re-arm memo (Scenario-C / $200 Tier-2).
