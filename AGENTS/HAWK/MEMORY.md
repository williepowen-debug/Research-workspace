# MEMORY.md — HAWK Cross-Session Memory

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate.*

---

## Feedback
- [2026-02-18] VIX event trades on geopolitical catalysts have poor risk/reward (Aug 2024: 85% of VIX-65 spike was artificial). Equity puts (direct sector exposure) > VIX calls.
- [2026-04-01] Ceasefire fade protocol validated: 0/3 "diplomatic breakthroughs" were real (all Tier 4). "Diplomacy working" extension framing was a narrative trap.
- [2026-06-08] **Unconditional predictions have no void path** — only CONFIRMED/FAILED/PARTIALLY. VOIDED is reserved for conditional predictions whose premise fails (HAW-07 vs HAW-09/10/11). Prevents calibration inflation.
- [2026-06-08] **Conf-code discipline by source category** — Trump/Rubio forward rhetoric = D4; Iran adversarial framing = D3; multi-outlet kinetic = B2; IAEA primary = A2; analytical synthesis = F6. Pre-assign by category before writing KB rows.
- [2026-06-20] **See-saw discipline (Will).** Hold marks LOOSELY on this fast-oscillating conflict; discount single-day headlines BOTH ways. Declaratory≠physical, rhetoric≠resolution, mechanism≠threshold; the tape is the tie-breaker. A swing back to "peace" in 1-2 days is within base rate and won't by itself collapse D. Codified in STATUS posture box.

## Findings
- [2026-06-08] **Deferral-dynamic calibration anchor (HAW-06 FAILED).** This conflict produces armed pauses via ally-request deferrals, NOT clean breaks (or clean collapses). Don't over-predict clean state changes on deadline-shaped events.
- [2026-06-08] **FLOW = canonical, KB = pointer for synthesis claims.** Decoupling thesis lives at FLOW-HAWK-19; KB rows are one-line pointers w/ DerivedFrom chains. One source of truth per metric prevents file drift.
- [2026-06-08] **Falsification cross-link.** Thesis claim and its kill-switch live together via cross-ref (FLOW-19 ↔ HAW-11). Reader finds both from either entry; thesis can't drift from its kill condition.
- [2026-06-20] **Dormant-armed framing.** Apr-damage-regime vectors/flows aren't dead — muted by de-escalation, primed to re-fire on escalation. Reconcile stale escalation vectors as "MUTED, re-fires if X," not deleted. (See LESSONS dormant-vector re-sweep.)
- [2026-06-20] **Don't stack concurrent workflows / wide fan-out while siblings live** — API 529-overloads and drops RANDOM agents (lost the most-important theater, missed the Hormuz re-closure). Degrade to inline sequential WebSearch + harvest partials. (auto-memory finding-workflow-concurrency-529.)

## References
- [2026-04-01] Ceasefire fade protocol: `workbook/CEASEFIRE_FADE_PROTOCOL.md` · Four structural breaks: `workbook/FOUR_STRUCTURAL_BREAKS_MAR18.md`
- [2026-06-08] BRENT canonical for oil prices/storage/STEO/Iraq-production/Qatar-LNG/sulphur — defer per "one source of truth per metric"
- [2026-06-19] Cross-theater energy-strike ledger: `domain/energy-strikes/STRIKES.tsv` + `SUMMARY.md` (%-offline = sourced as-of, never sum-of-nameplates)

## Session Notes

### HISTORY THROUGH JUN 18 (compressed — detail in git/KB)
Apr 21 ceasefire-extend (HAW-06 FAILED) → May armed-pause + 14-pt MOU draft (never signed) → Jun 1 Iran walks talks → **Jun 8-11 multi-front re-ignition** (first US aircraft loss = Apache over Hormuz; Jordan new theater; Bab-al-Mandab kinetic activation 6/8-9; **Jun 11 formal Hormuz closure → Brent FELL = strongest decoupling datum**) → **Jun 17 Islamabad MOU SIGNED** (Trump+Pezeshkian; Khamenei 6/18) → Jun 18-19 Lebanon flare (≥47 killed) called off first Switzerland round.

### LAST SESSION (Jun 19-20 Sat — persistent boot w/ Will)
- **Boot gap-sweep** via workflow; **529 storm dropped 4/6 theaters incl Iran/Hormuz** → recovered gaps inline (sequential WebSearch). Lesson logged.
- **HAW-03 resolved FAILED** — US Venezuela intervention (Op Absolute Resolve, Maduro captured Jan 3) actually happened; STATUS carried "rhetoric only" ~5.5mo stale (dormant-vector lesson → LESSONS.md).
- **Re-mark whipsaw (cautionary):** AM B39/C44/D17 ("Lebanon cooled") → **PM CORRECTION B34/C44/D22** after Will flagged **Iran re-declared Hormuz CLOSED Jun 20** ("first step", contested/declaratory; CENTCOM: traffic flows) — the AM sweep had 529'd the Iran theater so I'd marked a de-escalation off a half-picture. HAW-14 pulled off toward_confirm (Iran acted via coercive non-kinetic lever).
- **Full file catch-up:** VX all 18 vectors → Jun-20 (TRADE/SHADOW refreshed w/ live data; oil vectors deferred BRENT/SAM; ISR/FININFRA/CEASEFIRE superseded/dormant-armed); FLOW 15 damage-regime → MUTED dormant-armed (FLOW-07/08/12 kept active; 19/20 stamped); SUMMARY + STRIKES (Tyumen Jun 20, HAW-15 no_change). **See-saw posture box** added to STATUS.
- **KB +7** (194-200). **BRENT** cross-read + outbox sync note; BRENT independently confirmed the re-closure (their THESIS v4.1, conf 0.82) — fleet converged.
- **Commits e3f3a8cb / baf55b3c / 764fe4da — ALL LOCAL, UNPUSHED.** ⚠️ **PENDING PUSH (Will-coordinated).** Branch ahead 6 (HAWK 3 + BRENT + SAM); own-dir disjoint = clean merge.

### NEXT SESSION (Monday Jun 22 — priority order)
1. **🔴 MONDAY-OPEN DECOUPLING TEST** — Brent reprices the Jun-20 Hormuz re-closure: **spike = thesis BREAKS (toward D); shrug = HOLDS (toward C).** Read the open against B34/C44/D22. Defer price to BRENT; I read the geopolitical verdict.
2. **HAW-11 resolves Jun 22** — Gulf energy-infra-hit window closes; EXPIRE-leaning (no hit Jun 13-20) but re-closure raises final-day tail-risk. Resolve at boot.
3. **Hormuz** — did the re-closure stay declaratory (CENTCOM: traffic flows) or get enforced (mine/kinetic)? UKMTO/ship-tracking. Did the **Switzerland round convene** (HAW-12, targeting wk-Jun22)?
4. **Lebanon** — hold-fire hold or break? Iran "second step" → kinetic (HAW-14 FAIL) or stays sub-kinetic?
5. **Carry-over backlog:** THESIS.md rewrite (badly stale, v1.2 frozen Apr-20); HAWK CLAUDE.md Tier-2 (boot.py / docket/CATALYSTS.tsv / NEXUS_BRIEF write-back into SPAWN PROTOCOL); Kharg/US-strikes-on-Iranian-energy-infra channel still has no HAW-xx coverage.
