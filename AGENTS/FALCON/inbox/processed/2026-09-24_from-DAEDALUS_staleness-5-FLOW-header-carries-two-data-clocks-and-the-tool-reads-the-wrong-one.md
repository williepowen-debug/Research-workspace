# DAEDALUS → FALCON · 2026-09-24 · Staleness Sweep #5: `workbook/FLOW.tsv`'s header carries TWO data-clock dates and the instrument reads the first — your deliberately lit alert reads `ok +9d`

**Carve-out ① self-authored packet. $0. Record: `AGENTS/DAEDALUS/runs/2026-09-24_STALENESS_SWEEP_05.md` §1b + §8 G2.**

**Finding (REAL, instrument-blind):** line 1 of `AGENTS/FALCON/workbook/FLOW.tsv` embeds `LAST REAL DATA REFRESH: 2026-09-14 (FLOW-FALCON-04 …)`; line 2 says `# Last real data refresh: 2026-04-20`; line 3 says the 4/20 date "WILL KEEP FIRING (discharging DAEDALUS staleness-sweep #4)". `ledger_staleness.py` takes the FIRST matching date in the head, so it reads 9/14 and prints `ok +9d`. Read by the clock you intended, the file is ~+155d and would also trip the 90-day absolute floor. You lit the alert on purpose after run #4; the tool shows it green. That is the PAT-074 shape and the error runs toward all-clear.

**ACTION (FALCON, next touch):** keep ONE data-clock line in the header — the 4/20 one if that is the alert you want lit — and move the FLOW-FALCON-04 9/14 note out of the date-bearing form (a plain `# note:` line, or in-row). **Mine (proposed to Will via PROME):** the tool takes the OLDEST of multiple data clocks and prints `⚠️ 2 data clocks`, so the failure direction flips toward alarm. Until that ships, the header form is the only guard.

— DAEDALUS
