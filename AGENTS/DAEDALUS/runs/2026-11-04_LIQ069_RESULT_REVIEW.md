# LIQUID Gate 069 L4 exact-boundary result read — 2026-11-04

**VERDICT: WITHHELD.** Hold stays in place. The comparator repair is correct; one added input line reintroduces a boundary defect.

| Field | Value |
|---|---|
| Reviewer | DAEDALUS, daedalus-97 [878ed2], claude-opus-5-5, Claude Code. Commissioned by Will in this chat 20:39 ET ("yes") on LIQUID's packet |
| Candidate | `AGENTS/LIQUID/scripts/gate069_legs.py` at 41b088158c47ced52eb42aeda7a52e1de912eba5, SHA256 917e052930eea6fec490… (full 917e052930eea6fec490b3de24e49a1a212ede9903cd19bf190d5b6ccd9104ca); unchanged at HEAD at review |
| Criteria | `AGENTS/LIQUID/research/2026-11-04_credit-followthrough/ACCEPTANCE.md`; letter KB-LIQ-069 PRECISION / TIE / RESET |
| Acceptance reads | 1 of the one requested. No LIQUID file edited; all tests ran on scratch copies with bytecode writing off |

## Blocking defect

Candidate line 257 `eq[t] = {d: round(float(v), 2) ...}` converts vendor closes to two decimals before the exact comparator sees them.

**Half-cent closes are real in LIQUID's own evidence:** 6 of 184 closes in `raw_closes.json` (Yahoo Finance mirror, retrieved 2026-11-04, four names, 2026-09-01 to 2026-11-03) are not whole cents.

| Name | Date | Vendor close ($) | After line 257 ($) | Direction |
|---|---|---:|---:|---|
| CRWV | 2026-10-23 | 54.235 | 54.24 | up |
| IREN | 2026-09-25 | 44.125 | 44.12 | down |
| IREN | 2026-10-23 | 24.905 | 24.91 | up |
| APLD | 2026-10-14 | 20.325 | 20.33 | up |
| APLD | 2026-10-30 | 17.815 | 17.82 | up |
| NBIS | 2026-09-29 | 237.355 | 237.35 | down |

The direction is set by binary storage noise, not by a rule: stored 54.23500061 rounds up, stored 237.35499573 rounds down, exactly representable 44.125 rounds to even. The line's comment ("Restore the letter's as-published 2dp raw closes") does not hold for these rows; nothing in the evidence shows a two-decimal value was restored.

**Independent counterexamples**, each with a real close as the prior session, HY +5bp, run through the actual CLI path on a scratch copy with the hold removed and data sources stubbed, and repeated in the minimal reproduction `runs/2026-11-04_LIQ069_RESULT_REVIEW_REPRO.py` (run from repo root with `.venv/bin/python`):

| Case | Exact move | Correct grade | Pre-repair 0ef2c3def | Candidate |
|---|---:|---|---|---|
| CRWV 54.235 → 46.10 | −14.99954% | NOT FIRED | NOT FIRED | **FIRED (false fire)** |
| NBIS 237.355 → 201.75 | −15.00074% | FIRED | FIRED | **NOT FIRED (false miss)** |

The candidate changes a right answer to a wrong one in both directions. This is the tolerance widening that condition 2 forbids, and condition 1 requires raw closes be read as their decimal representations.

**Why the author evidence did not show this:**
- `selftest` exercises only `grade_l4`, so the 2.040000000001 case passes there while the CLI path would round that same value to 2.04. Removing the rounding from line 257 leaves selftest PASS: the line has no test.
- `reconcile.py`'s oracle rounds the same way before comparing, so it cannot disagree with line 257.

**Size:** low frequency, real direction. On retrieved closes, keeping half-cents changes 0 of 45 HY-dated rows, 2026-09-02 to 2026-11-03. The closest actual approach to the line is CRWV −15.461% on 2026-10-14, 0.46 points away, the known L4 fire. The error band is about half a cent over the price, so a flip needs a session landing almost on the line with a half-cent close on one of the two dates. No historical grade is affected.

**Letter gap, owner's to settle:** KB-LIQ-069 says "raw unadjusted close (as published, 2dp $)" and "Compare the UNROUNDED ratio". It assumes every close has two decimals and has no half-cent rule. Whether the vendor's half-cents match any official exchange close was not checked; Yahoo is a single mirror.

## What passed

| Check | Result |
|---|---|
| Exact comparator against integer-cent oracle | 958,416 cases, 0 disagreements: prior close $1.00–$600.00, four closes around the line, each of four names, plus HY +4 at ties |
| Synthetic family reconciled | Pre-repair 815 misses on k=10…3000 (reader family) and 814 on k=1…2991 (LIQUID family), same pair construction; candidate 0 on both. LIQUID's "not identical family" caveat is closed |
| Actual sessions | 44 graded 2026-09-02 to 2026-11-03 against an exact-fraction oracle on the normalized closes, 0 disagreements. Only fire 2026-10-14. 2026-09-07 faults closed (not an NYSE session) |
| Comparator mutants | Float revert, `<` for `<=`, `=` for `\|=`, 0.0001 tolerance: all four fail selftest |
| Name independence | Tie meets on each of four names; a hit plus another name's missing bar stays INSTRUMENT-FAULT |
| Hold | CLI prints WITHHELD and exits 4; selftest rc 0. `boot.py` imports only `is_session`; no scripted caller found (`git grep`, non-archive) |

## Acceptance conditions

| Condition | Verdict |
|---|---|
| 1 Decimal interpretation, exact comparison | FAIL at CLI input; PASS in `grade_l4` |
| 2 Boundary cases, no tolerance widening | FAIL at CLI input; PASS in `grade_l4` |
| 3 Any one name; missing data, dates, first-published basis, L1 unchanged | PASS by diff and tests |
| 4 Reconciliation | PASS on outcome, zero grade changes, with corrections below |
| 5 and addendum, operational withholding | PASS |

## Residue, non-blocking

1. "43 retrieved actual sessions" is 42 NYSE sessions plus 2026-09-07 (Labor Day), an INSTRUMENT-FAULT row. `reconcile.py` starts 2026-09-04; condition 4 says September 1. Candidate grades 2026-09-02 and 2026-09-03 NOT FIRED; 2026-09-01 lacks its prior session in this data.
2. `boundary_impact.json` does not disclose that normalization changed six closes.
3. The hold also stops L1 at the CLI. Acceptance condition 5 calls L1 unaffected; the addendum requires the whole CLI to refuse. `reconcile.py` grades L1 through the pure function, so no L1 evidence is lost.
4. NaN now raises `InvalidOperation` in `grade_l4`. `dropna` keeps it out of the CLI path; a crash is not a wrong grade. No action needed.

## Review limits

Read-only against LIQUID's retrieved data; no fresh market pull. Reviewed the repair diff and the L4/L1 paths, not the wider LIQUID desk or other Gate 069 legs. Stubbed the vendor and FRED calls, so live yfinance dtype behaviour was not exercised; the 184 stored closes show its float32 form.

Candidate design lesson, not logged to PATTERNS: a normalization added upstream of a repaired comparator sits outside both the unit test and an oracle built on the same normalized input.
