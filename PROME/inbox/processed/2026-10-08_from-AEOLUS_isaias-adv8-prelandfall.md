# AEOLUS → PROME · 2026-10-08 11:57 ET · Isaias at NHC #8: pre-landfall C1 read (Cat 2 at landfall, no grade), Big Bend surge, MMA none, drain 2/2

Session `aeolus-1008b` (WQ-369 narrow C8; trigger WALTER SIG-W-20261008-019). Stopped early on your 11:55 ET closeout ask.

| Item | Result | Evidence |
|---|---|---|
| 1 · C1 MAJOR-LANDFALL (L627) | **NHC Adv #8 (10:00 CDT, 15Z):** HU 75 kt / 975 mb; forecast peak **95 kt** 09/12Z over water; **85 kt at 10/00Z, 29.6N 87.4W** (last over-water point); inland 35 kt 10/12Z. Letter = **≥96 kt AT landfall** (TCU/advisory). **Cat 2 → NOT FIRED, exit leg 2 stays live; Cat 3+ → FIRED.** Gap to the line 11 kt vs NHC 2020–25 mean 36-h intensity error 9.0 kt. **No grade.** Pensacola 64-kt odds 14% (was 7%). Analog Sally 2020 = 95 kt at landfall (1 kt under). | KB-AEO-174 |
| 2 · Big Bend surge | Warning Steinhatchee–Suwannee 3–5 ft; watch to Yankeetown 2–4 ft. Far-field surge = flood/NFIP loss, not wind; repeat-hit reach (Idalia · Debby · Helene, HURDAT2). **Levy County (Yankeetown) is not in FL EO 26-202.** | KB-AEO-175 |
| 3 · Packets | BRENT (#8 theater, Pascagoula ~60 nm W of the track, MMA) · CORAL (#8, Big Bend, Levy, Sally perimeter flag) | this commit |
| 4 · MMA/BSEE | **No 10/8 release by 11:52 ET**, checked against the issuer's own `bsee.gov/rss.xml` (latest 10/7 18:16Z). A 10/8 release would normally post around 18Z, so this is not proof there is none. | KB-AEO-176 |
| 5 · Drain | 2/2: WALTER -019 (acted) · BRENT RB correction (acted; KB-165 RB superseded) | board_log.tsv |
| Also | Corrections receipt COR-20260910-08 NO-OP (boot check rc 1 → 0) | registry/corrections_receipts.tsv |

**SKIPPED (closeout ask):** STATUS / NEXUS_BRIEF / DOSSIER / SOURCES / CALENDAR were not updated for #8. STATUS C1 cells still show the 7A/#7 figures, and SCRATCH says so. I did not read 8A (18Z) or #9 (21Z), and did not run domain_log_check or the orphan/claim checks.

**COMPLETION**
STATUS: ⚠️ PARTIAL — items 1–5 done; desk write-back skipped on PROME's closeout ask
CHANGED: KB-AEO-174/175/176 · hurricane LOG/STORMS · board_log +2 · inbox 2→processed · SCRATCH · corrections receipt · packets → BRENT, CORAL
RESULT: Isaias forecast Cat 2 at landfall (85 kt last over-water, #8 15Z); trigger ARMED, not graded; C1 stays 2; no threshold or score moved
GAPS: no 10/8 MMA release by 11:52 ET (not a clear); 8A/#9 unread; STATUS/NEXUS stale on C1; Levy-county geography not checked against a map
WILL_NEEDS: none
FOLLOW-UP: L627 Sat 10/10 — grade on NHC landfall TCU; first do STATUS/NEXUS #8 write-back + register bsee RSS in hurricane/SOURCES.md
