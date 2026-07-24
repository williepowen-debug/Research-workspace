# TERRY — Cross-Session Memory

**Purpose:** lean DURABLE layer — mandate + accrued lessons/decisions, not a log.
Activity detail lives in commit messages, daytrading/JOURNAL.md, and `memory/auto/`.
Keep this load-bearing: append a Durable Finding only when it survives the episode.

---

## Mandate (one line)

TERRY converts thesis into trade plans with explicit entry/invalidation/sizing/expiry/
roll rules and an approval gate. **Owns the ACTION/card side, not macro truth. Never executes.**
Detection (HY-280 break, print alerts) is LIQUID/SENTRY; TERRY owns everything AFTER the alert.

---

## Standing Decisions (Will-set — load-bearing)

- **Max loss = $500 per card** (Will 2026-06-26). Applied to all fire cards + setups.
- **Fresh capital deploys ONLY on a fired trigger** (Will 2026-06-26) — never a mechanical/calendar
  book-reshape; limited funds = dry powder. Reshape = recycle decaying premium, no new net risk.
- **Default risk ceiling:** 0.25× Kelly or lower (RISK_SCORING.md). Final size = min(Kelly, max-loss, liquidity, event-risk).
- **Day-trading review = bounded SIDE project, subordinate to the thesis system** (Will 2026-06-27). Its only job: plug discretionary-scalp leaks so it can *generate dry powder* to deploy on **researched** thesis trades. It must **not** displace or co-equal the core thesis/fire-card work (transmission thesis, regional/credit cards) or absorb session attention. *Don't let the journal become the system.* (Currently underwater — S3 −$3,969, cumulative −$1,017 — so it's funding nothing: fix the leak, keep it small.)
- Open Q for Will (unresolved): preferred risk UNIT ($/%/R); track-all-considered vs approved-only.

---

## Durable Findings

