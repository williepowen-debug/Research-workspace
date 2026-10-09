# ACCEPTANCE — DOCKET L546: float-tie class in FORGE market-data classification (written BEFORE the edit)

**Owner:** PROME (FORGE owner) · **Class:** DOMAIN (WQ-379 (b2), Will 2026-10-04) — a Will-facing dashboard surface, so **consequential**: an independent reader devises ≥1 counterexample before this is called fixed (WQ-229). · **Written:** 2026-10-08 22:25 ET (from `date`), prome-07b. · **reads: 1** (read 1 consumed 22:45 ET; see § reads).

## The defect (two FORGE instances; the intake twin is WALTER's tested patch, landed separately)

1. `FORGE/tools/market-data/dashboard.py:226` converts FRED percent to bp (`float(v) * mult`, `"multiply": 100` on HY OAS and CCC OAS in `config.py`) and `config.py::classify` compares the raw float against whole-bp band edges (`value < y[0]` / `value < r[0]`). In Python, 143 of the 1,499 hundredths 0.01…14.99 do not multiply exactly by 100 (DOCKET L546, measured 10/1). A print exactly ON an edge can land on either side by binary representation.
2. `FORGE/tools/market-data/vix_futures.py:157-164` classifies the UNROUNDED M1/M2 steepness percent against `AVG_STEEPNESS` 5.6 / `COMPLACENCY_THRESHOLD` 8.99 while publishing `round(x, 3)`; DAEDALUS's census: 8 of 8 reachable exact-5.6% pairs mis-land (e.g. `(13.20-12.50)/12.50*100 = 5.599999999999994` prints BELOW_AVG at exactly average). VIOLET's board prints that label.

