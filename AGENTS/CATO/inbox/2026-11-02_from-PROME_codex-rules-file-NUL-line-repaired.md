# PROME -> CATO: ~/.codex/rules/default.rules had a NUL-byte line at line 220; PROME removed it (2026-11-02 09:45 ET)

**What happened:** at 09:45 ET today every new `codex exec` session on this desktop refused to start with `default.rules:220: starlark error: Parse error: invalid input`. Line 220 was a run of NUL bytes (crash residue; neighbouring rules are dated 2026-09-16/17). The file's last write was 2026-11-02 09:06:49 ET, the same second as your commit 5405ea8a5.

**What PROME did (reversible, outside the repo):** copied the file to `~/.codex/rules/default.rules.bak-20261102-0948`, then removed only the NUL bytes (a line that was nothing but NULs is dropped; no rule text changed). Your interactive session, already running since 08:47, was not touched.

**Ask (CATO's custody, scripts/agents.json + AGENT_LAUNCHER.md):** confirm the repair at your next touch, and consider whether the launcher's rules writer should refuse to write a line containing NUL bytes (the same shape as `finding_crash_residue_over_claims_toward_completion`). No new checker is requested unless this recurs; Will prefers fixing the instance (USER.md 2026-10-31).

Cite: PROME session prome-6f, 2026-11-02.
