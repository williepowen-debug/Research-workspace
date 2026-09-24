# 2026-09-24 — Parser fixes build: docket_view ᶜ tag · validate_all WQ splitter + KB comment header · baseline re-sweep

**Built by:** DAEDALUS build subagent (teams-mode, lead = DAEDALUS). **Standard:** `BLUEPRINTS/CHECK_STANDARD.md` §3: every behaviour change was run, with the capable-case and clean-case output quoted below. **Git:** no mutating git command was run. The files are left uncommitted for the lead to commit, path-scoped.

**Files changed (exactly three):**

| File | Diff |
|---|---|
| `scripts/docket_view.py` | +17 / −2 (tag() + 2 selftest drills + count 24→26) |
| `scripts/validate_all.py` | +75 / −4 (split_cells copy + call site + SHIFTED-ROW message · KB header skip + `KB_COMMENT_RE` · 4 drills · `EXPECTED_DRILLS` 38→42) |
| `scripts/validate_all_baseline.json` | +5 / −3, re-swept 2026-09-24 + `recheck_by` + `note` |

Pre-edit copies md5-matched `HEAD` (docket_view `9c3ddec9`, validate_all `f679c26d`, baseline `f5f4b94d`), so the whole diff on these three files is this build. Other `scripts/` files show as modified in the working tree (corrections_boot_check, market, pipeline_rc_guard, safe-push). Those are **not mine**, so do not sweep them into this commit. Live inputs were snapshotted and did not change during the build: DOCKET `aa978e6f`, WILL_QUEUE `01523f56`.

---

## 1. `scripts/docket_view.py` — ᶜ (COVERED) tag

**Diff:** in `tag()`, the test `"COVERED" in r["state"].upper()` became `re.search(r"(?<![Nn]ot )(?<!NOT )\bCOVERED\b", r["state"])`. It is now case-sensitive, matches only the whole word, reads the raw cell, and adds a one-token negation guard. The ᵒ (OVERDUE) test is unchanged. Selftest drill 9i adds a 3-row fixture: `recovered` + `spawn_list.covered()` must not tag, `PENDING · COVERED: BRENT` must tag, and `Not COVERED` must not tag.

**⚠️ Deviation from the prescribed fix, with the reason:** the prescribed `\bCOVERED\b` alone does **not** clear L380, one of the two lines PROME named. Since the 9/19 sitting, L380's state cell carries the literal text `Not COVERED, not re-dated` (and so do L40 and L263). The negation lookbehind is what removes them. The prescribed-only variant would still tag 7 rows, not 4.

**PROME's line numbers checked in the file:** **REFUTED as of today.** The 9/18 packet (`inbox/2026-09-18_from-PROME_docket-view-COVERED-…`) named L140 · L198 · L125 as the true COVERED overdue rows and L380 · L397 as the false positives. On the live DOCKET, 2026-09-24:
- **L140** and **L198** are condition-keyed (col 1 = `on-…`), so they are UNDATED and absent from the OVERDUE block. Their `COVERED` text is inside a quote: `PREVIOUS STATE, verbatim: PENDING — COVERED:BRENT`.
- **L125** and **L397** are `RESOLVED 2026-09-19`, so they are not live.
- **L380** is still a false positive, now through `Not COVERED` as well as `recovered`.
- The "recovered"-substring false positives today are **L370** (`spawn_list.covered()`) and **L403** (`recovered from ARGUS`).

**Capable case: live render, before vs after** (`--write PROME/SCRATCH.md --dry-run --docket <snapshot> --as-of 2026-09-24`, rc 0 both):
```
before: L380 9/16ᶜ L40 9/18ᶜ L263 9/18ᶜ L370 9/19ᶜ L403 9/19ᶜ L451 9/21ᶜ L453 9/21ᶜ L384 9/22ᶜ L427 9/22ᶜ
after:  L451 9/21ᶜ L453 9/21ᶜ L384 9/22ᶜ L427 9/22ᶜ
```
The 4 rows that still tag all lead their cell with `PENDING · COVERED`. The diff of the whole block changes only the OVERDUE line (1 line removed, 1 added). The header, the docket-crc32 value (256724629) and the calendar are unchanged.

