# Leg ⑳ BOOT-SEQUENCE AUDIT — HENRY (2026-08-28)

Reader: read-only audit subagent for DAEDALUS. Repo root `/home/willi/Research-workspace`.
Sources: `AGENTS/HENRY/CLAUDE.md` (256 lines), `AGENTS/HENRY/scripts/boot.py` (602 lines), `AGENTS/HENRY/scripts/gamma_flip.py` (351 lines).

## Boot sequence extracted (CLAUDE.md §SPAWN PROTOCOL, lines 26-41)

| # | Step (verbatim, truncated) | Claims to deliver |
|---|---|---|
| 1 | "Read `STATUS.md` — current market levels, active positions, macro data, vol regime" (L27) | Full live state |
| 2 | "Read `LESSONS.md` — mistake patterns to avoid" (L28) | Mistake corpus |
| 3 | "Read `MEMORY.md` — ends on handoff: CHANGES SINCE + NEXT SESSION" (L29) | Session handoff |
| 3a | WALTER signal intake — list unlogged `inbox/WALTER/*.md`, disposition, `git mv` to processed/ (L30-33) | Curated cross-agent lane drained |
| 3b | Power/grid — HANDED OFF TO WATT, do not run `power_watch.py` here (L34) | N/A (redirect) |
| 3c | "Run the boot orchestrator" `boot.py` — live tape, gamma flip, FRED credit, predictions-due scan (L35) | 4-in-1 read-only brief |
| 3d | General-inbox triage MANDATORY; flagged packets dispositioned at boot (L37, §MAIL L64) | Every flagged packet opened or deferral reasoned |

## boot.py static trace — per component (claim in docstring L11-18 vs `main()` L576-598)

