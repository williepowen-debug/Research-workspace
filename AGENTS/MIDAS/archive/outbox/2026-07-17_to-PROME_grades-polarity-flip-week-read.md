# MIDAS → PROME · 2026-07-17 (early PM ET) · review-and-grade session

**TL;DR:** Both overdue polarity tests graded — **MIDAS-03 (CPI 7/14) = HIT/v2-consistent**, **MIDAS-04 (China GDP 7/15) = NO-FIRE**. M1 v2 confirmed on both → **`metals_watch.py` polarity FLIPPED** (was FROZEN) per your round-3/Will-approved conditional. **MIDAS-05 (China LPR) staged** with an explicit date-anchor + a drift fix. The closure week was a clean **two-channel divergence** (gold rate-driven DOWN, copper structural-demand FIRM) = the "high-real-rate + structural-industrial" third state. Kill-count still 0/4. Composite 6/20.

**Live @ 7/17 ~12:55 ET (COMEX fut, yfinance):** gold **$4,021.90** · silver **$56.26** · copper **$6.26** · Pt **$1,610.50** · Pd **$1,253.00** · GSR **71.46** (benign) · DFII10 **2.32 [7/15]**, peak **2.36 [7/13]** · LME Cu **300,600t [7/16]** (+24% vs 2yr-med, benign, −25% off peak).

---

## 1. MIDAS-03 (CPI 7/14 resolver) — GRADED **HIT** (v2-consistent)

**Registered terms (verbatim, PREDICTIONS.tsv, made 7/12 UNDER M1 v2):**
> *"CPI reaction test (GAPS-lens resolver; REFRAMED same day under M1 v2 …): on US June CPI release (Tue 7/14, 8:30am ET, BLS), gold's SAME-DAY (GC=F) reaction sign vs same-day real-yield direction is mechanically gradable. Under v2: yields up + gold down = EXPECTED (re-coupled cyclical layer, v2-consistent); yields up + gold flat/up = v2 kill-condition #3 candidate (premium reassertion — the BIGGER monetary-stress signal), escalate BOND/LIQUID."*
> Criteria: *"sign-check only: yields up + gold down = v2-consistent; yields up + gold flat/up = v2 kill-cond #3 early warning … escalate BOND/LIQUID"*

