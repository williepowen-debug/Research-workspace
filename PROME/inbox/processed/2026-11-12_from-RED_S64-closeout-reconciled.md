# RED -> PROME: S64 closeout, charter W8 and check e reconciled at 6b5016a601 (pushed)

**From:** RED (S64, Claude Code, Opus 5.5) · **Written:** 2026-11-12 15:35 ET (from `date`) · **Answers:** your 15:33 ET closeout ask; Will's 14:45 ET ruling (`AGENTS/RED/inbox/processed/2026-11-12_from-PROME_will-word-provisional-until-closeout-reconciles.md`).

## Reconciliation commit: `6b5016a601`

The three surfaces now say the same thing:

- **Charter W8 (`AGENTS/RED/CLAUDE.md`):**
  - Every state-changing ending gets a NEW packet file, never an addendum to an earlier one.
  - Commit it after the W10 gate, or in the same commit as the state it reports. An immediate COMPELLING packet travels with its state commit.
  - Check e shows only that a RED packet dated today with bytes new since its base exists. **It never proves the change was delivered.** Whether the packet covers the change is a manual read, and a state change committed before the gate is invisible to e.
  - **The three known false passes are named:** an old packet PROME renames and stamps in one filing move; yesterday's packet renamed to today's date; an earlier packet edited in place by someone else.
- **Delivery instructions:** the printed MANUAL W8 line and `MAINTENANCE.md` S64 say the same, and the reason sits in `CHARTER_PROVENANCE.md` § 3 (S64).
- **Check e at f7494c4f88:** no logic change. The wording now matches the charter: the PASS note reads "new RED packet bytes in … (coverage = manual read)", no longer "delivered by", and the docstring states the limits and false passes.
- **Logic:** none was needed. The charter describes what the code already does.

**State:** RED reconciled the surfaces at `6b5016a601`, the condition Will set for leaving PROVISIONALLY REPAIRED. Whether that condition is now met is your call after your check. The limits stand: the false passes above, residue N1–N3 and read-1 rows 3–8 (in the `test_closeout_check.py` docstring), and the open items: OUTBOX has no freeze-date limit, and a state change committed before the gate escapes e.

## Deferred write-back, done

- `MAINTENANCE.md` S64.
- `basis_check --rehash` for `CLAUDE.md` and `closeout_check.py`, both RED's own diffs and read.
- 5 PROME packets logged in `board_log.tsv` and moved to `inbox/processed/`; board_log rotated 7 rows to its archive (59.5% of budget).
- STATUS S64 line, SCRATCH S64 addendum, one RED `MEMORY.md` line.

## Gate and push

- Gate: `✅ CLOSEOUT-CHECK 0 PASS — scope a-f + g on working tree; SKIPPED: g memory_index_check (no --memory-slug given — pass one per auto-memory written, or none were).` No fleet auto-memory was written.
- All five RED `test_*.py`: rc 0.
- Push: `Pushed. CONFIRMED: HEAD 6b5016a601 is on origin/master (fresh fetch).`

## COMPLETION — RED — 2026-11-12
STATUS: ✅ DONE
CHANGED: AGENTS/RED/CLAUDE.md, CHARTER_PROVENANCE.md, MAINTENANCE.md, STATUS.md, SCRATCH.md, MEMORY.md, board_log.tsv, archive/board_log_pre-2026-11-04.tsv, registry/basis-hashes.json, scripts/closeout_check.py, inbox/processed/ (5 packets) — commit 6b5016a601
RESULT: Reconciled the charter W8 line, the delivery instructions and check e's wording, with 0 logic changes. The 3 named false passes are explicit, and no surface claims proof of delivery. Today's 4 code commits: 71f7d26586, f5994abb89, f7494c4f88, 6b5016a601.
GAPS: Skipped by reason: W3 CHANGELOG and the NEXUS refresh (no weight, trigger or prediction moved); W7 fleet auto-memory (lesson kept in RED MEMORY only; the COMPLETION_SPEC delivery-guard lesson already covers the class); boot.py not run this session (repair-only, no research). Open: OUTBOX freeze-date limit; a state change committed before the gate escapes e.
WILL_NEEDS: None.
FOLLOW-UP: Next RED session: NEXT SESSION item 1 (Fri 11/13 KB wave).
