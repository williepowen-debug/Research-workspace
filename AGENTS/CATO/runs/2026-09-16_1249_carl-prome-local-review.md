# CARL and PROME local-work review

Will requested review of both sessions' local work, including uncommitted changes. Read-only with respect to their files; CATO authored only this report and continuity. Review snapshot September 16, approximately 12:40–12:49 ET. Starting HEAD `7c7b33e8a`; during review PROME committed `e210dc884`, `7ac1d4569`, `c50ba27a0`, `fb2f803c6`, and CARL committed `905594e5b`. This is an in-progress review, not certification of either session's eventual closeout. No owner response requested or received.

## Assessment

The inspected spending analysis is useful and its central arithmetic reproduces. CARL carries aggregate counterevidence without inventing a cohort conclusion or regrading its frozen tests. PROME distinguishes a bounded structural checker from actual runtime receipts, and its Kernel work remains draft/spec-gated. Two medium issues and one low evidence-reproducibility issue remain in the reviewed artifacts. No owner files repaired.

## Findings

### 1. Medium — CARL's cross-agent consumer brief misses the new counterevidence

VERIFIED: `AGENTS/CARL/STATUS.md:58` and `domain/sources/2026-09-16_news-catchup.md` incorporate the August retail rebound and mixed issuer credit evidence. Commit `905594e5b` contains this research and a refreshed SCRATCH, but no NEXUS_BRIEF update. The brief's last commit remains `aad6cb793`, September 11. `NEXUS_BRIEF.md:112` still presents August retail as an upcoming September 15 event and July's adverse spending print as the operative prompt. Its V16 branch at line 85 also remains PROVISIONAL while the new SCRATCH carries WQ-182's ratification.

Owner contract: `AGENTS/CARL/CLAUDE.md:104` requires the brief to be the last write-back after STATUS, immediately before commit; material STATUS changes must propagate. It explicitly says NEXUS normally reads the brief instead of raw STATUS. Consequence: a cross-domain synthesis can miss counterevidence already held by CARL. This is a delivery gap in the current committed result, not evidence CARL has ended its session or will refuse to finish it.

Proposed owner action: reconcile the existing brief with the final STATUS and approval state before declaring closeout. Preserve calibration and cross-domain qualifications; no new summary surface is needed.

### 2. Medium — PROME's checker loses unresolved touches across midnight

VERIFIED at `PROME/tools/orch_closeout.py:52`: rows outside the selected calendar date are dropped. CLI line 131 defaults to today's Eastern date, and `prome_gate.py` invokes the checker without a date or session interval. The plan deliberately specifies a selected-day checker, so this is an acceptance/design coverage gap against session closeout, not failure to implement that narrower plan. L378 remains PENDING; PROME is not claiming all runtime conditions are fulfilled.

Independent counterexample, temporary ledger only: one PROME-owned helper touched at `2026-09-15T23:55:00-04:00`, observed `23:56`, state ASKED_WORKING, session_id `overnight-helper`, nonempty ask. At a September 16 01:00 ET observation, evaluating September 15 names the pending helper; evaluating September 16 returns no rows and only generic inventory UNKNOWN. A CLI invocation for September 16 with `--inventory-complete` and no expected keys returns rc=0 and no output: that assertion is truthful about September 16 touches but does not settle the still-running session's September 15 helper.

Consequence: the ordinary boot/closeout report no longer names the unresolved helper after midnight. Explicitly supplying its old key exposes a generic missing-row issue but cannot produce its four-state disposition for the current day. This recreates the omission class at the date boundary. The default gate does retain UNKNOWN; CATO does not characterize it as a default false PASS. No actual lost overnight helper was established.

Proposed owner action: define coverage by the current coordinator session, or enumerate outstanding prior-date touches alongside today's population. Add an overnight fixture retaining the actual helper/state, and keep incomplete external inventory explicit. Merely adding prose about checking yesterday will not repair the default consumer.

### 3. Low — CARL's WalletHub text attribution lacks its claimed retained vintage

