# RESULT READ 2 — FORGE/STATUS.md rotation 2026-10-08 (blind cold reader, Opus; read-only)
Stamped: Thu Oct  8 19:18:27 EDT 2026 (`date`)

```
COLDREADER · FORGE/STATUS.md (installed, 24406 B) + FORGE/_archive/STATUS_ROTATION_2026-10-08.md (18677 B) + PROME/plans/2026-10-08_forge-status-rotation-PLAN.md (22107 B) · 57 claims
SCORE: 42/57 ✅ · 12 ⚠️ · 3 ❌
INVARIANTS: 12 PRESENT · 0 PART-MISSING · 0 MISSING · 1 CONTRADICTED (12, the evidence clause; its mechanics are PRESENT)
❌ 21 Plan: the "USO $159C" mapping's evidence is kept on L94. Wrong object. PLAN:68 says "the USO $159C name is kept on L94", and PLAN:89 says "(QQQ $730P Sep-30 · USO $159C Sep-30) … their evidence is an italic/blockquote line (USO)". But STATUS:94 (Robinhood) reads "USO $159C Sep-11 (bought 9/10, expired $0 — D-58)", while position_management.tsv:16 reads "Fidelity USO $159C 2026-09-30 … SOLD TO CLOSE by Will ×2 @ $0.01 (net $1.87; realized −$919.46…)". These are different contracts. The Sep-30 evidence lives only in _archive/STATUS_ROTATION_2026-10-01.md:36. The fix for read-1 I12 kept the very false match that read 1 had warned about.
❌ 22 Plan: QQQ $730P is "noted on D-70" (PLAN:68) and "D-70 carries the re-point for the next ANVIL pass" (PLAN:89). But STATUS:120 (D-70) is byte-identical to source L129. It names neither mapping and says "ANVIL edits no TSV or card". The re-point obligation exists only in the plan.
❌ 25 Plan chunk map I: "two rows (L135–136): D-71 (= WQ-347 …) · D-70 / D-74 …" (PLAN:19). But STATUS:135 is "🔴 **QQQ Oct-09 750C ×1 — NEW, no card**…" and STATUS:136 is "🔴 **USO Oct-09 150C ×1**…". The two rows actually sit at STATUS:138–139. This is a mis-aimed line pointer, the same class as read-1 #20/#26.
POINTERS: 72/73 resolve; mis-aimed: PLAN:19 "L135–136" (→ L138–139). A further pointer resolves to the wrong object: PLAN:68/89 cite L94 as the USO $159C Sep-30 evidence.
ONE-LINE VERDICT: yes for the installed files, no for the plan's mapping claims. A cold reader would act correctly from STATUS.md + the archive: every chunk is verbatim, every parser output matches except the VLO note, and every obligation has a carrier. The plan's invariant-12 statements about mapping evidence are wrong (wrong contract; a D-70 note that does not exist), and its sweep tool cannot detect a parse_money change. All 3 ❌ are basis/pointer class. None is action-class on the hot file.
```

Conventions: SRC = `git show ef2bc83f1:FORGE/STATUS.md` (183 lines, 32523 B). HOT = installed `FORGE/STATUS.md` (145 lines). ARCH = installed archive (94 lines). PLAN = the plan (90 lines). S = scratchpad `forge-rot/`. Rows are VERIFIED at the artifact unless marked INFERRED. All Python ran from stdin.
**Writes disclosed:** (a) at the start, a temp copy of SRC was written to `scratchpad/src_ef2.md` (outside `forge-rot/`, not in the repo). It was trashed at 19:18. (b) An in-memory `exec_module` of positions_from_forge refreshed the gitignored `AGENTS/TERRY/scripts/__pycache__/positions_from_forge.cpython-312.pyc` (19:09:49). No tracked or untracked repository file was created or changed; `git status --short` is unchanged (4 entries). This ledger is the only intended write.

