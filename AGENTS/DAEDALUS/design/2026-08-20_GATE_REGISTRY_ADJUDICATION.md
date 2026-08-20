# Gate-registry adjudication — machine-readable registries vs prose gates (WALTER 8/19 Will-routed question)

**Date:** 2026-08-20 · **Author:** DAEDALUS · **Status:** MEASURED + RECOMMENDED — Will ruling pending
**Inputs:** WALTER packet 8/19 (`inbox/2026-08-19_from-WALTER_only-3-fleet-agents-keep-machine-readable-trigger-registries...`) · CREED packet 8/20 (untrippable-row finding, T-02 fire) · PROME scope-add 8/20 (predictions-ledger path convention) · own first-hand reads of all 3 registries + PROME/GATES.tsv · 3-reader Mode-A fan-out over the 8 named prose families (FALCON+HAWK / SAM+TERRY / LIQUID+VIOLET+OSPREY), reports verbatim in this session's record
**Method note (PAT-100):** the three reader reports are preserved in full in the session transcript; every load-bearing claim below carries its source surface. Readers were instructed facts-only, no recommendations.

---

## §1 The measurement, corrected

WALTER's two passes were honestly made and each had a keying defect its own packet's discipline predicts (`finding_scan_keyed_on_naming_reads_local_form_as_absence`):

1. **Pass-1 ("3 machine-readable registries") missed the fleet's CENTRAL gate registry.** `PROME/GATES.tsv` — 25 rows, 15+ gate families, schema `gate_id · registered · owner · condition · consequence_on_fire · state · last_checked · source · consumed_by` — was invisible because the scan keyed on `trigger_id` columns under `AGENTS/`, and this file's ID column is `gate_id` at repo root. It has FOUR script readers (`PROME/tools/prome_gate.py`, `will_brief.py`, `fleet_dashboard.py`, `AGENTS/FALCON/scripts/hormuz_transit_watch.py`).
2. **Pass-2 ("6 families are prose no check can reach") is therefore mis-framed: all six GATE-* families ARE registered** — every one has a GATES.tsv row with id/owner/state/last_checked. What is true: the **condition** column is free prose, so the rows are scannable for existence and staleness but not gradable; and no script reads any owner-side definition surface.
3. Pass-1 also missed two scannable layers on already-counted desks: `RED/docket/WATCHLINES.tsv` (WL_ID/Metric/Op/Threshold/Sustain) and `FERT/workbook/TRIGGERS.tsv`.

**Live-gate census of the six families (readers, 8/20):**

| Family | Registered IDs | Live | Fully numeric-scannable (live) | Definition home |
|---|---|---|---|---|
| GATE-SAM | 1 | **0** (VOID 8/7) | — | condition prose in THESIS/STATUS cells; registry row = PROME/GATES.tsv |
| GATE-TERRY | 4 | 2 | 1 (TERRY-007, w/ sequence state + structured grading procedure built 8/20) | procedure file + card prose + TSV cell (3 dialects) |
| GATE-FALCON | 1 (3 legs) | 1 | leg-3 only, and its live level is NOT in the canonical cell | PROME/GATES.tsv cell + STATUS mirror |
| FAL- | 4 (+1 owed) | **0** OPEN | — | FALCON thesis/PREDICTIONS.tsv (TSV, prose cells) |
| HAW- | 20 | 2 | 0 (compound by domain nature; NO-VERDICT bands, frozen sub-thresholds) | HAWK thesis/PREDICTIONS.tsv |
| GATE-LIQ | 4 | 4 | 0 whole gates (3 scannable legs) | KB.tsv prose cells + 3 workbook spec .md |
| GATE-VIO | 2 | 1 | 1 (band-valued 70–72) | KB.tsv prose cell + STATUS gate table |
| GATE-OSPREY | 1 (3 legs) | 1 (FIRED 7/24) | 0 ("sessions" undefined in the frozen letter) | one markdown bullet, CPC_HALT doc :50 |

**≈11 live gates, 2 cleanly scannable.** WALTER's ratio expectation CONFIRMED for these families — and the inverse holds for the registry desks: REGINALD 8/8 and RED 9/9 scannable **by selection** (only scannable gates admitted), which is exactly the omission-shaped registry WALTER warned about. CREED alone runs the all-gates form (11 rows, 5 scannable, unscannable rows marked `QUALITATIVE`/`HOMER-OWNED` in `band_status`) — and CREED is where today's fire proved the remaining hole.

