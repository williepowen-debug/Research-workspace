# System and fleet examination: a draft list of what to do, repair, build and investigate

Written 2026-11-16 12:12 ET by PROME (prome-6f) on Will's word in PROME's chat 12:09 ET: "please examine the system and our agents. Try to draft a list of what should be done, repaired, built, investigated, etc". A DRAFT for his choosing. Nothing here is approved, registered or started unless its row says so.

## Method and limits

A survey from existing instruments in about 15 minutes, not an audit. Sources: a per-desk pass over `AGENTS/*/` (last commit, STATUS size, inbox files, open DOCKET rows, live GATES rows), `scripts/read_cap_check.py` per desk, `scripts/ledger_staleness.py --all --quiet`, `PROME/DOCKET.tsv` (235 PENDING rows), `PROME/tools/forecast_report.py` (590 forecast rows), `PROME/ideas/list.tsv` (98 ideas), `git log` for 14 days, TERRY's STATUS and SETUPS, FORGE's header, this morning's gate output.

Not done: no desk's research was read for quality; no fleet-wide test run; the "last seen" dates come from commit history and are approximate (a desk can work without committing, and a subject-prefix match can mislabel a commit); trade results were not scored. Each row says what its evidence is.

## A. The three things most worth Will's attention

| # | Item | Evidence (2026-11-16) | Kind |
|---|---|---|---|
| A1 | **Research is not turning into positions.** The book is 71.45% cash. TERRY's last two sessions returned NO CARD on every packet (13 on 11/16). One approved hedge (HYG, 5 put spreads) is unfilled; one idea has its trigger met but fails its price cap ($5.25 to $6.14 against $4.90). Several strong findings have no listed instrument at all (United Fidelity, Car-Mart). Worth a one-time read by TERRY of the last 60 days of NO CARD verdicts by reason: no instrument, price cap, red-day rule, trigger not met, no directional owner. | `will_brief --book-line` (marks 11/10); `AGENTS/TERRY/STATUS.md` 11/16 and 11/13 blocks; SETUPS states: 17 conditional, 14 shelved, 12 not-fired, 12 fired, 11 approved, 3 lapsed. Trade results NOT scored here. | Investigate; needs Will's word (a new study) |
| A2 | **The coordinator is a third of all activity.** PROME made 943 of 3,090 commits in 14 days (31%); WALTER 290; the busiest research desk 127. 235 obligations are open; the roster file is 69,507 B. Worth asking which PROME duties produce nothing a desk or Will uses. | `git log --since='14 days ago'` by subject prefix; DOCKET count; `measure.py PROME/ROSTER.md`. Commit count is a rough proxy for effort. | Investigate, then trim (C12 covers PROME's own checks; anything wider is Will's) |
| A3 | **Forecasts carry a small real edge, and the most confident calls are the weakest.** Fleet Brier 0.223 against 0.249 for always quoting the hit rate (gain +0.026, range +0.001 to +0.047, overstated because calls share roots). Calls stated at 90% or more came true 6 times in 10. 59 of 300 decided calls have no usable probability: HENRY 37 decided with none, MIDAS 7 with none, FERT 6 of 8 without. CORAL (4) and CYPHER (8) have no decided call yet. Not read by the report: CARL and MARCO sub-ledgers, NEXUS monitors, TERRY's calibration file, ORACLE. | `forecast_report.py` run 12:1x ET, 590 rows, 33 desks | Repair (probabilities on HENRY and MIDAS calls) and investigate (the 90% bucket, n=10) |

## B. Repair

| # | Item | Evidence | Who / what it needs |
|---|---|---|---|
| B1 | Five desks hold unread packets and have not committed since 11/9 to 11/11: CREED (8 packets, 9 open rows), WAL (9 packets), GIBBS (8), FLG (5), OZK (5). GIBBS also has two of its own calendar rows past due (the Q3 holding-company filing window 11/14, its post-Q3 review 11/15) and nothing scheduled ahead, so nothing will wake it. | fleet survey; gate line "desk catalyst summons" | GIBBS: covered by the standing due-row rule, PROME wakes it. The other four: no due row, so a wake is a proposal (cost), Will's word |
| B2 | Six more desks not seen since 11/11, each with 1 to 3 packets waiting: AEOLUS, HAWK, MARCO, VIOLET, YURI, ZHAO. HANS and YURI are already scheduled for Wed 11/18. | fleet survey | Mostly resolves at their dated rows; listed so it is seen |
| B3 | ZHAO's knowledge base is 364,296 B, eleven times the read budget, and its boot tells it to read it. It cannot be read whole, so ZHAO boots on part of its own knowledge. | `read_cap_check.py --agent ZHAO` (🔴, boot-step line 29) | ZHAO at its next session: split hot and cold |
| B4 | Three desk charters are over the read budget: FALCON 158%, AEOLUS 156%, HOMER 128%. Near the limit: REGINALD's status 98%, CARL 95%, SAM and OSPREY 91%; FORGE 91% of its cap. One REGINALD board file is at 121%. | `read_cap_check.py` per desk; `measure.py` | Each owner at its next touch; PROME carries it in launch briefs |
| B5 | WALTER's signal index is 498,513 B, fifteen times the budget, and two charters name it as a read. Open since September. | DOCKET L388 | WALTER, next spec pass |
| B6 | Stale ledgers behind their desk's status: SAM's BIS liquidity series 59 days, LIQUID's gate-79 calendar 48 days, REGINALD's predictions 32 days and VX 34 days, MARCO's VX 32 days. | `ledger_staleness.py --all --quiet` | Each owner: refresh or freeze (root Data Hygiene) |
| B7 | A dry run of the SEC filing poller still writes FORGE files. Found 10/31, not fixed. | DOCKET L902 | PROME (FORGE owner) |
| B8 | One PROME test rewrites a tracked file when run (`test_session_panel.py` restamps `dashboard_build.json`). Found today. | observed 11:54 ET, restored from git | PROME, small |
| B9 | TERRY's closeout sweep misreads a timestamp with seconds as a clock time and can block a clean closeout. | ideas list 11/4 | DAEDALUS (owner), next sitting |
| B10 | RED has one routed signal unlogged for 3 days. Packets also sit unread at desks that are not running: YEYOU 4 (retired), BARON 1 (dormant), RAV 6 (special, Will-driven). (Corrected 2026-11-16 12:42 ET: the first text counted each folder's placeholder file and called RAV retired; RAV is a special desk Will runs on demand, and its packets stay. YEYOU's four were filed 2026-11-16 12:42 ET on Will's word, 79113fe4a3; BARON's stays as a to-do for any revival.) CATO's inbox holds 34 files back to 10/20. | gate line; fleet survey | RED at its next session; YEYOU's packets filed by PROME; CATO is Will's own adviser |
| B11 | PROME's own slips this morning share one cause: the right tool exists and the procedure in use did not route to it (commits made without the commit-checking wrapper; the plain file reader used at boot). | NOW page item 0; today's boot | PROME: put the wrapper command where mid-session commits happen (its own manuals, C13) |
| B12 | The obligations ledger is heavy: 235 open rows; its calendar view is 9 KB against a 6 KB budget; 37 rows carry no registration date; 4 rows wait on a Decision Deck that has been paused since 10/19. | DOCKET; `docket_view.py` | Will: retire the Deck for good (closes L523, L580, L663, L734) or resume it. PROME: prune under C12 |
| B13 | The Codex bridge's live test (repaired today, verified against a stand-in only), and its output should say in its own words that an empty list is not proof of absence. | DOCKET L907; reader finding 5 | PROME; the live test needs a Codex desk open |

