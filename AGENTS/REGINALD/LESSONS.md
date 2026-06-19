# LESSONS.md — REGINALD Mistake Patterns & Rules

*Read at boot. Learn once, prevent forever. This file is for verified mistakes that burned us — each with a prevention rule. For Will's working preferences and data source learnings, see `MEMORY.md` (Feedback + Findings sections).*

---

### [Data] — Verify Agent Data Against Primary Filings
**Mistake:** PSEC was reported at 35% PIK — actual was 8.6% per SEC filing. Consumer finance names (SYF, BFH, ALLY) were assumed stressed but SEC filings showed improvement.
**Rule:** Before any metric informs a trade, verify against the 10-K/10-Q. Agent research is a starting point, not ground truth.

### [Data] — NDFI Is Not What It Looks Like
**Mistake:** WAL's NDFI ($6.5B) was initially flagged as major risk. Reality: 68% is mortgage warehouse (0.08% reserves, near-zero losses), NO auto warehouse. Ex-mortgage only $4.3B in secured SPV structures.
**Rule:** Decompose NDFI by type before assessing risk. Mortgage warehouse ≠ auto subprime ≠ BDC lending.

### [Analysis] — Hidden CRE Methodology
**How to screen:** Pull FFIEC Call Report Schedule RC-C Part I. Item 4 = C&I loans. Memo Item 3 (RCON2746) = "Loans to finance CRE not secured by RE." Ratio = Memo3/Item4. Flag if >20%.
**Key finding:** WAL ratio is GROWING (15.5% → 24.2%), only bank with upward trend. OZK worst at 37.6%.

