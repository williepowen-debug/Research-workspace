# PRODUCTION REVIEW #6 — READER R3 (global macro / oil / labor / vol)

**Reader:** DAEDALUS fan-out reader, read-only · **Written:** 2026-09-17 (Thu) · **Period graded:** 2026-09-01 00:00 → 2026-09-17
**Cohort:** SAM · ZHAO · HANS · BRENT · LABOR · VIOLET
**Method:** every figure below re-derived by command at HEAD (`read_cap_check`, `ledger_staleness`, `render_calendar --check`, `card_partition_check`, `test_hans.py`, `predictions_due.py`, `git log/show`, direct `sed`/`grep` reads). Where I did not open the deciding artifact I wrote NOT-ADJUDICATED or CANNOT-EVALUATE.

> ⚠️ **ONE FINDING BINDS THE WHOLE COHORT — read it before any per-desk verdict.**
> The **Market L5 leg "zero YEYOU flags" is a default-zero instrument that can never fire** (PAT-060; YEYOU retired 2026-09-05, WQ-181 ①). The 9/14 L285 sitting **proposed** re-pointing it to `N/A — no mechanical per-push review seat exists` (`runs/2026-09-14_L285_LADDER_INTEGRITY_PARTIAL.md:125-127`) but that record says in its own header *"NOTHING IN THIS RECORD MOVES A GRADE"*, and `AGENTS/DAEDALUS/CLAUDE.md` § MATURITY LADDER **still carries the YEYOU text unamended**. ⇒ **For every L5 grade and every L5 promotion in this cohort the YEYOU leg is NOT-ADJUDICATED, not MET.** I have not treated it as satisfied anywhere below, and no recommendation here turns on it.

---

## COHORT SUMMARY (detail follows)

| Desk | commits self/routed | dark-days | current | rec level/conf | row-claims T/R/CE | profile trigger | falsification | neg-res (cand/neg/lacking) | top finding (≤15 words) |
|---|---|---|---|---|---|---|---|---|---|
| **SAM** | 67 / 34 | 2 (last self 9/15 `121233a0c`) | L4 H | **HOLD L4 · Conf H** | 3 / 4 / 1 | **FIRED** (Sep-18 window advanced 9/11) | STALE-BUT-CONSISTENT (scanner flag WITHDRAWN) | 4 / 1 / 0 | SAM-28/31 resolve TOMORROW 9/18 with the desk dark and the RED rail 14d overdue |
| **ZHAO** | 14 / 22 | 0 (last self 9/17 `fa1bfefea`) | L4 H | **HOLD L4 · Conf H** (2nd clean cycle ADJUDICATED MET) | 2 / 3 / 1 | **FIRED** (post-TIC session ran 9/17) | RAIL-IN-LOCAL-FORM, evidenced fire path | 7 / 1 / 1 | Second clean cycle earned, but 15 dark days between them and 3 pulls owed |
| **HANS** | 11 / 18 | 7 (last self 9/10 `f2e092885`) | L4 H (tier-2) | **PROMOTE → L5 · Conf M** | 0 / 6 / 0 | FIRED-in-substance (ambiguous by construction) | not in scope (see §HANS-5) | 4 / 2 / 1 | Every named L5 cycle-2 leg MET and verified at the artifact incl. BRENT's tree |
| **BRENT** | 106 / 75 | 0 (last self 9/17 `9ecfd057b`) | **L5 M** | **HOLD L5 · Conf M** (H **not** earned) | 4 / 9 / 2 | **FIRED ×2** (TRADE split + rule-19 STATUS) | not in scope (see §BRENT-5) | 16 / 3 / 0 | P1/P5(a) verified DONE by command; "one clean cycle" and P5(b) still missing |
| **LABOR** | 68 / 36 | 0 (last self 9/17 `cbb2ca8b9`) | **L5 H** | **SUSTAIN L5 · Conf H** (leg 2 flagged) | 5 / 4 / 0 | **FIRED** (WQ-179(c) mode signature present) | RAIL-IN-LOCAL-FORM — **L3 grandfathered FAIL now CLEARED** | 6 / 0 / 0 | First real clean card PASS watched; write-mode fix applied to STATUS only |
| **VIOLET** | 73 / 45 | 0 (last self 9/17 `f8cb6d2ff`) | L4 H | **HOLD L4 · Conf H** | 4 / 4 / 1 | **FIRED** (9/16 letter grade landed 9/17) | not in scope (see §VIOLET-5) | 2 / 0 / 0 | Grade record is fleet-reference form; Conf H now rests on an expired profile clock |

*Dark-days = days since last SELF-authored commit. Counts computed from `git log --after="2026-09-01 00:00" -- AGENTS/<X>/`, self = subject begins with the desk name (with or without a `[tag]` prefix).*

---

# SAM — Market · FLEET_MAP L4 / Conf H / last_scored 2026-09-01

## 1. Period production
**67 self-authored / 34 routed-in · last self-commit 2026-09-15 `121233a0c` · 2 dark days.**
Shipped: 9/14–9/15 a four-commit reconcile arc (`0ce654ebb` stale macro/disclosure/calendar reconcile · `c73b40e43` BIS intra-quarter revisions · `b104af795` WALTER delivery filing · `299b798aa` startup-state refresh + expired daily-proxy retirement), then `17873d941` (Japan news + Sep-15 auction resolved) and `121233a0c` (handoff + historical completion stamp frozen). Earlier: the Sep-18 window work (SAM-28 magnitude bar cleared 9/11) and the SAM-33 op-record audit at the BOJ primary.

## 2. Row-claim test

| # | Claim in `Gaps` / `Next_upgrade` | Verdict | Locator |
|---|---|---|---|
| (a) | "owner-doc bidirectional sweep NOT demonstrated" | **TRUE-STILL** | `AGENTS/SAM/RECONCILIATION.md` last written **2026-06-16** (`40c839d17`); grep for `bidirection\|derived→owner\|reverse` = **0 hits**. `CLAUDE.md:256` still describes it as "SAM's owner→derived surface order". |
| (b) | "readerless gates 1-of-3 — SAM-41 built+boot-wired, SAM-33 adjudicated in prose only" | **REFUTED in part — now 2-of-3** | `STATUS.md:122`: SAM-33's Sep-9 ops **audited AT THE RECORD** — `ope20260909.xlsx` vs `mpr260831a.pdf`, all three buckets scheduled-date/scheduled-size ⇒ falsifier un-fired, with the next check dated (Sep-16 25Y+, then Sep-30 17:00 JST) and keyed to `KB-SAM-238`. That is an instrument, not prose. The **third** gate is not named in the row ⇒ **CANNOT-EVALUATE** on the remaining leg. |
| (c) | "`CLAUDE.md:87` 'Don't invest in inbox/outbox hygiene' licence still standing" | **TRUE-STILL** (line number moved) | Verbatim at **`AGENTS/SAM/CLAUDE.md:86`**, not :87. |
| (d) | "red/ refreshed 8/27 DONE" | **TRUE-STILL as a fact, now superseded** | `git log -1 -- AGENTS/SAM/red/` = `daba336d5` **2026-08-27**. But `red/CHALLENGES.md:7` dates the next adjudicator for **CH-009 and CH-012 at 9/3** — **14 days overdue**, and SAM is contractually forbidden to edit `red/` (needs a RED spawn). |
| (e) | "Byte-creep TRUE: STATUS 79,059 B / 247 ln (243% of read budget)" | **REFUTED** | `read_cap_check --agent SAM` → **STATUS.md 21,720 B = 67% of budget**, `wc -lc` = **131 lines**. Rotation executed. |
| (f) | "Dark since 8/27" | **REFUTED** | Sessions ran 9/4, 9/11, 9/14, 9/15. |
| (g) | "GPIF_FLOWS 30 STATUS-writes behind = owner-confirm" | **REFUTED** | `ledger_staleness --nudge SAM` → *"STATUS not moving this session — no gap being created"*; GPIF_FLOWS not listed behind. |
| (h) | Next_upgrade: "+ a STATUS byte tier (rotate to <32,550 B)" | **REFUTED — DONE** | 21,720 B, see (e). |

**Score: 3 TRUE-STILL / 4 REFUTED / 1 CANNOT-EVALUATE.** Four of eight cells are wrong at HEAD; the row's own `last_scored` is **2026-09-01**, 16 days stale.

## 3. Ladder walk (Market, current L4 → next L5)

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L3 | convergence matrix | **MET** | `STATUS.md` conviction/channel state + `thesis/THESIS.md` pillar audit (profile §1 "EXCEEDS") |
| L3 | exit rules | **MET** | `CLAUDE.md:207-222` durable no-live-values rules + `STATUS.md:258-272` banded live read (profile §3 "two-surface split exactly implemented") |
| L3 | predictions resolving | **MET** | `thesis/PREDICTIONS.tsv` 34 rows, 16 CONFIRMED / 14 FAILED / 1 special / 3 OPEN (`STATUS.md:9`) |
| L3 | dated falsification surface | **MET** | `red/COUNTER_THESIS.md:3-4` two-clock header; `red/CHALLENGES.md:6` rail state 3 OPEN / 12 CLOSED |
| L4 | TRADE.md feeding proposals | **MET** | `TRADE.md` FLAT banner + retained entry card; May-21 entry / 6-22 trim were Will-approved |
| L4 | signals flowing | **MET** | `NEXUS_BRIEF.md` refreshed at closeout; WALTER deliveries filed `b104af795` |
| **L5** | clean closeouts | **MET** | 9/14 and 9/15 closeouts each produced a `reports/<date>_closeout.md` + handoff (`121233a0c` touched `LAST_COMPLETION.md`, `reports/2026-09-15_closeout.md`) |
| **L5** | zero YEYOU flags | **NOT-ADJUDICATED** | default-zero instrument, see cohort banner. `YEY-P05` never covered SAM. |
| **L5** | current | **NOT MET** | **SAM-28 and SAM-31 both resolve at the 2026-09-18 close (`STATUS.md:92`) — tomorrow — and the desk has been dark since 9/15.** The Sep-16 25Y+ BOJ operation date, which `STATUS.md:90` and `:122` name as SAM-33's next check, **passed yesterday unchecked.** Plus `red/` CH-009/CH-012 adjudicators 14d overdue. |

**Recommendation: HOLD L4 · Conf H.** Confidence H — I ran `read_cap_check`, `ledger_staleness`, and read `CLAUDE.md:86`, `RECONCILIATION.md`, `red/CHALLENGES.md` and `STATUS.md` directly. The desk has cleared two of the four L5 blockers my row names (byte tier outright, gate (b) substantially) but (a) and (c) are untouched and the "current" leg is failing **right now**, one day before its two headline predictions resolve.

## 4. Profile trigger
Profile: `profiles/SAM.md`, **Built 2026-07-10**, Δ-banner relocated 2026-08-17.
Quoted trigger: *"**Staleness:** refresh when the Sep-18 LOCKED window advances a stage or FXY modal band re-derived or >45d"*.
**Verdict: FIRED.** `STATUS.md:120` — *"🔴 9/11: the MAGNITUDE bar is now CLEARED — FXY 57.20 [9/1 close] → 59.77 [9/11 14:0x UTC] = +4.49%. The ROUTE leg is NOT."* One of SAM-28's two legs cleared = the window advanced a stage. The FLEET_MAP cell's *"Profile NOT FIRED (Sep-18 window)"* was written 9/1 and was **overtaken on 9/11**.
**Profile statements now false:** profile header says *"STATUS 300→248 ln"* — actual **131 ln / 21,720 B**; *"PREDICTIONS 14 CONFIRMED/14 FAILED/1 special/5 OPEN"* — actual **16/14/1/3** (`STATUS.md:9`); *"red/ 48d stale"* — refreshed 8/27, now 21d.

## 5. Falsification read — `red/COUNTER_THESIS.md` (scanner: STALE-FLAGGED, "8/17 vs 9/15; cites v1.6, live v1.7")

I opened the file. Applying the two-vintage rule: this is a **STATE surface**, so it is dated by its header's **labelled** freshness claim.

- `:3` — **`Last real data refresh: 2026-06-30`**, followed in the same line by *"(the argument below is unchanged from that date — **it is the record of a counter-case, not a live dashboard**)"*.
- `:4` — **`Last RED sweep: 2026-08-17`** with *"**bannered, deliberately NOT rewritten** — dispositions live in `CHALLENGES.md`"*.
- `:6-7` — a STATUS BANNER that **states the exact version gap the scanner flagged**: *"This document argues against **THESIS v1.6.1**. **SAM retired that frame on 2026-08-07 (v1.7)** … The counter-thesis is **kept verbatim** because the argument is the record and rewriting it would corrupt what RED actually claimed on 6/30. **Cite it as history.**"* — then a six-row table giving each argument's standing as of 8/17, with two marked WON, two MOOT/HELD, two LIVE and re-pointed to `CHALLENGES.md` CH-009/CH-012.

