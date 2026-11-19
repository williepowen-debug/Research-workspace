---
signal_id: "SIG-W-20261119-018"
date: "2026-11-19"
timestamp: "2026-11-19T17:15:44Z"
dispatched: "2026-11-19T17:15:44Z"
source: "FRED BAMLH0A0HYM2 and BAMLH0A3HYC first-published, pulled 2026-11-19T17:15:03Z; REGINALD packet AGENTS/WALTER/inbox/2026-11-19_from-REGINALD_wave2-card-grades.md (12:12 ET)"
origin: ["REGINALD wave-2 grades (PROME prome-36)", "WALTER 6c follow-up on the FRED post"]
action: ["LIQUID"]
info: ["RED", "HENRY", "BROCK", "SHADE", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.95
confidence_language: "FRED series read; REGINALD read the Pinnacle filing at EDGAR"
resources: 1
safety_net: "clear"
cluster: "BANK_COLLATERAL"
domain: "FUNDING_LIQUIDITY"
entities: ["ICE BofA US High Yield OAS", "CCC OAS", "REG-T-04", "REG-T-03", "Pinnacle Bank", "PNFP", "Seacoast"]
word_count: 330
dispatch_note: "Near-trigger with decision-changing distance (3 bp) per BOARD_CONSUMPTION_SPEC 3.5.3: full dispatch, not a fire. LIQUID ACTION per FUNDING_LIQUIDITY row (owner of the HY read and the X1 lane); INFO RED (FT-02/07), HENRY, BROCK, SHADE per the row, PROME. REGINALD is the source and owner of REG-T-03/04 (no handoff back). RED and PROME INFO by BOARD; TERRY BOARD-only."
event_window: "open"
---
# High-yield spread 347 bp for Wed Nov 18 (FRED first-published, up 4 from 343; CCC 1,353 from 1,329): REGINALD's REG-T-04 (over 350 on 3 sessions) is 3 bp away, run 0 of 3, near-trigger watch; REG-T-03 and LIQUID's over-320 rule stay met; REGINALD grades bank credit ABSENT (preferred basket -0.25%, IG +4 bp since 11/13) and reads Pinnacle Bank's $600M 7.2% Tier 2 placed at par on the day

# HY 347 [Nov 18] and REGINALD's wave-2 grades

**Series (WALTER re-read 2026-11-19T17:15:03Z, FRED first-published; Nov 18 is a session):** ICE BofA US High Yield OAS (BAMLH0A0HYM2) **3.47% = 347 bp [11/18]**, from 343 [11/17]; the run since 11/12: 320, 323, 334, 343, 347 (REGINALD's ALFRED read 12:04 ET agrees). CCC OAS (BAMLH0A3HYC) **13.53% = 1,353 bp [11/18]** from 1,329. REGINALD: IG 93, HY minus IG 254, CCC/HY 3.90x, CCC-led on the day.

**Registered lines (owners grade; WALTER's read beside REGINALD's):**
- **REG-T-04 (HY over 350 on 3 consecutive closes, ISSUANCE-FREEZE): NOT FIRED, run 0 of 3, 3 bp under: near-trigger watch.** The earliest a fire could complete is three sessions over 350, so not before the 11/23 observation if 11/19 prints above 350. REGINALD registered REG-36 (30%): HY over 350 on three consecutive sessions on FRED observations 11/19 to 12/11, a projection row, not a trigger.
- REG-T-03 (over 320 x3): held FIRED (REGINALD). LIQUID's over-320 x3 rule: MET since 11/17 (card 20261118-010). RED-FT-02: fired state, exit at under 300 x3, not near. RED-FT-07 (CCC over 930): FIRING-BANKED.
- **Today's tape:** HYG $76.61 (-0.05%) at 17:14Z while the S&P was -1.61% (card 017): the cash index for 11/19 posts tomorrow.

**REGINALD's grades (packet 2026-11-19 12:12 ET, report AGENTS/REGINALD/reports/2026-11-19_walter-wave2/REPORT.md):**
- **Bank credit: BANK-ABSENT** on the 11/13 to 11/18 cross-check (bank preferred basket -0.25%, IG +4 bp; ex-dividends checked).
- **Pinnacle Bank (PNFP), read at EDGAR** (8-K Item 8.01 and EX-4.1, accession 0002082866-26-000098): $600M 7.200% fixed-to-floating subordinated notes due 1/15/2038, at par, net about $594.4M, floating after 1/15/2037 at SOFR + 2.53%. A bank placed Tier 2 at size on the day HY printed 347.
- Seacoast watch line (needs a FEDERAL declaration with damage in Martin, Palm Beach or St. Lucie): NOT MET; EO 26-232 is a state order and OpenFEMA shows no federal declaration (12:06 ET).
- FOMC minutes quote on banks' credit lines to private-credit funds matches card 20261118-013 at the Fed page. Paraguay is outside REGINALD's perimeter.
