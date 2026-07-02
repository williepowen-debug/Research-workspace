# VIOLET — NEXUS Brief

**As of:** 2026-07-01 ~23:00 ET — post-close boot after 5-market-day gap (6/24-6/30 dark); reconstructed via 5-thread web workflow + own pulls (yf closes, FRED daily path, official CBOE SKEW closes, COT). | **STATUS commit:** 384ff7f0 (7/1 close basis).

**Status:** 🟠 v3.6 — **THE DIVERGENCE IS THE STORY: VIX 16.59 / SKEW 154.82 / credit tree in first-ever BIN-A.** The 6/23 Path-B partial-fire did NOT resolve — it chopped and **broadened** (narrative inverted capex-slowdown→capex-flood→antitrust/demand-destruction; MU round-tripped a +15.7% earnings pop to BELOW its 6/23 panic close; window SOX −8.8% vs SPX +0.1%, VIX DOWN). The **KB-VIO-090 credit tree fired BIN-A in the gap** (cross 6/23 → escalator 9.68 + dispersion 8.01 on 6/25 → CCC stuck 9.70 / disp new-high 8.06 on 6/30) — though **DISH DBS's prepack Ch11 (6/30, largest-CCC-structure class) is a direct idiosyncratic contributor**; LIQUID breadth is the registered discriminator (SIG sent). **SKEW ramped +15.4pts in 3 sessions to 154.82** (top-decile, cycle-2nd-highest) while equity P/C collapsed 0.85→0.64: hedge flow rotated ATM→far-OTM crash wings, which **mechanically suppresses headline VIX** — the 16.59 print is partly hedge structure, not calm (KB-VIO-108). Macro re-hawked into 7/1 (Warsh Sintra, ~70% Sep-hike odds, 10Y +14bp/2d, **yen 40-yr low, zero haven bid through the Asia stress window**). Formal DIET/STRICT NOT fired (VVIX flat = binding leg) — monitored, not L1-sized. Matrix 23/45 (verified): external vectors at floor ⚪, internal vectors at cycle highs (credit 🔴🔴, SKEW 🔴, Path-B 🔴). No position.

**Domain:** VIX / vol term structure / SKEW / VVIX / credit-to-vol transmission timing; broadcasts vol-regime to HENRY/LIQUID/RED; receives from BROCK/HENRY/HAWK/LIQUID/SAM/BRENT.
**Thesis version:** v3.6 (bumped 7/1 — tail rotation + Fed-HIKE formalized; first Bin-A; wings-rotation suppression. CHANGELOG has the full old→new).
**Recent thesis pivot:** 7/1 — credit tree Bin-A makes the Path-A re-activation question LIVE (hawkish-Fed-cracks-the-tail now has supporting tape, pending DISH decomposition); all short-vol/fade entries structurally dead while Bin-A stands.

---

## VIEW

- **The tape is one big divergence.** Spot vol at complacency prices (VIX 16.59, ~1.7% below SPX ATH), tail insurance at top-decile prices (SKEW 154.82 fresh — >146.7 AND faster-than-mechanical), credit tail stuck wide into a hawkish Fed (CCC 9.70/disp 8.06 new high while BB/HY retraced). Under KB-VIO-036 this is fragility being PRICED beneath an absorbing surface.
- **The absorption regime survived its hardest test** — a broadening multi-cause semis unwind (two −10% single-name days in one week) + a hawkish whipsaw = index flat, VIX lower. Offshore the same unwind REALIZED: KOSPI circuit-breakers ×2 in one week (KRX first), standing ~$9B 2x-single-stock-ETF mechanical amplifier with only jawboning as policy response, Taiwan record margin defaults. The un-indexed sector chop is distribution-shaped, not resolution-shaped.
- **Bin-A honest read:** mechanical verdict stands per pre-registration (no post-hoc softening), but the composition evidence is strong — DISH prepack (pay-in-full, >88% support) + IG rallied + bond funds took INFLOWS + strategist texture "concentrated in higher-beta." Two decisive upgrades pending: CCC persistence on post-DISH prints (7/2-3) and LIQUID mover-breadth.
- **Invalidation lines:** counter 0/5 (VIX <<23) · VIX3M/VIX 1.155 (inversion dormant) · R12 intact and strengthening (20d-avg 144.08, +4.08).

---

## CALIBRATION

- **Conviction (decomposed):** direction-MEDIUM-HIGH for the long-vol/tail branch (the divergence configuration is cycle-sharpest and now has a measured suppression mechanism under the VIX print) · timing-LOW (trigger still external/unscheduled; nearest dated = jobs ~7/2) · level-MEDIUM. Short-vol/fade branch: structurally DEAD while Bin-A stands (not a judgment call — registered).
- **Diverge from market by:** the crowd reads VIX 16.59 + record quarter as all-clear; VIOLET reads the SAME print as partly hedge-structure artifact (wings rotation, KB-VIO-108) with tail demand at top-decile and credit not confirming the calm. Burry's 6/30 short disclosure and the Benzinga "strange disconnect" coverage say parts of the market see it too.
- **Calibration discipline this session:** formal trigger status MEASURED not narrated (DIET/STRICT unfired — VVIX binding leg; the 3-session visual is not the 20-td formal window) · pre-registered tree verdict NOT softened despite strong composition evidence (refinement candidate logged for next calibration pass instead) · own 6/23 trigger attribution CORRECTED by the reconstruction (KB-VIO-105 → CORRECTED; framing-precision class) · fade adjudicated FALSIFIED even though its directional call paid (the asymmetry is the design).
- **Cross-agent tensions:** **One live:** VIOLET's Bin-A mechanical verdict vs the workflow-sourced composition read (DISH-led) — resolution assigned to LIQUID breadth per pre-registration; VIOLET holds the mechanical verdict until then. (HENRY flip-level remains an input GAP, not a disagreement.)

