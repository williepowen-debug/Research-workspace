# FIRE CARD — TLT — Duration short / TLT puts (deploy-on-trigger)
**Setup ID:** TRY-FIRE-004 · **Trigger class:** FLOW/VELOCITY discriminator (explicitly NOT the bare level)
**Thesis owner:** BOND (BND-11 / VX-BND-05) + LIQUID (demand-hole workbook, now secondary context post-7/9 re-scope) + SAM/ZHAO (TIC flow) — routed by PROME 2026-07-06 xdomain synthesis. **Primary channel re-scoped 2026-07-09 (Will-ratified) to inflation/term-premium (BOND HEN-40 two-channel frame) — see CHANGELOG.**
**Card pre-built:** 2026-07-09 (spec routed to TERRY inbox 2026-07-06 as a PRE-BUILD task, ID-corrected 2026-07-08; the card file itself was not actually written until this session — flagged as a process gap in the outbox note to PROME)
**Fired:** ____ (fill at fire)
**Status:** PROPOSE-ONLY — Will [Approve] required (rule #5). Confidence: **LOW / contingent** — readiness, not a lean (7/6 xdomain synthesis: "demand-hole convergence" graded MIXED-leaning-refuted, one correlated term-premium root, not independent votes).

**CHANGELOG**
- **2026-07-09 PM patch (red-team F5/F6/F9/F10, Will-approved):** card re-scoped, NOT lapsed, despite BOND's 7/9 30Y-reopen grade (indirect 77.74%, no tail — maximally clean) literally reading as a card-global lapse trigger under the old wording. Fix: (1) F5 — invalidations re-scoped per-arm, card-level lapse now requires ALL THREE arms individually dead; arm-#1 formally DEAD as of 7/9, arm-#2/#3 still live; (2) thesis re-scoped from demand-hole to inflation/term-premium channel (BOND's HEN-40 two-channel frame), consistent with the 7/6 synthesis and 7/9 auction read; (3) F6 — added disarm-dominates-arm precedence + arm latch rule; (4) F9 — pinned arm-#2 five-consecutive-close semantics + reset rule + close source; (5) F10 — arm-#3 respecified to valuation-adjusted TIC transactions (not bare holdings-down, which fires on pure valuation with zero selling).

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (do NOT re-derive at fire)
══════════════════════════════════════════════════════════════
- **Trigger condition (exact):** ARM only on **ANY ONE** of 3 flow/velocity discriminators — **never the bare level** (30Y touching 5.00% alone does not arm this card):
  1. **BND-11 ACUTE at the 7/9 30Y reopen** (BOND grades): indirect (%-of-competitive-accepted) **<52%** AND (**BTC <2.15** OR tail >2bp) AND **dealer >18–20%**. *(BTC threshold reconciled 2026-07-09 per BOND: canonical is <2.15, not the earlier 2.3 — the 2.3 figure was a mis-ported 5Y-auction line.)*
  2. **10Y five consecutive closes ≥4.50** — the 10Y-sustain escalation leg of BOND's **VX-BND-05**. *(ID note: this is NOT "BND-12" — BND-12 is BOND's separate 30Y>5.00-sustain call. Corrected by PROME 2026-07-08, HENRY-flagged.)* **Pinned semantics (2026-07-09 PM patch, F9):** five CONSECUTIVE closes ≥4.50; any close <4.50 resets the count to zero. Close source = Treasury CMT / FRED DGS10 daily. (**BOND CO-RATIFIED 2026-07-10, no dispute + 3 riders:** published 2dp DGS10 value, ≥ inclusive; holidays/non-trading days neither count nor reset; official DGS10 governs retroactively over ^TNX provisionals — memo `AGENTS/BOND/outbox/2026-07-10_to-PROME-TERRY_arm2-semantics-coratification.md`.) **Current count — SUPERSEDED by the 2026-07-16 COMPLETE entry below (5-of-5, official). Historical snapshot (PROME restatement 2026-07-10, FRED-verified): 2-of-5 OFFICIAL** (7/7 close 4.55, 7/8 close **4.56** — the 4.57 previously carried here was a ^TNX read; count-neutral, both ≥4.50) **/ 3-of-5 PROVISIONAL** (7/9 ^TNX 4.539 → **official DGS10 4.54** now posted; R3 retroactive, count-neutral, ≥4.50 — carry 4.54, not 4.539). Fri 7/10 (4.56) + Mon 7/13 (4.62) closes ≥4.50 → **completed 5-of-5 Mon 7/13** (7/14 4.58 = 6 straight; BOND co-graded CONFIRM 7/16). Record confirmed closes in the discriminator log at/after 4PM ET, do not count off intraday.
  3. **Soft May TIC 7/16** (ZHAO/LIQUID/SAM): **respecified 2026-07-09 PM patch, F10** — valuation-adjusted flow, not bare holdings-level (holdings-DOWN can fire on pure valuation: yields up → mark-to-market holdings down with zero actual selling, which is not a flow signal). Arm condition: TIC **net TRANSACTIONS** in long-term Treasuries show China **AND** Japan both net **sellers**, comparison month = April 2026 vs May 2026 transactions data (converts Japan from correlation-amplifier to a real flow-subtractor — PACKET-C flow test). **Fallback if transactions-level granularity is unavailable at the 7/16 release:** do not treat bare holdings-down as sufficient to arm; flag the data-granularity gap to PROME and hold arm-#3 as UNDETERMINED pending a transactions-level read, rather than arming on a valuation-contaminated holdings print.
