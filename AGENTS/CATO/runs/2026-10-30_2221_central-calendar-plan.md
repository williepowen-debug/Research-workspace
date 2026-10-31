# Central calendar draft plan

**October 30, 2026 · CATO · Draft for discussion; implementation not commissioned.**

Build a calendar that answers: **What matters this week, why does it matter, and which agents have work around it?** The proposed first version is a local Calendar window opened from the Agent Launcher. It combines economic events, scheduled agent work and dated research follow-ups, with links back to their sources and results.

Will requested a plan after discussing the idea. The working assumption is that it should support both morning planning and occasional checks during the day. Week view is the default. This assumption can change during discussion without changing the underlying source work.

## First version experience

| View | Purpose and behavior |
|---|---|
| Week | Main planning view. Timed events appear at their Eastern time; date-only obligations sit in a separate area. Previous, next and Today navigation. |
| Month | Look ahead for clusters of releases and work. Short labels and counts open the selected day's agenda. |
| Today | Relevant events in time order, followed by due agent work. Earlier unresolved work has its own collapsible list. |
| Details | Plain-language title, why it matters, time or date window, owner and other involved desks, related assignments, source and verification caveats, and links to available research. |

Three independently selectable layers: **Events**, **Agent work**, and **Follow-ups**. Search and filters narrow by agent and research theme. Theme tags come from explicit source fields or a small reviewed mapping; the application does not invent significance from keywords. A date window stays a window; an unknown time never becomes midnight. Undated work remains accessible in a separate list, without fake calendar dates.

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

PROME already has `state/CALENDAR.md`, generated from DOCKET. It is useful prior capability, but reading both it and DOCKET as independent feeds would double-count the same records. The app should consume original records through supported readers.

The calendar is a view of owner-maintained records. Rescheduling and completion changes continue at their authoritative sources. No second manually maintained event database is proposed. CATO would own the application work if commissioned; PROME and desks retain scheduling and source-content authority. Any required owner export change must have an explicit owner and bounded scope before implementation.

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

The first version offers **Open source**, **Open research**, and **Prepare in launcher**. Preparing selects the desk and carries the dated assignment plus source references into an editable launch prompt. Starting the session remains the existing explicit launcher action, using its current eligibility and duplicate-session protections and their disclosed limits.

The application does not run PROME's operational boot or closeout to refresh its display. Shared collectors must be called through isolated, read-only interfaces. No scheduled spawning, background model calls, automatic docket edits or outbound reminders are included in this draft.

## Delivery stages and acceptance

| Stage | Deliverable | Completion condition |
|---|---|---|
| 1. Layout and source sample | Reviewable Week/Today/details sketch; representative preserved records from the proposed feeds | Will can assess the layout and information density. Every displayed item can be traced to a source; missing fields and coverage are explicit. |
| 2. Calendar data reader | Normalized snapshot with source provenance, event-to-work links and refresh diagnostics | Real-source fixtures cover date-only items, windows, time zones, moved dates, duplicate feeds, conflicting records, missing files and malformed rows. No source files change. |
| 3. Desktop window | Week, Month, Today, filters, details and source/research opening | Opens through the existing launcher; navigation stays responsive while refreshing; long titles and overlapping entries remain readable on desktop and laptop. |
| 4. Launcher handoff | Editable assignment passed to the existing launcher | Fake-launch checks prove correct desk and exact assignment context, cancellation and repeat-click behavior. Opening or preparing an item starts no agent. |
| 5. Review and ordinary use | Applicable independent acceptance plus a brief real-use walkthrough | Source coverage and failure cases are checked; Will can find the next relevant event, identify owed agent work and open its evidence without searching repo files. Record actual usefulness and any remaining limitations. |

Stages describe a proposed build sequence, not current authorization or a time estimate. Architecture recommendation: reuse the launcher's existing local Windows/WSL support, with a separate calendar reader and UI module so source refresh cannot block the launcher. Confirm the actual control/layout choice during the sketch; no new hosting or external calendar service is needed for the initial scope.

Possible later additions: optional reminders, calendar export, broader event coverage, richer result history, or scheduled launches under a separately agreed policy. They are deferred until ordinary use identifies a need. No personal calendar or broker-position integration is proposed.

## Current assessment and resume point

The likely benefit is less manual searching between events, agent obligations and resulting research. The principal implementation risk is reconciling inconsistent source records while preserving their meaning; the visible calendar grid is the simpler part. A modest, explicitly covered source set is sufficient for a useful first version.

**Plan delivered.** Next CATO action is to discuss Will's changes to this draft. If he commissions the build, begin with the layout and representative source sample, resolving any required owner interface work before integration. No owner task, send, launch or application change has been made by this planning assignment. Existing unrelated approvals survive.

## Evidence and delivery record

Baseline: `master` at `c0687f8b73616146ace0780a324a068ca90de8d0`; working tree and index were clean at planning inspection. This is CATO-authored design work, not independent implementation acceptance.

Inspected references: `scripts/AGENT_LAUNCHER.md` due-work, platform and Research/Decisions pointers; `PROME/tools/spawn_list.py` contract and CLI options; `PROME/tools/spawn_slate.py` source/return contract and options; current `SUMMONS_LEDGERS` registration; `PROME/state/CALENDAR.md` generator header; relevant roster owner rows; HENRY's calendar header and sample records plus its October 21 refresh packet. Prior calendar review `2026-10-20_calendar-review.md` supplies the accepted generated-view history and limits; its settled findings were not reopened.

These reads establish existing interfaces and documented limits. No live economic dates were externally reverified, full fleet coverage audited, application built or runtime behavior newly certified. Examples in this plan are illustrative.

Delivery checks: verified existence/readability of all ten inputs. Weekday check clean on `PROME/DOCKET.tsv`, `PROME/GATES.tsv`, `PROME/WILL_QUEUE.md`, `AGENTS/CATO/CONTINUITY.md` and this plan; glued-date check clean on the two changed CATO documents. Read-cap check covers exactly `AGENTS/CATO/AGENTS.md`, `AGENTS/CATO/CHARTER.md`, `AGENTS/CATO/CONTINUITY.md`, `CLAUDE.md`, `USER.md`, `AGENTS.md`: all below the cap, with root CLAUDE's existing 75%-tier advisory. No CATO STATUS/calendar/catalyst input exists to include. Orphan advisory clean; no work outside CATO, no staged paths, and whitespace check clean. No memory, ledger or superseded-figure check condition arose. Only this plan and continuity are intended for commit. Publication receipt is delivered in-session; there is no app to publish.
