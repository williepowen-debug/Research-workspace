# OZK → PROME · 2026-10-01 12:3x ET · L126 reprice day: reset SCHEDULED-UNCONTRADICTED, coupon ≈6.19% from the indenture; Dec-18 flag re-read; inbox 3→0

**Spawn:** `prome-0c` due-row (WQ-184, Will "spawn the slate" 12:13 ET). $0 · no trade view · **zero grades, thresholds, weights or conviction moved.** Desk commit `f48e8062e`; packets `5d14d8e7c` (REGINALD) · `69aa7d1ee` (CREED) · `a6912b119` (PROME cadence) · `92bae5fc6` (WALTER cc).

## 1. L126 — the $350M sub-notes reset (primary task)

| Item | Result | Confidence |
|---|---|---|
| FDIC FLNG cert 110 (`flng_watch.py`, 12:14 ET) | **rc 0** — 182 filings, schema+coverage OK, none after 11981 | VERIFIED (a no-newer-filing return, not proof) |
| Press search, OZK sub-notes call/refi | none (hits = OZK's 2021 redemption of its old 5.50% notes; other banks) | SEARCH-NOT-FOUND |
| Event | **reset 10/1 SCHEDULED-UNCONTRADICTED** — a call needs 10–60 days' holder notice via the agent/DTC, which need not be filed | — |
| Indenture (FDIC FLNG 5869, Fiscal Agency Agmt + Global Note; circular FLNG 5866) | benchmark **CME 3M Term SOFR** + 209bp, floor 0, **Actual/360**; fixing time = "calculation agent after giving effect to the Three-Month Term SOFR Conventions" — **no lookback stated**; initial calc agent = the Bank | VERIFIED |
| Fixing date | Tue **9/29** (T−2 U.S. Gov't Securities business days = market practice) | INFERRED |
| 3M Term SOFR 9/29 | **4.09580%** (9/24 4.07433 · 9/28 4.07457 · 9/30 4.08330) — global-rates.com republishing CME; CME data licensed, no second source | SINGLE-SOURCE |
| **Reset coupon** | **6.18580%** (range 6.164–6.186% across 9/24–9/30) | DERIVED |
| Cost vs 2.75% | **≈+$12.3M/yr pre-tax** (Act/360, 365d), **≈$0.09 EPS** (22.5% tax, 109.6M dil. sh); first floating quarter (92d) +$3.13M | DERIVED |

**The 9/24 figure (≈5.96% / ≈+$11.2M / ≈$0.08) is superseded** — it used overnight SOFR 3.87% as a proxy for 3M Term and 30/360 arithmetic. Re-based on OZK's live surfaces (STATUS, CALENDAR, THESIS §4, SCENARIOS, WEAKNESSES, CHANGELOG, KB-OZK-241); dated research threads left as records. Evidence → `AGENTS/OZK/research/threads/2026-10-01_SUBNOTES_RESET.md`.

**Today's read is final on the coupon question; the 10/2 read (L463) stays armed for the filing question only.** It must: (1) run `flng_watch.py` → rc 0 = SCHEDULED-UNCONTRADICTED (log rc, row count, time) · rc 1 = read each filing (call/refi = 🟠 REGINALD+PROME, recalculate per THESIS §Invalidation 4; a Q3-date 8-K sets the Q3 row) · rc 2 = UNKNOWN, re-run; (2) one press search "Bank OZK" subordinated/redemption 9/1–10/2. The coupon becomes VERIFIED only at the **Q3'26 10-Q (~early Nov)** — OZK is its own calculation agent; added to the Q3 10-Q row in OZK CALENDAR (could ride DOCKET L520 — your call).

**Consumers of the superseded figure (`consumer_check --old 11.2M --new 12.3M`):** REGINALD `CALENDAR.md` l.30 → packet sent. **PROME's own DOCKET L126 + L463 carry "≈+$11.2M / SOFR 3.87% / INFERRED"** — yours to annotate; I did not touch them. The other 🔴 hits are bare-figure collisions (Amerant $11.2M, a Bain CLO €, etc.) — no packet.

## 2. Firetime "Dec 18" DATE DRIFT — full logic re-read done
The flagged "Dec 18" is a **past** maturity (Baltimore land, **2025-12-18**), written without a parseable year; the checker's `mon_d` pattern ignores a trailing year and read it as 2026-12-18. Re-read the whole Problem-Credits passage against primary: Baltimore 2025-12-18 (Q1+Q2 MC "This loan matured December 18, 2025" + multi-parcel buyers) and Boston **2026-02-13** (Q1 MC "following its February 13, 2026 maturity" + $330M pending sale) both VERIFIED; the four nonaccrual credits sum to $251.9M ✓. Dates now ISO. ⚠️ The checker now flags **2026-12-22** — a genuine NEW forward date (end of the holder-notice window for a 1/1/27 par call: 11/2–12/22), not drift. Tool note for the checker's owner: `mon_d` should consume a following ", YYYY".

## 3. Inbox (L0, whole inbox: 3 items + .gitkeep = census 4; WALTER/ 0)
- DAEDALUS 9/24 market.py prev-close/stale marking → FYI, no-op (boot.py uses fetch.py).
- PROME 9/25 WQ-295 → **cadence EVENT-DRIVEN declared** (`PROME/inbox/2026-10-01_from-OZK_cadence-and-watch-terms.md`) + 3 WATCH_FOR phrases (`IQHQ` · `BPRE` · `Campus at Horton`) for triggers that would not name the bank, + a lane-query gap (no lane query fetches IQHQ — the 9/17 Spur→Apollo deed-in-lieu reached no lane surface). **No WQ-295 R3 verdict packet exists for OZK** (OZK had proposed nothing; WALTER's `61a90bbd3` sent none here) — nothing to adopt/decline.
- CREED 10/1 → both inconsistencies resolved at primary: Sullivan prior charge-off = **$72.4M, Q4'25** (Q4 MC Fig. 26) — W1 corrected; San Carlos = INFERRED-HIGH debt-on-debt (10-Q "Other" class Q2 c/o $15.3M; Jack+San Carlos = $42.5M vs RIAD5409 $42,437K) — the 7/21 scoring-card line bannered SUPERSEDED, KB-232 stands; BROCK already holds flip (a) FIRED-INFERRED. Reply packet sent.

**Tape:** OZK **$45.96** live 10/1 12:20 ET (<$45 band 2.1% away, not fired); −6.4% since 8/31 vs KRE ≈−5.4% — mostly beta. Q3 earnings date not announced.

## COMPLETION — OZK — 2026-10-01
STATUS: ✅ DONE
CHANGED: AGENTS/OZK/{STATUS,CALENDAR,THESIS,CHANGELOG,SCENARIOS,WEAKNESSES,INDEX,MEMORY}.md, workbook/{KB.tsv,KB_INDEX.md,Q2_2026_SCORING_CARD.md}, research/threads/{2026-10-01_SUBNOTES_RESET.md (new),2026-09-27_Q2_WORKOUT_CHECK_OZK.md}, inbox 3→processed; packets → REGINALD, CREED, WALTER, PROME
RESULT: Reset 10/1 SCHEDULED-UNCONTRADICTED (FLNG rc 0, 182, none after 11981). Indenture VERIFIED (CME 3M Term SOFR+209, Act/360); coupon ≈6.19% on 4.09580% [9/29, single-source, T−2 INFERRED] ⇒ ≈+$12.3M/yr (~$0.09 EPS), superseding ≈$11.2M. "Dec 18" = past Baltimore maturity, re-verified; inbox 3→0; cadence EVENT-DRIVEN; zero grades moved.
GAPS: 3M Term SOFR single-source (CME licensed); fixing date INFERRED (no lookback in the note) — both close at the Q3 10-Q. No WQ-295 R3 verdict packet existed for OZK. Push receipt below if safe-push passed.
WILL_NEEDS: None.
FOLLOW-UP: L463 Fri 10/2 = FLNG + press search only (coupon done). PROME: annotate DOCKET L126/L463 (+$11.2M → +$12.3M); optional row for the 11/2–12/22 call-notice window / Q3 10-Q coupon VERIFY (could ride L520).
