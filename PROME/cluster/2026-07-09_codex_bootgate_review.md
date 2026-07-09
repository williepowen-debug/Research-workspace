# Codex cross-vendor adversarial review — boot-gate scripts (2026-07-09)

**Reviewer:** OpenAI Codex via the `codex@openai-codex` plugin (first live run of the cross-vendor lane, Will-directed shakedown).
**Scope:** `scripts/session_banner.sh` + `scripts/firetime_check.py`, read-only.
**PROME verification:** every H/M finding verified against the live code before endorsement; line numbers were accurate throughout. M2's CRLF scenario was overstated (`\r` doesn't split TSV fields) — the only quibble found.
**Disposition:** H1/H2/M1 FIXED + verified (`e1435b67`, Will-approved). M2 + L1–L5 LOGGED, deliberately not fixed (low yield vs. added regex complexity on a boot gate). If one of the open findings bites, this file is the pointer.

## Fixed (commit `e1435b67`)

- **H1 — session_banner.sh: silent "0/0 clean" on unresolvable `origin/master`.** The `"?"` ahead/behind sentinel had no output path and the all-clear line hardcoded "0/0". Fix: explicit `[SYNC STATE UNVERIFIED]` flag + interpolated counts. Verified both paths.
- **H2 — firetime_check.py: year-boundary silent miss on bare date tokens.** `Jul-16`/`7/9`-style tokens parsed with `default_year = today.year`; a December run reading "Jan 5" landed it in the past → dropped by the provenance filter → never drift-checked (and inverse: early-Jan false-flag on prior-Dec stamps). Fix: ±183-day year-roll for bare kinds only. Verified by Dec/Jan simulation, both directions.
- **M1 — firetime_check.py: false DEAD POINTER on head-of-list agent names / acronym prose.** `(?<!/)` guard only blocked mid-list tokens; `PROME/LIQUID/WALTER` and `skills/MCP` (prose) false-flagged — this was the root cause of the standing "cosmetic" SCRATCH flag tolerated since ~7/6. Fix: skip extension-less tokens whose tail segments are all CAPS/digits. Verified: 7→6 flags, all real pointers kept.

## Open — logged, not fixed (severity LOW / LOW-MED)

- **M2 (partial) — firetime `load_docket()` silently drops malformed rows** (<4 tab fields, or a date cell failing the strict `YYYY-MM-DD[..]` regex). A corrupt/renamed docket row silently un-gates its artifacts; the "fail-loud" docstring only covers a *missing* file. Watch-for: a docket edit that breaks a row's tab structure will vanish from `--window` checks without complaint. (Codex's CRLF vector overstated; the silent-drop mechanism itself is real.)
- **L1 — `DEAD_OK_RE` skips the whole line:** a line declaring one path dead suppresses pointer-checking for every other path on that line, including a genuinely-dead third pointer.
- **L2 — `ANNOTATION_RE` over-broad:** common live-prose words (`updated`, `refreshed`, `was `) before a date suppress a real future-date drift flag.
- **L3 — extension-less bare path that exists only as `.md` false-flags** (e.g. `memory/2026-07-08` vs the real `…-07-08.md`). *(Partially mitigated by the M1 fix — all-digit tails now skip.)*
- **L4 — banner `env_doctor FAIL` conflates "python3/script broken" with "env unhealthy";** hardcoded `origin`/`master` + coreutils `timeout` are the machine-portability assumptions.
- **L5 — banner DIRTY count silently 0 if `git status` itself errors** (corrupt repo) → reports clean. Same silent-pass class as H1, much lower probability.

## Lane verdict

Cross-vendor review earns its slot for silent-failure hunting on harness code: it found two latent H-severity bugs and the root cause of normalized noise, on its first run, with accurate line references. Guardrails held: review-only, findings verified before endorsement, fixes applied by PROME under pathspec discipline. Next natural use: red-team of high-stakes decision-rail logic (fire-cards, gate definitions) before arm decisions.
