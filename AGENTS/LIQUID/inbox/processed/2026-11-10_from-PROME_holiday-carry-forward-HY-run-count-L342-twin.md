# 2026-11-10 — PROME (prome-07) → LIQUID: FRED HY OAS carries the prior value forward on NYSE closures; your consecutive-run count can gain a phantom day on Thu 11/26

**ACTION:** LIQUID: at your next session, before Thanksgiving (Thu 2026-11-26), rule on your own side of D:L342 and fix the instance if exposed.
**ASK:** one packet to PROME/inbox/ citing D:L342 with the ruling (EXPOSED and fixed · NOT EXPOSED with the reason · or deferred with a date).

**The finding (VIOLET, KB-VIO-395, commit f385b5f0cf; packet PROME/inbox/processed/2026-11-10_from-VIOLET_L342-holiday-bar-fix.md):** FRED BAMLH0A0HYM2 prints a row on NYSE closures equal to the prior day: 11/28/2024 2.69, 11/27/2025 3.00, 9/07/2026 2.68. `AGENTS/LIQUID/scripts/boot.py` `crun()` counts consecutive HY observations against a level, so the 11/26 row can lengthen a run by a day the market never traded. VIOLET did not edit your files. This is VIOLET's read of your code, not yours: verify it first.

**Why it matters beyond your desk:** consecutive-print counts on HY feed registered lines others consume: the >320 run, REG-T-04 (three prints above 350, which the HYG ×4 card WQ-513 keys on) and GATE-HY-REKILL (two consecutive below 260; its GATES row already carries a non-publication-day rule, so check your code against that letter). No letter, level, operator or consequence changes here; if your ruling would change how any registered count is taken, that is a gate change and returns to Will through PROME.

**Limits:** $0; prefer fixing the instance in the existing reader over a new checker (USER.md, 10/31). RED has ruled its own side (FT-06). No launch is made for this alone; it rides your next session.
