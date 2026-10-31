# Central calendar draft plan

**October 30, 2026 · CATO · Updated October 31: one-week sketch delivered; production implementation not commissioned.**

Build a calendar that answers: **What matters this week, what does it mean for our research and recorded positioning, and which agents have work around it?** The proposed first version is a local Calendar window opened from the Agent Launcher. It combines economic events, scheduled agent work and dated research follow-ups, with links back to their sources and results. Will’s October 31 relay permits the sketch alongside the Decisions review if no frozen build/dependency file changes; full calendar implementation remains uncommissioned.

Will requested a plan after discussing the idea. The working assumption is that it should support both morning planning and occasional checks during the day. Week view is the default. This assumption can change during discussion without changing the underlying source work.

## First version experience

| View | Purpose and behavior |
|---|---|
| Week | Main planning view. Timed events appear at their Eastern time; date-only obligations sit in a separate area. Previous, next and Today navigation. |
| Month | Look ahead for clusters of releases and work. Short labels and counts open the selected day's agenda. |
| Today | Relevant events in time order, followed by due agent work. Earlier unresolved work has its own collapsible list. |
| Details | Plain-language title, why it matters, linked gate or trade-card relevance with source date, time or date window, owner and other involved desks, related assignments, source and verification caveats, and links to available research. |

Four independently selectable layers: **Market events**, **Desk research**, **Research follow-ups**, and **System housekeeping**. The first three are on by default; housekeeping is off. Process repairs, maintenance and review administration belong on housekeeping even when a domain desk owns them. PROME-owned market research remains visible: ownership alone does not classify an item as housekeeping. Use explicit source classifications where available, otherwise a small reviewed mapping bound to source records; no keyword-only hidden-row decisions. Unclassified items remain visibly counted and accessible for inspection.

Search and filters narrow by agent and research theme. Theme tags come from explicit source fields or a small reviewed mapping; the application does not invent significance from keywords. A date window stays a window; an unknown time never becomes midnight. Undated work remains accessible in a separate list, without fake calendar dates. Overdue research remains visible in its own list; overdue process work follows the housekeeping toggle. A compact count makes hidden housekeeping discoverable without filling the default calendar with it.

Illustrative interaction, not a live schedule: select an employment release, read its relevance, see LABOR's linked assignment and HENRY's downstream read if recorded, then open the relevant source or prepare that agent in the launcher. Later, return to the same item to open explicitly linked research. Opening a document does not mark its assignment complete.

Use concise text labels and modest category styling. Existing severity colors keep their established meanings. The default should make the next week readable without hiding overdue or unavailable information.

## Sources and ownership

| Information | Existing source to reuse | Integration requirement |
|---|---|---|
| Economic releases and their relevance | HENRY's `domain/ECON_CALENDAR.md` | Preserve verification window and source-specific caveats. HENRY retains its calendar content. This is an initial economic feed, not a complete global calendar. |
| Scheduled obligations | PROME `DOCKET.tsv`, through existing parsing/export logic | Reuse the versioned `spawn_list.open` export where suitable. It includes open work but covers DOCKET only. Preserve full owner text and annotations. |
| Dated review obligations | PROME `GATES.tsv` | Include explicit review dates via an isolated reader; a conditional trigger with no date belongs outside the dated grid. Review dates are not economic releases. |
| Desk catalysts | Ledgers registered in `PROME/tools/prome_gate.py` under `SUMMONS_LEDGERS` | Enumerate the current registry during implementation and support its actual schemas. Show the included sources; do not claim every desk calendar is covered. |
| Wake context | Existing `spawn_list.py`, `spawn_slate.py`, roster and launcher behavior | Preserve the distinction between due work, a candidate for a wake, and a verified running session. Reuse owner rules rather than creating a new schedule policy. |
| Research results | Explicit source references and existing Research viewer | Show a link when recorded. A related commit or document mention is only a pointer, not proof the work was completed. |
| Gate and position relevance | Explicit links in PROME `GATES.tsv` and TERRY's dated trade cards | Carry the gate/card ID, exact stated relationship, source date and recorded proposal/position status. Resolve actual supported card fields during the source sample; neither a ticker match nor an old proposed trade establishes a current holding. |

