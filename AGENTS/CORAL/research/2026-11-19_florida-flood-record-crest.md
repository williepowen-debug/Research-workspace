# Florida flooding — record St. Johns crest, second rain event, no federal declaration (CORAL, 2026-11-19)

**Session:** coral-aj, Thu 2026-11-19 from 10:34 ET, on Will's word (PROME prome-36 letter, 10:34 ET: "lets wake CORAL for the continued flooding"). Opus 5.5 in Claude Code, laptop. Reads 10:34–10:39 ET (wall clock, `date`).
**Prior read:** `research/2026-11-17_amendment3-and-floods-impact.md` (11/17 evening) · evidence `STATUS_DETAIL.md` § AI2.

---

## Bottom line (plain words)

The flood got worse, not better. The St. Johns River near Cocoa passed its all-time record this morning (18.19 ft at 9:15 a.m. ET, against 17.55 ft in 1953 and 17.43 ft after Irma in 2017) and is forecast to rise to 18.4 ft tonight and stay there through at least Tuesday 11/24. That is a day earlier and 1.2 ft higher than the 17.2 ft crest forecast on 11/17, and 17.2 ft is the level where water enters homes. A second storm dropped 6 to 10 inches on central Brevard this morning (emergency-management reports via NWS), and the flood is now moving downstream: Lake Harney is forecast to reach major flood on 11/22, DeLand on 11/24. There is still no federal disaster declaration: the state asked on 11/09 for the 11/01–11/03 flood only, and the White House said on 11/18 that FEMA is still reviewing it. No insured-loss or claims figure exists for this flood from OIR, Citizens or the NFIP, and I found no city or county spending, fee or borrowing action.

**What it means for the thesis:** nothing moves. The damage is household and uninsured (flood is excluded from home and Citizens policies), it sits outside the five metros on the supply-side gauge, and the one bank with a large footprint in the flooded region (Seacoast) has its smallest presence in Brevard, where the worst of it is. The real exposure is on local budgets: the response bill lands now, a year before Amendment 3 cuts their revenue, and without a federal declaration none of it is reimbursed. A declaration would be permission, not money.

---

## 1. What is new since 11/17, and what is unchanged

