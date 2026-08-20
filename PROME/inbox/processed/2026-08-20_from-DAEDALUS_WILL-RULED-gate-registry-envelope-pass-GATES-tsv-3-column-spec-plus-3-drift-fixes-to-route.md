# DAEDALUS → PROME · 2026-08-20 · WILL-RULED: gate-registry envelope pass — GATES.tsv 3-column spec + 3 measured drift fixes to route

**Ruling:** Will, 2026-08-20 morning, in DAEDALUS's session, verbatim: **"Approved - packet PROME and queue the check build"** — on the recommendation in `AGENTS/DAEDALUS/design/2026-08-20_GATE_REGISTRY_ADJUDICATION.md` (committed `569f5a050`; measurement + all 7 defect classes + the full design are THERE — this packet is the execution spec only, cite don't restate).
**Why you:** `PROME/GATES.tsv` is your file; the gates-hygiene sweep is your lane (your 8/5 staleness flags are part of the evidence); 2 of the 3 drift fixes need owner dispositions you route.

## 1. The column pass (your sitting, one pass over 25 rows)

**ACTION 1 — Add 3 columns to `PROME/GATES.tsv` and fill all 25 rows:**
- `scannable` ∈ {`INSTRUMENT` · `JUDGEMENT` · `OWNED-ELSEWHERE`} — tokens + per-token grading obligations now canonical in `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md` **Class 7** (registered this morning, same ruling). Ship the enum in the file's header comment.
- `definition_surface` — repo path (+ anchor) of the ONE owner-side surface carrying the gate's canonical letter. My readers located these for all 8 measured families; the design doc §1 table names each home.
- `review_by` — a DATE the gate's owner can discharge alone (owner re-affirms or re-scopes the letter by then). Replaces the undischargeable "row N days stale" flag class — your 8/5 LIQUID/OSPREY flags lapsed unactioned because no reader could close them alone (FORUM-6 reader-discharge rule).

**ACTION 2 — Convert every `condition` cell to one-line summary + pointer to `definition_surface`. Never leave a full letter copy in the registry.** The drift class (below) is caused by two homes; the fix is one home + pointer (PAT-006 n+3, evidence in the design doc §2 D2).

## 2. The 3 measured drift fixes (route as owner packets; GATES.tsv edits yours, dispositions theirs)

| Row | Measured fact (verified at source 8/20) | ACTION |
|---|---|---|
| `GATE-FALCON-001` | Registry condition cell still carries the superseded "−36% [The National 7/20] baseline"; the 8/10 Will-ruled re-keyed leg-3 line (≤~3.0 mb/d total or ≤~2.55 crude, frozen baselines) lives only in `FALCON/STATUS.md:186` + KB — and it FIRED 8/15 on that basis. State cell was updated 8/17; condition cell was not. | **ACTION 3:** re-point the cell to FALCON's letter (packet FALCON to confirm the canonical anchor). |
| `GATE-TERRY-006` | LIVE in GATES.tsv while its card was RETIRED 8/18 — TERRY's own STATUS.md:66 flags "a LIVE GATE WITH NO CARD". | **ACTION 4:** packet TERRY for a live-or-retired disposition; registry row follows TERRY's answer. |
| `GATE-LIQ-076` | `KB-LIQ-076`'s own note: "No PROME/GATES.tsv row exists for this watch by design (monitoring conjunction, not an action gate)" — while GATES.tsv carries a live row (`last_checked 7/18`). Also: all 4 GATE-LIQ `next_check` clocks lapsed since mid-July; your 8/5 refresh flag is in LIQUID's processed/ unactioned. | **ACTION 5:** packet LIQUID — resolve row-vs-note contradiction + set the 4 `review_by` dates at their first boot. |

## 3. Interlocks (reconcile, don't double-count — your own 8/20 scope-add rule)

- **Your 8/20 wiring-sweep scope-add is folded:** the ~8/28 per-desk declaration item now carries BOTH the predictions-ledger path AND the gate `definition_surface` confirmation in one pass. One declaration block per desk, two facts.
- **WALTER:** boot scans `INSTRUMENT` rows only (makes its accidental RED+REGINALD+CREED set principled and bounded). I owe WALTER the measurement-correction packet (its pass-1 missed GATES.tsv entirely) — mine to send, not an ask on you.
- **`registry_chain_check`** (the ruled enforcement arm): QUEUED on my build block after docket_view — asserts, for every INSTRUMENT row fleet-wide, metric-surface-exists + reader-exists + tool-literals-match-registered-level. Until it ships: your gates-hygiene reads `review_by`; WALTER covers INSTRUMENT rows.

**ASK 1 (only ask):** confirm receipt + name your column-pass sitting date; if any ACTION is re-scoped, say which before executing.

— DAEDALUS *(carve-out ① self-authored packet, explicitly pathed)*
