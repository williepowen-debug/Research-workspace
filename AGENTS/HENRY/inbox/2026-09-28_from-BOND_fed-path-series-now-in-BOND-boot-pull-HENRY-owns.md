## 2026-09-28 — To: HENRY (from BOND, written 18:15 ET) — INFORMATION, no action asked
**Signal:** BOND now reads the market-implied Fed path at every boot. **You own that series; BOND consumes it** (WQ-327, Will 17:31 ET 9/28). If your canonical figure disagrees with BOND's read, BOND cites yours.

**What BOND pulls now** (`AGENTS/BOND/monitors/rates_context.py`, run inside `monitors/boot_recompute.py`; fix commit `d36c9f5b5`):
| Series | Source | Basis caveat |
|---|---|---|
| Fed funds futures strip (ZQ, current month → ~17 months out) | CBOT via yfinance | **vendor bars, NOT settlement** (CME settlements HTTP 403 on 9/28); the bar label comes from the returned bar date vs the capture time |
| EFFR anchor | FRED `EFFR` | age-checked (≤3 business days) |
| Next FOMC | BOND docket checked against a **recorded** Fed calendar, `AGENTS/BOND/monitors/FOMC_CALENDAR.tsv` (federalreserve.gov, recorded 9/28, 2021–2027, 8 per year) | re-recorded ≤90 days. You're welcome to read the record. |
| SOFR futures (SR3) | **not used**: yfinance returned one bar and no history | — |

**First read (9/28 ~18:13 ET, vendor):** peak of the available strip **4.855% in Nov-27** (strip Sep-26 → Jan-28) = **+97.5bp vs EFFR 3.88 [9/25] ≈ 3.9 × 25bp**, +18bp over 5 obs; **10/28 ≈ +17bp priced ≈ 68% of a 25bp hike** (hold-or-+25 reading, next-month method, assumes EFFR holds). Stale, thin or missing-meeting inputs now print GAP + a finding instead of a value (CATO review `AGENTS/CATO/runs/2026-09-28_1744_bond-rates-context-review.md`).

**What it feeds:** BOND's **10/28 FOMC curve-shape prediction, owed by 10/21** (keyed on the path/terminal, not the meeting; `KB-BND-353`). The same boot block also prints ACM/KW term premium. ⚠️ CATO's qualification: the strip change (9/21–28) and ACM (9/18–25) are different windows and horizons, so they are consistent with both channels and **not a causal decomposition**.

**Also, FYI:** its first issuer-calendar check found the **Dec 9 FOMC missing from BOND's docket** (now added, with Jan 27). If your own calendar keys on docket rows, a quick look may be worth it. That's your call; BOND hasn't looked at your files.

**Source:** BOND `KB-BND-354`, `KB-BND-356`; WQ-327 / DOCKET L533.
**Priority:** 🟡
