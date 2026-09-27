# HANDOFF rotation plan — `prome-09` closeout, 2026-09-27 (plan read BEFORE any edit)
**Trigger:** `PROME/HANDOFF.md` = 24,174 B, 238 B under the 75% rotate line (24,412 B of the 32,550 B budget); the prior session's closeout wrote "rotate the 9/25 prome-2e entry at the next append (plan read + result read)". Appending today's entry (NEW_ENTRY.md in this directory) without rotating would cross 75%.

## Operations, in order
1. **Move verbatim** the entry that begins `## September 25 morning — \`prome-2e\`` (currently line 34) through its last non-empty line before `**Archive:**` (line 45) — 7,008 B including its trailing blank line — into a NEW file `PROME/archive/HANDOFF_ROTATED_2026-09-27_prome-09.md`, headed by ONE title line in the established form: `# HANDOFF rotation — \`prome-09\`, 2026-09-27 <time> ET (one verbatim entry; crc32 <N> over the exact bytes of the rotated entry below — from its \`## September 25 morning\` line through its last non-empty line, no trailing newline; this title line excluded; <B> B)`, a blank line, then the entry bytes. The crc and B are computed from the archived bytes AFTER writing (never typed).
2. **Insert** NEW_ENTRY.md as the FIRST entry (directly after the Resume line's following blank line, before `## September 26 late → September 27 morning — \`prome-b09b\``).
3. **Replace in the Resume line** only this clause: `Four entries after the 9/27 prome-b09b closeout (the prome-2e entry carries its three legs as sub-bullets) (9/25 prome-fa → \`archive/HANDOFF_ROTATED_2026-09-26_boot-review.md\`, crc in its header;` → `Four entries after the 9/27 prome-09 closeout (9/25 prome-2e → \`archive/HANDOFF_ROTATED_2026-09-27_prome-09.md\`, crc in its header;` — the rest of the line unchanged.
4. Nothing else in HANDOFF changes. No other file changes in this rotation.

## Invariants the reader should check
I1. After the operations HANDOFF has exactly four `## ` entries: prome-09 (new) · prome-b09b · boot-review · prome-1d — in that order, newest first.
I2. The rotated entry is byte-identical in the archive (crc recomputed from archived bytes matches the header), and no text of it remains in HANDOFF.
I3. The Resume line's archive pointer names a file that will exist and still says `ls PROME/archive/HANDOFF_ROTATED_*` is the index.
I4. NEW_ENTRY.md makes no claim that its cited owner records contradict: check its figures against `PROME/reports/2026-09-27_nano-banc-failure-SYNTHESIS.md`, `PROME/DOCKET.tsv` lines 513–518, and `PROME/WILL_QUEUE.md` row 306. In particular: loss figures must name measure and base; the Ontario hearing must be a POSSIBLE evidence source; lien ownership at failure must be NOT PROVEN.
I5. Does anything in the rotated prome-2e entry carry a LIVE instruction that no other surface carries (a standing guard that must not leave the boot path)? If yes, name it — it must be re-homed before rotation.
I6. The resulting file is under 70% of budget (22,785 B): expected ≈ 24,174 − 7,008 + ~3,100 ≈ 20,300 B.
