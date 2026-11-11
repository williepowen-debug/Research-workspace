# GPU-finance lane backlog triage, 2026-11-11 (Will 12:36 ET, "can we fix it now as opposed to tomorrow")

Input: `lane_gpu_obsolescence_headlines.tsv`, 115 unique titles from Research-Intake rows `gpu-obsolescence-1..4`, batches 10/11 to 11/10. Batch date is not event date: the 10/11 batch was the rows' first sweep and pulled older articles.

| Story group | Disposition | Basis |
|---|---|---|
| Lender pushback on Nvidia GPU collateral, 3–4y vs 10y underwriting | DUP | SIG-W-20261010-009 |
| Goldman/JPM decline $3.7B chip loan at 11% (Volta) | DUP | SIG-W-20261013-013, -1016-005; VULCAN, BROCK KB |
| CoreWeave $8.5B, $3.1B, $2.6B GPU loans; 2029 A100 contract | DUP | 16 BOARD cards; VULCAN, BROCK KB |
| Meta $279B leases, Hyperion | DUP | 9 BOARD cards |
| Burry useful lives, Huang response | DUP | 14 BOARD cards; VULCAN KB |
| Lambda loans; GMI Cloud $635M | DUP | SIG-W-20261020-011; -1010-009 |
| Big Tech $300B residual-value guarantees (FT) | DUP | SIG-W-20261010-009, -0627-033 |
| Broadcom $43.5B guarantee of Anthropic $63B | DUP | SIG-W-20261027-029 |
| Nscale cosigner, ING $500M loan sale, SpaceX $40B | DUP | -1104-040, -1106-004, -1105-047 |
| Ares CEO on GPU depreciation (call 10/29) | DISPATCH | SIG-W-20261111-020 |
| A. Nvidia $500B platform | KILL (stale) | Nvidia release 2026-08-10: MOUs only, "subject to execution of the final agreements"; "Nvidia signs $500B GPU bond deal" (Tech Times) unverified and misstates MOUs |
| B. $70B off-book AI guarantees | KILL (stale) | Briefs relaying Bloomberg 2026-08-15 |
| C. Neoclouds in equipment ABS (9fin) | DISPATCH | 10/8; SIG-W-20261111-021 |
| D. Korean banks, $83.1B GPU-backed deals | DISPATCH | 11/4–11/5; SIG-W-20261111-021; "$111B" is won/dollar confusion |
| E. Nebius $775M GPU-backed loan | KILL (stale) | Nebius release 2026-07-17 |
| F. USD.AI / Barker / Munich Re GPU-loan cover | KILL (stale) | Reinsurance News 2026-03-04 |
| G. S&P "contractual structures evolving" | KILL (stale, unverified) | Infrastructure Investor 2026-07-08 |
| Opinion and explainer pieces (CNBC, Yardeni, Verge, Seeking Alpha, crypto lending tokens, Google Needs More Money) | NO-ACTION | commentary, no new fact |

Method: WALTER grouped titles into stories and grepped BOARD plus VULCAN, BROCK and SHADE KBs; a Rule 9 Opus helper verified A–G at source (dates, figures, completed vs talk). WALTER did not open those pages itself. Group-to-title mapping was by hand and is not row-exact. From 2026-11-11 the intake scan lists new rows under GPU_FINANCE_REVIEW (BOOT_PROTOCOL 7e(g2)).
