# BOND THESIS — Changelog

Version history for `thesis/THESIS.md`. Newest first. Bump rules: **major (X.0)** = regime change / conviction reversal / channel restructure; **minor (X.Y)** = refinement, threshold update, prediction resolution. Every entry logs old view → new view.

---

## v1.1 — 2026-07-01 (long-end re-engagement + JGB-FX channel + mandate extension)

**Triggers:** 11-day gap sweep (6/20→7/1); three predictions resolved (BND-02 FAILED, BND-04 FALSE, BND-10 VOID); a new transmission channel; a Will-approved coverage extension.

**Old view (6/20):** the hawkish FOMC bear-flattened — risk migrated to the front-end (HENRY's lane); BOND's long-end anchored; the one escalating vector was DFII10 (real-rate side); TLT puts on the "wrong tape."

**New view (7/1):**
1. **The long end is re-engaging, phase III** — 30Y 4.97 (+11bp/2d), globally synchronized: domestic hawkish-data repricing (JOLTS beat, ISM prices 73, Dec-hike ~79-82%) **co-firing with a JGB super-long rout** (6/30: 30Y JGB +8.8bp; weakest 20Y JGB auction since May-2025 on 6/25; rinban step-down effective 7/1). NOT real-rate-led this time (DFII10 peaked 2.29 → 2.20): policy-repricing + global term premium. Long-end vector 2→3; composite 11→12/35.
2. **New channel 6 — Global long-end / JGB-FX:** window evidence shows JGB↔UST *duration decoupling* (weak JGB 20Y auction → USTs rallied 4 sessions), so the armed leg is **FX-routed**: yen at a 40-year low (162+), record ¥11.7T intervention spent, Mimura verbal warning 7/1 — *actual* MOF intervention = mechanical UST reserve selling. Built from SAM's 6/30 signal + independent verification (their baseline was one session stale — pre-rout).
3. **Demand composition rotating:** June cluster cleared (6th straight benign — BND-11 arms the 7th test at the 7/7-9 refunding) but indirects fell <60% at 2Y/7Y with 13-21pp m/m slides, absorbed 1:1 by directs. VX-08/13 → 3. Dealer long-end stock at a **fresh record** ($74.6B 11-21Y, 6/17) — →4 trigger ARMED; 7/2 print + 7/9 30Y decisive.
4. **Falsified legs cleaned up:** issuance-freeze mechanism resolved FAILED (Apr-Jun was an AI-capex issuance BOOM — April HY $40B, record June IG); CLO-AAA canary FALSE (BSL never near SOFR+160; MM near-miss S+158). Warsh MBS-sales supply leg deferred to 2027 ("years, not months," Sintra) — removed as near-term amplifier. Oil→breakevens re-arm bar proven HIGH (live kinetic Iran exchange 6/25-28 bought only ~2-6bp of breakeven).
5. **Mandate extension integrated (6/27 SIG):** + MBS/housing-finance/FHLB advances (VX-17/18) and Eurozone rates (VX-19 — ECB is HIKING: first hike since 2023 on 6/11, OAT-Bund widening). EU leg starts at watch-level 2.

**No conviction change:** TLT puts HOLD/no-add — gates pre-registered (BND-11/12; DFII10 >2.5; 30Y >5.0 ×5 + weak auction), none fired. But the tape rotated from working *against* the expression (bear-flattener) to working *toward* it (global steepening tilt into a supply gauntlet with a record-thin dealer backstop).

---

## 2026-06-20 — intra-v1.0 POV note (no version bump)

**Trigger:** the live post-refunding gate resolved — 6/16 20Y, 6/17 FOMC, 6/18 TIPS.

**POV pivot (refinement, not reversal):** the hawkish surprise hit the **front-end, not the long-end.** The Warsh FOMC (6/17) delivered a hawkish pivot (dot median +40bp to 3.8, core PCE +60bp to 3.3, 9/18 see a hike) but the curve **bear-FLATTENED** — 2Y +15bp, **30Y flat at 4.93** — the *inverse* of the supply/term-premium bear-*steepener* the thesis is built around. The long end **held below thresholds through a hawkish Fed**, and the 6/16 20Y printed **STRONG** (BTC 2.75, best in 3mo) → **BND-09 FALSE** (5th straight benign auction-stress resolution). Net: "expensive, not broken" is *strengthened* — even a hawkish catalyst couldn't break the long end.

**What this changes:** (1) the term-premium re-fire *failed its cleanest test* — the TLT-puts add-case weakens (a bear-flattener is the wrong tape for a duration short; TLT rallied). (2) The one BOND-domain vector now *escalating* is the **real-rate side (DFII10 2.23, +7, rising)** — re-framed as the cleanest single re-arm metric (watch → 2.5), displacing the nominal-threshold watch. (3) Confound logged: an Iran interim-peace/oil-down signal 6/17 aided the long-end anchoring, so it is not purely a clean-FOMC read. **No conviction change** — composite 11/35 flat; TLT puts HOLD/no-add.

---

## v1.0 — 2026-06-15 (first formal thesis doc)

**Change:** Migrated the durable thesis out of STATUS.md prose into a standalone `thesis/` structure (THESIS.md + CHANGELOG.md + PREDICTIONS.tsv), matching the mature peer pattern (BRENT/SAM/CARL). STATUS.md is now pure live-state (dashboard, convergence matrix, catalysts, compact exits, bottom line); the durable read, transmission channels, full exit/falsification, and position rationale live in THESIS.md.

**State captured at v1.0:**
- Regime: 🟡 WATCH — "expensive, not broken." The May–June long-end term-premium episode (BND-07) fired, mean-reverted, re-fired into the June refunding, and relaxed once the refunding cleared.
- Conviction: TLT puts HOLD/no-add; short-credit not supported; composite 11/35.
- Evidence: June refunding cleared (10Y strong, 30Y soft-orderly) → BND-08 FALSE; working model held 4 straight resolutions (BND-05 F · 06 T · 07 T · 08 F).

**No conviction change** — structural migration, not a thesis revision. View unchanged from the 6/9 STATUS regime read; restated in durable form and refreshed to the post-refunding tape.

---

## Pre-v1.0 — historical arc (reconstructed from STATUS / PREDICTIONS; not versioned at the time)

Provenance for the thesis predating this doc:
- **BND-07 episode (May):** long-end leg fired — 30Y >5.0 ~9 sessions + 10Y >4.5 for 6 (5/14–5/27). Threshold TRUE, but resolved as an **episode, not a one-way break** [[threshold_vs_mechanism]] — term premium gave back into early June.
- **TIPS-vs-nominal correction (5/21):** the 5/21 "10Y reopening" was a 10Y *TIPS* reopening (CUSIP 91282CPU9), not nominal — conflation corrected in the 6/9 STATUS; the add-gate keyed to it was mis-specified (moot).
- **"Expensive, not broken":** established across the May refunding / 20Y / TIPS reads — the long end clears demand at price; term-premium digestion, not mechanical failure.
- **Dealer-backstop-thin (6/9):** NY Fed FR2004 (5/27) — dealer long-end inventory near/at record; buyback long-end offer/accept ~13x. Dealer-absorption vector → 3.

*Reconstructed for continuity; historical context, not contemporaneous version entries.*
