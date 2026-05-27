\*\*On Q1 (source):\*\* Go direct Excel/CSV scrape from stat.go.jp. Matches the pattern of mof\_flows (CSV), cftc\_jpy (text), jgb\_auctions (HTML). No API auth friction. Defer e-Stat until the scraper proves brittle. Make sure the script handles "file for current month not published yet" cleanly — Tokyo prints last Friday of month, National \~3 weeks later. Record both \`series\` (Tokyo/National) and \`reference\_month\` per row.

\*\*On Q2 (thresholds):\*\* The 1.9% anchor is sourced correctly (CALENDAR May 28-29 row \+ April national print), but the 3-bucket scheme has three problems worth fixing before you bake it in:

1\. \*\*Single-series only.\*\* You're fetching both core and core-core but only thresholding core-core. BOJ's actual policy target is \*\*headline core (ex-fresh-food)\*\* — core-core is the trend gauge. April printed core 1.4% / core-core 1.9% — that 50bp gap \*is\* the signal (energy/subsidy vs underlying). Drop it as a separate flag and you lose half the data's value.

2\. \*\*Middle bucket missing.\*\* Jumping from "\<1.5% collapse" straight to "\<1.9% leading threshold" leaves no state for "softening continues but stays in trend" (Tokyo May likely prints in this band). That's the modal outcome and needs its own status.

3\. \*\*≥2.0% as "hawkish anchor" is too generous.\*\* Core-core was 2.4% in March 2026 (verified via live stat.go.jp pull). 2.0% flat is at-target, not hawkish.

\*\*Bake in these two threshold tables instead:\*\*

\`\`\`  
Core (ex-fresh-food) — BOJ target series:  
  \<1.2%      Deep miss; June pricing collapses (\<30%)  
  1.2-1.5%   Soft band (April national 1.4% sits here); pricing biased lower  
  1.5-1.8%   In-line; pricing stable  
  ≥1.8%      Toward consensus; pricing firms toward 70%+

Core-core (ex-fresh-food-and-energy) — trend gauge:  
  \<1.5%      Dovish trajectory broken below; June pricing collapses  
  1.5-1.8%   CALENDAR \<1.9% threshold tripped; softening continues  
  1.8-2.1%   Sticky (current national 1.9% lives here); no new signal  
  ≥2.2%      Hawkish anchor / re-accelerating; pricing firms  
\`\`\`

\*\*Plus a cross-series divergence flag:\*\*  
\- \`core\_core − core ≥ 0.5pp\` → softness is energy/subsidy-driven; BOJ can look through it  
\- \`core\_core − core ≤ 0.2pp\` → broad-based softening; less BOJ cover to hike

\*\*Tokyo handling:\*\* Tokyo is noisier than National \*and\* currently running \~30-40bp below it across the board (April Tokyo core 1.5% vs National 1.4% headline / 1.5% Tokyo core / 1.5% Tokyo core-core all sub-2%, per stat.go.jp). Two implications for the script:

\- Widen each band ±10bp when labeling a Tokyo print (noise adjustment). The CALENDAR "\<1.9% leading-indicator" trigger becomes Tokyo \<1.95% core-core.  
\- Add a one-line comment in the status output: \`\# Tokyo currently runs \~30-40bp below National core; do not false-positive a Tokyo core 1.7% as hawkish — it's still soft relative to National 1.4%.\` The Tokyo bands are calibrated absolute, but the \*comparison\* to National matters more than the level.

Source authority for these levels: CALENDAR.md:12 (the \<1.9% threshold), STATUS.md:91 ("if core-core 1.9% slips further, 55% can break lower"), SAM-27 in PREDICTIONS.tsv (April print anchor: core 1.4% / core-core 1.9%, prior 1.8% / 2.4%), STRATEGY.md:168 (Tokyo leading 1.5% reference). All anchor values reconfirmed against live stat.go.jp / CNBC May 22 release.

Proceed with the build using the two-table scheme \+ divergence flag \+ Tokyo-vs-National comparison note. Same emoji status conventions as \`thresholds.py\` (🔴/🟠/🟡/🟢).  