## ❌ (3) — five-field
| # | Claim | Artifact:line | Command | Observed | Proposed change |
|---|---|---|---|---|---|
| 21 | "the USO $159C name is kept on L94" serves as the evidence line for the Fidelity USO $159C Sep-30 mapping; residue: "their evidence is an italic/blockquote line (USO)" | PLAN:68, PLAN:89 vs HOT:94, TSV:16 | `grep -n -o '.{80}159C.{80}' FORGE/STATUS.md`; `sed -n 16p FORGE/position_management.tsv \| tr '\t' '\n'`; `grep -n 159C FORGE/_archive/STATUS_ROTATION_2026-10-01.md` | HOT:94 "USO $159C Sep-11 (bought 9/10, expired $0 — D-58)" is a Robinhood contract. TSV:16 is "Fidelity / USO / $159C / 2026-09-30 … SOLD TO CLOSE by Will ×2 @ $0.01 … ROLLED into USO Oct-09 150C". Its only evidence is 10/01 ARCH:36 ("USO $159C Sep-30 ×2 −$919.46, both SOLD"). Neither SRC nor HOT has a Sep-30 USO $159C line. This is the same situation as QQQ $730P (pre-existing, not lost by this rotation), but the plan certifies it as carried. | Plan: say "both terminal mappings (QQQ $730P, USO $159C Sep-30) have NO evidence line in this file; L94's USO $159C is the RH Sep-11 contract". Drop "kept on L94" as evidence. |
| 22 | QQQ $730P "noted on D-70, re-point at the next ANVIL pass"; "D-70 carries the re-point" | PLAN:68, PLAN:89 vs HOT:120 | `cmp <(git show ef2bc83f1:FORGE/STATUS.md \| sed -n 129p) <(sed -n 120p FORGE/STATUS.md)` → identical; `grep -c 730P FORGE/STATUS.md` → 0 | D-70 = "**Management mappings / cards follow-through** … Any byte change here invalidates mappings pinned to the old `source_sha256` until re-review … ANVIL edits no TSV or card". It names neither mapping and assigns ANVIL no TSV work. Nothing in HOT tells the next ANVIL pass about the re-point. | Put the two mapping identities on D-70 (or a DOCKET row), or have the plan say the re-point is carried only here. |
| 25 | Chunk I survives as "two rows (L135–136)" | PLAN:19 vs HOT:135–139 | `sed -n 134,139p FORGE/STATUS.md` | L135 = 750C 🔴 row; L136 = USO 150C 🔴 row; D-71 = L138, D-70/D-74 + carried(18) = L139 | L135–136 → L138–139 |

