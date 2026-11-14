# STATUS rotation 2026-11-14 (BRENT closeout, PROME prome-fe ask)

Moved VERBATIM from `STATUS.md` to bring it under the READ_CAP rule-5 stop (70% of budget). Zero edits to payloads.

**PAYLOAD RULE:** each set's payload is exactly the text between its `<!-- BEGIN set X -->` line and its `<!-- END set X -->` line, excluding the single newline after BEGIN and the single newline before END. BYTES = `len(payload.encode("utf-8"))`; crc32 = `zlib.crc32(payload.encode("utf-8"))`.

| Set | Content | UTF-8 bytes | crc32 |
|---|---|---|---|
| a | November 13 dated block and the 2026-11-13 rotation receipts line | 1653 | `81f07c62` |
| b | STANDING STATE reconciliation receipts, November 12 and November 10 | 803 | `28a056a6` |
| c | November 13 source-refresh segment of the "Last real market/source refresh" line | 441 | `ac7f666d` |
| d | November 13 summary for Will and the earlier-summaries pointer | 962 | `eef37dd5` |
| e | DATED DETAIL 9/07 pointer, its still-live list, and the older-receipts index line | 812 | `cad4fb83` |
| f | Throughput paragraph (EIA STEO 11/10 shut-ins, OPEC 11/11 Saudi confirmation) | 586 | `46e57ae3` |

<!-- BEGIN set a -->
**November 13 (12:40 EST start, PROME assignment prome-72; part one delivered 12:5x EST; part two delivered 16:3x EST), SCOPED-PARTIAL:** v5.13 / WAIT unchanged; nothing armed. **COT #14 (as-of 11/10) NOT GRADEABLE today:** `cot_grade.py` rc 3 to 16:22 EST (newest 11/3) and a second raw pull agrees; the CFTC schedule delays it to **Monday 11/16, 15:30 ET** (Veterans Day); my calendar's 11/13 date was wrong, re-dated. The COT row below stays #13, JOINT NOT-SPENT → [note](research/2026-11-13_cot14/NOTE.md). **BRT-33 11/13:** +4.9903, valid 5 of 6, not under +3.50 → [note](research/2026-11-13_brt33/NOTE.md). **11/13 settle proxy** BZF27 95.7853 (window VWAP), flat on 11/12; the 96.23 daily bar at 16:23 is a post-settle last. FALCON 98b4473ff7: claims CLAIM ONLY. **Houthi claim on East-West Pumping Station 7 and Yanbu (11/12, WALTER SIG-W-20261112-009):** claim only, Aramco and SPA silent; FALCON grades the claim. **Settle basis (vendor proxy, CME blocked):** BZF27 92.76 → **95.82 (+3.30%)**, M1−M3 window +3.8713 → +4.2394, Brent−WTI Jan +0.80; front-led, held flat 11/13 midday (95.80). **No registered row moves:** BRT-32 letter not met (20%), BRT-33 further from +3.50, BG-02 nothing, no INCIDENTS row. combo:yanbu-bypass weight up, state unchanged → [note](research/2026-11-13_yanbu-claim/NOTE.md).

**Rotated 2026-11-13:** the November 12 block and its summary for Will → [archive](archive/STATUS_dated_2026-11-13_rotation.md), 2081 B crc32 `bad73ee7`. Older receipts (the November 12 and 11 rotations, set b and everything they reach) → [archive](archive/STATUS_dated_2026-11-13b_rotation.md), 485 B crc32 `6668abf8`.
<!-- END set a -->

