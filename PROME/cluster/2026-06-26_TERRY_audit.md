# TERRY Audit — Alert → Approve-Ready Card in Minutes
**Date:** 2026-06-26 · **Author:** TERRY (cluster, propose-only) · **Scope:** everything AFTER an alert fires. Detection = LIQUID/SENTRY.

## CARD-READINESS
The `2026-06-26_bank-put-reshape-roll.md` is a strong decision *skeleton*, ~90% pre-locked — but it is **not one Approve-ready card**. Two blockers:
1. **It's a menu, not a card** — V1/V2/V3 still force a choice at fire-time. Collapse to V1-default + one-line override.
2. **It's a RESHAPE (book maintenance), not a fresh-deploy card.** Will's new rule = fresh capital ONLY on a fired trigger. There is **no** fire-ready card for "HY breaks 280 → fresh regional put" or "WAL Jul-30 build-confirmed → fresh WAL put." That is the real gap.

**Pre-lockable (survives to fire):** path→catalyst→duration logic; harvest/let-expire lists; strike ladders; kill/confirm lines; "no new net risk" frame.
**MUST re-pull live at fire (rule #4 / option-marks-go-phantom):** every price in the ref line; the 2027 TLT chain (bid/ask/OI/IV — these were ~10:50 ET marks); 10Y for path-b confirm; green/red check (rule #6); recoverable premium vs **live broker book** (image = snapshot, rule #3).

## GRADING-AS-TOOLING
The Jul-print instrument is a static lookup table — at fire-time a human still reads the release, extracts Provision$/NCO$, classifies specific-vs-collective, and tallies ≥2-bank paths under time pressure. But the **logic is fully deterministic and needs no market data — only filing numbers.** Ideal script candidate. A `grade_print.py` would: load Q1 baselines + thresholds + the documented unit-traps as JSON config; accept new-quarter Provision/NCO/ACL/coverage/AOCI/TBV + a roll-forward language flag; output per-name BUILD/RELEASE + specific/collective + path (a)/(b)/(c) ≥2-tally. Encode the 3 known mis-grade traps as forced prompts: WAL adjusted-vs-GAAP NCO, ZION total-AFS-not-muni AOCI, ALLY collective-not-counting.

## PIPELINE (minimal trigger→card)
Two trigger classes: **price** (HY 280 / 10Y level) and **print** (WAL build). Path: ALERT → [price: confirm level | print: run `grade_print.py`] → pull live prices+chain (one cmd) → drop into pre-staged skeleton (structure/strikes/kill-lines already in) → `risk_calc.py` sizing → Approve. **Biggest blocker: no live option-chain CLI** — `fetch.py` has no `chain` cmd; the proposal pulled chains ad-hoc via yfinance. `chain_parse.py` only parses *pasted* broker exports. That makes rule #4 a manual scramble exactly when speed matters.

## FIX (propose-only, all local)
1. **`chain_fetch.py`** (TERRY/scripts, yfinance `option_chain` wrapper): `chain_fetch.py TLT --expiry 2027-03-19 --type put` → kills the ad-hoc step.
2. **`grade_print.py`** — config-driven grader above; traps as guards.
3. **Two pre-staged fresh-deploy skeletons** in `setups/`: `PRICE-TRIGGER_HY280_regional-put.md` + `PRINT-TRIGGER_WAL-EGBN-build.md` — all pre-locked except a `LIVE MARKS` block.
4. **`card_fill.py`** (or 3-cmd runbook): snapshot → chain_fetch → risk_calc, stamps the skeleton's live block.
5. Collapse reshape V1/V2/V3 → single default card.

**Net:** items 1+3 alone convert ~hours to ~minutes. APPROVAL REQUIRED — Terry never executes.
