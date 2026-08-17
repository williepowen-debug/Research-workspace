# STATE VOCABULARY — controlled tokens for machine-read state (fleet build standard)

**Owner:** DAEDALUS · **Created:** 2026-07-31 (Will-approved; provenance: STE/ASD-STE100 adaptation assessment, `design/2026-07-31_STE_WRITING_STANDARD_ASSESSMENT.md` §3A) · **Pattern:** PAT-075.

**Governing rule: where a machine or a cross-agent reader parses the token, the token is an INTERFACE (PAT-069).** Every synonym is a future recognizer-widening or a silent false-negative. This registry fixes ONE canonical token per state for the cross-agent handle and for all NEW surfaces. It is **floor, not ceiling (PAT-015)**: rich local states (HENRY's CRACKING/RE-ARMED, LIQUID's DORMANT→TRIGGERED, VIOLET's 45-pt) stay canonical locally — the registry binds only the comparable handle written *alongside* them, never replaces them.

**Scope:** binds NEW surfaces and cross-agent handles at build/registration time (REGISTRATION_CHECKLIST row 15). Existing files are **grandfathered** — enforcers must keep recognizing the legacy set; nobody rewrites historical tokens (statement-time grades are retained verbatim, fleet practice). Free prose *after* the canonical token is always fine: `FROZEN 2026-07-04 — superseded by X, do not cite rows as current`.

---

## Class 1 — Dead/static surface banners

*Enforcement home: `scripts/ledger_staleness.py` `STATIC_BANNER_MARKERS` (cite the symbol, not a line number — it moves). Inventory 2026-07-31, banner-position (first 4 lines), fleet-wide: FROZEN 146 · SUPERSEDED 52 · RETIRED 34 · ARCHIVED 10 · NOT MAINTAINED 4 · DO NOT CITE 4 · NOT CURRENT 2.*

| Canonical token | Meaning (one each — the STE rule) | Banner must carry |
|---|---|---|
| `FROZEN <date>` | Static snapshot, not maintained. **No successor implied.** | Date + one-line why + where truth lives now |
| `SUPERSEDED <date>` | Replaced by a **named successor** — go there. | Date + **the successor's path** (a SUPERSEDED banner without a successor pointer is a defect) |
| `RETIRED <date>` | Role/surface ended by decision. No successor. | Date + the deciding ruling/session |

- **Legacy, recognized but not for new surfaces:** `NOT CURRENT` · `DO NOT CITE` · `NOT MAINTAINED` · `ARCHIVED` (as primary token — `archive/` the *directory* is unaffected). The recognizer keeps them (PAT-035/059 widenings stand); new surfaces pick from the canonical three.
- **Not state tokens (never as primary banner token):** `DEAD` · `OBSOLETE` · `DEPRECATED` — fine as prose after a canonical token.
- ✅ **SUPERSEDED recognizer gap CLOSED same day (2026-07-31, TERRY-S1 session as planned):** `SUPERSEDED` added to `STATIC_BANNER_MARKERS` under the existing banner-form guards; fleet-validated — zero live flips (confirming the gap was latent), synthetic capable-case passes, trade-mode output byte-identical.

## Class 2 — Gate / trigger states

*Inventory 2026-07-31 (GATES.tsv + all STATUS.md): FIRED 136 · ARMED 97 · **negative pole split four ways:** `NOT FIRED` 42 · `NOT-FIRED` 40 · `NO-FIRE` 13 · `UNFIRED` 12 · RE-ARMED 10 · STOOD DOWN 2 · DISARMED 1 · TRIGGERED 1. Any grep for one negative form silently misses half the fleet — the exact PAT-074 shape (a scan's clean PASS meaning "searched the wrong spelling").*

| Canonical token | Meaning |
|---|---|
| `ARMED` | Gate registered and watching; condition not yet met |
| `FIRED` | Condition met (carry the date + level: `FIRED 7/28 @ 281bp`) |
| `NOT-FIRED` | Evaluated, condition not met. **Hyphenated — one spelling.** (Chosen because the blueprint's donor triad, market-agent §4/HENRY, already writes `FIRED / NOT-FIRED`) |
| `STOOD-DOWN` | Deliberately disarmed (carry the ruling). Distinct from NOT-FIRED |

- `TRIGGERED` → use `FIRED`. `UNFIRED` / `NO-FIRE` / `NOT FIRED` (spaced) → use `NOT-FIRED` on new surfaces.
- **Local richness protected (PAT-015):** HENRY's `CRACKING`/`RE-ARMED`, LIQUID's `DORMANT→TRIGGERED` ladder, and any agent's richer state machine stay canonical in their own files — the registry token is the *cross-agent handle* written beside them, and a re-arm cycle is legitimately `FIRED → STOOD-DOWN → ARMED (re-armed <date>)`.

## Class 3 — Prediction resolution states

*Inventory 2026-07-31, PREDICTIONS status columns fleet-wide: ~5 synonyms per pole (HIT/CORRECT/TRUE/CONFIRMED vs MISS/WRONG/FALSE/FALSIFIED/DISCONFIRMED) + free-prose outcomes in status cells. Grading DISCIPLINE canon lives in `FORGE/PREDICTION_DISCIPLINE.md` (PROME/FORGE-lane) — this registry owns only the build-standard token set for NEW ledgers.*

| Canonical token | Meaning |
|---|---|
| `OPEN` | Live, resolution date/condition not reached |
| `HIT` | Resolved true as written (the letter, not the thesis — [[finding_confidence_priced_against_thesis_not_letter]]) |
| `MISS` | Resolved false as written |
| `VOID` | Premise failed / unresolvable as specified — excluded from Brier (carry the reason: `VOID (premise-mismatch)`) |
| `STUCK` | Cannot resolve because window/instrument broke — a STATUS state, never a confidence cut ([[finding_resolvability_defect_is_status_not_confidence]]) |

- Nuance rides a parenthetical, not a new token: `HIT (letter; thesis-partial)`, `MISS (direction right, magnitude short)`. Narrative outcomes go in the Outcome/Notes column — **the Status cell holds ONLY a registry token.**
- **Historical rows are never rewritten** — grades stand verbatim as made; the registry binds new ledgers and new rows in ledgers that adopt it.

## Class 4 — Queue / disposition states (added 2026-08-12; provenance: LABOR L-16 via PROME — one wrong word re-queued a finished judgment SIX times)

*The defining defect: LABOR's SIG-006 was parked six times across six sessions while its 7/31 board_log row already held a complete merits assessment — the filing token was `deferred`, which is NON-TERMINAL, so finished work re-entered the queue five more times. The interface property this class adds: **every disposition token is marked TERMINAL or NON-TERMINAL, and queue tooling may enforce that mechanically** (a NON-TERMINAL token on a row older than ~2 sessions is a re-queue candidate; a TERMINAL token never re-queues).*

| Canonical token | Meaning | Terminal? |
|---|---|---|
| `QUEUED` | Awaiting assessment | NON-TERMINAL |
| `DEFERRED <until/condition>` | **Not yet assessed**, deliberately postponed — must carry a re-look date or condition | NON-TERMINAL |
| `NO-ACTION <date>` | **Assessed on merits; nothing warranted. Do not re-queue.** The token L-16 was missing | TERMINAL |
| `DONE <date>` | Assessed and acted; record where | TERMINAL |

- The trap this exists to kill: using `DEFERRED` to mean "I looked, nothing to do." That is `NO-ACTION`. `DEFERRED` asserts the assessment has NOT happened yet.
- **Local richness protected (PAT-015):** WALTER's KILL/DISPATCH/FOLD lane vocabulary and any agent's richer disposition ladder stay canonical locally (WALTER's spec is its own, unchanged) — this class binds NEW queue/board_log-shaped surfaces and the cross-agent handle, per the standing scope rule above.
- Fleet cross-check candidate (registered, not yet run): grep queues/board_logs for `deferred` rows older than ~2 sessions whose notes read like completed assessments — LABOR's n=6 says the class is not rare.

## Class 5 — Zero / UNKNOWN / not-applicable distinction (added 2026-08-14; ruling: `PROME/proposals/2026-08-12_audit-convention-RULED.md` §Ruling 1; provenance: BRENT AUDIT_2026-08-12b I-1/I-4/I-5, first-application vocabulary in BRENT's 8/13 encode-confirm packet)

*The defining defect: `0` in a quantitative column can mean six different things — a real measured zero, a restored-to-zero, an intact-and-untouched zero, an anti-double-count zero, an unmeasured cell, or a wrong-unit cell — and a blank is a seventh. BRENT hit all six on one file (INCIDENTS): a 77-MTPA LNG force majeure stored as `0` in a `bpd` column, 13 blank rows summing as zeros in downstream reads, and one `0` token carrying four meanings on adjacent rows. The interface property this class adds: **a quantitative column MUST carry a state token beside its value; `0` alone is not a claim.** New quantitative columns ship with the enum in their header; legacy grandfathered per standing scope rule.*

| Canonical token | Meaning | The distinction it protects |
|---|---|---|
| `MEASURED` | A real, measured number — **including a genuine measured 0** | Zero-as-observed is a datum, not a gap |
| `ZERO-RESTORED` | 0 because the facility was restored / the incident RESOLVED | Distinguishes "back to normal" from "never damaged" |
| `ZERO-INTACT` | 0 because nothing was damaged — attacked-and-spared, or a watch row with no loss | Preserves that an event was evaluated and produced no loss |
| `ZERO-NODOUBLECOUNT` | **Deliberately** 0: quantity already carried on an earlier row for the same key | Prevents an anti-double-count from being aggregated as absence |
| `UNKNOWN` | Unit is right; nobody has ever measured it. **NOT zero.** | Kills the silent-zero-from-blank aggregation defect |
| `NA-WRONG-UNIT` | Asset is real but **not denominable in this column's unit** — read the paired unit/qty column | Kills the 77-MTPA-in-bpd class |
| `UNLOGGED` | Blank: never published or attempted. **NOT zero, NOT unknown-after-looking.** | Distinguishes "we did not try" from "we tried, no answer" |

- **Adopted spellings verbatim from BRENT's first application** (his ASK: canonical vs local — the distinctions are the ruling, spellings were not). Rename-in-place is prohibited by the anti-ratchet rider: existing legacy blanks and bare `0`s are grandfathered; the class binds NEW quantitative columns and any column undergoing a next-write.
- **A candidate 8th token — quiescent watch row (event never occurred vs event evaluated with zero loss)** — is deliberately NOT added on n=1. If a second desk hits the distinction, promote per PAT-089. Until then, BRENT-style watch rows use `ZERO-INTACT`.
- **In force immediately, no encode needed (fleet-binding restatement from the ruling):** no aggregate over a column carrying these tokens is quotable until the schema declares its unit — the tokens make units visible, they do not make the file summable.
- **Local richness protected (PAT-015):** rich domain vocabularies (BRENT's `facility_key`, MIDAS's provenance ladder, any richer categorical alongside the token) stay canonical locally; this class binds only the state-token beside the number.

## Class 6 — Source-authority distinction (added 2026-08-14; ruling: `PROME/proposals/2026-08-14_rows-49-50-RULED.md` §Row 49; provenance: HOMER 2026-08-14 issuer-primary-sourcing PROPOSAL, first application on `AGENTS/HOMER/workbook/RATES.tsv` from 2026-08-13)

*The defining defect: a mirror-as-primary delivers correct numbers stripped of the issuer's caveats. HOMER's live example (8/13): FRED's bare `6.67%` PMMS print vs Freddie's release carrying "applications rising" — same number, materially different read.* **This class is the state-token half of the convention; the writing rule lives in `STRICT_TEXT.md` rule 6 (issuer-primary-where-reachable).**

| Canonical token | Meaning | Attached to |
|---|---|---|
| `PRIMARY` | Cited to the issuer of record (Freddie for PMMS, Treasury for DGS, USBR for Powell, etc.) | Any load-bearing figure |
| `MIRROR` | Cited to an aggregator (FRED, Yahoo, vendor cache) — issuer reachable but not read | Non-load-bearing figures; mirror is acceptable |
| `MIRROR-WALLED` | Cited to an aggregator because the issuer is unreachable (403, paywall, no API) — carry the wall note | Load-bearing figures where the primary is genuinely blocked |

- **Next-write-only** — no retroactive sweep; existing citations grandfathered; the token governs each figure's next write.
- **The "where reachable" carve-out is load-bearing (`finding_blocked_mirror_is_not_an_unreachable_primary`):** `MIRROR-WALLED` is legitimate; using `MIRROR` when the issuer IS reachable is the defect this class kills. A 403 is a fact about ONE host — try the API and enumerate before writing `MIRROR-WALLED`.
- **Load-bearing = writes into a THRESHOLD, a prediction letter, a Will-facing synthesis, or a downstream agent's inbox.** Prose citations in research/audit narratives are exempt (STRICT_TEXT scope rule).

---

## Enforcement map (who reads these tokens)

| Class | Machine reader today | Registry obligation |
|---|---|---|
| 1 (banners) | `ledger_staleness.py` recognizer | Recognize canonical + legacy set; SUPERSEDED addition owed (rides TERRY-S1 session) |
| 2 (gates) | greps in sweeps/audits/screens (no single enforcer) | Any NEW check greps the canonical spellings + documents which legacy spellings it covers |
| 3 (predictions) | boot due-scans, scoreboard tooling (per-agent) | New ledgers ship with the token enum in their header comment |
| 4 (queue/disposition) | queue re-scan tooling, board_log audits (per-agent today; no single enforcer) | New queue surfaces ship the enum + TERMINAL marking in their header comment; any re-queue tooling keys on the TERMINAL flag, never on token spelling |
| 5 (zero/UNKNOWN/NA) | ⛔ **UNBUILT — CORRECTED 2026-08-17: `basis_check` never shipped as code** (BRENT-confirmed — class-5 tokens live as INCIDENTS.tsv column enum + prose, no script check exists; this cell previously named it as the ruled enforcement arm, and the correction sat in an overflow 4th cell GFM silently dropped at render — self-audit F25). Candidate home rides the forum-4 #11 registration-checklist build; extend an existing checker per anti-ratchet rider | New quantitative TSV columns ship the enum in a header comment; existing columns adopting the class name what they supersede |
| 6 (source authority) | No dedicated enforcer today — reader-side convention; a fleet grep for `PRIMARY`\|`MIRROR`\|`MIRROR-WALLED` on threshold rows is a candidate follow-on *(pipes escaped 2026-08-17 — unescaped they split this row and GFM dropped the obligation cell, self-audit F25)* | New citations on load-bearing figures carry one of the three tokens; HOMER `RATES.tsv` (`workbook/`) is the first-application worked example |

**Build-time check (REGISTRATION_CHECKLIST row 15):** new agents' state-bearing surfaces use canonical tokens; DAEDALUS verifies at registration. Blueprint variants cite this file — they do not restate the tables.
