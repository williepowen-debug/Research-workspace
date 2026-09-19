# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** session 27 — opened **2026-09-19 ~11:38 ET**, Will-directed catch-up ("focus on getting caught up on anything owed, stale"), worked the owed list top-down. Closed ~13:0x ET.

## CHANGES SINCE (session 26 → 27) — 2 days
- **Nothing moved against MARCO while dark.** 3 inbound items arrived (LABOR 9/17 FL claims, ZHAO 9/18 self-corrected China PPI, WALTER lane SIG-W-20260917-008 Section-301 delay) — **none processed; MARCO was not spawned for inbox and the WALTER item is INFO-only with ZHAO owning the action.**
- **SAM had 12 uncommitted files outside my directory all session ⇒ NO PULL was taken** (root §Before-pulling step 2). All work is on `e4661eeb1`.

## WHAT I DID (session 27) — the three dated resolvers, then four owed pulls

### 1. Dated/mechanical resolvers — all graded on rules written before the numbers
- **`ES-MARCO-05` → DID_NOT_APPEAR.** Aug fresh F&V **+3.13% YoY** (`CUUR0000SAF1131`=413.359), 3rd consecutive sub-6%, ~6.9pp from the >10% threshold, **robust to basis** (2-yr stack +5.50%). Both pre-registered readings agree ⇒ no discretion. **Base-effect recorded:** the YoY fade is substantially a 2025 base effect (Aug-25 +1.68% MoM) while the 2-yr stack barely moved. **Counter-print logged not buried:** Aug gasoline **+2.53% MoM** while produce **fell** −0.65% — first divergence from the co-movement `ES-MARCO-08` resolved on. Does NOT re-open a resolved signal. **MAR-14 20%→12%.**
- **`MAR-11` → PUSHED to the OFLC Q4 disclosure (~Nov), confidence HELD 72%.** Live check: newest file is still `FY2026_Q3`; FY26-thru-Q3 **349,867**, identical to 8/21. **9/30 is the EVENT anchor, not the resolver** — grading there would grade Q3 data. Not re-rated **because no new data arrived**.
- **`MAR-24` → 55%→70% on a COMPUTED conditional base rate.** June is the **first all-3-negative month of 2026** (FLL −13.22 / MCO −7.27 / MIA −5.48) but **is Q2 and does not resolve the row**. P(≥1 all-3-neg in next 3 │ this month all-3-neg) = **9/16 = 56.2%** ex-COVID vs 14.2% unconditional; structurally FLL needs +15.2% and MCO +7.8% to flip positive ⇒ **MIA is the sole swing leg** (30% of Q3 months negative). ⛔ **Ex-Spirit FLL +22.28% / MCO +4.52% — if it fires it fires on a BANKRUPTCY.** Spec addition pre-registered: **grade on REVISED BTS data or state the vintage** (first-print bias 0.8–2.3pp toward negative).
- **`MAR-22` was ALREADY RESOLVED 8/21** and was still sitting in STATUS's **ACTIVE** predictions table — removed. Ledger right, narrative wrong.

### 2. Banxico July (CE81) — 1 of 2 clean forward prints
Value $5,570.6M +3.00%; **count 13,081.6k −0.02% YoY**; avg **$426**. **The band flip is 3,021 operations out of 13.08M, and June's own count revised by 6,600 between pulls — twice the margin.** Graded CRITICAL on the letter, recorded as noise; **0%-boundary spec defect registered.** Real signal = **2-yr stack −6.76%, a 4-month run ≤−5%, longest since 2010** (≤−5% = **10.6% of 235 months**). **Apr/May/Jun are IN-SAMPLE** (re-spec written 8/11); **July is the first out-of-sample print and it MEETS; August ~Oct 1 is the second.** Multi-causal check **NOT passed** — avg transfer broke $390/$393/$390 → **$408**, so consolidation explains it equally.

