# BRENT STATUS

> **CATO bounded repair, 2026-09-15:** rig-reader missing-current-cell failure fixed; prior mail filing reconciled. [Repair and checks](../CATO/runs/2026-09-15_1904_brent-walter-repair.md). No new market observation, prediction grade or position change.

> **Workdown 2026-09-15 — SCOPED-PARTIAL:** Receipt/rig readers and diesel metadata repaired; September 11 rig observation graded. [Evidence and remaining queue](research/2026-09-15_workdown/REPORT.md). All six previously flagged standing rows reconciled with content corrections. EIA retains September 4 vintage; older market analysis was not re-underwritten. Positions are owned by TRADE.md.

**Last real data refresh: 2026-09-16 — scoped:** EIA primary through September11; named-contract market snapshot September16 14:19 EDT; direct source checks through 18:34 UTC. [Cross-war reassessment](research/2026-09-16_cross-war-oil/REPORT.md), [market basis](research/2026-09-16_cross-war-oil/MARKET.md), [SPR resolution](research/2026-09-16_cross-war-oil/EIA.md). Refining-margin evidence strengthens; prolonged uninterrupted crude-loss case not confirmed. Net lost crude UNKNOWN. Earlier entries retain their vintages. Positions and approvals: [TRADE.md](TRADE.md).

---

# ⚡ CURRENT STATE — *read this first. Dated blocks follow newest first; STANDING STATE is the hot half; ARCHIVE INDEX is history.*


## September 16 — oil reassessment and EIA resolver

**Products and crude split:** reported Russian refinery shutdowns support product-margin persistence; later crude-export evidence and Saudi partial-restart objectives counter an uninterrupted worsening-crude scenario. Net lost barrels remain UNKNOWN. [Sourced table and dispositions](research/2026-09-16_cross-war-oil/REPORT.md).

**US balance:** L305 Branch A on the frozen numerical test; DOE schedule caveat retained. Cushing above its alert, third distillate build, gasoline T not reached; BRT-29 final OPEN. [Unrounded evidence](research/2026-09-16_cross-war-oil/EIA.md). Morning access gap resolved.

**Market:** backwardation persists and matched product margins strengthen. September15 strength followed September14's pause; the old “repriced once and stopped” description is not current. Intraday diagnostics do not grade a close-specified gate. Fed/dollar, demand and restart expectations coexist. [Dated tape](research/2026-09-16_cross-war-oil/MARKET.md).

**Own correction:** a quoted loading premium does not confirm completed loadings. September14 inference withdrawn. No new national outage sum, YASREF confirmation, generalized Bab closure or capital fire.

**Recovery note 2026-09-17 ~08:4x ET:** the 9/16 session crashed before closeout; this block and the linked files were re-read against HEAD and committed unchanged in substance by a PROME-spawned recovery session, with sender pins filled ([REPORT § Provenance](research/2026-09-16_cross-war-oil/REPORT.md)). HAWK synthesis `b28680b9e` consumed — concordant. FOMC 9/16 hiked 25bp to 3.75–4.00% [CONF PROME brief]. Post-FOMC named check 08:38 ET 9/17 [CONF Yahoo MIRROR, intraday]: BZX26 $101.62 (−3.98%) · CLX26 $94.85 · Nov−Jan +$6.55 — no registered line crossed, no gate graded off intraday; ⚠️ continuous `BZ=F` has rolled onto the Last-Day-Financial contract and its −7.3% print is an artifact.

## September 15 — backlog review

[Full results](research/2026-09-15_backlog-review/REPORT.md): six standing rows reconciled; all twelve aged incidents reviewed; KNPC nameplate corrected and seven stale outage amounts withdrawn. Airline milestone remains indeterminate after additional issuer review. Cargo replacement windows clarified but cancelled volume remains unknown. Shanghai chart verification closed as UNVERIFIED after image arithmetic and Will's source-availability reply; reopen only on new metadata. No new capital grade.

## September 15 — earlier workdown

Primary rig observation graded; receipt and instrument readers repaired; Will confirmed the expired-call sale. Direct Saudi cargo reporting recovered; IATA jet basis integrated. [Evidence, dispositions and remaining work](research/2026-09-15_workdown/REPORT.md). Delivery disruption is reported; aggregate lost barrels and event attribution remain unmeasured. No new BG-02 grade or capital action.

