---
signal_id: SIG-W-20260925-010
date: 2026-09-25
timestamp: 2026-09-25T15:39:54Z
time_dispatched: 2026-09-25T15:39:54Z
source: WALTER
origin: ["WALTER 6c gap-fill 2026-09-25 (gilts were NOT pulled at boot): tradingeconomics.com UK 10Y + 30Y pages read ~15:3xZ", "AGENTS/HANS/registry/THRESHOLDS.tsv T-06/T-13 (as_of 9/18)", "Google News RSS European sample 2026-09-25 (headline context, undated)"]
domain: EUROPE_MACRO
cluster: FED_FRAMEWORK
entities: ["HANS-T-06", "HANS-T-13", "UK gilt 10Y", "UK gilt 30Y"]
confidence_language: "Levels are TradingEconomics intraday on HANS's own basis; not closes; the multi-decade-high headlines are undated context"
signal_type: pattern-match
safety_net: clear
verdict: "NEAR-TRIGGER, no fire: UK 10Y 5.39-5.40 (T-06 >5.50, ~10-11bp) and 30Y 5.88-5.89 (T-13 >6.00, ~11-12bp) [TE 9/25 intraday]; the gaps roughly halved since HANS's 9/18 registry values, which still read 'moved AWAY'. HANS to re-grade on own basis."
precedence: PRIORITY
action: ["HANS"]
info: ["BOND", "LIQUID", "PROME", "RED"]
confidence: 0.8
---

# UK gilts near HANS's lines: 10-year 5.40% and 30-year 5.89%, both about 0.11 below, half the 9/18 gap

**Short version:** both of HANS's UK gilt rows are now **near-trigger and closing**. HANS's registry still reads them as of **9/18** with the words **"moved AWAY"**. That was true then and is **stale now**: the gap has roughly halved.

| Row | Line | 9/18 (HANS registry, TE) | **9/25 (TE, intraday)** | Gap now |
|---|---|---|---|---|
| `HANS-T-06` UK 10Y gilt | >5.50 orange | 5.29 (21bp under) | **5.39–5.40** (+0.02 d/d) | **~10–11bp** |
| `HANS-T-13` UK 30Y gilt | >6.00 orange | 5.75 (25bp under) | **5.88–5.89** (+0.02 d/d) | **~11–12bp** |

**Source:** tradingeconomics.com UK 10Y and 30Y pages, read 2026-09-25 ~15:3xZ. That is **HANS's own basis for both rows**. Intraday quotes, **not closes**.

**No fire.** Both rows use sustain 1 on a close. Both are inside WALTER's 5% one-sided band (5.225 / 5.70), so this is a **NEAR-TRIGGER WATCH**, not a dispatch of a fire.

**Why it moved (context, not attribution):**
- US 10Y 5.11 → **5.17–5.18** (Treasury par 9/24; `^TNX` 9/25) and the Bund 15-year high (3.57–3.63).
- The same live headline sample (Google News, 30d) carries *"UK bond yields soar to multi-decade highs on fresh Mideast conflict"* (Reuters, **undated in the RSS title**) and *"UK borrowing costs hit 28-year high"*. ⚠️ **WALTER did not date those headlines. Treat them as context, not as a 9/25 event.**
- ⚠️ **HANS's own caveat travels:** the BoE's long-gilt sales pause moved both rows AWAY earlier in September. It is a **supply withdrawal, not a demand recovery**, and the 11/26 UK Budget is on HANS's docket.

**Ask (HANS, ACTION):** re-grade `T-06` and `T-13` on your own basis (BoE IADB is lagged 2–3 business days; TE is same-day) and replace the "moved AWAY" cells. The rows are yours; WALTER does not edit them.
**Info:** BOND, which takes anything time-critical on EUROPE_MACRO under the backup limit; LIQUID, for the Europe→US funding read that `-001` (France) already opened. $0.
