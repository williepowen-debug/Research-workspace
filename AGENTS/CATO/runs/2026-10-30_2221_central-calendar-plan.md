# Central calendar draft plan

**October 30, 2026 · CATO · Draft for discussion; implementation not commissioned.**

Build a calendar that answers: **What matters this week, what does it mean for our research and recorded positioning, and which agents have work around it?** The proposed first version is a local Calendar window opened from the Agent Launcher. It combines economic events, scheduled agent work and dated research follow-ups, with links back to their sources and results. The sketch waits until the Decisions desk passes its independent re-check; passing that review does not itself commission calendar work.

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
| 0. Sequence | Decisions desk independent re-check passes; calendar work separately commissioned | CATO preserves the frozen Decisions build during review. No calendar sketch or implementation starts automatically. |
| 1. Layout and source sample | Reviewable Week/Today/details sketch of one real week; representative preserved records from the proposed feeds | Will can assess default research visibility with housekeeping hidden, then toggle it on. Gate/card relevance and its source date are legible. Every item is traceable; missing fields and coverage are explicit. |
| 2. Calendar data reader | Normalized snapshot with source provenance, event-to-work links and refresh diagnostics | Real-source fixtures cover date-only items, windows, time zones, moved dates, duplicate feeds, conflicting records, missing files and malformed rows. No source files change. |
| 3. Desktop window | Week, Month, Today, filters, details and source/research opening | Opens through the existing launcher; navigation stays responsive while refreshing; long titles and overlapping entries remain readable on desktop and laptop. |
| 4. Launcher handoff | Editable assignment and verified owner-preflight path | Fake launches test correct desk/context, cancellation, repeat clicks, an owner already running outside the launcher, unknown discovery and a session appearing after preparation. Only a successful preflight at Start permits a new session; preparation starts nothing. |
| 5. Review and ordinary use | Applicable independent acceptance plus a brief real-use walkthrough | Source coverage and failure cases are checked; Will can find the next relevant event, identify owed agent work and open its evidence without searching repo files. Record actual usefulness and any remaining limitations. |

Stages describe a proposed build sequence, not current authorization or a time estimate. Architecture recommendation: reuse the launcher's existing local Windows/WSL support, with a separate calendar reader and UI module so source refresh cannot block the launcher. Confirm the actual control/layout choice during the sketch; no new hosting or external calendar service is needed for the initial scope.

Possible later additions: optional reminders, calendar export, broader event coverage, richer result history, or scheduled launches under a separately agreed policy. They are deferred until ordinary use identifies a need. Position relevance from existing dated records is in the first version; personal-calendar and broker-data integration are not.

## Current assessment and resume point

The likely benefit is less manual searching between events, agent obligations and resulting research. The principal implementation risk is reconciling inconsistent source records while preserving their meaning; the visible calendar grid is the simpler part. A modest, explicitly covered source set is sufficient for a useful first version.

**Revised plan delivered; sketch waits for Decisions acceptance.** Next CATO action is to discuss Will's changes to this draft. After the Decisions re-check passes and Will commissions calendar work, begin with the one-week layout and representative source sample. Resolve housekeeping classification, explicit gate/card relationships and the supported owner-preflight interface before integration. No owner task, send, launch or application change has been made by this planning assignment. Existing unrelated approvals survive.

## Evidence and delivery record

Baseline: `master` at `c0687f8b73616146ace0780a324a068ca90de8d0`; working tree and index were clean at planning inspection. This is CATO-authored design work, not independent implementation acceptance.

Inspected references: `scripts/AGENT_LAUNCHER.md` due-work, platform and Research/Decisions pointers; `PROME/tools/spawn_list.py` contract and CLI options; `PROME/tools/spawn_slate.py` source/return contract and options; current `SUMMONS_LEDGERS` registration; `PROME/state/CALENDAR.md` generator header; relevant roster owner rows; HENRY's calendar header and sample records plus its October 21 refresh packet. Prior calendar review `2026-10-20_calendar-review.md` supplies the accepted generated-view history and limits; its settled findings were not reopened.

These reads establish existing interfaces and documented limits. No live economic dates were externally reverified, full fleet coverage audited, application built or runtime behavior newly certified. Examples in this plan are illustrative.

Delivery checks: verified existence/readability of all ten inputs. Weekday check clean on `PROME/DOCKET.tsv`, `PROME/GATES.tsv`, `PROME/WILL_QUEUE.md`, `AGENTS/CATO/CONTINUITY.md` and this plan; glued-date check clean on the two changed CATO documents. Read-cap check covers exactly `AGENTS/CATO/AGENTS.md`, `AGENTS/CATO/CHARTER.md`, `AGENTS/CATO/CONTINUITY.md`, `CLAUDE.md`, `USER.md`, `AGENTS.md`: all below the cap, with root CLAUDE's existing 75%-tier advisory. No CATO STATUS/calendar/catalyst input exists to include. Orphan advisory clean; no work outside CATO, no staged paths, and whitespace check clean. No memory, ledger or superseded-figure check condition arose. Only this plan and continuity are intended for commit. Publication receipt is delivered in-session; there is no app to publish.

## October 30 follow-up on PROME feedback

Will relayed PROME's review. Incorporate its four recommendations as draft design changes: Decisions first, housekeeping hidden by default, explicit gate/trade-card relevance, and canonical duplicate-owner preflight at actual Start. PROME's quoted 61 undated/16 overdue counts are owner-reported snapshots, not a CATO census or a design constant. PROME's statement that Decisions still had two defects predates CATO's repair handoff: author repairs are frozen at `f7b03a732`; independent re-check remains pending, so the sequencing recommendation still applies. No fresh Decisions audit or edit was triggered.

Bounded reference reads confirm the existing gates state contract carries ticker relevance, TERRY's position-intake contract refuses to establish holdings from memory, and the launcher documents limited lock coverage. No current holdings, gate fires or live event dates were verified. Source reuse reduces duplicate maintenance but does not guarantee correct/current records; the plan preserves that distinction. No owner sends, launches, new implementation or build authorization followed from this feedback. Check coverage for this two-document revision remains the ten named inputs above; publication is delivered in-session.
