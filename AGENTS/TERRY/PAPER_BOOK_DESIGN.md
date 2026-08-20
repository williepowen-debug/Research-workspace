# TERRY Paper-Book — BUILD-READY SPEC
**Status:** ✅ PHASE-1 BUILT 2026-07-19 (Will greenlit; commit `ae739980` — `PAPER_BOOK.tsv` + `scripts/paper_book_mark.py` + boot step 5b / closeout wiring + seed `PB-0001`). Phase-2 salaried desk remains DEFERRED behind the volume gate (§Phase 2). Originally 💡 Will's idea 2026-07-17, TERRY endorsed; the BUILD-READY spec below was Will-reviewed 7/19.
**Problem it solves:** PAT-028 — 0 cards fired live → 0 track record → the card product is un-instrumentable. The only "product" so far is the *refusals* (005 gate, book-aware NO-ADD). A paper book manufactures a falsifiable track record without capital risk, and finally gives `RISK_SCORING.md` §5 (calibration/Brier) something to score. Measures **process calibration** (structure / timing / sizing / prioritization) — NOT behavioral/execution edge.

## The core insight — "salary" = opportunity cost
A **fixed/salaried** bankroll (not unlimited paper money) is the key. Infinite paper money only tests per-trade accuracy ("how often right"); a **limited/salaried** book forces *choosing* which setups get paper capital → tests **prioritization judgment** (is 004 worth it over the builder card?), which is the more valuable feedback and mirrors the real tranche-by-tranche capital constraint. *(NB — this insight powers Phase 2; Phase 1 is deliberately un-salaried, see the volume gate in §Sharpening 4.)*

