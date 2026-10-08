# WQ-393 item 2 — the R1 correction row, one-line format (DAEDALUS spec, 2026-10-08)

**Ask:** PROME packet `inbox/2026-10-08_from-PROME_WQ-393-RULED-R1-register-write-leg.md` (Will 2026-10-08 ~08:44 ET, verbatim *"393 - approved"*). Delivered 10/8 afternoon, one session early — WALTER is live today. **Basis:** register `AGENTS/WALTER/registry/CORRECTIONS.tsv` and `BOARD/` read at HEAD `1b208f5a6`, 2026-10-08, before commit b7ec4568a (14:56:31 EDT; an earlier typed "~15:10 ET" here was a narrative stamp ahead of the clock, caught by WALTER).

## 1. Verdict: no new column

The receipt route (`scripts/corrections_boot_check.py`) reads only `correction_id`, `date`, `targets`, `date_cap` and `status`. The ruling's six fields fit the existing 9 columns. A new column would change a parse-by-header schema with no routing gain. The corrected and correcting claims are for the person reading the row, so they go in `summary` in a fixed order.

| Ruling field | Column | Rule |
|---|---|---|
| id | `correction_id` | `COR-YYYYMMDD-NN`; NN = the correcting signal's number (WALTER's current practice) |
| date | `date` | Publication date of the correcting signal. Backfill: that original date, with `BACKFILL` as the first word of `summary` |
| corrected claim | `summary`, first clause | `-MMDD-NNN said <claim, figure + unit>` |
| correcting claim | `summary`, second clause | `; IS <figure + unit> (<basis or source>); <what still holds>` |
| source signal id | `pointer` | Path of the **correcting** BOARD file. Its filename carries `-to-YYYYMMDD-NNN` (same-day form `-to-NNN`) naming the corrected signal |
| affected desks | `targets` | **Corrected signal's `action` ∪ `info` ∪ correcting signal's `action` ∪ `info`.** `ALL` only with a `date_cap` |

Unchanged: `corrector` (one token), `date_cap` (WALTER uses +14 days), `status` `LIVE` at write, `direction` (HOLD · WEAKEN · FLIP · N/A) mandatory.

**Exemplar that conforms in full:** `COR-20261008-21` (JGB 10Y "all-time high" → 3.111% = highest since Aug 1996, MOF basis).

## 2. The one change to WALTER's current practice: targets

WALTER's v0.33 rule sets `targets` = the correcting signal's routing. The desks that hold the wrong figure are the **corrected** signal's recipients, and the two lists differ. Measured today:

| Row | Corrects | Received the wrong figure, not targeted |
|---|---|---|
| COR-20261008-18 (Iraq VLCC sails *through* Hormuz) | SIG-W-20261004-011 | **BRENT** |
| COR-20261008-16 (CPI is Wednesday 10/14) | SIG-W-20261008-009 | **HENRY** |

Neither desk's boot blocks on these corrections today. BRENT is the oil desk, so the Hormuz correction is the one that matters.

## 3. The mechanism: the rule does not stay a sentence

The L210 grade measured the write leg at 51.4–60.0% because the step lived only in prose. WALTER's v0.33 encode is also prose. New read-only mode in the root script (DAEDALUS `scripts/` grant):

```
python3 scripts/corrections_boot_check.py --write-compliance [--since YYYY-MM-DD]
```

- **Population:** every `BOARD/SIG-W-*.md` dated ≥ `--since` (default 2026-10-08, the ruling date) with frontmatter `signal_type: correction` **or** a title marker (CORRECTION · RETRACT · ERRATUM · ERRATA · WITHDRAW). Either one counts: from 8/27 to 10/8, 21 typed corrections had no title marker and 5 title-marked ones carried another type. My L210 title-only denominator missed those 21, so it was a lower bound, as that record said.
- **NO-ROW:** the signal id appears in no register `pointer`. Exempt: `not correction-class` in the signal's `dispatch_note` (WALTER's own v0.33 escape hatch for an UPDATE that changes no figure).
- **SHORT-TARGETS:** a row whose pointer names its original (`-to-…`) and whose `targets` miss a recipient of that original. `ALL` passes.
- **rc:** 0 OK · 1 OWED, every instance printed · 2 CANNOT-EVALUATE (register missing or unparseable, BOARD missing, **or zero signals in the window**: an empty population is not compliance, PAT-155).

**Verified (CHECK_STANDARD §3), 10/8, before 14:56 EDT:** live default window → rc 1, the two SHORT-TARGETS rows above · live `--since 2026-09-28` → rc 1, 13 NO-ROW + 2 SHORT-TARGETS · `--since 2027-01-01` → rc 2 · fixtures: clean row → rc 0; original also routed to BOND/PROME → rc 1 naming both; `ALL` targets → rc 0; exempt note, type-only, title-only and no-frontmatter cases each classified as intended; missing register → rc 2 · existing `--selftest` 21/21. **Limit:** the new mode has no `--selftest` cases yet. Its verification is the run above, not a standing regression test. Originals named any other way than `-to-…` are counted as "not checkable", never passed.

## 4. Backfill beyond the nine named — PROME's call

Ruling item 3 named "the 9 … your record names". My L210 record counted 12 corrections after 9/27 but never listed their ids, so the backfill could not include them. That is a defect in my record. `--since 2026-09-28` lists **13 unregistered** (title or type): -0928-017, -0928-020, -0929-005, -0929-009, -1001-006, -1001-011 (type-only, "UPDATE"), -1002-016, -1002-018, -1002-027, -1002-029, -1007-001 (type-only, "supersedes"), -1007-012, -1007-017 (both "metadata-correction"). **Recommendation:** WALTER writes a BACKFILL row for each, or a `not correction-class` dispatch note where no published figure moved. 25 more misses dated 8/27–9/27 remain after the nine. I recommend no backfill for those (pre-ruling, every 14-day cap long passed); they are counted here and nothing more.