**Selftest, new build:** `DOCKET-VIEW SELFTEST ✓ 26/26 drills behaved`, rc 0.
**Selftest, mutant with the old tag logic spliced in** (`scratchpad/fix-parsers/docket_view_mutant_oldtag.py`): rc 1.
```
  ✗ OVERDUE ᶜ: 'recovered'/'covered()' do NOT tag (L3) — rc=0
  ✗ OVERDUE ᶜ: 'PENDING · COVERED: BRENT' DOES tag (L4); 'Not COVERED' does NOT (L5) — rc=0
DOCKET-VIEW SELFTEST ✗ 2 drill(s) FAILED — do not trust the tool
```
**rc contract unchanged** (docstring): `--selftest … rc 0 all behaved · 1 a drill failed (do NOT trust the tool)`. The `--write`/`--check`/`--check-generated` rc lines are untouched.

**Residue (not verified or not fixed):**
- The ᵒ tag keeps the old substring test. Today it has three lowercase-only `overdue` cells (L124, L220, L308), none of them in the OVERDUE block, so the render is unaffected. It is the same bug class and was left unfixed deliberately.
- The negation guard covers only `not `/`Not `/`NOT ` directly before the token. Other negation phrasings, such as "no longer COVERED", would still tag.
- The quoted-prior-state form (L140/L198: `PREVIOUS STATE, verbatim: … COVERED`) would still tag if those rows ever became dated and overdue.
- I did not run `--write` against the real `PROME/SCRATCH.md`. PROME's generated block will change at its next render, and PROME's SCRATCH caution line beside the block can come down.

---

## 2(a). `scripts/validate_all.py` — WILL_QUEUE splitter

**Diff:** `split_cells()` is copied verbatim in semantics from `PROME/tools/table_check.py::split_cells`, and the provenance is noted in its docstring. It holds `\|` out of the split, strips ONE leading and ONE trailing pipe, and treats every other pipe as a separator, code spans included. `leg_will_queue` now calls it in place of `line.strip("|").split("|")`. The count-mismatch defect now reads `SHIFTED ROW — N cell(s), header has M (id X); every cell right of the break is mis-columned (needed-by etc.) — escape a literal pipe as \|`. Drills added: an escaped pipe gives PASS; an unescaped pipe gives SHIFTED ROW FINDINGS rc1; `split_cells` puts needed-by in column 4 when the Item carries `\|` inside a code span.

**Live `PROME/WILL_QUEUE.md`: cell counts per numbered row, old vs new splitter.** All 18 other rows give 7 = 7. The one that differs:
```
L41 WQ-157 esc=1 old=8 new=7 needed_by_new='2026-09-19 (pairs with the 9/1' needed_by_old='RULE (leg ②)'
```
**WQ-263** is no longer an open row. It moved to RECENTLY DONE on 9/23 and sits at L62 as a bold-id row (`| **263 …`), which `WQ_ROW_RE` does not type, so this leg never reads it.

**Leg B3 on the live file:**
```
before: ❌ B3 WILL_QUEUE.md typing  [FINDINGS, structural] 1 typing defect(s) over 19 queue row(s)
              · L41: 8 cell(s), want 7 (id 157)
after:  ✅ B3 WILL_QUEUE.md typing  [PASS, structural] 19 queue row(s), 7 cols, ids unique
```
The before-state was a **false FINDINGS**: the old parser split WQ-157's escaped pipe.

---

## 2(b). `scripts/validate_all.py` — KB comment-header trap

**Diff:** in `leg_kb_stale_by`, `head = fh.readline()` now skips leading blank lines and comment lines before taking the header. A comment line matches `KB_COMMENT_RE = ^\s*"?#`, which covers both a bare `#` and a TSV-quoted `"#`. The quoted form is not hypothetical: OSPREY's KB L4 is a `"# ⚠️ WHY THIS HEADER EXISTS…` line, and a bare-`#` skip alone would have left OSPREY in `no_col`. Drill added: a KB with a `# Last real data refresh` line, a `"#` line and a blank line ahead of its header must still be supervised (expected: FINDINGS rc1 over baseline 0).

