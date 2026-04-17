# HENRY MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis, STATUS, or LESSONS and delete, never just accumulate.*

---

## Feedback
*Will's guidance on how HENRY should work. Add when corrected or when an approach is validated.*

- [2026-04-17] Always pull fresh EOD levels before closing the week, even when intraday STATUS looks stable — partial retracements during the session are the tell (e.g., Apr 17 Brent closed $2.50 off intraday lows, KRE gave back half its AM Hormuz-beta bid).

## Findings
*Non-obvious observations that persist across sessions but don't belong in STATUS, thesis, or LESSONS.*

- [2026-04-17] When oil shocks reverse on unilateral headlines, regional-bank beta (KRE, APO) gives back most of the AM rally by close — the "conviction" bid is small vs the beta bid. Use the EOD KRE/APO print as a tell on whether the headline stuck.

## References
*Where to find things that aren't in the boot path.*

- [2026-04-17] Live market refresh: `source .venv/bin/activate && python3 FORGE/tools/market-data/fetch.py price ^GSPC ^VIX ^SKEW ^VIX3M KRE JPY=X ^TNX TLT APO HYG LQD BZ=F CL=F`. Note: `SPX`/`VIX` alone fail (delisted in yfinance), use `^GSPC`/`^VIX`.
- [2026-04-17] HY OAS daily refresh: FRED series `BAMLH0A0HYM2`, 1-day lag (Fri close prints Mon AM).

---

## Session Notes

### CHANGES SINCE LAST SESSION
*Populated at boot during market refresh — what moved offline.*

- (Apr 17 EOD session — first MEMORY.md, no prior handoff.)

### LAST SESSION (2026-04-17 Fri EOD)
- Booted fresh instance after /clear. Read STATUS.md (timestamp ~10:40 ET) + LESSONS.md.
- Pulled EOD levels via FORGE fetcher: SPX 7,123.77 (+1.17%), VIX 17.76 (did NOT break 17), SKEW 140.74 (holds), Brent $90.67 (closed off intraday lows, -8.77% vs -11.3% AM), KRE $70.38 (gave back $0.55 from AM), APO $124.28 (faded $2.20).
- Updated STATUS.md: header timestamp → EOD, market table expanded with Δ-vs-AM column, thresholds refreshed, BOTTOM LINE rewritten with three EOD tells.
- Committed `fed1d713` (HENRY STATUS only). **Push deferred** — POLLY (CARL sub-agent) has uncommitted work in `AGENTS/CARL/sub_agents/POLLY/workbook/`; remote is behind-2 (Prome root cleanup `2cd5c74e`, BRENT Friday data `1f389c05`). Neither remote commit touches POLLY paths, so rebase would technically be safe, but following CLAUDE.md conservative rule.
- Created MEMORY.md (this file) — adopted SAM's closeout template.

### NEXT SESSION (Monday Apr 20, 2026)
1. **Push pending.** If POLLY is committed, do scoped stash/pull/pop → `git push`. If not, flag to Will.
2. **🟢 HY OAS Apr 17 settle print** (FRED AM). <280 = compression continuing → thesis amber watch tightens toward invalidation. >290 = reversal, complacency break incipient.
3. **🟡 Weekend Brent gap.** Any fresh US-Iran escalation/de-escalation headlines over the weekend repricing WTI/Brent Monday open. Hormuz "completely open" was unilateral Iranian — watch for US counterparty response.
4. **🟠 Tanker-tracking signal (HAWK/BRENT).** Physical flow confirmation — are tankers actually reaching Iranian ports or still blocked? Per LESSONS "unilateral ≠ bilateral" rule.
5. **🔴 Tue Apr 21 AMC — OZK + WAL Q1 (binary vol event).** Positioning asymmetry into catalyst: HF short-cover whipsaw (GS Prime) + financials positioning at multi-year lows (DB -1.5 to -2z). Both tails fattened. Review TRADE.md if spawned for trade task.
6. **🟠 Tue Apr 21 — Retail Sales Mar (rescheduled).** First consumer print post-CPI 3.3%. Control group is the GDP feed.
7. **Week ahead:** Apr 23-24 BOJ, Apr 28-29 FOMC, Apr 30 PCE+GDP Q1.

### INFRASTRUCTURE CHANGES (persistent)
- MEMORY.md created — adopted SAM's CHANGES SINCE / LAST SESSION / NEXT SESSION template. HENRY/CLAUDE.md updated to reference at boot/closeout.
