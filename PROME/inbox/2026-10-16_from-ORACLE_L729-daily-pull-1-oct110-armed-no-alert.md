# ORACLE → PROME — DOCKET L729 daily pull 1 (Fri 10/16): the October $110 leg is ARMED at 20.5%, no Alert · letter fixed · inbox 5/5

**ORACLE · 2026-10-16 13:36–13:5x ET (from `date`) · spawn by prome-ac under WQ-184 L0, Tier 1, $0, no trade.** Runtime: Claude Code Agent-tool desk, Opus. Root/desk instructions read explicitly. Corrections check rc=1 → receipted → rc=0.

## 1. The read (D:L729)

| Field | Value |
|---|---|
| Read | Polymarket `will-wti-reach-110-in-october-2026` (id 4936102) YES **20.5%** · ODDS_LOG row **2026-10-16T17:36Z** (first pull of ET 10/16) |
| Liquidity | **$34,832** ⇒ **QUALIFIED** (≥ $5K) · vol $125.6K · Gamma d1 +6.0, d7 +10.5 |
| Run | post-switch reads 10/14 9.5 (2026-10-15T03:56Z) · 10/15 9.0 (12:39Z) · 10/16 20.5 ⇒ **run 3, ARMED** |
| Band state | **No Alert, no Critical** (every read < 40.0). In the letter's words: armed run of 3 qualified reads, none ≥ 40.0 |
| Spot (context) | CME CLZ26 proxy **$98.64** (+2.22%, `fetch.py` 17:37Z) ⇒ $110 is +11.5%; the leg resolves on ICE |
| Next read | **Mon 2026-10-19**, first pull of the ET day (Fri→Mon = no gap under R2) |
| Ledger | `AGENTS/ORACLE/workbook/V5_OCT110_READS.tsv` (one row per business-day read, back to 9/28) |

⚠️ **This differs from PROME's 10/15 framing ("nothing is ARMED today", "the FIRST of the daily pulls").** The letter counts READS, not spawns: under O3 the first pull of ET Wed 10/14 was the Will-launched session's 2026-10-15T03:56Z row (23:56 EDT, post-switch by UTC per R3), recovered and verified 10/15 (commit 5eae08a1c), then 10/15 12:39Z. Three consecutive qualified business days ⇒ armed today. If PROME or Will reads the letter as counting from the first L729 spawn instead, run = 1 and nothing is armed; that changes no fire today.

⚠️ **The leg moved +11.5pp in 29h (9.0 → 20.5, qualified book)** — the charter's >10pp/48h PROME-triage line. A higher chance of touching $110 is a price-event signal, not lost supply (letter §6); BRENT/HAWK own the reality.

## 2. Inbox drain (5/5, logged in `AGENTS/ORACLE/board_log.tsv` 2026-10-16T17:41Z, moved to `processed/`)

| Packet | Disposition |
|---|---|
| `2026-10-15_from-PROME_WQ314b-WQ439-WQ440-RULED.md` | **acted.** VX.tsv: ORC-04 bands encoded (🟡); ORC-07 48h-pair-only (WQ-439 A), graded 🔴 on a 29h pair — PM Fed NO-change-at-Oct 66.0 → 86.5 (+20.5, liq $549.6K); ORC-08 RETIRED SPENT, Polymarket trigger venue (WQ-440 a+b). Successor → `PROME/inbox/2026-10-16_from-ORACLE_ORC08-successor-october-fomc-PROPOSAL.md` (ask for Will; not encoded) |
| `2026-10-15_from-PROME_WQ314b-second-read-…` | **acted** — see §3 |
| `2026-10-15_from-PROME_crash-recovery-residue-WQ436.md` | **acted earlier** (10/15, commits 5eae08a1c + 91ab67173); only the file move was owed |
| WALTER `SIG-W-20261015-013` | noted — superseded by -002 |
| WALTER `SIG-W-20261016-002` (CORRECTION) | **acted** — COR-20261016-02 receipted NO-OP: no ORACLE artifact cited -013 |

## 3. The second read's three ❌ — fixed at the letter (`AGENTS/ORACLE/analysis/2026-10-09_wq314b-v5-observation-and-reset-rules.md` §7)

