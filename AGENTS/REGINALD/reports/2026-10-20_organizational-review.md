# REGINALD organizational review — October 20, 2026

Scope: Will requested boot and an explanation/assessment of REGINALD's organization. This is a review of the local checkout, not an organizational migration, new research program or approval request. References below describe files inspected this session; prior numerical observations keep their own dates.

## Judgment

REGINALD is a regional-bank synthesis and comparative-research desk. Its strongest organizational feature is specialist separation: regional-bank comparisons belong here, while named specialist desks own their bank judgments and upstream desks own their domain evidence. Its main weakness is accumulated documentation: the operating structure has evolved faster than the instructions and secondary summaries. A fresh session can recover an obsolete reporting relationship, repeat completed work or carry a stale state into a current brief.

Keep the present division of analytical responsibility. The first improvement should be instruction and ownership reconciliation, followed by reducing repeated state. More agents or another folder hierarchy are not justified by this review.

## Responsibility and authority

| Relationship | Actual role and boundary | Evidence |
|---|---|---|
| Will | Sets direction and approves trades and gated changes. Broker/Will evidence is position truth. | Root CLAUDE.md; USER.md |
| PROME | Coordinates fleet priorities, decisions and operator synthesis. Coordination does not transfer domain evidence ownership. | Root CLAUDE.md |
| REGINALD | Regional-bank watchlist and comparisons; multi-channel exposure matrix; FHLB advances; hidden-CRE classification; sponsor-bank balance-sheet exposure. | Local CLAUDE.md DOMAIN SCOPE; BANK_RESEARCH_STANDARD.md |
| WAL / OZK / FLG | Separate single-bank specialists. REGINALD consumes their work and supplies cohort context; it does not own their thesis versions or edit their records. | PROME/ROSTER.md; AGENTS/_NETWORK.md |
| GIBBS | Large-bank comparison desk: helps distinguish regional-specific pressure from an industry-wide move. Shared non-bank-finance figures reconcile with BROCK. | PROME/ROSTER.md; AGENTS/_NETWORK.md |
| CREED | Separate national CRE/CMBS desk in the Tier-2 roster. Launch requires Will's explicit permission; REGINALD's old subordinate wording grants no launch authority. | PROME/ROSTER.md Tier-2 row |
| Other upstream desks | Labor/consumer, Florida/housing, private credit/insurance, funding and rate/carry evidence feed the bank analysis. Their underlying domain judgments remain owner-held. | AGENTS/_NETWORK.md; local DOMAIN SCOPE |
| WALTER / NEXUS / VIOLET / RED / TERRY | WALTER routes signals; NEXUS synthesizes across domains; VIOLET evaluates the credit-to-volatility lag; RED challenges claims; TERRY constructs trades, with Will deciding. These are coordination interfaces, not REGINALD staff. | Root CLAUDE.md; AGENTS/_NETWORK.md |

The eight-channel convergence map describes possible transmission routes. It is not evidence that all eight are firing. STATUS's live thesis says severity is concentrated rather than tier-wide, and explicitly says only two channels are instrumented locally while the others remain owner-held. This distinction is central to the desk's design.

Local BELT/CREED/TEX/RENO trees are archived evidence, not an operating staff. BELT's historical mortgage-delinquency revival condition survives in SUB_AGENTS.md, but this does not independently authorize a launch or override roster/Will restrictions.

## Where the work lives

| Layer | Main files | Purpose |
|---|---|---|
| Instructions | Root CLAUDE.md, AGENTS.md, USER.md; PROME completion/playbook; local CLAUDE.md | Shared rules, operator preferences, runtime mechanics and desk charter |
| Current judgment | STATUS.md; BANK_EXPOSURE_MATRIX.md | Canonical thesis, observed levels and scores; matrix method and evidence |
| Continuity | MEMORY.md; ROADMAP.md; CALENDAR.md; LESSONS.md; optional SCRATCH.md | Handoff, open work, event dates, verified mistake patterns and temporary notes |
| On-demand detail | STATUS_DASHBOARD.md; STATUS_MATRIX.md; ROADMAP_BACKLOG.md | Expanded analysis and unstarted ideas, kept outside routine boot reads |
| Evidence | reports/; domain/sources/; workbook/ | Dated judgments, primary-source material and structured evidence/outcomes |
| Subject navigation | research/FHLB/; research/EGBN/; research/market-technicals/ | Topic entrypoints, evidence collections and dated data. These are subject folders, not agents. |
| Rules and intake | registry/THRESHOLDS.tsv + NOTES.md; registry/REG_T02_EXIT_LOG.tsv; inbox/; board/BOARD_LOG.tsv | Alarm definitions and basis, settled-close counts, incoming packets and consumption records |
| Outputs | NEXUS_BRIEF.md; TRADE.md; POSITIONS.md | Cross-domain synthesis, research-to-trade interface and broker-derived position context |
| History | archive/; retired thesis pointer stubs | Prior evidence and decisions. STATUS owns current thesis; CALENDAR owns dates. |

The FHLB hub mixes canonical reports and explicitly marked immutable copies. EGBN primarily collects copies/extracts whose originals remain authoritative. Both are useful navigation aids, but opening a convenient copy does not establish freshness. POSITIONS is a local mirror; it cannot supersede broker truth or PROME's structured FORGE mirror.

## How a session works

1. Resolve runtime/root and explicitly load shared and local instructions; check Git safety before pulling.
2. Recover STATUS → LESSONS → CALENDAR → MEMORY → ROADMAP. Read the bank-research standard for substantive research and recover prior expectations before forming a new judgment.
3. Refresh market context, settled-price ladder, ledger freshness and corrections; scan inbox and applicable BOARD signals. Fuller boot.py monitoring runs during the earnings window.
4. Compare evidence across banks. The research standard connects property → loan cash/recovery → accounting → earnings/book → regulatory capital → valuation → catalyst. Unknown layers remain unknown; no cash recovery is inferred from a disappearing loan row.
5. Save results, update the owning record, disposition intake, carry unresolved dependencies forward, then fold the NEXUS brief after final STATUS write-back. Signals go through WALTER; analysis goes to the appropriate owner's inbox; PROME requests go to root PROME/inbox/.

