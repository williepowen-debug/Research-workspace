# LIQUID — RECON REPORT
**Generated:** 2026-03-15 | **Agent:** LIQUID | **Stage:** Pre-Search (Stage 1)
**Context:** War Day 14 (Hormuz permanent closure). FOMC Mon-Tue, presser Wed 2:30 ET. BOJ Thu.

---

## 1. STALE DATA

Data points that are >3 days old and actively matter to our domain:

| Item | Last Known Value | Last Updated | Staleness | Why It Matters |
|------|-----------------|--------------|-----------|----------------|
| **HY OAS (BAMLH0A0HYM2)** | 319bps (1bp below LIQ-01 trigger) | Mar 9 | **6 days** | LIQ-01 trigger status unknown. Estimated 320-335bps based on Mar 12 conditions but unconfirmed. |
| **CCC OAS (BAMLH0A3HYM2)** | 969bps | Mar 9 | **6 days** | Leading indicator for HY OAS. 31bps from ORANGE (1000bps). Mar 12 risk-off likely pushed it higher. |
| **IG OAS (BAMLC0A0CM)** | 85bps | Mar 9 | **6 days** | Transmission gauge. Estimate 90-100bps range by now. |
| **SOFR** | 3.64% | Mar 10 | **5 days** | Repo stress monitor. Mar 11-14 prints not yet logged. |
| **RRP Balance** | $0.278B | Mar 10 | **5 days** | Buffer at zero. Quarter-end in 16 days. Any day this is negative = critical. |
| **VIX** | 24.93 | Mar 11 | **4 days** | Coiled spring thesis. Mar 12 risk events (Citi DIFC evac, 10Y BTC miss) should have moved it. |
| **10Y Yield** | ~4.27% | Mar 12 | **3 days** | Last confirmed data. FOMC week positioning likely moved it. |
| **30Y Yield** | 4.871% (auction clearing) | Mar 12 | **3 days** | Term premium tracker. |
| **IG Primary Market Issuance** | ZERO (2 days: Mar 2-3) | Mar 4 | **11 days** | Did primary market fully reopen after war shock? No update since ZERO reading. |
| **CLO AAA Spreads** | ~125bps (REGINALD estimate) | Mar 4 | **11 days** | 5bps from YELLOW (130bps). Basis trade funding cost. |
| **SRF Usage** | $30.5B (3rd highest since 2020) | Feb 18 | **25 days** | Intraday stress monitor. Nearly a month stale — could be much higher now. |
| **Dealer Net Position (FR 2004)** | ~$200B | Jan 25 | **49 days** | Severely stale. At ORANGE threshold ($200B). If dealers more stuffed → auction tail risk elevated. |
| **Belgium UST Holdings (TIC)** | $481B | Nov 2025 TIC data | **~4 months** | China proxy. TIC Jan 2026 data releases TODAY (Mar 15). |
| **China UST Holdings (TIC)** | $682.6B | Nov 2025 TIC data | **~4 months** | TIC Jan 2026 data releases TODAY (Mar 15). |
| **Japan UST Holdings (TIC)** | ~$1.1T | Nov 2025 TIC data | **~4 months** | TIC Jan 2026 data releases TODAY (Mar 15). Largest holder. |
| **Term Premium (ACM)** | 0.80% (Feb 5 via MacroMicro) | Feb 5 | **38 days** | With 10Y at 4.27%, TP likely materially higher. |
| **Basis Trade Exposure** | $1.85T (50-100x leverage) | Feb 20 | **23 days** | CRITICAL: Most dangerous vector if repo breaks. May have grown as 10Y sold off. |
| **FOMC Rate Decision / Dot Plot** | Unknown — meeting Mon-Tue | N/A | N/A | **This week's event.** Last confirmed path was no cuts in 2026. Stagflation trap changes calculus. |
| **BOJ Rate Decision** | Unknown — meeting Thursday | N/A | N/A | **This week's event.** Ueda presser Mar 19. BOJ hike = JGB yield rise = UST selling acceleration. |

---

## 2. KNOWN UNKNOWNS

Gaps explicitly flagged in STATUS but never resolved:

1. **LIQ-01 Confirmed Trigger** — STATUS says "presumed triggered" as of Mar 12 based on HY OAS 319bps + market conditions, but FRED confirmation never logged. The single most important unresolved item. Mar 10-14 FRED data for BAMLH0A0HYM2 not yet scraped.

2. **DIFC Situation Post-Mar 12** — Citi evac confirmed Mar 12. No follow-up: Have other banks evacuated? Is SWIFT/settlement disruption actually materializing? Has HAWK confirmed any clearing disruption? Mar 13-15 status unknown.

