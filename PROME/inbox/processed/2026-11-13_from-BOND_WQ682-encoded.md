# 2026-11-13 — From BOND to PROME (prome-72): WQ-682 RULED A encoded

**Commit:** `67fc152632` (BOND (orch): encode WQ-682 RULED A, VX-BND-18 red leg is the CFR collateral ratio).
**Ruling verified before edit:** `PROME/WILL_QUEUE.md` RECENTLY DONE (WQ-682, RULED A, Will 11:37 ET "682 A") and `PROME/proposals/2026-11-13_wq682-RULED.md`.

**Encoded cell, `AGENTS/BOND/workbook/VX.tsv` row VX-BND-18, column Threshold_Red, exact text:**
CFR issuer-stated all-borrower collateralization ratio ≤3.0 at a quarter-end OR >$900B system-wide

Replaced: "Advance-depletion narrative OR >$900B system-wide". Yellow leg, score 2 and every other level, operator, instrument and consequence unchanged. Red not met: ratio 3.7 and advances $810.7B, both [6/30/2026]. The four caveats sit in the row's Notes (n=2 of 30 quarters; confirms about six weeks after quarter-end and never warns; blind to one bank's collateral; gross collateral before haircuts). Q3 CFR not re-scored: issuer had not posted at 10:27 ET; the re-score uses the new leg. RULING packet filed to `AGENTS/BOND/inbox/processed/`. No TERRY packet: a score rule, nothing tradeable.

## COMPLETION — BOND — 2026-11-13
STATUS: ✅ DONE
CHANGED: AGENTS/BOND/workbook/VX.tsv, AGENTS/BOND/STATUS.md, AGENTS/BOND/inbox/processed/2026-11-13_from-PROME_WQ682-RULED-A-encode.md, this memo
RESULT: VX-BND-18 Threshold_Red encoded to option A (ratio ≤3.0 OR >$900B) in commit 67fc152632; latest 3.7 [6/30/2026], so nothing fires; score stays 2.
GAPS: Q3 CFR re-score not done — the issuer had not posted the Q3 report (out of this job's scope until it does).
WILL_NEEDS: None.
FOLLOW-UP: BOND re-scores VX-BND-18 on the new leg when the Q3 CFR posts.
