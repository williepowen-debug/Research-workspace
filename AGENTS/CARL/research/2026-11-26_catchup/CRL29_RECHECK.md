# CRL-29 (CARL-AUTO-OUTFLOW-01) re-check, ages 28 to 30 — PANEL NO VERDICT

**Written:** 2026-11-26 12:01 ET, CARL, on PROME prome-80's follow-up (the November re-check had no record). Rules unchanged: WQ-437 (Will 10/15) = RED's C1–C5. **CRL-29 stays 30%, OPEN.** No score, band or rule moved.

**What was owed and why it is the 10-D panel, not the HHDC:** CRL-29's instrument is the SEC 10-D EX-99.1 panel (AMCAR 2023-2, AMCAR 2024-1, EART 2024-1). The 10/21 thread said "re-check at the Q3 HHDC row"; that names the timing, not the instrument. Re-check = the same grader on the next seasoning-matched window.

**Window choice (made before the grader ran):** the next window sharing one end-point with the first: ages 28→29→30 (first grade was 26→27→28). Trusts unchanged. ⚠️ This window was chosen by CARL today, not pre-registered in `domain/sources/2026-10-12_followup/auto-age-match.tsv` (which registered ages 26–28 only). Proposal, ⚠️ written AFTER seeing this result, so a proposal for RED and Will, not a rule: step windows by two ages (26–28, 28–30, 30–32), next 30–32; no later window is read today.

**Method:** `crl29_grade_2026-11-26.py` = the 10/21 grader with only the panel months and the age base changed. Nine certificates fetched from SEC 11/26 (non-identifying desk client string), sha256 in `crl29_certificates_sha256_2026-11-26.txt`, output `crl29_out.json`. **Control:** the three age-28 rows reproduce the 10/21 output exactly (bop, eop, net loss, 61+, 31+, extensions, loss, extension rate, stock). Printed extension rates match computed ones.

| Trust (collection months) | Δ61+ stock (pp) | Δ annualized loss (pp) | Δ extension (pp) | Month cells | Trust |
|---|---|---|---|---|---|
| AMCAR 2023-2 (Dec 2025 → Jan → Feb 2026) | −0.4519 / +0.0451 | −1.9412 / −1.3135 | −0.5038 / −0.7630 | stock down, loss down, extension down = NV · premise absent | NO VERDICT |
| AMCAR 2024-1 (Aug → Sep → Oct 2026) | +0.1943 / −0.0846 | −0.4937 / **+1.3603** | −0.3816 / +0.3554 | premise absent · **A** | NO VERDICT |
| EART 2024-1 (May → Jun → Jul 2026) | +0.5560 / −0.3314 | −0.9441 / **+2.3362** | +0.2534 / −0.5545 | premise absent · **A** | NO VERDICT |

**Panel: NO VERDICT** (0 trusts with two same-band changes). A registered null: neither support for CARL's loss read nor for the Philly Fed extension read.

**What to watch, stated plainly:** in the second change two of three trusts landed in **Band A** (stock down, annualized loss up ≥0.77pp), CARL's own read. ⚠️ Each is ONE month, and both sit in the seasonal climb in auto losses out of the spring tax-refund low (Jun→Jul, Sep→Oct), so a seasonal loss rise with a falling stock is the no-stress baseline (MEMORY M39). Under the two-age stepping above these cells do not carry into the next window. A rolling reading would put two trusts at "A, 1 of 2"; that is a different rule and is not applied.

**Forward view (unscored):** CARL expects the 30–32 window to stay NO VERDICT more likely than not, because the AMCAR 2024-1 leg needs Nov and Dec 2026 certificates and seasonal loss climbs inflate Band A cells; meaningful alternative: Band A in two trusts if subprime losses keep rising faster than the season. Horizon: AMCAR 2024-1 December collection month, 10-D about 2027-01-27. Would change the view: a second consecutive A on AMCAR 2024-1 (Oct→Nov).

**Stock levels at age 30 (61+ / end pool):** AMCAR 2023-2 3.55%; AMCAR 2024-1 4.23% (age 28 4.12%, a year-later vintage running higher); EART 2024-1 10.48%.
