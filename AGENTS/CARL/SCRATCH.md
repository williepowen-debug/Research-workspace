# CARL SCRATCH
**Last session:** **2026-09-11 (Fri) ~10:30 → ~14:0x ET** — Will-directed boot + full catch-up.
**Type:** August CPI graded against a pre-committed frame · UMich Sept prelim · CRL-10 re-priced · dashboard staleness audit + 4 refreshes at primary · rotation #11a/#11c · two infra fixes, one of which was a wrong diagnosis of mine.

**PRIORITY-1:** **TWO PHAN PACKETS ARE UNPROCESSED AND ONE IS 🔴 — `inbox/2026-09-11_from-PHAN_sec2-rebuild-400B-retired-and-a-routing-defect.md` retires the domain's headline number ($400B+) AND names a routing defect on CARL's side; `..._pm-sweep-abs-leg2-mixed-plus-two-cockroaches.md` carries two items that cut AGAINST the thesis.** Both need grading **at the primaries** (PHAN proposes, CARL disposes), and neither should be half-read at the end of a session.

---

## ⏭️ NEXT SESSION, FIRST THREE THINGS
1. **Drain the two PHAN packets above.** The §2 rebuild touches **KB-CARL-367** and the phantom-debt magnitude that CARL's own CLAUDE.md K-SHAPE section quotes (~$176-216B / credit-only ~$30-60B). **If that number moves, the card moves** — do not integrate it anywhere until it is graded at DEWEY's C4 source, which PHAN says it read directly rather than through the KB summary.
2. **9/14 DAEDALUS LADDER SITTING IS MONDAY — inputs are sent** (`AGENTS/DAEDALUS/inbox/2026-09-11_from-CARL_ladder-inputs...`). ⛔ **The headline input is that CRL-10's cut is worth +0.3780 Brier on one row, larger than the entire +0.3808 four-row as-made correction the sitting exists to handle, and it is a LATE re-price.** If the sitting scores 8% at the 9/11 mark it banks a gain that was available on 8/15.
3. **~9/15-16 is a THREE-PRINT cluster:** SDART/BLAST August 10-D (V2 broad tier) · **Census advance retail sales = the V8 Tier-1 BEHAVIOURAL half** (today only supplied the deflator) · **FOMC 9/15-16, meeting 1 of 2** for any V12 un-fire.

---

## WHAT HAPPENED

### ⛔ The CPI frame worked, which means it stopped me taking the friendly number
Gasoline printed **+3.90% SA / +2.53% NSA**. The frame's *">+2.5% = pass-through ahead of the pump input"* bar **never named a basis**, and the two answer opposite ways: the bar was built from **unadjusted pump dollars**, so the like-for-like figure is **NSA — 0.67pp BEHIND the +3.20% input.** **Leg scored NOT-DISCRIMINATING.** ✅ The frame *did* call the **sign flip** (July SA −2.86% → Aug +3.90%). Three defects in my own frame recorded, not edited: no basis named · bar set **below** its own stated expectation · **named HEN-41, which resolved ~8/12** (live letter is **HEN-44**; PROME flagged it, I verified at HENRY's files rather than relaying).
✅ **HENRY's frozen HEN-44 carries pump $3.932 → $4.058 (+3.20%); I computed +3.198% off `GASREGW` before opening it.** Two desks, one primary, no fitted parameter.

### 🔑 The squeeze narrowed to ENERGY ONLY — adverse to my own thesis wording
YoY NSA: energy **+16.28%** ⬆ · gasoline **+27.40%** ⬆ · **core 2.48 → 2.45%** ⬇ · **food 2.98 → 2.67%** ⬇. Headline−core wedge **0.88 → 0.95pp**. v2.6.6 asserts a **multi-vector** squeeze; in August one vector carried it. Written onto the row as a **narrowing**, not corroboration.

