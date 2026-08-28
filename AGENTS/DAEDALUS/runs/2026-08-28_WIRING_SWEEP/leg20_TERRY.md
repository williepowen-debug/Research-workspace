# Leg ⑳ — BOOT-SEQUENCE AUDIT: TERRY

**Method:** PAT-125 (delivered content vs claim). Static trace of `AGENTS/TERRY/CLAUDE.md` §BOOT + every script it invokes, then live execution of `scripts/boot.py` (write-free, network-free by static check) on today's real state. Repo root `/home/willi/Research-workspace`. All work confined to this leg file — no edits to TERRY.

## Execution transcript

- Gate check: `git status --short AGENTS/TERRY/` → clean (empty) before run.
- `grep` for writes in `boot.py`: only `subprocess.check_output`/`subprocess.run` (git commands + `ledger_sweep.py`/`snapshot.py` subprocess calls); no `open(...'w')`, no `write_text`, no `to_csv`. `ledger_sweep.py`'s only two `subprocess.run` calls (`ledger_sweep.py:991,1011`) are `git log ...` (read-only); its `write_text` calls (`:1282-1287`) are inside `--selftest`'s `tempfile` sandbox only. Default `boot.py` invocation takes no `--snapshot` arg, so `snapshot.py` (which does live network fetch) is never reached. **Cleared to execute.**
- Ran `cd /home/willi/Research-workspace && python3 AGENTS/TERRY/scripts/boot.py` from repo root. **rc=0.** stderr empty. Full stdout captured.
- Post-run `git status --short AGENTS/TERRY/` → still clean. No checkout needed.

## Step table

| Step | Claim (CLAUDE.md) | Instrument | Verdict | Evidence |
|---|---|---|---|---|
| 1 | git status/diff/ahead-behind | `boot.py sh()` git calls | DELIVERS | `boot.py:225-227`; live: `## master...origin/master [ahead 2]` |
| 2 | "Read AGENTS/TERRY/STATUS.md" (full manual read) | harness Read tool | **DELIVERS-PARTIAL / OVER-CAP risk** | `CLAUDE.md:142`; `STATUS.md` = 90,236 B — see Read-cap leg below |
| 3 | Read RISK_RULES.md | manual read | DELIVERS | `CLAUDE.md:143`; file = 36,857 B, under cap |
| 4 | Read RISK_SCORING.md before sizing/edge claims | manual read | DELIVERS (content) / **SILENT (automated check)** | `CLAUDE.md:144`; file exists, 10,134 B, but absent from `boot.py`'s `REQUIRED` file-health list (`boot.py:22-27`) — the one automated instrument that could catch its disappearance doesn't watch it |
| 5 | Run `boot.py` read-only boot card | `boot.py run()` | DELIVERS | rc=0; full stdout below |
| 5b | paper-book mark + STALE flag via `paper_book_mark.py` | separate invocation, NOT called by `boot.py` | **CANNOT-JUDGE (not executed — see below)** / static trace DELIVERS-as-designed | `CLAUDE.md:150`; `paper_book_mark.py:434-491` |
| 6 | Read CHART_OPTIONS_WORKFLOW.md | manual read | DELIVERS | file exists, 7,026 B |
| 7 | Read TRADE_CARD_TEMPLATE.md | manual read | DELIVERS | 4,418 B; note `TRADE_CARD_TEMPLATE_FIRE.md` (cited in CONTRACT block, `CLAUDE.md:12`) exists (4,874 B) but is in neither the numbered BOOT list nor `boot.py REQUIRED` |
| 8 | Read TRADE_BOOK.md + SETUPS.tsv if touching existing trades | manual read | DELIVERS | 35,886 B / 95,253 B |
| 9-13 | Conditional/manual (position intake, price pulls, sizing, chain parse) | manual/on-demand | CANNOT-JUDGE (not triggered by a plain boot; no ticker/task given) | `CLAUDE.md:154-160` |
| — | Setups block: "actionable/open rows" | `boot.py setups()` | DELIVERS | live: 16 open rows printed with full annotated context (`_tsv_rows`/`_tsv_shape_errors`, `boot.py:83-94`) |
| — | Signals block: active rows + **21d anti-rot stale flag** | `boot.py signals()` | **SUBSTITUTED / SILENT — see Finding #1** | `boot.py:246-287` |
| — | Inbox: unprocessed packets | `boot.py inbox_report()` | DELIVERS | live: 5 unprocessed flagged, one marked ⚠️ IMMEDIATE-pattern-eligible (none matched today) |
| — | Ledger sweep advisory | `boot.py ledger_sweep_summary()` → subprocess `ledger_sweep.py` | DELIVERS | live: 1 real, present-day finding — `SIGNALS.tsv:22` future-dated stamp (see below) |
| — | STATUS head (18 lines) | `boot.py latest_status_head()` | DELIVERS (by design — deliberate partial read via Python, not the harness Read tool) | `boot.py:171-175,298-300` |

