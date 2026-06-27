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
- **Day-trading (Session 2, 5/1–6/23):** realized +$2,951.67; 0 shorts; leak = −$2,793 walked-to-$0-expiry;
  puts +2,347 vs calls +604; QQQ 0DTE +3,044 engine. Detail in daytrading/.
- **No closed Terry-reviewed thesis trades yet** — POSTMORTEMS.md is template-only until one closes.
- **Routed positioning/timing INFO lands in `SIGNALS.tsv`, not STATUS/MEMORY** (Will 6/27: "store in lasting memory, don't put everything of value in STATUS"). Decay-tracked ledger (as_of/decay/conf/status/bears_on); `boot.py` surfaces active rows + flags any >21d for re-verify/retire. STATUS keeps only a one-line current read + the durable level map. New WALTER/INFO signal → add a row; recall the cluster at fire-time when sizing.

---

## Current Session (2026-06-26 — cluster member under Prome)

**Delivered:** audit (trigger→card readiness) + built the trigger→card toolchain, all in AGENTS/TERRY/:
- `scripts/chain_fetch.py` — live option-chain CLI (selftest PASS; validated vs proposal marks).
- `TRADE_CARD_TEMPLATE_FIRE.md` + `setups/PRICE-TRIGGER_HY280_regional-put.md` + `setups/PRINT-TRIGGER_WAL-EGBN-build.md`.
- `scripts/grade_print.py` + `grade_config.json` — print grader, 3 traps as hard guards (selftest PASS).
- `.gitignore` (scripts/.cache/ + grades/). Arch peer-review vs LIQUID → PROME/cluster/.
- This Fix-B durable layer: MEMORY.md + CLOSEOUT.md created; STATUS.md rewritten to live state.

**Status (truth-up 6/27):** all delivered — committed (`1fa1ca23` + `d9498dfd`) and pushed via WALTER's push-train; synced 0/0. $500/card set by Will.

---

## Next Session

1. **No cards fired live yet** — fire cards are staged, waiting on a real LIQUID/SENTRY trigger (HY≥280 or a Jul print).
2. **Jul print week (16–30):** when a print lands, run `grade_print.py NAME …` then `--tally`; if transmission grades, the PRINT-TRIGGER skeleton is the card.
3. **HY≥280 sustained:** PRICE-TRIGGER skeleton → fill ZONE 2 → present.
4. **Carry:** resolve Will's risk-UNIT question; consider a hy_oas_watch-style detector handoff is LIQUID's, not mine.
