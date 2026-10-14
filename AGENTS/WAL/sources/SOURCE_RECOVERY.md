# WAL source portability and recovery — inventoried October14 2026

`SOURCE_INVENTORY_2026-10-14.tsv` inventories full files present on this machine by content hash, bytes, Git persistence and known recovery source. TRACKED files travel through Git; LOCAL_ONLY_GITIGNORED originals do **not**. PREPARED_FOR_TRACKING denotes this maintenance commit's new receipts, not a pre-existing backup. No ignored filing was indiscriminately added to Git. Existence/hashes establish local preservation, not off-machine backup; external backup status is UNKNOWN.

## Decisive recovery paths

- **Q2 full SEC original:** accession0001628280-26-051418, sourceURL in inventory; original SHA25663f0a86758850f7c833bfe111d86dbd7bb9810b0ea6ce0550cc841e0b66ad85f,6,664,360bytes. Tracked October13 extracts/receipt and earnings extract provide context; they do not replace the whole filing. On a new machine, fetch the exact archive URL to a temporary file with the contact user-agent required by SEC access policy, then verify SHA256/bytes before restoring `sources/q2_2026/wal-20260630.htm`. A403 or different hash is a source gap; do not overwrite the accepted cache silently.
- **Q1 SEC original:** accession/URL recorded in inventory; verify filing identity and the inventoried original hash after download. Cache origin provenance is less complete than the freshly receipted Q2 source; preserve that distinction.
- **Proxy14A PDFs:** local-only; original retrieval URL/accession not located in the reviewed saved receipt. The inspected cover identifies WAL definitive proxy; filename alone does not establish year/accession. Resolve the proper DEF14A from SEC/issuer index, verify meeting/year/identity and compare hashes. Different PDF rendering can differ by bytes; retain both and explain rather than calling it corruption. Do not assume a Git clone can restore these originals without source work.
- **Plaza Doc100:** tracked PDF/text/identity receipt, public RECAP URL and hash. If re-fetching, verify case8:26-bk-10986,entry100,filedOctober2 in the document header, as well as hash. Identity verification is distinct from interpretation/current court order.
- **OZK peer primary:** canonical original/source/hash stays in `AGENTS/OZK/sources/2026-10-12/FDIC_FLNG_12019_8K.pdf` and the OZK owner report. WAL's integration receipt retains URL/hash; no second peer cache or research owner created.
- **Dated vendor/FINRA snapshots:** tracked original payloads/receipts retain retrieval and dataset dates. A later endpoint response may differ; re-fetch creates a new dated observation, never overwrites the old accepted snapshot to fake the old hash. FINRA read-only query body/filter is in its receipt.

## Recovery verification

Use `sha256sum <temporary-file>` and compare the exact inventoried hash; then inspect the issuer/form/period or case/document identity. Only after matching identity should a recovered file support a conclusion. Network/sandbox approvals remain runtime-specific; a saved URL is not access authorization. Source absence on another machine is UNKNOWN access, not an adverse/benign economic result. Extracts and frozen frames stay unedited while the missing original is recovered.

Inventory excludes itself and this navigation note to avoid self-referential hashes. Do not read every raw filing at boot: follow the task's source pointer. No credential files are inventoried or copied; FFIEC desktop credential renewal remains a separate dependency.