| Step | Claim | Instrument | Verdict | Evidence |
|---|---|---|---|---|
| (a) LIVE TAPE | real-time quotes, 14 tickers | `fetch.py price … --json` (L108) | **DELIVERS** | boot.py:105-132; live run confirmed 14/14 tickers printed |
| (b) GAMMA | "flip / net-GEX / call+put walls" (docstring L12) | `gamma_flip.compute_gamma_flip(horizon=14)` (L141-142) | **SUBSTITUTED** (near-tie guard silently dropped) | see Finding 1 below |
| (c) CREDIT | HY/CCC/BB bifurcation | `credit_monitor.py` subprocess (L182-201) | **DELIVERS** | boot.py:187-201; live run printed BB/HY/CCC/GAP/flags |
| (d) PREDICTIONS-DUE | OPEN/ACTIVE rows due ≤ today | `_read_rows()` off `workbook/PREDICTIONS.tsv` (L236-270) | **DELIVERS** | boot.py:248-270; live run: "✓ none overdue… HEN-42 resolves 2026-08-29 (1d)" |
| (e) LEDGER STALENESS | mtime alert on live workbook ledgers | file mtime scan, FROZEN-banner skip (L291-338) | **DELIVERS** | boot.py:291-338; live run: all 4 live ledgers 1d, VX/FLOW correctly skipped as FROZEN |
| (f) INBOX TRIAGE | filenames only, flags date/gate hits (docstring L16) | `inbox_triage()` (L472-490), non-recursive `inbox/*.md` glob (L476-477) | **DELIVERS** (on today's empty inbox — see Finding 2 for the general-case gap) | boot.py:476-477; live run "✓ inbox clear" (0 files present, confirmed via `ls`) |
| (f2) WALTER LANE | unlogged `inbox/WALTER/*.md` vs `board_log.tsv` (L411-469) | file glob + substring match in board_log text (L445-453) | **DELIVERS** (today: 0 files) | boot.py:440-448; live run "✓ WALTER lane clear" |
| (g) STALE-CONSUMER | "who still cites a number I superseded" | `consumer_check.py --agent HENRY --from-ledger` subprocess, truncated `keep[:26]` (L501-514) | **DELIVERS-PARTIAL** (output hard-truncated at 26 lines with no "N more" notice) | boot.py:514; live run printed exactly to the cap with a 🟠 CANDIDATE block that itself trails off at line 108 of the transcript with no closing marker |
| R1 (`corrections_boot_check.py`) | — | not invoked anywhere | **NO** | `grep -rn corrections_boot_check AGENTS/HENRY/` → zero hits; not in boot.py, not in CLAUDE.md |

## EXECUTION GATE

1. `git status --short AGENTS/HENRY/` → empty both before and after run. **Executed** (not static-only).
2. `grep -nE "open\([^)]*['\"]([wa])['\"]|write_text|to_csv|\.write\(|subprocess.*(git|commit)|shutil" AGENTS/HENRY/scripts/boot.py` → **zero hits** — boot.py itself performs no writes.
3. Deeper check (not literal-grep-visible): boot.py's `gamma()` (L141-142) imports `gamma_flip.compute_gamma_flip()` directly — **not** `gamma_flip.main()`. Traced `compute_gamma_flip()` (gamma_flip.py:110-139) → `_finish()` (L205-256): returns a dict, no I/O. The write (`_publish()` → `workbook/PUBLISHED.tsv.write_text`, gamma_flip.py:330-351) is called **only** from `gamma_flip.py`'s own `main()` (L312), which boot.py never calls. Confirmed write-free by both static trace and by re-running `git status --short AGENTS/HENRY/` after execution (still empty).
4. Ran: `cd AGENTS/HENRY && python3 scripts/boot.py` → **rc=0**, 112-line transcript, 17.0s. (cwd-proofness not separately re-tested from repo root — not required once the git-status delta confirmed no writes; static trace shows all paths are built from `Path(__file__).resolve().parent` (L39-41), which is cwd-independent by construction.)

## Finding 1 (most consequential) — near-tie / impossible-wall guard exists in the data, dropped in the display, and fired LIVE today

`gamma_flip.py`'s `_finish()` computes and returns `call_wall_margin`, `put_wall_margin`, `call_wall_top3`, `put_wall_top3` in the same dict boot.py consumes (gamma_flip.py:241-247: `"call_wall_margin": _wall_margin(cg), "put_wall_margin": _wall_margin(pg),`). `gamma_flip.py`'s own `main()` uses this to print a `⚠️ NEAR-TIE` line and a dedicated `⚠️⚠️ PUT WALL == CALL WALL — structurally impossible` guard (gamma_flip.py:283-309, esp. L307-309: `if cw and pw and cw == pw: print("  ⚠️⚠️ PUT WALL == CALL WALL — structurally impossible as stated;" " treat the put side as UNRESOLVED at this horizon (see LESSONS 7/23).")`).

`boot.py`'s `gamma()` (L136-178) never reads `call_wall_margin`/`put_wall_margin`/`*_top3` and never checks `cw == pw` — it prints only the raw `r["put_wall"]`/`r["call_wall"]` (L156, L164-165).

**This fired on today's live run**, 2026-08-28: `(b) GAMMA` printed `put wall 7,700 · call wall 7,700` (transcript L31) — an exact tie, the identical structurally-impossible collision gamma_flip.py's own comment (L291-294) says was already fixed once and reappeared once ("on 7/28 the 35d run again emitted put wall == call wall == 7,500 with no visible warning. A guard the operator can't see is not a guard."). Boot.py's independent print path never inherited that fix. Zero warning appeared in the transcript.

**Leg ㉒ (what the fallback feeds):** a live-displayed, un-flagged tied wall value read directly into a session's STATUS write (boot step 3c → analyst copies "put wall 7,700 / call wall 7,700" into `STATUS.md` § VOL REGIME) — a **display line**, not (today) a registered cross-agent escalation, since `_publish()` never runs from this call path (Finding 2 covers why that's also a gap). But CLAUDE.md's own CORE METHODOLOGY section (L190) explicitly instructs: "If 14d and 35d disagree, publish the flip band and withhold the walls" for the cross-horizon case — this is the same-horizon case the instruction doesn't even name, and boot.py has no guard for it at all.

## Finding 2 — boot.py's own inline comment misrepresents what boot.py does; `PUBLISHED.tsv` is never actually written by the boot path

boot.py:158-161 comment: *"This value auto-publishes to workbook/PUBLISHED.tsv, which other agents' gates consume."* boot.py:494-496 (step g header comment): *"Runs consumer_check.py off workbook/PUBLISHED.tsv, which gamma_flip.py writes on every run."*