## Finding #1 (most consequential) — the 21-day anti-rot stale flag is SILENT for exactly the status vocabulary it was built to cover

`boot.py`'s own comment (`boot.py:29-30`) promises: *"Active rows older than [21] days get a re-verify / retire flag at boot (anti-rot)."* `_is_active()` (`boot.py:253-255`) was deliberately widened on 2026-07-30 (comment at `boot.py:248-252`) to catch rich status strings by **substring** match (`"LIVE" in st or "DECAYING" in st`) — explicitly because the old exact-match set was silently dropping rows like `SHAPE-LIVE / LEVELS-STALE`. But the **staleness flag itself** (`boot.py:278-281`) still gates on the **old exact-match set**:
```python
if st in {"LIVE", "LIVE-WEAK"} and days > SIGNAL_STALE_DAYS:
    flag = "  ⚠ STALE >21d — re-verify or retire"
elif st == "DECAYING" and days > SIGNAL_STALE_DAYS:
    flag = "  ⚠ decaying >21d — reconfirm before use"
```
So a row can correctly count as "active" (inclusion widened) while its retirement warning never fires (flag logic not widened) — the exact split-brain the 7/30 fix was supposed to close on one side only.

**Verified live, today, on 3 of 12 active `SIGNALS.tsv` rows, all well past the 21-day bar:**
- `SIG-W-20260626-021` `[SHAPE-LIVE / LEVELS-STALE]` — **65 days old** (`as_of 2026-06-24`), status literally contains the word "STALE," printed with **no** flag. `SIGNALS.tsv:12`.
- `SIG-W-20260626-026` `[LIVE-RECONFIRMED]` — **36 days old** (`as_of 2026-07-23`), no flag. `SIGNALS.tsv:14`.
- `DEW-MECH-SELL-20260720` `[LIVE (CLAIM-2 RETRACTED)]` — **39 days old** (`as_of 2026-07-20`), no flag. `SIGNALS.tsv:16`.

Live boot output (exact printed lines, no flag appended to any of the three):
```
- [WALTER] SIG-W-20260626-021 [SHAPE-LIVE / LEVELS-STALE] index short entry/expiry/sizing | CTA 7352/7063/6642; -$40bn vs +$6.7bn | as_of 2026-06-24 (65d)
- [WALTER] SIG-W-20260626-026 [LIVE-RECONFIRMED] any short squeeze-risk sizing | median SI 15yr/GFC high | as_of 2026-07-23 (36d)
- [DEWEY] DEW-MECH-SELL-20260720 [LIVE (CLAIM-2 RETRACTED)] any mechanical-cushion / vol hedge sizing... | as_of 2026-07-20 (39d)
```
Every other active row today happens to be ≤17d old, so the gap is invisible on a casual read of a normal boot — it only shows up when a row is BOTH richly-named AND actually stale, which is the exact conjunction the anti-rot line exists for. **Verdict: SILENT.** The age itself is delivered correctly (age math is untouched); only the warning is missing.

## Finding #2 — STATUS.md (step 2's mandatory full read) is 90,236 B, over the real harness read cap, and TERRY's own self-declared budget is ~3x too permissive to ever catch it

`CLAUDE.md:142` mandates an unqualified full `Read` of `STATUS.md` at boot. Measured size: **90,236 B**. Per the read-cap formula this audit was given (25,000-tok cap × 2.17 B/tok = 54,250 B raw; DAEDALUS's own re-derivation elsewhere applies a 60% safety margin → 32,550 B), TERRY's `STATUS.md` is at **166% of the raw cap / 277% of the safety-margined cap** — solidly **OVER-CAP**, meaning a plain `Read` of the file at boot step 2 will silently truncate.

TERRY's own governance line (`CLAUDE.md:189`) declares: *"BYTE BUDGET `150,000 B` (soft `117,000` = 78%)... rotate [only] Over soft."* That self-declared cap is **~2.77x the real harness cap (raw) / ~4.6x the safety-margined one** — the file could grow all the way to 117,000 B, more than double the real cap, before TERRY's own rotation rule even fires. This is the identical failure class DAEDALUS's own charter documents about itself (`AGENTS/DAEDALUS/CLAUDE.md` §OUTPUT RULES: *"This line said `48,000 B` for six days after the budget was re-derived... 88% of the read cap"*) — a locally-declared size budget that isn't actually keyed to the harness constraint it exists to protect against, so the guard passes clean while the underlying read silently truncates.

Practical mitigation observed: the file's own top block is explicitly labeled *"MARKET OPEN. READ THIS BLOCK FIRST; EVERYTHING BELOW IS DATED HISTORY"* (STATUS.md line 74, captured in boot's head-print) — so a truncated read likely still gets the current-state block. But that is a lucky authoring convention, not a property the boot mechanism itself guarantees or checks.

