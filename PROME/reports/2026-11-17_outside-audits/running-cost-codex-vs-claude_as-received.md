# What the fleet costs to run, and Codex versus Claude

**Date:** 2026-11-18 · **Repository pin:** `78ed22bb9d` (2026-11-17 18:44 ET), full history · **Read only:** nothing in the repository was changed.
**Question 4 of 7** in the follow-up round William approved on 2026-11-17.

## The short answer

The repository does **not** keep a running record of cost. There is no dollar figure, no subscription record, and no standing log of session time or tokens anywhere in it.

There is **one direct measurement**, made once: on 2026-11-05 the RED desk counted tokens by desk from the Claude and Codex transcript files on the desktop machine, for the 30 days from Oct 6 to Nov 5 (`AGENTS/RED/research/2026-11-05_op-scale_usage/`). It was built to argue about the fleet-shrink proposal (which William declined on 2026-11-06, WQ-599) and has not been run again. Everything below about tokens comes from that one count; everything about output comes from git.

What it shows, for those 30 days on the desktop:

| | Figure | Basis |
|---|---|---|
| New tokens (input written fresh + output) | **299.5 million** | RED count, both runtimes |
| of which Claude | 172.7M (58%) | RED count |
| of which Codex | 126.9M (42%) | RED count |
| Tokens re-read from cache | 11.8 billion (Claude 8.0B, Codex 3.8B) | RED count |
| Three coordinating desks (PROME, WALTER, DAEDALUS) | **50%** of new tokens | RED count |
| The 19 desks TERRY's draft called dormant | 7.7% | RED tier roll-up |
| Claude at published API prices (an equivalent, not a bill) | **about $2,500 to $5,000 a month** | my arithmetic, below |
| Codex at API prices | not estimated | model and price not recorded |

**So what:** half of the measured token use goes to coordination (PROME 23%, WALTER 17%, DAEDALUS 10%), not to domain research. The 30-odd domain desks together use about the other half, and the smallest ones are close to free. If William ever wants to cut running cost, the lever is how much PROME, WALTER and DAEDALUS read and re-read, not the number of desks. That matches RED's own reading at the time.

On Codex versus Claude: the desks are not split by runtime. Almost every busy desk ran on both in the window. Comparing Claude sessions with Codex sessions on the same desk, I find **no meaningful difference in error rate** and roughly **equal research output per token**. Codex commits are larger and more often touch research files, but that looks like a difference in how often each runtime commits, not in what gets done.

## 1. What is recorded, and what is not