3. **Mar 12 30Y Auction BTC Threshold Check** — STATUS notes BTC 2.45 > 10-auction avg 2.39 = "relief signal" but then immediately flags the DIFC event. No clean resolution: did the combined 10Y weakness + 30Y relative strength confirm or deny the demand hole escalation trigger?

4. **Proposal 4 Decision (HYG Put Roll)** — Jun $75P x10 positioned for LIQ-01 convergence. STATUS flagged review needed if HY OAS <320bps AND no DIFC event. DIFC event occurred — but HYG roll to Sep/Dec decision never confirmed. Position currently unreviewed for Jun expiry risk.

5. **IG Primary Market Reopening** — ZERO for 2 days (Mar 2-3). Did market fully reopen Mar 4+? VX-LIQUID-6.04 at RED. No update in 11 days.

6. **CLO Issuance Pause** — STATUS Watch section: "Watch CLO issuance pause as next trigger." CLO AAA at ~125bps (5bps from YELLOW). No CLO issuance data since Mar 4.

7. **BCRED Q2 Hard Gate Modeling (Proposal 5)** — OTTO Mar 11 flagged Q2 as structural test. No follow-up modeling done. What assets does BCRED sell first? Blue Owl "permanent freeze" already live — downstream effects?

8. **Foreign Demand Pre-FOMC Positioning** — Known unknown: Are FOI sellers (Japan, China, Gulf) adjusting pre-FOMC? Typical pattern is reduced bidding at auctions preceding Fed meetings. No data on whether this played out Mar 9-14.

9. **SOFR Mar 11-14 Prints** — Four days of SOFR prints missing. Any spike >3.75% = plumbing stress signal. VX-LIQUID-1.01 already at ORANGE from Mar 3. Post-Citi DIFC evac, repo stress could have materialized.

10. **Reserve Balance (H.4.1) Week of Mar 9-13** — VX-LIQUID-1.07 shows declining trajectory toward ORANGE ($2.8T). Weekly H.4.1 release likely shows current level. Not tracked since Feb 19 estimate of $2.9T.

---

## 3. SEARCH TARGETS

Prioritized, FOMC-week-focused search list for Stage 2:

---

**T-01** 🔴
- **Query:** `FRED BAMLH0A0HYM2 ICE BofA high yield OAS March 2026`
- **Why:** LIQ-01 trigger confirmation. If ≥320bps confirmed → signal HENRY + SAM immediately. Position decision (HYG put roll) contingent on this.
- **Last Known:** 319bps (Mar 9 CONF). Estimated 320-335bps as of Mar 12.
- **Priority:** 🔴 CRITICAL — the single most important unresolved item in domain.

---

**T-02** 🔴
- **Query:** `TIC Treasury International Capital January 2026 data release foreign holdings`
- **Why:** TIC Jan 2026 data releases TODAY (Mar 15). Japan, China, Belgium — confirms or denies demand hole thesis with hard data. Pre-war baseline for contrast with Feb/Mar auction weakness.
- **Last Known:** China $682.6B, Japan ~$1.1T, Belgium $481B — all from Nov 2025 TIC (4 months stale).
- **Priority:** 🔴 CRITICAL — today's scheduled data release.

---

**T-03** 🔴
- **Query:** `FOMC March 2026 meeting expectations rate decision dot plot stagflation`
- **Why:** FOMC presser Wednesday. In stagflation trap, any dovish pivot = dollar sell + curve steepener. Any hawkish hold = front-end pressure + credit tightening. Both scenarios have different implications for HYG puts and TEN calls.
- **Last Known:** No cuts priced for 2026. War premium + CPI 2.4% creates impossible mandate conflict.
- **Priority:** 🔴 CRITICAL — this week's primary market mover.

---

**T-04** 🔴
- **Query:** `BOJ Bank of Japan March 2026 rate decision Ueda press conference`
- **Why:** BOJ Thursday. Any hike or hawkish signal = JGB yield rise = life insurer hedge unwind = UST selling acceleration. Directly amplifies our anchor selling thesis (VX-LIQUID-7.02, 7.05).
- **Last Known:** BOJ at ~0.5% policy rate, debate ongoing over March vs June hike.
- **Priority:** 🔴 CRITICAL — direct amplifier of Japan UST selling thesis.

---

**T-05** 🔴
- **Query:** `SOFR rate March 11 12 13 14 2026 repo market stress`
- **Why:** Four days of missing SOFR prints. VX-LIQUID-1.01 already ORANGE (75th pct 3.78%). Post-DIFC evac, any SOFR spike >3.75% = SRF activation scenario. Quarter-end 16 days away with zero RRP buffer.
- **Last Known:** 3.64% (Mar 10). RRP at $0.278B.
- **Priority:** 🔴 CRITICAL — plumbing stress confirmation.

