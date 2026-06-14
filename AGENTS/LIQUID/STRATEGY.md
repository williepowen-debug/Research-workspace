# LIQUID — Decision Playbook

**Last Updated:** 2026-06-12 (post-THESIS-restamp; conviction 60, duration oscillating; basis canon per CLAUDE.md KEY THRESHOLDS preamble)

---

## Position Framework

### When to Escalate (signal other agents / propose trades)
- HY OAS crosses 320bps with momentum (not just a touch)
- **HY OAS <260 sustained ≥3 sessions** → credit-thesis kill (see `workbook/KILL_MEMO_HY_OAS_260.md`)
- **APO >$130 for 3 sessions** (raw closes only) → HEARTBEAT line 80 reassessment trigger. **FIRED 6/11** (closes 6/9-6/11: 132.70/131.14/133.91) — **NOT Trigger C**: escalation requires concurrent HY OAS *compression*, and HY widened 274→280 through the window. Reassess resolved 6/12 (equity/mark-decoupling read → BROCK). Re-fires as Trigger C precondition only if a ≥3-close streak coincides with HY compression. May history: ten straight closes 5/8–5/21, broke 5/22.
- SOFR sustained above 3.70% (not Q-end seasonal — see KB-LIQ-051 mechanical-vs-structural test)
- SOFR-IORB sustained positive for ≥3 sessions on non-tax-day, non-quarter-end catalyst
- SRF usage >$50B sustained
- Auction BTC <2.0x on any coupon maturity OR indirect bid <55% sustained
- Second private credit fund hard-gates
- 10Y sustained >4.50% with TLT confirming (KB-LIQ-052 — ⚠️ framing under re-derivation 6/12: duration is currently a 5.00-pivot oscillation, NOT sustained; this escalation line keys off a genuine re-establishment, ≥5 consecutive closes)
- 10Y single-session move >10bps (acute repricing within duration regime — 5/18 +12bps is the canonical example)

### When to Hold / Monitor
- HY OAS in 270-310 range (current: 280 — 20bps above the kill and widening away from it, 40bps below 320 confirmation)
- VIX in 15-25 (currently ~19; floor lifted from May's 15-17 — two >21 closes within four sessions 6/5-6/10; the gamma-suppression regime has shifted, watch credit-vol catch-up)
- SOFR within normal IORB band (currently -5bps, below ceiling)
- Duration channel oscillating around the 5.00 pivot (30Y 4.95 / 10Y 4.46 closes 6/11 / TLT ~$86) — between "durable" and "unwinding"; <4.90 sustained fires the unwind branch, FOMC 6/17 resolves
- Geopolitical flows de-escalating but not resolved

### When to De-escalate (kill levels)
- **HY OAS <260 sustained ≥3 sessions → KILL credit-thesis component** (see `workbook/KILL_MEMO_HY_OAS_260.md` for full trigger ladder). ⚠️ **False-kill guard (BROCK-aligned 6/8; consistency-checked vs conviction-60 frame 6/12):** if the <260 compression is tape-only (rate-cut / risk-on) while PC *substance* is worsening (record defaults, gate cascade, BDC div cuts), do NOT auto-kill — that's a tape-kill, not a substance-kill. Confirm substance reversal with BROCK before pulling the thesis. **6/12 amendment:** the guard's fallback ("re-frame around the duration channel") was written against the duration-matured frame; with duration now oscillating, a credit kill that fires while 30Y is sub-5.00/testing 4.90 goes to the FULL-reassessment branch (both channels weak), not the migrate-to-duration branch. *(Fuller treatment → KILL_MEMO, Tier-3 pass.)*
- 10Y back below 4.30 sustained AND HY OAS <270 → both channels unwinding, full thesis reassessment
- Fed signals expanded liquidity facilities (kills the "Fed losing rate control" leg)
- Foreign official buying resumes (TIC confirmation) (kills the FOI demand-hole leg)
- Ceasefire confirmed + oil below $90 (kills the stagflation-trap leg + reduces duration pressure) *(6/12: LIVE-WATCH — zero sub-$90 Brent closes yet, 6/11 closed 90.38; no ceasefire; not fired)*

## Active Position Views

| Position | Thesis | Current Assessment (6/13) |
|----------|--------|--------------------|
| ~~HYG $75P Jun x10~~ | LIQ-01 credit stress (HY OAS retest of 320) | ⬛ **WRITTEN OFF (cut bait 6/13).** Dead, deep OTM ($79.94 vs $75); let expire worthless 6/19. No action, no further surfacing. *(The HY OAS retest-to-320 thesis it expressed did not play — but HY OAS itself remains a tracked signal; only this position is dead.)* |
| ~~TEN calls Jun $30~~ | Triple premium (war + FOI + basis) | ✅ **CLOSED (Will, 6/12-13) — winner booked** (was ITM ~$7.11). |

## Active Workbooks
- `workbook/KILL_MEMO_HY_OAS_260.md` — pre-written trigger ladder + verification + PROME template
- `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` — Q1 BDC mark convergence watch (FSK NAV -9.9% in; OBDC/ARCC/BXSL/MAIN pending)

## Asymmetry Notes
- Puts on green days, calls on red days (root CLAUDE.md rule)
- Roll duration, don't trim size (duration uncertainty ≠ thesis broken). Cut size only when thesis is broken (e.g., HY OAS <260 sustained for credit-thesis positions).
- Credit tightening = tactical, not structural. Don't close positions on 10bps of tightening.
- **Active channel can migrate.** If one leg of the thesis dies (SOFR-IORB plumbing, Apr 16 → resolved 5/18), check the others before exiting the whole book. Duration channel reignited as the bear thesis migrated out of plumbing.
- **Gamma-suppression caveat:** an OAS print that looks too calm during loud substance prints may be tape, not signal. Watch for gamma unwind.
