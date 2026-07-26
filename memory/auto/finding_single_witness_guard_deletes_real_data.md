---
name: finding_single_witness_guard_deletes_real_data
description: A corroboration guard keyed to ONE witness series silently deletes real data when that witness lags; require any-of a witness SET (all skip together on the true failure mode)
metadata: 
  node_type: memory
  type: project
  originSessionId: e0e9467c-9aa3-4945-b270-8641896bb80b
  modified: 2026-07-26T02:13:27.937Z
---

**The pattern (VIOLET backfill.py, 2026-07-25):** a holiday guard built 6/1 to drop yfinance ^VIX phantom rows required ^VIX3M corroboration ("an orphan ^VIX row is a phantom"). Yahoo's ^VIX3M *daily-history endpoint* then ran ~4 sessions behind while ^VIX/^VVIX/^SKEW stayed current — and the guard silently dropped **five real trading days** (7/20-7/24) from VX_DAILY, including the day VIX broke 20 intraday. The repair tool even reported success ("touched 95 rows") while the gap persisted, because the touches were elsewhere.

**Why:** a guard against failure-mode A (phantom rows on holidays) becomes failure-mode B (real-data deletion) the moment its *single named witness* rots independently. The true discriminator for A was "ALL companions skip together," not "this one companion is present."

**How to apply:** when writing any keep-only-if-corroborated filter (data pipelines, dedup guards, phantom-row drops), key it to **any-of a witness set**, not one series — and pick the set so the genuine failure mode fails ALL witnesses at once. When a repair tool claims success, verify the *specific rows/records you came for* exist afterward (kin of [[finding_verify_fix_against_capable_case]]). Related staleness family: [[finding_tool_default_asof_date_drift]], [[finding_yahoo_sparse_index_date_shift]].
