# CYPHER — INBOX PROTOCOL

**Processed at boot step 3, every session** (`inbox/` and `inbox/WALTER/`). Everything present is **unprocessed by definition** — no read-marker, no second reader.

| Disposition | When | Action |
|---|---|---|
| **INTEGRATE** | The packet changes an incident row, a watch-row state, a catalyst date or a stance | Apply it to the owning surface (`workbook/*`, `docket/CATALYSTS.tsv`, `STATUS.md`), cite the packet, then file |
| **LOG** | Useful context, no surface changes today | One `KB.tsv` row with the packet as `Source`, then file |
| **DISCARD** | Not CYPHER's lane, or superseded | One line naming **who owns it instead**, then file |

**File = `git mv` to `inbox/processed/`**, never a bash `mv`.

## Standing rules

0. **Folded claim cards (WALTER ROUTING_TABLE v0.48, Will-approved 2026-10-23 17:16 ET):** WALTER now routes every cyber event or claim; claims with no visible money channel arrive folded in one ROUTINE card per sitting. Intake: ONE `board_log.tsv` row per card, its notes listing every claim and its disposition. A claim gets its own `workbook/INCIDENTS.tsv` row only if (a) the victim is a financial firm, a financial vendor or a `CHOKEPOINTS.tsv` supplier, or (b) a desk has cited it, or (c) CYPHER checked it at a source (the verdict, FALSE included, keeps its row). Any other claim stays in the board_log notes, findable by grep. A claim that later gains a channel is promoted to a row in the same session. WALTER adopted the matching card format 2026-10-23 (commit 9f11bc019, ROUTING_TABLE v0.48 CYBER row): one table line per claim with victim, actor, claim date, source handle and any figure exactly as claimed.

1. **Verify a claim at the artifact before acting on it.** A relayed operator word never clears a Will-gated surface.
2. **A packet older than ~30 days is a finding about the SENDER.** Say so in the reply.
3. **Never edit another agent's files.** Route a packet.
4. **You own the event, not the consequence.** A packet asking you to grade bank credit, insured loss or a price move goes back to its owner (charter § IDENTITY).
5. **Low cadence, published:** CYPHER is Tier-2. It boots when PROME spawns it — on a routed cyber item, a fired escalation row or a dated catalyst. **For anything time-critical, send the consequence owner and PROME too, and say so in the packet.**

Reply channel: the sender's `inbox/`, committed by CYPHER (carve-out ①), subject `CYPHER -> <RECIPIENT>: <what>`.