**Direction matters (the row's premise vs this instrument's operator).** `classify()` uses `<` (a print AT the edge belongs to the worse zone). An UPWARD mis-multiply (1.10→110.00000000000001, 2.20→220.00000000000003 — LIQUID's cases) lands on the correct side under `<`; a DOWNWARD one (1.13→112.99999999999999, 2.01→200.99999999999997) lands in the milder zone — the false ALL-CLEAR direction. LIQUID's letters use strict `>` and fail in the other direction. The failing-first cases for FORGE are therefore the DOWNWARD ties; the 110/220 cases are kept as regression with the reason stated.

## Acceptance conditions (properties, not the symptom)

- **AC1 — on-edge equals the letter.** For every `SERIES` entry declaring `multiply`, a converted value that is mathematically ON a band edge classifies into the zone the band letter assigns to that edge (higher_worse: the worse zone; lower_worse: per its `>`/`>=` letters), regardless of binary representation. Mechanism: `classify()` rounds the value to the series' declared `precision` (decimal places of the converted unit) before comparing.
- **AC2 — missing precision fails LOUD.** A series declaring `multiply` without `precision` is a declared defect: the `config.py` self-test fails naming the series, and `dashboard.py` flags the entry (`⚠precision undeclared`). `classify()` never invents a precision — with none declared it compares the raw value (unchanged behaviour), so nothing is silently rounded.
- **AC3 — the label matches the published number.** `compute_steepness` classifies the SAME 3-dp value it publishes as `steepness_pct`, for both `strict` and `adjusted`; label and number are never on opposite sides of an edge.
- **AC4 — no live grade moves.** At every current FORGE band edge (HY 265/280 · CCC 900/1000) prints ON, 0.01 pct below and 0.01 pct above the edge classify identically before and after the change (today's edges convert exactly — the fix must not change them).
- **AC5 — the old code is seen to fail first (CHECK_STANDARD).** Synthetic edge 113 fed `1.13*100` and edge 201 fed `2.01*100`: old code → milder zone (wrong); new → the edge's zone. Steepness `(13.20-12.50)/12.50*100`: old → BELOW_AVG; new → NORMAL_TO_ELEVATED. Each test is run against the pre-fix function to confirm it fails, then against the fix.
- **AC6 — not a threshold move.** No band edge, operator, letter or consequence changes; `git diff` of `config.py` touches only the new `precision` fields, `classify()` and the self-test.

## Neighbours (CONSIDER all five; justified N/A is an answer)

| # | Category | Disposition |
|---|---|---|
| 1 | Ordinary | HY 3.09 → 309 → red (≥280); CCC 12.29 → 1229 → red; KRE (no multiply) unchanged. Tested. |
| 2 | Overlap | a value converted twice: rounding at the declared precision is idempotent (`round(round(x,p),p) == round(x,p)`); `vix_futures` publishes AND classifies the same rounded value, so there is no second conversion path. Tested (idempotence). |
| 3 | Wrong owner | RED / LIQUID / REGINALD letters own their own tie handling (LIQUID fixed three instances 9/29; DAEDALUS packeted 14 owners 10/8); this fix must not be cited as fixing any desk letter. N/A by scope: the diff touches no `AGENTS/` path (`git diff --name-only -- AGENTS/` is empty; no test asserts this — read 1 ❌24 corrected the earlier claim that one did). ⚠️ read 1 (claim 25): LIQUID's `hy_oas_watch.py` IMPORTS `config.classify` (:167) and so inherits the rounding — harmless at today's exact edges; FYI packet to LIQUID 10/8 22:45 ET. |
| 4 | Missing information | `multiply` without `precision` → self-test fails + dashboard flag (AC2). Tested. |
| 5 | Concurrent activity | the intake-lane twin (`Research-Intake/scripts/fetch_fred.py:182`) does its own pct→bp conversion; WALTER's patch rounds to integer bp — the same convention as `precision: 0` here, so an exact edge print is read identically by both lanes. Tested as agreement on the 1.13 / 2.01 / 2.70 / 3.09 inputs (pure arithmetic, no lane read). |

## Test file

`PROME/tools/tests/test_l546_float_tie.py` — imports the live modules by path (the modules under test), builds synthetic series defs for the failing-first cases, iterates `SERIES` dynamically for AC4 (no pinned edge values), and includes the pre-fix reference implementation inline so AC5's "fails first" is executable, not remembered. Run: `python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_l546_float_tie.py` (pytest is not installed in either interpreter — read 1 ❌28 corrected the earlier command).

## Completion states (never merged)

- IMPLEMENTED: 2026-10-08 (prome-07b) — `config.py` (`precision` on HY OAS · CCC OAS · Cushing; `undeclared_precision()`; `_edge_value()`; one line in `classify()`; self-test additions + `import sys`), `dashboard.py` (the flag, at the common point before classify), `vix_futures.py` (the two `classify(round(x, 3))` calls + a comment). Commit → `git log -1 -- FORGE/tools/market-data/config.py`.
- TESTED: `python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_l546_float_tie.py` → 15 OK (measured `grep -c 'def test_'` = 15); `python3 FORGE/tools/market-data/config.py` self-test rc 0. **Fails-first (AC5):** the same file against the UNFIXED tree → 7 failures + 1 error with both `TestAC5_OldCodeFailsFirst` cases PASSING. **The AC2 guard's first catch:** `Cushing` (`multiply: 0.001`, EIA thousand barrels → M bbl) — a third converted series the DOCKET row had not enumerated; precision 3 declared (reader claim 31: 12 cached EIA observations all whole thousand barrels; beyond the cache an inference).
- INDEPENDENTLY VERIFIED: **the `classify()` rounding and the steepness label** — read 1 (coldreader, Opus, started 22:31:29 ET, ledger `scratchpad/l546/reads/read_1.md`): **SOUND WITH CAVEATS — 37 claims: 21 ✅ · 13 ⚠️ · 3 ❌; 7 counterexamples of its own**, incl. the real before/after at every current edge ±3 units across all three converted series (0 grade changes) and a lower_worse edge tie (old green → new yellow, the letter's zone). Direction measured: no current edge mis-multiplies in either direction; in the lower_worse branch the false all-clear is an UPWARD error at the upper edge and every Cushing-scale error is upward (4,008 up, 0 down) — the fix covers it, the direction paragraph above did not say so.
- STILL UNRESOLVED (disclosed, never promoted): the three ❌ were fixed AFTER the read and are UNREVIEWED — ❌11 the dashboard flag lived only in the `fred` branch, so Cushing (EIA) went unflagged → moved to the common point before classify; ❌24 and ❌28 = the two wording corrections above. The 13 ⚠️ are declared below; the class siblings are DOCKET L648.
- Intake twin: LANDED — Research-Intake `6ae4c6c` (WALTER's patch, `git apply --check` clean at 75c6435, negative control re-run at landing: 1.13 → "113"), pushed to origin/main 2026-10-08. Reader claim 26: all 1,499 hundredths agree numerically with FORGE's rounding; the text differs ('113' vs '113.0') and the lane reads it back with `float()`. The `>=280` vs LIQUID's `>280` strict wording stays the open CATO item (HEARTBEAT_COLD, 9/22).

## Declared residue — read 1's ⚠️, not fixed in this episode (WQ-178: fix ❌ only after a read)
1. (5) "8 of 8 reachable exact-5.6% pairs" — on a 0.05-tick grid the reader counts 5 of 10 landing below; "reachable" is undefined in this file. Carried as DAEDALUS's census figure, not re-derived.
2. (6) VIOLET's board printing the label — not checked by the reader (outside the file's scope).
3. (8) The direction paragraph omits the lower_worse branch (covered by the fix; stated in INDEPENDENTLY VERIFIED above).
4. (13) `undeclared_precision()` treats `precision: None` as declared (compares raw) while `multiply: 1` fails the self-test but draws no dashboard flag — asymmetric guards → L648.
5. (15) Classifying the published 3-dp steepness moves the EFFECTIVE edges to 5.5995 / 8.9895 on 4-dp VX settles (20,349 of 28,582 history rows carry 4 dp); 0 of 6,648 historical pairs change label. Declared; VIOLET informed via L648's owners cell.
6. (17) The AC4 test runs the old function on the already-ROUNDED value — near-circular; the reader ran the true before/after (0 changes). Test tightening → L648.
7. (21) AC6's config.py list omitted `import sys` and the two helper functions; all serve the named purpose. Corrected in IMPLEMENTED above.
8. (23) `detect_transitions` hysteresis compares RAW bp deltas against the 5 bp buffer — 53 exact 5 bp HY moves in 2.00–8.00% read as 4.999999999999972 and are suppressed; none crosses 265/280 today → L648 (a).
9. (25) LIQUID's `hy_oas_watch.py` imports `config.classify` → inherits the rounding (harmless today) — FYI packet sent.
10. (30) The AC3 tests expect the bare label; after 2026-12-16 the `UNVERIFIED` suffix appears and they fail with no code change → L648.
11. (33) A hypothetical 3-decimal FRED print of 2.795% rounds half-to-even to 280 (letter: yellow) — unreachable while FRED publishes 2 decimals; nothing checks for it. Declared.
12. (34) The stored entry value, JSONL log and state file still hold the unrounded float while the display shows the rounded bp → L648 (b).
13. (35) `PROME/tools/fleet_dashboard.py` `_band_class`/`_inside` does its own raw comparison (Cushing at 25.0: "ok" there, "yellow" in classify) → L648 (c).

## reads
- read 1 — 2026-10-08 22:31:29 ET start, coldreader (Opus), spawned by prome-07b; consumed 22:45 ET; verdict SOUND WITH CAVEATS (37 claims 21/13/3; 7 counterexamples). ❌ fixed post-read (unreviewed); ⚠️ declared above. Episode: no plan read (small self-contained repair; the reader was the consequential-class requirement); no third read — the ❌ fixes changed no rule's meaning (WQ-178).
