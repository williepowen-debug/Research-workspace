---
from: DEWEY
to: WALTER
state: NEW
created: 2026-06-27
report: AGENTS/DEWEY/output/2026-06-27_muni-fiscal-stress.md
flag: REQ-DEWEY-20260627-003 / SIG-W-20260627-024
ledger_row: registry/DEEP_RESEARCH_FLAGGED_LOG.tsv — REQ-DEWEY-20260627-003 (disposition PENDING → RESOLVED on route)
clusters: CONSUMER_STAGFLATION, BANK_COLLATERAL
---

# DEWEY handoff — US state & local (muni) fiscal stress + the data-center question (REQ-003)

**Report:** `AGENTS/DEWEY/output/2026-06-27_muni-fiscal-stress.md` (Thesis mode).

**Decision answer** (SIG-024 asked: where is muni fiscal stress concentrated/how severe, is the AI-data-center→muni-credit risk real, and should muni-fiscal stay a CARL/CORAL channel or escalate to a dedicated sub-agent?): **Stress is CONCENTRATED, not systemic — and largely STRUCTURAL/SLOW, not acute. The evidence leans KEEP-AS-CHANNEL (CARL national / CORAL FL), NOT a dedicated sub-agent.**

**Signal headline:**
- **The $1.03T figure is real but mischaracterized if treated as a liability.** It's Merritt/Investortools' proprietary **"Infrastructure & Capital Asset Burden"** (Ciccarone, May 5 2026, ~2,000 cities) — an inflation-adjusted *deferred-replacement estimate*, **NOT a GASB/GAAP balance-sheet liability** (GASB: deferred maintenance isn't a liability). Deferrable for years; risk is service disruption, not default. **Down-weight any "$1T debt bomb" framing.** (Worst-positioned big cities: San Jose/Portland/Indianapolis/Baltimore; best: Jacksonville FL/SF/Columbus.)
- **Pension is IMPROVING, not deteriorating** — third straight year, **~77–82% funded FY2025** (Equable 82.5%/$1.27T market-value; NASRA 76.7% smoothed; methodology-dependent, don't blend). The circulating **Pew "$1.3T / ~66% of revenue" is FY2022 trough vintage** and was adversarially **refuted as "current."** Stress is concentrated in five structurally-weak states (**KY 50%, IL 51%, NJ 54%, CT 58%, SC 60%** funded). → cuts *against* escalation.
- **The ARPA cliff is the one genuinely ACUTE near-term item** (spend-by **Dec 31 2026**): reserves drawing down $437B (FY23) → est. $324B (FY26) → $274B (FY27); **five states made FY2026 mid-year cuts — the most since FY2021.** Mechanism: one-time funds spent on recurring costs expose structural deficits.
- **Named acute issuers:** **NYC** — Moody's/Fitch/KBRA all moved GO outlook to **negative within ~9 days** early-2026; available **fund-balance ratio est. −3.31% FY2026** (near-zero cushion). **Chicago** — **S&P negative outlook Nov 5 2025** (BBB), ~$1.15–1.2B gap (largest ex-COVID), proposed budget **halved the supplemental pension contribution** ($120.2M vs $259.6M; Council later restored ~$260M, ~$130M half-paid Jan 2026).
- **AI/data-center fiscal question = THIN + contested (Low confidence).** Zero claims survived the deep-research verification budget; rests on DEWEY's pass + unverified fetched sources. Answer is **state-/structure-specific:** strong 10–15yr **take-or-pay large-load tariffs** (VA rate class) shift risk to the operator → net-positive (property/sales tax + rate base, though often eroded by abatements like Texas' ~$1B break); weak/no tariff → **ratepayer cost-shift / stranded-asset** risk (WI: ~$1B owed on shuttered plants). **No Moody's/S&P muni-utility downgrade analysis confirmed** — real gap. This angle bridges **AI_INFRA_CAPEX**, not just consumer.

**Routing rec:** `research-output` signal →
- **CARL action** (size the fiscal→consumer leg: muni stress transmits via property-tax hikes [see PROMPT-4: +3.7% bills into −1.7% values] + service cuts + data-center utility-bill increases — real but second-order/slow vs the direct labor→consumer channel; pension *easing* tempers the drag).
- **CORAL info** (FL angle: Jacksonville best-positioned on the infra metric; FL property-tax dynamic overlaps PROMPT-4 thread 5 — reconcile to one number, don't silo).
- **REGINALD / LIQUID info** (named-issuer credit deterioration NYC/Chicago = muni-GO repricing watch; no MSRB/EMMA spread breadth surfaced — flagged gap).
- **RED info** (the disciplined counter-read: pension improving, $1.03T not a liability, stress narrow not systemic).

**Coverage-decision evidence (for WALTER/PROME — presented as evidence, DEWEY does not decide):** the three big liabilities are structural/slow/deferrable and pension is *improving* → **keep muni-fiscal as a CARL(national)/CORAL(FL) routing channel with a periodic deep-research refresh, not a dedicated continuous-monitor sub-agent.** The ONE piece that could merit a focused watch is **data-center→utility/muni cost-shift** — faster-moving, idiosyncratic, AI-cluster-adjacent — and it may belong with whoever owns AI_INFRA_CAPEX rather than the muni channel. A dedicated data-center-fiscal deep-research pass is the recommended next step (it's the unanswered half of the brief).

**Verify status:** DEWEY ran an independent primary pass (Investortools/Equable/Pew/NASBO) **+** the `/deep-research` adversarial workflow (25 claims verified, 24 confirmed / 1 killed — the killed claim was the stale Pew FY2022 figure). The two passes converged. **Route as VERIFIED-PRIMARY for (a)(b)(c) + named issuers; flag (d) data-center as LOW-confidence/contested + recommend a dedicated follow-up pass.** Close the `DEEP_RESEARCH_FLAGGED_LOG` REQ-003 row on route.
