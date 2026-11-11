# BOOT.md rotation #4 — PLAN (D:L1108)

**Authority:** DOCKET L1108 (PROME's own housekeeping row, registered 2026-11-10 from `scripts/read_cap_check.py --agent PROME`: `PROME/BOOT.md` is at the rotate tier, 75% or more of the 32,550 B whole-read budget) and Will in PROME's chat 2026-11-11 10:54 ET, verbatim: "Okay lets have you work on the housekeeping for PROME now". **Owner:** PROME (`PROME/BOOT.md` and `PROME/BOOT_MODULES.md` are PROME manuals). **Written:** 2026-11-11 11:04 ET (from `date`) by PROME prome-2b, against HEAD e54fce06a3.

**Reads (PROME/CLAUDE.md § Review budget, archival split):** ONE plan read of THIS file by a Sonnet cold reader, fix ❌ only, ⚠️ to the residue block below; then the move in ONE edit set; then ONE result read at the commit; then declared residue.

## What moves and why

`PROME/BOOT.md` is read whole at every boot. `PROME/BOOT_MODULES.md` is not a boot read: each of its sections is opened at the trigger its BOOT.md pointer names. Four spans of BOOT.md are needed only at a trigger, not at every boot, so they move verbatim to the module file and a pointer naming the trigger stays in place. No rule, threshold, command or authority changes.

## Measurements (instrument: Python `len(text.encode())` and `zlib.crc32` over the exact span in `PROME/BOOT.md` at HEAD e54fce06a3; re-measured with `PROME/tools/measure.py` after the move)

| Unit | Source span in `PROME/BOOT.md` | Bytes | crc32 | Destination | Pointer bytes |
|---|---|---|---|---|---|
| A | step 5, the bullet beginning `- **Reading those four verdicts`, through the line before `6. **Decide conditional reads:**` | 1298 | 1087820349 | `PROME/BOOT_MODULES.md` § Gate verdict rules | 261 |
| B | step 6, the bullet beginning `- **Desk decision-surface alerts that name PROME as the route**` | 799 | 1018005200 | `PROME/BOOT_MODULES.md` § Desk decision-surface alerts | 280 |
| C | step 6, the bullet beginning `- **BOARD diff-scan (every boot, ALREADY inside` | 746 | 4133925632 | `PROME/BOOT_MODULES.md` § BOARD diff-scan | 283 |
| D | step 8, the parenthesis after `stale agents` beginning ` (source: the spawn slate's DARK rows;` | 219 | 581504177 | `PROME/BOOT_MODULES.md` § Stale-agents source | 60 |

BOOT.md before: 24680 B. Expected after: 22502 B, which is 69.1% of 32,550 B; target under 22,785 B (70%). `PROME/registry/READS.tsv`: BOOT.md stays `whole`; BOOT_MODULES.md stays `scoped`; no registry change.

## Exact new texts in `PROME/BOOT.md`

### Pointer A (replaces unit A in place, exact)
```
   - **Reading those four verdicts (rules the gate's printed lines do not carry) → `PROME/BOOT_MODULES.md` § Gate verdict rules (moved verbatim 2026-11-11, rotation #4); open it on any CAPABILITY, position-agreement or 5b corrections line that is not ✅.**
```
### Pointer B (replaces unit B in place, exact)
```
   - **Desk decision-surface alerts that name PROME as the route → `PROME/BOOT_MODULES.md` § Desk decision-surface alerts (moved verbatim 2026-11-11); open it when an inbox packet is such an alert. The duty: PROME registers the WQ row in the session that consumes the alert.**
```
### Pointer C (replaces unit C in place, exact)
```
   - **BOARD diff-scan: every boot, ALREADY inside `prome_gate.py boot`. The standalone re-run rule, the cursor rule and the rc=1 meaning → `PROME/BOOT_MODULES.md` § BOARD diff-scan (moved verbatim 2026-11-11); open it if the gate was skipped or its board_scan line is not ✅.**
```
### Pointer D (replaces unit D in place, exact)
```
 (source → `PROME/BOOT_MODULES.md` § Stale-agents source)
```

## Exact new text in `PROME/BOOT_MODULES.md`

One new section is APPENDED at the END of the file, after `## Rotated banners (2026-10-30)` and its text, so no existing section moves. Its form:

```
---

## Rotation #4 (2026-11-11, D:L1108): four trigger-keyed spans moved verbatim from `PROME/BOOT.md`
*Plan `PROME/proposals/2026-11-11_boot-rotation-4-PLAN.md`. Each block below is byte-identical to its BOOT.md span at the move except that the leading list indentation and bullet marker are kept as they were; the crc32 over each moved span is in the plan and the commit body. Maintained HERE from now on, never re-copied into BOOT.md.*

### Gate verdict rules
*Trigger: any CAPABILITY, position-agreement or 5b corrections line of the boot gate that is not ✅ (BOOT.md step 5).*
<unit A verbatim>

### Desk decision-surface alerts
*Trigger: an inbox packet is a desk decision-surface alert that names PROME as the route (BOOT.md step 6).*
<unit B verbatim>

### BOARD diff-scan
*Trigger: the boot gate was skipped, or its board_scan line is not ✅ (BOOT.md step 6).*
<unit C verbatim>

### Stale-agents source
*Trigger: filling the "stale agents" field of the boot report (BOOT.md step 8).*
stale agents<unit D verbatim>
```

## Pointer-adjusted edits outside the two files

- `PROME/SYSTEM.md` line 193 reads "Desk decision-surface alert receipt: `PROME/BOOT.md` step 6 owns the instruction." It becomes "Desk decision-surface alert receipt: `PROME/BOOT_MODULES.md` § Desk decision-surface alerts owns the instruction (pointer at `PROME/BOOT.md` step 6)."
- `PROME/.claude/skills/boot/SKILL.md` and its root copy `.claude/skills/boot/SKILL.md`: NO edit. Item 4 names "the rest of BOOT.md step 5 in full (… four-verdict rules, 5b corrections)" and item 3 says "step 6 owns the board-scan re-run rule". Both stay true as pointers because BOOT.md steps 5 and 6 keep a bullet for each that names the module section.
- `BOOT_MODULES.md` line 1 (its creation-history line) gains "; M8 rotation #4 (verdict rules · desk alerts · BOARD diff-scan · stale-agents source) 2026-11-11 — plan `PROME/proposals/2026-11-11_boot-rotation-4-PLAN.md`".
- `PROME/BOOT.md` header line: the `**Updated:**` stamp becomes "2026-11-11 (rotation #4, D:L1108: four trigger-keyed spans moved verbatim to `BOOT_MODULES.md`; plan `proposals/2026-11-11_boot-rotation-4-PLAN.md`). Prior: 2026-11-10 (WQ-662 B: step 8 delta-brief evidence rule; `proposals/2026-11-10_wq662-RULED.md`)." and the 2026-11-09 prior moves to `archive/BOOT_STAMP_CHAIN_2026-10-16.md` as one appended line, because the header keeps the latest stamp and at most ONE prior.

## Invariants (the result read checks each)

1. Every moved span appears in `PROME/BOOT_MODULES.md` with the crc32 in the table above, and no longer appears in `PROME/BOOT.md`.
2. Each of the four places in BOOT.md keeps a pointer that names the destination section AND the trigger for opening it.
3. No other byte of BOOT.md changes except the header stamp line.
4. No section already in BOOT_MODULES.md is moved, edited or reordered; the new section is appended at the end, and line 1 gains only the M8 clause.
5. Every `§` name used in a BOOT.md pointer exists as a heading in BOOT_MODULES.md, spelled the same.
6. BOOT.md measures under 22,785 B with `PROME/tools/measure.py`.
7. The root and PROME copies of the boot runner are untouched and still identical.
8. `scripts/read_cap_check.py --agent PROME` shows BOOT.md below the rotate tier and reports no new over-budget surface.

## What a reader of BOOT.md loses at boot, stated plainly

- The meanings of CAPABILITY states, the position-agreement rc=1 rule and the corrections receipt rule are no longer on the boot-read path; the gate's own printed lines carry the state and the receipt command, and the pointer says to open the module on any such line that is not ✅.
- The BOARD scan's standalone re-run rule and cursor rule are no longer on the boot-read path; they matter only when the gate was skipped or the scan is flagged, and the pointer says so.
- The desk decision-surface alert rule keeps its one-sentence duty in the pointer; its history and scope sentence move.
- The stale-agents source moves; the pointer names where it is.

## Residue (filled after each read)

*(empty before the plan read)*
