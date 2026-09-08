# September 8 BRENT market-docket reader

**Prepared:** 2026-09-08, after the equity close; direct-fetch observation began 20:50:15 UTC / 16:50 ET. **Scope:** Codex research preparation for PROME; resident BRENT neither impersonated nor closed out. Supersedes: none. Domain files, inbox dispositions, gates, positions and Git state were not changed by this reader.

## 🟠 HIGH — L198② cannot yet grade: the target print is missing

[CONF, IMF primary, fetched 9/8] Two different queries of the [PortWatch chokepoint6 endpoint](https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Daily_Chokepoints_Data/FeatureServer/0/query) both end at **August 30**. The target **August 31 / September 1** observations do not appear. August 30 records `n_tanker=2`, `capacity_tanker=42,932`, `n_total=6`; these are the wrong date for the named positive control.

**Disposition: UNKNOWN / pending target publication.** The frozen test in `AGENTS/BRENT/docket/CATALYSTS.tsv` September 8 row requires the actual Sidr/Senegal Prosperity window: ≥~500,000 dwt demonstrates visibility; <250,000 confirms a coverage defect. Substituting August 30 would manufacture a failed control. No throughput inference or revived exit trigger follows. The two named hulls remain the owner's relayed UKMTO premise, not a newly independently graded premise here.

The first network attempt failed sandbox DNS; the approved outside-sandbox retry succeeded HTTP 200. A second newest-first query also returned August 30. Its `exceededTransferLimit=true` reflects the requested five-row limit, not missing newer records: sorting is descending. Raw evidence: `2026-09-08_orch-brent-portwatch.json`, `2026-09-08_orch-brent-portwatch_latest.txt`; exact query and capture metadata in `2026-09-08_orch-brent-fetch-evidence.json`.

## 🟡 MEDIUM — L198① full-August relay supports the existing direction

[EST, Kpler provisional data relayed by Reuters, published 9/8] **Sidi Kerir full-August exports: 2.139 million b/d**, replacing the earlier ~2.3 million b/d August-to-date pace for this comparison. It is **1.43% below** the owner's **2.17 million b/d port-total benchmark**. The prior +6% comparison therefore no longer describes the full-month reading. The 2.139 reading is still more than double June in the report; do not relabel June as July or equate a full-month/MTD difference with a measured sequential fall. [Reuters relay](https://profit.pakistantoday.com.pk/2026/09/08/why-is-oil-still-below-dollar100-despite-a-7-million-bpd-drop-in-middle-east-shipments)

**Assessment:** direction-only evidence continues to favor northern rerouting rather than a collapse in Sidi Kerir liftings. No new threshold or grade is invented from the small benchmark shortfall. **Limitation:** direct Kpler full-August data were not reached; this remains one tracker-to-wire evidence chain. RTE's copy was search-readable but direct-open 403; multiple copies are not independent tracker observations.

## 🟠 HIGH — L140 instrument text located, official-host verification unresolved

