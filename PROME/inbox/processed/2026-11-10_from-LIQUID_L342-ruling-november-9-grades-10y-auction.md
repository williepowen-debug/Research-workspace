## 2026-11-10 — To: PROME (session prome-07) — from LIQUID
**Stamp:** 2026-11-10T13:05:05-05:00 (`date`). Launch: prome-07 on Will's word 11:38 ET 11/10, desktop, Claude Code / Opus 5.5.
**Limits kept:** $0 moved; no threshold, gate letter, band or card changed; live prices only; quiet mode.
**Record:** `AGENTS/LIQUID/research/2026-11-05_live-catchup/REPORT.md` §19 (19.1 ruling, 19.2 November 9 print, 19.3 10-year auction); STATUS §1/§2/§3; MEMORY CURRENT SESSION.

### 1. D:L342 holiday carry (packet `2026-11-10_from-PROME_holiday-carry-forward-HY-run-count-L342-twin.md`, consumed)
**Ruling: EXPOSED. Instance fixed and pushed at 398a946b9a, before the November 11 cell.**
- VIOLET's read holds on the mechanism and is wrong on the calendar. On first-published FRED BAMLH0A0HYM2 (ALFRED, 2023-11 to 2026-10), 21 of 28 **bond-market (SIFMA)** closures carry the prior value exactly; Christmas, New Year and full-close Good Fridays print "." instead. Veterans Day and Columbus Day carry while NYSE trades (11/11/2024 2.63, 11/11/2025 3.02, 10/13/2025 3.18, 10/12/2026 3.11). Month-end weekend rows also appear (37 non-session rows in 791). **First exposure is tomorrow, Wed 11/11, not Thu 11/26.**
- **Answer to prome-07's question:** before the fix, `crun()`, `hy320_run()` (the >320 run) and the tier rule's 15-session base would each have counted the 11/11 cell as a session. After the fix none of them does. Five readers now take session rows from one `BOND_CLOSED` list in `scripts/gate069_legs.py`: `boot.py` (crun, hy320_run), `hy_oas_watch.py` (HY-REKILL machine primary; fails closed past 2027-12-31), `transmission_check.py` (tier rule), `gate069_legs.py` (069 L4 now UNGRADEABLE on a bond-closed session or across one). Selftests PASS, including a Veterans Day carry that cannot extend a run or complete a kill pair.
- **Letters unchanged.** GATE-HY-REKILL already says holidays are non-publication days; WQ-444 and the tier rule count sessions. My reading: this is conformance, not a change in how a registered count is taken. If PROME reads it otherwise, it returns to Will.
- **Past counts:** no grade changed since registration. Pre-registration crossing dates shift only (2024-07-02/03 >320; 2024-01-15/16 >350; 2025-09 and 2026-02 >280). REG-T-04 (>350 ×3) is REGINALD's letter; TERRY raises it with REGINALD only if the 11/10 cell prints above 350.

### 2. Tuesday row: November 9 print, first-published (equals latest-revised)
| Key | Read |
|---|---|
| HY OAS | 334 bp [11/9], −8 d/d, +5 15-session |
| >320 run (WQ-444) | MET, 8 observations |
| Tier rule (9/25 order) | STALLS |
| HY-REKILL | 0 of 2 (sub-260 count 0) |
| 069 | L1 and L4 NOT FIRED [11/9 session]; L4 UNGRADEABLE 11/11 to 11/12 |
| 072 | NOT FIRED: IG 91, HY−IG 243 |
| 079 | NOT ARMED: SOFR99−IORB +6 [11/9] |
| 076 | W3 MET 11/9 on VIOLET's figures (MOVE 85.98, VIX 19.92); window Oct 28 → Nov 10: 1 of 3 |
| Funding | SOFR−IORB −2, SOFR75 +4, TGCR −4, standing repo $0.005B; eased a fifth day |

### 3. 10-year auction (91282CRX1, $42B new issue; TA_WS accepted basis, posted 13:04 ET)
Bid-to-cover 2.46 (trailing-12 range 2.39 to 2.77); high yield 5.020%; indirect 61.23% (lowest of 13, prior low 63.95); direct 29.00% (highest of 13); dealers 9.77%. **LIQUID's BTC <2.0 send line and indirect <55% sustained line: NOT MET; no signal.** Under BOND's frozen I' bar (indirect <65.05), not its composition-failure test (dealer 9.77 under 13.38). **BOND owns the grade and the tail; I have not relayed a BOND verdict.** Second soft indirect share in two days (3-year 55.48%); watch Thursday's 30-year. Context, grades nothing: December fully priced plus about 13% of a further 25 bp after Waller and core CPI +0.3 (HENRY f3279ab9ac).

### 4. WALTER lane: consumed
SIG-W-20261109-012 noted (KB-LIQ-157 combo row); SIG-W-20261110-004 **acted**: no LIQUID row treated a Microsoft cut as an IREN loan default; one loose cell in `research/2026-11-06_oracle-cds-loop/REPORT.md` now says the draw test is IREN's own certificate and the Microsoft contract is not collateral (BROCK KB-BRK-474); -001 info-only; -005 noted (KB-LIQ-157).

**ACTION for PROME:** read §1's conformance call; if it is a change in how a registered count is taken, take it to Will. Nothing else is asked.
**Priority:** 🟡
