# CARL Sub-Agent Team

**Updated:** 2026-09-01 (**Tue eve — NO sub-agents spawned; PROME-scoped Tier-1 work-through.** ⚠️ **PHAN IS NOW +49d AND ITS GATE FIRED 8/27 (Affirm FQ4 + Klarna Q2).** Change from the 8/27 entry: **it is no longer only a TEAM.md flag — a dated row now exists at `docket/CATALYSTS.tsv` 2026-09-08**, at PROME's instruction, so the boot-7a past-due scan becomes its scheduled runner. That is the (a)/(b) fix from the 8/15 *obligation-with-no-owner-who-boots* finding finally applied to my own desk — the flag had sat here with no runner for 49 days, which is the exact failure that finding describes.)

> **Freshness discipline (2026-07-10):** the Status/ages below are hand-written snapshots as of the Updated stamp — **verify against each sub-agent's `STATUS.md` mtime before trusting** (`ls -l sub_agents/*/STATUS.md`). Freshness keys on the CANONICAL SURFACE's own state, never on SV-receipt (PAT-044: the Jun-22 GIG SV was marked "🟢 fresh" here while GIG's STATUS rotted 66d into asserting falsified facts). Mtime-derived ages in boot.py = open build item (pairs with consistency_check).

---

## 📬 INBOX LAYER — ALL SEVEN SUB-AGENTS (built 2026-08-03, Will-ruled 2026-08-02)

**Will ruled the whole layer symmetric.** Every sub-agent now has `sub_agents/<NAME>/inbox/` — DOC, GIG, PHAN, POLLY, POP and META joining STUE (which was first, 7/31). PROME's parent-fan-down register was **overruled**; this is a direct Will instruction, not a recommendation.

| Sub-agent | inbox | README | boot-card wiring | processed/ |
|---|---|---|---|---|
| STUE | ✅ 7/31 | ✅ | ✅ (both paths) | ✅ |
| DOC · GIG · PHAN · POLLY · POP · META | ✅ **8/3** | ✅ **8/3** | ✅ **8/3 — step 0 of `On Session Start` + a closeout note in `On Session End`** | ✅ seeded |

**Build spec applied to all six** (STUE's mitigation pattern is the layer standard, not optional):
1. **Inbox scan on BOTH boot paths, including the spawned-mode card** — a scoped spawn is exactly where the scan gets skipped, so it is **step 0**, not an appendix.
2. **Everything present is unprocessed by definition** — no read-cursor state to rot.
3. **Packet AGE is a finding** — >~30d means the sender has been acting on a false assumption about what the sub-agent knows; **telling the sender outranks actioning the packet.**

Channel properties carried into each card: plain `.md` packets (`YYYY-MM-DD_from-<SENDER>_<subject>.md`) · **NOT** the DM-v1 coded route (`MSG-*` stays allowlisted to PROME→BRENT/SAM; a `MSG-*` here is an ordinary packet) · **CARL remains system of record — sub-agents propose, CARL disposes** · boot-cadence honesty stated on every card so senders learn it from the surface they read. Each `inbox/` is seeded with a `README.md` (empty dirs don't commit — the lane has to exist on origin, not just on this box).

> ⚠️ **THE THREE CARDS THAT NEED THEIR CADENCE READ BEFORE YOU SEND:** **POP** and **PHAN** are **dossier-mode** and **META is FROZEN with an explicit do-not-spawn** — so a packet placed in META's inbox has **no scheduled reader whatsoever.** Their READMEs say this in the sender section rather than burying it: for methodology, send to **DAEDALUS** (which inherited META's digest) or to **CARL**. This is the exact risk STUE named when it proposed the options — *an inbox nobody reads on a cadence is worse than no inbox, because it presents as a live channel while silently absorbing mail.* Will ruled for the symmetric layer anyway, which is right; **the age check is the mitigation and it is not optional.**

---

## ROSTER

### Standing sub-agents (spawn per docket catalysts)

| Agent | Domain | Last real refresh | Canonical-surface state (7/10) | Next catalyst (docket) |
|-------|--------|-------------------|-------------------------------|------------------------|
| **STUE** | Student loans (DQ, SAVE→RAP, servicers, Treasury collections; **+SLABS collateral-transmission + higher-ed institutional stress, Will-ruled 7/31** — neither creates a CRL row) | **Aug 10** (inbox ×3 drained + Treasury verify INCONCLUSIVE + CRL-14→28 residue swept ×6 surfaces; SV-STUE-2026-08-10-01; prior data pass **Jul 25** — the Jul-15-fired gate discharged; 2 packets: CRL-14 55%/STUCK Will-approved + cascade-rescope + CRL-13 window compression; applied at parent 7/31) | ✅ current; SV-STUE-2026-07-25-01; no own PREDICTIONS.tsv (its predictions ARE parent CRL-04/05/13/14 — accepted 7/10). **📬 HAS AN INBOX (Will-ruled 7/31, first sub-agent with one): route STUE-destined mail to `sub_agents/STUE/inbox/` directly — CARL is no longer the letterbox. ⚠️ STUE boots ~5×/qtr: time-critical routes keep a CARL-docket copy.** PROME audit hand-downs (VASP category error + monotone law) ✅ PROCESSED 8/10. | ~Aug 13 Treasury re-scoped (Default Resolution Hub primary watch) 🟠 · ~8/14 MOHELA docket check (pre-answered silent through 8/10) 🟡 · Q2 HHDC student-loan read (post-print, ~8/11+) 🔴 |
| **HOMER** | Housing (foreclosures, MF DQ, builders, state-level) | **PROMOTED 2026-07-12** — top-level agent, `AGENTS/HOMER/` (Will-directed; DAEDALUS review `AGENTS/DAEDALUS/builds/homer_promotion/PROMOTION_REVIEW.md`). No longer a CARL sub-agent / no longer spawned here — see `AGENTS/HOMER/STATUS.md` + `NEXUS_BRIEF.md` for live state. CARL retains 6 consumer-transmission rows (STATUS.md Housing section) + CRL-06/CRL-23 (parent-retained predictions, HOMER = data owner). | n/a — HOMER runs its own docket (`AGENTS/HOMER/docket/CATALYSTS.tsv`) |
| **DOC** | Healthcare costs (medical debt, OOP, care avoidance, GLP-1, ACA cliff) | **Aug 10** (refresh: med-debt aligned to DEWEY-C4 ~$195B; Med-CPI 2.0% YoY 3-mo low, P03 35→30; **DOC-P04 CONFIRMED** — rural closures 206>200, Chartis Feb-2026, sat unintegrated 6mo [process miss logged in SV]; GLP-1 OOP bifurcating; SV-DOC-2026-08-10-01) · prior Jun 8 data / 7/10 verify | ✅ verified CLEAN (exemplar build held); Apr CPI sign-flip hypothesis resolved MISS; TSV schema defects repaired (PREDICTIONS 8→9-col, ML stub padded); honest staleness banner. **⚠️ 7/31: `workbook/FLOW.tsv` 53d stale** (surfaced by the new `workbook/LEDGER_GLOB` declaration, STUE fix) — **✅ RESOLVED 8/10: FROZEN** (banner added; all 7 pathways conceptually valid, numbers-only staleness — the last rotting non-FROZEN sub-agent ledger is closed). | 7/14 June CPI 🔴 (ride-along, tagged 7/10) · ~Oct 30 DOC-P10 🟡 |
| **GIG** | Gig economy (oversupply, Dave provisioning, gas squeeze, AV) | **Aug 10** (Q2 platform prints: **Dave canary resolved REVERT** +151%→+14.3% YoY, **VX-GIG-3.08 CRITICAL→NORMAL ratified**; Uber/DD/Lyft supply MIXED — first Uber localized-tightness flags; gas VX-6.01 re-armed; SV-GIG-2026-08-10-01) · prior 7/10 reconciliation of Jun-22 data | ✅ current; **GIG-P03/P06 DUE-UNRESOLVED (Gridwise annual-only ×3 checks — re-instrumentation owed at parent; do NOT re-search)**; **AV_TRACKER.tsv ⛔ FROZEN 2026-08-12 by CARL** (last real refresh 7/08; PROME spawn-rider + DAEDALUS Sweep-#3 asks dispositioned — the sweep's one true rot item in the CARL tree). **Freeze ≠ the DOC/FLOW case: that was structural/date-insensitive, this is pure point-in-time numerics in a fast-moving domain, so the banner is an admission we are NOT tracking AV.** **Re-open trigger written onto GIG's own card: next spawn (~Nov) must EITHER re-pull the table from primary and lift the banner OR retire it — not neither.** Early re-open if the V7 FL-composition review needs a live AV number or any prediction gets instrumented on an AV series (none is today). | ✅ Dave-Q2 gate FIRED 8/10 (revert). Next: Q3 platform prints ~Nov (invalidation watch: Dave provision re-accel >+70% YoY) |

### Dossier-mode (ad-hoc spawns against the dossier; no standing refresh)

| Agent | Entry surface | State | Spawn trigger |
|-------|---------------|-------|---------------|
| **POP** | `POP/STATUS.md` (banner'd; rows are Apr-17 vintage, do not cite as current) + `state_vectors/SV-POP-2026-07-24-01.md` | **DEMOTED 2026-07-24** after the final refresh at its Sub-V-sunset gate: P01 ❌ MISSED (Ch-11 H1 +28% vs >40% bar), P02 ❌ MISSED at 80% (NFIB June **97.4 and rising**), P03 70→15%, P06 50→55% (monotonicity fix vs CARL CRL-15). Parent trims: CRL-15 65→35, CRL-17 55→40. Owed ad-hoc: P04 QSR pull, IEEPA rate tags, ML field drift. **8/10 narrow ad-hoc RAN** (CRL-16/17 evidence: no SB provision line at HBAN/ZION/OZK; Sub-V July +24% = 4th decel month; SV-POP-2026-08-10-01 + dated STATUS addendum; parent forced CRL-16 → MISSED) | Sub-V/SBA/NFIB shock, or the Q3 Epiq release (~Oct) for P03 |
| **POLLY** | `POLLY/STATUS.md` (final-refresh snapshot 8/10, vintage map in header) + `state_vectors/SV-POLLY-2026-08-10-01.md` (**DOSSIER CARRY LIST at bottom = the handoff, 9 items**) | **DEMOTED 2026-08-10** after the final gate-fired refresh (Will-approved sequencing; gate = Q2 P&C prints, fired late-Jul; CARL ratified 8/10): **P05 82→90 (HOLDS — ALL auto CR 83.3%/PGR 87.3% H1, 8-13pp under 95)** · P02 72→55 (CA FAIR net-add decel ×3 qtrs, ~705-716K EOY trend vs 750K bar — reverses April raise) · P03 60→85 (Citizens 278,196 flat, 30% under line) · ML-17/18 merged-line defect REPAIRED · ML-19 intact must-carry | Major cat event (hurricane/wildfire spiking FAIR/Citizens), a P05 breach quarter, or CMS 2027 OEP effectuated-enrollment data (CRL-22 leg B, ~Nov+) |
| **PHAN** | `PHAN/DOSSIER.md` (CLAUDE/STATUS FROZEN w/ Klarna-refuted warning) | 7/10 pass: 7 predictions dispositioned (P02 12% premise-refuted; P03 96% tracking-HIT on 1033 withdrawal), FLOW crosswalk reconciled (TSV numbering canonical); ⚠️ **`COCKROACH.tsv` + `REGULATORY.tsv` "stay live-append" (7/10) COLLIDED WITH DOSSIER-MODE and rotted to +37d — flagged every boot with no owner.** Both given **PAT-044 two-clock headers 8/15** (DATA clock 2026-07-10, hygiene clock 2026-08-15); **NOT frozen — the channels are live and a spawn is imminent.** | **Aug 20 Affirm FQ4** (8/20 CONFIRMED, after close) + Klarna Q2 ~mid-Aug. ⛔ **LEDGER SWEEP RIDES THIS SPAWN:** sweep events since 7/10 → advance the DATA clock, **or** record an explicit DID_NOT_APPEAR null. Advancing only the hygiene clock may not launder freshness. |

### Refresh-then-demote at catalyst (Will-approved sequencing — do NOT demote early)

| Agent | Domain | Last real refresh | Gate |
|-------|--------|-------------------|------|
| ~~**POLLY**~~ | ~~Insurance~~ | — | **✅ GATE FIRED late-Jul, final refresh RAN 2026-08-10 — POLLY DEMOTED to dossier-mode (CARL ratified).** Moved to the Dossier-mode table above. ML-POLLY-19 carried intact. |
| ~~**POP**~~ | ~~Small business~~ | — | **✅ GATE FIRED 2026-07-24 — final refresh RAN, POP DEMOTED to dossier-mode.** Moved to the Dossier-mode table above. |

### Frozen / dead

| Agent | Disposition |
|-------|-------------|
| **META** | FROZEN 7/10 (WP-2; RESEARCH_DIGEST harvested to DAEDALUS/reference/). Do not spawn. |
| **COOK** | Never built; **declared dead as a standing agent 7/10** (CARL disposition, DAEDALUS concurrence). If OBBBA/SNAP fires (Dec-2026 window) → DOC dossier-section or ad-hoc spawn. Plan git-recoverable at `0f2c59ab`. |

---

## REFRESH RULES (rewritten 2026-07-10 — catalyst-driven, replacing the never-held "3-7 day" cadence)

- **Spawn on catalyst, not calendar:** spawn a standing sub-agent when the docket (`docket/CATALYSTS.tsv`, `who_cares` column) shows its catalyst inside ~1 week, or when a domain shock fires (e.g., HAWK gas alert → GIG).
- **Staleness is a citation rule, not a spawn alarm:** a sub-agent's data older than its last catalyst = don't cite as current; STALE-tag on read. Between catalysts, stale-but-tagged is the EXPECTED state, not a violation.
- **Every refresh runs the SPAWN_PROTOCOL exit-checklist** (STATUS + every TSV touched-or-STALE-marked + due predictions dispositioned + SV to own `state_vectors/`). A refresh that only touches STATUS is a bypass.
- **Parent catch-up gathers write down same-session** or stamp `BYPASSED <date>` (SPAWN_PROTOCOL rule #10).

## UPCOMING CATALYSTS → `docket/`

Forward catalysts + owning sub-agent (`who_cares`) live in `docket/CATALYSTS.tsv` / `CALENDAR.md`; boot.py's docket countdown surfaces them. This file is roster + freshness + spawn rules only.
