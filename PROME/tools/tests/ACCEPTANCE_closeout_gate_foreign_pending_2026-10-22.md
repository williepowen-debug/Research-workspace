# ACCEPTANCE — closeout gate: foreign PENDING arrivals after the freeze are advisory, not blocking (Will 2026-10-22 12:34 ET)

**Written BEFORE the edit (WQ-229), PROME a5be8f8c.** Will's word, verbatim: *"This seems to happen almost everytime. We need to change these rules"* — on the closeout report line that the gate's 'ARGUS review manifest' check blocked six times on other desks' files dropped after the freeze (DOCKET L796). Defect in its own terms: `argus_contract.verify()` on the WORKING TREE treats every inventory path without a matching observed snapshot as an error, including files another owner created or changed after the freeze that PROME's commit never touches; with a live fleet the check cannot converge.

## Acceptance conditions
- **AC1 ordinary:** a PENDING path created or changed after the freeze by a non-PROME owner (not OWNED by perimeter rule, no PROME authorship evidence) makes `--verify-review` (working tree) return rc 0 with a `FOREIGN-PENDING (advisory)` line naming it.
- **AC2 wrong owner:** such a path in PROME's OWNED lane, or carrying PROME authorship evidence, still returns rc 1 `UNCLASSIFIED`.
- **AC3 delivered content:** a delivered path whose bytes changed since the freeze still returns rc 1 `CHANGED-SINCE-REVIEW`.
- **AC4 delivery commit:** `--verify-review --ref <sha> --paths …` is unchanged — actual commit paths outside the delivered set still fail (`UNREVIEWED ACTUAL COMMIT PATH`); foreign pending files are not in the commit and never were checked there.
- **AC5 suites:** the four argus test suites stay green.
- Neighbours: overlap (a foreign path both committed-since-baseline and pending: advisory on the working tree, attributed-by-commit for the committed side) · missing information (an observed record present but stale for a foreign path: advisory, the newer version is listed) · concurrent activity is the case itself.

## Results
**Run 2026-10-22 12:36 ET on the live tree (mini-frozen candidate bf4c0a77…, 2 delivered paths):**
- AC1 ✅ working-tree `--verify-review` rc 0 with two REGINALD files that arrived during the check listed as `FOREIGN-PENDING (advisory)` (AGENTS/REGINALD/CALENDAR.md, archive/CALENDAR_rotation_2026-10-22.md).
- AC2 ✅ an OWNED pending probe (`PROME/state/_ac2_probe.txt`, created and removed for the test) ⇒ rc 1 `UNCLASSIFIED`.
- AC3 ✅ one appended line on a delivered path ⇒ rc 1 `CHANGED-SINCE-REVIEW`; restored ⇒ rc 0.
- AC4 ✅ (observed earlier the same sitting, 12:3x ET): `--verify-review --ref` on a HEAD that was WAL's commit reported `UNREVIEWED ACTUAL COMMIT PATH: AGENTS/WAL/NEXUS_BRIEF.md` — the delivery-commit check is untouched by this patch (code path: `target is None` guards the advisory branch).
- AC5 ✅ four suites OK (15 · 28 · 6 · 37).

**State: IMPLEMENTED · TESTED. INDEPENDENTLY VERIFIED: owed — one counterexample read (Opus) at the next boot, before the first closeout that relies on it (DOCKET L796). Will's word 12:34 ET authorized the change; the read is PROME's WQ-229 duty, not a second approval.**