### 3. StatCan August — ID-01's noise floor is measured too low
Total return trips **2,574,637; 2-yr stack −26.63%** — BREACHED 10th straight month, **shallowest since Nov-2025**; air **−22.67%** (YoY **+3.61%, first positive**), land-auto −27.39%. **Level breached, trend RECOVERING.** **`VX-1.01` basis corrected** — it was reading the air+auto TOTAL level against the AUTO-leg stack.
⛔ **`ID-01`: the 2.5pp floor came from ONE observation.** Over 11 pre-tariff transitions the gap moves **mean 4.21pp / max 7.95pp; 82% clear 2.5pp, 45% clear it in ID-01's direction.** FP by reading: **either-month 45% · cumulative 30% · both-months 10%.** **Both-months reading PRE-COMMITTED 9/19, before the window opens; PROME packeted + doorbelled.**

### 4. NTTO — two instruments unblocked by one fetch
**`ES-MARCO-09` → APPEARED**: Jun+Jul **5,837,141 vs 7,485,330 (2019) = −22.02%**. Volume leg PASSED, vs-2019 leg FAILED, ≥−20% FAIL band MET — **exactly the split pre-registered 8/21**. **`VX-1.02` UNSCORED → CRITICAL** (Aug **−24.20%**, YTD −20.73%; same band either way). Shortfall **WIDENING**: −16.5% Jan → −24.2% Aug.
⛔ **The named resolver was fictional — the workbook has NO vs-2019 column** (35 sheets checked); replaced with primary-to-primary arithmetic. It had been logged "PRIMARY WORKBOOK NOT READ" for 4 weeks and was one fetch away.

### 5. Instruments built (mechanising what was hand-read)
- **`tools/banxico_monthly.py`** (CE81 monthly) + wired into `boot.py` with a content-derived vintage check, 35-day cadence. **Root cause: the boot step named "Banxico remittances" guarded CE100 — the QUARTERLY state map — on an 85-day cadence.** Guard falsified in 3 directions; from **Oct 2 it flags August automatically**.
- **`tools/statcan_travel.py`** (air 24-10-0056 v1324883057 / land-auto 24-10-0057 v1545883120). **Reproduces all four hand-carried ID-01 baselines within 0.05pp** (`--verify`).

### 6. Read-cap
**STATUS 33,789 → 32,461 B, under the 32,550 budget.** Achieved by **rotation, not rewriting** — 4 new archive files. ⚠️ **Three separate "tighten the prose" attempts each ADDED bytes (+48, +46, +5)**, exactly as `READ_CAP.md` warns.

