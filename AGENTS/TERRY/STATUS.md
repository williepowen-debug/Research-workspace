# TERRY STATUS
**Updated:** 2026-07-16 Thu (teams session w/ PROME): **TRY-FIRE-004 ARMED — first card to reach ARM.** arm-#2 (VX-BND-05 10Y 5-close sustain ≥4.50) FIRED — 5-of-5 completed Mon 7/13 (TERRY-verified FRED DGS10: 7/7 4.55·7/8 4.56·7/9 4.54·7/10 4.56·7/13 4.62·7/14 4.58). Arm packet → Will [Approve]. VIO-116 rates-vol hedge shape memo delivered (folds into TRY-FIRE-004, no separate hedge). arm-#3 (May TIC) grades today 4pm — template staged. · **Status:** 🟠 ARMED (1 card armed, still 0 fired live — awaits Will [Approve] + live marks)
**Agent:** TERRY — trade construction / tactical execution discipline. Owns the ACTION/card side; never executes. Detection = LIQUID/SENTRY.

> Durable mandate + lessons → `MEMORY.md`. Session-end procedure → `CLOSEOUT.md`. Role/start-here → `README.md`. Risk gates → `RISK_SCORING.md`.

## Live state

**Standing rules (Will 2026-06-26):** fresh capital deploys ONLY on a fired trigger (no mechanical reshape; dry powder). **Max loss = $500 per card.**

| Capability | State | Note |
|---|---|---|
| Trigger→card toolchain | 🟢 BUILT & TESTED | the minutes-not-hours path is live end-to-end |
| `scripts/chain_fetch.py` | 🟢 built, selftest PASS, live-validated | live option-chain CLI; marks matched the bank-put proposal exactly |
| `scripts/grade_print.py` + `grade_config.json` | 🟢 built, selftest PASS | Q2 print grader; 3 mis-grade traps as hard guards; `--tally` rolls path (a)/(b)/(c) |
| Fire cards | 🟢 staged, **0 fired live** | `TRADE_CARD_TEMPLATE_FIRE.md` + **4** skeletons (HY≥280 / WAL-EGBN / monoline COF-SYF-ALLY / **duration-TLT-put, flow-gated**), $500 budget locked · side-by-side: `setups/FIRE_CARDS_LADDER.md` |
| Day-trading review loop | 🟢 live · **SIDE tool** | dry-powder feeder, **subordinate to the thesis system** (Will 6/27) — must not displace the core work. S3 6/24–26 **−$3,969** (wiped S2; cumulative −$1,017) = funding nothing; plug the leak, keep it small. `daytrading/` |
| `SIGNALS.tsv` context ledger | 🟢 NEW, live | trade-construction context (WALTER INFO / my chart obs / thesis-owner timing); decay-tracked, boot-surfaced. **NEXUS regime PIN = STALE (6/16 pre-FOMC), refresh owed** |
| `inbox/WILL/` drop zone | 🟢 NEW, live | Will's reserved trading-data drop; raw gitignored (stays local), boot-surfaced; feeds the day-trading review |
| Older scripts | 🟢 selftested | boot.py (now surfaces signals + drop zone), snapshot.py, risk_calc.py, chain_parse.py, csv_pnl.py |
| Live thesis trade cards | ⚪ none fired | fire cards await a real trigger; POSTMORTEMS template-only (no closed trade yet) |
| Position truth | 🟡 from Will/FORGE only | existing book in FORGE/STATUS; pull live before any fire-card sizing |
| Risk unit for Will | 🟡 open | $/%/R preference unresolved (see MEMORY Standing Decisions) |

## What's pending
- **2026-07-16 (ARMED):** TRY-FIRE-004 **ARMED via arm-#2** (10Y 5-close sustain, 5-of-5 complete Mon 7/13, FRED-verified independently this session). Registered consequence executed → arm packet `outbox/2026-07-16_to-PROME_try-fire-004-arm-packet.md` → Will [Approve]. **Terry fill-verdict = CONDITIONAL:** live TLT Sep-18 put marks were unavailable at 09:32 ET (bid/ask 0.00, stale 7/15 last-trades, broken IV) → **live re-pull required before fill (rule #4)**; TLT RED and at range lows → today's open is a rule-#6 chase (prefer green-day/scaled entry); deep-OTM (74–77 strikes) = low-delta tail. arm-#1 DEAD (7/9); **arm-#3 (May TIC) grades TODAY 4pm** — template `setups/ARM3-TIC-grading-template_2026-07-16.md` staged (⚠️ grade the CARD's net-TRANSACTIONS wording, not GATES.tsv "holdings-down"). VIO-116 rates-vol hedge → shape memo `outbox/2026-07-16_to-PROME_vio-116-rates-vol-shape-memo.md`: **no stand-alone shape** (MOVE round-tripped: spiked **77.77 Mon 7/13** [investing.com daily, web-verified] → 68.48; folds into TRY-FIRE-004). **NOTE:** an interim F3→F1 attribution correction was **RETRACTED** — the yf 1h-bar was mislabeled 1 day; the spike was 7/13, so on 7/13 both 10Y 4.62>4.60 AND MOVE 77.77>70 → **F3 fired cleanly, PROME's original GATES attribution is correct.** See `setups/FLOW-TRIGGER_duration-TLT-put.md`.
- **Inbox deferred (non-arm, 7/16):** `2026-07-03_from-DAEDALUS_utility-firming-sweepAB-pat031-drift` + `2026-07-09_from-PROME_hban-oct16p-thesis-stub` + WALTER/ WILL/ subdirs — none arm-critical; process next normal session. `2026-07-01_firetime-freshness-check` = integrated (ran `firetime_check.py` on the card, clean).
- **Awaiting a fired trigger** to exercise a fire card (HY OAS ≥280 sustained, or a Jul 16–30 print grading as transmission). Detection = LIQUID/SENTRY.
- **NEXUS regime PIN stale** — `SIGNALS.tsv` carries NEXUS's 6/16 *pre-FOMC* read; refresh owed (flag in `outbox/2026-06-27_to-NEXUS_post-fomc-reanchor-flag.md`). Will refreshing NEXUS soon → re-stamp the PIN then.
- **Day-trading S3 carries:** (1) request a timestamped order export (confirms RH auto-close + closes churn/cancel gap); (2) Monday-mark the open book — WAL 9/18 75P (**THESIS-scope → FORGE, not day-trade**), WEN 7/2 8.50P.
- **Positioning backdrop (current read):** crowded-long / froth → squeeze risk **elevated on any short**. Evidence + decay in `SIGNALS.tsv` (boot surfaces it; don't re-list rows here). Durable level map: GS-CTA SPX **7,352 / 7,063 / 6,642** — mechanical-sell window opens <7,352.

## Open questions for Will
- Preferred default risk unit: $ max loss / % portfolio / R? (Day-trade Rule 3 cap needs a number to be enforceable.)
- Track every considered setup, or approved/rejected only?

## Guardrails
- No execution; Will approval on every trade. No stale prices/option marks in cards (pull live at fire). No position triage without broker/Will truth. No macro re-underwriting — cite the thesis owner.
