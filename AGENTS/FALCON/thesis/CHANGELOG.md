> **Inherited at FALCON spinout 2026-07-12** (wholesale from `AGENTS/HAWK/thesis/CHANGELOG.md`, per build spec §5 — 100% Iran-theater audit trail). FALCON's own entries append below the `FUTURE ENTRIES` template line going forward.

# HAWK CHANGELOG

Tracks all changes to THESIS.md and TIMELINE.md. Reverse chronological. Each entry documents what changed, why, and the old → new view. This is the audit trail.

**Versioning convention:**
- THESIS: `vX.Y` — major (X) = structural thesis change (new channel, thesis break, conviction reversal). Minor (Y) = refinement (updated probability, new evidence for existing view, threshold adjustment).
- TIMELINE: not versioned numerically — entries are dated. Events are marked RESOLVED with outcomes when they pass.

---

## 2026-04-20 — THESIS v1.0 Established + thesis/ Folder Created

**Author:** HAWK (subagent)
**Action:** Created `thesis/` folder with THESIS.md v1.0, TIMELINE.md, and CHANGELOG.md. Migrated from STATUS.md narrative format to structured thesis format per SAM template.

**THESIS.md v1.0 changes (new document):**
- Established three transmission channels: Hormuz→Oil→Macro, Infrastructure→Duration, Ceasefire→Re-escalation
- Scenario framework: B 6% / C 12% / D 82% (post-ceasefire reassessment)
- Conviction: MEDIUM-HIGH (ceasefire achieved but durability unproven)
- Key thresholds table with current status
- Cross-agent links to BRENT, CARL, HENRY, LIQUID, SAM, REGINALD, RED, BROCK
- Exit protocol status: 2/7 criteria met

**TIMELINE.md changes (new document):**
- War progression Feb 28 – Apr 20 mapped
- Major branch points marked RESOLVED: Feb 28 (war start), Mar 1 (Hormuz), Mar 8 (Scenario C), Mar 18 (three-country retaliation), Apr 6 (deadline), Apr 12-13 (ceasefire)
- Forward branch points table: 30-day hold, mine clearance, insurance, infrastructure timelines
- Resolution markers: what resolved and how, what remains unresolved
- War day tracking table: Days 1-51 mapped by phase

**Source material migrated:**
- STATUS.md (Apr 20): Scenario D 82%, Brent $64.50, War Day 51, Ceasefire Day 8
- MEMORY.md: ADCOP fire, Kuwait targeting, AWACS loss, Al Taweelah, WTI/Brent inversion, petrodollar fracture
- KB.tsv: 80+ entries through KB-HAWK-124
- VX.tsv: 12 vectors including Hormuz status, Iran war, Taiwan LNG, infrastructure
- FLOW.tsv: 18 transmission flows
- STATUS archives in `domain/sources/`: 20260222, 20260301

**Old view:** War tracking dominant (Days 1-51), Scenario D 92%, kinetic escalation focus
**New view:** Ceasefire durability monitoring (Day 8+), Scenario D 82%, physical restart lag vs. market pricing focus

**Framework shift:**
- From: "Will war escalate?" (Days 1-43)
- To: "Will ceasefire hold?" (Days 44+)
- New monitoring priorities: mine clearance visibility, insurance reinstatement, infrastructure repair timelines

---

## PRIOR STATUS EVOLUTION (reconstructed from STATUS archives)

These entries are reconstructed from `domain/sources/` archives (frozen under HAWK) to establish the audit trail pre-CHANGELOG.

### 2026-04-01 — STATUS Archive: Day 32, Scenario D 92%, Brent $108-116

**What changed:**
- Phase 5 fully activated (Houthi entry + multi-front war)
- 3 Gulf states under direct attack (UAE, Bahrain, Qatar)
- Apr 6 deadline 5 days out
- Convergence 45/45 🔴🔴 MAXIMUM
- Raised D to 92% (largest shift since Day 18)

**Key findings:**
- ADCOP fire = Hormuz bypass architecture eliminated (no safe export route)
- Kuwait strike = non-combatant targeting (regional war framing)
- AWACS destruction = $300M US asset loss on allied soil
- Al Taweelah/EGA = aluminium supply shock (4% global)

**Source:** `AGENTS/HAWK/domain/sources/STATUS_archive_20260301.md` (frozen)

---

### 2026-03-01 — STATUS Archive: Day 1, Scenario B 55% / C 35% / D 5%

