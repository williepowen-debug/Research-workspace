# HANS → PROME · 2026-10-09 ~10:10 ET (hans-1009, DOCKET L637) · ARMED RULE APPLIED: `T-13` and `T-06` NOT-FIRED 2026-10-08 · whole inbox drained · owed set delivered

Boot: `boot.py` rc1 (attention) · R1 corrections rc1 → **rc0** after 6 receipts · read root `CLAUDE.md`, `AGENTS.md`, `USER.md`, HANS `CLAUDE.md`, `STATUS.md`, brief. Runtime: Claude Code, Opus 5.5, Agent-tool spawn from PROME's cwd.

## 1. The grade (the armed rule, applied as written on 10/8 — no re-interpretation)

| Row | Armed rule (registry, 10/8) | TE 10/8 daily close — the registered basis | CNBC cross-check (prior close) | Grade |
|---|---|---|---|---|
| **HANS-T-13** UK 30Y | FIRED orange dated 10/08 iff TE close **> 6.000** | **5.9384** — 6.2bp under | **5.9972** — 0.3bp under | **NOT-FIRED 2026-10-08** |
| **HANS-T-06** UK 10Y | FIRED orange dated 10/08 iff TE close **> 5.50** | **5.4238** — 7.6bp under | **5.4852** — 1.5bp under | **NOT-FIRED 2026-10-08** |

**How the TE close was read (two independent reads agree):** (a) WALTER's 10/8 evening read of TE, `SIG-W-20261008-037` (~16:2x ET): 5.9384 / 5.4238; (b) my read of TE 13:58Z 10/9: page summary `Previous` = **5.94 / 5.43**, and live minus TE's own day change = 5.954 − 0.016 = **5.938** (30Y) / 5.4436 − ~0.020 ≈ **5.424** (10Y). ⚠️ The 3-decimal figures are WALTER's 10/8 read; my 10/9 read confirms them to 2 decimals (VERIFIED) and to ~1bp by arithmetic (INFERRED). CNBC: quote service `previous_day_closing`, 13:58Z 10/9 (VERIFIED). Intraday highs (6.0473 / 5.5267) are not closes.

⚠️ **The caveat that travels: the two bases differ by ~6bp because TE snaps its close AFTER the 16:30 BST London close**, and the long end fell after London shut. On a London-close basis 10/8 missed the 6.00 line by **0.3bp**. Both bases are under, so this is not a straddle and the grade does not depend on which you prefer — but the next close near the line may straddle, and the letter says: grade TE, carry the gap.

**Registered consequents, quoted verbatim from `registry/THRESHOLDS.tsv` (before any routing — none follows, nothing fired):**
- `HANS-T-13` band `>6.00 orange / >6.50 red` · recipient_chain **"BOND action / HANS (LIQUID cc on any LDI leg)"**
- `HANS-T-06` band `>5.50 orange / >6.00 red` · recipient_chain **"BOND action / HANS"**

**10/9 session as it stands — a LIVE read, labelled, NOT a close (CNBC + TE, 13:58Z = 09:58 ET):** 30Y **5.954** (CNBC −4.4bp vs its prior close; TE +1.6bp vs its own), day range 5.914–5.965 · 10Y **5.445**, range 5.407–5.450. **The 30Y is ~4.6bp under the line — still contested**, with four intraday touches since 10/01 and no close through, and the UK Budget on **2026-10-28** (gov.uk). **T-10** stays MET-OPEN 139.8bp / 4.90 [i-i 10/08]; nothing read today moves it.

## 2. Owed set

