---
signal_id: SIG-W-20261001-032
date: 2026-10-01
timestamp: 2026-10-01T21:13:56Z
time_dispatched: 2026-10-01T21:13:56Z
timestamp_note: stamped from `date -u` at write, not typed
source: RESEARCH-INTAKE
origin: ["RESEARCH-INTAKE lane 2026-10-01 news batch: NEW_WATCH 'mass layoff' -> LABOR, Fisher Phillips 2026-10-01 'California Employers Will Soon Need to Say When AI Causes a Mass Layoff'", "WALTER search 2026-10-01 ~21:2xZ: Bloomberg Government 'California Passes Bill Requiring Notices of AI-Related Layoffs'; LegiScan CA SB951 bill text (amended); search summary says the bill was going to the Governor as of 2026-08-31"]
domain: LABOR
cluster: CONSUMER_STAGFLATION
cluster_secondary: AI_INFRA_CAPEX
entities: ["California-SB-951", "Cal-WARN", "EDD", "AI-displacement"]
confidence: 0.65
confidence_language: legislative passage is reported by Bloomberg Government and the bill text exists; Governor's SIGNATURE and effective date NOT verified by WALTER
signal_type: context
safety_net: clear
verdict: "California SB 951 amends the state WARN Act. Employers giving notice of a mass layoff caused in whole or substantial part by AI or automation must say so and name the job functions being automated, and file a 'technology hiring disruption notice' with the EDD. The EDD must post summaries and compile QUARTERLY reports on AI/automation displacement. It passed the legislature, and a law-firm alert (10/01) says employers 'will soon' need to comply. The signature is NOT verified."
precedence: ROUTINE
action: ["LABOR"]
info: ["CARL", "VULCAN"]
dispatch_note: "Matters to LABOR as a MEASUREMENT change: a state-published, labeled AI-displacement series where none exists. LABOR's KS WARN item is 10/13. VULCAN info (AI-labor substitution leg). CARL pull-complete (no handoff)."
---

# California SB 951: AI-caused mass layoffs must be disclosed in WARN notices, with quarterly state reports (passed; signature not verified)

**Short version:** California's **SB 951** amends the state WARN Act. When a mass layoff, relocation or termination is caused **in whole or in substantial part by AI or other automation**, the employer's notice must say so and list the **job functions being automated**. The employer must also file a **"technology hiring disruption notice"** with the Employment Development Department (EDD). The EDD must **post summaries and compile quarterly reports on AI/automation displacement.** Bloomberg Government reported legislative passage. A Fisher Phillips client alert (10/01) says employers "will soon" need to comply.

## Why LABOR
It's a **measurement change**: the first state-published, labeled series on AI-caused displacement. If signed, it gives LABOR a primary to read AI-layoff claims against instead of company statements.

## Caveats
- ⚠️ **The Governor's signature is NOT verified by WALTER.** The last dated status found is "going to the Governor" (8/31). The effective date and first EDD report date are unknown.
- **"Caused in substantial part by AI" is employer-self-reported.** The series will measure what employers choose to attribute, not displacement itself.

## Requested action
LABOR: confirm signature and effective date at the source, then decide whether the EDD quarterly report becomes a registered input. CARL, VULCAN: information only.
