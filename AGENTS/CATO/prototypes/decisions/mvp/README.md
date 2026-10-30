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

Replace the ID/hash with values from `list`. Export prints a self-contained JSON transport object; it sends nothing. The receiver command is explicitly synthetic. It can record received, needs_clarification, rejected or integrated. Received can advance to one interpretation; each event survives. Neither integrated nor received is completed work. Conflicting terminal interpretations require a new response rather than overwriting history. There is no production import, owner acknowledgment or completed-work adapter yet.

## Author verification and limits

Fifteen Python checks cover restart recovery, exact scope/terms, retry identity, changed terms without a revision bump, record changes, source failures, wrong controls, live-source rejection, free-text/deferral/task semantics, preserved replacements, overlapping answers, rollback on a simulated write failure, bound receipt progression, export hashes and HTTP Host/Origin/capability/size rejection. Reproduction:

```sh
python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_mvp.py -v
```

Ten browser checks at each of 1440 × 1150 and 520 × 1100 pass in native Windows Chrome against the actual Python service. The harness uses isolated stores/profiles and adds test-driving JavaScript to the served page. Screenshots inspected. Reproduce on this Windows/WSL setup with `python3 -B AGENTS/CATO/prototypes/decisions/mvp/test_browser.py`; it writes only the author receipt here and temporary browser evidence. Initial immediate launches failed with connection refused; a Windows HTTP readiness probe resolved that observed startup failure without configuration changes. This is not evidence that every machine's forwarding works.

Checks are author work, not independent acceptance. Opening a new Store proves database recovery; no power-loss durability claim is made. SQLite transactions and injected rollback tests do not simulate every filesystem failure. The display record plus presentation hash binds the application terms; it does not prove which pixels a person actually read. A loopback capability protects the browser path, not identity against another process with the same user account. Tests use fictional data only. Narrow-window checks are not laptop hardware verification. Actual laptop handoff, live source/trust/receipt adoption, queue reconciliation, independent review, launcher integration and the real pilot remain pending in [the plan](PLAN.md).
