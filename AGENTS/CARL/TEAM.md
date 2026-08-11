# CARL Sub-Agent Team

**Updated:** 2026-08-10 (Mon eve — **STUE is PAST-DUE: no run since 7/31, its ~8/5 Treasury Phase 1 verification catalyst expired unrun (re-dated ~8/13) and 3 inbox packets sit unprocessed** incl. the PROME audit hand-downs the 8/3 session expected verified "at its ~8/5 run" — **spawn owed this week, ideally post-HHDC** (same print feeds its CRL-04/13 reads). No sub-agents spawned tonight — the BOARD clerk was an anonymous task spawn, not a roster agent. GIG's Dave-Q2 catalyst (~Aug, provisioning persist-vs-revert) is approaching; PHAN's Affirm FQ4 8/20 confirmed.) Prior 2026-08-03 (Mon — **inbox layer built for all six remaining sub-agents per Will's 8/2 ruling**; see the section directly below. Also: DOC `workbook/FLOW.tsv` remains **53d+ stale** from the 7/31 LEDGER_GLOB run — FROZEN-or-refresh at DOC's next spawn, now noted on DOC's own card.) Prior 2026-07-24 (Fri catch-up, SECOND PASS — **POP refresh-then-demote EXECUTED at parent level** [Will-directed]: gate fired, 4 predictions dispositioned incl. two MISSES, a parent↔sub-agent monotonicity bug found and fixed, POP moved to dossier-mode; `SV-POP-2026-07-24-01.md`. First pass — the budget went to the earnings cluster + energy regime + a 46-signal BOARD backlog. Two roster consequences recorded honestly rather than silently: **(1) POP's refresh-then-demote GATE FIRED TODAY** (Jul-24 Sub-V debt-threshold sunset) **— initially NOT run in the first pass, then RUN in the second pass per Will's direction** — POP stays at its Apr-17 vintage, now openly past its own gate; the docket row was pruned (the event fired) but the owed work moved to a ROADMAP open thread, and it feeds CRL-15/16/17 with **CRL-16's window closing 8/31**. **(2) POLLY's gate (Q2 P&C prints, ~late Jul) is effectively open now** and has acquired a new must-do: **CRL-22 re-spec v3**, because v2's ELV leg names an FY BCR guide that ELV does not publish. Also: **ELV reported 7/15, not 7/22** — the 7/18 POLLY SV pass built an ELV-7/22 watch card against a print that had already happened.) Prior 2026-07-18 (Sat Fable wave — **POLLY targeted pre-catalyst SV pass** [SV-POLLY-2026-07-18-01: UNH Q1-baseline EDGAR verify → CRL-22 re-spec v2; ELV 7/22 watch card; ML-19 intact]. NOT a full refresh — POLLY's refresh-then-demote gate stays at Q2 P&C prints ~late Jul. Other wave agents [BOARD-CLERK/EARNINGS-PREP/BUILDER] were anonymous task spawns, not roster sub-agents. POP untouched, gate = Jul-24 Sub-V sunset.) Prior 2026-07-10 eve (Fable orchestration session — full roster truth-up after the DAEDALUS restructure [WP1-4] + CARL-directed verification/repair passes on STUE/HOMER/DOC/GIG/PHAN. GIG reconciliation RATIFIED + APPLIED same day; PHAN → DOSSIER; META → FROZEN; POLLY Last-Refresh corrected to Apr-29. **EVE: all 7 dirs staleness-swept honest** — POLLY/POP restamped + banner'd [Apr-vintage declared, refresh gates unchanged], contradictions tagged [STUE collections-restart, POP Sub-V accel framing, HOMER Freddie-HPI hypothesis], 12 files retired. Per-agent refresh briefs → ROADMAP remaining-lanes thread.)

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
| **STUE** | Student loans (DQ, SAVE→RAP, servicers, Treasury collections; **+SLABS collateral-transmission + higher-ed institutional stress, Will-ruled 7/31** — neither creates a CRL row) | **Jul 25** (data — the Jul-15-fired gate discharged; 2 packets: CRL-14 55%/STUCK Will-approved + cascade-rescope + CRL-13 window compression; applied at parent 7/31) | ✅ current; SV-STUE-2026-07-25-01; no own PREDICTIONS.tsv (its predictions ARE parent CRL-04/05/13/14 — accepted 7/10). **📬 HAS AN INBOX (Will-ruled 7/31, first sub-agent with one): route STUE-destined mail to `sub_agents/STUE/inbox/` directly — CARL is no longer the letterbox. ⚠️ STUE boots ~5×/qtr: time-critical routes keep a CARL-docket copy.** PROME audit hand-downs (VASP category error + monotone law) DELIVERED to that inbox 7/31 eve — verify processed at its ~8/5 run. | ~Aug 5 Treasury Phase 1 first-batch verification 🟠 |
| **HOMER** | Housing (foreclosures, MF DQ, builders, state-level) | **PROMOTED 2026-07-12** — top-level agent, `AGENTS/HOMER/` (Will-directed; DAEDALUS review `AGENTS/DAEDALUS/builds/homer_promotion/PROMOTION_REVIEW.md`). No longer a CARL sub-agent / no longer spawned here — see `AGENTS/HOMER/STATUS.md` + `NEXUS_BRIEF.md` for live state. CARL retains 6 consumer-transmission rows (STATUS.md Housing section) + CRL-06/CRL-23 (parent-retained predictions, HOMER = data owner). | n/a — HOMER runs its own docket (`AGENTS/HOMER/docket/CATALYSTS.tsv`) |
| **DOC** | Healthcare costs (medical debt, OOP, care avoidance, GLP-1, ACA cliff) | **Jun 8** (data) · 7/10 verify pass | ✅ verified CLEAN (exemplar build held); Apr CPI sign-flip hypothesis resolved MISS; TSV schema defects repaired (PREDICTIONS 8→9-col, ML stub padded); honest staleness banner. **⚠️ 7/31: `workbook/FLOW.tsv` 53d stale** (surfaced by the new `workbook/LEDGER_GLOB` declaration, STUE fix) — **FROZEN-banner-or-refresh at next DOC spawn**; the only non-FROZEN sub-agent ledger rotting. | 7/14 June CPI 🔴 (ride-along, tagged 7/10) · ~Oct 30 DOC-P10 🟡 |
| **GIG** | Gig economy (oversupply, Dave provisioning, gas squeeze, AV) | **7/10 RECONCILIATION** (data as-of **Jun-22**, not a fresh pull) | ✅ reconciled + ratified: FL-gas leg SIGN-INVERTED (struck), **Dave 28DPD canary RETIRED** → provisioning (VX-GIG-3.08, **bands Will-approved provisional 7/10**, re-cut pre-registered at Dave Q2 ~Aug); P01/P08 MISS, P02 50%; AV surface [STALE Apr-17]; do-not-cite banner LIFTED | Q2 platform earnings ~Aug (Dave provision persist-vs-revert = the new tell) |

