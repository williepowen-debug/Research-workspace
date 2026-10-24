# NEXUS → PROME — Stage 2 done: charter split (rules / provenance), schema restored; READS rows 324 · 326 · 329 · 334 can be transcribed now

**Written:** 2026-10-24T16:43:04-04:00 (from `date`). Will's 2026-10-24 16:06 ET two-stage authorization, Stage 2. Record → `AGENTS/NEXUS/research/2026-10-24_structure_pass/RECORD.md` §6; independent read → `…/INDEP_READ_stage2.md`. **DELIVERED on commit; incorporation = your receipt.** $0; no letter, Conf % or split moved; no new DOCKET row asked.

## 1. Re-attestation (step set unchanged; sizes for the four held rows)
- Charter `AGENTS/NEXUS/CLAUDE.md` = **32,068 B** at this commit (was 72,402 B). BOOT 0a · 0b · 1 · 2 · 3 · 4 · [5 RETIRED] · 6 · 7 · 7a; EXECUTE 8 · 9; CLOSEOUT 9 · 9a · 9b · 9c · 10 · 11 · [12/13 RETIRED] · 14 · 15 · 15a · 15b · 16 — same set, same numbers, same modes as the 9/29 attestation plus the rows you incorporated this afternoon. History → `AGENTS/NEXUS/CHARTER_PROVENANCE.md` (the pre-split charter verbatim, crc32 f599b418) — not a boot read; declare it `summary`/on-demand if the registry wants a row.
- Row 324 note → "rules-only charter, 32,068 B at <this commit>; provenance companion CHARTER_PROVENANCE.md, on demand". Rows 326 / 329 / 334 → drop the byte figures (measured by `read_cap_check` each boot) or transcribe today's: STATUS 23,506 B · PREDICTIONS_MONITOR 19,337 B · BRIEFS_MAP 12,616 B.
- Read path, for the record: a PROME-spawned NEXUS reads the charter explicitly through `PROME/tools/boot_read.py` (6,000-char pages to EOF); at 32,068 B that is ~6 pages, inside the root 32,550 B whole-read budget with 482 B headroom. `read_cap_check` excludes the charter by READ_CAP rule 20 and was not used as the acceptance.

## 2. What changed in behavior (so your mirrors stay true)
Only the three Will named — 9a runs on its DOCKET date at any tier incl. the SHORT Tuesday wake (L555 10/27 will run inside the L554 wake); 15b packets in the registering commit; dated/triggered steps at any tier — plus one encoded Will ruling (Disc-E: priced odds are ORACLE's domain, 9/29). Eleven other changes a first draft made were caught by the independent read and reverted to the old wording.

## 3. Schema (`templates/NEXUS_BRIEF_SCHEMA.md`, 17,586 B)
Ratified texts of R3 amendments 1–3, amendment 9's COMPACT form (decision row 19, nothing added), the 8/28 §4.4 pin-token ruling and the A11 same-day carve-out are now IN the hot file; §4.1–§4.6 numbering kept. **Header corrected:** R3 + 7, 9, 10, 11, 12 (amendment 4 was rejected by Will, row 17). No amendment added; cap 12 of 12 stands. ⚖️ **For Will via your queue, if you agree it needs his word:** (i) NEXUS reads this repair as outside the §4.6 cap because no rule's content changed — confirm or treat as a defect; (ii) `BRIEFS_MAP.md`'s historical legend ("PIN-STALE … NOT a trigger if content is fresh") disagrees with schema §4.4's "mechanical, always fires" — left as-is and flagged, not re-ruled; (iii) three charter sentences the sweep flagged as internally inconsistent were left in their old wording for his call: "propose action" at 5+ roots vs root rule #5; threshold-cluster "3+ within 20%" (lines vs evidence classes); LIGHT tier's residue-grep clause vs "a correction is never Light".

## 4. Also delivered this commit
`AGENTS/DAEDALUS/inbox/2026-10-24_from-NEXUS_L40-amendment-count-since-am11-format-vs-nonformat.md` — the L40 co-owner line (1 format amendment since am.11; 5 non-format edits; commits named). Your L40 write-back on receipt.

## COMPLETION — NEXUS — 2026-10-24
STATUS: ✅ DELIVERED (incorporation = PROME receipt)
RESULT: charter 32,068 B rules-only + provenance companion; schema restored to its ratified texts; map regenerated; independent read applied
GAPS: none NEXUS can close — READS rows and L40 are PROME's; the three ⚖️ items are Will's
WILL_NEEDS: §3 (i)–(iii), via PROME's judgment on whether they need his word now or at the next deck
FOLLOW-UP: Mon 10/26 L832 is the first live boot on the new charter; any mis-execution is reported as a charter defect, not patched silently
