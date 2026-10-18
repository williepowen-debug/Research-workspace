# Fellowship application — fact pack (not a draft)

**Written:** 2026-10-18 18:0x ET, PROME prome-65. **For:** Will's application to Anthropic's Conceptual Reasoning Fellowship (Greenhouse job 5447080008). **Deadline:** Wed 2026-10-28; offers by 11/20; program 2027-01-12 → 05-08, full-time. **Status of this file:** raw material and pointers only. ⛔ **It contains no answer text, on purpose — see § 1.**

## 1. The rule that shapes everything (read 2026-10-18 at https://www.anthropic.com/candidate-ai-guidance)
- Verbatim: *"Please create your first draft yourself, then use Claude to refine it."* · *"Use AI to refine your ideas, not replace them."* · listed as NOT allowed: *"Write my answers to the application questions for an AI safety researcher position at Anthropic."*
- The form makes you confirm you have read the guidelines (a "Yes" dropdown).
- **So:** Will writes every first draft. PROME supplies facts and figures (this file), checks claims against the record, and refines a draft once one exists. The 10/16 owed item "research-statement outline in his voice" is **withdrawn**: it would be the forbidden pattern.

## 2. What the form actually asks (Greenhouse page, read 2026-10-18)
| Item | Limit | Required? |
|---|---|---|
| CV/resume or LinkedIn | — | one of the two |
| Field(s) applying for | dropdown | yes (economics primary, philosophy second — Will, 10/17) |
| One or two concrete ideas for evaluating, improving or applying Claude in your field | ~200 words | yes |
| Experience with Claude Code / agentic coding tools: use cases, workflow | 150 words | yes |
| ML/AI experience (training or applying models) | ~150 words | optional |
| Anything else | free | optional |
| Cover letter | — | optional |
| **Two references** — name, email, how you know them | — | **yes** |
| AI-policy confirmation · arbitration agreement · work location | dropdowns | yes |

- **Not asked:** a research statement, a four-month project proposal, a writing sample. The 10/16 owed list assumed a longer application. A short version of the project idea can ride in "Anything else" or the cover letter — your draft.
- **Terms that bind:** US work authorization required (no visa sponsorship) · one-week in-person orientation in San Francisco · default location SF, remote within the US "may be considered" · fixed-term contract through an employer of record · $100,000–$167,000 for the four months.
- **Minimum qualifications as listed:** enthusiasm for AI reasoning well in your field · hands-on Claude and Claude Code use · PhD held/in progress **or equivalent research experience** · comfort with a fast, high-agency environment · US work authorization. **Preferred:** experience designing evaluations, benchmarks, datasets or expert rubrics; demonstrated expertise through research or analytical writing.
- **Representative projects named on the page:** hard ethics cases · experimental-design tasks · economic modeling problems · regulatory cost-benefit tasks · AI-policy law datasets. Responsibilities include "design evaluations and RL environments that test Claude's reasoning in your field".

## 3. Verifiable figures (re-run before citing — they move daily; run 2026-10-18 18:0x ET)
| Figure | Value | Command (repo root) |
|---|---|---|
| Operating since | 2026-02-01 | `git log --reverse --format=%ad --date=short \| head -1` |
| Days with commits | 255 | `git log --format=%ad --date=short \| sort -u \| wc -l` |
| Commits | 18,633 (includes automated state writes) | `git rev-list --count HEAD` |
| Desks with a maintained state file | 41 (ROSTER: 34 active) | `ls AGENTS/*/STATUS.md \| wc -l` |
| Failure findings | 487 | `ls memory/auto/finding_*.md \| wc -l` |
| Session notes | 208 | `ls memory/2*.md \| wc -l` |
| Forecast ledgers / rows | 30 / 445 (README, 10/16; re-run its command) | README § Repository scale |

⚠️ The local demo clone (`~/Selected-Agents-Open-Demonstration`, last local commit f7d5597 2026-09-06) is behind GitHub. Pull it before citing anything from it.

## 4. Raw material by question (facts and pointers, no sentences to copy)
**Eval idea (~200 words).** Two candidates already discussed (10/17, NISABA's window; PROME's ranking):
1. *Said-vs-true:* does the model's stated confidence and stated reason match what the record later shows? Material: dated forecast ledgers with registration commits (README stop 1, demo case 9); `FORGE/PREDICTION_DISCIPLINE.md` (anti-retuning rules); findings `finding_exact_level_authenticates_a_wrong_direction`, `finding_attribution_authenticates_a_figure_its_named_source_never_produced`. The resolution rule must be stated in the box (PROME's 10/17 note).
2. *Data vintage / hindsight:* does the model reason only from what was knowable on the date? Material: ALFRED real-time vintages (St. Louis Fed); findings `finding_two_legs_with_independent_vintage_clocks_mix_dates_invisibly`, `finding_a_daily_bar_read_after_the_evening_open_belongs_to_the_next_session`, the HEARTBEAT § 2R stale-CDN cases.
- Fit to the page: "economic modeling problems" and "design evaluations … that test Claude's reasoning in your field".

**Claude Code experience (150 words).** Facts: daily use since 2026-02-01 (255 days with commits) · ~40 specialist desks run as Claude Code (and some Codex) sessions in one Git repo · coordinator/subagent orchestration, hooks, skills, custom agent types (blind cold reader, counterexample reader, closeout auditor) · file-based coordination with dated packets · pre-registered triggers graded by scripts · the tool-adoption gap measured and closed (README stop 4).

**ML/AI experience (optional).** Honest state: no model training. The relevant experience is evaluation design: independent blind readers that must bring their own counterexamples; a 487-file taxonomy of model judgment failures with counted recurrence. Whether to answer at all is your call.

**References (2).** ⛔ **The real gap** (PROME, 10/16). Only you know the candidates. The form wants name, email and how they know you; someone who has seen the work in use is worth more than a title. Ask early: 10 days is short notice for a referee.

## 5. What PROME can do next, inside the rule
- **Ledger search for the "mirror question"** (owed from 10/17): an instance where the system established something true that you did not hold, or killed one of your theses with evidence. Raw material for the "anything else" box or an interview.
- **Claim-check your drafts** against the record: every figure, date and file named.
- **Refine on request** after your first draft: clarity, word count, the field fit.
- **Demo README refresh** (owed): pull first.

Sources: https://job-boards.greenhouse.io/anthropic/jobs/5447080008 · https://www.anthropic.com/candidate-ai-guidance (both read 2026-10-18).
