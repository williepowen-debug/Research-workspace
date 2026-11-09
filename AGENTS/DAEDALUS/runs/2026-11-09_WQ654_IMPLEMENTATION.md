# WQ-654 bounded implementation — 2026-11-09

Authority: `PROME/proposals/2026-11-07_wq654-RULED.md`, Will “654 A”; current session Will “okay then go ahead”. No unrelated inbox work or new fleet audit.

| Item | Implemented result |
|---|---|
| 1 | Separate profile-refresh row retired, resolve_by cleared; nine whole profiles and twelve targeted deltas credited. Prior row preserved verbatim in WQ654_PRIOR.json. Individual vintages untouched. |
| 2 | Profile child removed from sweeps_due; executable command and rc0/1/2 interpretation inserted into Production Review. Parser unchanged. Legacy --no-profile-clock accepted as no-op. Gate label and one stale charter phrase aligned. |
| 3 | A09 no longer a required closure leg. Gate-spec/closeout lines retained; revisit on own-charter edit or concrete contradiction. |
| 4 | Active 90-day Harness detection clock October 4; next January 2, 2027. Scope narrowed to WQ-577 removals/simplifications and git/authority/trade-path contradictions across all charters, changed or unchanged. |
| 5 | Provider switch counts as model upgrade even when exact version unknown; unconditional review preserved, no detector. Current runtime/provider review remains unverified, outside this implementation. |
| 6 | Four affected basis identities refreshed (sweeps, unchanged profile checker, gate label, charter phrase); other snapshots remain explicitly historical. PROME owns READS update after implementation receipt. |

REVIEW: required — changes guard invocation/read boundary and cadence state; scope scripts/sweeps_due.py, gate B1 label, invocation tests, registry two rows, both playbooks, CHECKS two rows, basis hashes, charter SPAWN5 phrase, unchanged profile checker and read-declaration consumers; reader `/root/wq654_review`; disposition APPLIED 1, RESIDUE 1 (PROME owner declaration application). Exact hashes, ranges, counterexample and caveats: `runs/2026-11-09_WQ654_REVIEW.md`.

POST-INITIAL-REVIEW: one false charter invocation phrase removed and its basis identity refreshed; reader reread both and accepted final bytes. No other reviewed implementation changed after acceptance. Continuity, delivery and self-row reconciliation are register/prose write-back, not a fresh grade or scope change.

Validation: new invocation tests 3/3, retained profile tests 17/17, existing boot-reporting tests 12/12, sweeps selftest 5/5. Original-code negative control fails 2 of 3 invocation tests. Standalone checker clean rc0, alert rc1 and malformed rc2 watched through CLI; independent mixed alert/refusal case passes. Evidence `runs/2026-11-09_WQ654_VALIDATION.json`. Live cadence: rc0, 17 tracked, zero skipped/resolve_by passed. Standalone November 9 profile run: rc1, 38 attempted, 33 evaluated, 5 undated, 0 cannot-evaluate. This is instrument verification, not a Production Review; no profile/body/Production-Review clock reset.

CHECKS final state: sweeps_due and profile_clock_check both WIRED-SINGLE-INVOKER. The former runs at boot/closeout via its owner gate; the latter is an executable step in exactly one protocol (Production Review). The counterpart's MANUAL-BY-DESIGN suggestion conflicts with the register's existing token definition; final reader independently accepted WIRED-SINGLE-INVOKER. No token introduced.

Coverage limits retained: no fleet runtime/hooks behavioral test; October 23 did not reread whole ORCHESTRATION_PLAYBOOK, NEXUS or WALTER BOOT_PROTOCOL. No whole-audit closure, L5 clearance, owner-charter edits, other retirement or runtime test claimed. Existing ZHAO/Will, WQ-601 unit 4 and TERRY consumer conditions remain.

Read declarations requiring PROME application by identity: READ DAEDALUS profiles/*.md (no longer boot summary; now Production Review); BASIS sweeps_due.py (remove conditional child); BASIS profile_clock_check.py (no longer boot-defining, retained review instrument). Update affected gate/charter identity reference as appropriate. Physical lines observed 286,291,292 are locators only. New hashes live in registry/basis-hashes.json; no shared registry edit by DAEDALUS.

No new blueprint/ladder standard: this is an approved maintenance invocation/playbook change; UPGRADE_PROTOCOL, profile clock contract and individual profiles unchanged. Required EVOLUTION read completed, no new standards-pairing claim. Prior self-row and status/handoff text preserved in WQ654_PRIOR.json and FLEET_MAP_HISTORY.tsv; generated directory refreshed, grade/date unchanged.

Publication, final gate results and PROME application/consumption are recorded separately; an accepted implementation does not certify those steps.

Closeout 20261109T155847Z rc 0: CLEAN 8, DUE 1 ledger nudge, no BLOCKING/UNKNOWN; check-register/self-row updates are in this commit, PATTERNS/SURFACES data unchanged. Re-read amended Harness playbook and applied its scope to this package; no expanded audit. Final inbox enumeration unchanged, WQ-654 handled by this result; three unrelated packets retained pending. Exact reviewed hashes rechecked 11/11.