## ⚠️ (12) — five-field
| # | Claim | Artifact:line | Command | Observed | What a stranger needs |
|---|---|---|---|---|---|
| 2 | Invariant 1 verification: sweep reports "parse_money() output identical" | PLAN:57; S/sweep.py:33–37 | `grep -n "def parse_money" PROME/tools/will_brief.py` → `def parse_money():` (no params) | `wb.parse_money(old)` raises TypeError, so the except branch sets `pm_old=wb.parse_money(); pm_new=pm_old`. The check compares the installed file to itself and **cannot fail**. The substance still holds: replicating the regexes gives ('34,650.69', ('11,421.19','32.96'), '2026-10-08', '2026-10-08') for both SRC and HOT. | Mark the sweep's parse_money leg as tautological, and keep the independent regex replication as the receipt. |
| 3 | "pending_receipts.py output identical"; "its FORGE closure candidates keep STNG by name" | PLAN:57, PLAN:82 (I1 fix) | ran `pending_receipts.py` (rc 0, == baseline). Replicated the CLOSED_RE × TICKERS scan on SRC vs HOT | The output is identical only because BRENT TRADE.md has no pending row, so FORGE is never read. The candidate set moved: SRC:146 (D-17 row, "Recalled / **closed** pre-7/30") → HOT:122 (summary row), which matches only through the negation "None **closed**, re-dated or re-owned". If triggered, it would print the whole 18-ID summary row as an STNG "closure CANDIDATE". | Say the FORGE leg is untested (vacuous), and that STNG's candidate now rides on the word "closed" in a negation. |
| 9 | VLO note: "…nothing of it is restated here." followed by "The gate reads the crack and the text, not the share's mark." | HOT:28 | read vs GATES.tsv:21 cell 4 | The gloss is accurate (A = ULSD crack settlement; B1 = signed text). It still characterizes the condition cell straight after saying nothing is restated, and "the crack" is undefined in HOT. | Either drop the gloss or say "(see the letter)". |
| 11 | Every WQ identifier in SRC appears in HOT (spawner test A) | SRC:28 vs HOT | python scan `(D-\d+\|WQ-\d+\|L\d{3})` + GATE/MGMT/sha scan | Only WQ-330 is absent (it was in SRC:28's VLO note, "REGISTERED 9/28 18:36 ET (WQ-330, Will "both")"). It survives in chunk H and in the GATES:21 `registered` cell. Invariant 7's chunk list (C, D1, D2, E, I) excludes H, so the drop is undeclared. "C5" (chunk C) is also absent, and "DOCKET L605" is reduced to "L605" (HOT:136). | Declare WQ-330 as reachable via GATES. |
| 16 | "Pass notes 9/27 → 10/8 → rotation 10/08 chunk G" (read-1 #87 claimed fixed) | HOT:145; PLAN:82 | `sed -n 145p`; read ARCH chunk G | The text is byte-for-byte what read 1 flagged at CAND:145. Chunk G holds the 10/8 note plus pointers to 10/01 chunk F (9/27–10/1) and `git show e8fd99acf` (10/7), a two-hop chain. The fix landed only in PLAN:17's prose. | "10/8 note → 10/08 chunk G; 9/27–10/1 → 10/01 chunk F; 10/7 → e8fd99acf". |
| 28 | Residue: "40 'exercise unfundable' appears in this plan's audit table" (declared, not fixed) | PLAN:83 vs PLAN:35 | `grep -n -i unfund PLAN` → only L83 | The phrase is no longer in the audit table (L35 = "Fri 15:00 ET hard stop (WQ-366 DECLINE, L605)"). The declaration is stale: the item was in fact fixed. This is a self-describing claim, so ⚠️ only. | Move #40 to "fixed". |
| 29 | Audit: the 750C obligation is carried by "the EXPIRING italic (TERRY woken tonight, terry-1008pm, to card it)" | PLAN:34 vs HOT:112 | read HOT:112 | The italic says only "QQQ $750C ×1 (NEW, no card)". The TERRY wake is a plan annotation that a reader would expect to find in the italic. (Note: an untracked `AGENTS/TERRY/setups/QQQ750C_oct09-sell-or-roll_2026-10-08.md` exists. "no card" is true of committed state and carried verbatim from the reconcile, so it is not a rotation defect.) | Mark it as a plan annotation. |
| 30 | Audit: WQ-386/VLO-SCALE owners "TERRY grades · Will executes · PROME integrates", carried by the owner-decides italic | PLAN:44 vs HOT:124, ARCH:69 | read | HOT:124 has "WQ-386 / VLO-SCALE: TERRY grades, Will executes". Chunk E's "PROME integrates" is carried nowhere in HOT, and the GATES:21 owner cell does not name PROME. Counterexample CE1 hit (minor). | Add "PROME integrates", or drop it from the audit row. |
| 31 | Owner-decides italic is readable as four items with owners | HOT:124 | read | "·" is used both between items and inside D-47's owner list ("… time stop 12/4: Will harvests · REGINALD grades · TERRY proposes · WQ-386 / VLO-SCALE: TERRY grades, Will executes · WQ-200 — …"), so the item boundaries are ambiguous. | Use ";" between items. |
| 33 | Summary row: "Ticker-bearing items, for the text scan: STNG (D-17) · … · AAPL … (D-1) · D-75" | HOT:122 vs ARCH:44–60 | read D2 rows | "the text scan" is undefined (it means pending_receipts' closure scan). The list reads as exhaustive but omits D-55 (VLO, which IS in pending_receipts' TICKERS), D-61 (QQQ 730P, TLT 77P) and D-65 (707/708 strikes). | "e.g." or a complete list; name the scan. |
| 34 | Immediate Actions D-71 row: "the same Activity scrolled to 10/1 (the roll's exit fill; = WQ-347)" | HOT:138 vs ARCH:91 (chunk I) | read | SRC:174 bundled "D-71 / D-69 / D-66 — the same Activity scrolled to 9/30–10/1 + order detail". D-69's ask ("Activity 9/30→10/1 (below the cut)", ARCH:45) and D-66 now sit only in the summary row with owner "Will". The cue that one scroll to 9/30 also closes D-69 is lost from HOT. The obligation is still carried (owner named), so ⚠️ only. | "scrolled to 9/30–10/1 (also D-69)". |
| 44 | Install step 6 commits "`PROME/DOCKET.tsv` (L646)" | PLAN:77 | `git log -2 --format='%h %ci %s' -- PROME/DOCKET.tsv` | L646 was already committed in 88ab4a45d (19:09:33, "L646 registered"), and that committed row cites `FORGE/_archive/STATUS_ROTATION_2026-10-08.md` and the plan, both still UNTRACKED. On origin, those are dead pointers until the rotation commit lands. | Drop DOCKET.tsv from step 6. Land the rotation commit before the next push, or note the order. |

## A. Invariant table
| Inv | State | Evidence (command → observed) |
|---|---|---|
| 1 | PRESENT (instrument ⚠️ 2, 3) | in-memory `extract(SRC)` vs `extract(HOT)` (asof 2026-10-08): only `live[3].note` (VLO) differs; warnings/withheld identical. CLI `--json --asof 2026-10-08` rc 0, diff vs S/baseline_positions.json = VLO note only. `--selftest` → "SELFTEST: PASS", RC=0 (read bare). `desk_attention.holdings()` on SRC (fake root) vs HOT: 22/22 rows, errors [] both, only VLO `note` differs, line numbers identical. parse_money regexes identical tuple. pending_receipts rc 0, `diff` vs baseline → identical (vacuous, ⚠️3) |
| 2 | PRESENT | python over table lines in `## Fidelity*` / `## Robinhood` / `## Account*`: 36/36 rows, one differs (SRC:28/HOT:28 VLO); cells 1–7 equal `[' VLO ',' Stock ',' 1 ',' $412.00 ',' $445.995 ',' $445.99 ',' +$33.99 / +8.25% ']`. Only other region line changed: L94 (blockquote, not a row) |
| 3 | PRESENT | difflib SRC:9 vs HOT:9 → one pure insertion of "`_archive/STATUS_ROTATION_2026-10-08.md`, "; the four shapes `**Updated:** 2026-10-08` · `marks = 2026-10-08` · `account total:** $34,650.69` · `money market):** $11,421.19 (32.96%)` each present once |
| 4 | PRESENT | python: each ARCH `## Chunk X` body == SRC lines a–b (10/10 True), == S/chunk_X.txt (10/10), header bytes+crc == recomputed (10/10). `measure.py S/chunk_*.txt` → A 1084·3510813514 · B 842·2632567345 · C 2926·2591328773 · D1 523·2218341014 · D2 4007·487926030 · E 1664·2660099432 · F 936·2479073510 · G 1772·89507236 · H 1172·2811584083 · I 521·365315039, all = ARCH:6–15 |
| 5 | PRESENT | `cmp <(SRC 117p) <(HOT 118p)` → identical |
| 6 | PRESENT (⚠️ 9) | HOT:28 names `GATE-TERRY-VLO-HELD-01`, "the letter (condition AND consequence cells, incl. who acts on each leg) is read at `PROME/GATES.tsv`, as amended by WQ-386", points to "rotation 10/08 chunk H". VLO-SCALE: "TERMINAL on the 9/25 F1 fire (TERRY 4ad672c43; its optional CME source-① override remains as written there)" = GATES:19 state cell. Quote “Yes, still one share” has no inner punctuation. No level, operator, leg or actor of HELD-01 appears in HOT:28 |
| 7 | PRESENT | Python ID scan: every D-/WQ- ID of chunks C, D1, D2, E, I is in HOT (WQ-347 ×2, at L112/L138); the only absent SRC ID is WQ-330 (chunk H, ⚠️11). EXPIRING lines each have a position row (L44–48, L62, L85) and an Immediate-Actions row (L134–137); chunk I is cited at L139; D-47's facts are at HOT:98; WQ-386 is at GATES:21 cell 4 |
| 8 | PRESENT | HOT:126 has D-72 −$886.90 / −$1,302.97 "(derived; per-row contract counts NOT shown)", D-73 "$15,524.70 → $12,993.82 → $11,421.19", −$1,572.64 → −$1,572.63 (D-75). HOT:50 "(D-72 → § Reconcile discrepancies, CLOSED this pass)" lands on HOT:126 under HOT:108 |
| 9 | PRESENT | `[10/8 rcv]` on every Fidelity note / L21 / L68 italic; `[9/29 13:4x intraday]` at HOT:9, 94; "marks are NOT closes" at HOT:5 |
| 10 | PRESENT (⚠️ 16) | python: SRC:183 prefix through "New consumers: add yourself here in the same commit that starts parsing." == HOT:145 prefix (1001 chars). The conventions sentence is verbatim. The pass note's claims (only VLO note among position rows; three `###` → italics; 18 rows → one; four header shapes byte-identical, one appended pointer) each verified |
| 11 | PRESENT | `measure.py FORGE/STATUS.md` → 24406 B, 145 lines, crc32 2187489639. int(0.75×32550)=24412 → 6 B under; 22785 → 1621 B over (declared at PLAN:86). DOCKET L646 exists (2026-10-15, committed 88ab4a45d). `scripts/read_cap_check.py FORGE/STATUS.md` → "✅ … 24,406 B 75% of budget", RC=0 (note: the display rounds 74.98% up to "75%") |
| 12 | CONTRADICTED (clause) | Mechanics PRESENT: `sha256sum FORGE/STATUS.md` = 964ffd1f…2272. Python over TSV HEAD vs working: exactly 10 rows changed (L6, 8–13, 15, 16, 22), and only `source_sha256` changed (old = sha of SRC 18075a84…; `checked` was already 2026-10-08, so the re-pin of `checked` was a no-op). No other row changed, none is VLO, no CR, final newline present. `desk_attention.coverage()` → errors [] (no "Management evidence changed/missing"). Eight evidence lines are byte-identical (HOT:58, 62, 68, 74, 78, 85, 98 = SRC). Evidence clause CONTRADICTED: ❌21 (USO $159C is the wrong contract), ❌22 (D-70 carries no note) |
| 13 | PRESENT | `git log -1 --format=%h -- FORGE/STATUS.md` → ef2bc83f1 = ARCH:3; `git show --stat a1eb75287` → only `FORGE/position_management.tsv`; `git log ef2bc83f1..HEAD -- FORGE/STATUS.md` → 0 commits; receipts = measure.py over the chunk files |

## B. Read-1 fixes — did each land at the installed artifact?
| Read-1 item | Claimed fix (PLAN:81–82) | Result |
|---|---|---|
| ❌ I6 | VLO note pointer-only | landed (HOT:28; ⚠️9 gloss residue) |
| ❌ I7 | WQ-347 on EXPIRING italic + D-71 row | landed (HOT:112; HOT:138 "= WQ-347"; WILL_QUEUE.md:35 confirms WQ-347 is the D-71 10/1 scroll) |
| ❌ 69 | `git status --short -- FORGE/` | landed (PLAN:72). Observed exactly ` M FORGE/STATUS.md`, ` M FORGE/position_management.tsv`, `?? FORGE/_archive/STATUS_ROTATION_2026-10-08.md` |
| ❌ 77 | pass-note L9 wording | landed (HOT:145 "the four parsed header shapes are byte-identical, that line carrying one appended rotation pointer") |
| ❌ 5 | net-growth wording | landed (PLAN:5) |
| ❌ 20 | L92 → L94 | landed (PLAN:11, 51) |
| ❌ 26 | L143 → L145 | landed (PLAN:17, 52, 66) |
| ❌ 44 | 14 + D-28 + 2 + D-75 = 18 | landed (PLAN:39–42; HOT:122 owner cell: 14 Will · D-28 RH history · PROME D-62 · D-65 · D-75) |
| ❌ 72 | 2,461 B | landed (`sed -n 44,48p FORGE/STATUS.md \| wc -c` → 2461) |
| ⚠️ 2 | build.py reads git show | landed (S/build.py:4) |
| ⚠️ 8 | NEXUS wording | landed (AGENTS/NEXUS/STATUS.md:12 "positions → `FORGE/STATUS.md`") |
| ⚠️ 23/55/86 | owners in owner column; D-28 RH history | landed (HOT:122). "re-enters when it moves" → "Returns to this table when its state changes" (still a rule in the conjecture column; tolerable) |
| ⚠️ 34 | L36/L104 trims withdrawn | landed (no diff hunk at 36/104) |
| ⚠️ 45/48 | D-47 / APD owners on italic | landed (HOT:124) |
| ⚠️ 80–85 | vanish with pointer-only note; "every gate" | landed ("canonical for every gate here", HOT:124; "(rule 7)" gone from L28; CME override named) |
| ⚠️ 87 | pass-note hop | **not landed in HOT** (⚠️16; prose only at PLAN:17) |
| ⚠️ 89 | a1eb75287 wording | landed (ARCH:3 "changed only `FORGE/position_management.tsv`") |
| ⚠️ 88 | chunk I pointer | landed (HOT:139) |
| ⚠️ I1 | STNG named on summary row | landed differently (candidate survives only through "None closed"; the vacuity is not stated, ⚠️3) |
| ⚠️ I8 | D-73 figures restored | landed (HOT:126) |
| ⚠️ I12 | USO $159C name kept on L94; QQQ $730P noted | **landed wrong**: the kept name is a different contract (❌21); the "noted on D-70" note is absent (❌22) |
| ⚠️ 74 | DOCKET row | landed (L646, 88ab4a45d; ⚠️44 sequencing) |
| ⚠️ 78 | "re-pinned in the installing commit" | landed (wording; the TSV is re-pinned in the working tree, commit pending) |
| declared 40 / 76 / <70% | not fixed | 40: declaration stale (⚠️28) · 76: not re-tested (UNKNOWN) · <70%: declared truthfully (1621 B over) |

## C. Counterexamples aimed at the fix round (7 devised; 5 hits)
- **CE1 owner on a pointer line ≠ archived owner.** Compared HOT:122 owner cell with D1/D2 Decision-owner cells (18/18 match), HOT:124 with chunk E, and HOT:139 with chunk I. **Minor HIT:** "PROME integrates" was dropped (⚠️30).
- **CE2 figure on a pointer line ≠ chunk.** Token scan ($, m/d, ×n, 9-hex, n/n, (n)) over HOT lines 5, 15, 28, 94, 112, 122, 124, 126, 138, 139, 145: every token exists in SRC. The only new tokens are the "10/08" chunk labels and "(18)". Spot-checked associations (Fri 10/16 = TLT/HBAN Oct-16; 12/4 time stop; D-73 chain). **Negative.**
- **CE3 pointer names a chunk tag that does not exist.** 13 "rotation 10/0x chunk X" pointers checked against ARCH and 10/01 headings (A–I incl. D1/D2; A–F): **negative**, all resolve.
- **CE4 consumer change hidden by the sweep's ignore-list or logic.** positions/holdings: **negative** (independent in-memory runs show nothing hidden, not even line numbers). parse_money: **HIT**, the sweep leg is tautological (⚠️2). pending_receipts: **HIT**, the FORGE leg is never executed and the STNG candidate silently moved to a negation match (⚠️3).
- **CE5 same name, different object (aimed at fix I12).** **HIT ❌21**: RH USO $159C Sep-11 ≠ Fidelity USO $159C Sep-30.
- **CE6 re-aimed line pointers after the fix round shifted lines (class of #20/#26).** Checked 23 PLAN line pointers against HOT/SRC. **HIT ❌25** (L135–136).
- **CE7 carriage claimed on a row the rotation did not edit.** **HIT ❌22**: D-70 is byte-identical to SRC:129.

## D. What a stranger would misread in the pointer lines / summary row
HOT:122 "for the text scan" (undefined, non-exhaustive, ⚠️33) · HOT:124 "·" overloading (⚠️31) · HOT:138 narrowed scroll date (⚠️34) · HOT:145 one-hop reading of a two-hop chain (⚠️16) · HOT:28 gloss after "nothing restated" (⚠️9). Notes only, not graded: ARCH:69 (chunk E, verbatim) says "exact rule/ref retained in Longs", but Longs now holds a pointer; `read_cap_check` prints "75% of budget ✅" for 74.98%.

## ✅ (42), compact: claim → artifact → command → observed
1 I1 substance → see A1 · 4 I2 · 5 I3 · 6 I4 · 7 I5 · 8 I6 · 10 I7 · 12 I8 · 13 L50 xref · 14 I9 · 15 I10 · 17 I11 · 24 I13 → table A.
18 DOCKET L646 → `PROME/DOCKET.tsv` line 646 → python → "2026-10-15 ⇥ 🟡 `FORGE/STATUS.md` WRITE MODE …".
19 re-pin mechanics · 20 eight evidence lines byte-identical · 23 coverage() errors [] → table A row 12.
26 PLAN chunk-map line pointers L5/L94/L112/L118/L122/L124/L126/L145/L28/L50 → `sed -n` → each lands on the stated content.
27 PLAN audit line pointers L44/L45/L46/L47–48/L62/L85, source L66–67 → `sed -n` → correct rows.
32 HOT:122 → 18 IDs = D1 (1) + D2 (17), same order; owners equal the recorded cells (D-1 "Will / an older window" under Will).
35 HOT:112 WQ-347 → D-71 → `grep -n "^| 347 |" PROME/WILL_QUEUE.md` → "THE 10/1 ROLL'S EXIT FILLS ARE STILL UNBOOKED (D-71)".
36 HOT:112 dates → Fri 10/09 · Thu 10/15 · Fri 10/16 (2026-10-08 = Thu per `date`) → correct; lines match HOT:44–48/62/85.
37 HOT:5 → $21,945.52 + $11,421.19 + $1,283.98 = $34,650.69; 19/19; 1 NEW · 0 GONE · 2 QTY · 16 MARK = ARCH:19.
38 HOT:94 → $295.15 / BP $8.94 `[9/29 13:4x intraday]`, $290.15, $5.00 D-64, D-57/D-58 = ARCH:23.
39 HOT:15 → `head -c 1200 HEARTBEAT.md` → "TWENTY-EIGHTH re-base".
40 ARCH:3 working file byte-identical at rotation start → INFERRED (read 1 verified `git diff --quiet` rc 0; no later commit to the path).
41 ARCH:3 / PLAN:5 32,523 B = 100% → SRC bytes 32523; 32523/32550 = 99.92%.
42 ARCH:5 separator rule → python split: exactly one blank line between chunks, not counted; the file ends with a single newline.
43 PLAN:72 step-1 expectation → `git status --short -- FORGE/` → exactly the 3 entries.
45 PLAN:80 read-1 counts (89/56/24/9; 8/3/0/2; 7 CEs) → S/reads/plan_read_1.md header + totals → equal.
46 PLAN:21 145 / 94 lines → measure.py → 145 / 94.
47 candidate/archive = installed → `cmp S/STATUS_candidate.md FORGE/STATUS.md`; `cmp S/STATUS_ROTATION_2026-10-08.md FORGE/_archive/…` → identical; build.py == build_final.py.
48 build.py:4 `git show ef2bc83f1:` → read → present. 49 NEXUS → NEXUS STATUS.md:12.
50 HOT:139 chunk I pointer + "(18)" → ARCH:91–94 four rows; 18 = summary IDs.
51 13/13 chunk pointers resolve (CE3). 52 L9 rotation files 10-08 · 10-01 · 09-29 · 09-27 · 09-20 · 09-10 · RECONCILE_2026-08-29_RECORD → `ls FORGE/_archive/` → all exist.
53 file pointers (PROME/proposals/2026-10-07_VLO-december-management-RULED.md "RULED APPROVED October 7"; PROME/data/2026-10-08_broker-capture-TRANSCRIPTION.md; JOURNAL; PORTFOLIO; DASHBOARD; READS.tsv:238 WALTER scoped; scripts/read_cap_check.py; USER.md; HEARTBEAT.md) → `ls` → resolve.
54 VLO-SCALE sentence → GATES.tsv:19 cell 6 "RESOLVED(TERMINAL — F1 FIRED for 2026-09-25 … 4ad672c43 … Source-① override is Will's hand, optional" → consistent.
55 Will quote verbatim → HOT:28 “Yes, still one share” (period outside the bold) vs SRC:28 → no added inner punctuation.
56 sweep ignore-list hides nothing for positions/holdings (CE4 negative half).
57 PLAN:5 precedent → `FORGE/_archive/STATUS_ROTATION_2026-10-01.md` chunks A–F exist; SCRATCH instruction not re-tested (read 1 verified).

## Totals
57 claims · 42 ✅ · 12 ⚠️ · 3 ❌ (all basis/pointer class: 21 wrong-object evidence, 22 absent carrier note, 25 mis-aimed line pointer; none is action-class on HOT/ARCH). Invariants 12 PRESENT / 1 CONTRADICTED (12, clause). Counterexamples: 7 devised, 5 hits (CE1 minor, CE4 ×2 legs, CE5, CE6, CE7), 2 negative (CE2, CE3).
Reads: this is result read 2 of the episode (plan read 1 + this). Read 1 had action-class ❌ (I6, I7, 69, 77); this read has none.
