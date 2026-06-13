# LIQUID — Decision Playbook

**Last Updated:** 2026-06-13 (HY OAS tracking RETIRED — Will, KB-LIQ-060; conviction 60, duration oscillating; basis canon per CLAUDE.md KEY THRESHOLDS preamble)

---

## Position Framework

### When to Escalate (signal other agents / propose trades)
- *(HY OAS 320-confirmation / 260-kill escalation lines RETIRED 6/13 — KB-LIQ-060. Credit-leg escalation now keys off CCC OAS >1000 + BDC mark cascade, below.)*
- **CCC OAS >1000bps** (tail watch; 957 on 6/10) OR a **BDC mark cascade** (multi-name NAV cuts + div cuts — see BDC_MARK_CONVERGENCE_MONITOR) → credit-leg escalation, route to BROCK/REGINALD
- **APO >$130 for 3 sessions** (raw closes only) → HEARTBEAT line 80 reassessment trigger. **FIRED 6/11, Day 4 close 6/12 ($133.88).** The old Trigger-C precondition (concurrent HY OAS *compression*) is now moot with HY OAS retired — the reassess read stands on the equity/mark-decoupling alone (→ BROCK). May history: ten straight closes 5/8–5/21, broke 5/22.
- SOFR sustained above 3.70% (not Q-end seasonal — see KB-LIQ-051 mechanical-vs-structural test)
- SOFR-IORB sustained positive for ≥3 sessions on non-tax-day, non-quarter-end catalyst
- SRF usage >$50B sustained
- Auction BTC <2.0x on any coupon maturity OR indirect bid <55% sustained
- Second private credit fund hard-gates
- 10Y sustained >4.50% with TLT confirming (KB-LIQ-052 — ⚠️ framing under re-derivation 6/12: duration is currently a 5.00-pivot oscillation, NOT sustained; this escalation line keys off a genuine re-establishment, ≥5 consecutive closes)
- 10Y single-session move >10bps (acute repricing within duration regime — 5/18 +12bps is the canonical example)

### When to Hold / Monitor
- CCC OAS below 1000 + no BDC mark cascade (current: CCC 957 6/10; the credit-leg hold zone post-HY-OAS-retirement)
- VIX in 15-25 (cooled to 17.68 close 6/12, off the 22.22 CPI-day spike — back toward the May range)
- SOFR within normal IORB band (currently -5bps, below ceiling)
- Duration channel oscillating around the 5.00 pivot (30Y 4.975 / 10Y 4.487 closes 6/12 / TLT ~$86) — between "durable" and "unwinding"; <4.90 sustained fires the unwind branch, FOMC 6/17 resolves
- Geopolitical flows de-escalating but not resolved

### When to De-escalate (kill levels)
- *(The HY OAS <260 credit-thesis kill is RETIRED 6/13 — KB-LIQ-060. No replacement credit-kill threshold set; the credit leg is now read qualitatively via BDC marks. The substance-vs-tape "false-kill guard" logic is preserved in BDC_MARK_CONVERGENCE_MONITOR — confirm substance reversal with BROCK before treating any credit calm as a kill.)*
- Credit leg de-escalates on a BDC mark-RECOVERY (NAVs stabilizing, div cuts ceasing) confirmed with BROCK — not on an index level
- Fed signals expanded liquidity facilities (kills the "Fed losing rate control" leg)
- Foreign official buying resumes (TIC confirmation) (kills the FOI demand-hole leg)
- Ceasefire confirmed + oil below $90 (kills the stagflation-trap leg + reduces duration pressure) *(6/13: oil leg HALF-FIRED — Brent's first sub-$90 close printed 6/12 ($87.33); ceasefire NOT confirmed, so the full kill is not fired — watch the pairing)*

## Active Position Views

| Position | Thesis | Current Assessment (6/13) |
|----------|--------|--------------------|
| HYG $75P Jun x10 | LIQ-01 credit stress (HY OAS retest of 320) | **Thesis broken** — and the HY OAS retest it keyed off is now a retired metric (KB-LIQ-060). HYG $79.94 (close 6/12), strike $75 = deep OTM; **expiry Fri 6/19 — T-4, decision window closing.** **→ close / let expire (Will decision).** Equity/credit puts bleed in regime-suppressed tape (see `put_vs_duration` memory). |
| ~~TEN calls Jun $30~~ | Triple premium (war + FOI + basis) | ✅ **CLOSED (Will, 6/12-13) — winner booked** (was ITM ~$7.11). |

## Active Workbooks
- ~~`workbook/KILL_MEMO_HY_OAS_260.md`~~ — **RETIRED 6/13 → `archive/`** (HY OAS tracking cut)
- `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` — Q1 BDC mark convergence watch (**now the primary credit-leg read**; FSK NAV -9.9% in; OBDC/ARCC/BXSL/MAIN pending)

## Asymmetry Notes
- Puts on green days, calls on red days (root CLAUDE.md rule)
- Roll duration, don't trim size (duration uncertainty ≠ thesis broken). Cut size only when thesis is broken (credit-leg break now judged via BDC mark cascade + BROCK confirmation, not an HY OAS level — KB-LIQ-060).
- Credit tightening = tactical, not structural. Don't close positions on 10bps of tightening.
- **Active channel can migrate.** If one leg of the thesis dies (SOFR-IORB plumbing, Apr 16 → resolved 5/18), check the others before exiting the whole book. Duration channel reignited as the bear thesis migrated out of plumbing.
- **Gamma-suppression caveat:** an OAS print that looks too calm during loud substance prints may be tape, not signal. Watch for gamma unwind.