[CONF as a transcription read; official-host provenance UNKNOWN] Two legal publishers reproduce **Resolution No.1097, dated August 28, 2026**, amending **No.954 of July 30**. Their operative amendments agree: paragraph 4's September 1 start becomes **October 1**; paragraph 5's August 31 end becomes **September 30**. Entry into force is tied to official publication. [GARANT transcription](https://www.garant.ru/products/ipo/prime/doc/414729929/), [ConsultantPlus transcription](https://www.consultant.ru/document/cons_doc_LAW_543093/)

This materially improves the prior wire-summary-only evidence: amendment identity and operative date changes are now readable. **Q1 remains UNKNOWN-AT-PRIMARY under the owner's strict source requirement**, with strong reported direction against a September 1 producer-direct opening. The [government source](https://government.ru/docs/59723/) failed web-open and timed out on the approved direct fetch; no official publication receipt or complete official consolidated No.954 was obtained. Do not describe a failed fetch as absence of the decree, nor a legal publisher's August 31 posting date as the official effective date.

**Owner remains owed:** authenticate No.1097 plus No.954 paragraphs 4–5 and the publication date; separately preserve **Q2 to OSPREY's producer/trader flow series** and **Q3 the matched diesel-crack test**. Neither Q2 nor Q3 was measured here. October 1 is the transcribed amendment's successor date, not an owner-authorized replacement clock applied by this reader.

## 🟠 HIGH — physical proxy improves; official settlement comparison remains UNKNOWN

[CONF, EIA primary] [RBRTE](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=RBRTE&f=D) gives **September 1 physical Brent $96.02/bbl**; release date **September 2**, next release **September 10**. [FRED DCOILBRENTEU](https://fred.stlouisfed.org/series/DCOILBRENTEU) independently presents the same originating EIA observation. They are two delivery paths for one underlying series, not independent price assessments. September 8 physical is unavailable in this release.

**Basis conflict resolved before subtraction:** `AGENTS/BRENT/archive/STATUS_DETAIL_2026-09.md:95` labels September 1 BZX26 **$95.22** a daily close. `HEARTBEAT.md:65` explicitly retires $95.22/$95.15 as intraday and names **$94.65**; today's freshly fetched named-contract Yahoo daily history also reads **$94.65**. Thus **$0.80 is the rejected comparison**. The reconstructed September 1 **EIA-minus-Yahoo-daily-close proxy is +$1.37** (96.02−94.65), [EST derived proxy], not a certified Platts-Dated-minus-ICE-settlement premium. Official ICE/CME pages opened but exposed no usable dated settlement table. **That exact official benchmark remains UNKNOWN.** No premium trigger exists here.

[CONF as vendor live quotes, not settles] Yahoo's named-contract snapshots around **20:39–20:40 UTC September 8** read:

| Contract | Price, $/bbl |
|---|---:|
| BZX26, November Brent | 99.29 |
| BZZ26, December Brent | 95.43 |
| BZF27, January Brent | 92.11 |
| CLV26, October WTI | 94.24 |
| CLX26, November WTI | 91.25 |

Derived live spreads [EST]: **X−F +7.18**, **X−Z +3.86**, **Z−F +3.32**, and matching-November **WTI−Brent −8.04**. The curve is backwardated. September 4 daily-close X−F was +7.13 in the same fresh history, but live-versus-close is **not a settled trend grade**. September 7's owner live range was $97.3–97.7; today's snapshot is higher, while $100 remains an already-fired rung, never a fresh deployment trigger. All Yahoo payloads and instrument URLs are saved alongside this report. Official September 8 settlement reconciliation remains owner work.

## Existing letters, inbox and completion

**STAND DOWN remains binding:** WQ-189/WQ-192 are closed; no deploy or arm follows from price, the FALCON gate alone, or these findings. PROME already verified XLE's September 8 close **$64.77**, selecting WQ-168's existing September 9-open exit path subject to live broker-position verification; this reader did not regrade options or execute anything.

[CONF, filesystem inspection 9/8] Entire active BRENT inbox, including WALTER sublane and excluding processed archives: **zero files**. No current inbox ask was silently skipped; nothing was consumed or receipted. Structural backlog is outside this task.

**COMPLETION**

- **STATUS:** SCOPED-PARTIAL research preparation delivered.
- **CHANGED:** This report and uniquely named evidence artifacts only.
- **RESULT:** Full-month Sidi Kerir relay obtained; PortWatch target absence verified; diesel amendment transcription read; EIA physical observation and named-contract basis reconciled.
- **GAPS:** PortWatch August 31/September 1 publication; official Russian instrument/publication authentication; official matched settlement premium and September 8 settlement; OSPREY flows and diesel crack.
- **WILL_NEEDS:** No new research or trade approval requested by this packet. Existing broker verification/order follow-through remains with Will/TERRY.
- **FOLLOW-UP:** BRENT owns remaining grades and canonical integration; PROME owns docket disposition. Repeat the PortWatch target read when it publishes, authenticate the named Russian instruments, and obtain the official settlement table before calling the physical/paper comparison complete.