PROME already has `state/CALENDAR.md`, generated from DOCKET. It is useful prior capability, but reading both it and DOCKET as independent feeds would double-count the same records. The app should consume original records through supported readers.

The calendar is a view of owner-maintained records. Rescheduling and completion changes continue at their authoritative sources. No second manually maintained event database is proposed. This reduces duplicate-maintenance drift; it cannot make a stale or incorrect source current. CATO would own the application work if commissioned; PROME and desks retain scheduling and source-content authority. Any required owner export change must have an explicit owner and bounded scope before implementation.

## Event relevance to positioning

Each relevant event can carry a short **Why it matters** line linked to an existing gate or trade card. Illustrative wording: “Linked review: HY gate; see its registered condition” or “Relevant to the QQQ put thesis in TERRY's dated card.” The card supplies the mechanism and condition; the calendar does not infer either from a ticker or an event title. A scheduled release is not proof that a gate fired.

Keep a proposed trade, previously recorded position and verified current holding distinct. If current holdings are unverified, say so beside the relationship and use thesis/card wording rather than “your current position.” Preserve the source's date, contract scope and qualifications. Broker access, fresh prices, position valuation, trade recommendations and execution remain outside this version. Missing links say that no relationship is recorded, not that the event is irrelevant. This feature supplies event context; it does not add expiry reminders or repeated sell-or-roll prompts.

## Data behavior that makes the calendar dependable

- Keep event identity separate from assignment identity. One release can link to several desk assignments; those assignments can have different due times and completion states.
- Use explicit identifiers and source links to join records. When identity is uncertain, retain separate entries instead of silently merging similar titles. Different release periods must stay separate.
- Preserve source path, row identity, original text and snapshot revision. DOCKET physical line references can move; never treat a line number alone as permanent identity across refreshes.
- Keep release time, preparation time, due date and review window distinct. Do not invent a standard pre-release wake or a recurring wake from cadence alone.
- Display Eastern time with daylight-saving handling. Retain original zones where supplied; unresolved zone assumptions stay visible.
- Refresh on opening and on demand, in a bounded background worker. Show when records were read separately from when their dates were last verified. Reading an old file now does not make its contents current.
- If a source fails or cannot be parsed, keep usable sources visible and identify the missing coverage. A retained prior snapshot must be labelled stale. Empty and unavailable must look different.
- Display conflicting dates with their sources until resolved by the owner. Never silently choose the newest file modification time as authority.
- Show recorded work status. Due work, recorded assignment, a linked return and accepted completion are distinct; the UI must not infer live presence or acceptance.

## Agent actions

The first version offers **Open source**, **Open research**, and **Prepare in launcher**. Preparing selects the desk and carries the dated assignment plus source references into an editable prompt; preparation starts nothing.

Any calendar-origin launch must pass the same-minute, same-host duplicate-owner preflight required by `PROME/CLAUDE.md` before the session starts. Recheck at Start, not only when the prompt was prepared. Evidence must identify possible writers across the runtimes in use; a known running, idle or approval-blocked owner prevents a duplicate launch. Incomplete or unavailable discovery is UNKNOWN and blocks starting a new owner. The draft remains available while that condition is resolved. Launch eligibility and the existing assignment's approval remain separate requirements.

The launcher's current file lock covers sessions launched through that mechanism; its documentation explicitly excludes manually opened, detached and other-machine sessions. That lock is insufficient to satisfy this requirement by itself. During source/interface planning, identify the supported owner-preflight path with PROME. Until that path is verified, Calendar may prepare a draft but cannot offer an ungated Start. No independent calendar liveness service or automatic message to an existing owner is proposed.

The application does not run PROME's operational boot or closeout to refresh its display. Shared collectors must be called through isolated, read-only interfaces. No scheduled spawning, background model calls, automatic docket edits or outbound reminders are included in this draft.

## Delivery stages and acceptance

