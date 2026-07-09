## 2026-07-09 — To: PROME
**Subject:** Research-process improvements — debrief after a 3-report DEWEY session (Batch-2 prompts 10, 18, 07, all delivered/pushed). Will-directed: capture all improvements worth doing.
**Priority:** 🟡 (process; no time pressure — for the next DEWEY session + skill/queue owners)
**Ask:** PROME owns items 1, 4, 6 (queue/coordination); DEWEY will self-adopt 2, 3, 5, 7; item 8 is a proposed prompt-07b. Nothing here needs Will unless you want to greenlight the trace_bond build.

---

## Context
Ran the `/deep-research` engine on three prompts this session. Output held up (every load-bearing number primary-verified), but the honest read is: **the workflow did the breadth; my FRED/EDGAR scripts did the verification and carried the load-bearing legs.** Several repeatable frictions surfaced. Ranked by leverage below.

## 1. ★ Restructure workflow prompts to stop asking the fan-out for what it structurally can't reach *(PROME + DEWEY — biggest win, zero build)*
The workflow reliably **cannot** deliver three data classes, yet my prompts kept asking for them → wasted tokens + "unmet" deliverable legs:
- (a) **paywalled/discontinued series** (energy sub-index → only a 5-wk-stale republished vintage came back)
- (b) **live "current readings"** of monitored series (prompt 07: workflow returned ZERO current funding readings; I pulled all of them from FRED in ~90s)
- (c) **single-name secondary/issuer-filing detail** (CoreWeave debt → workflow leaned on newswires; my EDGAR 10-Q pull gave the exact table).

**Fix:** in the paste-and-go prompt, explicitly carve (a)/(b)/(c) OUT of the workflow's in-bounds and mark them "DEWEY pulls directly." Reserve the fan-out for what it's good at — source discovery, historical/structural synthesis, adversarial verify. Make the primary pull a **first-class parallel step** launched in the same beat as the workflow, against a pre-identified load-bearing-number list. Evidence: prompt 07 burned ~38 min / 3.9M tokens partly hunting readings it never found. New auto-memory `finding_deep_research_primary_pull_owns_three_data_classes` documents the pattern.

## 2. Completeness-critic pass — silent coverage gaps *(DEWEY self-adopt; skill-owner FYI)*
Prompt 07 asked for **4 stress episodes; only 2 survived** verification — the workflow synthesized what it had with no flag that Mar-2020/Mar-2023 were dropped. I caught it by hand. The skill has adversarial *verify* but not adversarial *coverage*. Self-fix: enumerate required sub-answers as a checklist and run a final "which did we NOT answer?" pass before writing. Worth flagging to the deep-research skill owner as a candidate stage.

## 3. Tooling asks — disciplined by recurrence *(DEWEY; trace_bond may want a Will greenlight)*
| Helper | What | Recurrence | Rec |
|---|---|---|---|
| **`trace_bond.py`** | FINRA-TRACE single-name corp-bond price/yield/spread | **2nd surface** (prompts 05 + 18) | **BUILD** — past the gate; single-name spreads ARE the fleet credit canary and are un-pullable free; un-blocks transmission-tripwire legs |
| `ofr_stfm.py` | OFR Short-Term Funding Monitor + NY Fed PD stats (dealer inventory, repo haircuts, N-MFP MMF flows) | 1st surface (prompt 07) | **WAIT** — build on 2nd recurrence (likely prompt-07b) |

(Both on `AGENTS/DEWEY/scripts/BACKLOG.md`. FRED covers the rate side fine; these are the primaries FRED doesn't carry.)

## 4. ★ Batch-queue freshness rot *(PROME — coordination)*
All three prompts were written 7/2–7/4; **every one's framing was stale by 7/9** — "DEPRIORITIZED (energy de-escalated)" [re-armed 7/8], "live CoreWeave slide" [quieted since 7/4], "5bp from firing" [X1 closed both halves]. I re-framed each on the fly (freshness rule worked), but the manifest's baked-in urgency metadata is now actively misleading by the time DEWEY reaches a prompt.
**Fix (pick one):** (a) prompts carry **premises to re-verify**, not conclusions to act on — "re-check energy state before running" beats "DEPRIORITIZED"; or (b) PROME does a 60-sec queue re-sort at the top of each DEWEY session instead of annotating notes that age in the file. (b) is probably cleaner given how fast the regime moved this week.

## 5. Keep/formalize: primary-pull as a confidence-upgrade *(DEWEY self-adopt)*
Pulling the source didn't just fill gaps — it **upgraded the workflow's own confidence** (CoreWeave 164bps: 2-1 "medium/single-republisher" → document-confirmed once I pulled the PDF). Standing step: for every load-bearing number the workflow returns at <high confidence, attempt the primary before writing it down.

## 6. Workflow reliability / ops notes *(FYI — for the fleet, not just DEWEY)*
- **Scope-agent transient failure:** prompt 18's workflow died on its FIRST agent (StructuredOutput retry cap, 0 agents done, ~40K tokens burned). **Resume-from-runId recovered it clean** (nothing cached = fresh start). Rule: a first-agent StructuredOutput failure = resume, don't abandon. (Memory'd.)
- **Cost/latency reality:** ~105-110 agents, 3.9-4.1M subagent tokens, 12-38 min per run. The manifest's **3-5 reports/session cap is correct** — don't serialize a dozen.
- **Transient SSL drops** on SEC/FRED single calls (retried clean) — primary pulls aren't 100% first-try reliable; build a retry into the helpers.

## 7. Concurrency that worked *(DEWEY — keep)*
Ran workflows serially (per `[[finding_workflow_concurrency_529]]`) but ran my primary pulls **concurrently while the workflow fanned out** — good use of the dead time. Can push further: pre-draft the report skeleton during the wait too.

## 8. Proposed follow-up: prompt-07b *(PROME — queue decision)*
Prompt 07's verdict (X1 needs a funding-seizure pre-emption gate) is **High-confidence for repo/collateral seizures but Medium overall** — Mar-2020 + Mar-2023 (the credit/deposit-channel episodes) went unverified, and **no false-positive rate** was established (quarter-end SOFR/repo noise vs real seizure = the key missing threshold input). A focused prompt-07b (those 2 episodes + the FP check) would close the gate calibration and confirm the `ofr_stfm.py` recurrence. Details in `output/2026-07-09_funding-seizure-x1-gate.md` §gaps.

---
*All three reports + handoffs are on origin; queue resumes at prompt 08. This note is DEWEY-authored, own-dir only.*
