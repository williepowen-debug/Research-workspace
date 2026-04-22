# MARCO ↔ TOURISM Thread

**Purpose:** Live coordination file between MARCO and TOURISM. MARCO opens prompts; TOURISM responds with structured signals. Will may drop `WILL:` sections anytime.

**Protocol:** See `CLAUDE.md` → "Coordination with MARCO" section.

**Thread history:** `threads/INDEX.md` (full archive in `threads/archive/`)

---

## Active thread

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
