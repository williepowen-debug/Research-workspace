# C3 LIMB-2 CANVASS — Black Sea war-risk repricing, window 2026-10-06 → 2026-10-21

**Run:** 2026-10-21 (Wed) 21:23–21:27 ET (ask received 21:23 per the hook clock; commit 9449f14cb at 21:27:28 EDT per git) — STAMP CORRECTED 21:28 from `date`/git: the first version read "~21:25–21:40 ET (from `date`)", typed from narrative, not from `date`; osprey-1021, brought forward from Mon 10/26 on Will's word via PROME prome-56 (21:22 ET). **For HAWK to grade** (DOCKET L439; KB-HAWK-428/445). **OSPREY does not grade limb 2.**
**Window:** RIO anchor `RU-20261006-AFRAMAX-RIO-SOCHI` (10/06) → run date. **Letter (EXIT RULES §1, Channel 3, limb 2):** *"no war-risk-premium repricing (insurer/P&I reporting, via HAWK's cross-war enforcement read) in the same window."*
**Source set:** the WARRISK.tsv header enumeration (a STARTING set, never the scope), plus outlet-name-free queries and the TD6 proxy.

## 1. In-window numeric items found (each is a CLAIM with its own provenance; none is an underwriter or P&I primary)
| # | Figure | Unit | As-of | Who / chain | Scope stated | Grade |
|---|---|---|---|---|---|---|
| A | **0.2–0.5% → 0.6–1.0%** (before a 50% no-claims discount; ~0.3–0.5% after, vs 0.1–0.25%) | % of vessel value, hull war-risk QUOTES | **2026-10-09** (week-on-week) | **BPG Shipping** (Gennadiy Ivanov, shipping director) → Ukrainian Shipping Magazine → **Cyprus Shipping News 2026-10-19** (body READ) and **Türkiye Today 2026-10-14** (body READ) | Black Sea vessels generally; not tanker-specific, not Russian-port-specific | Named broker, two relays agree on figures. Quotes, not bound rates |
| B | **0.1% → 0.5%** in two weeks; "the 0.5% rate was confirmed by insurers as of October 6"; ≥1% forecast | % of vessel value | **2026-10-06** | **Konstantin Sobol**, founder of Marelis Navigation (freight broker / shipowner) → Latifundist → **UkrAgroConsult 2026-10-08** (body READ); also Türkiye Today 10/14 | Black Sea transit; example a 5,000 dwt $1.5M vessel; grain trade context; ~90% of the fleet hugs Romanian/Bulgarian 12 nm waters to avoid it | Named broker; "confirmed by insurers" is his word, no insurer named |
| C | **~$0.2M → ~$2.5M per tanker** ("recent months") | USD per vessel | reported 2026-10-12/13 | Evgeni Simeonov, Lukoil Bulgaria commercial manager (BNT) → Türkiye Today 10/14, Novinite | Oil tankers crossing the Black Sea | Already LEAD (KB-206): single interested source, per-vessel metric |
| D | **1.5% → 6%** "over the past three months" | % (base unstated) | ~2026-10-14 | Anonymous "maritime source", Türkiye Today 10/14 | Black Sea ships | Anonymous; unit/base unclear. Not usable as a print |

**Context that is NOT a rate:** a broker report of 10/13 notes rising enquiries for cover on Ukrainian ports and Danube voyages, with no new range (via Cyprus Shipping News). JWLA-035 and Swedish Club 452/2026 predate the window (9/16, 9/18). NATO's Black Sea surveillance build-up was announced 10/21. Lloyd's List (10/5, via a search summary) has the Black Sea–Med suezmax index, which "has an added premium due to the Russia-Ukraine war", at $801,077/day; that is a freight figure.

## 2. TD6 continuous proxy (Baltic Exchange, 135,000 mt CPC → Augusta) — the tripwire
| Week ending | TD6 | TD19 (Cross-Med, Ceyhan→Lavera) | TD6 ÷ TD19 | Source (body READ) |
|---|---|---|---|---|
| 2026-09-04 | WS285.67 | WS222.5 | 1.28 | The DCN weekly 9/4 (search summary) |
| 2026-10-02 | WS634.44 (+133) | WS625 | **1.02** | The Edge Malaysia, Baltic weekly 10/2 |
| 2026-10-09 | WS1008.33 (+87) | WS780 | **1.29** | The DCN weekly 10/9 (pub 10/12) |
| 2026-10-16 | ~WS1092 (+68) | WS720 (−60) | **1.52** | The DCN weekly 10/16 (pub 10/19) |
**Reading:** TD6 rose ~72% from 10/2 to 10/16 while TD19 rose ~15%. **The Black Sea-specific spread over the cross-Med benchmark widened inside the window** (1.02 → 1.52). That is the TRIPWIRE FIRING: it is the cue to look for a print, and it does not measure the premium itself. Freight also carries tonnage tightness: DCN's own Black Sea comment is "available tonnage remains tight"; neither report mentions war risk. Platts states (9/3) that its tanker assessments EXCLUDE AWRP; whether Baltic TD6 embeds it is not established.

