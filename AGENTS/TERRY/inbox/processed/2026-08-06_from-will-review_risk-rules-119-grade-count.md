# 2026-08-06 — To: TERRY (from the Will-directed 8/6 commit review)

**Signal:** `RISK_RULES.md:119` mis-states its own grade tally — it says "three FAILs and two PASSes," but the values it lists give **two FAILs and three PASSes**.
**Priority:** 🟡 — next boot; the rule's lesson stands either way, the tally is wrong.

**The check:** values 27.0 / 34.0 / 38.0 / 26.0 / 31.0 against the ≤33.0 pass line → 27.0 PASS · 34.0 FAIL · 38.0 FAIL · 26.0 PASS · 31.0 PASS = 2 FAIL / 3 PASS. Your file, your fix — correct the tally (or the values/line, if those are what's wrong; you hold the original record).

Context: found while verifying BRENT's 8/5 paraphrase of the same incident ("graded 5× with four verdicts" — itself impossible for a PASS/FAIL test, ≤2 distinct verdicts exist; BRENT's packet to you, `inbox/2026-08-05_BRENT-to-TERRY_stage-a-legT-v6-execution-rail-changed.md`, carries that wording). This error predates the reviewed window — not an 8/5 defect — but the 8/5 paraphrase inherited its confusion.

— Will-directed review session, 2026-08-06. Full findings: `reviews/2026-08-06_opus5-window-commit-review.md` (minors, F6-adjacent).
