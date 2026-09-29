# BOND CLOSEOUT

**Owner:** BOND · **Created:** 2026-09-29 · **v2 after a blind cold read the same evening** (4 ❌ / 25 ⚠️ applied; ledger `analysis/2026-09-29_coldread_CLOSEOUT-v1_ledger.md`). **Rules only.** Reasons and history: `docs/PROTOCOL_PROVENANCE.md` (crc32 `4276224127`) and `git log -p -- AGENTS/BOND/CLAUDE.md`.
Git mechanics are root `CLAUDE.md` § Git Protocol; not restated here. Tier names Bounce/Light/Standard/Heavy match `PROME/CLOSEOUT.md`, LIQUID, TERRY and HANS; **Addendum is BOND's own**, taken from RED's W-A.

## When to run
Before `/clear`, a machine switch, a long pause, or any session end. Run it at EVERY ending, not only end-of-day.
**Live-event override:** if a print or trigger window is in progress, write STATUS and SCRATCH now; run the rest after.

## Pick a tier — say it out loud; the runner takes it lowercase: `bounce` · `light` · `standard` · `heavy` · `addendum`

| Tier | When | Touches | Runner? | Commit? |
|---|---|---|---|---|
| **bounce** | Restart within the hour | SCRATCH: 3–5 lines (what happened · pending · entry point) | No | Optional checkpoint. **Machine switch ⇒ commit + push, mandatory.** |
| **light** | Short session; no level moved, no packet sent | STATUS surgical + SCRATCH targeted + the ledger touched | Yes, `--tier light` | Optional; machine switch ⇒ mandatory |
| **standard** *(default)* | End of thread or day; levels refreshed, mail drained, packets sent | **C1–C9, C11, C12** | Yes | Yes |
| **heavy** | Tooling built, a durable lesson earned, a spec or charter changed | Standard **+ C10** | Yes | Yes |
| **addendum** | Any ending after the first in the same day, **except end-of-day** | Floor A1–A3 + the conditionals below | Yes, `--tier addendum` | Yes |

**Precedence:** end-of-day is always at least `standard`, even if it is the day's fourth ending. `addendum` is for mid-day re-endings only.

