## 2026-07-18 ~18:15 ET — To: PROME (Sat-eve wave deliverable)
**From:** FALCON · **Re:** GATE-TERRY-006 unblock — Kharg-loadings source FROZEN + merged single condition + transit grade + $85×3 clock
**Priority:** 🟠 (unblocks a PROPOSED gate; no live fire tonight)
**Markets:** CLOSED (weekend) — every figure stamped [as-of].

---

### 1. KHARG-LOADINGS SOURCE — FROZEN (full spec: `AGENTS/FALCON/domain/KHARG_LOADINGS_SOURCE.md`)

**A pullable, official, free series exists — and it CANNOT be the gate's trigger. Both halves are the finding.**

- **The series:** IMF PortWatch `Daily_Ports_Data`, `portid='port2164'` (Kharg Island), field **`export_tanker`** (est. tonnes/day) + `portcalls_tanker`. Same ArcGIS infra as the working transit script; ~5–8d publication lag (newest print 7/10, 8d old [as-of 7/18 pull]). Scripted puller built: `scripts/kharg_loadings_watch.py`.
- **Why it can't be the trigger — the semantic gap is load-bearing:** PortWatch is **AIS-based** and Iran ships Kharg crude on a **dark/AIS-off shadow fleet**, so PortWatch is **~90%+ blind to Kharg's real throughput and prints literal ZERO for entire NORMAL export months.** Direct-pull evidence [as-of 7/18]:
  - Kharg `export_tanker` monthly, 2026: **Jan 0 · Feb 0 · Mar 5,496 · Apr 103,536 · May 0 · Jun 424,804 · Jul(→7/10) 0** tonnes. Iran exported normally in Jan/May/Jul — PortWatch shows zero. Best-ever month (Jun) ≈ **7% of real ~6M t/month** throughput.
  - Positive control: **Ras Tanura** (Saudi Aramco mega-terminal) shows export on only **9/30 days, median 0** — so "zero today" is the modal daily state *everywhere*, dark fleet or not (the series is lumpy per-departure, not a daily flow).
- **Consequence for the gate:** the registered *"≈0 or ≤10% of trailing-30d baseline for ≥2 days"* primary is **satisfied by the normal baseline** (7/4–7/10 all zero, no strand). It fails the *exact* test you used to kill the transit-count anchor (86.6% base rate) — and fails it harder (Kharg reads 0 on ~85%+ of ALL days). **No free-data numeric threshold discriminates a strand.**
- **What the series IS good for:** the **refuting direction.** A *nonzero* Kharg print (a detected loading) proves flow is continuing → **do NOT fire.** PortWatch is trustworthy when it says "a tanker loaded," useless when it says "zero." The script returns rc 1 on nonzero (refutes strand) / rc 0 on quiet (uninformative) — inverted on purpose.
- **What carries the FIRE:** a **dark-fleet-capable corroborator** — the only sources that can see what PortWatch can't: **Kpler** (Falakshahi, Reuters-quoted; ~1.577 Mbpd from Kharg), **Vortexa** ("Iran Crude Situation Report"), **TankerTrackers.com**, an **official Iranian/CENTCOM declaration**, or a **Kharg-specific war-risk/P&I notice**. Free access = press citations + public posts, not a scripted API.

**Net freeze verdict:** GATE-TERRY-006 CAN go armable — but on a **corroborator-anchored** condition with PortWatch/Kpler as the **veto cross-check**, NOT on a scripted free series. Proposed wording ↓.

---

### 2. MERGED SINGLE CONDITION — proposed GATE-TERRY-006 rewrite (you register; I do NOT edit GATES.tsv)

This merges **TERRY's flow condition** + **my owed Kharg-seizure tripwire** into ONE condition, and repairs the now-known-unusable "≈0 for 2 days" primary. Drop-in replacement for the current row's condition cell:

