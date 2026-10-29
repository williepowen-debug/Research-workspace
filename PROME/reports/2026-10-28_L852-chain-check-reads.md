# Independent read — check_heartbeat_chain() repair, fedf689ed (DOCKET L852) — 2026-10-28

Reader: Opus, read-only against the repo. Probe fixtures: `/tmp/claude-1000/-home-willi-Research-workspace-PROME/79a8b1bc-9934-45e0-8f29-755c4beae050/scratchpad/hbprobe/`.
Baseline: author suite 9/9 pass (stand-in runner, pytest absent); live `check_heartbeat_chain()` → ok=True "chain at 2 amendment(s) (header-declared count agrees)". VERIFIED.

Format: claim → artifact/command → observed → grade → proposed change. ❌ first.

| # | Claim (property) | Artifact / command | Observed | Grade | Proposed change |
|---|---|---|---|---|---|
| P-14 | A3: a file whose HEADER carries no readable declaration records FAIL/UNVERIFIABLE, never a silent PASS | `heartbeat_chain_counts()` + `check_heartbeat_chain(p)` on: header `**Base:** x, no declaration here.`, two `**Amendment N —` blocks, a body line quoting `the header's **Amendment chain: 2.** line` | (2, 2), ok=True, "chain at 2 … (header-declared count agrees)" — confident PASS | ❌ | `HB_DECLARED_RE.search` runs over the WHOLE file, so "header" in A3 is not mechanized: any body/quoted/archived occurrence fills a missing header declaration. Search only the header region, e.g. `text[:HB_BLOCK_RE.search(text).start()]` (whole text when no block). Tested in-probe: this scoping returns the same `declared` as the current code on all 43 files (42 archive snapshots + live) — history-neutral. Add a test for this fixture. Related P-01b: header without declaration, body quote `**Amendment chain: 1.**` before a later one → declared read from body (loud only because the count happened to disagree). |
| P-15 | Cross-check catches a block-format move | header `chain: 2`, two `**Amendment N —` blocks + third block in an unknown form `**Amdt 3 — c:**` | (2, 2), PASS | ⚠️ | Two-fault case (format moved AND header not bumped) is inherently invisible to a count-vs-declaration check. Declare as residue; no code change proposed. |
| P-13 | A6: prose mentioning an amendment is not a block | wrapped prose, line starts `amendment 2 is the operative one.` (lowercase) | (3, 2), UNVERIFIABLE, trips on 3 | ⚠️ | Fail-loud direction, but `re.I` + optional prefix makes any line-start prose a block. A6 only tested mid-line. Same for P-12 (`Amendment 1 above is superseded…` at line start) and P-16 (`**Amendment` / `2027 roadmap**` across a newline — `\s*` spans `\n`). Consider requiring `**`/`#`/`>` prefix and a dash/colon after the number, and `[ \t]*` instead of `\s*`. Noise that trips loud invites a later loosening. |
| A8 | Message names the accepted forms | `HB_FORMS` vs `HB_BLOCK_RE` | Message lists 3 block forms; regex also accepts bare `Amendment N`, `## Amendment N` without `>`, `> **Amendment N —` (P-05, P-06, P-12) | ⚠️ | Either narrow the regex to the three named forms or name what it really accepts. |
| A2 basis | Acceptance says the 34th-base snapshot is "prior style … `Chain: 4`" and the declaration moved at the 35th base | `grep` over snapshots; `git log -S'**Amendment chain:' -- HEARTBEAT.md` | The 10-23 and 10-26 snapshots already use `**Amendment chain: N.**`. The form first appears at 26f69a9da (2026-10-19, 33rd base); every snapshot through 10-19 uses `**Amendments append … Chain:`. Before this fix the check read no declaration from 10-19 to 10-28. The blocks were still counted in that period. | ⚠️ | Correct the A2 and defect-history wording. The old declaration form is now exercised only by the synthetic `OLD_STYLE` fixture. Any 10-19 or earlier snapshot would serve as a real-file test. |
| H1 | Regression over real history | `heartbeat_chain_counts` over every `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_*.md` + live | All 36 snapshots from 08-07 on + live: counted == declared. The 6 snapshots from 07-10 to 07-31 → declared None (from before declarations existed; now UNVERIFIABLE if checked) | ✅ | none |
| P-01 | Declaration appearing twice → header wins | header chain 2 + later body `**Amendment chain: 3.**` | (2, 2) PASS (first match = header) | ✅ | none (scoping in P-14 keeps this) |
| P-10 | Overlap: archived prior base pasted in the file | header chain 2, 2 new blocks + pasted old base with 4 `> **AMENDMENT #N` | (6, 2) UNVERIFIABLE, trips on 6 | ✅ | none — fail-loud |
| P-02/03 | Leading zeros, double digits | `**Amendment 01 —`, `002`; 12 blocks / chain 12 | (2,2) PASS; (12,12) ok=False "~5 trip HAS OCCURRED" | ✅ | none (count is by match, not number) |
| P-04 | Indented block | `  **Amendment 1 —` | (1, 2) UNVERIFIABLE | ✅ | none — loud |
| P-07 | `**Amendment 2 of 3 —` | — | counted | ✅ | none |
| P-08/19 | CRLF; UTF-8 BOM | bytes with `\r\n`; leading `﻿` | (2,2) PASS both | ✅ | none |
| P-09 | `Amendment chain: 0` with no blocks | — | (0,0) PASS "chain at 0" | ✅ | none — a fresh base declared at 0 is a legitimate PASS |
| P-11 | Table cell `\| **AMENDMENT #1` | — | not counted | ✅ | none |
| P-17/18 | Declaration variants `**Amendment chain:** 2.` / `**Amendment Chain: 2.**` | — | declared None → UNVERIFIABLE naming forms | ✅ | none — A3 fail-loud works |
| P-20 | Fenced code block (A6 declared N/A) | ```` ``` ```` fence containing `**Amendment 3 —` | counted (3 vs 2) → UNVERIFIABLE | ✅ (N/A confirmed loud) | none |
| A7 | Concurrent activity N/A | single read of one file | agreed | ✅ | none |

Verdict: **HOLD** — 1 ❌ (P-14: A3 "header" is whole-file. A missing header declaration plus a body quote of the declaration gives a confident PASS. The fix is to search only the header region, which changes no archive result).
Unresolved ⚠️: P-15 (two-fault blind spot, residue) · P-13/P-12/P-16 (line-start prose and newline-spanning matches over-count, loud) · A8 (HB_FORMS narrower than the regex) · A2 basis (declaration moved 10-19 at the 33rd base, not the 35th).

---

## READ 2 — result read of f2d450421 ("PROME: chain check reads the declaration from the header only"), 2026-10-28

Baseline: the stand-in runner passes 10/10 tests (`grep -c 'def test_'` = 10). Regression sweep at HEAD over 43 files (42 snapshots + live): 37 have counted == declared. The 6 from 07-10 to 07-31 have declared None, which is unchanged from read 1 because they predate declarations. VERIFIED.

| # | Claim (property) | Artifact / command | Observed | Grade | Proposed change |
|---|---|---|---|---|---|
| R5 / R8 | A3 after the fix: a header with no readable declaration records FAIL. The P-14 class is closed | `heartbeat_chain_counts()` + `check_heartbeat_chain(p)`. R5: header `**Base:** fresh, no declaration.`, zero blocks, body quotes `**Amendment chain: 0.**`. R8: header with no declaration, the only amendment written in an unrecognised form `**Amdt 1 — a:**`, body note quotes `**Amendment chain: 0.**` | Both give (0, 0), ok=True, "chain at 0 amendment(s) (header-declared count agrees)". This is a confident PASS. The new code does `header = text[:blocks[0].start()] if blocks else text`, so with zero recognised blocks the "header" is the whole file again. P-14 survives in the zero-block branch. R8 is the original L852 failure (block format moved, count 0, PASS) combined with a missing header declaration. | ❌ | Bound the header by a delimiter that does not depend on finding a block. For example, take the text before whichever comes first: a block, or the first body section (`^\*\*\d+\.` or `^#{1,3} *(\d+\.\|§)`). Tested in-probe: this rule returns the same declared value as HEAD on all 43 files, and it returns None for R5 and for R8 when the body section is numbered. It still falls back to the whole text when a file has no numbered section. A stricter option: when there are zero blocks, read the declaration only from the `**Base:**` paragraph, or treat a whole-file fallback as UNVERIFIABLE. Add R5 and R8 as tests. A non-zero body quote over zero blocks is already loud (R6). |
| R1 | P-14 fixture re-run | read-1 fixture | (2, None), UNVERIFIABLE naming the forms | ✅ | none |
| R2 | A false-positive "block" in the header region cuts the header off before the declaration | header line `Amendment 1 above was folded into the base.` before `**Base:** … **Amendment chain: 2.**` | (3, None), UNVERIFIABLE | ✅ (loud) | none. It joins the P-12/13 residue: line-start prose now also hides the declaration, which is still loud |
| R3 | Declaration placed after the blocks by a future style move | `**Amendment chain: 2.**` after the blocks | (2, None), UNVERIFIABLE naming the forms | ✅ | none. A8's message tells the next author what broke |
| R4 | Empty file | `""` | (0, None), UNVERIFIABLE | ✅ | none |
| R6 | Zero blocks, body quotes a non-zero chain | body `**Amendment chain: 3.**` | (0, 3), UNVERIFIABLE, trips on 3 | ✅ (loud) | none |
| R7 | The prior base's declaration appears in the header before the current one | `Prior base closed at **Amendment chain: 4.**; this base **Amendment chain: 2.**` | (2, 4), UNVERIFIABLE (first match wins) | ⚠️ | Loud, but it would trip the re-base rule on 4. Residue: the header should carry only one declaration token. |

