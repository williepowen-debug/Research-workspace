# WAL Q3 Call Report — current result and source conditions

**Later result, November 4 2026:** source supplied by CATO and independently verified/extracted; see `2026-11-04_Q3-independent-extraction.md`. The UNCHECKED result below is the preserved earlier attempt, superseded for current extraction status.

**2026-11-04, WAL / OpenAI Codex. Result: UNCHECKED; retrieval attempted, independent extraction remains source-blocked.** Narrow current-summary corrections are complete against the existing October 30 grade. No 10-Q re-grading, score/weight change, broader rotation or new research program.

## Existing-source check first

Read WALTER's `research/2026-11-04_WAL-source-recovery/REPORT.md` and its administrative notice to WAL. Its bounded retained-source recovery closed **NOT RECOVERED**, with limits explicitly recorded (not a proof about other machines/backups). The original Q3 receipt records Western Alliance Bank, RSSD 3138146, period 20260930, FFIEC RetrieveFacsimile SDF, retrieved 2026-11-01T02:18:33.515051+00:00, 1,792 rows, SHA-256 `2e04cc7bf1a78e525a68059c358215c8ce9e3c24c3639d84ea74ccb8d69c60a4`. Its recorded temporary path is missing. A current filename inventory of AGENTS/FORGE (including untracked/ignored local source files) found no Q3 WAL SDF; the matching SEC 10-Q HTML and FINRA file are different objects, not substitutes.

WALTER's two surviving selected-row TSVs were opened and filtered on bank=WAL / period=20260930; row identities were checked for date 20260930 and RSSD 3138146. They contain 27 and 21 selected rows, **45 distinct MDRMs combined**, not the full 1,792-row source. Both lack **RCON1766**. Hashes of these actual TSV files, the existing original-receipt pointer, and a complete 70-field input catalog are saved in `../sources/ffiec_2026-11-04/missing-inputs.json`. This is a custody/input inventory, not reconstructed source bytes or a replacement extraction.

## Fresh direct retrieval and controls

All requests used the existing configured credentials without printing or persisting authentication material. Endpoint base: `https://ffieccdr.azure-api.us/public/`.

| UTC on 11/04 | Request | Result | Durable receipt |
|---|---|---|---|
| 21:13:44 | RetrieveFacsimile, Q3 WAL SDF, existing curl-config transport | HTTP 500 | `retrieval_20261104T211344447120Z.json` |
| 21:14:09 | Same endpoint, Q2 WAL control, curl-config | HTTP 500 | `retrieval_20261104T211409614792Z.json` |
| 21:14:09 | Q3 WAL SDF, urllib transport | HTTP 403 | `retrieval_20261104T211410018021Z.json` |
| 21:14:39 | RetrieveReportingPeriods, established header-stdin transport | HTTP 500 | `transport-controls.json` |
| 21:14:40 | Q3 WAL SDF, header-stdin, same unpadded 9/30/2026 period style used by WALTER | HTTP 500 | `transport-controls.json` |

Receipts live under `../sources/ffiec_2026-11-04/`. Alternate-transport receipt retains response byte counts and hashes, not credentials or server-body content. **The Q2 and reporting-period controls also fail**, so these responses cannot establish Q3 filing absence, a Q3-specific problem, credential expiration or the root cause of access failure. No complete source returned and none is claimed preserved.

The configured desktop JWT metadata expires **2026-11-05 19:02:19 UTC (14:02 ET)**; it was not expired during these tests. PROME's committed 11/01 renewal notice to REGINALD says the renewed token (expiry 2027-01-31) was installed on the **laptop**, with desktop installation still owed. That does not establish installation here; the configured desktop expiry still matches the older token. WQ-31 already owns this condition; no duplicate decision/credential request.

## Exact missing inputs and withheld outputs

1. **Complete, unmodified Q3 SDF for Western Alliance Bank RSSD 3138146, period 20260930**, with endpoint/format, retrieval timestamp, row count and SHA-256 at a durable path. A fresh verified retrieval may differ from the historical hash if the filing was revised; preserve its actual receipt rather than forcing a match. A recovered historical original must match its historical receipt.
2. **MI3 denominator RCON1766 (C&I item 4)** is absent even from the surviving extracts. RCON2746 alone cannot supply MI3. No percentage, band or quarterly delta computed.
3. **Approved bank-level extraction inputs:** RCONJ454 and NDFI subtypes/nonaccrual/unused commitments; modifications; arrears and GNMA population controls; losses and provision; mortgage activity/MSA/recourse; bank CET1/RWA/AOCI and contingent exposures. The exact pre-existing 70-field/MDRM mapping is cataloged with null values and UNCHECKED extraction states. **54 of 70 codes are absent even from the surviving selected extracts**; 2 of those (RCONC410/RCONC411) are June/December semiannual fields, not expected at Q3, leaving 52 other absent named codes. None of the 16 available selected codes is promoted to a full-document independent extraction.

No Q3 MI3_SERIES data row, ratio, NDFI integration, grade, score or weight change. The series attention date advances; **its real-data clock stays 2026-08-07**. Missing is not zero; semiannual omission is not stress. The Call Report MI3 measure concerns CRE lending not secured by real estate; it does not resolve the secured-office $99M loan.

## Narrow summary reconciliation

Read the already-completed `2026-10-30_Q3_10Q_GRADE.md` and accepted PREDICTIONS states, without rerunning the grading. Current NEXUS table now carries WAL-01 **INVALIDATED FINAL** (926 + 165 = 1,091 cross-check passed), WAL-02 **INVALIDATED FINAL, 10-Q-confirmed at 30bps**, and the $99M appraisal **NO-VERDICT after all four carriers, question carried to Q4**. NDFI's old waiting-for-10-Q clause is replaced with the completed MIXED result (25.7% of HFI with dollars up), score held. The earlier 10/30 preferred-coupon question is retained as a dated snapshot with its later 8.36% answer noted. Current STATUS exit/matrix labels are aligned; its original print/call grade table is explicitly identified as a historical snapshot and preserved verbatim. No frozen frame or dated grade is edited.

## Delivery and closeout

WALTER's administrative custody notice was integrated and moved via git to WAL's processed inbox; no WALTER signal-row receipt was invented for an administrative notice. The unrelated DEWEY packet remains queued. STATUS, MEMORY, MI3 attention line and final NEXUS pin record this outcome. Existing thesis/calibration/positions/grades were hashed before the edits and checked unchanged afterward. Scope remains bounded; other carried work is not advanced. Own result plus dated PROME completion packet are persisted with explicit paths; pull was refused for foreign dirty work, which was not stashed/edited. Push publication is established only by the final safe-push receipt. Thread-local discovery exposes only this root task; cross-runtime peer presence, transport and consumption remain UNKNOWN.

**Remaining condition:** restore verified source access (including reconciling the desktop credential with the recorded laptop renewal) or supply a verified complete cross-desk SDF, then perform WAL's independent extraction. This session's retrieval attempt is closed with an honest source-blocked result; it does not discharge the outstanding extraction by narrative inference.
