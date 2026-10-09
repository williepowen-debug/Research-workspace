# PLAN READ 1 — FORGE/STATUS.md rotation 2026-10-08 (blind cold reader, Opus; read-only)
Stamped: Thu Oct  8 18:55:42 EDT 2026

```
COLDREADER · PROME/plans/2026-10-08_forge-status-rotation-PLAN.md · 17228 B · 89 claims
SCORE: 56/89 ✅ · 24 ⚠️ · 9 ❌
INVARIANTS: 8 PRESENT · 3 PART-MISSING · 0 MISSING · 2 CONTRADICTED
POINTERS: 24/24 file/commit/row pointers resolve; 2 LINE pointers mis-aimed (L92→is L94; L143→is L145)
ONE-LINE VERDICT: no — the verbatim mechanics are clean, but the hot VLO note misstates who acts on a B1 fire, one ID (WQ-347) vanishes against invariant 7, and the hot file's own pass note asserts a byte-identity L9 does not have.
```

Conventions. S = scratchpad `forge-rot/`; SRC = `git show ef2bc83f1:FORGE/STATUS.md` (183 lines; working copy byte-identical: `git diff --quiet -- FORGE/STATUS.md` rc=0, `cmp` IDENT); CAND = `S/STATUS_candidate.md`; ARCH = `S/STATUS_ROTATION_2026-10-08.md`; PLAN = the plan. Line numbers are 1-based. Confidence: every row below is VERIFIED at the artifact unless marked INFERRED / UNKNOWN / SEARCH-NOT-FOUND. All Python was run from stdin with `-B` (no bytecode written); no file was written except this ledger.

## ❌ (9)

