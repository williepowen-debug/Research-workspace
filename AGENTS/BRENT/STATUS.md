# BRENT STATUS

**Current judgment — October 28 closeout (23:42 ET onward), SCOPED-PARTIAL:** v5.13 / WAIT unchanged. Product tightness persists while refiners report no demand destruction (Valero Q3 margin $39.24/bbl; Phillips 66 $38.00/bbl, 98% utilization, US diesel demand about −1.5%) [CONF 8-K]. BRT-31 week three −0.6762%, NON-QUALIFYING, OPEN at 40%. No confirmed Saudi production or export loss: the October 27 Ras Tanura hit is a Houthi claim with no Saudi/Aramco statement. [Catch-up report](research/2026-10-28_catchup/REPORT.md).

**🟠 Held-VLO December crack below the $95 NOTICE line (TERRY grades):** HOZ26×42−CLZ26 = **$94.0224 on October 27** (source 2, vendor daily rows within $0.15 of the window proxy) and **$93.0634 on October 28** (source 3 ESTIMATE; the October 28 daily row is evening-session and rejected). Still $2.90+ above the $90.16 sell line. October 23 source 2 reproduces CME FINAL 97.7840 exactly. [Observations](research/2026-10-28_catchup/vlo-source3/source2_check.json); packets to TERRY and HENRY.

**Settlements (wire-reported, not exchange pages) [EST]:** Brent December BZZ26 **115.81 / 113.88 / 115.32**; WTI December CLZ26 **101.76 / 99.90 / 102.78** on October 26 / 27 / 28. WTI−Brent −12.54 on October 28. Dated Brent physical 123.10 on October 27 [CONF FRED], above $120 (thresholds.py grades). October 27 fell on Iran–Saudi talks; October 28 rose mainly on the relayed WSJ report of a "short, intense" US campaign after the November 3 midterms. Brent December last trades Friday October 30.

**Official boundary:** CME has **IP-blocked this machine** (HTTP 403, terms-of-use message, October 28 23:49 ET); no evasion attempted. Latest authenticated CME pair remains October 23 (CLZ26 103.27 / HOZ26 4.7870, crack 97.7840). No official ICE page read. Vendor and wire values never complete a registered count.

**Throughput:** current comparable Gulf volume UNRESOLVED. PortWatch chokepoint 6, October 18–25: 2–5 AIS-visible transits a day, 0–2 tankers (lower bound, not volume). Iran's strait authority (PGSA) declared "legal action" against all Sinokor vessels from **November 1**; Sinokor carries around half of Hormuz supertanker transits (Lloyd's List, October 26). Watch freight and route exits November 1–3. Qatar's 7-day draft framework awaits Tehran's reply.

**Routines:** L526 boot preamble **installed live** in all four routines (WQ-510 A, 2026-10-29 03:45–03:46Z). The October 4 prompt correction went live with it; before this, the live prompts were still the October 2 text. Thursday connector removal remains a Will UI action. [Install report](audits/2026-10-28_L526-preamble-install/REPORT.md).

