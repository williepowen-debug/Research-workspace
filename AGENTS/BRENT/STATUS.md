# BRENT STATUS

**November 6 window and COT (closeout 2026-11-06 15:34 EST, prome-51), SCOPED-PARTIAL:** **COT #13 [CONF raw CFTC, two pulls match]:** as-of 11/3 shorts 125,654 (−651), longs 147,382 (−10,051), OI 1,908,732 (+22,452), 6.5831%, JOINT NOT-SPENT, 7th consecutive. **F-a:** 14:28–14:30 window NOT MEASURABLE, BZH27 no bars in two captures, same-minute +$5.04 at 14:25 ET, not crossed. **BRT-33:** 11/6 no observation, valid 0 of 1; needs 8 or NO-VERDICT → [note](research/2026-11-06_window/NOTE.md). **Window proxies [EST vendor, not settles]:** BZF27 98.35, CLZ26 90.8551, January 3:2:1 $37.19 (boundary #8 count 0), December crack $91.12. November 6 settles and Baker Hughes not read; Friday Close routine carries them. Card 033 logged on combo:diesel-buffer. No line fired.

**November 6 wake (2026-11-06 11:4x EST, Will's word 11:36 ET, prome-51, bounded), SCOPED-PARTIAL:** v5.13 / WAIT unchanged; nothing armed; no line fired; no trade, card, gate, band or threshold moved. **Distillate [CONF EIA history file and WPSR]:** 99.259M week 10/30, lowest since 5/2/2003 (97.303M); SPR 282.184M, lowest since 10/15/1982. Cover 23.8 days on 4,175 kb/d [own arithmetic], lowest late-October reading since 1991. No TRACKER line sits on the level; BRT-34 first grades 11/12, 45% unchanged. **Diesel read (Will 11:49 ET, 1–4): PRICED.** December crack about $90.59 vendor 11:39 ET, 99.9th percentile to 4/2024; Dec 27 crack $66.25; front over fourth 28.75¢, in line with past low-cover weeks. The 8-week draw is seasonal; the low is a carried deficit. Over 39 weeks vs 5-yr: exports −79.1M, production +77.8M, demand −3.5M. BRT-34 mechanism line resolved: exports right, runs wrong, demand right long-run only. → [Diesel note](research/2026-11-06_diesel/NOTE.md). **Card 018 and FALCON:** no lost barrel established, flow NOT MEASURABLE, no November flow or freight print found; BG-02 NOT MET, no INCIDENTS row, BRT-32 no event. **COT-35B:** #13 not out, `cot_grade.py` exit 3; #12 reproduced by own raw pull. **Tape [EST, vendor 11:29 ET, not settles]:** BZF27 $97.88, CLZ26 $90.75, M1−M3 +$5.42, January 3:2:1 $37.30, December crack $90.93. → [Note](research/2026-11-06_wake/NOTE.md).

**Rotated 2026-11-06, second set:** November 5 evening session block and the November 5 summary → [archive](archive/STATUS_dated_2026-11-06b_rotation.md), 2137 B crc32 `5ab808f9`.

**Rotated 2026-11-06:** November 4–5 session block and the November 4 summary → [archive](archive/STATUS_dated_2026-11-06_rotation.md), 1728 B crc32 `a63c015c`.

**Rotated 2026-11-05:** November 2, November 1 and October 29 session blocks and the October 28 summary → [archive](archive/STATUS_dated_2026-11-05_rotation.md), 3551 B crc32 `ee5efd81`.

**Rotated 2026-11-02:** October 28 judgment, the held-VLO October 27–28 $95-notice observations, October 26–28 settlements and the October 28 routine-install paragraph → [archive](archive/STATUS_dated_2026-11-02_rotation.md), 1990 B crc32 `3bea9eb6`.

**Official boundary:** CME has **IP-blocked this machine** (HTTP 403, terms-of-use message, October 28 23:49 ET); no evasion attempted. Latest authenticated CME pair remains October 23 (CLZ26 103.27 / HOZ26 4.7870, crack 97.7840). No official ICE page read. Vendor and wire values never complete a registered count. **WQ-533 (b), Will 10/29 13:33 ET:** sources (2)/(3) accepted as the crack basis while blocked, with a near-the-line exception → [TRADE](TRADE.md).

**Throughput:** current comparable Gulf volume UNRESOLVED. PortWatch chokepoint 6, October 18–25: 2–5 AIS-visible transits a day, 0–2 tankers (lower bound, not volume). Iran's strait authority (PGSA) declared "legal action" against all Sinokor vessels from **November 1**; Sinokor carries around half of Hormuz supertanker transits (Lloyd's List, October 26). Watch freight and route exits November 1–3. Qatar's 7-day draft framework awaits Tehran's reply.

