# HAWK whole-profile refresh — 2026-10-22

**Status:** whole-profile comprehension COMPLETE to the declared reader coverage. Second of the nine accepted cohort refreshes (AEOLUS 10/21), run early on Will's word 17:41 ET ("Can we do this now actually").
**Runtime:** Claude Code, Opus 5.5, session daedalus-e7. Three Mode-A readers, Opus, read-only, launched 17:41 ET, all delivered by 17:50 ET.
**Readers:** A architecture/state · B thesis/domain/research · C ledgers/scripts/guards. Raw reports are verbatim in `runs/2026-10-22_HAWK_REFRESH_READERS/`, with coverage and not-read lists in each §7/§6. HAWK's tree was clean before and after every reader; C proved this with `git status` at 17:42 and 17:47.
**Prior profile:** verbatim at `profiles/_prior/HAWK_2026-10-22_before_refresh.md` (sha256 prefix 5470b5e5f1db3980, matching the pre-refresh `profiles/HAWK.md`).

## Lead verification (every 🔴/🟠 rechecked at the artifact)

| Claim | Result |
|---|---|
| N6 October observation done 10/21 (A1, B F15) | ✅ KB-HAWK-448 present |
| MARCO S338 correction unprocessed; STATUS still says "autos stack on 232" (A2) | ✅ packet in inbox top level; the line is STATUS:**11**, not :22 (reader line error) |
| K2 names HAW-19 LEG A, "NOT YET REGISTERED" (B F1) | ✅ FALSIFICATION:31 |
| HAW-20 "in spirit" softening (B F3) | ✅ KB-HAWK-451; ❌ not at FALSIFICATION:15 as cited (reader citation error) |
| 21 CATALYSTS rows PENDING with past dates (C1) | ✅ awk count 21 |
| war_monitor `int("5-10")` dead branch (C3) | ✅ code at war_monitor.py:188/219/227 |

## Outputs
- `profiles/HAWK.md` rewritten (vintage 2026-10-22).
- Owner packet `AGENTS/HAWK/inbox/2026-10-22_from-DAEDALUS_profile-refresh-findings.md`, ranked 1–9, opening with the reader errors (UPGRADE_PROTOCOL Step 0 rule).
- FLEET_MAP HAWK row re-cut, L4/H retained; prior cells in FLEET_MAP_HISTORY.tsv.

## Fleet-tool finding routed to DAEDALUS's own duty
`scripts/claim_check.py` counts an unsupported-suffix path as a clean file (`✓ 1 file(s) clean` over zero bytes read; reader C repro via `/dev/fd/63`). This is the PAT-074 class on the suffix branch. Owed and not fixed this session.

## Not done
- No market-value validation.
- Raw domain sources not read.
- No independent final reader on the new profile; the AEOLUS refresh had one. DAEDALUS rates its own synthesis as unreviewed (`finding_a_correction_pass_is_unreviewed_work`).
- Queue clock: 2 of 9 complete; the profile-refresh queue `last_run` does not advance until the whole queue is done.
