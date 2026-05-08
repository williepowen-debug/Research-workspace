---
signal_id: SIG-W-20260508-004
precedence: PRIORITY
timestamp: 2026-05-08T13:55:00Z
source: WALTER
origin: ["WALTER kill_log re-research follow-on (Will direction msg 1503 5/8 12:59 UTC + green-light msg 1507 5/8 13:48 UTC) — re-evaluation of 2026-04-20 FHA '180% of 2009' kill (CORRECTED-FRAMING 0.55) revealed underlying SDQ has been STABLE on distress-adjusted basis but headline rose materially due to Oct-2025 TPP rule-change reporting artifact", "WALTER verify-research sub-agent 2026-05-08 ~13:30 UTC (~$0.05) — verdict CONFIRMED 0.85 on the underlying data + the artifact mechanism", "Center for Responsible Lending (PRIMARY): https://www.responsiblelending.org/research-publication/policy-related-reporting-change-not-increasing-financial-distress-drove-late — 'Policy-Related Reporting Change, Not Increasing Financial Distress, Drove Late-2025 FHA Delinquency Rise'", "Mortgage Bankers Association Q4 2025 release (independent corroboration): https://www.mba.org/news-and-research/newsroom/news/2026/02/12/mortgage-delinquencies-increase-in-the-fourth-quarter-of-2025 — FHA total DQ 11.52%, SDQ +104bps QoQ to ~5.14%", "National Mortgage News context: https://www.nationalmortgagenews.com/news/seriously-delinquent-loans-hit-highest-level-since-2022 — overall mortgage DQ 3.72%, conventional/GSE ~1.8%"]

to: CARL (ACTION — Path C consumer-stretch framework load-bearing input; FHA SDQ is leading-indicator for low-income mortgage stress; downstream agents must read headline-vs-distress-adjusted distinction before treating any forward FHA print as Path C confirmation)
info: REGINALD (info — bank-collateral-compression cluster; FHA exposure mapping; same lesson family as MBA Q4 framing for bank credit transmission), BROCK (info — PC-stress cluster cross-reference; same methodology-noise risk for any FHA-derivative reading), RED (auto-cc per v0.7 CORRECTED-FRAMING tag — adversarial-overlay calibration cycle 1 input on framing-correction discipline), NEXUS (info — CONSUMER_STAGFLATION cluster classification + headline-vs-substance-adjusted axis)
group: THESIS_CORE
dispatched: 2026-05-08T13:55:00Z
dispatch_note: "Will-direction msg 1503 5/8 12:59 UTC ('Would any of these benefit from additional research?') → green-light msg 1507 5/8 13:48 UTC. WALTER kill_log re-research follow-on after Will-requested kill_log audit. **Original 2026-04-20 kill stands as correct** — '180% of 2009' was count-basis distortion (FHA portfolio ~1.65× larger; rate-basis ~1.08× of 2009; actual SDQ ~45% of 2009 peak); kill validated 18 days later. **NEW signal surfaced via re-research:** the Oct 2025 Trial Payment Plan (TPP) rule change is generating a methodology-noise gap between headline FHA SDQ (5.23% Jan 2026) and distress-adjusted SDQ (~3.70%, stable +13bps in 4 months). Headline rose +166bps Sep25→Jan26; **92% of that (153bps) is the TPP reporting artifact**, not credit deterioration. CRL primary + MBA Q4 release independent corroboration. Distress-adjusted '~39% of 2009 peak' on rate-basis (vs 9.4% peak) — **not approaching 2008-09**. **Why dispatch despite the kill being correct:** when CARL/REGINALD/RED read the next FHA SDQ headline coming weeks (a load-bearing leading-indicator for Path C consumer-stretch + bank-collateral), the 5.23% headline will look like credit deterioration. They could misread it as Path C 92→97% confirmation when it's actually methodology-noise. **Same lesson family as MEMORY 4/20 finding** ('% of 2009 / vs peak framings often portfolio-size artifacts not rate moves') + yesterday's SIG-W-20260507-002 (Fed G.19 Mar consumer credit beat NON-revolving-led, headline misleading at margin) + 5/7 SIG-004 Sternlicht (TRD 'just hit special servicing' framing misleading — transfer was Jan 2026, 4mo stale). Pattern: **headline reads stretched but methodology / composition / artifact distorts the read.** This is RED-side adversarial-overlay calibration cycle 1 input. **Re-verify trigger:** if FHA SDQ headline crosses 6.0% OR the distress-adjusted measure rises >25bps in any single month, re-open. RED auto-cc per v0.7 CORRECTED-FRAMING. **Cluster ToC update:** CONSUMER_STAGFLATION 20→21. Confidence 0.85 (CRL primary + MBA Q4 corroboration; high-quality institutional research source)."

signal_type: thesis-frame
confidence: 0.85
confidence_language: institutional-research-primary-corroborated
resources: 0
safety_net: clear

word_count: 312

cluster: CONSUMER_STAGFLATION
cluster_mediating: false
verify_verdict: CORRECTED-FRAMING 0.85 (headline-vs-distress-adjusted gap; 92% of headline rise is TPP reporting artifact)
---

## Signal

**FHA SDQ headline 5.23% Jan 2026 (+166bps from 3.57% Sep 2025) is 92% TPP-reporting-artifact, NOT credit deterioration. Distress-adjusted SDQ ~3.70%, stable +13bps in 4 months. Do not treat forward headline drift as Path C 92→97% confirmation.**

## Body

### The headline vs distress-adjusted gap

| Measure | Sep 2025 | Jan 2026 | Δ (4 months) |
|---------|----------|----------|--------------|
| Headline FHA SDQ | 3.57% | **5.23%** | **+166bps** |
| Distress-adjusted SDQ | 3.57% | ~3.70% | **+13bps** |
| Of which artifact | — | ~153bps | **92% of headline rise** |

