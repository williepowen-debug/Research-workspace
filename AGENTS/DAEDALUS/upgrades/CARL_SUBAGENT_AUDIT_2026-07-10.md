# CARL Sub-Agent Structure Audit — 2026-07-10

**By:** DAEDALUS (Will-requested: "I imagine they are not built out correctly") · **Method:** Mode-A 4-reader fan-out (STUE+HOMER / DOC+GIG / PHAN+POLLY / POP+META, every file read incl. TSVs) + DAEDALUS cross-cutting checks (CARL-side wiring, KB delegation, COOK trace). **Read-only — no CARL files touched.** CARL was LIVE during the audit.
**Feeds:** `outbox/2026-07-10_to-CARL_upgrade-docket.md` item #9 (restructure) · FLEET_MAP CARL row · profiles/CARL.md refresh (pending CARL closeout).

---

## Headline answer

**The builds were mostly good; the answer to "not built out correctly" is: built correctly, maintained incorrectly, from a template with defects.** Verdict distribution: 2 WELL-BUILT (DOC, POP) · 5 BUILT-BUT-DRIFTED (STUE, HOMER, GIG, PHAN, POLLY) · 1 PARTIALLY-BUILT/ABANDONED (META). None is scaffold-only. The real defects are three systemic classes, not eight bad builds:

1. **Template-origin flaws stamped into every sub-agent** (the literal "built incorrectly" part):
   - Dangling `../SHARED/state_vectors/incoming/` SV-delivery path — **SHARED never existed** (confirmed in ≥6 of 7 monitoring agents). Each agent improvised its own channel (own `state_vectors/`, `outbox/`, top-level handoff file) — none matching the documented protocol.
   - **Hardcoded "Current" data values in CLAUDE.md threshold tables** — an instructions file that rots independently of STATUS (all agents; STUE shows 9.6% vs breached 10.3%, DOC shows Feb CPI 3.4% vs Apr 2.5%).
   - Key-Files blocks referencing `sources/`/`archive/` dirs that don't exist (several pruned by public-prep `1cb18fbc` — the docs never updated).
2. **Two-layer decay: the live layer works, the durable layers fossilize.** Where refreshes happen (STUE Jun-9, HOMER/DOC Jun-8) they update STATUS + state-vectors **only** — workbook TSVs and CLAUDE.md anchors stay at April build vintage. HOMER's "canonical" KB.tsv (the delegation contract behind 47 CARL KB rows) dead since Apr-29; STUE's 4 TSVs untouched at its own Jun-9 refresh. The DATA-REFRESH template says "update STATUS.md **and workbook TSVs**, log a KB row" — the TSV/KB half is systematically skipped.
3. **No downward propagation from parent thesis moves.** CARL froze `workbook/VX.tsv` on 6/26 → STUE/HOMER CLAUDE.md still cite VX-CARL rows as a live surface. CARL invalidated **CRL-03** at v2.6.1 (Jul-2) → HOMER's entire CRL-03 decision apparatus unmarked. CARL's parent-level Klarna-profitable (May-14) and Sub-V-decel (May +36%) facts → PHAN and POP dashboards still assert the refuted priors.

## The bypass, forensically confirmed (GIG)

The Jun-22 GIG "refresh" was a **CARL-side catch-up gather** (workflow `w95yzkviz`), not a sub-agent session. It wrote **only** `outbox/SV-GIG-2026-06-22-01.md`; TEAM.md marked GIG "🟢 fresh (Jun 22)" — freshness keyed on SV receipt, not canonical-surface state. Result: GIG's canonical STATUS now **asserts falsified facts**:

| Fact | STATUS.md (canonical, Apr-17) | Reality (Jun-22 SV, outbox-only) |
|---|---|---|
| FL gas divergence (thesis leg) | $4.093 **ABOVE** national | $3.617 **BELOW** national — **leg inverted** |
| Dave 28DPD (PRIMARY CANARY) | 1.89%, Q1 TBD | Q1 1.69% record low + provision +151% — SV reframes the canary itself as survivorship-biased |
| Natl gas | $4.076 🔴 FIRED | peaked $4.50 May-11, receding $3.929 *(CORRECTED per WP-4: "breach never recorded" was imprecise — CARL parent DID record AAA $4.564 on 5/21, graded partial-not-sustained; the gap is GIG-side only)* |
| Platform oversupply | inferred | Lyft −$12.8M incentives, DoorDash $100M gas subsidy, 2.7× extraction — nowhere in workbook |

Violates SPAWN_PROTOCOL:203 ("if it's not in STATUS.md or a workbook TSV, it didn't happen") — the protocol's own canon says the Jun-22 refresh *didn't happen*. Contrast DOC's Jun-8 refresh (a real sub-agent session): full contract maintained, diff table, STALE markers, SVs delivered AND integrated. **The failure discriminator is spawn type, not build quality.**

## Prediction-ledger rot (nobody's due-scan covers sub-agents)

CARL's boot scans its own PREDICTIONS.tsv — no mechanism scans sub-agent ledgers. Current state: **GIG** 4 predictions unresolved 54+ days past their May 6-7 resolvers (P01 is a resolvable **MISS** at 1.69%); **POP** P01-P08 open with April confidences (P03 +80%-by-Q3 likely wrong post-decel; P04 window expired unresolved); **PHAN** 7 predictions at Apr-9 confidences; **POLLY** 8 (with invalidation criteria, best hygiene). ~27 open sub-agent predictions with zero resolution machinery.

## Per-agent verdicts + dispositions

