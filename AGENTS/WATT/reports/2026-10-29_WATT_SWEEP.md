# WATT weekly coverage + inbox drain — October 29, 2026

Window 13:27–14:0x ET October 29. Will's instruction 13:31 ET: "go" (on the boot brief's next step: ISHM custody reply, inbox drain, overdue weekly coverage WQ295). Claude Code, Opus 5.5 (`claude-opus-5-5`). Startup pull refused on WALTER's dirty registry files; origin not ahead; continued on checkout. DM2 calls: 2 at boot + 3 deliberate (tape, verified hourly, outages), spaced. No trade, threshold change, spend or Will decision.

## Bottom line

**P1 re-escalates 3 → 5 on the registered RED letter.** October 27 18:50 / 18:55 / 19:00 EPT printed $2,026.73 / $1,970.77 / $2,297.21 (DM2 unverified 5-min, PJM-RTO) while EIA-930 demand was 97.9% (T22Z) and 99.8% (T23Z) of the trailing-24h peak (94,460 MW). Composite **16/20** (5+5+4+2). The fire went unseen for two days: no WATT session October 24–28, and boot reads only the current EPT day.

## P1 — the week's tape

| EPT day | Prints | Max $/MWh (stamp) | ≥$1,000 | ≥$500 | Missing stamps |
|---|---:|---|---:|---:|---|
| Oct 23 | 288 | 748.30 (06:30) | 0 | 1 | none |
| Oct 24 | 278 | 436.76 (00:15) | 0 | 0 | 16:50, 17:45–18:10 (6 adjacent), 18:20, 18:30, 22:20 |
| Oct 25 | 288 | 399.74 (21:40) | 0 | 0 | none |
| Oct 26 | 288 | 1,340.04 (07:50) | 1 | 3 | none |
| Oct 27 | 280 | 2,297.21 (19:00) | 3 | 6 | 15:30–16:05 (8 adjacent; inside PJM's announced 14:50–17:00 maintenance) |
| Oct 28 | 288 | 306.10 (00:05) | 0 | 0 | none |
| Oct 29 (to 13:25) | 162 | 81.18 (06:50) | 0 | 0 | none |

TotalRows 1,872 = items 1,872 (no row-cap truncation). October 26's $1,340.04 is a single print (07:45 $681, 07:55 $222): not a run, does not meet the letter.

**Letter test (STATUS P1 upgrade trigger):** LMP ≥$1,000 for 2+ consecutive 5-min — **MET** (3 consecutive). AND (emergency-class posting OR demand ≥97% of trailing-24h peak) — posting **not found**; demand **MET** (97.9% / 99.8% / 100.3% at T22/T23/T00Z, so met under either hour-stamp convention). **FIRED-ON-LETTER → P1 = 5.**

**Corroboration:** verified `rt_hrl_lmps` (version 1, row_is_current) HB18 10/27 $719.87, HB19 $351.57, HB07 10/26 $416.45: the stress is real, not a feed glitch. Hourly averages do not themselves print ≥$1,000.

**What it is not:**
- Not KILL_MEMO C1 (needs EEA2+): ladder not triggered.
- No emergency-class posting: board empty at 13:32 ET 10/29; posting ids 105577–105760 all blank (size test; controls 105576 and 105478 return valid pages). Unissued vs withdrawn cannot be told apart.
- No new DOE 202(c): index newest is still 202-26-50.
- No PJM explanation: the Inside Lines feed's newest item is dated 10/22.
- Short-lived: $180 by 19:15, $53 by 19:20.

**Recorded disagreement (letter applied as written, threshold unchanged):** the demand limb was met in an ordinary evening-peak hour. In shoulder season, demand near its own 24-hour peak at 19:00 is routine, so this limb discriminates weakly. A posting-limb fire would carry more information. Candidate for a deliberate quiet-day threshold review, not changed here.

**Context:** same-day outage forecasts 72,722 MW 10/26 (planned 47,386 / maintenance 12,432 / forced 12,904) and 69,470 MW 10/27 (43,300 / 12,819 / 13,351), against 71.5 GW total and 10.4 GW forced on 10/22. These are forecasts, not live availability. The fire shares its outage-season root with the 10/7 and 10/13 fires (NEXUS: count the root once).

**Gaps:** the 10/24 (6 adjacent) and 10/27 (8 adjacent) gaps could hide a RED run; that is unknowable without a replay. The 10/27 gap falls inside PJM's announced maintenance window (SIG-W-20261027-027).

**De-escalation:** under the KB-149 letter, seven clear calendar days October 28–November 3 (no EEA-class posting, no 202(c), no RED re-fire; a re-fire restarts the count), graded on the first boot on or after November 4. November 1 DST adds a repeated hour (300 stamps that day).

## P4

Same-vintage spark +$39.62/MWh: RT on-peak mean $60.13 over 10/23–10/28 (n=1,134) minus 7.0 × HH $2.930 (10/29). HR8 gives +$36.69. Positive, NOT-FIRED. This is a window proxy, not matched settlements, and it is not compared with the 10/15–19 window (+$28.93) as a series.

## P2 / P3

Unchanged (5 / 4). No new FERC, BRA or queue primary this pass. Inbox counterevidence (PG&E 12,870 MW staged pipeline with large load beyond 1.8 GW delayed or deferred, CAISO; Site Selectors Guild survey: 35% report fewer groundbreakings) is outside PJM or survey-grade. It does not touch the P3 discriminator.

## Grid-equipment custody (WQ-506)

**ACCEPT**, under Will's 13:31 ET go. WATT owns the Eaton Electrical and GE Vernova Power + Electrification orders/backlog figure as P3 supply-chain evidence, not a new channel. Charter scope line added. The last owned read (KB-097, September 2) is stale; refresh at the next issuer print. Packets go to ISHM and PROME.

## Inbox disposition — 30/30

| Item | Disposition |
|---|---|
| DAEDALUS 10/23 ISHM equipment ASK | ACTED: ACCEPT, packet to ISHM (cc PROME), KB184 |
| DAEDALUS 10/23 WQ-508 lines | Applied by DAEDALUS f4149bf51; diff read, no contest; filed |
| ISHM 10/26 first-session boundary | ACTED (same reply) |
| ISHM 10/26 CAT power-gen scope | Noted: CAT stays ISHM's, no grid share; KB184 |
| ISHM 10/26 equipment crowding | Noted: Beige Book qualitative; KB184 |
| BRENT 10/26 EQT/Range | Noted: no near-term P4 effect; KB185 |
| VULCAN 10/26 conditional financing | Assessed: no MW or power rights, P3 unchanged; KB185 |
| VULCAN 10/26 power execution | Assessed: PG&E outside PJM, NERC petition proposed, Bloom block ≠ compute; KB185 |
| AEOLUS 10/29 SSW forecast | Noted: winter P1 gate HELD, AEO-08 leg; KB185 |
| ZHAO 10/29 truce instruments | Noted: B1/58 UNFIRED, 11/10 clock unchanged; KB185 |
| 20 WALTER signals | board_log rows 10/29; info-only except 027 (source qualification applied to the 10/27 gap) and 026 (gas vs backup MW kept separate); KB185 |

## Records

KB-WATT-181–185 · VX P1 · STATUS · CLAUDE.md scope line · LESSONS · SCRATCH · board_log. Captures with SHA256: `sources/2026-10-29/capture-manifest.json`.

## Addendum 13:5x ET — is it getting worse? Year-over-year test (Will asked)

Verified hourly PJM-RTO price, September 1–October 28, 2025 vs 2026 (n=1,392 each) [KB-WATT-186]:

| Measure | 2025 | 2026 |
|---|---:|---:|
| Median hour $/MWh | 34.79 | 36.78 |
| Mean $/MWh | 45.43 | 67.30 |
| Hours ≥$200 / ≥$500 / ≥$1,000 | 10 / 1 / 0 | 52 / 19 / 7 |
| Worst hour | $691.78 | $3,478.96 |
| Henry Hub mean | $3.06 | $2.99 |
| Demand mean / hours >110 GW | 87.6 GW / 45 | 93.7 GW / 190 |

Same-load rate of hours ≥$200: 90–100 GW 4.3% vs 0.7%; 100–110 GW 5.1% vs 3.5%; >110 GW 14% vs 2%.

**Reading:** the typical hour is unchanged and gas is flat, but extreme hours are far more frequent, including at the same demand level. That is a thinner-cushion signature. **Limits:** only one baseline year (the 2024 pull was refused at the archive boundary); about six clustered episodes; ±1 h demand alignment; 2025 outages and any PJM pricing-rule changes not checked; weather not separated from load growth.

## Addendum 14:0x ET — 2024 baseline and outage causes (Will: "next steps approved")

**2024 hourly price: NOT obtained.** DM2 serves 2024 from its archive, and archived `rt_hrl_lmps` rejects the `pnode_id` and `fields` filters. That leaves only an all-node pull (millions of rows, the silent-truncation pattern). The EIA ICE daily index was rejected as a substitute: it is a day-ahead traded peak block and misses intraday spikes (October 27 delivery $64.89). KB-186 remains a one-baseline-year comparison.

**Outages, same-day forecasts, Sep 1–Oct 28** [KB-WATT-187]:

| October 1–28 mean, GW (total = planned + maintenance + forced exactly) | 2024 | 2025 | 2026 |
|---|---:|---:|---:|
| Total | 65.7 | 64.7 | 67.3 |
| Planned | 50.3 | 47.8 | 47.0 |
| Maintenance | 8.4 | 7.6 | 8.7 |
| Forced | 7.0 | 9.4 | 11.6 |

*Corrected 14:0x ET (KB-WATT-189, caught by WALTER): the first version of this table paired October totals with full Sep 1–Oct 28 component means (planned 32.4/30.4/30.7, forced 7.4/9.0/11.1), so the parts appeared not to sum.*

**Correction of frame:** the autumn maintenance stack is normal and the same every year. "Outage-driven" names the trigger, not the worsening. The 2026 difference is higher demand (+6.1 GW mean) plus more unplanned breakdowns (+2.1 GW vs 2025): about 8 GW less average headroom, before any fleet-size change (not measured).

## Addendum 14:1x ET — fleet size (Will: "go ahead if valuable")

EIA-860M, PJM balancing authority, August of each year [KB-WATT-188]:

| Net summer GW | 2024 | 2025 | 2026 |
|---|---:|---:|---:|
| Firm (gas, nuclear, coal, oil, hydro, other) | 181.4 | 181.0 | 181.4 |
| Solar | 12.6 | 16.7 | 19.3 |
| Wind | 11.3 | 11.5 | 12.0 |
| Storage | 0.4 | 0.5 | 0.7 |

**Reading:** no shrinking fleet, but no firm growth either. Since autumn 2025: firm flat, demand +6.1 GW mean, forced outages +2.1 GW, and solar +2.6 GW that contributes nothing at the late-October evening peak. ⚠️ EIA's perimeter is not PJM's accredited capacity; read the trend only. 860M is preliminary.