## NEXT SESSION
0. **🔴 `MEMORY.md` 49,058 B = 151% of the read budget — STILL UNROTATED, 3rd session carried.** It is now the only over-budget boot read. **Rotate before any append** (a MARCO-specific lesson from this session is owed to it and was deliberately NOT written for this reason).
1. **🔴 STATUS needs a HOT/COLD SPLIT, not more shaving.** It spent this session bouncing off the ceiling and landed at 32,461/32,550 — it re-breaches on any edit.
2. **🟠 Banxico AUGUST (~Oct 1) — the SECOND forward print that completes or breaks the SDL-01 re-spec.** Boot now flags it automatically.
3. **🟠 StatCan SEPTEMBER (~mid-Oct) — leg 1 of the ID-01 window, first post-counter-tariff month.** Needs PROME's ruling on the both-months reading first.
4. **🟠 NTTO September (~mid-Oct)** — `VX-1.02` is −24.20% and the BREACHED line is −25%.
5. **🟠 Awaiting CORAL:** refreshed FL Citizens PIF (MARCO's copy is dated 2026-06-30, ~11 weeks old). CORAL was DARK; PROME flagged per messaging rule 6b.
6. ✅ **MAR-24 routing rule — CLOSED 9/19, Will-approved.** Re-specified in `CLAUDE.md`: the all-three trigger fires only **carrier-adjusted** (raw figure reported alongside), **MIA promoted to PRIMARY tell** (verified Spirit-free since Feb-2023), **expiry registered** (docket 2027-08-15 — May-2027 is the first clean YoY). REGINALD + CARL packeted ahead of the trigger. ⏳ **Remaining thread: Spirit's seat deletion is economically real (~84% backfilled at MCO) and is a SUPPLY question MARCO has not sized** — deliberately not folded into a demand signal.
7. **🔴 ENERGY RE-ARM still un-re-specified** (3rd session). Fresh forward window, exchange-suffixed contract (`BZX26.NYM` form). ⚠️ Energy is re-accelerating (Aug gasoline +27.40% YoY) while the instrument sits dead.
8. **🔴 Channel 4 — EMMA/MSRB credit leg STILL UNRUN** (since 8/12); it gates the retire-or-hold ruling.
9. **🟠 Promotion flag owed to PROME:** `finding_threshold_spec_fails_before_world` is COLD-tier and was extended with 2 new instances (n=5) ⇒ promotion flag per the Batch-A rule. Also advisory: that memory's sibling hot hook is 118 chars vs the 80-char canon — **did not edit the shared index myself.**
10. **Carried:** FL-$ hole scope-mismatched — **do not re-cite** · `VX-2.01` BREACHED on an unrefreshed Jun-15 arrest rate · BofA Q1'26 metro claim documented-not-merged · CBP Ch.98/drawback defect · USMCA-preference not primary-supported · `VX.tsv` two-clock banner still 2026-07-02 (correct by rule) · **VX-1.02's band says "vs the same period of 2019" without naming the period — name it forward** (both readings agree today; they would NOT have in April).
11. **Do NOT hunt a fifth Channel-1 transmission instrument.** v3.0 pre-commits against it.

## OPEN THREADS
| Item | Status |
|------|--------|
| ✅ **MAR-24 routing rule** | **CLOSED 9/19** — carrier-adjusted trigger, MIA primary, expiry docketed 2027-08-15, REGINALD/CARL packeted |
| ⏳ **Spirit seat deletion unsized** | Real capacity loss (~84% backfilled at MCO); a SUPPLY thread, deliberately kept out of the demand trigger |
| 🔑 **`ID-01` both-months reading** | Pre-committed 9/19; **awaiting PROME ruling before the Sep print (~mid-Oct)** |
| 🟠 **SDL-01 re-spec: 1 of 2 forward prints** | August (~Oct 1) completes or breaks it |
| 🔴 **`MEMORY.md` 151% of budget** | Unrotated 3 sessions; blocks its own appends |
| 🔴 **STATUS at 99.7% of budget** | Needs a hot/cold split |
| 🔴 **Energy re-arm un-re-specified** | Carried s25→s26→s27 |
| 🔴 **Channel 4 EMMA/MSRB leg unrun** | Gates the retire-or-hold ruling |
| 🟠 **CORAL: Citizens PIF** | Asked 9/19; CORAL dark |
| ✅ **NTTO primary — READ** | Closed. Resolver was fictional; replaced with primary-to-primary |
| ✅ **Canadian + Banxico series — MECHANISED** | Closed. Both reproduce prior hand-reads |

## Mail state
**Inbox 3 UNPROCESSED** (LABOR 9/17 · ZHAO 9/18 · WALTER-lane SIG-W-20260917-008) — **not a backlog failure: MARCO was not spawned for inbox this session.** The WALTER item is INFO-only (ZHAO owns the action). ⚠️ The WALTER lane is normally a boot-time drain — **drain it next boot**.
**Sent:** **PROME** (`PROME/inbox/`, ID-01 noise floor + ASK; doorbelled `prome-73`) · **CORAL** (`AGENTS/CORAL/inbox/`, FL airports ex-Spirit + Citizens PIF ask; CORAL dark, PROME flagged per rule 6b).
**Not sent, deliberately:** nothing to WALTER (analysis, not a signal; no threshold fired). ✅ **REGINALD + CARL WERE sent the airport read 9/19** once the rule was re-specified — ahead of the trigger, not as a correction after it.

## PUSH STATE
Session 27 — see the closeout commits and the `safe-push.sh` receipt line.