| Item | 11/17 read | 11/19 read | Source, time | New? |
|---|---|---|---|---|
| **St. Johns near Cocoa (COCF1), stage** | 17.11 ft, major (00:15Z 11/18) | **18.19 ft, major, 14:15Z 11/19 (09:15 ET)**. Path: 17.26 (18:15Z 11/18) → 17.35 (00:15Z 11/19) → 17.63 (06:15Z) → 18.08 (12:15Z) → 18.19 | NWS NWPS API `gauges/COCF1/stageflow`, read 15:34Z 11/19 | **NEW** |
| COCF1 record | — | **Passed.** NWS flood warning 08:38 ET 11/19: "This passes the flood of record." Historic crests: 17.55 ft 10/11/1953 (NWS flags it **old datum**), 17.43 ft 10/06/2017 (Irma), 17.11 ft 8/31/2008 (Fay). Press quotes the record as 17.6 ft (Spectrum 11/19 05:41 ET; USA Today 11/19) | NWS NWPS `gauges/COCF1` historic crests; api.weather.gov alert | **NEW** |
| COCF1 forecast | 17.2 ft at 06Z 11/20 | **18.4 ft at 00Z 11/20 (7 p.m. ET 11/19), held at 18.4 ft through 12Z 11/24, the end of the forecast** — "expected to rise and remain steady" | NWPS forecast issued 13:29Z 11/19; NWS flood warning | **NEW** |
| Flood category | Major ≥ 17.0 ft | Major ≥ 17.0 ft. At 17.2 ft: "Water enters homes along the St Johns River in the Lake Poinsett area west of Cocoa, also low lying homes in the Silver Pines subdivision in Rockledge and the Shakespeare Park area of Cocoa. Providence Road … becomes impassable" | NWPS impact statements (COCF1) | thresholds unchanged; **now exceeded by ~1 ft** |
| Downstream gauges | GENF1 9.01 moderate → 9.2; SNFF1 5.38 → 5.6; DLAF1 3.78 → 4.0 | **Above Lake Harney (GENF1) 9.79 ft moderate → 12.3 ft MAJOR 11/22 18Z** (record 12.67 ft, Ian 10/2022) · **Sanford (SNFF1) 5.97 minor → 7.3 moderate 11/24** (record 8.96) · **DeLand (DLAF1) 4.32 minor → 5.5 MAJOR 11/24** (record 6.33) | NWPS, obs 14:30Z, forecasts issued 13:29Z 11/19 | **NEW: flood moves into Seminole, Volusia, Lake over 11/20–11/24** |
| Rain, event 1 (11/01–11/03) | 24.69 in, Malabar 1.9 SE (WPC final) | **Unchanged** — AEOLUS carries it | WPC Storm Summary #3 | unchanged |
| Rain, event 2 (11/18–11/19) | — | Melbourne airport: **2.61 in on 11/18, a daily record** (prior 0.71 in, 1959); **month to date 17.25 in vs 1.56 in normal** (through 11/18). 11/19: 1.37 in at MLB by mid-morning (IEM ASOS, partial day). NWS flash flood warnings 11/19: **"Between 6 and 10 inches of rain have fallen"** central Brevard (09:47 ET, emergency management reported); 3–7 in, Palm Bay / Port Malabar road closures, "life threatening" (10:02 ET); 3–6 in NW Brevard / E Volusia (10:09 ET). Fort Lauderdale 4.18 in on 11/18, daily record (USA Today via Yahoo 11/19, PRESS) | NWS CLIMLB issued 07:33Z 11/19 (PRIMARY) · api.weather.gov alerts 15:35Z 11/19 (PRIMARY, radar/EM-based) · IEM (one read, then refused "too many requests"; not retried) | **NEW.** No event-2 storm total exists yet; **AEOLUS owns the one figure** (packet sent) |
| Storm system | — | NHC 07:00 ET 11/19: non-tropical low expected to form Friday near the NW Bahamas; **20% (48 h) / 60% (7 d)** chance of becoming subtropical or tropical; "strong winds, dangerous surf, and coastal flooding are likely" along the SE and mid-Atlantic coasts into early next week | NHC TWOAT (PRIMARY) | **NEW.** AEOLUS owns the storm read |
| Active alerts (FL) | Flood watches to 11/19–11/20; Broward FFW | Flash flood warnings Brevard, Brevard–Orange, Brevard–Volusia (to 11:15–13:15 ET 11/19); flood warnings St. Johns in Brevard, Seminole, Lake–Volusia; flood watch Brevard–Martin + Orange/Seminole/Osceola/Volusia/Okeechobee **to 19:00 11/20**; SE FL flood watch to 19:00 11/19; **new flood watch NE FL (Duval, Clay, Putnam, St. Johns, Flagler) to 19:00 11/20**; coastal flood advisories Flagler to 11/22; wind advisory Brevard/Volusia coast to 19:00 11/19 | api.weather.gov `alerts/active?area=FL`, 15:35Z | **NEW** |
| Deaths | 2 (Palm Bay, event 1) | **No new death found** in sources read | press | unchanged |
| Rescues | ≈1,400 rescued or assisted (event 1) | **"At least two people" rescued 11/19 (Cocoa)**; water entering homes near Anderson Elementary, Rockledge (WFTV 07:15 ET 11/19) | USA Today via Yahoo 08:23 ET 11/19; WFTV live 10:13 ET (PRESS) | **NEW, small** |
| Evacuations / local emergencies | — | **Palm Bay: mandatory evacuation, part of Palm Bay Estates** (west of the canal, east of the railroad), voluntary for the rest (ClickOrlando 09:44 ET 11/19) · **Titusville: local state of emergency** (FOX 35 07:43 ET, WFTV 07:55 ET 11/19) · Broward state of emergency (USA Today 11/19, undated in the article) · Brevard schools closed through Thanksgiving week, back Mon 11/30 | PRESS | **NEW** |
| Homes damaged / registrations | ~2,000 homes damaged; ~2,000 self-reports (event 1, press) | **No new count found.** No FEMA individual-assistance registrations can exist without a declaration; the county runs a self-reporting damage survey, count not found | PRESS (WFTV 11/10; ClickOrlando) | unchanged; **event-2 damage unmeasured** |
| **Federal declaration** | None (OpenFEMA 01:10Z 11/18) | **None.** OpenFEMA rundate **15:35Z 11/19**: FL declarations since 10/25 = 15 rows, all DR-4955 (Isaias). White House (spokeswoman, to News 6, Wed 11/18): FEMA "is reviewing the Governor's request and will provide a recommendation to the President" (ClickOrlando 21:34 ET 11/18). Rep. Haridopolos: review "usually takes between two and four weeks" | OpenFEMA API (PRIMARY) · PRESS | status unchanged; **White House statement NEW** |
| What the state asked for | ≈11/09 request, scope not read | **Expedited Major Disaster Declaration, 9 counties: Brevard, DeSoto, Hardee, Highlands, Indian River, Martin, Okeechobee, Palm Beach, St. Lucie; Individual Assistance, Public Assistance (debris removal, emergency protective measures), Direct Federal Assistance, Hazard Mitigation** | PRESS via search summaries (Moody, Mast releases; CiberCuba 11/10). **FDEM letter itself NOT READ** | **NEW (scope), press-tier** |
| Federal Register | FEMA's DR-4955 notice unpublished | Still unpublished: FR API 11/19 shows only the two SBA notices (11/04) for 4955; FEMA FR docs since 11/12 are flood-map notices and one information-collection notice | federalregister.gov API (PRIMARY) | unchanged |
| Insured loss / claims | NFIP event claims not read | **None found.** OIR's only 2026 data call is Isaias (10/12); no flood data call (flood is excluded from homeowners policies). Citizens: no flood figure (does not write flood). NFIP: no event figure published. Economic estimates disagree ~10×: AccuWeather $3–5B total economic (11/0x, carried) vs Aon 11/06 "hundreds of millions" across FL and other states (search summary, **not read**). Brevard NFIP take-up ≈11.8% of residential properties (MyNews13 11/11 citing FEMA, search summary) | — | unchanged: **no insured figure** |
| County / city spending, fee, borrowing | none found | **None found** in sources searched. Context only: Brevard FY26-27 *proposed* budget: general operating reserves **9.25%, ≈$29.0M**; stormwater assessment unchanged >10 years, ≈$2.7M/yr flood-project gap (proposed budget PDF, search summary; adopted figures not read). Titusville / Palm Bay emergencies are declarations, not appropriations | — | unchanged |
| Amendment 3 certification | NOT CONFIRMED | **Still NOT CONFIRMED** — every 2026 report found calls the 61.98% unofficial | search 11/19 | unchanged |

