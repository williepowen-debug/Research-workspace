# STATE VOCABULARY — controlled tokens for machine-read state (fleet build standard)

**Owner:** DAEDALUS · **Created:** 2026-07-31 (Will-approved; provenance: STE/ASD-STE100 adaptation assessment, `design/2026-07-31_STE_WRITING_STANDARD_ASSESSMENT.md` §3A) · **Pattern:** PAT-075.

**Governing rule: where a machine or a cross-agent reader parses the token, the token is an INTERFACE (PAT-069).** Every synonym is a future recognizer-widening or a silent false-negative. This registry fixes ONE canonical token per state for the cross-agent handle and for all NEW surfaces. It is **floor, not ceiling (PAT-015)**: rich local states (HENRY's CRACKING/RE-ARMED, LIQUID's DORMANT→TRIGGERED, VIOLET's 45-pt) stay canonical locally — the registry binds only the comparable handle written *alongside* them, never replaces them.

**Scope:** binds NEW surfaces and cross-agent handles at build/registration time (REGISTRATION_CHECKLIST row 15). Existing files are **grandfathered** — enforcers must keep recognizing the legacy set; nobody rewrites historical tokens (statement-time grades are retained verbatim, fleet practice). Free prose *after* the canonical token is always fine: `FROZEN 2026-07-04 — superseded by X, do not cite rows as current`.

---

## Class 1 — Dead/static surface banners

*Enforcement home: `scripts/ledger_staleness.py` `STATIC_BANNER_MARKERS` (:108). Inventory 2026-07-31, banner-position (first 4 lines), fleet-wide: FROZEN 146 · SUPERSEDED 52 · RETIRED 34 · ARCHIVED 10 · NOT MAINTAINED 4 · DO NOT CITE 4 · NOT CURRENT 2.*

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

---

## Enforcement map (who reads these tokens)

| Class | Machine reader today | Registry obligation |
|---|---|---|
| 1 (banners) | `ledger_staleness.py` recognizer | Recognize canonical + legacy set; SUPERSEDED addition owed (rides TERRY-S1 session) |
| 2 (gates) | greps in sweeps/audits/screens (no single enforcer) | Any NEW check greps the canonical spellings + documents which legacy spellings it covers |
| 3 (predictions) | boot due-scans, scoreboard tooling (per-agent) | New ledgers ship with the token enum in their header comment |

**Build-time check (REGISTRATION_CHECKLIST row 15):** new agents' state-bearing surfaces use canonical tokens; DAEDALUS verifies at registration. Blueprint variants cite this file — they do not restate the tables.
