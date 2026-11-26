# HOMER SCRATCH — 2026-11-25 (fifth session: boot 17:25 ET; closed 20:47 ET; reopened 22:04 ET for script 2; closed 23:35 ET)

**Runtime/session:** Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop. No helpers spawned. Fourth-session handoff: `git show c711ec8526:AGENTS/HOMER/SCRATCH.md`.

## Done

| Item | Result |
|---|---|
| Plan item 1 (DAEDALUS steps 3, 4, 5, 7; STATUS red marks) | Done 17:31 ET (8911d54f2c); MAINTENANCE. Start-up read 109,457 B to about 90.7 KB |
| Plan item 2, script 1 (Will 18:28 ET "yes go ahead and build") | `tools/fetch_series.py` built and pushed (68d770494d); selftest 12 malformed inputs refused; live run matched hand readings |
| Will 18:49 ET "ok go" | January prior-year Treasury feed (d05e2671e0); Treasury 11/25 close 4.85 / 4.61 as context in RATES and STATUS; spread stays on 11/24 (LESSONS §44) |
| READS re-sign | DONE by PROME at 02571a598e (packet consumed; HOMER rows re-signed in `PROME/registry/READS.tsv`) |
| Script 2 after closeout (Will 22:02 ET, full scope) | `tools/filing_reader.py` built; tag survey 11 of 36 pairs tagged; `check` 5 of 5 hand readings match; draft `reports/filing_drafts/2026-09-30_servicers_DRAFT_2026-11-25_2226.md`; DEWEY told by packet |
| Script 2 upgrade (Will 22:52 ET "build 1 and 2 and 3") + DAEDALUS fixes (23:22 ET) | Statement pages, confirmed labels (4 stored in `registry/FILING_LABELS.tsv`), balance sheet change since last draft; year-in-label and blank-cell fix; check 8 of 8. Drafts: June `..._2301`, September `..._2325`. **Next: read the UWMC, LDI, ONIT hedge matches (derivative balance changes, not settlement cash) and RITM/ONIT advances rows before confirming any label** |
| Every-session checks | ATTOM 404 ×3 at 17:28 ET; servicer rating search nothing new (one thin search) |

No reading, band, count, kill test or registered odds changed.

## Due next

1. **Run `python3 tools/fetch_series.py` first at each PMMS, FMHPI or Apartment List pull** (it saves and checks; it grades nothing, so the reading still goes to the ledger by hand). ICE October First Look, next check Mon 11/30 (**HOM-07, HOM-08**, C1). ATTOM Sept/Oct/Q3.
2. Apartment List Nov (**HOM-06**) · FMHPI Oct · Redfin weekly · 11/30 EO check · 12/01 combination review (046 trigger HAS fired; 045 gained PennyMac) · ~12/01–05 Trepp Nov (**HOM-05**: did Cove revert, did Blackjack enter?) · 12/02 read-cap re-measure and MBA apps · 12/03 PMMS · 12/04 construction jobs · 12/07 Toll · 12/09 NAR (**HOM-09**).
3. HUD FHA October report (~December): read EVERY table; starts against ~10,465 a month.
4. PennyMac Q4 (about February): cushion over the Fannie/Freddie test (unscored view: lower than $94M about 25%, shortfall under 3%); Walker & Dunlop Q4 allowance (above $63.2M about 75%, unscored).

## PLAN OF RECORD (Will 2026-11-25 17:19 ET; carry until done)

Dated prints come first: the 11/30 ICE check outranks this plan.

1. DONE 2026-11-25 (fifth session).
2. **Script 1 BUILT 2026-11-25 18:31 ET (Will 18:28 ET "yes go ahead and build", option A):** `tools/fetch_series.py`. Use it at the next PMMS (12/03), FMHPI (~11/30) and Apartment List (~11/30) pulls; **keep or delete by the end of the December refreshes**: delete if it does not plainly save time. It is 353 lines, not the ~150 scoped (selftest included).
3. **Script 2 BUILT 2026-11-25 22:26 ET (Will 22:02 ET, full scope, no trial):** `tools/filing_reader.py`. Use at the Q4/10-K servicer filings (~Feb 2027): `check` first, then `read --period 2026-12-31`, then read each filing. after the 23:07 upgrade 7 of 36 pairs come back with nothing and pattern matches still need confirming by hand (`confirm`); 4 labels stored (see MAINTENANCE 22:31 ET).
4. **Not in the plan:** step 6 (band history out of CLAUDE.md) CLOSED, NOT DONE (Will 2026-11-25 23:46 ET "ok agreed go ahead" on HOMER's recommendation): saving ~5% of the start-up read, and several derivation lines work as caveats; reopen only if CLAUDE.md passes 45,000 B (docket row); the one-to-one with LABOR skipped; no new band, kill test, rule or check.

Sources: `AGENTS/DAEDALUS/runs/2026-11-25_HOMER_ARCHITECTURE_REVIEW_READ.md` (incl. addendum) and `2026-11-25_HOMER_PEER_COMPARISON.md`.

## Carry by name until closed

- TERRY's answer on the corrected FHA packet · Freedom 10% note: use of proceeds unread ($540M due January 2027) · Fannie Sept as first published · brokers' commissions line at BEA · MBA FHA serious-DQ history (Will's browser only, optional) · LABOR on the A3 edge. Tracked: OBLIGATIONS_OTHERS B11, B13, B14.
- A1: re-ask PROME if ICE skips its Dec, Jan AND Feb editions (docket ICE Monitor row).
- No new kill tests, bands or rules (Will 11/24 23:33 ET). Three reporting questions from the outside review are with Will through PROME, not mine.