**Last real market/source refresh:** October 28, 23:42–23:58 ET: EIA week 10/23 (release-day files), EIA retail 10/26, vendor one-minute and daily bars, wire settlements, issuer 8-Ks via the sweep. Not refreshed: COT (next #12 October 30), insurance quotes, FINRA USO short interest. Prior header and summary: [rotation](archive/STATUS_dated_2026-10-28_rotation.md), 3,406 B crc32 `4fc76796`. Positions/receipts → [TRADE](TRADE.md); broker truth off-repo.

**Navigation:** [README](README.md) · [handoff](SCRATCH.md) · [cleanup accepted; warning retained](audits/2026-10-20_organisation-cleanup/REVIEW-CLOSED.md) · [USO](USO/README.md) · [live-routine acceptance still unverified](audits/2026-10-04_cato-correction/REPORT.md#live-deployment-follow-up--2026-10-04-2302-et).

---

# ⚡ CURRENT STATE — *read this first. Dated blocks follow newest first; STANDING STATE is the hot half; ARCHIVE INDEX is history.*


**Correction sentinels retained hot:** GulfTimes October12 transit figures match Reuters August17; quarantine as October evidence ([check](research/2026-10-12_resume-l633/MAIL_UPDATE.md#cor-20261012-04--transit-vintage)). Dated Brent >$120 was a real breach (EIA RBRTE125.44 on10/6,135.51 on10/2); the10/8 anomaly/not-real-breach label remains withdrawn. These are dated corrections, not fresh observations or proof of barrels lost.

## 📌 STANDING STATE — *current values, live rules and active obligations. Read this; it is the hot half.*

> ⚑ **CREATED 2026-09-07 — first application site of READ_CAP rule 19** (Will-ruled; DAEDALUS P1 ACTIONs 1–4).
> **Reconciliation November 5 (closeout):** all 8 rows re-read; both archive payloads reproduce (88,876 B `4bb7aad6`, 9,970 B `d82761d3`); BRT-26 and BRT-30 rows and the COT ledger tail match; export row rewritten for week 10/30; stance row carries the November 4 thesis paragraph (WAIT, nothing armed). Row parentheticals dated November 2 keep their own vintage. No fresh COT, JWC or rig observation; the JWC index is still not re-fetched since October 26. **November 2 (closeout):** all 8 rows re-read after the 11/1–11/2 docket grades; both archive payloads reproduce; COT row advanced to #12 from the ledger (routine grade, no live pull); no fresh JWC or rig observation. **October 28 (catch-up closeout):** all 8 rows re-read after the day's docket grades; both archive payloads reproduce; no fresh COT/JWC/rig observation. **October 26 (key-file review):** both standing archive payloads re-hashed and reproduced; closed BRT-26 and COT #11 matched to owner rows, JWC to saved October 26 grade, sentinels/source scope read, THESIS/TRADE/owner links reconciled. No fresh weekly/COT/insurance observation claimed. [Receipt and scope](audits/2026-10-26_key-file-review/REPORT.md).
> **The rows below are STANDING, not dated** — extracted verbatim, each carrying `⏱ as-of` (data vintage) and `✓ reconciled` (last checked against its canonical record). 📖 *(how the extraction was scoped, and the stale line-number near-miss: `archive/STATUS_DETAIL_2026-09.md` § repairs)*

| | |
|---|---|
| **📦 **DATED HISTORY 2026-08-27 → 2026-08-09 — ROTATED VERBATIM, LOAD-BEARING CONTENT RETAINED BELOW.** ✓ **reconciled `2026-11-05`** (payload re-hashed November 2 after the docket grades: 88,876 B, `4bb7aad6` reproduces, rule = after first standalone separator; receipt unchanged) | **88,876 UTF-8 payload bytes → [`workbook/STATUS_archive_20260828_dated_history_wave2.md`](workbook/STATUS_archive_20260828_dated_history_wave2.md), `crc32 4bb7aad6`, contiguous, zero edits.** ⛔ **Historical payload checksum confirmed; prior byte count corrected. No live rules moved by this review.** Every ladder figure, band, baseline and ⛔⛔ sentinel from those rows is preserved in the four rows that follow. **Read the archive for the reasoning; these rows carry the constraints.** |
| **BRT-26 rig ladder / frozen line** · as-of **2026-09-25** · ✓ **reconciled `2026-11-05`** (PREDICTIONS row re-read November 2: CONFIRMED 2026-09-25, closed; 10/30 routine rig print 462 is record-only on the retired line; WALTER boundary 7 retired 10/31) | **✅ RESOLVED CONFIRMED 2026-09-25: US Oil 455 (+3) at the final in-window print, 457 NOT reached (headroom 2)**. Baker Hughes primary (09-25-2026 workbook, D4 25/09/2026), 3 retrievals, one lineage. Horizontal −1 ⇒ mechanism unchanged; part of the win is lag timing. Brier 0.0225 at 85%. Grade and caveats: [BRT-26 note](thesis/prediction_notes/BRT-26.md) § September 25. The 457 line now governs nothing live. |
| **COT-FUEL-35B — frozen band** · saved vintage **#13, as-of 2026-11-03** · ✓ **reconciled `2026-11-06`** (graded live 15:34 ET: 125,654 / 6.5831%, JOINT NOT-SPENT, 7th consecutive; second raw `f_disagg.txt` pull matches, rc 0, no re-issue) | **Base `122,904.5` (trailing-8wk median 2026-06-16…08-04; an 8-observation median = mean of `122,319` and `123,490`) · Leg-A SPENT ≤`109,164` · NO-VERDICT deadband `109,165–118,325` · NOT-SPENT ≥`118,326` · Leg-B OI-share ≤`4.909%` GATING · `median_unit 9,160` FROZEN · both legs must agree; NO-VERDICT is a real answer (base-case sizing).** ⚠️ **`113,745` is the deadband's CENTRE, never a boundary — THE DEADBAND IS DECISIVE INSIDE ITS RANGE.** **Saved #12 grade (10/30, Friday routine, raw `f_disagg.txt`): JOINT NOT-SPENT, sixth consecutive** (shorts 126,305, 7,979 above the NOT-SPENT floor 118,326; OI share 6.6960%). Current inputs and dated receipt → [ledger](workbook/COT_VINTAGES.tsv) / [routine output](demand_destruction/data/friday_2026-10-30.md) §1. Next #13: as-of November 3, release Friday November 6 ~15:30 ET. Historical ladder preserved [verbatim](archive/2026-10-20_consistency-repair/STATUS.md). ✅ **4.909% REPRODUCED 2026-09-18 at the CFTC archive: 104 obs ending 8/4 inclusive = 4.9086% (REGISTRY note; the only window definition that reproduces). RE-REPRODUCED 2026-10-08 16:37 ET from a fresh archive download: 4.908595% (identical; PM note).** ⛔ **Re-basing = a NEW N1 build + a fresh Will ruling, never maintenance.** 📖 *(repair record: `archive/STATUS_DETAIL_2026-09.md` § repairs)* |
| **JWC / WAR-RISK BASELINE** · document as-of **2026-09-16 (JWLA-035)** · ✓ **reconciled `2026-11-05`** (BRT-30 PREDICTIONS row re-read: CONFIRMED 2026-10-26; IUA index NOT re-fetched since October 26, so the listing state is as of October 26 and the instrument stamp is 12d stale vs its 9d budget) | **JWLA-035 (16 Sep 2026) read at the LMA PDF 2026-09-18: amends Europe/Black Sea ONLY; Persian/Arabian Gulf, Gulf of Oman, Indian Ocean, Gulf of Aden and Southern Red Sea (south of 25.5°N — Yanbu is INSIDE), Saudi Arabia, Yemen, Oman, Iran, Iraq, Kuwait, Qatar, UAE, Bahrain ALL STILL LISTED ⇒ `KILL-LEG2-JWC-LISTING` NOT FIRED; probe baseline re-stamped 034→035; BRT-30's frozen prediction baseline stays JWLA-034 (closed CONFIRMED 10/26).** Listing is neither a current premium quote nor throughput evidence. |
| **⛔⛔ **RETAINED — ALL 17 CORRECTED-CLAIM SENTINELS FROM THE ROTATED ROWS (one line each; full narrative in the archive). These are historical correction reminders, not refreshed market claims; they stop a wrong claim re-entering by pattern-match — the compression target is the prose, never the constraint.** ✓ **reconciled `2026-11-05`** (all 17 sentinels re-read November 2; ⑤ applied to the relayed Iran–Qatar ceasefire-talk reports behind the 11/2 price drop; no retired instrument, revived claim or operator-free loss adopted) | **① Context notes are NOT trade proposals — `$0` moved.** · **② The 38%-of-war-days-at/below-bar caveat: longest run 2026-06-12→07-20, 25 trading days, went NEGATIVE to −3.27.** · **③ Source class upgraded — first PRIMARY-sourced BRT-26 grade, and the reason was a month-old error of mine.** · **④ Baker Hughes request failures are not publisher outages. Minimal headers recovered the September 11 workbook on September 15; old categorical header/WAF-cause assertions are withdrawn.** · **⑤ STANDING KILL-ON-SIGHT: a "Hormuz is open" headline on US authority is a claim about LEGAL/MILITARY status, never THROUGHPUT.** · **⑥ The 8/15 incident is NOT the same event — UKMTO used the identical phrase "unknown projectile" for both.** · **⑦ Boot-protocol gap: an autonomous routine ran 09:55 and boot never read it.** · **⑧ PortWatch required target observations remain missing; access recovered. Instrument coverage failure does not refute the premise.** · **⑨ Near-miss: `instrument_check` reported FRED-GASREGW DEAD on an SSL timeout — a source that HANGS is not a source that is DOWN.** · **⑩ The silent-UNFIRE hazard is REAL — a fired modifier can un-fire under REVERT semantics.** · **⑪ `BRT-26` keys on the OIL leg, NEVER the US total.** · **⑫ The archived EU-storage low/90%-out-of-reach forecast is DATED HISTORY, not a current measurement or deadline. Current decision dates/targets live in the docket.** · **⑬ A same-day RETRACTION by my own vintage ladder (P1) — original text preserved.** · **⑭ P2: 3.0M bpd of asserted OFFLINE capacity was WRONG, and it cuts against my own thesis.** · **⑮ The crowd found a zero-transit day my own throughput record missed by one day.** · **⑯ DEMOTED 8/17 — both claims in that cell are CANDIDATE DETECTION ARTEFACTS, not established physical events.** · **⑰ The peak landed at the PRICE LOW — 8/5 front futures $79.45, bottom of the ~15% selloff.** |
| **EXPORT-SIGN WARNING** · ✓ **reconciled `2026-11-06`** (week 10/30 crude exports 3.675M b/d, −1.179M WoW, 4-week average 4.135M b/d [CONF WPSR table1 via routine file demand_destruction/data/eia_2026-11-04.md], no causal attribution) | **Refinery outages can free crude feedstock for export**, conditional on production, storage, domestic use and export-route availability. A terminal/pipeline loss has a different effect. Rising crude exports alone do not establish greater supply or a measured refinery-loss contribution. Old August Russia/Gulf figures are historical, not a current causal decomposition. [THESIS transmission table](thesis/THESIS.md) and [incident review](research/2026-09-15_backlog-review/INCIDENT_REVIEW.md). |
| **STANCE + GATE STATE** · ✓ **reconciled `2026-11-05`** (THESIS v5.13 and TRADE re-read November 2; OPEC+ December HELD 11/1 changes no gate; WQ-264 shadow run closed INCOMPLETE, see sentence below) | **THESIS v5.13 (10/14 OMR crude/product/global-demand refinement; 9/30: F-b Cushing FIRED on its letter; BRT-29 FAILED; BRT-12 VOID; 10/01 BRT-31 registered, no version bump); v5.8 numerical calibration retained; WQ-192 stand-down unchanged.** Deploy gate v3 retired August 7; no registered re-arm. Surviving frame-breaker, Stage-A and off-ramp clauses remain governed by [TRADE](TRADE.md) and its complete specs; this row provides no capital authority. A deal is not measured throughput. **9/25 17:0x: BG-02 instance (4) LAPSED ⇒ NOT MET on the letter** (not re-opened, not extended). The successor restart resolver (9/18 PROPOSAL `setups/2026-09-18_saudi-restart-resolver-PROPOSAL.md`) remains unregistered: the WQ-264 shadow run ended October 24 with only 3 logged reads (9/25, 9/28, 10/2) of about 30 planned, too few to set its threshold, so it is not registrable as designed. **ABANDONED by Will 10/29 13:33 ET (WQ-533 (a)); no Saudi-relief grader is registered (WQ-331 P4).** Nothing armed. [Reconciliation scope](research/2026-09-15_backlog-review/STANDING_REVIEW.md). |
| **➡️ EVERYTHING ELSE THAT USED TO BE RESTATED HERE NOW LIVES WITH ITS OWNER** ✓ **reconciled `2026-11-05`** (owner files present; standing-block archive re-hashed November 2: 9,970 B, `d82761d3` reproduces) | ⛔⛔ **NINE 'standing state' rows were rotated out 2026-08-21 → [`workbook/STATUS_archive_20260821_standing_blocks_aug4_aug13.md`](workbook/STATUS_archive_20260821_standing_blocks_aug4_aug13.md)** (9 rows, 9,970 UTF-8 payload bytes, `crc32 d82761d3`, VERBATIM). **THREE OF THEM HAD GONE FACTUALLY FALSE** while sitting under a CURRENT heading — *"NO OPEN ACTION"* (Will ruled SELL ONE 8/21, unexecuted), *"INBOX EMPTY 8/7"* (14 days stale), *"NOTHING OWED TO WILL"* (three `KILL-LEG2` decisions are with him now). ★ **The cause was DUPLICATION, not staleness — a second copy cannot be kept in sync and will always eventually contradict its owner.** ⇒ **CANONICAL OWNERS, read them instead: positions / action state / arm triggers / execution log → [`TRADE.md`](TRADE.md) · mail state → `board_log.tsv` · owed decisions + next-session items → [`SCRATCH.md`](SCRATCH.md) · thesis stance → [`thesis/THESIS.md`](thesis/THESIS.md) · every registered test → [`workbook/REGISTRY.tsv`](workbook/REGISTRY.tsv).** |

---

## 📦 DATED DETAIL 9/07 → [archive](archive/STATUS_DETAIL_2026-09.md) (50,350 B, crc32 `645c5ded`); its still-live list → [archive](archive/STATUS_dated-detail-pointer_2026-09-07.md) (1710 B, crc32 `fa53ae4a`)

> **Still live, each at its owner:** BG-02 letter (Will 9/7, WQ-189; prospective-only) → `setups/SPECS_GATES.md` · WQ-189/192 RULED and CLOSED, do not re-open → TRADE · **BRT-30 CONFIRMED 10/26 on the JWLA-034 baseline** → PREDICTIONS + the JWC row above · Russia diesel carve-out Q1 UNKNOWN-AT-PRIMARY → CATALYSTS 9/1 row · FALCON GATE 2 fired on its letter; descriptive, no capital trigger.

---

## 📚 ARCHIVE INDEX + OWNER POINTERS — *one line each; narrative lives at the link*

> 📦 **Rotation receipts (every crc32, 2026-08-04 → 2026-09-14) live in [archive/STATUS_DETAIL_2026-09.md](archive/STATUS_DETAIL_2026-09.md) § ROTATED 2026-09-14** — moved there 2026-09-14 because a receipt is PROVENANCE, not state. Older sets: [`workbook/STATUS_archive_*`](workbook/) (8/4 · 8/7 · 8/13 · 8/21 ×2 · 8/27 · 8/28) · [`archive/STATUS_dated_2026-09-09_audit.md`](archive/STATUS_dated_2026-09-09_audit.md) · [`archive/STATUS_dated_2026-09-09_maintenance.md`](archive/STATUS_dated_2026-09-09_maintenance.md). ⛔ **Every rotation was VERBATIM; tombstones and impeachment banners that still BIND live in STANDING STATE above.**

> ➡️ **OWNERS (read these, never a copy here):** thesis stance → [`thesis/THESIS.md`](thesis/THESIS.md) · positions / rules / execution log → [`TRADE.md`](TRADE.md) · predictions → [`thesis/PREDICTIONS.tsv`](thesis/PREDICTIONS.tsv) · registered tests → [`workbook/REGISTRY.tsv`](workbook/REGISTRY.tsv) · operational lines → `demand_destruction/TRACKER.md` · forward items → [`SCRATCH.md`](SCRATCH.md) § NEXT SESSION + `docket/CATALYSTS.tsv` · Saudi dual-route watch (7/21, never executed) → Yanbu/Bab rows in `docket/CATALYSTS.tsv` + `refinery_damage/INCIDENTS.tsv` · convergence matrix: 7/21 score is a point-in-time record, a new read is a fresh scoring pass.

---
## 📅 CATALYST CALENDAR (forward; canonical source `docket/CATALYSTS.tsv`)

> Generated view of `docket/CATALYSTS.tsv` (human twin, same event SET). `scripts/render_calendar.py --write`; boot's Derived Views check fails closed on drift. Unresolved rows with past dates stay until GRADED — an expired date is not completion.

<!-- CALENDAR:BEGIN generated from docket/CATALYSTS.tsv — do not hand-edit -->

| Date | Release | Priority |
|------|---------|----------|
| **Tue Sep 1** | RUSSIA producer-direct carve-out — September 8 Q1 read UNKNOWN-AT-PRIMARY | 🔴 |
| **Tue Oct 6** | ✅ EIA October STEO — GRADED 2026-10-07: release and same-series comparison MET | 🟠 |
| **Tue Oct 6** | SPR EXCHANGE (up to 40M bbl, Big Hill + Bryan Mound) — BIDS CLOSE 11:00 CT; awards follow | 🟠 |
| **~Thu Oct 8** ⌁*modeled* | ✅ CHINA PRODUCT-EXPORT HALT — GRADED 2026-10-09: GUIDANCE MET (unofficial) — October exports APPROVED ~3.7 Mt gasoline+diesel+jet combined, below Sep ~4 Mt expected and Aug 4.6 Mt actual;… | 🟠 |
| **Sat Oct 10** | HURRICANE ISAIAS — northern Gulf landfall (late Fri 10/9 – early Sat 10/10) and offshore/refinery restart read | 🟠 |
| **~Sat Oct 10** ⌁*modeled* | IRAN-OMAN PERMANENT-ROUTE WINDOW — owner L229 LAPSED / NOT VERIFIED AS AGREED October 26 | 🟠 |
| **Sat Oct 10** | DIESEL TAX RELIEF — five-day implementation directive from October5 order | 🟠 |
| **Wed Oct 14** | 🟠 IEA OMR OCTOBER — stock-release delivery / supplemental-diesel watch + global stock draw | 🟠 |
| **Thu Oct 15** | ✅ IEA GOVERNING BOARD — GRADED October20: October15 statement/acceleration verified; delivery sizing remains open | 🟠 |
| **~Thu Oct 22** ⌁*modeled* | G7 STOCK IMPLEMENTATION — modeled end of first20-day frontloaded-diesel window (October2 commitment,100M oil over4months; incremental overlap not assumed) | 🟠 |
| **Thu Oct 22** | ✅ VALERO Q3 2026 RESULTS — GRADED 2026-10-28: margin $39.24/bbl, runs 2,972 kb/d, 'no signs of demand destruction' | 🟠 |
| **Thu Oct 22** | ✅ HELD VLO LEG-A — first December observation PUBLISHED 2026-10-28: Oct 22 = $99.4672 (source 2) | 🟠 |
| **Thu Oct 22** | AAL Q3 RESULTS (call 08:30 ET) and LUV Q3 CALL (10:00 ET) — HEN-46 resolution; realized jet-fuel cost read | 🟡 |
| **Fri Oct 23** | ✅ CFTC COT #11 — GRADED 2026-10-23 15:51 ET: JOINT NOT-SPENT, 5th consecutive (shorts 127,226; OI share 6.9328%) | 🟠 |
| **Sat Oct 24** | TEXAS DIESEL WAIVER — existing 20-day window ends | 🟠 |
| **Sat Oct 24** | ✅ WQ-264 YANBU BERTH SHADOW RUN — ENDED 2026-10-24, INCOMPLETE: 3 logged reads of ~30 planned | 🟠 |
| **Mon Oct 26** | USO SHORT INTEREST — October15 settlement snapshot publication | 🟡 |
| **Mon Oct 26** | ✅ BRT-30 — GRADED 2026-10-26 CONFIRMED: both Gulf areas remain listed | 🟠 |
| **Tue Oct 27** | ✅ EQT/RANGE Q3 RESULTS — GRADED 2026-10-28: EQT 583 Bcfe incl. 21 curtailed; calls cancelled | 🟡 |
| **Wed Oct 28** | ✅ PHILLIPS66 Q3 2026 RESULTS — GRADED 2026-10-28: margin $38.00/bbl, 98% utilization, record 41% distillate yield | 🟡 |
| **Wed Oct 28** | ✅ EIA WPSR — week ending 10/23 GRADED 2026-10-28: BRT-31 week three −0.6762%, NON-QUALIFYING | 🟠 |
| **~Thu Oct 29** ⌁*modeled* | TOTALENERGIES Q3 2026 RESULTS — written SATORP restart confirmation | 🟡 |
| **Fri Oct 30** | ✅ BZZ26 LAST TRADING DAY — GRADED 2026-11-05: January legs verified, boundary #8 count 0 — boundary #8 (Brent 3:2:1) month switch: Dec legs BZZ26/RBZ26/HOZ26 → Jan BZF27/RBF27/HOF27 from… | 🟡 |
| **Fri Oct 30** | ✅ CFTC COT #12 — GRADED 2026-10-30 by the Friday routine: JOINT NOT-SPENT, 6th consecutive (shorts 126,305; OI share 6.6960%) | 🟠 |
| **Sat Oct 31** | ✅ RUSSIA PRODUCER DIESEL EXPORT BAN — GRADED 2026-11-01: EXTENDED to 31.01.2027 (producer exemption deleted) | 🟠 |
| **Sun Nov 1** | IRAN PGSA 'LEGAL ACTION' VS ALL SINOKOR VESSELS — effective date | 🟠 |
| **~Sun Nov 1** ⌁*modeled* | 🟠 EU GAS STORAGE — RESOLVED 2026-08-13: the target, the DATE and the pace are now all verified | 🟠 |
| **Sun Nov 1** | ✅ ROUTINE CRONS — DST RE-SET DONE 2026-11-02 02:28–02:30Z by PROME (WQ-585 A), with the WQ-543 text; validation PASS | 🟠 |
| **Sun Nov 1** | ✅ OPEC+ SEVEN-COUNTRY MONTHLY MEETING — GRADED 2026-11-01: OUTCOME (1) DECEMBER HELD (third consecutive hold) | 🟠 |
| **Mon Nov 2** | ✅ YUR-005 — GRADED HIT by YURI 2026-10-31: extended by Resolution №1436 to 31.01.2027 (BRENT consequence read on the 10/31 row) | 🟠 |
| **Tue Nov 3** | MPC Q3 2026 RESULTS — L689 conditional refiner candidate | 🟠 |
| **~Tue Nov 3** ⌁*modeled* | ARAMCO Q3 2026 RESULTS and US MIDTERM ELECTION | 🟠 |
| **Wed Nov 4** | ✅ EIA WPSR — week ending 10/30 GRADED 2026-11-05: BRT-31 week four −0.4351%, NON-QUALIFYING | 🟠 |
| **Thu Nov 5** | ✅ BRENT M1−M3 SETTLEMENT WINDOW — GRADED 2026-11-05: window NOT MEASURABLE (BZH27 no bars), F-a not crossed | 🟠 |
| **Fri Nov 6** | ✅ CFTC COT #13 — GRADED 2026-11-06 15:34 ET: JOINT NOT-SPENT, 7th, 125,654 / 6.5831% | 🟠 |
| **Tue Nov 10** | EIA NOVEMBER STEO — COPS_OPEC re-pull for the 11/29 OPEC+ letter | 🟡 |
| **Thu Nov 12** | EIA WPSR — week ending 11/6, Veterans Day shifted release, Thursday | 🟠 |
| **Thu Nov 12** | COMBO WATCH yanbu-bypass — is the Red Sea bypass at risk of a real loading loss? | 🟡 |
| **Thu Nov 12** | COMBO WATCH gulf-flow-basis — do the tracker reads converge on one Gulf export figure? | 🟡 |
| **Thu Nov 12** | COMBO WATCH diesel-buffer — is the world diesel buffer thinner than the US stock print shows? | 🟡 |
| **Thu Nov 12** | COMBO WATCH paper-physical-gap — is the paper curve pricing a surplus the physical market does not show? | 🟡 |
| **Thu Nov 12** | COMBO WATCH gulf-access-cost — is the attack pace turning into route exits or cost? | 🟡 |
| **Fri Nov 13** | NORTHEAST HOME HEATING OIL RESERVE — up to 315,000 bbl exchange deliveries due complete | 🟠 |
| **Fri Nov 13** | CFTC COT #14 — as-of 11/10, release ~15:30 ET | 🟠 |
| **Wed Nov 18** | ✅ WQ-386 HELD VLO — DISCHARGED 2026-11-05: original share sold, no basis review needed | 🟠 |
| **Thu Nov 19** | ✅ WQ-386 HELD VLO — DISCHARGED 2026-11-05: no further leg-A observations owed | 🟠 |
| **~Fri Nov 20** ⌁*modeled* | CHINA GAC OCTOBER PRODUCT EXPORTS — physical sizing of the October quota (successor to the 10/08 halt row) | 🟡 |
| **Fri Nov 27** | BRT-33 — last session of M1−M3 BZF27−BZH27 on the pinned pair | 🟠 |
| **Sun Nov 29** | OPEC+ 69th JMMC — monitoring committee (watch for an ONOMM call / 2027-baseline language) | 🟡 |
| **Sun Nov 29** | 🟠 OPEC+ SEVEN-COUNTRY MONTHLY MEETING — the January 2027 production decision (successor to the 11/1 row) | 🟠 |
| **Tue Dec 1** | COMBO WATCH us-fuel-policy — will Washington tax or restrict fuel? | 🟡 |
| **Mon Dec 21** | BRT-35 — last GASREGW print in the window | 🟠 |
| **Wed Dec 23** | BRT-34 — WPSR for data week 12/18, last window print | 🟠 |
| **Thu Dec 31** | BRT-32 — Yanbu loading-halt window ends | 🟠 |
| **Sun Jan 31 2027** | RUSSIA FUEL EXPORT BAN — full expiry (gasoline all-participants + non-producer diesel) | 🟡 |
| **Wed Apr 7 2027** | OFAC GENERAL LICENSE 135 EXPIRES — Russian-origin diesel (sale, delivery, offloading, importation incl. into the US) authorized through 12:01 a.m. EDT 4/7/2027 | 🟡 |

*`~` + ⌁*modeled* = `date_class=modeled` in the record: a PROJECTED date, not a published one — do not grade a row against a modeled date as though it were confirmed. 7 of 56 rows are modeled.*

*56 event(s), generated from `docket/CATALYSTS.tsv` — the canonical forward-state record. Full graded text lives there and is deliberately not restated. Regenerate with `scripts/render_calendar.py --write`; verify with `--check` at closeout.*

<!-- CALENDAR:END -->
**✅ FIRED & GRADED history:** canonical text remains in `docket/CATALYSTS.tsv`; it is not duplicated here.

---

## SUMMARY FOR WILL

**November 6 close:** Speculators' bets against oil are still not used up: 125,654 short contracts in the week to November 3, the seventh straight NOT-SPENT reading, which matters only as a sizing descriptor. The March Brent contract did not trade in today's window, so the spread forecast has no reading for its first day. No BRENT line fired.

**November 6:** US distillate stocks are confirmed at 99.3 million barrels, the lowest since May 2003, and about 23.8 days of cover, the thinnest late-October reading since 1991. No BRENT line fired. Diesel is PRICED: the crack is near a record and scarcity is priced a year out. The recent draw is normal for the season; the low comes from exports running about 24% above normal for nine months, covered only by refiners running very hard. The tanker incidents establish no lost barrel, but no November flow or freight print exists at sources reached, so that is coverage, not a zero. WAIT retained; no new Will decision from BRENT.

October 28's summary is preserved in the [November 5 rotation](archive/STATUS_dated_2026-11-05_rotation.md), not carried as current.

October 26's summary is preserved in the [rotation](archive/STATUS_dated_2026-10-28_rotation.md), not carried as current.

*(Prior summaries 10/21 and 10/14, the 10/21 evidence-limit sentences, the 10/21 judgment sentences, the 10/21 refresh boundary, the reconciliation note and the 10/14 OMR pointer → [archive](archive/STATUS_dated_2026-10-23_rotation.md), 4138 B crc32 `d37d2d49`.)* *(Prior: 10/8 → [archive](archive/STATUS_DETAIL_2026-10-09.md) (1772 B, crc32 `a3288962`); 10/7 → [archive](archive/STATUS_summary-for-will_2026-10-07.md), 503 B crc32 `b716a32f`; 10/2 16:55 → [archive](archive/STATUS_summary-for-will_2026-10-02_PM.md), 894 B crc32 `8063742b`; 10/2 midday → [archive](archive/STATUS_dated_2026-10-02_midday.md); 10/2 AM → [archive](archive/STATUS_dated_2026-10-02_AM.md); 10/1 + 9/30 → [archive](archive/STATUS_summary-for-will_2026-10-01_and_09-30.md), 1699 B crc32 `4ef5c581`.)*
