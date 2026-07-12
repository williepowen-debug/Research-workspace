# Cross-War Energy-Strike Aggregate — Summary (thin, derived)

> **Convention:** this file is **regenerated from OSPREY's and FALCON's own strike ledgers at HAWK closeout (CLAUDE.md step 13), never independently maintained.** HAWK does not log strike rows — that discipline lives with the theater owners. If this file drifts from the siblings' ledgers, re-pull from them; do not hand-edit rows here.
> **Predecessor:** the original `STRIKES.tsv` + `SUMMARY.md` in this directory are 🧊 FROZEN 2026-07-12 (pre-split, 36-row combined ledger) — see their banners.
> **Regenerated:** 2026-07-12 (split day) from OSPREY's and FALCON's `domain/energy-strikes/` as of spinout.

---

## One row per theater

| Theater | Ledger | Rows | Date range | Swept-through mark | Channel state (as of spinout) | Pointer |
|---|---|---:|---|---|---|---|
| Russia/Ukraine | `AGENTS/OSPREY/domain/energy-strikes/STRIKES.tsv` | 32 | 2026-02-23 → 2026-07-10 | **2026-07-12** (current — 7/12 backfill sweep closed the gap inherited from HAWK) | THREE channels running in parallel: refineries/products FIRING (~1/3 capacity offline), crude-export terminals re-fired (flip-trigger #2 FIRED, damage limited), shadow-fleet tankers newly kinetic (7/6-12) | `AGENTS/OSPREY/domain/energy-strikes/ANALYSIS_2026-07-12.md` |
| Iran/Gulf | `AGENTS/FALCON/domain/energy-strikes/STRIKES.tsv` | 4 | March 2026 only (seed rows) | **2026-03-19** (STALE — backfill is FALCON's founding-mandate item #1, not yet run as of spinout) | Thin/unbuilt — ledger asymmetry is explicit, not silently absorbed (per build spec §2b) | `AGENTS/FALCON/domain/energy-strikes/` |

**Total pre-split combined ledger: 36 rows** (frozen at `AGENTS/HAWK/domain/energy-strikes/STRIKES.tsv`).

---

## The one genuine cross-war observation (from the frozen SUMMARY.md's own header)

Russia's refinery-strike campaign **peaked the same week Iran signed its (now-collapsed) MOU** — two independently-driven escalation cycles crested in the same window with no shared causal mechanism found. Worth re-checking each time both theaters show a coincident intensity spike: coincidence until a mechanism is shown, not before.

---

## Reading this table

- **Ledger asymmetry is real, not a data gap to paper over:** OSPREY inherited a mature, actively-swept ledger; FALCON inherited 4 March-vintage seed rows and owes its own backfill sweep. Do not read "4 rows" as "Gulf theater was quiet" — read it as "not yet swept."
- **HAWK's synthesis job here** is limited to (a) keeping this pointer table current at closeout and (b) flagging if both theaters' swept-through marks go stale simultaneously (a sign HAWK itself should nudge the siblings, not re-build their ledgers).
