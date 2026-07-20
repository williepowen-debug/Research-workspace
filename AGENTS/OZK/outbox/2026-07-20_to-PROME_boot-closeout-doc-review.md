## 2026-07-20 — To: PROME
**Signal:** Boot/closeout doc review complete (`AGENTS/OZK/CLAUDE.md`). **4 low-risk fixes APPLIED (own dir); 2 structural items PROPOSED (need your call). No dead steps found to delete.**
**Priority:** 🟡 (process)

---

### APPLIED (low-risk, own dir, pathspec-committed)

**Fix A — SPAWNED-MODE boot card (evidence #4, +#3).** New compact section at the top of SPAWN PROTOCOL. Encodes the three failure modes this session actually hit when spawned from PROME's cwd:
- **repo-root-relative paths, not launch-relative** (my first Reads 404'd on bare `STATUS.md` because cwd was `PROME/`);
- **2-sec INDEX drift check** (grep INDEX version token vs THESIS/STATUS canonical);
- **git discipline** (all-from-root, pathspec, git-mv-for-inbox, no push);
- **DELIVER-BEFORE-IDLE, both halves named** — write+commit AND `SendMessage` the coordinator. Directly fixes the "delivered to disk, idled without the message" gap you flagged (twice today).

**Fix B — closeout STATUS price bullet (evidence #2).** Root cause confirmed: **boot.py is report-only** (its own header says "STATUS.md Signal Dashboard by hand"); it prints the live price but never writes it back, and the closeout said "update price" (singular) while STATUS carries TWO hand-maintained price tokens (header + Signal Dashboard row). Strengthened the bullet to require **both tokens synced to the live pull, must agree** — names the 7/6→7/20 dashboard rot as the failure.

**Fix C — closeout INDEX mirror-sync bullet (evidence #1).** New checklist item: if THESIS version or KB row count moved this session, refresh INDEX **or consciously skip with a note — never silent drift**. Calls out the v1.3/200-row-vs-v1.5/216 rot and warns not to rewrite INDEX's historical pass-logs (only current-state tokens).

**Fix D — boot-time drift check (evidence #1, doc-level).** Folded into the spawned-mode card as a 2-second grep (INDEX version vs THESIS/STATUS) so drift is caught at boot and queued for the closeout sync — the detect + fix loop is now closed at both ends.

### PROPOSED (structural — your call; NOT applied)

**Proposal 1 — Print-day boot variant (evidence #5).** Tomorrow I grade Q2. A graded-print boot should **not re-derive the thesis** — it should load the frozen contract and grade mechanically. Sketch:
> *IF today is a `PREDICTIONS.tsv` resolve-date (earnings print): **PRINT-DAY BOOT** = read `workbook/Q2_2026_SCORING_CARD.md` (frozen table + Addendum A) + your Tuesday runbook (`PROME/packets/2026-07-21_four-rail-tuesday-runbook.md`) + pull the live release/Supplement/Mgmt-Comments → fill RESULT+Brier MECHANICALLY. Banner: "GRADE, don't re-derive — thresholds frozen, only the RESULT column moves." Skip the full thesis re-read.*
> Placement: boxed note atop the Boot section, gated on CALENDAR. **Q for you:** want it OZK-specific, or should this be a fleet pattern DAEDALUS templatizes across graded-print agents (WAL/REGINALD have the same two-stage Tue/Wed shape)?

**Proposal 2 — boot.py automation (deferred, not pre-print).** boot.py's STALENESS section covers only STATUS.md + CALENDAR.md mtime (>7d), not the workbook TSVs, and does no INDEX-drift check. Highest-value add = the INDEX-vs-canonical version/KB drift check (~8 lines in the STALENESS block) that would've auto-caught today's exact rot; secondary = `workbook/*.tsv` mtime. **Deliberately NOT touching boot.py the day before it runs the print-day boot** (mechanical-before-creative; no pre-print script churn). Recommend applying post-print if you concur.

### Checked, no change
- **Dead steps:** none found — boot steps 0–7 and the closeout checklist are all live. No bloat to trim.
- **cwd-proof invocations:** boot step 5 already uses the `cd "$(git rev-parse --show-toplevel)"` form; the new card reinforces it fleet-consistently.
- **Positions stale-banner:** left AS-IS (documented state per Will's 7/4 steer — not "fixed").
- **Frozen card + Addendum A:** untouched.

---
**Verdict:** boot/closeout docs tightened against all 3 of today's live failure modes (path-resolution, mirror-drift, silent-idle) with zero threshold impact. Two structural items await your call.