> September 14 dated analysis rotated verbatim to [archive](archive/STATUS_dated_2026-09-14.md), 8757 B, crc32 `45833649`. It is historical analysis, not today's assessment.

## 📌 STANDING STATE — *current values, live rules and active obligations. Read this; it is the hot half.*

> ⚑ **CREATED 2026-09-07 — first application site of READ_CAP rule 19** (Will-ruled; DAEDALUS P1 ACTIONs 1–4).
> **The rows below are STANDING, not dated** — extracted verbatim, each carrying `⏱ as-of` (data vintage) and `✓ reconciled` (last checked against its canonical record). 📖 *(how the extraction was scoped, and the stale line-number near-miss: `archive/STATUS_DETAIL_2026-09.md` § repairs)*

| | |
|---|---|
| **📦 **DATED HISTORY 2026-08-27 → 2026-08-09 — ROTATED VERBATIM, LOAD-BEARING CONTENT RETAINED BELOW.** ✓ **reconciled `2026-09-15`** *(24 STATUS Markdown links resolve; payload CRC rechecked)* | **88,876 UTF-8 payload bytes → [`workbook/STATUS_archive_20260828_dated_history_wave2.md`](workbook/STATUS_archive_20260828_dated_history_wave2.md), `crc32 4bb7aad6`, contiguous, zero edits.** ⛔ **Historical payload checksum confirmed; prior byte count corrected. No live rules moved by this review.** Every ladder figure, band, baseline and ⛔⛔ sentinel from those rows is preserved in the four rows that follow. **Read the archive for the reasoning; these rows carry the constraints.** |
| **BRT-26 rig ladder / frozen line** · as-of **2026-09-18** · ✓ **reconciled `2026-09-18`** | **US Oil 452 (+2), primary verified (live reader, BH workbook uuid ad65c983…). 457 NOT BREACHED, headroom 5; prediction OPEN, confidence unchanged.** One remaining September print: 9/25 (resolves the end-Q3 window). Full original ladder and grading constraints: [before-image](research/2026-09-15_workdown/before/STATUS.md); current observation and one-lineage limitation: [BRT-26 note](thesis/prediction_notes/BRT-26.md). |
| **📊 **RETAINED — `COT-FUEL-35B` BAND + LADDER (frozen spec).** ⏱ **as-of `2026-09-08` vintage #5** · ✓ **reconciled `2026-09-14`** against canonical `workbook/REGISTRY.tsv` row COT-FUEL-35B. | **Base `122,904.5` (trailing-8wk median 2026-06-16…08-04; an 8-observation median = mean of `122,319` and `123,490`) · Leg-A SPENT ≤`109,164` · NO-VERDICT deadband `109,165–118,325` · NOT-SPENT ≥`118,326` · Leg-B OI-share ≤`4.909%` GATING · `median_unit 9,160` FROZEN · both legs must agree; NO-VERDICT is a real answer (base-case sizing).** ⚠️ **`113,745` is the deadband's CENTRE, never a boundary — THE DEADBAND IS DECISIVE INSIDE ITS RANGE.** **Ladder: `129,072` (7/7, RETIRED predecessor base) → `123,490` (7/21) → `101,016` (7/28) → `110,638`/5.8463% (8/11) → `108,059`/5.7206% (8/18) → `112,862` (8/25, JOINT NO-VERDICT) → `111,019`/`5.7790%` (9/1, OI `1,921,085`; Leg A inside deadband ⇒ NO-VERDICT, Leg B `5.7790%` > `4.909%` ⇒ NOT-SPENT ⇒ **JOINT NO-VERDICT, 3rd consecutive**) → **`107,229`/`5.5275%` (9/8 vintage #5, OI `1,939,911` **+18,826**; Leg A **SPENT** — 1,935 below the `109,164` bar, first SPENT since 7/28; Leg B `5.5275%` > `4.909%` ⇒ NOT-SPENT/GATING ⇒ **JOINT NO-VERDICT, 4th consecutive**, sizing stays BASE CASE).** 🔑 **The OI-share fall is OVER-DETERMINED: 78.5% genuine short covering, 21.5% denominator growth.** **Verified at the RAW CFTC primary (`f_disagg.txt`, `report_date` `260908`, code `067651`) — not Socrata, not the reader alone.** ⚑ **PROMOTED INTO THIS STANDING ROW 2026-09-14, deliberately: the #5 grade had been sitting only in a DATED block — the exact route by which BRT-26 went 8/28-vintage once before.** **Next vintage as-of 9/15, releases Fri 9/18 ~15:30 ET.** ⛔ **Re-basing = a NEW N1 build + a fresh Will ruling, never maintenance.** 📖 *(repair record: `archive/STATUS_DETAIL_2026-09.md` § repairs)* |
| **JWC / WAR-RISK BASELINE** · document as-of **2026-07-29** · ✓ **reconciled `2026-09-15`** | [IUA index and LMA body re-read](research/2026-09-15_backlog-review/STANDING_REVIEW.md): **JWLA-034 newest of ten indexed circulars**, both Gulf areas retained; Saudi Arabia listed as **amended**. Frozen BRT-30 baseline/October 26 endpoint unchanged. Listing is neither a current premium quote nor throughput evidence. |
| **⛔⛔ **RETAINED — ALL 17 CORRECTED-CLAIM SENTINELS FROM THE ROTATED ROWS (one line each; full narrative in the archive). These are historical correction reminders, not refreshed market claims; they stop a wrong claim re-entering by pattern-match — the compression target is the prose, never the constraint.** ✓ **reconciled `2026-09-15`** *(17 retained; historical figures are not reissued; source/correction scope in backlog review)* | **① Context notes are NOT trade proposals — `$0` moved.** · **② The 38%-of-war-days-at/below-bar caveat: longest run 2026-06-12→07-20, 25 trading days, went NEGATIVE to −3.27.** · **③ Source class upgraded — first PRIMARY-sourced BRT-26 grade, and the reason was a month-old error of mine.** · **④ Baker Hughes request failures are not publisher outages. Minimal headers recovered the September 11 workbook on September 15; old categorical header/WAF-cause assertions are withdrawn.** · **⑤ STANDING KILL-ON-SIGHT: a "Hormuz is open" headline on US authority is a claim about LEGAL/MILITARY status, never THROUGHPUT.** · **⑥ The 8/15 incident is NOT the same event — UKMTO used the identical phrase "unknown projectile" for both.** · **⑦ Boot-protocol gap: an autonomous routine ran 09:55 and boot never read it.** · **⑧ PortWatch required target observations remain missing; access recovered. Instrument coverage failure does not refute the premise.** · **⑨ Near-miss: `instrument_check` reported FRED-GASREGW DEAD on an SSL timeout — a source that HANGS is not a source that is DOWN.** · **⑩ The silent-UNFIRE hazard is REAL — a fired modifier can un-fire under REVERT semantics.** · **⑪ `BRT-26` keys on the OIL leg, NEVER the US total.** · **⑫ The archived EU-storage low/90%-out-of-reach forecast is DATED HISTORY, not a current measurement or deadline. Current decision dates/targets live in the docket.** · **⑬ A same-day RETRACTION by my own vintage ladder (P1) — original text preserved.** · **⑭ P2: 3.0M bpd of asserted OFFLINE capacity was WRONG, and it cuts against my own thesis.** · **⑮ The crowd found a zero-transit day my own throughput record missed by one day.** · **⑯ DEMOTED 8/17 — both claims in that cell are CANDIDATE DETECTION ARTEFACTS, not established physical events.** · **⑰ The peak landed at the PRICE LOW — 8/5 front futures $79.45, bottom of the ~15% selloff.** |
| **EXPORT-SIGN WARNING** · ✓ **reconciled `2026-09-15`** | **Refinery outages can free crude feedstock for export**, conditional on production, storage, domestic use and export-route availability. A terminal/pipeline loss has a different effect. Rising crude exports alone do not establish greater supply or a measured refinery-loss contribution. Old August Russia/Gulf figures are historical, not a current causal decomposition. [THESIS transmission table](thesis/THESIS.md) and [incident review](research/2026-09-15_backlog-review/INCIDENT_REVIEW.md). |
| **STANCE + GATE STATE** · ✓ **reconciled `2026-09-16`** | **THESIS v5.9 evidence refinement; v5.8 numerical calibration retained; WQ-192 stand-down unchanged.** Deploy gate v3 retired August 7; no registered re-arm. Surviving frame-breaker, Stage-A and off-ramp clauses remain governed by [TRADE](TRADE.md) and its complete specs; this row provides no capital authority. A deal is not measured throughput. [Reconciliation scope](research/2026-09-15_backlog-review/STANDING_REVIEW.md). |
| **➡️ EVERYTHING ELSE THAT USED TO BE RESTATED HERE NOW LIVES WITH ITS OWNER** ✓ **reconciled `2026-09-15`** *(owners checked; archived payload CRC reproduced)* | ⛔⛔ **NINE 'standing state' rows were rotated out 2026-08-21 → [`workbook/STATUS_archive_20260821_standing_blocks_aug4_aug13.md`](workbook/STATUS_archive_20260821_standing_blocks_aug4_aug13.md)** (9 rows, 9,970 UTF-8 payload bytes, `crc32 d82761d3`, VERBATIM). **THREE OF THEM HAD GONE FACTUALLY FALSE** while sitting under a CURRENT heading — *"NO OPEN ACTION"* (Will ruled SELL ONE 8/21, unexecuted), *"INBOX EMPTY 8/7"* (14 days stale), *"NOTHING OWED TO WILL"* (three `KILL-LEG2` decisions are with him now). ★ **The cause was DUPLICATION, not staleness — a second copy cannot be kept in sync and will always eventually contradict its owner.** ⇒ **CANONICAL OWNERS, read them instead: positions / action state / arm triggers / execution log → [`TRADE.md`](TRADE.md) · mail state → `board_log.tsv` · owed decisions + next-session items → [`SCRATCH.md`](SCRATCH.md) · thesis stance → [`thesis/THESIS.md`](thesis/THESIS.md) · every registered test → [`workbook/REGISTRY.tsv`](workbook/REGISTRY.tsv).** |

