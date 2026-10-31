FOURTH READ of the WQ-295 R2 cadence-wake gate fix · named further read authorized by Will 2026-10-31 14:41 ET (WQ-575, "yes go ahead") · independent reader · written 2026-10-31 15:00 EDT (from `date`)
Scope: the `clock-evaluated` fail-closed fix for the third read's ❌1, in the uncommitted diff of PROME/tools/spawn_list.py and PROME/tools/prome_gate.py. The declared residue in record § 9 is not re-graded.
Versions read (sha256 prefixes, unchanged 14:45 → 14:59 ET): spawn_list.py 07dab60947316021 · prome_gate.py 60641d5d6e41d72c · record adc366e868491cf9. HEAD moved twice during the read (56ddcfe0b, then 70046806f, both other desks' commits); the three tool files are unchanged at HEAD since 10/30, so the HEAD copies in scratch are the diff's base.
Read-only on the repository: I edited, staged, committed, stashed, checked out and pushed nothing. HEAD tool copies, fixtures, a fake `git` wrapper, scripts and outputs are under scratchpad/wq295-fourth/. The repo test suites ran with TMPDIR pointed there.

VERDICT: HOLD — 1 ❌ · 3 ⚠️
- The fix closes five of the third read's six ❌1 cases: V2, V3, V4, V6 and git failing for every desk now read UNKNOWN. It does NOT close V5 (`## ACTIVE` renamed), which is one of the third read's own cases. V5 still reads ✅ "CADENCE-DUE: none" because three WEEKLY desks outside ACTIVE still reach the clock test (DAEDALUS, SPECIAL; HANS and OTTO, TIER-2). clock-evaluated is therefore 3, not 0. Every damage that leaves 1–3 desks evaluable does the same (❌1).
- No new defect found. The fix only adds a not-ok branch. Dated rows, rc, `--open`, the slate and the DARK/ACTIVE/CADENCE-DUE naming are unchanged. The live ROSTER and every real day since 9/26 read without a false UNKNOWN. The token cannot be spoofed from a desk name or a reason.

════════ 1. Counterexamples ════════
Unless marked, inputs are frozen git objects: the 10/9 vintage 96622a349 (as-of 2026-10-09; the intact ROSTER owes C:MARCO, C:HAWK, C:SHADE) and HEAD 56ddcfe0b (as-of 2026-10-31). Each run is the real CLI with stdout+stderr merged, as run_script does, fed to the working-tree summarize_spawn_list. Header figures are clock-evaluated / CANNOT-EVALUATE.
| # | Probe | Observed | Result |
|---|---|---|---|
| R1 | the third read's V2 (a `## ` heading above the desk table); the file is byte-identical to its fixture (`cmp`) | 0 / 40 (10/9), 0 / 43 (10/31) → "cadence UNKNOWN", ok False | HELD |
| R2 | V3 (desk table moved below `## Transmission chain`) | 0 / 40, 0 / 43 → UNKNOWN | HELD |
| R3 | V4 (desk-table rows deleted, header kept) | 0 / 40, 0 / 43 → UNKNOWN | HELD |
| R4 | V5: only `## ACTIVE (34)` renamed `## LIVE DESKS (34)`; the file is byte-identical to the third read's fixture | 10/9: 3 / 33, rc 0, ok TRUE, "CADENCE-DUE: none · UNREACHED: CREED · cadence CANNOT-EVALUATE: CATO, RAV, AEOLUS, …" (33 names). The three owed wakes are gone. 10/31: 3 / 34, ok TRUE. The evaluated three are DAEDALUS, HANS and OTTO (VERIFIED: read_cadence ∩ roster_classes on the V5 file) | FAILED → ❌1 |
| R5 | V6 (desk cells written as links) | 0 / 75, 0 / 80 → UNKNOWN | HELD |
| R6 | git failing for every desk (P16), done for real: a fake `git` first on PATH fails every `git log --grep=^DESK…` with rc 128; PROME-only DOCKET, empty GATES | rc 0, 0 / 40 → UNKNOWN. With the real HEAD DOCKET/GATES: rc 2 and UNKNOWN | HELD |
| R7 | A16 regressions: heading renamed (`*`), empty ROSTER file, ROSTER path missing | 0 / 1 → UNKNOWN in all three, and the dated rows still print | HELD |
| P1 | V5b: ACTIVE, TIER-2 and SPECIAL headings all renamed (the form A17 tests) | 0 / 35, 0 / 37 → UNKNOWN | HELD |
| P2 | V5c: ACTIVE and TIER-2 renamed, SPECIAL kept (DAEDALUS survives) | 1 / 36, 1 / 38 → ✅ "CADENCE-DUE: none" | FAILED → ❌1 |
| P3 | V5d: `## 🟢 ACTIVE (34)` (an emoji prefix defeats `startswith("ACTIVE")`) | 3 / 33, 3 / 34 → ✅ | FAILED → ❌1 |
| P4 | V7 / V8: a `## ` heading inserted after the 1st / 2nd desk row | 1 / 39 and 2 / 38 (10/9); 1 / 42 and 2 / 41 (10/31) → ✅ | FAILED → ❌1 |
| P5 | V10: desk table truncated to its first row | 1 / 39, 1 / 42 → ✅ | FAILED → ❌1 |
| P6 | git failing for every desk except DAEDALUS / except DAEDALUS and HANS (fake git, PROME-only rows, rc 0) | 1 / 39 and 2 / 38 → ✅ "CADENCE-DUE: none · cadence CANNOT-EVALUATE: …" | FAILED → ⚠️1 |
| P7 | V9 (every `WEEKLY` written as `WEEKLY (floor)`) · V12 (desk cells bolded, which read_cadence skips) · V13 (a prose line quoting "### DESK CADENCE" above the class tables) | 0 evaluated in each → UNKNOWN | HELD (V13 would have read green before the fix) |
| P8 | Minimal fixture with WEEKLY desks in ACTIVE (MARCO, HAWK, SHADE, past clock), TIER-2 (HANS) and SPECIAL (DAEDALUS) — scripts/fixture_v5.py | intact: 5, CADENCE-DUE C:MARCO, C:HAWK, C:SHADE, not-ok · only ACTIVE renamed: 2, ✅ "CADENCE-DUE: none · cadence CANNOT-EVALUATE: HAWK, MARCO, SHADE" · all three renamed: 0, UNKNOWN | FAILED → ❌1 |
| P9 | The selftest's own A17 fixture, captured during the selftest run, with only ACTIVE renamed | clock-evaluated 0: its one non-ACTIVE launchable desk (ABSENT, TIER-2) has no cadence row, and it has no SPECIAL section. The suite cannot tell V5 from V5b | FAILED (coverage) → ⚠️2 |
| S1–S2 | "clock-evaluated 9" inside a CANNOT-EVALUATE reason or an UNREACHED reason, header at 0 | UNKNOWN. The token is read only from the header line, which carries numbers only | HELD |
| S3–S7 | Header token duplicated (0 then 7), missing, non-numeric, "00", "-5" | UNKNOWN in all five (the first match wins; `\d+` refuses a sign) | HELD |
| S8 | Header not at the start of its line | "cadence block MISSING", ok False | HELD |
| S9–S10 | Block printed twice: 0 first → UNKNOWN; 5 first, then 0 → ✅ | Not producible: render prints one block per process, and run_script opens a fresh log per run (mode "x") | HELD / note |
| S11 | In-process: clock-evaluated 1 with 40 CANNOT-EVALUATE | ✅ | FAILED → ❌1 (the class) |
| S12–S16 | A C: row with evaluated 9 → not-ok naming C:HANS · header 1 with the C: row deleted → UNKNOWN · `*` with a non-zero count → UNKNOWN · evaluated 1 and nothing named → ✅ · DARK row with evaluated 0 → DARK id still named, UNKNOWN appended | as stated | HELD |
| F1 | LIVE, the gate's own call (`spawn_list.py --horizon 0`, working-tree inputs, 14:42 ET) | clock-evaluated 28 · CADENCE-DUE 0 · UNREACHED 4 · governed 0 · CANNOT-EVALUATE 3 → ✅ "CADENCE-DUE: none · UNREACHED: CREED, FLG, RED, WAL · cadence CANNOT-EVALUATE: CATO, CYPHER, RAV" | HELD |
| F2 | 38 real days, 9/24–10/31: each day's last commit, `--as-of` that day — scripts/hist.py | clock-evaluated is 0 only on 9/24 (no desk had declared yet; 39 named, a true UNKNOWN). 9/25: 10 evaluated / 28 named → green. 27 from 9/26 and 28 daily from 9/28. No "cadence UNKNOWN" from 9/25 on. Days with CADENCE-DUE read not-ok with their ids (for example 10/2 C:MARCO, 10/20 C:HAWK) | HELD |
| F3 | A past-clock governed desk plus a within-clock MONTHLY desk | evaluated 2: both are counted, so a fully governed fleet is not a false UNKNOWN | HELD |
| F4 | A fleet with no WEEKLY/MONTHLY desk | evaluated 0 at every boot: a permanent UNKNOWN. No instance (28 WEEKLY today) | note |
| N1 | `--selftest` / `--cadence-selftest` / `--cadence-wake-selftest` | 11/11 · PASS · PASS (31 ✅) | HELD |
| N2 | Dated part and rc, HEAD copy against the working tree on the same git objects: 5 (inputs, as-of) pairs × h0/h1/h3 × tsv/non-tsv = 30 runs | Byte-identical after removing the 4–7 cadence-block lines and the READ-footer sentence; rc identical in all 30 | HELD |
| N3 | `--open` human / `--tsv` / `--json` × 2 vintages | identical, rc 0/0 | HELD |
| N4 | `spawn_slate.py --stdout` × 6 (h0/h1; `--orch-log` passed as the same git object; the stamp normalized) | identical, rc 0/0 | HELD |
| N5 | summarize_spawn_list on 8 real bodies (5 at rc 0, 3 at rc 1 with DARK rows) against HEAD's summarize | HEAD's summary is an exact prefix of the new one in all 8. DARK/ACTIVE ids identical. The CADENCE-DUE ids on the line equal the body's C: rows. ok = HEAD ok ∧ cadence green. The two "FAILED" lines in out/parity.txt are my checker's trailing-space artifact, re-checked by printing both summaries (scripts/summ_diff.py) | HELD |
| N6 | Repo suites | fail_closed 15/15 · covered_L368 26 OK · spawn_slate 37 OK · L455 attribution 22 OK · docket_open_query 9 OK · open_export 14 OK · presence_reader_contract PASS · test_gate_orch_summary c13 + c17 PASS (a pytest shim; pytest is not installed) | HELD |
| N7 | Runtime of the gate's call | 2.07 s (0.08 s at HEAD; about 35 extra `git log` calls) against run_script's 120 s timeout | HELD |

════════ 2. Findings ════════
❌1  The fix reads UNKNOWN only when ZERO desks reach the clock test, so the third read's V5 and every damage that leaves a few desks evaluable still read ✅ "CADENCE-DUE: none".
  claim → record § 9: "The reader's proposed fix (UNKNOWN when no WEEKLY/MONTHLY desk reaches the clock test) is IMPLEMENTED … and TESTED by PROME (A17: …; live: … three damaged ROSTERs UNKNOWN)". § 7 A17 says a "class-headings-renamed … ROSTER reads UNKNOWN". The summarizer's comment reads "zero desks reached the clock test = nothing checked".
  artifact → prome_gate.summarize_spawn_list returns UNKNOWN on `int(em.group(1)) == 0` only. cadence_wakes counts any one desk that reaches the clock. A desk outside the damaged part of ROSTER keeps the count positive: when only `## ACTIVE` is lost, DAEDALUS (SPECIAL), HANS and OTTO (TIER-2) are still evaluated. The third read's own proposed fix had the same blind spot, because it assumed V5 evaluated zero desks. It also asked to "Pin V2–V6 and P16 as fixtures", and V5 was not pinned.
  command → scripts/battery.py (R4, P2–P5), scripts/fixture_v5.py (P8), scripts/probes.py (S11).
  observed → V5 on 10/9: rc 0, ok True, CANNOT-EVALUATE 33. The intact ROSTER owes C:MARCO, C:HAWK and C:SHADE that day, and the ✅ line drops them into a list of 33 names (the usual list has 2–3). V5c, V5d, V7, V8 and V10 behave the same way at 1–3 evaluated. Only V5b, with all three launchable headings lost, reads UNKNOWN. Severity follows the third read's standard: in its V2–V6 the desks were also named on the ✅ line, and it graded them ❌.
  proposed change → key the UNKNOWN on coverage, not on zero. Both options below use only figures the block already prints:
    (a) UNKNOWN when CANNOT-EVALUATE > clock-evaluated. On these runs it trips on every failing case: V5 33>3 and 34>3, V5c 36>1 and 38>1, V5d 33>3, V7 39>1, V8 38>2, V10 39>1, partial git 39>1 and 38>2. It stays green live (3<28) and on every real day from 9/26 (at most 5 named against at least 27 evaluated). It would have read UNKNOWN on 9/25 (28>10, the pre-rollout day), which is arguably true. A damage that leaves more than half the desks evaluable still reads green, with the names on the line; declare that.
    (b) Key on the cause: any cadence-table desk "not launchable (ROSTER class absent)" (0 on all 38 real ROSTER vintages, 31–36 under V5/V5c/V5d) or any "git log FAILED" (the dated half's own rule) → UNKNOWN. Table truncation (V7/V8/V10, "no cadence row" in bulk) still needs (a) or a count.
    Whichever option is taken, pin V5 with WEEKLY desks also under TIER-2 and SPECIAL (the current fixture cannot express it), plus V7 or V10 and a partial git failure. Any such fix lands after this read and is unreviewed. WQ-575's row says a ❌ here means revert to HEAD and carry to L903.

⚠️1  A partial git failure leaves the cadence half green, while the dated half reads the same failure as UNKNOWN.
  claim → Liveness's "FAIL CLOSED" comment, and the render footer: "A failed check is not evidence a desk is dark". On the dated half, a failed `git log` makes the row UNKNOWN and rc 2.
  artifact → cadence_wakes names "git log FAILED" as CANNOT-EVALUATE, and the summarizer ignores it unless clock-evaluated is 0.
  command → scripts/battery.py § C (fake git with FAILDESKS=ALLBUT:DAEDALUS and ALLBUT:DAEDALUS,HANS; PROME-only DOCKET).
  observed → ✅ at clock-evaluated 1 or 2, with 38–39 desks named. This bites only when no failing desk owns a dated row in the horizon; otherwise rc 2 already makes the line not-ok. git failures are usually global, and a global failure now reads UNKNOWN. Low plausibility.
  proposed change → make any "git log FAILED" entry a cadence UNKNOWN (fold this into ❌1's change, option b).

⚠️2  A17 and § 9 state the tested scope more broadly than the tests cover.
  claim → § 7 A17: "fixtures: class headings lost … live: … class-headings-renamed … reads UNKNOWN". § 9: "three damaged ROSTERs UNKNOWN".
  artifact → the selftest's `nohdr` renames ACTIVE and TIER-2 in a fixture with no SPECIAL section, whose one TIER-2 desk has no cadence row. That is the "every launchable heading lost" form.
  command → scripts/selftest_fixture_v5.py.
  observed → the selftest fixture with only ACTIVE renamed gives clock-evaluated 0, so the suite passes whether or not the V5 failure exists. Live, V5b reads UNKNOWN and V5 reads ✅.
  proposed change → name the variant tested in A17 and § 9, and carry V5 as open (❌1).

⚠️3  The third read's ⚠️3 and ⚠️4 are neither fixed nor declared.
  claim → PROME/CLAUDE.md § Review budget: after a read, every ⚠️ goes into a declared residue block.
  artifact → record § 9's "Third read" paragraph declares ⚠️ T1 and ⚠️ T2 only. Two items are missing:
    · The third read's ⚠️3: summarize_spawn_list's docstring (prome_gate.py:1700) still says "ok follows rc exactly as before". That is false now: at rc 0, ok is False when CADENCE-DUE exists, the block is missing, or the cadence state is UNKNOWN. Line 1663 is summarize_orch_closeout's own docstring and is still true there.
    · The third read's ⚠️4: COVERED rows due +1 to +14 days are discounted by the wake but printed nowhere at horizon 0. It appears nowhere in § 9.
  command → read of record § 9 · `grep -n "ok follows rc" PROME/tools/prome_gate.py`.
  proposed change → declare both in § 9, or fix the one-sentence docstring.

════════ 3. The four questions ════════
1. The third read's ❌1 cases: V2, V3, V4 and V6 read UNKNOWN on both vintages. Git failing for every desk reads UNKNOWN (rc 0 with PROME-only rows; rc 2 plus UNKNOWN with the real DOCKET). V5 still reads ✅ GREEN.
2. Lies:
   · Green over a partial evaluation: yes, in V5, V5c, V5d, V7, V8, V10 and a partial git failure.
   · Token missing, duplicated, non-numeric or spoofed through a name or reason, header off its line start, block printed twice: each fails closed or cannot be produced.
   · False UNKNOWN on a healthy ROSTER: none (live 28 ✅; 38 real days).
3. Nothing else moved: dated rows and rc (30 runs), `--open` (6), the slate (6), the summary's DARK/ACTIVE/CADENCE-DUE naming (8 bodies) and nine test suites all hold.
4. The fix does not resolve the third read's ❌1 completely (V5 is still open). It introduced no new defect.

════════ Evidence (scratchpad/wq295-fourth/) ════════
scripts/variants.py (ROSTER damage variants) · scripts/battery.py → out/battery.txt + out/<case>.txt (the full body of each run) · scripts/probes.py → out/probes.txt · scripts/parity.py → out/parity.txt · scripts/summ_diff.py · scripts/dark_parity.py · scripts/hist.py → out/hist.txt · scripts/fixture_v5.py · scripts/selftest_fixture_v5.py · fakebin/git (fails `git log --grep` per $FAILDESKS; every other call passes to /usr/bin/git) · head/tools/{spawn_list,spawn_slate,prome_gate}.py (HEAD copies, for parity only) · fx/r1009_V*.md and fx/rH_V*.md (variants), fx/docket_prome_only.tsv, fx/gates_empty.tsv · out/selftest-*.txt, out/t_*.txt (suite logs) · shim/pytest.py
