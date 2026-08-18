# FIRE CARD — TLT — Duration short / TLT puts (deploy-on-trigger)
**Setup ID:** TRY-FIRE-004 · **Trigger class:** FLOW/VELOCITY discriminator (explicitly NOT the bare level)
**Thesis owner:** BOND (BND-11 / VX-BND-05) + LIQUID (demand-hole workbook, now secondary context post-7/9 re-scope) + SAM/ZHAO (TIC flow) — routed by PROME 2026-07-06 xdomain synthesis. **Primary channel re-scoped 2026-07-09 (Will-ratified) to inflation/term-premium (BOND HEN-40 two-channel frame) — see CHANGELOG.**
**Card pre-built:** 2026-07-09 (spec routed to TERRY inbox 2026-07-06 as a PRE-BUILD task, ID-corrected 2026-07-08; the card file itself was not actually written until this session — flagged as a process gap in the outbox note to PROME)
**Fired:** ~~____ (fill at fire)~~ → ✅ **2026-07-20 ~09:50 ET — 30× TLT Sep-30-26 77P @ $0.11** ($330 at risk, basis **$0.11563** fees-in). **Will sold 5 at 3.23× on 7/31; 25 remain.**
**Terry verdict:** 🟢 **FIRED / ACTIVE — this is the desk's ONE live position.** *(Current, as of 2026-08-04. The dated `CONDITIONAL` verdict below is the **2026-07-17 pre-fire** reasoning and is preserved as history — do not read it as current.)* **Management is pre-registered and unchanged: harvest ≥3× ($0.33) → take half · disarm on an official DGS10 close <4.50 · defined-risk, no stop.** ⚠️ **The ≥3× harvest still owes 10 contracts — the 7/31 sale did NOT consume it** (ruled 8/3). **Mark is a MOMENT property** (`RISK_RULES` #14) — pull it live, never read one off this card.
**Status:** ~~PROPOSE-ONLY — Will [Approve] required (rule #5)~~ → **FIRED/ACTIVE since 2026-07-20.** *Historical pre-fire framing follows:* Confidence: **LOW / contingent** — readiness, not a lean (7/6 xdomain synthesis: "demand-hole convergence" graded MIXED-leaning-refuted, one correlated term-premium root, not independent votes).

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

**Verdict (2026-07-16): arm-#2 FIRED → ~~card ARMED~~ → card FIRED/ACTIVE 2026-07-20.** *(ARMED was correct on 7/16; the card fired four days later. Superseded inline so this dated arm-verdict is not read as the card's current state — it was, until 8/4.)* Registered consequence executed: arm packet → `AGENTS/TERRY/outbox/delivered/2026-07-16_to-PROME_try-fire-004-arm-packet.md` → Will [Approve] + live broker book. **Terry fill-verdict = CONDITIONAL** (armed as registered, not a chase-now rec): live option marks were unavailable at 09:32 ET (bid/ask 0.00, stale 7/15 last-trades, broken IV) → live re-pull required (rule #4); TLT is RED and at range lows → today's open is a rule-#6 chase, prefer a green-day/scaled fill. Context: June CPI 7/14 cool (−0.42% MoM headline) yet 10Y held the line = term-premium channel confirmed; MOVE round-tripped (spiked **77.77 Mon 7/13** — investing.com daily, same day as the 5-of-5 completion — → 75.03 [7/14] → 68.48 [7/15]); July CPI (mid-Aug) carries the Hormuz/Brent oil shock. **Latch:** arm-#2 is ARMED and latches until a <4.50 close disarms it (F6 precedence rule).

**2026-07-16 grade, logged 2026-07-17 ~09:55 ET — ARM-#3 (May TIC) FIRED **WEAK** → DEEPEN-CONFIRM ONLY. NO NEW TRADE.** Grader: **PROME** (per the 7/16 session-end handoff — TERRY delegated this gate rather than leaving it un-owned; graded against `setups/_archive/ARM3-TIC-grading-template_2026-07-16.md` + BOND's CUT-A/CUT-B). Canonical: `PROME/research/2026-07-16_arm3-may-tic-grade.md` (CSLT-sourced, press-notice cross-checked). Routed to `inbox/2026-07-16_from-PROME_may-tic-arm3-grade.md`; consumed this boot.

| Discriminator | State as of 7/17 | Arm threshold | Met? |
|---|---|---|---|
| #1 BND-11 acute (30Y reopen) | DEAD since 7/9. | — | **DEAD (unchanged)** |
| #2 VX-BND-05 10Y-sustain | FIRED 7/13 (5-of-5), latched; no <4.50 close since. | 5 consecutive closes ≥4.50 | **ARMED (latched)** |
| #3 Soft May TIC | May LT net **transactions** (CSLT): China **−$0.129B** · Japan **−$2.838B** — **both net sellers**, Apr→May. Graded on the card's F10 net-TRANSACTIONS wording, NOT the stale GATES "holdings-down" (reconciliation held). | China AND Japan both net sellers (transactions) | **YES — FIRED, but WEAK** |

**Why WEAK, and why it changes nothing:** the sign test passes mechanically, but the **China leg is economically flat** — −$0.129B against a series that routinely swings ±$30B is noise wearing a minus sign. Thin confirmation depth; this is not a strong second arm and must not be cited as one. It **deepen-confirms an already-ARMED card** — it does **not** re-open Will's 7/16 NO-ADD, which stands. **Data-vintage correction:** the actual release was **7/14**, not the 7/16 the docket carried (PROME fixed the vintage). Note the pre-registered expectation was **likely NO-FIRE/UNDETERMINED** (China nowcast UP + Japan buying) — it fired against expectation, which is worth *less* comfort than it sounds precisely because the China leg is flat. **Card state unchanged: ARMED/HOT, $500 banked, no fresh capital.** All three arms now resolved (#1 DEAD · #2 ARMED-latched · #3 FIRED-weak) → card-level lapse (F5: requires all three individually dead) **cannot** fire while #2 latches.

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (fill ONLY at actual fire — rule #4)
══════════════════════════════════════════════════════════════

### ★ RE-FIRE MARKS — 2026-07-17 ~16:00 ET (crash-tail 77P; the $500-banked re-fire question)
- **Timestamp (ET):** 2026-07-17 ~16:00 ET (TERRY live pull — re-fire entry marks, NOT a new arm).
- **Trigger-level confirm:** this is a **RE-FIRE on ENTRY QUALITY, not a new arm.** arm-#2 remains **ARMED/latched** — official DGS10 closes all ≥4.50 (7/13 4.62 · 7/14 4.58 · 7/15 4.55), **no <4.50 close = no disarm**; live 10Y **4.54** [^TNX]. **No FRESH discriminator fired today** — arms all resolved (#1 DEAD · #2 latched · #3 fired-weak 7/16). The case for acting today is a cleaner *entry*, not new information.
- **Spot(s):** TLT **$84.51/$84.52 (+0.36%)** [fetch.py + chain_fetch, 16:00 ET] · 10Y **4.54%** · TBT **$36.35** (−0.85%) · context: **HY OAS 271** [7/16, FRED] (9bp under 001's 280 line, flat on the week).
- **Green/red day check (rule #6):** **GREEN day (TLT +0.36%) → rule-#6 CLEAN** (puts on green). This is the material change vs 7/16, when TLT was **RED at range lows** and the fill would have been a rule-#6 chase. Vol also cooled: 77P IV **12.79%** (vs 75P IV 15.55 on 7/16 → 13.97 now; MOVE round-tripped) — the tail is marginally cheaper on vol.
- **Chain marks (TLT Sep-30 puts, live 16:00 ET, spot $84.52):**
  | Strike | Mny% | Bid/Ask | Mark | IV% | OI | Spread% |
  |---|---|---|---|---|---|---|
  | **77 P** | −8.9 | 0.10 / **0.11** | 0.11 | 12.79 | 657 | 9.5 |
  | 76 P | −10.1 | 0.07 / 0.08 | 0.08 | 13.38 | 715 | 13 |
  | 75 P | −11.3 | 0.05 / 0.06 | 0.06 | 13.97 | 2199 | 18 |
- **Liquidity OK?** YES — all three rungs fine at $500 scale; 77P is cleanest (tightest spread, deep-dated OI 657).
- **Broker position truth:** *(from 7/17 ~12:30 ET snapshot — dated context copy, CONFIRM live at fire)* Will owns the **grind** three ways — TLT 85P Sep-30, TLT 82P Oct-16, TBT 14sh (≈$1,009 mkt) — but does **NOT** own the 77/76/75 crash-tail. **The 77P is net-new and non-redundant** (this is exactly the "one gap" the 7/16 NO-ADD carved out).
- **Sizing (live asks, $500 cap):** **77P → 45 ct = $495** · 76P → 62 ct = $496 · 75P → 83 ct = $498. Approved fallback shape = 77/76/75 ladder; **77P standalone is the cleanest single expression.**
- **Stress (77P × 45 ct, $495 risk, Sep-30 terminal intrinsic):** TLT 77 (ATM) / 80 / unch → **−$495 (−100%)** · BE **76.89 (−9.0%)** · TLT 75 → **+$8,505 (~18×)** · 73 → **~36×** · 70 → **~63×**. Two correctors: **(a)** a *fast* shock pays MORE than terminal intrinsic (IV expands + residual theta — TLT→78 could mark ~3–4× at $0 intrinsic); **(b)** the **grind pays ZERO** — strike sits ~1.6σ out (IV-implied P(ITM) ~6–8%), so this is a **fast-duration-shock instrument only**, correct for the tail role (Will owns the grind already).

### (7/16 ARM-pull — historical record, do not re-mark)
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

### ★ RE-FIRE DECISION — 2026-07-17 (crash-tail 77P, $500 banked)
- [x] Card ARMED (arm-#2 latched, no disarm) — **but NO fresh discriminator today** (re-fire is on entry quality, not new info)
- [x] Live marks pulled (TLT chain + spot, 16:00 ET, <15 min old)
- [x] **Green/red rule SATISFIED** — GREEN TLT day = puts-on-green, rule-#6 clean (the fix for 7/16's red-day chase)
- [x] Liquidity acceptable (all rungs) · [x] Max loss = $495 ≤ $500 (defined-risk) · [x] Vol cooled (77P IV 12.79 vs 7/16 tail 15.55)
- [~] Position truth = 7/17 12:30 snapshot (Will owns grind, NOT the 77 tail → **77P non-redundant**); confirm live at fire
- [x] §9 concentration: deepens the Hormuz-shared cluster, BUT the 77P leans on the **real-yield channel that survives a de-escalation** (the durable leg)

**Terry verdict (2026-07-17): CONDITIONAL — CLEAN structure + CLEANEST entry window since arm, GATED on Will's re-fire appetite.** What improved vs the 7/16 NO-ADD: rule-#6-clean entry (green vs red-day chase), vol cooled ~2 IV pts, and the 77P is specifically the **non-redundant "one gap"** the NO-ADD itself carved out — so proposing it is consistent with that decision, not a reversal. What did NOT change: no fresh discriminator fired today (better entry ≠ new information), and it deepens the same concentrated Mideast-shared-falsifier book.

**★ BOND shock-probability read (2026-07-17 ~16:00 ET, via TERRY-spawned read-only proxy — pending real-BOND ratification, routed to BOND inbox):**
- **P(TLT<77 by 9/30) ≈ 9–13% (pt ~11%) vs ~7% implied → FATTER, mildly.** P(TLT<75) ≈ 4–6% (thin). Live levels: 30Y 5.06, DFII10 real **2.36 [7/13] series high** (14bp from the 2.5 re-arm) backing to 2.32, breakevens anchored 2.22, MOVE ~68 compressing.
- **WHY FATTER:** IV 12.79% / MOVE ~68 is *cheap* because realized vol just compressed on the 4.62→4.54 round-trip — so backward-looking IV **underweights the dated forward catalysts**: hot July CPI 8/13 (Hormuz/Brent pass-through, +0.4–0.6pp headline) + the **auction gauntlet (20Y 7/22 · 10Y TIPS 7/23 · month-end 2/5/7Y 7/27–28)** + real yield at a series high with headroom + MOF-intervention wildcard (dormant).
- **★ DECISIVE — GAP vs GRIND: modal path is a GRIND, which cuts AGAINST this strike.** The real-yield mechanism re-prices ~14bp/week with repeated round-trips; a +50bp move in 72d by grind needs ~7bp/wk for 10 weeks with no retrace — inconsistent with the tape. **The 77 strike only pays on a GAP** (hot-CPI surprise or a failed auction after 7 benign tests, ~70% benign base rate); a slow correct-direction drift expires it worthless.
- **Verdict: FATTER-TAIL (mild)** — cheap-vol tail, slightly-better-than-fair odds, but edge cashes **only on a fast CPI or auction gap.** Size as a **small conditional lottery, not a conviction position**; decays fast if Hormuz de-escalates (BOND's single biggest swing factor = Hormuz/Brent — the same shared falsifier as §9).

**TERRY structural synthesis w/ BOND:** the edge is *real but thin and conditional.* The "gap-not-grind" finding is actually a **clean structural fit, not a strike-off**: Will already owns the GRIND (85P/82P/TBT), so a pure GAP-tail is the exactly-complementary instrument — it pays where the grind holdings don't and doesn't compete with them. The right framing is **not** "hold a tail to Sep-30" but **"buy cheap vol (MOVE 68) ahead of the 7/22–28 auction gauntlet + 8/13 CPI gap catalysts"** — vol-timing supports entering while compressed. **Net: right instrument, right role, right day, mild positive edge — but a small conditional lottery, not a lean.** $495 defined risk is the correct size for exactly that.

**Decision (WILL, 2026-07-17):**  [ ] APPROVE 77P × ~45 ct ($495)   [ ] APPROVE 77/76/75 ladder   [ ] HOLD — wait for a FRESH discriminator, not just a better entry   [ ] REJECT
→ **HELD 7/17 (banked).** Re-fired and APPROVED 2026-07-20 — see below.

### ★★ FILLED — 2026-07-20 ~09:50 ET — FIRST LIVE FIRE OF A TERRY CARD ★★
- **APPROVED + FILLED (Will):** **TLT Sep-30-26 77 Put × 30 @ $0.11** (limit lifted the offer; ticket showed 0.10/0.11, filled at ask). **Premium at risk = $330** (+~$15 fees ≈ $345 order value). **Break-even TLT 76.89** (~76.885 incl. fees).
- **Size note:** 30 ct (not the proposed 45) = **$330 of the $500 bank**; **~$170 left dry** to scale on a fresh discriminator. Deliberately conservative for a small conditional lottery — correct instinct, not a compromise.
- **Entry gates (all green at fill):** arm-#2 LIT/latched (10Y ~4.57, no <4.50 close) · **rule-#6 CLEAN — TLT GREEN on the day** (proven by the chain: 77P & 75P marked *below* Friday close even as IV rose ~1pt → underlying up) · 77P ask $0.11 ≤ no-chase $0.12 · spread ~9.5%, OI 657, liquid.
- **Live chain at fill (broker, ~09:50 ET):** 77P 0.10/0.11 mark 0.105 IV **13.67%** Δ−0.050 Γ0.020 Θ−0.0032 V0.0388 OI657 · 76P 0.08/0.09 IV14.55 · 75P 0.06/0.07 IV15.24. IV ~+1pt vs 7/17 (12.79) = market pricing more gap risk (consistent w/ WALTER SIG-009 dealer-gamma halved $16.2→6.2bn) — confirmatory for a gap-tail buyer; price did not chase.
- **Position delta:** ~−150 TLT-share-equiv (0.05 × 30 × 100). Negligible vs book.
- **★ MANAGEMENT (pre-registered):**
  - **Defined risk, no stop** — max loss = $330 premium; the premium IS the stop.
  - **Pays on a GAP, not a grind.** Catalyst cluster: 20Y auction + 40Y JGB **7/22** → month-end 2/5/7Y **7/27-28** → FOMC **7/28-29** → July CPI **8/12** → **Aug CPI 9/11**. A slow correct-direction drift expires it worthless (modal path).
    > **📅 DATE CORRECTION (PROME → TERRY, 2026-07-26; RED S25b 7/24, OMB PFEI-verified).** July CPI is **Wed 8/12**, not 8/13; August CPI is **Fri 9/11**, not ~9/10. **Earlier 8/13 / 9/10 references in the 7/16–7/17 vintage blocks below are left as-written** (delivered-record canon) — **this line is the live catalyst map.** Two management-relevant consequences: **(1)** 8/12 is **base-effect-PROTECTED** (HENRY 7/23 — July pump avg ~$3.94 sits *below* June's ~$4.05, so gasoline CPI can print negative MoM with pumps at $4.09 and rising): **a soft 8/12 print is NOT the mechanism failing** and must not be read as a disarm signal. **(2)** The real passthrough test is **Aug CPI 9/11**, which sits **inside 004's life** (~19 days of runway to Sep-30 expiry) and lands **inside the Sept-FOMC blackout with the SEP-carrying 9/15–16 meeting four days later** — repricing risk loads onto the meeting itself. **That back-half cluster is arguably the better gap candidate than the front-half one this card was built around.** Frozen management rules above are untouched; only the catalyst map is re-dated.
  - **Harvest rule:** on a FAST spike marking **≥3× (≥$0.33)** at ~$0 intrinsic, **take at least half** (a fast shock pays more than terminal intrinsic via IV expansion); if it goes **deep ITM (TLT<77)**, manage vs the stress table (TLT 75 ≈ +$5,670 net on 30ct / ~17×).
  - **No roll planned** — a $330 tail isn't worth a rule-#7 duration roll (that rule is for conviction grinds; this is a lottery). Let it ride the catalyst cluster or expire.
  - **Disarm:** an official DGS10 **close <4.50** kills arm-#2 → close for salvage if any value remains.
- **§9 concentration (updated):** the 7/18 rates RELABEL (real-policy-path, not term-premium) + CARL weld decomposition make the rates arm **doubly Mideast-insulated** → this add is *less* concentration-additive than the 7/16 framing implied (PROME-relayed; not independently re-verified by TERRY).
- **PAT-028 note:** the card product goes from **0 fired live → 1 fired live.** First live data point on TERRY card quality; still N=1, no track-record claim yet.

---

### (7/16 ARM decision — historical record)
- [x] A discriminator actually fired (arm-#2, 5-of-5 7/13) · [x] Live marks (broker chain 10:04 ET) · [~] Green/red (RED, muted for spread — §7.1)
- [x] Liquidity OK (all rungs) · [x] Max loss ≤ $500 (defined-risk, every variant) · [ ] Position truth (Will confirms)

**Terry verdict (2026-07-16):** flat-book analysis reached CLEAN/REC=81/76 spread — then **position truth (10:09 ET) REVERSED it to book-aware NO ADD** (§9 in arm packet): Will already owns the grind 3 ways (TBT + ITM 85P + 82P ≈$1,150, ~186 sh short-delta, live not stubs), so the spread ≈doubles his short-delta redundantly. Arm-#2 FIRED (5-of-5 7/13); arm-#1 DEAD; arm-#3 grades today 4pm. Card ARMED.
**Decision (WILL, 2026-07-16 ~10:30 ET):** **NO ADD — book-aware rec accepted.** Redundant + deepens a concentrated "Mideast-stays-hot" bet (shared Hormuz-de-escalation falsifier across his rates-short AND oil-long books). **Card stays ARMED; the $500 is BANKED for a re-fire** (arm-#3 4pm, or a red-day/vol-cooldown entry). **Crash-ladder (77/76/75) = approved fallback shape** if a re-fire warrants deploying — the one non-redundant exposure.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