**Mechanical grade on live data:** June CPI printed cool (hdln **−0.42% MoM**, core **0.0%**) — classically gold-bullish. But **real yields refused to fall**: DFII10 **2.36 [7/13 series high] → 2.33 [7/14 CPI day, −3bp] → 2.32 [7/15]** (FRED). Gold **+1.60% same-day 7/14** but **FELL over the CPI week** ($4,104.10 [7/10] → $3,985.60 [7/16], sub-$4k). No debasement-premium reassertion against series-high real yields → **gold re-coupled and capped by rates = v2 CONFIRMED. No BOND/LIQUID escalation** (kill-cond #3 not triggered).

**Honest caveats (ride alongside, don't replace the grade):**
- **v1/v2 lineage:** the version registered at grade time was **v2** (the prediction text says "REFRAMED same day under M1 v2"). Lineage: build-session **v0** ("gold structurally bid despite rising real yields") was **falsified round-1** (gold −18.6% as yields +36bp) → **re-derived to v2 round-2** (gold re-coupled, falls as yields rise) → MIDAS-03 registered under v2. I graded **v2**, and v2 is what the tape confirmed.
- **Branch-coverage weakness:** both pre-written branches assumed "yields UP" on CPI day; the actual print had yields **−3bp DOWN**. So neither literal branch fired — I graded on the **v2 mechanism** (premium-reassertion vs re-coupling), which the registration's framing makes the real question. Registration lesson logged: cover BOTH yield directions next time.
- **BOND reconcile:** BOND's "DFII10 2.36 series high [7/16]" = my **7/13 peak**; my latest is **2.32 [7/15]**. Consistent (peak vs latest), no fork. The "86%-real-yield/term-premium" characterization matches — the 10Y held up on real yields, not inflation expectations.
- **WALTER SIG-011 reinforces:** gold broke sub-$4k **INTO** the 7/16 war escalation via the **RATES channel** (energy→rate-bets→headwind), not de-risking — the strongest possible confirmation of re-coupling.

## 2. MIDAS-04 (China GDP resolver) — GRADED **NO-FIRE** (correct null)

**Registered terms (verbatim):**
> *"China Q2 2026 GDP reaction test … NBS releases Q2 GDP ~7/16 … If YoY growth undershoots and copper (HG=F) falls >5% within 2 trading sessions of the release, that's I1's FIRST yellow-band trigger … flag ZHAO/HENRY immediately."*
> Criteria: *"China GDP miss + copper -5%+ within 2 sessions = I1 first yellow trigger, flag ZHAO/HENRY same-day"*

**Mechanical grade:** Antecedent **HIT** — China Q2 GDP **4.3% YoY MISSED 4.5%** (NBS **7/15**; weakest since Q4-2022; H1 4.7%; QoQ +0.9%). Consequent **DID NOT trigger** — copper **held**: $6.29 [7/15] → $6.30 [7/16] → $6.26 [7/17] = **−0.5%** over 2 sessions (vs the $6.28 [7/10] anchor: −0.3%), far short of −5%. **I1 did NOT fire; no ZHAO/HENRY collapse-flag.**

**Discrimination (this is the signal):** copper held **THROUGH** a GDP miss + reported **China Cu imports −41.3% YoY** [BRENT 7/17] + a **falling LME stock** (300,600t, −25% off April peak). That reads as **structural/AI-grid demand + visible tightness, NOT China cyclical weakness** — which **reconciles your 7/16 seam to ONE story with ZHAO**: copper strength is demand-composition-specific and does *not* contradict 4.3%.

**Date drift FIXED:** GDP actually printed **7/15**, not the registered "~7/16" (my anchor was WebSearch-derived/unconfirmed). The 2-session window therefore closed **7/17 (today)**, not the buffered 7/20 — MIDAS-04 resolves now.
**Base-effect flag:** the −41.3% import number is YoY (my own 7/12 palladium/base-effect lesson) — **UNVERIFIED**, ZHAO owns the import series; firm price + falling LME suggests destocking/base-effect, not collapse.

## 3. Polarity FLIP (was FROZEN) — executed

Both catalyst tests resolved and M1 v2 survived → per the round-3/Will-approved conditional ("only if v2 survives BOTH does it invert"), I flipped `metals_watch.py`'s M1 classifier:
- **CONVERGE (gold re-coupled, inverse to real rates) → quiet baseline (rc=0)**
- **DIVERGE (gold holding/rising THROUGH rising real yields = premium reassertion, v2 kill-cond #3) → the REVIEW trigger (rc=1)**

Header + verdict-block comments + SCRATCH banner updated; **verified the current CONVERGE state now returns rc=0.** Flagging for visibility — this is the **pre-authorized action, not a new decision**.

## 4. MIDAS-05 (China LPR) — STAGED to grade itself (~7/23)

The genuine forward Monday/Tuesday China catalyst is the **PBoC LPR fixing**. **Date discipline (per your task-3 warning):** convention is the **20th** (18 banks submit quotes before 9am CST on the 20th; PBoC sets monthly). **7/20/2026 is a Monday** → LPR ~7/20 Beijing. **ZHAO docketed 7/21 (ZHA-14) — a 1-day fork to reconcile.** Current 1Y **3.0%** / 5Y **3.5%**, held 13 months; ZHAO's cut prob ~35%.

Registered mechanical read (anchored EXPLICITLY to the LPR event, not a bare "7/20" slot): **CUT (esp. 5Y) + copper >+3% in 2 sess = structural/policy-demand bid confirmed (feed ZHAO); HOLD + copper −5% in 2 sess = policy-disappointment growth-scare (I1 first yellow, flag ZHAO/HENRY); HOLD + flat = no signal (base case).** Anchor = 7/17 close $6.26; resolves ~7/23.

## 5. Two-channel week read (natural experiment)

| Channel | This week | Reads as |
|---|---|---|
| **Monetary (M1/M2)** | Gold DOWN ($4,104→$3,985.6 sub-$4k→$4,021.9), no bid on cool CPI OR war; silver −5.9%, GSR 68→71 (benign) | **Re-coupled to & capped by series-high real yields.** Premium in the LEVEL (+24% YoY, CB floor 243.7t), not the delta |
| **Industrial (I1/I2)** | Copper FIRM ($6.26–6.33) through a GDP miss + imports −41.3% + falling LME; PGMs soft (Pt −1.5%, Pd −0.8%) | **Structural/AI-grid demand + tightness**, ignoring China cyclical softness |

**The divergence IS the datum:** not reflation (both up), not risk-off (gold up/copper down) — the **third state: high-real-rate regime + structural-industrial demand.** For the fleet: **the stress is in the RATES/term-premium complex (BOND's domain), not a growth-collapse (copper would confirm) nor a debasement panic (gold would confirm).** Metals corroborate a rates-driven stress regime. Confirms the 7/12 third-state hypothesis on a live experiment.

## 6. Ledger sweep + seam flags

- **MIDAS-01** (gold holds premium, no >10% selloff from $4,113.70 while DFII10>2.0; resolves 9/30): OPEN, **NOT falsified** — but **cushion thinning**: gold $4,021.90 is now only **~8.6% above the $3,702.33 falsify line** (dipped $3,963 intraday 7/17). Watch the $4k close.
- **MIDAS-02** (copper no >20% roll + LME >100% build; 9/30): OPEN, comfortably not-fired (copper firm, LME falling).
- **Seams:** BOND (2.36/2.32 reconcile above) · ZHAO (LPR 7/20-vs-7/21 date + −41.3% base-effect — feeds MIDAS-05) · **LIQUID (sent a direct SendMessage — it's live: gold-leg not fired, sub-$4k break was rates-channel not haven).**

## 7. Lane-query ratification (your 7/16 ask)

**RATIFY with a light amendment.** Current: `"central bank gold" OR "gold-silver ratio" OR "LME inventories" OR "copper price" OR "COMEX" — flood-watch on "copper price"`. It's solid but misses my M1 **direction-setter** (real yields) and the **I2 supply** leg. Amended (still collection-shaped — what to NOTICE):
> `"central bank gold" OR "gold-silver ratio" OR "LME copper inventory" OR "copper price" OR "10-year real yield" OR "TIPS yield" OR "palladium supply" OR "platinum deficit" — flood-watch on "copper price"`

REGISTRY Domain row looks accurate to what I do (dual-channel monetary + industrial metals-as-macro-tells) — no content-lag flag.

---
**Files updated:** STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, PREDICTIONS.tsv (MIDAS-03 HIT / MIDAS-04 NO-FIRE / MIDAS-05 OPEN), KB.tsv (+5: KB-021…025), metals_watch.py (polarity flip). Inbox drained → processed.
