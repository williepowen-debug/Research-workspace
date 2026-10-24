# SWEEP C — NEXUS live boards + record directories (read-only)

Reviewer: read-only subagent, 2026-10-24 Sat afternoon ET. Repo HEAD on NEXUS = e1758b4fb (2026-10-24 15:20:12 -0400), tree clean.
Scope: STATUS.md, CONFIRMED.md, STATUS_COLD.md (headers + tail), LAST_COMPLETION.md, board_log.tsv, registry/, directory hygiene, BRIEFING_2026-08-29. Charter and templates out of scope.

**Counts: ❌ 6 · ⚠️ 17 · ✅ 14**

## ❌ BROKEN / WRONG

| # | path:line | quote | problem | fix |
|---|---|---|---|---|
| ❌1 | CONFIRMED.md:4 | "**Full C-ID index** … `recon/2026-06-06_c_id_index.md`" | The file exists, but it is a 6/6 snapshot and its IDs **collide** with this table: index line 40 = "C-35 Fertilizer Supply Collapse → Food CPI", line 41 = "C-36 Hotel California Employment Trap". CONFIRMED's C-35 (Iran bull-trap, promoted 6/8) and C-36 (real-duration channel, 7/31) are different claims. "Full" is false and a reader following the pointer gets the wrong meaning for the two live rows. It also still carries an open 6/6 backlog item ("Promote C-34", lines 39/51/67) 140 days on, while the merge table at :26 still names C-34 as a merge target with no row. | Re-label the pointer "6/6 snapshot; C-35/C-36 IDs since re-used — see rows here", or archive the index and fold the C-34/C-10/C-07 merge-target lines into the Merged table. |
| ❌2 | CONFIRMED.md:18 | "the stale half is struck above and the resolution is below" | The file has **zero** `~~` strikethroughs (grep count 0). The superseded "BOND adjudicates…" text is not struck; the claim of a repair is false. | Strike the stale sentence or drop "struck above". |
| ❌3 | STATUS.md:106 (and §H23C source row) | "HHDC Q3 ~mid-Nov (PRED-41, DOCKET L575)" in the **11/20–11/24** row | DOCKET L575 is dated **2026-11-06** ("placeholder inside 'early November'"); PREDICTIONS_MONITOR.md:13 says "~early Nov". STATUS files the wake two weeks late, under the wrong row. | Move PRED-41 / L575 to the 10/31–11/10 row as "~early Nov (L575 placeholder 11/06; re-dated at the NY Fed announcement)". |
| ❌4 | STATUS.md:25 | "M-10 … 25% … Sept TIC ~mid-Nov; **no letter**" | Disc-J: a Conf % carried across ≥2 passes needs a registered falsifier; M-10 has held 25% since 10/20 with L11/PRED-30 closed and nothing that would force a move. Per the charter the number is "a mood, not an estimate" and the file must say so. | Either register an M-10 letter on Sept TIC (with date, both edges, NO-VERDICT band) or mark the cell "judgment, no number" like M-06. |
| ❌5 | LAST_COMPLETION.md:11 | "via `STATUS_COLD.md` §H23–§H23E (7d9190d3 · 55ccb9c8 · b3991b55 · c7c7dab4 · 75c40b26 · c1444386)" | Six crc32s, but `c1444386` is **§H23F** (the L13/L16 header paragraphs). The range label omits the block. (Also there is no §H23A heading — §H23 then §H23B.) | "§H23–§H23F". |
| ❌6 | CONFIRMED.md:18 (8/10 paragraph) | "**Successors, both frozen:** T6 … *not triggered*; hard close 8/29 … HEN-42 still resolves 8/29" | Forward legs parked inside a confirmed row (the C-05 defect) and now past-dated. T6 was **GRADED NO-VERDICT 2026-08-30** (STATUS_COLD.md:240/346/651) and that result never reached this row; T7 has no outcome here. The trophy case still reads as if they are pending. | Add a one-line resolution: "T6 ⚪ NO-VERDICT 8/30 (STATUS_COLD §…); T7 → …", or move the successor text out to PREDICTIONS_COLD. |

## ⚠️ STALE / OWED / INCOMPLETE

