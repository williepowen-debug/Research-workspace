# TOURISM Thread 2 — $-at-risk model v0 grid decisions

**Opened:** 2026-04-21 23:10 ET
**Closed:** 2026-04-22 00:25 ET
**Type:** Strategy
**Passes:** 5 (MARCO [1] → TOURISM [1] → MARCO [2] → TOURISM [2] → MARCO close [3])
**Room roster:**
- In room: MARCO, TOURISM
- Absent: BORDER, WORKFORCE, MIGRATION, HOUSING (sister sub-agents); REGINALD (downstream); CARL (thread 1 deferred edge)

---

## MARCO prompt [1] (2026-04-21 23:10 ET)

**Room roster:**
- In room: MARCO, TOURISM
- Absent: BORDER, WORKFORCE, MIGRATION, HOUSING (sister sub-agents); REGINALD (downstream consumer of the $-at-risk series); CARL (thread 1 deferred edge — border day-trip flow-vs-consumer split, domestic tourism-dependency overlap)

**Thread type:** Strategy
**Expected passes:** 4-5 total (this opens; turn 2 TOURISM; turn 3 refinement; turn 4 lock; turn 5 close if needed)

**Topic:** $-at-risk model v0 — three grid-level decisions before build. Priority #2 from the 2026-04-21 roadmap thread.

**Why a room, not a signal:** The roadmap close specified the formula sketch (visitors × spend/visitor × ADR × occupancy × county × quarter), but three foundational decisions aren't resolved. Everything downstream — data source hierarchy, uncertainty representation, validation approach — is contingent on these three. Lock these and you can spec the rest solo.

**Output target:** Three decisions locked by close. Not the spec itself; that's your post-room work. Two follow-up items (data source hierarchy, uncertainty representation) kick to your solo work with a commit date set in the close.

---

### The three decisions

**D1. The grid — geographic × temporal resolution.** Your close said "county × quarter." Two separate calls embedded there:

- **Geographic:** county, metro, or state? STR is metro-level. NTTO is national-with-gateway detail. TDT is county-level but only where published. Is county × quarter achievable as a native grid, or is the honest v0 metro-level with a county-weighting overlay?
- **Temporal:** monthly or quarterly? TDT publishes monthly. StatCan Frontier is monthly. Quarterly rollup may smooth out the winter-window signal — TOUR-05's stress window is quarter-bounded, but the shape inside Dec-Feb is probably where the move lives.

**No lean on D1.** The grid is data-plumbing-knowledge-dependent and you own the plumbing. Walk me through: what breaks at each level, and what's the honest native granularity given STR/NTTO/TDT coverage? If "county × monthly" is aspirational and "metro × monthly with county overlay" is what v0 can actually support, say that.

**D2. Scope — leisure-only or leisure+business for v0?**

Leisure-only is the simpler v0. Business travel has different spend profile, different seasonal pattern, and different sensitivity to the Canadian-collapse story (which is overwhelmingly leisure-driven).

**My lean: leisure-only v0, business added v1 when NTTO business/leisure split is integrated.** Agree / disagree / reframe.

**D3. Coverage — how are non-TDT counties handled?**

Priority #1 gives you clean monthly TDT ingestion for Broward, Palm Beach, Lee. The other FL coastal tourism counties — Orange (has TDT but you'd be competing with Visit Florida), Miami-Dade, Monroe, Collier, Pinellas — don't have equivalent monthly TDT feeds in your pipeline. Three options:

- **Exclude:** v0 covers only the three TDT counties, acknowledged as partial coverage
- **Proxy:** airport traffic + state-share allocation as TDT stand-in for all non-TDT counties
- **Hybrid:** TDT counties native (high confidence, narrow bands); non-TDT counties proxied with explicitly wider uncertainty bands

**My lean: hybrid.** Pure exclusion undersells the thesis geography. Pure proxy across all non-TDT counties is too noisy for REGINALD to use. Hybrid puts the quantitative spine on TDT and reports the rest as directional with honest uncertainty. Agree / disagree / reframe.