| Stage | Deliverable | Completion condition |
|---|---|---|
| 0. Sequence | Sketch can proceed outside the Decisions frozen build; full calendar implementation remains separately commissioned | CATO preserves every frozen build/dependency file during review. Sketching does not authorize integration or changes to that build. |
| 1. Layout and source sample | Reviewable Week/Today/details sketch of one real week; representative preserved records from the proposed feeds | Will can assess default research visibility with housekeeping hidden, then toggle it on. Gate/card relevance and its source date are legible. Every item is traceable; missing fields and coverage are explicit. |
| 2. Calendar data reader | Normalized snapshot with source provenance, event-to-work links and refresh diagnostics | Real-source fixtures cover date-only items, windows, time zones, moved dates, duplicate feeds, conflicting records, missing files and malformed rows. No source files change. |
| 3. Desktop window | Week, Month, Today, filters, details and source/research opening | Opens through the existing launcher; navigation stays responsive while refreshing; long titles and overlapping entries remain readable on desktop and laptop. |
| 4. Launcher handoff | Editable assignment and verified owner-preflight path | Fake launches test correct desk/context, cancellation, repeat clicks, an owner already running outside the launcher, unknown discovery and a session appearing after preparation. Only a successful preflight at Start permits a new session; preparation starts nothing. |
| 5. Review and ordinary use | Applicable independent acceptance plus a brief real-use walkthrough | Source coverage and failure cases are checked; Will can find the next relevant event, identify owed agent work and open its evidence without searching repo files. Record actual usefulness and any remaining limitations. |

Stages describe a proposed build sequence, not current authorization or a time estimate. Architecture recommendation: reuse the launcher's existing local Windows/WSL support, with a separate calendar reader and UI module so source refresh cannot block the launcher. Confirm the actual control/layout choice during the sketch; no new hosting or external calendar service is needed for the initial scope.

Possible later additions: optional reminders, calendar export, broader event coverage, richer result history, or scheduled launches under a separately agreed policy. They are deferred until ordinary use identifies a need. Position relevance from existing dated records is in the first version; personal-calendar and broker-data integration are not.

## Current assessment and resume point

The likely benefit is less manual searching between events, agent obligations and resulting research. The principal implementation risk is reconciling inconsistent source records while preserving their meaning; the visible calendar grid is the simpler part. A modest, explicitly covered source set is sufficient for a useful first version.

**One-week sketch delivered; await Will's layout judgment.** Will subsequently directed the sketch to proceed while PROME reviews Decisions. [Open the preview](../prototypes/calendar/week-sketch/index.html); the October 31 delivery below records its bounded coverage and checks. The source selection, housekeeping mapping and explicit gate/card examples are demonstrated in a frozen sample. Production reading, source refresh and the supported owner-preflight interface remain future work, requiring commissioning. Existing unrelated approvals survive.

## Evidence and delivery record

Baseline: `master` at `c0687f8b73616146ace0780a324a068ca90de8d0`; working tree and index were clean at planning inspection. This is CATO-authored design work, not independent implementation acceptance.

Inspected references: `scripts/AGENT_LAUNCHER.md` due-work, platform and Research/Decisions pointers; `PROME/tools/spawn_list.py` contract and CLI options; `PROME/tools/spawn_slate.py` source/return contract and options; current `SUMMONS_LEDGERS` registration; `PROME/state/CALENDAR.md` generator header; relevant roster owner rows; HENRY's calendar header and sample records plus its October 21 refresh packet. Prior calendar review `2026-10-20_calendar-review.md` supplies the accepted generated-view history and limits; its settled findings were not reopened.

These reads establish existing interfaces and documented limits. No live economic dates were externally reverified, full fleet coverage audited, application built or runtime behavior newly certified. Examples in this plan are illustrative.