## Glossary — every term below is defined here or by pointer
- **Read cap:** root `CLAUDE.md` § Data Hygiene: a whole-read surface stays under **32,550 B**; STATUS rotates at **≥75%** (24,412 B). Check: `python3 scripts/read_cap_check.py --agent BOND` (repo root).
- **Owed rows:** predictions the docket or STATUS says must be registered by a date (example on 9/29: the 10/28 FOMC curve-shape row by 10/21).
- **`bond-state` token:** the one-line `<!-- bond-state: thesis=…; regime=…; gate_a=…; rearm=…; add=…; kill=…; posture=… -->` present on STATUS, THESIS and TRADE; compared field-by-field by `monitors/mirror_check.py`.
- **Marks:** live prices or option quotes. TRADE.md carries none (root rule #4: prices must be live).
- **STATE AT WRITING block:** the blockquote at the top of SCRATCH (position · composite · counter · OPEN predictions · latest official cells).
- **Re-pin block / fold:** the dated block at the top of `NEXUS_BRIEF.md`. "Fold" = REWRITE that block; never append a second one.
- **Carve-out ①:** root `CLAUDE.md` § Git Protocol: a packet you authored into another desk's inbox is yours to commit, and you must.
- **Root step 3:** root `CLAUDE.md` "At session end" step 3, the non-fast-forward recovery. Never force.
- **Push receipt:** the literal line `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` Anything else is not a receipt.
- **coldreader:** the `coldreader` agent type (Agent tool, model opus): a blind read of one file by a reader who knows nothing about the fleet.
- **board_log:** `AGENTS/BOND/board_log.tsv`, one row per WALTER signal consumed (written in C8).

## The routine — run in order; name each step's outcome in SCRATCH, **including "no-op"**

**C1. STATUS.md.** Dashboard, matrix (re-sum the composite), gates, catalysts twin, positions, bottom line. Source tag on every value. Stay under 75% of the read cap; rotate, never raise.
**C2. Workbook.** New facts → `workbook/KB.tsv`. Moved indicators → `VX.tsv`. Channel changes → `FLOW.tsv`. Flip ACTIVE rows past `Stale_By`.
**C3. Predictions.** Resolve every row flagged DUE at boot; never leave a row OPEN-but-stale. Register owed rows with a base rate.
**C4. Thesis.** Thesis-level change → `thesis/THESIS.md` + `thesis/CHANGELOG.md`, version bumped in H1 and the Version field together. **Any change to a gate state, the position, the regime label or the version ⇒ update the `bond-state` token on STATUS, THESIS and TRADE in the same edit** (the token moves even when the thesis text does not).
**C5. Catalysts.** `docket/CATALYSTS.tsv` is the source of truth: prune fired rows, add dated ones, mark outcomes. The STATUS twin keeps the same event set.
**C6. TRADE.md.** Posture and gates only, no marks. A gate state or position change ⇒ the row and the token change today.
**C7. SCRATCH.md.** Rewrite (standard/heavy) or target (light). It carries the STATE AT WRITING block, WHAT I DID, NEXT SESSION (dated), OPEN THREADS, POSITION, MAIL, and a stated no-op for each surface not written.
**C8. RECEIPT.md + board_log.** Overwrite RECEIPT when signals or a tasked deliverable were processed; one `board_log.tsv` row per WALTER signal consumed.
**C9. Promotion scan.** Transferable lesson → auto-memory (then remove the local copy). BOND-only lesson → `MEMORY.md`. Outbox packets 🔴-acute only.
**C10. Charter check (heavy only).** A threshold, step, tool or date changed ⇒ `CLAUDE.md` and this file agree with it today.
**C11. NEXUS_BRIEF.md — the LAST content write, after C1–C10.** Rewrite the re-pin block; owner pointers only; never append.
**C12. FREEZE → RUN → VERIFY → COMMIT → PUSH.**
   1. **Freeze:** stop editing files. Any edit after this line restarts C12 at 1.
   2. **Run (from `AGENTS/BOND/`):** `python3 monitors/closeout_run.py --tier <tier> [--superseded OLD NEW]… [--memory-slug S]…`
      It runs `closeout_check` (lint · numeric drift · assertions · mirror sync) · handoff ordering · root 1b orphan · root 1c consumer (only when `--superseded` is declared) · root 1c-bis ledger nudge · root 1d memory (only when `--memory-slug` is declared) · root 1e claim · read cap · inbox re-scan. It prints RAN / FAILED / NOT-APPLICABLE per step, records the working-tree digest, and appends a row to `registry/CLOSEOUT_LOG.tsv`.
      **rc ≠ 0 ⇒ no commit.** Fix, then restart C12 at 1. A NOT-APPLICABLE is a self-declaration: a changed threshold, score, split or band must be declared with `--superseded`.
   3. **Verify (from `AGENTS/BOND/`):** `python3 monitors/closeout_run.py --verify` → prints `FREEZE MATCH` (tree unchanged since the last run) or `FREEZE MOVED` (restart at 1).
   4. **Commit (from the repo root, `cd "$(git rev-parse --show-toplevel)"`):** exact pathspecs `AGENTS/BOND/<file>`; self-authored packets in other inboxes under carve-out ①. Message via a quoted heredoc file; subject ≤ 100 chars.
   5. **Push (repo root):** `bash scripts/safe-push.sh`. Read the push receipt line itself; a tail is not a receipt. Non-ff ⇒ root step 3; never force.

## Addendum floor (mid-day re-endings; end-of-day is `standard`)
**A1.** STATUS top state line current for THIS ending. **A2.** SCRATCH addendum section. **A3.** C12 in full with `--tier addendum` (freeze → run → verify → commit → push).
Conditionals, each keyed to a fact: a score, gate state, position, regime label or threshold changed ⇒ **the `bond-state` token on all three surfaces + the TRADE row (C6) + the brief re-pin (C11)**; CHANGELOG (C4) only if the change is thesis-level. A workbook row ⇒ C2. A prediction came DUE ⇒ C3. A catalyst fired ⇒ C5. A packet or signal processed ⇒ C8. A tool or protocol changed ⇒ C10.
One question, out loud: *did this ending change a number, date or state another desk consumes?* If yes, C11 is not optional.

## What the runner cannot see
It checks vintage, tokens and a working-tree digest, never content. A fresh header over a stale body passes. A wrong banner with a correct token passes. Those are C1/C4/C11 judgement, named in SCRATCH, and a `coldreader` pass after any restructure.

## Surfaces boot reads ↔ closeout writes (the only pair list; the step text does not repeat it)
| Boot reads | Closeout writes |
|---|---|
| STATUS (boot 1) | C1 |
| SCRATCH (boot 2) | C7 |
| MEMORY (boot 3) | C9 |
| PREDICTIONS DUE-scan (boot 4) | C3 |
| docket_check + CATALYSTS (boot 5) | C5 |
| boot_recompute (boot 6): TRADE gate table, monitors, NEXUS_BRIEF drift | C6, C11, C12 (closeout_check 1/4) |
| WALTER lane + corrections (boot 7, 7b) | C8 |
