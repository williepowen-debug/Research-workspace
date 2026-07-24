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
| Bankroll size / salary cadence | **N/A for Phase 1** — the shadow book needs no bankroll; it tracks would-fire cards to close. Bankroll is a Phase-2 concern. **Phase-2 gate now quantitatively pinned (2026-07-24, Will-approved) — see §Phase 2 / Sharpening 4; no live salary set until volume nears the gate.** | Phase 1 measures card quality, not prioritization — no capital constraint needed yet. |
| Shadow-only vs straight to salaried | **Shadow-only (Phase 1).** Salaried desk deferred behind a quantitative volume gate. | The prioritization test can't bind at ~2-3 cards/month (Sharpening 4). |
| Auto-fill on trigger vs approved-only | **Auto-fill on trigger — regardless of Will's approval.** | The *only* version that generates a record: the whole problem is 0 approvals. Approved-only would inherit the same near-zero volume. Labeled "card-quality record, not a P&L Will endorsed." |

### The 6 sharpenings (baked into the build spec below)
1. **Auto-fill on trigger is THE design decision, not a detail.** Every card that reaches would-fire state fills the shadow book *independent of the approval gate* → measures card quality. This is what actually attacks PAT-028.
2. **Capture the refusals — they're the best data.** The only product so far *is* the refusals. Every row carries a `will_decision` field (APPROVED / PASSED / NO-DECISION); the **PASSED subset is the counterfactual "ghost"** — at close it answers *did the discipline to say no save or cost money*. One table, a decision column (cleaner than a separate lane). Explicitly NOT a P&L that argues for looser deployment — it calibrates the pass decision.
3. **Fill rule needs one more tooth.** Ask/bid still flatters at size and widens at the open. Add: (a) fill at the **trigger timestamp**, not close; (b) a **slippage penalty** for wide-spread names (bid/ask > 15% of mid → fill one tick worse than the posted side, or a fixed haircut); (c) record `entry_basis` (exact quote + timestamp) so every fill is auditable; (d) trigger while market closed → fill at next-open, never mid.
4. **Defer Phase 2 behind a quantitative volume gate.** Prioritization is only testable when would-fire setups *exceed* bankroll capacity. Build the salaried desk ONLY once the trailing would-fire rate exceeds a plausible salary tranche — otherwise it's complexity measuring nothing. **★ Gate pinned 2026-07-24 (Will-approved "pin the # / defer live salary"):** Phase 2 opens when **trailing-90-day would-fire count ≥ 6 cards** (≈ ≥2 would-fire/month sustained a full quarter — the point where a monthly tranche can no longer fund them all and *choosing* becomes a real judgment test). Measured from `PAPER_BOOK.tsv` `opened` timestamps; `paper_book_mark.py` surfaces the running `would-fire (90d): N/6` count at boot as an early-warning. **No live salary is set now** (at N=2 it would measure nothing) — only the trigger is armed.
5. **Small-N honesty.** A clean shadow book gives *directional* feedback, not significance, for a long while. No calibration/Brier scoring and no decision acts on the record until **N ≥ 10 closed positions per lane**; until then rows carry `notes = "N-too-small"`. Guards against over-reading an early lucky/unlucky streak.
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

## Post-build refinements (TERRY, next boot — non-blocking)
Surfaced by the 7/19 build verification (PROME): (1) **live marks need `.venv/bin/python`** (yfinance), not bare `python3` — the mark helper degrades to UNMARKED under bare python; boot step 5b notes it, but confirm your boot invokes the venv. (2) **Seed PB-0001 `entry_basis` says "live pull"** for a 7/17 timestamp — tidy to "last-close pull" (the $0.11 value is the correct documented basis) and confirm the **Sep-30** expiry matches the ZONE 2/3 card (arm ladder was Sep-18; the 7/17 re-fire crash-tail may legitimately differ — just verify).

## Phase 2 — SALARIED DESK (deferred behind the volume gate — trigger now pinned)
Notional bankroll (monthly salary tranche), prioritization, running equity curve. **Build ONLY once the volume gate trips** (Sharpening 4) — until prioritization actually binds, it measures nothing. Clearly labeled SEPARATE and bound by the same-rules guardrail.

**Pinned gate (2026-07-24, Will-approved):**
- **Volume trigger:** trailing-90-day would-fire count **≥ 6 cards** (from `PAPER_BOOK.tsv` `opened`). Below it, prioritization can't bind; at/above it, choosing which cards get tranche capital is a real test. `paper_book_mark.py` prints `would-fire (90d): N/6` each boot.
- **Placeholder salary tranche: ~$1,500/month notional** (= 3 cards at the $500/card cap) — **deliberately set BELOW the would-fire $-demand at the gate so prioritization actually binds.** *(The old "$10k" example was too loose: at $500/card it funds 20 cards/month and would never bind at any realistic desk volume.)* **Placeholder only — Will confirms the exact figure when volume nears the gate** (that's the "defer live salary" half of the 7/24 decision).
- **Cadence:** monthly tranche, top-up on the 1st; unspent capital does NOT roll (a salary is use-it-or-lose-it opportunity cost, which is the whole point of the test).

## Standing guardrails
- **Subordinate to the thesis work** (same rule as the day-trading loop) — never displaces core construction.
- **Never an argument for looser real deployment** — it calibrates process; it is not a license to size up. Keep everything clearly labeled PAPER.
- **Auto-fill measures card quality, not a P&L Will endorsed** — the shadow book fills trades independent of the approval gate; that is the point, and it must be labeled so no one mistakes shadow P&L for a real or approved return.
