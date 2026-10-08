# L530 owner-notice patch v2 — independent DELTA read (W1/W2)

**Verdict: ACCEPT-WITH-RESIDUE — ❌ 0 · ⚠️ 3 · ✅ 17.** W1 FIXED (reported shape) · W2 FIXED · no new defect that changes any verdict; v2 output is byte-identical to v1 on the 47 live desks compared, and rc is identical to the unpatched file on all 51.
**Finished:** 2026-10-08 15:06:24 EDT. Read-only on the repo; this file is the only repo write.
**Started:** 2026-10-08 15:01:07 EDT
**Scratch:** `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-DAEDALUS/fb3036d7-4638-4833-8e75-c6a4f2e92ca4/scratchpad/l530_reader/` (`v1/`, `v2/` = live `scripts/read_cap_check.py` + each patch; fixtures under `ce/`).

## Running log
- 15:01 hashes: `sha256sum` live `scripts/read_cap_check.py` = b5fbd2fd… (= target_hashes `before`; last commit 39178712a 2026-10-05, HEAD a37ce7b1d). `patch -p1` v1 → ecd31652… (= `after_v1`), v2 → e7f511e1… (= `after`). Both apply clean.
- 15:01 `diff -u v1 v2`: 2 code hunks, both in `foreign_reads` (under_home W1; directory skip + `exists` W2), plus EXPECTED_LEGS 125→127 and N5/N9/N10 test hunks. No other code moved.
- 15:02 `--selftest`: v1 125/125 rc 0; v2 127/127 rc 0. Revert of ONLY the two code hunks (`patch -R` of the code part of the v1→v2 diff) → 125/127 rc 1, ❌ exactly N9 and N10. Author's falsification claim reproduced.
- 15:02 live tree shape (`for d in AGENTS/*/sub_agents/*/`): 12 sub-agent dirs — CARL×7 chartered, MARCO/TOURISM chartered, MARCO/{BORDER,HOUSING,MIGRATION,WORKFORCE} charterless. 0 files directly in `sub_agents/`, 0 nested `sub_agents/*/sub_agents`, 0 duplicate sub-agent names, 0 sub-agent names colliding with a top-level chartered desk, 0 non-regular CLAUDE.md.
- 15:03 reviewer fixtures `tools/ce.py` (16 cases, frozen tempdirs, both v1 and v2, `m.ROOT`/`m.READS_TSV` set to the fixture; output `ce/all.txt`). Results summarised in the leg table below.
- 15:04 `grep -rn foreign_reads --include=*.py` (repo, excluding builds/): the only caller is `check_agent` → `foreign_reads(name)` with no `root`, so `base_root == ROOT` on every reachable path. `desk_home.ambiguous` is set at :142 and read nowhere. Live READS.tsv rows ending `/`: 1 (`NEXUS AGENTS/NEXUS/ grep`, not cap-bearing).

- 15:04 live, three builds (`base` = unpatched live file, `v1`, `v2`), each `--agent` run in a fresh process via `tools/live.py` (importlib, `m.ROOT`=repo, `m.READS_TSV`=live manifest): 38 `fleet_desks()` + DAEDALUS + 7 CARL sub-agents + TOURISM, then SENTRY/BARON/RAV/CATO = all 43 FLEET_DIRECTORY rows + 8 sub-agents = 51 desks.
- 15:05 receipts re-checked: `git log ae7bf8d27` = "HANS 10/8 … THRESHOLDS rotated 103%->68%" (live 22,120 B, 68%); BROCK/ZHAO packets committed in f2d5733de 15:01:13; live `scripts/read_cap_check.py` still b5fbd2fd… at end of read.

## Legs