- **(a) Settlement text quoted VERBATIM** (§7.1; Gamma `/markets/4936102` 2026-10-16T17:37Z; description sha256 `bfff6022b8048b8840406ce693acc027d9c7c383e9c2b7f13fa27a61f91c0b62`). It settles the ≥$110 tie (inclusive), the Active-Month definition, the worked example, the first session and the fallback scope (§7.2).
- **(b) ❌37 fired state at the Nov pin:** held and carried into November, re-graded on November's first 3 qualified reads (R4 and §5.2 rewritten; O8 already said a reset never clears a fired state, so this removes the contradiction in O8's direction). **Thin/gap during clearing:** restarts the clearing count (O8, R1, R2).
- **(c) ❌23** n=7 = the April–October events (created 25 Mar – 25 Sep, re-read at Gamma today) · **❌43** pointer → `inbox/processed/`.
- **C1 claim:** no level, operator or instrument moved; ❌37's resolution is the reading O8's own text compels, and ⚠️ **PROME should verify that claim** — the other reading (state ends at the pin) would be the consequence change.
- **Declined (move a consequence ⇒ Will via PROME):** the Critical→Alert downgrade path, and whether a Pyth ≥$110 candle seen before Gamma's close fires Critical. Neither can bite today (20.5%). Holiday calendar, gap counting and half-tie rounding are moot through 10/30 (§7.4).

## 4. Other priced odds (venue + timestamp)

| Market | Read | Depth | Stamp |
|---|---|---|---|
| PM Fed HIKE at Oct mtg (meeting-specific) | **12.5%** (31.5 on 10/15 12:39Z) | vol $10.0M · liq $352.8K | 2026-10-16T17:36Z |
| Kalshi KXFED-26OCT >4.00 | **16.0%** (Δprev −8) | OI 72.6K | 17:39Z |
| PM Fed HIKE at Dec mtg | 77.5% | liq $123.2K | 17:36Z |
| PM US–Iran next senior meeting by 12/31 | 35.5% | liq $47.6K | 17:36Z |
| PM US ends Iran blockade by 3/31/27 | 58.5% | liq $96.6K | 17:36Z |
| PM US invade Iran <2027 | 15.5% | vol $74.4M | 17:36Z |
| PM any US bank fails by 12/31 | 84.5% (42.0 on 10/15) ⚠️ THIN $3.0K liq | not marked | 17:36Z |

The Fed figure supersedes what NEXUS/LIQUID hold from 10/15 (~30); LIQUID packet sent. The bank jump may be traders on WALTER's false "fourth failure" item; one thin print, ≥3-day re-check.

COMPLETION
STATUS: DONE — D:L729 pull 1 of 11 read at 2026-10-16T17:36Z: Oct $110 20.5%, liq $34.8K QUALIFIED, run 3 ARMED, no Alert/Critical (all <40.0); inbox 5/5 consumed
CHANGED: ORACLE letter §7 + O2/O8/R1/R2/R4/§5.1–5.2 · VX.tsv ORC-04/07/08 · KB-ORC-104/105 · V5_OCT110_READS.tsv (new) · ODDS/KALSHI logs · STATUS/SCRATCH/NEXUS_BRIEF · board_log · corrections receipt · 5 packets → processed
RESULT: WQ-314b/439/440 encoded; ORC-07 🔴 on a 29h pair (PM Oct NO-change +20.5); PM Oct hike 12.5% / Kalshi 16.0 (17:36–17:39Z); second read's 3 ❌ fixed, settlement text verbatim
GAPS: ARMED depends on counting the 10/14 23:56 EDT read (PROME framed 10/16 as first) · spread tool, coverage, history not run · signed Kalshi lane still unverified (laptop)
WILL_NEEDS: VX-ORC-09 Oct-FOMC successor proposal (PROME/inbox/2026-10-16_from-ORACLE_ORC08-successor-october-fomc-PROPOSAL.md) · Critical→Alert downgrade + touch-before-close definitions (letter §7.4)
FOLLOW-UP: D:L729 read 2 Mon 2026-10-19 · PROME verify the C1 claim on ❌37 · Nov $110 pin ~10/25 · bank-any thin re-check ≥10/19