| # | path:line | quote | problem | fix |
|---|---|---|---|---|
| ⚠️1 | STATUS.md:9 | "Nearest refuter KRE $72.74." | The source (AGENTS/TERRY/STATUS.md:5; VIEW.md:67) says "KRE **reclaims** $72.74 (10/23 close $72.46)", 0.4% away. STATUS drops the direction and the distance. Under the anti-laundering rule the direction of a conditional must survive. | "Nearest refuter: KRE closes above $72.74 (the 9/16 gap-down close); $72.46 [10/23] = 0.4% below (TERRY)". |
| ⚠️2 | STATUS.md:24 | "DOWN dead" | No reason given on the board. The basis is the 10/15 commit ("069 kills M-09 DOWN"), but DOCKET L573 still lists the DOWN branch ("`GATE-LIQ-069` review RELEASED ⇒ −4") and the STATUS docket (:104) still schedules a "LIQ-069/076 review" for 10/30. A reader can't tell why the branch is dead or whether the 10/30 review could bring it back. | "DOWN dead (LIQ-069 review 10/15 ruled out RELEASE — ref)", then packet PROME to annotate L573. |
| ⚠️3 | STATUS.md:3, :100; LAST_COMPLETION.md:4,10,22,28,51; PREDICTIONS_MONITOR.md:18 | "10/24 15:1x ET", "FRED 15:0x", "registered by PROME 22:1x" | Typed-clock `HH:Mx` stamps on the header and other records other desks grade from. The charter's stamp rule (A8) bans this form there. 3 on STATUS, 7 on LC, 1 on PREDICTIONS. | Take the stamp from `date`/`git log` (`e1758b4fb` = 15:20:12) at the next touch. When quoting PROME's own `22:1x`, label it as a quote. |
| ⚠️4 | PROME/DOCKET.tsv L631 (NEXUS's mirror) | "M-01 · M-03 · **M-04** · M-05 · M-07 falsifier windows END … M-04 carries the ~3pp-high flag" | Not annotated since registration. M-04's 10/8 letter FIRED 10/19 and its successor M-04b grades at L632. The ~3pp-high caveat was cleared 10/20 (board_log row SIG-W-20261019-020). STATUS:105 is already right ("M-01 · M-03 · M-05 · M-07"), so PROME's mirror and NEXUS disagree. | Packet PROME: annotate L631 "M-04 discharged (fired 10/19; M-04b at L632); 3pp flag cleared 10/20". Do not edit. |
| ⚠️5 | PROME/DOCKET.tsv L752 · L753 · L754 | "PENDING — PROVISIONAL anchor not yet qualified … confirm/re-date once actual anchor and count are known" | The anchor QUALIFIED 10/19 (graded 10/23 01:03; L751 is annotated to that effect). These three rows still say provisional. The dates (11/09 · 11/10 · 11/24) still fit a 10/19 anchor, but the confirm step the rows ask for was never packeted. | Packet PROME: "anchor qualified 10/19, L 329 · C₀ 1,310; L752/753/754 dates confirmed". |
| ⚠️6 | PROME/DOCKET.tsv L40 | "2026-10-12 Amendment-12 watch grades … DAEDALUS/NEXUS … PENDING" | 12 days overdue. NEXUS is co-owner and the row is on no NEXUS board. The question looks answerable now: the charter says amendment 12 shipped (cap 12 of 12), so per the row's own test "a twelfth … amendment has appeared". | Note it on the STATUS docket or packet DAEDALUS/PROME with whether amendment 12 is a format amendment (which decides the row). |
| ⚠️7 | LAST_COMPLETION.md:4 | "**CLOSED OUT 2026-10-24T12:32:41-04:00** … Owed next: …" | This sits **above** the later 15:19 block, so it reads as the current state. The 15:19 session, committed at e1758b4fb, has no close line of its own. | Move the line under its own block, or add a 15:20 receipt line on top. |
| ⚠️8 | CONFIRMED.md:17 (C-35) | "PortWatch target rows are UNKNOWN at the owner and no new date is set ⇒ C-35 is UNGRADEABLE … and stays that way" | The note dates from 9/17. Forward instrument state with no resolver and no expiry, 47 days on, inside a confirmed row (RECORD 10/23:48 "unchanged"). Fails BOOT 0b test (iii)/(i). | Mark it FINAL-UNGRADEABLE (pattern record frozen at 3/4) or register a dated re-check in PREDICTIONS with a resolver. |
| ⚠️9 | STATUS.md:62 | "T-11/T-12 · T-21/T-23 \| closed \| → §H23" | A closed state still sits in the live TENSIONS table, as a pointer row. The rotation moved the rows but kept a closed row. | Drop it. The header already points to §H23. |
| ⚠️10 | STATUS.md (whole) | 22,779 B = 70.0% | Only 6 B under the rule-5 STOP (22,785 B). The 10/23 RECORD says a full pass regrows about 10 KB, so Monday's L832 read will go past the trigger. LC:14 already owes "rotate STATUS first". | Rotate before writing on Monday (BOOT 0a). |
| ⚠️11 | board_log.tsv (67 rows, 2026-08-12 → 09-17) | e.g. "2026-09-02T21:4x-04:00" | Breaks the charter's 7/31 `YYYY-MM-DDTHH:MM-04:00` standard (5 more rows before 7/31 have no offset, which is grandfathered). Rows from 9/17 on are clean. | Leave as history. A header note that `x`-rows are approximate stops a parser from reading them as exact. |
| ⚠️12 | board_log.tsv rows 171–175 (10/19) | source `WALTER`; notes "Committed2d9238d29 INFO read/filed;HOMER…" | Source vocabulary drifts: the charter specifies `INBOX_WALTER` (114 rows use it). The notes column has glued words (root Output Canon: "never glue words together"). | Grandfather the rows. Use `INBOX_WALTER` from now on and write spaced text. |
| ⚠️13 | board_log.tsv rows 6, 52, 60, 107, 108 | row 6: `deferred` "Packet A, dedicated deliverable owed by 7/14"; 52/60 (9/02 FHA, Yen/JGB); 107/108 (9/29 FORUM-7, "before FINAL 10/1 / 10/2") | The last disposition for these 5 signal IDs is `deferred`, and no later row discharges them. The signal-lifecycle rule needs a dated resolver plus a STATUS docket row. All resolvers are long past: Packet A is in archive/2026-07-10_correlation-collapse-map_packetA.md, and FORUM-7 went FINAL 10/2 (CONFIRMED C-36 note). | Append 5 discharge rows (`noted`, with pointer). |
| ⚠️14 | AGENTS/NEXUS/outbox/, signals_archive/ | (no banner file) | The charter calls both "RETIRED 2026-09-29 — historical only", but neither directory carries a RETIRED marker. Only SIGNALS.md has its FROZEN banner. A stranger who lands in the directory can't tell it is retired. | Move both under archive/ (see the candidate list below), which retires them structurally. |
| ⚠️15 | BRIEFING_2026-08-29_SYSTEMS_REVIEW.md:1–3 | "# 🔴 READ THIS FIRST … **Status of the review itself: NOT STARTED.**" | Stale. DOCKET L206 says "LEG ① RESOLVED 2026-09-02" (slate = proposals/2026-09-02_self-audit-improvement-slate.md). It is a top-level file with a red read-first banner that is now false. Last commit 2026-08-28, so it becomes retirement-eligible **10/28** (>60 d). References: PROME/DOCKET.tsv L206 (a resolved ledger row), proposals/2026-09-02 slate, research/2026-10-01_pass_record.md, inbox/processed (2 files), DAEDALUS profiles (2). None is a live NEXUS analytical or protocol doc. | `git mv` to archive/ on/after 10/28. Its banner misleads before then, so a "SUPERSEDED — review delivered 9/02" note is worth adding either way. |
| ⚠️16 | inbox/processed + inbox/WALTER/processed | 81 of 259 files last committed before 2026-08-25 | Inside the retirement rule's age class. They are records (not boot-read). Most are referenced only from board_log/LC history. | Optional batch `git mv` to archive/inbox_processed_<range>/. Low priority. |
| ⚠️17 | LAST_COMPLETION.md:40 | "Delivery → `PROME/inbox/2026-10-23_from-NEXUS_full-pass-…`" | The file now lives at `PROME/inbox/processed/…` (consumed by PROME). That is fine as history, but the path no longer resolves. | None needed. Optionally append "(consumed → processed/)". |

## ✅ WORKING

| # | what was checked | result |
|---|---|---|
| ✅1 | crc32 recomputed over every §H21A–§H23F block body | 12/12 match the header values; all values quoted in LC:11/22/46 match. |
| ✅2 | Every §H pointer in STATUS (§H16 §H22A §H22B §H22C §H23 §H23B §H23C §H23D §H23E) | all 9 exist as headings in STATUS_COLD.md. |
| ✅3 | File pointers on STATUS/LC/CONFIRMED (research/2026-10-23_full_pass/{RECORD,DISC_J_POSTFIRE_LETTERS,COLDREAD_STATUS*}, research/2026-10-24_structure_pass/{RECORD,COLDREAD_PREDICTIONS_MONITOR}, analysis/WQ342_grading_log.tsv, archive/LAST_COMPLETION_COLD_* ×4, PROME proposals/inbox, ZHAO TIC report, recon c_id_index, FORGE/STATUS.md) | all resolve, except ⚠️17 (moved to processed). |
| ✅4 | FRED marks vs raw pulls in research/2026-10-23_full_pass/raw_*.csv | HY 340 · CCC 1,340 · B 346 · BB 210 · IG 89 · DGS10 5.13→4.96 · DFII10 2.76→2.64 (2.88 [10/13]) · T10YIE 2.32/2.34 [10/23] · VIX 19.03 all match. HY >320 ×7 (325,323,331,329,333,327,340) ✓; +13 d/d ✓; +24 since 10/13 (316) ✓; CCC +33 ✓; BB +12 ✓; L13 anchor-date HY 331 [10/16] ✓. |
| ✅5 | Threshold distances | L16 DOWN 21bp ✓ · L13 UP 20bp ✓ · M-07 4bp ✓ (LIQ-072 ">94" = 5bp to 94, 6 to fire under strict >) · M-01 10bp ✓ · M-09 10bp ✓ · M-05 $2.70 = 3.7% ✓, $8.44 ✓ · breakeven 6bp (from 8) ✓ · REKILL 80bp ✓. |
| ✅6 | Cell/date arithmetic | L13 cells 5–8 = obs 10/23·26·27·28, earliest fire read ~10/29 ✓; L16 cells 4–5 = obs 10/23·10/26, read Tue 10/27 ✓; docket publication days line up. |
| ✅7 | Catalyst docket | No row is in the past (earliest Mon 10/26); weekday claims clean (`claim_check --check weekday` ✓ on STATUS, LC, CONFIRMED, PREDICTIONS). |
| ✅8 | DOCKET rows NEXUS carries: L554 10/27 · L555 10/27 · L572 11/10 · L573 10/30 (annotated M-09-only) · L574 11/20 · L630 10/29 · L632 11/20 (+M-04b/M-08b rider) · L751 10/27 · L832 10/26 · L229 10/26 · L773 10/28 · L794 10/30–11/02 · L826 10/27 · L827 10/29 | All PENDING, with dates matching STATUS and LC NEXT. None is RESOLVED or re-dated differently. Exceptions: ⚠️4 (L631), ⚠️5 (L752–754), ❌3 (L575). |
| ✅9 | L639 (NEXUS-owned, dated 10/25) | Absent from STATUS, but packeted to PROME 10/24 as "RESOLVED → L730" (PROME/inbox/2026-10-24_…L639-note.md:19). Handled. |
| ✅10 | `read_cap_check.py --agent NEXUS` | rc 0; STATUS 70%, LC 50.5%, PREDICTIONS 59.1%. rotation_due=5 refers to other desks' STATUS (OSPREY 95%, LIQUID 88%, CORAL 87%, VULCAN 82%, REGINALD 79%), not NEXUS-owned. |
| ✅11 | `corrections_boot_check.py NEXUS` | 0 unreceipted NAMED; 11 receipts. COR-20261023-39 does not name NEXUS (WALTER register :122), so no receipt is owed, and board_log :202 says so. |
| ✅12 | registry/corrections_receipts.tsv | Well-formed: 4-column header, 11 rows, UTC `Z` stamps, actions in {APPLIED, NO-OP}, post-WQ-399 rows carry artifact/validation_ref/scope with `path#key`. The two 9/11 rows have an empty note (pre-WQ-399, grandfathered). |
| ✅13 | board_log.tsv structure | v0.2 header exact; all 207 rows have 5 columns; dispositions within the closed set; no timestamp issue since 9/17 (see ⚠️11–13). |
| ✅14 | SIGNALS.md banner | "FROZEN 2026-09-29 — not maintained; STATUS is canonical, do not cite rows as current" matches the root Data Hygiene form and the charter's claim. orphan_check clean. |

## Retirement candidates (root rule: >60 d AND not boot-read AND no live analytical/protocol reference; cutoff = last commit before 2026-08-25)

| path | last commit | referenced by (NEXUS *.md, CLAUDE.md, DOCKET, GATES) | verdict |
|---|---|---|---|
| signals_archive/SIGNALS_THROUGH_PASS11.md | 2026-04-04 | none | ELIGIBLE |
| signals_archive/SIGNALS_PRE_MAY21_RESET_20260521.md | 2026-05-21 | none | ELIGIBLE |
| signals_archive/SIGNALS_E_PHASE_RESOLVED_20260606.md | 2026-06-06 | SIGNALS.md (FROZEN, not live) | ELIGIBLE |
| signals_archive/SIGNALS_REANCHOR_RESOLVED_20260627.md | 2026-06-27 | none | ELIGIBLE |
| signals_archive/S-26071701_RESOLVED_20260722.md | 2026-07-22 | SIGNALS.md (FROZEN) | ELIGIBLE |
| signals_archive/GATE_ADJUDICATIONS_20260710_20260716.md | 2026-07-31 | PREDICTIONS_COLD.md (cold companion, not live) | ELIGIBLE |
| signals_archive/PREDICTIONS_PASS_LOG_20260627_20260724.md | 2026-08-28 | PREDICTIONS_COLD.md | eligible 10/28 |
| outbox/delivered/ — 9 packets 2026-06-27 → 07-22 (+ .gitkeep 6/30) | 07-05 … 07-22 | none | ELIGIBLE (retired lane) |
| outbox/delivered/2026-09-02_to-PROME_self-audit-slate-drain-and-split.md | 2026-09-29 | none | not yet (11/28) |
| research/2026-08-12b_falsifier_base_rate_audit.md | 2026-08-12 | none | ELIGIBLE |
| research/2026-08-12_split_falsifier_RESOLUTION.md | 2026-08-17 | PREDICTIONS_COLD.md only | ELIGIBLE |
| research/2026-08-03_split_and_coverage_prereg.md | 2026-08-03 | CLAUDE.md Disc-J (live protocol) | KEEP |
| research/2026-08-28_successor_falsifier_RESOLUTION.md | 2026-08-28 | BRIEFING, PREDICTIONS_COLD, STATUS_COLD | eligible 10/28 |
| recon/2026-06-06_c_id_index.md | 2026-06-06 | CONFIRMED.md:4 (live, but a nav pointer, which root clause ② does not count) | ELIGIBLE once ❌1 is fixed; archive it and repoint |
| BRIEFING_2026-08-29_SYSTEMS_REVIEW.md | 2026-08-28 | DOCKET L206 (resolved), proposals, processed inbox, DAEDALUS profiles | eligible 10/28 (⚠️15) |

Retired lanes, as the charter claims: `SIGNALS.md` FROZEN banner ✅ · `outbox/` no banner ⚠️ · `signals_archive/` no banner ⚠️ (last touched 8/28, as the charter says).

## Verdict
- **Works:** the mechanical spine. Every crc32 recomputes, every §H and file pointer resolves, every FRED mark and threshold distance recomputes from the raw pulls, no docket date is past, and the NEXUS-carried DOCKET wakes match PROME's rows.
- **Does not:** the trophy case (CONFIRMED.md) carries an ID-colliding "full index" pointer, a false "struck above", an unrecorded T6 outcome and an open-ended C-35 note. PROME's mirror rows L631 and L752–L754 lag NEXUS's state with no packet sent. STATUS misfiles the PRED-41 wake (11/06 → "mid-Nov") and holds M-10 at 25% with no falsifier.
- **Most valuable change:** one Standard-tier correction commit before Monday. Fix CONFIRMED (❌1, ❌2, ❌6, ⚠️8), STATUS (❌3, ❌4, ⚠️1, ⚠️2) and LC (❌5), and send one PROME packet covering L631, L752–L754 and L40, all inside the rotation Monday's pass needs anyway (STATUS has 6 B of headroom).
