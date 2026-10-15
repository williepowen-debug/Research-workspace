# GIBBS — INBOX PROTOCOL

**Processed at boot step 3, every session** (`inbox/` and `inbox/WALTER/`). Everything present is **unprocessed by definition** — no read-marker, no second reader.

| Disposition | When | Action |
|---|---|---|
| **INTEGRATE** | The packet changes a read, a perimeter cell, a catalyst date or a stance | Apply it to the owning surface (`workbook/*`, `docket/CATALYSTS.tsv`, `STATUS.md`), cite the packet, then file |
| **LOG** | Useful context, no surface changes today | One `KB.tsv` row with the packet as `Source`, then file |
| **DISCARD** | Not GIBBS's lane, or superseded | One line naming **who owns it instead**, then file |

**File = `git mv` to `inbox/processed/`**, never a bash `mv`.

## Standing rules

1. **Verify a claim at the artifact before acting on it.** A relayed operator word never clears a Will-gated surface.
2. **A packet older than ~30 days is a finding about the SENDER.** Say so in the reply.
3. **Never edit another agent's files.** Route a packet.
4. **REGINALD owns the regional cohort; BROCK owns BRK-31.** On a shared figure, the tie-break is the primary filing, not either ledger.
5. **Low cadence, published:** GIBBS boots around each quarter's print weeks (mid-Jan/Apr/Jul/Oct) and on PROME spawns. **For anything time-critical, send REGINALD or PROME too, and say so in the packet.**

Reply channel: the sender's `inbox/`, committed by GIBBS (carve-out ①), subject `GIBBS -> <RECIPIENT>: <what>`.
