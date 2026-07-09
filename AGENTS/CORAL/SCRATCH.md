# CORAL SCRATCH — 2026-07-09 (catch-up session, 14-day gap; 2 passes)

**Purpose:** Canonical ephemeral session handoff. Read at boot; rewrite at closeout. Durable findings → `MEMORY.md`/workbook; live state → `STATUS.md`.

---

## CHANGES SINCE LAST SESSION

**Pass 1 (16:55 ET):** Spawned by PROME for a catch-up session (14-day gap, stalest in fleet). Drained 8 scoped inbox items, resolved AEOLUS boundary handshake, refreshed STATUS/SCRATCH, stated forward-prep watch items. Full detail in prior SCRATCH revision (superseded by this rewrite) + `CATCHUP_2026-07-09.md`.

**Pass 2 (17:35 ET, same evening, Will-approved):** PROME follow-up — drain the full WALTER SIG backlog flagged in Pass 1 (18 items) + a 2-item PROME routing bundle (MARCO migration reconcile, AEOLUS C1 sharpen). This pass produced **real thesis-relevant updates**, not just housekeeping:
- **Property-tax amendment (pillar 9) MAJOR rewrite** — Amendment 3/HJR 1F is verified-primary CERTIFIED (was a vague "🔴 ballot watch" placeholder since 6/19). New CRE/MF/business burden-shift headwind identified (extends DEWEY's original framing).
- **Hurricane forecast MATERIAL update** — CSU cut twice since the 6/19 dashboard figure (14/7/3 → 11/5/2 → **9/4/1**, fewest since 2014). This was stale on the dashboard for 3 weeks; caught this pass via the AEOLUS ENSO reconcile ask.
- **Neg-equity refresh** — Cape Coral 10.1%→11.1% (2nd independent source), 2024-vintage cohort 35.4%, Lakeland 10.8% added.
- **Fire-sale consolidation** — 3 overlapping Parcl-MSI-family WALTER signals (004/011/627-003) reconciled to one read instead of risking triple-counting.
- **Insurance — 2 new structural threads** — construction-insurance *availability* block (not just price) on a $1.6B Miami tower; flood-uninsured mortgage-credit tail (FL ~18% of NFIP policies).
- **Migration divergence CLOSED** (routing bundle #1) — BofA Q1 metro-negative claim vs MARCO's canonical +22,517: documented as different vintage/basis, MARCO's figure adopted explicitly as canonical, no CORAL number changed.
- **Citizens/depopulation scope flag OPENED, not resolved** (routing bundle #2) — CORAL's 294,253 (personal-lines) vs AEOLUS's ~395K (scope unspecified) are plausibly different line-scopes, not a contradiction, but unverified — carried as an open question, not silently reconciled either way.

## WHAT I DID THIS SESSION

**Pass 1:** boot chain read, 8-item scoped inbox drain, AEOLUS handshake resolution, STATUS/SCRATCH/COVERAGE updates, forward-prep table, CATCHUP note, commit `f1617d32`.

**Pass 2:**
- Read all 18 remaining WALTER SIGs (`inbox/WALTER/`, oldest 2026-06-26 SIG-004 → newest 2026-07-04 SIG-006) + the ENSO routing NOTICE + the PROME routing bundle.
- `git mv` all 19 WALTER-lane files to `inbox/WALTER/processed/`; `git mv` the routing bundle to `inbox/processed/`.
- Logged 19 disposition rows to `board_log.tsv` (oldest-first, one line each — acted/noted/superseded, no LAPSED candidates found in this batch — none carried a hard watch-window that passed unmet).
- **Major STATUS.md rewrite**: new "7/9 EVENING — WALTER BACKLOG SWEEP" block (9 numbered sub-sections covering all 18 signals + both routing-bundle items); updated dashboard rows (neg-equity, hurricane forecast) and pillar-table rows (migration, CRE, state fiscal, labor, insurance-commercial); added 2 new Open Questions (hurricane asymmetry watch, Citizens-scope reconcile). STATUS still 171 lines (under the 250-line cap).
- Cross-read `AGENTS/MARCO/STATUS.md` (migration canonical figure + its own divergence-flag language, commit `a95631b7`) and `AGENTS/AEOLUS/STATUS.md` (C1 ENSO figures, Citizens ~395K/−8.7%/17+carriers) to do the reconcile — did NOT edit either file (not CORAL's to write; per fleet rule, own the FL-specific number, cite the other agent's file for their side).

## NEXT SESSION

1. **Citizens scope reconciliation (unresolved, flagged this session)** — pull Citizens' own filing/dashboard to confirm whether CORAL's 294,253 (personal-lines) and AEOLUS's ~395K are genuinely different line-scopes or an actual conflict. Don't carry both silently past one more session.
2. **Pull current Parcl MSI dashboard live** — the fire-sale tripwire (MSI >6.0 across ≥5 FL metros, 2+ wks) is pre-registered but has never been checked against a live pull, across two sessions now.
3. **Ballot-language lawsuit + re-pull polling** on Amendment 3/HJR 1F before sizing anything off the 64%±3.8 poll (DEWEY's own caveat, not yet actioned).
4. **Q2 FL bank earnings** (~7/21-28, TBC) — the bank-transmission gate re-test, unchanged from Pass 1.
5. **Verify exact Q2 earnings + FL State Employment release dates** (still TBC placeholders).
6. **Per-metro convergence grid** and **MARCO Miami-Dade condo-supply reconcile** — both carried over multiple sessions now, still not built.

## OPEN THREADS

- **Bank-transmission gate:** unchanged, NOT met; Q2 prints are the live re-test.
- **Citizens scope flag:** open, needs primary-source resolution (see Next Session #1).
- **Property-tax amendment:** now has a verified-primary structure and a sharpened two-sided read (homeowner tailwind vs CRE/MF headwind vs muni-fiscal tail); P(pass) tight, watch the lawsuit + repolling.
- **Hurricane/ENSO:** season forecast keeps cutting (now 9/4/1) under a soft reinsurance market — AEOLUS's asymmetry framing adopted; watch for any August upward revision (bear-thesis threat) or landfall (bull-thesis trigger).
- **Substance-vs-beta:** unchanged from Pass 1 — FL's macro-independence from the fleet's energy/rates sequence holds after two passes of new inbound data.

## MAIL STATE

- `inbox/`: **0 pending** (root — all items processed across both passes today).
- `inbox/WALTER/`: **0 pending** — full backlog cleared this session (4 items Pass 1 + 18 items + 1 notice Pass 2 = 23 total WALTER-lane items processed today).
- `outbox/`: none written — no 🔴 acute signal either pass; all cross-agent items are LIST-only per catch-up rules.
- **Pending push:** local commits only, per fleet auto-push-at-closeout (PROME/Will-coordinated). Queue: 1d371108, 245cfc52, ee8c195e (6/25) + f1617d32 (7/9 Pass 1) + this session's Pass-2 commit, still pending push per prior SCRATCH notes.