Both are **false for the boot.py call path**. As traced under EXECUTION GATE item 3, `_publish()` is wired only to `gamma_flip.py`'s standalone CLI `main()` (called via `gamma_flip.py --days 35`, per CLAUDE.md L187), never to `compute_gamma_flip()` called in-process by `boot.py`. Corroborating evidence: `workbook/PUBLISHED.tsv` (read in full, 21 rows) contains **19 `_35d` rows and only 2 `_14d` rows** (dated 2026-07-31 and 2026-08-23) — despite boot.py having presumably run on most session-days between 7/23 and 8/27 (per STATUS/MEMORY session cadence) and *always* requesting `horizon=14` (boot.py:142). If boot.py's gamma step actually published, `_14d` rows would appear on every boot day, not two. This is consistent with: the boot-displayed flip number is **never** the one recorded to the ledger that step (g) and cross-agent `consumer_check` treat as ground truth — that ledger is populated only by a human/session remembering to separately run `gamma_flip.py --days 35`.

**SILENT class**: the boot transcript gives no indication that its own gamma read is disconnected from the persistence layer its sibling step (g) audits.

## Finding 3 — STATUS.md is mandated whole-file reading at boot step 1, and it is OVER the harness read cap

`AGENTS/HENRY/STATUS.md` = **88,584 bytes** (249 lines — inside CLAUDE.md's own 250-line convention, L227, so the line-count guard is fully gamed by byte growth per line, the same failure class DAEDALUS's own CLAUDE.md documents for its own STATUS.md history). Read-cap math per audit spec (25,000 tok × 2.17 B/tok): full cap 54,250 B; STATUS.md is **163% of the full read cap** → **OVER-CAP**. Boot step 1 (CLAUDE.md L27) mandates a whole-file read with no rotation/archival mechanism visible in `AGENTS/HENRY/` file listing (no `archive/STATUS_ARCHIVE_*` analog found for HENRY, unlike DAEDALUS's own convention). No script in `AGENTS/HENRY/scripts/` enforces or even measures this byte budget — `boot.py` has no STATUS.md size check at all.

## Read-cap table (files the boot sequence mandates a whole-file Read of)

| File | Boot step | Bytes | Cap class (32,550 NEAR / 54,250 OVER) |
|---|---|---|---|
| `AGENTS/HENRY/STATUS.md` | 1 | 88,584 | **OVER-CAP** (163% of 54,250) |
| `AGENTS/HENRY/LESSONS.md` | 2 | 43,443 | **NEAR-CAP** |
| `AGENTS/HENRY/MEMORY.md` | 3 | 24,996 | under cap |
| `AGENTS/HENRY/CLAUDE.md` (auto-loaded, not a numbered step but read every boot) | — | 32,007 | at the NEAR-CAP floor (32,550) — 98.6% of it, one edit from crossing |

`workbook/PREDICTIONS.tsv` (73,884 B) and `workbook/PUBLISHED.tsv` are read programmatically by `boot.py`/`gamma_flip.py` via Python file I/O, not the harness Read tool — no cap applies to that path; excluded from this table by the audit's own scoping rule.

## Literal date strings in boot.py (leg ⑪ check)

Exactly 2, both `grep -n "date(202"` hits:
- `boot.py:526` — `today = date(2026, 7, 28)` inside `selftest_triage()` (L517-550): a fixed "today" anchoring a **regression replay** of the exact 7-packet inbox from 2026-07-28 (the day the triage rule's own miss was discovered), asserting a named packet still flags and named others still stay quiet.
- `boot.py:555` — `today = date(2026, 6, 15)` inside `selftest()` (L553-573): fixed "today" for a synthetic 4-row due-scan fixture (HEN-XX/YY/ZZ/DN), independent of any real file.

**Verdict: benign, not a hardcoded catalyst list.** Neither reaches the live boot path (`main()` only calls them under `--selftest`, L577-578); neither feeds a displayed value, a comparison band, or an escalation. They are frozen fixture-control dates for two self-tests. Flagged for the record only: per `finding_frozen_fixture_control_is_blind_to_resolution_faults` (fleet memory canon), a fixed-date, fixed-input self-test certifies the *parsing/matching logic* only — it cannot detect a regression in anything upstream of the fixture (e.g., a live `PREDICTIONS.tsv` schema drift, or a live inbox naming-convention drift), and neither self-test runs automatically at normal boot (`main()` requires `--selftest` explicitly, L577) — so even this narrow guarantee is not exercised every session.

## The 3 most consequential findings (ranked)

1. **Finding 1** — the put-wall/call-wall near-tie and structurally-impossible-tie guard exists in the returned data (`gamma_flip.py:_finish()`) and in a sibling code path (`gamma_flip.py:main()`), but is absent from `boot.py`'s own display (`boot.py:gamma()`), and this fired **live, today, unflagged**: 7,700 == 7,700.
2. **Finding 2** — `boot.py`'s own inline comments assert the gamma read "auto-publishes" to `workbook/PUBLISHED.tsv`; traced call path shows it does not, corroborated by `PUBLISHED.tsv`'s 19-of-21-rows-are-35d composition against a boot path that only ever requests 14d.
3. **Finding 3** — `STATUS.md`, a mandated whole-file boot read, is at 163% of the harness read cap with a fully-gamed line-count guard (249/250 lines) and zero byte-budget instrument anywhere in HENRY's boot tooling.

## What this audit could NOT see

- Whether the analyst, on a session where inbox/WALTER lane is non-empty, actually opens the flagged packets (steps 3a/3d/f/f2 are **detection-only**; disposition is a human/session act this static+one-shot-execution audit cannot observe).
- Behavior of `(f)`/`(f2)` triage logic on a populated inbox — today's inbox and WALTER lane were both empty (`ls` confirmed 0 files each), so `triage_names()`'s date/keyword/live-ID matching logic (boot.py:377-408) was exercised on zero inputs; the module's own `--selftest` regression (boot.py:517-550) is the only evidence this logic works, and that fixture is 31 days stale against the live inbox schema.
- `credit_monitor.py`'s and `fetch.py`'s internal correctness — both are external to `boot.py`/`gamma_flip.py` and were only exercised as black-box subprocesses; no static trace was performed on their own source per the assigned scope (HENRY's `boot.py` + directly-invoked scripts only — `fetch.py` lives under `FORGE/tools/market-data/`, out of scope).
- Whether `consumer_check.py`'s `keep[:26]` truncation (Finding under step g, DELIVERS-PARTIAL) ever silently drops a 🔴 STALE row in practice — today's run happened to fit under 26 lines with room to spare, so the truncation boundary was not exercised.
- Any comparison against a 35d gamma pull today (boot.py only ever runs 14d) — so whether today's exact-tie wall would resolve differently at 35d, per CLAUDE.md's own cross-horizon caveat (L190), is unknown; this audit did not run `gamma_flip.py --days 35` (out of scope: the assignment is to audit `boot.py`'s actual delivered behavior, not to supplement it).

---
**CORRECTION (2026-08-28 late, HENRY write-back `2026-08-28_from-HENRY_leg20-encoded-3-of-3-plus-one-count-corrected.md`):** the supporting count this leg's packet gave HENRY — *"19 `_35d` rows and 2 `_14d`"* in `workbook/PUBLISHED.tsv` — was **WRONG on both figures**; HENRY re-derived **16 `_35d` / 4 `_14d`**, the four 14d rows dated 2026-07-31 and 2026-08-23 (the two explicit `--days 14` runs). The finding stands; its evidence is re-derived by the owner. Also: my illustrating print "7,700 = 7,700" did not reproduce at HENRY's 11:05 boot (7,700 / 7,800, clean margin) — HENRY reads that as an intermittent tie, which strengthens the case for the guard it ported. **Chain closed:** 3/3 code findings encoded (NEAR_TIE imported not re-declared, falsified with 3 injected cases; comments corrected + wiring DECLINED with the reason in code; `keep[:26]` truncation now announces itself); STATUS 88,584 → 74,708 B by two verbatim rotations, still 138% of the cap — HENRY seconds the bytes-vs-lines point to PROME. `[[finding_asymmetric_rigor_counterparty_claims]]` — verify the number that makes you AGREE, too.