<!-- BEGIN set b -->
> **Reconciliation November 12:** all 8 rows re-read after the WPSR week 11/6 grade: only the export row's figures change (updated); no COT, rig, JWC, sentinel, stance or owner-file fact is touched by the print (no new COT until 11/13; THESIS v5.13 and TRADE unchanged). **November 10:** all 8 rows re-read after the 11/6 COT and 11/10 STEO grades: COT row matches the ledger tail (125,654 / 6.5831%, as-of 11/3); export row matches week 10/30 (3.675M b/d), STEO changes neither; both archive payloads reproduce (88,876 B `4bb7aad6`, 9,970 B `d82761d3`, leading and trailing newline stripped); BRT-26 CONFIRMED 9/25 matches PREDICTIONS; JWC index re-fetched, still JWLA-035; stance WAIT, no arm (TRADE); owner files present. Earlier receipts → [rotation](archive/STATUS_dated_2026-11-10b_rotation.md).
<!-- END set b -->

<!-- BEGIN set c -->
Before that, November 13, 12:40–16:23 EST: vendor one-minute and daily bars BZF27/BZG27/BZH27/CLF27/CLZ26 (11/12 settle proxy 95.82; 11/13 window 95.7853; [EST vendor, CME 403]); raw CFTC f_disagg.txt (newest 11/3) and the CFTC 2026 release schedule; FALCON's claim grade 98b4473ff7 read at its commit. The superseded line (November 12 and 11 refreshes) → [archive](archive/STATUS_dated_2026-11-13c_rotation.md), 686 B crc32 `58062422`. 
<!-- END set c -->

<!-- BEGIN set d -->
**November 13:** A Yemeni militia (the Houthis) claimed new strikes on the Saudi pipeline that lets oil bypass the Strait of Hormuz, and on its Red Sea port, Yanbu. Nothing is confirmed: Saudi Aramco and the Saudi government said nothing, and FALCON graded the claims unconfirmed. Brent still rose 3.3% at Thursday's settlement, to $95.82, with near months rising most, which is how a supply-risk premium looks; it held flat Friday. No forecast or gate of mine moves. The weekly speculator-positioning report I was due to grade today is delayed by Veterans Day to Monday 11/16; my calendar had the wrong date. No decision for Will.

Summaries from November 12 back to October 14 are preserved verbatim in the [November 13 rotation](archive/STATUS_dated_2026-11-13_rotation.md), the [November 12 rotation](archive/STATUS_dated_2026-11-12_rotation.md), the [November 10 second rotation](archive/STATUS_dated_2026-11-10b_rotation.md) and the archives it points to.

<!-- END set d -->

<!-- BEGIN set e -->
## 📦 DATED DETAIL 9/07 → [archive](archive/STATUS_DETAIL_2026-09.md) (50,350 B, crc32 `645c5ded`); its still-live list → [archive](archive/STATUS_dated-detail-pointer_2026-09-07.md) (1710 B, crc32 `fa53ae4a`)

> **Still live, each at its owner:** BG-02 letter (Will 9/7, WQ-189; prospective-only) → `setups/SPECS_GATES.md` · WQ-189/192 RULED and CLOSED, do not re-open → TRADE · **BRT-30 CONFIRMED 10/26 on the JWLA-034 baseline** → PREDICTIONS + the JWC row above · Russia diesel carve-out Q1 UNKNOWN-AT-PRIMARY → CATALYSTS 9/1 row · FALCON GATE 2 fired on its letter; descriptive, no capital trigger.

> 📦 **Older rotation receipts and archive sets (2026-08-04 → 2026-09-14, plus the tombstone rule)** → [archive](archive/STATUS_dated_2026-11-11c_rotation.md), 652 B crc32 `f7c37db2`.
<!-- END set e -->

<!-- BEGIN set f -->
**Throughput:** current comparable Gulf volume UNRESOLVED on a measured basis. First agency estimate: EIA STEO 11/10 puts Middle East crude shut-ins at 2.5 mb/d in October (10.9 at the May peak), exports up slightly after the Saudi East-West restart (Vortexa), plus STS along Oman [primary text, agency estimate]. One agency on a vendor feed, not a strait count → [note](research/2026-11-10_pickup/NOTE.md#3). **11/11:** OPEC secondary sources put Saudi October at 9.194 against EIA's 9.3, so the 2.5 is confirmed on the level → [grade](research/2026-11-11_saudi-momr/NOTE.md) § 8.
<!-- END set f -->
