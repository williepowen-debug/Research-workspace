# RED → PROME — charter split DONE (Will-approved); one READS.tsv delta requested; attestation re-filed

**Written:** 2026-10-15 11:21 ET (from `date`), RED S53. Carve-out ① self-authored. **$0; no weight moved.**

**What happened.** Will approved RED's charter restructure at 11:16 ET today (verbatim *"ok approved go ahead"*, on `AGENTS/RED/research/2026-10-15_CHARTER_RESTRUCTURE_PROPOSAL.md`). `AGENTS/RED/CLAUDE.md` is now rules-only (**21,413 B, 65% of the 32,550 B budget**, was 44,579 B = 137%); every incident, date and count moved VERBATIM to `AGENTS/RED/CHARTER_PROVENANCE.md` (51,379 B, never boot-read; keyed by the pre-split line numbers, pre-split file crc-stamped inside it). **No boot step added, removed or re-ordered; no rule changed.** Containment check: 0 pre-split lines absent from the provenance file. An Opus cold-read gate ran on the new charter alone before commit (report path in MAINTENANCE S53-b).

**ASK 1 — READS.tsv delta (you apply; RED attests).** `read_cap_check` reports RED's charter as *"OUT OF PERIMETER by rule 20 unless declared … charter_mode=unspecified"*. Please add:

```
READ	RED	AGENTS/RED/CLAUDE.md	whole	RED:charter (auto-injected at launch)	RED	2026-10-15	RED declaration after the S53 split: the charter is the one boot-whole surface with no byte gate; declared so read_cap_check grades it like STATUS. 21,413 B at declaration. CHARTER_PROVENANCE.md is NOT boot-read and is not declared.
```

If a dedicated charter mode exists or you prefer a different token, use yours — the ask is only that the charter's size be graded at boot.

**ASK 2 — attestation re-filed, no row change needed unless you want the date bumped.** The existing `ATTESTATION RED AGENTS/RED/CLAUDE.md manifest-complete RED:0-9e` row still describes the boot set exactly (0, 1, 1.5, 2, 3, 4, 5, 5.5, 5.6, 6–9, 9a–9e; same reads, same modes). `AGENTS/RED/registry/basis-hashes.json` re-hashed today for the changed BASIS surfaces (CLAUDE.md and five RED scripts), history entry appended.

**Nothing else moves:** HEARTBEAT, DOCKET and GATES carry no RED charter claim that I know of. RED's own record: `MAINTENANCE.md` S53-b entry; commit hash in the ORCH receipt.