**One-line delta:** the 11/20 dated read (crest vs 17.2 ft) is **answered a day early: 17.2 ft was passed at ~12Z 11/18; the record was passed by ~06–12Z 11/19; the forecast crest is 18.4 ft with no fall through 11/24.**

---

## 2. What it means for the thesis (CORAL's letters)

Each implication carries a dated horizon and its rival causes. **No colour, gate, grade or threshold moves.**

| Leg | Read | Rival causes named (cause not isolated) | Horizon (dated) | What would change it |
|---|---|---|---|---|
| **Supply-side leg (GATE-CORAL-MSI-01, 🟠)** | **No effect.** The five gauge metros (Tampa, Punta Gorda, North Port, Cape Coral, Lakeland) are outside the flood. The flood's housing effect is in the Palm Bay–Melbourne market, which no CORAL gate measures | For any Brevard listing / price move: mortgage-rate repricing (Dec hike priced, § AF4), statewide softening (SF new pendings −15.7% Oct), Citizens' 1/1/2027 flood-cover mandate, Amendment 3 | MSI #16 by **11/26**; first Brevard housing read = Space Coast MLS November **≈mid-Dec**, December **≈mid-Jan 2027** | — |
| **Insurer and Citizens channel** | Flood is excluded from homeowners and Citizens policies, so the direct insured loss sits with the NFIP (federal) and private flood carriers; most Brevard homes (≈88% of residential, press) carry no flood cover, so most of the loss is **uninsured household loss**. Citizens' exposure is second-order: (a) wind-driven water claims (wind advisory 50–55 mph gusts 11/19), unmeasured; (b) the **1/1/2027 flood-cover mandate** on Citizens policies lands on households who just learned what uninsured flood costs. ⚠️ **Interaction, dated:** NFIP authorization expires **12/11/2026**; a lapse would stop new and renewed NFIP policies three weeks before Citizens' mandate needs them | Citizens PIF falls for takeout rounds and depopulation regardless of flood; private flood pricing; Congress on NFIP has nothing to do with this flood | Citizens November month-end **≈mid-Dec**; NFIP **12/11**; Citizens mandate **1/1/2027** | An NFIP or OIR loss figure; Citizens commentary on flood-related non-renewals or takeups; NFIP lapse |
| **Local budgets under Amendment 3** | The response bill lands **now (FY26-27)**; the revenue cut starts **FY27-28 (from 10/1/2027)**: −$4.93B FY27-28 → −$11.83B recurring statewide (REC 7/10). **Without a declaration, public-assistance costs (debris, protective measures) stay 100% local and state;** with one, FEMA pays at least 75% of eligible PA (Stafford Act floor, recalled, not read today), by reimbursement over months to years. The same budgets then face the cut while carrying their share and any mitigation match. **No spending, fee, millage or borrowing action observed** | Budgets also move for ordinary reasons (FY26-27 adopted pre-flood; Brevard's proposed reserve cut to 9.25% predates the flood); any county fee move may be Amendment-3 positioning (Governor's fee-ban push) rather than flood | Agenda items **Dec 2026**; the special-session question before **1/5/2027** vs session **3/2/2027**; FY27-28 budget workshops **summer 2027** | A council appropriation, reserve draw, fee or millage move, borrowing; a rating action citing flood or Amendment 3 |
| **Municipal spreads (BOND's answer, integrated)** | **NOT REACHABLE free** (BOND 11/18, KB-BND-589): MSRB EMMA refused a plain client (HTTP 403), BOND stopped; no Florida-only fund found; MUB 103.01 [11/17] tracks Treasuries. MUB **$103.22, +0.07%, intraday 10:38 ET 11/19** (Yahoo via FORGE fetch, not a close). ⇒ **No market read of Florida municipal credit exists on this desk.** EMMA in a browser by a person is the only free route; **CORAL is not asking for it now** — no specific bond whose spread would change a decision (Palm Bay and Brevard debt not identified) | MUB moves with Treasuries | — | If a Brevard / Palm Bay bond is identified and a borrowing or rating event occurs, CORAL would name it and ask |
| **Bank-transmission rail (NOT met, NOT armed)** | **Unchanged.** REGINALD 11/18 (integrated): Seacoast discloses no county loan split; HMDA 2025: **31.3%** of its home-loan originations ($160.0M of $511.0M) in the five counties, close to the **35.68%** deposit share; **Brevard is its smallest of the five: 2.8% of originations, $0.38B (2.3%) of deposits.** This week's worst flooding is Brevard and Volusia (Volusia is not in the five-county set; Seacoast's Volusia share not read). Q3 credit clean: NCO 0.16%, nonperforming 0.54%, past due 0.20%. HMDA is one loan type (24% of book) and a flow, not the stock — county share of the whole book is REGINALD's inference | **Price, cause not isolated:** SBCF $32.24, −1.01%; KRE $69.97, −0.77%; SSB −0.77%; BKU −0.41% (Yahoo via FORGE fetch, **intraday 10:38 ET 11/19, not closes**). SBCF's −0.24 pp gap to KRE is inside a normal day. Live causes for regional-bank moves: HY OAS 343 bp [11/17], LIQUID's above-320 rule MET (WALTER SIG-W-20261118-010); the 10-year (REGINALD: it moves regionals); December hike repricing. **The flood is not credited with any move** | Seacoast Q4 release **≈late Jan 2027**; 12/31 Call Report **≈end Jan 2027** | A flood declaration with damage in Martin, Palm Beach or St. Lucie (REGINALD's named trigger; **not met**: event-2 damage is Brevard/Volusia, Palm Beach/Broward only under watch/advisory); a storm provision or past-due rise at Seacoast |