| Looked for | Found? | Where / what |
|---|---|---|
| Dollar spend, invoices, subscription plan | **No** | The only "$100/month Max plan" line is a quoted outside blog post in a WALTER bookmark packet, not William's plan. |
| Tokens by desk | **Once** | RED, 2026-11-05, desktop only, Oct 6 to Nov 5. Scripts read `~/.claude/projects` and `~/.codex/sessions` on that machine. Not in any boot or closeout routine. |
| Session count | **Once**, same source | 337 main Claude sessions plus 226 helper (subagent) sessions; 349 Codex sessions. |
| Session clock time | **No** | No start/stop record. Commit timestamps exist but do not measure session length. |
| Which model ran | **Yes, per commit, for Claude** | `Co-Authored-By: Claude <model>` trailer on 4,161 of 6,168 commits in the window (Opus 5.5 77%, Fable 5.1 22%). Codex commits carry no trailer; a few dozen say "Runtime: OpenAI Codex, gpt-6.1-sol" or "variant UNKNOWN" in the body. |
| Running out of usage | **Yes, scattered** | Jul 10 (session limit mid-run, DEWEY), Jul 29 (Claude ran out mid-FOMC day; RAV was built on Codex that day to keep going), Oct 14 (CATO "out of usage"), Nov 2 and Nov 4 (BRENT's scheduled EIA runs failed on the usage limit; no output for either day). |

⚠️ **Limits of the one measurement.** It covers the desktop only; anything run on the laptop is missing. That is why some desks show almost no tokens but plenty of commits (MARCO 47 commits, 0 tokens; YURI 36 commits, 0.2M; SHADE 43 commits, 0.2M). Tokens are not dollars and not usage-limit units. RED's script assigns subagent ("helper") work to the desk that spawned it, so a PROME-spawned desk session is counted to that desk where it could be identified.

## 2. Cost per desk against output (30 days, Oct 6 to Nov 5)

"Output" here is **commits that changed a research, forecast-ledger or source-data file**, using the pass 6 classifier (`/mnt/project-files/coordination-load/classify.py`) unchanged. It is a proxy: it counts that research was touched, not whether it was any good. PROME's job is coordination, so it scores badly on this measure by design.

| Desk | New tokens | Share | Claude / Codex sessions | Commits | Commits touching research | Tokens per research commit |
|---|---:|---:|---|---:|---:|---:|
| PROME | 69.2M | 23.1% | 126 / 66 | 1,655 | 36 | 1,921k |
| WALTER | 49.9M | 16.7% | 23 / 106 | 717 | 392 | 127k |
| DAEDALUS | 30.4M | 10.1% | 17 / 35 | 227 | 117 | 260k |
| DEWEY | 20.0M | 6.7% | 10 / 6 | 97 | 69 | 289k |
| REGINALD | 12.5M | 4.2% | 11 / 10 | 311 | 173 | 72k |
| TERRY | 10.6M | 3.5% | 9 / 13 | 193 | 114 | 93k |
| CATO | 10.4M | 3.5% | 0 / 32 | 242 | 236 | 44k |
| BRENT | 10.3M | 3.4% | 6 / 12 | 219 | 130 | 79k |
| VULCAN | 7.9M | 2.6% | 10 / 3 | 145 | 59 | 134k |
| LIQUID | 7.1M | 2.4% | 8 / 7 | 200 | 95 | 75k |
| WAL | 7.1M | 2.4% | 8 / 4 | 123 | 55 | 129k |
| NEXUS | 5.3M | 1.8% | 5 / 16 | 104 | 67 | 78k |
| BROCK | 4.5M | 1.5% | 10 / 4 | 94 | 37 | 120k |
| OZK | 4.4M | 1.5% | 5 / 4 | 70 | 32 | 138k |
| BOND | 4.3M | 1.4% | 5 / 6 | 50 | 33 | 131k |
| CREED | 4.2M | 1.4% | 3 / 0 | 47 | 26 | 162k |
| RED | 4.2M | 1.4% | 9 / 0 | 87 | 36 | 116k |
| HENRY | 3.7M | 1.2% | 7 / 1 | 99 | 37 | 100k |
| VIOLET | 3.4M | 1.1% | 4 / 4 | 75 | 42 | 82k |
| CYPHER | 3.1M | 1.0% | 5 / 0 | 103 | 47 | 65k |
| FALCON | 2.7M | 0.9% | 8 / 1 | 100 | 37 | 73k |
| OSPREY | 2.5M | 0.8% | 7 / 0 | 74 | 36 | 69k |
| MIDAS | 2.2M | 0.7% | 3 / 1 | 86 | 59 | 37k |
| CARL | 2.2M | 0.7% | 2 / 4 | 88 | 39 | 55k |
| ZHAO | 1.9M | 0.6% | 7 / 0 | 30 | 14 | 138k |
| SAM | 1.9M | 0.6% | 1 / 5 | 32 | 12 | 158k |
| 17 smaller desks together (FLG, WATT, OTTO, HOMER, HANS, CORAL, CRUISE, LABOR, FERT, HAWK, ISHM, ORACLE, AEOLUS, GIBBS, YURI, SHADE, MARCO) | 13.1M | 4.4% | | 830 | 344 | about 38k |

Full table with file counts: [per_desk_cost_vs_output.tsv](per_desk_cost_vs_output.tsv). Every commit in the window with its runtime and class counts: [commits_window.tsv](commits_window.tsv).

What stands out:
- **PROME costs about 2 million tokens for every research-touching commit.** That is expected for a coordinator, but it is also the single biggest line: 23% of everything, plus most of the re-reading from cache (2.4B of Claude's 8.0B). Pass 6 found the same thing from the file side.
- **DEWEY and DAEDALUS are the expensive research-side desks** (260k to 290k tokens per research commit), roughly three times the domain-desk median. For DEWEY that fits its role (long deep-research runs with many helper sessions: 62 helper files). DAEDALUS is the fleet's maintenance and design desk, sits outside the 41, and alone uses more than the 19 dormant desks combined.
- **Most domain desks land between 40k and 140k tokens per research commit.** There is no obvious outlier among them that would justify a desk-by-desk cut.

## 3. A dollar equivalent, labelled as such

The repository shows William runs on usage-limited plans (the repeated "out of usage" events), so the real cash cost is his subscription fees, which are not recorded anywhere. As a sense of scale only, here is what the measured **Claude** tokens would cost at Anthropic's published API prices (Opus 5.5: $4 per million input, $20 output, $0.20 cache read; Fable 5.1: $10 / $50):

| Scenario | New tokens | Cache reads | Total, 30 days |
|---|---:|---:|---:|
| Low: all Opus 5.5, new tokens mostly cache writes (about $5 per million) | $863 | $1,600 | **about $2,500** |
| High: 22% Fable 5.1 as in the commit trailers, a quarter of new tokens being output | about $2,000 | about $3,000 | **about $5,000** |

The split between input and output is not in RED's printout, so the range is wide. Codex tokens are not priced: the model is recorded only as "gpt-6.1-sol" or "unknown", and I do not have a reliable price for it.

## 4. Codex versus Claude

**First, a correction to the framing.** Desks are not Codex desks or Claude desks. Root `CLAUDE.md` says a desk keeps its identity on whichever runtime it is launched on, and the data shows that: of 45 desks with commits in the window, 27 have at least 10 commits from each runtime. Only CATO is all Codex; RED, LABOR, OSPREY, AEOLUS, CREED, HANS, ZHAO and CORAL are all Claude. So the fair comparison is **Claude sessions against Codex sessions, within the same desk**.

**How I told them apart (a proxy).** Claude commits carry a "Co-Authored-By: Claude" trailer; I treated commits without it as Codex. Checked against RED's token count, the share of a desk's commits without the trailer tracks the share of its tokens that came from Codex (correlation 0.70 across desks). It is not exact: some desks with no desktop Codex tokens (SHADE, YURI, HAWK) still have untrailered commits, likely laptop Codex sessions.

| Oct 6 to Nov 5 | Claude | Codex (proxy) |
|---|---:|---:|
| Commits | 4,161 | 2,007 |
| New tokens (desktop) | 172.7M | 126.9M |
| Tokens per session | about 310k (incl. helpers) | about 360k |
| Commits touching analysis or ledgers | 1,118 | 852 |
| ...per million tokens | 6.5 | 6.7 |
| Files per commit | 7.7 | 11.2 |
| Share of commits that are boot or closeout | 12.9% | 11.6% |
| **Rework rate**: analysis files changed again within 3 days by a commit titled fix / correct / revert | **23%** (domain desks 26%) | **17%** (domain desks 23%) |
| Commit subject itself says fix / correct | 12.7% | 11.7% |
| Commits writing outside the desk's own lane (domain desks) | 3.0% | 0.3% |

Within the 27 desks that used both, Codex commits were more often research-touching on 18 of 27 desks and larger on 21 of 27, while the fix rate was higher for Codex on only 11 of 27 (median difference: Codex 2 points lower).

**What this means:** per token spent, the two runtimes produce about the same amount of research-touching work, and I cannot find an error-rate difference that survives restricting to domain desks. Codex commits less often and in bigger batches, which is why it looks "more research per commit". The one clear difference is that Claude sessions on domain desks more often write outside their own directory (3.0% against 0.3% of commits); most of those are legitimate shared files, so treat it as a lead, not a finding.

⚠️ **What this cannot tell you.** None of these are quality measures. A fix titled "fix" is counted whether it fixed a factual error or a typo, and a forecast graded wrong is not counted at all. Pass 5's forecast ledgers are too sparse to split by runtime. The comparison is one 30-day window on one machine's tokens.

## 5. What would make this answerable properly

The data already exists on William's machines; the repository just does not keep it. A small change would turn this from a one-off into a standing figure:

1. **Re-run RED's script monthly** on each machine and keep the output under a dated folder, so the figure is not frozen at Nov 5.
2. **Record the runtime in every commit.** Claude does this already through the trailer; Codex sessions should add one line (for example `Runtime: OpenAI Codex, <model>`), so a runtime comparison stops depending on the absence of a trailer.
3. **Log usage-limit hits in one place** (date, machine, what failed), since those are the only direct sign of hitting the plan ceiling.

Method and scripts: [scripts/](scripts/). They read only the clone and RED's committed output files.

---

## Copy-paste block for PROME

```
PROME — running-cost follow-up from William's outside audit (2026-11-18). Read-only findings; nothing in the repo was changed by the audit. No trade, gate or threshold is affected.

Context: the repo keeps no standing cost record. The only token-by-desk measurement is RED's one-off count, AGENTS/RED/research/2026-11-05_op-scale_usage/ (desktop only, Oct 6 to Nov 5): 299.5M new tokens, of which PROME 23.1%, WALTER 16.7%, DAEDALUS 10.1%. Claude at API list prices would be about $2,500 to $5,000 for that month (an equivalent, not a bill). Claude and Codex sessions on the same desk show about equal research output per token and no meaningful error-rate difference.

Please do the following, and bring any change to a shared or root file to William first:

1. Ask RED (owner of the script) whether it will re-run usage_by_desk.py and tier_rollup.py once a month on each machine, saving output to a new dated folder under AGENTS/RED/research/. Laptop sessions are missing from the Nov 5 figure; the next run should cover both machines and say which is which.

2. Propose to William a one-line runtime record for Codex commits (for example "Runtime: OpenAI Codex, <model or UNKNOWN>") alongside the existing Claude co-author trailer. This is a commit-message convention, so it touches docs/GIT_WORKTREE_PROCEDURES.md or root CLAUDE.md: William's approval needed before any edit.

3. Start one log of usage-limit hits (date, machine, runtime, what failed or was skipped) in a PROME-owned file. Known hits so far: Jul 10, Jul 29, Oct 14, Nov 2, Nov 4 (BRENT's scheduled EIA runs failed both days).

4. For William's brief, one line: PROME, WALTER and DAEDALUS together used half of all measured tokens in the month to Nov 5; the 19 dormant-tier desks used 7.7%. If running cost ever needs to come down, the lever is coordination reading, not desk count. This is information only; William already declined the fleet shrink on 2026-11-06 (WQ-599).

Source report: William's audit folder, running-cost/2026-11-18_running-cost-and-codex-vs-claude.md.
```
