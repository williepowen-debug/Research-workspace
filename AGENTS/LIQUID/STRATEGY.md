# LIQUID — Decision Playbook

**Last Updated:** 2026-05-18 (revival session)

---

## Position Framework

### When to Escalate (signal other agents / propose trades)
- HY OAS crosses 320bps with momentum (not just a touch)
- SOFR sustained above 3.70% (not Q-end seasonal — see KB-LIQ-051 mechanical-vs-structural test)
- SOFR-IORB sustained positive for ≥3 sessions on non-tax-day, non-quarter-end catalyst
- SRF usage >$50B sustained
- Auction BTC <2.0x on any coupon maturity OR indirect bid <55% sustained
- Second private credit fund hard-gates
- 10Y sustained >4.50% with TLT confirming (active duration-channel transmission per KB-LIQ-052)

### When to Hold / Monitor
- HY OAS in 270-310 range (current: 280 — 20bps above 260 kill, 40bps below 320 confirmation)
- VIX in 15-25 (currently 17.82, possibly gamma-suppressed — see 5/14 signal)
- SOFR within normal IORB band (currently -10bps, well below ceiling)
- Duration channel grinding (10Y 4.59 / TLT $83.56 / Brent $109) — bear thesis intact through this leg
- Geopolitical flows de-escalating but not resolved

### When to De-escalate (kill levels)
- **HY OAS <260 sustained ≥3 sessions → KILL credit-thesis component** (see `workbook/KILL_MEMO_HY_OAS_260.md` for full trigger ladder)
- 10Y back below 4.30 sustained AND HY OAS <270 → both channels unwinding, full thesis reassessment
- Fed signals expanded liquidity facilities (kills the "Fed losing rate control" leg)
- Foreign official buying resumes (TIC confirmation) (kills the FOI demand-hole leg)
- Ceasefire confirmed + oil below $90 (kills the stagflation-trap leg + reduces duration pressure)

## Active Position Views

| Position | Thesis | Current Assessment (5/18) |
|----------|--------|--------------------|
| HYG $75P Jun x10 | LIQ-01 credit stress (HY OAS retest of 320) | **Thesis weakened.** HY OAS 280 well below 320 trigger and within 20bps of 260 KILL. If kill memo Trigger A fires (<265 ×2 sessions), CUT. Hold pending Will decision and live re-verification of OAS print. |
| TEN calls Jun $30 | Triple premium (war + FOI + basis) | Dimona extends — hold through ceasefire resolution. Out of credit-thesis-kill scope (cross-check BRENT/HAWK before action). |

## Active Workbooks
- `workbook/KILL_MEMO_HY_OAS_260.md` — pre-written trigger ladder + verification + PROME template
- `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` — Q1 BDC mark convergence watch (FSK NAV -9.9% in; OBDC/ARCC/BXSL/MAIN pending)

## Asymmetry Notes
- Puts on green days, calls on red days (root CLAUDE.md rule)
- Roll duration, don't trim size (duration uncertainty ≠ thesis broken). Cut size only when thesis is broken (e.g., HY OAS <260 sustained for credit-thesis positions).
- Credit tightening = tactical, not structural. Don't close positions on 10bps of tightening.
- **Active channel can migrate.** If one leg of the thesis dies (SOFR-IORB plumbing, Apr 16 → resolved 5/18), check the others before exiting the whole book. Duration channel reignited as the bear thesis migrated out of plumbing.
- **Gamma-suppression caveat:** an OAS print that looks too calm during loud substance prints may be tape, not signal. Watch for gamma unwind.