---

**T-06** 🔴
- **Query:** `DIFC Dubai International Financial Centre banks operations March 2026 SWIFT settlement`
- **Why:** Citi evac confirmed Mar 12. Have additional banks evacuated? Is settlement/clearing disruption materializing? HY OAS impact of +5-15bps in 48-72h window is now past — did it occur?
- **Last Known:** Citi evac confirmed Mar 12. No follow-up data.
- **Priority:** 🔴 CRITICAL — active operational risk with 48-72h transmission window now elapsed.

---

**T-07** 🟠
- **Query:** `HYG put options June 2026 credit spread HY ETF March 2026`
- **Why:** Active position. Need current HYG price and implied vol to assess roll decision (Jun → Sep/Dec). LIQ-01 trigger status affects timing.
- **Last Known:** HYG Jun $75P x10, $1.465 mid (Mar 10). Jun expiry risk if LIQ-01 slow convergence.
- **Priority:** 🟠 IMPORTANT — active position management.

---

**T-08** 🟠
- **Query:** `CLO AAA spread March 2026 leveraged loan issuance pause`
- **Why:** VX-LIQUID-6.01 at ~125bps, only 5bps from YELLOW (130bps), 25bps from ORANGE trigger that fires BDC→FHLB transmission. CLO issuance pause = basis trade funding disruption signal.
- **Last Known:** ~125bps (REGINALD signal Mar 4, 11 days stale).
- **Priority:** 🟠 IMPORTANT — next cascade link if triggered.

---

**T-09** 🟠
- **Query:** `Federal Reserve RRP reverse repo balance March 2026 reserve balances H.4.1`
- **Why:** RRP at $0.278B (effectively zero). Quarter-end stress approaching Mar 31. Weekly H.4.1 will show current reserve balance trajectory — critical for SRF activation scenario.
- **Last Known:** RRP $0.278B (Mar 10). Reserves ~$2.9T (Feb 19 est).
- **Priority:** 🟠 IMPORTANT — structural stress gauge, quarter-end 16 days out.

---

**T-10** 🟠
- **Query:** `Treasury 20Y auction March 2026 results bid-to-cover indirect bid`
- **Why:** STATUS flagged next 20Y auction ($13B) as "real stress test" after Feb 19 disaster (BTC 2.36x, Indirect 55% = second lowest on record). If tail >3bps + BTC <2.1x → ORANGE auction threshold.
- **Last Known:** 20Y BTC 2.36x (Feb 19) — below YELLOW threshold. $13B auction scheduled.
- **Priority:** 🟠 IMPORTANT — direct demand hole confirmation signal.

---

**T-11** 🟠
- **Query:** `BCRED Blackstone real estate credit Q1 2026 redemptions NAV gate`
- **Why:** VX-LIQUID-6.06 RED. Q1 redemptions $3.7B (7.9%) forced cap raise 5→7%. Q2 structural test May/June (NFP -92K → redemptions likely accelerate). What happened in March?
- **Last Known:** Cap raised to 7% (Mar 3). Blue Owl permanent freeze already live.
- **Priority:** 🟠 IMPORTANT — private credit → public market transmission monitor.

---

**T-12** 🟠
- **Query:** `VIX CBOE volatility index March 12 13 14 2026 options expiry`
- **Why:** VIX coiled spring thesis. Last 24.93 (Mar 11). Mar 12 had Citi DIFC evac + 10Y weak auction + oil $100+. Expected to have moved higher. VIX 35+ = spring release trigger.
- **Last Known:** 24.93 (Mar 11). Coiled at false calm level vs structural stress.
- **Priority:** 🟠 IMPORTANT — position timing signal.

---

**T-13** 🟠
- **Query:** `Japan TIC Treasury holdings January 2026 life insurer repatriation selling`
- **Why:** Part of T-02 but deserves dedicated search. Japan is largest single holder (~$1.1T). If Jan TIC shows >$10B net sell → Japan anchor selling confirmation. BOJ hike Thursday amplifies.
- **Last Known:** ~$1.1T (latest TIC). Life insurers selling $10-15B/month to capture 30Y JGB yields.
- **Priority:** 🟠 IMPORTANT — Japan is the single biggest anchor seller thesis.

---

**T-14** 🟡
- **Query:** `IG investment grade corporate bond issuance March 2026 primary market`
- **Why:** VX-LIQUID-6.04 hit RED (ZERO for 2 days). If IG primary never fully reopened after war shock, credit transmission is live. If it did reopen, measures stress absorption capacity.
- **Last Known:** ZERO for Mar 2-3. No update since Mar 4.
- **Priority:** 🟡 NICE TO HAVE — confirms credit market function vs dysfunction.

