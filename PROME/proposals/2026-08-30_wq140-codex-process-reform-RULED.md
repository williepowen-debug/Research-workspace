# WQ-140 — Codex process-reform batch — RULED + EXECUTED
**Ruled:** 2026-08-30 22:56 ET, Will verbatim *"approved go ahead"* (on the amended package; same word covers WQ-141) · **Executed:** same sitting, ~23:0x ET · **Forward-only — no retroactive sweep ruled.**
**Provenance:** Codex 8-item process review relayed by Will ~22:48 → PROME assessment (core-three swap: assertion ledger → confidence vocabulary) → Codex 2nd-round reply with four refinements + one governance catch (all verified, all adopted into the rec) → ruling.

## The ruled package
| # | Item | Disposition |
|---|---|---|
| ③ | Measurement helper | **ADOPTED, built:** `PROME/tools/measure.py` — SOLE approved source for reported byte/line/crc receipts. wc semantics, labeled units, re-reads at receipt time, crc32-excluding-final-newline (archive convention). Falsification set `--selftest`: 18/18 PASS at build (published crc vector · Unicode bytes≠chars · missing final newline · multiple trailing newlines strip exactly one · empty file · post-edit remeasure · `--identical` detects one extra newline · live agreement vs `wc -c`/`wc -l`). |
| ⑦ | Confidence vocabulary | **ADOPTED:** VERIFIED · INFERRED · SEARCH-NOT-FOUND · UNKNOWN, with operational definitions; absence upgrades SEARCH-NOT-FOUND → VERIFIED only after owner-declared path/identifier + documented fallback checked (a broader grep is not an upgrade). Binding on PROME reports now (`PROME/CLAUDE.md` § Session Process Controls); fleet registration packeted to DAEDALUS STATE_VOCABULARY (`AGENTS/DAEDALUS/inbox/2026-08-30_from-PROME_confidence-tokens-for-STATE_VOCABULARY.md`; may ride WQ-117 item C's encode sitting; DAEDALUS dark → rides next boot). |
| ⑤ | Two-correction stop | **ADOPTED:** two correction commits to the SAME FILE in one session (typo fixes COUNT) ⇒ stop editing that file, independent cold read before further edits. In-sitting cascades bind as discipline pre-commit; "what counts as one correction" pinned at DAEDALUS encode if ambiguity bites. |
| ② | Discovery/implementation split | **ADOPTED SCOPED:** pre-edit cold read of proposed findings/diff + invariants for root canon · registry-wide transformations · archival splits · broad batches. Post-edit validation RETAINED (different failure modes). |
| ① | Assertion ledger | **ADOPTED SCOPED:** five-field format (claim → exact artifact → verification command → observed result → proposed change) = the deliverable shape for AUDIT passes only; NOT an every-edit requirement (the vocabulary is the everyday control — Codex concurred 2nd round). |
| ④ | New blocking checks | **FOLDED:** byte==wc-c + crc round-trip → the ③ helper; pointer resolution → already-registered structure item ⑤ (`canon_check.py`); mirror divergence → weekly spine audit + `.claude/` parity (existing); header-stamp-vs-committed = closeout-gate CANDIDATE, builds under CHECK_STANDARD with negative controls, not tonight. |
| ⑥ | Atomic commits | **EXISTING PRACTICE RETAINED:** one commit per item is the norm; a deliberate single atomic commit for canon batches (one-revert rollback, WQ-137 pattern) stays legitimate when declared. |
| ⑧ | Late-session rule | **ADOPTED as correction-count policy, not clock policy:** once the ⑤ stop has tripped anywhere in a session, prefer closeout/documentation/read-only work over new broad edits. |

## Codex 2nd-round refinements (all adopted)
1. Helper = sole source, not optional; test set includes Unicode, missing/multiple trailing newlines, post-edit remeasure. *(Built as specified; PROME added: receipts re-read the file at receipt time, killing the stale-figure family by construction.)*
2. Operational token definitions; the VERIFIED-ABSENT bar as above.
3. Stop counter = correction COMMITS per file per session, typos included.
4. Pre-edit cold-read scope named as the four classes; post-edit retained.
5. Governance: non-ISO `9/4 batch` date cells fixed to `2026-09-04 (9/4 batch)` on rows 140/133/117 (gate parses ISO only — all three had been invisible to due-nagging).

## Execution anchors
`8ffca80a4` row registered · `a0c657c09` amended + ISO dates + WQ-141 registered · measure.py + `PROME/CLAUDE.md` § Session Process Controls + DAEDALUS packet + this record + row closures = the commit carrying this file. WQ-141 (same word): RESEARCH-INTAKE `8e0589d`, pushed.

## Evidence base the package answers (for the record)
Errors #34/#38 (stale byte figures) + #45/#50 (`len()` chars-as-bytes) → ③. Errors #41–46 false-absence cluster + `finding_scan_keyed_on_naming_reads_local_form_as_absence` (n=10) → ⑦/①. Error #49 + `finding_a_correction_pass_is_unreviewed_work` → ⑤/⑧. WQ-137 pass-3 (defect introduced by PROME's own repair round) → ②.