## Finding #3 — corrections_boot_check.py is not wired into TERRY at all

Grepped `AGENTS/TERRY/CLAUDE.md` and every file under `AGENTS/TERRY/` for `corrections_boot_check` — zero hits. Unlike DAEDALUS (`CLAUDE.md` step 5b, mandatory) and other audited desks, TERRY's boot sequence has no R1-corrections check. Answers procedure item 6 directly: **NO.**

## Correction to this leg's own briefing assumptions

Two premises in the assignment do not hold for this desk's current code, worth stating plainly rather than silently working around:

1. **"TERRY's boot reads FORGE/STATUS.md"** — false for the numbered BOOT sequence. No step 0-13 in `CLAUDE.md`, and no line in `boot.py`, touches `FORGE/STATUS.md`. The only script that parses it, `scripts/positions_from_forge.py` (`CLAUDE.md:212`), is invoked solely for the desk-dashboard Artifact, which is explicitly **"ON REQUEST ONLY... do not auto-regenerate it at boot or closeout"** (`CLAUDE.md:166`). This appears to be deliberate design consistent with HARD BOUNDARY #6 ("do not assume current holdings... mark `[POSITION_STATE_UNKNOWN]`") rather than a gap — flagging as a correction, not a defect.
2. **"`paper_book_mark.py` uses an mtime proxy"** — grepped the whole `scripts/` dir for `st_mtime`/`getmtime`: zero hits anywhere in TERRY's own scripts. `paper_book_mark.py`'s staleness math (`business_days_between(_asof_date(row["mark_asof"]), today)`, lines 221-240, 459-461) is entirely **content-derived** from the TSV's own `mark_asof` cell, never filesystem mtime — the file's docstring (lines 12-16) states this is deliberate ("Stale marks are surfaced, not hidden, same discipline as the ledger-staleness boot alert"). The one mtime reference in the whole boot chain is the repo-shared `scripts/ledger_staleness.py:220`, and there it is the documented last-resort fallback behind git-commit-time — canon-compliant, not a defect. Per PAT-125 the audit should report what's actually there rather than confirm an unverified premise, so this is corrected rather than assumed.

## Read-cap table

| File (boot-mandated whole read) | Bytes | Verdict |
|---|---|---|
| `STATUS.md` (step 2) | 90,236 | **OVER-CAP** (166% of 54,250 B raw cap) |
| `RISK_RULES.md` (step 3) | 36,857 | NEAR-CAP (68% of raw cap; over the 32,550 B safety-margined cap) |
| `RISK_SCORING.md` (step 4) | 10,134 | under cap |
| `CHART_OPTIONS_WORKFLOW.md` (step 6) | 7,026 | under cap |
| `TRADE_CARD_TEMPLATE.md` (step 7) | 4,418 | under cap |
| `TRADE_BOOK.md` (step 8) | 35,886 | NEAR-CAP |
| `SETUPS.tsv` (step 8) | 95,253 | **OVER-CAP** (176% of raw cap) — mandated "if the task touches existing/queued trades," not unconditional |
| `SIGNALS.tsv` | 36,001 | NEAR-CAP |
| `POSTMORTEMS.md` | 41,063 | NEAR-CAP |
| `CLAUDE.md` itself | 28,697 | under cap |

Only `STATUS.md` is both **unconditionally mandated** and **OVER-CAP** — that is why Finding #2 is scoped to it. `SETUPS.tsv` is also OVER-CAP but its read is conditional ("if the task touches existing/queued trades"), so it is a real but narrower risk, noted here for completeness.

## What this audit could NOT see

- `scripts/paper_book_mark.py` and `scripts/snapshot.py` were **not executed** — both require live network (yfinance/chain fetch via a shared key) and `paper_book_mark.py` additionally **writes back** to `PAPER_BOOK.tsv` (`save_tsv`, line 488), which the EXECUTION GATE explicitly bars from an unattended audit run. Their delivered-content behavior is asserted only from static trace + their own `--selftest` design, not from a live run against today's chain.
- Steps 9-13 (position triage, live price pull, sizing calc, chain parse) are conditional/manual and were not exercised — no ticker or trade task was in scope for this leg.
- `ledger_sweep.py`'s full check suite (A-I) was only observed through `boot.py`'s advisory summary filter (`ledger_sweep_summary()`, which prints only lines starting with `🔴`/`STATE `/`SUPERSEDED`/`AGENTS/`/`->`) — the full unfiltered output of `python3 AGENTS/TERRY/scripts/ledger_sweep.py` was not separately captured, so any check that prints in a format outside that filter would be invisible to boot's advisory view even though it ran.
- Whether the 3 unflagged-stale signal rows found in Finding #1 have already been actioned outside the boot's view (e.g., a pending inbox packet not yet consumed) was not checked — only that the boot output itself carries no warning for them.