## 3. Reachability, per outlet (HAWK's ask: 403/unreachable = UNMEASURED, never negative)
| Outlet | Status | What was reached |
|---|---|---|
| **The Insurer** | ⬛ **UNMEASURED** (paywall/401 on bodies, per prior runs; not re-fetched) | Search surfaced only its 7/21 and 7/29 headlines; no in-window headline surfaced. Index-level only |
| **Lloyd's List** | ⬛ **UNMEASURED** for rates (paywall) | Search summary of a 10/5 piece (suezmax index, freight); The Daily View is 7/21 (read: no figure) |
| **Insurance Day** | ⬛ **UNMEASURED** — no result surfaced from its domain | none |
| **Insurance Journal** | ◻ SEARCHED, nothing in-window surfaced (domain-filtered search) | none fetched |
| **Insurance Business** | ✅ REACHED — **negative in window** | Both hits are DEC-2025 vintage traps (558492 = 1 Dec 2025; 559204 = 7 Dec 2025), fetched and dated |
| **S&P Global Platts** | ⬛ **UNMEASURED** — 10/9 article "Russia's shadow fleet freight rates fracture on Black Sea premiums" **403** | Search summary only: Black Sea-origin vessels getting higher compensation for security/insurance late Sep–early Oct; no figure reached. Its last per-barrel AWRP seen is $2.1/bbl 7/20 |
| **Marsh** (Mortimer / Baker) | ◻ SEARCHED — no October statement found (open web) | Dec-2025 items only |
| **Gibson weekly** | ◻ SEARCHED — no October Black Sea weekly surfaced; index NOT fetched | none |
| **Noah Intelligence** | ⬛ **UNMEASURED** — no result surfaced | none |
| **Relays:** Cyprus Shipping News | ✅ REACHED — **item A** (10/19) | body read |
| beinsure | ✅ REACHED — pre-window (9/23 article; figures from earlier periods) | body read |
| Ship Universe | ✅ REACHED — pre-window (8/6) | body read |
| Maritime Executive · ofimagazine | ◻ SEARCHED — nothing in-window surfaced | none fetched |
| **Outlet-name-free queries** (3 run) | ✅ surfaced **Türkiye Today 10/14** (items A–D, body read), **UkrAgroConsult 10/8** (item B, body read), Modern Diplomacy 10/8 (**403**, UNMEASURED; its "~1% → 2% this summer" is a pre-window relay), Discovery Alert 10/7 (read: "no published post-incident figures"), BLiTZ 10/21 (not read) | — |
| **TD6** | ✅ REACHED — three in-window weeklies | §2 |

## 4. OSPREY's notes for the grader (not a grade)
- **Numeric repricing is reported inside the window by two named brokers (A, B).** Neither is an underwriter or P&I primary. The letter's parenthetical says *"insurer/P&I reporting"*, and whether a broker's quote counts under it is HAWK's call.
- ⚠️ **Scope mismatch, stated so it is not lost:** A and B are general Black Sea transit quotes, and the reporting ties them to the JWC listed area and to attacks off Romania and Bulgaria. They are not Russian-port tanker calls. Only C is tanker-specific, and C is a single interested per-vessel claim.
- ⚠️ **A letter-vs-meaning question I am ROUTING, not self-ruling.** The repricing reported in A and B is driven by attacks on NATO-coast shipping that the reporting attributes to RUSSIA (Romania 10/5, Obzor 10/6, Bulgaria 10/13, Sulina 10/14–15). The 9/19 self-ruling put an attacker limb on C3 limb 1 because a Russian strike was counting as evidence of Ukraine's campaign. **Limb 2 carries no attacker or cause qualifier.** As written, repricing caused by Russia's attacks would keep alive a channel that measures Ukraine's campaign against Russian tankers. This is the same defect shape. **I do not fix it**: the fix would make C3 easier to kill, in my own channel, the day before its clock. It goes to PROME and HAWK as a question.
- **Direction, in clock terms (LESSONS 10):** if HAWK grades limb 2 as REPRICING PRESENT, C3 cannot be killed on 10/27 even though limb 1 reaches 21/21 that day. The channel is then HARDER to kill and holds at 3, which keeps this desk's live mark. If HAWK grades NOT-REPRICING (for example, broker quotes not admissible, or Russia-caused repricing out of scope), the 10/27 kill turns on limb 1 alone. That makes it EASIER to kill.
- **Data clock:** WARRISK.tsv gets these as dated rows. The "Last real data refresh" header advances to 10/21 on **item A (BPG, 10/9)**, carrying its scope label. It is the first numeric print with a named originator since 9/18.
