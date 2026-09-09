# SAM — approved integration

**September 8, 2026 ET; BOJ source check crossed into September 9 JST.** This implements the approved recommendations following the [catch-up assessment](2026-09-08_catchup-assessment.md). It preserves v1.7's retirement and does not promote a successor, trade, or revise a historical prediction grade.

| Home | Integration |
|---|---|
| [THESIS](../thesis/THESIS.md) | Current policy/FX, conditional domestic demand, intervention and energy interpretations replace contradictory live prose. Old conviction, route and sizing material is explicitly historical. |
| [JGB supply/demand](../research/outputs/JGB_SUPPLY_DEMAND_THESIS.md) | Mixed sponsorship replaces the blanket demand vacuum. Retired carry-vol trade expression removed from current guidance; GPIF tenor and Norway execution questions remain open. |
| [Insurer tracker](../insurers/TRACKER.md) | August investor-type flows added separately from dated company disclosures. Existing two-institution/two-window reactivation rule replaces the conflicting “any one” list. |
| [MOF playbook](../MOF_INTERVENTION_PLAYBOOK.md) | Independent broker baseline, forecast versus actual, settlement calendars, source-content checks and reserve-stock attribution are separate controls. Both tested projection URL forms returned identical XLSX bytes; the official index link is preferred. |
| [Knowledge base](../workbook/KB.tsv) | KB-209 rewritten as one current fact with official aggregate, FIMA-use retraction and unresolved funding. Quoting defects in 169/197/209 repaired separately; 169/197 substantive historical judgments unchanged. |
| [BOJ source contract](../workbook/BOJ_OIS_README.md) | Replaces the impeached source with reviewed Totan image ingestion; old and new instruments have separate ledgers. A changed image requires a new SAM visual review. |
| [Candidate](../thesis/V18_CANDIDATE_PILLAR1.md) | Current BOJ reference updated to the newer reviewed vintage; original candidate conditions retained. |
| STATUS / MEMORY / CHANGELOG / TIMELINE / NEXUS | Canonical state, completed work, remaining obligations and peer interpretation reconciled; outgoing STATUS session preserved verbatim. |

The durable interpretation is that Japan-specific yen strength and policy repricing merit attention, while systemic liquidation, named-insurer UST selling and official funding mechanisms each require their own evidence. Stronger yen can cushion oil costs without eliminating them. Proposals and aggregate flows cannot establish named transactions. Exact macro observations and source limits remain in the assessment rather than being copied into every structural document.

## BOJ source validation and remaining limitation

The [Totan publisher page](https://www.totan.com/archives/15647) published a new table during this work: **September 9, 11:15; JST assumed because the chart does not print a timezone**. September OIS is 1.2213%, with a 98% incremental 25bp equivalent; cumulative expected hikes reach 2.65 by March 2027. The source is indicative OTC meeting OIS, not an exchange-traded futures probability. The September 8 97% observation remains valid only at its own historical vintage. The standalone cumulative chart still pointed to its prior image and was not spliced into the new table.

Five reviewed rows were ingested into [BOJ_MEETING_OIS.tsv](../workbook/BOJ_MEETING_OIS.tsv); a second live run appended zero rows. Each carries source time, retrieval time, reference terms, quote kind, image hash and expiry. Live methodology/hash checks reject a changed chart; date and arithmetic validation reject stale, future, expired or inconsistent inputs. The former `BOJ_OIS.tsv` is preserved unchanged as frozen history.

**Image decoding remains assisted:** SAM must inspect each new chart and add its dated transcription before the script can ingest it. No automatic OCR feed was claimed or installed. The replacement is usable now with that dependency; unattended extraction remains an enhancement. The existing boot slot is retained, with visible success/failure text and no fallback to the impeached source.

## Validation and audit

- Ten BOJ regression tests passed, including changed-image/error-HTML, stale/future/expired dates, invalid arithmetic, missing/duplicate terms, methodology drift, idempotency, same-vintage conflict and no-write/fetch-failure behavior. Live validation and repeat ingestion passed.
- Boot tool inventory passed after excluding regression-test modules from operational-tool discovery. No full market boot was rerun for this document integration.
- Read-cap, weekday and local-link checks passed; before-images and historical prediction/trade/frozen-ledger preservation verified byte-for-byte. Detailed [validation and consumer dispositions](../research/outputs/2026-09-08_integration/validation.md).
- Quoting-only commit `c922e355b`; source replacement commit `bfaea9825`. Analytical integration is committed separately. Validation receipts are saved under [the integration evidence directory](../research/outputs/2026-09-08_integration/).
- [Before-images](../research/outputs/2026-09-08_integration/before/) retain the full original owner documents and script, including malformed KB quoting. Source URLs and hashes are in `sources.json`; code tests use the saved primary table/page fixture.
- The operator-only fresh-session SAM judgment eval was not run or scored here. Its existing re-baseline obligation remains in MEMORY; no thesis-version promotion is claimed.
- Other agents have dirty/staged work. Only SAM paths are committed; shared pull/push is deferred under the dirty-peer rule. No peer messages were sent and no peer files edited. NEXUS is refreshed last for readers who consume it in place.

Next data work remains the September funding/CFTC gap, independent intervention baseline, upcoming Fed/BOJ releases, September 14 funding-proxy pair expiry, and the prospective auction-tail precision ruling before September 29. These are forward obligations, not findings closed by document integration.