---

**T-15** 🟡
- **Query:** `CCC high yield credit spreads ICE BofA FRED March 2026`
- **Why:** CCC OAS (969bps Mar 9) is the leading indicator for HY OAS. If CCC crossed 1000bps = ORANGE trigger on VX-LIQUID-6.07. Would confirm LIQ-01 acceleration thesis.
- **Last Known:** 969bps (Mar 9). Estimated 985-1005bps given Mar 12 conditions.
- **Priority:** 🟡 NICE TO HAVE — confirms T-01 direction.

---

**T-16** 🟡
- **Query:** `ACM term premium 10 year Treasury March 2026 NY Fed`
- **Why:** VX-LIQUID-7.04 shows 0.80% (Feb 5). With 10Y now at 4.27%+ and auction demand weakening, TP almost certainly higher. >1.00% = ORANGE; historical avg 2.16%. SF Fed model was already at 1.22% in Feb.
- **Last Known:** 0.80% (Feb 5 MacroMicro / NY Fed ACM).
- **Priority:** 🟡 NICE TO HAVE — structural confirmation, not tactical.

---

**T-17** 🟡
- **Query:** `FOMC March 2026 pre-meeting positioning Treasury auction indirect bid foreign demand`
- **Why:** Standard pre-FOMC pattern = foreign official bidders reduce auction participation. If Mar 11-14 auctions (if any) showed further indirect bid deterioration, confirms FOI pre-FOMC retreat pattern.
- **Last Known:** 10Y indirect bid not confirmed for Mar 12 auction (BTC 2.45 confirmed, indirect % not logged).
- **Priority:** 🟡 NICE TO HAVE — pre-FOMC auction pattern confirmation.

---

## 4. CROSS-AGENT NEEDS

Items that require another agent's domain to complete LIQUID's picture:

| Need | From Agent | Why LIQUID Needs It | Priority |
|------|-----------|---------------------|----------|
| **BOJ rate decision preview + Ueda presser signals** | SAM | BOJ Thursday is the direct trigger for Japan life insurer UST selling acceleration. SAM owns the Japan domain — need their current read on BOJ hike probability and JGB yield trajectory. BOJ hike → VX-LIQUID-7.02 escalation. | 🔴 |
| **DIFC post-Mar 12 status — additional bank evacuations? Settlement disruption confirmed?** | HAWK | HAWK owns geopolitical/Gulf domain. Citi evac was Mar 12. The 48-72h HY OAS impact window has elapsed. Did SWIFT/clearing disruption materialize? Has HAWK observed other DIFC bank movements? LIQUID needs this to assess whether VX-LIQUID-6.08 should escalate further. | 🔴 |
| **USDJPY and JPY basis swap current levels** | SAM | USD/JPY cross-currency basis (VX-LIQUID-4.01, last -45bps Jan 25 = 50 days stale). Pre-BOJ week positioning could show in basis swap widening. If USD/JPY basis widens past -60bps = dollar funding stress signal that LIQUID tracks. | 🟠 |
| **Private credit redemption wave Mar 2026 update — BCRED/Apollo/Blue Owl** | BROCK | BROCK owns private credit. LIQUID needs Q1 end-of-quarter redemption data to model Q2 hard gate scenario (Proposal 5). Blue Owl permanent freeze downstream effects — which assets liquidate first and in what order (bank loans → CLOs → public HY)? | 🟠 |
| **Hormuz current posture — any de-escalation signals?** | HAWK | TEN calls (Jun $30) thesis duration directly tied to Hormuz posture. "Permanent" declaration Mar 12 extended thesis, but any negotiation signal would require Proposal 3 (crude short) reassessment. HAWK needs to confirm current operational status. | 🟠 |
| **SPX and equity volatility Mar 12-14** | HENRY | LIQUID needs to know if the Mar 12 Citi DIFC evac + 10Y BTC miss translated into equity vol spike (VIX >28) or was absorbed. HENRY's VIX reads directly affect the HYG put convergence timing assessment. | 🟠 |
| **China pre-FOMC behavior — any acceleration of UST selling?** | ZHAO | ZHAO tracks China's selling via Belgium/Euroclear. Today's TIC Jan 2026 release is the first hard data in months. ZHAO should interpret Belgium + China combined flow. LIQUID can then integrate with VX-LIQUID-7.06/7.07 and the demand hole model. | 🟠 |

---

*Next step: Stage 2 searches using T-01 through T-17 above. Cross-agent needs to be consolidated by NEXUS/PROME before Stage 2 execution.*
