# Cross-War Energy-Strike Aggregate — Summary (thin, derived)

> **Convention:** this file is **regenerated from OSPREY's and FALCON's own strike ledgers at HAWK closeout (CLAUDE.md step 13), never independently maintained.** HAWK does not log strike rows — that discipline lives with the theater owners. If this file drifts from the siblings' ledgers, re-pull from them; do not hand-edit rows here.
> **Predecessor:** the original `STRIKES.tsv` + `SUMMARY.md` in this directory are 🧊 FROZEN 2026-07-12 (pre-split, 36-row combined ledger) — see their banners.
> **Regenerated: 2026-08-20** from both siblings' `domain/energy-strikes/`, **reading each ledger's own analysis header, not just its row count** — and both desks had just delivered, so this is a regeneration against *fresh* sources rather than the usual lag.
>
> **OSPREY — `STRIKES.tsv` 75 data rows, swept through 2026-08-16.** Newest row `RU-20260816-SKIROS-CPC` (added this session): the Greek Suezmax *Skiros* struck at the CPC berth carrying **Russian** cargo. ⚠️ **Its newest `ANALYSIS_` is 2026-07-23 — 28 days behind its own ledger, and OSPREY flagged that regeneration as owed in its own closeout**, so this is a self-declared gap, not a catch. *(Dated observation, not a standing claim — the sibling may be fixing it as this is read.)*
>
> **FALCON — `STRIKES.tsv` 37 data rows, newest `GI-20260813-JIZAN3` (2026-08-13).** Newest `ANALYSIS_` is 2026-08-06. ⚠️ **The 25-day Kharg loadings halt (7/18→8/12) FALCON surfaced on 8/20 is NOT in this ledger, and that is probably correct rather than a gap** — it is an *interruption*, not a *strike*, and a strike ledger has no row shape for it. **But it means the largest export interruption of the window is invisible to anyone reading only the strike ledgers, which is exactly what this derived surface exists to catch.**
>
> ⚠️ **"Derived" is NOT "self-updating"** — this file is only as current as this stamp. *(Prior regenerations: 2026-08-15; 2026-07-28; 2026-07-25; 2026-07-12 split day.)*

---

## One row per theater

