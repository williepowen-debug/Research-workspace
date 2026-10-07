---
signal_id: SIG-W-20261007-001
date: 2026-10-07
timestamp: 2026-10-07T14:54:04Z
time_dispatched: 2026-10-07T14:54:04Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER live pull (fetch.py / Yahoo) + PROME 10/7 news catch-up
origin: ["fetch.py price 2026-10-07 ~10:46 and ~10:51 ET (Yahoo, intraday)", "PROME/reports/2026-10-07_news-catchup.md §2, §3, §8", "Reuters via Investing 10/7 (STOXX banks, SINGLE)", "Business Wire 10/6 (WAL Q3 date, lane)", "JDSupra 10/5 (Fed supervisory statement, lane)"]
entities: ["Flagstar-Financial", "FLG", "Western-Alliance", "WAL", "Huntington-Bancshares", "HBAN", "KRE", "STOXX-Europe-600-Banks", "Societe-Generale", "Deutsche-Bank"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
precedence: IMMEDIATE
action: ["REGINALD", "FLG"]
info: ["WAL", "LIQUID", "HANS", "TERRY", "RED", "PROME"]
confidence: 0.9
confidence_language: "Prices are live intraday pulls (not closes). The RED line is close-basis and only REGINALD grades it."
signal_type: position-risk
safety_net: clear
dispatch_note: "Today-dated: FLG trades under REGINALD's VX-REG-6.03 RED $11.39 intraday; only the regular-session close counts. Position-adjacent: HBAN Oct-16 $16P x2 and WAL $70P Dec-18 x1 per the stale 10/1 and 9/29 mirrors. KRE -2.2% is under the >3% intraday bypass, so not FLASH. Telegram unavailable in this container. REG-T-02 WAL <78 has been in a fired state since 9/1, so today's print is a re-entry, not a new fire. No ticker convergence: no FLG/WAL/HBAN BOARD signal in the prior 5 sessions. TERRY/PROME/RED info via BOARD ID-diff. FLG carve-out: the ticker belongs to FLG, the cohort to REGINALD."
---
# Regional banks sell off 10/7: Flagstar trades below REGINALD's RED $11.39 line intraday (close decides); WAL −3.7%, KRE −2.2%, HBAN −1.7%

**Live pulls (fetch.py → Yahoo, INTRADAY, not closes):**

| Name | Price | Day | Time (ET) | Registered line (owner) | Read |
|---|---|---|---|---|---|
| FLG | $11.30 | −2.29% | ~10:51 | VX-REG-6.03 RED **$11.39** (REGINALD; close-basis) | **Below on an intraday print, $0.09 under.** The close decides. ORANGE $12.10 has been broken since 9/28 |
| WAL | $73.24 | −3.75% | ~10:51 | REG-T-02 <78 (sustain 1); **fired state since 2026-09-01** (77.26), exit ≥81.90 on 3 closes | A re-entry inside the fired state, **not a new fire**; exit not met |
| KRE | $68.55 | −2.17% | ~10:51 | REG-T-01 <60; FILTER bypass is an intraday drop >3% | Neither reached |
| HBAN | $15.06 | −1.73% | ~10:46 | none | position-adjacent (below) |

- **FLG history (PROME helper, SINGLE):** closed $11.57 [10/5] and $11.56 [10/6]; $11.42 intraday at 09:31 ET 10/7. FLG's own STATUS has it at the RED line intraday on 10/1 ($11.39 at 11:06 ET), unsettled. The cause is UNKNOWN (FLG: no filing since 8/14).
- **Europe (Reuters via Investing, SINGLE):** STOXX banks −3.5% on 10/7 (SocGen −5.2%, Deutsche −4.5%), with French contagion cited as the cause. See `SIG-W-20261007-003` for gilts and OATs.
- **WAL:** Business Wire 10/6 says WAL announced its Q3 2026 earnings release date and call. The date is in the release; WALTER did not open it. TERRY's lane watch phrase hit on this.
- **Regulatory (lane, NOT read at the Fed primary):** JDSupra 10/5 reports the Fed updated its statement of supervisory operating principles for bank examiners after the report on a 2023 bank failure. See `SIG-W-20261007-010` for the NY Fed private-credit probe of banks.

**Position-adjacent (FORGE mirror, which is NOT position truth; TERRY's lines; no trade proposed here):**
- HBAN $16P Oct-16 ×2 [mirror 10/1 pc]: at $15.06 it is ~$0.94 in the money. It **expires before HBAN's Thu 10/22 earnings**. WQ-302 decision is due by 10/14.
- WAL $70P Dec-18 ×1 [Robinhood card 9/29, unverified since]: WAL $73.24 is $3.24 above the strike.

**Not established:** whether today is FLG-specific or a cohort beta move (FLG −2.3% vs KRE −2.2% intraday looks like cohort beta so far, but that is an intraday read). No FLG filing was found.
