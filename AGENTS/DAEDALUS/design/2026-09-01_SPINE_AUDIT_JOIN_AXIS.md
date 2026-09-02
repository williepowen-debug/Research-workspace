# Spine-audit axis spec — "reconcile across the registration JOIN by whoever owns neither side" (WQ-86, Will 2026-09-01)

**Owner:** DAEDALUS (spec) · **Consumer:** PROME's weekly spine audit (`/spineaudit`, `PROME/tools/spine_audit.workflow.js`) · **Rule encoded:** `BLUEPRINTS/STRICT_TEXT.md` rule 7 (registration join) + `PROME/GATES.tsv` header · **Status:** SPEC — PROME wires it as a reader group at its next spine-audit touch; DAEDALUS does not edit PROME's tools.

## The join
Two registries describe one gate: the DESK's (RED `registry/FALSIFICATION_TRIGGERS.tsv`, REGINALD `registry/THRESHOLDS.tsv`, CREED `registry/THRESHOLDS.tsv`, BRENT `workbook/REGISTRY.tsv`, FERT `TRIGGERS.tsv`, …) and PROME's `GATES.tsv`. Each side is audited by its owner and each owner's audit passes clean while the JOIN is broken (a gate ratified at a desk that never reached GATES; a GATES row naming an owner that has no read-path to it). The 8/30 GATES condition-column pass found no defect in either file and four in the instrument — because it read one side.

## The axis (one reader, neither owner)
| Leg | Test | Verdict tokens |
|---|---|---|
| J1 ratified-at-desk → GATES | every desk-registry row with state `LIVE`/`ARMED`/`FIRED` has a GATES row whose `definition_surface` resolves to it (by the desk's LOCAL id — never by GATES's own id first; `gates_pointer_check` contract form 4) | `JOINED` · `DESK-ONLY` (① breached — owner's duty) |
| J2 GATES → owner read-path | every GATES row naming an owner ≠ registrar is cited from a surface that owner's boot reads (charter boot section, `READS.tsv` row, or a boot-line grep) | `JOINED` · `UNDELIVERED` (② breached — registrar's duty) |
| J3 state agreement | for JOINED pairs, the desk state token and the GATES state token map to the same Class-2 token (legacy spellings via the recognizer set) | `AGREE` · `DISAGREE(desk=…, gates=…)` |
| J4 fire-time routing | for any desk row that moved to `FIRED` in the window, a GATES change within one session of the fire | `ROUTED-AT-FIRE` · `LATE(nd)` · `NEVER` |

**Reader assignment:** a session that owns neither the desk registry nor GATES — in practice DAEDALUS or a spine-audit clerk. **Output:** one table, counts by token, DESK-ONLY / UNDELIVERED / DISAGREE / NEVER rows named with file:line; a clean run prints its perimeter (which desk registries it read; which it could not parse).

## Falsification before trust (CHECK_STANDARD §3)
Positive controls from the 8/30 pass: GATE-REG-T02 ↔ REGINALD §REG-T-02 (JOINED, local id) · GATE-BRENT-COT-35B ↔ COT-FUEL-35B · GATE-FERT-G5 ↔ FERT T4. Negative control: a planted desk row with no GATES counterpart must print DESK-ONLY; a planted GATES row naming a desk whose boot never cites it must print UNDELIVERED.

**Prior-art line (§13):** searched — PAT-063 (a trigger's metric-owner absent from its recipient chain), PAT-099 (a publisher's consumer list is itself a stale surface), `finding_transfer_completes_only_when_the_receiver_encodes`. This axis is their registry-side instrument; not a new pattern.
