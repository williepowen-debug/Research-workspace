# BRENT: the Jazan Port hit against BRT-32 and BG-02; barrels; price; dated rows; the BRT-23 Glencore read (D:L1266)

Session brent-desk-agent-2026-11-25-b, Claude Code, Opus 5.5 (claude-opus-5-5), laptop. PROME prome-77 woke this desk at 20:05 ET for one bounded follow-up on DOCKET D:L1266. Boot 20:06 EST (times from `date`). Evidence cutoff about 20:12 EST 11/25 (01:12Z 11/26). $0. Energy arm RETIRED (Will 8/7), energy STAND DOWN: nothing below is a trade proposal or a fired trigger.

Inputs: FALCON packet `inbox/processed/2026-11-25_from-FALCON_jazan-port-hit.md` and its record `AGENTS/FALCON/reports/2026-11-25_red-sea-followup-d1266.md`; WALTER SIG-W-20261125-016, -020, -023, -034, -042. Own capture `e1` (vendor one-minute and daily bars, 20:07:02–20:07:19 EST; `pull.py`, raw in `raw/`, windows in `window_e1.json`). Glencore primary saved in `glencore/` (sha256 bc1e5b0a…afbe6).

## 1. Grades by the letter

### BRT-32 (Yanbu loading halt, 20%, window 11/06 → 12/31): NOT MET by this event; stays OPEN

| Words of the letter | The Jazan event | Met? |
|---|---|---|
| "crude loadings at Yanbu stop" | Jazan Port is about 930 km south-east of Yanbu (great-circle, own arithmetic); no attack on Yanbu found (FALCON to 01:00Z 11/26; my searches to about 01:12Z) | **No** |
| "for at least 24 consecutive hours" | no stop of any length stated anywhere | **No** |
| "because of hostile action or a security threat" | a hostile act on a Saudi Red Sea port did occur (coalition-confirmed) | the cause class exists; the effect does not |
| YES needs (a) Aramco, energy ministry or SPA statement that loadings stopped, or (b) Reuters or Bloomberg report on shipping or trade sources | the only official source is the coalition spokesman (a military spokesman, neither class), and he states minor damage at Jazan Port, no loading effect | **No** |
| "A fall in volume without a stated halt is NO" | no volume print found either | n/a |

One reading only: the letter is site-specific (Yanbu) and effect-specific (a stated stop). No two-way question. Registered 20% is frozen. My unscored view of the event over the remaining window (to 12/31): **about 20%**, unchanged on balance. Up: the Houthis have now shown a confirmed hit on a Saudi Red Sea port and state a "port for port" rule tied to each Hodeidah strike; the September 2026 halt (Reuters 9/15) shows a halt can happen. Down: Yanbu is about 990 km from Saada (great-circle, own arithmetic; Jeddah about 620 km from Jazan), the round's only confirmed damage is at the nearest port, Jeddah's drone was intercepted, and a halt also needs the operator or a wire to say so.

### BG-02 (frame-breaker head clause): NOT MET under either reading of its liveness

| Words of the letter | The Jazan event | Met? |
|---|---|---|
| head clause "a confirmed **destroyed-capacity** event" | "minor damage", no capacity named, port operating status not stated | **No** |
| "clean FAL-01" (R4) | FALCON: production rung NOT FIRED, a port is out of class | **No** |
| "named-major with confirmed capacity loss" | no Aramco or other major named; no capacity loss | **No** |
| "vessel SUNK with confirmed loss of cargo or of Gulf export/transit throughput" | no vessel hit | **No** |
| R1: "an Aramco, MoE or SPA statement naming capacity offline" | coalition spokesman only; names no quantity, so C4 applies even if he counted ("a statement that names no quantity is not R1 met") | **No** |
| "≥0.7 mb/d of throughput", 7-day MA | no throughput figure exists | **No** |
| C1/C6 tracker | no tracker read offered; nothing to return as CORROBORATION WITHOUT SUPPORT | n/a |

