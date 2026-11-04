# CRUISE capital-event coverage review — November 4, 2026

Bounded Rule 9 helper verification for WALTER's approved maintenance review. OpenAI Codex, exact model unavailable; inherited WALTER cwd verified, root/local CLAUDE instructions explicitly read. No production change, collector write, new source retrieval, desk launch, commit or external message. Saved replay is retrospective classifier evaluation, not fresh news triage or claimed company-source verification.

## Finding

**The residual KNOWN worklist gap remains, but the October misses have already been routed.** Do not dispatch them again. The October 14 CRUISE packet names a September 30 NCLH note pricing and the RCL/Sandals acquisition plus loan syndication. BOARD `SIG-W-20261014-028-LATE-cruise-capital-events-nclh-950m-8point75-notes-repay-revolver-rcl-3b-sandals-stake-morgan-stanley-syndicating-loan.md` repairs those misses. November 3's Sandals joint-venture headline is a candidate for source/date/dedup inspection, not a proven new transaction.

Current `tools/intake_scan.py` lines 207–260 still emits NEW_ALERT/NEW_WATCH aggregates and NEW_WATCH_HIT/DEVELOPMENT per-item records, not ordinary KNOWN. This was intentional in PROME's September 25 packet: the lane delivers KNOWN rows for CRUISE's own review without a WALTER alert. Seven CRUISE WATCH_FOR phrases now installed in `Research-Intake/scripts/newsweep_config.py` lines 738–749 cover guidance/conference-call wording, not generic bond pricing, loans, stakes or joint ventures. They do not close this category gap.

The October 16 EDGAR expansion added CCL/RCL/NCLH/NCLC. It closes part of the gap, not issuer-release-only or Item 8.01-only coverage: `fetch_edgar_8k.py` has no 8.01 severity flag, while intake consumes `critical[]`. Current cruise filings are `entity_class: other`, `route_to: []` — intentional consumer judgment, not proof they were routed to a wrong owner. On November 4 the saved CCL 1.01/2.03 filing was captured and WALTER card 071 carries the $2 billion commercial-paper capacity, with capacity-versus-draw qualification. NCLH 5.02 was captured and card 075 carries CFO succession. These are evidence that the filing path now works, not evidence that all news-only capital events are covered.

## Reproducible saved sample

`python3 AGENTS/WALTER/research/2026-11-04_maintenance/cruise_sample.py` reads only seven named saved news files. `cruise-sample.json` preserves input hashes, row indices, titles and source-date fields. No production import or --mark call.

| Saved run | CRUISE rows | KNOWN rows | Narrow capital candidates |
|---|---:|---:|---:|
| October 1 | 22 | 15 | 1 |
| October 5 | 16 | 13 | 1 |
| October 6 | 18 | 15 | 1 |
| October 7 | 17 | 11 | 2 |
| November 2 | 15 | 15 | 0 |
| November 3 | 16 | 16 | 1 |
| November 4 | 15 | 15 | 0 |
| **Total** | **119** | **100** | **6** |

The six candidates are: NCLH notes offering (Oct 1 row 11); RCL stake acquisition (Oct 5 row 7); RCL 50% Sandals stake (Oct 6 row 8); Bloomberg and TradingView loan syndication relays (Oct 7 rows 2 and 5); Sandals joint-venture relay (Nov 3 row 7). Thus five historical titles cover the previously documented missed events and one recent title may repeat them. These are not six independent events. The pattern does not match October 6's generic “Sandals deal” title, but another title for that event matches. This exposes title-vocabulary recall risk rather than proving full recall.

## Concrete recommendation — proposed worklist behavior, not deployed

At an ordinary launched WALTER intake pass, add a **human-review candidate** for a saved item only when all are true:

1. `classification == KNOWN`.
2. `entity` is the already registered Carnival Corp, Royal Caribbean or Norwegian Cruise, and `agents` contains CRUISE. Do not add a bare `CCL` text match that can bind CCL Industries.
3. Title contains the proposed bounded capital vocabulary: notes offering, bond offering, commercial paper, credit facility/facilities, revolver, refinance variants, debt financing variants, loan, stake, joint venture, acquisition, tender offer or debt exchange. Exact candidate regex is in the saved replay.

This changes **WALTER's candidate queue**, not collector classification, authority or automatic dispatch. It should be visible as `CRUISE_CAPITAL_REVIEW`/ROUTINE for WALTER adjudication, carry original title/link/event-date fields and require ordinary source-body validation, BOARD/EDGAR/owner overlap checks and a recorded disposition. New versus repeated event is decided from source/event identity, not collection date. Repeated relays may fold into one disposition; do not silently discard a new term or changed financing stage merely because the issuer already appeared. Do not blanket-clear all KNOWN rows with this rule. Preserve existing alert key behavior; use a separate candidate namespace with explicit consumed-item identity and no automatic replay of the entire archive on installation.

**Do not condition this on CRUISE being DARK.** UNKNOWN runtime visibility is not DARK, and collector/owner publication gaps exist even when a desk is live. Any actual wake/doorbell remains governed separately by the existing messaging contract. No unattended session or owner launch is created.

## Acceptance cases for a bounded implementation

| Case | Expected |
|---|---|
| Saved Oct 1 NCLH notes pricing | Candidate, then DUP/FOLD to card 20261014-028 in a retrospective replay; historical absence repaired |
| Oct 5/6 Sandals stake and Oct 7 syndication relays | Candidate; combine duplicate relays, preserve acquisition versus financing-stage distinction |
| Nov 3 Sandals joint-venture title | Candidate requiring original event-date check; must not be auto-routed as new November acquisition |
| Nov 4 CCL commercial-paper filing, also a matching headline if present | Existing EDGAR route remains; candidate dedup must avoid a second dispatch |
| Guidance/conference-call WATCH_HIT | Existing path only; no duplicate candidate from new KNOWN-only branch |
| Royal Caribbean itinerary/promotion, Norwegian NHL sponsorship, analyst price target or stock performance | No capital candidate merely from owner/entity match |
| CCL Industries bond story | Reject unless normalized cruise entity and CRUISE recipient are both actually established |
| Institutional shareholder “stake” trade | May be a false-positive candidate; human review must distinguish secondary-holder trading from issuer financing/M&A |
| Debt financing headline without matched entity/CRUISE recipient | No candidate under this bounded rule; report recall limitation, do not silently broaden domain |
| Corrupt/missing saved news file | Explicit unavailable/error state; do not mark unseen items consumed |

The 119-row purposive sample is not a random precision/recall benchmark; the rule is informed by known misses and can overfit them. Six candidates out of 100 KNOWN rows estimates review volume only for this sample. No claim of production miss rate, zero false negatives or optimal vocabulary. Recommended next step is the narrow WALTER worklist change with these acceptance cases and ordinary source adjudication, subject to the parent's interpretation of the present approval's deployment scope. PROME owns any collector-side change; none is needed for this proposal.
