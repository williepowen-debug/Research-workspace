# WALTER boot-basis review and READS re-attestation — 2026-10-22 afternoon

**Trigger:** `tools/boot_basis_check.py` printed REVIEW REQUIRED on 10 paths at boot (basis last recorded 68044f367, 2026-10-16). `PROME/tools/reads_check.py --agent WALTER`: READS-CAP UNKNOWN (attestation 2026-10-12 predates boot-defining changes). Will: "knock out the backlog now" (12:44 ET).

**Method:** `git diff 68044f367 HEAD` per path, read in full for prose files and at docstring/comment/print level for the two scripts (105 and 273 added lines); commit subjects read. Question asked of each diff: does it add, remove or change a WALTER boot or closeout operation?

| Path | Change since 10/16 | WALTER operation affected? |
|---|---|---|
| AGENTS/WALTER/CLAUDE.md | 7e(f) phone sweep RETIRED 2026-10-21 (WQ-204 DECLINE), tombstone | Yes: one boot read removed. Executed today as retired. READS row 147 (READ phone_scan.py) should be retired to match (packet) |
| CLAUDE.md (root) | Output Canon: "write normal spaced words and numbers"; Git "Before committing / Before pulling" moved to `docs/GIT_WORKTREE_PROCEDURES.md` | Yes: (a) WALTER STATUS DATED MARKET OBSERVATIONS rows are glued text and violate the new rule; fix at the next STATUS rewrite; (b) the git procedure was read at its new home this boot |
| USER.md | No-expiry-nagging (10/20) and trade-ideas-loosened (10/20) operator rulings | No new WALTER step; expiry rule already in WALTER MEMORY Feedback (10/14) |
| PROME/COMPLETION_SPEC.md | Helm retired (WQ-461), Deck paused (WQ-460) in PROME's integration steps | No |
| PROME/ORCHESTRATION_PLAYBOOK.md | L378 lifecycle reconciliation event grammar (PROME's ORCH_LOG writer) | No (WALTER reads ORCH_INFLIGHT only) |
| AGENTS/WALTER/tools/walter_doctor.py | YAML-quoted dispatch timestamps parsed via gen_board_index.scalar_value | No (bug fix) |
| AGENTS/WALTER/design/X_BOOKMARKS_ACCEPTANCE.md | §10 continuation/completion contract (10/19), binding repair accepted (10/20) | Already in the executed 7h procedure (review-template, --mark --review used today) |
| AGENTS/WALTER/tools/x_bookmarks_scan.py | Same continuation and exact-ID stage binding | Same; exercised today |
| scripts/corrections_boot_check.py | R1 resolver: explicit `corrects:` frontmatter first, no filename guessing; malformed explicit pointer fails | Consistent with 9a; SIG-W-20261022-014 uses an explicit `corrects:` header |
| scripts/read_cap_check.py | Owner-directed notice (READ_CAP rule 15, DOCKET L530); advisory, not cap-bearing | No change to WALTER's verdict use |

**Result:** hashes re-recorded in `AGENTS/WALTER/registry/boot_basis_hashes.json`; `boot_basis_check.py` → `BOOT BASIS MATCH: 29 declared paths; execution not certified`.

**Re-attestation (WALTER, reader = declarer):** WALTER's boot manifest for printed steps 0–9b is complete as of 2026-10-22, with one change from the 10/12 attestation: the 7e(f) phone-sweep read is retired (READ row 147). No new boot read was added since 10/12. PROME transcribes (READS rule: WHO MAY ATTEST); packet `PROME/inbox/2026-10-22_from-WALTER_reads-reattestation-basis-review.md`.

**Owed from this review:** STATUS spaced-words fix (next STATUS rewrite, today's closeout).
