## 2026-11-13 — BRENT to PROME (prome-72): part one, card SIG-W-20261112-009 graded; inbox drained

**Answer to WALTER's ask (card SIG-W-20261112-009):** no registered row moves; the bypass-risk read gains weight, not state.

| Item | Read |
|---|---|
| Settle, not vendor last | CME 403 here since 10/28, so a vendor proxy that agrees to the cent: BZF27 (Jan Brent) 1-minute VWAP [14:28,14:30) ET 95.8278, daily close 95.82, against 92.76 on 11/11: **+3.30%** (the card's 96.04 / +3.5% is the 16:15 ET last). M1−M3 +3.8713 → +4.2394 (steeper). Brent−WTI Jan-Jan +0.80 wider. 11/13 ~12:40 ET: 95.80, flat [vendor, advisory]. |
| What the shape says | Front-led and Brent over WTI is the shape of a supply-risk premium; a pure macro day would not lift Brent over WTI. Consistent with the claim being priced; attribution still NOT ESTABLISHED (no barrels reported lost, other news that day). |
| BRT-32 Yanbu loading halt | Letter not met: no Aramco, ministry or SPA loading statement, no Reuters/Bloomberg halt report (secondary search 11/13 midday found none). OPEN 20% unchanged. |
| BRT-33 / BG-02 / gates / TRACKER / INCIDENTS | No move. BRT-33's 11/12 window +4.2394 is further from +3.50. No INCIDENTS row on a claim (LESSONS #1). |
| combo:yanbu-bypass | Member logged in `docket/CATALYSTS.tsv`: fourth claim or hit on the bypass in five days, and the settle priced it. Review 11/19 unchanged. State moves only on a qualifying halt report or a Saudi statement that the line or a station is out. |
| TERRY | No packet: nothing confirmed, nothing registered moved. If FALCON confirms damage to the line or a station, that goes to TERRY the same session. |

**Inbox drain:** SIG-W-20261112-009 (acted) and SIG-W-20261113-004 (noted; item 2, the unverified Volgograd refinery fire photo, logged on combo:diesel-buffer because the tag WALTER used, russia-refinery-strikes, has no BRENT row). 2 board_log rows = 2 `git mv` to `inbox/WALTER/processed/`. ⚠️ **The "one direct packet" in your brief was not found:** top-level `AGENTS/BRENT/inbox/` is empty in the working tree, on origin/master (fetched 12:40 EST) and in git history since 11/12 15:00; no `MSG-*` file. If it exists elsewhere, name the path.

**Boot (rc 2, 3 findings, none new):** TANKER-LIVENESS instrument dead (chronic); 4 ledgers past budget (COT_VINTAGES refreshes at #14 today); 2 elapsed-expiry rows in FORGE D-98 are Will/PROME rows, not BRENT's.

Record: `AGENTS/BRENT/research/2026-11-13_yanbu-claim/NOTE.md`, STATUS November 13 block.

## COMPLETION — BRENT — 2026-11-13 (part one)
STATUS: ⚠️ PARTIAL (part one done; part two, G:GATE-BRENT-COT-35B #14, after the 15:30 ET COT release)
CHANGED: AGENTS/BRENT/research/2026-11-13_yanbu-claim/{NOTE.md,daily_bars.txt}, AGENTS/BRENT/docket/CATALYSTS.tsv, AGENTS/BRENT/board_log.tsv, AGENTS/BRENT/STATUS.md, 2 cards moved to inbox/WALTER/processed/
RESULT: Card SIG-W-20261112-009 graded on the settle basis: Brent +3.30% to 95.82, M1−M3 +0.37 steeper; 0 registered rows moved (BRT-32 20% unchanged); 2 cards consumed, 2 combo members logged.
GAPS: No official settlement (CME 403, no evasion); vendor proxy used. The brief's direct packet was not found.
WILL_NEEDS: None.
FOLLOW-UP: Part two after 15:30 ET; FALCON's claim grade may change the BRT-32 or INCIDENTS read.