Delivery checks: verified existence/readability of all ten inputs. Weekday check clean on `PROME/DOCKET.tsv`, `PROME/GATES.tsv`, `PROME/WILL_QUEUE.md`, `AGENTS/CATO/CONTINUITY.md` and this plan; glued-date check clean on the two changed CATO documents. Read-cap check covers exactly `AGENTS/CATO/AGENTS.md`, `AGENTS/CATO/CHARTER.md`, `AGENTS/CATO/CONTINUITY.md`, `CLAUDE.md`, `USER.md`, `AGENTS.md`: all below the cap, with root CLAUDE's existing 75%-tier advisory. No CATO STATUS/calendar/catalyst input exists to include. Orphan advisory clean; no work outside CATO, no staged paths, and whitespace check clean. No memory, ledger or superseded-figure check condition arose. Only this plan and continuity are intended for commit. Publication receipt is delivered in-session; there is no app to publish.

## October 30 follow-up on PROME feedback

Will relayed PROME's review. Incorporate its four recommendations as draft design changes: Decisions first, housekeeping hidden by default, explicit gate/trade-card relevance, and canonical duplicate-owner preflight at actual Start. PROME's quoted 61 undated/16 overdue counts are owner-reported snapshots, not a CATO census or a design constant. PROME's statement that Decisions still had two defects predates CATO's repair handoff: author repairs are frozen at `f7b03a732`; independent re-check remains pending, so the sequencing recommendation still applies. No fresh Decisions audit or edit was triggered.

Bounded reference reads confirm the existing gates state contract carries ticker relevance, TERRY's position-intake contract refuses to establish holdings from memory, and the launcher documents limited lock coverage. No current holdings, gate fires or live event dates were verified. Source reuse reduces duplicate maintenance but does not guarantee correct/current records; the plan preserves that distinction. No owner sends, launches, new implementation or build authorization followed from this feedback. Check coverage for this two-document revision remains the ten named inputs above; publication is delivered in-session.


## October 31 sequencing update

Will relayed PROME's instruction that calendar sketch and ORACLE launcher preset work may continue in parallel if no file in the frozen Decisions build changes. Preserve that permission; it supersedes the prior sketch wait condition. Full calendar implementation, deployment and owner scheduling changes are not inferred. This update reconciles the plan only; no sketch, launcher change or source audit was performed.

## October 31 — one-week sketch delivery

Will's subsequent “okay go ahead and proceed” commissioned the suggested real-week sketch. **Recommendation: judge the Week layout and the details panel before commissioning the reader.** The useful first interaction is Monday's HENRY gamma assignment: deadline, conditional wake and explicit dated QQQ relationship together. Source interpretation, rather than calendar drawing, remains the material implementation risk.

Delivered [self-contained preview](../prototypes/calendar/week-sketch/index.html), [preserved sample](../prototypes/calendar/week-sketch/snapshot.json), [author checks](../prototypes/calendar/week-sketch/checks.json), and desktop/narrow captures under the same directory. Week, Day, Today, layer toggles and modal source details work locally. Today outside the sample explicitly means unavailable coverage. No network fetch, writes, agent launch or launcher integration occurs. The Windows Chrome desktop open request returned success; user viewing and usefulness remain unobserved.

Scope: November 2–8, 2026, snapshot `db5226357f67390cf7b4dc4abef55047851f4c16`. Twenty-two curated cards preserve 34 source-row references: eight market, eight desk research, three research follow-up and three housekeeping. Default visibility is 19. HENRY, DOCKET, GATES, LABOR, VIOLET, CYPHER and one TERRY card are sampled; remaining registered ledgers and rows are explicitly omitted. This fixture is not the proposed live reader or a new schedule of record. No owner sources, frozen Decisions artifacts/dependencies or launcher files were edited. WALTER and PROME had concurrent dirty/staged work; it was preserved.

The supported read-only export was `python3 -B PROME/tools/spawn_list.py --open --json --as-of 2026-10-31 --docket db5226357f67390cf7b4dc4abef55047851f4c16:PROME/DOCKET.tsv`. Its `spawn_list.open` v1 output contains 204 open rows; 51 have a parsed due date in the selected week, 56 no parsed date, 18 overdue before October 31. These are dated source counts, not complete calendar coverage. The parser's range-end date is preserved separately from presentation. The older owner-reported 61/16 figures remain historical, not a discrepancy to repair.