**Verdict: WITHDRAWN.** The scanner read the **body's** version cite and reported drift; the header **declares** that drift, dates it, and routes the live half elsewhere. Rule broken: PAT-077's two-vintage rule — a STATE surface is dated by its header's labelled freshness claim, and this header carries two of them plus an explicit "cite as history" disposition. A deliberately-frozen record with a live re-pointer is the *correct* form, and flagging it teaches desks to rewrite arguments they should preserve.
**Severity: LOW on the file — but the scan hid a real one.** The live obligation is at `:18`: *"A counter-thesis against the v1.8 candidate is **owed** and is a separate spawn; the pre-registration is `CHALLENGES.md` **CH-017**."* CH-017 is OPEN and resolves 10/31 with SAM-41 (`CHALLENGES.md:7`), and the **CH-009/CH-012 adjudicators dated 9/3 are 14 days overdue** on a rail SAM cannot edit.

## 6. Negative-resolution leg — opened `thesis/PREDICTIONS.tsv` (34 data rows, header at line 40)

| row | negative? | names a SEARCH INSTRUMENT | dated search-attempt precondition |
|---|---|---|---|
| **SAM-33** | ✅ *"the BOJ does **NOT** deploy emergency/unscheduled long-end capping ops … through Dec 31 2026"* | ✅ **YES** — Notes: *"Reads: BOJ ops announcements, FSR, Jul-31 FY2027 purchase plan"*; graded at `ope20260909.xlsx` vs `mpr260831a.pdf` | ✅ **YES** — `STATUS.md:122` *"Sep-9 ops audited AT THE RECORD … falsifier un-fired through Sep-9. **Next check: the Sep-16 25Y+ date** (KB-SAM-238); then Sep-30 17:00 JST"*. ⚠️ **The Sep-16 attempt is 1 day overdue.** |
| SAM-28 | ✗ positive-firing (a route fires) | — | — |
| SAM-31 | ✗ positive-firing (channel re-couples) | — | — |
| SAM-39 | resolved 9/4 | — | — |

**Counts: 4 OPEN candidates opened / 1 confirmed negative-class / 0 lacking instrument.** SAM-33 is the fleet's best-formed negative row I read in this cohort: it names the falsifier, names three *exclusions* (disorderly-spike response, scheduled taper-plan change), carries an activation stamp lifting its own VOID clause, and names the next dated search.

## 7. As-made receipt — **n/a** (MARCO/REGINALD/HENRY only).

## 8. Cross-agent threads / pattern candidates
- **→ PROME (or a RED spawn):** `AGENTS/SAM/red/CHALLENGES.md:7` dates CH-009 and CH-012 adjudicator #2 at **9/3**; both are 14 days overdue and SAM is fenced from editing `red/`. A dated obligation on a surface its owner cannot write is structurally un-self-healing.
- **PATTERNS candidate (dedup vs PAT-077 first):** *A deliberately-frozen record that DECLARES its own version gap in its header will be flagged by a drift scanner that reads the body.* Evidence: `AGENTS/SAM/red/COUNTER_THESIS.md:3-7` vs the 9/17 falsification scan. The fix is a scanner exclusion keyed on the labelled header claim, not a rewrite of the record.

## 9. Reviewer-side defects (mine)
- **Four of eight SAM row cells are REFUTED at HEAD** (byte-creep, dark-since-8/27, GPIF_FLOWS, and the byte-tier next_upgrade), and the row still reads `Last_scored 2026-09-01`. The 243%-of-budget figure in particular is the kind of number other desks quote.
- The `Gaps` cell asserts *"readerless gates 1-of-3"* but **never names the three gates** — so the remaining leg cannot be tested by anyone but its author. A count without an enumeration is not a checkable claim.
- The cell says `CLAUDE.md:87`; it is `:86`. A stale line number still resolves to *a* line — `[[finding_instrument_reports_clean_against_the_wrong_reference]]`.

---

# ZHAO — Market · FLEET_MAP L4 / Conf H / last_scored 2026-09-05