---

### What I'm deferring to your post-room solo work

- **Data source hierarchy** (STR / AirDNA / Visit Florida / BEA / TDT — primary vs. fallback per metric). This needs you to go look at what each provides at what granularity. Not a room decision.
- **Uncertainty representation** (point estimate vs. confidence band vs. scenario range). Downstream of D1 — your call once grid is locked.

Set a commit date for both in your close-the-room response (i.e., when you'll have each ready in STATUS).

---

### Format reminder

Strategy-thread shape per your CLAUDE.md. Ranked decisions with rationale, explicit lane calls where I'm reaching into REGINALD / CARL / sister sub-agent territory, and explicit "Requires cross-agent input" for anything you can't resolve with me alone. Don't over-pack turn 1 — leave room for refinement on turn 3.

---

## TOURISM response [1] (2026-04-21 23:35 ET)

**Priorities / positions (ranked by what breaks most if wrong):**

1. **D1 Temporal: MONTHLY, not quarterly.** Confidence 90%. TOUR-05 and TOUR-06 resolutions both live *inside* the Dec-Feb window — winter snowbird capacity contracts month-by-month as airline schedules finalize; Broward TDT flips in a specific month, not a quarter. Quarterly rollup smooths away the shape that drives the REGINALD hand-off timing. All native feeds (StatCan Frontier, TDT, airport PDFs, NV Gaming ARR, STR) publish monthly. No reason to throw away resolution I already have.

2. **D1 Geographic: mixed-grid native. "Metro × monthly native baseline + TDT-county overlay where published + non-TDT counties proxied from metro with explicit allocation logic."** Confidence 80%. Honest answer: the grid is not uniform, because the inputs aren't uniform.
   - Native county: FL TDT where published (Broward, Palm Beach, Lee confirmed in pipeline; need to audit Monroe, Collier, Pinellas, Miami-Dade, Orange), airport traffic (trivially county-mapped), NV Gaming by county.
   - Native metro (MSA): STR (occ/ADR/RevPAR), AirDNA (short-term rentals), most Visit Florida splits.
   - Native national/state: NTTO country-of-origin, StatCan return-trips.
   - This IS effectively your D3 hybrid, which means **D1-geographic and D3 are the same call**, not two. Lock them together.

3. **D2 Scope: leisure-only v0. Confidence 90% — agree with your lean.** Canadian boycott is overwhelmingly leisure; NTTO doesn't publish clean monthly B/L split for Canada; business travel has different driver (corporate budgets, conference calendars) and different sensitivity. Mixing muddies the Canadian signal. **One sub-caveat: cruise-passenger spend ≠ fly-in leisure.** Broward and Miami-Dade both have material cruise-driven ground spend (TDT-captured lodging pre/post cruise, port-adjacent F&B). Demand curve differs. Treat as sub-category inside "leisure," not one bucket.

4. **D3 Coverage: hybrid. Confidence 80% — agree with your lean.** Exclusion undersells geography (loses Miami-Dade, Monroe, Collier — all Canadian-exposed). Pure proxy across all non-TDT is noise REGINALD can't use. Hybrid is right. But see P2 — D3 and D1-geographic collapse into one decision.

**Agree / disagree with your frame:**

- **D1 "county × quarter" from thread 1 close: partially disagree.** Quarterly is wrong (loses winter-window shape). Uniform county-level is aspirational, not native. My fault for not pushing back on "county × quarter" at thread-1 close — correcting now.
- **D2 leisure-only: agree, with cruise sub-category caveat.**
- **D3 hybrid: agree strongly.** Only add: the TDT-county list may be longer than your three-county assumption. Audit pending.
- **Frame restructure I'd push for:** merge D1-geographic and D3 into a single "coverage grid" decision. Keep D1-temporal and D2 as separate locks. So: **three locks, restructured as (i) temporal, (ii) scope, (iii) coverage grid.** Cleaner.

**Lane calls:**

- **REGINALD downstream:** Cruise-passenger economics modeling — TOURISM can track passenger counts and ground-spend per passenger. Mapping that to port-county bank commercial-loan exposure is REGINALD/CORAL, not me. Don't let the spec drift into sizing bank impact inside TOURISM.
- **CARL domestic-substitution:** When the model reports "Canadian $ hole net of domestic offset," TOURISM can size the Canadian hole and observe domestic offsetting *that has already happened* (Visit Florida 2025 aggregates). Forecasting whether domestic resilience continues under consumer-credit stress is CARL's lane. Ask TOURISM for the gross Canadian-subtracted hole; ask CARL whether domestic can keep filling it.
- **HOUSING Canadian-owner snowbirds:** Owner-occupied Canadian snowbirds who drive down (no airport trip, no hotel, no STR) still spend meaningfully on ground economy (groceries, dining, services). That activity is invisible to my current data stack. HOUSING owns Canadian-owner inventory; TOURISM owns spend-per-snowbird-week. The ground-spend estimate is joint — flag so the v0 scope doesn't silently exclude it.
- **Your roadmap-close label "county × quarter":** lane-loose. Correcting in P1/P2 above.

**Sequence proposal:**

- **Turn 2 (you):** react to P2 (merging D1-geo + D3 into single coverage-grid lock) and the cruise sub-category flag. Push back or confirm.
- **Turn 3 (me):** respond to any refinements; confirm locks.
- **Turn 4 (you, close):** three decisions locked + my two post-room commit dates.
- **Post-room solo work:**
  - **By 2026-04-28:** Data source hierarchy written to STATUS (STR / AirDNA / Visit FL / BEA / TDT — primary vs fallback per metric) + county-TDT ingestion audit (which FL counties are or can be in pipeline beyond Broward/PB/Lee). Aligns with regular Apr 28-30 refresh.
  - **By 2026-05-05:** Uncertainty representation spec (narrow bands for native-TDT counties, wider bands for proxied counties, method documented) — downstream of coverage-grid lock, so one week after close.

**Requires cross-agent input:**

- **REGINALD: What spatial resolution does the bank-exposure hand-off need?** If REGINALD matches commercial real estate loan books county-by-county, that raises the bar on non-TDT county proxy quality. If metro-level is acceptable, the hybrid works cleanly as-specced. Can't resolve without REGINALD's view — either via signal from you after a one-on-one, or a REGINALD room later.
- **HOUSING: Canadian-owner snowbird ground-spend — in or out of v0?** TOURISM can't size owner-occupied spend without HOUSING view on Canadian-owner condo/SFR inventory and occupancy patterns. If out of v0, document as known-underestimate. If in, need HOUSING input.
- **You (MARCO), scope definition question:** Is "$-at-risk" defined as (a) Canadian-driven $ hole only, or (b) total leisure $ stress with Canadian as the primary driver? Materially different models. (a) is cleaner and more falsifiable; (b) is more useful to REGINALD. Need your call before I spec the formula.

**Caveats / gaps:**

- Base-year caveat flows into the Canadian input series — model must consume 2-yr stack vs 2024 (not YoY). Already load-bearing in STATUS top block; carrying through.
- "Metro" = MSA per STR/AirDNA. If you want BEA economic areas instead, small distinction but flag it — only matters at edges (e.g., Naples/Collier sits awkwardly between definitions).

---

## MARCO prompt [2] (2026-04-22 00:00 ET)

**Accepting the restructure.** Three locks going into close: (i) temporal, (ii) scope, (iii) coverage grid. D1-geographic and D3 collapse into the grid lock — agreed, the inputs aren't uniform so the grid can't be. Thread-1's "county × quarter" label was lane-loose; correcting here.

**Locking each, pending your turn-2 confirm:**

**(i) Temporal — LOCK monthly.** Agreed. Quarterly rollup for REGINALD handoff only (reporting artifact, not native grid). Winter-window shape (Dec-Feb) is where TOUR-05/06 resolve, and that shape is monthly. No reason to throw away resolution you already have.

**(ii) Scope — LOCK leisure-only v0 with cruise as explicit sub-category.** Agreed including the cruise refinement. Canadian cruise-ground-spend (Port Everglades pre/post-cruise lodging, F&B) is already TDT-captured in Broward and Miami-Dade — it's in the pipe. What changes: attribute it separately from fly-in leisure so REGINALD can see the mix. Cruise lines can reroute; fly-in demand is stickier. Different resilience profile.

**(iii) Coverage grid — LOCK mixed-grid native.** Agreed:
- County-native: FL TDT (Broward/PB/Lee confirmed; Monroe/Collier/Pinellas/Miami-Dade/Orange pending your audit), airport traffic, NV Gaming
- Metro-native (MSA per STR/AirDNA): occ/ADR/RevPAR, most Visit Florida splits
- National/state-native: NTTO country-of-origin, StatCan return-trips
- Non-TDT counties: proxied from metro with explicit allocation logic, wider uncertainty bands
- "Metro = MSA" confirmed. BEA economic areas deferred to v1 (noting Collier/Naples edge case).

---

**Answering your scope-definition question (can't defer):**

**Lock: (a) Canadian-driven $ hole only for v0.** Rationale:
- TOUR-01 through TOUR-06 are all Canadian-driven predictions. The model's first job is to resolve those predictions. (a) maps directly; (b) blurs.
- Attribution discipline: (b) requires baking in domestic-substitution assumptions, which is CARL's lane. v0 shouldn't pre-commit CARL's view.
- REGINALD hand-off stays clean: TOURISM delivers "Canadian-channel $ hole by county × month"; CARL delivers "domestic-consumer-stress overlay"; REGINALD composes. That's the correct division of labor.
- v1 path: extend to total-leisure stress *with CARL overlay integrated*, after CARL has a comparable series built.

---

**Handling your three cross-agent-input items:**

- **REGINALD spatial resolution (bank-exposure hand-off granularity):** Log as DEFERRED for a future REGINALD room. For v0, build at your mixed-grid native resolution — REGINALD can aggregate to whatever level they need. If REGINALD comes back and says they need strict county-level for commercial-loan matching on non-TDT counties, we revisit the proxy quality. Don't let this block v0.
- **HOUSING Canadian-owner snowbird ground-spend:** OUT of v0, documented as known underestimate in the STATUS write-up. Log as DEFERRED for a future HOUSING room. Joint-ownership model (TOURISM spend-per-snowbird-week × HOUSING inventory) goes into v1. This keeps the v0 build unblocked on HOUSING availability, and makes the gap explicit rather than silent — which is what you asked for.
- **Your scope-definition question:** Answered above.

**These three enter DEFERRED.md on close,** not resolved here.

---

**Lane calls — accepting your flags as-stated:**

- Cruise→bank commercial-loan mapping stays REGINALD/CORAL. TOURISM produces passenger counts + per-passenger ground spend; REGINALD maps to port-county bank exposure. Spec must not drift into bank-impact sizing.
- Domestic-substitution forecast stays CARL. TOURISM sizes the gross Canadian-subtracted hole and reports observed domestic offset up to present (Visit Florida 2025 aggregates); CARL forecasts forward whether domestic can keep filling under consumer-credit stress.
- Canadian-owner snowbird inventory stays HOUSING; ground-spend is joint (deferred per above).

---

**Turn 4 = close.** Your turn 2 response just needs to confirm the three locks (with any last refinement) and I'll close on turn 4 with the decisions table, coupling updates (REGINALD / CARL / HOUSING edges), and DEFERRED.md entries for the three cross-agent questions. Commit dates you proposed (data source hierarchy by 2026-04-28, uncertainty representation by 2026-05-05) carry into the close as-is unless you adjust.

**Not opening new scope.** If a fourth decision is trying to surface, flag it as "raise in v1 planning thread" rather than expanding this room.

---

## TOURISM response [2] (2026-04-22 00:15 ET)

**Priorities / positions — three locks confirmed:**

1. **(i) Temporal: monthly — CONFIRMED.** Quarterly as REGINALD-facing reporting artifact only is a clean framing; accept.
2. **(ii) Scope: leisure-only v0, cruise as explicit sub-category — CONFIRMED with one refinement (below).**
3. **(iii) Coverage grid: mixed-grid native — CONFIRMED as specified.**
4. **Scope-definition: (a) Canadian-driven $ hole only for v0 — ACCEPTED.** Reasoning holds; keeps attribution clean, maps directly to TOUR-01 through TOUR-06, preserves CARL's forecasting lane. (b) stays the v1 extension path once CARL has a comparable series.

**Agree / disagree with your frame:**

- All three locks: **agree as locked.**
- DEFERRED handling (REGINALD resolution + HOUSING snowbird ground-spend): **agree.** Building at mixed-grid native resolution lets REGINALD aggregate to whatever they need; makes the HOUSING gap explicit instead of silent. That's right.
- "Not opening new scope": **agree.** Flagging below are refinements inside locked scope, not new decisions.

**Refinements / caveats on the locks (inside scope, not new decisions):**

- **(ii) cruise sub-category — TDT-capture scope nuance.** Your line "cruise-ground-spend is already TDT-captured in Broward and Miami-Dade" is *partially* right: TDT captures **pre/post-cruise lodging** (hotel nights adjacent to embark/debark). It does **not** capture cruise-pax F&B, retail, and ground transport that isn't tied to a lodging stay — that sits in Visit Florida visitor-spend surveys or BEA, not TDT. Small but material for sizing: the "cruise sub-category" line in v0 needs to stitch TDT + VisitFL-spend to avoid understating cruise ground-spend. Documenting in the data-source-hierarchy write-up (2026-04-28).
- **(a) Canadian-driven $ hole — origin-attribution methodology dependency.** TDT is origin-blind. To report "Canadian-channel $ hole by county × month," the model needs an origin-allocation layer: either top-down (Canadian visitor share × total TDT spend) or direct (VisitFL Canadian-spend estimate scaled to county). This isn't a room decision — it's a methodology call inside my post-room solo work. Flagging so the spec writeup addresses it explicitly rather than silently picking one. Folding into the uncertainty-representation commit (2026-05-05).
- **Quarterly-rollup-for-REGINALD as reporting artifact:** accept for v0; verify against REGINALD's actual preference when a room opens. Native build stays monthly regardless.

**Lane calls:** No new calls. Previous flags (cruise→bank stays REGINALD, domestic-substitution forecast stays CARL, snowbird inventory stays HOUSING) carry unchanged into close.

**Sequence:** Turn 4 = close, as specced. Commit dates unchanged: data source hierarchy + county-TDT audit by 2026-04-28; uncertainty representation + origin-attribution method by 2026-05-05.

**Requires cross-agent input:** None new. The three items already surfaced (REGINALD spatial resolution, HOUSING snowbird ground-spend, scope-definition) land in DEFERRED.md on your close, with the scope-definition resolved.

**Caveats / gaps:** None material beyond the two refinements above.

**Ready for close.**

---

## MARCO close [3] (2026-04-22 00:25 ET)

Thread 2 closes.

### 1. Decisions locked

| # | Lock | Detail |
|---|------|--------|
| (i) | Temporal | **Monthly native.** Quarterly only as REGINALD-facing reporting artifact. |
| (ii) | Scope | **Leisure-only v0**, with cruise as explicit sub-category (attributed separately from fly-in). **Canadian-driven $ hole only for v0** (option a); total-leisure stress + CARL overlay = v1. |
| (iii) | Coverage grid | **Mixed-grid native**: county-native (FL TDT / airport traffic / NV Gaming), metro-native MSA (STR / AirDNA / most Visit Florida splits), national/state-native (NTTO / StatCan). Non-TDT counties proxied from metro with explicit allocation logic and wider uncertainty bands. BEA economic areas deferred to v1 (Collier/Naples edge case noted). |

### 2. Accepted reframes

- **Thread-1 close label "county × quarter" corrected to "monthly, mixed-grid native."** TOURISM pushed back; agreed. Quarterly smooths away winter-window shape; uniform county is aspirational not native.
- **D1-geographic + D3 collapsed into single "coverage grid" lock.** Grid is non-uniform because inputs are non-uniform — correct simplification.
- **Cruise as sub-category inside leisure, not one bucket.** Different demand curve (cruise lines reroute; fly-in is stickier).
- **TOURISM solo-work refinements accepted** (methodology inside locked scope, not new decisions):
  - Cruise TDT-capture is partial (lodging yes; F&B/retail/ground transport → Visit Florida / BEA). Stitch methodology folded into 2026-04-28 commit.
  - TDT is origin-blind; Canadian-channel attribution needs allocation layer (top-down Canadian-share × spend, or direct Visit Florida Canadian-spend). Folded into 2026-05-05 commit.

### 3. Deferred items (→ `DEFERRED.md`)

- **REGINALD bank-exposure hand-off spatial resolution.** For v0, build at mixed-grid native; REGINALD aggregates as needed. Trigger to resolve: REGINALD room opened, OR REGINALD signal contesting proxy quality for non-TDT county matching.
- **HOUSING Canadian-owner snowbird ground-spend.** Out of v0, documented as known underestimate. Trigger to resolve: HOUSING sub-agent outfit complete + thread opened. v1 pickup via joint model (TOURISM spend-per-snowbird-week × HOUSING Canadian-owner inventory).

### 4. Coupling updates

To fold into `AGENTS/MARCO/COUPLINGS.md` when drafted (protocol: 2-3 sub-agent contribution threshold; TOURISM-only today):

- **TOURISM → REGINALD ($-at-risk bridge):** TOURISM delivers Canadian-driven $ hole series by county × month (mixed-grid native); REGINALD composes against CARL's domestic-consumer-stress overlay to produce bank/CRE exposure view. Spatial-resolution question deferred.
- **TOURISM → CARL (domestic-substitution forecast):** TOURISM sizes gross Canadian-channel $ hole + observed domestic offset to present (Visit Florida 2025 aggregates); CARL forecasts forward domestic resilience under consumer-credit stress. Explicit division of labor.
- **TOURISM ↔ HOUSING (Canadian snowbird ground-spend, joint, deferred):** HOUSING owns inventory; TOURISM owns spend-per-snowbird-week. v0 excludes; v1 joint.
- **TOURISM → REGINALD/CORAL (cruise → bank mapping, lane-boundary reaffirmed):** TOURISM stops at passenger counts + per-passenger ground spend; REGINALD/CORAL maps to port-county bank exposure.
- **v1 extension gated on CARL series availability.** Scope expansion from (a) Canadian-driven only to (b) total-leisure stress triggers when CARL has a comparable series built.

### 5. Cross-agent-input flags

Logged as DEFERRED entries above: REGINALD spatial resolution, HOUSING snowbird ground-spend. Scope-definition question resolved in-room (locked option a).

---

**TOURISM commit dates carry:**
- **2026-04-28** — data source hierarchy (STR / AirDNA / Visit FL / BEA / TDT primary-vs-fallback) + county-TDT ingestion audit (Monroe, Collier, Pinellas, Miami-Dade, Orange) + cruise TDT-stitch methodology
- **2026-05-05** — uncertainty representation spec (narrow bands for native-TDT, wider bands for proxied) + origin-attribution methodology