Consequential source examples and decisions:

- L575's November 6 date is explicitly an early-November placeholder. It appears outside the dated grid, with the actual release as the wake dependency.
- L180 retains both November 5 access expiry and November 7 cohort-screen deadline; L895's separate four-bank tail remains its own obligation. Credential/decision state was not freshly checked.
- L888's before-open deadline is distinct from roughly 06:00–07:00 input availability and a conditional wake. HENRY's running status is unknown. TERRY's October 22 card explicitly links gamma evidence and records an October 23 fill; current holdings are unverified.
- Gate reviews use their owner-set review dates; neither review dates nor adjacent economic releases are portrayed as gate fires. GATES_README's review/consumer semantics govern this distinction.
- L170 illustrates why an overdue open row does not prove undone work: its partial grade and 10-Q successor remain visible. No repeat work is assigned.
- Housekeeping is explicitly mapped by purpose: L143, L893 and L37/GATE-OP-SCALE-01, including the TERRY-owned governance row. Unselected rows are not silently classified.

Primary schedule reads on October 31: [BLS November](https://www.bls.gov/schedule/2026/11_sched.htm) confirms JOLTS November 3 at 10:00, productivity November 5 at 08:30 and jobs November 6 at 08:30 ET; [BEA](https://www.bea.gov/news/schedule/full) confirms trade November 4 at 08:30; [ISM](https://www.ismworld.org/supply-management-news-and-reports/reports/rob-report-calendar) has readable November dates 2/4 at 10:00. The Services table-read uncertainty is therefore resolved for this sketch, with HENRY's original caveat preserved and no owner edit/send. Claims remains pattern-only; the election date remains VIOLET-recorded, not independently verified by CATO. No prices, gate grades or holdings were reverified.

Author validation: exact revision/line/excerpt and file SHA-256 checks pass for all 34 source references; 22 IDs are unique; November 2–8 Eastern offsets are EST. Native Chrome passed ten assertions at each of 1520×1140 and 600×1100: defaults, event/assignment join, housekeeping toggle, undated/placeholder/window/overdue separation, qualified card relevance, Day selection, out-of-sample Today, native modal open/close, Week horizontal overflow and absence of write/launch controls. Captures visually inspected. Initial Windows/WSL transport failures were retried, not counted as passes. A 430px capture clipped due to the native minimum layout width; final narrow evidence is 600px. No independent review or actual mobile-device claim.

Reconciliation: the authorized sketch implementation and author verification are complete. Will's remaining action is a layout/usefulness judgment; closure is whether the week, due work and relevance are understandable. Full reader/integration remain proposed, not owed implementation. If commissioned, CATO must cover the unsampled schemas and failures, classification inventory, refresh, and supported same-minute duplicate-owner preflight before offering launch. PROME retains the Decisions review; this work changes neither its candidate nor acceptance. No new owner obligation, message, recurring job or trade decision was created.

Delivery checks: existence/readability established for all intended inputs. Weekday clean on `PROME/DOCKET.tsv`, `PROME/GATES.tsv`, `PROME/WILL_QUEUE.md`, CATO `CONTINUITY.md`, this report and the sketch `README.md`; glued clean on those three CATO documents. Exact-source validation covers the raw excerpts preserved in JSON/HTML instead of rewriting owner annotations. Read-cap covers CATO `AGENTS.md`, `CHARTER.md`, `CONTINUITY.md` and root `CLAUDE.md`, `USER.md`, `AGENTS.md`: all below cap, root CLAUDE retains the 75%-tier advisory. No CATO STATUS/calendar/catalyst input exists to include. Orphan advisory flags only HENRY's untracked `research/2026-10-31_L616_breadth/` at the check, left untouched and flagged to Will in delivery; CATO has no self-authored external packet. No memory, ledger or superseded-figure condition arose. Whitespace clean. Concurrent commits advanced shared HEAD after the pinned sample; the preview remains visibly frozen at its named revision. Publication receipt is delivered in-session. Publication is the sketch only, not a live calendar service.
