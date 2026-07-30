---
signal_id: SIG-W-20260730-003
date: 2026-07-30
time_dispatched: 2026-07-30T15:25:00Z
origin: WALTER midday news sweep (Will-directed) — post-FOMC rates decomposition
source: Bloomberg 7/29 ("US 30-Year Yield Soars to Highest Since '07 After Fed Stands Pat" / "Fed hold trims September hike bets"); CNBC 7/29 (30Y highest since 2007; Warsh credibility analysis); Seoul Economic Daily 7/30 (tops 5.2%); own fetch.py pulls 15:10Z (^TYX 5.21 +1.34%)
domain: RATES
cluster: FED_FRAMEWORK
precedence: PRIORITY
action: [BOND]
info: [LIQUID, HENRY, RED, ORACLE]
signal_type: threshold-crossed
confidence: 0.88
verdict: CONFIRMED-MULTI-WIRE + OWN-TAPE (level); decomposition = the routed question, BOND adjudicates
---

# 📈 THE 30-YEAR PRINTED 5.244% — HIGHEST SINCE JULY 2007 — AND THE DECOMPOSITION POINTS AT BOND'S OWN DISCRIMINATOR: September hike odds were CUT while long yields spiked. A hold that steepens the long end is a TERM-PREMIUM / credibility move, not a policy-path move — and BOND's standing regime call is "policy-path-led." BOND adjudicates its own regime label.

**The facts:**
- **30Y hit 5.239–5.244% on 7/29** (Bloomberg + CNBC: highest since **July 2007**), after the **9-3 hawkish hold** and Warsh's presser (*"no soft inflation target"*; on the dissents: *"I asked for a good family fight, and I got one"*). **Holding ~5.21 today** (own ^TYX pull 15:10Z, +1.34% on the day); 10Y ~4.66.
- **The decomposition is the signal:** Bloomberg's own framing is the *hold* **trimmed September hike bets** — the short-end priced *less* tightening while the long end sold to a 19-year high. A market cutting policy-path odds while long yields spike is pricing **term premium / inflation credibility / fiscal**, not the path. CNBC ran a Warsh-credibility analysis the same evening ("for a chairman who prizes credibility... the market's reaction must have been painful").
- **Real-yield leg, FLAGGED NOT VERIFIED:** secondary coverage says real yields led a sixth straight weekly gain. **BOND's DFII10 re-arm sits at 2.50 and its last recorded print was 2.43 (series high, 7/28)** — if real yields led this move, the re-arm may have FIRED. I could not pull DFII10 (FRED 403 from this box, 3rd session) — **BOND: check your own re-arm at your source before marking.**
- **Context rows BOND already holds, now moved:** its 7/28 state was 10Y 4.69 / ^TNX 4.64 / ^MOVE 77.21, regime "real-rate / higher-for-longer POLICY-PATH-LED, passed a clean out-of-sample test across the crude collapse." **This move is the counter-case to that label: the FOMC hold was the input, and the long end repriced anyway.** Whether that flips the regime label is BOND's call, not mine.

**For ORACLE (info):** the crowd's Fed-HIKE-2026 base case (71.5% on 7/24, extending) now has a countervailing post-FOMC datum — September odds were *cut* on a hawkish hold. Your mark's vintage predates the decision; re-pull before citing.

**For LIQUID/HENRY (info):** duration regime legs (DGS30 >5.00 / DGS10 >4.50) are now deep through their thresholds at the long end; the equity tape absorbed it today (NDX +3.07% recovery) — long-yield-up + equity-up + VIX −10% is not a stress print, it is a repricing print.

**⚠️ Guards:**
- **"Oil breached $92" is circulating in secondary rate wrap-ups (ts2/cryptobriefing class) — REFUTED by the tape:** Brent front-month has printed ~$84–89 all week (own pulls; 7/29 spike high ~$88–89). Do not let a rates story import a false oil level.
- The 5.244% is an **intraday/close print from 7/29** — cite it with its date; today's level is ~5.21 and moving.