---

## 📦 DATED DETAIL — ROTATED 2026-09-07 (rule 19)

> **Blocks 9/07 ×2 · 9/06 · 9/02-09/01 rotated WHOLE, VERBATIM, on the day** → [`archive/STATUS_DETAIL_2026-09.md`](archive/STATUS_DETAIL_2026-09.md) (**50,350 B, crc32 `645c5ded`**; the read cap does not bind that cold file — rule 19 exemption). ⛔ **Nothing summarised away: the ANALYSIS moved, the standing VALUES stayed.**

> **STILL LIVE from them, so no obligation dies with the narrative:** 🔴 **FRAME-BREAKER carve-out ⛔ NOT MET on the M/T Kylo (9/7) — the deciding word is *UNLADEN*; head clause reads ZERO on four axes. LETTER IS CANONICAL IN [`setups/SPECS_GATES.md` BG-02](setups/SPECS_GATES.md), amended by Will 9/7 14:42 (WQ-189) to require confirmed loss of cargo or Gulf export/transit throughput — ⚠️ PROSPECTIVE-ONLY, it never re-grades 9/5.** · ✅ **`WQ-192` + `WQ-189` RULED AND CLOSED (Will, 9/7 14:42) — no deploy, no arm, `$0`. ⛔ Do not re-open.** · 🔴 **FALCON GATE 2 FIRED on its own letter and was not softened; my limb is met on its face — but the LETTER governs my pair and this surface is DESCRIPTIVE, carrying no capital trigger (WQ-192).** · ⚖️ **BRT-30 CHECKED NOT GRADED — resolves on a DATE (2026-10-26), baseline `JWLA-034`.** · 📋 **WQ-112 applied to BRT-26 (`58%` 7/28 → `85%` 9/6 window-shrink; the STANDING row above is canonical).** · 📅 **Russia diesel carve-out: Q1 `UNKNOWN-AT-PRIMARY`, reported NEGATIVE — transcriptions reached, official authentication/publication and original scope still missing.** ⚑ **DOCKET L198 → re-registered ACCESS-BLOCKED and L140 → retry re-keyed to a PUBLICATION event (PROME, 2026-09-14, on my read — PROME owns both rows).**
---

