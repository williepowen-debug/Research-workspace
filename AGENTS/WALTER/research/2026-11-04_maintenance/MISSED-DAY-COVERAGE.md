# Missed release-day coverage — bounded proposal

November 4, 2026. Will approved completing the outstanding coverage review. This is a concrete operating proposal, not an installed scheduler or new domain mandate. Existing WQ-388 refusal of unattended WALTER launches remains. Inputs: PROME/DOCKET.tsv (canonical dates/owners), HENRY/domain/ECON_CALENDAR.md and the named owner's dated catalyst ledger; WALTER BOARD/disposition records and owner report/print/board logs. Calendar dates are leads until verified in the owning calendar; no new external release-date assertion here.

## Problem and observed controls

October 29 GDP/PCE card015 explicitly arrived about6.5 hours late although HENRY L774 and LABOR already had grades. ECB card016 was late but HANS had a primary grade (PROME L317 now resolved). October28 FOMC L773 was read by HENRY the following day. November2 ISHM L899 survey work was interrupted and subsequently recovered November4; initial absence of a WALTER card could not distinguish interruption from no review. November4 cards006/035 were deferred, then owner acted rows completed them. These are different states; counting absent cards alone would produce false alarms and duplicate work.

## Proposed next-launched-session pass

1. Use the previous completed coverage cutoff in LAST_COMPLETION, not the last file modification or collector-run date. Select elapsed scheduled releases through the current clock from existing calendars. Leave future and not-yet-published observations pending. If a gap spans many days, enumerate all dated candidates first, then prioritize; never silently truncate to the newest day.
2. For each release, match issuer/series, reference period, release date and vintage. Check BOARD, WALTER's recorded kill/no-action/disposition, then the owner's actual report/print/board log. A source body or explicit scope must support the status. No substring match, file timestamp or blank inbox can prove completion.
3. Record one row per release using the existing session review/disposition artifact: event key, calendar source, owner, publication state, source/vintage, WALTER disposition, owner-grade state, evidence path, next action. This is a session artifact, not a second permanent calendar.
4. Outcomes: **reviewed/routed**, **reviewed/no route** (reason), **owner reviewed/routing reconciliation owed**, **not reviewed**, **interrupted/partial**, or **unpublished/source unavailable**. These are proposal labels; no production schema is changed in this pass. A published but unreviewed release needs normal source triage; an owner-completed event needs only its remaining routing/delivery duty. Preserve first-release/revision distinctions.
5. Apply the existing CHECKLIST, batch manifest and duplicate gates to actual content. Receipt processing or an owner grade is not a new independent signal. Close with enumerated dispositions and the new cutoff; exact source exceptions retain a named next touch.

## If no WALTER session runs

The dated owner/PROME calendar remains the existing path. The domain owner grades within its authorized task; PROME coordinates existing due work under its current launch rules. Neither this proposal nor a calendar gap authorizes WALTER to self-schedule, declare an owner DARK or launch a substitute. At the next human-launched WALTER session, reconcile recovered owner work before searching again. No guarantee of real-time WALTER coverage is made. Any guaranteed on-release wake would be a separate explicit operational decision, not hidden in this fix.

## Acceptance cases for a future narrow implementation

| Case | Required result |
|---|---|
| GDP/PCE October29: owner grade precedes late BOARD card | Owner reviewed; route reconciliation only, not missed research |
| ECB October29: card and primary owner grade exist | Covered; no repeat fetch merely to empty a list |
| ISHM November2: interrupted source attempt, no final grade then | Partial; recover preserved work, not complete and not restart |
| ISHM006/035 later acted rows after historical deferrals | Latest explicit result wins; retain older history |
| Release reviewed and rejected under CHECKLIST | Covered/no-route with reason; no invented BOARD requirement |
| Future November5 release or unpublished November4 observation | Pending; no early grade |
| Headline/collector saved-date differs from event date | Verify event/vintage before calling it a new release |
| No owner receipt and no WALTER record | Unknown review coverage; source/owner check, never proof of DARK |

Recommendation: add this bounded calendar-to-evidence reconciliation to the next launched WALTER boot, reusing the existing session review and disposition machinery. The specific boot wording/implementation is ready for the next policy decision; no scheduler, production code or owner calendar was changed here. This proposal fulfills the requested missed-day design work, while explicitly leaving deployment unclaimed.