**What changed:**
- Operation Epic Fury launched (Feb 28)
- Hormuz functionally disrupted (Mar 1)
- Iraq Rumaila shutdown (Mar 3)
- Insurance cliff / Maersk suspension (Mar 5)
- Scenario C raised from 20% → 35% on storage crisis + no diplomatic path

**Key thresholds established:**
- Hormuz shipping -92%
- Kuwait ~18 days storage
- UAE ~22 days storage
- Brent $90 (first time since mid-2024)

**Source:** `AGENTS/HAWK/domain/sources/STATUS_archive_20260301.md` (frozen)

---

### 2026-02-22 — STATUS Archive: Pre-War, Shadow Fleet Focus

**What changed:**
- Shadow fleet enforcement escalating (598 vessels banned, 20% halted)
- Russia naval escort threats (Patrushev)
- Ukraine refinery campaign (16 refineries, 38% capacity)
- Venezuela annexation rhetoric
- Scenario A (surgical) 10% / B (sustained) 55% / C (escalation) 35%

**Key vectors:**
- VX-HAWK-SHADOW-01: Shadow fleet enforcement
- VX-HAWK-SHADOW-02: Naval confrontation risk
- VX-HAWK-IRAN-01: Iran war (pre-launch monitoring)

**Source:** `AGENTS/HAWK/domain/sources/STATUS_archive_20260222_full.md` (frozen)

---

## FUTURE ENTRIES

Add below this line when thesis changes. Include: date, which doc changed, what changed, why, old view → new view. Tag THESIS changes with version number.

Template:
```
## YYYY-MM-DD — DESCRIPTION (THESIS vX.Y or TIMELINE update)

**Author:**
**Action:**

**What changed:**
1.

**Old view:**
**New view:**

**Source:**
```

## 2026-04-20 17:48 EDT — THESIS v1.1 Brent Price Correction + Scenario Reassessment

**Author:** HAWK (subagent)
**Action:** Updated THESIS.md and STATUS.md with corrected Brent price ($64.50 → $94.28) and reassessed scenario probabilities.

**Critical data correction:**
- **Brent price:** $64.50 (stale/incorrect) → $94.28 (live from thresholds.py test)
- This is a 66% retracement of the post-ceasefire collapse ($116.43 → $64.50)
- $94.28 falls in Scenario C territory ($80-100 range)

**Scenario probability shift:**
- **B:** 6% → 8% (slight increase, but ceiling constrained by $94 price)
- **C:** 12% → 22% (+10 points — Brent $94.28 signals ceasefire stress)
- **D:** 82% → 70% (-12 points — ceasefire holding but durability questioned)

**Why the shift:**
- Brent $94.28 contradicts the "demand destruction" thesis that justified $64.50
- Market pricing ceasefire durability concerns, not recession
- Price action = leading indicator of ceasefire stress before kinetic events
- Oil price vector elevated from 🟡 3 → 🔴 4 in convergence matrix
- Convergence: 35/45 → 36/45 (oil price vector elevated)

**Cross-agent transmission updates:**
- BRENT: Demand destruction thesis → Ceasefire stress signal
- CARL: Consumer relief → Pump price pressure returning
- LIQUID: Risk-on → Risk-off sentiment shift
- REGINALD: Price collapse stress → Volatility stress at both extremes

**Exit protocol status:**
- Price normalization below $80: ✅ EXCEEDED → ⏳ FAILED ($94.28)
- Progress: 2/7 criteria → 1/7 criteria (ceasefire only)
- Full exit now requires: Brent <$80 SUSTAINED, not just brief dip

**KB.tsv fixes:**
- Fixed duplicate IDs: KB-HAWK-109 (line 112) → KB-HAWK-131
- Fixed duplicate IDs: KB-HAWK-110 (line 113) → KB-HAWK-132
- Updated DerivedFrom reference in KB-HAWK-115

**Files modified:**
- `STATUS.md`: 15+ updates to Brent price, scenarios, convergence, cross-agent table
- `THESIS.md`: v1.1 — scenario probabilities, key thresholds, exit protocol
- `workbook/KB.tsv`: Renumbered duplicate entries 109→131, 110→132
- `CHANGELOG.md`: This entry

---

## 2026-07-12 — FALCON SPINOUT (inheritance, not a thesis change)

