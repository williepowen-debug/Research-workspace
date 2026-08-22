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

### Class 1 extension — surface-role enum (EXTENDED 2026-08-22; ruling: Will verbatim "ok both approved" 14:34 EDT, `PROME/codex/2026-08-21_RAV_operating-improvements-feedback.md` §MINTED; provenance: RAV item 1, census-first draft `design/2026-08-22_CLASS11_12_ENUM_SITTING_DRAFT.md`. EXTENDS this class's field-family — ruled no fork)

Role labels declaring what a surface IS, joining the banner family that declares that one died:

| Canonical token | Meaning | Census basis |
|---|---|---|
| `CANONICAL` | Owner-of-record surface for its facts — resolve conflicts HERE (`finding_owner_of_record_means_authoritative_not_correct` still applies: authoritative ≠ correct) | 139 |
| `DERIVED` | Regenerated/join surface — edit the sources, never this file. `GENERATED` = the machine-written **subtype**, declared via the established "GENERATED — do not hand-edit" banner form (subtype, not a separate token) | 185 (+38) |
| `SCRATCH` | Working surface; no cross-agent citation | de-facto file names fleet-wide |
| `HISTORICAL` | Kept as record — cite as history, never current | 221 |

- **Not re-minted (ruled):** `archive` — already Class-1 territory (`archive/` directory + FROZEN/RETIRED banners).
- **Form guard (part of the ruling):** any authority MAP over these labels is a GENERATED join over surface-local declarations (the `render_directory.py` model) — labels canonical at surfaces, map derived; a hand-maintained authority map is pre-declined (PAT-006/PAT-113).
- First live exemplar: HEARTBEAT's 2026-08-22 derived banner.

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

## Class 7 — Gate-registry envelope: scannability (added 2026-08-20; ruling: Will in-session "Approved" on `AGENTS/DAEDALUS/design/2026-08-20_GATE_REGISTRY_ADJUDICATION.md`; provenance: WALTER 8/19 Will-routed measurement + CREED 8/20 untrippable-row finding; first application = `PROME/GATES.tsv` `scannable` column)

For the `scannable` cell of a gate-registry envelope row. Declares HOW the gate is graded — never whether it is important. One token per row, no compounds:

| Token | Meaning | Grading obligation it creates |
|---|---|---|
| `INSTRUMENT` | Named metric/series with operator + level; a machine can grade it | Row must complete the chain: named metric surface (VX row / METRIC_MAP entry / watcher) + a named reader. `registry_chain_check` asserts all three; a tool-side literal for the same gate must match the registered level |
| `JUDGEMENT` | Compound / event-class / qualitative; the OWNER grades it at boot | Row must carry a dated `review_by` the owner can discharge alone; scanners COUNT these rows and print lapses — they never grade them |
| `OWNED-ELSEWHERE` | The metric belongs to another desk (named in the row) | Metric-owner named in the row; the gate-owner cites, never keeps a competing copy (PAT-006/PAT-063) |

⚠️ **The registry cell is an ENVELOPE field. The condition LETTER lives at exactly one owner-side `definition_surface`; the registry carries a one-line summary + pointer, never a copy** (PAT-006 n+3, 2026-08-20: both drift directions measured live, including a canonical cell stale against a fire that had already happened).

## Class 8 — Ledger cadence declaration (added 2026-08-20; provenance: OSPREY+HAWK ledger-nudge day-one field report via PROME, `AGENTS/OSPREY/outbox/2026-08-20_to-PROME_ledger-nudge-caveat-event-driven-surfaces.md`; first application = the mechanism's motivating surface, OSPREY `workbook/WARRISK.tsv`, owner-adopted)

For a live workbook ledger whose header comment block declares its publication cadence. One declared form today:

