# HY alert consumers / SRF date alignment — acceptance conditions

Written **2026-10-14T16:15:50.955909-04:00**, before editing either live script, on Will's instruction to implement CATO's proposed updates. Same sole LIQUID writer/session `01a13b8c-ebf0-74c0-a1c3-5ae79550bd06`. Acceptance record must be committed before the code edit. Pre-edit code and state are archived with hashes in `scope-before.json`.

## Required properties

1. **Every actual alert consumer preserves every fresh event.** PROME packet, SIGNALS rows and local alert log retain current escalation and any simultaneously recovered historical event. No240-character truncation. SIGNALS has an individually dated row for each event, its appropriate target/priority and the applicable guard/qualification. Widening remains a level only, strict >280 sustained plus BROCK conjunction; no sizing. Kill-side preserves no automatic invalidation/retirement and the conditional live-arbiter rule. Packet routing and file-only delivery remain unchanged.
2. **A recovered event keeps its original date and separate current quote.** Packet headline, SIGNALS date and full log distinguish original terminal event from current observation date/value; a290bp current reading cannot be presented as a current sub260 condition. Ordinary/late/mixed packet notes retain only the applicable sides. An unknown historical date is UNKNOWN rather than today's date.
3. **Transition logic and existing deduplication remain stable.** No threshold/operator/count/terminal-registration change. Existing delivered keys are respected; repeated delivery and repeated main runs add no duplicate events. Polling gaps cannot skip a resetting published observation, and lost state can recover the original single terminal event. Unrelated rows/packets in temporary destinations survive. No unattended Git, external sends or router bypass is added.
4. **SRF composite grades only on two aligned, known observation dates.** For a mismatch, missing date/value or failed leg, retain separately dated components and keep the combined grade unavailable; never assign a cross-date sum to the later day. On aligned dates, preserve strict >$50B and existing priority/routing. Do not substitute another series or alter LIQ-07's separate RPONTTLD input.
5. **Normalize published HY OAS to integer bp before comparisons.** Apply the existing whole-bp basis to both latest zone value and first-published kill series.259 qualifies,260/261 do not; tiny floating representation errors cannot alter the boundary. Preserve latest-versus-first-published roles. This is preventive normalization, not evidence of an observed misgrade.
6. **Supplementary context never extends LIQ-07's frozen condition.** Verdict preparation/STATUS/MEMORY explicitly distinguish required registered inputs and both session lists from ETF, discount-window and named-financing context. Missing required evidence remains pending; missing supplementary evidence is reported alongside an otherwise adjudicable verdict.
7. **Preserve unrelated evidence and authority.** All prediction rows, letters, gates, thresholds, calendar twins, shared FORGE config and withheld swap-line code/letter remain byte-stable. Tests use temporary destinations and synthetic or captured observations. Real alerts, SIGNALS, state, recipient inboxes and the timer are never invoked by tests.

## Five-category neighbour tests

| Category | Required tests |
|---|---|
| Ordinary | Escalation-only and current two-close event; aligned quiet/equal50/above50 SRF; end-to-end main rendering in temporary files |
| Overlap | Escalation plus recovered terminal event in one run; both original event dates/sides/qualifications reach all consumers; aligned values near threshold |
| Wrong owner | Existing unrelated packet/SIGNALS entry preserved; each event's existing target and priority remain its own; no other owner/shared file mutated |
| Missing information | Single known kill observation cannot fire; first-publication failure prevents kill grade; SRF missing leg/date cannot grade total; undecodable late date never becomes current date |
| Concurrent activity | Repeat with saved delivery/terminal state; append to a destination already carrying foreign rows; repeated delivery does not refile or overwrite a historical packet |

Test actual emitted files via temporary paths, not only helper return strings. Existing watcher/boot selftests must pass. Compare baseline/current transitions on captured published readings and first-release fixture boundaries. Mutation probes must show the old truncation/mixed-headline/cross-date defects fail the new checks.

## Review and completion boundary

WQ229's [ruling](../../../../PROME/proposals/2026-09-11_wq229-repair-completion-discipline-RULED.md) says: “A consequential repair goes to an independent reader BEFORE it is called fixed,” with at least one reader-devised counterexample. Owner tests establish IMPLEMENTED/TESTED, not INDEPENDENTLY VERIFIED. No additional agent is authorized/launched by this work. Deliver the exact code/tests/receipts to PROME for the existing independent-review process; declare that dependency and distinguish it from future LIQ-07 publications. This does not create a new withholding rule for the watcher or release the already WITHHELD swap tool.

Delivery failure/retry redesign, general stale-state-language proof, the whole dashboard, GATE079 FIRE-band calibration and original historical-vintage reconstruction are outside this bounded repair. Any newly reproduced failure within the properties above is corrected before delivery; unrelated limitations stay explicit.
