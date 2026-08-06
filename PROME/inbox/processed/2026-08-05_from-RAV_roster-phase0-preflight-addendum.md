# RAV Preflight Addendum - Roster Phase 0 / Phase 1

Date: 2026-08-04
Prepared by: RAV
Scope: read-only Research-workspace preflight after PROME Phase 0 closeout
Reference mirror: `/home/moltbot/research-workspace-readonly` at `08c136741`
No Research-workspace edits made.

## Bottom Line

PROME's narrowed Phase 1 scope holds.

The roster problem is local to `PROME/ROSTER.md`'s `ACTIVE -- persistent domain owners (30)` bucket. The rest of `ROSTER.md` already separates Tier-2, dormant, retired, archive-source, special, tool-class, spinout provenance, and explicit unowned gaps. Phase 1 should split the misleading ACTIVE bucket only.

No ruling breaks in this preflight. I do not recommend re-cutting the taxonomy before Phase 1.

## Design-Affecting Facts

1. Root `CLAUDE.md` is the material active-list mirror.

   It carries the full active/Tier-2/special line at root `CLAUDE.md:26`, is boot-loaded fleet-wide, and cites `PROME/ROSTER.md`. This should remain a named Will-gated Phase 1 step.

2. I did not find a second root-style auto-injected active-list mirror in live boot/nav markdown.

   `AGENTS.md`, `README.md`, `PROME/BOOT.md`, `PROME/CLAUDE.md`, and `AGENTS/_NETWORK.md` mostly point back to `PROME/ROSTER.md`. `AGENTS/_INDEX.md` does carry a canonical roster table and must align in Phase 1, but it is a navigation table, not the same kind of auto-injected root canon mirror.

3. `AGENTS/_INDEX.md` is a real Phase 1 participant.

   It currently groups active + Tier-2 + meta agents under one canonical roster table. It should be aligned with the descriptive bucket split or it will preserve the old mixed mental model.

4. DAEDALUS registry ownership is real.

   `AGENTS/DAEDALUS/sweeps/REGISTRY.tsv` already owns recurring sweep cadence, and `sweeps_due.py` checks it. PROME's C3 correction stands: service rules should register into that mechanism at Phase 2, not become ROSTER prose.

5. NEXUS already owns brief schema and brief freshness/order invariants.

   `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` explicitly locks amendment 10: brief fold is the last write-back. This supports the plan's split: NEXUS owns synthesis-read/order mechanics; PROME should consume the compact decision packet.

## ACTIVE(30) Proposed Buckets

This is a preflight classification, not an edit.

| Bucket | Agents | Notes |
|---|---|---|
| ORGANIZING / SERVICE | PROME, WALTER, NEXUS, TERRY | Not persistent domain owners. PROME = operator rail; WALTER = intake/delivery; NEXUS = synthesis; TERRY = trade construction. |
| REVIEW / QC | RED | Active review lane inside current ACTIVE bucket. YEYOU/RAV remain SPECIAL outside ACTIVE. |
| DOMAIN ACTIVE | SAM, LIQUID, VIOLET, BRENT, HENRY, CARL, LABOR, BROCK, HAWK, REGINALD, MARCO, ORACLE, BOND, CORAL, SHADE, ZHAO | Standing source-detail / thesis / diagnostic owners. HAWK is domain synthesis, not system organizing; ORACLE is diagnostic but owns a substantive prediction-market lens. |
| PROVISIONAL ACTIVE | AEOLUS, WATT, VULCAN, MIDAS, OSPREY, FALCON, HOMER | Active-by-intent or recently built/promoted; proof criteria remain uneven. Some are already stronger than others, but the bucket is descriptive, not a demotion. |
| EVENT-DRIVEN SPECIALIST | OZK, WAL | Standing single-name specialists with catalyst/print-driven cadence; both have real analytical authority in narrow lanes. |

## Contested Or Watch Rows

1. ORACLE

   Could be classified as `ORGANIZING / SERVICE` because it provides prediction-market diagnostics, but I recommend `DOMAIN ACTIVE`: it owns a substantive information domain and has external signal content, not merely workflow service.

