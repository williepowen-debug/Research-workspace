# ACCEPTANCE — ARGUS-efficiency P3: SHARED paths read by AUTHORSHIP EVIDENCE, every path still listed

**Written 2026-10-10 17:26 ET** (after read 1 ❌4 split P3 out of the P1 episode), per `PROME/CLAUDE.md` § Session Process Controls (WQ-229). Will's word 16:56 ET (WQ-417 RULED APPROVE). CATO's condition (16:50 ET): preserve visibility of every shared path and demonstrate that PROME-authored cross-directory work cannot disappear, including the historical hidden-packet case.
reads: 2   (read 1: no path dropped, 29/29 listed, ⚠️9 named three evidence gaps; read 2 ⚠️5: `via-PROME` matched 4 desk-written files in history and `MSG-*.md` ignored the sender in the filename — both corrected in pass 3: via-PROME is now labelled 'likely writer, confirm at git log', MSG matches `MSG-PROME-` only)

## The change, in its own terms
`argus_scope.py` labels every SHARED path `SHARED/PROME-EVIDENCED` or `SHARED/UNEVIDENCED`; the ARGUS agent definition reads EVIDENCED paths in full and LISTS unevidenced ones unopened unless an OWNED hunk references them. The lane stays SHARED; nothing is reclassified; nothing is dropped.

## Acceptance conditions
- **P3-AC1 (visibility):** the path listing with and without the change is identical in length and membership for the same tree (every SHARED path printed, with its sub-lane).
- **P3-AC2 (the hidden-packet case):** `AGENTS/FALCON/inbox/data/…` committed by 888924d2e (`PROME -> FALCON, DAEDALUS: …`) reads PROME-EVIDENCED by commit subject; the 10/10 `from-PROME` packets read PROME-EVIDENCED by filename even while pending (uncommitted).
- **P3-AC3 (evidence rules, closing read 1 ⚠️9):** a relay PROME wrote, named `from-X-via-PROME_…`, is EVIDENCED (`via-PROME`); a top-level `AGENTS/<X>/inbox/MSG-PROME-*.md` is EVIDENCED (Direct Messaging v1 names the sender in the filename, `MSG-<SENDER>-<date>-<n>__…`; `MSG-WALTER-…` is not); `via-PROME` is evidence of LIKELY authorship with a confirm-at-git-log label (4 desk-written files in history carry it); a commit subject `Prome: …` / `prome ->` counts (case-insensitive); `from-PROMETHEUS` and a `PROMETHEUS:` subject do NOT count.
- **P3-AC4 (the reader cannot skip evidenced work):** the agent definition (root and PROME copies byte-identical) instructs: EVIDENCED → read in full and audit on the named evidence; UNEVIDENCED → list, open only on an OWNED reference or a declared consumed move; report how many were listed unopened.
- **P3-AC5 (measure, P5):** the next ordinary Standard closeout's RUN-LOG row records tokens · tool uses · seconds · lines, PLUS the correction effort after it, beside today's figures (238,445 tokens · 83 tool uses · 676 s; then a 5.3-min reader and three fix passes) — one comparison, no standing programme.

## Neighbours
- **Ordinary:** a WALTER signal file in another desk's inbox → UNEVIDENCED, listed. **Overlap:** a path both pending and committed by a PROME subject → EVIDENCED (either side suffices). **Wrong owner:** a desk's own `from-<DESK>` packet in PROME's inbox is EXCLUDED by the perimeter before sub-lanes apply — N/A here, stated. **Missing information:** a sha absent from the window's subject map → no evidence from that sha (never an error). **Concurrent activity:** the subject map is read once per run; a commit landing mid-run is outside the baseline window — N/A.

## Completion note (17:26 ET)
IMPLEMENTED (rules + labels + agent text) · TESTED (`tests/test_argus_scope_evidence.py`, 7 cases) · INDEPENDENTLY VERIFIED: read 1 covered visibility and found the three gaps; read 2 re-checks the three rules · STILL UNRESOLVED: none known.
