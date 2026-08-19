# FIRE CARD — USO — Kharg-strand supply-loss / OTM call spread (deploy-on-flow-trigger)
**Setup ID:** TRY-FIRE-006 · **Trigger class:** FLOW (physical supply-interruption discriminator — explicitly NOT a price level, NOT a headline, NOT a Hormuz transit count)
**Thesis owner:** RED (reversibility red-team, finding A — `AGENTS/RED/outbox/2026-07-17_to-PROME_reversibility-consensus-redteam.md`) + BRENT (energy/oil, Scenario-C / $200 Tier-2) + FALCON (Kharg flow tripwire + `domain/FRESH_LEG_BASELINE.md`). Routed by PROME 2026-07-17 (Will-approved PRE-BUILD, "build it flow-anchored").
**Card pre-built:** 2026-07-17 ~15:40 ET
**Fired:** ____ (fill at fire)
**Terry verdict:** 🔴 **RETIRED (terminal)** — **Will-ruled 2026-08-18**, on TERRY's recommendation. **NEVER FIRED, NEVER ARMED, `$0` AT RISK FROM BUILD TO RETIREMENT.** Design extracted to `research/PLAYBOOK_flow-trigger-supply-strand.md` before archiving — **the card decayed; the design did not.** ⛔ **A re-arm is a NEW CARD built on live numbers, never a revival of this one.**
> *Superseded verdict, kept dateable:* ~~🟡 CONDITIONAL / ARMABLE — unfired, $0 at risk, $200 fenced.~~
**Status:** **RETIRED** *(was PRE-BUILT / ARMABLE until the 2026-08-18 Will ruling; earlier still PRE-BUILT / SHELVED — corrected 2026-07-30; the 7/18 FALCON dependency discharge and 7/20 wording confirm moved this card to ARMABLE on `setups/INDEX.md` and `STATUS.md` pickup 7, but **this card, `SETUPS.tsv` and `TRADE_BOOK.md` all carried SHELVED for 12 more days** — caught by `scripts/ledger_sweep.py`, not by a human read)* — **built ≠ armed ≠ deployed.** Will [Approve] + live broker book required (rule #4/#5). Confidence in structure: **Medium** (thesis owner-held; the trade's job is to survive the vol-rich entry, which the spread does).

> **Capital note (do NOT conflate reserves):** this card draws on a **NEW ~$200 max-loss tranche** (BRENT 7/16 Tier-2 sizing language). It is **separate** from the **$500 banked for TRY-FIRE-004** re-fire. Firing this does not touch 004's budget and vice-versa.


> ## 🔴 RETIREMENT RULING — Will, 2026-08-18 EVE. **"ok retire."**
>
> **TERRY recommended RETIRE and Will ruled it. `$0` at risk from build (2026-07-17 ~15:40 ET) to retirement — never armed, never fired, no capital ever committed.**
>
> **The four reasons, strongest first:**
> 1. 🔴 **32 days in the most favourable environment this trigger will ever see, and it never armed.** The 60-day US–Iran MOU expired 8/17 with no deal · extension refused · the threat aimed at Muscat itself · crude cleared a settle it had failed five sessions · throughput ~21% of baseline. **If it cannot fire in that, the strand either is not happening or is not measurable by us. Both answers are "no trade."**
> 2. 🔴 **The fire path was narrower than the card read.** Four corroborator doors were listed; **one — the dark-fleet-capable tanker read (Kpler/Vortexa) — is not available to this fleet** (no API, no credential, no fetcher; a website entry in FALCON's `SOURCES.md`, reaching us only as second-hand routed estimates explicitly labelled *"estimates, not measurements"*). **The missing door was the only QUANTITATIVE one**, so in practice this card could fire only on an official declaration or an insurance notice — and **nobody wrote that down for 32 days.**
> 3. 🔴 **The pre-build's own value proposition failed its test.** A pre-built card exists so nobody re-derives under pressure — **but the PRE-LOCKED layer is exactly what rotted**, twice, in the two places a reader trusts most (the §9 concentration guard, stale by **2.23×**, and the fire-time position line still reading "20 sh"). **A stale concentration guard does not fail loudly — it PASSES.** ⇒ the card was no longer buying what it claimed, and a fresh build on live numbers is strictly better than firing a 7/17 one.
> 4. ⚠️ **The book moved underneath it.** `N_eff = 1` across the whole oil sleeve, base doubled to **$6,262**, and the largest leg (35 USO shares) is now held **by explicit Will ruling with NO exit rule**. `RISK_RULES` #17 — the size-INCREASING branch carries the higher evidential burden, and that evidence did not exist.
>
> ✅ **What was TRUE and is NOT being retired with it — extracted to `research/PLAYBOOK_flow-trigger-supply-strand.md`:** the corroborator-anchored + AIS-veto-only inversion (FALCON 7/18) · the ban on anchoring to chokepoint transit counts (PROME's denominator ruling: ≤18/day fires on **86.6% of ALL crisis days**) · the antecedent gate (BRENT/PROME 7/27) · the rule-#6 gap-continuation pre-authorisation · and the one-directional-bias rule written 8/18. **Retiring a card must not delete cross-agent work that cost real effort.**
>
> 🔴 **A DEFECT FOUND WHILE RETIRING, RECORDED BECAUSE THE RETIRE WOULD HAVE ERASED IT:** `FIRE_CARDS_LADDER.md` still carried **TWO** stale claims for this card — the header read **`PRE-BUILT / SHELVED`** (corrected to ARMABLE on three other surfaces 7/30, never here) and **"⚠️ BLOCKED before ARM: needs a Kharg-EXPORT-loadings data source frozen with FALCON"** (that dependency was **DISCHARGED 7/18**). **Stale for 19 and 32 days respectively, and `ledger_sweep` did not flag either.** Third distinct failure of that one file (007 absent entirely 8/7; 005 SHELVED 8/4). ⚠️ **Fixed as part of this retirement — and note the sequencing rule it produced: reconcile EVERY surface BEFORE archiving, because archiving removes a card from check A and ends the only thing that would catch drift.**
>
> ⛔ **Nothing was bought. Nothing was sold. No position exists or ever existed under this card.**

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (written in advance; do NOT re-derive at fire)
══════════════════════════════════════════════════════════════

### The thesis this card serves
The book's oil posture is **pass-on-chase**: no new convexity at Brent ~$87, re-entry deferred to a ~$80–82 stabilized pullback "with the closure still in force." That plan is optimized for the **reversible-premium** world (RED steelman: six strike nights → zero capacity destroyed → premium reverses). **A Kharg flow interruption breaks that plan.** Kharg Island handles **~1.5 Mbpd ≈ 90% of Iran's crude exports**; a de facto stoppage (seizure, blockade, insurance withdrawal, or Iranian shut-in) is a **supply-loss** event — oil gaps toward **$95–100+ and grinds higher on inventory draw**, never revisiting the $80–82 entry band, so the pass-on-chase strands the book flat through the whole move. Critically, **FAL-01 (FALCON's oil-infra-HIT kill-switch) stays DARK on the strand path** — a seizure removes barrels *without destroying capacity*, so the fleet's "no capacity destroyed" anchor would read a seized Kharg as a non-event while 1.5 Mbpd leaves the market. **That mis-read IS the edge:** the reversible-premium market systematically under-prices the non-destruction supply-loss path because its tripwires are destruction-specific. This card is the pre-built response — it forgoes the initial gap **by design** (Will chose pre-build over pre-buy) and captures the **post-trigger continuation** as 43-year-low buffers (SPR 319.5M = Apr-1983 low; Cushing 20.04M = at the sub-20M line) draw down.

### Trigger condition (exact) — FLOW-ANCHORED, Kharg-EXPORT-specific
**ARM only on the observable FLOW state of Kharg crude exports — never the political act, the headline, or a Hormuz chokepoint transit count.** "Seizure" that maintains loadings does NOT fire; a de facto stoppage never labeled "seizure" DOES.

- **✅ FROZEN 2026-07-18 with FALCON — GATE-TERRY-006 LIVE (corroborator-anchored + veto).** The open dependency is DISCHARGED. **CRITICAL INVERSION applied** (FALCON `outbox/2026-07-18_to-TERRY_kharg-merged-condition-confirm.md`): the loadings-≈ZERO test **canNOT be the primary** — the only pullable Kharg export series (IMF PortWatch `port2164` field `export_tanker`) is **AIS-based and ~90%+ blind to Iran's dark fleet**, so it prints literal ZERO for entire NORMAL months (Jan/May/Jul-2026 all 0). A ZERO-loadings primary would be TRUE right now with no strand = a false-fire generator. So:
  - **PRIMARY FIRE = ≥1 dark-fleet-capable CORROBORATOR, sustained ≥2 days, NOT vetoed** (was the "AND" clause; now the trigger itself):
    - UKMTO / JWC / P&I war-risk withdrawal or listing **specific to Kharg / Bandar-e-Emam** (not the generic Gulf listing standing since JWLA-033), **OR**
    - an official Iranian export-suspension statement or an official seizure/blockade declaration affecting the Kharg loading complex, **OR**
    - a **Kpler / Vortexa dark-fleet-capable tanker-tracking read** showing Kharg loadings genuinely collapsed (dark-fleet-visible, unlike PortWatch AIS), **OR**
    - **FALCON's Kharg-seizure tripwire fires** (now folded IN as corroborator (d) — ONE condition, not a near-duplicate row).
  - **PortWatch/Kpler AIS loadings = REFUTING VETO cross-check ONLY** (the inversion): a **NONZERO loadings print = flow continuing = do-NOT-fire.** It can kill a false political-label fire; it can never *cause* a fire. This mechanizes anti-false-fire guards #2 (seize-but-flow-continues) and #4 (bypass-still-running).
  - **⏱ Operational lag:** scripted data lags news **~1 week** (5–8d PortWatch publication lag). The FIRE always comes from the corroborator FIRST (declaration / Kpler-Vortexa / war-risk notice); the PortWatch veto confirms-or-refutes ~a week later. **Do NOT wait on the data print to arm — arm on the corroborator, then let the veto kill a false fire.**

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

> ## 🔴 DAY-32 RE-UNDERWRITE TRIGGER HAS FIRED — TERRY 2026-08-18 ~16:1x ET (`boot.py` WALL CLOCK, copied not inferred)
>
> **This card's OWN clause reads: *"Retire if unfired at ~30d → re-underwrite (don't let a pre-built tail rot on a stale premise)."* Card pre-built **2026-07-17 ~15:40 ET**. Today is **day 32**. The trigger came due ~**8/16** and was ungraded for 2 days.** ⚠️ **Found by reading this card, NOT by the two WALTER packets that prompted the read** — and it is the fourth time this desk has written the sentence *the spec was frozen in advance and correct; the INVOCATION was late.* **`$0` at risk throughout; the card is unfired and Will-pending, so the cost is zero and the pattern is the finding.**
>
> ### Construction half of the re-underwrite — DONE below. Thesis half is NOT mine and is routed.
>
> **✅ (1) STRIKES ARE FINE — MY STALENESS HYPOTHESIS WAS WRONG, RECORDED AS WRONG.** USO has run **115.96 (8/4) → 125.63 (8/14) → 130.67 (8/18)**, and I expected to find strikes locked to a stale level. **They are not:** ZONE-1 specifies the ladder as *"LOGIC, not locked — long leg ~ATM-to-5% OTM **of the post-gap USO print**, short leg ~10–15% further OTM."* **Relative to the fire-day print, so USO's ~+12.7% run since 8/4 does not touch it.** The card was built correctly on this axis and I am not manufacturing a defect out of a hypothesis that failed.
>
> **✅ (2) FIRE LOGIC ALREADY SURVIVES WALTER'S OBJECTION — the inversion did this work on 7/18.** AIS/PortWatch is **veto-only and can never CAUSE a fire**; the primary is a dark-fleet-capable corroborator. So *"the count is unmeasurable"* cannot produce a false ARM here. **No change needed.**
>
> **⚠️ (3) THE VOL BASE MOVED A LOT — a NOTE, not a defect, and the distinction matters.** At build: **OVX ~61 / VIX ~18** (RED 7/17 13:09), cited as **OVX p93** + ratio p96.8 (VIOLET KB-VIO-120). Today: **OVX 47.81 (−9.66% on the day) / VIX 15.72**, ratio **3.04**; in a **120-day** window OVX 47.81 sits at the **11th percentile** (min 40.33 · median 68.45 · max 120.91). ⚠️ **NOT a like-for-like percentile comparison — my window is 120d and the card's p93 is VIOLET's KB-VIO-120 measurement on a window I have not matched. The unambiguous facts are the LEVEL (~61 → 47.81, −21.6%) and that both readings point the same way.**
> ✅ **The "spread is MANDATORY" mandate STANDS and is NOT invalidated** — it is conditioned on **fire-day** vol (*"a strand gaps it higher"*), which is unknowable today and elevated by construction on a strand. **My second hypothesis also failed and is recorded as failed.**
> 🔑 **What DOES change is the ECONOMICS, and this is the one live construction finding:** the short leg exists to offset *"the vol-rich premium you're paying."* **Starting a gap from a p11 vol base instead of p93, that premium is materially cheaper, so the short leg gives up more upside per dollar of premium it saves.** ⇒ **At fire, re-test spread-vs-outright on the live post-gap chain rather than treating the mandate as settled.** The card already says to re-anchor at fire; this names WHAT to re-test and WHY.
>
> **🔴 (4) OPEN ITEM ROUTED, NOT DECIDED — retire vs extend is NOT TERRY's call.** The premise (*is a Kharg strand still live?*) belongs to **RED / BRENT / FALCON**, and the retire/extend decision is **Will's**. ⛔ **I have NOT extended this card by writing this block** — an anti-rot clause that a construction desk silently renews is not a clause. **It stays ARMABLE with the day-32 trigger recorded as FIRED-AND-UNRESOLVED until Will rules.**
>
> ### Consumed here: WALTER `SIG-W-20260818-001` + `-002`
> - **`-001` (MOU expired 8/17, no deal, Trump will not extend):** the thesis invalidation is *"de-escalation confirmed (Muscat/Article-5 executes) → loadings resume → RETIRE."* **Every clause moved FURTHER AWAY.** RED's ~5–10% de-escalation branch is, if anything, thinner. ✅ **Premise intact on that axis.** ⛔ *An invalidation moving away is NOT an entry signal* (WALTER says this itself, and `RISK_RULES` #15 is the reason).
> - **`-002` (four instruments give 0/3/5/12 Hormuz transits for one day):** 🔴 **INSTRUMENT CONFLATED — transits are NOT loadings, and this card bans the former BY NAME.** ZONE-1 already reads *"do NOT anchor the trigger on the Hormuz transit count"* under PROME's 7/17 denominator ruling (a ≤18/day print fires on **86.6% of ALL crisis days**), and *"a collapsed transit count is NOT a collapsed export volume"* — the Oman bypass + STS move crude without appearing in chokepoint counts. **This card grades KHARG EXPORT LOADINGS, a different quantity.** ✅ **BUT THE CLASS-LEVEL POINT SURVIVES AND I AM NOT NITPICKING IT AWAY:** the loadings series (PortWatch `port2164` `export_tanker`) is **also AIS-derived** and shares the same **~90% dark-fleet blindness**, so the impeachment reaches it.
> - **🔑 AND THE BIAS DIRECTION PROTECTS THE RETIRE CLAUSE, which is the opposite of the alarm:** AIS **under**-counts ⇒ it will not falsely show *"loadings resumed"* ⇒ **a FALSE RETIRE is unlikely.** The real residual is the mirror — **FAILURE to retire**: loadings genuinely resume, AIS stays blind, and the card rides a dead premise. ⭐ **The backstop for exactly that is the ~30-day re-underwrite clause — which is the thing that just came due.** The card's two defences are correctly paired; only the invocation was late.

### Invalidation / kill / confirm
- **Invalidation (thesis):** de-escalation confirmed — the Muscat/Oman Article-5 safe-passage mechanism executes (RED estimates this branch **~5–10%**) → Kharg loadings resume, the supply-loss premise dies → **RETIRE the card.**
  > 🔧 **RE-SPEC'D 2026-08-18 (TERRY) — the July inversion fixed the FIRE side of this instrument and left the RETIRE side standing. A guard fixed on one side reads exactly like a guard on every side.**
  >
  > **The general form, which the 7/18 inversion implied but never stated: the AIS bias is ONE-DIRECTIONAL (it under-counts), therefore ⇒ a NONZERO print is TRUSTWORTHY and a ZERO print is WORTHLESS — in BOTH directions of use.**
  >
  > | AIS/PortWatch print | on the FIRE side | on the RETIRE side |
  > |---|---|---|
  > | **NONZERO / recovering** | ✅ **strong — VETOES a fire** (flow is demonstrably continuing) | ✅ **strong — SUFFICIENT to retire.** If the ~90%-blind instrument can *see* loadings, they are genuinely there. |
  > | **ZERO / no visible loadings** | 🔴 **worthless — can NEVER cause a fire** (it prints zero in normal months: Jan/May/Jul-2026) | 🔴 **worthless — can NEVER keep this card alive.** |
  >
  > 🔴 **THE RESIDUAL THIS CLOSES — "FAILURE TO RETIRE":** the old wording let a **zero print** function as implicit evidence the strand persisted, so loadings could genuinely resume while the card rode on a dead premise. **Absence of visible resumption is NOT evidence of continued strand.** ⇒ **RETIRE grades on: a nonzero/recovering AIS print, OR any dark-fleet-capable corroborator (Kpler/Vortexa/official statement) — and NEVER on the absence of one.**
  > ⚠️ **Because the retire trigger can therefore be SILENT (the instrument may simply never show it), the dated clock below is not hygiene — it is this clause's only backstop.**
- **Kill line (post-fill):** a confirmed resumption of Kharg loadings to normal (bypass absorbs / seizure reversed) → exit; and standard time-stop — the inventory-draw grind should be visible within the tenor, no draw-through-buffers by ~half the DTE = thesis not confirming.
- **Confirm line (go/hold):** loadings stay stranded AND Cushing/SPR buffers visibly draw (HEARTBEAT dashboard) AND war-risk-freight stays elevated → the supply-loss is real and compounding, hold to target.
- ~~**Retire if unfired at ~30d** → re-underwrite~~ 🔴 **FIRED 2026-08-16 (day 30), GRADED LATE ON DAY 32 — see the day-32 block above.**
  > 🔧 **CLAUSE RE-SPEC'D 2026-08-18: `~30d` IS NOT A CLOCK AND THAT IS WHY IT DRIFTED.** A tilde has no fire date, so nothing can be late against it and no boot check can flag it. **Replaced by a REAL DATE:**
  > **`RE-UNDERWRITE DUE: ________`** — ⛔ **left BLANK deliberately: the date is set at Will's retire-vs-keep ruling and is not TERRY's to pick.** If the card is kept, this line carries **one absolute date** (never "~Nd"), and reaching it **without a written grade is itself the defect**, not merely a prompt.
  > **Durable form:** *a self-destruct clause needs an absolute date; a relative one cannot fire, and cannot be measured as late.*

### §9 Concentration (aggregate the shared-falsifier book — REQUIRED read before ARM)
> 🔴 **§9 IS STALE AND IT IS THE ONE SECTION THAT MUST NOT BE — TERRY 2026-08-18 EVE, surfaced by Will asking "is this just adding another USO position?"**
>
> **The section below prices the falsifiable oil cluster as *"USO oil-long (20 sh) + this ~$200 tail"* ≈ **$1,350**. That book no longer exists.**
>
> | | §9 as written (7/17) | actual, 8/18 post-close (USO **130.66**) |
> |---|---:|---:|
> | USO shares | **20** | **35** |
> | other oil legs | none | **135C ×2 $1,210 · XLE 65C ×2 $194 · Sep-18 sprd $85** |
> | cluster + a new $200 tail | **$2,813** | **$6,262** |
> | | | ⇒ **2.23× what the guard describes** |
>
> ⚠️ **This is the section the card itself labels "REQUIRED read before ARM" — so the guard a future session would consult before firing is measuring a book roughly HALF the real size.** A stale concentration guard does not fail loudly; it **passes**, which is worse (`[[finding_standing_guard_is_a_false_negative_risk]]`).
>
> **Three things it gets wrong now, beyond the total:**
> 1. **"Dies on de-escalation: USO oil-long (20 sh) + this ~$200 tail"** — the dying set is now **four legs**, and per BRENT's 8/14 measurement **`N_eff = 1` VIEWS**: every oil leg shares the one falsifier. Firing this card makes it **five expressions of one view**, not a diversifying add.
> 2. **"This card is the smallest, most defined-risk leg of the cluster"** — ✅ **still TRUE** ($200 defined vs 35 undefended shares) and it remains the **only leg built to pay on the STRAND path the others miss**. That argument survives and is the strongest thing left in favour of the card.
> 3. ⚠️ **NEW, and it did not exist on 7/17: Will ruled HOLD on the USO shares 2026-08-18 with NO exit rule and the round-trip explicitly accepted.** The book is now **committed to oil without a defined exit**, which **raises the bar for adding a fifth correlated leg** — `RISK_SCORING` §2b: *the combined exposure is the number that matters.*
>
> ⇒ **CONSTRUCTION VERDICT (not a thesis verdict, not a decision): a re-arm cannot reuse §9 — it requires §9 RECOMPUTED on the live book.** ⛔ **Which means "extend" is not actually available as a cheap option: the honest choices are RETIRE, or REBUILD (new card, fresh §9, fresh chain).** Recorded for Will's retire-vs-extend ruling and routed to BRENT with the premise question.

**🔒 RE-LOCKED 2026-08-18 EVE (TERRY). Live book, USO 130.66 post-close.** This deepens the **one-Mideast-bet**. The shared falsifier is a **Hormuz de-escalation** (Muscat/Article-5, RED ~5–10%), which fires on multiple book legs at once.

| Dies on de-escalation | value | risk shape |
|---|---:|---|
| USO **35 sh** | **$4,573** | 🔴 linear, **UNDEFENDED — Will ruled HOLD 8/18 with NO exit rule** |
| USO **Oct-16 $135C ×2** | $1,210 | defined; ⚠️ **no management rule** (#9 violated on that leg) |
| USO **Sep-18 150/165 ×1** | $85 | defined, ~spent |
| **XLE Sep-30 $65C ×2** | $194 | defined, ~spent |
| **this card, if fired** | **$200** | defined |
| **TOTAL falsifiable oil cluster** | **$6,262** | **vs the $2,813 the 7/17 text assumed = 2.23×** |

- **Survives de-escalation:** `TRY-FIRE-004`'s **real-yield / term-premium leg** — NEXUS/RED grade it independent of oil (10Y held ≥4.50 *through* a deflationary June print). ⛔ **Do NOT double-count it as "shared."**
- 🔴 **`N_eff = 1` VIEWS, not 4 legs** (BRENT 8/14, verified by TERRY): **every** leg above dies on the **one** falsifier. **Firing this card makes it a FIFTH expression of a single view** — `RISK_SCORING` §2b: *the combined exposure is the number that matters, and it is stated as one number here precisely so it cannot be read as five trades.*
- ✅ **What still argues FOR the card, kept because it survived the recompute:** it is the **smallest and most defined-risk leg** ($200 vs 35 undefended shares) and **the only one built to pay on the STRAND path the others miss** — the rest are riding a **risk-premium repricing on a diplomatic clock**, not a confirmed supply loss.
- ⚠️ **Arming bar RAISED vs 7/17, and say so at the ticket:** the base this sits on has **doubled**, and the largest leg now has **no exit rule by explicit ruling**. `RISK_RULES` #17 — **the size-INCREASING branch carries the higher evidential burden.**

> *Superseded 7/17 text, kept so the drift is dateable:* ~~"Dies on de-escalation: USO oil-long (20 sh) + this ~$200 tail … Aggregate … ≈ $1,350."~~ **The book grew ~2.2× underneath a pre-locked guard that nobody re-read — which is the failure mode ZONE 1 exists to prevent, arriving inside ZONE 1 itself.**

> ### 🔒 ANTECEDENT GATE — the shared falsifier CANNOT grade as fired on price action alone
> **Added 2026-07-27 (BRENT recommendation, PROME endorsed) after the book came within one relay of walking into exactly this trap.**
>
> **The defect:** the falsifier's **antecedent** is *"fast Hormuz de-escalation."* Its **observable legs** are *"oil retraces AND bonds rally."* Anyone grading off the **legs** without first establishing the **antecedent** reads an ordinary premium unwind as a fired falsifier — and de-risks the whole book on it.
>
> **This is not hypothetical. It nearly happened on 2026-07-27:** Brent fell **−6.8%** and TLT rallied on a *two-night pause* in the US-Iran strike campaign. Both legs "fired." The coordinator relayed it to Will as *"splitting, oil leg firing."* **BRENT ruled that categorically wrong — the antecedent never happened:** Hormuz still closed, transits still down ~17%, naval blockade still in effect, no deal, no signature. A suspension is not a de-escalation.
>
> **The gate, binding on this card and on every leg of the shared-falsifier cluster:**
>
> > **The Hormuz-de-escalation falsifier may NOT be graded as fired unless ≥1 PHYSICAL de-escalation leg confirms FIRST:**
> > 1. **Transits sustained >~35/day** (not a single print — sustained)
> > 2. **War-risk premium halves**
> > 3. **P&I / war-risk resumption notice** issued
> > 4. **Signature or sovereign action** (Muscat/Article-5 mechanism actually executes)
> >
> > **Price action alone must NEVER trigger it.** Oil down + bonds up, with no physical leg confirmed, is a **premium unwind** — which is *reversible* and is precisely what this card is built to survive. Grading it as the falsifier inverts the card into selling the strand path at its cheapest.
>
> **Why this belongs on the CARD and not just in a memo:** the falsifier is what a future session grades *under time pressure*, often without re-reading the thesis. The legs are the observable part, so the legs are what get graded. Naming the antecedent as a **hard precondition** is the only form that survives a fast read. *(Full reasoning: `AGENTS/BRENT/outbox/2026-07-27_to-PROME_oil-collapse-adjudication.md`.)*
>
> **Scope:** this gate governs the *de-escalation* falsifier only. The card's own **kill line** (confirmed resumption of Kharg loadings to normal) is a **physical** observable and is unaffected — it was already correctly specified.

### Alternatives rejected (named once)
Naked calls (vol tax) · shares (no convexity, already held) · long-dated calls (wrong tenor) · Hormuz-transit-anchored trigger (86.6% base rate, transit≠volume) · pre-buy now (Will chose pre-build; the $87/OVX-61 tape is a chase per BRENT's valid vol-rich argument).

### ✅ OPEN DEPENDENCY — DISCHARGED 2026-07-18 (FALCON froze the source; GATE-TERRY-006 LIVE)
~~The trigger needs a Kharg-EXPORT-loadings data source…~~ **RESOLVED.** FALCON investigated (`AGENTS/FALCON/domain/KHARG_LOADINGS_SOURCE.md`): the PortWatch `port2164`/`export_tanker` series exists but is **AIS-based, ~90%+ dark-fleet-blind** (prints ZERO in normal months) → **disqualified as a trigger, repurposed as the refuting veto.** The card is now **corroborator-anchored** (see the inverted Trigger condition above) and is **ARMABLE the moment a dark-fleet-capable corroborator fires** — no structural rework, one trigger inversion. GATE-TERRY-006 registered LIVE by PROME 2026-07-18. **TERRY confirmed 2026-07-20: card wording is consistent with the registered GATES condition (fire = ≥1 dark-fleet-capable corroborator, ≥2 days, not vetoed) — no contradiction.** Still gated on Will [Approve] + live broker book at fire (rule #4/#5); $200 fenced from 004's $500.

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
- **Broker position truth:** existing USO exposure — ⛔ **DO NOT fill from memory or from this card.** Run `python3 AGENTS/TERRY/scripts/positions_from_forge.py` and copy what it returns, or mark `[POSITION_STATE_UNKNOWN]`.
  > 🔧 **FIXED 2026-08-18: this line said "(20 sh + any calls)" — the 7/17 figure, wrong since at least 8/02, sitting in the FIRE-TIME checklist.** Worse than the same error in §9, because **this is the line somebody fills in at the ticket while the tape is moving**, and a familiar-looking wrong number is the kind you tick rather than check.
  > ⭐ **THE PATTERN FIX, not just this instance: ZONE 1 and ZONE 2 must NEVER HARDCODE A POSITION FIGURE. Point at the live source instead.** A hardcoded number in a pre-locked layer is a **guaranteed future defect** — the layer's whole purpose is that it is written once and read much later, so any figure in it decays by construction while looking authoritative. *(Both rot instances found today, 7/17 → 8/18, were hardcoded counts.)*
- **Spread-vs-outright RE-TEST (added 2026-08-18) — do NOT treat "spread is MANDATORY" as settled at fire:** the mandate was written at **OVX ~61 (p93)**; on **2026-08-18 OVX was 47.81**, the **11th percentile of a 120-day window** *(⚠️ not like-for-like against the card's p93 — different windows; the unambiguous fact is the level, −21.6%)*. **A gap starting from a low vol base makes the premium you are offsetting materially cheaper, so the short leg gives up more upside per dollar it saves.** ⇒ **Price BOTH the spread and the outright on the live post-gap chain and write which won, with the numbers.** ⛔ **This is a re-test instruction, NOT a relaxation — if the vol is rich at fire the mandate stands, and `RISK_RULES` #14 says this is a MOMENT property graded ONCE, at fire.**
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

**ZONE-3 decision line — 🔴 VOID. Never filled, never will be: card RETIRED 2026-08-18 before any fire.**
> *(Original fill-in, restated in lowercase so a dead template cannot impersonate a live claim: it offered the three verdict options — clean, conditional, no-trade — **in the live claim's own syntax**, which is the defect itself. History preserved; only the syntax is broken.)*
> ⚠️ **Latent ambiguity, surfaced by the retirement and worth carrying forward:** this line is a **fill-in TEMPLATE**, but it is formatted *identically to a live verdict claim*, so `ledger_sweep` check C read it as the card declaring `NO_TRADE` against a `RETIRED` header. **It stayed invisible for 32 days only because the header happened to say `CONDITIONAL`, which the template list contains** — the moment the header moved to a state the template does not list, a template started arguing with a claim. *(`[[finding_a_file_that_examples_its_own_structure_is_ambiguous]]` — a template quoting its own structure is indistinguishable from an assertion of it.)* **⇒ Fill-in option lists in future cards must not use the live claim's own syntax** — bracket them, or the guard will eventually read the menu as the order.
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
