# CATO — SPECIAL / manual-only registration pass (2026-10-01)

**Ruling:** Will, 2026-09-26 13:07 ET, WQ-255, verbatim *"Approve WQ-255: SPECIAL, with CATO remaining my manual adviser and independent reviewer, without automatic launch or signal-routing eligibility."* PROME's packet `inbox/2026-09-26_from-PROME_WQ-255-RULED-CATO-is-SPECIAL.md` asked for three things: (1) a SPECIAL-convention entry with no maturity-ladder row, (2) the directory, (3) this checklist pass.
**Reconciling the packet's two clauses:** "a CATO row … (RAV is the precedent)" and "no maturity-ladder row" pull in different directions, because RAV HAS a FLEET_MAP ladder row (Meta L2). The ROSTER row is the canonical text, and it says **"no maturity-ladder row"**. So CATO gets **no FLEET_MAP row**. It gets a rendered SPECIAL entry with `—` grades, and a guard that fails if a grade row ever appears.

## `builds/REGISTRATION_CHECKLIST.md`, walked for a SPECIAL / manual-only, routing-excluded seat
| # | Surface | Disposition for CATO | Evidence |
|---|---|---|---|
| 1 | `PROME/ROSTER.md` | ✅ DONE by PROME. The row is under § SPECIAL with Will's ruling verbatim, and § CLASSIFICATION PENDING reads (0). | ROSTER:154, :175 (read 2026-10-01) |
| 2 | Root `CLAUDE.md` | N/A. Root carries no membership by design (WQ-120). | checklist row 2 note |
| 3 | `AGENTS.md` | N/A. It points to ROSTER and does not re-list membership. | AGENTS.md "Sources of truth" |
| 4 | `AGENTS/_INDEX.md` | ⚠️ **PROME's call, not mine.** RAV has a nav row (`_INDEX.md:64`) and CATO has none. A nav row is navigation, not routing or launch, so the ruling neither requires nor forbids it. Suggested text if PROME wants it: `\| CATO \| [\`CATO/\`](./CATO/) \| SPECIAL — Will's manual Codex/Astra adviser + independent reviewer (manual-only; never launched or routed) \|` | grep 2026-10-01: CATO=0, RAV=1 |
| 5 | `AGENTS/_NETWORK.md` | N/A. CATO has no transmission role, and the ruling excludes signal routing. | grep: CATO=0 |
| 6 | Thematic group pages | Same call as row 4: `_SYNTHESIS_OPS.md:34` lists RAV, CATO is absent. Nav only, so it is PROME's call. | grep |
| 7 | WALTER routing | ✅ **EXCLUDED by ruling, and verified absent.** `ROUTING_TABLE.md` / `ROUTING_OVERLAYS.md` / `ROUTING_CARVEOUTS.md` contain 0 CATO rows. CATO's name appears in WALTER's checklist only as the reviewer behind rule v0.48 (CATO-U1), which is provenance, not a route. | grep -c 2026-10-01 |
| 8 | `FLEET_MAP.tsv` row | ✅ **NO ROW, by ruling.** `render_directory.py` now dies if CATO gains one (guard watched firing on an injected row, and passing clean on the real map). | below |
| 9 | `FLEET_DIRECTORY.md` | ✅ Regenerated. CATO renders in the SPECIAL table as `— — — —`, with "UNGRADED BY RULING (WQ-255, 2026-09-26): manual-only — no launch, no routing, no ladder row". Footer count: 3 special. | `render_directory.py` rc 0 |
| 10 | Peer/parent surfaces | N/A. No parent, no peers by ruling. "RAV succession stays its own later question" (ROSTER). | — |
| 11 | Inbox handoffs | N/A. CATO carries no routine fleet obligations, and Will directs it by hand. | ROSTER:154 |
| 12 | DAEDALUS script registries | ✅ `maturity_scan.py`: CATO **was silently absent** (no CLAUDE.md/STATUS.md ⇒ `agent_dirs()` skipped it, the PAT-074 shape). It is now announced in both modes as `NOT GRADED · by ruling`. `render_directory.py`: new `SPECIAL_UNGRADED` map + guard. | runs below |
| 13–16 | Behavioural registries · split seeding · state-token conformance · sub-agent layer | N/A. This is not a build, split or promotion, and DAEDALUS creates no CATO surfaces. CATO's own files are Will's and CATO's, and are untouched. | — |

## Guard receipts (CHECK_STANDARD §3)
- **FIRE:** a copy of FLEET_MAP with an appended `CATO Meta L1 …` row fed to `render_directory.main()` printed `render_directory: FAIL — ['CATO'] carry a FLEET_MAP row but are UNGRADED BY RULING (SPECIAL_UNGRADED) — remove the row, or get the ruling changed and move the agent to SPECIAL`. The live directory was byte-identical after the fire run (`cmp`).
- **CLEAN:** the real FLEET_MAP gives `render_directory.py --check` → rc=0, and a writing run rendered the CATO line.
- **maturity_scan:** before the edit, the output had no CATO line. After the edit, it prints `| CATO | — | **NOT GRADED** | by ruling | …` and the TSV prints `CATO - NOT-GRADED by-ruling`.