**Source:** Center for Responsible Lending (May 2026), "Policy-Related Reporting Change, Not Increasing Financial Distress, Drove Late-2025 FHA Delinquency Rise."

### The mechanism (Trial Payment Plan / TPP rule)

In Oct 2025, FHA changed loan-modification reporting: TPP loans now require **3 consecutive on-time payments** before being reclassified back to "current." Previously the reclassification could happen sooner. Net effect: loans that ARE performing get held in days-delinquent classification longer → headline SDQ rises without underlying borrower-distress change.

**MBA Q4 2025 release (independent corroboration):** FHA total DQ 11.52%; SDQ rose 104bps QoQ to ~5.14%. Same artifact.

### Why this is dispatch-worthy despite the original kill being correct

The 4/20 kill on "FHA delinquencies 180% of 2009" was correct — that was a count-vs-rate distortion (180% on portfolio ~1.65× larger = rate-basis ~1.08×). The **18-day refresh validated the kill**. But it surfaced a NEW methodology-noise risk: forward FHA SDQ headlines will be inflated by TPP artifact through approximately mid-2026 as TPP-flagged loans roll off.

**Risk to network if not dispatched:** CARL Path C 92→97% direction confirming via WHR + KHC Q1 prints (per yesterday's SIG-W-20260508-001). Without the TPP-artifact context, an FHA SDQ headline at 5.5%+ in Apr/May 2026 reads as Path C 97%+ confirmation. With the context, the same headline reads as stable underlying + artifact unwinding pace.

### Cross-context (Q4 2025, MBA)

- Overall mortgage DQ: 3.72% (90+ DPD subset rose 3%)
- Conventional/GSE: ~1.8% — FHA-to-conventional gap is ~6.5× but pre-existing structural, not a new break
- 2009 FHA SDQ peak: ~9.4% (rate-basis) — distress-adjusted current ~3.70% = **~39% of 2009 peak**, not approaching it

### Routing rationale

- **CARL action** — Path C consumer-stretch framework load-bearing; FHA SDQ is direct leading-indicator for low-income mortgage stress component; without this signal, CARL risks misreading methodology-noise as Path C confirmation.
- **REGINALD info** — bank-collateral-compression cluster; FHA exposure mapping for KRE constituents; same headline-vs-substance distinction applies to MBA Q4 read on conventional too.
- **BROCK info** — PC-stress cluster has FHA-derivative collateral indirectly via MSR / mortgage-backed positions in BDC books.
- **RED auto-cc** per v0.7 CORRECTED-FRAMING tag.
- **NEXUS info** — cluster classification + the headline-vs-substance-adjusted axis itself is a recurring framing-correction pattern in CONSUMER_STAGFLATION.

### Pattern: headline-stretched-but-methodology-distorts cluster

Same lesson family as:
- **MEMORY 4/20 finding** — "% of 2009 / vs peak framings often portfolio-size artifacts not rate moves" (reference signal SIG-W-20260420-005-FHA-180pct-of-2009 killed CORRECTED-FRAMING)
- **SIG-W-20260507-002** (Fed G.19 Mar consumer credit) — beat NON-revolving-led at headline; revolving annual rate 0.3%→9.1% only at margin
- **SIG-W-20260507-004** (Sternlicht-Starwood) — TRD "just hit special servicing" framing misleading; transfer was Jan 2026, 4mo stale at press date

Pattern: **headline reads stretched but methodology / composition / artifact distorts the read.** Adversarial-overlay calibration cycle 1 input for RED.

### Re-verify trigger

- If FHA SDQ headline crosses **6.0%** → re-open (could be artifact-amplification OR could be real distress accelerating; need to distinguish)
- If distress-adjusted measure rises **>25bps in any single month** → re-open
- Otherwise scheduled re-check at next MBA quarterly release (Q1 2026 release ~mid-May)

## Cross-references

- **MEMORY [4/20] "% of 2009 / vs peak" finding** — durable framing-correction pattern; this signal is the second instance
- **kill_log 2026-04-20T21:30:00Z** (FHA "180% of 2009" Will Telegram msg 917) + **kill_log 2026-04-20T21:35:00Z** (jimmy dean / Melody Wright same data) — original kills validated by this re-research
- **SIG-W-20260507-002** (Fed G.19 Mar consumer credit CORRECTED-FRAMING 0.55) — same family methodology-noise lesson
- **SIG-W-20260507-004** (Sternlicht-Starwood Capital $265M K-Star CMBS) — same family stale-framing lesson
- **SIG-W-20260508-001** (Nightingale 3-CEO consumer-stretch synthesis) — Path C trigger; this signal de-risks downstream FHA SDQ readings against false-positive Path C confirmation
- **SIG-W-20260424-007** (NY Fed CC 90+ delinq 12.7% approaching 2009 peak) — adjacent consumer-credit indicator; CC delinq is rate-basis, more directly comparable to 2009 than FHA which has the portfolio-size adjustment

## Caveats

- TPP-artifact unwinding pace is not deterministic — depends on borrower performance on the modification plans. If borrower defaults rise during TPP, "stable distress-adjusted" framing weakens.
- CRL is a consumer-advocacy organization with policy priors; their framing favors the "no real distress" read. Steelman: an adversarial read of the same data could argue TPP rule masked real deterioration. Distress-adjusted methodology + MBA Q4 independent corroboration mitigate but don't eliminate this.
- 2009 peak comparison (rate-basis ~9.4%) is an aggregate; FHA borrower composition has shifted since 2009 (more first-time buyers, different geographic distribution, lower-FICO accommodations). Cohort-adjusted comparison would refine the read.