| Token (declaration form) | Meaning | Obligation it creates |
|---|---|---|
| `Cadence: EVENT-DRIVEN` | The data clock must NOT advance without a real print (per-voyage premia, canvass-only series) — writes-behind measures desk activity, not staleness, on this surface | Header MUST also carry the re-pull clock `Last re-pull ATTEMPTED: YYYY-MM-DD` (PAT-044's second clock) — a declaration without it is MISCONFIGURED (`--nudge` rc 2): absence-expected certifies nothing unless somebody provably looked. The fitting freshness check is the re-pull clock, not the data clock |

⚠️ **Scope: the declaration affects `ledger_staleness.py --nudge` ONLY** (distinct ℹ️ label, not counted behind — a check structurally always-red on one surface trains skipping on every surface, PAT-110's inverse). The `--days`/`--writes`/`--abs-floor` scans still grade the file — the owner's dispositions there stay "refresh / freeze / say why not." The declaration is a FORM, not a keyword (PAT-059): `Cadence:`-prefixed, front-loaded (col ≤100), header-block only — bare prose "event-driven" mentions do not declare (measured live: WARRISK's own caveat prose would have self-declared under a bare-token match).

*Exemption-law cross-ref (ruled 2026-08-22): the declared-exemption law is HOMED at Class 11 — the pending `SCHEDULED`/`EXEMPT-BY-CHARTER` tokens (8/28 register ②) point there at mint, never restate it.*

## Class 9 — Marker-role separation: severity vs priority (added 2026-08-21; ruling: Will in-session, AskUserQuestion "Forward-only, P1/P2/P3 text" selected off the DAEDALUS rec; provenance: ZHAO 8/21 S8 implementation `9f97c7f5f` via PROME — a stdout-scrape verdict read permanent-REVIEW because §4 prints 🔴 as a PRIORITY glyph on healthy forward catalysts; the fleet's emoji vocabulary double-served as severity marker AND priority marker)

**The rule: one marker family per semantic role.** The colored-circle family (🟢 🟡 🟠 🔴) is RESERVED for **severity/risk-state** — root CLAUDE.md's Status key is the existing canon and stays the sole authority for its meanings. **Priority/importance is expressed as TEXT tokens, never as a colored circle:**

| Token | Meaning |
|---|---|
| `P1` | act this session / blocks a decision |
| `P2` | act by the named date on the row |
| `P3` | informational / next natural touch |

Emoji beside a priority token is DECORATION ONLY — permitted, but never the machine-read carrier; a parser keys on the `P`-token, and a priority cell containing 🔴 without a `P`-token is the legacy form, not a new-write option.

⚠️ **Enforcement is FORWARD-ONLY (Will-ruled): new surfaces and next-writes conform; legacy is grandfathered — NO retroactive fleet sweep.** **Template-surface rider (added same day, ZHAO `9c5bd623d` — refines the ruling's application, does not reinstate a sweep): on a surface whose EXISTING ROWS ARE THE TEMPLATE FOR NEW ONES (TSVs, registries, schema-bearing files), forward-only is defeated by copy-the-neighbour — the next writer consults the row above, not the ruling, so grandfathered rows TEACH non-conformance. Rider: conform-on-touch, OR conform-now-while-the-author-is-still-holding-it (ZHAO's own 10-cell conversion cost ten minutes, four hours after authoring). Prose surfaces are exempt — a stale paragraph is not copied into the next paragraph. Kin: `finding_a_ruling_governs_the_next_write_not_the_existing_state` (64% compliance hours after the author's own ruling — template-copying is the hypothesized driver, n=1, testable at the 8/28 ⑫ walk).** Rationale on the record: 🔴-as-priority exists on hundreds of legacy surfaces (packet headers, HEARTBEAT, DOCKET, dashboards); a big-bang re-mark creates a mixed-vocabulary transition worse for every scraper than one dirty vocabulary, and the grandfather-forward pattern is how every prior class of this file healed. **Companion rule, NOT restated here:** verdicts key on alert COUNTS returned by code, never on scraping output for glyphs — that is CHECK_STANDARD §8 territory (encode at the ⑤b sitting); this class fixes the vocabulary, that rule fixes the mechanism, and neither substitutes for the other (a clean vocabulary still collides in quoted/historical text).

## Class 10 — Assertion-row contract: standing-state rows (added 2026-08-21; ruling: forum-6 R6, in-lane per `FORUM/2026-08-17_correction-propagation/04_synthesis/06_PROME_rulings-record.md` — "PROME lane + blueprint-encode at DAEDALUS's next touch"; this section IS that touch. Provenance: forum-6 incident I-3 — a "corrections owed" row outlived its 8/10 completion by 7 days and produced a duplicate packet, a duplicate banner, and a publicly-owned delay that never happened)

**The rule (general form, for OWNER ledgers — PROME's own queue/DOCKET rules are the PROME-lane implementation, not restated here):** any coordination-ledger row asserting a standing state — `OWED` / `PENDING` / `NEVER-DELIVERED` / "never done" — carries, **at registration**:

| Field | Content |
|---|---|
| (a) **completion artifact path-or-pattern** | WHERE the action will leave evidence (recipient `processed/`, encode target, lineage row) — the row names its own verification surface |
| (b) **expiry-or-resolver date** | when the assertion stops being trustworthy unread; a standing-state row with neither is the rot shape itself (`no assertion-rows without a consumption-moment check or an expiry` — the forum's adopted design law) |

**Read-side rule: reconciliations and re-presentations verify at the COMPLETION ARTIFACT, never at the asserting row.** The three-place search (target's `processed/` · own delivery record · downstream lineage) is the CONTRACT of the row, not a memory item. Kin: `finding_record_of_an_action_is_not_the_action` (n=11, owed-row limb) · PAT-115 (a resolver dated to an expected event inherits its slip risk — name the anchor type in the cell).

⚠️ **Rows that EXPIRE or are re-derived at read time (fire-ledger rows, artifact-verify-per-presentation) are already conformant** — the class targets rows that ASSERT; that is where the rot concentrates (forum-6 P1 measurement). Deployment, not invention: GATES `consumed_by` + WILL_QUEUE artifact-verify-per-presentation are this contract already working on two surfaces.

## Class 11 — Consumption-state ladder (added 2026-08-22; ruling: Will verbatim **"ok both approved"** 14:34 EDT, `PROME/codex/2026-08-21_RAV_operating-improvements-feedback.md` §MINTED; provenance: RAV item 3; census-first draft `design/2026-08-22_CLASS11_12_ENUM_SITTING_DRAFT.md` — tokens mined from measured fleet usage, census 2026-08-22)

For the delivery lifecycle of a packet/finding/correction between desks. The ladder is ORDERED — each token asserts strictly more than the one before it, and skipping a rung is a claim, not a shortcut:

| Canonical token | Meaning | Census basis |
|---|---|---|
| `ROUTED` | Written + committed toward the recipient; asserts nothing about arrival | 265 |
| `DELIVERED` | At the recipient's surface (inbox/board), not yet read. Compound display `LANDED-UNREAD` stays legal prose = `DELIVERED` + an age | 255 (+7) |
| `CONSUMED` | Recipient read/processed it (their filing or explicit ack) — says nothing about their surfaces changing | 281 |
| `ENCODE-CONFIRMED` | The change landed on the owner's own surface, owner-attested | 17 |
| `CLOSED-VERIFIED` | Sender verified the encode AT THE ARTIFACT — the chain's terminal state | 22 |
| `EXEMPT-PULL` | Declared exemption: pull-complete recipient — for this route `DELIVERED` **is** complete (`finding_deferral_rule_hides_its_own_cost`) | WALTER exemption class |

**Operative rules (travel with the class — RAV item 3's operative sentences):** nothing may be described as **resolved** below `ENCODE-CONFIRMED`; a sender may not write `CLOSED-VERIFIED` without the artifact check.

**Don't-mints on the record (ruled):** `CREATED` (census 0 — a state nobody records) · `READ` (collapses into CONSUMED) · `ANSWERED` (a prose verb — an answer is itself a packet with its own ladder) · `OWNER-ENCODED` (RAV's spelling; `ENCODE-CONFIRMED` survives, 17 vs 4) · **`UNPROCESSED` (ruled NOT minted — it is `DELIVERED` + age; the unfiled-vs-unprocessed distinction resolves at the METRIC layer: the fleet_triage metric is named `delivered_unread`; "unprocessed" stays legal prose).**

**⚖️ One-breath exemption law (SINGLE HOME — this paragraph; other token families POINT here, never restate):** *a declared exemption must be expressible, or the guard trains its readers to ignore it.* `EXEMPT-PULL` (this class), Class-8 `SCHEDULED`/`EXEMPT-BY-CHARTER` (pending mint, 8/28 register ②), and the roster cadence enum's designed-quiet are ONE law: every guard family needs a token for "correctly quiet," distinct from silence.

First live exemplar (citable): the 2026-08-22 encode-ask packet's own ladder — ROUTED at commit `7f963e93a` → DELIVERED at DAEDALUS `inbox/` → CONSUMED at this encode session → ENCODE-CONFIRMED at this section's commit.

## Class 12 — Verification-basis (added 2026-08-22; same ruling §MINTED; provenance: RAV items 2+8 merged; census-first draft ibid.)

Declares what KIND of checking stands behind a load-bearing claim — the repo-vs-world line made a token:

| Canonical token | Meaning | Census basis |
|---|---|---|
| `PRIMARY-VERIFIED` | Checked against the primary/external source itself; domain subtypes (`EDGAR-verified`) stay legal prose mapping to it | 333 (+36) |
| `ARTIFACT-VERIFIED` | Checked against a REPO artifact — internal consistency, **NOT external truth** | 146 |
| `SECONDARY-SOURCE` | Rests on a secondary report only | 162 |
| `OWNER-ASSERTED` | A counterparty's claim, not independently checked; "not independently verified" stays legal prose mapping to it (ruled: compact token minted) | 62 |
| `UNANCHORED` | No anchor exists — the visible-absence token, the class's real payoff (`finding_silent_blank_evades_review`) | 20 |

**Scope guard (in-class, ruled): load-bearing/decision claims ONLY** — thresholds, prediction letters, Will-facing synthesis, cross-desk packets. Labeling every sentence is the VULCAN 4-of-7 over-reporting class: a basis token on routine prose is ceremony, not information.

**Don't-mints on the record (ruled):** `UNVERIFIED` as a token (census 1,591 but generic — it cannot discriminate `OWNER-ASSERTED` from `UNANCHORED`, the exact distinction this class exists to make; stays prose) · `MARKET-DATA-CURRENT-AS-OF` (a timestamp practice, governed by PAT-044 + root pricing rules — not a state).

**Neighbour reconciliation (Class 6):** Class 6 declares the SOURCE a figure cites (`PRIMARY`/`MIRROR`/`MIRROR-WALLED`); Class 12 declares the CHECKING performed on a claim. A `MIRROR`-cited figure can later be `PRIMARY-VERIFIED`; the two compose, neither substitutes.

## Enforcement map (who reads these tokens)

| Class | Machine reader today | Registry obligation |
|---|---|---|
| 1 (banners) | `ledger_staleness.py` recognizer | Recognize canonical + legacy set; SUPERSEDED addition owed (rides TERRY-S1 session) |
| 2 (gates) | greps in sweeps/audits/screens (no single enforcer) | Any NEW check greps the canonical spellings + documents which legacy spellings it covers |
| 3 (predictions) | boot due-scans, scoreboard tooling (per-agent) | New ledgers ship with the token enum in their header comment |
| 4 (queue/disposition) | queue re-scan tooling, board_log audits (per-agent today; no single enforcer) | New queue surfaces ship the enum + TERMINAL marking in their header comment; any re-queue tooling keys on the TERMINAL flag, never on token spelling |
| 5 (zero/UNKNOWN/NA) | ⛔ **UNBUILT — CORRECTED 2026-08-17: `basis_check` never shipped as code** (BRENT-confirmed — class-5 tokens live as INCIDENTS.tsv column enum + prose, no script check exists; this cell previously named it as the ruled enforcement arm, and the correction sat in an overflow 4th cell GFM silently dropped at render — self-audit F25). Candidate home rides the forum-4 #11 registration-checklist build; extend an existing checker per anti-ratchet rider | New quantitative TSV columns ship the enum in a header comment; existing columns adopting the class name what they supersede |
| 7 (gate-envelope scannability) | ⛔ UNBUILT — `registry_chain_check` is the ruled enforcement arm (Will 2026-08-20), queued after docket_view; until it ships, PROME's gates-hygiene sweep reads `review_by` and WALTER's boot scans `INSTRUMENT` rows only | `PROME/GATES.tsv` ships the enum in its header comment at the column-add; the 3 desk registries (RED/REGINALD/CREED) are exempt-by-form (their rows are all INSTRUMENT-class by construction; CREED's `band_status` legacy spellings grandfathered) |
| 8 (ledger cadence) | `ledger_staleness.py --nudge` (LIVE 2026-08-20 — all paths capable-case watched at ship, incl. the rc-2 no-re-pull-clock path) | Declaring ledgers carry BOTH the token line and the re-pull clock; owners adopt per surface (opt-in), never batch-applied — a wrong declaration silently exempts a rotting ledger from the nudge |
| 9 (marker-role: severity vs priority) | No dedicated enforcer today — reader-side convention + REGISTRATION_CHECKLIST row 15 at build time; the CHECK_STANDARD §8 glyph-vs-count rule (pending encode, sweep-input ⑤b) is the mechanism-side twin | New priority cells/columns carry `P1`/`P2`/`P3` text tokens; colored circles stay severity-only on new writes; legacy grandfathered, healed at natural rewrites — never batch-swept |
| 10 (assertion-row contract) | ⛔ UNBUILT as script — Staleness Sweep gains a grading leg at run #4 ~9/1 (registered in `sweeps/STALENESS_SWEEP.md` same commit as the class); PROME-lane surfaces enforced by prome_gate extension (PROME's build) | New standing-state rows carry both fields at registration; reconciliations read the completion artifact, never the asserting row; existing rows conform-on-touch (Class 9 template-surface rider applies — TSV rows teach their neighbours) |
| 6 (source authority) | No dedicated enforcer today — reader-side convention; a fleet grep for `PRIMARY`\|`MIRROR`\|`MIRROR-WALLED` on threshold rows is a candidate follow-on *(pipes escaped 2026-08-17 — unescaped they split this row and GFM dropped the obligation cell, self-audit F25)* | New citations on load-bearing figures carry one of the three tokens; HOMER `RATES.tsv` (`workbook/`) is the first-application worked example |
| 11 (consumption ladder) | No dedicated enforcer today — reader-side convention; `fleet_triage` (post-8/28 build) reads DELIVERED-age as its `delivered_unread` metric; packet audits/write-back watches grep the canonical spellings | New cross-desk packets and watch rows use ladder tokens; "resolved" below `ENCODE-CONFIRMED` is a defect; `CLOSED-VERIFIED` requires the artifact check — both rules travel with the class text |
| 12 (verification-basis) | No dedicated enforcer today — reader-side convention; candidate rider on `registry_chain_check` / the forum-4 #11 registration-checklist build | Load-bearing claims on NEW surfaces carry one basis token; scope guard applies (no ceremony labeling); legacy prose grandfathered per standing scope rule |
| 1-ext (surface-role enum) | No machine reader today — `render_directory.py` is the worked DERIVED-map example; role labels reader-side at surfaces | New non-agent/shared surfaces declare a role label in their header; authority maps are GENERATED joins, never hand-maintained |

**Build-time check (REGISTRATION_CHECKLIST row 15):** new agents' state-bearing surfaces use canonical tokens; DAEDALUS verifies at registration. Blueprint variants cite this file — they do not restate the tables.