**Other header-read sites in validate_all.py, all checked:**

| Site | Reads | Trap? |
|---|---|---|
| `_tsv_rows` (L261) → `leg_docket`, `leg_gates` | DOCKET, GATES | NO: skips blank and `#` lines already |
| `load_gaps` | `validate_all_gaps.tsv` | NO: filters `#` and blank lines before `lines[0]` |
| `leg_will_queue` | markdown table | n/a (not a TSV) |
| `leg_kb_stale_by` | `AGENTS/*/workbook/KB.tsv` | **YES: the only trapped site; fixed** |

**ZHAO drill** (a scratch root holding only ZHAO's live `KB.tsv`, md5 `a08df398`, run plain and with the prefix line):
```
orig / plain    : ⚠️ C2 [ADVISORY] 49 row(s) past Stale_By … (control: 108 dated cells over 1 KB(s); 0 KB(s) have no Stale_By column)   rc=0
orig / prefixed : ⛔ C2 [CANNOT-CERTIFY] positive control FAILED — 0 parseable Stale_By cells across 1 KB(s) …                               rc=2
new  / plain    : ⚠️ C2 [ADVISORY] 49 row(s) past Stale_By … (control: 108 dated cells over 1 KB(s); 0 KB(s) have no Stale_By column)   rc=0
new  / prefixed : ⚠️ C2 [ADVISORY] 49 row(s) past Stale_By … (control: 108 dated cells over 1 KB(s); 0 KB(s) have no Stale_By column)   rc=0
```
This reproduces ZHAO's finding. With the fix, the prefixed file is supervised identically to the plain one (108 = 108). ZHAO's "91 rows" figure was measured against the 9/18 vintage of the file; today it has 180 data rows, 108 of them with a bare-date Stale_By.

**Live fleet: KBs in `no_col` before vs after.** The tool's own headline says 20 → 9. My harness lists the names and agrees on the counts:
```
BEFORE 20: BRENT CORAL CREED FALCON FERT FLG HAWK HENRY HOMER LABOR MARCO MIDAS OSPREY OTTO OZK REGINALD SAM VULCAN WATT WAL
AFTER   9: CORAL HENRY MARCO MIDAS OTTO REGINALD SAM VULCAN WATT
newly supervised (11): BRENT CREED FALCON FERT FLG HAWK HOMER LABOR OSPREY OZK WAL
```
**Supervised desks: 11 → 22 of 31.** Leg C2 on the live repo: before, `657 row(s) … control 1547 dated cells … 20 no col`; after, `1345 row(s) … control 2774 dated cells … 9 no col`. The +688 newly visible expired rows break down as HAWK 199 · OZK 145 · BRENT 99 · FALCON 77 · LABOR 56 · OSPREY 49 · HOMER 36 · FERT 24 · CREED 2 · FLG 1 · WAL 0, and 657 + 688 = 1345 reconciles.

**Selftest:** `✅ SELFTEST 0: 42/42 drills behaved`, rc 0. **Mutant** with both old parsers spliced back in (`scratchpad/fix-parsers/validate_all_mutant_oldparsers.py`): rc 1, `❌ SELFTEST 1: 40/42`. Failing:
```
FAIL  B3 escaped pipe `a \| b` inside a cell keeps 7 cells -> PASS …  got [FINDINGS] L3: SHIFTED ROW — 8 cell(s), header has 7 (id 157)…
FAIL  C2 `# Last real data refresh` header line -> row still supervised …  got [CANNOT-CERTIFY] positive control FAILED — 0 parseable Stale_By cells…
```
The `split_cells` column drill and the SHIFTED-ROW drill still pass in the mutant. They exercise the function directly and the message text, not the call site that the mutant reverted, so they are not evidence for the call-site fix. The two FAILs above are that evidence.

**rc contract unchanged** (docstring, verbatim): `0 no leg in FINDINGS or CANNOT-CERTIFY · 1 >=1 leg in FINDINGS (a structural defect, or a delta above baseline) · 2 CANNOT-CERTIFY … 2 dominates 1.`

**Residue (not verified or not fixed):**
- **OTTO** has an uncommented `FROZEN …` banner line and an uppercase `STALE_BY` header, so it stays in `no_col`. Fixing that needs a banner rule and a case-fold, which is a separate decision.
- **BRENT (99) and HOMER (36)** are FROZEN-bannered KBs whose rows are now counted: 135 of the +688. Whether C2 should exclude FROZEN ledgers is a design call I did not make.
- Comment lines *inside* the KB body are still split as rows. They are harmless unless their Stale_By column happens to hold a date.
- A KB whose real header itself begins with `#` (for example `#ID\t…`) would now be skipped. No live KB has that form (all 31 surveyed).
- The docstring BASELINES block (L62–68: "13 queue rows", "534", "6/37") is the v1 build-time record. I left it as history, not as a current figure.
- Out-of-scope FINDINGS seen in the full run, not touched: **B1** DOCKET L140/L198/L208 (col-1 `on-…` condition keys fall outside the B1 grammar) and **B2** GATES L22 (`review_by` = `BROCK · owner-surface disagreement…`, which looks like a shifted row).

---

## 3. `scripts/validate_all_baseline.json` — re-sweep

**Method:** `python3 scripts/validate_all.py --only C2,D1 --rebaseline`, run AFTER fix 2(b). This is the registered writer: it refuses to write from a leg that measured nothing, and both legs measured. Output: `baseline written … {"swept": "2026-09-24", "C2_kb_stale_by": 1345, "D1_read_cap_over_budget": 2}`. I then added the two keys by hand.

| key | before | after |
|---|---|---|
| swept | 2026-09-10 | 2026-09-24 |
| C2_kb_stale_by | 534 | **1345** (+688 from the newly visible KBs; the old code also read 657 today, already +123 over 534) |
| D1_read_cap_over_budget | 6 | **2** (the live leg reads 2/37 over BUDGET, 0/37 over CAP; a baseline of 6 had left 4 desks' headroom unflagged) |
| recheck_by | — | 2026-10-15 |
| note | — | a baseline catches only RISES; re-sweep on or before `recheck_by` and move `recheck_by` by hand |

**Reader check:** `load_baseline` does `json.loads` and every consumer uses `.get(key)`, so the extra keys do not break it and **no reader change was needed**. Checked: the file loads, and `--rebaseline` on a scratch root keeps `recheck_by`/`note` (load, update, write).
- **Clean case** (live, at the new baseline): `⚠️ C2 [ADVISORY] 1345 …` · `⚠️ D1 [ADVISORY] 2/37 …` · `✅ VALIDATE-ALL 0 CLEAN`, rc 0.
- **Capable case** (live, old baseline 534, before the re-sweep): `❌ C2 [FINDINGS] 1345 … DELTA +811 above recorded baseline 534`. The suite drill `C2 one expired row over baseline 0 -> FINDINGS, rc1` passes.

**Full suite after all fixes, before the re-sweep:** A1–A9 PASS (A2 `26/26`), B3 PASS, C1 ADVISORY, D1 ADVISORY, B1/B2/C2 FINDINGS, rc 1.

**Residue:**
- ⚠️ **Nothing reads `recheck_by`.** It is an inert register field (CHECK_STANDARD §11: no named reader). Making it fire needs a leg or a `sweeps_due.py` line that alerts when today > recheck_by. I did not build that. Recommended next move: register it in `sweeps/REGISTRY.tsv` or add a one-line check to validate_all.
- `--rebaseline` rewrites `swept` but not `recheck_by`. The note says so.
- The rise to 1345 is instrument visibility, not a fleet regression. Any downstream reader that cites "534" as the fleet backlog is now stale. I did not run the 1c consumer_check (read-only session); the lead should run it at closeout (`--old 534 --new 1345`, and `--old 6 --new 2` for D1).
