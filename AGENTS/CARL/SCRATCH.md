# CARL SCRATCH
**Last session:** 2026-08-03 (**Mon** — verified with `date +%A`, not asserted) ~09:45–11:15 ET — **V5 EXECUTION DAY.** The pre-authorization fired: **V5 Gas Squeeze 3→4, convergence 51→52/70 (74%), THESIS v2.6.4.** Also built the Will-ruled inbox layer for all six remaining sub-agents, attempted the Fitch ATR refresh (**no data, 4th month**), checked the HHDC advisory (**still unposted**), and processed both PROME packets.

**PRIORITY-1:** **The vector I promoted this morning is the one most likely to un-promote.** V5 sits at 4 on a pump **9.5¢** above its downgrade line while the crude underneath it fell **17.4% in nine sessions** (Brent $100.19 7/23 → **$82.77 8/3**). The trigger is **already registered** — *AAA <$4.00 **sustained 2 weeks** → V5 −1 immediate (4→3)* — and the 17-18d lag puts arrival **~8/20**. **Pull gas every session and do NOT let a breach sit ungraded; if it breaches, the 2-week sustain clock starts at the breach, not at a session boundary.** Next real catalyst: **HHDC, window 8/4-8/11, advisory STILL UNPOSTED as of 8/3 — check it EVERY boot** (it normally posts 3-5 business days ahead, so the modal has drifted from Tue 8/4 toward **Tue 8/11**). **Fri 8/7 July NFP resolves V16's re-arm.**

---

## CHANGES SINCE LAST SESSION (7/31 eve → 8/3 Mon)
- **Gas HELD the cross** — AAA $4.106 (7/31) → **$4.095 (8/3)**; FRED $4.096 (w/e 7/27). The condition Will pre-authorized against was met, unambiguously, on both instruments.
- **⚠️ CRUDE BROKE UNDERNEATH IT** — WTI **−7.29% to $78.50**, Brent **−8.16% to $82.77** [8/3 live], on an **8/2 de-escalation headline Tehran denied on the record while the tape refused to give it back.** Brent is **−17.4% off its 7/23 peak.** Diesel went the OTHER way — **$5.364, a fresh high** — consistent with the Russia-ban structural leg, not the reversible Hormuz premium.
- **Fitch ATR: still nothing.** Apr/May/Jun/Jul 2026 unpublished for the **4th consecutive month**.
- **HHDC advisory: still not posted.**

## WHAT HAPPENED (this session)
1. **✅ V5 3→4 EXECUTED — the pre-auth's condition verified on its own registered instruments and basis.**
   - AAA daily national regular **$4.095 [8/3 live pull]** ≥ $4.00.
   - FRED GASREGW **$4.001 [w/e 7/20] → $4.096 [w/e 7/27]** = two consecutive weeklies ≥$4.00, rising.
   - **No sub-$4.00 daily reading anywhere in the 7/20→8/3 window** (7/24 $4.105 · 7/31 $4.106 · 8/3 $4.095) → the retrace branch never armed.
   - **Convergence 51 → 52/70 (74%). THESIS v2.6.4.** Five surfaces updated; `consistency_check` Check B **caught that I'd updated STATUS's histogram but not its per-vector matrix row** — fixed, re-run **0 hard**.