### Dossier-mode (ad-hoc spawns against the dossier; no standing refresh)

| Agent | Entry surface | State | Spawn trigger |
|-------|---------------|-------|---------------|
| **POP** | `POP/STATUS.md` (banner'd; rows are Apr-17 vintage, do not cite as current) + `state_vectors/SV-POP-2026-07-24-01.md` | **DEMOTED 2026-07-24** after the final refresh at its Sub-V-sunset gate: P01 ❌ MISSED (Ch-11 H1 +28% vs >40% bar), P02 ❌ MISSED at 80% (NFIB June **97.4 and rising**), P03 70→15%, P06 50→55% (monotonicity fix vs CARL CRL-15). Parent trims: CRL-15 65→35, CRL-17 55→40. Owed ad-hoc: P04 QSR pull, IEEPA rate tags, ML field drift | Sub-V/SBA/NFIB shock, or the Q3 Epiq release (~Oct) for P03 |
| **PHAN** | `PHAN/DOSSIER.md` (CLAUDE/STATUS FROZEN w/ Klarna-refuted warning) | 7/10 pass: 7 predictions dispositioned (P02 12% premise-refuted; P03 96% tracking-HIT on 1033 withdrawal), FLOW crosswalk reconciled (TSV numbering canonical); COCKROACH.tsv + REGULATORY.tsv stay live-append | ~Aug 13 Affirm FQ4 + Klarna Q2 (docket row live) |

### Refresh-then-demote at catalyst (Will-approved sequencing — do NOT demote early)

| Agent | Domain | Last real refresh | Gate |
|-------|--------|-------------------|------|
| **POLLY** | Insurance (P&C, FAIR plans, MA culling, FL/CA) | **Apr 29** *(TEAM previously said Apr-17 — corrected 7/10 per audit)* | Q2 P&C prints ~late Jul → final refresh (must-carry: ML-POLLY-19 MA/OBBBA synthesis), then dossier |
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
