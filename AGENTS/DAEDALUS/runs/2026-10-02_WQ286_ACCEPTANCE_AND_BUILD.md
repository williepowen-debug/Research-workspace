**CURRENT DISPOSITION — 2026-10-03:** October 2 source landed in `536480c90`. The referenced October 2 reader ledger was not recovered; its verdict is not reconstructed. Fresh independent review found three G1 boundary defects; a narrow repair and final result read now pass 33 producer + 9 independent tests, with zero attention-result changes across 323 declared-glob files. G2 and R2 accepted within their stated limits. Review: `runs/2026-10-03_WQ286_READER_REPORTS.md`; synthesis: `runs/2026-10-03_CATCHUP.md`. Historical acceptance/build text follows unchanged.

---

# WQ-286 ①–④ — acceptance conditions (written before the edits) and build record

**2026-10-02 17:45 EDT, DAEDALUS, Will-launched ("lets start working through all this").** Ruling: Will 2026-09-24 18:30 ET, verbatim *"The rest are approved"* on PROME's list that named WQ-286 with PROME's recs (`PROME/proposals/2026-09-24_wq-batch-284-252-285-286-RULED.md` row WQ-286: ① BARON freeze, leg (b) waived · ② G1 · ③ G2 · ④ R2 = REQUIRE THE RECEIPT). Source findings: `runs/2026-09-24_STALENESS_SWEEP_05.md` §2 and §8; `runs/2026-09-24_D4_CHECKER_INDEPENDENT_READ.md` R2.
At this stamp: `scripts/ledger_staleness.py` md5 `3e07836bdaa5cf6422e3292c976abff0` · `scripts/corrections_boot_check.py` md5 `8c60250120b912f50cd174978b1201fc`. Both are in my `scripts/` grant (Will 2026-07-31). Process-ceiling note: PROME's WQ-299 R1 is PROME's rule; these four are Will-approved builds Will asked for today by name.

## ② G1 — attention-clock aliases (`ledger_staleness.py`)

**Property:** a behind ledger whose header says someone LOOKED on a date is classed by that date whatever of the fleet's three measured spellings it uses; a ledger with none of them is byte-identical to today's output.