**The rule reads two ways on one point, and I do not choose (sent to PROME for Will):** whether BG-02 is still a live letter at all.
- **Reading 1, live:** `TRADE.md` § POSITIONS header says "BG-02 remains binding" and § FRAME-BREAKER STATE lists "BG-02 head clause met on the letter" as gate (i) "at any fire"; my 11/10 record applied R1 to the Madinah pipeline statement as a live test. On this reading the Jazan event is graded and is NOT MET.
- **Reading 2, lapsed:** `setups/SPECS_GATES.md` § BG-02 lists "the window closing Fri 2026-09-25 17:00 ET (lapse = NOT MET)" among the unchanged terms, and `workbook/REGISTRY.tsv` header line 79 says "BG-02 is lapsed; this binds its successor resolver" (the successor was abandoned by Will 10/29, WQ-533 (a)). On this reading there is no live letter to grade and the event is not engaged.
- Both readings give the same answer tonight (no fire), and the three gates (head clause, WQ-192 lifted in Will's words, Will's [Approve]) are unmet regardless. The question matters only for a future event that meets the head clause.

## 2. Barrels on the Saudi Red Sea coast (to about 01:12Z 11/26)

| Site | State | Label | Source, time |
|---|---|---|---|
| Jazan Port (commercial port, Jazan Economic City area) | projectile hit, "minor damage", no civilian casualties; operating status NOT STATED; no Mawani suspension found | **CONFIRMED** hit (coalition spokesman al-Maliki on X, read via relays); effect NOT FOUND | Anadolu 11/25 (own read, no clock time), FALCON's relays (MEE 17:00Z first found, AFP 21:39Z); houseofsaud.com 11/25 (own read: "No suspension of port operations was announced by the coalition or by Mawani", single secondary) |
| Jazan refinery (Aramco, 400 kb/d) | not reported hit 11/25; my record RF-039 holds it ACTIVE outage since the 7/27 strike (last re-verify 10/29: OilPrice 10/27 "still shut", low reliability; Kpler 10/21) | **NOT FOUND** (hit); prior outage REPORTED, not refreshed | `refinery_damage/INCIDENTS.tsv` RF-039, RF-044 |
| Jeddah Islamic Port / Jeddah products terminal | drone intercepted near the port, no damage | interception **CONFIRMED**; Houthi "precise hit" **CLAIMED** | FALCON (Arab News, Reuters via Times of Israel, Xinhua); Boston Report 11/25 (secondary) |
| Yanbu (crude and products; Samref, YASREF) | nothing found | **NOT FOUND** | FALCON; my searches 20:1x EST |
| Rabigh | nothing found | **NOT FOUND** | same |
| Ras Tanura (Gulf side, for context) | four drones intercepted; refinery fire | interception **CONFIRMED**; fire **CLAIMED** | FALCON, The National |
| Aramco "9-month crude output -13.7%" | sidebar title only on houseofsaud.com | **NOT CARRIED** (unread, unverified source; WALTER flagged it too) | — |
| Yanbu November loadings about 2.7 mb/d (Kpler) | relayed in WALTER card 042 | **REPORTED**, secondhand | WALTER 042 |

**No export, loading or refinery effect is established anywhere on the Saudi Red Sea coast.** No Aramco, energy ministry, SPA or Mawani statement found; no Reuters or Bloomberg loading report found; no tanker-tracking print after 11/20 at a primary. Even a hit on the Jazan refinery would remove little current flow if it is still shut, which my record cannot confirm today. Jazan Port is not in BRENT's facility table (`INCIDENTS.tsv` takes facility-damage strikes; FALCON also excluded it from STRIKES as a commercial port), so no row is added.

## 3. Price (own capture e1, 20:07 EST; vendor proxy, not settles; CME blocks this box)

| Contract | 11/24 window [14:28,14:30) ET | 11/25 window | Change | Other 11/25 reads |
|---|---:|---:|---:|---|
| Brent January BZF27 | 91.4165 | **94.5689** | **+3.15 (+3.45%)** | last day-session bar 94.69 (16:54 ET); evening trades 94.49–94.60, 29 lots, last 94.60 at 19:25 ET |
| Brent February BZG27 | 88.7864 | 90.6538 | +1.87 (+2.1%) | vendor `BZ=F` is this contract: 90.63 |
| Brent March BZH27 | 86.6034 | 88.0174 | +1.41 | |
| WTI January CLF27 | 82.0556 | 83.6919 | +1.64 (+2.0%) | |
| M1−M2 / M1−M3 / M2−M3 | +2.63 / +4.81 / +2.18 | **+3.92 / +6.55 / +2.64** | | |
| Diesel HO−CL January | 71.64 | 69.81 | −1.83 | |