## Findings that matter

| Finding | Verified example | Consequence / recommended treatment |
|---|---|---|
| Instructions retain the old organization | Local opening calls CREED a sub-agent; SUB_AGENTS.md calls it a separate desk, assumes all sessions are Claude Code, omits WAL/FLG/GIBBS from its directory and prescribes direct signal delivery. Spawn boot card says never push; root specifies closeout safe-push. | Reconcile these instructions to root/roster/network canon. Keep responsibilities stable and do not invent new launch authority. |
| Current-facing summaries repeat older state | NEXUS opening contains today's HY FIRED result and a prior 2-of-3 paragraph; lower Nano row still schedules October 20 despite the next check now October 27. STATUS prediction prose still calls a REG-07 re-mark owed while MEMORY says VOID. | Replace repeated task/status text with a current synthesis and owner pointers. A fresh header does not make the body fresh. |
| Instructions have become expensive to recover | Local charter 45,337 bytes; five mandatory continuity files total 92,786 bytes, excluding root instructions, registry and specialist reads. | Shorten the charter by moving historical explanations to references. Keep essential rules at their point of use. File-size checks do not measure total boot context or understanding. |
| Completeness checks have limited coverage | Ledger check scans 16 declared ledgers and excludes 26 TSVs. VX has 62 rows, including 33 explicitly STALE; charter still says 27. Read-cap passes 12 inferred whole-read surfaces but excludes the explicitly read charter and has no REGINALD READS.tsv declaration. | Do not interpret a passing checker as proof of complete/current coverage. Reconcile the declared read and ledger perimeters before adding another check. No new checker proposed here. |
| Discovery paths lag the research | research/README.md still lists old Q1/KB repair gaps; MTB/STATUS.md is an April dashboard without the leading frozen banner present on its neighboring thesis. Current M&T work is in October reports. | Make existing indexes point to the current work; clearly mark historical bank material. Avoid moving files until inbound references and tool paths are checked. |
| Automation covers part of boot | boot.py runs eight market/filing scripts; it does not run the separate ladder, corrections, ledger/read-cap or inbox/BOARD steps. thresholds.py also carries hardcoded contextual levels rather than evaluating the full registry. | Describe boot.py as a monitoring sweep, not a complete organizational boot or official trigger grader. Any later integration should preserve source/basis and registered-rule distinctions. |
| Documentation follows attention more easily than outcomes | The existing October 20 key-file audit found funding and settled-exit follow-through still owed despite extensive research delivery; this session did not complete those research tasks. | At existing reads, close the original expectation/outcome and dated obligation before expanding coverage. Preserve the October 13 research standard. |

## Recommended order — proposals only

1. Reconcile local organizational/runtime/routing instructions against existing canon, including CREED permission and the three single-bank peers.
2. Establish one current statement per thesis, task and rule state; reduce mirrors in STATUS/MEMORY/ROADMAP/NEXUS/TRADE and improve current-versus-historical navigation.
3. Reduce boot context and document what each existing check actually covers. Preserve deeper evidence for task-specific reads.

This is a proposed local documentation cleanup, not a recommendation to create/revive desks, change the bank cohort or reorganize canonical agent directories. No approval is required to understand this report; implementation was not part of this assignment.

## Boot receipt and limits

- Desk REGINALD; OpenAI Codex / GPT-6 family, exact variant UNKNOWN; session 01a15b3f-a3a2-72e0-849c-219e82d05a2d; root /home/willi/Research-workspace; launch cwd AGENTS/REGINALD. Shell/files/Git/Python and web available. Thread-local collaboration exists; no fleet-wide cross-runtime discovery or live messaging to independently launched owners verified. No agents launched.
- Shared/local instruction loading was explicit. Startup pull withheld under the root dirty-owner rule because DAEDALUS and WALTER had uncommitted paths. This review therefore concerns the local checkout; unseen remote changes are not assessed.
- Separate market refresh succeeded; vendor quotes have unverified quote clocks/delay and are not formal settled grades. FLG detector returned rc1 for the existing RED state: October 19 settled close $10.96, nine closes below RED; October 20 excluded. No new rule, score, forecast or trade action.
- Corrections check: zero unreceipted named rows, not proof of correct application. Ledger/read-cap limits are stated above. Fuller monitoring receipt is retained beside this report.
- A new WALTER housing-affordability/spread-basis INFO packet (SIG-W-20261020-028) was read for awareness. HOMER owns its requested analysis; no bank grade, monitor or threshold follows from it. Intake disposition and final persistence receipt follow in session write-back.
- This review used local source/configuration evidence rather than external financial research. No claim of live owner-session liveness, peer consumption, completed owed bank research or organizational change is made.

### Final session write-back

Full monitoring: seven scripts OK, one filing ALERT (CFG/OZK/WAL/ZION). OZK newly posted its Q3 earnings package; its items are UNPARSED by the monitor and this organizational review does not grade it. Dark-pool off-exchange values are NO DATA despite script OK; short-interest observations remain September 29. Frozen feeds were not appended; boot updated only the KRE float cache. Full output: `2026-10-20_organizational-review_boot.txt`.

WALTER INFO intake disposition logged and packet moved to processed. STATUS/continuity pointers updated without implementing the recommendations; no new research outcome or figure superseded. NEXUS fold follows STATUS persistence. No external send or peer notification.
