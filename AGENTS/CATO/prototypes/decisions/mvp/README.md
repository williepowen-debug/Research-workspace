# Decisions — first durable component

October 30, 2026. The approved MVP is in progress. This component is a working **fictional rehearsal**, not a live decision channel. [Concrete storage, delivery and pilot plan](PLAN.md) · [browser check receipt](validation.json) · [desktop screenshot](preview.png).

It reuses the existing record validator, pinned fictional record and view-placement logic. The completed three-real-record comparison remains accessible as a separate read-only page. The original mockup, schema and comparison are unchanged.

## Run locally

From the repository root, with the existing Python/jsonschema environment:

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/server.py --store AGENTS/CATO/prototypes/decisions/mvp/local-state/responses.sqlite3
```

Open the printed `http://127.0.0.1:<port>/` URL in Windows Chrome. If the first connection fails, retry after WSL localhost forwarding has become ready. Stop the server with Ctrl+C. Restart with the same store to recover saved responses. The ignored local-state directory belongs to this computer and is not Git delivery. No server, scheduled job or launcher entry is installed by the build.

Try choosing an option with an exact condition, cancelling the review, then saving. Refresh or restart the server. Revise the answer into a question or deferral; both responses remain in history. Report the fictional personal task done; that creates no approval or owner receipt. The browser uses all four views. Historical samples never acquire submission controls.

## Inspect and simulate receipt

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/store.py --store AGENTS/CATO/prototypes/decisions/mvp/local-state/responses.sqlite3 list
python3 -B AGENTS/CATO/prototypes/decisions/mvp/store.py --store AGENTS/CATO/prototypes/decisions/mvp/local-state/responses.sqlite3 export EVENT_ID
python3 -B AGENTS/CATO/prototypes/decisions/mvp/store.py --store AGENTS/CATO/prototypes/decisions/mvp/local-state/responses.sqlite3 simulate-receipt EVENT_ID EVENT_SHA256 received 'Fictional receiver read'
```

Replace the ID/hash with values from `list`. Export prints a self-contained JSON transport object; it sends nothing. The receiver command is explicitly synthetic. It can record received, needs_clarification, rejected or integrated. Received can advance to one interpretation; each event survives. Neither integrated nor received is completed work. Conflicting terminal interpretations require a new response rather than overwriting history. The public rehearsal does not import real responses, receive actual PROME acknowledgment or infer completed work. The candidate pilot adapters below are separate and not activated.

## Author verification and limits

Fifteen Python checks cover restart recovery, exact scope/terms, retry identity, changed terms without a revision bump, record changes, source failures, wrong controls, live-source rejection, free-text/deferral/task semantics, preserved replacements, overlapping answers, rollback on a simulated write failure, bound receipt progression, export hashes and HTTP Host/Origin/capability/size rejection. Reproduction:

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_mvp.py -v
```

Ten browser checks at each of 1440 × 1150 and 520 × 1100 pass in native Windows Chrome against the actual Python service. The harness uses isolated stores/profiles and adds test-driving JavaScript to the served page. Screenshots inspected. Reproduce on this Windows/WSL setup with `python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_browser.py`; it writes only the author receipt here and temporary browser evidence. Initial immediate launches failed with connection refused; a Windows HTTP readiness probe resolved that observed startup failure without configuration changes. This is not evidence that every machine's forwarding works.

Checks are author work, not independent acceptance. Opening a new Store proves database recovery; no power-loss durability claim is made. SQLite transactions and injected rollback tests do not simulate every filesystem failure. The display record plus presentation hash binds the application terms; it does not prove which pixels a person actually read. A loopback capability protects the browser path, not identity against another process with the same user account. Tests use fictional data only. Narrow-window checks are not laptop hardware verification. Actual laptop handoff, live source/trust/receipt adoption, queue reconciliation, independent review, launcher integration and the real pilot remain pending in [the plan](PLAN.md).


## WQ-555 A — candidate pilot adapters

Will selected A for the supervised non-trade pilot after the explanation in CATO's chat. That does not answer L884 or change the queue's authority. [Candidate contract and pre-edit acceptance properties](PILOT_CONTRACT.md) · [candidate browser receipt](pilot-validation.json) · [receipt-screen fixture](pilot-preview.png).

`pilot_files.py` supplies the proposed pilot-only source reader, immutable response export, transactional restoration from committed events, PROME receipt reader and truthful delivery labels. `PilotStore` connects those adapters to the existing service/UI, with submissions disabled by default. The rehearsal server command still opens only the fictional rehearsal. The separate `pilot_launch.py` command below opens the accepted real pilot in preview mode by default. The source path, expected WQ and unit are supplied explicitly by the eventual caller, not discovered or inferred. Owner acceptance must confirm the source contract and non-trade scope; a mode label is not authority.

