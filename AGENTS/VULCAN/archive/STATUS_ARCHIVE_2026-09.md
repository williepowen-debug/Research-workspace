# VULCAN — STATUS ARCHIVE 2026-09

> **FROZEN — never cite a row here as current.** `STATUS.md` is canonical for SCORE, BAND STATE and FIRED-COUNT; this file holds session RECORDS rotated off it under READ_CAP rules 16-17.

---

## ROTATED 2026-09-06 from `STATUS.md` §0c — VERBATIM, crc32 `0x26842de0`, 1,976 B
> Cut because STATUS hit **33,229 B vs a 32,550 B budget** — pushed over by the session's own correction text. **History moved, state kept:** a list of already-fixed defects is not a score, a band or an owed item, so it is exactly what a canonical live-state surface should shed first.

**0c-2026-09-06. FOUR INSTRUMENT DEFECTS FOUND AND FIXED THIS SESSION — three of them in my own guards.**
1. 🔴 **`scripts/validate_workbook.py` could not grade an EMPTY ledger.** It took the header from `data[0].keys()`, so a ledger with a **correct** header and zero rows reported **every** declared column as missing — a header-drift ERROR against a perfect header. That made the correct discipline (create the ledger and pre-commit the cadence *before* the first row) impossible to satisfy cleanly. Fixed to read the header from the file. **Falsified by 3 injections — wrong header / empty file / ragged row — 3 of 3 fire, no false positive.**
2. 🔴 **And my own fix printed a false certification**, caught by injection 1: the new *"header conforms, ZERO data rows"* note was emitted **before** the drift check, so it said *"header conforms"* over a header that did not. **Reordered.** `[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]` — and it is the fix that produced it, which is `[[finding_a_correction_pass_is_unreviewed_work]]` measured on myself inside one session.
3. 🔴 **`scripts/catalyst_countdown.py` had NO market-holiday calendar** — `trading_days_between()` counted weekdays only. On Sunday 9/6 it reported 9/08 as **2d trd** while **9/07 was Labor Day**. Every trading-day distance past the next holiday was overstated, **silently and in the reassuring direction**. Fixed with a **rule-based** NYSE calendar (not a hardcoded year list, which is a dated carry item that goes stale without saying so); **verified against an independently derived 2026 list — exact 10/10 match**; 2027 spot-checked. Ad-hoc closures and half-days named as not modelled.
4. 🟠 **My own `semi_watch.py` cadence was 3-of-8 registered.** Five slots existed only in CLAUDE.md prose with **no surfacing mechanism** — the same PAT-063 transport gap this desk raised with DAEDALUS on 8/21, reproduced on my own rule. All five now registered.


---

## ROTATED 2026-09-06 from `STATUS.md` — prior session header — VERBATIM, crc32 `0xb37d1695`, 684 B
> Cut under READ_CAP rules 16-17. **History moved, state kept.** Rule-17 check: no owed item, standing rule or dated commitment is stated only here.

**Prior header, retained:** session spans 2026-09-02 22:47 ET → 2026-09-03 07:1x ET — stated as a span, not a point, because the clock crossed midnight mid-session and picking one date would be the narrative rather than the clock *(`[[finding_write_timestamps_from_the_clock_not_the_narrative]]`; every `date` call is in the record)*. **Analysis and market reads are 2026-09-02 vintage; the closeout is 2026-09-03.** (**PROME-orchestrated full owner session after 6 dark days.** VULCAN-16 GRADED · MU FQ4 date CONFIRMED at the issuer primary and it REFUTES my own 8/27 re-derivation · S1 YELLOW band TRIPPED on its registered trigger · READ-CAP split executed · inbox 17→0)

---

## ROTATED 2026-09-06 from `STATUS.md` — delivered-this-session list — VERBATIM, crc32 `0x54414857`, 691 B
> Cut under READ_CAP rules 16-17. **History moved, state kept.** Rule-17 check: no owed item, standing rule or dated commitment is stated only here.

✅ *Delivered this session:* **WALTER lane drained 4/4** with dispositions and reasons · **`SIG-W-20260904-001` CONTESTED at the primary and refuted on its load-bearing cell** (packets to WALTER, cc DEWEY + ZHAO) · **WATT's seam wording adopted verbatim on 8 surfaces + the 33-day provenance disclosed** · **VIOLET's inverted-headroom flag applied to 3 prediction rows + the brief** · **DAEDALUS answered** (lesson phrasing with a testable discriminator · `S4_SERIES` owner-confirm · profile trigger re-dated · the seam defect disclosed against my own grade) · **the GPU-rental instrument ENCODED** (11th ledger, schema, spec, cadence pre-committed, registered, surfacing at boot).
