# ORCH_LOG `zero_capital` — the carried repair, RESOLVED AS DECLINE + a one-line header edit

**Written 2026-09-12 22:39 ET** (LAPTOP `WilliePOwen`, Opus 5) · **Owner:** PROME · **Status: DECISION RECORDED; the
header edit is the ONLY proposed change and it is pending an independent cold read** (the two-correction
stop on `PROME/state/ORCH_LOG.tsv` is standing, carried from a prior session).

---

## What the carried item actually was

`PROME/SCRATCH.md` owed-item ⓑ and the STATUS work-queue row both read *"ORCH_LOG `zero_capital=OK` —
still blocked on an independent cold read OF THAT DIFF."* ⛔ **The referenced diff is not locatable** — it
survives in neither `PROME/proposals/`, `PROME/reports/`, the archives, nor `git log -S`. The item was
carried by its *symptom string* and lost its *deliverable*, the same shape as SCRATCH ⓓ (*"LABOR spawn-card
step-3 text NOT LOCATED — ask or drop"*). `[[finding_dated_carry_item_has_no_expiry_check]]`

**Re-derived from the artifact instead.** The defect the string names is real and reproducible:

| Observed | Count |
|---|---|
| `OK` (bare) | 86 |
| `yes` (bare) | 23 |
| `OK` + trailing prose | 5 |
| `yes` + trailing prose | 3 |

**The column carries two vocabularies.** The schema header defines `OK` and never says it is the only legal
value, so 23 pre-schema-v2 rows say `yes` and nothing ever reconciled them.

---

## DECISION: do NOT normalize the historical rows

Four findings at the artifacts, each checked, none inferred:

1. **The owning checker passes either.** `python3 scripts/orch_log.py check` → `ORCH-LOG ✓ 117 data rows ×
   13 columns, typed cells int-or-EMPTY`, rc 0. `zero_capital` is not a typed cell and is not validated.
2. ★ **The only metric consumer already accepts both, deliberately.**
   `AGENTS/DAEDALUS/scripts/scorecard.py:350` tests the cell's first token against
   `{OK, YES, ZERO, N/A}`, and `:488` documents it in the rendered scorecard as *"the cell is free text"*.
   Normalizing would change no metric anywhere.
3. **The second consumer does not gate on it.** `coordination_scorecard.py:171` builds a `Counter` of the
   distinct values; it reports the spread, it does not require a token.
4. ⛔ **Three of the 23 rows carry prose** (`yes — $0`, `yes — $0, no fill`). A token-only rewrite destroys
   the better-described rows and keeps the barer ones —
   `[[finding_status_token_membership_test_desupervises_improved_rows]]`.

⇒ **A 23-row rewrite of an append-only operational ledger, changing no consumer's output and costing
information on 3 rows, is not a repair.** The last time a sealed ledger here was hand-edited it took 12
errors plus a broken seal (2026-09-12, CODEX audit). **Declined on the evidence, not deferred.**

## The ONE change proposed — the header, so nobody re-derives this

Reason: this item has now cost two sessions precisely because the header states a token without stating the
vocabulary, which reads as a violation to every fresh reader.
`[[finding_correction_beside_an_instruction_leaves_two_live_instructions]]` — so the header is REPLACED in
place, not annotated.

**Current (line 1, one segment of the schema prose):**

```
zero_capital (OK = $0 moved, no thresholds, gated items returned to PROME)
```

**Proposed:**

```
zero_capital (OK = $0 moved, no thresholds, gated items returned to PROME. ⛔ TWO VOCABULARIES ARE LIVE
AND HISTORICAL ROWS ARE NOT TO BE NORMALIZED: 23 pre-v2 rows read `yes`, DAEDALUS scorecard.py:350 accepts
{OK, YES, ZERO, N/A} by design and calls the cell free text, and 3 of the 23 carry prose a token-only
rewrite would destroy. NEW rows use OK. Decision record: PROME/proposals/2026-09-12_orch-log-zero-capital-DECISION.md)
```

### Invariants the edit must not break

- **I1** Exactly one line is touched (line 1, the comment header). No data row changes. Row count stays 117.
- **I2** `python3 scripts/orch_log.py check` returns rc 0 and still reports 117 data rows × 13 columns.
- **I3** No tab is introduced into the comment line — a tab there would make the header parse as a data row.
- **I4** The replacement REPLACES the old clause; the file must not end up carrying both the bare
  definition and the amended one.
- **I5** Nothing in the edit asserts a capital fact, a level, a threshold or a gate state.

### Disposition of the standing stop

The two-correction stop on this file is carried from a prior session and is not discharged by this
decision. **The DECISION above required no edit and is therefore not gated by it.** The header edit is,
and the independent cold read is commissioned for exactly that one-line diff — no wider scope.

**Completion state (WQ-229):** the decision is **IMPLEMENTED** (recorded here). The header edit is
**PROPOSED ONLY** — not implemented, not tested, not verified.
