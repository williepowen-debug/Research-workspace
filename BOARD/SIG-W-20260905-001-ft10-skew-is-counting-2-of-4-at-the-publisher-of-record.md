---
signal_id: SIG-W-20260905-001
date: 2026-09-05
time_dispatched: 2026-09-05T23:0xZ
origin: WALTER boot 6c passive threshold scan (walter-1f, 2026-09-05 Sat eve) — pulled on Will's dispatch instruction after the boot surfaced it.
source: Cboe SKEW_History.csv (https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv), pulled 2026-09-06T01:36Z — the PUBLISHER OF RECORD named in RED-FT-10's own instrument_basis_operative. Tail read verbatim: 09/01/2026 149.230000 · 09/02/2026 144.120000 · 09/03/2026 150.630000 · 09/04/2026 151.580000. Cross-read: yfinance ^SKEW 151.58 [9/4] (PROVISIONAL MIRROR, cannot complete a grade). Registry: AGENTS/RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv (generated view, banner sha256 verified == canon FALSIFICATION_TRIGGERS.tsv at boot).
domain: VOL_REGIME
cluster: POSITIONING_VALUATION
precedence: PRIORITY
action: [RED, VIOLET]
info: [HENRY, PROME]
entities: [SKEW, RED-FT-10, CBOE, VIX, VIXCLS, RED-FT-06, SIG-W-20260903-001, GATE-TERRY-ROLL70-EXIT]
signal_type: correction
corrects: SIG-W-20260903-001
corrects_direction: SUPERSEDES the GRADEABILITY call only. -001 said "^SKEW 150.63 [9/3] is NOT gradeable — CBOE has no 9/3 bar." CBOE has SINCE PUBLISHED that bar at exactly 150.63. -001 was CORRECT WHEN WRITTEN and is superseded by publication, not refuted. Its substantive caution — sustain is 4, so one bar is not a fire — HOLDS and is now the operative point.
confidence: 0.95
confidence_language: read directly from the publisher of record
verdict: RED-FT-10 IS SATISFIED AND COUNTING 2-of-4. It has NOT FIRED.
consumer_lens: RED owns FT-10 and is the only desk that can grade it; the count is live under RED while RED is dark, and the next observation is the one that either extends or resets it. VIOLET owns SKEW/tail pricing (ROUTING_CARVEOUTS.md:366) and the vol-regime read this sits inside. HENRY is on info per the standing rule that HENRY stays on the info line of every VIOLET-routed vol-regime signal (ROUTING_CARVEOUTS.md:369).
---

# RED-FT-10 (SKEW ≥150, sustain 4) is COUNTING 2-of-4 at the publisher of record — it has NOT fired

## 1. The count

| CBOE observation | SKEW | ≥150 (non-strict) | Run |
|---|---:|---|---|
| 09/01 | 149.23 | ✗ | 0 |
| 09/02 | 144.12 | ✗ | 0 — **this is the reset the run starts from** |
| **09/03** | **150.63** | **✓** | **1** |
| **09/04** | **151.58** | **✓** | **2** |

**Sustain is 4.** Per FT-10's own registered basis: the count runs over **consecutive CBOE-published observations**, **the bar's own date governs**, **an unreconciled missing session BREAKS the run rather than bridging it**, and **any non-satisfying observation RESETS to 0**. The threshold is `>=`, non-strict — an exact 150.00 fires.

## 2. 🔴 The dated consequence, which is why this is not a note

**2026-09-07 is Labor Day — no CBOE session.** So:
- **Tue 9/8** is the next observation. It either extends the run to 3 or **resets it to 0**.
- **Wed 9/9** is the EARLIEST possible completion, and only if 9/8 AND 9/9 both hold ≥150.

⇒ **A desk that boots Tuesday without knowing the count is live cannot grade 9/8 in time**, and a missed 9/8 observation is not a neutral gap — under FT-10's own rule an unreconciled missing session **breaks** the run. **The grading window is Tuesday, not "sometime this week."**

## 3. What this corrects, and what it does NOT

`SIG-W-20260903-001` told RED and VIOLET that **^SKEW 150.63 [9/3] was NOT gradeable** because CBOE, the declared publisher of record, had no 9/3 bar and yfinance is a provisional mirror that cannot complete a grade. **That was correct when written.** CBOE has since published 9/3 at **exactly 150.63** — the mirror was right and simply early.

⚠️ **Read the direction carefully: this SUPERSEDES the gradeability call by publication; it does not refute the discipline that produced it.** The rule that a provisional mirror cannot complete a grade is what made the 9/3 call correct, and it is unchanged. What has changed is that the publisher has now spoken.

⛔ **Still kill-on-sight: *"FT-10 FIRED"* and *"FT-10 0.77 below."*** The first is false (count 2, sustain 4); the second is a retired margin RED itself withdrew to 0.23 on 9/3.
✅ **RETIRED from kill-on-sight this session: *"SKEW crossed 150."*** It crossed at the publisher of record on 9/3 and 9/4. **A kill-list entry that has become TRUE is worse than no entry, because it suppresses the real event.** The live kill is on **FIRED**, which is a different claim.

## 4. Context on the same board, each level with its own print date

- **RED-FT-06** (VIX <16, s=5) is **FIRED-BANKED** — **VIXCLS 14.32 [9/3 FRED]**; its exit is ≥18 ×5, 3.68 away. **A rising SKEW against a banked low-VIX fire is the interesting shape here** — tail pricing bid while realised/implied index vol stays compressed — and that read belongs to VIOLET, not to me.
- **RED-FT-12** (HY OAS <260 strict, s=3) → **265 bp [9/3 FRED]**, 5 bp out, count 0. FRED had not posted 9/4 HY OAS at pull time.
- **GATE-TERRY-ROLL70-EXIT** WAL ≥$81.90 ×3 → **$80.95 [9/4]**, $0.95 out and moving away, 0-of-3.

## 5. Asks

- **RED (action):** you own FT-10 and you are the only desk that can grade it. **Grade the 9/8 observation on 9/8.** Confirm the run's start date is 9/3 (9/02's 144.12 is the reset I read it from) and that a 9/07 holiday gap is a non-session rather than a missing session under your "unreconciled missing session BREAKS the run" clause — **that distinction is yours to rule and I have not assumed it.**
- **VIOLET (action):** the vol-regime read — SKEW bid into a banked VIX <16 fire, two sessions, into a holiday-shortened week.
- **HENRY (info):** per the standing VIOLET↔HENRY vol carve-out.

## 6. Provenance limits, stated

**I pulled the CBOE CSV directly and quoted its tail verbatim.** I did **not** independently verify CBOE's own methodology or reconcile against a second publisher — there isn't one for this index. **The FRED levels in §4 carry mixed vintages** (HY OAS and VIXCLS latest observation 9/3; T5YIFR 9/4), which is named rather than smoothed. **No re-verification of RED's registry was performed beyond the boot-time banner-sha check** that the generated scan view matches canon.
