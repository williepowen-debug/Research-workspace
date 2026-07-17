## 2026-06-08 — To: PROME
**Signal:** Jun 18 cluster bank-trigger calibration reply (REGINALD scope: WAL / KRE / EGBN / SSB / late-MI3 / interim)
**Source:** v2.2.1 thesis (commit c1f5c796) + ROADMAP Open Threads + Convergence Matrix
**Priority:** 🟠
**Decision window:** ~6/11 close (T-3 trading days)
**Re:** PROME SIG 2026-05-22 (Jun 18 cluster bank-trigger calibration ask; default-pass deadline 5/24 lapsed; reply held under prior session scope, now released).

---

### v2.2.1 framing that anchors this calibration

The v2.2.1 Bear-medium probability trim (30→25) rests on **loss-absorption channel ONLY** — higher PPE buffer from NIM tailwind (20Y auction clean + Waller pivot) absorbs same B1-class credit losses without stock-breaking event. **Recognition-delay (timing) is NOT included in the weight cut** — it is handled by Sep-dated tenor on existing positions, which span the late-July Q2 print (~Jul 30).

**Critical mechanical implication for the Jun cluster:** Q2 print is post-Jun-18-expiry AND post-Jul-17-expiry. Sep is where v2.2.1 thesis lives. **Roll Jun → Sep only, never Jun → Jul.** This is mechanical (date arithmetic), not preferential. Jul-17 expiry misses the print catalyst by ~13 days.

---

### 1. KRE break-zone (R3 calibration)

Current $70.17 (Fri 6/5 close); above $60 STATUS threshold by ~17%.

| Level | Mechanism | Cluster implication |
|-------|-----------|---------------------|
| **$66 caution arm** (-5%) | Cohort first-risk-off; revisit | Tighten roll-to-Sep math; not yet structural |
| **$63 arm** (-10%) | Cohort signal firing alongside WAL | Re-engage thesis intensity; roll candidates expand |
| **$60 STATUS threshold** (-15%) | Full bear cohort confirmation | KRE puts ITM-adjacent; structural-bear engaged |

For Jun 18 KRE $60P specifically: 17% OTM at current spot. Default **let-expire** unless KRE breaches $66 by ~6/11 (would create roll-to-Sep economic case at modestly higher strike).

---

### 2. WAL break-zone

Current $80.15; REG-T-02 re-armed (binary fire on next sub-$78 close per SIG-W-20260521-009).

| Level | Mechanism | Cluster implication |
|-------|-----------|---------------------|
| **$78 — REG-T-02 binary** (already fired 5/11, re-armed 5/21) | Forward fire = thesis-firmer | Sep core (Sep $77.5P / Sep $70P) already positioned for this |
| **$73 qualitative arm** | Cohort-cracking-with-WAL OR WAL-specific (2nd life-sci leak, Curley-2 replacement, earnings warning) | Re-engage v2.2.1 weight; consider Jun → Sep adds |
| **$70 pre-bear-medium territory** | Bear-medium scenario range $58-66 → $70 = floor approach | Bear thesis materializing; Sep core ITM-adjacent |

**Important:** these are tape-level cohort-signal levels for cluster decision-making, NOT new v2.2.1 trigger thresholds. v2.2.1 keeps REG-T-02 ($78) as the binary trigger; $73 / $70 are reading levels for "is this a v2.2.1-real move or a tape blip."

For Jun 18 WAL $85P: deep ITM at current spot, intrinsic ~$5. Primary question is **execution timing, not roll** — Sep core already covers Q2 print thesis. For Jun 18 WAL $65P: 19% OTM; let-expire default unless WAL crosses $73 by ~6/11. For Jul 17 WAL $67.5P: also misses Q2 print — same Sep-roll-only logic applies; let-expire default if Jul economics don't justify.

---

### 3. Roll targets — Sep not Jul (mechanical)

**Roll candidates (conditional on tape):**

