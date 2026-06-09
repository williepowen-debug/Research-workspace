# LIQUID — Decision Playbook

**Last Updated:** 2026-06-08 (catch-up restamp from 5/19; live-primary figures)

---

## Position Framework

### When to Escalate (signal other agents / propose trades)
- HY OAS crosses 320bps with momentum (not just a touch)
- **HY OAS <260 sustained ≥3 sessions** → credit-thesis kill (see `workbook/KILL_MEMO_HY_OAS_260.md`)
- **APO >$130 for 3 sessions** → HEARTBEAT line 80 reassessment trigger. Fires before HY OAS hits 260; *re-arming* — fired ~$135 mid-May, retraced, then **re-crossed $130 on the 6/8 bounce (~$131.5), Day 1 of 3**. If concurrent with HY OAS compression, treat as KILL_MEMO Trigger C precondition.
- SOFR sustained above 3.70% (not Q-end seasonal — see KB-LIQ-051 mechanical-vs-structural test)
- SOFR-IORB sustained positive for ≥3 sessions on non-tax-day, non-quarter-end catalyst
- SRF usage >$50B sustained
- Auction BTC <2.0x on any coupon maturity OR indirect bid <55% sustained
- Second private credit fund hard-gates
- 10Y sustained >4.50% with TLT confirming (active duration-channel transmission per KB-LIQ-052)
- 10Y single-session move >10bps (acute repricing within duration regime — 5/18 +12bps is the canonical example)

### When to Hold / Monitor
- HY OAS in 270-310 range (current: 276 — 16bps above 260 kill and narrowing, 44bps below 320 confirmation)
- VIX in 15-25 (currently ~18.8, possibly gamma-suppressed — see 5/14 signal)
- SOFR within normal IORB band (currently -2bps, below ceiling)
- Duration channel grinding (10Y 4.55 / TLT ~$84.6 / Brent ~$91) — bear thesis intact through this leg; Brent reflation co-driver has reversed
- Geopolitical flows de-escalating but not resolved

### When to De-escalate (kill levels)
- **HY OAS <260 sustained ≥3 sessions → KILL credit-thesis component** (see `workbook/KILL_MEMO_HY_OAS_260.md` for full trigger ladder). ⚠️ **False-kill guard (BROCK-aligned 6/8):** if the <260 compression is tape-only (rate-cut / risk-on) while PC *substance* is worsening (record defaults, gate cascade, BDC div cuts), do NOT auto-kill — that's a tape-kill, not a substance-kill. Confirm substance reversal with BROCK before pulling the thesis. *(Fuller treatment → KILL_MEMO, Tier-3 pass.)*
- 10Y back below 4.30 sustained AND HY OAS <270 → both channels unwinding, full thesis reassessment
- Fed signals expanded liquidity facilities (kills the "Fed losing rate control" leg)
- Foreign official buying resumes (TIC confirmation) (kills the FOI demand-hole leg)
- Ceasefire confirmed + oil below $90 (kills the stagflation-trap leg + reduces duration pressure)

## Active Position Views

| Position | Thesis | Current Assessment (5/19) |
|----------|--------|--------------------|
| HYG $75P Jun x10 | LIQ-01 credit stress (HY OAS retest of 320) | **Thesis broken.** HYG $79.54, strike $75 = deep OTM; HY OAS 276 tightening *away* from the 320 trigger; June expiry (~6/19). The retest-to-350 thesis didn't play. **→ close / let expire (Will decision).** Equity/credit puts bleed in regime-suppressed tape (see `put_vs_duration` memory). |
| TEN calls Jun $30 | Triple premium (war + FOI + basis) | **ITM winner — TEN $36.83 (~$6.83 intrinsic).** Dimona/ice-class war thesis intact; Brent reversal to ~$91 does NOT hit this (TEN is war/ice-class, not reflation). Hold/evaluate near expiry. Cross-check BRENT/HAWK before action. |

## Active Workbooks
- `workbook/KILL_MEMO_HY_OAS_260.md` — pre-written trigger ladder + verification + PROME template
- `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` — Q1 BDC mark convergence watch (FSK NAV -9.9% in; OBDC/ARCC/BXSL/MAIN pending)

## Asymmetry Notes
- Puts on green days, calls on red days (root CLAUDE.md rule)
- Roll duration, don't trim size (duration uncertainty ≠ thesis broken). Cut size only when thesis is broken (e.g., HY OAS <260 sustained for credit-thesis positions).
- Credit tightening = tactical, not structural. Don't close positions on 10bps of tightening.
- **Active channel can migrate.** If one leg of the thesis dies (SOFR-IORB plumbing, Apr 16 → resolved 5/18), check the others before exiting the whole book. Duration channel reignited as the bear thesis migrated out of plumbing.
- **Gamma-suppression caveat:** an OAS print that looks too calm during loud substance prints may be tape, not signal. Watch for gamma unwind.