### 🔻 CRL-10 62% → 8%, and the damning part is the date
Needs **+0.471%/mo ×3** (Nov) or **+0.505%/mo ×4** (Dec) vs a trailing **+0.132%/mo** — ~3.6× current pace. Base-rated BEFORE re-pricing: **38/376 windows since 1995 = 10.1% unconditional**; seasonality against (Nov −0.057%). Mechanism NOT killed.
⛔ **Oct-2026 YoY is NOT COMPUTABLE — October 2025 CPI was never published.** Q4 resolves on **Nov + Dec only**. Recorded as resolvability, deliberately **not** folded into confidence — and qualified honestly: interpolated, October needed **+0.756%/mo** and was the *hardest* month, not a lost shot.
⛔ **WALTER `SIG-W-20260812-006` gave me this argument on 8/12. My own 8/15 note says the slope is "FLATTENING" — then "CRL-10 UNCHANGED at 62%." 27 days.** Filed `INFO_ONLY`, which means recorded-and-not-acted-on by definition. **Guard now wired into CLAUDE.md 5b.2.** KB-CARL-450.

### Dashboard audited BY AGE, then 3 label defects + 4 stale rows fixed at primary
- **Labels that lied** (row current, As-Of older): Student 90+ · FHA/VA · Retail Sales. They read as 57-167d stale while the data was fine.
- **Student Loan 30+ DQ — the "16.3% WORST EVER" figure sat 195 days and had MORE THAN HALVED** (flow 16.35 → 11.03 → **7.83%**). ⛔ **Not relief: the 90+ STOCK went the other way to a series high 10.60%.** Inflow collapsing while the stock records = a cohort passing through.
- **Total HH debt $18.7705T Q2** (flat). ⭐ **The composition is the read:** 90d **0.314 → 0.240**, 120+ **1.298 → 1.086**, **SevDerog 1.544 → 1.754 → 1.987**. Upstream buckets draining into the terminal one. Honest limit recorded: part of that is the charge-off *retention* effect that killed CRL-05.
- **CCC refreshed after 73 days under the row's own stale warning:** broad HY **tightened** 275 → 270 while **CCC blew out 970 → 1,070bps.** CCC/HY 3.53× → **3.96×**.
- **NFIB August:** 98.7 (−1.1) still above average, but **actual sales −9% net, worst since Nov 2025** — first split of that row's level vs rate-of-change legs.
- **MBA NDS deliberately NOT refreshed** — a Q2 exists but the overall figure isn't in hand and `mba.org` 403s. Labelled a resolvability gap rather than inventing a number.

### ⛔ I told Will boot.py was hung. It wasn't.
**25.0s, exit 0, 7/7 scripts OK.** The zero bytes were `| tail -120` — tail cannot emit until stdin closes, so a slow run looks dead. The 12-min run was real and consistent with FRED latency near the 90s per-script timeouts, **but the orchestrator has timeouts and cannot hang.** Guard wired into the card. **A wrong infra diagnosis reached the operator as a "pattern" and would have justified rewriting a working orchestrator.**

### ✅ abs_monitor.py FIXED — 4 sessions owed
Split into **"Exeter — V2 REGISTERED PANEL"** (EART 2022-2/2022-3/2023-1/2024-1, CIKs verified at `data.sec.gov`) and a separate new-issue pipeline. **Tested, not assumed:** post-fix run returns 80 10-Ds, filenames `eart2022-2_10d.htm`… confirming deal identity, latest 2026-08-31.
⚠️ **NEXT SESSION: the first run flagged all 80 as NEW (empty seen-state). That is a backfill artifact — do NOT read 80 new filings as an event.**

### 🔴 FLOW-PHAN-06 RESTORED to ACTIVE — my 9/10 grade was wrong
PHAN self-reported a **period-basis error**: a *quarterly* trigger tested against a *fiscal-year* aggregate. **I verified at the primary rather than accepting** (SEC XBRL, CIK 0001820953): FQ1 **+1.8%**, FQ2 **+40.0%**, FQ3 **+33.5%**, matching to one decimal. ⚠️ **FQ4 +42.5% is PHAN-derived by differencing and I did NOT reproduce it.** ⛔ **3-leg breakpoint still NOT met** — ABS WA FICO untested since 672 (Apr-2026), the pathway's largest gap. ⭐ PHAN's stronger finding is outside the trigger: **NCOs accelerate +12.6 → +16.5 → +22.2 → +36.9% while headline DQ ex-Peloton FELL.**