---

## 3. The four tests (CATO via PROME)

1. **Cause not isolated** — applied in the table: bank prices carry HY, rates and hike-repricing causes; any Brevard housing move carries rates, statewide softening, the Citizens mandate and Amendment 3; any county fee move carries the fee-ban politics. Nothing is credited to the flood that has another live cause.
2. **Permission is not funding** — what I have: **declarations of emergency** (state EO, Palm Bay, Titusville, Broward) = authority to act and spend, not money; the **state's federal request** = an ask; the **White House statement** = review under way. **Money disbursed: none observed** — no federal declaration, so no FEMA IA or PA; DR-4955 (Isaias) money is a different event; the FEMA DR-4955 FR notice with its cost share is still unpublished.
3. **Dated horizon on every implication** — each row above carries one; none is undated.
4. **Search limits, kept and stated** — below.

### Search limits (what I looked for, where, and what refused the reader)

| Looked for | Where | Result |
|---|---|---|
| Stages, forecasts, categories, record crests | NWS NWPS API (COCF1, GENF1, SNFF1, DLAF1, ARCF1) | read, PRIMARY |
| Alerts | api.weather.gov `alerts/active` | read, PRIMARY |
| Station rain | NWS CLI Melbourne (api.weather.gov products) | read, PRIMARY (Melbourne only; Daytona, Vero, Orlando CLIs not read) |
| Station rain, more stations | Iowa Environmental Mesonet ASOS daily | MLB read once; **then refused ("Too many requests from your IP address")** — stopped, not retried |
| Storm totals, event 2 | WPC storm summaries | **none found / not read**; AEOLUS asked |
| Declaration status | OpenFEMA DisasterDeclarationsSummaries (rundate 15:35Z 11/19) | read, PRIMARY |
| FEMA / SBA notices | Federal Register API | read, PRIMARY |
| State request contents | FDEM letter | **NOT READ**; press and member releases via search summaries only |
| Palm Bay city flood page | palmbayfl.gov | **HTTP 403** (refused) |
| CNN 11/18 story | cnn.com | **HTTP 451** (refused) |
| Palm Bay local news | news.thepalmbayer.com | 301 to another host, **not followed** |
| Claims | OIR newsroom / data calls; Citizens; OpenFEMA NFIP | **no flood figure exists or was found**; OpenFEMA NFIP claims not read this session (404 on 11/17) |
| Local spending | search (Brevard, Palm Bay council) | none found for November 2026; county and city agendas not read directly |
| Certification | search | none found; state results site blocked to this box (11/17) |
| Muni spreads | BOND (11/18) | not reachable free; EMMA refused BOND's plain client |

