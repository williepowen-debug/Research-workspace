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



## Rotated 2026-09-01 (hot file at 99.4% of budget before the WQ-140 / WQ-117 C / WQ-148 registrations; verbatim, never edited)

### Class 2 exemplars bullet
- **Three exemplars promoted to canon 2026-08-28 (Falsification #2 ⭐, wiring-sweep ②):** **AEOLUS** renders `CANNOT FIRE` vs `NOT FIRED` per leg (spelling normalises to the hyphenated tokens above on next-write); **HENRY** publishes per-leg live counts under an explicit **non-latching AND** rule (a fired leg does not stay fired for the conjunction; every leg is re-tested at every evaluation); **VULCAN**'s dated retrofit rail (a band re-keyed AFTER registration carries the retrofit date on the row, so a fire can be read against the band that was live when it fired). Display form (AEOLUS): `total · range · moved · fired` beside any convergence score.

### Class 9 rider narrative
⚠️ **Enforcement is FORWARD-ONLY (Will-ruled): new surfaces and next-writes conform; legacy is grandfathered — NO retroactive fleet sweep.** **Template-surface rider (added same day, ZHAO `9c5bd623d` — refines the ruling's application, does not reinstate a sweep): on a surface whose EXISTING ROWS ARE THE TEMPLATE FOR NEW ONES (TSVs, registries, schema-bearing files), forward-only is defeated by copy-the-neighbour — the next writer consults the row above, not the ruling, so grandfathered rows TEACH non-conformance. Rider: conform-on-touch, OR conform-now-while-the-author-is-still-holding-it (ZHAO's own 10-cell conversion cost ten minutes, four hours after authoring). Prose surfaces are exempt — a stale paragraph is not copied into the next paragraph. Kin: `finding_a_ruling_governs_the_next_write_not_the_existing_state` (64% compliance hours after the author's own ruling — template-copying is the hypothesized driver, n=1, testable at the 8/28 ⑫ walk).** Rationale on the record: 🔴-as-priority exists on hundreds of legacy surfaces (packet headers, HEARTBEAT, DOCKET, dashboards); a big-bang re-mark creates a mixed-vocabulary transition worse for every scraper than one dirty vocabulary, and the grandfather-forward pattern is how every prior class of this file healed. **Companion rule, NOT restated here:** verdicts key on alert COUNTS returned by code, never on scraping output for glyphs — that is CHECK_STANDARD §8 territory (encode at the ⑤b sitting); this class fixes the vocabulary, that rule fixes the mechanism, and neither substitutes for the other (a clean vocabulary still collides in quoted/historical text).

### Class 11 don't-mints
**Don't-mints on the record (ruled):** `CREATED` (census 0 — a state nobody records) · `READ` (collapses into CONSUMED) · `ANSWERED` (a prose verb — an answer is itself a packet with its own ladder) · `OWNER-ENCODED` (RAV's spelling; `ENCODE-CONFIRMED` survives, 17 vs 4) · **`UNPROCESSED` (ruled NOT minted — it is `DELIVERED` + age; the unfiled-vs-unprocessed distinction resolves at the METRIC layer: the fleet_triage metric is named `delivered_unread`; "unprocessed" stays legal prose).**

### Class 11 first exemplar
First live exemplar (citable): the 2026-08-22 encode-ask packet's own ladder — ROUTED at commit `7f963e93a` → DELIVERED at DAEDALUS `inbox/` → CONSUMED at this encode session → ENCODE-CONFIRMED at this section's commit.

### Class 10 deployment paragraph
⚠️ **Rows that EXPIRE or are re-derived at read time (fire-ledger rows, artifact-verify-per-presentation) are already conformant** — the class targets rows that ASSERT; that is where the rot concentrates (forum-6 P1 measurement). Deployment, not invention: GATES `consumed_by` + WILL_QUEUE artifact-verify-per-presentation are this contract already working on two surfaces.

### WQ-117 C provenance
Ruling row text (PROME/proposals/2026-09-01_wq-batch-RULED.md row 117) quotes the pre-RAV single-axis wording *"operating-mode axis MACHINE-MONITORED / OWNER-GRADED / EVENT-SUMMONED"*; the bundle Will approved *"with your recs"* (`design/2026-08-28_late-batch-three-encodes-for-Will.md` §C) recommends the RAV-redesigned two-axis form (Trigger ∈ {SCHEDULED, EVENT, MANUAL} + the existing INSTRUMENT/JUDGEMENT adjudicator). Encoded per the rec; flagged to PROME 2026-09-01 so the two texts cannot be read as two rulings.


## Rotated 2026-09-01 — second pass (the first pass left the hot file at 34,781 B = 106.9%; the commit message `4d937cb91` claimed 'under budget' and was WRONG — corrected here, never amended)

### Class 2 Trigger provenance clause
(WQ-117 C, Will 2026-09-01 *"approve … with your recs"* — the rec being the RAV-redesigned two-axis form in `design/2026-08-28_late-batch-three-encodes-for-Will.md` §C; PROME's ruling-row label quotes the pre-redesign single-axis wording, flagged 9/1):

### Class 12 don't-mints
**Don't-mints on the record (ruled):** `UNVERIFIED` as a token (census 1,591 but generic — it cannot discriminate `OWNER-ASSERTED` from `UNANCHORED`, the exact distinction this class exists to make; stays prose) · `MARKET-DATA-CURRENT-AS-OF` (a timestamp practice, governed by PAT-044 + root pricing rules — not a state).

### Class 12 neighbour
**Neighbour reconciliation (Class 6):** Class 6 declares the SOURCE a figure cites (`PRIMARY`/`MIRROR`/`MIRROR-WALLED`); Class 12 declares the CHECKING performed on a claim. A `MIRROR`-cited figure can later be `PRIMARY-VERIFIED`; the two compose, neither substitutes.

### Class 8 scope paragraph
⚠️ **Scope: the declaration affects `ledger_staleness.py --nudge` ONLY** (distinct ℹ️ label, not counted behind — a check structurally always-red on one surface trains skipping on every surface, PAT-110's inverse). The `--days`/`--writes`/`--abs-floor` scans still grade the file — the owner's dispositions there stay "refresh / freeze / say why not." The declaration is a FORM, not a keyword (PAT-059): `Cadence:`-prefixed, front-loaded (col ≤100), header-block only — bare prose "event-driven" mentions do not declare (measured live: WARRISK's own caveat prose would have self-declared under a bare-token match).

### Enforcement map Class 5 row
| 5 (zero/UNKNOWN/NA) | ⛔ **UNBUILT — CORRECTED 2026-08-17: `basis_check` never shipped as code** (BRENT-confirmed — class-5 tokens live as INCIDENTS.tsv column enum + prose, no script check exists; this cell previously named it as the ruled enforcement arm, and the correction sat in an overflow 4th cell GFM silently dropped at render — self-audit F25). Candidate home rides the forum-4 #11 registration-checklist build; extend an existing checker per anti-ratchet rider | New quantitative TSV columns ship the enum in a header comment; existing columns adopting the class name what they supersede |

### Enforcement map Class 6 row
| 6 (source authority) | No dedicated enforcer today — reader-side convention; a fleet grep for `PRIMARY`\|`MIRROR`\|`MIRROR-WALLED` on threshold rows is a candidate follow-on *(pipes escaped 2026-08-17 — unescaped they split this row and GFM dropped the obligation cell, self-audit F25)* | New citations on load-bearing figures carry one of the three tokens; HOMER `RATES.tsv` (`workbook/`) is the first-application worked example |

### Class 13 neighbour
**Neighbour reconciliation (Class 12):** Class 12 says what KIND of checking backs a load-bearing claim (`ARTIFACT-VERIFIED` vs `PRIMARY-VERIFIED` …); Class 13 says how far THIS session's check went on THIS claim — a Class-13 `VERIFIED` on a repo artifact is Class-12 `ARTIFACT-VERIFIED`, never `PRIMARY-VERIFIED`. They compose. Machine reader today: none — reader-side convention on packets/reports; candidate rider on the forum-4 #11 registration checklist.