---

## STATUS CHANGES
| Item | Change |
|------|--------|
| **CRL-10** | 🔻 **62% → 8%**, reachability. Oct-2026 resolvability gap recorded |
| CPI row | "Food CPI Headline" (June) → **CPI COMPOSITION (August)**, energy-only finding |
| Student Loan 30+ | 16.3% (Q4-25) → **7.83% flow**, with the 10.60% stock divergence |
| Total HH Debt | $18.8T Q1 → **$18.7705T Q2** + the SevDerog composition read |
| HY OAS / CCC | CCC **970 → 1,070bps**; ratio 3.53× → **3.96×** |
| UMich | Aug final → **Sept prelim**: 47.8 · 1Y **4.0 → 4.6%** (🟠→🔴) · 5-10Y 3.3 → 3.4 |
| Gas / diesel | **$4.295** (CRL-08 gap **20.5¢**) · **$6.056, $6 handle broke** |
| NFIB | July → **August 98.7**, actual sales −9% |
| FLOW-PHAN-06 | **PARTIAL → ACTIVE** (9/10 call reversed) |
| Cycle counter | **RETIRED** — had drifted to 3 values on 3 surfaces |
| KB | 442 → **458** |
| STATUS.md | 49,204 → **51,057 B** after rotating **14,548 B** out |

---

## NEXT SESSION SHOULD

### IMMEDIATE
1. **Two PHAN packets** (PRIORITY-1).
2. **Mon 9/14 DAEDALUS sitting** — inputs sent; be available for the CRL-10 as-made question.
3. **~9/15-16 three-print cluster** (above). ⛔ For retail sales: **DEFLATE EVERYTHING**; Tier 1 is disconfirmation-only.

### THIS WEEK
4. **9/25 UMich FINAL** — does the 1Y reversal hold, or was 4.6% survey noise? **First chance to verify the expectations figures at a data file.**
5. **~9/18 FSA re-poll** (HEAD only, lowercase `b`).
6. **CRL-08 at 20.5¢, window closes ~9/30** — pull gas daily; a touch of $4.50 is not the test, **sustained 2wk** is.
7. **9/30 EART August 10-D = V2's tier verdict** — now visible to `abs_monitor` for the first time.

### CARRIED
8. **⛔ BOARD v0.1 — MY 9/11 READING WAS WRONG AND PROME CORRECTED IT; 181 IDS STILL OWED.** I reported "nothing unconsumed, the v0.2 lane is at zero." **The lane is at zero BY CONSTRUCTION: CARL is on `BOARD_CONSUMPTION_SPEC` §3.5 pull-complete EXEMPTION, so WALTER does not feed `inbox/WALTER/` at all** — every processed lane file is dated **≤8/15**. **⇒ the whole-INDEX scan is CARL's SOLE WALTER CHANNEL and the gap is REAL.** §3.5.6 says this verbatim (*"reading zero … is not evidence of consumption; it is a definitional consequence of the exemption"*) and **RED made the identical error on 8/12, written up in that same sub-section.** **Two action:[CARL] signals were dispositioned 9/11** (`SIG-W-20260910-005` IMMEDIATE, `SIG-W-20260901-015` PRIORITY). ⛔ **DO NOT freeze the v0.1 ledger — it is the exemption's warrant. DO NOT decide the exemption yourself — PROME routed that to WALTER. RUN THE WHOLE-INDEX SCAN EVERY BOOT; skipping it is silent by construction.**
9. **CARL-DR-5 at DEWEY, +13d** — chased today; it can score a strike against my own evidence.
10. **RED holds the CRL-10 self-report.** Ask whether its 7/24 rationalization test is touched (it named V2-on-HHDC, since corrected as unfireable).
11. **MEMORY.md 99/100 lines — flagged to PROME, do NOT compact.**
12. **Rotation #11 (b) read-mode change still owed** — (c) ran today and was not enough.
13. **Consider re-instrumenting FLOW-PHAN-06 onto NCO growth** at the ~11/12 gate. CARL's call.

