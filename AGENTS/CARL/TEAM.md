# CARL Sub-Agent Team

**Updated:** 2026-07-10 PM (Fable orchestration session — full roster truth-up after the DAEDALUS restructure [WP1-4] + CARL-directed verification/repair passes on STUE/HOMER/DOC/GIG/PHAN. GIG reconciliation RATIFIED + APPLIED same day; PHAN → DOSSIER; META → FROZEN; POLLY Last-Refresh corrected to Apr-29.)

> **Freshness discipline (2026-07-10):** the Status/ages below are hand-written snapshots as of the Updated stamp — **verify against each sub-agent's `STATUS.md` mtime before trusting** (`ls -l sub_agents/*/STATUS.md`). Freshness keys on the CANONICAL SURFACE's own state, never on SV-receipt (PAT-044: the Jun-22 GIG SV was marked "🟢 fresh" here while GIG's STATUS rotted 66d into asserting falsified facts). Mtime-derived ages in boot.py = open build item (pairs with consistency_check).

---

## ROSTER

### Standing sub-agents (spawn per docket catalysts)

| Agent | Domain | Last real refresh | Canonical-surface state (7/10) | Next catalyst (docket) |
|-------|--------|-------------------|-------------------------------|------------------------|
| **STUE** | Student loans (DQ, SAVE→RAP, servicers, Treasury collections) | **Jun 9** (data) · 7/10 verify/repair pass | ✅ verified; workbooks two-stated (STATE_DQ FROZEN; SERVICER/CASCADE/TIMELINE live w/ STALE tags); no own PREDICTIONS.tsv (its predictions ARE parent CRL-04/05/13/14 — accepted 7/10) | ~Jul 15 Treasury Phase 1 🔴 |
| **HOMER** | Housing (foreclosures, MF DQ, builders, state-level) | **Jun 8** (data) · 7/10 verify/repair pass | ✅ verified; CRL-03 parent-invalidation stamped ×6; KB.tsv FROZEN (delegation provenance protected); SV-02 refiled; 4 build-vintage docs → archive/. **Owes a real data-refresh spawn** (live TSVs Jun-8 vintage) | ~Jul 16 ATTOM Q2 🟠 + ~Jul 22 builders 🟠 |
| **DOC** | Healthcare costs (medical debt, OOP, care avoidance, GLP-1, ACA cliff) | **Jun 8** (data) · 7/10 verify pass | ✅ verified CLEAN (exemplar build held); Apr CPI sign-flip hypothesis resolved MISS; TSV schema defects repaired (PREDICTIONS 8→9-col, ML stub padded); honest staleness banner | 7/14 June CPI 🔴 (ride-along, tagged 7/10) · ~Oct 30 DOC-P10 🟡 |
| **GIG** | Gig economy (oversupply, Dave provisioning, gas squeeze, AV) | **7/10 RECONCILIATION** (data as-of **Jun-22**, not a fresh pull) | ✅ reconciled + ratified: FL-gas leg SIGN-INVERTED (struck), **Dave 28DPD canary RETIRED** → provisioning (VX-GIG-3.08, bands ⚠ Will-review); P01/P08 MISS, P02 50%; AV surface [STALE Apr-17]; do-not-cite banner LIFTED | Q2 platform earnings ~Aug (Dave provision persist-vs-revert = the new tell) |

### Dossier-mode (ad-hoc spawns against the dossier; no standing refresh)

| Agent | Entry surface | State | Spawn trigger |
|-------|---------------|-------|---------------|
| **PHAN** | `PHAN/DOSSIER.md` (CLAUDE/STATUS FROZEN w/ Klarna-refuted warning) | 7/10 pass: 7 predictions dispositioned (P02 12% premise-refuted; P03 96% tracking-HIT on 1033 withdrawal), FLOW crosswalk reconciled (TSV numbering canonical); COCKROACH.tsv + REGULATORY.tsv stay live-append | ~Aug 13 Affirm FQ4 + Klarna Q2 (docket row live) |

### Refresh-then-demote at catalyst (Will-approved sequencing — do NOT demote early)

| Agent | Domain | Last real refresh | Gate |
|-------|--------|-------------------|------|
| **POLLY** | Insurance (P&C, FAIR plans, MA culling, FL/CA) | **Apr 29** *(TEAM previously said Apr-17 — corrected 7/10 per audit)* | Q2 P&C prints ~late Jul → final refresh (must-carry: ML-POLLY-19 MA/OBBBA synthesis), then dossier |
| **POP** | Small business (Sub-V, closures, owner income, tariff) | **Apr 17** | **Jul 24 Sub-V Sec 122 cliff** (dual catalyst) → final refresh (resolve P01-P08, absorb NFIB ×3 + Sub-V decel; deep-dives survive verbatim), then dossier |

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