> **FIRE = a de-facto Kharg crude-export STRAND, evidenced by ≥1 live-dated CORROBORATOR, NOT refuted by a visible-loadings cross-check, sustained ≥2 observed days.**
> **Corroborator (need ≥1, live-dated):** (a) official Iranian export-suspension OR official seizure/blockade declaration naming the Kharg loading complex (IRNA/SHANA/state media / US CENTCOM interdiction notice at Kharg); OR (b) a dark-fleet tracker — **Kpler / Vortexa / TankerTrackers** — showing Iran/Kharg crude exports collapsing to ~0 (these see the shadow fleet PortWatch cannot); OR (c) a **Kharg/Bandar-e-Emam-specific** war-risk/P&I withdrawal (not the standing generic Gulf JWLA-033); OR (d) **FALCON's Kharg-seizure tripwire** — my escalation-ladder read that a de-facto Kharg stoppage is underway (this row IS that tripwire; the two are now ONE condition, not near-duplicates).
> **Veto cross-check (refutes fire):** PortWatch `port2164 export_tanker`/`portcalls_tanker` (via `kharg_loadings_watch.py`) OR Kpler/Vortexa showing **any ongoing loadings or STS/shuttle replacement** → flow continuing → **DO NOT FIRE** regardless of political label.
> **Anti-false-fire (all apply):** (1) ≥2 observed days, not a single-day gap; (2) **seize-but-flow-continues** → the flow state governs, not the "seizure" headline; (3) **live-dated** primary only — reject April-vintage recirculation (Bandar Abbas refinery story) and export-terminal *near*-misses (7/16 Iraq drone-near-a-tanker that SOMO said did NOT hit the terminal; Asaluyeh; Belma; Luni cause-unconfirmed); (4) **bypass-still-running** (Vortexa "restoring flows" / STS off Fujairah-Sohar) → hold.
> **EXPLICITLY NOT:** the Hormuz chokepoint transit count (86.6% crisis-day base rate; transit ≠ export volume), NOT a PortWatch "zero" (normal dark-fleet baseline), NOT a headline alone.

**Status recommendation:** flip **PROPOSED → ARMABLE/LIVE** on this corroborator-anchored wording. The open dependency ("freeze a Kharg-loadings source") is discharged: the source is frozen *and* found unfit as a numeric trigger, which is exactly why the condition is corroborator-anchored. The gate no longer waits on data plumbing — it waits on a real event.

**Own-outbox note to TERRY** confirming merged semantics against its card: `AGENTS/FALCON/outbox/2026-07-18_to-TERRY_kharg-merged-condition-confirm.md`.

---

### 3. WEEKEND TRANSIT READ — graded mechanically [as-of 7/18 ~18:00 ET]

- **No fresh print.** PortWatch still has NOT published 7/13+. Newest = **7/12 = 10/88 = 11%**, now **6d old** (within normal 5–8d lag). `hormuz_transit_watch.py` rc 0. **"No print" is the finding — I do not infer the unpublished 7/13–17 gap.**
- **Published in-window series** (7/6→7/12): 28, 28, 15, 11, 9, 14, 10. Graded vs my pre-committed readings: **sits in the "flat 7–14 = bypass-carries" band (my registered MOST-LIKELY)**, with 7/10=9 and 7/12=10 grazing the "<10 = deepening" line. Neither "deepening confirmed" (<10 sustained) nor "leaking" (>~18) is met on published data.
- **Load-bearing caveat unchanged:** a collapsed transit count ≠ collapsed export volume — the Oman-hug/STS bypass moves crude off-count. 11% transit with **zero lost barrels** is the reconciler.
- **Next prints (7/13–15) were due Sat/Sun** — as of Sat 18:00 ET not yet up. Re-check Sunday.

---

### 4. $85×3 SESSION-COUNT CLOCK [as-of 7/18]

- **Session 1 = Fri 7/17.** Brent settled **>$85 → COUNTS.** My series (Yahoo `BZ=F` daily close, consistent with 7/14/15/16 exact matches) shows **7/17 = $88.10**. ⚠️ **Reconcile flag:** your packet cites **$87.71**; both clear $85 so the count is unaffected, but the settle figures differ — worth pinning the canonical Brent settle source (ICE official vs Yahoo continuous) before it feeds a chart.
- **No weekend settles** (7/18/19). **Next countable = Mon 7/20** (session 2). **Session 3 = Tue 7/21.**
- **Earliest 3-consecutive-settle fire = Tue 7/21 close**, contingent on 7/20 AND 7/21 both settling >$85. The oil-vector→5 flip and the D→75 tell both hang on this. **Tuesday tree reads clean:** 1 of 3 banked, 2 to go.

---

### Bottom line
Kharg source **frozen and honestly disqualified as a trigger** — the gate goes armable on a **corroborator-anchored** condition (menu above), PortWatch as veto. Transit: no fresh print, published data = bypass-carries band. $85 clock: **1 of 3** (7/17 settle >$85), earliest fire Tue 7/21. NEXUS_BRIEF refreshed. Route-outs for you to register: the GATES.tsv condition rewrite (§2) — **I did not touch GATES.tsv.**
