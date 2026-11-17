ACCEPT — 0 blocking findings, 2 non-blocking (⚠️). 78994ce38a is safer than c5aec45139.

# Independent read 3 (final): second fix diff only (c5aec45139 to 78994ce38a)

Reader: the same independent, read-only Opus reader as reads 1 and 2. Date 2026-11-17 (ET). Scope: `git diff c5aec45139 78994ce38a -- PROME/tools/forecast_report.py`. That diff makes two changes: is_decided now takes the version's own resolved date, and the known date now includes the earliest resolved date carried by any decided version. Residue from reads 1 and 2 is not re-raised. The working-tree tool is byte-identical to 78994ce38a (`diff -q` empty).

Read-2 ❌1 is fixed. ZHAO ZHA-09 is BORN-DECIDED again, with known date 2026-07-04. Fixture fx3 row Z-9 is BORN-DECIDED with known date 2026-11-07.

## Every scored row whose class or known date changed (c5aec45139 to 78994ce38a, all 272 scored rows)

| Row | Old class, known | New class, known | Population | Reading |
|---|---|---|---|---|
| ZHAO ZHA-09 | BEFORE, 2026-08-21 | BORN-DECIDED, 2026-07-04 | closed, both | Correct. The first commit c1ea0e3244 (2026-07-09) backfilled the row already "LIKELY MISSED" with Date_Resolved 2026-07-04. |
| CREED PRED-CREED-009 | BEFORE, 2026-08-20 | AFTER, 2026-07-02 | closed, both | Correct, and a new true catch. The graded version c831f06a44 (2026-08-20) says in its Date_Resolved cell "The 2-consecutive-month condition was satisfied at the JUNE print (~2026-07-02)". The row was first committed 2026-07-27 at 30% (commit 43639b22c4). The call was logged after its condition had already been met. |
| REGINALD REG-09 | BEFORE, 2026-08-13 | BEFORE, 2026-07-10 | closed, both | Class unchanged. The 2026-07-10 date comes from an open "FROZEN-PENDING" version (653cec3d73, 2026-08-13 09:18 ET), whose Outcome reads "PENDING RESOLVE … retrieve Q1 EPS actuals". This is an open status read as decided (see ⚠️ 1). The event itself was April's Q1 prints, so the earlier date is still not too early in fact. |
| REGINALD REG-10 | BORN-DECIDED, 2026-03-04 | BORN-DECIDED, 2026-02-10 | closed, both | Class unchanged. The carried date is earlier than the first record. |

No row moves between the forward table and the closed population. The live run is unchanged: 23 BEFORE, 0 in every other forward class, 249 closed, 4 restarted, 2 LOOK, rc 0.

## ⚠️ 1. An open-type status that carries a date is read as decided; latent hole of read-1 ❌1's class (not blocking)
- **Claim:** is_decided docstring: "an owner dates a row when it is finished, and leaves the date empty while it is open."
- **Exact artifact:** is_decided (`… or resolved is not None`) and the per-version `res`. On inline-date ledgers, `res` is the first full date anywhere in the outcome cell, so a dated progress note counts.
- **Verification command:**
  - Scan of every committed version under 78994ce38a (is_decided wrapped to count tokens). Open-type tokens now read as decided: FROZEN-PENDING 44 versions, NEEDS_VERIFY 16 (OTTO, an inline ledger; example OTTO-10's Result "NEEDS_VERIFY 2026-09-30 (s026 …"). STUCK, STALE, RESOLVING, AT-RISK and UNQUANTIFIED stay open.
  - Fixture fx4 (/tmp/tmp.B6KNxmYUpn/fx4, OTTO inline ledger), row O-1:
    - 2026-10-20: OPEN at 60%.
    - 2026-11-03: NEEDS_VERIFY, with Result "2026-11-03: October print 6.3, direction supports; verify vintage mix".
    - 2026-11-16: HIT at 80%, with Result "HIT 2026-11-14 …". The probability was raised two days after the outcome.
  - A check of every row not yet graded HIT or MISS, for any whose known date the new rule moves on or before 2026-11-05.
- **Observed result:** fx4 O-1 gets known date 2026-11-03 and is counted in "report 1's closed population". The forward table shows AFTER 0. Under c5aec45139 the same row reads AFTER in the forward table. So a real post-outcome change is hidden, which is the dangerous direction.
  - Exposure today is zero. No scored row changes population.
  - Only three ungraded rows would move on or before the cut, and all three carry final statuses with true dates: CREED PRED-CREED-011 NO-VERDICT, HAWK HAW-19 DEFECTIVE-INSTRUMENT 2026-09-28, HENRY HEN-40 GRADED-MIXED 2026-07-10.
  - The hole needs an open-type, non-map status with a date on or before 2026-11-05 on a row graded later.
- **Proposed change:** declare it as residue, or narrow it in one line. For example, apply the date rule only on resolved-date-column ledgers (ZHA-09 stays fixed, because ZHAO is a column ledger), or never count tokens containing PENDING, NEEDS, STUCK, HELD or RESOLVING as decided.

## ⚠️ 2. Carried dates come from free text in a date cell (not blocking)
- **Exact artifact:** `parse_iso(g(idt))` takes the first full date in the cell, whatever the cell says.
- **Observed result:** in CREED-009 the Date_Resolved cell held a paragraph, and its first date ("~2026-07-02") was the true outcome date. A cell that begins with a reference date or a target date would carry that date instead. A decided row only ever carries a date this way, so such a date moves the known date earlier. That gives a false AFTER or BORN-DECIDED (safe direction), or a move into the closed population (the hiding direction of ⚠️ 1). I found no real case of a target date carried by a decided version: the four changed rows are listed in full above.
- **Proposed change:** none required now. Name it in the declared limits beside the existing outcome-cell caveat.

## Fixtures against 78994ce38a
- **fx1:** no row changed from read 2.
  - A-1 SAME-DAY; A-3 BEFORE; A-4 BORN-DECIDED (×2); A-5 BEFORE; A-7 AFTER; A-8 BEFORE.
  - X-9 BEFORE at AEOLUS and BORN-DECIDED at WATT.
  - BR-1 BORN-DECIDED; B-1 BEFORE; B-2 BEFORE; B-3 BORN-DECIDED.
- **fx2:** unchanged. R-1 BORN-DECIDED, restarted.
- **fx3:** Z-9 changed from BEFORE to BORN-DECIDED (fixed; known 2026-11-07). Unchanged: T-1 BEFORE (read-2 residue), P-1 BORN-DECIDED and restarted, C-1 BORN-DECIDED.
- **fx4 (new):** O-1 sits in the closed population, though it should read AFTER in the forward table (⚠️ 1).

**Which commit is safer:** 78994ce38a. Its new error makes known dates too early. That mostly gives false AFTER or BORN-DECIDED flags, and hides a row only in the narrow case above, with no row exposed today. The c5aec45139 error gave false BEFORE on real born-decided rows (ZHA-09) and missed CREED-009's true AFTER.

**Ran:**
- selftest (PASS 47, rc 0) and the live run (rc 0)
- old against new timing over all 272 scored rows (scratchpad/probe6.py)
- the token scan of decided versions
- a git history read of CREED-009 and REG-09
- fx1, fx2, fx3 and the new fx4
- the scan of ungraded rows that would move into the closed population

**Only read:** the selftest's new cases, and how inline-date ledgers fall back to the outcome cell when an archive has no Date_Resolved column. I exercised that fallback only through fx4's OTTO ledger, which is registered as inline.

No repository file was edited, staged or committed except this ledger.