## 📚 ARCHIVE INDEX + OWNER POINTERS — *one line each; narrative lives at the link*

> 📦 **Rotation receipts (every crc32, 2026-08-04 → 2026-09-14) live in [archive/STATUS_DETAIL_2026-09.md](archive/STATUS_DETAIL_2026-09.md) § ROTATED 2026-09-14** — moved there 2026-09-14 because a receipt is PROVENANCE, not state. Older sets: [`workbook/STATUS_archive_*`](workbook/) (8/4 · 8/7 · 8/13 · 8/21 ×2 · 8/27 · 8/28) · [`archive/STATUS_dated_2026-09-09_audit.md`](archive/STATUS_dated_2026-09-09_audit.md) · [`archive/STATUS_dated_2026-09-09_maintenance.md`](archive/STATUS_dated_2026-09-09_maintenance.md). ⛔ **Every rotation was VERBATIM; tombstones and impeachment banners that still BIND live in STANDING STATE above.**

> ➡️ **OWNERS (read these, never a copy here):** thesis stance → [`thesis/THESIS.md`](thesis/THESIS.md) (v5.9) · positions / rules / execution log → [`TRADE.md`](TRADE.md) · predictions → [`thesis/PREDICTIONS.tsv`](thesis/PREDICTIONS.tsv) · registered tests → [`workbook/REGISTRY.tsv`](workbook/REGISTRY.tsv) · operational lines → `demand_destruction/TRACKER.md` · forward items → [`SCRATCH.md`](SCRATCH.md) § NEXT SESSION + `docket/CATALYSTS.tsv` · Saudi dual-route watch (7/21, never executed) → Yanbu/Bab rows in `docket/CATALYSTS.tsv` + `refinery_damage/INCIDENTS.tsv` · convergence matrix: 7/21 score is a point-in-time record, a new read is a fresh scoring pass.