## The 3 failure modes that would make the data LIE (design around all three)
1. **Fill fidelity (THE make-or-break).** Paper fills at mid are fantasy — for a long-premium options book the bid/ask + slippage is a huge chunk of real P&L (DHI front-week spreads ran 50-200%). **RULE: fill buys at the ASK, sells at the BID** (never mid) — hardened further in Sharpening 3 (timestamp + slippage tooth).
2. **Discipline decoupling.** Free paper-trading drifts into setups I'd never propose live → the record becomes a *looser* strategy than the real one, useless for transfer. **RULE: the paper book trades the SAME rules** — same triggers, same $500/card, same construction discipline.
3. **Logging survivorship.** Losers get quietly forgotten → the record flatters itself. **RULE: every paper position logged with entry mark / thesis / invalidation + mark-to-market on a boot cadence** (same staleness discipline as the ledgers; a paper book that isn't marked rots).

---

## ★ RESOLVED (Will-reviewed 2026-07-19)

### The 3 open questions — answered
| Open Q | Resolution | Why |
|---|---|---|
| Bankroll size / salary cadence | **N/A for Phase 1** — the shadow book needs no bankroll; it tracks would-fire cards to close. Bankroll is a Phase-2 concern. **Phase-2 gate pinned + salary SET 2026-07-24 (Will): gate = trailing-90d would-fire ≥6 cards; tranche = $1,500/mo paper (see §Phase 2). Desk activates when the gate trips.** | Phase 1 measures card quality, not prioritization — no capital constraint needed yet. |
| Shadow-only vs straight to salaried | **Shadow-only (Phase 1).** Salaried desk deferred behind a quantitative volume gate. | The prioritization test can't bind at ~2-3 cards/month (Sharpening 4). |
| Auto-fill on trigger vs approved-only | **Auto-fill on trigger — regardless of Will's approval.** | The *only* version that generates a record: the whole problem is 0 approvals. Approved-only would inherit the same near-zero volume. Labeled "card-quality record, not a P&L Will endorsed." |

### The 6 sharpenings (baked into the build spec below)
1. **Auto-fill on trigger is THE design decision, not a detail.** Every card that reaches would-fire state fills the shadow book *independent of the approval gate* → measures card quality. This is what actually attacks PAT-028.
2. **Capture the refusals — they're the best data.** The only product so far *is* the refusals. Every row carries a `will_decision` field (APPROVED / PASSED / NO-DECISION); the **PASSED subset is the counterfactual "ghost"** — at close it answers *did the discipline to say no save or cost money*. One table, a decision column (cleaner than a separate lane). Explicitly NOT a P&L that argues for looser deployment — it calibrates the pass decision.
3. **Fill rule needs one more tooth.** Ask/bid still flatters at size and widens at the open. Add: (a) fill at the **trigger timestamp**, not close; (b) a **slippage penalty** for wide-spread names (bid/ask > 15% of mid → fill one tick worse than the posted side, or a fixed haircut); (c) record `entry_basis` (exact quote + timestamp) so every fill is auditable; (d) trigger while market closed → fill at next-open, never mid.
4. **Defer Phase 2 behind a quantitative volume gate.** Prioritization is only testable when would-fire setups *exceed* bankroll capacity. Build the salaried desk ONLY once the trailing would-fire rate exceeds a plausible salary tranche — otherwise it's complexity measuring nothing. **★ Gate pinned 2026-07-24 (Will-approved "pin the # / defer live salary"):** Phase 2 opens when **trailing-90-day would-fire count ≥ 6 cards** (≈ ≥2 would-fire/month sustained a full quarter — the point where a monthly tranche can no longer fund them all and *choosing* becomes a real judgment test). Measured from `PAPER_BOOK.tsv` `opened` timestamps; `paper_book_mark.py` surfaces the running `would-fire (90d): N/6` count at boot as an early-warning. **No live salary is set now** (at N=2 it would measure nothing) — only the trigger is armed.
5. **Small-N honesty.** A clean shadow book gives *directional* feedback, not significance, for a long while. No calibration/Brier scoring and no decision acts on the record until **N ≥ 10 closed positions per lane**; until then rows carry `notes = "N-too-small"`. Guards against over-reading an early lucky/unlucky streak.

5b. **★ The N≥10 gate counts ROWS, and rows are not observations (added 2026-07-26 — surfaced by CARL's 7/24 design question).** Ten rows that share one antecedent are **not ten independent trials**; they are roughly one trial logged ten times, and scoring them as ten manufactures false confidence at exactly the moment the gate says it is safe to start trusting the record.
   - **Live proof, in this book, right now:** `PB-0001` and `PB-0002` are **both TRY-FIRE-004, both TLT Sep-30 77P** — same card, same strike, same expiry, differing only in size and Will's decision. **Two rows. One observation about card quality.** The `lane` split (paper/real) happens to separate these two, but it does not solve the general case: ten TLT-duration rows in one lane would trip the gate on ~1–2 effective observations.
   - **Requirement:** every row records an **`antecedent`** — the thesis/driver that would kill it (`rates-duration`, `regional-bank-credit`, `escalation-oil`, …). This is the same field as the card's `EFFECTIVE-N` shared-antecedent line (`RISK_SCORING.md` §2b) and should be copied from it.
     - ✅ **NOW A REAL COLUMN (2026-07-30, col 20).** ⚠️ From 7/26 until 7/30 this requirement existed **only in this document** — `PAPER_BOOK.tsv` had no such column and antecedents sat in freeform `notes`, i.e. **uncountable**. So the independence half of the gate below was both **unenforced and unmeasurable**: the design asserted scoring was protected, and nothing computed the protection. Found independently by **RAV and DAEDALUS** the same day. Backfilled for all 4 existing rows; `paper_book_mark.py` now prints both counters per lane. **A row with a blank `antecedent` is reported as uncountable — set it at fill time.**
   - **Gate becomes conjunctive:** scoring opens at **N ≥ 10 closed per lane AND ≥ 5 distinct antecedents per lane.** Rows short of the second condition carry `notes = "N-not-independent"` rather than `"N-too-small"` — a different failure with a different fix (get *varied* cards, not merely *more* cards).
   - **Why the second condition matters more than the first here:** this desk fires rarely and concentrates in one or two theses at a time. **Row-count is the easy number to reach and the misleading one.** Left unfixed, the gate would have opened on a book that was mostly one trade.
6. **Marking cadence caveat.** TERRY is spawned on-demand, not continuous — a paper option can sit unmarked for days while it decays. Marks are **as-of-last-spawn**, stamped and staleness-flagged; the equity curve is lumpy by construction and must be labeled so, never pretended continuous.

---

## ★ PHASE-1 SHADOW BOOK — BUILD SPEC (build on Will's go)

**Purpose:** auto-fill every card that reaches would-fire state at realistic marks, track to close, measure card quality; the PASSED subset doubles as the refusal-calibration counterfactual.

### Data model — `PAPER_BOOK.tsv` (append-only rows; `mark`/`status`/close fields updated in place)
| Column | Meaning |
|---|---|
| `paper_id` | PB-0001, sequential |
| `card_id` | originating setup/fire card (e.g. TRY-FIRE-004-ZONE2/3, TRY-BUILDER-DHI-PHM) |
| `opened` | ET date/time of the would-fire trigger |
| `will_decision` | APPROVED / PASSED / NO-DECISION (the refusal-calibration key; PASSED = the ghost subset) |
| `lane` | `paper` / `real` (added 2026-07-24). A would-fire card that Will ALSO filled live gets `real`; auto-filled cards he didn't execute are `paper`. Keeps the card-quality record from being blended with a live P&L at scoring — split by lane once N≥10. |
| `funding_status` | **(Phase-2 column — add when the desk activates)** FUNDED / UNFUNDED-deprioritized / UNFUNDED-displacement-miss / NO-FILL-underspecified. Records how a would-fire card fared against the $1,500 salary cap (see §Decision Logic). |
| `structure` | e.g. "TLT Sep-18 77P x1" |
| `entry_fill` | paper fill price per the fill rule |
| `entry_basis` | exact quote + side + timestamp + any slippage penalty applied (auditable) |
| `risk_$` | defined-risk premium at stake, within $500/card |
| `thesis` | one line |
| `invalidation` | exit/invalidation condition (from the card) |
| `mark` | latest mark-to-market |
| `mark_asof` | timestamp of the latest mark (staleness stamp) |
| `status` | OPEN / CLOSED |
| `close_date` · `close_fill` · `pnl_$` · `pnl_pct` | fill-out at close |
| `notes` | e.g. "N-too-small; not yet scored" |

**INDEX discipline:** one row per paper position, marked-to-market in place; never delete a losing row (survivorship rule).

### Fill rules (the fidelity teeth)
1. **Buys fill at the ASK, sells at the BID** — at the **trigger timestamp**, from a live chain snapshot (`chain_fetch.py`). Never mid.
2. **Wide-spread penalty:** if bid/ask > 15% of mid, fill one tick worse than the posted side (or a fixed % haircut) — you don't get the full posted quote at size.
3. **Record `entry_basis`** = the exact quote + timestamp so the fill is reproducible/auditable.
4. **Trigger while market closed → fill at next-open** quotes (note it). No mid-fills, ever.

### Marking (boot cadence)
- At each TERRY boot, mark every OPEN row via `chain_fetch.py`/`snapshot.py`; update `mark` + `mark_asof`.
- If `mark_asof` > N business days → flag "STALE mark" (ledger-staleness discipline).
- Equity curve is as-of-last-spawn — label it lumpy, not continuous.

> **⚠️ Marking ≠ filling — do not read the ask/bid fill rule above as the marking rule.** Fills are deliberately pessimistic (**ask-for-buys / bid-for-sells, never mid**) because that is what execution actually costs. **Marks are the two-sided MID**, because that is what the position is currently worth. Different questions, deliberately different prices.

**`mark_asof` means "when the mark was TAKEN", not "when the option last traded"** *(clarified 2026-07-30 after the implementation had it backwards).* With a live two-sided quote the mid is current, so the stamp is **now** — and any illiquidity is reported in the **note** (`mid/live-quote (no trade since …)`). Only when there is **no two-sided market** does the mark fall back to the last print, and *then* the stamp is genuinely that print's time (`last/no-nbbo`).

> **Why this is a rule and not an implementation detail.** The original stamped `last_trade` whenever an option hadn't traded that day, which made a **live** mid look days old and tripped the STALE alarm on it — PB-0004 (KRE Dec-18 68P) read "⚠ STALE 10bd" while its NBBO was 1.65/2.11 and current. **This book is deep-OTM options: "quoted but not traded today" is its normal state, not a defect.** An alarm that fires on the normal state stops being read, precisely where it needs to be trusted. Same root as the desk's `finding_grade_execution_only_against_same_timestamp_marks` — **a timestamp must describe the thing it is attached to.**

**Multi-leg (spread) marking** *(added 2026-07-30 — PB-0003 was UNMARKED/PARSE-ERROR on the one day it mattered)*:
- Structures parse as `TICKER [(ROOT)] EXPIRY K1[P|C][/K2[P|C]] … xQTY`. **Fetches use the option ROOT, not the underlying** — `VIX (VIXW)` pulls the VIXW chain; using `VIX` pulls the wrong chain entirely.
- **Net mark = mid(leg 1) − mid(leg 2).** Leg order is as written, **first leg LONG, second SHORT** — the convention every row in this book already uses (`20C/25C call debit spread` = long 20, short 25). Positive net = debit.
- **Both legs are required. One dead leg ⇒ NO net mark**, never a mark off the live leg alone — reporting a two-leg position at a one-leg value is worse than reporting nothing (`finding_fail_loud_on_incomplete_data`).
- Per-leg detail is written into the note (`net-mid/live [360C@19.9+380C@15.2]`) so any net is auditable back to its legs.

### Scoring gate
- **No calibration/Brier scoring, and no decision (sizing / deployment / card-design) acts on the paper record, until N ≥ 10 closed positions per lane.** Until then: directional read only, `notes = "N-too-small"`.
- Once N clears → feed `RISK_SCORING.md` §5 (Brier/calibration) · structure validation (did the crash-tail actually pay?) · entry-timing validation (does the green-day rule improve fills?) · post-print-vs-pre-print (builder card) · refusal calibration (PASSED subset P&L).

### Tooling (mostly exists — keep new code minimal)
- Reuse: `chain_fetch.py` (entry + mark quotes), `snapshot.py` (marks), `csv_pnl.py` (P&L), the `SETUPS.tsv`/INDEX pattern for the ledger.
- New (small): a `paper_book_mark.py` helper (or fold into boot) that marks OPEN rows + flags staleness. Nothing heavier.

### Boot / closeout wiring
- **TERRY boot:** mark OPEN paper positions; surface any STALE. (Same shape as the ledger-staleness alert.)
- **TERRY closeout:** log any new would-fire fills from the session + set `will_decision` for each; the fill rule + marking procedure get a one-line pointer in CLAUDE.md/CLOSEOUT.

### Seed row (natural first entry)
The **7/17 004 re-fire ZONE 2/3** (77P × 45ct = $495) is the natural seed: it reached would-fire (TLT green, rule-#6 clean, Approve-ready) and Will passed → row with `will_decision = PASSED`, which immediately seeds the refusal-calibration counterfactual. TERRY picks the exact seed at build time.

### Definition of done (Phase 1)
- `PAPER_BOOK.tsv` created with the schema above.
- Fill rule + marking procedure documented (CLAUDE.md/CLOSEOUT pointer).
- Boot-mark wired + staleness flag.
- Seed row logged.
- Guardrails restated in the ledger header.

---

## Decision Logic — open / prioritize / close (Phase-2 rulebook)
*Added 2026-07-24 (Will-approved, rulings A–D below). The **open** and **close** logic governs Phase 1 too; the **prioritize** block is Phase-2-only (it needs the salary cap to bind). This is the rulebook the closeout log-step + `paper_book_mark.py` execute against — it removes discretion so the paper record measures the SAME strategy as the real cards (design failure-mode #2, discipline decoupling).*

### 0. Governing principle
**The card is the algorithm; the book executes it.** Entry and exit are inherited mechanically from card fields — TERRY makes no discretionary buy/sell call on a paper position.
- **Corollary — NO-FILL on an underspecified card:** a would-fire card missing any required field (entry trigger / invalidation / target / time stop — HARD BOUNDARY #5) **cannot enter the book.** Log `NO-FILL-underspecified`, never guess. (Doubles as a card-quality gate.)

### 1. OPEN (entry)
- **Trigger = would-fire state** = all *objective* ZONE-3 gates would pass: the card's entry trigger fired · an under-reaction still exists (not chasing a completed gap) · liquidity OK · no-chase level respected. The **`Will approves` and `position truth` gates are set aside** — auto-fill is independent of approval (the PAT-028 point; that's what generates a record at all).
- **Fill:** buy at the **ASK** at the **trigger timestamp**; wide-spread penalty (bid/ask >15% of mid → one tick worse than posted); `entry_basis` records the exact quote+timestamp. Market closed at trigger → next-open ask. **Never mid.**
- **Late detection** (TERRY on-demand, asleep at the trigger): fill at the trigger-timestamp quote if reconstructable, else the next-open TERRY-observed ask, **flagged** in `entry_basis` (lumpy-by-construction, Sharpening 6).

### 2. ADD (scale into an existing paper position)
- **Default: NO adds.** The real book is deploy-once-on-trigger; so is the paper book.
- **Exception:** the card pre-registered a scale rule (e.g. 004's *"scale the remaining ~$170 only on a FRESH discriminator"*) → follow it mechanically. An add is a fresh OPEN drawing fresh tranche → it competes in the same priority pool (§3).
- **Banned:** discretionary averaging-down / adding to a loser with no card rule (the day-trade-leak behavior).

### 3. PRIORITIZE (the $1,500 salary cap — Phase-2 only)
Phase 1 auto-fills every would-fire card (no cap). Phase 2's tranche forces a choice when **would-fire outlay demand > available tranche** that month.
- **Salary unit:** each fill is charged at its **premium / net-debit outlay = the `risk_$` field** (for defined-risk longs, outlay = max loss).
- **Ranking (RULING A):** sort by the card's **qualitative edge bucket** (Strong / Moderate / Small — RISK_SCORING §2) FIRST; within a bucket, tiebreak on **edge_score = expected_return / max_loss**. *No invented precise expected-return — the scoring doc forbids fake p_model precision on convex tails; the bucket is the honest unit.*
- **Independence tiebreak:** a card that **deepens an existing paper exposure** (shared falsifier / same driver — e.g. the 004 Hormuz-concentration flag) ranks **below** an independent one, all else equal.
- **Capital timing (RULING B): first-come, no reserve.** Fund any card clearing the edge bar the moment it fires; if a higher-edge card arrives after the tranche is spent, log it `UNFUNDED-displacement-miss`. Holding capital for a maybe-better setup is not allowed — the misses ARE the lesson.
- **Rejected cards** get a `funding_status`: `UNFUNDED-deprioritized` (lost the edge rank) or `UNFUNDED-displacement-miss` (tranche gone). **This is the whole point of the salary** — at close it answers *did the deprioritized cards underperform the funded ones?* (prioritization calibration).
- **Real fills (RULING C):** the paper desk runs its own priority over **ALL** would-fire cards regardless of your approval; `lane=real` just tags the ones you also executed live. The signal to watch is **divergence** — a `lane=real` card the model would have deprioritized (you funded something it wouldn't), or a deprioritized card you also skipped live (agreement).

### 4. CLOSE (exit)
Exits are **rule-driven from the card, never P&L-driven.** Close when the card's pre-registered exit fires:

| Close trigger | Source | Fill |
|---|---|---|
| **Target / partial** | card §6 (e.g. 004 *"harvest ≥3× fast spike → take half"*) | sell at **BID**, trigger timestamp |
| **Invalidation / kill** | card §5 (e.g. 004 *DGS10 close <4.50 → disarm*) | sell at **BID**, trigger timestamp |
| **Time stop** | card §6 (catalyst-miss date) | sell at **BID** |
| **Roll** | card roll rule, pre-registered only (rule #7) | **close old @ BID + open new @ ASK — two fills, both pay the spread**; new leg draws fresh tranche |
| **Expiry** | option expiry date | **auto-close at intrinsic** (0 if OTM); no fill/spread — it just expires |

- **Partial exits (RULING D):** a partial splits the row into a closed child + an open child (`PB-0002a` closed / `PB-0002b` open) — keeps P&L clean and survivorship intact; `notes` cross-links the pair.

- **Approval-gated arms (RULING E — Will-ruled 2026-08-19, queue row 63, Option 3 of `PAPER_BOOK_RULING-E_would-fire-vs-approval_2026-08-19.md`):** a GATE-class card (arm → [Approve] → fire) whose **objective legs all pass on one session** auto-logs a row at that timestamp — **LOG ALWAYS: the counterfactual record is the product** (the USOARM +45%-mid/negative-at-touch measurement had to be reconstructed by hand; this rule makes it a routine mark). The row carries the token **`[RULING-E approval-pending]`** in `notes` and is **EXCLUDED from the `would_fire_90d` Phase-2 volume gate until Will flips inclusion** — the gate's ≥6 input is Will-pinned (7/24) and the 8/13 counter fix's bias is preserved: *an under-count cannot false-trip the gate.* Rows keep their timestamps, so a later flip to inclusion recomputes losslessly (the RULING-D stamp-keeping precedent). Fill per §Fill rules at the legs-pass timestamp; `will_decision = PASSED` when the arm expires unapproved — that IS the refusal-calibration datum. Founding row: `PB-0005` (USOARM, opened 2026-08-04 13:57 ET, retro-created 8/19 on Will's word — count stays 3/6).
- **Marks ≠ exits.** `paper_book_mark.py` marks OPEN rows to MID on boot cadence; a mark moving closes nothing.
- **NOT an exit trigger:** "it's up/down a lot" with no card rule behind it. Banned.

### 5. Disposition taxonomy (how a row is fully labeled)
- **`will_decision`** — APPROVED / PASSED / NO-DECISION (your call; PASSED = the refusal ghost)
- **`lane`** — paper / real
- **`funding_status`** (Phase-2) — FUNDED / UNFUNDED-deprioritized / UNFUNDED-displacement-miss / NO-FILL-underspecified
- **close-reason tag** — target / invalidation / timestop / roll / expiry (feeds the RISK_SCORING §6 postmortem)

### 6. What TERRY must NOT do (guardrail restatement)
- No discretionary P&L exits — only card rules close a row.
- No averaging-down / adds without a card scale-rule.
- No re-entry after a rule-based stop unless the card **re-triggers fresh** (a stopped card is done; a new would-fire is a new row).
- No mid fills, ever (ask-buy / bid-sell).
- No holding tranche in reserve for a hypothetical better card (Ruling B).

### 7. Worked example — TRY-FIRE-004 through the logic
1. **Open:** 7/20 arm-#2 latched + green-TLT day + ask $0.11 ≤ no-chase $0.12 + liquid → would-fire → auto-open, buy @ ASK $0.11, `entry_basis` stamped (PB-0002). *(Phase 1: no cap. Phase 2: had it competed for tranche that week, 004 is a Small/convex-tail bucket → a Moderate credit-transmission card would outrank it.)*
2. **Hold:** marked to MID each boot ($0.135 as-of 7/23); marks don't close it.
3. **Close — whichever fires first:**
   - *Harvest:* TLT gaps and 77P ≥ 3× ($0.33+) → sell HALF @ BID → split `PB-0002a` (closed) / `PB-0002b` (open).
   - *Disarm:* official DGS10 close <4.50 → close full @ BID (invalidation).
   - *Expiry:* neither fires by Sep-30 → auto-close at intrinsic (0 if TLT>77) — the grind path pays $0.

---

## Post-build refinements (TERRY, next boot — non-blocking)
Surfaced by the 7/19 build verification (PROME): (1) ~~**live marks need `.venv/bin/python`** (yfinance), not bare `python3` — the mark helper degrades to UNMARKED under bare python; boot step 5b notes it, but confirm your boot invokes the venv.~~ ✅ **OBSOLETE 2026-07-30 — the tools SELF-HEAL now.** `paper_book_mark.py`, `chain_fetch.py` and `snapshot.py` all re-exec under `.venv` when yfinance is missing, so the bare `python3` form works regardless of invocation (and works directly on any box where yfinance is already in base python). They exit **non-zero with the fix printed** when the heal is unavailable — they no longer silently degrade. *(Flagged by RAV: this paragraph contradicted the shipped behaviour.)* (2) **Seed PB-0001 `entry_basis` says "live pull"** for a 7/17 timestamp — tidy to "last-close pull" (the $0.11 value is the correct documented basis) and confirm the **Sep-30** expiry matches the ZONE 2/3 card (arm ladder was Sep-18; the 7/17 re-fire crash-tail may legitimately differ — just verify).

## Phase 2 — SALARIED DESK (deferred behind the volume gate — trigger now pinned)
Notional bankroll (monthly salary tranche), prioritization, running equity curve. **Build ONLY once the volume gate trips** (Sharpening 4) — until prioritization actually binds, it measures nothing. Clearly labeled SEPARATE and bound by the same-rules guardrail.

**Pinned gate (2026-07-24, Will-approved):**
- **Volume trigger:** trailing-90-day would-fire count **≥ 6 cards** (from `PAPER_BOOK.tsv` `opened`). Below it, prioritization can't bind; at/above it, choosing which cards get tranche capital is a real test. `paper_book_mark.py` prints `would-fire (90d): N/6` each boot.
- **Salary tranche: $1,500/month notional — SET by Will 2026-07-24** (= 3 cards at the $500/card cap). Binds once would-fire runs **≥4 cards/month** — modestly above the 6-card/90d gate, so a normal month can fund two independent setups while a busy month still forces a rejection. *(For contrast: the rejected "$10k" example funds 20 cards/month and never binds; a $1,000 tranche would bind exactly at the gate. Will chose $1,500 for the extra headroom.)* Still **paper** — no real capital; the desk activates only when the volume gate trips (currently 2/6).
- **Cadence:** monthly tranche, top-up on the 1st; unspent capital does NOT roll (a salary is use-it-or-lose-it opportunity cost, which is the whole point of the test).

## Standing guardrails
- **Subordinate to the thesis work** (same rule as the day-trading loop) — never displaces core construction.
- **Never an argument for looser real deployment** — it calibrates process; it is not a license to size up. Keep everything clearly labeled PAPER.
- **Auto-fill measures card quality, not a P&L Will endorsed** — the shadow book fills trades independent of the approval gate; that is the point, and it must be labeled so no one mistakes shadow P&L for a real or approved return.
