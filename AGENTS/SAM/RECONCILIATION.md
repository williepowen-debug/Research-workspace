# SAM — POST-CATALYST RECONCILIATION

**Trigger:** run when a *scheduled* catalyst resolves — BOJ MPM, FOMC, or a major data print (CPI, NFP, trade balance, key auction). Not for routine boot refreshes.

**Why this exists:** the Jun-14→16 BOJ window proved that even a careful write-back + a peer review leaves derived surfaces carrying the pre-event framing. Drift hid in the *derived* docs (THESIS catalyst-table, CATALYSTS.tsv, NEXUS), not the owner doc; and a schema/order bug in `usdjpy.py` was silently feeding a stale spot to boot. A mechanical sweep + lint catches both classes; eyeballing does not. Lessons institutionalized here: `[[finding_doc_mirror_consistency_check]]`, `[[finding_verification_correction_downstream_propagation]]`, `[[finding_threshold_vs_mechanism]]` (trajectory-before-resolve), `[[finding_followup_audit_pass]]`.

*This is the SAM-local binding. The domain-agnostic version is proposed for PROME to own fleet-wide (see `outbox/2026-06-16_to-PROME_reconciliation-protocol-fleet.md`). If PROME stands one up, this file becomes "SAM's surfaces + bindings" and defers the generic disciplines to the fleet doc.*

---

## THE THREE DISCIPLINES

### 1. SWEEP — cross-surface consistency (mechanical, not by-eye)
For **every mark you changed** (probability, level, label, status), `grep -rIE` the OLD value/phrasing across all live docs and confirm none survives as a *live* mark.
- Dated / CHANGELOG / TIMELINE / event-log mentions are **expected to survive** — they're history, leave them.
- A pattern hit is only a failure if it reads as *current state*. When in doubt, check whether it sits under a "superseded"/dated marker.
- This is the catch the Jun-16 oil-relabel missed (landed in STATUS/TRADE/CALENDAR, not THESIS) until the sweep flagged it.

### 2. TRUE-UP — resolution integrity
- **Trajectory carries the FINAL mark BEFORE you flip Status.** Score calibration against your last estimate, not a stale one (SAM-23 had to read …→~72%→~30% before resolving FAILED, or the no-show scores against the wrong number).
- After the pass: **0 OPEN predictions** the catalyst resolved; **no past-dated event** left in a forward/pending table.
- Resolve on the catalyst's own terms — apply pre-registered frames, don't re-derive.

### 3. EDIT-CLASS-TAG-AS-GATE
Tag every edit by class and **keep commits pure — one class per commit:**
- `[propagation]` — flip wrong-now references to the resolved fact. **References only**: status labels, checkboxes, probability cites, catalyst-table rows. NEVER rewrite the playbook/spec, touch money fields (cost basis, size, strikes, expiries, stops), compress, or add new analysis.
- `[cleanup]` — schema/hygiene (field counts, sort order, whitespace, generator bugs).
- `[thesis-change]` — actual view moves; log old→new in `thesis/CHANGELOG.md`. (A relabel/resolution is NOT a thesis-change.)
The **two sweeps (1 + 2) are the pre-commit gate** — run them, confirm clean (modulo intentionally-retained dated/analysis lines), then commit. Auto-regenerated files (boot.py-written tsvs): fix the *generator*, don't hand-tag the data (ephemeral).

---

## SAM'S SURFACE ORDER (owner-doc first, derived after)

| # | Surface | Action on catalyst resolution | Class |
|---|---|---|---|
| 1 | `thesis/PREDICTIONS.tsv` | Resolve every due row — true-up trajectory (Disc. 2) THEN flip Status/Date/Outcome/Notes. Keep 9 fields. | propagation |
| 2 | `STATUS.md` | Lead the banner with the resolved event (outcome/vote/reaction/path-effect). Relabel pending→resolved. **Full compression to <250 lines = its own pass** (migrate narrative → TIMELINE). | propagation (+ compression) |
| 3 | `docket/CALENDAR.md` **+** `docket/CATALYSTS.tsv` | Mark resolved; add next catalysts; **keep the two in lockstep** (same dates/events; CATALYSTS field-count = header). → **KOYOMI** owns this. | propagation → KOYOMI |
| 4 | `thesis/THESIS.md` **+** `thesis/CHANGELOG.md` | Flip catalyst-sequence rows / status / one-liner refs. Log old→new **only if a view moved**. | propagation / thesis-change |
| 5 | `thesis/timeline/TIMELINE.md` | Add the RESOLVED narrative entry (this is where event play-by-play lives). | propagation |
| 6 | `NEXUS_BRIEF.md` | Sync the status/as-of line to the new STATUS. | propagation |
| 7 | `TRADE.md` / `STRATEGY.md` | **LAST.** Flip references only (boxes, PENDING/WATCHING, prob cites — these ARE reference cells, must be *flipped* not just prose-refreshed). Money fields frozen unless a Will-approved decision. Playbook/staging untouched. → **METSUKE** flags staleness. | propagation → METSUKE |

**Routing:** KOYOMI = docket lockstep + CATALYSTS schema. METSUKE = TRADE/STRATEGY drift (propose-only; never money fields). Both spawned on command, not network peers.

---

## PRE-COMMIT CHECKLIST
1. [ ] PREDICTIONS: due rows resolved, trajectories carry final mark, 0 OPEN, no past-dated forward event.
2. [ ] Sweep clean: `grep -rIE "<changed marks>"` across THESIS/STATUS/CALENDAR/CATALYSTS/TRADE/STRATEGY/NEXUS → only dated/CHANGELOG/superseded-marked hits survive.
3. [ ] Commits class-pure (no `[propagation]`/`[cleanup]` bleed); money fields untouched.
4. [ ] Auto-regenerated data files: generator fixed, not hand-tagged.
5. [ ] CALENDAR ↔ CATALYSTS in lockstep.