| Theater | Ledger | Data rows | Date range | Swept-through mark | Channel / gate state | Pointer |
|---|---|---:|---|---|---|---|
| **Russia/Ukraine** | `AGENTS/OSPREY/domain/energy-strikes/STRIKES.tsv` | **71** (was 48, 7/28) | 2026-02-23 → 2026-08-14 | **2026-08-15**, current (catch-up sweep 8/11→8/15 this session) | Three channels. **Ch.1 refineries/products 4🔴** — 10 named refinery strikes 8/1-8/13 alone (Orsk 8/11 ~6mo shut EST, Salavat 8/13 2nd hit in a month); heaviest tempo of the war, crude keeps escaping. **Ch.2 crude-export terminals 4🔴 — GATE-OSPREY-001 remains FIRED** (7/24); legs (a) SPM damage / (c) Tengiz FM still **UNFIRED, last verified 8/10** (this sweep found zero CPC-specific developments either way — UNFIRED-by-default-of-no-evidence, not by fresh re-verification). **Sheskharis is now a 3-episode recurrence** (halt 7/22-26 → RE-STRUCK 8/12, Neptune missiles+jet drones+USVs, capability step-change → halted again 8/14, two unmerged causes) — CPC direct-checked NOT hit in either 8/12 or 8/14 event. **Ch.3 shadow-fleet tankers** — no new row since 7/30, 16 days, approaching the 21-day kill threshold (~8/20). | `ANALYSIS_2026-08-15` (session block in `STATUS.md`), `STRIKES.tsv` header |
| **Iran/Gulf** | `AGENTS/FALCON/domain/energy-strikes/STRIKES.tsv` | **32** (was 31, 7/28) | 2026-03-02 → 2026-07-27 | **2026-08-06** on the facilities ledger (zero new facility rows 7/30→8/6 is itself the finding — the window's kinetics were all maritime); **STATUS re-verified 8/15** | **GATE-FALCON-001 leg-1 FIRED 7/23** (Encelia). **Leg-2 NOT FIRED**, adjudicated 8/10 like-for-like on the registered TankerMap basis — a recovery (+200% w/w), not a step-down. **🔴 Leg-3 ADJUDICATED FIRED 8/15** (Yanbu w/c-8/3, Kpler 1.78 / Vortexa 2.38 mb/d, both below the ≤2.55 crude fire line) — **but R3 itself is Will-ruled HOLD 8/15**, mechanism ambiguous (genuine constraint vs Petroline/Ras-Tanura reallocation), discriminator commissioned to BRENT next session. **FAL-01 remains RESOLVED FAILED (7/27, Jazan).** Marks **UNCHANGED B 5 / C 35 / D 60, convergence 43/50** — session was watch-only, no self-applied moves. | `reports/2026-08-15_gate-falcon-001-leg3-yanbu-wc0803-fire-adjudication.md` |

**⚠️ Correction to this file's own prior version (logged, not silently overwritten).** The 7/28 regeneration is now itself the stale artifact this note describes — this is the **fourth** consecutive skip DAEDALUS's war-triad review caught (regens due at every HAWK closeout; none ran 7/29 through 8/10). Root cause unchanged from the 7/25 and 7/12 instances: **a derived surface is only as current as its last regeneration**, and closeout step 13 was not being executed, not merely executed late. This regeneration reads both ledgers' *own* current headers rather than carrying forward the 7/28 table, which was reporting FALCON convergence at **B10/C40/D50** when FALCON has stood at **B5/C35/D60, 43/50** since 8/6 — a 9-day-stale scenario read that this file was the last surface still carrying.

---

## The cross-war observations

**1. THE THEATERS REMAIN DIRECTIONALLY DECOUPLED (7/28 finding, re-verified 8/15) — but a SEPARATE mechanism now couples them, and the two findings are not the same claim.** Directional decoupling (belligerent dyads move independently — Saudi-Houthi still escalating on tempo, Russia-Ukraine still continuing at heaviest-of-war tempo, US-Iran still holding its 8/8 pause) is unchanged and confirmed again this session. **What's new is a MECHANISM finding that sits alongside it, not against it:** `KB-HAWK-252`/`266` establish that the US selects its intervention instrument by **leverage over the attacker** (a phone call for a client, a coalition for an adversary) — this explains *why* interventions land where they do, without implying the theaters move in lockstep. Keep the two claims separate: **directional independence** (this section) is a fact about belligerent trajectories; **mechanistic coupling** (KB-HAWK-252) is a fact about the US response function. Both are true at once.

**2. 🆕 THE 8/8 CPC UNDERSTANDING SURVIVED ITS LOUDEST TEST.** Sheskharis (Russian/Transneft, NOT CPC) was re-struck 8/12 with Ukraine's most capable strike package of the war — Neptune anti-ship missiles + jet drones + naval USVs against the Black Sea Fleet's main base, a capability step-change with no precedent in this conflict — and halted again 8/14. **CPC itself was not reported hit in either episode, direct-checked by OSPREY 8/15.** This is the third Sheskharis disruption episode since 7/22 (halt 7/22-26 → re-strike 8/12 → halt 8/14), and BRENT has independently marked its own CPC-convergence row 2→3 on *recurrence* — frequency, not severity, capturing information reversibility-only readings miss. → `KB-HAWK-266`.

**3. THE CPC RESOLUTION (7/27) — still the cleanest natural experiment either theater has produced; unchanged this session.** HAWK's pre-registered test resolved: SPMs reopened intact, no repair, no new force majeure, the returning charterer (Tengizchevroil) the same Chevron entity whose refusal defined the 7/23 willingness leg. **Magnitude no longer discriminates a premium event from a physical supply event — only reversibility does.** → `KB-HAWK-235/236`, `FLOW-HAWK-19`.

**4. Production-class sparing remains a CURRENT-CYCLE regime (re-verified 8/15), not a war-long constant.** The Feb28–Apr9 acute-phase damage table (Khurais/Manifa/South Pars/Ras Laffan+Pearl GTL/Shah+Habshan/East-West pipeline, full detail in the 7/28 version's history) is unchanged. **What is spared THIS cycle (Jun 27→) is unstruck upstream production/export-terminal infrastructure specifically** — Jazan's repeated hits (7/25 confirmed, 8/9 confirmed fire, 8/13 claim-only) are a *refining* asset, a different class from the upstream/export-terminal set this observation tracks, and do not contradict it. **🆕 Cross-reference, not a merge:** the Yanbu loadings decline (leg-3, §above) is an economic/logistics indicator, not a kinetic strike — it does not enter this table and its cause (constraint vs. reallocation) is undetermined; see `KB-HAWK-265` for the full reconciliation against HAWK's own blockade-rerouting synthesis.

**5. The old timing observation (Russia's refinery campaign peaking the same week as Iran's now-collapsed MOU) stays retired as coincidence** — no mechanism has been demonstrated since 7/28, and observation 1 above gives less reason to look for one, not more.

---

## Reading this table

- **Both ledgers are current as of this regeneration (8/15).** OSPREY (71 rows, swept through 8/15) and FALCON (32 rows on the facilities ledger, swept through 8/6, STATUS re-verified 8/15) are not comparable by row count — 71 vs 32 reflects campaign tempo and duration, not data quality, same as the 48-vs-31 note this file carried on 7/28.
- **The regeneration itself was the finding this pass, not the content.** Four skipped closeouts is a HAWK-side process gap (this file's own maintenance step, `CLAUDE.md` step 13), flagged by DAEDALUS's 2026-08-15 war-triad review, not a theater-desk failure.
- **HAWK's job here** is limited to (a) keeping this pointer table current at closeout and (b) flagging when the siblings' swept-marks go stale — **not** rebuilding their ledgers. Where a metric has a theater owner, cite theirs; keep no competing copy.

---

## Cross-war observation, 2026-08-20 regeneration — what the two ledgers say *together* that neither says alone

**1. Both theaters' newest recorded events are VESSEL-AT-TERMINAL events, not infrastructure destruction** — *Skiros* at the CPC berth (8/16, RU-UA) and the third claimed Jizan strike (8/13, GULF-IRAN). Neither destroyed capacity. That is the strike ledgers independently reproducing the migration thesis: **the kinetic record is drifting from steel toward hulls and claims.**

**2. 🔴 THE STRIKE LEDGERS SYSTEMATICALLY UNDER-REPRESENT THE ACTUAL SUPPLY EFFECT, and this regeneration is where it becomes visible.** The two largest crude-flow events of this window appear in **neither** ledger: the **25-day Kharg halt** (~90% of Iran's exports, 7/18→8/12) and the **~−640 kbpd five-week slide in Russian seaborne crude exports**. Both are *interruptions and deterrence effects*, not strikes — so a strike ledger has no row for them **by construction**.
> **⇒ Anyone sizing war-supply risk off strike counts is reading the wrong instrument, and the error is one-directional: strike ledgers UNDER-count.** The barrels move through willingness, and willingness leaves no strike row.

**3. A destroyed crude-export asset predates both ledgers' current window and neither carries it:** CPC's **SPM-2**, irreversibly destroyed **2025-11-29** (operator: *"operation impossible"*), out ~270 days — while CPC **kept exporting through SPM-1**. Crude-export terminals are **redundant by construction**, so component destruction does not aggregate to terminal flow loss. → `KB-HAWK-278`.
