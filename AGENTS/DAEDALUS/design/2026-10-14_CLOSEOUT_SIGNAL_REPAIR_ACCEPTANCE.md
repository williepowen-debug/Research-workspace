# Closeout signal repair — acceptance conditions (written BEFORE the code, WQ-229 / CHECK_STANDARD §3)

**Written:** 2026-10-14 22:07 ET · **Authority:** Will 22:05 ET in session, verbatim *"Can we fix the close out checklist now? and the false alarms?"* — on DAEDALUS's ideas-list rows 1–2 (`PROME/ideas/list.tsv`, 60368b462). DAEDALUS owns `daedalus_gate.py`, `complete_check.py`, `profile_clock_check.py` (own dir) and `scripts/orphan_check.sh` (root `scripts/` grant: break-fix + standards; behaviour change Will-visible — Will asked for it).

**The defect, in its own terms:** the 10/14 final closeout reported BLOCKING 1 · UNKNOWN 1 · DUE 3 with **zero new problems** — every item was known and already explained. A checklist that can never be green trains its reader to stop reading it. Two of the findings were false (a profile clock that ignored the "WHOLE refresh" wording; an orphan check that called another desk's filing of a delivered packet "likely YOURS").

## Fix 1 — `complete_check.py` leg (ii): a DOCUMENTED late pairing is RECORDED-LATE, not BLOCKING
- **AC1.1** A standards commit with no same-commit EVOLUTION.md is flagged exactly as today **unless** the COMMITTED `EVOLUTION.md` (at HEAD, never the working tree) contains a line naming that commit's 9-character hash AND the words PAIRING … LATE (in either order, ≤40 chars apart). Then it prints `📝 PAIRING RECORDED LATE: commit <h> … — late entry EVOLUTION.md:<line>` and does **not** count as a finding.
- **AC1.2** A hash mention WITHOUT the late-pairing words (e.g. "encoded 0cc007f28") does NOT excuse the commit — still a finding.
- **AC1.3** A late entry present only in the working tree (uncommitted) does NOT excuse it.
- **AC1.4** The miss stays visible: the RECORDED-LATE line prints every run in range; nothing is hidden. Legs (iii)–(v) unchanged.
- Drill: scratch clone — commit touching `BLUEPRINTS/` without EVOLUTION → rc 1; add a hash-only mention → rc 1; add uncommitted late entry → rc 1; commit the late entry → rc 0 with the 📝 line. Live: today's range → 47bd8f55d RECORDED-LATE.

## Fix 2 — `daedalus_gate.py`: NEW vs CARRIED, without changing any class or exit code
- **AC2.1** **Classes and the overall rc are unchanged** (rc 2 UNKNOWN · 1 BLOCKING · 0) — PROME tooling, candidate receipts and the charter's rc contract read them.
- **AC2.2** A register `runs/GATE_ACKS.tsv` (`step · mode · fingerprint · reason · owner · added · expires`). `daedalus_gate.py ack <mode> <step> --reason … --owner … --expires YYYY-MM-DD` writes a row from the **latest receipt** of that mode: it acknowledges exactly what was seen.
- **AC2.3** The fingerprint is a hash of the step's finding lines with digits and hex hashes normalised away — so a daily age tick does not break it, but **any added, removed or changed finding line does** (a new agent in an UNKNOWN list re-surfaces as NEW).
- **AC2.4** A step is CARRIED only if: its class is DUE / UNKNOWN / ADVISORY, an ack row matches mode + step + fingerprint, `expires` ≥ today, and `expires` ≤ `added` + 21 days. **BLOCKING can never be carried** (the `ack` command refuses it and the matcher ignores it).
- **AC2.5** Output adds a VERDICT block after the steps: `NEW this run: <steps>|none` and `CARRIED: <step · class · reason · owner · expires>`. Expired or malformed ack rows are named (never silently ignored). The receipt JSON gains `carried` per step and `new` list; GATE_LOG row format unchanged.
- **AC2.6** Existing selftests pass unchanged; new selftest cases: match → CARRIED; fingerprint drift → NEW; expired → NEW + named; >21d → refused/ignored; BLOCKING → never carried.
- Drill: live closeout with acks for C0/C3/C7 → VERDICT `NEW: none`; then a synthetic extra finding line → that step NEW.

## Fix 3 — `profile_clock_check.py`: read the "WHOLE refresh <date>" wording
- **AC3.1** A header `Body: A, refreshed B, WHOLE refresh C` (no explicit Body vintage) reads vintage **C**; a standalone segment `WHOLE refresh C` reads **C**.
- **AC3.2** A "WHOLE refresh" date after the as-of date fails loud (existing future-vintage rule), never silently accepted.
- **AC3.3** Live before/after over all `profiles/`: identical verdicts (VULCAN and ZHAO already carry explicit `Body vintage:`), proven by diff.

## Fix 4 — `scripts/orphan_check.sh`: an already-committed packet moved or edited by its RECIPIENT is not "likely YOURS"
- **AC4.1** Classify by state, not by filename alone: a path (or a rename's SOURCE) that exists in `HEAD` is **delivered**; an uncommitted change to it is the recipient's live work → printed under a distinct `[delivered — recipient's change]` label with do-not-commit guidance.
- **AC4.2** An untracked or newly-added (never committed) file matching the author pattern stays `[likely YOURS]` with the commit instruction — the capable case must still fire.
- **AC4.3** Exit 0 always and read-only, as before; the clean line unchanged.
- Drill (scratch clone, never the live index): commit a `_from-DAEDALUS_` packet into another inbox, `git mv` it to `processed/` → `[delivered]`, not YOURS; an untracked `_from-DAEDALUS_` packet → `[likely YOURS]`; nothing dirty → clean line.

## Review
These change guards other sessions rely on: **one independent fresh-context read of all four diffs**, with its own counterexample, before any is called fixed (WQ-229). Records: EVOLUTION entry (complete_check semantics), CHECKS.tsv `orphan_check` row, gate spec §8 amendment, charter step 9 one line for `ack`.