- **Trigger→card must be MINUTES not hours.** The slow steps are live re-marking + grading.
  Pre-lock structure/strikes/kill-lines in a fire card; only the LIVE-MARKS block is filled at fire (rule #4).
- **Option marks go phantom in state files** — always pull a live chain at fire (chain_fetch.py / live broker),
  never cite stored option marks. Image/broker snapshots are not authoritative (rule #3).
- **The 3 Q2 bank-print mis-grade traps** (now hard guards in grade_print.py): WAL NCO adjusted-vs-GAAP
  (39bps was NON-GAAP adj; GAAP ~1.45%); ZION AOCI total-AFS not muni-only (~$869M FV is NOT the mechanism);
  ALLY collective/growth build = BETA → non-counting for path (a) even though Prov>NCO.
- **DISC-1 ≠ path-(a) tally membership.** Specific/collective classification applies to ANY name's build;
  only the regionals {CFG,OZK,EGBN,WAL} feed the ≥2 path-(a) count. Consumer/gate names (SYF/ALLY/COF) classify but don't tally.
- **Day-trading — leak CONFIRMED REPEAT + engine is regime-conditional (S2→S3):** S2 (5/1–6/23) +$2,951.67;
  **S3 (6/24–26) −$3,968.84** — wiped S2, cumulative 5/1→6/26 −$1,017. Walk-to-$0-expiry leak fired BOTH reviews
  (S2 −2,793/19, S3 −1,624/5). The QQQ 0DTE engine (+$3,044 in S2 trend) **reverses in whipsaw** — both-ways is a
  chop tactic, NOT a whipsaw tactic. NEW R6: don't hold 0DTE into RH's ~3pm auto-liquidation window (≈$327 lost on
  the 6/26 709P, force-closed before a settlement it would have won). Detail in daytrading/.
- **VRP is regime-bounded AND instrument-split — don't price a long-premium tail flat (7/17).** The "buying options is negative-EV" doctrine described a window ~1987-2010 that CLOSED for SPX post-2012 (Dew-Becker/Giglio: alpha≈0 = fairly priced, NOT profitable). But the collapse is index-specific: **TLT/rates tails still pay the full vol tax** (VRP persisted; institution-dominated market), **single-names are ~fairly priced** (premium lives at the index level as a correlation premium) **except into earnings**, and the **deep-OTM strike (8-13%) is where any residual premium concentrates** (untested post-2012; price-insensitive hedging + pure-jump strikes). ⇒ the **crash-ladder pays a DOUBLE tax** (rates + deep skew), justified only by convexity (TT-02: the short-strangle's terminal-window CVaR explosion IS the long tail's payoff window). Full: `options/RESEARCH.md`; auto-memory `finding_vrp_split_rates_vs_singlename`. **Prices the tax, never vetoes — edge still must come entirely from the thesis.**
- **Grind vs crash — a slow thesis wants SHALLOW+LONG, not DEEP+SHORT (7/17 Part B diagnostic).** The bank-put basket bleeds because it expresses a *slow-grind* thesis (credit transmission, 2–4 quarters, name re-rates 10–20%) with *crash-tail* instruments (deep-OTM 13–22%, near-dated). Reachability data: KRE 60P (21.8% OTM) has 0–0.4% empirical 3y reach across ALL tenors — a strike the name never hit; WAL 75P (9.5% OTM) reaches ~20% vs the held 67.5P (18% OTM) ~7%. Deep near-dated puts have the WORST reachability on the grind path → pay the deep-OTM tax AND get near-zero odds on the thesis's actual trajectory. **Fix: strike ~5–10% OTM + tenor 6–12mo + fewer better-positioned puts; sell the rarely-reached deep strike as a spread to fund the reachable one.** Deep-OTM is correct ONLY for a *deliberate* crash tail (TLT ladder) — size it as a lottery, apply TT-02. Same depth, opposite verdict by thesis type. Wired to `CHART_OPTIONS_WORKFLOW.md` §3d; diagnostics in `options/{IV_CRUSH_PARTA,TENOR_DISCIPLINE_PARTB}_2026-07-17.md`. **Part A corollary:** earnings IV-crush is a MINOR contributor to this book (holds mostly sit past the print); the leak is depth+tenor, not crush.
- **No closed Terry-reviewed thesis trades yet** — POSTMORTEMS.md now has ONE *process* entry (TRY-FIRE-005: correct DENY, 7d logging lag; no trade/P&L). Still no closed thesis trade.
- **`SIGNALS.tsv` = the trade-construction context ledger** (Will 6/27, "store in lasting memory, don't put everything of value in STATUS" → option B). Durable home for anything that shapes timing/sizing/structure but isn't the thesis. `source` column spans WALTER (routed INFO), TERRY-chart (my own levels/IV/expected-move), and thesis-owner timing notes (REGINALD/CARL/LIQUID/… scaffolding, NOT their thesis truth). NEXUS regime = one **PIN** row (denominator), refreshed not streamed. Decay-tracked (as_of/decay/conf/status); `boot.py` surfaces PIN + active rows, flags >21d for re-verify/retire. OUT of scope: thesis truth + raw catalyst calendar. STATUS keeps only a one-line read + pointer. New context → add a row; recall at fire-time.
- **Position truth BEFORE structure on a marginal add (7/16, load-bearing).** A clean *flat-book* structure rec can be exactly wrong against the real book. My 81/76 grind-spread was the best flat-book expression — but Will already owned the grind 3 ways (TBT linear + ITM 85P + 82P ≈$1,150, ~186 sh short-delta), so the spread ≈DOUBLED his short-delta redundantly. The "his puts are decaying stubs" escape hatch failed on a delta check (the dominant leg was an ITM 85P at −14%, not a stub). Rule #4 isn't just "don't cite stale marks" — for any marginal add, **pull the book and rank the marginal exposure, not the standalone trade.** Also: watch **shared falsifiers across the WHOLE book** — Hormuz de-escalation would hit his rates-short (via the oil-driven term premium) AND his oil-longs at once; a card that looks defined-risk in isolation can concentrate a portfolio-level bet.
- **Sparse-index intraday endpoints can be date-shifted (7/16).** yfinance `^MOVE` 1h-bars returned degenerate single points labeled **one day late** (carried 7/10's 69.55 onto 7/13), which led me to a wrong F3→F1 gate-attribution correction I had to RETRACT. The posted **daily** (investing.com, arithmetic-self-consistent + tied to the yf 7/10 anchor) showed the real spike was 7/13 (77.77 +11.82%). **Before canonizing any date-dependent claim off a sparse index, verify against a posted daily source** — don't trust the intraday/1h endpoint's date labels. (VIOLET's ±1-day ^MOVE caveat, confirmed the hard way.)
- **Rule #6 reads off the option's OWN underlying, and in a yields-up regime TLT-color decouples from equity-color (7/20, now standing on 004).** For a TLT put the clean "puts-on-green" entry is a GREEN **TLT** day (bonds bid / yields easing) — NOT a red equity tape. In the current higher-for-longer regime a red equity day frequently coincides with TLT *also* selling off (yields up = TLT red), so buying the TLT put into equity-red is a **chase**, not a rule-#6-clean entry. Confirmed BOND's inversion. Field-verified trick: read the green/red day off the option chain itself — on 7/20 the 77P & 75P marked **below** Friday's close *even as IV rose ~1pt*, and a put only falls while its vol rises if the underlying moved up → TLT green, confirmed without needing a clean spot quote. Generalizes to any single-name/ETF put: apply rule #6 to the thing you're buying puts on, not the index.

---

## Current Session (2026-07-24 Fri — boot + 3d catch-up + position refresh + shadow-book build-out; no capital moved)

**Delivered:** Booted 3 days dark → caught up 7/22 slate + 7/23 prints. **(1) Resolvers, all clean/no-trade:** WAL-GRIND **HELD DORMANT** (REGINALD Stage-1+2: narrow-middle — (b)-migration on known $99M life-sci + (a)-no new credits; no lapse/no entry; Sep puts→Q3); **monoline TRY-FIRE-003 graded NO-FIRE** (COF printed 7/21 beat/provisions-DROPPED = counter-evidence; ALLY+SYF 0/4 each → path (m) 0-fired all 3 → consumer leg defers to Q3; card grade logged; un-owned-gate closed); WALTER reconfirmed squeeze-risk signal 7/23. **(2) Position truth REFRESHED to live 7/24 marks** (STATUS snapshot rebuilt: $39,527/61% cash/−9.98% [improved from −16.6%]; 004 = +12.4%/$390 into FOMC week; day-trade QQQ 690C 0DTE ITM auto-exercise flagged to Will). **(3) Shadow-book build-out (Will-approved):** Phase-2 salary **SET $1,500/mo paper** + gate pinned ≥6/90d (now 2/6); mark-helper dedupe+retry+gate-line; `lane` column; **`Decision Logic` rulebook codified** (open/prioritize/close, 4 rulings A–D, card-is-the-algorithm). 5 commits (4 TERRY + swept HEARTBEAT), all on origin.

**Next entry:** 004 monitor into FOMC 7/28-29 (harvest ≥3×→half; disarm DGS10 close<4.50; gap cluster month-end→FOMC→~8/13 CPI). Consumer/monoline + WAL roll-vs-salvage → Q3 prints. Standing Will Qs still open: risk unit ($/%/R), track-all-vs-approved.

---

## Prior Session (2026-07-21 Tue — four-print day graded, ZERO tells, no trade)

**Delivered:** Boot consumed 3 inbox items (REGINALD WAL-grind CONFIRM · PROME VIO-116 re-open · DEWEY info) → **(1)** WAL-grind card upgraded: confirm folded in, Jan-27 tenor locked, **§2b PRINT GATE staged** (lapse/enter tells, credit-line-not-NIM read, 77.5-netting + 67.5-roll-leg execution flags). **(2)** **ALLY + SYF graded 0/4 un-mask tells each** (SEC 8-K primary for SYF) → **path (m) 0/2 NO FIRE**, TRY-FIRE-003 defers to COF 7/23 (strong-single ≥2 tells now required); SYF datum for CARL-side: masking lever (book shrinkage) REVERSING while credit improves = contrary evidence to the mechanism. **(3)** **WAL Q2 graded off the 8-K within the hour: enter-tells 0/3 → NO ENTRY**; SM −22% QoQ / NCO 37bps below band / $99M ABSENT (unresolved≠cured); **counter-grain nonaccrual +$70M + classified assets +$58M → improvement-vs-migration adjudication routed to REGINALD** (card = GATE-CLOSED/ADJUDICATION-PENDING, not lapsed); WAL grader MASTER=BUILD but collective-beta NON-COUNTING → path (a) no advance. **(4)** **VIO-116 write-back → PROME: 004 RIDES UNCHANGED** ($170 stays fenced; confirmation ≠ fresh discriminator). **(5)** OZK headline only (credit/RESG = call 7/22); after-hours WAL −0.75%/OZK −1.14% = no gap. **(6)** HY OAS re-stamped 269 [7/20], moved AWAY from 280. 004 marked $0.13 mid vs $0.11 fill; paper book marked live.

**Next entry:** STATUS pickup item 0 — the **7/22 resolver slate** (WAL call noon $99M + REGINALD (a)/(b) adjudication · OZK credit grade · EGBN print · JGB auctions for 004). Standing Will Qs still open: risk unit ($/%/R), track-all-vs-approved.

---

## Prior Session (2026-07-20 Mon — ★ FIRST LIVE FIRE of a TERRY card)

**Delivered:** **TRY-FIRE-004 re-fire FILLED — the desk's first live card** (30× TLT Sep-30 77P @ $0.11 = **$330 at risk**; Will sized 30 not 45 → ~$170 bank dry). Clean process end-to-end: ruled rule-#6 day-color definitively (→ new Durable Finding), verified arm-#2 LIT + green-TLT day **off the live option chain**, live-marked, Will approved. Recorded across card ZONE-3 / STATUS / SETUPS / TRADE_BOOK / PB-0002. Pays on a GAP (7/22→8/13 cluster); harvest ≥3×→half; disarm DGS10 close <4.50. Also this session: **HBAN retired** to dust-rider (Will EXIT-THESIS); **Kharg-006 trigger INVERTED** + wording confirmed (PortWatch AIS = dark-fleet-blind → refuting veto only; GATE-TERRY-006 LIVE, card ARMABLE); **`paper_book_mark` venv self-heal fixed** (gotcha: venv python is a symlink to system python → `sys.executable` compare falsely blocked re-exec; rely on env-flag loop-breaker); **desk dashboard artifact built** (refresh ON REQUEST — `[[reference_terry_desk_dashboard]]`); **full file sweep** → STATUS spine reconciled to post-fire (was still "0 fired"), **WAL-GRIND REGINALD confirm ROUTED** (never sent since 7/17 — closed that crack; awaiting reply into 7/21 AMC), **DHI-PHM LAPSED** (Will; archived). All committed + pushed.

**+ desk dashboard v2 + PROME-trio applied (7/20 PM):** Will asked for dashboard ideas → converged with PROME's Will-approved list. Built: **3-tab split** (Cards / Shadow Book / Positions), **NEEDS-WILL strip**, desk lede, since-refresh delta, **unified all-cards catalyst calendar**, **shared-falsifier "what dies together" map**, 004 payoff-ladder/DTE/disarm-cushion, distance-to-trigger bars, expiry-runway flags. **Positions wired to FORGE (PROME #6):** new `scripts/positions_from_forge.py` parses `FORGE/STATUS.md` (PROME-reconciled mirror) → normalized rows + DTE (selftest PASS, reconciled EXACTLY vs the prior hand-transcription = no hidden error) — kills the re-key risk; one reconcile feeds both surfaces. Also closed: **entry_basis spec** (PROME ruled — exp-labeled full instrument id, stops firetime parsing expiries as docket dates) applied to PB-0001/0002 + guardrail; **`paper_book_mark` venv self-heal** fixed. Same artifact URL throughout (refresh-on-request; do NOT auto-regen). Full pointer → `[[reference_terry_desk_dashboard]]`.

**Next entry:** watch inbox for REGINALD's WAL-GRIND reply (grind-not-crash / timeline / roll-vs-die; note 77.5 leg stacks on the RH WAL 77.5P Aug-21) into the 7/21 print; monitor 004 (disarm DGS10<4.50, harvest ≥3×). Natural next dashboard refresh = post-7/21 print. Standing Will Qs still open: risk unit ($/%/R), track-all-vs-approved.

**7/17 digest:** cleanup (005 SHELVED→first POSTMORTEM; arm-#3 fired-weak→deepen; HBAN stub; DAEDALUS firming) + options lane (`options/RESEARCH.md`: VRP regime-bounded+instrument-split, PDT elimination verified) + live-book applied (IV-crush Part A / tenor Part B diagnostics; WAL-GRIND card formalized) + paper-book Phase-1 built (7/19) + 004 re-fire ZONE 2/3 written, Will passed → seeded PB-0001 ghost. NEXUS PIN refreshed (Break 22/Grind 37/Unres 41; HY OAS 272, 8bp under 001).

**Delivered 7/17 #2 (Will gave live book screenshots → applied the options research to it):**
- **Position-truth snapshot folded into STATUS** (main book $38,999 / cash 60% / unrealized −16.6%; the whole loss lives in the regional-bank put basket). Corrected the stale ~$1,150 duration figure to the real ~$1,009.
- **TT-02 promotion decision (Will-approved): NOT a numbered rule** → wired as a scoped construction note `CHART_OPTIONS_WORKFLOW.md` §3c, tag-gated to deliberate-tail cards, walled off from directional puts. RESEARCH.md updated to match.
- **IV-crush diagnostic Part A** (`options/IV_CRUSH_PARTA_2026-07-17.md`): term-structure method (no weeklies). **Crush hypothesis PARTIALLY REFUTED for the book** — minor except OZK's tiny Aug-21 deep strikes; holds mostly sit past the print. Re-pointed diagnosis to depth+tenor.
- **Tenor diagnostic Part B** (`options/TENOR_DISCIPLINE_PARTB_2026-07-17.md`): reachability model → the real leak = grind thesis in crash instruments (see new Durable Finding). Wired to §3d note.
- **WAL grind put-spread card formalized** (`setups/WAL_grind-putspread_2026-07-17.md`, CONDITIONAL): 77.5P/67.5P Jan-2027, ~$3.45 debit, ~1.9:1; the $500-cap-compliant version (outright breaches); flagged as ROLL TARGET for the dying Sep WAL puts, not additive. Thesis owner = REGINALD `[CONFIRM_NEEDED]`; not armed/fired. Logged TRADE_BOOK + SETUPS.tsv.

**Status:** ✅ pushed since (commit `51c1abb6` swept on a later clean push; the 7/17 non-ff/deferred note is resolved — origin has carried it for days). *(Stale-note cleared 2026-07-20 sweep.)* Downstream: the WAL-GRIND REGINALD confirm was finally **routed 7/20** (into the 7/21 AMC print); DHI-PHM builder card **lapsed 7/20** (Will).

---

## Next Session

1. **TRY-FIRE-004 — LIVE POSITION (fired 7/20, 30× TLT Sep-30 77P, $330 at risk).** Monitor only: harvest ≥3× fast spike → half; disarm on DGS10 close <4.50; catalyst cluster 7/22 JGB → 7/27-28 month-end → FOMC → ~8/13 CPI. Scale the ~$170 ONLY on a fresh discriminator (VIO-116 re-open adjudicated NOT one, 7/21).
2. **Un-owned-gate check before every closeout** (from the 005 postmortem, now standing): any resolver landing after session end gets a named grader or an explicit STATUS pickup line. 005 drifted 7d because nobody owned its gate.
3. ✅ **DONE (7/24 catch-up):** HBAN 7/23 print (rode through, lottery dust), OZK 7/21 (graded — headwind), WALTER decay (squeeze-risk row RECONFIRMED as-of 7/23), monoline 003 (NO-FIRE, defers Q3). All cleared from the pickup.
4. **WAL grind put-spread card** (`setups/WAL_grind-putspread_2026-07-17.md`) — **REGINALD adjudicated it HELD DORMANT (7/22): no lapse, no entry.** Sep WAL puts (70P/67.5P, ~$95 mkt, −92/−95%) roll-vs-salvage defers to Q3; preferred as ROLL TARGET not additive (rule #7). Don't let them silently expire in Sept without a roll decision.
7. **Options diagnostic follow-ups:** Part C (historical IV-crush) is BLOCKED on paid IV-surface data (named, not attempted). The grind-vs-crash §3d note is a candidate to promote to a numbered rule after a bank card actually fires. Consider the same reachability check on the KRE/OZK basket if Will wants those re-expressed too (KRE 60 is the worst-positioned — 0% empirical reach).
8. **Carries:** Will's risk-UNIT question ($/%/R); day-trade timestamped order export. **Options open items** (RESEARCH.md): deep-OTM/rates VRP gaps = acknowledged, NOT tracked (recognize-if-encountered).
