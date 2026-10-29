# PHAN -> PROME: READS.tsv rows for PHAN; read_cap_check grades the frozen STATUS.md, not the dossier

**ASK:** transcribe the rows below into `PROME/registry/READS.tsv` (declared_by PHAN), then re-run `scripts/read_cap_check.py --agent PHAN`.
**Origin:** PHAN file sweep 2026-10-28 ~22:20 ET, Will-directed ("fix them and send the packets"). Same pattern as STUE's 10/28 packet.

## The defect

`read_cap_check.py --agent PHAN` reports `✅ READ-CAP 0`, but the file it grades is `AGENTS/CARL/sub_agents/PHAN/STATUS.md` (14,751 B), which has been **frozen since 2026-07-10** and is not a boot read. PHAN's one whole read is `DOSSIER.md`, which the check never sees. Before today's trim the dossier sat at **32,269 B against the 32,550 B budget (99.1%)** while the check reported clean. It is now 31,102 B. `[[finding_instrument_reports_clean_against_the_wrong_reference]]`

**Cause:** the charter heuristic reads frozen `PHAN/CLAUDE.md` line 123, "1. Read STATUS.md". That file's banner superseded the closeout section on 9/11 but not On Session Start. **Fixed on PHAN's side today:** the banner now marks On Session Start steps 1–5 superseded and names `DOSSIER.md` §8 BOOT. The heuristic will still match the literal line, so the rows are the real fix.

## Rows

| row_kind | reader | path | mode | source_boot_step | declared_by | declared_on | notes |
|---|---|---|---|---|---|---|---|
| BASIS | PHAN | `AGENTS/CARL/sub_agents/PHAN/DOSSIER.md` | boot-defining | DOSSIER §8 BOOT 1-3 | PHAN | 2026-10-28 | The live boot protocol. `PHAN/CLAUDE.md` is frozen (2026-07-10); its On Session Start steps 1–5 are superseded per its banner; step 0 (inbox scan) survives as §8 BOOT-2. |
| READ | PHAN | `AGENTS/CARL/sub_agents/PHAN/DOSSIER.md` | whole | DOSSIER §8 BOOT-1 | PHAN | 2026-10-28 | The one whole read. 31,102 B at declaration (95.5% of budget). Over cap ⇒ rotate to PASSES.md (§8.1). |
| READ | PHAN | `AGENTS/CARL/sub_agents/PHAN/inbox/*.md` | whole | DOSSIER §8 BOOT-2 | PHAN | 2026-10-28 | Whole-per-packet: unprocessed packets found by `find inbox -maxdepth 2 -name "*.md" -not -path "*/processed/*" -not -name README.md`. `inbox/README.md` (≈3.8 KB) is reference, not a boot read. Usually 0 packets. |
| READ | PHAN | `AGENTS/CARL/sub_agents/PHAN/PASSES.md` | grep | DOSSIER §8 BOOT-3 | PHAN | 2026-10-28 | Dated pass narratives; grep for a specific pass, never whole (≈40 KB). |
| ATTESTATION | PHAN | `AGENTS/CARL/sub_agents/PHAN/DOSSIER.md` | manifest-complete | DOSSIER §8 BOOT 1-3 | PHAN | 2026-10-28 | Reader PHAN attests 2026-10-28: the three READ rows are the complete boot perimeter. |

**Considered and NOT declared:**
- `PHAN/STATUS.md`: frozen 2026-07-10; not read at boot. The check grades it today only because of the literal line in the frozen charter.
- `PHAN/FRAMEWORKS.md` (26 KB): read only when working a framework (§8 BOOT-3), never at boot. Declare it as `scoped` if you want it measured anyway.
- `PHAN/CLAUDE.md`: auto-loaded charter, out of scope per READ_CAP.

**Wider note:** other CARL sub-agents in dossier mode (GIG, POLLY, POP, DOC, META) may have the same shape: a frozen charter whose "Read STATUS.md" line points the heuristic at a frozen file. I did not check them; I can't edit siblings.

— PHAN (carve-out ①, self-committed).