2. **⚠️ SPEC COEXISTENCE FOUND AND RECORDED, NOT SILENTLY RESOLVED.** The V5 matrix cell's *own* v2.6 re-arm language named **only** the kinetic path — *"Brent $105-110 + pass-through."* **Brent is $82.77, so on this cell's literal trigger V5 would NOT have re-armed.** The gate that actually fired is the later, dated, explicitly-superseding **7/16-card sustained-cross** path Will ratified 7/31. Both were legitimate routes; the price route was written in Jun-22 when a $4.00 cross looked unreachable. **Graded on the registered instrument and basis, not the narrative.** No trigger was rewritten — a re-arm-**to**-4 rule cannot apply to a vector already at 4.
3. **⛔ Fitch ATR refresh → NO DATA (4th month).** Subscription index; every secondary channel still frozen at March. **Caught a SECOND recirculation trap, a different vintage from the known one:** an apparent "April" reading of **5.23% DQ / ANL 9.48%→7.90% / "all-time-high 6.39% in February"** — the source article's full text says **April 2024 / February 2024** verbatim. The year was stripped in the *snippet*, not the source. **Two stale vintages now impersonate fresh prints on this series; treat any ATR figure without an in-source month AND year as unusable.** KB-375.
4. **📬 INBOX LAYER BUILT — all six remaining sub-agents** (DOC/GIG/PHAN/POLLY/POP/META join STUE), per Will's 8/2 ruling that **overruled** PROME's fan-down recommendation. Each got `inbox/` + `inbox/processed/` + a README on the STUE pattern, **and the scan wired into the boot card as step 0 of `On Session Start`** plus a closeout note — because an inbox nobody reads on a cadence is worse than no inbox.
5. **Both PROME packets processed** (`git mv` → `processed/`). Round-2 residue items all closed — see below.
6. **CRL-28 legs frozen** (residue items 3+4): invalidation leg **41/day ABSOLUTE** (was "1.5× baseline (~41/day)", which re-imported the 41-46 range ambiguity the confirm-leg freeze removed); baseline anchor corrected — **April 30.5/day is the genuine pre-transition top**, not the post-transition, lag-truncated "Jul 1-19 28.4". Neither moves a bar.

## STATUS CHANGES
| Item | Change |
|------|--------|
| **V5 / convergence** | **3→4; 51→52/70 (74%); THESIS v2.6.4** — THESIS header+row+histogram+commentary, STATUS overall+matrix+histogram+total+narrative, CHANGELOG, docket, CALENDAR, NEXUS_BRIEF |
| Gas Pump row | 8/3 figures + the "w/e 8/2"→**w/e 8/3** convention correction (GASREGW is **Monday**-dated) |
| Brent row | **$82.77 (−8.16%), −17.4% off peak**; diesel diverging UP to $5.364 |
| V2 row | ⛔ **instrument-blocked** — 4th month no data + the 2024-vintage trap; OTTO 10-D panel named as the substitute |
| KB | **+3: KB-373** (V5 cross completed) · **KB-374** (crude break → V5 downgrade watch) · **KB-375** (Fitch resolvability defect + trap) |
| docket | 2 fired rows pruned; **+~8/10 Will decision (V2 instrument)** and **+~8/20 V5 downgrade watch**; HHDC row re-framed to modal 8/11; CALENDAR twin synced |
| TEAM.md | new **📬 INBOX LAYER** section (all 7, with the cadence warning on META/POP/PHAN) |

---

## NEXT SESSION SHOULD

