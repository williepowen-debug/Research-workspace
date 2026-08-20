# FLG — INBOX PROTOCOL

**Processed at boot step 3, every session.** Everything present in `inbox/` is **unprocessed by definition** — there is no read-marker and no second reader.

## The three dispositions

| Disposition | When | Action |
|---|---|---|
| **INTEGRATE** | The packet changes a figure, a threshold, a trigger date, or the thesis | Apply it to the owning surface (`workbook/*`, `THESIS.md`, `STATUS.md`), cite the packet, then file |
| **LOG** | Useful context, no surface changes today | One `KB.tsv` row with the packet as `Source`, then file |
| **DISCARD** | Not FLG's lane, or superseded | Note the routing in one line (**who owns it instead**), then file |

**File = `git mv` to `inbox/processed/`** — never a bash `mv` (bash leaves a dangling deletion in the index; auto-memory `git_mv_for_inbox_processing`).

## Standing rules

1. **Verify a claim at the artifact before acting on it** (PAT-032). A packet asserting "X is now registered" is an assertion about a surface — go read the surface. A relayed operator word never clears a Will-gated surface.
2. **A packet older than ~30 days is a finding about the SENDER**, who has been acting on a false assumption about what FLG knows. Say so in the reply.
3. **Never edit another agent's files in response to a packet.** Route a packet back. The two guards are permission *and* idleness, and FLG has neither over another desk.
4. **REGINALD packets carry parent authority on the cohort view, not on FLG depth.** Where a figure disagrees, the tie-break is **the primary**, not either ledger.
5. **A correction to a figure FLG has published** triggers `consumer_check` at closeout — including `--self`, since the cross-agent scan deliberately excludes FLG's own directory.

## Reply channel

Write the reply into the sender's `inbox/` and **commit it yourself** (root Git Protocol carve-out ①), subject `FLG -> <RECIPIENT>: <what>`. At packet-commit with an ASK of a named agent, run `ListAgents` and doorbell a live recipient (MESSAGING rule 6).