## C. Build

| # | Item | Evidence | Who / what it needs |
|---|---|---|---|
| C1 | The "owner has not consumed this" boot line, approved 10/15 (WQ-401), not built a month later. | DOCKET L730 | PROME; already approved |
| C2 | News collection starts 4 to 8.6 hours late every day (the host's scheduler), so overnight stories arrive late; coverage of an 08:30 ET release depends on when a session starts. Unattended runs were offered and not opened. | WALTER's 11/12 answer packet (figures as of 11/12); NOW page | Will's word (an unattended run is his to open) |
| C3 | WATT: at boot, scan the grid's 5-minute price tape since the desk's last cutoff, so a price spike during a dark interval is found at the next boot instead of never. | ideas list 10/29 | Will's word |
| C4 | A rule for forecasts that have no registered measurement (so they close as no-verdict by rule instead of one at a time by hand). | ideas list 11/9, offered, not ruled | Will's ruling |
| C5 | Decisions app: one-step confirmation for tasks and process items, chat "yes" kept for money, trades and gates; a "recently decided" view of what PROME recorded. | ideas list 10/30 to 10/31 | For discussion; CATO builds |
| C6 | Laptop: raise its memory cap to match the desktop (about twice as many desk windows fit), and the two tokens already parked as WQ-687. | ideas list 11/11; WILL_QUEUE 687 | Will's hands |

## D. Investigate

| # | Item | Evidence | Who / what it needs |
|---|---|---|---|
| D1 | "Who is paying to extend": for each stressed credit the desks follow, name the party funding the delay and how long it can. Turns a loss-timing question that keeps slipping into a dated capacity question. | ideas list 11/11; OZK, FLG, BROCK and HOMER hold most inputs | Will's word; a commission |
| D2 | United Fidelity's dated tells: a regulator release about Thu 11/19, the plan date 12/14. County loan records need a person with a browser. | TERRY 11/16; DOCKET row dated 11/24 | Runs on its rows; the county search is Will's if he wants it |
| D3 | How Japan would fund a currency intervention: open between SAM, BOND and LIQUID. First data that could show it: Fed custody holdings 11/19; the ministry's total about 11/30. | NOW page item 10 | Existing rows |
| D4 | An independent read of SAM's SoftBank leverage estimate (22% to 24% against a 25% ceiling), which the AI-debt theme leans on. | ideas list 11/9, offered | Will's word |
| D5 | Coverage with no owner: Indian banks (second flag from CYPHER); a window in which a physical loss in the Gulf would go unread (HAWK); three AEOLUS items with no row (a gas price level, a seismic re-spec, a coastal thread). | DOCKET L868; ideas list 11/9 | Will's word on owners |
| D6 | Data walls: the Definite and MT Newswires connectors fail to connect; Quartr has no subscription; the CME site blocks this machine; the official fund stress data is delayed to 2027-07, leaving one funding leg unmeasured. | session connector errors; STATUS owner lanes; fleet memory | Paid data is Will's call; the rest is noted |
| D7 | Retire controls that nothing uses: the uncounted 250-line status caps at 14 desks; HENRY's boot scan that takes 2.7 of its 3 boot minutes and found nothing on 11/5; `rotation_integrity.py` (left on demand today). | ideas list 10/30, 11/5; today's census | First is PROME's; HENRY's needs Will's word |
| D8 | The routing map against actual traffic (which desks really send to which). | DOCKET L890 | A Will-gated root file |
| D9 | Two mis-filed asset-backed filings found by CREED: whether to tell the filer or the regulator. | ideas list 11/9 | An external send: only on Will's word |

## What PROME would do first, if Will picks nothing

GIBBS's wake (B1, standing authority). Then B7, B8 and B11 (PROME's own small repairs), C1 (already approved), and the retired desks' packets in B10. Everything marked "Will's word" waits.
