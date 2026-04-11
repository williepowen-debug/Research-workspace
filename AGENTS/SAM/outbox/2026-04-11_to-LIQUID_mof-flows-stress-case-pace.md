## 2026-04-11 — To: LIQUID

**Signal:** MOF weekly LT-debt net selling has reached stress-case pace — 4-week rolling ¥-5.0T (~$-33B), squarely inside THESIS.md Channel 1 stress range ($25-40B/mo). Priority 🟠.

**Detail:**

The Mar 29-Apr 4 week alone printed **¥-2.46T** (~$-16.4B) of Japanese-resident net LT foreign debt selling — the single largest weekly figure in recent history, 2.5× the prior week's ¥-946B. The 4-week rolling (Mar 8-Apr 4) now sits at **¥-5.0T (~$-33B, run-rate $36B/mo)** which puts the observation inside THESIS.md's stress-case range ($25-40B/mo) rather than the 70%-weighted base case ($7-10B/mo).

The 12-week rolling is still at ~$18B/mo — sitting at the base/stress boundary. So the question is whether the Mar 29-Apr 4 print is:
- **(a) Regime change** — insurer repatriation accelerating into FY2026 (Japanese FY begins Apr 1), consistent with the ESR pressure + hedge ratio collapse thesis
- **(b) FY-start seasonal spike** — technical reallocation around the Japanese fiscal year boundary
- **(c) One-off technical factor** we don't know yet

We cannot distinguish from 1 data point. **The next MOF ITS release (~Thu Apr 16 JST) is decisive.** If Apr 5-11 week confirms another ¥2T+ weekly outflow, SAM will rebalance Channel 1 scenario weights (Option C from today's discussion with Will: Base 70% → 55%, Stress 25% → 37%, Crisis 5% → 8%). Until then SAM holds current weights.

**Parallel data points that should inform LIQUID's UST demand view:**
- CFTC JPY non-commercial net now **-93,742** (52.1% of Jul 2024 peak) — built +17K shorts WoW, still accumulating not covering. Two independent crowding signals (flows + positioning) pointing same direction.
- JGB 10Y sitting at 2.397% MOF Apr 9 — right at the 2.40% stress threshold. Curve at multi-decade highs is consistent with institutions pricing BOJ normalization and exiting USTs on a rate-differential basis.

**Correction to prior SAM STATUS:** Earlier SAM STATUS cited "3-week selling ¥2,215.8B running 2x base case pace" — that framing was too conservative. The ¥2.2T was the Mar 31 MOF snapshot. The Mar 29-Apr 4 release (published Apr 8-9 JST) moved the 4-week rolling to ¥-5T. SAM automation surfaced this today during Phase 2 tooling buildout.

**Source:** MOF ITS weekly CSV (authoritative): `mof.go.jp/policy/international_policy/reference/itn_transactions_in_securities/week.csv`. Parsed via new SAM tool `AGENTS/SAM/scripts/mof_flows.py` — 1,109 rows of historical data now in `AGENTS/SAM/workbook/MOF_FLOWS.tsv` for LIQUID cross-reference if useful.

**Priority:** 🟠 (stress case pace breached per THESIS scenario range, but single-week spike — not yet regime change).

**Ask:** No action required. FYI for LIQUID's UST demand/repatriation view. If LIQUID has independent confirmation from TIC data (Feb release Apr 15), cross-reference and flag if views diverge.