| # | Condition |
|---|---|
| 1 | ORDINARY: `Staleness sweep: D`, `Staleness sweep (no data): D`, `Last staleness check: D` each parse as an attention clock, case-insensitive, in a header line up to column 100 (`MARKER_COL_CAP`), including mid-line after a `\|` separator (the fleet's two-clock form) |
| 2 | OVERLAP: a header with the canonical key AND an alias uses the NEWEST date, as today's rule for the four legacy spellings |
| 3 | WRONG OWNER: prose mentions (`staleness-sweep #4`, `the staleness sweep found`) with no `: DATE` do not parse; a date past column 100 does not parse |
| 4 | MISSING INFO: a malformed date after an alias is skipped, never crashes |
| 5 | POPULATION: on `--all --quiet` the only lines that change are at desks whose headers carry an alias (sweep #5 measured 5 desks: CARL-STUE, FERT, FLG, TERRY, WAL); every other line byte-identical to the before-capture |
| 6 | The §3 watch: the alias line fires on a live file that carries one (FERT `workbook/FLOW.tsv`) and the clean line prints on a live file that carries none |

## ③ G2 — a header with two data clocks reads by its OLDEST (`ledger_staleness.py`)

**Property:** when the first 8 header lines carry more than one distinct `Last real data refresh:` date, the ledger's content clock is the OLDEST, and the scan says so; a header with one date, or one date repeated, is unchanged.

| # | Condition |
|---|---|
| 1 | ORDINARY: two distinct dates in either order → the oldest governs; the row prints `⚠️ 2 data clocks (older / newer)` |
| 2 | OVERLAP: the same date twice → one clock, no warning, byte-identical |
| 3 | WRONG OWNER: a date in a `prior:` history clause still counts (fail toward alarm — the sweep could not tell the 3 history-looking cases from FALCON's deliberate one without reading); the warning makes the owner's choice visible |
| 4 | MISSING INFO: no date → git time → mtime, as today |
| 5 | POPULATION: FALCON `workbook/FLOW.tsv` flips from `ok +9d` to a flag with the 2026-04-20 clock (sweep #5's instrument-blind case). HOMER STATE_HSG, REGINALD VX and PREDICTIONS, BRENT's snapshot: each outcome printed in the record, with the owner packeted only if a NEW flag appears |
| 6 | `--nudge` and `--trade` paths use the same reader, so they inherit the oldest-clock rule (one function) |

## ④ R2 — a RETIRED row does not discharge a named target without its receipt (`corrections_boot_check.py`)

**Property (Will: REQUIRE THE RECEIPT):** among rows naming this desk, a status of `RETIRED` is treated exactly like `RECEIPTED`/`DEAD-AT-CAP`: only this desk's own receipt of ANY action clears it.

| # | Condition |
|---|---|
| 1 | ORDINARY: NAMED `RETIRED` row, no receipt from this desk → BLOCK rc 1, labelled `[RETIRED — owner-declared closure; a receipt is still required, WQ-286 ④]` |
| 2 | NAMED `RETIRED` row, receipted by this desk (any action) → skip |
| 3 | `ALL` `RETIRED` row → the ALL-row rules (INFO/WARN, never block), unchanged |
| 4 | WRONG OWNER: a `RETIRED` row naming another desk is not this desk's |
| 5 | POPULATION: the live register carries 0 `RETIRED` rows at this stamp (`grep -c` on the status column), so every desk's boot rc is unchanged today; the selftest regression case "RETIRED NAMED unreceipted → 0" flips to → 1 and is renamed |
| 6 | The docstring's rc-1 line and the comment at the RETIRED branch say the new rule; the stale "the only thing that does" comment is scoped |

## ① BARON freeze

Not code. Leg (b) waived by Will; BARON dormant since 5/08 (ROSTER), last self-commit 2026-02-12. Files: `AGENTS/BARON/data/{CATALYSTS,EDGES,NODES}.tsv` (git-time 2026-02-01) + `STATE.md` ("Last Updated: 2026-02-12"). Banner form = root CLAUDE.md two-state rule: `FROZEN <date> — not maintained; …do not cite rows as current`. Recommendation to record: BARON stays DORMANT on ROSTER (a frozen ledger set is not a tool). Also to list: the unread PROME packet of 2026-08-12 in `AGENTS/BARON/inbox/`.

## Completion states
IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED (Opus reader, did not write the fix, ≥1 own counterexample) · STILL UNRESOLVED — kept distinct.

## Build record — 2026-10-02 17:59 EDT (DAEDALUS)

**STATE: ① DONE · ② G1 IMPLEMENTED · TESTED · INDEPENDENTLY READ (round 1 FAIL → fixes → round 2 pending at this write) · ③ G2 same · ④ R2 IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED (round 1 PASS, residue pinned).** Independent reader: Opus `wq286-reader` (did not write the edits); ledger copied to `runs/2026-10-02_WQ286_reader_ledger.md` at closeout.

| Item | What landed | Measured |
|---|---|---|
| ① BARON | `# FROZEN 2026-10-02 — …` banner on `data/{CATALYSTS,EDGES,NODES}.tsv`; `> FROZEN` header on `STATE.md` naming the unread 8/12 PROME packet (51 d) | `ledger_staleness.py BARON --glob 'data/*.tsv'` → 3 × FROZEN. Recommendation recorded: BARON stays DORMANT on ROSTER; a frozen ledger set is not a tool. 21 TSVs under `domains/` were not in the approved set and are not bannered |
| ② G1 | two alias regexes; a colon REQUIRED (reader's counterexample: "the staleness sweep 2026-09-20 flagged…" parsed under `[:\s]+`); the column cap is WAIVED for a key preceded by `\|` (the reader measured FERT's five alias segments at columns 201–328 and FLG's at 360/526 — past the cap, so the alias reached 0 files at the two desks that motivated it) | fleet `--all --quiet` delta: TERRY LEDGER `UNATTENDED (attention 44d)` · WAL PREDICTIONS `held (attention 5d)` · CARL-STUE CASCADE `UNATT 54d`; FERT 5 files annotated at `--days 0`; FLG 2 |
| ③ G2 | `content_clocks()` + `content_time()` = OLDEST of the distinct dates in the 8-line head; the row prints `⚠️ N data clocks (…), oldest governs`; the regex accepts a parenthetical qualifier before the colon (reader's silent-clean counterexample: `Last real data refresh (HAWK rows): 2026-04-20` beside a plain newer clock reproduced the FALCON blind shape) | population is **9 live ledgers, not the sweep's 4**: HOMER ×7 (`PRIOR HEADER VERBATIM` chains), WAL KB, REGINALD PREDICTIONS. New flags today: HOMER STATE_HSG (+42d), REGINALD PREDICTIONS (+38d) → owner packets sent. HOMER's other six read ok +19d and flip at +30d (~10/13) unless the chains lose the key phrase — in the packet. FALCON FLOW now carries ONE clock (FALCON removed the second between 9/16 and 9/28), so the sweep's capable case is gone; HOMER is the live capable case |
| ④ R2 | `RETIRED` no longer skips a NAMED row; label `[RETIRED — owner-declared closure; a receipt from this desk is still required, WQ-286 (4)]`; selftest 18 → 21 cases (the old "RETIRED → 0" regression case flipped to → 1; receipted → 0; other desk → 0; RETIRED ALL-row future cap → 0 WARN) | live register 0 RETIRED rows; reader: 0 rc / 0 output diffs across 47 desks + PROME; rc contract 0/1/2 unchanged; consumers key on rc only |
| selftests | `ledger_staleness.py --selftest` 20 → 33 (13 G1/G2 drills = the reader's counterexamples); `corrections_boot_check.py --selftest` 21/21; `validate_all --only A1` and `--only A7` PASS | mutants: cap waiver off · colon not required · oldest→newest · qualifier off — 4/4 killed |

**Acceptance conditions amended by the read:** G1 c3 letter (a date past column 100 DOES parse when the key follows a `\|`; the cap is on the match start) · G1 c6 (the FERT watch is on all five FERT ledgers at `--days 0`, FLOW among them) · G2 c5 (population 9; FALCON overtaken) · G2 c6 STRUCK (`--nudge` reads `status_writes_since`, not the content clock — the claim was false).

**STILL UNRESOLVED (declared):** R1 the `\|` waiver reads an alias in any header line containing a `\|` before it — a prose line with a pipe could parse (toward held, the quiet direction; no live instance found by the reader, who was asked to look again in round 2) · R2 a parenthetical of up to 60 chars before the colon could swallow text; a data cell in the first 8 lines containing the phrase becomes a clock (no live instance) · R3 the 8-line head scope is unchanged (an older clock on line 9 is invisible) · R4 in non-quiet mode an `ok` row with 2 clocks prints `⚠️` at rc 0 (marker/rc split; no marker-only consumer found) · R5 a NAMED RETIRED row with a passed cap is not counted in the DEAD-AT-CAP header line (cosmetic) · R6 WALTER's spec half of ④ (the prune ladder's RETIRED definition) is PROME's packet, not re-checked here · R7 round-2 read pending at this write; any fix after it is unread.