Read-2 verdict: **HOLD — ❌ R5/R8** (the zero-block fallback reads the declaration from the whole file, so a body quote of chain 0 PASSes when the header has none, including when the block format has moved). Unresolved ⚠️: R7, plus the read-1 residue (P-15, P-12/13/16, A8, A2 basis) that the author has declared. Per the review budget, a fix made after this read is unreviewed unless Will names a third read.

WQ-249 closeout receipt: this reader wrote nothing inside /home/willi/Research-workspace. Writes were this ledger and the probe fixtures under the `scratchpad/hbprobe/` folder. Importing `prome_gate` and the test module from the repo may create `__pycache__` there, and both are gitignored-class artefacts. I did not stage or commit anything.

---

## READ 3 (ceiling) — result read of 13741d522 ("PROME: chain check anchors the declaration to its header line"), 2026-10-28

Baseline: the stand-in runner passes 13/13 tests (`grep -c 'def test_'` = 13). Sweep at HEAD over 43 files: 37 have counted == declared, and the 6 from 07-10 to 07-31 have declared None, unchanged from reads 1 and 2. Every file from 08-07 on carries exactly ONE `^**Base:**` line, and the 07-10 file carries none (`grep -c`). VERIFIED.

| # | Claim (property) | Artifact / command | Observed | Grade | Proposed change |
|---|---|---|---|---|---|
| S4 / S5 | A3 after the line anchor: a header with no readable declaration records FAIL. The R5/R8 class is closed | S4: header `**Base:** fresh, declaration dropped.`, zero blocks, a body paragraph that STARTS `**Base:** (quoted from the prior file) **Amendment chain: 0.**`. S5: same, but the two amendments are written in a moved format `**Amdt N —` | Both give (0, 0), ok=True, "chain at 0 amendment(s) (header-declared count agrees)". This is a confident PASS. The anchor accepts ANY line that starts `**Base:**`. With zero recognised blocks the header scoping falls back to the whole text, so a body paragraph that quotes the header line stands in for it. S5 is again the original L852 shape (format moved, count 0, PASS) behind a dropped declaration. The exposure is narrower than R5/R8: the quote must start a line with `**Base:**`. | ❌ | Read only the FIRST `^**Base:**` line, falling back to the FIRST `^**Amendments append` line. A declaration-free first line ⇒ None. Tested in-probe: this rule returns the same declared value as HEAD on all 43 files and returns None on S4 and S5. (My first version of the idea, "first anchor line of either kind", was wrong: it differed on 34 files, because pre-33rd files have both a Base line and an Amendments-append line. It is recorded here so nobody adopts it.) Since every real file has exactly one Base line, an alternative is that a second `^**Base:**` line ⇒ UNVERIFIABLE. Per the ceiling this is now a DISPOSITION, not an edit. |
| R5 / R8 re-run | Read-2 fixtures | as in read 2 | both (0, None), UNVERIFIABLE | ✅ | none |
| S1 | A Base line carries the prior base's figure before the current one | `**Base:** … Prior base closed at **Amendment chain: 4.**; this base **Amendment chain: 2.**` | (2, 4), UNVERIFIABLE (`.*?` takes the first figure) | ⚠️ (loud) | Same as R7: one declaration token per header line. Residue. |
| S9 | Two Base lines in the header | pointer line `**Base:** … chain: 0` then the real `**Base:** … chain: 2` | (2, 0), UNVERIFIABLE | ✅ (loud) | none |
| S2 / S3 | Base line inside a blockquote or list | `> **Base:** …`, `- **Base:** …` | (2, None), UNVERIFIABLE naming the forms | ✅ (loud) | none |
| S6 | CRLF line endings | bytes with `\r\n` | (2, 2) PASS | ✅ | none |
| S7 | Base line hard-wrapped before the declaration | `**Base:** …\nby an editor. **Amendment chain: 2.**` | (2, None), UNVERIFIABLE | ✅ (loud) | none |
| S8 | BOM directly before `**Base:**` on line 1 | `﻿**Base:** …` | (2, None), UNVERIFIABLE | ⚠️ (loud) | Real files open with `# HEARTBEAT.md`, so the exposure is low. A `utf-8-sig` read would remove it. Residue. |
| S10 | Fresh base declaring chain 0 | `**Base:** x. **Amendment chain: 0.**`, no blocks | (0, 0) PASS | ✅ | none |

Read-3 verdict (ceiling): **HOLD — ❌ S4/S5** (with zero recognised blocks, a body paragraph that starts `**Base:**` and quotes `**Amendment chain: 0.**` still passes when the real header declaration is missing). The review budget says this ❌ is now a disposition: WITHHELD, or STILL UNRESOLVED with a DOCKET row, or a further read named by Will. It cannot be fixed and called verified. Unresolved ⚠️: S1/R7 (first figure on a Base line wins), S8 (BOM), plus the residue the author declared after read 1 (P-15, P-12/13/16, A8, A2 basis).

WQ-249 closeout receipt (read 3): I wrote nothing inside /home/willi/Research-workspace. Only this ledger and the fixtures in the `scratchpad/hbprobe/` folder. The only side effect inside the repo is `__pycache__` from imports, which is gitignored (`git check-ignore` confirmed). Nothing staged or committed.