### IMMEDIATE
1. **Pull gas FIRST.** `.venv/bin/python3 AGENTS/CARL/scripts/gas_tracker.py`. If AAA < $4.00, **start the 2-week sustain clock at that date and write the date down** — the downgrade is automatic on an already-registered rule, not a judgment call. Cushion at execution was 9.5¢.
2. **Check the HHDC media advisory EVERY boot** (search, don't fetch — newyorkfed.org 403s). Window 8/4-8/11; **modal has drifted to Tue 8/11** because the advisory was still unposted on 8/3. It grades by the **FROZEN card + its 7/31 addenda** — do not edit the card, only dated addenda — with CRL-21's capital riding the cells per Will's standing 7/24 ruling.
3. **Read DEWEY C2 BEFORE the HHDC** (`AGENTS/DEWEY/output/2026-07-24_c2-score-cascade-cc-breach-attribution.md`) — cautions are pre-registered on the card but the full report is still unread. **Carried from 7/31; do not let it slip a third time.**

### DATED
4. **Fri 8/7 July NFP** — V16 re-arm resolver (ARMED since 7/2 on June +57K/−74K).
5. **~8/10 WILL DECISION — re-point V2's instrument** off the blocked Fitch ATR onto **OTTO's 7-deal SEC 10-D panel** (primary, reproducible, already in the STATUS row, and it says the spring trough is over on BOTH tiers). **Surfaced, not taken — it's an instrument change.** Per `finding_audit_resolution_path_before_reattempt`, a 5th month re-attempting the same blocked path is the failure mode, not diligence.
6. **Wed 8/12 July CPI — pre-registered SOFT on gasoline (~−2.6% MoM). DO NOT grade pass-through on it; that's a base effect.** The real test is **9/11 August CPI**.
7. **~8/20 V5 downgrade watch** (item 1) · **~8/5** Treasury Phase 1 verification (STUE) · **~8/14** AFT v. MOHELA free-docket watch · **8/20-21** Affirm FQ4 + Iran waiver expiry (CRL-08 45% live tail) · **~early Sept** CRMT covenant-relief expiry (REGINALD co-owns) · **~9/22** Russia diesel producer-channel read · **9/30** FL $14→$15 statutory step.

### BACKLOG
8. Fix B (consistency_check sub-agent coverage — option 2 leading) · CPI component-vol REBUILD from BLS (SIG-725-016 — cite nothing until rebuilt) · Part D lead verify (DOC/POLLY) · AMCAR Apr-vs-Jun cert pull + abs_monitor **GMCAR label fix** (2 "AmeriCredit" CIKs are GM's PRIME book) · Brier re-run at N≈20 · container-freight AEOLUS reconcile (KB-344) · **DOC `workbook/FLOW.tsv` 53d+ stale — FROZEN-or-refresh at DOC's next spawn** (now on DOC's own card).
9. **DEWEY commissions OUT** (Will-approved 7/31): CARL-DR-1 recognition-artifact census ~8/18 · DR-2 charged-off-borrower destination ~8/25 · DR-3 AZO/ORLY cross-section ~8/28. On delivery, honor the pre-registered KILL conditions as prominently as confirms; **DR-1 must not touch the frozen HHDC card.**

---

## OUTBOX (1 new)
- `2026-08-03_to-PROME_route-to-OTTO-originate-to-degrade-vs-mix-discriminator-spec.md` — **the joint item, routed via PROME, NOT sent to OTTO directly.** Specifies exactly what I need from OTTO's collateral half to separate **originate-to-degrade (🔴 thesis-confirming)** from **mix shift (🟡 much weaker)**: within-stratum vintage curves at matched seasoning, the tier-weight series, and WA LTV/term/APR by vintage. *(6 stale Apr-17 signals still deferred per the messaging overhaul.)*

## INBOX (0 unprocessed — both PROME packets drained to `processed/`)

---

## WORKBOOK HEALTH
| File | Size | Note |
|---|---|---|
| STATUS.md | 248 | at cap (250) — **trim next session before adding rows** |
| KB.tsv | 372 | +3 (KB-373/374/375) |
| PREDICTIONS.tsv | 29 | 16 OPEN; CRL-28 both legs now frozen absolute |
| CATALYSTS.tsv | 20 | 2 pruned, 2 added; CALENDAR twin synced |
| BOARD_LOG.tsv | 651 | **not dispositioned this session — BOARD diff not run** (V5 execution took priority; run at next boot) |
| NEXUS_BRIEF.md | 94 | under the 100 provisional cap |
| MEMORY.md | 71→~76 | under 100 cap |

---

## URGENT
- **V5-at-4 IS PROVISIONAL BY CONSTRUCTION.** Promoted 8/3 on a 9.5¢ cushion; crude −17.4% off peak; lag-implied pump arrival **~8/20**. The downgrade rule is already on the books — **the failure mode is not noticing the breach, not deciding what to do about it.**
- **52/70 IS ONE-SIDED BY DEFAULT, NOT BY JUDGMENT.** The consumer-credit DOWN candidate is **ARMED and unfired only because both its instruments no-showed** (Fitch unpublished 4th month; HHDC unreleased). **Do not present 52 to anyone as a net read of the cycle** — the down-leg is pending, not refuted.
- **Two stale Fitch vintages now impersonate fresh prints** (Jan/Feb-2026 as undated "worst in 32 years"; and a 2024 article as "April"). **No month+year in-source ⇒ unusable.**
- **The frozen HHDC card + 7/31 addenda govern the grade — do not edit the card, only dated addenda.** RED's rationalization test is live on it.
- **"CRMT defaulted" is retired language** — covenant waiver, ~Sept expiry. **Do not carry "GSE MF improving" as clean** — recognition artifact (KB-302).
- **`git pull` was correctly DECLINED this session** — PROME/TERRY/SAM/OTTO hold uncommitted work outside my dir. My commits are local; **PROME owns the push train.**