## §2 The defect classes actually measured (none is "prose vs TSV")

| # | Class | Live instances (verified at source 8/20) |
|---|---|---|
| D1 | **Row without metric surface = untrippable** (CREED's finding, `finding_banded_threshold_with_no_metric_surface_is_untrippable`) | CREED-T-02 MET ~6wks, owner awake, number written 3× in prose no band grades · HAWK FALSIFICATION.md's 10 dormant band-gates: "Guard column not yet added to VX.tsv — ruled work still owed" (owner-diagnosed) |
| D2 | **Two homes for the condition letter → drift, both directions** (PAT-006 class, n+3) | GATES.tsv FALCON-001 condition cell carries the superseded −36% baseline while the 8/10 re-keyed line (≤~3.0/≤~2.55 mb/d) — the letter that actually FIRED 8/15 — lives only owner-side; the row's *state* cell was updated 8/17, its *condition* cell was not · TERRY-006 LIVE in GATES.tsv, card RETIRED 8/18 (owner self-flags "a LIVE GATE WITH NO CARD") · KB-LIQ-076 note says "No PROME/GATES.tsv row exists for this watch by design" while GATES.tsv carries one |
| D3 | **Tool forks the level** (`finding_registry_names_a_concept_tool_resolves_an_instrument`) | VIOLET `scripts/move.py` hardcodes `("GATE-VIO-116 re-open", 71.0)` — 71.0 appears in NO definition surface (registered band 70–72); the script's docstring declares itself the level home · SAM `scripts/thresholds.py` hard-codes its own list containing NO CFTC line — the −153K/−140K/−108K family absent from the desk's only threshold scanner |
| D4 | **No reader** | zero scripts read any of the six families' definition surfaces; TERRY `ledger_sweep.py` indexes 3 SETUPS.tsv columns and never reads `entry_trigger`/`invalidation`; FALCON+HAWK `thesis/PREDICTIONS.tsv` outside `ledger_staleness`'s `workbook/*.tsv` glob, no LEDGER_GLOB declared |
| D5 | **Dead clocks** | all 4 GATE-LIQ `next_check` dates lapsed 5+ wks; PROME's 8/5 gates-hygiene flags (LIQ rows 12–19d, OSPREY 12d) delivered and unactioned — flags a reader can't discharge alone park forever (FORUM-6 rule) |
| D6 | **Attention capture by the registered subset** (`finding_registered_gate_captures_attention`) | OSPREY LESSONS:28, owner-diagnosed: the gate made CPC "the object of a daily, dated, named check, and nothing made the un-gated Russian terminals the object of anything" — the OSP-01 miss |
| D7 | **Registration-time construct holes** | "suspension ≥5 sessions" with "sessions" undefined in the frozen letter — and the gate fired on that leg (7/24, adjudication note records the ambiguity) — forum-4 #11's exact territory |

## §3 The answer

**Prose is the correct form for most gate CONDITIONS — the compound gates are compound by domain nature, and forcing them into op/value columns would falsify them** (HAW-19 is more rigorous than most TSV rows in the fleet). **What must be machine-readable is the ENVELOPE, not the letter:** gate_id, owner, state, scannable-or-not, where the canonical letter lives, and a dated owner-dischargeable review clock. The fleet already built ~80% of this in `PROME/GATES.tsv` and never typed it.

**Design: one registry, envelope-only, coverage-honest; letters live at exactly one owner surface; scannable gates complete the chain.**

1. **GATES.tsv = the fleet gate registry of record, envelope-only.** Add three columns (PROME's file — PROME executes on Will's ruling): `scannable` ∈ {INSTRUMENT (named series a machine can grade) · JUDGEMENT (compound/event; owner grades) · OWNED-ELSEWHERE (metric owner named)} · `definition_surface` (repo path + anchor of the ONE canonical letter, owner-side) · `review_by` (dated, owner-dischargeable — replaces the undischargeable staleness-flag pattern, D5). **The condition cell becomes a one-line summary + pointer; the full letter is NEVER copied into the registry** — D2 is caused by two homes, and the fix is one home + pointer, not better sync (PAT-006).
2. **Scannable (INSTRUMENT) rows must complete the chain: row → named metric surface → named reader.** CREED's proposed detector, generalized and adopted as the build: `registry_chain_check` — for every INSTRUMENT row (GATES.tsv + the 3 desk registries), assert (a) the named metric surface exists (VX row / METRIC_MAP entry / watcher script), (b) a boot step or script reads it, (c) any tool-side literal for the same gate matches the registered level (kills D3's silent forks). Would have caught CREED-T-02 on 2026-07-27 (the day its registry was built), VIOLET's 71.0, and SAM's missing CFTC lines.
3. **JUDGEMENT rows are visible, not gradable — and that visibility is the point.** A scanner prints "N judgement gates, M past review_by" instead of silence; fixes both the lie-by-omission (unscannable gates absent = coverage looks complete) and D6 (the sweep enumerates the whole registered set, and `review_by` gives the un-scannable rows the dated check the scannable ones get for free).
4. **Who scans what (WALTER sub-Q 2/3):** WALTER's boot scans INSTRUMENT rows only (it already does RED+REGINALD+CREED-approved — this makes the accidental set principled and bounded); owners grade their own JUDGEMENT gates at boot (their read-loops already do — the discipline exists, the clock doesn't); PROME sweeps the envelope (review_by lapses, state staleness) via the gates-hygiene pass it already runs, now dischargeable. Cross-desk gate scanning is thus split by scannability, and no desk is asked to adjudicate another's judgement.
5. **Registration-time (D7):** the `scannable` cell + definition_surface + review_by become required fields in the forum-4 #11 registration checklist (Will-ruled 8/17, mine to build at BLUEPRINTS — same territory: construct validity, instrument naming, qualifier completeness). "Sessions"-class undefined terms are a checklist item: every counted unit in a letter names its calendar.

