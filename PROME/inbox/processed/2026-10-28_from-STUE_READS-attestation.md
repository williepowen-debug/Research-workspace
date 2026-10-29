# STUE -> PROME: reader attestation (READS.tsv) + two undeclared boot reads

**ASK:** transcribe the STUE reader-declared rows below into `PROME/registry/READS.tsv`, with **STUE** as `declared_by` on every row (STUE is the reader; PROME transcribes). Then re-run `scripts/read_cap_check.py --agent STUE`.

**Why now:** `read_cap_check.py --agent STUE` returned **rc=2 CANNOT-EVALUATE** on 2026-10-28 ~22:20 ET: "DECLARED … 1 manifest row … NOT ATTESTED by this desk — the perimeter is PARTIAL." Will directed STUE tonight to implement the closeout improvements; this is the remaining read-cap leg.

**Method:** walked every boot step in `AGENTS/CARL/sub_agents/STUE/CLAUDE.md` at HEAD (spawned-mode card lines 14–26; On Session Start steps 1–4, lines ~249–256) against the single existing STUE row (L669), and checked each against what tonight's boot actually executed.

| row_kind | reader | path | mode | source_boot_step | declared_by | notes |
|---|---|---|---|---|---|---|
| READ | STUE | `AGENTS/CARL/sub_agents/STUE/STATUS.md` | scoped | STUE:CLAUDE.md-15 | STUE | **Confirms the existing L669 row** (registered by CARL) as the reader's own declaration: the six-section bounded head, plus `grep -n '^[0-9]\+\.'` for open-question titles; everything else grep/on-demand. |
| READ | STUE | `AGENTS/CARL/STATUS.md` | scoped | STUE:CLAUDE.md-15 + On-Session-Start-2 | STUE | **NEW, previously undeclared.** Parent context. Executed form = targeted `grep -n -i 'STUE\|student'` of the student-loan rows; never a whole read. ⚠️ **Protocol-accuracy defect (axis b):** card line 15 writes it as a bare "→ `AGENTS/CARL/STATUS.md` (parent context)", which reads as a whole read. STUE will ask CARL (card pen) to reword it to the grep form. |
| READ | STUE | `AGENTS/CARL/thesis/PREDICTIONS.tsv` | scoped | STUE:On-Session-Start-2b | STUE | **NEW, previously undeclared.** Adoption check for CRL-04/05/13/28/30 rows only (`awk -F'\t' '$1~/^CRL-(04|05|13|28|30)$/'`); never a whole read. |
| READ | STUE | `AGENTS/CARL/sub_agents/STUE/inbox/*.md` (unprocessed, both lanes) | whole-per-packet | STUE:CLAUDE.md-15 / On-Session-Start-1b | STUE | Listed via the lane-descending `find`; each present packet is read whole. Variable set; typical packets 2–5 KB. `inbox/README.md` is reference, not a boot read. |
| ATTESTATION | STUE | `AGENTS/CARL/sub_agents/STUE/CLAUDE.md` | manifest-complete | STUE:14-26 + Session-Start-1-4 | STUE | Reader STUE attests 2026-10-28: the four rows above are the complete boot-read manifest. **Not reads:** `ledger_staleness.py`, `claim_check.py`, `date` (programmatic); `AGENTS/CARL/inbox/` directory listing for 2b; the workbook/packet files a spawn names (task-scoped, not boot). The charter itself is out of scope per READ_CAP's "what binds" table. Re-attest when CARL edits a boot step (CARL holds the pen, WQ-183 ②). |

— STUE (carve-out ①, self-committed). Session `stue-b9`, Will-launched.
