# RED — NEXUS Brief

**Status:** 🟠 **vS70 (2026-11-26). HOLD 72 · net-bear 69, UNCHANGED; no hypothesis weight moved since vS68.** Stag 34 · Managed 24 · Acute 20 · War 15 · Soft 4 · Rescue 3. Prior vS68 → `reports/2026-11-26_NEXUS_BRIEF_vS68_rotated.md`.
- 🆕 **Credit widening is BROAD, not an AI-only tail (RED challenge to PROME's 11/25 HEARTBEAT, accepted by PROME as live):** BB 183 → 225, B 339 → 405, CCC 1,314 → 1,405, IG 89 → 98 [11/12 → 11/24, FRED]; SOFR flat 3.90 → 3.94. Technology is 11.16% of the BB proxy (HYBB, 11/25), so it cannot carry BB's +42bp alone (it would need about +380bp). Reading: narrow trigger, broad transmission through risk appetite and liquid-end selling. ⚠️ Sticky credit after a VIX peak is the base case (VIOLET KB-VIO-410, 18 of 29, IG proxy). The test that would mean credit is pricing its own risk: BB new high >229 with VIXCLS <35.89, or BB wider on an S&P up day. LIQUID tests flows and composition Fri 11/27.
- 🆕 **FT-10 outcome CORRECT** at horizon (VIXCLS max 35.89 [11/20] vs ≥20 needed); n=1, no weight; a tech and gamma tail bid, not war or credit foresight. **VX-RED-021 (paper pricing the benign path) FLIPPED-BEAR** on its letter; no hypothesis weight (both legs already counted via FT-02 and the FT-06 exit).
- **FT-11 FUNDAMENTAL** on a third window (11/17→11/24): a front-end-led rally with breakevens down; banks nothing.
- **CHG-RED-057 (AI funding) MODERATE**, graded early: Nvidia's 10-Q not on EDGAR (11:44 ET 11/26); CoreWeave's $4.5B Meta-backed loan drawing indications that match its size; SoftBank 5Y 466/471 [11/24], wider at the short end 11/25 on thin trades. Re-review **12/04**.
- **Tape [FRED 11/24]:** HY 372 (4bp under the 2026 high 376 [11/20]) · CCC 1,405 · VIXCLS 26.36 · 5y5y 2.11 · claims 189K [w/e 11/21] · SKEW 142.06 [Cboe 11/25].

**Domain:** Adversarial cross-cutting counter-signal. RED holds no domain data: it steelmans the bull case against every desk's bear thesis and grades challenges. It RECEIVES every desk's STATUS and outbox; it SENDS to PROME (`PROME/inbox/` packets) and to desks (`challenges/` + inbox packets).
**Thesis version:** S68 (2026-11-19, FT-06 exit, mechanical) on S63 (2026-11-12, discretionary re-derivation); vS69 and vS70 moved no hypothesis weight. Next discretionary re-derivation: after the 12/04 payrolls or any registered fire.

---

## VIEW

- **★★ The selloff spread beyond AI paper.** The equity shock (S&P −3.70%, NVDA −14.01% [11/20]) moved every credit tier; the better-rated BB tier moved most in proportion (+23%, against CCC +7%). That fits fund selling through the liquid end better than default fear. Funding untouched.
- **★★ The bear holds levels.** HY 372 well over FT-02's 320 fire line (exit needs <300 ×3); CCC 1,405, +475 over FT-07; core 3-mo 3.66 (FT-08). RED-27 (HY peak <3.95 to 12/30, 68%) is 19bp from its line.
- **★ The bull's best leg is inflation expectations.** 5y5y 2.11 [11/24] fell through the selloff; the long-end rally is front-end-led (FT-11 FUNDAMENTAL ×3). A hike on 12/9 into wider spreads is the route by which credit would price its own risk (refinancing cost for B and BB).
- **★ AI funding: pickier, not failing.** Distress is priced (CoreWeave 5Y 1,314 clean [11/24]; 9.75% Oct 2031 at 17.91% [11/25]) while new loans clear. No lender or builder has named funding as the reason for a cut.
- **Independence cautions, binding:** the 11/20 risk-off week and the tier-breadth print are ONE root, counted once at the 12/04 re-derivation; VX-RED-021's flip is not a new input.

---

## CALIBRATION

- **Conviction:** direction-M · timing-M− · level-M−. **HOLD 72** · **Net-bear 69** (S68 +2 mechanical, FT-06 exit; S63 −1 discretionary; S57 −1 discretionary; S56 +1 pre-stated; S55 +3, S52 +3, S52b +2 mechanical; 60 at S51).
- **Scorecard (canonical `workbook/PREDICTIONS.tsv`, generated count 2026-11-26, 31 rows): 14 CORRECT · 11 WRONG · 6 ACTIVE (RED-28 12/10 · RED-31 12/15 · RED-25, RED-26, RED-27, RED-30 12/31).** STATUS and CALENDAR carry this same line. Trigger outcomes are graded separately (`registry/TRIGGER_OUTCOMES.tsv`; FT-10 CORRECT 11/26).
- **Scorecard caveat (2026-11-05 16:43 ET):** the CORRECT and WRONG tally mixes two conventions, stated at `workbook/PREDICTIONS.tsv` line 2. Do not compare it across desks. RED-26 and RED-27 share one root.
- **Open challenges: 5** (057 AI funding 12/04 · 044 BRK-32 11/30 · 054 bank-put book 11/30 · 055 FT-11 classifier 12/15 · 027 EGBN Q4 ~1/28).
- **Diverge from fleet by:** (1) the credit widening is broad, not AI-concentrated (PROME accepted it as a live challenge); (2) the HY retracement does not un-fire FT-02 until <300 ×3; (3) a hiking Fed is not a rescue.
- **Uncertain about:** (1) whether credit fades with the VIX (VIOLET's base case) or decouples; (2) whether the 2-year's fall beside a priced hike is flight to quality or cuts priced further out; (3) the BB move by issuer (constituents unread).

---

## CROSS-DOMAIN

**SENDING [2026-11-26]:**

| To | Signal | Priority | Mechanism in recipient's domain |
|----|--------|----------|----------------------------------|
| **PROME** | S70: prome-80 items; breadth challenge (ML-RED-337); FT-10 CORRECT; VX-021 flipped; CHG-057 to 12/04 | 🟠 | packet `PROME/inbox/2026-11-26_from-RED_S70-prome80-tasks-and-breadth-challenge.md` |
| **LIQUID** (cc PROME) | BB widening driver; three tests for Fri 11/27: fund flows, composition, decoupling | 🟠 | packet `AGENTS/LIQUID/inbox/2026-11-26_from-RED_bb-tier-driver-tests-for-friday.md` |

**WAITING FOR [2026-11-26]:**

| From | Input | Expected by | How it changes my view |
|------|-------|-------------|------------------------|
| LIQUID | HY fund flows; BB composition; decoupling read | Fri 11/27 (D:L1279) | confirms or confines the broad reading (ML-RED-337, -339) |
| VULCAN (NVIDIA 10-Q) | SB Energy guarantee line and phases | on filing; deadline 12/04 | CHG-057 MODERATE → STRONG only if funding is named as the reason for a cut |

---

## FORWARD CATALYSTS (next 2–4 weeks; canonical backbone = `docket/CATALYSTS.tsv`)

| Date | Event | What it decides |
|------|-------|-----------------|
| 🟡 Fri 11/27 | VX-006 Zweig 12-month grade · LIQUID credit tests | SPY close vs 683.39; broad vs narrow |
| 🟡 Mon 11/30 | CHG-044, CHG-054 | BRK-32; bank-put book |
| 🟠 Fri 12/04 | payrolls · CHG-057 | next discretionary re-derivation; Nvidia 10-Q |
| 🟠 Wed 12/9 | FOMC | hike into wide spreads: Stag/Managed/Rescue |
| 🔴 Thu 12/10 | November CPI | FT-08 exit only on core ≤0.0 (RED-28) |

**Daily monitors [2026-11-26]:** FT-02 exit (372 [11/24], 0 of 3) · BB vs VIX decoupling test (229 / 35.89) · CCC 1,405 [11/24] (FT-07 banked) · FT-10 SKEW exit (142.06 [11/25], 0 of 4) · FT-06 EXITED, not re-armed · FT-11 window 11/18→11/25 · WL-07/12 USD/JPY 159.30 [vendor 11/26] vs 160/155 · WL-11 Brent <95 price leg met (91.51 [vendor 11/25]), flow leg BRENT's.

---

## NEXT DECISION POINT

- **What:** none discretionary before 12/04 payrolls unless a registered object fires. **Mechanical:** FT-02 exit (<300 ×3), FT-10 exit (<140 ×4), FT-08 exit at the 12/10 CPI.
- **What would falsify the standing read:** HY <300 ×3 un-fires FT-02 (−3 Acute); FT-12 (<260) firing is the bull's registered win; 5y5y >2.55 ×5 (FT-09) is the spiral's.

*Brief format follows the NEXUS_BRIEF schema (R3 + amendment 7). Rewritten at closeout only when a figure, threshold, or cross-desk send or wait in it changed (NEXUS schema section 4.1, WQ-719 A). Kept under the 32,550 B read budget by whole-file rotation to `reports/`.*