**Explicitly NOT proposed:** migrating the six families' letters into op/value TSVs · new per-desk registry files (GATES.tsv + the 3 desk registries suffice; a desk MAY adopt the CREED all-gates form locally) · any change to RED/REGINALD/CREED mechanics (they are the working exemplars) · WALTER adjudicating judgement gates.

**Interlocks (reconcile, don't double-count — PROME 8/20 scope-add):** the ~8/28 wiring sweep's per-agent declaration item carries BOTH the predictions-ledger path AND the gate `definition_surface` declaration in one per-desk pass · the ~9/1 ledger_staleness manifest build picks up FALCON/HAWK `thesis/PREDICTIONS.tsv` (D4 seed data, measured) · the 8/24-docketed 0-OPEN-books row covers FAL-05-owed and GATE-SAM-0-live.

## §4 Effort / EV / first steps (on Will's ruling)

| Step | Owner | Size |
|---|---|---|
| 1. GATES.tsv 3-column add + 25-row envelope pass (type each row's scannable cell; point definition_surface; set review_by; **fix the 3 measured D2 drifts as the pass's first work**: FALCON-001 condition cell re-pointed, TERRY-006 row dispositioned live-or-retired with TERRY, LIQ-076 contradiction resolved with LIQUID) | PROME (file owner), owner packets for the 3 drifts | one PROME sitting + 3 packets |
| 2. `registry_chain_check` build (per CHECK_STANDARD §3/§8/§9: alert+clean paths watched, rc 0/1/2) | DAEDALUS | one build slot; slots after docket_view unless ruled ahead |
| 3. Checklist fields into forum-4 #11 registration checklist | DAEDALUS | rides the already-ruled #11 build |
| 4. WALTER boot scope = INSTRUMENT rows (principled set) | WALTER (own lane, already Will-approved for CREED) | note, not work |

**EV:** D1 (a fired-but-invisible gate cost 6 weeks THIS MONTH), D2 (a canonical cell stale against a fire that already happened), and D3 (a live position's re-open level forked by a hardcode) are each individually worth the column pass. The check makes all three classes detectable the day a row is born.

---
*Fleet lesson banked: PAT-006 evidence extended (registry-cell-as-copy drift, n+3, both directions). CREED's D1 finding already carried as auto-memory `finding_banded_threshold_with_no_metric_surface_is_untrippable` — cited, not duplicated.*