2. HAWK

   Could look like organizing because it synthesizes OSPREY/FALCON, but it should stay `DOMAIN ACTIVE`: the synthesis is inside the geopolitical/oil-risk domain, not a fleet coordination function.

3. FALCON

   Stronger than the other newborns by DAEDALUS level (`L3`) and live signal flow. Still fits `PROVISIONAL ACTIVE` descriptively because it is newly split/promoted and its maturity/consumption proof is still being settled.

4. AEOLUS

   Older than the July newborns, but still `L2` with spawn-cadence debt and missing falsification surface class. `PROVISIONAL ACTIVE` remains fair until DAEDALUS says otherwise.

5. OZK and WAL

   Both are real active agents with narrow authority. Do not let `EVENT-DRIVEN SPECIALIST` read as lower authority; it is cadence/scope description.

## B2 Cadence vs Authority Qualifying Set

Cadence/authority separation earns its keep for these rows:

- PROME, WALTER, NEXUS, TERRY: standing service/coordination functions, not domain ownership.
- RED: active review authority, not domain ownership.
- AEOLUS, WATT, VULCAN, MIDAS, OSPREY, FALCON, HOMER: provisional active status can be misread as demotion or full maturity.
- OZK, WAL: event-driven cadence with real narrow authority.

Outside ACTIVE, B2 also applies to:

- DAEDALUS, YEYOU, RAV under SPECIAL / meta / review.
- CREED, DEWEY, HANS, OTTO under Tier-2-with-real-authority.

This is a manageable set, not a reason to add cadence/authority columns everywhere.

## Plan Amendments Required Before Phase 1

No blocking amendments.

Recommended wording refinements:

1. In Phase 1 scope, name root `CLAUDE.md` explicitly, not as "other mirrored boot-orientation surfaces."
2. In the Phase 1 implementation instruction, treat `AGENTS/_INDEX.md` as a navigation mirror that must align with the new buckets.
3. In the ROSTER block, say service-rule cadence belongs to DAEDALUS/WALTER/NEXUS owner mechanisms, not ROSTER.

## Questions For Will

1. Should ORACLE be `DOMAIN ACTIVE` or `ORGANIZING / SERVICE`?

   RAV recommendation: `DOMAIN ACTIVE`.

2. Should FALCON remain `PROVISIONAL ACTIVE` despite being DAEDALUS `L3` and already carrying live signal flow?

   RAV recommendation: yes, for Phase 1 descriptive taxonomy; DAEDALUS can mature it later.

3. Should event-driven specialist wording explicitly state "not lower authority"?

   RAV recommendation: yes, to avoid WAL/OZK reading as demoted.

## Go / No-Go

Go for Phase 1 drafting after Will/PROME accepts the minor wording refinements above.

Do not start Phases 3-4. Do not make labels operational. Do not silently edit root `CLAUDE.md`; draft the mirror change and send it to Will as already ruled.

## Correction Block - 2026-08-05

This addendum preserves RAV's original 2026-08-04 preflight text above, including the now-superseded placement of TERRY under `ORGANIZING / SERVICE`.

Correction: TERRY is `DOMAIN ACTIVE`, not `ORGANIZING / SERVICE`.

Reason: TERRY owns trade construction / canonical risk-rule authority in its lane. Root canon names TERRY the canonical owner of trade-construction rules, and live trade cards cite TERRY's numbered rules as a stable API. An agent that owns canon in its lane is a domain owner.

Corrected Phase 1 bucket set:

- `ORGANIZING / SERVICE`: PROME, WALTER, NEXUS
- `REVIEW / QC`: RED
- `DOMAIN ACTIVE`: SAM, LIQUID, VIOLET, BRENT, HENRY, CARL, LABOR, BROCK, HAWK, TERRY, REGINALD, MARCO, ORACLE, BOND, CORAL, SHADE, ZHAO
- `PROVISIONAL ACTIVE`: AEOLUS, WATT, VULCAN, MIDAS, OSPREY, FALCON, HOMER
- `EVENT-DRIVEN SPECIALIST`: OZK, WAL

This correction does not change the original artifact's audit value; it records the later Will/PROME/RAV ruling needed to consume it safely.
