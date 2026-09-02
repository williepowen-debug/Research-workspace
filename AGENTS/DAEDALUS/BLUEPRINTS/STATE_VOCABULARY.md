# STATE VOCABULARY — controlled tokens for machine-read state (fleet build standard)

**Owner:** DAEDALUS · **Created:** 2026-07-31 (Will-approved; provenance: STE/ASD-STE100 adaptation assessment, `design/2026-07-31_STE_WRITING_STANDARD_ASSESSMENT.md` §3A) · **Pattern:** PAT-075.

**Governing rule: where a machine or a cross-agent reader parses the token, the token is an INTERFACE (PAT-069).** Every synonym is a future recognizer-widening or a silent false-negative. This registry fixes ONE canonical token per state for the cross-agent handle and for all NEW surfaces. It is **floor, not ceiling (PAT-015)**: rich local states (HENRY's CRACKING/RE-ARMED, LIQUID's DORMANT→TRIGGERED, VIOLET's 45-pt) stay canonical locally — the registry binds only the comparable handle written *alongside* them, never replaces them.

**Cold half:** `STATE_VOCABULARY_PROVENANCE.md` carries every class's ruling record, defining-defect narrative and census (split 2026-08-28; this file cites, that one explains).

**Scope:** binds NEW surfaces and cross-agent handles at build/registration time (REGISTRATION_CHECKLIST row 15). Existing files are **grandfathered** — enforcers must keep recognizing the legacy set; nobody rewrites historical tokens (statement-time grades are retained verbatim, fleet practice). Free prose *after* the canonical token is always fine: `FROZEN 2026-07-04 — superseded by X, do not cite rows as current`.

---

## Class 1 — Dead/static surface banners


| Canonical token | Meaning (one each — the STE rule) | Banner must carry |
|---|---|---|
| `FROZEN <date>` | Static snapshot, not maintained. **No successor implied.** | Date + one-line why + where truth lives now |
| `SUPERSEDED <date>` | Replaced by a **named successor** — go there. | Date + **the successor's path** (a SUPERSEDED banner without a successor pointer is a defect) |
| `RETIRED <date>` | Role/surface ended by decision. No successor. | Date + the deciding ruling/session |

- **Legacy, recognized but not for new surfaces:** `NOT CURRENT` · `DO NOT CITE` · `NOT MAINTAINED` · `ARCHIVED` (as primary token — `archive/` the *directory* is unaffected). The recognizer keeps them (PAT-035/059 widenings stand); new surfaces pick from the canonical three.
- **Not state tokens (never as primary banner token):** `DEAD` · `OBSOLETE` · `DEPRECATED` — fine as prose after a canonical token.
- ✅ **SUPERSEDED recognizer gap CLOSED same day (2026-07-31, TERRY-S1 session as planned):** `SUPERSEDED` added to `STATIC_BANNER_MARKERS` under the existing banner-form guards; fleet-validated — zero live flips (confirming the gap was latent), synthetic capable-case passes, trade-mode output byte-identical.

### Class 1 extension — surface-role enum *(ruling + provenance → `STATE_VOCABULARY_PROVENANCE.md`)*

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


| Canonical token | Meaning |
|---|---|
| `ARMED` | Gate registered and watching; condition not yet met |
| `FIRED` | Condition met (carry the date + level: `FIRED 7/28 @ 281bp`) |
| `NOT-FIRED` | Evaluated, condition not met. **Hyphenated — one spelling.** (Chosen because the blueprint's donor triad, market-agent §4/HENRY, already writes `FIRED / NOT-FIRED`) |
| `STOOD-DOWN` | Deliberately disarmed (carry the ruling). Distinct from NOT-FIRED |
| `CANNOT-FIRE` | **Evaluated and found UNGRADEABLE: at least one leg has no metric surface / no producer** — distinct from `NOT-FIRED` (tested, condition not met). A conjunctive gate renders `CANNOT-FIRE` if its WEAKEST leg does; per-leg, never per-gate (Falsification #2 L-31; AEOLUS exemplar) |
| `UNOBSERVABLE` | Spec sound, instrument exists, **the world may never emit the observable** (a disclosure a filer need not make, a print a source stopped publishing) — FORUM-5 deferral, BRK-25 class, DOCKET row 188. Distinct from `CANNOT-FIRE` (we cannot measure) |
| `CONTESTED` | A leg ANOTHER desk owns is under dispute — not down, not fired; carry the adjudicator + review date (LIQUID X1 / BROCK, DOCKET 8/27 review 2026-09-15). The honest state of a disputed leg is never `CANNOT-FIRE` (PROME 8/27 correction, verified at LIQUID's retraction) |

- `TRIGGERED` → use `FIRED`. `UNFIRED` / `NO-FIRE` / `NOT FIRED` (spaced) → use `NOT-FIRED` on new surfaces.
- **`Trigger` companion field (WQ-117 C, Will 2026-09-01; RAV two-axis form — provenance → PROVENANCE):** `Trigger ∈ {SCHEDULED, EVENT, MANUAL}` says WHEN a gate is evaluated (at a boot/cadence · when a named event fires · only when someone chooses to). The second axis — **Adjudicator ∈ {MACHINE, OWNER}** — already exists on `PROME/GATES.tsv` as `INSTRUMENT` / `JUDGEMENT` and is recognised, not duplicated (PAT-006). Together they say what `LIVE` cannot: *a LIVE JUDGEMENT gate with `Trigger=EVENT` is a gate nobody reads until something happens* (CORAL-MSI-01's seam). **Declined (same word):** `CANNOT_FIRE_PARTIAL` / `UNKNOWN` — covered by the weakest-leg rule above. GATES column = PROME's, rides the GATES current-state redesign; desk registries adopt on next-write. `registry_chain_check` leg (b) is what will POPULATE `SCHEDULED` mechanically; until built the cell is owner-declared.
- **Exemplars promoted to canon 2026-08-28:** AEOLUS per-leg `CANNOT-FIRE` vs `NOT-FIRED` render · HENRY per-leg live counts under a **non-latching AND** · VULCAN dated retrofit rail. Display form: `total · range · moved · fired` beside any convergence score. *(Narrative → PROVENANCE, rotated 2026-09-01.)*
- **Local richness protected (PAT-015):** HENRY's `CRACKING`/`RE-ARMED`, LIQUID's `DORMANT→TRIGGERED` ladder, and any agent's richer state machine stay canonical in their own files — the registry token is the *cross-agent handle* written beside them, and a re-arm cycle is legitimately `FIRED → STOOD-DOWN → ARMED (re-armed <date>)`.

## Class 3 — Prediction resolution states


| Canonical token | Meaning |
|---|---|
| `OPEN` | Live, resolution date/condition not reached |
| `HIT` | Resolved true as written (the letter, not the thesis — [[finding_confidence_priced_against_thesis_not_letter]]) |
| `MISS` | Resolved false as written |
| `VOID` | Premise failed / unresolvable as specified — excluded from Brier (carry the reason: `VOID (premise-mismatch)`) |
| `STUCK` | Cannot resolve because window/instrument broke — a STATUS state, never a confidence cut ([[finding_resolvability_defect_is_status_not_confidence]]) |

- Nuance rides a parenthetical, not a new token: `HIT (letter; thesis-partial)`, `MISS (direction right, magnitude short)`. Narrative outcomes go in the Outcome/Notes column — **the Status cell holds ONLY a registry token.**
- **Historical rows are never rewritten** — grades stand verbatim as made; the registry binds new ledgers and new rows in ledgers that adopt it.

## Class 4 — Queue / disposition states *(ruling + provenance → `STATE_VOCABULARY_PROVENANCE.md`)*

| Canonical token | Meaning | Terminal? |
|---|---|---|
| `QUEUED` | Awaiting assessment | NON-TERMINAL |
| `DEFERRED <until/condition>` | **Not yet assessed**, deliberately postponed — must carry a re-look date or condition | NON-TERMINAL |
| `NO-ACTION <date>` | **Assessed on merits; nothing warranted. Do not re-queue.** The token L-16 was missing | TERMINAL |
| `DONE <date>` | Assessed and acted; record where | TERMINAL |

- The trap this exists to kill: using `DEFERRED` to mean "I looked, nothing to do." That is `NO-ACTION`. `DEFERRED` asserts the assessment has NOT happened yet.
- **Local richness protected (PAT-015):** WALTER's KILL/DISPATCH/FOLD lane vocabulary and any agent's richer disposition ladder stay canonical locally (WALTER's spec is its own, unchanged) — this class binds NEW queue/board_log-shaped surfaces and the cross-agent handle, per the standing scope rule above.
- Fleet cross-check candidate (registered, not yet run): grep queues/board_logs for `deferred` rows older than ~2 sessions whose notes read like completed assessments — LABOR's n=6 says the class is not rare.

## Class 5 — Zero / UNKNOWN / not-applicable distinction *(ruling + provenance → `STATE_VOCABULARY_PROVENANCE.md`)*

| Canonical token | Meaning | The distinction it protects |
|---|---|---|
| `MEASURED` | A real, measured number — **including a genuine measured 0** | Zero-as-observed is a datum, not a gap |
| `ZERO-RESTORED` | 0 because the facility was restored / the incident RESOLVED | Distinguishes "back to normal" from "never damaged" |
| `ZERO-INTACT` | 0 because nothing was damaged — attacked-and-spared, or a watch row with no loss | Preserves that an event was evaluated and produced no loss |
| `ZERO-NODOUBLECOUNT` | **Deliberately** 0: quantity already carried on an earlier row for the same key | Prevents an anti-double-count from being aggregated as absence |
| `UNKNOWN` | Unit is right; nobody has ever measured it. **NOT zero.** | Kills the silent-zero-from-blank aggregation defect |
| `NA-WRONG-UNIT` | Asset is real but **not denominable in this column's unit** — read the paired unit/qty column | Kills the 77-MTPA-in-bpd class |
| `UNLOGGED` | Blank: never published or attempted. **NOT zero, NOT unknown-after-looking.** | Distinguishes "we did not try" from "we tried, no answer" |

- **In force immediately, no encode needed (fleet-binding restatement from the ruling):** no aggregate over a column carrying these tokens is quotable until the schema declares its unit — the tokens make units visible, they do not make the file summable.
- **Local richness protected (PAT-015):** rich domain vocabularies (BRENT's `facility_key`, MIDAS's provenance ladder, any richer categorical alongside the token) stay canonical locally; this class binds only the state-token beside the number.

## Class 6 — Source-authority distinction *(ruling + provenance → `STATE_VOCABULARY_PROVENANCE.md`)*

| Canonical token | Meaning | Attached to |
|---|---|---|
| `PRIMARY` | Cited to the issuer of record (Freddie for PMMS, Treasury for DGS, USBR for Powell, etc.) | Any load-bearing figure |
| `MIRROR` | Cited to an aggregator (FRED, Yahoo, vendor cache) — issuer reachable but not read | Non-load-bearing figures; mirror is acceptable |
| `MIRROR-WALLED` | Cited to an aggregator because the issuer is unreachable (403, paywall, no API) — carry the wall note | Load-bearing figures where the primary is genuinely blocked |

- **Next-write-only** — no retroactive sweep; existing citations grandfathered; the token governs each figure's next write.
- **The "where reachable" carve-out is load-bearing (`finding_blocked_mirror_is_not_an_unreachable_primary`):** `MIRROR-WALLED` is legitimate; using `MIRROR` when the issuer IS reachable is the defect this class kills. A 403 is a fact about ONE host — try the API and enumerate before writing `MIRROR-WALLED`.
- **Load-bearing = writes into a THRESHOLD, a prediction letter, a Will-facing synthesis, or a downstream agent's inbox.** Prose citations in research/audit narratives are exempt (STRICT_TEXT scope rule).

---

## Class 7 — Gate-registry envelope: scannability *(ruling + provenance → `STATE_VOCABULARY_PROVENANCE.md`)*

For the `scannable` cell of a gate-registry envelope row. Declares HOW the gate is graded — never whether it is important. One token per row, no compounds:

| Token | Meaning | Grading obligation it creates |
|---|---|---|
| `INSTRUMENT` | Named metric/series with operator + level; a machine can grade it | Row must complete the chain: named metric surface (VX row / METRIC_MAP entry / watcher) + a named reader. `registry_chain_check` asserts all three; a tool-side literal for the same gate must match the registered level |
| `JUDGEMENT` | Compound / event-class / qualitative; the OWNER grades it at boot | Row must carry a dated `review_by` the owner can discharge alone; scanners COUNT these rows and print lapses — they never grade them |
| `OWNED-ELSEWHERE` | The metric belongs to another desk (named in the row) | Metric-owner named in the row; the gate-owner cites, never keeps a competing copy (PAT-006/PAT-063) |

⚠️ **The registry cell is an ENVELOPE field. The condition LETTER lives at exactly one owner-side `definition_surface`; the registry carries a one-line summary + pointer, never a copy** (PAT-006 n+3, 2026-08-20: both drift directions measured live, including a canonical cell stale against a fire that had already happened).

## Class 8 — Ledger cadence declaration *(ruling + provenance → `STATE_VOCABULARY_PROVENANCE.md`)*

For a live workbook ledger whose header comment block declares its publication cadence. One declared form today:

| Token (declaration form) | Meaning | Obligation it creates |
|---|---|---|
| `Cadence: EVENT-DRIVEN` | The data clock must NOT advance without a real print (per-voyage premia, canvass-only series) — writes-behind measures desk activity, not staleness, on this surface | Header MUST also carry the re-pull clock `Last re-pull ATTEMPTED: YYYY-MM-DD` (PAT-044's second clock) — a declaration without it is MISCONFIGURED (`--nudge` rc 2): absence-expected certifies nothing unless somebody provably looked. The fitting freshness check is the re-pull clock, not the data clock |
| `Cadence: SCHEDULED next_due=YYYY-MM-DD` | The next legitimate write has a KNOWN date (a quarterly print, a season opening, a dated re-pull) — quiet until then is correct | Strict `YYYY-MM-DD` (A2: unparseable = `--nudge` rc 2, never a row-skip); after `next_due` the ledger counts BEHIND with the passed date named — a schedule is a promise with an expiry, not an exemption |
| `Cadence: EXEMPT-BY-CHARTER — <charter clause>` | The desk's CHARTER exempts this surface from refresh (AEOLUS `seismic/`: a pull-only archive) | The clause after the token is REQUIRED (≥8 chars, cite the charter section); a bare token is MISCONFIGURED (rc 2) — an exemption nobody can read exempts nothing |
| `Last attention check: YYYY-MM-DD` *(header KEY line, WQ-148 — Will 2026-09-01 21:09 *"Approve 147 and 148 with your recs"*)* | The THIRD clock of a PAT-044 header: the data clock is old ON PURPOSE and someone provably looked on this date. Canonises four convergent local inventions — FALCON/OSPREY `Last re-pull ATTEMPTED:` · CARL `Last hygiene/no-event check:` · OZK `Last reviewed:` · RED prose (Staleness #4 M2; PAT-011 n+1: when N desks invent one field in N spellings the vocabulary is late) | `ledger_staleness.py` prints `held (attention Nd)` when the attention date is inside the threshold and `stale AND unattended` when it is older or absent; the data clock is never touched. **Forward-only:** owners rename their OWN headers at their next boot; the checker honours the legacy spellings during the soak; a ledger with NO attention line prints unchanged (default byte-identical) — the `unattended` word applies only when a line exists and is older than the threshold. |
| `PINNED` *(row-level, READ not declared)* | A row byte-frozen by a Kernel submission/accepted event (`native_refs[].path` + `locator` + `raw_record_sha256`) — a THIRD ledger state the two-state rule does not express: LIVE ledger, FROZEN row | Not written by the owner: `--nudge` READS the Kernel record and names pinned rows beside a behind ledger; the remedy becomes *refresh only UNPINNED rows* (MIDAS-06, 8/27 — the nudge was pushing toward a forbidden edit and nothing in the nudge knew) |

⚠️ **Scope: the declaration affects `ledger_staleness.py --nudge` ONLY** (distinct ℹ️ label, not counted behind) — **until WQ-147 (M1, Will 2026-09-01) lands, which extends the same recognition to `--all`**. The declaration is a FORM, not a keyword (PAT-059): `Cadence:`-prefixed, front-loaded (col ≤100), header-block only. *(Rationale + the WARRISK measurement → PROVENANCE.)*

*Exemption-law cross-ref (ruled 2026-08-22): the declared-exemption law is HOMED at Class 11 — `SCHEDULED`/`EXEMPT-BY-CHARTER` (MINTED 2026-08-28, wiring-sweep ②; enforcement LIVE in `ledger_staleness.py --nudge`, all paths fixture-watched at ship) point there, never restate it.*

### Class 8 extension — DESK cadence class (ROSTER column; same token family, designed in one breath so the two cannot fork — Will-approved 2026-08-21 "ok approve 1 and 2", instrument = `fleet_triage.py`, PROME applies the column)

One token per desk, declaring the cadence a triage instrument measures overdue-ness AGAINST, so designed quiet ≠ rot: `DAILY` · `WEEKLY` · `MONTHLY` *(print-keyed desks, PROME's addition)* · `EVENT-DRIVEN` *(spawned by a theater/print/filing event)* · `ON-DEMAND` *(Tier-2 / special; never overdue by clock)*. ⚠️ **The ledger declaration (`Cadence: EVENT-DRIVEN` on a FILE) and the desk class (`EVENT-DRIVEN` on a ROSTER row) are the SAME word with the SAME meaning at two granularities** — a desk-level class never overrides a file-level declaration and vice versa; triage reads the desk class, the nudge reads the file declaration.

### Class 8 extension — catalyst `date_class` (ZHAO census 2026-08-21: 8 values + 19 blanks + one desk-private token fleet-wide; ZHAO's docket = reference implementation, VULCAN conforming second; one-field-one-token)

Tokens for a catalyst row's date: `FIRM` · `MODELED (~)` · `WINDOW` · `TBD` — the ZHAO census form (8 values + 19 blanks + one desk-private token fleet-wide; ZHAO's docket = reference). *(Full table + ruling → PROVENANCE, rotated 2026-09-01.)* ⚠️ A `MODELED` date can slip EARLY (LABOR L-26, 9/1): every check that assumes lateness is blind to a print that landed before its docketed day.

## Class 9 — Marker-role separation: severity vs priority *(ruling + provenance → `STATE_VOCABULARY_PROVENANCE.md`)*

**The rule: one marker family per semantic role.** The colored-circle family (🟢 🟡 🟠 🔴) is RESERVED for **severity/risk-state** — root CLAUDE.md's Status key is the existing canon and stays the sole authority for its meanings. **Priority/importance is expressed as TEXT tokens, never as a colored circle:**

| Token | Meaning |
|---|---|
| `P1` | act this session / blocks a decision |
| `P2` | act by the named date on the row |
| `P3` | informational / next natural touch |

Emoji beside a priority token is DECORATION ONLY — permitted, but never the machine-read carrier; a parser keys on the `P`-token, and a priority cell containing 🔴 without a `P`-token is the legacy form, not a new-write option.

⚠️ **Enforcement is FORWARD-ONLY (Will-ruled): new surfaces and next-writes conform; legacy is grandfathered — NO retroactive fleet sweep.** **Template-surface rider (ZHAO `9c5bd623d`):** on a surface whose existing rows are the template for new ones (TSVs, registries), forward-only is defeated by copy-the-neighbour — **conform-on-touch, or conform-now-while-the-author-is-still-holding-it**; prose surfaces exempt. Companion mechanism rule = CHECK_STANDARD §8. *(Rationale → PROVENANCE.)*

## Class 10 — Assertion-row contract: standing-state rows *(ruling + provenance → `STATE_VOCABULARY_PROVENANCE.md`)*

**The rule (general form, for OWNER ledgers — PROME's own queue/DOCKET rules are the PROME-lane implementation, not restated here):** any coordination-ledger row asserting a standing state — `OWED` / `PENDING` / `NEVER-DELIVERED` / "never done" — carries, **at registration**:

| Field | Content |
|---|---|
| (a) **completion artifact path-or-pattern** | WHERE the action will leave evidence (recipient `processed/`, encode target, lineage row) — the row names its own verification surface |
| (b) **expiry-or-resolver date** | when the assertion stops being trustworthy unread; a standing-state row with neither is the rot shape itself (`no assertion-rows without a consumption-moment check or an expiry` — the forum's adopted design law) |
| (c) **the ARTIFACT owed, never only the OCCASION** *(added 2026-08-28, CREED DOCKET row 33)* | a row keyed to an occasion (`COVERED: next spawn`) is discharged by the occasion ARRIVING while the work is skipped — nothing looks late and the tracker actively vouches for the gap. Artifact-named rows are checkable by anyone; occasion-named rows only by the owner who already forgot |

**Read-side rule:** reconciliations verify at the COMPLETION ARTIFACT, never at the asserting row — the three-place search (target's `processed/` · own delivery record · downstream lineage) is the row's CONTRACT. Kin: `finding_record_of_an_action_is_not_the_action` · PAT-115. *(Full text → PROVENANCE.)*

⚠️ Fire-ledger / artifact-verify-per-presentation rows are already conformant — the class targets rows that ASSERT. Deployment exemplars (GATES `consumed_by`, WILL_QUEUE artifact-verify) → PROVENANCE. First base rate measured Staleness #4 2026-09-01: 13 standing rows ex-PROME, both fields 0/13, neither 5/13 — stays a sweep leg, no script enforcer.

## Class 11 — Consumption-state ladder *(ruling + provenance → `STATE_VOCABULARY_PROVENANCE.md`)*

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

**Don't-mints on the record (ruled):** `CREATED` · `READ` · `ANSWERED` · `OWNER-ENCODED` · `UNPROCESSED` (= `DELIVERED` + age; the metric is `delivered_unread`). *(Reasons → PROVENANCE, rotated 2026-09-01.)*

**⚖️ One-breath exemption law (SINGLE HOME — this paragraph; other token families POINT here, never restate):** *a declared exemption must be expressible, or the guard trains its readers to ignore it.* `EXEMPT-PULL` (this class), Class-8 `SCHEDULED`/`EXEMPT-BY-CHARTER` (pending mint, 8/28 register ②), and the roster cadence enum's designed-quiet are ONE law: every guard family needs a token for "correctly quiet," distinct from silence.

First live exemplar → PROVENANCE (the 2026-08-22 encode-ask packet's own ladder, rotated 2026-09-01).

## Class 12 — Verification-basis *(ruling + provenance → `STATE_VOCABULARY_PROVENANCE.md`)*

Declares what KIND of checking stands behind a load-bearing claim — the repo-vs-world line made a token:

| Canonical token | Meaning | Census basis |
|---|---|---|
| `PRIMARY-VERIFIED` | Checked against the primary/external source itself; domain subtypes (`EDGAR-verified`) stay legal prose mapping to it | 333 (+36) |
| `ARTIFACT-VERIFIED` | Checked against a REPO artifact — internal consistency, **NOT external truth** | 146 |
| `SECONDARY-SOURCE` | Rests on a secondary report only | 162 |
| `OWNER-ASSERTED` | A counterparty's claim, not independently checked; "not independently verified" stays legal prose mapping to it (ruled: compact token minted) | 62 |
| `UNANCHORED` | No anchor exists — the visible-absence token, the class's real payoff (`finding_silent_blank_evades_review`) | 20 |

**Scope guard (in-class, ruled): load-bearing/decision claims ONLY** — thresholds, prediction letters, Will-facing synthesis, cross-desk packets. Labeling every sentence is the VULCAN 4-of-7 over-reporting class: a basis token on routine prose is ceremony, not information.

**Don't-mints (ruled):** `UNVERIFIED` (generic — stays prose) · `MARKET-DATA-CURRENT-AS-OF` (a timestamp practice). *(Reasons → PROVENANCE.)*

**Neighbour (Class 6):** Class 6 = the SOURCE cited; Class 12 = the CHECKING performed. They compose.

## Class 13 — Claim-confidence tokens *(WQ-140, Will 2026-08-30 22:56 *"approved go ahead"*; record `PROME/proposals/2026-08-30_wq140-codex-process-reform-RULED.md`; encoded 2026-09-01)*

Report-side twin of CHECK_STANDARD §14; forward-only on NEW surfaces.

| Canonical token | Operational definition |
|---|---|
| `VERIFIED` | Directly checked at the ARTIFACT (the owner-side file/cell/row the claim is about), THIS session |
| `INFERRED` | Supported by evidence but not directly established at the artifact |
| `SEARCH-NOT-FOUND` | A query returned nothing. **A claim about the SEARCH, never about the world** — the pattern set missed; it does not say the thing is absent (kin in PROVENANCE) |
| `UNKNOWN` | No check run |

**Upgrade rule (the point of the class):** an ABSENCE claim moves `SEARCH-NOT-FOUND → VERIFIED` **only after** (a) the owner-declared path/identifier for the thing was checked AND (b) any documented fallback location was checked. **A broader grep is NOT an upgrade.** **Neighbour (Class 12):** Class 12 = the KIND of checking; Class 13 = how far THIS session's check went. A Class-13 `VERIFIED` on a repo artifact is Class-12 `ARTIFACT-VERIFIED`, never `PRIMARY-VERIFIED`.

## Enforcement map (who reads these tokens)

| Class | Machine reader today | Registry obligation |
|---|---|---|
| 1 (banners) | `ledger_staleness.py` recognizer | Recognize canonical + legacy set; SUPERSEDED addition owed (rides TERRY-S1 session) |
| 2 (gates) | greps in sweeps/audits/screens (no single enforcer) | Any NEW check greps the canonical spellings + documents which legacy spellings it covers |
| 3 (predictions) | boot due-scans, scoreboard tooling (per-agent) | New ledgers ship with the token enum in their header comment |
| 4 (queue/disposition) | queue re-scan tooling, board_log audits (per-agent today; no single enforcer) | New queue surfaces ship the enum + TERMINAL marking in their header comment; any re-queue tooling keys on the TERMINAL flag, never on token spelling |
| 5 (zero/UNKNOWN/NA) | ⛔ UNBUILT — `basis_check` never shipped as code (corrected 2026-08-17; story → PROVENANCE); class-5 tokens live as INCIDENTS.tsv column enum + prose | Candidate home rides the forum-4 #11 registration-checklist build |
| 7 (gate-envelope scannability) | ⛔ UNBUILT — `registry_chain_check` is the ruled enforcement arm (Will 2026-08-20), queued after docket_view; until it ships, PROME's gates-hygiene sweep reads `review_by` and WALTER's boot scans `INSTRUMENT` rows only | `PROME/GATES.tsv` ships the enum in its header comment at the column-add; the 3 desk registries (RED/REGINALD/CREED) are exempt-by-form (their rows are all INSTRUMENT-class by construction; CREED's `band_status` legacy spellings grandfathered) |
| 8 (ledger cadence) | `ledger_staleness.py --nudge` (LIVE 2026-08-20 — all paths capable-case watched at ship, incl. the rc-2 no-re-pull-clock path) | Declaring ledgers carry BOTH the token line and the re-pull clock; owners adopt per surface (opt-in), never batch-applied — a wrong declaration silently exempts a rotting ledger from the nudge |
| 8-ext (SCHEDULED / EXEMPT-BY-CHARTER / PINNED) | `ledger_staleness.py --nudge` (LIVE 2026-08-28 — fixture battery: future/past/unparseable `next_due`, clause/no-clause exemption, bare-prose trap, pinned row, all-quiet, real CREED pins) | Owners declare per surface; PINNED is never declared (read from `AGENTS/*/outbox/kernel/submissions/` + `KERNEL/shadow/events/`); desk cadence class applied by PROME on ROSTER, read by `fleet_triage.py` (post-sweep build) |
| 2 (CANNOT-FIRE / UNOBSERVABLE / CONTESTED) | `falsification_scan.py` (sweep #3 ~9/14 gains the per-leg CANNOT-FIRE render — F1/F2 fixes first); `registry_chain_check` leg (a) when built | A conjunctive gate's cell renders the WEAKEST leg's token; `CONTESTED` rows carry adjudicator + review date; `UNOBSERVABLE` rows carry the emitter that may never emit |
| 9 (marker-role: severity vs priority) | No dedicated enforcer today — reader-side convention + REGISTRATION_CHECKLIST row 15 at build time; the CHECK_STANDARD §8 glyph-vs-count rule (pending encode, sweep-input ⑤b) is the mechanism-side twin | New priority cells/columns carry `P1`/`P2`/`P3` text tokens; colored circles stay severity-only on new writes; legacy grandfathered, healed at natural rewrites — never batch-swept |
| 10 (assertion-row contract) | ⛔ UNBUILT as script — Staleness Sweep gains a grading leg at run #4 ~9/1 (registered in `sweeps/STALENESS_SWEEP.md` same commit as the class); PROME-lane surfaces enforced by prome_gate extension (PROME's build) | New standing-state rows carry both fields at registration; reconciliations read the completion artifact, never the asserting row; existing rows conform-on-touch (Class 9 template-surface rider applies — TSV rows teach their neighbours) |
| 6 (source authority) | No dedicated enforcer — reader-side convention; fleet grep for the three tokens on threshold rows is a candidate follow-on | New citations on load-bearing figures carry one of the three tokens; HOMER `workbook/RATES.tsv` is the worked example |
| 11 (consumption ladder) | No dedicated enforcer today — reader-side convention; `fleet_triage` (post-8/28 build) reads DELIVERED-age as its `delivered_unread` metric; packet audits/write-back watches grep the canonical spellings | New cross-desk packets and watch rows use ladder tokens; "resolved" below `ENCODE-CONFIRMED` is a defect; `CLOSED-VERIFIED` requires the artifact check — both rules travel with the class text |
| 12 (verification-basis) | No dedicated enforcer today — reader-side convention; candidate rider on `registry_chain_check` / the forum-4 #11 registration-checklist build | Load-bearing claims on NEW surfaces carry one basis token; scope guard applies (no ceremony labeling); legacy prose grandfathered per standing scope rule |
| 13 (claim-confidence) | No machine reader — packet/report convention (PROME Session Process Controls since 8/30) | New audit/verification reports and cross-desk packets tag load-bearing claims; an absence claim below `VERIFIED` names what was searched |
| 8 (`Last attention check:`) | `ledger_staleness.py` (LIVE 2026-09-01, WQ-148; legacy spellings honoured) | Owners rename their own headers on next boot; never batch-renamed by DAEDALUS |
| 1-ext (surface-role enum) | No machine reader today — `render_directory.py` is the worked DERIVED-map example; role labels reader-side at surfaces | New non-agent/shared surfaces declare a role label in their header; authority maps are GENERATED joins, never hand-maintained |

**Build-time check (REGISTRATION_CHECKLIST row 15):** new agents' state-bearing surfaces use canonical tokens; DAEDALUS verifies at registration. Blueprint variants cite this file — they do not restate the tables.
