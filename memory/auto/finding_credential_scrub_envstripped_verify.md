---
name: finding_credential_scrub_envstripped_verify
description: Scrubbing a hardcoded credential needs (1) a comprehensive grep for ALL copies and (2) verification with the credential source STRIPPED — soft-fail scripts report success while their data goes silently blank
metadata: 
  node_type: memory
  type: finding
  originSessionId: 1024a372-529b-4a79-a25a-8fceaa7c7976
---

2026-07-01: scrubbing "the" hardcoded FRED API key from `fetch.py` (public-prep). Two traps, both hit and caught:

1. **The literal lived in 10 files, not 1** — fetch.py, a FORGE timing script, 4 CARL scripts, BRENT, BOND, DEWEY, and a tracked daily-memory note. A single-file scrub would have shipped 9 live copies to the public repo. ([[finding_comprehensive_grep_over_sampling]] applied to credentials.)

2. **"Still works" was a lie until tested with the key source stripped.** After removing the fallbacks, the agent scripts *kept reporting success*: BRENT's monitor printed "All scripts completed successfully" with its FRED rows silently missing; CARL's gas tracker appended a row with an empty FRED column (its `except` returns `[{"error"}]` and the caller blanks the field). rc=0 + a success banner proved nothing — the scripts soft-fail by design. Only running with `env -u FRED_API_KEY` (and inspecting the actual data fields) exposed it.

**Why:** data-pipeline scripts commonly wrap fetches in try/except and degrade to blanks so one dead source doesn't kill the run — which means credential removal doesn't *break* them, it silently *hollows* them. The failure you're testing for is missing data, not a nonzero exit.

**How to apply:** before calling a credential scrub done: (a) grep the literal repo-wide (code + docs + memory notes) — fix every copy; (b) re-run the consumers with the credential source explicitly stripped (`env -u KEY`) and verify the *data fields*, not the exit code; (c) give each consumer a loud warn when the key is unresolvable (fail-loud beats blank columns, [[finding_fail_loud_on_incomplete_data]]); (d) remember HEAD-scrubbing doesn't touch git HISTORY — rotate the credential if the repo is public-bound ([[finding_history_scrub_verify_by_content_not_pickaxe]]). Bonus trap: a `~/.bashrc` export placed BELOW the interactive guard is invisible to non-interactive shells — the harness's Bash tool never sees it.
