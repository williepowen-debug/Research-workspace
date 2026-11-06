# D:L973 record, 2026-11-06

**Session:** assigned by PROME prome-51 under WQ-626 A (Will's go 09:48 ET), message received 10:00 ET. Runtime Claude Code, Opus 5.5. Reads by CYPHER: curl, WebSearch, yfinance. Limits per PROME: no trades, no sizing, no new gate, level or threshold without Will; own rows only; packets to other desks.

## 1. Capcom (CYB-INC-030): the desk's 10/23 read was wrong

| Item | Reading | Basis |
|---|---|---|
| Registered rule | "No new source -> set FALSE; a company statement -> re-class" | CATALYSTS row, 10/23 |
| Outcome | **Company statement exists. Re-classed CONFIRMED. FALSE branch not taken** | Capcom notice 2026-10-22 and update 2026-10-23, both read |
| Records | 11,774,247 worldwide: email plus account-creation time, last-login time, login count, last-login IP | PRIMARY-VERIFIED |
| Subset | 43 records also birth date, gender, country/region, nickname | PRIMARY-VERIFIED |
| Passwords | 196 accounts changed without authorization, reset. Customer-set passwords: "has not confirmed any compromise" | PRIMARY-VERIFIED |
| e-Capcom | 19 of the 196 (Japan): name, phone, address, purchase and inquiry history | PRIMARY-VERIFIED, 10/23 update |
| Cards | Not included | PRIMARY-VERIFIED |
| Dates | Detected and confirmed 10/19; police and privacy commission 10/21; scope investigation complete 10/23 | PRIMARY-VERIFIED |
| Attack method | "identified and addressed", not published. No PHP2Shell link on any evidence | PRIMARY-VERIFIED absence |

**Why the 10/23 read failed.** Capcom's notice was public on 10/22 and BleepingComputer covered it the same day. CYPHER's search on 10/23 17:1x ET returned only the 2020 attack, and the desk wrote "likely recirculation" and a do-not-relay line. It never tried the issuer's own press page, which is a fixed URL pattern. The row's default ("no source -> FALSE") would have turned that miss into a refuted claim about a true event if today's search had also missed. The issuer page is the check; a search result is not.

**Consequence:** none for any bank or insurer. Game publisher, phishing risk to account holders, no financial victim. WALTER card 045 carries the wrong read in its title (`capcom-11point7m-claim-likely-2020-recirculation`), so WALTER gets a correction packet. SAM gets it as Japan context.

## 2. Kiteworks victim check: nothing found, and the limits of that

| Instrument | Reading 11/06 | Limit |
|---|---|---|
| Advisory `info.kiteworks.com/php2-vulnerability-advisory` | HTTP 200. "Last updated: 2026-10-27 8:00 PDT". No exploitation statement | Silence, not a denial |
| Fix version in advisory | 9.5.3 unchanged; 10.0 Early Access now reads `10.0.0-ng29`, ledger held `10.0.1-ng178` from 10/22 | Change undated, no changelog |
| GitHub `kiteworks/security-advisories` | Newest advisories on page 1 dated 2026-09-30; nothing newer | Page 1 only |
| EDGAR full text "Kiteworks" 10/17-11/06 | 0 hits, 8-K and all forms | Filers rarely name vendors |
| Boot legs 8 and 9 | No Item 1.05 since 10/30; Revolve already 058 | Only US-listed filers |
| Google News "Kiteworks" 21 days | 10 items, all product, hiring or list articles | Headlines only |
| Searches: victim, Clop, notice letter, law firm | Only the 9/26-9/27 shutdown and 2021 Accellion | Absence in an index |
| State AG portals | **Domain-restricted search only: no Kiteworks notice surfaced. No portal was queried row by row** | Notices rarely name the route in the listing |
| Extortion sites | **Not read directly.** Secondary search only | Desk does not visit them |

**Result:** no organisation names Kiteworks as a route. Row 3 does not fire. This is weak evidence, not an all-clear: MOVEit's first leak-site names came at about +14 days and the list kept growing for 13 months (KB-CYP-004). Disclosure +16 days today. Kiteworks' silence on exploitation also means the check cannot separate "none" from "not said". Next look 11/13, inside the R1 window.

## 3. GMO (CYB-INC-032): procedure started, cost still unknown

| Item | Reading | Basis |
|---|---|---|
| Promise | Application method, documents, period and payment timing by 11/06, on the website and by email | 4th notice, 10/24, read today |
| Delivered | Individual contact with contracted customers began 11/06. Public page states only that, and refers back to the 4th notice | news/article/264, stamped 18:00 JST; TSE disclosure 11/06 |
| ⚠️ Gap | The promised method, documents, period and timing are **not on the public page** | Read today |
| Cost | "現時点では算定できておりません": cannot yet be calculated, because neither the customer count nor the qualifying trades are fixed | TSE disclosure 11/06, PRIMARY-VERIFIED |
| Next date | Application status and the outlook for calculating the earnings effect at the **11/13 results briefing** | Same |
| Also | Pay cuts 11/02: chairman 30%, president 25%, two executive officers 20%, each for 3 months from December; a further review of management responsibility after the verification | TSE disclosure 11/02 |

Threshold on the row ("confirmed scope or cost change") is **not met**. No figure exists. SAM and LIQUID hold the consequence; SAM gets the 11/13 date, LIQUID has no new fact to act on and gets nothing.

## 4. Row 9 magnitude: proposal, not a letter change

PROME's limit today is no new threshold without Will, so this goes as a proposal; the row's letter is untouched.

**Measured 11/06, about 10:05 ET, yfinance adjusted closes; 11/06 is intraday.**

| Name | 10/20 close | 11/05 close | 11/06 live | Since 10/20 | Worst close since 10/20 |
|---|---|---|---|---|---|
| PANW | $340.28 | $314.67 | $325.09 | -4.5% | -7.5% (11/05) |
| HACK | $118.38 | $111.40 | $113.23 | -4.4% | -5.9% (11/05) |
| SPY | $769.05 | $733.00 | $739.43 | -3.9% | -4.7% (11/05) |
| KRE | $70.62 | $72.31 | $72.20 | +2.2% | 0.0% |
| XLF | $55.72 | $57.50 | $57.22 | +2.7% | +0.3% |

PANW peaked at $401.70 on 10/27 and is 19.1% below that today. ⚠️ That drawdown is not this test: the 10/20 close is the pre-disclosure base, and a peak base would be already breached at write time. PANW's -9.6% on 11/05 sat inside a market-wide fall (S&P -4.36%, Nasdaq 100 -6.36%, HENRY STATUS 11/06); nothing found ties it to the wave.

**Option tested, 2 consecutive closes:**

| Rule | CrowdStrike 2024 | Progress 2023 | PANW 2026 now | False alarms, 906 PANW 20-day windows without earnings |
|---|---|---|---|---|
| -15% and 10 points behind HACK | Fires 2024-07-23 | Does not fire | Does not fire | 14, 1.55% |
| -10% and 10 points behind HACK | Fires 2024-07-22 | Fires 2023-06-28, session 20 of 20 | Does not fire | 47, 5.19% |

With earnings inside the window the -15% rule fired on 38 of 441 windows (8.62%), and on Fortinet 2026 it would fire from 10/30 on an earnings reaction. Both are why the vendor list is frozen and an issuer's own results are excluded.

**Limits:** windows overlap, so the rates are not independent; history is 2021-06 to 2026-11; HACK holds PANW, which slightly shrinks the gap; earnings dates are Yahoo's. SolarWinds cannot be tested (delisted, no price data). DEWEY's -23% over 2 days clears the -15% leg, the HACK leg is unverified.

**Calendar fact:** PANW reports fiscal Q1 after the close on Wed 11/18 (company release dated 11/03; secondary calendars say 11/19, the company wins). The 11/18 close is read before that print.

**Other two legs:** the cyber-gain and bank legs are also unsized. They were not asked. Today's readings would fire neither (HACK -0.5 points against SPY, banks ahead). HENRY owns the bank leg.

## 5. Boot re-checks, search level only

| Row | Reading | State |
|---|---|---|
| CYB-INC-005 Japan cluster | No official statement linking the incidents found. Taira's "emergency" remains a party remark. Prime Minister Takaichi spoke of "neutralisation measures" (Kyodo via Bernama, not opened) | REPORTED holds |
| CYB-INC-019 AI agents at banks | Schwab's CEO on record blocking outside agents (InvestmentNews, American Banker, not opened). Still no loss. ⚠️ A digit.in headline ties it to "PHP vulnerability exposure"; no source read supports that link | REPORTED holds |

## 6. Leads re-checked and closed, so they are not re-opened

| Lead | Why it is not row 1 evidence |
|---|---|
| "Japanese real estate company" (SOCRadar) | Desk read 10/29: the report itself says no link; intrusions ran 10/9-11. SOCRadar 403 today, read not repeated |
| "European government entity" (Unit 42) | Unit 42 retracted the initial-access link 10/25 (KB-CYP-046) |
| Kaspersky, 11/03 | Counterevidence: "no wave of breaches has materialized"; attackers picked 240 of about 19,000 devices found. A vendor blog, not a measurement |

## 7. Shinkin Kyodo Center outage (card SIG-W-20261106-005, arrived 10:09 ET mid-session; CYB-INC-062)

| Item | Reading | Basis |
|---|---|---|
| Event | 128 shinkin credit co-ops, Tokai and Hokuriku westward: counters, ATMs, internet banking and transfers stopped from about 13:30 JST on 11/06 | Nikkin quoting the Center, read; NHK, read |
| Restoration | From about 17:30 JST in stages (ABC), all services after 19:00 JST (NHK update 20:13 JST): about 5.5 hours | SECONDARY |
| Cause | Shinkin Central Bank and the Center: "機器の故障によるもので、サイバー攻撃に起因するものではないと考えている" (equipment failure, and they think it did not stem from a cyberattack). ABC: communications equipment, "とみられ" (apparently) | SECONDARY, operator quoted. ⚠️ A stated view on the day, not a forensic finding |
| Operator's own page | shinkin.co.jp and shinkin-central-bank.jp front pages carry no text on it to my reader | Not read at primary |
| Fake phishing emails after it | On WALTER's card; **not in anything CYPHER read** | UNVERIFIED by CYPHER |
| Zengin (interbank) failure | None found by WALTER; Nikkin says the co-ops' exchange transactions stopped. Whether same-day transfers settled late is unknown | Open |

**Judgment.**

| Test | Result |
|---|---|
| Row 8 | Not applicable by letter: it reads "outside Japan". NOT-FIRED stands, and the wave is not involved |
| Cluster watch, duration limb | Not met: "1 business day or more"; about 5.5 hours. ⚠️ 128 institutions is the widest count in the ledger; branches held staff back because they could not close the day (Nikkin) |
| Cluster watch, count limb | Already met 11/05 on Finzly and Abrigo; this does not add to it, since the watch is built on the US supplier list |
| Map | No CHOKEPOINTS row: the map is US finance |
| Consequence | SAM (Japan); LIQUID and REGINALD already INFO on the card |

**Viral claim:** "Japanese banks are collapsing as 128 banks went offline" stays do-not-relay: co-ops, none failing, posted after restoration.

**Also seen, headline only, not opened:** Nikkin 11/06 "government draws up emergency cyber measures"; NHK 11/06 "government approves JPY 10B from reserves for unauthorized-access measures". Logged to the Japan theme; a later session should read them.