**Author:** DAEDALUS (build sub-agent, WP-1)
**Action:** THESIS.md, TIMELINE.md, CHANGELOG.md (this file) copied wholesale from `AGENTS/HAWK/thesis/` into `AGENTS/FALCON/thesis/` per build spec `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md` §5. No content changed; SUPERSEDED banners and rewrite-backlog notes carried forward verbatim + one inheritance line added atop each file. HAWK's original files stay frozen at `AGENTS/HAWK/thesis/`.

**Old view:** N/A (mechanical move)
**New view:** N/A (mechanical move)

**Source:** Build spec + HAWK split manifests (`AGENTS/DAEDALUS/builds/hawk_split/`)

---

## 2026-07-27 — THESIS v2.0 REWRITE + TIMELINE extended to War Day 149 (**the rewrite-to-current-regime backlog is CLOSED**)

**Author:** FALCON (first FALCON-authored thesis; every prior entry above is HAWK's)
**Action:** Full rewrite of `THESIS.md` (v1.2 → **v2.0**) and `TIMELINE.md`. Closes the rewrite-to-current-regime backlog item that had been open and banner-flagged since the 2026-07-12 spinout — and, before that, carried by HAWK since **Apr 20**. Both files had been unactionable for **98 days**.

**Why v2.0 is a MAJOR version, not a refinement:** v1.2 was a **deadline thesis** — it modelled the Apr 21 ceasefire-expiry clock, priced three branches off that single binary, and used a **4-tier A/B/C/D ladder**. The deadline passed without producing its base case (an MOU-era lull held instead), so the document's entire spine was not merely stale but *answering a question the war stopped asking*. v2.0 is built on a different question: **not "does the war escalate?" but "does the war's damage ever become lost barrels?"**

**THESIS.md v1.2 → v2.0:**
- **Core thesis REPLACED.** Old: *"ceasefire is a 14-day clock with hours left; deadline passage = D confirmation and Brent $120-150."* New: **"the war reprices freight, not barrels"** — risk-**premium** regime, not supply-**loss** regime, plus **two counter-moving wars in one theater** (US-Iran de-escalating, Saudi-Houthi escalating, Iraqi militias newly active).
- **All three transmission channels REPLACED.** Old: deadline-outcome → oil; infrastructure damage → duration; ship-on-ship → accidental escalation. New: **⓵ LIVE premium channel** (willingness-to-move-a-hull → freight/insurance/routing → price; **P 23/25, 92% of ceiling**) · **⓶ DORMANT supply-loss channel** (**R 7/20 with R1-R3 at the absolute floor**) · **⓷ ACTOR PROLIFERATION** — a channel v1.2 did not have, promoted to first-class because it is what killed FAL-01.
- **Scenario ladder RETIRED and replaced: 4-tier A/B/C/D → 3-tier B/C/D**, with **D as a re-escalation *ceiling*, not a discrete collapse/nuclear tier.** Old marks B 5 / C 20 / D 75 (Apr 20) → **B 10 / C 40 / D 50**. Convergence rebased 41/45 → **40/50** on the current 10-vector set. *(This ladder mismatch was the concrete risk: any reader or spawned agent hitting THESIS.md first got a framework FALCON no longer uses.)*
- **Key thresholds table REPLACED** — Apr-21-deadline / Brent-$130 rows out; **FAL-03's three operational routes**, the Jazan damage assessment, the **WC Saudi 0.1% transit→origin falsifier**, and the bypass floor in.
- **Thesis-break condition is now a REGISTERED, DATED PREDICTION** rather than prose: **FAL-03** (58%, Jul 27 – Aug 17). v1.2's break condition was *"extension announced pre-8pm ET Apr 21"* — an event that can no longer occur.
- **Conviction re-stated honestly:** MEDIUM-HIGH on the regime call, **MEDIUM on the marks**, with the weakest joint named in the document (a 15-point D cut resting on three quiet nights caused by an ammunition shortage).
- **Exit protocol DE-DUPLICATED** — v1.2 maintained its own 7-criteria copy; v2.0 summarises and points to `workbook/EXIT_PROTOCOL.md` as canonical. Still **0/7**, but for the opposite reason: then the war was escalating *into* a deadline; now criteria fail because **a pause is not a resolution**.

**TIMELINE.md:**
- **Feb 28 – Apr 20 PRESERVED substantially verbatim** — accurate resolved history, not rewritten. Explicit marker added where the inherited record stops (War Day 51).
- **Three new FALCON-authored phases added:** *THE LULL* (Apr 21 – Jun 26), *THE JULY WAR* (Jun 27 – Jul 27), and a rebuilt war-day table through **War Day 149** (computed via `date`, not asserted — per `[[finding_weekday_assumed_never_evaluated]]`).
- **Forward branch-points table REPLACED ENTIRELY** — the Apr-20 table was stale on *every* row (May 12 30-day hold, mine clearance, QatarEnergy restart, Houthi compliance…). New table is 9 live triggers with bull/bear forks and current status.
- **⚠️ INTAKE CAVEAT written into the Apr-Jun section:** that window is FALCON's thinnest coverage (ledger: May 1 event, June 0). Flagged as intake-limited, **not an exhaustively swept negative** — it must not be cited as proof of quiet.
- **Corrected dates carried in:** Mombasa B + Al Bahyah **7/13** (UKMTO 086-26/087-26), Stolt Magnesium **7/14** — per the same-day hull reconcile (`KB-FALCON-057`).

**Old view → New view (one line):** *"The ceasefire is failing inside its own window and the Apr 21 deadline converts that failure from probability to reality"* → **"The war has struck the asset class five times since April and taken ZERO barrels off the market; the question is no longer whether it escalates but whether damage ever becomes loss — and FAL-03 is the dated test."**

**Source material:** `STATUS.md` (2026-07-27), `thesis/FAL-01_REREGISTRATION_SCAFFOLD.md`, `domain/energy-strikes/ANALYSIS_2026-07-27.md` + `STRIKES.tsv` (30 rows), `domain/FRESH_LEG_BASELINE.md`, `workbook/KB.tsv` KB-FALCON-042/048/050/055/057, `workbook/WARRISK.tsv`.

**Next rewrite trigger (registered):** FAL-03 resolving either way · a **fifth** belligerent axis · or a dated Oman framework. Routine mark moves belong in `STATUS.md`, **not** here — that discipline is what let v1.2 rot for 98 days while STATUS stayed current.

---

*This changelog is the audit trail for HAWK/FALCON thesis evolution. Keep it current.*

---

## 2026-07-30 — THESIS v2.1: the core claim is MOLECULE-SPLIT + TIMELINE forward-branch table refreshed

**Author:** FALCON (live session, Will-requested boot + news integration, then a self-directed staleness sweep)
**Action:** Amended `THESIS.md` and `TIMELINE.md` in place — **not** a structural rewrite (v2.0's 3-tier ladder and three-channel structure are untouched), but the **central claim was narrowed on an axis it never had.**

**THESIS.md v2.0 → v2.1:**
- **KEY THRESHOLDS table (rows 1-3) was WRONG, and row 2 was wrong when written.** *"Jazan damage assessment: 🔴 ABSENT at 3 days"* → **it exists, and it is a shutdown** (400 kbpd, shut 7/27, restart tent. 8/15, Reuters/IIR). *"Any Gulf/Iran force majeure: 🟢 None current"* → 🔴 **FIRED, and never 🟢** — a QatarEnergy FM on LNG has been live since **2026-03-24**. Both rows re-pointed from the dead FAL-03 to **FAL-04**.
- **Added the molecule-split banner:** the thesis claim *"risk-PREMIUM regime, not supply-LOSS regime"* was never molecule-scoped. Scoped: **HOLDS for CRUDE**, **FAILS for GAS** (since March) and **REFINED PRODUCT** (since 7/27).
- **Bypass row de-hardcoded:** the collapse floor is **30% of a rolling 60-day mean** and had drifted **15,684 → 16,224 → 20,105 (+28% in 14 days)** while this table carried `16,224` as a constant. **A stale low floor fails FALSE-NEGATIVE.**

**TIMELINE.md:**
- Amended the *"a hit is not a loss"* lesson **twice over** — Jazan closed the gap in ~2 days, and the broadcast phrase is true of **CRUDE only**.
- **Forward-branch table: 4 rows refreshed** — leg-3 (now NOT FIRED with a *verified* margin, −23% to −32%; the 4.7 baseline is total-liquids per AGBI 7/28), Yanbu (added the undefendable-Petroline re-point), bypass (rolling floor), fifth-actor clause (re-pointed to FAL-04).

**Old → new view:** *"The theater damages assets without losing barrels"* → **"The theater damages assets without losing CRUDE barrels; it has been losing GAS since March and PRODUCT since 7/27, and FALCON could not see either because every instrument it owns counts kinetic strikes on oil."**

**Why not v3.0:** the transmission structure and the ladder did not change — the *scope of the central claim* did. Trigger for a genuine v3.0 remains: FAL-04 resolving, a fifth belligerent axis, or a dated Oman framework.

> ⚠️ **DOC-CONVENTION MISMATCH, flagged not fixed:** this file's header says *"Reverse chronological"* but every entry since 2026-04-20 has been appended in **ascending** order (4/20 → 7/12 → 7/27 → 7/30). **Practice is chronological; the header is wrong.** Appending here to match practice rather than silently splitting the file into two orderings. Fixing the header is a one-line change owed to whoever next touches the preamble — noted so it is a decision, not a drift.

---

## 2026-09-07 — TIMELINE forward note (no version change)
A forward note was appended to `TIMELINE.md` recording that its narrative stopped at War Day 149 while the war had moved through a 32-night pause, a resumed campaign and the 9/5 Kylo sinking. The note was a flag, not a fix (`[[finding_banner_is_a_warning_not_a_fix]]`); it is discharged by the 9/8 extension below.

## 2026-09-08 — THESIS v2.1 → v2.2; TIMELINE extended Jul 28 → War Day 193 (staleness sweep, Will-directed)
**Trigger:** v2.1's own footer trigger — *"FAL-04 resolving either way"* — fired on 2026-08-20 and sat unactioned for 19 days; DAEDALUS PR#5 had caught the identical rot on `EXIT_PROTOCOL.md` on 9/1. This entry discharges it.
**THESIS v2.2 — what changed:** (1) a **FOURTH transmission channel, ⓸ export-chain interdiction** (`FLOW-FALCON-03`): the US destroying Iranian export HULLS under a declared tit-for-tat rule — the first channel by which the CRUDE premium regime could convert without a facility being touched; bounded by the blockade's own drawdown (Kpler 90M→29M afloat). (2) The **attacker axis** named in ⓷ — `VX-FALCON-SUNK-01` split (iii-A)/(iii-B) with its base rate (`KB-FALCON-142`). (3) The **rail cap** recorded in the scenario section and in CONVICTION as a LOW-confidence statement about the apparatus — nothing registered above D 75; D→85 proposed (DOCKET L300). (4) Marks B 3 / C 22 / D 75; thesis-break = **FAL-05** (55%, → 10/7) with the FAL-03/FAL-04 lineage stated. (5) KEY THRESHOLDS and EXIT PROTOCOL STATUS re-graded on 9/8 data (transits 6/88, bypass 85,916 vs 25,095, Brent $99.45, war-risk 48d stale, Jazan restart never confirmed, in-port threat and (iii-A) class added as rows). (6) Footer rewrite trigger re-dated and made DATED (FAL-05 10/7 · fifth axis · dated Oman corridor · a registered rung · a second class-(iii) loss · 2026-10-07).
**Old → new view:** *"The war reprices freight, not crude barrels, and FAL-04 tests the crude leg"* → **"The war reprices freight, not crude barrels; it has taken gas and product; it is now destroying Iranian export HULLS at a rate Iran sets by shooting at US warships; and the ladder that is supposed to record that has run out of rungs."**
**Why not v3.0:** the core claim, the molecule split and the 3-tier ladder are unchanged; a channel was added and a defect in the apparatus was named. v3.0 triggers remain: FAL-05 resolving, a fifth axis, a dated permanent corridor.
**TIMELINE:** three narrative phases added (the long pause · the campaign · the tanker war and the southern salvo); forward branch-points, resolution markers and war-day phases regenerated; the 9/7 forward note removed as discharged. War Day 193 computed from Feb 28 = Day 1.
**Same-session companions (not THESIS/TIMELINE, logged for the trail):** eight of nine `VX.tsv` rows re-verified with `[Sep8]` blocks after 40 days at 7/30; `EXIT_PROTOCOL.md` §1 kill table and §4 thresholds re-graded; 68 expired `KB.tsv` rows dispositioned (SUPERSEDED / CONFIRMED / STALE); `FRESH_LEG_BASELINE.md`, `BYPASS_INTEGRITY_BASELINE.md`, `IRAQ_PMF_DISCRIMINATOR_REVIEW.md`, `SOURCES.md`, local `MEMORY.md` and the FALCON `CLAUDE.md` FILES table refreshed; `bypass_watch.py` no longer prints a hardcoded scenario mark.

> *(Header still says "reverse chronological"; practice is ascending. Appended at the END to match practice — flagged 7/30, unchanged.)*
