# Comcast layoff claim — bounded verification

Verified: 2026-10-31 19:19 UTC. Verdict: **CORRECTED-FRAMING** (announced gross reductions confirmed; realized/net employment interpretation unsupported).

## Exact claim and conclusion

The October 30 PhillyVoice headline reports Comcast mass layoffs during restructuring. Pennsylvania and New Jersey primary WARN listings confirm **634 Pennsylvania positions plus 119 New Jersey positions = 753 announced affected positions**. These are prospective reductions, not 753 completed departures on October 30. Pennsylvania's effective window runs **December 31, 2026 through December 31, 2027**; New Jersey lists **January 27, 2027**.

The same article reports **over 500 planned new Philadelphia positions and over 1,100 across U.S. campuses**, with affected employees potentially transferring internally. Keep that offsetting context with the cuts. Neither realized exits nor realized hiring is established; subtracting announced additions from gross cuts would not establish a measured net employment change. The 753 sum covers Pennsylvania and New Jersey only, not the national restructuring total.

## Evidence locators and observations

| Source | Observation |
|---|---|
| [Pennsylvania Department of Labor & Industry, WARN Notices](https://www.pa.gov/agencies/dli/programs-services/workforce-development-home/warn-requirements/warn-notices), **2026 → October → Comcast Technology Center** | Lists 1800 Arch Street and 1701 JFK Boulevard, Philadelphia County; **634 affected**, layoff; effective beginning **12/31/2026**, ending **12/31/2027**. The listing supplies a month, not an exact receipt day. |
| [New Jersey DOL 2026 WARN archive](https://www.nj.gov/labor/assets/PDFs/WARN/2026_WARN_Notice_Archive.pdf), **page 3, final Comcast row** | **October**, effective **1/27/27**, **119**; Atlantic, Burlington, Camden, Cumberland, Gloucester, Mercer, Monmouth, Ocean and Union counties. PDF coordinate extraction confirmed the company, date and count occupy the same row. |
| [PhillyVoice, Kristin Hunt, October 30](https://prod.aws.phillyvoice.com/comcast-layoffs-philadelphia-restructuring/), article body | Reports 634 cuts, some affected positions retained through December 31, 2027; approximately/over 500 new Philadelphia roles and over 1,100 U.S. roles; attempted placement of affected employees into open/new roles; severance for workers not transitioning. Its headline omits the prospective hiring detail, but its subhead and body include it. |
| [WHYY, Meir Rinde, October 30](https://whyy.org/articles/comcast-phliadelphia-new-jersey-layoffs/), article body | Independently reports 634 Pennsylvania and 119 New Jersey reductions, with notice to state/city describing more than 1,100 new positions including more than 500 Philadelphia. Corroborates the additions as company plans, not observed hires. |

All four sources were read directly via ordinary HTTPS requests (HTTP 200). Earlier web-open failures did not persist through that retrieval method. The primary state listings verify counts and dates; the underlying employer notice/letter was not separately obtained. Hiring and redeployment caveats remain attributed to the company's statements as reported by the two articles. No exact filing day is asserted from the monthly state records.

## Routing boundary

Usable as a company-specific forward layoff/restructuring observation for LABOR, with gross/planned and hiring caveats attached. It does not independently establish broad labor deterioration, 753 net lost jobs, or AI as the quantified cause. No domain grade or threshold judgment supplied.

Dedup before new research: `rg` of LABOR STATUS/KB, then all LABOR Markdown/TSV files found no Comcast/CMCSA matches. October BOARD matches were unrelated cable financing/comparability records (October 2 and October 19), not this layoff event. Parent retains the routing decision.

Runtime/scope: OpenAI Codex helper `/root/verify_comcast`, inherited WALTER cwd; root resolved to `/home/willi/Research-workspace`. Root CLAUDE/AGENTS/USER and local WALTER CLAUDE explicitly loaded. Shell, HTTPS and web search used; exact model not exposed. This report is the sole repository write; no sends, dispatches, commits or owner-file edits.