---

## CROSS-DOMAIN

**SENDING:**

| To | Signal | Priority | Mechanism it triggers in recipient's domain |
|----|--------|----------|---------------------------------------------|
| **LIQUID** | **Bin-A fired (KB-VIO-107); your mover-breadth is now DECISIVE** — idiosyncratic (DISH-led) vs breadth decides Path-A re-activation. Full packet: `outbox/2026-07-01_SIG-VIO-BINA_...md`. | 🔴 | Breadth answer adjudicates the registered abandon condition (KB-VIO-098); also your own CCC-complex read gains the DISH-decomposition datum. |
| HENRY / RED / NEXUS | **Wings-rotation VIX suppression (KB-VIO-108):** P/C 0.85→0.64 while SKEW +15.4 — headline VIX is partly hedge structure. Treat sub-17 VIX prints as suppressed, not calm, when reading market stress. | 🟠 | HENRY: pairs with your GEX-suppression mechanics — flow-level sibling; the index-absorption of an −8.8% SOX week is your domain's datum. RED: adversarial check on the "suppressed not calm" read. |
| SAM | **Zero haven bid through an Asia stress window** — yen 40-yr low (~162), JGB 2.67% cycle high, while KOSPI hit CBs twice. Does the 162 print + hawkish-Fed repricing move your 60d unwind %? [KB-VIO-109] | 🟠 | Carry channel stretched under your Sep-18 convexity-tail frame; the "next stress lands with no shock absorber" input is yours to weigh. |
| PROME | VIX COT alert band delivered per 6/30 ask: `VIX_LEV_NET_BAND = (-75_000, 0)` — both lines empirically ~p5-p7 tails. File: `outbox/2026-07-01_to-PROME_...md`. | 🟡 | Activates the RESEARCH-INTAKE CFTC feed alert layer. |

**WAITING FOR:**

| From | Input | Expected by | Why it matters | How it changes my view |
|------|-------|-------------|----------------|------------------------|
| **LIQUID** | **CCC mover-breadth 6/23-6/30** (KB-VIO-098 discriminator) | ASAP — decision-blocking on a fired tree | Only registered adjudicator of Bin-A meaning | Idiosyncratic → composition-artifact, tree refinement proceeds, Path-A back to dormant; breadth → Path-A re-activating under Fed-HIKE = hedge flag escalates to packet. |
| **HENRY** | Dealer-gamma FLIP LEVEL + GEX re-confirm | Open since 6/9 | The Path-B release trigger VIOLET can't self-compute | Flip proximity sizes the release risk; sizing stays L1-based until it lands. |
| HAWK | Post-6/29 Iran read (formal de-escalation) | rolling | Confirms the oil-vol channel stays closed | Re-escalation would re-open + amplify. |

---

## NEXT DECISION POINT

- **What:** **Tail-hedge gate ARMED — Will approved 7/1 (KB-VIO-110).** Packet-build fires on any of: Gate A post-DISH CCC persistence (7/2 print ≥9.65 / disp ≥8.00) · Gate B jobs shock (7/2 8:30 ET, hawkish + tape confirms) · Gate C LIQUID breadth. Build = same-session, spec pre-registered (VIX calls 30-60 DTE — the VVIX-suppressed leg, NOT the SKEW-rich wings; 1% starter); execution still Will-[Approve]. Stand-down if all three benign; re-arm on SKEW 4td sustain / DIET fire / new Bin-A condition.
- **When:** June jobs ~7/2 (verify timing; 7/3 = observed holiday, short week) · post-DISH prints 7/2-3 · VIX exp 7/15 · FOMC 7/29.
- **What would re-engage short-vol:** nothing while Bin-A stands (registered). Bin-A state exits only via the tree's own lines (CCC back <9.55, or a written re-mark after a clean +5td re-check with LIQUID breadth confirming idiosyncratic).

---

## FORWARD CATALYSTS (next 2-6 weeks)

| Date | Event | Threshold / Signal |
|------|-------|---------------------|
| 🔴 ~Jul 2 | June employment report (verify timing) | NFP-class print (the 6/5 trigger class) into the divergence configuration |
| 🔴 Jul 2-3 | Post-DISH CCC prints | Persistence = Bin-A upgrade; retrace = composition confirmation |
| 🟡 ~Jul 10 | SK Hynix ADR Nasdaq listing (verify) | Semis capital-rotation |
| ⚪ Jul 15 | VIX July expiration + Q2 earnings season opens | Standard monthly; concentration = the earnings-gap tail |
| 🟠 Jul 29 | FOMC (no SEP, Warsh) | Hike optionality live post-Sintra |
| 🟠 Sep 16 | FOMC + SEP + VIX Sep quarterly expiry | ~1 hike priced by Sep |

**Dominant near-term tail remains the Path-B unwind (unscheduled)** — now with dated amplification checkpoints above and a standing offshore mechanical amplifier (KOSPI 2x-ETFs; watch the 8,200 line).

---

*Brief format follows the NEXUS_BRIEF schema (R3 + amendment 7). VIOLET is a MEDIUM cross-domain agent. Updated at every closeout. This refresh: 5-market-day gap reconstruction — Bin-A first fire + DISH decomposition tension (LIQUID decisive), SKEW 154.82 wings-rotation suppression, unwind broadened un-indexed, thesis → v3.6, Reversion Fade falsified per registration, hedge flag strengthened (Will-gated).*
