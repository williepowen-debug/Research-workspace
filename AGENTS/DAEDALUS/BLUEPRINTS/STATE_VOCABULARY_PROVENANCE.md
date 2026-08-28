# STATE VOCABULARY — PROVENANCE (cold half; the hot file cites, this one explains)

**Owner:** DAEDALUS · **Split 2026-08-28** at the wiring sweep (leg ②): `STATE_VOCABULARY.md` sat at 58% of the harness read cap and the ② mints would have pushed it past the 60% budget. Every class heading's ruling/provenance tail and every leading *defining-defect / inventory* paragraph moved here VERBATIM, keyed by class; the hot file keeps headings, tables and operative rules. ⛔ Never re-inline — add new provenance HERE. Read on demand (`grep -n '^## Class N' STATE_VOCABULARY_PROVENANCE.md`).

### Class 1 extension — surface-role enum

**Heading tail (verbatim):** (EXTENDED 2026-08-22; ruling: Will verbatim "ok both approved" 14:34 EDT, `PROME/codex/2026-08-21_RAV_operating-improvements-feedback.md` §MINTED; provenance: RAV item 1, census-first draft `design/2026-08-22_CLASS11_12_ENUM_SITTING_DRAFT.md`. EXTENDS this class's field-family — ruled no fork)

## Class 1 — Dead/static surface banners

*Enforcement home: `scripts/ledger_staleness.py` `STATIC_BANNER_MARKERS` (cite the symbol, not a line number — it moves). Inventory 2026-07-31, banner-position (first 4 lines), fleet-wide: FROZEN 146 · SUPERSEDED 52 · RETIRED 34 · ARCHIVED 10 · NOT MAINTAINED 4 · DO NOT CITE 4 · NOT CURRENT 2.*

## Class 2 — Gate / trigger states

*Inventory 2026-07-31 (GATES.tsv + all STATUS.md): FIRED 136 · ARMED 97 · **negative pole split four ways:** `NOT FIRED` 42 · `NOT-FIRED` 40 · `NO-FIRE` 13 · `UNFIRED` 12 · RE-ARMED 10 · STOOD DOWN 2 · DISARMED 1 · TRIGGERED 1. Any grep for one negative form silently misses half the fleet — the exact PAT-074 shape (a scan's clean PASS meaning "searched the wrong spelling").*

## Class 3 — Prediction resolution states

*Inventory 2026-07-31, PREDICTIONS status columns fleet-wide: ~5 synonyms per pole (HIT/CORRECT/TRUE/CONFIRMED vs MISS/WRONG/FALSE/FALSIFIED/DISCONFIRMED) + free-prose outcomes in status cells. Grading DISCIPLINE canon lives in `FORGE/PREDICTION_DISCIPLINE.md` (PROME/FORGE-lane) — this registry owns only the build-standard token set for NEW ledgers.*

## Class 4 — Queue / disposition states

**Heading tail (verbatim):** (added 2026-08-12; provenance: LABOR L-16 via PROME — one wrong word re-queued a finished judgment SIX times)

*The defining defect: LABOR's SIG-006 was parked six times across six sessions while its 7/31 board_log row already held a complete merits assessment — the filing token was `deferred`, which is NON-TERMINAL, so finished work re-entered the queue five more times. The interface property this class adds: **every disposition token is marked TERMINAL or NON-TERMINAL, and queue tooling may enforce that mechanically** (a NON-TERMINAL token on a row older than ~2 sessions is a re-queue candidate; a TERMINAL token never re-queues).*

## Class 5 — Zero / UNKNOWN / not-applicable distinction

**Heading tail (verbatim):** (added 2026-08-14; ruling: `PROME/proposals/2026-08-12_audit-convention-RULED.md` §Ruling 1; provenance: BRENT AUDIT_2026-08-12b I-1/I-4/I-5, first-application vocabulary in BRENT's 8/13 encode-confirm packet)

*The defining defect: `0` in a quantitative column can mean six different things — a real measured zero, a restored-to-zero, an intact-and-untouched zero, an anti-double-count zero, an unmeasured cell, or a wrong-unit cell — and a blank is a seventh. BRENT hit all six on one file (INCIDENTS): a 77-MTPA LNG force majeure stored as `0` in a `bpd` column, 13 blank rows summing as zeros in downstream reads, and one `0` token carrying four meanings on adjacent rows. The interface property this class adds: **a quantitative column MUST carry a state token beside its value; `0` alone is not a claim.** New quantitative columns ship with the enum in their header; legacy grandfathered per standing scope rule.*

## Class 6 — Source-authority distinction

**Heading tail (verbatim):** (added 2026-08-14; ruling: `PROME/proposals/2026-08-14_rows-49-50-RULED.md` §Row 49; provenance: HOMER 2026-08-14 issuer-primary-sourcing PROPOSAL, first application on `AGENTS/HOMER/workbook/RATES.tsv` from 2026-08-13)

*The defining defect: a mirror-as-primary delivers correct numbers stripped of the issuer's caveats. HOMER's live example (8/13): FRED's bare `6.67%` PMMS print vs Freddie's release carrying "applications rising" — same number, materially different read.* **This class is the state-token half of the convention; the writing rule lives in `STRICT_TEXT.md` rule 6 (issuer-primary-where-reachable).**

## Class 7 — Gate-registry envelope: scannability

**Heading tail (verbatim):** (added 2026-08-20; ruling: Will in-session "Approved" on `AGENTS/DAEDALUS/design/2026-08-20_GATE_REGISTRY_ADJUDICATION.md`; provenance: WALTER 8/19 Will-routed measurement + CREED 8/20 untrippable-row finding; first application = `PROME/GATES.tsv` `scannable` column)

## Class 8 — Ledger cadence declaration

**Heading tail (verbatim):** (added 2026-08-20; provenance: OSPREY+HAWK ledger-nudge day-one field report via PROME, `AGENTS/OSPREY/outbox/2026-08-20_to-PROME_ledger-nudge-caveat-event-driven-surfaces.md`; first application = the mechanism's motivating surface, OSPREY `workbook/WARRISK.tsv`, owner-adopted)

## Class 9 — Marker-role separation: severity vs priority

**Heading tail (verbatim):** (added 2026-08-21; ruling: Will in-session, AskUserQuestion "Forward-only, P1/P2/P3 text" selected off the DAEDALUS rec; provenance: ZHAO 8/21 S8 implementation `9f97c7f5f` via PROME — a stdout-scrape verdict read permanent-REVIEW because §4 prints 🔴 as a PRIORITY glyph on healthy forward catalysts; the fleet's emoji vocabulary double-served as severity marker AND priority marker)

## Class 10 — Assertion-row contract: standing-state rows

**Heading tail (verbatim):** (added 2026-08-21; ruling: forum-6 R6, in-lane per `FORUM/2026-08-17_correction-propagation/04_synthesis/06_PROME_rulings-record.md` — "PROME lane + blueprint-encode at DAEDALUS's next touch"; this section IS that touch. Provenance: forum-6 incident I-3 — a "corrections owed" row outlived its 8/10 completion by 7 days and produced a duplicate packet, a duplicate banner, and a publicly-owned delay that never happened)

## Class 11 — Consumption-state ladder

**Heading tail (verbatim):** (added 2026-08-22; ruling: Will verbatim **"ok both approved"** 14:34 EDT, `PROME/codex/2026-08-21_RAV_operating-improvements-feedback.md` §MINTED; provenance: RAV item 3; census-first draft `design/2026-08-22_CLASS11_12_ENUM_SITTING_DRAFT.md` — tokens mined from measured fleet usage, census 2026-08-22)

## Class 12 — Verification-basis

**Heading tail (verbatim):** (added 2026-08-22; same ruling §MINTED; provenance: RAV items 2+8 merged; census-first draft ibid.)

### Class 5 — relocated 2026-08-28 (adopted-spellings + 8th-token note, verbatim)

- **Adopted spellings verbatim from BRENT's first application** (his ASK: canonical vs local — the distinctions are the ruling, spellings were not). Rename-in-place is prohibited by the anti-ratchet rider: existing legacy blanks and bare `0`s are grandfathered; the class binds NEW quantitative columns and any column undergoing a next-write.
- **A candidate 8th token — quiescent watch row (event never occurred vs event evaluated with zero loss)** — is deliberately NOT added on n=1. If a second desk hits the distinction, promote per PAT-089. Until then, BRENT-style watch rows use `ZERO-INTACT`.