VERIFIED: `domain/sources/2026-09-16_news-catchup.md:46` attributes $11,153 / Q1 2026 / inflation-adjusted to the article. The retained `wallethub.html`, however, contains $11,313 / Q2 2026 text, also seen in CATO's fresh [publisher read](https://wallethub.com/edu/credit-card-debt-report/127704). The retained nominal/real arrays reproduce CARL's +15.12%/+5.44% Q4-2022→Q4-2025 calculations exactly. Those comparisons and the unknown carrying-balance denominator still justify refusing to certify the +83% chart.

This is a provenance gap for that particular text attribution, not proof that CARL never saw a different web vintage or that its overall chart disposition is wrong. Proposed owner action: retain/cite the exact older web receipt, or label the attribution as an earlier unretained observation and use the saved article's actual quarter/value when describing the retained source. Do not silently splice vintages.

## Checks and positive evidence

- Ten `test_orch_closeout.py` tests pass, run with PYTHONDONTWRITEBYTECODE=1. The independent overnight test above was devised separately and did not mutate production or the live ledger.
- CARL's derive.py was copied with its inputs to a temporary directory and run there. Its output equals the retained derived.json. Independently using exact Fraction arithmetic over Census Table 1 gives control 421,968 versus 416,300 million, +1.361518%; excluding nonstore gives +0.754323%. This supports both desks' derived figures.
- Fresh [Census CB26-153](https://www.census.gov/retail/marts/www/marts_current.pdf) read confirms release date, headline +1.2%, revised July -0.5%, the six transcribed category levels, September 28 tentative revision and October 15 next release. Nominal/revised-vintage caveats are carried correctly.
- Fresh [Capital One exhibit](https://investor.capitalone.com/static-files/0191ea61-5769-40a9-b1fe-300682ded325) confirms August card and auto rates/delinquent amounts. Fresh [Synchrony exhibit](https://www.sec.gov/Archives/edgar/data/1601712/000160171226000037/creditstatsfinancialtables.htm) confirms flat adjusted NCO despite rising reported NCO. No discrepancy found in those sampled current observations. July Capital One and Bread were not independently reopened in this pass.
- Inspected L247 F3/F8 plan, result receipt, current docket integration and selected spec changes; named RED/DAEDALUS gate approval remains owed. This is not an independent Kernel acceptance review or full review of every pre-existing spec clause.
- PROME's current morning checkpoint acknowledges four retrospective helper registrations, missing exact initial action timestamps, UNKNOWN machine evidence, absent native domain transport and pending hosted publication. These are honestly recorded unresolved conditions, not completed runtime verification.
- L392 is a bounded observation setup; no numerical calibration or successful future-window collection was established by CATO. No new price pull, trade analysis or gate regrade performed.

## Revision pins and review limits

SHA-256 of reviewed files:

| File | SHA-256 |
|---|---|
| CARL/NEXUS_BRIEF.md | 870b4bb3661ae7d87bee656c46cac10e57b9bded90414039336753dde46d50b5 |
| CARL/domain/sources/2026-09-16_news-catchup.md | 8b78b76952d935892f2a164b4d539e889c3f5396b456969721b61abb79b859c1 |
| CARL retained wallethub.html | 95f832a5ee2ad5ba2d759fa999645b3a19317dfa93f11dd63705ab80f0743d59 |
| PROME/tools/orch_closeout.py | f26c1931d655665519ca722e00a3a059d952593358885d9c7088dc5656f07caf |

CARL paths above are under AGENTS/. Owner files changed during review, so findings apply to these pins and stated commits. Full BOARD backlog, complete market-source validation, all prediction grades, source-authenticity of every stored series, all runtime messages and final publication remain outside the inspected perimeter. Prior CATO repairs are not independently recertified by this pass. CARL read-cap debt is already declared; no unsolicited restructuring undertaken.

Review complete. No repair or owner-message task assigned. Next CATO session: orient and await Will; if assigned follow-up, first check whether owners already corrected these exact findings. Shared working tree still contains PROME's in-flight edits. Commit/push outcome is delivered in-session; no synchronization through another owner's active edits is authorized by this review.
