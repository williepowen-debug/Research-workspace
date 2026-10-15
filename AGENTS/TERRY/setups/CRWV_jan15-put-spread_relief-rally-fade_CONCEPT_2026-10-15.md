# CONCEPT CARD — CRWV (CoreWeave) — Jan-15-2027 put spread on a relief rally against unrepaired credit

**Id:** `TRY-COND-CRWV-RALLYFADE`
**Terry verdict:** CONDITIONAL — CONCEPT, NOT PROPOSED. Saved as a working idea on Will's word (2026-10-15 12:05 ET, verbatim *"lets save this one as an idea/concept we are working on"*). No [Approve] is asked; nothing fills from this file.
**Date:** 2026-10-15 Thu, written 12:0x ET (`date`). Session: TERRY, Will-direct, Claude Opus 5.5 (`claude-opus-5-5`), Claude Code.
**Thesis owners (NOT TERRY):** LIQUID — CRWV bonds / 5Y CDS read (GATE-LIQ-069); VULCAN — AI-infra financing fragility (S5, fired 10/9). Both asked by packet 2026-10-15; Will is spawning both.
**Full working:** `research/2026-10-15_fleet-trade-idea-sweep/CRWV_relief-rally-fade_exploration.md` (facts, n=6 base rate, model structures). Construction rules 14–23 read in full before writing.
**`$0` MOVED · NO ORDER · NO GATE REGISTERED · NO THRESHOLD MOVED.**

## 1. One-line setup
If CRWV bounces hard while its lenders stay scared, fade the bounce with a defined-risk January put spread. The edge claimed is the equity/credit DIVERGENCE, not the direction.

## 2. Preconditions (all, same session) — the draft letter
- **(a) Rally:** CRWV regular-session close **≥ $70.00**, any session **Fri 10/16 → Wed 11/04**.
- **(b) Credit unrepaired:** LIQUID's read of CRWV 5Y CDS for that session **≥ 1,000bp (model)** — or LIQUID's stated equivalent on the 2032 notes. **Owner: LIQUID. Unanswered as of this write.**
- **(c) Green CRWV session** (root rule #6; a rally day is green by construction).
- ⚠️ **Construction rule #15:** a price-rally gate opens exactly as the market disagrees more with the bear case. Leg (b) carries the thesis information; **a fire is never evidence the thesis is working.**

## 3. Entry
- **Void (do-not-chase):** a CRWV close **< $58.00** before (a) fires ⇒ concept dies, no entry.
- Window ends 11/04 because the Q3 print is unannounced (third-party estimates Nov 5–16, unverified) — confirm at investors.coreweave.com before any build.

## 4. Structure (sketch — moment properties graded only at fire, construction rule #14)
- **1× Jan-15-2027 put spread:** long strike nearest 94% of fill-day spot, short 12.5 lower. ~85 DTE at a late-Oct entry (inside the 60–90 band; Dec-18 would be ~57 DTE, outside).
- **Model at spot $72:** Jan 67.5/55P ≈ $410 debit, max gain ≈ $840, breakeven ≈ $63.40. Comparator if bought today (live 11:31 ET): Jan 60/50P ≈ $402–425, max ≈ $575–598.
- Fire-time: `chain_fetch.py CRWV 2027-01-15 --legs <K1>,<K2> --no-cache` rc=0; price off Fidelity's quote, never the vendor (RISK_RULES 5b).

## 5. Risk
- **Max loss:** the net debit, **≤ $480 (≤ $500 incl. fees) = 2R cap.**
- **Kill:** CRWV close **≥ $82.00** (10/8 close $81.58 retraced) **OR** LIQUID CDS **< 840bp** (the 10/7 pre-scare level) ⇒ sell next session.
- **Gap/event:** Q3 print inside the tenor (known reactions −16.3% 2025-11-11, +19.3% 2026-08-12, n=2); financing/customer headlines; ±15% days are normal for this name (RV20 78%, RV60 102%).

## 6. Management
- **Harvest (#9):** spread net bid **≥ 1.8× debit** ⇒ sell. **Time stop:** sell by **Fri 2027-01-08**. **Roll:** none.

## 7. Why not / counter-trade
- 2 of 6 past ≥25%/10-session drops never bounced 10% and fell a further 22–29% — the card misses that path by design.
- The divergence rule is reasoned, **untested (n=0)**.
- **N_eff:** shares the credit-recovery falsifier with the bank-put book; a broad credit repair hurts both.

## Decision
None asked. To become a proposal it needs LIQUID's leg-(b) instrument named, VULCAN's thesis read, the print date confirmed, and a fire under § 2.
**APPROVAL REQUIRED — Will must approve/reject before execution.**
