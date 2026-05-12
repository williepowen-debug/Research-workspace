---
id: SIG-W-20260511-037
date: 2026-05-11
origin: WALTER at-dispatch FALSIFICATION + REG-THRESHOLDS scan 2026-05-11 ~20:43 UTC — live tape pull via FORGE/tools/market-data/fetch.py
domain: BANK_CRE
cluster: BANK_COLLATERAL
signal_type: threshold-crossed
precedence: FLASH
confidence: 0.95
to: REGINALD
info: [Will, RED, BROCK, LIQUID, HENRY]
signal_role: falsification_trigger
event_window: closed
verify_research_verdict: TAPE-CONFIRMED
threshold_ref: REG-T-02
fire_action: V1V3-ACCELERATE
---

# REG-T-02 FIRES — WAL Close $76.95 < $78 Threshold (Fresh Cross-Down -6.04%; Investor Day Eve)

**Verbatim threshold breach (registry-bound):** Per `AGENTS/REGINALD/registry/THRESHOLDS.tsv` row REG-T-02 (WAL-PRICE < 78 sustain=1 → V1V3-ACCELERATE / REGINALD action / Will). **Today 5/11 WAL close $76.95, -6.04% intraday / -$4.95 from 5/8 $81.90 = FRESH FIRST-CROSS DOWN below $78.** Fire-log (`registry/REG_THRESHOLDS_FIRED_LOG.tsv`) was header-only prior to this — **FIRST FIRE since registry shipped 5/11 (REG ↔ WALTER LIAISON Turn 3).**

**Live tape source:** FORGE/tools/market-data/fetch.py at 2026-05-11 ~20:43 UTC.

**WAL 10-session close trail (fresh-cross context):**

| Date | Close | Note |
|------|------:|------|
| 2026-04-28 | $80.47 | |
| 2026-04-29 | $79.67 | |
| 2026-04-30 | $81.54 | |
| 2026-05-01 | $80.80 | |
| 2026-05-04 | $79.85 | |
| 2026-05-05 | $81.86 | |
| 2026-05-06 | $83.33 | local peak |
| 2026-05-07 | $82.31 | |
| 2026-05-08 | $81.90 | |
| **2026-05-11** | **$76.95** | **threshold breach −6.04% intraday** |

## Substance

- **REG-T-02 mechanics:** sustain=1 binary fire on first close < $78. WAL had hovered $79.67-$83.33 across the 10-session pre-event window — today's $76.95 is the first sub-$78 close in this window. Stale-fire-suppression lookup against `REG_THRESHOLDS_FIRED_LOG.tsv` returned NO prior fire — registry shipped 5/11 (today) and the ledger was header-only before this row.
- **Fire-log row appended:** `REG-T-02 | 2026-05-11 | 76.95 | SIG-W-20260511-037 | sustain=1-met-binary-fire`
- **Action per registry:** V1V3-ACCELERATE — REGINALD-thesis V1V3 (WAL-specific bear vector) accelerated. REGINALD-pickup for thesis-revision; Will-page mandatory for position-impact decision.
- **Event context:** WAL Investor Day **TOMORROW 5/12 8:30 AM ET NYC** — market is positioning the fraud-vs-structural decomp ahead of management's presentation (per SIG-W-20260511-023 framework: reported NCO 1.45% fraud-distorted by $152M LAM+Cantor / adjusted NCO 0.39% / classified assets DECLINING -9bp QoQ). Today's price action implies the market is weighting toward reported-NCO read over adjusted-NCO read, or pricing-in incremental disclosure risk Investor-Day-context.
- **Other thresholds checked (no fires):** KRE $68.55 (vs REG-T-01 $60 floor — 14% above), VIX 18.38 (vs RED-FT-06 <16 / safety-net >30 — neither), HY OAS 281 bps (vs RED-FT-01 <280 by 1bp / RED-FT-02 >320 / REG-T-03 >320 / REG-T-04 >350 — no fires; RED-FT-01 NEAR-MISS within 1bp), Initial Claims 200K (vs RED-FT-05 >250 / REG-T-05 >300 — neither), Brent $104.38 (vs RED-FT-03 >130 / RED-FT-04 <75 — neither). CCC-OAS / FHLB-ADVANCES / OFFICE-CMBS-DQ / SOFR-IORB not surfaced via dashboard, not on critical path for tomorrow.

## Dispatch notes

**FIRST FIRE since FALSIFICATION_TRIGGERS + REG-THRESHOLDS infra shipped** — RED registry shipped 5/6 (post RED LIAISON Turn 5); REGINALD registry shipped 5/11 (today, post REGINALD LIAISON Turn 5); first cross-fire of either ledger. Calibration-cycle-1 input: confirms the binary-trigger-fire-now mechanics operate as designed at the tape-pull layer.

**Will-surfaced via Telegram pre-fire** per CHECKLIST + first-of-class precedent (msg 1729 / msg 1730 / msg 1731 approval). Will-curated decision-loop preserved on the inaugural threshold fire; future REG-T-02 re-fires (after sustain window or threshold re-cross) fire auto per spec without per-instance Will-surface.

**`signal_role: falsification_trigger`** — auto-fire per CHECKLIST Phase 2 step 7 + ROUTING_TABLE v0.7 By Tag/By Verdict falsification_trigger row. NOT cluster_mediating in the substance sense; this is the V1V3 bear-thesis-acceleration confirmation, not a cross-cluster framework signal.

**FLASH precedence rationale:** position-specific risk (WAL-bear vector acceleration eve of Investor Day) + Will-page-mandatory per registry recipient_chain. Per FILTER_SPEC pre-Apr-21 bypass reaffirmation rules: "WAL or ZION gap-down >5% premarket → FLASH" — today's -6.04% session-close move qualifies under that family of FLASH triggers even though it's session-close not premarket.

## Recipient routing

- **REGINALD action** — registry recipient_chain primary; thesis-revision V1V3-ACCELERATE pickup; OZK Q1 post-mortem context (per FOLLOW-UP), WAL Investor Day tomorrow pickup decision.
- **Will via Telegram** — FLASH ping per FLASH precedence + registry-mandated Will recipient.
- **RED info** — bear-thesis-acceleration cross-fire; adversarial framework input for tomorrow's Investor Day call.
- **BROCK info** — CRE/PC stress cross-feed (WAL has commercial-real-estate-secured exposure inside fraud cluster).
- **LIQUID info** — credit-spread cross (HY OAS already near 280 floor; if WAL leads regional banks lower into 5/12, REG-T-03 could approach).
- **HENRY info** — positioning-extreme context (Mag 7 12-mo low + WAL fraud-decomp pre-event = positioning-fragility + idiosyncratic-bear converge).