---
## 📅 CATALYST CALENDAR (forward; canonical source `docket/CATALYSTS.tsv`)

> Generated view of `docket/CATALYSTS.tsv` (human twin, same event SET). `scripts/render_calendar.py --write`; boot's Derived Views check fails closed on drift. Unresolved rows with past dates stay until GRADED — an expired date is not completion.

<!-- CALENDAR:BEGIN generated from docket/CATALYSTS.tsv — do not hand-edit -->

| Date | Release | Priority |
|------|---------|----------|
| **~Mon Aug 17** ⌁*modeled* | CPC understanding — historical test UNRESOLVED; cargo/source coverage required | 🟠 |
| **Mon Aug 24** | Treasury Operation Economic Outcast — announcement observed; operative-mechanism review PARTIAL | 🔴 |
| **~Sun Aug 30** ⌁*modeled* | Jazan August 30 modeled restart — actual restart UNRESOLVED | 🟠 |
| **Tue Sep 1** | RUSSIA producer-direct carve-out — September 8 Q1 read UNKNOWN-AT-PRIMARY | 🔴 |
| **Fri Sep 4** | ✅ FRIDAY PAIR — FIRED 2026-09-04, BOTH LEGS GRADED 2026-09-06 (2d latency, desk dark Fri; no stack — graded before the 9/11 prints) | 🔴 |
| **Sun Sep 6** | ✅ OPEC+ MEETING — FIRED 2026-09-06. GRADED SAME DAY AT THE SECRETARIAT PRIMARY: OUTCOME (3) DEFERRED AGAIN | 🔴 |
| **~Tue Sep 8** ⌁*modeled* | L198 September 8 owner read — Sidi Kerir direction-only updated; PortWatch UNKNOWN / PENDING PUBLICATION | 🔴 |
| **Wed Sep 9** | ✅ XLE approved exit — FIRED AND GRADED: FILLED 2026-09-11 @ $1.51, line FLAT | 🔴 |
| **Wed Sep 9** | USO October 135C — CLOSED; October 9 time stop discharged | 🟡 |
| **Wed Sep 9** | EIA retail gasoline/diesel — READ: September 7 observation | 🟠 |
| **Wed Sep 9** | EIA September STEO — READ: same-series comparison completed | 🟠 |
| **Thu Sep 10** | SPR / Edouard — WPSR wk-9/4 READ 9/10: FIRST PRINT NO VERDICT (SPR −1.244M); Edouard narrow read RIGHT; resolver wk-9/11 (9/16) | 🔴 |
| **Fri Sep 11** | Friday pair — GRADED: September 11 rigs primary verified September 15; COT vintage #5 graded September 12 | 🔴 |
| **Wed Sep 16** | WPSR wk-9/11 — GRADED September16: L305 Branch A | 🔴 |
| **Thu Sep 17** | ✅ USO 150/165 spread — CLOSED EARLY 2026-09-10 ~15:1x by Will's hand, $630 proceeds (+$330); WQ-207 9/17 rail discharged unexecuted | 🟡 |
| **Thu Sep 17** | Petroline BG-02 — EARLIEST GRADEABLE DATE on the 7-day-MA floor (not an event; an arithmetic gate) | 🔴 |
| **~Fri Sep 18** ⌁*modeled* | ✅ YANBU EXPORT-STOCK DEPLETION WINDOW — the date routing would convert to BARRELS (modeled from Reuters 5-7 days off the 2026-09-11 shut) — GRADED 2026-09-18: loadings stopped DAY 1 (9/11… | 🔴 |
| **Fri Sep 18** | FRIDAY PAIR — rigs GRADED 2026-09-18 (452, +2, NOT BREACHED, headroom 5); COT vintage #6 (as-of 9/15) PENDING the ~15:30 ET print | 🔴 |
| **~Tue Sep 22** ⌁*modeled* | ATA truck tonnage AUGUST — first print fully carrying $6+ retail diesel | 🟡 |
| **Fri Sep 25** | Petroline frame-breaker resolver WINDOW CLOSES 17:00 ET — BG-02 instance (4) lapse date | 🔴 |
| **Wed Sep 30** | XLE September 30 expiry — residual check only after selected September 9 exit | 🟡 |
| **Thu Oct 1** | 🟠 EU STORAGE 80% FLOOR — DECISION DATE (binding 1 Oct-1 Dec window OPENS) | 🟠 |
| **Sun Oct 4** | 🟠 OPEC+ SEVEN-COUNTRY MONTHLY MEETING — the November 2026 production decision (successor to the 9/6 row) | 🟠 |
| **~Mon Oct 5** ⌁*modeled* | 🟠 ARAMCO NOVEMBER OSPs — first monthly price signal set entirely under the Petroline shut | 🟠 |
| **Tue Oct 6** | EIA October STEO — successor same-series vintage read | 🟠 |
| **~Sat Oct 10** ⌁*modeled* | 🟠 IRAN-OMAN PERMANENT-ROUTE WINDOW — 30-60d after 8/26 interim framework | 🟠 |
| **~Wed Oct 14** ⌁*modeled* | 🟠 IEA OMR OCTOBER — second collective-action watch + global stock draw (successor to the Sept OMR read 9/18) | 🟠 |
| **~Sun Nov 1** ⌁*modeled* | 🟠 EU GAS STORAGE — RESOLVED 2026-08-13: the target, the DATE and the pace are now all verified | 🟠 |
| **Sun Jan 31 2027** | RUSSIA FUEL EXPORT BAN — full expiry (gasoline all-participants + non-producer diesel) | 🟡 |

*`~` + ⌁*modeled* = `date_class=modeled` in the record: a PROJECTED date, not a published one — do not grade a row against a modeled date as though it were confirmed. 9 of 29 rows are modeled.*

*29 event(s), generated from `docket/CATALYSTS.tsv` — the canonical forward-state record. Full graded text lives there and is deliberately not restated. Regenerate with `scripts/render_calendar.py --write`; verify with `--check` at closeout.*

<!-- CALENDAR:END -->
**✅ FIRED & GRADED (full graded text retained in `docket/CATALYSTS.tsv`, not restated here):** Jul 22 EIA wk-7/17 · Jul 24 CPC leg-(b) · Jul 24 COT+Baker Hughes · Jul 28 OPEC JMMC · Jul 29 EIA wk-7/24 · Jul 29 FOMC · Jul 31 COT as-of 7/28 · Jul 31 Russia diesel-ban expiry · Aug 2 OPEC+ September quotas · Aug 3 the frozen behavioral settle test · Aug 5 EIA wk-7/31 · Aug 7 COT as-of 8/4.

---

## SUMMARY FOR WILL

[Cross-war reassessment](research/2026-09-16_cross-war-oil/REPORT.md): product/refiner evidence strengthens; net crude loss remains unquantified, with restart and Russian-export counterevidence. SPR test resolves Branch A, not proof of program end. WQ-213 reaffirmation and entry checks remain. Screenshot adds same-day USO165C; current broker status UNKNOWN, distinct from USO37 shares. TRADE owns position reconciliation.
