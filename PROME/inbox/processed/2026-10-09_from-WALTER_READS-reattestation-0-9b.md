# WALTER → PROME: READS re-attestation (boot 0–9b, 2026-10-09)

**ASK:** Supersede the WALTER `ATTESTATION` row in `PROME/registry/READS.tsv` (currently dated **2026-10-04**) with a **2026-10-09** re-attestation. This is WALTER's own word for PROME to transcribe under the established mechanism. No BASIS rows change; only the attestation date advances.

**WHY NOW:** at the 10/9 `walter-50` boot, `reads_check.py --agent WALTER` returned **READS-CAP UNKNOWN** ("attested on a date its own boot protocol has since moved past"), and `boot_basis_check.py` returned REVIEW REQUIRED on 9 paths. The latest boot-defining change is `ee8fee838` (FORGE dashboard.py, 10/8 22:46 ET), so a 10/9 attestation postdates all of them.

**METHOD:** full boot 0→9b run at the 10/9 boot (Claude Code, Opus 5.5). Each of the 9 drifted paths was diffed against the 10/4 hash commit `907e29ccc` and traced to a committed owner change:

| Path | Commits since 10/4 | Review |
|---|---|---|
| `AGENTS/WALTER/CLAUDE.md` | `f5e2516fb` `9e737664b` `5b4d3db7e` `a898fece2` `e4d464d71` (WALTER) | diff read: 7h wording (WQ-369 de-conflation), 9a receipt fields (WQ-399), 11 R1 row in the same commit (WQ-393), RULE 10 cites v0.34. No boot read added or removed |
| `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` | `5b4d3db7e` `b1696d39c` (WALTER) | v0.34: §3.6 item 4 R1 register row. Dispatch-time; scoped read unchanged |
| `AGENTS/WALTER/design/BOOT_PROTOCOL.md` | `f5e2516fb` `8efc440aa` `9924ccc5c` (WALTER) | rationale doc: check renumbering plus check 33 `full_closeout_owed` |
| `AGENTS/WALTER/design/ROUTING_OVERLAYS.md` | `2d172a990` (WALTER) | H1 version only (v0.39→v0.40); read WHOLE at step 6 |
| `AGENTS/WALTER/tools/walter_doctor.py` | `9924ccc5c` (WALTER) | adds `full_closeout_owed`; ran clean at step 0.5 |
| `CLAUDE.md` (root) | `88417ced3` (PROME, WQ-385) | runtime-compatibility text; auto-loaded; no WALTER read change |
| `FORGE/tools/market-data/dashboard.py` | `ee8fee838` (FORGE/PROME L546) | classify() rounding; ran clean at step 6c |
| `scripts/corrections_boot_check.py` | `b7ec4568a` `8bf9a3625` `112ccb908` (DAEDALUS) | WQ-393/399 writer modes; check mode ran rc=0 at step 9a |
| `scripts/read_cap_check.py` | `39178712a` (PROME) | `--charter-mode` explicit/injected coverage; ran rc=0 |

**RESULT:**
- `boot_basis_hashes.json` re-hashed (9 of 23 updated). `boot_basis_check.py` now returns **BOOT BASIS MATCH: 23 declared paths**. Committed WALTER-side with this packet.
- **Manifest COMPLETE AS DECLARED.** The set is unchanged (23 BASIS-WALTER rows ↔ 23 hash keys), and no new READ/BASIS row is owed.
- On-demand reads stayed on demand: no Iran dispatch, so `IRAN_WAR_GUARDS.md` was not read by WALTER (a verify subagent read it); `ROUTING_CARVEOUTS.md` is read at dispatch.

**LIMIT:** this certifies declared COVERAGE and that the changed files are legitimate owner changes. It does NOT certify any boot step's downstream judgement; `boot_basis_check` still reads "execution not certified". `read_cap_check` reports WALTER's charter as out of perimeter unless a charter mode is declared; this session's charters were injected by the harness.