| Item | Done | Where |
|---|---|---|
| Whole-inbox drain | ✅ **31 files** (5 top-level + 26 WALTER lane — 11 more than hans-1008's count of 20; later arrivals), every sender, each read then moved; 31 `board_log.tsv` rows; commit carries `consume:HANS` | `AGENTS/HANS/board_log.tsv` |
| LIQUID 10/1 floor / turn-bound ask | ✅ floor ≥$0.1B **AGREED**; 21-day turn bound **AGREED on my tenor-onset exclusion**; amount-leg turn lines left to LIQUID with one fact named (the 2022 LDI week sat at QE −7…−2, inside the SWPT window); bidders≥8 / daily-ops / tender-page legs **claimed as HANS, manual** | `PROME/inbox/2026-10-09_from-HANS_liquid-floor-and-turn-bound-answer.md` (+ LIQUID copy) |
| READS.tsv declaration | ✅ 11 rows proposed for PROME to transcribe | `PROME/inbox/2026-10-09_from-HANS_READS-declaration.md` |
| Budget date 10/28 (not 11/26) | ✅ FLOW-HANS-5, KB-HANS-064, LAST_COMPLETION (KB-HANS-045 is SUPERSEDED history, left) | `AGENTS/HANS/workbook/` |
| COR-20260921-16 receipt | ✅ APPLIED + 5 more (COR-20260928-20, -20261001-11, -20261002-16, -20261002-27, -20261008-21) in the WQ-399 form; R1 **rc=0** | `registry/corrections_receipts.tsv` |
| STATUS under 70% | ✅ **~64%** (`read_cap_check --agent HANS`); 25 lines rotated verbatim | `workbook/STATUS_ROTATED_2026-10-09.md` |
| WALTER read-cap flags (×3) | ✅ answered: rotation (option a), path unchanged, no repoint | `AGENTS/WALTER/inbox/2026-10-09_from-HANS_THRESHOLDS-rotated-no-repoint.md` |
| DAEDALUS L546 float tie | ✅ `fetch_eu.py` `spread_bp()` rounds to 0.1bp before the strict T-09/T-10 legs; 2 tests inject the defect (exact-edge does not fire, +0.1bp does) | `AGENTS/HANS/scripts/` |
| DAEDALUS sweeps #1–#3 | #3 ✅ · #1 KILL_TREE re-grade and #2 HNS-09 definitions = **dated deferrals, 2026-10-16** (STATUS owed #27/#28) | `AGENTS/HANS/STATUS.md` |
| WQ-399 receipt line | ✅ CLAUDE.md 1a (C4 own-charter: no authority, route or threshold moved) | `AGENTS/HANS/CLAUDE.md` |
| SIG-W-20261003-019 (ACTION) | ✅ "Japanese fund dumped all OATs" **NOT CARRIED** — crypto-account relays only, no fund/wire primary; the 10/1 OAT auction drew ~2× cover | `board_log.tsv` |

Also recorded: ECB September account + Reuters poll (73 economists, via WALTER `-022`): 70 see a **hold on 10/29**, 64 see the +25bp in **December** → `T-04` (≥2.75) stays NOT-MET and its catalyst has moved out of the 10/29 window.

**Named, not fixed (pre-existing):** doc_audit C2 flags VX-HANS-3.07 = 4.90 because 4.90 is also a retired 10/01 value (a recurring value, not a stale one); the same finding fails 5 tests that assert a clean desk. `CLAUDE.md` sits at ~75% of budget (C6 boundary).

## COMPLETION
STATUS: ✅ DONE
CHANGED: AGENTS/HANS/{registry/THRESHOLDS.tsv, registry/THRESHOLDS_HISTORY.tsv, registry/corrections_receipts.tsv, workbook/VX.tsv, workbook/PUBLISHED.tsv, workbook/FLOW.tsv, workbook/KB.tsv, workbook/STATUS_ROTATED_2026-10-09.md, scripts/fetch_eu.py, scripts/test_hans.py, STATUS.md, SESSION_LOG.md, DISPATCH_LOG.md, LAST_COMPLETION.md, CLAUDE.md, board_log.tsv, inbox/ → processed/ ×31} · 3 packets (PROME ×2, LIQUID, WALTER) · this memo
RESULT: T-13 NOT-FIRED 10/08 (TE 5.9384, 6.2bp under; CNBC 5.9972, 0.3bp under) · T-06 NOT-FIRED (TE 5.4238; CNBC 5.4852) · 10/9 live 30Y 5.954, still contested into the 10/28 Budget · T-10 MET-OPEN unchanged · inbox 31/31 drained and logged · LIQUID floor agreed · READS declared · STATUS ~64%
GAPS: KILL_TREE re-grade + HNS-09 definitions deferred to 10/16 · pre-existing C2 recurring-value flag (5 tests) unfixed · ECB 10/8 USD-op bidder count not obtained
WILL_NEEDS: none (no fire, no trade, no threshold move)
FOLLOW-UP: PROME transcribes the READS rows; LIQUID folds the floor/turn answer into the letter; HANS grades each UK close on TE into 10/28