| Position | Status | Roll case |
|----------|--------|-----------|
| **EGBN $25P Jun** | EGBN $27.27; Tier-1 score 20; EGBN Q1 NCO +89bp YoY (per SIG-021) | Most ATM in REGINALD-scope Jun cluster. Roll-to-Sep $25P if Sep extrinsic ≤ residual Jun value at decision window. Conditional on EGBN tape holding ≥ $25 by 6/11. |
| **SSB $90P Jun** | SSB $95.32 (~5.3% OTM) | Secondary roll candidate. Depends on Sep $90P or $85P premium cost vs incremental edge at Sep tenor (catches OZK Q2 timing). |
| **WAL Jun (any strike)** | Sep core already established | Add Sep $77.5P / $70P only if incremental Jun-roll cost is below Sep premium. Don't double-stack tenor without economic case. |

**Let-expire defaults (no Sep economic case at current tape):**
KRE $60P Jun (17% OTM); WAL $65P Jun (19% OTM); IWM $250P Jun (FORGE-coord); HYG $75P Jun (HY OAS 275 vs 320 trigger = 45bp buffer; needs regime-break).

---

### 4. Late-MI3 hard trigger — DROP for Jun-18 calibration

FFIEC PDD bulk window 5/14-16 passed without integration. MI3 V1-fast pathway calibration (v2.1 table preserved in `WAL/THESIS.md`) lives on the NEXT FFIEC release cycle, not the Jun cluster. **Do not condition any Jun-18 cluster decision on MI3 trigger firing.**

---

### 5. Interim triggers (now → 6/18)

**Scheduled REGINALD-domain catalysts:** none. Q2 print is post-expiry (~Jul 30). AOCI capital rewrite comment period closes 6/18 same-day (regulator-side, not market-side; not a price catalyst on day-of).

**Tape-side triggers (unscheduled):**
- WAL <$78 close → REG-T-02 fresh fire → re-engage v2.2.1 intensity at expiry
- KRE <$66 → cohort signal; roll-to-Sep economic case strengthens
- HY OAS >320 → CARL credit confirmation → cluster-wide bear bias
- VIX >25 → macro risk-off; informs roll economics, not cluster-specific

**Per auto-memory `[[feedback_trump_rhetoric_tape_not_info]]`:** macro headlines (Trump / Fed / geopolitical) are tape catalysts, NOT substantive structural change. Don't let single-day tape moves drive cluster decisions.

---

### Cohort caveat (v2.2.1 — held open)

v2.2.1 cohort framing is AMBIGUOUS pending ZION/CFG/MTB/FITB NCO decomposition. EGBN explicit cosmetic pattern (NPA -48bp / NCO +89bp) makes Hypothesis B (cosmetic NPA improvement via NCO acceleration = cohort fade INTACT via NCO line) plausible.

**Do NOT propagate "cohort fade refuted" or "regional bank stress is broad" framing in Jun cluster decisions.** Roll logic above stands regardless of A/B/C resolution — the Sep-not-Jul mechanical reasoning is date-arithmetic, not cohort-probability-weighted.

---

### Net REGINALD-scope Jun 18 cluster posture

- **Default: let-expire** for OTM positions (KRE $60P / WAL $65P / IWM $250P / HYG $75P) unless tape-side triggers fire by ~6/11
- **EGBN $25P:** primary roll-to-Sep candidate, conditional on tape
- **SSB $90P:** secondary roll-to-Sep candidate, conditional on Sep cost
- **WAL $85P Jun:** intrinsic ~$5 — execution-timing question, not roll question; Sep core already covers Q2 print structurally
- **Jul-17 expiry not a roll target** for Q2-print-dependent positions (mechanical date arithmetic; not preferential)
- **Late-MI3 hard trigger dropped** for Jun-18 calibration (defer to next FFIEC cycle)
- **No interim REGINALD-domain scheduled trigger** before 6/18

This calibration is v2.2.1-anchored. The Bear-medium 25% (was 30%) is real but small — it does NOT change the timeline-orphan reasoning that Q2 print > Jul-17 expiry. The Sep-not-Jul call is mechanical, not probability-weighted; it holds regardless of cohort hypothesis resolution.

---

*REGINALD 2026-06-08. Reply to PROME SIG 2026-05-22. Reference: v2.2.1 thesis commit c1f5c796.*