- **One-line setup:** duration short / TLT puts expressing a duration shock via the **inflation/term-premium channel** (BOND's HEN-40 two-channel frame) — **re-scoped 2026-07-09 PM patch, Will-ratified.** BOND's 7/9 30Y-reopen grade refuted the demand-hole channel at the flow level (indirect 77.74%, no tail, foreign demand surged) while confirming term-premium/inflation-driven duration pressure as the live channel. Arm-#2 (10Y five-close sustain) is this channel's natural discriminator; arm-#3 (TIC transactions) tests the flow-subtractor leg as a secondary, not primary, confirmation.
- **Structure:** TLT puts, **Sep expiry** (captures the 7/9→7/16 window plus buffer), strike ladder **8–12% OTM** — confirm exact strikes at fire against live chain.
- **Why this expression:** the 7/9→7/14 CPI downside is asymmetric with near-zero buffer if a duration shock confirms via the term-premium/inflation channel (hot CPI → 10Y sustains/extends through 4.50 → term premium re-prices) — a convex options structure captures that asymmetry better than outright TLT short. *(Re-scoped 2026-07-09: the original "soft reopen → gap through 4.50" framing was demand-hole-flavored; superseded per the thesis re-scope above.)*
- **Alternatives rejected:** outright TLT short = unbounded + margin; long-dated (2027) puts = wrong tenor for a velocity-window catalyst; arming on the 30Y level alone = the exact mis-read the 7/6 xdomain synthesis warned against (level is one correlated root, not independent confirmation).
- **Max-loss budget:** $500 per card (Will 2026-06-26 standing rule).
- **Invalidation — scoped PER-ARM, not card-global (2026-07-09 PM patch, F5):**
  - **Arm-#1 (BND-11 acute) DISARM:** a **clean 7/9 print** (indirect holds ≥58%, no tail) → **arm-#1 DEAD.** *Fired 7/9: indirect 77.74%, dealer 10.05%, BTC 2.44, no tail — arm-#1 confirmed DEAD (see discriminator log).* Arm-#1-adjacent: 30Y retraces **<5.00%** post-auction reads as the same auction-level signal family and also kills arm-#1 if not already dead.
  - **Arm-#2 (VX-BND-05 10Y-sustain) DISARM:** 10Y mean-reverts **<4.50%** — any close <4.50 resets the consecutive-close count to zero (this IS arm-#2's reset mechanism per F9 above, not a separate condition).
  - **Arm-#3 (soft TIC) DISARM:** 7/16 TIC transactions show China and Japan **not** both net sellers (i.e., flat/net-buyer on either leg) → arm-#3 DEAD.
  - **Card-level lapse:** fires ONLY when **ALL THREE arms are individually DEAD.** As of this patch: arm-#1 DEAD, arm-#2 LIVE WATCH (2-of-5, pending 7/9 close), arm-#3 PENDING (7/16). **Card stays ALIVE, re-scoped — not lapsed.**
- **Kill line:** a scoped arm DISARM kills that arm only; the card lapses only when all three arms are dead (see Invalidation above).
- **Precedence + latch (2026-07-09 PM patch, F6):** within a session, a firing DISARM dominates a firing ARM. An arm, once graded ARMED by PROME+Will, LATCHES until its scoped disarm fires — intraday oscillation does not un-arm.
- **Confirm line:** any ONE live arm discriminator fires; CPI 7/14 hot core (MoM ≥+0.3%) is a compound amplifier on an already-armed card, not itself an arm condition (CPI grade owned by HENRY/CARL/LIQUID).

══════════════════════════════════════════════════════════════
DISCRIMINATOR LOG (dated entries — record, don't re-derive ZONE 1)
══════════════════════════════════════════════════════════════

**2026-07-09 ~14:30 ET — NO-ARM (formal).** Source: BOND adjudication ~14:25 ET on BND-11 (2026-07-09 30Y reopen), PROME primary-verified vs TreasuryDirect API.

| Discriminator | State as of 7/9 | Arm threshold | Met? |
|---|---|---|---|
| #1 BND-11 acute (30Y reopen) | Indirect **77.74%**, dealer **10.05%**, BTC **2.44**, high yield **5.058%**. Foreign demand *surged* — inverse of a demand hole. 7th straight benign auction. | indirect <52% AND (BTC<2.15 OR tail>2bp) AND dealer>18–20% | **NO — every leg failed** |
| #2 VX-BND-05 10Y-sustain (5 closes ≥4.50) | *(Restated 7/10, FRED-verified)* **2-of-5 OFFICIAL** (7/7 4.55, 7/8 **4.56** [DGS10; prior 4.57 was ^TNX, count-neutral]) / 3-of-5 provisional (7/9 — **official DGS10 now = 4.54**, R3 retroactive; ^TNX 4.539 was the provisional). **→ SUPERSEDED: FIRED 5-of-5 7/13, see 7/16 entry above.** | 5 consecutive closes ≥4.50 (BOND co-ratified 7/10 + riders) | ~~Do not count until official close posts~~ → **COMPLETE 7/13 (4.62), 6th straight 7/14 (4.58).** |
| #3 Soft May TIC (7/16) | Not yet released (grades 4PM ET 7/16). | **Net TRANSACTIONS: China AND Japan both net SELLERS, valuation-adjusted Apr→May** (ZONE 1 #3 canonical, F10 — NOT bare holdings-down). | N/A — future date; template staged |

**Verdict: arm-#1 formally NO-ARM today (HIGH confidence per BOND).** Channel context: BOND grades the ~5.05% 30Y level as **oil/term-premium channel (orderly)**, NOT a demand-hole — consistent with the 7/6 synthesis's "one correlated root" read. **arm-#2 is now the live duration channel** pending the 7/9 4PM ET close. **Card stays PRE-BUILT/SHELVED — no trade proposal, no sizing.**

**2026-07-09 PM patch note:** per-arm re-read of the above (F5, see ZONE 1 Invalidation) — the clean 7/9 print (indirect 77.74%, no tail) is arm-#1's DISARM, formally confirming **arm-#1 DEAD**, not a card-global lapse. Card-level lapse requires arm-#2 AND arm-#3 also dead, which they are not (arm-#2 LIVE WATCH 2-of-5 pending close; arm-#3 PENDING 7/16). **Card stays ALIVE, re-scoped — PRE-BUILT/SHELVED status is about trade-readiness (no arm yet fired), not about the card being lapsed/dead.**

**2026-07-16 ~09:35 ET — ARM-#2 FIRED → CARD ARMED (arm packet built for Will [Approve]).** Source: FRED DGS10 direct pull, TERRY-verified this session (independent of PROME's boot pull). Fleet was offline 7/13–7/15 (usage limits); arm-#2 completed during the gap and is caught + actioned same-session per the fire-ledger rule.

| Discriminator | State as of 7/16 | Arm threshold | Met? |
|---|---|---|---|
| #1 BND-11 acute (30Y reopen) | DEAD since 7/9 (indirect 77.74%, no tail). | — | **DEAD (unchanged)** |
| #2 VX-BND-05 10Y-sustain | **5-of-5 COMPLETE Mon 7/13** — official DGS10: 7/7 4.55 · 7/8 4.56 · 7/9 4.54 · 7/10 4.56 · **7/13 4.62** · 7/14 4.58 (streak intact, count 6; no <4.50 close = no disarm). | 5 consecutive closes ≥4.50 | **YES — FIRED, HIGH confidence** |
| #3 Soft May TIC (7/16) | Releases **today 4:00 PM ET**; grading template pre-staged. Per F10: net TRANSACTIONS (China AND Japan both net sellers, Apr vs May), NOT bare holdings-down. | China AND Japan both net sellers (transactions) | **PENDING — grades today PM** |

**Verdict: arm-#2 FIRED → card ARMED.** Registered consequence executed: arm packet → `AGENTS/TERRY/outbox/2026-07-16_to-PROME_try-fire-004-arm-packet.md` → Will [Approve] + live broker book. **Terry fill-verdict = CONDITIONAL** (armed as registered, not a chase-now rec): live option marks were unavailable at 09:32 ET (bid/ask 0.00, stale 7/15 last-trades, broken IV) → live re-pull required (rule #4); TLT is RED and at range lows → today's open is a rule-#6 chase, prefer a green-day/scaled fill. Context: June CPI 7/14 cool (−0.42% MoM headline) yet 10Y held the line = term-premium channel confirmed; MOVE round-tripped (spiked **77.77 Mon 7/13** — investing.com daily, same day as the 5-of-5 completion — → 75.03 [7/14] → 68.48 [7/15]); July CPI (mid-Aug) carries the Hormuz/Brent oil shock. **Latch:** arm-#2 is ARMED and latches until a <4.50 close disarms it (F6 precedence rule).

**2026-07-16 grade, logged 2026-07-17 ~09:55 ET — ARM-#3 (May TIC) FIRED **WEAK** → DEEPEN-CONFIRM ONLY. NO NEW TRADE.** Grader: **PROME** (per the 7/16 session-end handoff — TERRY delegated this gate rather than leaving it un-owned; graded against `setups/ARM3-TIC-grading-template_2026-07-16.md` + BOND's CUT-A/CUT-B). Canonical: `PROME/research/2026-07-16_arm3-may-tic-grade.md` (CSLT-sourced, press-notice cross-checked). Routed to `inbox/2026-07-16_from-PROME_may-tic-arm3-grade.md`; consumed this boot.

| Discriminator | State as of 7/17 | Arm threshold | Met? |
|---|---|---|---|
| #1 BND-11 acute (30Y reopen) | DEAD since 7/9. | — | **DEAD (unchanged)** |
| #2 VX-BND-05 10Y-sustain | FIRED 7/13 (5-of-5), latched; no <4.50 close since. | 5 consecutive closes ≥4.50 | **ARMED (latched)** |
| #3 Soft May TIC | May LT net **transactions** (CSLT): China **−$0.129B** · Japan **−$2.838B** — **both net sellers**, Apr→May. Graded on the card's F10 net-TRANSACTIONS wording, NOT the stale GATES "holdings-down" (reconciliation held). | China AND Japan both net sellers (transactions) | **YES — FIRED, but WEAK** |

**Why WEAK, and why it changes nothing:** the sign test passes mechanically, but the **China leg is economically flat** — −$0.129B against a series that routinely swings ±$30B is noise wearing a minus sign. Thin confirmation depth; this is not a strong second arm and must not be cited as one. It **deepen-confirms an already-ARMED card** — it does **not** re-open Will's 7/16 NO-ADD, which stands. **Data-vintage correction:** the actual release was **7/14**, not the 7/16 the docket carried (PROME fixed the vintage). Note the pre-registered expectation was **likely NO-FIRE/UNDETERMINED** (China nowcast UP + Japan buying) — it fired against expectation, which is worth *less* comfort than it sounds precisely because the China leg is flat. **Card state unchanged: ARMED/HOT, $500 banked, no fresh capital.** All three arms now resolved (#1 DEAD · #2 ARMED-latched · #3 FIRED-weak) → card-level lapse (F5: requires all three individually dead) **cannot** fire while #2 latches.

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (fill ONLY at actual fire — rule #4)
══════════════════════════════════════════════════════════════
- **Timestamp (ET):** 2026-07-16 ~09:32–09:35 ET (ARM pull; NOT a fill)
- **Trigger-level confirm:** arm-#2 (10Y 5-close sustain) — DID IT ACTUALLY HIT? **Y** (5-of-5 complete 7/13, FRED-verified §DISCRIMINATOR LOG)
- **Spot(s):** TLT **$83.80** (fetch.py, −0.52% d/d) — as-of 2026-07-16 09:35 ET; 10Y 4.59, 30Y 5.12, MOVE 68.48
- **Green/red day check (rule #6):** **RED day (TLT −0.52%, at range lows) — BREAKING rule #6.** Why noted: arm is a registered consequence firing today; but the FILL should not chase — prefer green-day/scaled entry (see arm packet §7.1). Vol axis partially offsets (MOVE 77→68.48, IV deflating).
- **Chain marks:** FORGE tool could NOT serve live NBBO (0.00 across 3 pulls 09:32/09:45/09:52 — yfinance feed limitation). **Live marks = Will's broker chain, ~10:04 ET, TLT $83.89** (bid/ask): 82 P 0.65/0.67 · 81 P 0.43/0.44 · 80 P 0.28/0.29 · 77 P 0.11/0.12 · 76 P 0.08/0.09 · 75 P 0.06/0.07. Put skew steep (75 P IV 15.55% >> 82 P 11.53%). Full greeks in arm packet §3.
- **Liquidity OK?** YES on all rungs at $500 scale (77 P ask 0.12×1030; 82 P bid 0.65×1394).
- **Broker position truth:** `[POSITION_STATE_UNKNOWN]` — Will confirms no conflicting TLT/duration book (VIO-116 same lane).
- **Sizing (live asks, $500 cap):** outright 77 P → 41 ct/$492 · 76 P → 55/$495 · 75 P → 71/$497. **Grind-spreads:** 82/77 → 8 ct/$448 (7.9×) · **81/76 → 13 ct/$468 (12.9×) [TERRY REC]** · 80/75 → 21 ct/$483 (20.7×). Decisive: at TLT→78 grind, spreads pay 7–9× while outright ladder = $0.

══════════════════════════════════════════════════════════════
ZONE 3 — TRIGGER CONFIRM + DECISION
══════════════════════════════════════════════════════════════
- [x] A discriminator actually fired (arm-#2, 5-of-5 7/13) · [x] Live marks (broker chain 10:04 ET) · [~] Green/red (RED, muted for spread — §7.1)
- [x] Liquidity OK (all rungs) · [x] Max loss ≤ $500 (defined-risk, every variant) · [ ] Position truth (Will confirms)

**Terry verdict (2026-07-16):** flat-book analysis reached CLEAN/REC=81/76 spread — then **position truth (10:09 ET) REVERSED it to book-aware NO ADD** (§9 in arm packet): Will already owns the grind 3 ways (TBT + ITM 85P + 82P ≈$1,150, ~186 sh short-delta, live not stubs), so the spread ≈doubles his short-delta redundantly. Arm-#2 FIRED (5-of-5 7/13); arm-#1 DEAD; arm-#3 grades today 4pm. Card ARMED.
**Decision (WILL, 2026-07-16 ~10:30 ET):** **NO ADD — book-aware rec accepted.** Redundant + deepens a concentrated "Mideast-stays-hot" bet (shared Hormuz-de-escalation falsifier across his rates-short AND oil-long books). **Card stays ARMED; the $500 is BANKED for a re-fire** (arm-#3 4pm, or a red-day/vol-cooldown entry). **Crash-ladder (77/76/75) = approved fallback shape** if a re-fire warrants deploying — the one non-redundant exposure.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
