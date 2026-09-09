# Dashboard management data

Owner: PROME. Will approved the attention/coverage additions September 9, 2026.

`STATUS.md` owns mirrored holdings, including individual tax lots and historical rows. `position_management.tsv` owns only the dashboard's reviewed contract-to-management relationship: account, ticker, instrument, explicit expiry, responsible owner, next review, action, completion evidence, and independent approval/order/fill states. It does not own quantities, marks, thresholds or trade authority. Linked source rulings and broker receipts govern those facts. Empty expiry is allowed for stock; spread instruments retain all strikes and option types. Account attribution limitations stay on the holding row.

When an execution, ruling or management source changes, reconcile the affected row here in the same pass. `source_sha256` is the SHA-256 of the evidence file's bytes at review; the renderer withholds the mapping if the source changes or vanishes. Refreshing a hash requires reading the evidence, not merely making a warning disappear. `checked` dates the review, never the underlying market observation. `review` is a dated obligation or an explicit undated review description; UNKNOWN is honest when no next review is registered. New thresholds or trades still return to Will.

Approval states: APPROVED, NOT_RECORDED, NOT_APPLICABLE. Order states: UNKNOWN, PLACED, NOT_APPLICABLE. Fill states: UNKNOWN, FILLED, NOT_APPLICABLE. PLACED and FILLED require linked evidence; approving an action never sets either. A blank action is management follow-through, not an immediate broker task. Closed holdings are excluded from action rows. Gate IDs are explicit per contract; ticker mentions never establish coverage. A LIVE gate is a recorded rule state, not evidence of continuous monitoring or a broker order.

Known omissions surface as unrecorded management mappings. Historical Robinhood rows stay visible as unverified; stale table notes cannot establish current holdings. Recent confirmed sales are read directly from receipt tables linked by STATUS.md. Scheduled settlement never upgrades cash to verified settled cash.

PROME outstanding work is generated from DOCKET.tsv, preserving physical line identifiers. Queue rulings remain in WILL_QUEUE.md. Build time is separate from source dates; publication to the recorded hosted tabs requires a separate verified publication receipt.