| # | Claim | Artifact | Verification command | Observed | Proposed change |
|---|---|---|---|---|---|
| 5 | "The next edit is Friday 10/9's reconcile (…), which can only add bytes." | PLAN:5 | read PLAN:5 against PLAN:77 | PLAN:77 says that same reconcile shrinks the file: "Dated re-trigger: Friday 10/9's reconcile — the three Oct-09 rows leave the hot table (≈1.5 KB)". The two sentences contradict each other (rationale class, not action) | drop "can only add bytes" or say "adds fills before it can drop rows" |
| 20 | Chunk B survives at "L92 rewritten: not captured since 9/29; $295.15 / BP $8.94 …"; audit row: "chunk B verbatim; L92 names them" | PLAN:11, PLAN:48 | python diff of SRC vs CAND lines 1–111 | changed lines = {5,9,15,28,36,94,104}. CAND:92 is byte-identical to SRC:92 ("*All holdings/figures below retained from the 9/29 source; …*"); the rewritten text and the D-57/D-58 mention sit at CAND:94 | L92 → L94 (both sites) |
| 26 | Chunk G survives at "L143 of the candidate: the consumer registry VERBATIM …"; repeated at audit row "restated verbatim in the new L143 note" and invariant 10 "in the new L143" | PLAN:17, PLAN:49, PLAN:63 | `sed -n 143p;145p CAND` | CAND:143 = "*History → `_archive/JOURNAL.md` \| Prior reconciles …"; the PARSED-BY-MACHINE line is CAND:145. Content claim itself holds (registry prefix verbatim, 1,012 B, python prefix compare True) | L143 → L145 (three sites) |
| 44 | "Will supplies (14) · PROME re-reads (D-62 · D-65)" for the 17 carried IDs | PLAN:39 | python over CAND:122 + chunk_D1/D2 owner cells | CAND:122 lists **15** IDs under "**Will supplies** D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1". 14+2=16≠17. The 14 is right only if D-28 is excluded — its recorded owner cell (SRC:141) is "RH history before 9/01", no person — but CAND files D-28 under Will (see ⚠️ 23) | reconcile the count and D-28's placement in one direction |
| I6 | "The VLO note (R28) restates GATE-TERRY-VLO-HELD-01 … without changing a level, operator, instrument, date or **consequence**"; chunk-H row restates it as "B1 signed export-restriction text at primary ⇒ SELL next regular session; TERRY grades, Will executes" | PLAN:59, PLAN:18 | `sed -n 21p PROME/GATES.tsv \| tr '\t' '\n'` (cells 3–5) vs CAND:28 | GATES consequence cell: *"B1 (TERRY §3 verbatim): "SELL the share at the next regular session. Will can act on this without the desk. TERRY writes the rec at its next touch if Will has not acted." — NEVER an order placed for him."* SRC:28 carried it: "(Will may act without the desk; TERRY recs if he has not); **A:** TERRY grades, Will executes". CAND:28: "B1 = signed US distillate export-restriction text at primary ⇒ SELL next regular session; TERRY grades, Will executes (rule 7)." — the A-scoping is gone and "TERRY grades, Will executes" now trails B1, so a reader waits for TERRY on a B1 fire. Ruling record (`2026-10-07_VLO-…-RULED.md`:31) "Policy legs B1–B3 and their existing execution limitations continue unchanged" | restore "A: TERRY grades, Will executes; B1: Will may act without the desk, TERRY recs if he has not" |
| I7 | "every ID in chunks C, D1, D2, E, I appears in the hot candidate with its owner" | PLAN:60 | python regex `D-\d+\|WQ-\d+\|GATE-…\|MGMT-…\|L\d{3}\|sha9` over SRC, CAND, each chunk | the ONLY source ID absent from CAND is **WQ-347**, present in chunk C at SRC:116 ("\| WQ-347 \| **QQQ $755P Oct-09 ×1 (was ×2)** \|") and SRC:120 ("\| WQ-347 \| **QQQ $745P Oct-15 ×1 (was ×2) + $740P Oct-15 ×4** \|"); `grep -c WQ-347 CAND` = 0. (WILL_QUEUE row 347 is now the D-71 Activity-scroll ask; CAND's D-71 row does not cite it either) | carry WQ-347 on the D-71 row / EXPIRING italic, or state it was re-cut |
| 69 | Install step 1: "(then `git diff --stat` shows exactly these two paths plus the TSV in step 3)" | PLAN:69 | `git diff --stat \| tail -1`; `git status --short \| wc -l` | unscoped `git diff --stat` already shows 13 files changed by other sessions (NEXUS, WALTER, PROME/WILL_QUEUE.md, PROME/DOCKET.tsv …), and the new archive is UNTRACKED so `git diff --stat` can never show it. The check cannot pass as written | path-scope it: `git status --short -- FORGE/` (shows `??` for the archive) |
| 72 | "§ Off-thesis rows 44–48 = 2,412 B" | PLAN:77 | `sed -n 44,48p CAND \| wc -c`; python len(str) vs len(bytes) | **2,461 B** (wc -c). 2,412 is the CHARACTER count incl. newlines (python `len(str)` = 2,412) — the ad-hoc `len()` error the measure.py rule forbids | re-measure with measure.py/wc -c |
| 77 | CAND pass note: "the header money line, `**Updated:**` and `marks =` are byte-identical" | CAND:145 | python: CAND:9 minus the one insertion == SRC:9 → True; CAND:9 == SRC:9 → False | PLAN:24 itself says L9 gets "ONE append inside the existing "rotations →" list"; the header money line IS L9 (SRC:9 "> **Updated:** 2026-10-08 … **Fidelity account total:** $34,650.69 …"), changed by a 94-B insertion. Only the parsed fields are identical | "the header money line's parsed fields (…) are byte-identical; one rotation pointer appended" |

## ⚠️ (24)

| # | Claim | Artifact | Verification | Observed | What a stranger needs |
|---|---|---|---|---|---|
| 2 | builder "extracts the chunks from the committed file by exact line range" | PLAN:2 | `sed -n 4p S/build.py` | build.py:4 reads the WORKING file `ROOT/'FORGE/STATUS.md'`, not `git show ef2bc83f1:` — identical today (cmp), so outputs are right; a re-run after any edit would silently diverge (anchors at build.py:10–17 catch only some moves) | say "working copy (verified == ef2bc83f1)" or read via git show |
| 8 | "PROME/registry/READS.tsv: WALTER `scoped`; TERRY and NEXUS parse it by script" | PLAN:5 | `grep FORGE/STATUS PROME/registry/READS.tsv`; `grep -rl FORGE/STATUS AGENTS/NEXUS --include=*.py/.sh/.js` | WALTER scoped ✅ (READS.tsv:238); TERRY ✅ (positions_from_forge.py); NEXUS: SEARCH-NOT-FOUND (no NEXUS script reads the file) | name the NEXUS consumer or drop it |
| 23 | D2 survives with "owners as recorded (Will supplies · PROME re-reads)" | PLAN:14, CAND:122 | owner cells of chunk_D2 | D-28's recorded owner cell (SRC:141) = "RH history before 9/01" (no person); CAND:122 files it under "Will supplies". Every other row matches its cell | file D-28 as "RH history (owner unnamed)" or say Will is inferred |
| 34 | L36/L104 "shortened in place; no identifier, figure or pointer removed" | PLAN:26 | diff SRC:36/104 vs CAND:36/104 | figures kept, but L36 drops the basis words "realized"/"total" and the year (2026-07-30 → 7/30); L104 drops the date "(this section's only row since 9/19)" | keep "realized" (basis) |
| 40 | Audit row: USO $150C "exercise unfundable" (column header: "Obligation (in moved text)") | PLAN:35 | `grep -c unfund` SRC, CAND, 10/01 archive | 0 / 0 / 0 — a new assertion with no source in the moved text | cite its basis or drop it |
| 45 | D-47 owners "Will (manual harvest) · REGINALD grades · TERRY proposes" carried by the RH row | PLAN:40 | read CAND:98, CAND:124 | Will's manual act ✅, REGINALD ✅; "TERRY proposes" survives only in chunk E | — |
| 48 | APD item owner "PROME / Will" carried | PLAN:43 | CAND:29, CAND:124 | facts survive; neither line names an owner | — |
| 55 | "Nothing is closed, re-dated, re-owned, re-graded or re-marked by this rotation" (also CAND:122 "None closed, re-dated or re-owned") | PLAN:51 | see #23, I7 | D-28 re-homed under Will; WQ-347 label dropped. No date/mark changed (figure test, §D CE5) | — |
| I1 | "Parser contracts unchanged … `pending_receipts.py` output identical" | PLAN:54 | in-memory `extract()`/`holdings()`/parse_money regex on SRC vs CAND; pending_receipts closure-candidate regex replicated | positions_from_forge: 19/3 live/withheld both sides, only VLO `note` differs, 0 warnings, baseline JSON == SRC; holdings(): 22 rows both, only VLO note differs (line numbers do NOT differ); parse_money: identical tuple; selftest PASS. pending_receipts: output identical only because BRENT TRADE.md has no pending row, so FORGE is never read; its FORGE closure-candidate set CHANGES — STNG at SRC:146 (D-17 "Recalled / closed pre-7/30") → none in CAND | state that pending_receipts' FORGE leg is untested (vacuous) and STNG's candidate line leaves |
| I8 | "The CLOSED italic keeps D-72's and D-73's figures as DERIVED and the 'per-row contract counts NOT shown' caveat" | PLAN:61 | CAND:126 vs chunk_F | D-72 figures + caveat ✅; D-73's figures (entries −$2,122.65 … ; running balance $15,524.70 → $12,993.82 → $11,421.19) are NOT in the italic ("the five 10/2–10/7 entries, every running-balance link holds") — they survive scattered in position rows / D-71 row | narrow the invariant to D-72 or carry D-73's balance chain |
| I12 | mapping re-pin "by a script that proves each mapped identity's position row (or terminal italic) is byte-identical old→new … (none expected)" | PLAN:65 | python over `FORGE/position_management.tsv` (source==FORGE/STATUS.md: 10 rows ✅, none VLO ✅, sha 18075a846ab4… = current file ✅) | 8 of 10 identities have a row/italic in both versions; **QQQ $730P Sep-30 and USO $159C Sep-30 (Fidelity) have NONE in SRC or CAND** (their dispositions −$2,229.54 / −$919.46 live only in `_archive/STATUS_ROTATION_2026-10-01.md`). A ticker+strike script false-matches SRC:137 (D-61 "QQQ 730P ×1", moved to chunk D2) and SRC:94 (RH "USO $159C Sep-11", a different contract, moved to chunk B). No such script exists in S yet (UNKNOWN) | name the evidence line per mapping, or hand-review the two |
| 74 | "register as a DOCKET row for the FORGE owner (PROME)" | PLAN:77 | — | future act, no row ID; the Friday ANVIL rotation is also an unregistered expectation | give the row ID at commit |
| 76 | D-62/D-65 images "desktop-local and gitignored" (also CAND:122 "desktop-local images") | PLAN:79 | search `PROME/data/2026-09-29_broker-capture-TRANSCRIPTION.md` | UNKNOWN — no image path found; new qualifier not in SRC:133/136 | cite the path |
| 78 | CAND pass note: "every mapping pinned to this file re-reviewed and re-pinned in the same commit" | CAND:145 | — | asserts install step 3 as done before it happens; true only if the TSV ships in the same commit | keep, but the install must not ship without step 3 |
| 80 | Will's quote | CAND:28 vs SRC:28 | diff | SRC “Yes, still one share” → CAND “Yes, still one share.” — a period added inside a verbatim operator quote | restore verbatim |
| 81 | "(rule 7)" | CAND:28 | diff | SRC attached "(rule 7)" to "not adjudicated here"; CAND attaches it to "TERRY grades, Will executes". Bare "rule 7" — which numbered list? (root rule #7 is "Roll duration…") | qualify the list |
| 82 | VLO-SCALE "TERMINAL on the 9/25 F1 fire" | CAND:28 vs GATES:19 state cell | — | state token right; dropped SRC:28's "optional CME source-① override remains as written" — GATES: "if CME's official … settle … reads ≥ 4.4622, ① supersedes ②, F1 was NOT fired and this row REVERTS to LIVE" | keep the reversion clause |
| 83 | VLO held-share A-leg restated | CAND:28 vs GATES:21 condition | — | levels/dates/instrument ✅ (table in §C). Dropped from the hot note: "prior exits remain owed" (in SRC:28; GATES "A prior established exit remains owed through switch, missing data or sunset") and "A is SUSPENDED … after 2026-11-19 absent another ruling" | keep "prior exits remain owed" |
| 84 | B1 definition "signed US distillate export-restriction text at primary" | CAND:28 vs GATES:21 | — | wording unchanged from SRC:28, but PLAN:59 lists "B1 = signed presidential action with legal force at primary (whitehouse.gov / Federal Register)" — none of those words are in CAND; a Commerce/BIS licensing rule is in GATES' B1 but is not "signed presidential" | name the primary sources |
| 85 | "`PROME/GATES.tsv` is canonical for both gates" | CAND:124 | — | the line names ROLL70-EXIT and "VLO-SCALE"; the live VLO rule is a third gate (VLO-HELD-01). "both" is ambiguous | name the gates |
| 86 | Summary row R_D | CAND:122 | 6 cells ✅ | owners sit in the "What is known" column; "Decision owner" cell = "per row, as recorded"; "What is conjectured" cell = "A row re-enters this table only when it moves" (a rule, and "moves" undefined) | put owners in the owner column |
| 87 | "Pass notes 9/27 → 10/8 → rotation 10/08 chunk G" | CAND:145 | read chunk_G | chunk G holds the 10/8 note and only POINTERS to the 9/27–10/1 notes (rotation 10/01 chunk F) and the 10/7 note (`git show e8fd99acf`) — two hops, read as one | "10/8 note → chunk G; earlier → 10/01 chunk F" |
| 88 | ARCH header: "Every chunk below is … SUPERSEDED in the hot file by a pointer or a shorter restatement" | ARCH:3 | `grep -o 'chunk [A-Z0-9]*' CAND` | chunks A,B,C,D1,D2,E,F,G,H are cited from CAND; **chunk I is cited nowhere** | add "→ chunk I" on CAND:138–139 |
| 89 | ARCH header: "as committed at `ef2bc83f1` (the 10/8 intraday reconcile ef2bc83f1 + the mappings pass a1eb75287 …)" | ARCH:3 | `git show --stat a1eb75287` | a1eb75287 touches only `FORGE/position_management.tsv` (child of ef2bc83f1); the "+" reads as if it contributed to the source text | drop or say "HEAD also includes a1eb75287 (TSV only)" |

## ✅ (56), compact: claim → artifact → command → observed
- 1 date Thu 2026-10-08 / laptop → PLAN:1 → `date`; `hostname` → Thu; WilliePOwen.
- 3 32,523 B = 100% of 32,550 → PLAN:5 → measure.py FORGE/STATUS.md → 32523 B, 183 lines, 99.92%.
- 4 rotate-tier → PLAN:5 → read `scripts/read_cap_check.py:696–703` → 24,412.5 ≤ 32,523 < 32,550 ⇒ 🟡 "rotate-tier" (INFERRED from code; not run with a file arg).
- 6 SCRATCH "27 B under cap ⇒ SPLIT FIRST at the next edit" → PROME/SCRATCH.md:8 → grep → present; 32,550−32,523 = 27.
- 7 10/01 precedent → `ls FORGE/_archive/` → STATUS_ROTATION_2026-10-01.md exists (chunks A–F).
- 9–18 chunk receipts A 1084·3510813514 · B 842·2632567345 · C 2926·2591328773 · D1 523·2218341014 · D2 4007·487926030 · E 1664·2660099432 · F 936·2479073510 · G 1772·89507236 · H 1172·2811584083 · I 521·365315039 → PLAN:10–19 + ARCH:6–15 → `git show ef2bc83f1:FORGE/STATUS.md | sed -n a,bp | cmp - chunk_X` (10/10 equal) + measure.py over each chunk (10/10 match bytes and crc32) + python split of ARCH on `## Chunk` headings (10/10 section bodies == chunk files).
- 19 A survives: CAND:5 keeps source, Σ $21,945.52 + $11,421.19 + $1,283.98 = $34,650.69, 1 NEW · 0 GONE · 2 QTY · 16 MARK, "→ … chunk A".
- 21 C survives: CAND:112 italic names all 7 expiring lines with Fri 10/09 · Thu 10/15 · Fri 10/16 (weekdays python-verified), points to rows + § Immediate Actions; D-60 first row.
- 22 D1: CAND:122 "PROME record only D-75 (mirror carries $322.65)".
- 24 E: CAND:124 italic; live letters at CAND:27–29 and CAND:98.
- 25 F: CAND:126; SRC/CAND:50 "(D-72 → § Reconcile discrepancies, CLOSED this pass)" still lands on it (text, not heading).
- 27 H first seven cells byte-identical → python split → True.
- 28 I: CAND:138–139 two rows as described.
- 29 CAND 145 lines, 23,986 B, crc32 2657826509, 73.7% → measure.py → exact.
- 30 ARCH 94 lines, 18,637 B, crc32 1512527879 → measure.py → exact.
- 31 under 24,412 by 426; over 22,785 by 1,201 → python → 426 / 1,201; 0.75×32,550 = 24,412.5, 0.70×32,550 = 22,785 (READ_CAP.md:11 rule 5 states both figures).
- 32 L9 single insertion; four parsed shapes identical → python (CAND:9 minus 94-B insert == SRC:9; parse_money regexes → ('34,650.69','11,421.19','32.96','2026-10-08','2026-10-08') both).
- 33 L15 HEARTBEAT "TWENTY-EIGHTH re-base" → `head -c 1500 HEARTBEAT.md` → present.
- 35 D-60 copied verbatim → `cmp <(SRC 117) <(CAND 118)` → equal.
- 36 Edits list complete → python positional diff L1–111 → only {5,9,15,28,36,94,104} changed, each accounted for; SRC 106–111/122–127/129–130/163–173/178–182 == CAND counterparts (diff clean).
- 37–39, 41–43, 46–47, 49–54 audit rows (755P incl. WQ-397 = WILL_QUEUE row 397 + HEARTBEAT:43; D-60; 750C; 745P/740P; TLT/HBAN at CAND:62/85/137; D-75; WQ-386 carriage at CAND:28; WQ-200 at CAND:27; D-72/D-73; D-71 CAND:119/138; D-70/D-74 CAND:120–121/139; receipt chunk A; prediction-market/D-57/D-58 in chunk B (L-pointer counted at #20); conventions sentence verbatim at CAND:145).
- I2 position rows byte-identical except VLO note → python over table lines in `## Fidelity`/`## Robinhood`/`## Account` → 36/36 lines, 1 diff (VLO), first seven cells equal.
- I3 → see #32. I4 → see #9–18. I5 → see #35.
- I9 → no position row changed; `[9/29 13:4x intraday]` at CAND:9/94; "marks are NOT closes" at CAND:5.
- I10 registry verbatim through "New consumers: …" (python prefix compare True, 1,012 B); pass note says "no structural change inside any `## Fidelity` / `## Robinhood` / `## Account` region" (locator L143 wrong → #26).
- I11 23,986 < 24,412 (candidate; install re-measures); miss declared PLAN:77 with dated re-trigger Fri 10/9.
- I13 `git log -1 --format=%h -- FORGE/STATUS.md` = ef2bc83f1 = ARCH:3; receipts computed by build.py:36 and reproduced by measure.py.
- 70 commit pathspec set (4 explicit paths, PROME-owned FORGE + own plan) → PLAN:74.
- 71 1,201 B over <70% → as #31. 73 three Oct-09 rows ≈1.5 KB → `sed -n 44,46p | wc -c` = 1,574 B. 75 KRE duplicated empty header → SRC:66–67 and 70–71 → present.
- 79 "three `###` subsections became italic pointer lines and 18 carried rows one summary row" → python header diff: removed `### EXPIRING …`, `### Owner decides — ruled / gated`, `### CLOSED this pass …`; none added; `## ` list identical; chunk D1+D2 = 18 rows = R_D's 18 IDs (same order).

## B. Specific tests (summary)
- Chunks == source ranges: 10/10 cmp-equal; measure.py reproduces every header byte+crc; ARCH section bodies == chunk files 10/10.
- Position rows: 36/36 region table lines identical except VLO (first 7 cells identical).
- L9: one 94-B insertion; parsed shapes identical.
- IDs: every D-ID in SRC is in CAND; **WQ-347 is the one SRC ID missing** (❌ I7). No ID appears in CAND that is not in SRC.
- VLO note vs gates (side by side):

| Element | GATES / ruling cell | CAND:28 | Grade |
|---|---|---|---|
| sell line | "closes BELOW $90.16" · ruling "strictly below $90.16 … for TERRY's SELL recommendation" | "A = matched crack settlement < $90.16 ⇒ sell rec" | ✅ |
| notice | "a settlement below $95 … = NOTICE ONLY on the held share … no action" | "(< $95 notice)" | ✅ |
| Nov window | "HOX26×42 − CLX26 through 2026-10-14" | "Nov through 10/14" (formula not spelled; same as SRC) | ✅ (abbrev.) |
| Dec window | "HOZ26×42 − CLZ26 for 2026-10-15 through 2026-11-19 inclusive" | "Dec HOZ26×42−CLZ26 10/15–11/19" | ✅ |
| suppression | "No adjustment, persistence test, roll suppression or automatic January roll" | "no roll suppression" | ✅ |
| review | "review 2026-11-18" | "review 11/18" | ✅ |
| suspension / prior exits | "SUSPENDED … after 2026-11-19 absent another ruling"; "A prior established exit remains owed …" | absent (SRC had "prior exits remain owed") | ⚠️ #83 |
| B1 definition | "A signed presidential action with legal force that bans, caps or licenses … — primary source required: … whitehouse.gov … or the Federal Register" | "signed US distillate export-restriction text at primary" | ⚠️ #84 |
| B1 consequence / who acts | "Will can act on this without the desk. TERRY writes the rec at its next touch if Will has not acted." | "⇒ SELL next regular session; TERRY grades, Will executes (rule 7)" | ❌ I6 |
| A who acts | owner cell "TERRY (grades …, writes the SELL rec) / Will (executes by his own hand)" | "TERRY grades, Will executes" | ✅ |
| VLO-SCALE | state "RESOLVED(TERMINAL — F1 FIRED for 2026-09-25 …)" + optional CME reversion | "TERMINAL on the 9/25 F1 fire, TERRY 4ad672c43" | ⚠️ #82 |

- D-60: CAND:118 == SRC:117 (cmp).
- Headers: no `## ` change; three `### ` removed (all under `## ⚠️ Reconcile discrepancies`). positions_from_forge sets `in_region=False` on that `## ` (`extract()` L210–212) so `SUBSEC_RE` there has no effect; desk_attention `holdings()` sets `account=''` there (L60–61) so its `###` ticker capture is inert; will_brief reads only before the first `## `; pending_receipts reads BRENT TRADE.md sections. No parser keys on the removed headers.
- Size: 23,986 B (crc32 2657826509); −1,201 vs 22,785 and +426 headroom vs 24,412 — the declared deviation is stated truthfully.
- Archive source commit = `git log -1 --format=%h -- FORGE/STATUS.md` = ef2bc83f1 ✅.

## C. Invariant audit
| Inv | State | Evidence |
|---|---|---|
| 1 | PART-MISSING | 3 parsers identical except VLO note (tested in memory); pending_receipts identical only vacuously; its FORGE closure candidates lose STNG (SRC:146) |
| 2 | PRESENT | 36/36 rows, VLO first 7 cells equal |
| 3 | PRESENT | one 94-B insert; parse tuple identical |
| 4 | PRESENT | 10/10 cmp + measure.py |
| 5 | PRESENT | cmp equal |
| 6 | CONTRADICTED | B1 execution path (GATES:21 cell 5 vs CAND:28) |
| 7 | CONTRADICTED | WQ-347 absent from CAND (SRC:116, :120) |
| 8 | PART-MISSING | D-73 figures not in CAND:126 |
| 9 | PRESENT | rcv / intraday stamps intact; "marks are NOT closes" CAND:5 |
| 10 | PRESENT | registry prefix verbatim; locator says L143, it is L145 (#26) |
| 11 | PRESENT | 23,986 < 24,412; miss declared PLAN:77 |
| 12 | PART-MISSING | pending install; 2 of 10 mapped identities have no evidence line in either version |
| 13 | PRESENT | ef2bc83f1; receipts computed |

## D. Counterexamples (my own)
- CE1 (invariant 1 blind spot) — pending_receipts closure-candidate regex replicated on SRC vs CAND: STNG candidate at SRC:146 → none in CAND. Invariant 1's "output identical" passes because TRADE.md has no pending row. **Not caught by the invariants.**
- CE2 (owner silently changed) — D-28 owner cell "RH history before 9/01" → CAND "Will supplies … D-28"; plan's own count (14) disagrees with CAND (15). Invariant 7 passes (an owner is named). **Not caught.**
- CE3 (mapping evidence missing) — QQQ $730P and USO $159C Sep-30 mappings cite "recorded at FORGE/STATUS.md" but no row/italic exists in SRC or CAND; a ticker+strike matcher false-matches the RH USO $159C **Sep-11** line (SRC:94→chunk B) and D-61 (SRC:137→chunk D2). **Not caught by invariant 12.**
- CE4 (hot file's self-claims) — no invariant tests the new pass note's assertions; one is false (❌ 77). **Not caught.**
- CE5 (figure drift) — every $ figure, m/d date, ×n, n-of-n, 9-hex sha and HO/CL formula in the 14 rewritten CAND lines (5,9,15,28,36,94,104,112,122,124,126,138,139,145) exists in SRC; only new tokens are "10/08" pointer labels and "(18)". **Negative — no drift.**
- CE6 (dead pointer) — every "rotation 10/08 chunk X" in CAND resolves to an ARCH heading; chunk I has no inbound pointer (⚠️ 88). Weekday check on all cited dates (10/8 Thu … 12/31 Thu): all correct.
- CE7 (measurement method) — PLAN:77's 2,412 "B" reproduces exactly as python `len(str)`; bytes are 2,461 (❌ 72). The plan's measure.py discipline is not an invariant.

## E. Stranger misreads in the new hot lines
- CAND:28 "TERRY grades, Will executes (rule 7)" trailing B1 → reads as "wait for TERRY" on a B1 fire (❌ I6); "rule 7" names no list.
- CAND:28 "matched crack" — which crack (ULSD) and the Nov formula are not given in the hot line.
- CAND:124 "canonical for both gates" — three gates are in play.
- CAND:122 owners in the "known" column; "re-enters this table only when it moves" — "moves" undefined.
- CAND:145 "Pass notes 9/27 → 10/8 → … chunk G" — a two-hop chain read as one; "header money line … byte-identical" is false (❌ 77).
- CAND:36 "(CLOSED 7/30, −$111.60)" — no year, no "realized" basis.
- CAND:138–139 → no pointer to chunk I (the four prior 🟡 rows).
- No chunk cited in CAND is missing from ARCH; no undated figure was introduced.

## Totals
89 claims · 56 ✅ · 24 ⚠️ · 9 ❌ · invariants 8 PRESENT / 3 PART-MISSING / 0 MISSING / 2 CONTRADICTED · counterexamples 7 devised: 4 found defects the invariants miss (CE1–CE4), CE7 found a method error, CE5–CE6 negative (CE6 found one unreferenced chunk).
Action-class ❌: I6 (who acts on B1), I7 (WQ-347), 69 (install check cannot pass), 77 (false self-claim in the installed file). Pointer/basis-class ❌: 5, 20, 26, 44, 72.
Reads: this is plan read 1 of the episode.
