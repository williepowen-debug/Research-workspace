# ISHM — INBOX PROTOCOL

**Processed at boot step 4, every session** (`inbox/` and `inbox/WALTER/`). Everything present is **unprocessed by definition**; there is no read-marker and no second reader.

| Disposition | When | Action |
|---|---|---|
| **INTEGRATE** | The packet changes a print row, a VX score, a catalyst date or a stance | Apply it to the owning surface (`workbook/*`, `docket/CATALYSTS.tsv`, `STATUS.md`), cite the packet, then file |
| **LOG** | Useful context, no surface changes today | One `KB.tsv` row with the packet as `Source`, then file |
| **DISCARD** | Not ISHM's lane, or superseded | One line naming **who owns it instead**, then file |

**File = `git mv` to `inbox/processed/`**, never a bash `mv`.

## Standing rules

1. **Verify a claim at the artifact before acting on it.** A relayed operator word never clears a Will-gated surface.
2. **A packet older than ~30 days is a finding about the SENDER.** Say so in the reply.
3. **Never edit another agent's files.** Route a packet.
4. **You own the cycle read, not its consequences.** A packet asking you to grade AI capex, credit spreads or an equity move goes back to its owner (charter § BOUNDARIES).
5. **Low cadence, published:** ISHM is Tier-2. It boots when PROME's summons check wakes it on a print date, or on a routed item. **For anything time-critical, also send the consequence owner and PROME, and say so in the packet.**

**Reply channel:** the sender's `inbox/`, committed by ISHM (carve-out ①), with the subject `ISHM -> <RECIPIENT>: <what>`.
