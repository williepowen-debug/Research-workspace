# 2026-11-13 — From BOND to PROME (prome-72): D:L226 VX-BND-18 escalation-leg retune — DRAFT for Will, not encoded

**Rows:** D:L226 (`PROME/DOCKET.tsv` physical line 226) · wake basis WQ-184, WQ-667 B · BOND `workbook/VX.tsv` VX-BND-18 · KB-BND-575, 576, 577.
**Runtime:** Claude Code, `claude-opus-5-5`, desktop. Root CLAUDE.md, AGENTS.md, USER.md, COMPLETION_SPEC and BOND CLAUDE.md read explicitly (no BOND AGENTS.md). Inbox empty at boot, every lane. `git pull` not run: the tree was dirty with PROME's `SCRATCH.md` / `WILL_QUEUE.md` (refusal is the rule); `git fetch` showed origin had nothing new.

## Answer

**The leg as written stays ungradeable, and the instrument BOND named on 8/23 does not exist.** The FHLB Combined Financial Report (CFR) publishes no system-wide unused borrowing capacity (full-text check of the 6/30/2026 report). It does publish, every quarter, an issuer-stated **collateralization ratio for all borrowers** (eligible collateral ÷ advances plus other credit). Over 30 quarters (2019Q1–2026Q2) its two lowest values are the two stress quarters: **2.8 at 3/31/2023 and 3.0 at 3/31/2020**; every other quarter is 3.2 or higher; **latest 3.7 at 6/30/2026**.

**Draft for Will (it creates a level, so it is a gate change; nothing encoded):**

| Option | Red leg of VX-BND-18 | BOND |
|---|---|---|
| **A** | "CFR issuer-stated all-borrower collateralization ratio ≤3.0 at a quarter-end OR >$900B system-wide" | **Recommended**: swaps an ungradeable clause for a gradeable one, so the rule count does not grow; caught 3/31/2020, which the $900B line missed (advances $797B) |
| B | Strike "advance-depletion narrative"; >$900B alone | Fewest rules |
| C | Leave as is | Not recommended: ungradeable since 8/23 |

⚠️ **Caveats that must reach Will with it:** (1) n=2: two stress quarters in 30 is a base rate, not a validation. (2) It confirms, never warns: a quarter-end snapshot published about six weeks later, so it scores the vector but cannot position anyone ahead. (3) It cannot see one bank running out of collateral (the CFR says borrowers are not cross-collateralized), which was the SVB mechanism. (4) Gross collateral before haircuts, not borrowing room.

**Corrections to BOND's own 8/23 return:** the candidate instrument was named without checking the source publishes it; and the deferral premise (the retune needed the Q3 CFR for a base rate) was wrong, since 30 back quarters were available. The 82-day wait bought nothing.

**Q3 CFR (catalyst for today):** not posted at 10:18 or 10:27 ET (index lists through 2026Q2; Q3 PDF path returns 403). The VX-BND-18 Q3 re-score and REGINALD's REG-T-06 leg 3 still wait on it. Not verified at the issuer when it will post.

**SAM's funding-line correction (with LIQUID):** baselines logged (KB-BND-576): foreign official custody Treasuries $2,524.189B [11/11], −$48.658B over three weeks (3.7th percentile since 2015, but 12 falls as large or larger since 2023); foreign official repo pool $336.357B. A securities-funded intervention would show in custody, a deposit-funded one in the repo pool; neither names Japan. Split proposed to LIQUID by packet; first read 11/19. Logged, not scored.

**TERRY:** no packet. Nothing here is tradeable: a draft quarterly gate sitting at 3.7 against 3.0, and an unidentified custody baseline. Stated so the skip is visible.

## COMPLETION — BOND — 2026-11-13
STATUS: ✅ DONE (draft returned; the Q3 re-score stays open because the issuer has not posted)
CHANGED: AGENTS/BOND/analysis/2026-11-13_L226-fhlb-retune/ (READ.md, table18.py, extract.py, two data files), workbook/KB.tsv (575–577), workbook/VX.tsv (VX-BND-18 notes only), docket/CATALYSTS.tsv, STATUS.md, SCRATCH.md, thesis/THESIS.md + monitors/DEALER_CAPACITY.md (FR2004 vintage drift, boot_recompute rc 1→0); AGENTS/LIQUID/inbox/2026-11-13_from-BOND_japan-intervention-funding-split.md
RESULT: L226 answered: the narrative leg stays ungradeable; the 8/23 instrument is not published; a 30-quarter base rate gives draft option A (ratio ≤3.0, 2 of 30 quarters, latest 3.7). No score, band or threshold moved. HY 320 [11/12].
GAPS: Q3 CFR not posted at 10:27 ET, so no Q3 re-score. VX-BND-20 11/11 review still unserviced (out of this task).
WILL_NEEDS: Rule on the VX-BND-18 red leg: A (recommended), B or C — a threshold change, his alone.
FOLLOW-UP: BOND re-scores VX-BND-18 when the Q3 CFR posts; LIQUID reply on the H.4.1 split; 11/19 H.4.1 read.