- Contract month: January BZF27 is the pinned Brent (last trade 11/30); the vendor's daily bar dated 11/25 already shows the evening session (29 lots), so the day's close is read from the one-minute bars, not the daily bar. PROME's BZF27 $94.44 at 16:07 ET and FALCON's $94.60 at 19:56 ET are their vendor reads; mine show 94.62 at 16:07 and 94.60 as the last trade (19:25 ET) carried to 19:56. FALCON's "belongs to the 11/27 session" is the usual Thanksgiving pattern; CME's holiday calendar is unreadable from this box, so that trade-date assignment is INFERRED, not verified by me.
- Secondhand "settles" seen: 94.61 (+3.5%, WTI 83.68) and 94.69 (+3.6%) on two low-grade aggregators (leprivatebanker.com, straits.live); not ICE or CME. They bracket my window VWAP within $0.12.
- **How much is Jazan: not separable.** The path: 89.54 at 03:00 ET, rising from about 03:40 ET (Ras Tanura interceptions overnight), 93.17 by 12:00 ET, so about +1.77 of the +3.15 came before the earliest Jazan relay FALCON found (MEE 17:00Z = 12:00 ET). A step of about +0.45 at 12:06–12:13 ET (93.14 → 93.59) came minutes after that relay, but WTI made the same step at the same minutes (82.99 → 83.52), the first wire time of the Jazan news is unknown, and nothing ties that minute to it. The last +0.9 drifted in through the afternoon. So at most about $1.4 of the $3.15 could be Jazan, and a Red-Sea-specific premium is not shown: WTI rose nearly as much. PVM's Tamas Varga is reported (secondhand) citing the Houthi risk premium and short covering before the US holiday; managed-money shorts were at a 15-row ledger high at COT #15 (137,797, as-of 11/17). The rest: January expiry-week mechanics in M1, and EIA's week 11/20 gave the tape nothing (muted at 10:30, morning note).
- **My own unregistered description crossed.** SCRATCH carried "M1−M3 above about +6.3 while flat price rises" as a signal to watch. At the 11/25 window M1−M3 is +6.55 with flat price +3.15. It is a description, not a registered line: it fires nothing and moves nothing. Part is January expiry; but February−March also widened +0.45 (+2.18 → +2.64), so the front is pricing nearer-term tightness beyond the expiring month, with no barrel lost.

## 4. Dated rows