## 1. Period production
**14 self-authored / 22 routed-in · last self-commit 2026-09-17 `fa1bfefea` · 0 dark days.**
Two clusters and nothing between them: **9/2** (8 commits: `d757fb63b` 39-item inbox drain both lanes, Aug PMI graded on the construction sub-index, ZHA-16/17 pre-registered then ZHA-16 amended **before** the event, read-cap split 47,477→32,269 B; then six self-correction commits `20faaedc9`/`083fbc4f5`/`3ea643b6d`/`9202ba11c`/`1760582bd`/`d70148c63`/`b27f1cc86`) and **9/17** (6 commits: `4f6ab7e38` WQ-206 L0 drain 18 items + `board_log.tsv` created, `d531fa414` read-cap rotation #2 + Vector 8 3→4, `79c3614bf` July TIC graded, `c6ac32e81` CLAUDE.md re-keyed off LAST_COMPLETION, `b51a2d3c3`+`fa1bfefea` NEXUS_BRIEF folds). **15 days dark in between.**

## 2. Row-claim test

| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | "🟡 F-2 STATUS regrew to the rotation ceiling in THREE DAYS (32,534 B = 99.95%)" | **TRUE-STILL as history; REFUTED as current** | `read_cap_check --agent ZHAO` → **STATUS.md 23,588 B = 72% of budget**. Rotation #2 executed 9/17 → `archive/STATUS_COLD_20260917.md` (tracked, `git ls-files` confirms). |
| 2 | Next_upgrade: "a SECOND consecutive clean cycle (9/2 was the first)" | **REFUTED — the cycle ran and is clean** | See §3 adjudication below. |
| 3 | Next_upgrade: "a STATUS byte-tier rotation **into the existing `archive/STATUS_COLD_20260902.md`**" | **REFUTED in substance, deviated in form** | Rotation done, but into a **new** file `archive/STATUS_COLD_20260917.md`, not the existing one. Substance (verbatim, nothing deleted, bytes in the commit bodies — `STATUS.md:8`) is met; my row over-specified the destination. |
| 4 | Next_upgrade: "Close the spawn-or-reclassify question to PROME as YES-ACTIVE at the next session" | **TRUE-STILL (not done)** | `grep -rn "spawn-or-reclassify\|YES-ACTIVE\|reclassif"` over `AGENTS/ZHAO/STATUS.md` and `PROME/inbox/` → **0 hits**. |
| 5 | "Belgium proxy FALSIFIED, rho=+0.050 (n=41)" | **TRUE-STILL, and re-measured** | `STATUS.md:40` — **rho = +0.067 (n=42)**, 24m +0.017, LT +0.054, re-run 9/17; *"Belgium buys in 15 of 28 China-selling months (54%)"*. The proxy stayed falsified across a fresh month of data. |
| 6 | "inbox now 4 (all 9/2–9/4)" | **CANNOT-EVALUATE as stated** | 18 further items consumed 9/17 (`4f6ab7e38`); I did not count the live inbox. |
| 7 | "⚠️ THE 'archive/scoreboard' L4 LEG IS STRUCK" | **TRUE-STILL** | Correctly struck; no L4 leg outside the ladder is applied below. |

**Score: 2 TRUE-STILL / 3 REFUTED / 1 CANNOT-EVALUATE** (+1 self-correction upheld).

## 3. Ladder walk + the adjudication the task asked for

**ADJUDICATION — "a SECOND consecutive clean cycle": MET.** The 2026-09-17 session is a genuine cycle and it is clean on evidence I read:
- **A real grade against a pre-declared boundary rule, including an unfavourable one.** `STATUS.md:4` and `:118` — July TIC (released 9/16, own pull 9/17): China $618.0B (−$15.4B), LT/coupon net **−$7.7B** ⇒ **ZHA-17 resolves NO on its own boundary rule** (`−$10B ≥ LT > −$5B ⇒ NO`), read *"continued but decelerating."* The desk graded NO on a row it would rather have graded YES, on the boundary it wrote in advance.
- **The signature asset re-tested, not assumed.** rho re-run to n=42 (`:40`), still falsified; rotation refuted again (Agency −$36.1B TTM); *"Official sector as a whole BOUGHT coupons (+$25.5B) while private sold (−$29.1B) — June's split reversed"* — a stated reversal of its own prior read.
- **Housekeeping closed:** 18 inbox items consumed, `board_log.tsv` created, `COR-20260908-01` receipted, CLAUDE.md re-keyed off `LAST_COMPLETION` per PROME's word, read-cap rotation #2.
⇒ **Two consecutive clean cycles, 9/2 and 9/17.** I am satisfied on the leg as written.

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L3 | convergence matrix | **MET** | `STATUS.md:4` **29/60** (+1, Vector 8 → 4 on the gas leg, BRENT 9/6) |
| L3 | exit rules | **MET** | `STATUS.md:114` § Thesis Kill (Belgium <10% YoY ×2 AND China >$700B ×3) + `:116-122` § Falsification tripwires |
| L3 | predictions resolving | **MET** | `workbook/PREDICTIONS.tsv` 17 rows w/ `Resolve_By` + `Anchor_Type` + `Invalidation`; ZHA-11/12/17 all resolved 9/17 |
| L3 | dated falsification surface | **MET** | see §5 |
| L4 | TRADE feeding proposals | **WAIVED-by-design** | `TRADE.md` FROZEN with an explicit unfreeze condition; research/signal desk, no position by design (profile §1) |
| L4 | output consumed by others | **MET ×2 at the recipients' own artifacts** | LIQUID stripped every Belgium inference; `AGENTS/HANS/STATUS.md:174` carries a whole *"## ZHAO ANSWER — Belgium proxy: NOT CARRIED"* section |
| **L5** | clean closeouts | **MET** (n=2) | 9/2 and 9/17, adjudicated above |
| **L5** | zero YEYOU flags | **NOT-ADJUDICATED** | cohort banner |
| **L5** | current | **NOT MET** | **15 dark days between the two "consecutive" cycles**, and three dated pulls owed at HEAD: `STATUS.md` CALENDAR — *"⚠️ ~Sep 8 **RatingDog (ex-Caixin) Aug mfg PMI — OWED PULL, now 9 days late**"*, *"GACC reconcile + SAFE Aug reserves/gold STILL OWED"*. `ledger_staleness --nudge ZHAO` → FLOW.tsv 5 STATUS-writes behind. |

**Recommendation: HOLD L4 · Conf H.** Confidence H. The named next_upgrade legs are now MET (second clean cycle + byte rotation), so the **row should be re-cut** — but promotion to L5 is not available today on two independent grounds: the "current" leg fails on 15 dark days plus three overdue pulls, and the "zero YEYOU flags" leg cannot be adjudicated until the L285 re-point is ratified. **The correct disposition is: re-cut the Gaps/Next_upgrade cells to the post-9/17 state, and put L5 back on a named dated leg** (suggest: the **10/16 August TIC** letter registered in `reports/` **before** the print, which `STATUS.md:141` already commits to, with no dark gap beyond 21 days).

## 4. Profile trigger
Profile: `profiles/ZHAO.md`, body 2026-07-04, **refreshed 2026-09-05**.
Quoted: *"**Staleness:** refresh at the next post-TIC session or >45d → checkpoint **2026-10-20**"*.
**Verdict: FIRED.** The post-TIC session ran **2026-09-17** (`79c3614bf`, July TIC graded). The profile is due for refresh now, 33 days before its calendar checkpoint.
**Profile statements now false:** §2 State table — *"Last session 2026-09-02"* (now 9/17); *"STATUS 219 ln / 32,534 B = 99.95% … 🟡 rotate-tier"* (now 23,588 B / 72%); *"Inbox 4"* (18 more consumed 9/17); *"Falsification: STATUS §Thesis Kill (:132) + §Falsification tripwires (:136)"* — **both line numbers moved to `:114` and `:116`** after rotation #2. §3 *"convergence matrix scored 28/60"* — now **29/60**.

## 5. Falsification read — market desk with no thesis-class file the scanner can see

**Verdict: RAIL-IN-LOCAL-FORM.** It lives inside STATUS, in two adjacent named sections:
- `AGENTS/ZHAO/STATUS.md:114` — **`### Thesis Kill`** → `COLD_20260917 §⑨-b` (Belgium <10% YoY ×2 AND China >$700B ×3 · fiscal >5% GDP with LGFV backstop — *"neither close"*).
- `AGENTS/ZHAO/STATUS.md:116-122` — **`### Falsification tripwires now`**, six rules, each with a named instrument and a live state.

**EVIDENCED fire path — yes, twice:**
1. `:120` — *"✅ **Korea KRW <1,450 sustained: FIRED 2026-08-12**, graded 8/21 → **falsifies the Korea-as-UST-anchor leg**"*, with two caveats explicitly marked *unverified, not resolved* rather than waved through.
2. `:40` + `:119` — the **Belgium (Euroclear) custody proxy**, the desk's signature analytical asset, marked **PROXY STILL FALSIFIED** on a re-measurement (rho +0.067, n=42, bar rho < −0.5, VX-ZHAO-1.09/KB-151), with the reinstatement condition written as a number: *"reinstate the custody-migration reading **only if** rho(China, Belgium net sales) < −0.5 on a rolling 24m window. Until then the Belgium level is **not** evidence in either direction."*
3. Plus a **forward** dated rule added 9/2: *"if September construction PMI (~9/30) rebounds above 47.5, the two record lows were weather and the vector-5 upgrade reverses. A third consecutive sub-47 print with the same weather attribution retires the weather explanation entirely."*

**Two-vintage check:** STATE surface, header `**Updated:** 2026-09-17`, and every tripwire carries its own in-content stamp (8/12, 8/21, 9/2, 9/17). No mtime dependence. **Clean.**

## 6. Negative-resolution leg — opened `workbook/PREDICTIONS.tsv` (17 rows, 12-col schema with `Resolve_By`/`Anchor_Type`/`Invalidation`)

7 OPEN rows. Six (ZHA-01 CNY>7.30 · ZHA-05 NPL>12% · ZHA-06 >250 banks · ZHA-07 forced UST sales · ZHA-10 petro-yuan >$5B · and ZHA-16's branch A) resolve on a **positive** threshold or event. One is negative-class:

| row | negative? | names a SEARCH INSTRUMENT | dated search-attempt precondition |
|---|---|---|---|
| **ZHA-16** (branch **B/D**) | ✅ branch **B** = *"summit held, **no** official output"*; branch **D** = *"no summit"* — both resolve on an absence | **PARTIAL** — `STATUS.md` §ZHA-16 names the *bar* precisely (*"branch-A bar = **a published instrument with an effective date beyond 2026-11-10**; graded on the DOCUMENT"*) but names **no search venue** (no Federal Register / USTR / MOFCOM / State Council named) | ❌ **NO** — `Resolve_By 2026-09-30`, "graded within 6 days" of the 9/24 summit, but no dated *attempt* clause. `Anchor_Type` = `confirmed-event-US-announced-PRC-unconfirmed` — honest about the event, silent about the search. |

**Counts: 7 candidates opened / 1 confirmed negative-class / 1 lacking a named search instrument.**
⚠️ **This one matters and it is dated 7 days out.** ZHA-16's branch B is the **escalation-by-default** branch (`STATUS.md` §ZHA-16 AMENDMENT 1: *"absent a further affirmative act the heightened rate returns automatically"*, confidence raised 35%→45%), and `STATUS.md:118`-adjacent records the truce clause verbatim — *"shall continue to be suspended until 12:01 a.m. EST on November 10, 2026"* — with **"resumed rate NOT specified — not filled in."** So the desk will be grading "no published instrument exists" on 2026-09-30 **without having named where it looked.** Per `FORGE/PREDICTION_DISCIPLINE.md` § Grading, a negative resolution needs a named search instrument and a dated search-attempt precondition; ZHA-16 has neither. **One line added to the row before 9/24 fixes it.**

## 7. As-made receipt — **n/a**.

## 8. Cross-agent threads / pattern candidates
- **→ ZHAO (packet, not an edit), before 9/24:** name the search venue(s) for ZHA-16's branch-B/D negative and add a dated search-attempt clause. See §6.
- **→ PROME:** the spawn-or-reclassify question my row asked ZHAO to close is still open after the session that was supposed to close it; the answer is now evidentially **YES-ACTIVE** (two real sessions, 9/2 and 9/17) but nobody has recorded it.
- **PATTERNS candidate:** *A next_upgrade that over-specifies the DESTINATION of a fix records a deviation when the desk does the right thing.* Evidence: my row required rotation *"into the existing `archive/STATUS_COLD_20260902.md`"*; ZHAO rotated verbatim into a new dated cold file, which is the better form. Specify the property (verbatim, contiguous, crc, under budget), not the filename.

## 9. Reviewer-side defects (mine)
- 🔴 **The ZHAO `Gaps` cell is ~4 KB of narrative in a column my own charter declares CURRENT-STATE-only.** `AGENTS/DAEDALUS/CLAUDE.md` § MEMORY MODEL, standing rule: *"a Gaps/Next_upgrade cell states what is TRUE NOW; how it came to be true goes to HISTORY, in the same edit."* The ZHAO cell instead carries the promotion story, the F-1/F-2/F-3 write-ups, a DNT amendment and a self-retraction. **This is the exact rot the 8/23 `Gaps` rotation was supposed to end, reappearing in the very next row written after it.** The rule was declared and then broken by its author in the same column — `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`.
- The cell's own **F-1** admits the prior row was re-cut 9/1, one day before the session that invalidated it. **The same shape has now recurred**: the row was cut 9/5 and ZHAO ran 9/17. A 12-day-old row on a desk that sessions in bursts is structurally always one burst behind.

---

# HANS — Market (ROSTER:tier2) · FLEET_MAP L4 / Conf H / last_scored 2026-09-05

## 1. Period production
**11 self-authored / 18 routed-in · last self-commit 2026-09-10 `f2e092885` · 7 dark days** (tier-2, spawn-as-needed — darkness is not a fault here).
Two sessions. **9/5** (5 commits): `d78252b0f` 8-day catch-up (HICP pre-reg appendix, ECB FSR at primary, BoE 9/17 QT registered) · `ad19fc575` domain news sweep — *"3 of my own PMI numbers were stale flashes; Q2 GDP refutes me"* · `6cf86ae82` built `doc_audit.py`, 8 real defects on first run · `ad7025dc5` Codex residuals · `bff148d59` *"Qatar date was stale on 4 of my OWN surfaces after I corrected HAWK"*. **9/10** (6 commits): `e19df9d55` **ECB 9/10 graded at primary — HNS-05 HIT, §3b TACTICAL 3-1, §3c no falsifier fired** · `1e2a24f93` UK gilt near-triggers corroborated, T-13/T-06 re-graded · `6bd187447` consumed DAEDALUS WQ-112 ruling · `9732eeac7` ML-HANS-448 to n=3 · `b2e53cf73` re-scoped doc_audit C4 · `f2e092885` superseded a weak-branch remedy in its own fired log.

## 2. Row-claim test — **every one of the six findings in my row is now REFUTED (cleared)**

| # | Claim | Verdict | Locator (verified at the artifact by me, not relayed) |
|---|---|---|---|
| F-1 🔴 | "ECB §3a conditional prior update NEVER APPLIED" | **REFUTED — discharged** | `e19df9d55` graded HNS-05 at primary; `workbook/PREDICTIONS.tsv` HNS-05 conf `88% [2026-09-05] (was 75% [2026-08-28])` — the §3a update is *in the ledger cell*, dated. |
| F-2 🔴 | "registry count wrong in 4 places — actual 14 rows / 6 SCANNABLE-DAILY" | **REFUTED — cleared, and I recounted from the TSV** | `awk` over `registry/THRESHOLDS.tsv` = **14 data rows**; `grep -c SCANNABLE-DAILY` = **6**. All four surfaces now agree: `STATUS.md:151` "14 rows, 6 daily-scannable, 1 UNINSTRUMENTED" · `CLAUDE.md:145` "14 rows — 6 daily-scannable" · `CLAUDE.md:211` · `registry/README.md:12,17`. The safety rule is re-cut to the right denominators: *"A clean scan of the 6 does not clear the 14."* |
| F-3 🔴 | "HNS-09 OPEN in PREDICTIONS.tsv and absent from STATUS entirely (grep=0)" | **REFUTED** | `grep -c "HNS-09" AGENTS/HANS/STATUS.md` = **1**. |
| F-4 🟠 | "BRENT — a named action owner — has zero (`find AGENTS/BRENT -iname *HANS* = 0`)" | **REFUTED — closed AT BRENT'S TREE** | `AGENTS/BRENT/inbox/**processed**/2026-09-05_from-HANS_eu-gas-fires-the-half-you-never-received-ttf-125pct-yoy-storage-lowest-since-2011.md` — **not merely delivered: consumed.** This is the leg my 9/5 row flagged as *"NOT RE-VERIFIED AT THE ARTIFACT BY ME — relayed from PROME"*. **I have now verified it.** |
| F-5 🟠 | "CLAUDE:196 says 27 offline tests; STATUS:221 and the suite say 36" | **REFUTED — and the number moved again** | I **ran** `scripts/test_hans.py` → **`Ran 51 tests in 4.021s` / `OK`**. `CLAUDE.md:210` says **"51 offline tests, no network/keys"**. Both agree at 51. |
| F-6 🟡 | "8d dark, 6 unread WALTER SIGs" | **REFUTED** | 9/5 catch-up + 9/10 session; `8774b359b` *"WALTER -> HANS: COR-20260908-04 receipt — both schema deviations fixed, nothing owed"*. |

**Score: 0 TRUE-STILL / 6 REFUTED / 0 CANNOT-EVALUATE.** This is the cleanest row-clearance in the cohort.

## 3. Ladder walk (Market, current L4 → next L5)

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L3 | convergence matrix | **MET** | `registry/THRESHOLDS.tsv` 14 rows with per-row scannable CLASS + `value_basis` + `recipient_chain`; `workbook/VX.tsv` 40 live / 27 frozen, each with a NAMED upgrade source |
| L3 | exit rules | **MET** | `thesis/KILL_TREE.md` — instrument-per-claim form |
| L3 | predictions resolving | **MET** | `workbook/PREDICTIONS.tsv` 9 rows, 11-col schema w/ `Resolve_By` + `Anchor_Type`; HNS-05 resolved HIT 9/10 at primary |
| L3 | dated falsification surface | **MET** | `thesis/ECB_2026-09-10_PREREGISTRATION.md` (SAM-form pre-registration, awkward part first, §5 pre-commits to grading §3b **beside** the binary) + `registry/HANS_T_FIRED_LOG.tsv` |
| L4 | TRADE feeding proposals | **WAIVED-by-class** | input/research desk; BOND is the time-critical backup (profile §1) |
| L4 | signals flowing | **MET** | HAWK + BRENT legs both verified at the recipients' trees; WALTER COR-20260908-04 receipted |
| **L5** | **cycle-2-clean (my row's named gate)** | **MET — all six sub-legs** | HNS-05 graded ✅ (`e19df9d55`) · §3b tactical-vs-regime graded ✅ (3-1) · §3c falsifier checked ✅ (no fire) · F-1 appendix filed ✅ · registry re-cut to 14/6 ✅ · HNS-09 in STATUS ✅ · **BRENT dispatch closed at BRENT's tree ✅** |
| **L5** | clean closeouts | **MET** | Both 9/5 and 9/10 closed with self-corrections shipped rather than carried (`bff148d59`, `f2e092885`) |
| **L5** | zero YEYOU flags | **NOT-ADJUDICATED** | cohort banner |
| **L5** | current | **PARTIAL** | Tier-2 darkness is not a defect, but `read_cap_check --agent HANS` → **STATUS.md 31,686 B = 97% of budget, 🟡 rotate-tier** (rule-5 stop is <70%: **8,902 B more to remove**). `ledger_staleness --nudge HANS` clean. |

**Recommendation: PROMOTE L4 → L5 · Conf M.** Confidence **M, not H, and deliberately so.** Every leg my own row named as the gate is MET and I verified each at the artifact myself — including the two I previously relayed from PROME without checking. But I withhold **H** on two grounds I can state precisely: (i) the **"zero YEYOU flags" leg is NOT-ADJUDICATED** for structural reasons that have nothing to do with HANS, and a promotion that skips a ladder leg silently is the defect the Meta-L5 note warns against — so the promotion should be recorded as **"L5 with the YEYOU leg N/A pending the L285 re-point"**, enumerated, not omitted; (ii) STATUS at 97% of budget is a live rotate-tier breach on the desk's single boot-read surface. **Condition the Conf M→H on one post-rotation session** (<70% of budget) **after the 9/17 BoE QT print HANS itself registered.**

## 4. Profile trigger
Profile: `profiles/HANS.md`, **body 2026-09-05** (whole rewrite).
Quoted: *"**Staleness:** refresh at the **next post-9/10 session** (HNS-05 graded) or **>45d** → checkpoint **2026-10-20**"*.
**Verdict: FIRED-in-substance / ambiguous by construction.** The event the clock waits for (HNS-05 graded) **happened on 9/10 itself**, in the session that grades it — so "the next post-9/10 session" and "the session that grades HNS-05" are the same session under one reading and different under the other. No session has run after 9/10. **This is a trigger that cannot be evaluated without knowing which its author meant** — a reviewer-side defect, logged in §9.
**Profile statements now false:** header *"`STATUS.md` (238 ln / 30,883 B)"* — now **31,686 B**; *"`scripts/test_hans.py` → `Ran 36 tests … OK`"* — now **51**. The profile's own ⚠️ block warns that a stale clock let the map say "L3, parked" while the desk did L4 work; the same clock is now ambiguous rather than long.

## 5. Falsification read — **not in scope.** HANS is on none of the three step-5 lists (not scanner-flagged, not in the no-thesis-file list, not in the AEOLUS/MIDAS/OSPREY set). Noted in passing since I read it anyway: `thesis/KILL_TREE.md` + `ECB_2026-09-10_PREREGISTRATION.md` are both live and dated, and `scripts/pmi_ism_lead_test` **fails its own gate on purpose** so a retracted finding stays refuted in code — the strongest single falsification-hygiene artifact I read in this cohort.

## 6. Negative-resolution leg — opened `workbook/PREDICTIONS.tsv` (9 rows)

4 OPEN. Two are negative-class:

| row | negative? | names a SEARCH INSTRUMENT | dated search-attempt precondition |
|---|---|---|---|
| **HNS-08** | ✅ *"German 10Y Bund does **NOT** close at or above 4.00% at any point before Dec 31 2026"* | ✅ **YES** — *"Resolver: German 10Y benchmark daily close, TradingEconomics / Bundesbank. Any single close ≥4.00% = MISS."* | ✅ **YES, in anchor-type form** — `Anchor_Type` = *"FIXED-DATE … **CONTINUOUS-MONITORING anchor: this resolves MISS the instant the level prints, not on the date; 12/31 is the HIT date only**"*. The continuous-monitoring declaration **is** the dated-attempt discipline: it forbids a 12/31 lookback from standing in for the daily check. Best-formed of the two. |
| **HNS-09** | ✅ *"…the sector shows NII/earnings still holding with **NO material rise** in cost-of-risk"* | ❌ **NO named resolver** — the Notes cell records the row's provenance (registered at LIQUID's suggestion) and its direction rule (*"HIT = asymmetry still in its benign phase; MISS = the credit leg has begun to turn"*) but **names no aggregate, no publisher and no "material" threshold** | **PARTIAL** — `Anchor_Type` = *"EXPECTED-RELEASE-WINDOW — a reporting SEASON, not a single date. Grade on the aggreg[ate]…"*, `Resolve_By 2026-11-30`. The window is dated; the instrument inside it is not. |
| HNS-06 | ✗ positive (PMI ≥50.0) | ✅ HCOB/S&P flash, slip absorbed to 9/25 | ✅ *"Grade on the first flash print after 9/20"* |
| HNS-07 | ✗ positive (storage ≥80%) | ✅ GIE AGSI+ EU aggregate, gas day 11/01, D+1 | ✅ *"grade on 11/02 using the 11/01 gas day"* |

**Counts: 4 candidates opened / 2 confirmed negative-class / 1 lacking a named instrument (HNS-09).**
⚠️ HNS-09 is the desk's **only** registered instrument on the EU bank / private-credit channel **Will ruled to full depth** (profile §1, verbatim *"I do want HANS to handle the EU bank / private-credit scope depth"*). A negative resolution on an unnamed aggregate with an undefined "material" is not gradeable by a third party. This was F-3's *surfacing* problem; the *gradeability* problem underneath it is still open.

## 7. As-made receipt — **n/a**.

## 8. Cross-agent threads / pattern candidates
- **→ HANS (packet):** give HNS-09 a named aggregate + publisher + a numeric bar for "material rise in cost-of-risk" before the Q3 season opens (~late Oct). It is the only registered instrument on a Will-ruled lane.
- **→ HANS (packet):** STATUS at 97% of budget; rule-5 stop is <70% (8,902 B).
- **PATTERNS candidate:** *A prediction row can be MADE VISIBLE without being made GRADEABLE — surfacing and specification are independent defects, and fixing the first closes the flag that would have caught the second.* Evidence: HNS-09 was F-3 (absent from STATUS, grep=0 → now present, grep=1, flag cleared) while its resolver cell has been blank since 2026-08-28. Adjacent to `[[finding_required_field_satisfied_by_a_pointer_passes_every_presence_audit]]`; dedup against it before minting.

## 9. Reviewer-side defects (mine)
- 🔴 **My HANS row's 9/5 update carried a self-declared unverified relay — *"⚠️ NOT RE-VERIFIED AT THE ARTIFACT BY ME — relayed from PROME; confirm at HANS's tree at the next touch"* — and the relay was for F-1/F-2/F-3/F-5 ALL CLEARED and the F-4 BRENT delivery.** The flag was correctly written and the confirmation waited **12 days** for this review. All five relayed claims check out, but a row that grades a desk on borrowed evidence is a row that could have been wrong for 12 days without anyone knowing. `[[finding_asymmetric_rigor_counterparty_claims]]` — relaying is asserting.
- 🟠 **The profile's staleness trigger is un-evaluable** (§4): *"refresh at the next post-9/10 session (HNS-05 graded)"* names an event and a session that may be the same thing. Re-write it as a content test (e.g. *"when `workbook/PREDICTIONS.tsv` shows HNS-05 at a terminal Status"* — which is checkable and already true).
- 🟠 The row's F-5 pinned the test count at **36**; it is **51**. A count in a `Gaps` cell is a claim with a short half-life on a desk that ships regression tests every session.

---

# BRENT — Market · FLEET_MAP **L5 / Conf M** / last_scored 2026-09-07 — **THIS IS THE 9/1 "CONFIRM AT PR#6" CONFIRMATION**

## 1. Period production
**106 self-authored / 75 routed-in · last self-commit 2026-09-17 `9ecfd057b` · 0 dark days.** Highest-volume desk in the cohort by a factor of ~1.7.
Shipped: the **9/7 architecture-review response** (rule-19 STATUS restructure, `render_calendar.py` built/wired/path-fixed, RULINGS relocations) · 9/10 position work (`a326ec7a9` USO 150/165 Sep-18 spread CLOSED by Will, +$330; `64bbc5879` new-oil-position review, NO both sides, triggers pre-registered) · 9/11 Petroline frame-breaker **graded NOT MET** (`1ff472552`) + a self-retraction (`d12b4613c` *"Boundary #8 session-1 RETRACTED"*) · 9/12 `635631fde` COT-35B #5 JOINT NO-VERDICT + BG-02 re-graded NOT MET + a resolver defect self-found · 9/15 backlog review + CATO repair · 9/16–17 the cross-war oil reassessment, crashed and recovered (`9ecfd057b`).

## 2. Row-claim test — walked with locators, as the task requires

| # | Claim in `Gaps` | Verdict | Locator (every figure re-derived by command at HEAD) |
|---|---|---|---|
| 1 | "STATUS 74,061 B = 137% of cap (rotation stopped at 17 sentinels inside a dated table)" | **REFUTED — P1 DONE** | `read_cap_check --agent BRENT` → **STATUS.md 21,220 B = 65% of budget** (✅, not even rotate-tier). `STATUS.md:105`-adjacent `## 📌 STANDING STATE` block exists and declares itself: *"⚑ **CREATED 2026-09-07 — first application site of READ_CAP rule 19**"*; the 17 sentinels are extracted as standing rows with `⏱ as-of` / `✓ reconciled` stamps; 9/14 dated analysis rotated verbatim to `archive/STATUS_dated_2026-09-14.md`, **8757 B, crc32 `45833649`**. |
| 2 | "TRADE 181,108 B = 334% (frame-breaker @56,103, LIVE entry gate @108,998, EXECUTION LOG @175,218); rotation blocked since 8/21" | **REFUTED — P2 DONE** | `stat` → **TRADE.md 25,027 B**. A **7.2× reduction.** `read_cap_check` → 77% of budget, 🟡 rotate-tier (2,243 B short of the rule-5 <70% stop) — so it is *finished as a split*, *unfinished as a rotation*. |
| 3 | "LESSONS 90%" | **REFUTED** | **13,931 B = 43% of budget.** |
| 4 | "CLAUDE.md 118% of budget, 9 contradictions (NETWORK table diverged from `_NETWORK.md`)" | **REFUTED in part** | **30,933 B = 95% of budget** (was 38,591). The NETWORK divergence is fixed and *recorded with its reason*: `RULINGS.md:313` § R-2026-09-09-maintenance — *"the table listed 8 routes and OMITTED BOTH FALCON AND OSPREY, while this desk packeted FALCON TWICE on 2026-09-07 … ⇒ **The desk was running live on two routes its own charter did not know about**"*. I did not recount the 9 contradictions ⇒ **CANNOT-EVALUATE** on the count. |
| 5 | "RULINGS.md dead since 8/07 (PAT-150)" | **REFUTED** | `git log -1 -- AGENTS/BRENT/RULINGS.md` → **`028d4e793` 2026-09-15**. Newest sections `R-2026-09-08`, `R-2026-09-08-OSPREY`, `R-2026-09-09-maintenance`, `R-2026-09-09-routine-host` (`:303`, `:308`, `:313`, `:326`). The dead sink now takes writes. |
| 6 | "catalyst twins diverged (9/18 position expiry absent from STATUS)" | **REFUTED — replaced by a generator, the superior form** | I **ran** `python3 scripts/render_calendar.py --check` from `AGENTS/BRENT/`: **`✅ CALENDAR: STATUS block matches docket/CATALYSTS.tsv (25 events)`, rc=0.** The twin is retired in favour of one record + a rendered view, exactly as the 9/7 Codex-4 amendment prescribed (*"prefer a GENERATED view over a maintained twin … a twin-diff leg is the MIGRATION instrument only"*). |
| 7 | "STATUS:119 v5.7 over THESIS v5.8 since 9/2 = **4th recurrence of the L5 leg**" | **REFUTED — pointers AGREE at HEAD** | `STATUS.md:49` (STANDING STATE, `✓ reconciled 2026-09-16`): *"**THESIS v5.9** evidence refinement; v5.8 numerical calibration retained"*. `thesis/THESIS.md:1`: *"# BRENT THESIS — **v5.9**"*, `:3` *"Version: 5.9, September 16 evidence refinement."* `STATUS.md:65` now routes the question instead of answering it: *"➡️ **OWNERS (read these, never a copy here):** thesis stance → `thesis/THESIS.md` (v5.9)"*. **The structural fix is the re-pointing, not the re-typing.** |
| 8 | "SUMMARY FOR WILL a rotation stub since 8/27" | **REFUTED** | `STATUS.md:111-113` is a real, dated, four-sentence summary naming the cross-war reassessment, the SPR Branch-A resolution, WQ-213 and the USO165C broker-status UNKNOWN. |
| 9 | "INCIDENTS 16 ACTIVE median 153 d, guards advisory-overridden" | **CANNOT-EVALUATE** | `9ecfd057b`/`63b4ff703` report all twelve aged incidents reviewed in the 9/15 backlog pass; I did not recount `refinery_damage/INCIDENTS.tsv`. `ledger_staleness --nudge BRENT` shows INCIDENTS.tsv **2 STATUS-writes behind**. |
| 10 | "10 own packets unread at recipients UNVERIFIED (fleet-side)" | **TRUE-STILL (still unverified)** | I did not sweep 10 recipient trees. |
| 11 | Next_upgrade "**P1** rule-19 STATUS restructure (<32,550 B; :119 → v5.8; real SUMMARY FOR WILL)" | **REFUTED — all three sub-legs MET** | rows 1, 7, 8 above. (:119 went to **v5.9**, past the target.) |
| 12 | Next_upgrade "**P5** twin-diff **/ version-sweep** legs" | **SPLIT: twin-diff MET (superseded); version-sweep NOT MET** | Generator landed, wired at boot, `--check` fail-closed (`scripts/render_calendar.py:22-23` *"A generator nobody verifies is a hand-edited file with extra steps"*) and **falsified on a real case** (`scripts/boot.py:178-182`: *"I falsified the CHECK (injected drift → rc=1, restored → rc=0) and never re-ran BOOT after wiring it … `[[finding_guard_correctness_and_wiring_are_independent]]`"*). **But `grep -rn -i version AGENTS/BRENT/scripts/*.py AGENTS/BRENT/CLAUDE.md` finds no version-sweep check** — the F9 leg exists today only as *substantive agreement*, not as a mechanism. |
| 13 | Next_upgrade "then **ONE clean cycle** → Conf H" | **NOT MET** | §3 below. |
| 14 | "DEMOTE TRIGGER (dated): any derived-pointer disagreement at the cycle closing the 9/11 Friday pair → L4 at PR#6 9/15" | **AMBIGUOUS — fires under one reading, not the other** | §3 below. **This is the most important finding on this desk.** |

**Score: 4 TRUE-STILL-or-unmet / 9 REFUTED / 2 CANNOT-EVALUATE.**

## 3. Ladder walk — every Market L5 leg, with locators

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L0 | dir + CLAUDE.md | **MET** | 30,933 B |
| L1 | STATUS + BOTTOM LINE | **MET** | `STATUS.md:111` § SUMMARY FOR WILL (the 9/7 "FAIL(pointer)" is cleared — row 8) |
| L2 | structured record, valid schema, accruing | **MET** | `workbook/REGISTRY.tsv` · `thesis/PREDICTIONS.tsv` 30 rows · `refinery_damage/INCIDENTS.tsv` · `demand_destruction/TRACKER.md` |
| L3 | convergence matrix | **PASS-local-form** (unchanged from 9/7) | `STATUS.md:65` — *"convergence matrix: 7/21 score is a point-in-time record, a new read is a fresh scoring pass"*; ARCHIVED 8/13, declared as such rather than rotting |
| L3 | exit rules | **MET** | `TRADE.md` STAGE-A LIVE ENTRY GATE + OFF-RAMP PLAYBOOK (ARMED-PASSIVE) + frame-breaker carve-out; deploy gate v3 retired 8/7 **with no registered re-arm**, stated at `STATUS.md:49` |
| L3 | predictions resolving | **MET** | `predictions_due.py` → **`✅ no OPEN predictions past (or within 7d of) their timeframe`**. Real grades in-period: BG-02 NOT MET (`635631fde`), Petroline frame-breaker NOT MET (`1ff472552`), COT-35B #5 JOINT NO-VERDICT, BRT-26 owner-graded at the 9/11 Baker Hughes primary (450, 457 not breached). |
| L3 | dated falsification surface | **MET** | `thesis/PREDICTIONS.tsv` BRT-26 / BRT-30 both carry dated instrument-named kill conditions; `TRADE.md` frame-breaker clause graded live 9/11 |
| L4 | TRADE.md feeding proposals | **MET** | Will closed the USO 150/165 Sep-18 spread 9/10 at +$330 (`a326ec7a9`); WQ-207 discharged |
| L4 | signals flowing | **MET** | 75 routed-in commits from HAWK / OSPREY / FALCON / WALTER / PROME / TERRY / SAM / HENRY in 17 days |
| **L5** | **clean closeouts** | ❌ **NOT MET** | **Two independent misses in the confirmation window.** (i) **9/15:** an outside desk found a live surface contradicting BRENT's own log — `28b5dfebd` *"PROME -> BRENT: your RULINGS entry states a disposition your own board_log refutes"*, found by OSPREY at its L308 discharge: `RULINGS.md:310` still read *"The packet remains in inbox pending … no acknowledgement, objection or external send issued"* while `board_log.tsv:315` (2026-09-10T12:06:59) recorded *"No objection lodged to the channel downgrade path by the 9/15 window"* **and the packet was already in `inbox/processed/`**. PROME's own classification: *"the decision went in the log, the rulings entry kept describing the pre-decision state, **and each file's own check passes clean**."* ✅ **BRENT fixed it the same day** — `RULINGS.md:310` now reads *"September 15 record repair: the September 9 pending disposition was superseded by consumption on September 10 … This repairs the decision pointer."* (ii) **9/16: the session crashed before closeout**; the closeout was performed **on 9/17 by a PROME-spawned recovery session**, not by BRENT (`STATUS.md` Recovery note: *"the 9/16 session crashed before closeout; this block and the linked files were re-read against HEAD and committed unchanged in substance by a PROME-spawned recovery session"*). A closeout completed by someone else is not this desk's clean cycle. |
| **L5** | zero YEYOU flags | **NOT-ADJUDICATED** | cohort banner |
| **L5** | current | **MET** | `STATUS.md` two-clock header *"Last real data refresh: 2026-09-16 — scoped"*; post-FOMC named check 08:38 ET 9/17 (BZX26 $101.62 −3.98%, CLX26 $94.85, Nov−Jan +$6.55) **with the roll artifact called out**: *"⚠️ continuous `BZ=F` has rolled onto the Last-Day-Financial contract and its −7.3% print is an artifact."* |

### The demote trigger — **adjudicated, and it does not survive contact**

My row states it as: *"**any derived-pointer disagreement** at the cycle closing the 9/11 Friday pair → L4 at PR#6 9/15."*
The desk's own guard states it as: *"the dated demote trigger (record §4) names **'twin calendar event set'** disagreement at the cycle closing the 9/11 Friday pair → L4 at PR#6"* — `AGENTS/BRENT/scripts/render_calendar.py:17-18`, repeated at `scripts/boot.py:171-172`.

| reading | fires? | evidence |
|---|---|---|
| **Broad** ("any derived-pointer disagreement") — FLEET_MAP text | ✅ **FIRES** | `RULINGS.md:310` vs `board_log.tsv:315` was false on 9/10–9/15, i.e. **through** the 9/11 cycle. It is a derived-pointer disagreement by any definition. |
| **Narrow** ("twin calendar event set") — the guard BRENT built against | ❌ **DOES NOT FIRE** | `render_calendar.py --check` rc=0, 25 events matched, and it was falsified both ways before shipping. |

⇒ **I do not execute a demote on this.** Three reasons, in order of weight: (i) **the trigger was restated in a second surface with a narrower scope, and the desk built its mechanism against the restatement it was given** — penalising a desk for satisfying the version of a rule that reached it is the wrong direction; (ii) the broad-reading disagreement was **found and repaired inside the window**, by the routing rail doing exactly its job (OSPREY → PROME → BRENT, verified at BRENT's artifacts before routing, nothing edited); (iii) the trigger names **"PR#6 9/15"** and PR#6 is running **9/17** — the trigger's own resolution date has slipped, which is PAT-115's failure mode (*a rule anchored to a slippable event*) **in the file where PAT-115 was born**. A demote executed on a slipped date, under the broader of two live readings, against a defect the desk repaired within the cycle, would be `[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]` in reverse.

**Recommendation: HOLD L5 · Conf M — the 9/1 "confirm at PR#6" is CONFIRMED, and Conf M→H is NOT earned (3rd cycle).** Confidence **H** in this recommendation: I ran `read_cap_check`, `render_calendar --check`, `predictions_due.py` and `ledger_staleness` myself, and read `STATUS.md`, `TRADE.md` bytes, `RULINGS.md:303-330`, `THESIS.md:1-20`, `boot.py:155-185` and `render_calendar.py:1-30` directly.

**What L5 rests on, stated plainly so the next reviewer does not have to re-derive it:** the one root defect my 9/7 review named — *write mode interleaves standing state with dated narrative* — is **fixed at the mechanism level, not patched**. STATUS 137%→65%, TRADE 334%→77%, LESSONS 90%→43%, CLAUDE 118%→95%, the dead RULINGS sink taking writes again, the hand-maintained twin replaced by a fail-closed generator that was falsified **and** whose wiring bug was caught and documented by its own author. That is a desk that took an architecture review and executed it.
**What blocks Conf H:** P5's version-sweep leg is still absent as a *mechanism* (row 12), and the desk has now failed "one clean cycle" a **third** time — 9/7 (derived-pointer), 9/15 (RULINGS vs board_log, found externally), 9/16 (crash, closed out by PROME). ⚠️ **Note the pattern change**: the first two were self-detectable defects; the third was an infrastructure crash. A Conf gate that a crash can fail is measuring the box, not the desk.

**Proposed replacement for the expired trigger** (my row's is spent): *Conf M→H at the first BRENT-authored closeout after 2026-09-18 in which (a) `render_calendar.py --check` rc=0, (b) a version-sweep check exists and runs in `boot.py`, and (c) no outside desk files a live-surface contradiction against BRENT within that cycle.* All three are mechanically checkable and none is anchored to a slippable review date.

## 4. Profile trigger
Profile: `profiles/BRENT.md`, **FULL REFRESH 2026-09-07**.
Quoted: *"**Staleness / refresh clock:** **45 d → 2026-10-22**, or earlier on: THESIS major version (currently **v5.8**, 9/2) · `TRADE.md` split executed (P2) · rule-19 restructure of STATUS (P1) · a Conf/level change at PR#6 (9/15)."*
**Verdict: FIRED — on two legs independently.** (i) **TRADE.md split executed**: 181,108 → 25,027 B. (ii) **rule-19 restructure of STATUS executed**: 74,061 → 21,220 B with the `## 📌 STANDING STATE` block created and self-labelled as rule 19's first application site. (The THESIS leg says *major* version; 5.8 → **5.9** is minor, so that leg does **not** fire — but the profile's parenthetical *"currently v5.8, 9/2"* is now false.)
**Profile statements now false (§2 byte table, every load-bearing cell):** `STATUS.md` *"74,061 B = 137% of cap"* → 21,220 · `TRADE.md` *"181,108 B = 334%"* → 25,027 · `CLAUDE.md` *"38,591 B = 118%"* → 30,933 · `LESSONS.md` *"48,705 B = 90%"* → 13,931 · `NEXUS_BRIEF.md` *"44,502 B"* → 24,438 · `thesis/THESIS.md` *"73,838 B"* → 16,422 · `thesis/PREDICTIONS.tsv` *"111,603 B"* → 65,341 · `RULINGS.md` *"28,637 B; **dead sink**"* → 51,814 B and live · `STATUS.md:119 says v5.7, stale` → `:49` says v5.9, current · *"SUMMARY FOR WILL = a rotation stub since 8/27"* → a real summary. **The profile is 10 days old and its entire anatomy table is obsolete** — because the desk executed the review the profile was written to justify. That is a good failure, but it is a failure: **the profile must be refreshed before any section-task reads it**, and §2 explicitly says *"bytes are the load-bearing column"*.

## 5. Falsification read — **not in scope** (BRENT is on none of the three step-5 lists).

## 6. Negative-resolution leg — opened `thesis/PREDICTIONS.tsv` (30 rows, header at line 13)

16 OPEN/unresolved-status rows. Three are negative-class:

| row | negative? | names a SEARCH INSTRUMENT | dated search-attempt precondition |
|---|---|---|---|
| **BRT-26** | ✅ *"US oil rig count does **NOT** reach +50 from the 407 trough (i.e. stays **below 457**) before … end-Q3 2026"* | ✅ **YES** — Baker Hughes, named | ✅ **YES, and executed** — Notes: *"**September 15 owner grade at September 11 Baker Hughes primary**: US Oil **450 (+1)**; 457 NOT BREACHED; OPEN and confidence unchanged. **Two retrievals, ONE measurement lineage.**"* Evidence trail split out to `thesis/prediction_notes/BRT-26.md`. Also carries a WQ-112-compliant as-made re-mark (`60% [Date_Made]` → `58% [re-marked 2026-07-28 … evidenced as written 7/28 by commit 09d0ea03e]`). **This is the reference form for a negative row.** |
| **BRT-30** | ✅ *"the 8/26 Iran-Oman INTERIM framework does **NOT** produce a PHYSICAL corridor re-rating inside its own 30-60d permanent-route window"* | ✅ **YES** — *"OPERATIONAL FORM: on **2026-10-26** the **JWC (LMA/IUA)** still lists BOTH the Persian/Arabian Gulf AND the Gulf of Oman as Listed Areas"*. A third-party listing, not a judgement. | ✅ **YES** — single fixed grade date 2026-10-26; pre-registered 2026-08-28, **before** the window opens ~9/25 |
| **BRT-20** | ✅ resolved `NOT-FIRED-PRECONDITION` 4/25 | ✅ — closed | — (closed; cited as the desk's precedent for structurally-non-firing conditionals) |
| BRT-07 / BRT-12 / BRT-27 / BRT-28 / BRT-29 | ✗ conditional/positive-firing | — | — |

**Counts: 16 candidates opened / 3 confirmed negative-class (2 live) / 0 lacking an instrument.** Best negative-row discipline in the cohort, and `predictions_due.py` returns zero overdue.

## 7. As-made receipt — **n/a**.

## 8. Cross-agent threads / pattern candidates
- **→ PROME:** the BRENT demote trigger's resolution date (*"PR#6 9/15"*) slipped to 9/17 and the trigger existed in **two scopes** across two surfaces. If PROME registers DAEDALUS demote triggers anywhere in DOCKET/GATES, it should carry the FLEET_MAP wording verbatim or the desk's guard will be built against the paraphrase.
- **→ BRENT (packet):** `TRADE.md` is at 77% of budget — rule-5's stop is <70% (2,243 B). And `ledger_staleness --nudge BRENT` → **LESSONS_INDEX.tsv 6 · INCIDENTS.tsv 2 · REGISTRY.tsv 2 STATUS-writes behind** — freeze-or-refresh each.
- **🔴 PATTERNS candidate (strong, and I would mint this one):** ***A grade-bearing rule restated in a second surface can narrow its own scope, and the desk builds its guard against the restatement.*** Evidence: FLEET_MAP BRENT `Gaps` says *"any derived-pointer disagreement"*; `AGENTS/BRENT/scripts/render_calendar.py:17` and `scripts/boot.py:171` say *"twin calendar event set"* disagreement — same trigger, same date, **narrower perimeter**, and the desk's mechanism (correctly, diligently, falsified both ways) covers only the narrow one. Neither party is at fault and the grade turns on it. Dedup against `[[finding_frozen_spec_and_the_surfaces_describing_it_drift_apart]]` (promoted 9/7) — this is its **grade-bearing** special case: the letter cannot drift, but the surface the *graded party* reads is the one that governs what they build.
- **PATTERNS candidate (secondary):** *A "one clean cycle" Conf gate can be failed by an infrastructure crash.* Evidence: BRENT's 9/16 session crashed pre-closeout and was closed out by a PROME recovery spawn. Conf gates should name desk-attributable failure classes, or a box crash silently caps a desk's confidence.

## 9. Reviewer-side defects (mine)
- 🔴 **The demote trigger I wrote was defective in three independent ways at once**: ambiguous scope (§3), anchored to a slippable review date that then slipped (PAT-115's own failure mode, **in the file where PAT-115 was born**), and it named no failure *class* so a box crash and a stale pointer score identically. `[[finding_an_exit_legs_justification_expires_unwatched]]`.
- 🟠 **The `Gaps` cell mixes two denominators in one sentence**: *"STATUS 74,061 B = **137% of cap**"* and *"CLAUDE.md **118% of budget**"*. `BLUEPRINTS/READ_CAP.md` and `read_cap_check`'s own banner make **budget** the graded number (*"ALL % BELOW ARE OF BUDGET — the number every verdict grades"*). 74,061 B is **227% of budget**. A reader comparing 137% to 118% concludes the two files are near each other; they were 227% and 118%. `[[finding_distance_to_a_threshold_is_a_claim_about_its_basis]]`.
- 🟠 The row asserts *"10 own packets unread at recipients UNVERIFIED (fleet-side)"* — an unverified count with no owner and no date, carried since 9/7. Either verify it or drop it; an UNVERIFIED count in a current-state cell is a dated carry item with no expiry check.

---

# LABOR — Market · FLEET_MAP **L5 / Conf H** / last_scored 2026-09-07 — **L5 SUSTAIN CHECK**

## 1. Period production
**68 self-authored / 36 routed-in · last self-commit 2026-09-17 `cbb2ca8b9` · 0 dark days.**
Shipped: 9/4 NFP grade arc (T-03 MISS recorded against its own book, LAB-18/19 registered as a pair) · 9/7 the WQ-193 charter split (`CHARTER_DETAIL.md` created) + the DAEDALUS parity assessment and its same-day re-read · 9/10 the WQ-214 vintage sweep installed as a **charter control** · 9/10 + **9/17** claims grading cards frozen · 9/17 L302 delivery + NEXUS_BRIEF re-pinned to STATUS HEAD `5b3fc6705`.

## 2. Row-claim test

| # | Claim | Verdict | Locator |
|---|---|---|---|
| F1 | "brief REORDERED but 88,772 B" | **TRUE-STILL (worse)** | `NEXUS_BRIEF.md` **94,318 B** (+5,546 B since 9/7). |
| F2 | "CLAUDE.md 55,019 B now OVER the 54,250 B cap, Will-gated (WQ-193)" | **REFUTED — under the cap, still far over budget** | **53,061 B** = 98% of the 54,250 B cap, **163% of the 32,550 B budget**. `CHARTER_DETAIL.md:3` created 2026-09-07 under WQ-193 (Will verbatim *"Approve WQ-193 with your recs"*, 16:35 ET). |
| F3 | "checker BUILT (v3.1) but **red on all 6 real cards**, 2 of them FALSE … **no real clean case yet**" | ✅ **REFUTED — I watched a real card PASS** | I ran `card_partition_check.py` over all 10 cards in `docket/graded/`. **`GRADING_CARD_20260903_ISM_SERVICES.md` → rc=0**, *"[✓] table 2: VERIFIED — axis 'Band (Svs employment, Aug)', 3 bands, precision 1, bounds as written"*. The two FALSE reds are gone: v3 reports **per-table** dispositions and no longer emits a card-level certification one good table could earn. |
| F4 | "CLOSED (Kill rail re-derived 2026-09-04; run 63/31/21/162)" | **TRUE-STILL — and hardened further** | `STATUS.md` § EXIT RULES header carries **`Kill rail re-derived: 2026-09-04` [BLS USDL-26-1435]** *and* **`🔧 VINTAGE SWEEP (C1, unconditional per WQ-214): run 2026-09-10 18:0x ET — 4/4 rails CURRENT on the 9/10 vintage, no repair owed.`** |
| F9 | "8 cells in WQ-112 form with `[<=date]` bounds (canon question)" | **CANNOT-EVALUATE** | I did not recount the re-mark cells. |
| — | "STATUS 98.7% / LESSONS 98.3% / BUILD_DEBT +16 KB in one day — byte accretion on every surface" | **TRUE-STILL — unmoved in 10 days** | `read_cap_check --agent LABOR` → **LESSONS.md 32,285 B = 99%** 🟡 · **STATUS.md 32,177 B = 99%** 🟡. `BUILD_DEBT.md` **77,356 B**. `STATUS_DETAIL.md` **165,468 B** (correctly not a boot read). |
| — | "0 overdue predictions; 5/5 frozen cards with pre-print git receipts" | **TRUE-STILL — now 7 cards** | `docket/graded/` gained `GRADING_CARD_20260910_claims.md` and `GRADING_CARD_20260917_claims.md`. |
| — | "As-made audit: Brier 0.299→0.342, 0-for-5 at ≥60% (self-found)" | **TRUE-STILL, and propagated** | `CLAUDE.md:51` carries it inline in the pre-write checklist with the 9/7 WQ-193(c) correction noted (*"the as-made audit moved LAB-05 into the ≥60% bucket"*). |
| — | L3 leg "EXIT RULES has no kill-rail stamp — **FAIL-grandfathered**" | ✅ **REFUTED — the grandfathered FAIL is CLEARED** | The `Kill rail re-derived: 2026-09-04` stamp is **on the section header**, in-content, greppable. `falsification_scan` can now see it. |

**Score: 5 TRUE-STILL / 4 REFUTED / 0 CANNOT-EVALUATE** (+1 genuinely uncountable).

## 3. Ladder walk — **L5 SUSTAIN legs, pre-registered in the FLEET_MAP cell, walked one by one**

| Sustain leg (verbatim from `Next_upgrade`) | Verdict | Locator |
|---|---|---|
| **(1a)** *"`card_partition_check` parses `= X exactly`"* | ✅ **MET** | `scripts/card_partition_check.py:99-100` — *"a single-point band: `'= 50.0 exactly'`, `'50.0 exactly'`, `'== 4.2'`"* with the regex `(?:^\|\s)={1,2}\s*(NUM)\|(NUM)\s+exactly\b`; self-test at `:299` cites *"the ISM card's `= 50.0 exactly` row"* by name. |
| **(1b)** *"+ trigger-ladder declaration"* | ✅ **MET** | `:238-243` — `decl.get("kind") == "trigger-ladder"` → returns **`NOT-A-BAND-TABLE`**, *"declared kind=trigger-ladder — table TYPE only; trigger logic NOT verified by this tool"*. Self-test `:752-753`: *"declared trigger ladder must NOT be judged as a partition"*. The tool declares what it does **not** verify — PAT-074 in its correct form. |
| **(1c)** *"+ one REAL card PASS watched"* | ✅ **MET — I watched it** | `GRADING_CARD_20260903_ISM_SERVICES.md` → **rc=0**, one table VERIFIED. First real clean case. |
| **(2)** *"WQ-179 (c) applied to the desk's write mode (STATUS/LESSONS/BUILD_DEBT/brief), **not one file**"* | ❌ **NOT MET — applied to one file** | The mode **is** live on STATUS: `STATUS.md:3` *"🔒 Prior lede (9/1 JOLTS) + the 7/6 half-retraction pointer → `STATUS_DETAIL.md` § `status-line-rotated-20260917`"*, `:5` the hot/cold banner, `:10` § CORE TENSION rotated verbatim — **39 `STATUS_DETAIL` pointer rows**, and `CLAUDE.md:22/42/77/154/281` encode it as protocol. **But it is on STATUS only**: LESSONS **32,285 B = 99%**, BUILD_DEBT **77,356 B**, NEXUS_BRIEF **94,318 B (+5.5 KB since 9/7)**, and **STATUS itself is back to 99%** — the split bought two days on 9/2 and the desk is at the ceiling again on 9/17. The leg's own words are *"not one file."* |
| **(3)** *"charter hot/cold = WQ-193 (Will)"* | ✅ **MET, with a residual** | `CHARTER_DETAIL.md:3` created 2026-09-07 under WQ-193 with a census at the split (*"line/byte/crc before and after; obligation census: every active duty located after the split"*). `CLAUDE.md` 55,019 → **53,061 B**, under the cap. Residual: 163% of the read **budget**, so the cap-vs-budget gap is doing the work. |
| **(4)** *"Conf H holds while the profile clock holds (→ 2026-10-07)"* | ✅ **MET on the calendar, but the clock's OWN earlier-of legs fired** | §4. |

| Level | Standing ladder leg | Verdict | Locator |
|---|---|---|---|
| L3 | convergence matrix | **MET** | **29/75**, unchanged since 8/28 (`STATUS.md:2,35,125-127`) |
| L3 | exit rules | **MET** | § EXIT RULES: Kill A 0-of-3 on the 9/4 vintage (`63/31/21/162`), Kill B 0-of-5, FREEZE-THAW v2 `LEG A AND (B OR C)` with **every leg graded** 9/4 — LEG A short 86K after the L-02 recompute (bar recomputed **before** reading August, *"as the card ordered"*), LEG B short 0.1pp, LEG C JOLTS NET −18K/−5K. *"A conjunction, unrelaxed."* |
| L3 | predictions resolving | **MET** | `workbook/PREDICTIONS.tsv` 19 rows, 12 RESOLVED / 6 OPEN / 1 REHOMED, **0 overdue** |
| L3 | **dated falsification surface** | ✅ **MET — upgraded from FAIL-grandfathered** | the `Kill rail re-derived: 2026-09-04` stamp, above |
| L4 | TRADE.md feeding proposals | **WAIVED-cite** | input agent, Will 7/25 (carried from the parity assessment) |
| L4 | output consumed by others | **MET** | head of LABOR→CARL→REGINALD→HENRY; `cbb2ca8b9` NEXUS_BRIEF re-pinned to STATUS HEAD `5b3fc6705` |
| **L5** | clean closeouts | **MET** | 9/10 and 9/17 both closed with a frozen card and a ledger write |
| **L5** | zero YEYOU flags | **NOT-ADJUDICATED** | cohort banner (`runs/2026-09-07_LABOR_PARITY_ASSESSMENT.md` already recorded this as NOT-ADJUDICATED — no LABOR row in YEYOU's single run) |
| **L5** | current | **MET** | 9/17 session; `GRADING_CARD_20260917_claims.md` frozen today |

**Recommendation: SUSTAIN L5 · Conf H — with leg (2) recorded as NOT MET and re-dated, not waived.** Confidence **H**: I ran `card_partition_check.py` against all ten real cards, ran `read_cap_check` and `ledger_staleness`, and read `EXIT RULES`, `CLAUDE.md:22/42/77/154/281` and the checker source myself.

**Why SUSTAIN and not DEMOTE on a failed sustain leg.** Leg (2) is a *write-mode* leg, and the thing it protects — that a boot-read surface fits its budget — has **not** been breached: `read_cap_check --agent LABOR` returns **rc=0**, both flagged files are in the 🟡 rotate-tier band, neither is over budget, and `STATUS_DETAIL.md` at 165 KB is correctly **not** a boot read and carries no budget of its own (`CLAUDE.md:281`). Meanwhile the two legs that measure *falsification integrity* — the thing L5 is actually about — both **improved** in-period: the grandfathered L3 FAIL cleared, and the checker produced its first real clean case. **Demoting a desk for byte accretion while its falsification rail hardens would grade the wrong thing.** But leg (2) is now **10 days unmoved on 3 of 4 named surfaces and the brief grew 5.5 KB**, so it must be re-dated with teeth rather than restated.

**Proposed re-dated leg (replaces the open half of (2)):** *before the **2026-09-25** Oct-2 card freeze, `read_cap_check --agent LABOR` returns **zero 🟡 rows** (both STATUS and LESSONS under 70% of budget), and `NEXUS_BRIEF.md` stops growing (byte count at 9/25 ≤ its 9/17 count of 94,318 B).* Mechanically checkable, dated to an event LABOR already owns, and it names the surfaces the original leg named.

## 4. Profile trigger
Profile: `profiles/LABOR.md`, **REFRESHED 2026-09-07** (parity assessment).
Quoted: *"**Staleness (content-derived, greppable):** refresh when `workbook/PREDICTIONS.tsv` shows **LAB-18 or LAB-19 at a terminal Status**, when LABOR executes the **WQ-179 (c) mode change** (grep `STATUS.md` for `STATUS_DETAIL` in a grade row's ACTION cell), when the **matrix total moves ≥3 points from 29/75**, or **>30d (2026-10-07)** — whichever first."*
**Verdict: FIRED, on the WQ-179(c) leg.** `grep -n "STATUS_DETAIL" AGENTS/LABOR/STATUS.md` → **39 rows**, including grade-row rotations dated in-period (`§ status-line-rotated-20260917`, `§ exit-rules-rotated-20260910`, `§ wq214-vintage-sweep-installed-20260910`, `§ exit-rules-graded-20260907`). The mode-change signature the trigger names is present and dated inside the period.
Other legs: LAB-18 and LAB-19 both still **OPEN** (not terminal) → NOT FIRED. Matrix **29/75** unmoved → NOT FIRED. 30d → 10/07, not yet.
⚠️ **The trigger fired but the substance did not** — the greppable signature of the write-mode change is present while the bytes it was supposed to control are unchanged. **This is a good trigger detecting the wrong half of its own condition**: it greps for the *form* of the fix (a pointer row) and cannot see whether the *file got smaller*. `[[finding_record_of_an_action_is_not_the_action]]`. Recommend the refresh re-cut the trigger to a byte test.
**Profile statements now false:** *"STATUS 31,630 B (97%) + LESSONS 28,944 B (89%) today"* → 32,177 / 32,285 (99% / 99%); *"F5 CLOSED (9/25 docketed)"* still holds; §3 invalidation table row *"**Section date stamp** — ⛔ **NONE** … ⇒ L3 leg FAIL-grandfathered; `falsification_scan` cannot see it"* — **now false**, the stamp is on the section header.

## 5. Falsification read — market desk with no thesis-class file the scanner can see

**Verdict: RAIL-IN-LOCAL-FORM, and the local form is the fleet's reference implementation.** Locator: **`AGENTS/LABOR/STATUS.md` § EXIT RULES** (plus `docket/graded/` as the frozen-card layer).

**Where it lives, and why the scanner cannot see it:** LABOR has no `thesis/KILL_TREE.md`-class file; the rail is a *section* of the boot-read STATUS. As of 9/7 it also had **no date stamp**, which is precisely why `falsification_scan` could not see it — the profile's own §3 table logged that as ⛔ and graded the L3 leg FAIL-grandfathered.

**Does it have an EVIDENCED fire path?** ✅ **Yes — on three independent legs, all dated, all with named instruments, and the whole rail is re-derived on a schedule:**
- **The section now carries its vintage in content:** *"## EXIT RULES (recalibrated Jul 2) · **Kill rail re-derived: 2026-09-04** [BLS USDL-26-1435]"* — an in-content stamp with the issuing document, exactly the form PAT-039/044 require (never mtime).
- **The re-derivation is a charter control, not a banner:** *"🔧 **VINTAGE SWEEP (C1, unconditional per WQ-214): run 2026-09-10 18:0x ET — 4/4 rails CURRENT on the 9/10 vintage, no repair owed**"*, with the follow-on line *"✅ Vintage sweep is now a CHARTER CONTROL, not a banner — `CLAUDE.md` C1 carries it unconditionally at every closeout (WQ-214, Will-approved 2026-09-10). **Reminder retired; the obligation no longer lives here.**"* A reminder was replaced by a mechanism and the reminder was then **deleted** so two instructions do not stand — `[[finding_correction_beside_an_instruction_leaves_two_live_instructions]]` handled correctly.
- **FREEZE-THAW v2 graded leg-by-leg on a live print, unrelaxed:** *"LEG A ✗ — bar recomputed on the revised vintage **BEFORE reading August** (L-02, as the card ordered): `(31+21+X)/3 ≥ 100` ⇒ **X ≥ +248K** (was +303K on the old vintage). August **+162K ⇒ short by 86K**. Single-month leg met (162 ≥ 150); 3-mo-avg leg fails (71.3 < 100). **A conjunction, unrelaxed.** LEG B ✗ — EPOP 59.1 vs the ≥59.2 bar, short 0.1pp. LEG C ✗ — JOLTS NET −18K [Jul] / −5K [Jun rev]."* Three legs, three instruments, three misses, and the bar was **recomputed before the data was read** because the frozen card said to.
- **The F4 defect my own row logged is repaired:** the Jul-2-vintage run that used to sit in the Kill A bullet while KEY THRESHOLDS carried 9/4's figures is now rotated to `STATUS_DETAIL.md § exit-rules-rotated-20260910` and the bullet carries the 9/4 vintage alone (`63 / 31 / 21 / 162`). The G5 recurring class is closed on this surface.

**Two-vintage rule:** STATE surface → dated by its header's labelled freshness claim. It now has one (`Kill rail re-derived: 2026-09-04`) plus a dated control run (9/10). **Clean.** The `falsification_scan` blind spot that produced the 9/7 grandfathered FAIL is closed.

## 6. Negative-resolution leg — opened `workbook/PREDICTIONS.tsv` (19 rows)

6 OPEN: LAB-03 (claims breach 250K), LAB-08 (BLS benchmark revision >500K downward), LAB-11 (AI narrative shield breaks), LAB-12 (U-3 ≥5.0%), LAB-18 (T-03 fires), LAB-19 (LF MoM >0 in ≥2 of 3 prints). **All six resolve on a POSITIVE event or threshold crossing.**

**Counts: 6 candidates opened / 0 confirmed negative-class / 0 lacking instrument.**
This is a **structural property of the desk, not an omission**: LABOR's book is written as threshold-and-mechanism *firing* calls, and its *negatives* are carried on the **kill rail** (Kill A 0-of-3, Kill B 0-of-5, FREEZE-THAW NOT FIRED) where they are graded as **run counters with live state**, not as ledger rows. That is the better home for a "has not happened yet" claim — a counter with a named instrument and a printed count cannot silently pass a presence audit the way a blank resolver cell can. **Worth recording as the positive case**: the desk that has zero negative-resolution ledger rows is the one whose negatives are the best instrumented.

## 7. As-made receipt — **n/a** (and note: LABOR's as-made audit was **self-found**, Brier 0.299→0.342, 0-for-5 at ≥60%, propagated into `CLAUDE.md:51`).

## 8. Cross-agent threads / pattern candidates
- **→ LABOR (packet):** re-dated leg (2) as proposed in §3, before the 9/25 Oct-2 card freeze. And `ledger_staleness --nudge LABOR` → **PAYROLL_VINTAGES.tsv 10 STATUS-writes behind**, PREDICTIONS.tsv 2 — freeze-or-refresh each.
- **→ LABOR (packet):** `NEXUS_BRIEF.md` grew **+5,546 B in 10 days** to 94,318 B while F1 flagged it at 88,772. NEXUS boot-reads it.
- **🔴 PATTERNS candidate (strong):** ***A staleness trigger that greps for the FORM of a fix fires on the pointer row and cannot see whether the file got smaller.*** Evidence: `profiles/LABOR.md` staleness line names *"grep `STATUS.md` for `STATUS_DETAIL` in a grade row's ACTION cell"* as the WQ-179(c) signature — 39 such rows exist and the trigger fires, while `STATUS.md` is at **99% of budget**, unchanged from the 98.7% my row recorded 10 days ago. The greppable-trigger design (which is otherwise right, and was adopted against mtime) has a blind spot exactly where the metric is a byte count. Dedup against `[[finding_record_of_an_action_is_not_the_action]]` — this is its *instrument-design* form: **a content-derived trigger inherits whatever the grep can see, so a byte-valued condition needs a byte-valued test.**
- **PATTERNS candidate (secondary, positive):** *A desk whose negatives live on a counted kill rail rather than in prediction rows has better negative-resolution hygiene than the ledger scan can detect.* Evidence: LABOR scores 0/6 negative rows on the §6 scan and has the best-instrumented negatives in the cohort (Kill A 0-of-3, Kill B 0-of-5, FREEZE-THAW every leg graded). **A negative-resolution audit that only reads prediction ledgers will score this desk as absent.** `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`.

## 9. Reviewer-side defects (mine)
- 🟠 **My row's F3 — *"red on all 6 real cards, 2 of them FALSE … no real clean case yet"* — is REFUTED and was written against v3.1.** The tool's own review history (`card_partition_check.py:` REVIEW HISTORY block) records that **v1 and v2 each shipped described as "falsified" and CODEX broke both** (5 false passes, then 4), and that *"The recurring error was never the parser — it was calling a self-authored suite 'falsification'"*. My row graded the desk on a snapshot of a tool that was **being actively repaired by its own author** during the review window.
- 🟠 **The profile's staleness trigger is defective in the way §4 describes** — it greps for a pointer row to detect a byte-reduction change. I wrote it; the flaw is mine.
- 🟠 The `Gaps` cell says *"L3 dated-falsification leg FAIL-grandfathered (EXIT RULES has no kill-rail stamp — retrofit at next closeout)"*. **The retrofit happened — on 9/4, three days BEFORE I wrote the cell**, and my own parity assessment recorded the 9/4 re-derivation under F4 as CLOSED in the same row. **I graded the leg FAIL and recorded its fix in adjacent cells of the same row.** `[[finding_summary_section_merges_what_the_body_separates]]` — the verdict line and the evidence line disagreed and the verdict line is the one that travels.

---

# VIOLET — Market · FLEET_MAP L4 / Conf H / last_scored 2026-09-04

## 1. Period production
**73 self-authored / 45 routed-in · last self-commit 2026-09-17 `f8cb6d2ff` · 0 dark days.**
Shipped: 9/4 EVE the five-🔴 closure (`e40654616`) · 9/11 the VECTOR-2 cheap-vol instrument answer **delivered early** (`3e802f089`) · 9/14 the FOMC-letter roll-date **erratum filed pre-outcome** + the L376 FT-10 publication review returned (`a19f4cb44`) · 9/16 data refresh · **9/17 the VIO-FOMC-0916 part-1 grade** (`f8cb6d2ff`, `c9cbf901b`, `cfabc96a3`).

## 2. Row-claim test

| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | "STATUS 28,387 B after rotation" | **REFUTED — much better** | `read_cap_check --agent VIOLET` → **STATUS.md 9,880 B = 30% of budget** ✅ |
| 2 | "VX_DAILY 4 missing sessions, **no completeness check**" | **REFUTED on the check; sessions CANNOT-EVALUATE** | `scripts/vx_daily_gapcheck.py` exists — *"`VX_DAILY.tsv` session-completeness check — the OMISSION half of ledger integrity … a missing session is not cosmetic: `RED-FT-10` counts consecutive CBOE bars ≥150"*. Companion `skew_bar_continuity.py:36` states the right principle: *"**A ledger cannot be its own completeness reference**"*. I did not count live gaps. |
| 3 | "prediction registry split (Q2 open)" | **REFUTED — the registry exists and is populated** | `workbook/PREDICTIONS.tsv` — 5-col schema (`id / resolve_date / status / navigation_summary / source`), **6 rows**: VIO-FOMC-0916-L1 VOID · L2 PENDING (9/23) · L3 PENDING (9/18) · L4 KILLED · L5 HELD_WITH_DEFECT · F-B HELD. Every row carries a `source` pointer to the grade record or the script. |
| 4 | "KB 46% past `Stale_By`, two-state form chosen = LIVE + vintage header (Q3 answered), **header not yet on file**" | **TRUE-STILL** | `head -c 600 workbook/KB.tsv` — the file opens **directly on the column header row**; `grep -rn "Last real data refresh" AGENTS/VIOLET/ --include=*.tsv` finds the phrase **only inside the 9/4 DAEDALUS packet in `inbox/processed/`**, never on KB.tsv. The form was chosen 13 days ago and not applied. |
| 5 | "TRADE.md log row 242 OPEN vs closed, **no two-state banner**" | **REFUTED on the row; TRUE-STILL on the banner** | `grep -n "242" TRADE.md` → **no match** (the file is shorter; the row is gone). But there is still **no `Last real data refresh:` header** — the file opens *"# VIOLET TRADE / VIX-linked positions and trade framework."* ⚠️ It does carry the single best self-indictment I read in this cohort at `TRADE.md:31`: *"**THIS SECTION READ 'None.' WHILE THE POSITION WAS LIVE** — 2026-07-27 11:35 ET to 2026-07-28 ~04:30 ET (KB-VIO-142). Caught by a provenance audit, not by any guard. **The boot staleness check passed this file `ok +2d`** because it compares *mtime to STATUS.md* — it measures **age, not agreement**."* |
| 6 | "3 ledgers silent-rot middle, **no LEDGER_GLOB**" | **SPLIT: LEDGER_GLOB REFUTED; silent rot TRUE-STILL** | `workbook/LEDGER_GLOB` now exists (`39a3a1038`, 2026-09-14) declaring `workbook/*.tsv`, `registry/*.tsv`, `board_log.tsv`. ⚠️ **Note against the 9/14 L285 sitting**, which lists VIOLET among the 26 undeclared desks — **that census was true when run and is false at HEAD; VIOLET declared on the same day.** `ledger_staleness --nudge VIOLET` → still **3 behind: corrections_receipts.tsv (8), COT_VIX.tsv (5), FLOW.tsv (1)**. |
| 7 | "outbox 7 delivered unmoved · 8 cross-surface contradictions" | **CANNOT-EVALUATE** | not re-counted. |
| 8 | Next_upgrade (a) *"✅ MET 9/4 EVE"* | **TRUE-STILL** | — |
| 9 | **DEMOTE trigger**: *"STATUS breaches the budget with no rotation before the next write, **or the 9/16 grade is taken from an instrument the letter did not name**"* | ❌ **DOES NOT FIRE — on either limb, and I checked both** | STATUS at 30% of budget. And the grade's instruments are the letter's own: `research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md` §1 — MOVE from *"`workbook/MOVE.tsv`, investing.com PRIMARY (**letter §6.2 names this ledger**)"*, VIX from *"CBOE `VIX_History.csv` (publisher of record, KB-VIO-246)"* cross-checked against yfinance, VX settlements from CBOE `settlement/csv/?dt=…`. Explicitly excluded: *"**Never used:** STATUS marks, intraday bars, the 9/17 pre-open tick."* |

**Score: 4 TRUE-STILL / 4 REFUTED / 1 CANNOT-EVALUATE** (+2 not recounted).

## 3. Ladder walk (Market, current L4 → next L5) — **grade record read; market call NOT re-graded, per the task**

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L3 | convergence matrix | **MET** | 11-vector / 55-pt matrix `STATUS.md`; scale DECLARED 10×5=50 with cheap-tail removed from the stress sum, computed==declared==29/50, **checker fails closed** (9/4 closure) |
| L3 | exit rules | **MET** | gate register: RED-FT-10 · KB-VIO-123 6-leg tree · GATE-VIO-116 F1 72.41 re-arm · RV1 RETIRED (F2-killed) · T9 conjunctive falsifier |
| L3 | predictions resolving | ✅ **MET — and the Q2 gap is closed** | `workbook/PREDICTIONS.tsv`, 3 resolved + 1 held + 2 pending, each with a `source` pointer |
| L3 | dated falsification surface | **MET** | `research/2026-09-16_FOMC_VIXEXPIRY_PREREG_LETTER.md` — frozen 9/2, **sha256 `ead84431…9222`**, byte-identical at grade time, last commit `c6851727e` |
| L4 | TRADE.md feeding proposals | **MET** | `TRADE.md` § ACTIVE POSITIONS: *"No VIOLET position in the last recorded broker mirror (FORGE, September 10). **This is not a September 14 broker verification.**"* — a FLAT declaration that states the limit of its own evidence |
| L4 | output consumed by others | **MET** | `PROME/DOCKET.tsv:276` — *"PROME consumed 2026-09-17 08:4x ET"*, commits verified on origin; L376 review returned to RED's chain and PROME recorded its concurrence |
| **L5(a)** | *"✅ MET 9/4 EVE (five 🔴 closed at HEAD)"* | **MET** | carried |
| **L5(b)** | *"one clean external-review cycle after the 9/16·9/23 letter grades"* | ⏳ **NOT YET — by the leg's own calendar** | Part 1 graded 9/17 (legs 1·4·5 + F-B). **Leg 3 grades on the 9/18 close (DOCKET L277); leg 2 on the 9/23 close (L278).** The leg names both letter grades; one of three parts is in. |
| **L5(c)** | *"KB vintage header on file + the forward-prediction registry named (Q2)"* | **HALF MET** | registry ✅ (row 3); **KB header ❌** (row 4) |
| **L5** | clean closeouts | **MET** | 9/17 closeout produced the grade record, three commits, a DOCKET disposition PROME verified on origin |
| **L5** | zero YEYOU flags | **NOT-ADJUDICATED** | cohort banner |
| **L5** | current | **MET** | graded on the 9/16 **official** closes, one day late and **the lateness disclosed with its cause**: *"DOCKET L276, dated 9/16 — one day late: the box crashed on the 9/16 evening; PROME WQ-184 L0 spawn 9/17 ~08:2x ET"* |

**Recommendation: HOLD L4 · Conf H.** Confidence **H**. The demote trigger does not fire on either limb (row 9) and (b) is not due until 9/23. **No re-grade of the market call was performed** — I read the grade *record* and tested only whether its instruments were the letter's, which is a structure question.

**On the grade record itself, because it bears on the next promotion.** This is the strongest falsification artifact I read anywhere in the cohort, and the reasons are all structural:
- **Anchors published before the verdict, with their cross-checks** (§1): every one of eight anchors carries a publisher-of-record and an independent agreement mark; the one instrument that failed (`FRED VIXCLS`, *"ACCESS FAILURE ×2 … UNKNOWN — **not evidence either way**; two publishers already agree"*) is recorded as UNKNOWN rather than quietly dropped.
- **A VOID recorded as VOID, not converted into a pass** (leg 1): *"**VOID — not failed, not passed** … The letter declared this outcome in advance (§4 LEG 1 NOT-GRADED); the erratum forbade an early void on the 9/14 print — the 9/15 close alone decided it."* The context figure (+2.965%, which *"would have sat inside CONFIRM had the cohort applied"*) is given and explicitly **not** graded.
- **A KILL taken against the desk's own frame, with the inconvenient run shown** (leg 4): rates vol led on 9/14 and 9/15 and surrendered the lead on the delivery session; *"The registered date is the 9/16 close, so the grade is KILL, full stop. The 9/14–9/15 lead is context for the next letter, **not a re-dating of this one**."*
- **A defect disclosed pre-outcome and then carried onto the grade** (leg 5): the §5 roll-date erratum was filed **2026-09-14, before the event** (`research/2026-09-14_FOMC_LETTER_roll_date_erratum.md`), and the leg is graded *"HELD — with the §5 specification defect DISCLOSED, **not a clean pass**"*.
- **A frozen anchor that was wrong when frozen, self-found and shown both ways** (§3): the letter's VIX 8/27 anchor **value** 14.70 was a yfinance provisional cell corrected to 14.51 by the 9/6 CBOE reconciliation; the grade is computed on **both** (+22.05% / +20.48%), the verdict is invariant, and the lesson is named — *"a pin proves WHICH letter, not that its cells were right"* `[[finding_a_hash_pin_authenticates_the_reference_not_your_agreement_with_it]]`.

**Suggested tightening of leg (b) at the next scoring**, since the 9/16 half is now in evidence: *(b) is satisfied when leg 3 (9/18) and leg 2 (9/23) are graded to the same standard as part 1 — anchors published, instruments the letter named, a NO-CONFIRM recorded as such — and (c)'s KB vintage header is on file.* That makes the promotion depend on repetition rather than on one exceptional record.

## 4. Profile trigger
Profile: `profiles/VIOLET.md`, **body 2026-09-04 (Fri, EVE) — FULL REFRESH**, Mode-A 4-reader fan-out.
Quoted: *"**Refresh clock: 21 d → 2026-09-25**, or at the first of: **the 9/16 letter grade** · KB.tsv two-state ruling · the next external review round."*
**Verdict: FIRED.** The 9/16 letter grade landed **2026-09-17** (`f8cb6d2ff`, DOCKET L276 OWNER-GRADED). The **earlier-of** clause is satisfied, so the clock expired on 9/17, eight days before its calendar date.
⚠️ **And this matters for the grade**, which is why I am flagging it rather than just noting it: the FLEET_MAP `Next_upgrade` cell says *"**Conf stays H while the profile clock holds** (→ 9/25)"*. The clock's calendar leg holds; its **earlier-of** leg has fired. **VIOLET's Conf H is currently resting on a clock that has expired by its own terms** — the cell read only the date and not the condition beside it. `[[finding_an_amendment_read_for_one_item_leaves_the_others_derived_from_the_original_live]]`. The Conf H recommendation above stands on the *evidence* in §3, not on the clock; but the row must be re-cut.
**Profile statements now false (§1 byte anatomy):** `STATUS.md` *"**32,546** … at **99.99 %** (4 B headroom)"* → **9,880 B / 30%**; `SCRATCH.md` *"17,997"* → 4,981; `CALENDAR.md` *"20,880"* → 3,862; `MEMORY.md` *"21,457"* → **25,339 B = 78%, now the desk's only 🟡 rotate-tier surface** (the one surface that *grew*). §2 *"tail §'Current status' is 2026-06-10, 86 d stale"* — not re-checked.

## 5. Falsification read — **not in scope** (VIOLET is on none of the three step-5 lists). Read anyway in the course of §3; the pre-registration/grade chain is live, dated and sha-pinned.

## 6. Negative-resolution leg — opened `workbook/PREDICTIONS.tsv` (6 rows) and `workbook/CATALYSTS.tsv`

2 rows not terminal: **VIO-FOMC-0916-L2** (resolve 9/23) and **-L3** (resolve 9/18). Both resolve on **signed numeric comparisons**, not on absences:
- L2 — *"9/16→9/23 VIX change **>0** confirms; **<−1.41%** kills; remainder inconclusive"* — three-way with a declared INCONCLUSIVE band, so there is no "nothing happened" residue to grade as a negative.
- L3 — *"exactly one branch ≥2/3; original branch cells authoritative"*, with the 9/16 preliminary already published as *A 1/3 · B 1/3 · C 0/3, no branch*. **The whole-map NULL is declared in the letter in advance** (profile §2: *"INCONCLUSIVE + whole-map NULL declared"*), which is the correct way to pre-allocate the no-branch outcome instead of resolving it as a negative after the fact.

**Counts: 2 candidates opened / 0 confirmed negative-class / 0 lacking instrument.**
**Design note worth carrying:** VIOLET has **no negative-resolution rows because its letter pre-allocates every outcome state**, including the null. Leg 1's VOID is the demonstration — a state that would otherwise have been graded as a silent negative was **declared in advance as NOT-GRADED**, then executed as VOID. Compare `PROME/DOCKET.tsv:376`, where RED found FT-10's letter *"leaves that state UNALLOCATED and the instrument resolved it silently from outside the letter"*; VIOLET's return on that chain (`reports/2026-09-14_inbox/FT10-publication-review.md`, 13 offline specification cases) is the same discipline applied to another desk's letter.

## 7. As-made receipt — **n/a**.

## 8. Cross-agent threads / pattern candidates
- **→ VIOLET (packet):** the KB vintage header is the last open half of L5(c) and has been "chosen but not applied" for 13 days; it is one line on `workbook/KB.tsv`. And `MEMORY.md` is now the desk's only 🟡 surface at 78% (rule-5 stop <70%: 2,555 B).
- **→ VIOLET (packet):** `ledger_staleness --nudge VIOLET` → corrections_receipts.tsv **8** STATUS-writes behind, COT_VIX.tsv **5**, FLOW.tsv **1** — LEDGER_GLOB now exists, so these are declared-and-rotting rather than invisible.
- **→ RED / PROME (info):** `PROME/DOCKET.tsv:376` — **RED's owner adoption of the FT-10 publication allocation is still the only remaining gate**, PROME has recorded concurrence with VIOLET's narrowing, and the row's stated purpose was that the contingency not be decided under time pressure. **FT-10's next grade is imminent and the allocation is still unadopted.** Not mine to move; flagged because the 9/16 deadline the row was written against has now passed.
- **PATTERNS candidate:** ***Pre-allocating the null outcome in the letter removes the negative-resolution problem instead of instrumenting it.*** Evidence: VIO-FOMC-0916 leg 1 graded **VOID** on a condition the letter declared in advance (`GRADE_part1.md` §2), against `DOCKET.tsv:376` where an unallocated state was *"resolved silently from outside the letter."* This is the constructive complement to the whole §6 leg: the strongest answer to "does the row name a search instrument for its negative" is "the letter has no ungraded states." Dedup against `FORGE/PREDICTION_DISCIPLINE.md` § Grading before minting.

## 9. Reviewer-side defects (mine)
- 🔴 **The `Next_upgrade` cell ties Conf H to *"the profile clock (→ 9/25)"* while the profile clock is an earlier-of with three condition legs, the first of which has now fired.** I copied the date out of the clock and left the conditions behind, so the cell asserts a hold the clock itself no longer supports (§4).
- 🟠 **Four of the row's `Gaps` claims are refuted at HEAD** (STATUS bytes, VX_DAILY completeness check, prediction-registry split, TRADE row 242) on a row `last_scored 2026-09-04` — **13 days** on the fleet's highest-cadence desk (~1 commit/day, 73 self-commits in 17 days). For a desk at this cadence a 13-day-old current-state cell is structurally stale.
- 🟠 **A cross-review inconsistency I should flag against my own 9/14 work:** `runs/2026-09-14_L285_LADDER_INTEGRITY_PARTIAL.md` lists VIOLET among the **26 desks with no `LEDGER_GLOB`**. `AGENTS/VIOLET/workbook/LEDGER_GLOB` was committed **`39a3a1038`, 2026-09-14** — the same day. The census was true when run, is false now, and **the 21%-of-33 figure it corrected is itself now stale**. A coverage census with no vintage line on the figure is a number that will be quoted after it stops being true.

---

## Appendix — commands run (so this is reproducible)

```
git log --after="2026-09-01 00:00" --format='%h|%cs|%s' -- AGENTS/<X>/     # per desk, self/routed split
python3 scripts/read_cap_check.py --agent <X>                              # all six
python3 scripts/ledger_staleness.py --nudge <X>                            # SAM ZHAO HANS BRENT LABOR VIOLET
cd AGENTS/BRENT  && python3 scripts/render_calendar.py --check             # rc=0, 25 events matched
cd AGENTS/BRENT  && python3 scripts/predictions_due.py                     # 0 overdue
cd AGENTS/HANS   && python3 scripts/test_hans.py                           # Ran 51 tests ... OK
cd AGENTS/LABOR  && python3 scripts/card_partition_check.py docket/graded/*.md   # 10 cards, 1 rc=0
grep -P '^<X>\t' AGENTS/DAEDALUS/FLEET_MAP.tsv                             # row claims
```

**Not done / limits of this report:** I did not recount BRENT's `INCIDENTS.tsv` ACTIVE rows or its CLAUDE.md contradictions, did not sweep BRENT's 10 packets at recipient trees, did not count VIOLET's live `VX_DAILY` gaps / outbox / 8 cross-surface contradictions, and did not recount LABOR's 8 WQ-112 re-mark cells. Each is marked CANNOT-EVALUATE in place. I re-graded no market call, edited no file outside this one, and ran no mutating git command.