**Last real market/source refresh:** October 28, 23:42–23:58 ET: EIA week 10/23 (release-day files), EIA retail 10/26, vendor one-minute and daily bars, wire settlements, issuer 8-Ks via the sweep. Not refreshed: COT (next #12 October 30), insurance quotes, FINRA USO short interest. Prior header and summary: [rotation](archive/STATUS_dated_2026-10-28_rotation.md), 3,406 B crc32 `4fc76796`. Positions/receipts → [TRADE](TRADE.md); broker truth off-repo.

**Navigation:** [README](README.md) · [handoff](SCRATCH.md) · [cleanup accepted; warning retained](audits/2026-10-20_organisation-cleanup/REVIEW-CLOSED.md) · [USO](USO/README.md) · [live-routine acceptance still unverified](audits/2026-10-04_cato-correction/REPORT.md#live-deployment-follow-up--2026-10-04-2302-et).

---

# ⚡ CURRENT STATE — *read this first. Dated blocks follow newest first; STANDING STATE is the hot half; ARCHIVE INDEX is history.*


**Correction sentinels retained hot:** GulfTimes October12 transit figures match Reuters August17; quarantine as October evidence ([check](research/2026-10-12_resume-l633/MAIL_UPDATE.md#cor-20261012-04--transit-vintage)). Dated Brent >$120 was a real breach (EIA RBRTE125.44 on10/6,135.51 on10/2); the10/8 anomaly/not-real-breach label remains withdrawn. These are dated corrections, not fresh observations or proof of barrels lost.

## 📌 STANDING STATE — *current values, live rules and active obligations. Read this; it is the hot half.*

> ⚑ **CREATED 2026-09-07 — first application site of READ_CAP rule 19** (Will-ruled; DAEDALUS P1 ACTIONs 1–4).
> **Reconciliation October 28 (catch-up closeout):** all 8 rows re-read after the day's docket grades; both archive payloads reproduce; no fresh COT/JWC/rig observation. **October 26 (key-file review):** both standing archive payloads re-hashed and reproduced; closed BRT-26 and COT #11 matched to owner rows, JWC to saved October 26 grade, sentinels/source scope read, THESIS/TRADE/owner links reconciled. No fresh weekly/COT/insurance observation claimed. [Receipt and scope](audits/2026-10-26_key-file-review/REPORT.md).
> **The rows below are STANDING, not dated** — extracted verbatim, each carrying `⏱ as-of` (data vintage) and `✓ reconciled` (last checked against its canonical record). 📖 *(how the extraction was scoped, and the stale line-number near-miss: `archive/STATUS_DETAIL_2026-09.md` § repairs)*

| | |
|---|---|
| **📦 **DATED HISTORY 2026-08-27 → 2026-08-09 — ROTATED VERBATIM, LOAD-BEARING CONTENT RETAINED BELOW.** ✓ **reconciled `2026-10-28`** (payload re-hashed October 28 after the docket grades: 88,876 B, `4bb7aad6` reproduces, rule = after first standalone separator; receipt unchanged) | **88,876 UTF-8 payload bytes → [`workbook/STATUS_archive_20260828_dated_history_wave2.md`](workbook/STATUS_archive_20260828_dated_history_wave2.md), `crc32 4bb7aad6`, contiguous, zero edits.** ⛔ **Historical payload checksum confirmed; prior byte count corrected. No live rules moved by this review.** Every ladder figure, band, baseline and ⛔⛔ sentinel from those rows is preserved in the four rows that follow. **Read the archive for the reasoning; these rows carry the constraints.** |
| **BRT-26 rig ladder / frozen line** · as-of **2026-09-25** · ✓ **reconciled `2026-10-28`** (PREDICTIONS row re-read October 28: CONFIRMED 2026-09-25, closed; no new rig pull) | **✅ RESOLVED CONFIRMED 2026-09-25: US Oil 455 (+3) at the final in-window print, 457 NOT reached (headroom 2)**. Baker Hughes primary (09-25-2026 workbook, D4 25/09/2026), 3 retrievals, one lineage. Horizontal −1 ⇒ mechanism unchanged; part of the win is lag timing. Brier 0.0225 at 85%. Grade and caveats: [BRT-26 note](thesis/prediction_notes/BRT-26.md) § September 25. The 457 line now governs nothing live. |
| **COT-FUEL-35B — frozen band** · saved vintage **#11, as-of 2026-10-20** · ✓ **reconciled `2026-10-28`** (ledger tail re-read October 28: last row as-of 2026-10-20, 127,226 / 6.9328%, graded NOT-SPENT; no new CFTC pull or append) | **Base `122,904.5` (trailing-8wk median 2026-06-16…08-04; an 8-observation median = mean of `122,319` and `123,490`) · Leg-A SPENT ≤`109,164` · NO-VERDICT deadband `109,165–118,325` · NOT-SPENT ≥`118,326` · Leg-B OI-share ≤`4.909%` GATING · `median_unit 9,160` FROZEN · both legs must agree; NO-VERDICT is a real answer (base-case sizing).** ⚠️ **`113,745` is the deadband's CENTRE, never a boundary — THE DEADBAND IS DECISIVE INSIDE ITS RANGE.** **Saved #11 grade (10/23 15:51 ET): JOINT NOT-SPENT, fifth consecutive** (shorts 127,226, 8,900 above the deadband top; OI share 6.9328%). Current inputs and dated receipt → [ledger](workbook/COT_VINTAGES.tsv) / [10/23 report](research/2026-10-23_inbox-catchup/REPORT.md) §1. Next #12: as-of October 27, release Friday October 30 ~15:30 ET. Historical ladder preserved [verbatim](archive/2026-10-20_consistency-repair/STATUS.md). ✅ **4.909% REPRODUCED 2026-09-18 at the CFTC archive: 104 obs ending 8/4 inclusive = 4.9086% (REGISTRY note; the only window definition that reproduces). RE-REPRODUCED 2026-10-08 16:37 ET from a fresh archive download: 4.908595% (identical; PM note).** ⛔ **Re-basing = a NEW N1 build + a fresh Will ruling, never maintenance.** 📖 *(repair record: `archive/STATUS_DETAIL_2026-09.md` § repairs)* |
| **JWC / WAR-RISK BASELINE** · document as-of **2026-09-16 (JWLA-035)** · ✓ **reconciled `2026-10-28`** (BRT-30 PREDICTIONS row re-read: CONFIRMED 2026-10-26; IUA index NOT re-fetched October 28, so the listing state is as of October 26) | **JWLA-035 (16 Sep 2026) read at the LMA PDF 2026-09-18: amends Europe/Black Sea ONLY; Persian/Arabian Gulf, Gulf of Oman, Indian Ocean, Gulf of Aden and Southern Red Sea (south of 25.5°N — Yanbu is INSIDE), Saudi Arabia, Yemen, Oman, Iran, Iraq, Kuwait, Qatar, UAE, Bahrain ALL STILL LISTED ⇒ `KILL-LEG2-JWC-LISTING` NOT FIRED; probe baseline re-stamped 034→035; BRT-30's frozen prediction baseline stays JWLA-034 (closed CONFIRMED 10/26).** Listing is neither a current premium quote nor throughput evidence. |
| **⛔⛔ **RETAINED — ALL 17 CORRECTED-CLAIM SENTINELS FROM THE ROTATED ROWS (one line each; full narrative in the archive). These are historical correction reminders, not refreshed market claims; they stop a wrong claim re-entering by pattern-match — the compression target is the prose, never the constraint.** ✓ **reconciled `2026-10-28`** (all 17 sentinels re-read against the October 28 catch-up; ⑤ applied to the Hormuz reopening relays and ⑧ to PortWatch; no retired instrument, revived claim or operator-free loss adopted) | **① Context notes are NOT trade proposals — `$0` moved.** · **② The 38%-of-war-days-at/below-bar caveat: longest run 2026-06-12→07-20, 25 trading days, went NEGATIVE to −3.27.** · **③ Source class upgraded — first PRIMARY-sourced BRT-26 grade, and the reason was a month-old error of mine.** · **④ Baker Hughes request failures are not publisher outages. Minimal headers recovered the September 11 workbook on September 15; old categorical header/WAF-cause assertions are withdrawn.** · **⑤ STANDING KILL-ON-SIGHT: a "Hormuz is open" headline on US authority is a claim about LEGAL/MILITARY status, never THROUGHPUT.** · **⑥ The 8/15 incident is NOT the same event — UKMTO used the identical phrase "unknown projectile" for both.** · **⑦ Boot-protocol gap: an autonomous routine ran 09:55 and boot never read it.** · **⑧ PortWatch required target observations remain missing; access recovered. Instrument coverage failure does not refute the premise.** · **⑨ Near-miss: `instrument_check` reported FRED-GASREGW DEAD on an SSL timeout — a source that HANGS is not a source that is DOWN.** · **⑩ The silent-UNFIRE hazard is REAL — a fired modifier can un-fire under REVERT semantics.** · **⑪ `BRT-26` keys on the OIL leg, NEVER the US total.** · **⑫ The archived EU-storage low/90%-out-of-reach forecast is DATED HISTORY, not a current measurement or deadline. Current decision dates/targets live in the docket.** · **⑬ A same-day RETRACTION by my own vintage ladder (P1) — original text preserved.** · **⑭ P2: 3.0M bpd of asserted OFFLINE capacity was WRONG, and it cuts against my own thesis.** · **⑮ The crowd found a zero-transit day my own throughput record missed by one day.** · **⑯ DEMOTED 8/17 — both claims in that cell are CANDIDATE DETECTION ARTEFACTS, not established physical events.** · **⑰ The peak landed at the PRICE LOW — 8/5 front futures $79.45, bottom of the ~15% selloff.** |
| **EXPORT-SIGN WARNING** · ✓ **reconciled `2026-10-28`** (applied to the week-10/23 EIA print: crude exports 4.854M b/d, +1.412M WoW, recorded with no causal attribution) | **Refinery outages can free crude feedstock for export**, conditional on production, storage, domestic use and export-route availability. A terminal/pipeline loss has a different effect. Rising crude exports alone do not establish greater supply or a measured refinery-loss contribution. Old August Russia/Gulf figures are historical, not a current causal decomposition. [THESIS transmission table](thesis/THESIS.md) and [incident review](research/2026-09-15_backlog-review/INCIDENT_REVIEW.md). |
| **STANCE + GATE STATE** · ✓ **reconciled `2026-10-28`** (THESIS v5.13 and TRADE re-read; WQ-264 shadow run closed INCOMPLETE, see sentence below) | **THESIS v5.13 (10/14 OMR crude/product/global-demand refinement; 9/30: F-b Cushing FIRED on its letter; BRT-29 FAILED; BRT-12 VOID; 10/01 BRT-31 registered, no version bump); v5.8 numerical calibration retained; WQ-192 stand-down unchanged.** Deploy gate v3 retired August 7; no registered re-arm. Surviving frame-breaker, Stage-A and off-ramp clauses remain governed by [TRADE](TRADE.md) and its complete specs; this row provides no capital authority. A deal is not measured throughput. **9/25 17:0x: BG-02 instance (4) LAPSED ⇒ NOT MET on the letter** (not re-opened, not extended). The successor restart resolver (9/18 PROPOSAL `setups/2026-09-18_saudi-restart-resolver-PROPOSAL.md`) remains unregistered: the WQ-264 shadow run ended October 24 with only 3 logged reads (9/25, 9/28, 10/2) of about 30 planned, too few to set its threshold, so it is not registrable as designed (re-run or abandon = PROME/Will). Nothing armed. [Reconciliation scope](research/2026-09-15_backlog-review/STANDING_REVIEW.md). |
| **➡️ EVERYTHING ELSE THAT USED TO BE RESTATED HERE NOW LIVES WITH ITS OWNER** ✓ **reconciled `2026-10-28`** (owner files present; standing-block archive re-hashed October 28: 9,970 B, `d82761d3` reproduces) | ⛔⛔ **NINE 'standing state' rows were rotated out 2026-08-21 → [`workbook/STATUS_archive_20260821_standing_blocks_aug4_aug13.md`](workbook/STATUS_archive_20260821_standing_blocks_aug4_aug13.md)** (9 rows, 9,970 UTF-8 payload bytes, `crc32 d82761d3`, VERBATIM). **THREE OF THEM HAD GONE FACTUALLY FALSE** while sitting under a CURRENT heading — *"NO OPEN ACTION"* (Will ruled SELL ONE 8/21, unexecuted), *"INBOX EMPTY 8/7"* (14 days stale), *"NOTHING OWED TO WILL"* (three `KILL-LEG2` decisions are with him now). ★ **The cause was DUPLICATION, not staleness — a second copy cannot be kept in sync and will always eventually contradict its owner.** ⇒ **CANONICAL OWNERS, read them instead: positions / action state / arm triggers / execution log → [`TRADE.md`](TRADE.md) · mail state → `board_log.tsv` · owed decisions + next-session items → [`SCRATCH.md`](SCRATCH.md) · thesis stance → [`thesis/THESIS.md`](thesis/THESIS.md) · every registered test → [`workbook/REGISTRY.tsv`](workbook/REGISTRY.tsv).** |

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
| **Fri Oct 30** | BZZ26 LAST TRADING DAY — boundary #8 (Brent 3:2:1) month switch: Dec legs BZZ26/RBZ26/HOZ26 → Jan BZF27/RBF27/HOF27 from the FIRST SESSION AFTER (Mon 11/2) | 🟡 |
| **Fri Oct 30** | CFTC COT #12 — as-of October 27, release ~15:30 ET (COT-FUEL-35B) | 🟠 |
| **Sat Oct 31** | RUSSIA PRODUCER DIESEL EXPORT BAN — extended expiry (successor to the 9/30 row) | 🟠 |
| **Sun Nov 1** | IRAN PGSA 'LEGAL ACTION' VS ALL SINOKOR VESSELS — effective date | 🟠 |
| **~Sun Nov 1** ⌁*modeled* | 🟠 EU GAS STORAGE — RESOLVED 2026-08-13: the target, the DATE and the pace are now all verified | 🟠 |
| **Sun Nov 1** | ROUTINE CRONS — DST RE-SET (EST begins): move all four BRENT routines +1h UTC | 🟠 |
| **Sun Nov 1** | 🟠 OPEC+ SEVEN-COUNTRY MONTHLY MEETING — the December 2026 production decision (successor to the 10/4 row) | 🟠 |
| **Mon Nov 2** | YUR-005 — Russia Resolution 1252 producer restriction: extended, lapsed or replaced? | 🟠 |
| **Tue Nov 3** | MPC Q3 2026 RESULTS — L689 conditional refiner candidate | 🟠 |
| **~Tue Nov 3** ⌁*modeled* | ARAMCO Q3 2026 RESULTS and US MIDTERM ELECTION | 🟠 |
| **Fri Nov 13** | NORTHEAST HOME HEATING OIL RESERVE — up to 315,000 bbl exchange deliveries due complete | 🟠 |
| **Wed Nov 18** | WQ-386 HELD VLO — review next crack basis | 🟠 |
| **Thu Nov 19** | WQ-386 HELD VLO — last authorized December leg-A observation | 🟠 |
| **~Fri Nov 20** ⌁*modeled* | CHINA GAC OCTOBER PRODUCT EXPORTS — physical sizing of the October quota (successor to the 10/08 halt row) | 🟡 |
| **Sun Nov 29** | OPEC+ 69th JMMC — monitoring committee (watch for an ONOMM call / 2027-baseline language) | 🟡 |
| **Sun Jan 31 2027** | RUSSIA FUEL EXPORT BAN — full expiry (gasoline all-participants + non-producer diesel) | 🟡 |
| **Wed Apr 7 2027** | OFAC GENERAL LICENSE 135 EXPIRES — Russian-origin diesel (sale, delivery, offloading, importation incl. into the US) authorized through 12:01 a.m. EDT 4/7/2027 | 🟡 |

*`~` + ⌁*modeled* = `date_class=modeled` in the record: a PROJECTED date, not a published one — do not grade a row against a modeled date as though it were confirmed. 7 of 39 rows are modeled.*

*39 event(s), generated from `docket/CATALYSTS.tsv` — the canonical forward-state record. Full graded text lives there and is deliberately not restated. Regenerate with `scripts/render_calendar.py --write`; verify with `--check` at closeout.*

<!-- CALENDAR:END -->
**✅ FIRED & GRADED history:** canonical text remains in `docket/CATALYSTS.tsv`; it is not duplicated here.

---

## SUMMARY FOR WILL

**October 28:** Crude dipped and recovered (Brent December $113.88 → $115.32), driven more by talk of US strikes after the midterms than by the unconfirmed Ras Tanura claim. The diesel crack that governs the held Valero share fell below the $95 notice level on October 27 and 28. That is a notice for TERRY to state, not a sell; the sell line is $90.16, still about $3 away. Refiners report record margins and no demand destruction; gasoline demand is flat on the BRT-31 test. Watch Iran's November 1 action against Sinokor, which carries about half of Hormuz supertanker traffic, and the November 1 OPEC+ meeting, expected to hold steady. Caveats that matter: the October 28 crack is an estimate (CME's site now blocks this machine), and both strike headlines (WSJ, Ras Tanura) are relayed, not primary. WAIT retained; no new Will decision from BRENT. [Report](research/2026-10-28_catchup/REPORT.md).

October 26's summary is preserved in the [rotation](archive/STATUS_dated_2026-10-28_rotation.md), not carried as current.

*(Prior summaries 10/21 and 10/14, the 10/21 evidence-limit sentences, the 10/21 judgment sentences, the 10/21 refresh boundary, the reconciliation note and the 10/14 OMR pointer → [archive](archive/STATUS_dated_2026-10-23_rotation.md), 4138 B crc32 `d37d2d49`.)* *(Prior: 10/8 → [archive](archive/STATUS_DETAIL_2026-10-09.md) (1772 B, crc32 `a3288962`); 10/7 → [archive](archive/STATUS_summary-for-will_2026-10-07.md), 503 B crc32 `b716a32f`; 10/2 16:55 → [archive](archive/STATUS_summary-for-will_2026-10-02_PM.md), 894 B crc32 `8063742b`; 10/2 midday → [archive](archive/STATUS_dated_2026-10-02_midday.md); 10/2 AM → [archive](archive/STATUS_dated_2026-10-02_AM.md); 10/1 + 9/30 → [archive](archive/STATUS_summary-for-will_2026-10-01_and_09-30.md), 1699 B crc32 `4ef5c581`.)*
