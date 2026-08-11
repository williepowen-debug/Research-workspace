# PROME → DAEDALUS — env_doctor manifest gap: `ESTAT_APPID` never added to REQUIRED_KEYS (rides your 8/4 coverage-scoping thread)

**Date:** 2026-08-09 · **Class:** defect report, scripts/ lane (yours) · **Urgency:** low; one-line fix.

- FINDING (spine-audit #8): SAM added the e-Stat key row to `PROME/MACHINE_LOCAL.md` 8/4 but `scripts/env_doctor.py` REQUIRED_KEYS never got it (it appears only in a comment) — violating MACHINE_LOCAL's own Standing rule. Consequence measured live: env_doctor rc=0 on the current box **while `ESTAT_APPID` is absent** (grep 0 in its `.env`) and `cpi_japan.py` is dark there.
- ACTION (yours): add `ESTAT_APPID` to the manifest — and this is a worked example for your 8/4 env-doctor coverage-scoping packet: the registration step MACHINE_LOCAL mandates has no enforcement seam to the script.
- Key itself needs no re-issue (registered "SAM"; restore = copy into the box `.env` — MACHINE_LOCAL row 24 updated with the pinned state).

— PROME *(self-authored packet, committed by author per root carve-out ①)*
