# AUDIT CONVENTION — RULED 2026-08-12 (Will, in-session, session 3)

**Ruling artifact of record. Owners CITE this file; do not reconstruct the ruling from packets or SCRATCH prose.**
*(Same single-reference pattern as `2026-08-12_rule-batch-RULED.md` and `2026-08-04_roster-phase0-ruling-table-RULED.md`.)*

**Will's word:** *"ok approved go ahead"* — on PROME's presentation of: Ruling 1 at **fleet scope** (PROME's rec, the flagged decision point), Ruling 2 **adopt as BRENT spec'd**, riders **approve as rec'd**. Batch-style approval off PROME recs; **flag-before-encode applies to every owner** — if a ruling is wrong on the merits, say so before encoding, do not encode a guess.

**Source findings:** `AGENTS/BRENT/AUDIT_2026-08-12_self-audit-canonical-surfaces.md` (F-series) + `AGENTS/BRENT/AUDIT_2026-08-12b_INCIDENTS-ledger-sweep.md` incl. ADDENDUM (I-series). All numbers below are BRENT's, verified per those reports. **ZERO capital, ZERO thresholds moved.**

---

## RULING 1 — THE CONVENTION (clears F-2 · F-3 · I-1 · I-4 · I-5 · I-9 as ONE decision)

**Adopted, FLEET SCOPE:**

> **A stored value must carry its unit and basis; a threshold must name the instrument that grades it (a continuous series is not a contract); and "zero" must be distinguishable from "unknown" and from "not applicable."**

**Why fleet, not BRENT-local (the ruled question):** the same defect class surfaced in TWO desks independently on the same day — BRENT's six findings above, and RED's n=4 "registry names a CONCEPT, tool resolves an INSTRUMENT" (FT-03/04 · FT-06 · VX-017 flip · the $100.19 figure). Precedents: the 36b/L-15 ruling (8/12, same shape, ruled UP to fleet with DAEDALUS encode) and STATE_VOCABULARY Class 4 (8/12, shipped off SIG-006's one-token-many-states finding).

**Ownership split:**
- **DAEDALUS — owns the fleet encode:** convention text into `BLUEPRINTS/STATE_VOCABULARY.md` (zero/UNKNOWN/N-A token classes) + the blueprint layer (unit/basis field requirement on quantitative TSV columns; threshold rows name their grading instrument; continuous-series-is-not-a-contract). **F-7's `basis_check` rides here as the enforcement arm** (scoped to NON-dated blocks — dated history is exempt per BRENT's own canon; anti-ratchet: extend an existing checker where possible, and the encode should name what it supersedes). New surfaces use canonical tokens; legacy grandfathered per STRICT_TEXT/STATE_VOCABULARY standing rules.
- **BRENT — first application, own surfaces:** ① F-2: the ABOVE-100/120/140 futures-vs-spot registry pairs — rename to carry basis OR mark one authoritative + demote the other to `informational` (BRENT's choice of mechanism; the convention requires only that a grader can never present them as one test). ② F-3: the six `BZ=F`-keyed thresholds — pin to a named contract with a documented roll rule, or record roll adjustments on the row. ③ INCIDENTS schema: `capacity_unit` + quantity covering **BOTH** `bpd_offline_est` AND `capacity_bpd` (I-9), value vocabulary separating restored-zero / intact-zero / anti-double-count-zero / **UNKNOWN** / **N-A-wrong-unit** / blank (I-1 · I-4 · I-5), plus a **facility key** (I-6's mechanical re-strike blindness).

**In force immediately, no encode needed:** **no aggregate over `refinery_damage/INCIDENTS.tsv` is quotable** until the schema carries units — it is an EVENT RECORD, not a CAPACITY MEASURE (BRENT's verdict of record, restated here so it binds fleet-readers, not just BRENT).

## RULING 2 — I-2 STALENESS BUDGET (the separate item)

**Adopted as BRENT spec'd (numbers are BRENT's):** `status=ACTIVE` is a present-tense claim; any ACTIVE row unverified **≥60d ⇒ re-verify-or-downgrade**, surfaced at boot, built as an **extension of `instrument_check.py`** — not a new script. Context ruled on: 23 ACTIVE rows at median 124d, the 18 rows ≥90d carrying 74% of the asserted total, all source_tier A-1.
**First work ticket under the budget:** the RF-033 Borouge/EGA carry-item, unverified 73 days (ADDENDUM).

## RIDERS — approved as recommended

- **F-4:** `KILL-LEG2-TRANSIT` relabeled **"post-hoc confirmer, not a live exit trigger"** (measured 3–8d PortWatch lag vs dated-option exit windows). No weakening — the falsifier's letter is untouched. Any live-exit instrument is a separate N1 build BRENT proposes on its own paper (prompt premium named as candidate, NOT registered).
- **I-3:** `# COVERAGE:` header on INCIDENTS naming the 5/17→7/12 gap **verified-quiet** (BRENT probed: de-escalation window, zero June events in its own CHANGELOG/TRACKER).
- **I-7:** Ras Laffan force-majeure provenance repointed to `thesis/THESIS.md` (which carries it); superseded pointer dated, not deleted.

## STAYS OWNER-LANE — no ruling needed

I-6 Dos Bocas candidate double-count (≤50K bpd, domain judgment) · I-8 owed Novorossiysk row · F-6 catalyst-retention pruning. F-1 and F-5 were fixed in session 2. All already on BRENT's carry-forward list.

---

## Execution

Standard riders travel on every edit: **dated re-spec · superseded text preserved verbatim · no threshold moved in the same edit.**
PROME 2026-08-12 session 3: this file + packets to **BRENT** (first application) + **DAEDALUS** (fleet encode) + **RED** (cc — its registry-basis class rides the same convention) + SCRATCH/queue reconciled.
**This ruling closes on OWNER ENCODE CONFIRMS, not on the approval** — BRENT and DAEDALUS confirm via run report or `PROME/inbox/`; PROME chases at boot.

— PROME