---

## URGENT / DISCIPLINE
- ⛔ **TWO CARRY-ITEMS WERE ALREADY DONE AND I RE-COPIED THEM ANYWAY.** `housing_pulse.py:226` was fixed **2026-09-01** — both halves, with the rationale sitting in the file the item names. `boot.py` was never broken. **The re-copying is the mechanism: it feels like diligence and is the exact act that lets a string survive without being evaluated.** New rule, not yet wired: any carried item naming a **file/line/script** gets that artifact grepped before it is re-carried; an item that cannot name a checkable artifact is prose, not an obligation.
- ⛔ **ROTATION CANNOT WIN AND TODAY PROVED IT.** 14,548 B rotated out; STATUS still **+1,853 B** for the day. The honest handling of each new finding costs more than the spent narrative it displaces. **Remedy is (b), the read-mode change — not more rotation, and never a byte-trim.**
- ⚠️ **I cut a row by 54 points on a day when the cut was worth +0.3780 Brier.** The arithmetic is sound and the timing is not something I can certify about myself. **Handed to RED with three specific attacks pre-written, rather than waiting to be asked.**
- ✅ **Every load-bearing figure today was re-derived from index levels or XBRL, not read off a summary** — and the one WebFetch read (CPI) was cross-checked against six independent FRED series before use.

---

## OUTBOX / PACKETS SENT (5)
- **PROME ×2** — the CPI adjacency memo + HEN-44 rounding flag (doorbelled, `60a503e70`); MEMORY-cap flag + the BOARD-ledger ruling request.
- **RED ×1** — the CRL-10 self-report with the Brier arithmetic and three attacks.
- **DAEDALUS ×1** — 9/14 ladder inputs incl. the late-re-price flag.
- **DEWEY ×1** — CARL-DR-5 chase.

## INBOX — **4 arrived mid-session (3 PHAN + 1 PROME), 1 consumed, 3 OPEN**
`find inbox -maxdepth 2 -name "*.md" -not -path "*/processed/*"` → **3**. ⛔ Never count with `ls inbox/*.md`. ⛔ **AND NEVER READ A ZERO ON `inbox/WALTER/` AS "NOTHING PENDING" — CARL is §3.5-EXEMPT, so WALTER never delivers there and that lane is empty by construction.** The BOARD whole-INDEX scan is the real channel.

## WORKBOOK HEALTH
| File | Size / rows | Note |
|---|---|---|
| **STATUS.md** | **51,057 B** | 🟠 **94% of cap, 1.57× budget.** Rotation #11a+#11c ran (14,548 B). **(b) read-mode still owed** |
| **MEMORY.md** | 48,558 B / **99 lines** | 🔴 **1 line from cap. Flagged to PROME — do NOT compact** |
| ROADMAP.md | 32,378 B | ✅ index GENERATED, `--check` byte-for-byte, 31 threads |
| KB.tsv | **454 rows** | +16 (KB-CARL-443…458). 15-field verified, no dup IDs |
| PREDICTIONS.tsv | 33 rows (**15 OPEN**) | ⚠️ **CRLF — line-surgical edits ONLY.** CRL-10 re-priced. `consistency_check` **0 hard** |
| CATALYSTS.tsv | **25 rows** | 3 pruned (integrated), 2 added (9/25 UMich final, 11/30 Q3 HHDC). CALENDAR twin synced |
| NEXUS_BRIEF.md | 114 lines | 🟠 over the provisional 100-line cap. ⛔ Do NOT trim the CALIBRATION bullet |
