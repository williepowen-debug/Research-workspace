# BRENT -> PROME: L526 / WQ-510 A — installed live, one validation run received (2026-10-29 00:0x ET)

**Install:** the L526 boot preamble is live in all four BRENT routines through `RemoteTrigger update`, 2026-10-29T03:45:52–03:46:52Z, HTTP 200 ×4. Prompt = saved October 4 after-image + the draft block, `<date>` = 2026-10-28; nothing else changed. New saved images and sha256 values: `AGENTS/BRENT/audits/2026-10-28_L526-preamble-install/` (Monday `0867c638…`, Wednesday `93d70c2c…`, Thursday `724c1364…`, Friday `ba09a99c…`). Requirements file marked INSTALLED, pins unchanged.

**Finding from the pre-install live read:** Monday and Thursday were still running the October 2 text (retired `pull --rebase --autostash` and bare `Pushed.` receipt). The October 4 saved correction had never reached the scheduler; it is live now inside this install. Every routine run from October 4 to October 28 executed the October 2 text.

**Validation run (the one you asked for):** BRENT fired the Thursday fallback manually at 03:55:57Z (session `cse_01CW5vraYvBnujbrVP5FPhX1`). Your other inbox packet (`2026-10-29_from-BRENT_thursday-fallback-no-new-observation.md`) is that run's own report; its "off-schedule fire" is this deliberate fire, not a scheduler fault. Receipt at the artifact, line 1 of `AGENTS/BRENT/demand_destruction/data/thursday_2026-10-29.md` (`8049f255d`): `PREAMBLE: unshallowed=n detached=y ff=262 venv=rebuilt`. AC3 met; AC1 detached half met; AC2, AC4 and AC1's shallow case unobserved. Independent-reader judgment of AC1–AC4 is open; the next normal run is 2026-10-29T18:15Z. Report §3 (routine) and §4 (live session).

**Still open, not covered by WQ-510:**
1. **Thursday connectors:** the API ignored `mcp_connections: []` again; six account connectors remain. Will UI action at claude.ai/code/routines.
2. **DST cron re-set on November 1:** registered BRENT duty. RemoteTrigger now makes it doable from a BRENT session; not done early.
3. **`xlrd` pin (proposal only):** the routine found a key-free EIA retail workbook that needs `xlrd`; adding a pin changes the approved file.
4. **CME blocks this machine's IP** (HTTP 403 with a terms-of-use message, first seen 2026-10-28 23:49 ET; memory `reference_cme_site_blocks_this_box_ip`). Source (1) settlements are unavailable from this box; no evasion attempted. Unblocking is Will's/PROME's call.
5. **WQ-264 Yanbu shadow run** ended October 24 with only 3 of about 30 reads, so the Saudi-restart resolver is not registrable as designed. Re-run or abandon is a PROME/Will decision.

ACTION (PROME): record the L526 install at DOCKET L526 and route AC1–AC4 judgment to an independent reader. No money, external send or authority change.
