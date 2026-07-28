# Outbox disposition — 2026-07-28

**Why this file exists:** HAWK's `outbox/` is scanned by PROME at boot (Convention B). It held **8 packets aged 16–38 days with `delivered/` empty**, so every PROME boot was re-surfacing asks that were already dead. **All 8 closed below.** None had an outstanding reply owed; all were superseded by the 2026-07-12 split or executed by it.

| Packet | Date | Age | Disposition |
|---|---|---:|---|
| `to-BRENT_hawk-boot-sync` | 6/20 | 38d | **SUPERSEDED — theater rehomed.** Iran/Hormuz closure content is FALCON's since the split; FALCON has been sending BRENT its own theater packets directly. |
| `to-PROME_truce-collapse-ladder-remark` | 7/8 | 20d | **SUPERSEDED BY THE OWNER'S OWN MARKS.** Carried HAWK's pre-split ladder **B12 / C42 / D46**. FALCON's live marks are **B10 / C40 / D50** (7/27). A stale scenario ladder from a non-owner is worse than none. |
| `to-PROME_russia-two-front-read` | 7/9 | 19d | **SUPERSEDED — theater rehomed.** Russian refinery campaign is OSPREY's; their `STRIKES.tsv` is at 48 rows swept through 7/23 vs this packet's handful. |
| `to-BRENT_crude-terminal-flip-trigger-fired-CORRECTION` | 7/12 | 16d | **SUPERSEDED — theater rehomed.** The correction was right and mattered (it is the HAW-15 miss), but the channel is OSPREY's and its ledger now carries it. Retained as history in `LESSONS.md` item 4, which is the durable home. |
| `to-BRENT_ukraine-tanker-campaign` | 7/12 | 16d | **SUPERSEDED — theater rehomed** to OSPREY (Channel 3, shadow-fleet tankers). |
| `to-DAEDALUS_war-agent-split-build-spec` | 7/12 | 16d | **✅ EXECUTED.** DAEDALUS built OSPREY and FALCON on 7/12; build record `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md`. |
| `to-PROME_third-strike-round-remark` | 7/12 | 16d | **SUPERSEDED.** Carried **D58 as base**; FALCON's live D is **50**, re-marked 7/27 off FAL-01's failure. |
| `to-PROME_war-agent-split-roster-notice` | 7/12 | 16d | **✅ EXECUTED.** Both agents are in `PROME/ROSTER.md` and root `CLAUDE.md`; HAWK reclassified to cross-war synthesis + dormant book. |

## The pattern worth keeping

**Six of eight died the same way: a packet outlived the scope that authored it.** They were written by pre-split HAWK about theaters HAWK no longer owns, and nothing in the split checklist swept the outbox — so the *agent* was rescoped while its *outbound queue* was not. **A scope change should trigger an outbound-queue sweep the same way it triggers a ledger split.** Cheap rule, and it is the outbound twin of the inbound lesson (`LESSONS.md` 2026-07-25: unprocessed lanes carry live content).

**Going forward:** anything landing in `outbox/` gets closed or moved here at the closeout that follows its delivery — `delivered/` is no longer allowed to sit empty while `outbox/` accumulates.
