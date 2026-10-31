RESULT READ (read 2 of the WQ-295 R2 encode episode) · independent Opus reader · written 2026-10-31 14:07 EDT
Artifacts: working-tree diff of PROME/tools/spawn_list.py · PROME/tools/prome_gate.py · PROME/CLAUDE.md · PROME/AUTONOMY.md, against record PROME/proposals/2026-10-31_wq295-R2-encode-RULED.md (read first, whole) and the plan-read ledger (scratchpad wq295-plan-read.md, read so that declared residue is not re-flagged).
Read-only on the repository: nothing edited, staged, committed or stashed. Fixtures, shadow copies and scripts live under scratchpad/wq295-result/ (listed at the end).

VERDICT: HOLD — 2 ❌ · 5 ⚠️. The tool logic matches § 2 on every boundary I could build, the dated-row output / exit code / slate / --open paths are untouched, and the inserted text is byte-identical to §§ 3a and 4. The two ❌ are (1) the inserted charter and AUTONOMY text say the opposite of the tool on COVERED rows, which on 36 days of real history is 12 of the 35 CADENCE-DUE desk-days, and (2) the gate line reads green "CADENCE-DUE: none" when the cadence section cannot be evaluated at all.

════════════════ 1. Counterexamples (my own; the author's selftests are run separately, row CX19) ════════════════
| # | Probe | How | Observed | Result |
|---|---|---|---|---|
| CX1 | COVERED first-owner row vs the charter's "no open dated row (a PENDING DOCKET row or a LIVE GATES row)" | battery.py CE1; frozen 10/9 run (runA); 36-day history hist.py | state_kind = PENDING; tool prints C:HAWK "no first-owner row ≤ +14d" two lines under "covered-suppressed … D:L321 HAWK [COVERED]"; history: 12 desk-days (HAWK ×6, HENRY ×3, MIDAS ×2, SHADE ×1) | FAILED → ❌1 |
| CX2 | Whole cadence evaluation impossible (heading renamed `### DESK-CADENCE`; ROSTER path missing) | runB / runC on 10/9 frozen inputs → prome_gate.summarize_spawn_list; battery CE4 | gate ok=True, "CADENCE-DUE: none · cadence CANNOT-EVALUATE: *"; same inputs with the section intact owe C:MARCO, C:HAWK, C:SHADE (ok=False) | FAILED → ❌2 |
| CX3 | Cadence leg raises (spawn_slate import broken) | shadow copy of the new spawn_list beside a spawn_slate.py that raises; HEAD copy beside the same | new: traceback, rc 1, 0 of 46 dated rows printed, gate UNKNOWN; HEAD: 46 rows, rc 0 | FAILED (fail-closed, availability) → ⚠️1 |
| CX4 | Past-clock desk whose governing row is ACTIVE class | battery CE2; runA (VIOLET) | dated row = ACTIVE (consumer read, no wake); governed line says the row "wakes them — one wake, not two"; VIOLET 8–11 d past clock 10/6–10/9, woken by neither path, absent from the gate line | FAILED (text) → ⚠️2 |
| CX5 | Owner cell "HANS-led (owner)" | battery CE3 | first-owner token "HANS-": DARK dated row for non-desk "HANS-" AND C:HANS (two wake entries, one desk) | FAILED, latent (0 instances in 146 sampled DOCKET revisions since 9/25) → ⚠️3 |
| CX6 | Rider ② end-to-end through real git | temp repo: HANS own commit 3/01; WALTER delivery 3/08; PROME packet; loose-form "HANS packet delivered by PROME" into its inbox; "HANS packet -> processed" in PROME/; PROME commit with body line "HANS: …" | last_self_commit = 3/01; C:HANS due 3/08, Δ2 on 3/10 | HELD (closes plan-read ⚠️ 42) |
| CX7 | A10 contract | HEAD vs new, 10/9 frozen REV inputs, modes default · --tsv · --horizon 3 · --horizon 3 --tsv; --open --json · --open --tsv | count line, every dated row and rc identical; block appended after covered-suppressed; READ footer gains one sentence (non-tsv); --open outputs byte-identical | HELD (⚠️ 43 as declared) |
| CX8 | Slate unaffected | spawn_slate.py --stdout with HEAD spawn_list vs new, horizon 0 and 3, REV inputs incl. ORCH_LOG | bodies identical (header stamp line excluded), rc equal; spawn_slate.py unchanged vs HEAD | HELD |
| CX9 | Gate summary honesty, ordinary paths | runA; block stripped from runA; live output today | CADENCE-DUE present → not-ok, ids named; block absent → not-ok "MISSING"; live 10/31 → ok, UNREACHED CREED/FLG/RED/WAL, CANNOT-EVALUATE CATO/CYPHER/GIBBS/RAV | HELD |
| CX10 | GATES FIRED-UNEXECUTED row naming the desk | battery CE5 | does not govern → C:BRENT; consistent with the text's "a LIVE GATES row" | HELD |
| CX11 | GATES header drift (`Owner`) | battery CE6 | gate rows UNKNOWN, rc 2, gate not-ok | HELD (fail-closed) |
| CX12 | Rider ③ boundary | battery CE7, next row +14 / +15 | +14 governs, +15 UNREACHED | HELD as declared (⚠️ 20 / 7) |
| CX13 | Name collisions | battery CE8 (WAL vs WALTER, token-named definition rows, WALTER DAILY) | only C:WAL; token rows never named | HELD |
| CX14 | Will-first owner cell "Will / HANS (prep)" | battery CE9 | C:HANS beside a WILL-OWNED row | HELD as declared (⚠️ 19) |
| CX15 | Approximate date "~YYYY-MM-DD" | battery CE10 | not collected on either path; C:HOMER | HELD (consistent) |
| CX16 | MONTHLY clamp / year boundary | battery CE11: 12/31→1/31 within, 2/1 due; leap 1/31→2/29 within, 3/1 due | all as expected | HELD |
| CX17 | Real ROSTER layout | live and 10/9 ROSTER: H3 under `## Coverage notes`, token table first, TIER-2 rows above the separator, SPECIAL bold lines | token rows filtered; 39 desks read; CANNOT-EVALUATE = CATO, CYPHER, GIBBS, RAV (no cadence row) | HELD |
| CX18 | Live first-owner tokens that are not desks | owner_token over live PENDING rows | only "STUE" (L150 STUE/CARL; CARL governed by D:L843) | HELD |
| CX19 | Author selftests + existing suites | --selftest 11/11 · --cadence-selftest PASS · --cadence-wake-selftest PASS; test_spawn_list_fail_closed 15/15, test_spawn_slate 37, presence contract, covered_L368 26, open_query 9, L455 22, open_export 14; test_gate_orch_summary needs pytest (absent) — its spawn-list tests pass under a minimal shim | all pass | HELD |
| CX20 | Boot-gate time budget | `time` live run | new 2.1 s vs HEAD 0.1 s (gate timeout 120 s) | HELD |

History scan (hist.py, 2026-09-26 → 10-31, DOCKET/GATES/ROSTER at each day's last commit, liveness --until that day): 35 CADENCE-DUE desk-days; first 10/2 (MARCO). Output: scratchpad/wq295-result/hist_0926_1031.txt.

════════════════ 2. Findings ════════════════
❌1  The inserted text and its named driver disagree on COVERED rows — on real data, about one in three cadence wakes.
  claim → PROME/CLAUDE.md L51 (inserted): a WEEKLY/MONTHLY desk is CADENCE-DUE only "with no open dated row (a PENDING DOCKET row or a LIVE GATES row) naming it first owner due by today +14 days (overdue included)". AUTONOMY Tier-1 clause "no open dated row"; change-log row "(PENDING DOCKET or LIVE GATES)"; § 6 the same parenthetical.
  artifact → the neighbour, CLAUDE.md L49, needs "a PENDING DOCKET row **not annotated COVERED**" to exclude COVERED rows, so the new sentence (which copies L49's form without the qualifier) reads as including them; repo vocabulary agrees ("open" = state_kind PENDING; `spawn_list.py --open` banner "no COVERED filtering"; docket_view COVERED_BUT_OWED → PENDING). The tool takes `governing` from collect(+14), which drops COVERED rows (spawn_list.py L474, L920), and prints "no first-owner row ≤ +14d" (L525).
  command → battery.py CE1; runA (frozen 10/9) lines 49–53; hist.py.
  observed → 10/9: "covered-suppressed … D:L321 HAWK [COVERED] COVERED: HAWK's HARD successor-registration date, NOT met" and, two lines later, "⚠️ C:HAWK … no first-owner row ≤ +14d … Tier-1 wake (WQ-295 R2)". History: 12 of 35 CADENCE-DUE desk-days are this case (HAWK 10/6–9, 10/18–19 · SHADE 10/9 · MIDAS 10/10–11 · HENRY 10/16–18). Under the charter's letter none of those 12 is a wake; under the tool each is a Tier-1 wake. § 9 declares COVERED-exclusion as a PROME reading (⚠️ 49, "any one can go to Will if it bites"), but not that the encoded text now says the reverse.
  change → align them. Preferred (matches § 2, the 9/26 schedule Will saw — its "≤14d" column was collect(), COVERED excluded — and the operational case: L321 was an unmet hard date): add "not annotated COVERED," inside the parenthetical in § 3a / CLAUDE.md L51, the AUTONOMY change-log row and § 6, using L49's exact words; reword the C: basis to "no unsuppressed first-owner row ≤ +14d". It bites, so per ⚠️ 49's own trigger put the COVERED reading in front of Will. Alternative: make COVERED rows govern in the tool (matches the text and the ruling's letter, but leaves HAWK's unmet L321 date with no wake).

❌2  The gate line reads green "CADENCE-DUE: none" when no desk could be evaluated.
  claim → prome_gate.summarize_spawn_list (L1714–1730): "A missing block is UNKNOWN"; ok = rc == 0 and no CADENCE-DUE row.
  artifact → spawn_list.cadence_wakes L489 returns ([], [], [], [("*", "no ROSTER cadence section …")]) when the section is absent or the ROSTER is unreadable; the summarizer reads that as zero CADENCE-DUE.
  command → runB (heading renamed) and runC (ROSTER path missing) on 10/9 frozen inputs, each fed to summarize_spawn_list; battery CE4.
  observed → both: (True, "… CADENCE-DUE: none · cadence CANNOT-EVALUATE: *"); the same inputs with the section intact: (False, "… CADENCE-DUE: C:MARCO, C:HAWK, C:SHADE"). The stderr warning sits in the log, but run_script prints previews only for not-ok lines, so the gate shows green. The dated-row analogue (a failed git log) fails closed (UNKNOWN, rc 2); this leg fails open. A heading edit is plausible: the section already moved once (L446, 9/23).
  change → in summarize_spawn_list, when the CANNOT-EVALUATE list carries "*" (or the header's "CADENCE-DUE n" disagrees with the parsed C: rows), append "CADENCE-DUE UNKNOWN — no cadence evaluation" and return False, the same branch as MISSING.

⚠️1  Any exception in the cadence leg kills the reader and all dated rows — main()'s own "THE CADENCE READ MUST NEVER BE ABLE TO KILL THE READER" (L902) no longer holds.
  artifact → main() L920 evaluates cadence_wakes(...) as render's argument with no guard; cadence_wakes L490 now imports spawn_slate (a new dependency; HEAD spawn_list imported nothing from it).
  command → shadow copies, CX3. observed → new: 0 of 46 dated rows, rc 1, gate UNKNOWN; HEAD: 46 rows. The slate fails in the same event, and its FAILED banner points to spawn_list.py. Fail-closed, so no lie; A8 tests only the unreadable-ROSTER path.
  change → wrap the call in try/except in main(); on failure pass a cad tuple whose CANNOT-EVALUATE is ("*", "cadence block FAILED (<ExcName>)"); with ❌2's fix the gate then reads UNKNOWN while the dated rows still print.

⚠️2  The "governed" line says the governing row "wakes them — one wake, not two". That is false for ACTIVE-class rows (consumer read, no wake) and, until their date, for LANDS-IN rows.
  artifact → spawn_list.py L556. command → battery CE2; runA. observed → VIOLET, WEEKLY, 8–11 days past its clock on 10/6–10/9, governed by D:L464 (ACTIVE), was woken by neither path and is not on the gate line. The "any class governs" reading is declared (⚠️ 49); the wording and the invisibility are not.
  change → print the governing row's class and say "governs them (DARK = its own wake · ACTIVE = consumer read first · LANDS-IN = waits for its date)"; optionally name ACTIVE-governed past-clock desks on the gate line.

⚠️3  Latent double listing from the owner-cell form "DESK-led (owner)": the first-owner token "HANS-" yields a DARK dated row for a non-desk and C:HANS for the real desk (battery CE3). This is inherited owner_token behaviour, and I found no instance in 146 sampled DOCKET revisions since 9/25. Change: governing_owners could normalise a trailing "-", or declare.

⚠️4  Neighbour frictions that § 9 ⚠️ 23 does not list. (a) AUTONOMY Tier 2 "**Reviving / catching-up stale agents**" (L43) sits beside the new Tier-1 clause, and a cadence wake is by construction a wake of a stale desk (history: SHADE 29–33 days quiet, 9/26–9/30). (b) "only a WEEKLY or MONTHLY desk … wakes by age" (L51) sits beside Aged waits (L53), "blocking desk is dark ≥7 days" → wake, for any cadence. The ruling's own "never wake by age" phrase carries the same tension. Change: one clause each ("a single CADENCE-DUE L0 wake is not a revival program"; "wakes by cadence age"), or declare.

⚠️5  Declared residue confirmed live, for the record. (a) The slate, which is what BOOT.md step 6 reads for "spawn candidates", omits CADENCE-DUE: on 10/9 the slate is byte-identical before and after while C:MARCO, C:HAWK and C:SHADE exist, so the gate line and its log are the only boot surface (§ 9 ⚠️ 50 / BOOT.md note). (b) CATO and RAV (SPECIAL, Will-driven, no cadence token by design) will now be "surfaced in the boot report as CANNOT-EVALUATE" at every boot. The plan read raised this under ⚠️ 18, but § 9's ⚠️ 18 line does not carry it.

Note (no finding): the AUTONOMY change-log's 4th column is headed "Reason"; the new row puts "PROME prome-34" there, following the 10/29 C9 row.

════════════════ 3. Text against the record (B) ════════════════
✅ § 3a: the paragraph is byte-identical to the record's quote, occurs once, sits directly after the WQ-184 paragraph (L49) with a blank line on each side; CLAUDE.md numstat +2/−0.
✅ § 4a: the clause matches with "change log 2026-10-31" in place of the placeholder, immediately after the "(WQ-184 L0, change log 9/05)" anchor. ✅ § 4b: the row is exact, is the file's last line and has 4 cells; table_check ok. AUTONOMY numstat +2/−1.
✅ A13: grep of CLAUDE.md L51 finds each phrase once: "never grades anything on the desk's behalf and never marks a BOARD item consumed" · "surfaced in the boot report as UNREACHED (not woken)" · "a PENDING DOCKET row or a LIVE GATES row".
Plan-read fixes: ❌15 opened no contradiction. ❌16: BOOT.md step 8 still has no UNREACHED item (declared). ❌17's fix opened ❌1 — it adopted L49's form without L49's COVERED qualifier.

════════════════ 4. Ruling fidelity (C) ════════════════
Within the letter: WEEKLY/MONTHLY only · clock at more than 7 days / same day next month, clamped · a separate block "beside, never instead" (dated rows byte-identical) · EVENT-DRIVEN and ON-DEMAND never woken · rider ① printed for PROME to enforce · rider ② held end-to-end (CX6) · rider ③ UNREACHED, report-only · exit code unchanged.
Beyond the letter, all DECLARED in § 2 / § 9: first owner only · the +14 d window · any class governs · COVERED rows excluded · DAILY out · TIER-2/SPECIAL launchable · CANNOT-EVALUATE surfacing · the gate line ⚠️ on CADENCE-DUE.
UNDECLARED drift: (i) the COVERED reading reached the tool, but the encoded charter/AUTONOMY/§ 6 text states the reverse (❌1); (ii) the "wakes them" claim for ACTIVE/LANDS-IN governed desks (⚠️2). No other drift found.
A12 (concurrent activity) N/A holds: the block's footer names the same-minute preflight and doorbell.

════════════════ Evidence (scratchpad/wq295-result/) ════════════════
scripts/battery.py (CE1–CE11) · scripts/hist.py → hist_0926_1031.txt · scripts/survey.py · fx/runA.txt (10/9 frozen) · fx/runB.txt (heading renamed) · fx/runC.txt (ROSTER missing) · fx/runD_new_brokenslate.txt / fx/runD_head_brokenslate.txt · fx/slate_head_{0,3}.md vs fx/slate_new_{0,3}.md · live_h0.txt (live 10/31) · selftest.txt / cadence_selftest.txt · tmpgit/ (rider ② repo) · shadow_head/, shadow_broken/, shadow_head2/ (HEAD and broken-import copies; nothing in the repository was touched).