| Row | Changes? | One line |
|---|---|---|
| OPEC+ Sun 11/29 (D:L913; CATALYSTS 2026-11-29) | **No** | Graded on the Secretariat statement against its three outcomes; the deliverability gate still needs a fresh spare-capacity pull. The Red Sea threat raises the stakes of spare, it does not change the letter. |
| BRT-33 (windows 11/25, 11/27; read 11/30; hard limit 12/02) | **No** | The 11/25 window read tonight from capture e1: **+6.5515, valid** (both legs positive volume; 11/23 +4.8917 and 11/24 +4.8131 reproduce to four decimals as a control). Valid 12, none under +3.5000. The grade stays at the first read after 11/27: NO unless the 11/27 window prints under +3.5000, which needs a one-session fall of about $3.05; my projection about 1%. Friday is a short session; the 11/27 window may print no bars (NO OBSERVATION), which changes nothing. |
| `MKT-BZ-F-BELOW-85` | **No** | Graded on the pinned BZF27 (REGISTRY header ①): 94.57 at the window, $9.57 above; the event moved it away. ⚠️ At the 11/30 roll the pinned contract becomes February (90.65), so the distance shrinks by about $3.9 from the roll alone: a basis change, never a move. MARCO consumes this row (ENR-02). |
| GATE-BRENT-COT-35B (review 11/30, COT #16) | **No** | #16 is as-of Tue 11/24, before Wednesday's rally, so any pre-holiday short covering on 11/25 cannot appear until #17 (as-of 12/01). For #16 to leave NOT-SPENT, shorts must fall 19,472 or more. |

## 5. BRT-23: the dated Glencore read (carried item; done tonight)

PROME held my 11/25 class C10 regrade (BRT-23 FAILED → CONFIRMED) as UNVERIFIED until I read the dated Glencore notice. Read:

| Document | Date | What it says | Label |
|---|---|---|---|
| Reuters via Kitco, "Glencore halted some cobalt deliveries over Congo export ban" | **2025-06-11** | "Glencore declared force majeure on some deliveries of cobalt from Democratic Republic of Congo", days after Congo suspended exports | REPORTED (Reuters, own read at Kitco); mining.com copy 403, not retried |
| Glencore First Quarter 2026 Production Report (primary, Baar, **30 April 2026**, saved `glencore/`) | 2026-04-30 | Own-sourced cobalt 5,800 t, 3,700 t (39%) lower than Q1 2025, "mainly due to the introduction of the DRC's export quota system in late 2025, as a result of which our DRC assets are now prioritising copper production"; the words "force majeure" do not appear | **CONFIRMED** at the issuer |
| Reuters via Kitco 2026-04-30; Semafor 2026-05-04 | 2026 | no force majeure in either; Semafor calls the cobalt fall "a deliberate move to avoid producing material it cannot export under its 2026 quota" | REPORTED |

**Finding: my regrade's stated basis is wrong.** The Glencore force majeure is dated June 2025, about nine months before BRT-23 was registered (2026-03-07) and before the Hormuz closure; it cannot be the event the letter predicts. My C10 regrade cited it as the met event, so **the regrade is withdrawn and the row's status is restored to its prior FAILED** (the state before my act), pending Will.

**The rule now reads two ways on a different basis, and I do not choose (to PROME for Will):**
- **Reading A, CONFIRMED:** the 30 April 2026 report is a major DRC SX-EW copper/cobalt operator announcing a significant curtailment (cobalt −39%, copper prioritised) by May 2026, inside "By May 2026". Against it: the clause "within 60 days of Hormuz closure persisting" (closure about 2/28, so about 4/29; the report is 4/30), and the cut began with a quota imposed in late 2025.
- **Reading B, FAILED on the letter:** no force majeure or curtailment was ANNOUNCED within the 60 days; the 30 April report discloses a cut already under way since the late-2025 quota (before registration), and a quarterly production figure is not an announcement of curtailment.
- Either way the sulphur-cost mechanism stays FALSIFIED and is the lesson. BRT-28 (FAILED on the letter, FRED-based) is unaffected and PROME already accepted it.

## 6. Combination watch (logged, moves nothing)

- `combo:yanbu-bypass` (review 11/30): Jazan Port hit, minor damage (CONFIRMED, coalition); Jeddah drone intercepted (Houthi hit CLAIMED); "port for port" rule (CLAIMED, Saree). Counterevidence: no Yanbu, Rabigh or King Abdullah Port attack; no Mawani, Aramco or carrier notice; Jazan refinery already shut per my record.
- `combo:gulf-access-cost` (review 11/30): "Red Sea war insurance rises" (WALTER 034, title only, unread). Still no war-risk or TD3C print read.
- Baker Hughes 27 Nov (published early): oil rigs 470 (+1), total 607 (WALTER 034, FirstSquawk text; issuer 403): record only, BRT-26 retired.

## 7. Forward view (unscored, not registered)

- **Brent (January to 11/30, then February), horizon two weeks:** I expect the front to stay bid and the curve steep while the Houthi-coalition exchange runs, with flat price held between about $88 and $98 (February basis about $3.9 lower after 11/30). Why: a demonstrated hit on a Saudi Red Sea port and an explicit retaliation rule, while Hormuz is still near shut (PortWatch 1 to 4 a day, FALCON) and OPEC spare is about zero (EIA STEO 11/10). Meaningful alternative (about 35%): the premium fades by 12/09 as it did after 11/20, with no barrel lost, the coalition pausing on Hodeidah, and a surplus narrative (IEA Q4 +1.7 mb/d forecast) back in charge; then February back toward $85–87. Tail (about 10%, matching FALCON): a state-stated loading cut at Yanbu, Jeddah or Rabigh; then the front gaps $5–10 and M1−M3 widens further.
- **Saudi Red Sea loadings:** I expect no stated loss this fortnight (about 90%). What would change my mind: a launch at Yanbu or Rabigh, any damage at Jeddah's terminal, a carrier or Mawani notice, a JWC or insurer re-quote, or a tracker fall in both Kpler and Vortexa.
- **Thanksgiving thin trade:** moves on Thursday and Friday are weak evidence either way.

## 8. Gaps

- Jazan clock time and the exact facility hit inside the port: not established; al-Maliki's X post not read directly.
- No tanker-tracking print after 11/20 at a primary; Lloyd's List, TradeWinds, Argus and Kpler not reachable without accounts.
- Reuters' 11/25 settle story not found; the two settle figures are aggregators.
- CME's holiday calendar and settlements unreadable (IP block, standing since 10/28).