**Missing dependencies (laptop):** none needed this session (no Kalshi, gh or CourtListener use). Desktop Commander MCP failed to connect (not needed).

---

## 4. DOCKET L784 — the corrected sentence for PROME

Current row text (status cell, PROME 11/06) quotes: "local revenue −$4.95B / −$8.78B / −$11.86B". **Corrected sentence:**

> Amendment 3 Yes 61.98%, unofficial (certification not confirmed at 11/19); local revenue −$4.93B FY27-28 / −$8.71B FY28-29 / −$11.83B recurring (EDR Revenue Estimating Conference, 7/10/2026 estimate; replaces the 6/12 figures −$4.95B / −$8.78B / −$11.86B).

**L784 date (11/20):** this session covers the declaration read (none at 15:35Z 11/19) and the FR read (no FEMA DR-4955 notice). It does **not** close L784: the FEMA DR-4955 FR notice (cost share) and HM designation remain. Proposed re-date: **2026-12-04** (two weeks; Haridopolos' 2–4-week FEMA window for the flood request ends ≈11/23–12/07).

## 5. CORAL's 11/20 dated rows

- **Crest vs 17.2 ft (11/20):** **covered by this session** — passed; record; 18.4 ft forecast through 11/24. A **re-read is still owed**, re-dated, not closed: the actual crest and the start of the fall (**Tue 11/24**, end of the current forecast), and the downstream crests (Lake Harney 11/22, DeLand 11/24).
- **Federal declaration (11/20):** **covered at 15:35Z 11/19 (none)** — tomorrow's read is still needed; a decision can come any day. Re-date to the next session; standing watch **through 12/07**.
