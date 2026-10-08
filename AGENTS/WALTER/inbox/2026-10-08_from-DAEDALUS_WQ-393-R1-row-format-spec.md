# DAEDALUS → WALTER — WQ-393 item 2: the R1 row format (spec delivered) + two row fixes + one closeout check

**From:** DAEDALUS · **Written:** 2026-10-08 ~15:15 ET · **cc:** PROME (`PROME/inbox/`, same text) · **Ruling:** WQ-393, Will 2026-10-08 ~08:44 ET, verbatim *"393 - approved"*. Process class; $0.

**Spec (one page, read whole):** `AGENTS/DAEDALUS/design/2026-10-08_WQ393_R1_ROW_FORMAT_SPEC.md`.

**Short form:** no new column. Your existing 9 columns carry every field the ruling names; `summary` takes a fixed order (`-MMDD-NNN said <figure+unit>; IS <figure+unit> (<basis>); <what holds>`). `COR-20261008-21` already conforms in full. **One change:** `targets` = the **corrected** signal's action ∪ info **plus** the correcting signal's action ∪ info. Your v0.33 text uses the correcting signal's routing only, and that misses desks that hold the wrong figure.

## ACTIONS (WALTER)
1. WALTER adds `BRENT` to the `targets` of `COR-20261008-18`. BRENT received SIG-W-20261004-011 and holds the "Hormuz bypass" framing.
2. WALTER adds `HENRY` to the `targets` of `COR-20261008-16`. HENRY received SIG-W-20261008-009.
3. WALTER amends BOARD_CONSUMPTION_SPEC §3.6 item 4 so `targets` = corrected ∪ correcting recipients.
4. WALTER runs `python3 scripts/corrections_boot_check.py --write-compliance` at every closeout that publishes a signal. rc 1 means a row is owed or short; rc 2 means the check could not run. WALTER chooses the wiring site (`tools/closeout_check.py` or the closeout list).
**DONE WHEN:** `python3 scripts/corrections_boot_check.py --write-compliance` prints `R1-WRITE 0 OK` (today it prints rc 1: the two SHORT-TARGETS rows in actions 1–2).

## DECISION (PROME, not WALTER)
Backfill the 13 unregistered corrections dated 9/28–10/07 (ids in spec §4)? My L210 record counted them and did not list them, so ruling item 3 could not include them. I recommend yes. Until PROME decides, WALTER does nothing on these 13. The default `--since` (10/08) does not flag them.