Twenty-four isolated Python checks pass, including a preserved real PROME producer record, original CRLF source bytes, dirty/changed source and queue terms, exact choice meaning, replay, concurrent replies, exported-file preservation, failed export/retry, a cloned repository's full history restoration, conflicting branches, namespace separation, receipt evidence and confirmation bindings. Thirty-four native browser checks cover writable fixtures, integrated owner-receipt fixtures at both widths and the default disabled preview. Existing fifteen Python and twenty browser rehearsal checks also pass after the shared store/UI changes. All pilot writes occur in temporary Git repositories; no real response/receipt directories were created.

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_pilot_files.py -v
python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_pilot_browser.py
```

These are author checks. Two local checkouts are not two-device evidence. Receipt validation verifies PROME's committed matching-confirmation assertion and reference availability, not the truth of a human conversation independently. The candidate's one-pilot file directory intentionally rejects foreign events; multi-pilot adoption is outside this batch. `received`, `needs_clarification`, `rejected_stale` and `integrated` are accepted owner states, with no completed-work state. A new response against an integrated old question is blocked; replay of the identical saved response remains safe.

PROME encoded WQ-555 A and accepted the pilot-only contract in `461cbcc82`; actual source WQ-558 / unit `558.L884` landed at `468f0457c`. The independent Opus ledger found three submission blockers in `6fe585ede`. This revision fixes selected-source binding, integrated receipts on superseded responses and unstable unpublished commit pins, plus ambiguous fences, the missing recommendation ID and disabled export. Missing Git evidence is quarantined visibly, with all new submissions blocked. Source and selected queue row must both match a published origin/master commit. The actual WQ-558 source reads successfully with submissions disabled. PROME accepted the independent re-read at `eeab020bb` with the procedure conditions and follow-up residuals below. The original submission blockers are independently closed. CATO supplied a fixed launch command and launcher entry; the actual laptop check and one real pilot through owner follow-through remain owed. General source-authority change remains a separately ruled later step. No additional user approval for the already accepted trust boundary is requested.

The independent review's accepted residue remains explicit: hashes are integrity checks, not identity; PROME attests to the matching chat confirmation and semantic ruling; old-terms saved events require PROME reconciliation. These author checks do not close independent acceptance. Sources and disposition basis remain inspectable in the full record; recommendation ID/label and option outcomes now appear on the card.

## Accepted pilot launch and device check

PROME's [acceptance packet](../../../inbox/2026-10-30_from-PROME_reread-verdict-submissions-may-be-enabled.md) accepts `7fc79dbc9` for WQ-558 under WQ-555 A. The separate `pilot_launch.py` checks that published acceptance and refuses changed reviewed core files. It never fetches, commits, pushes, creates receipts or selects another WQ. Default use is a preview:

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/pilot_launch.py --open-browser
python3 -B AGENTS/CATO/prototypes/decisions/mvp/pilot_launch.py --check
```

The launcher's **Decisions** tab offers those same preview/check operations. The persistent database is ignored, machine-local `local-state/wq558.sqlite3`. The check uses a disposable database and GET requests only; it prints Windows/WSL host, published source pin/revision and connection results. Desktop DESKTOP-BC6EF81 passed Python/Windows checks and actual native Chrome preview. `launch-validation.json` records the browser check and source hashes. Existing installer wrappers load current repository scripts. Actual laptop WILLIEPOWEN check and browser observation are still owed; local clones do not satisfy that requirement.

After those checks, CATO can start the authorized single supervised pilot with `python3 -B AGENTS/CATO/prototypes/decisions/mvp/pilot_launch.py --supervised --open-browser`. This explicit switch is an operator procedure, not new identity authentication or proof that device checks happened. The launcher currently never selects it. CATO must first establish the laptop observation and confirm the question is still open. Will chooses in the app; CATO commits/pushes the exact immutable event; PROME receives Will's matching chat confirmation and writes its own receipt/ruling. No real response has been created by these tests. Check the owner evidence before claiming acknowledgment or completion.

PROME's procedure conditions: at integration remove/change the open queue row (a bold done row alone is insufficient), keep event files under responses/, and pin receipt ruling/chat evidence only to commits already on origin/master (`git merge-base --is-ancestor`). Four residual classes remain CATO work before any second pilot: container/invalid-info record fences, orphan receipts after response-file retirement, and missing/unpublished receipt evidence hiding the card. These do not reopen the accepted first-pilot gate under those procedures. Other accepted semantic/authentication/stale-history limits remain in the two independent ledgers. Live use is not yet demonstrated.