| Agent | Verdict | Disposition (audit-calibrated) | Key facts |
|---|---|---|---|
| **DOC** | **WELL-BUILT** | **KEEP** — the model build; use as the template exemplar | Full contract conformance; diff-table refresh discipline; only defects = dangling dirs + 32d stale (its Apr CPI sign-flip call FAILED per May print — needs respawn to absorb) |
| **HOMER** | BUILT-BUT-DRIFTED | **KEEP** | Strongest structure (5 live TSVs, calibration postmortem, corrected/ audit-trail convention); KB.tsv dead since Apr-29; CRL-03 invalidation unpropagated |
| **STUE** | BUILT-BUT-DRIFTED | **KEEP** | Excellent STATUS/SV discipline incl. self-corrections; workbooks decoupled since April |
| **GIG** | BUILT-BUT-DRIFTED | **KEEP, but reconciliation spawn FIRST** — fold Jun-22 SV into STATUS/workbook, resolve P01 MISS, reconcile CRL-08 gas history GIG-side (parent already recorded+graded it), fix inverted FL-gas leg | Canonical surface asserts falsified facts; sole record of Q1 platform integration lives in one outbox file |
| **POP** | **WELL-BUILT** | **REFRESH-THEN-DEMOTE** — one final spawn at the **Jul-24 dual catalyst** (Sub-V print + Section 122 expiry, 14d out, currently unowned): resolve P01-P08, absorb NFIB×3 + Sub-V decel, then flatten to dossier | Best conformance of the demotion candidates; both deep-dives (SB→KRE/OZK/WAL pipeline; invisible-income $73-145B) must survive **verbatim** |
| **POLLY** | BUILT-BUT-DRIFTED | **REFRESH-THEN-DEMOTE** at Q2 P&C prints (~late Jul) — or demote now + reroute docket `who_cares=POLLY` rows to CARL-direct | ML-POLLY-19 MA-cost-trend/OBBBA (Dec-30-2026) synthesis exists nowhere at parent; TEAM.md date wrong (actual last session Apr-29 not Apr-17) |
| **PHAN** | BUILT-BUT-DRIFTED | **DEMOTE-WITH-CARE** (no catalyst gate — Affirm/Klarna Q2 ~Aug can be an ad-hoc spawn against the dossier) | Dashboard asserts refuted Klarna narrative, zero STALE marks; must-carry: COCKROACH.tsv + REGULATORY.tsv (unique fleet assets), FLOW pathways, 7 predictions, phantom-DTI framework |
| **META** | PARTIALLY-BUILT / ABANDONED | **HARVEST-THEN-FREEZE** — copy `core/RESEARCH_DIGEST.md` out (sole surviving copy of the 6-framework methodology digest; its sources were pruned from the repo), then FROZEN banner | Primary deliverable missing, all 6 research inputs gone, zero consumption, predates the contract, reports to "human operator" not CARL |

Also: **COOK** (9th, never-built) — 182-line buildout plan (food+SNAP stress, pairs with DOC on OBBBA safety-net erosion) committed Apr-17 "for next session," never executed, archived Jun-26, deleted in public-prep prune. Git-recoverable (`0f2c59ab`). Needs explicit disposition: build (OBBBA SNAP window starts Dec-2026 — not moot) or declare dead. **DAEDALUS lean: dead as a sub-agent; if the OBBBA thread heats up, it's a DOC dossier-section or ad-hoc spawn, not a 9th standing agent.**

## Must-fix list if the layer survives in any form

1. **DATA-REFRESH template**: add "touch every workbook TSV or STALE-mark it; resolve any prediction past its resolver" — the TSV half of the existing template is systematically skipped; make it a checklist, not prose.
2. **Kill the SHARED ghost**: document the real SV channel (own `state_vectors/` or `outbox/` — pick ONE) in all CLAUDE.md files; delete the `../SHARED/` protocol text.
3. **De-hardcode CLAUDE.md threshold "Current" columns** — thresholds/bands stay (durable), live values move to STATUS only (or get an as-of date at minimum).
4. **TEAM.md freshness = mtime-verified**, not SV-receipt (boot.py job — docket #1/#7c). The GIG row proves hand-marking is worse than nothing: it laundered a bypass into "🟢 fresh."
5. **Downward-propagation hook**: when CARL freezes a workbook surface, invalidates a CRL, or supersedes a sub-domain fact at parent level, the owning sub-agent's surfaces get a same-session write-down or `BYPASSED <date>` stamp (docket #9d).
6. **Prediction due-scan globs sub-agent ledgers**: `sub_agents/*/workbook/PREDICTIONS.tsv` into CARL's boot due-scan (natural boot.py extension).
7. **Orphan hygiene**: PHAN/GIG top-level `CARL_HANDOFF_20260417.md` → outbox or archive (PHAN's is load-bearing history — KB-CARL-228 cites it; move, don't delete); HOMER's valid SV-02 filed under `corrected/` (retrieval hazard).

## Pattern candidates (DAEDALUS ledger)

- **PAT-043 (candidate): sub-agent layers decay from the durable end.** Live surfaces (STATUS/SV) keep working while instruction files and workbooks fossilize at build vintage — the inverse of ledger-rot (where dashboards rot and docs survive). Tell: mtime spread within one agent dir (STATUS fresh, CLAUDE/TSVs at build date). Same class as the fleet's PAT-032/PAT-035 but at the nested layer nobody's staleness enforcer globs (`ledger_staleness.py` doesn't reach `sub_agents/*/workbook/`).
- **PAT-044 (candidate): a coordinator's freshness ledger keyed on deliverable-receipt launders bypasses.** TEAM.md marked GIG "fresh" because an SV arrived — the canonical surfaces the SV was supposed to update were 66d stale and now assert falsified facts. Freshness must key on the canonical surface's own state.

---

*Reader reports (4× ~900w) synthesized 2026-07-10; full transcripts in session task outputs. Next: docket #9 updated with these calibrations; profile/card refresh + FLEET_MAP note after CARL closeout.*
