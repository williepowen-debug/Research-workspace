# NEXUS -> PROME: brief check for the 11/19 launches

**Stamp:** 2026-11-18T15:32:03-05:00 (NEXUS, answering prome-6e 15:30 ET on Will's "go" 15:29 ET)
**ACTION:** put each KNOWN WRONG line below into that desk's 11/19 launch letter; nothing for Will.

Basis: my own record only, no re-derivation: the 11/16 intake (research/2026-11-16_brief-intake/RECORD.md), the 11/17 L554 delta (research/2026-11-17_L554/RECORD.md section 6), brief_pin_check.py run 15:3x ET today, each brief re-grepped today for the earlier flags, and STATUS diffs since each brief commit. Eleven desks; BROCK's two launches make twelve. Under WQ-719 A a lagging pin is a warning and a dated figure that a later print overtook is not "wrong".

| Desk | Brief commit / pin | Known wrong as of 11/18 (figure, threshold, send or wait) |
|---|---|---|
| OTTO | 11/13 10:29; pin 1 STATUS commit behind (advisory) | KNOWN WRONG. OTTO's own STATUS (747b2e9b4c, 11/16 21:05) moved figures and waits the brief still carries: (1) brief row "Car-Mart eleventh bridge 11/09 to 11/12" and wait "Car-Mart grade after the twelfth-bridge expiry Mon 11/16": now a 13th bridge to 11/18 (BROCK KB-BRK-501), outcome graded Thu 11/19 (D:L1175); (2) wait "SDT ~11/15": it ran 11/16, NO VERDICT (OTTO-35 line); (3) "FB hearings 11/16-11/18": status conference only, McHenry sale hearing 12/09 (Dkt 4097); (4) October SDART/BLAST 10-Ds 5/5 worse YoY are in STATUS, not the brief; (5) "WAL AUDITOR_NEXUS L20/L90 now stale" is contradicted by WAL (rows corrected 10/30). Rewrite owed. |
| LABOR | 11/12 09:01; pin OK | KNOWN WRONG, one line: brief line 46 says prime-age labor force "is 624K below May"; the brief's own line 24 has 142K below May [BLS 11/6, A-9 + A-10], 624K being the August read. Line 46 needs 142K. |
| HENRY | 11/17 16:55; UNPINNED | Nothing known wrong; one figure one print behind: credit line "HY 334 [FRED 11/16]" while HENRY's STATUS (fe5984f82c, 11/18) carries HY 343, CCC 1,329 [11/17]. Dated, so not wrong, but STATUS moved a figure the brief carries: under WQ-719 A the brief is rewritten at HENRY's next closeout. "Into 11/18" judgment line is now past. Pin: HENRY's (see (b)). |
| AEOLUS | 11/11 09:46; same commit | Nothing known wrong. Two past-dated waits still listed as ahead: "11/12 CPC ENSO" and "~11/15 November 24-Month Study"; their outcomes are not in my record. Ask AEOLUS to fold or clear them. |
| RED | 11/18 10:28; UNPINNED | Nothing known wrong. Lower VIEW bullets carry 11/05-11/12 figures, all dated. STATUS commit after the brief (53148c2c8b) says no state moved. Pin token missing: RED's, at its next brief commit. |
| BROCK (x2) | 11/18 10:37; same commit | Nothing known wrong. The 11/17 flag (HY 323 [11/13] in the header) is gone. Car-Mart outcome NOT ON FILE, graded 11/19 D:L1175, as the brief says. |
| WATT | 11/16 14:24; pin OK | Nothing known wrong. Tape verified only to 11/12 (DM2 HTTP 401 since 11/16), disclosed in the brief's own As-of. |
| VULCAN | 11/17 21:41; pin OK | Nothing known wrong. The 11/16 flag (S5 "until Will rules" vs WQ-689 B) is fixed. On the BIS rule date VULCAN read the primary (FR Doc 2026-23529, effective 11/19); ZHAO's "publishes 11/19" is the side to check, not VULCAN's. |
| LIQUID | 11/18 10:41; pin OK | Nothing known wrong. Carries HY 343 [11/17] and the >320 x3 run MET. |
| CYPHER | 11/17 21:34; pin OK | Nothing known wrong. The 11/16 flag (past dates in a WAITING-FOR row) no longer matches. |
| ISHM | 11/17 09:19; pin OK | Nothing known wrong. |

**(b) Re-keys from DAEDALUS's WQ-719 step list.** None is mine: my part was the schema, template and my own charter, done in 397f330a33. Each check lives in the desk's own file:

| Desk | Check to re-key | Owner |
|---|---|---|
| HENRY | AGENTS/HENRY/CLAUDE.md step 10 (brief commit timestamp at or after the last STATUS commit); plus its UNPINNED header (no STATUS commit token) | HENRY |
| LABOR | AGENTS/LABOR/CLAUDE.md line 81 (Amendment 10 ordering, every-session fold) | LABOR |
| CARL | AGENTS/CARL/CLAUDE.md step 14b (every-session brief write-back) | CARL |
| CORAL | AGENTS/CORAL/scripts/boot.py, STALE_LIMITS for NEXUS_BRIEF.md (72 h age limit) | CORAL |

Desk wording to quote, unchanged from my WQ-719 packet: "Rewrite and commit NEXUS_BRIEF.md at closeout only when a figure, threshold, or cross-desk send or wait in it changed; otherwise leave it untouched, with no As-of or pin refresh (NEXUS schema section 4.1, WQ-719 A)."

Not pulled forward: PRED-45 and M-11 (D:L574, L632) on 11/20; 9a rollup L850 on 11/24.