| id | claim tested | command / fixture | result | verdict |
|---|---|---|---|---|
| L1 | base hash = live; v1/v2 result hashes | `sha256sum` live + `patch -p1` builds | live b5fbd2fd… = `before`; v1 ecd31652… = `after_v1`; v2 e7f511e1… = `after`; both apply clean | ✅ |
| L2 | delta is confined to `foreign_reads` + tests | `diff -u v1/… v2/…` (`v1v2.diff`) | 2 code hunks (under_home; dir-skip/`exists`), EXPECTED_LEGS 125→127, N5 fixture + N9/N10. Nothing else | ✅ |
| L3 | v2 `--selftest` 127/127 | `python3 -B v2/scripts/read_cap_check.py --selftest` | `✅ READ-CAP SELFTEST 127/127`, rc 0 (v1: 125/125 rc 0) | ✅ |
| L4 | N9/N10 can fail (author's "watched") | `patch -R` of only the two code hunks onto v2, `--selftest` | 125/127 rc 1; ❌ exactly N9 `got (False, True, False)` and N10 `got (True, False, 0)` | ✅ |
| L5 | catch-up unittest unaffected | test copied under `$SCR/{base,v2}/AGENTS/DAEDALUS/tests/` (it resolves the module via `parents[3]`), `python3 -B -m unittest discover …` | 29 OK both | ✅ |
| L6 | W1: `sub_agents/S/CLAUDE.md` is a DIRECTORY (not a charter) | `ce.py c01` | v1: OW clean line, file nowhere (S rc 2). **v2: OW notice 🟠 `sub_agents/S/f.md` 123% ← RD:9, owner_notices=1/1**, no clean line | ✅ |
| L7 | W1 charter test agrees with desk_home on symlinks | `c02a` (CLAUDE.md → file symlink), `c02b` (dangling) | 02a: v1=v2, S owns it (S notice 1/1, OW clean). 02b: v1 nowhere; **v2 OW notice 1/1**, S rc 2 | ✅ |
| L8 | W1 one level down: chartered S, charterless `S/sub_agents/T/` | `c03b` | v1: OW and S both clean, file nowhere. **v2: S notice 1/1** | ✅ |
| L9 | W1 via a CLASS row: `AGENTS/OW/sub_agents/**/big.md` over chartered S1, charterless S2, and a file directly in `sub_agents/` | `c04` | v1: OW clean, S2 + loose file nowhere. **v2: OW notice 2/2 (S2/big.md, sub_agents/big.md); S1 notice 1/1**; no double count | ✅ |
| L10 | W1: file directly in `sub_agents/` | `c13` | v1 nowhere / OW clean; **v2 OW notice 1/1** | ✅ |
| L11 | desk whose home is a sub-agent (`AGENTS/P/sub_agents/S`) | `c07` (S has foreign reads of `reg/f.md` and of charterless `S/sub_agents/T/g.md`) | v2: S notice 2/2 (both), P clean (correctly: both are S's). v1 missed T/g.md | ✅ |
| L12 | no prefix collision / degenerate charter | `c14` (`sub_agents_old/S/` with a CLAUDE.md), `c15` (0-byte CLAUDE.md) | 14: stays with OW in v1 and v2 (`sub_rel` has trailing `/`). 15: 0-byte charter counts as chartered in desk_home and v2 alike → S owns it | ✅ |
| L13 | W2: directories never print DOES NOT EXIST | `c06a` (`AGENTS/OW/adir/` trailing slash), `c05` (glob `AGENTS/OW/d*` matching only dirs), `c11` (symlink→dir row + broken-symlink row) | 06a: v1 `⛔ AGENTS/OW/adir … DOES NOT EXIST`; **v2 clean, 0 notices**; reader shows `◦ whole · directory`. 05: no notice v1/v2 (members are files only). 11: v1 printed `linkdir … DOES NOT EXIST`; **v2 skips linkdir**, keeps `broken.md` DNE — same as the reader's own `DOES NOT EXIST` defect | ✅ |
| L14 | live rc identical before/after; v2 changes nothing live today | 51 desks × {base,v1,v2} (`live/*.txt`); machine line diffed with the two new keys stripped; `cmp` v1 vs v2 bodies | rc identical 51/51 (NEXUS 1, STUE 1, RAV 2, CATO 2, rest 0); machine-line diffs base vs v2 = 0; **v1 vs v2 output byte-identical on all 47 desks compared**. Over-budget owners: BROCK `NEXUS_BRIEF.md` 34,568 B 106% and ZHAO 39,556 B 122%, both ← NEXUS:6. HANS 2 notices, 0 over (THRESHOLDS 22,120 B 68%). MARCO clean (0 READS rows mention `sub_agents`). CARL 1 notice (NEXUS_BRIEF 23%). Author's "43/43" reproduced | ✅ |
| L15 | `--fleet` and PROME explicit mode unchanged | `main([…,'--fleet'])` per build; `--agent PROME --require-manifest --charter-mode explicit` | fleet rc 1 all three, `cmp` base==v2 and v1==v2 byte-identical. PROME explicit rc 0→0, machine line identical | ✅ |
| L16 | opt-in flag on live | `--agent ZHAO/BROCK/HANS --owner-notice-blocking` (v2) | ZHAO rc 1, BROCK rc 1 ("1 foreign-read file(s) over budget"), HANS rc 0 ("0 …"). Labelled CANON QUESTION | ✅ |
| L17 | `base_root` vs `ROOT` mismatch in `under_home` can misattribute | `grep -rn foreign_reads --include=*.py` | `home_rel` is ROOT-relative while `rel` and the new W1 test use `base_root`. The only caller is `check_agent` → `foreign_reads(name)` (no `root`), so they are equal on every reachable path, live and in selftest (selftest sets `ROOT = t`). Pre-existing in v1; v2's W1 test uses `base_root` consistently with `rel` | ✅ (unreachable) |
| X1 | W1 fix = "exclude only when S resolves as a desk home" | `c03a` (S and S/sub_agents/T both chartered), `c08` (top-level `AGENTS/S/CLAUDE.md` shadows `AGENTS/OW/sub_agents/S/`), `c09` (S chartered under OW and OX) | **v1 and v2 alike: the 123% file appears in NO run and OW prints its clean line** (03a: OW, S, T all clean; 08: OW and S clean; 09: OW/OX clean, S rc 2). v2's test is CLAUDE.md presence; `desk_home` also requires a unique sub-agent match, no top-level shadow, and only one level of nesting. 0 live instances (no duplicate names, no collisions, no nested `sub_agents`, 15:02 inventory). Trial fix in scratch `v2x`: replace the isfile test with `os.path.normpath(desk_home(parts[0])) == os.path.normpath(os.path.join(ROOT, sub_rel, parts[0]))` → selftest 127/127; c08/c09 OW now notice 1/1; c03a moves to S (notice 2/1); c01/c02a/c04/c07 unchanged. `desk_home.ambiguous` has no reader, so the side-effect is inert | ⚠️ latent, same false-clean class as W1, not introduced by v2 |
| X2 | W2 / W6 classification still diverges from declared_reads on non-directory non-files and trailing-slash files | `c12` (FIFO), `c06b` (`AGENTS/OW/x.md/` naming a file) | 12: v1 said `DOES NOT EXIST`; **v2 now prints `✅ AGENTS/OW/pipe 0 B 0% … read whole by RD:9`** and counts 1 notice, while the reader's run shows `◦ whole — not cap-bearing`. Less wrong than v1, still contradictory; git cannot store a FIFO, so not reachable in a committed tree. 06b (v1=v2): owner gets 🟠 123% notice for `x.md`, reader's run says `declared whole read 'AGENTS/OW/x.md/' DOES NOT EXIST`, rc 1 (normpath vs raw join). 0 live cap-bearing rows end in `/` | ⚠️ cosmetic/latent (W6 residue) |
| X3 | selftest pass line names its legs | `--selftest` tail | v2 still prints `C1–C12 + N1–N8 owner notice` though N9–N10 run and are counted (127) | ⚠️ text only |

## W1 / W2 status
- **W1: FIXED** for the defect as written (charterless `sub_agents/<S>/`, and a file directly in `sub_agents/`): L6–L11, live MARCO shape included. The proposed remedy's stricter form ("only when desk_home(S) resolves to it") is not what v2 implements; the three shapes where the two differ keep the W1 false-clean behaviour (X1). All three are absent from the live tree.
- **W2: FIXED.** Directory rows (plain, trailing-slash, symlink-to-dir, glob-of-dirs) never print DOES NOT EXIST; "missing" now matches declared_reads' `exists` test, broken symlinks agree in both runs (L13). Remaining divergences are in X2.

## New defects introduced by v2
None that changes an rc, a machine line or a live output (L14: v1 vs v2 byte-identical on 47 desks; `--fleet` byte-identical). The only behaviour v2 newly produces that is still wrong is the FIFO row in X2 (a false DNE becomes a 0 B ✅ notice), unreachable in a git tree. X3 is a label the v2 edit left stale.

## Limits
- Fixtures are reviewer-built tempdirs with `m.ROOT` redirected; `class_history()` git lookups are not exercised in them (no CLASS row in them matches 0 files).
- Live runs import the patched copy in-process per desk with ROOT redirected to the live repo; they read live files at 15:04–15:05 ET and are a snapshot. I did not re-run consumer parsers (prome_gate, TERRY boot.py, HANS closeout) — the v1 read covered them and v2's live output is byte-identical to v1's, so their v1 verdicts carry.
- X1's trial fix (`v2x`) was run on selftest and seven fixtures only, not on live desks; it is a suggestion, not a verified replacement.
- W3–W8 (v1 read) were not re-graded; nothing in the v2 delta touches them.