### [Analysis] — Distinguish Classification Levels
Three levels of CRE masking:
1. Extend-and-pretend (don't force refinancing)
2. Mark-to-model (don't write down)
3. Classification (call CRE "C&I" if unsecured) ← Memo Item 3
All three can coexist at the same bank. WAL uses all three.

### [Process] — Date Your Data
**Rule:** Every metric must have a date. "Office DQ is 12.34%" means nothing without "as of Jan 2026." Stale data in STATUS.md causes wrong analysis.

### [Process] — STATUS.md Is Not a Research Report
**Rule:** STATUS.md is a dashboard — current state, thresholds, positions. Research detail belongs in archive/, workbook/, or source files. If STATUS.md exceeds 10KB, it needs pruning.

### [Data] — Verify Real-Time Prices Before Building Narratives
**Mistake:** STATUS.md stated Brent $118-125 and built an entire FL energy shock cascade on that figure. Actual was $81.40. The error propagated through multiple sections before being caught.
**Rule:** Always confirm price levels from a live source before modeling downstream effects. A 45% error on an input produces garbage on all outputs.

### [Data] — Cross-Agent Signal Values May Conflict
**Mistake:** MFS/Barclays exposure listed as £500M in STATUS.md but HANS signal said £600M and MEMORY.md confirmed £600M. Stale value persisted until audit.
**Rule:** When integrating cross-agent signals, check if the new value supersedes an existing one. Update the older reference, don't just add the new one alongside.

### [Methodology] — Run Own Falsifier-Status Check Before Thesis-Level Reframings
**Mistake:** WAL THESIS v2.0 (May 1) demoted V1 (hidden CRE / MI3 reclassification) from "MI3/hidden CRE/fast-transmission" to "Office single-point" — a 14× scope narrowing — BEFORE V1's primary pre-registered falsifier (MI3 ≥25% via Q1 Call Report) actually ran. RED CHG-RED-025 stress-test (May 6, 6-method weighted) verdict: OVER-CORRECTED (~26% aggregate PASS). Strongest single critique: M2 (counter-factual / pre-registered falsifiers). Caught by external grep + methodology audit, not by self-review.
**Rule:** Before publishing thesis-level reframings, run own falsifier-status check. Pre-registered falsifiers live in `WEAKNESSES.md` and bank-specific thesis files. Ask "have any of my own falsifiers actually fired?" — if not, reframing is premature. Demoting on framework redefinition (renaming the vector to narrower scope) instead of falsifier-firing is the specific anti-pattern. Same lesson family as the WALTER Turn 2 catch (claimed "zero action" in BOARD routing without running the grep first) — both cases would have been prevented by 30-second verification pass before publishing.

### [Methodology] — Position EV Math Must Match Thesis Timeline
**Mistake:** WAL SCENARIOS v2.0 EV table credited Jun 18 puts with full multi-quarter bear-payout intrinsic ($22 on $85P at $63 stock) — but V2.0's own bear-case mechanics said "fires across Q2-Q3 2026 (not single event)." Q3 ends Sep 30, well after Jun 18 expiry. RED M4 catch: either the math or the thesis is wrong; they can't both be true.
**Rule:** For multi-quarter thesis with short-tenor positions, separate "unconditional scenario probability" from "conditional probability that scenario has resolved by expiry." Build Jun-conditional / Sep-conditional EV tables explicitly. The Jun-conditional bear-payout weight is much smaller than the unconditional weight when the bear scenario fires gradually over multiple quarters. Position-recommendation that flows from unconditional math is mis-calibrated.

### [Process] — Grep POSITIONS.md Ground-Truth Before ANY Position Task (REPEAT of the 5/8 phantom error)
**Mistake (6/19, ORC-caught):** On the Jun-18 expiry, I read the cluster contents from CALENDAR.md and reported what "expired worthless" — but CALENDAR was desynced from POSITIONS.md (canonical). Result: (a) reported a phantom **SSB $90P** that was never in POSITIONS (exact signature of the KRE $70P phantom I caught 5/8); (b) wrote off **IWM $250P** as Jun-18-expired when it's a LIVE Jun-30 position (the Jun-18 IWM was $257P) — nearly killed a live position with 11 days left; (c) omitted 4 real Jun-18 positions (WAL $77.5P / FITB $45P / APO $100P / ARES $95P). Economic impact this time was zero (all OTM either way), but the process failure is the same one MEMORY already records from 5/8 — I trusted a dashboard re-list instead of grepping ground truth.
**Rule:** POSITIONS.md is the SINGLE canonical source for strikes/expiries. **Before any position task, grep POSITIONS.md first** — never trust a STATUS/CALENDAR cluster list (they drift). **Structural fix (shipped 6/19):** STATUS Convergence Matrix + CALENDAR no longer re-list strikes/expiries — they POINT to POSITIONS.md. Re-listing IS the drift vector; the Doc Ownership table already mandated single-source but wasn't enforced. If you catch yourself typing a strike/expiry into STATUS or CALENDAR, stop — put it in POSITIONS and reference it.

### [Process] — Check a Trigger's Anchor Still Matches the Thesis (anchor-drift)
**Mistake (6/19, ORC-caught):** The standing "Exit 100% on HY OAS <260bps" rule was written for the original **broad-systemic** thesis. The thesis has since narrowed to **idiosyncratic-WAL + CRE-specific** (Office / B1 walk-away / maturity wall / NCO migration) — none of which prints in broad HY bond spreads. HY drifting to 263 (3bps from trigger) on a risk-on rally would have mechanically stopped out a thesis whose actual confirmation channel had moved to CMBS-DQ flows / bank CRE-DQ tier-creep / WAL Q2 NCO. The trigger's anchor silently de-coupled from the thesis it was meant to protect.
**Rule:** When the thesis narrows or shifts channel, re-audit every standing trigger/threshold/exit-rule: does its *anchor metric* still print the thing the thesis now depends on? If not, re-anchor (or downgrade auto-action to a review trigger). Same family as the boot drift-grep — but for trigger *semantics*, not just stale values.

---

*Last reviewed: 2026-06-19 (added POSITIONS-ground-truth repeat-lesson + anchor-drift lesson, both ORC-caught)*
