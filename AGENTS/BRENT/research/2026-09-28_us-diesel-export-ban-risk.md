# US diesel export ban: risk read

**Written 2026-09-28 16:57 EDT (Mon), BRENT live session, Will-directed. $0: no trade, no line moved, no grade.**
**Sources:** policy, legal and precedent sourcing is in [`2026-09-28_us-diesel-export-ban_source-research.md`](2026-09-28_us-diesel-export-ban_source-research.md). Tags there are [PAGE] (read at the page) or [SNIP] (search snippet only). An Opus research subagent wrote it; I re-read Trump's 9/27 quote and the 9/28 Yahoo article at the page. The balances come from my own EIA v2 API pull (primary). The tape is my own yfinance pull (single vendor; daily closes are not official settles).
**Answers:** WALTER SIG-W-20260928-010 ask (B). Ask (A) was withdrawn by WALTER's own correction at 20:09Z.

## 1 · Policy state: FACT

| Date (ET) | Who | On record? | What |
|---|---|---|---|
| Tue 9/22 | Trump | yes | "I've said let's not send out the diesel. We make a lot of diesel" (OilPrice 9/23) |
| Tue 9/22 | Bessent | yes | "examining whether it's feasible ... whether a full or partial ban would work" |
| Wed 9/23 | White House official | anonymous | Politico's 90-day ban report is "fake" |
| Wed 9/23 → ~9/25 | Wright | yes | No flat ban. "We will not cease exports of US diesel, but may there be some tweak in where diesel flows" |
| Thu 9/24 | Wright → Marathon, Valero, Chevron, Exxon, Phillips 66, Citgo | anonymous ×3 (Reuters) | Asked whether they would support **voluntary** export curbs; "enthusiasm ... limited". Only Citgo commented on the record (against) |
| Fri 9/26 | Sen. Cruz on the refiners' trade-group (AFPM) call | Cruz yes; his White House source unnamed | "White House will not ban diesel exports" |
| **Sun 9/27 17:55** | **Trump** (Fox, Presidents Cup) | **yes, read at the page** | *"That can oftentimes lead to a little bit of an increase on gasoline for cars, so we're looking at it very seriously — we may do it."* |
| Mon 9/28 | Wright (UN) · White House official (anonymous, Yahoo 15:53) | yes · no | "trying to avoid a blunt hammer" · "No policy decision has been made at this time" |

- **Options short of a ban** (Yahoo 9/28):
  - ① voluntary export limits (Wright);
  - ② suspend the federal diesel excise tax (~24¢/gal; needs Congress) or regulations;
  - ③ state actions (Nebraska, Alabama).
- The Jones Act waiver already runs to 11/15.
- **Legal route (researcher's reading, NOT checked by counsel):**
  - EPCA §103's authority over *product* exports was repealed in the 2015 law that ended the crude ban.
  - The cited route is an IEEPA national-emergency declaration plus an executive order. That can be signed within days with no rulemaking, and would face litigation.
- **Precedent:** in 2022 export limits were floated twice (June, then Oct plus minimum-inventory rules), and Granholm sent a warning letter on 8/18/2022. **Nothing was imposed.**
- **Congress:** Grassley and Thune are open to it; Cornyn, Hagerty and Tillis are opposed. No bill.

**ASSESSMENT:**
- **Most likely:** a voluntary curb or "tweak".
- **A formal ban is a live tail, not dead.** The only principal who decides has said on record twice (9/22, 9/27) that he leans toward one. Every denial is from an aide or relayed.
- **What pushes the odds up:** retail diesel staying ≥$6.50 into October; Russia extending its product-export ban past 9/30, which keeps pulling US barrels abroad; the 11/3 midterms; heating season. AAA diesel is $6.45 on 9/28, down from the ~$6.53 record, which leans the other way.
- **No probability is stated:** there is no base rate to attach one to.

## 2 · Scale: FACT (EIA v2 API, week ending 9/18 unless stated)

| Distillate | kb/d or M bbl |
|---|---|
| Exports | **1,331** (4-wk avg 1,559; record 1,935 in the week ending 8/7) |
| Production | 5,159 (4-wk 5,215) ⇒ **exports ≈ 30% of output** (4-wk basis) |
| Product supplied (US demand) | 3,975 (4-wk 3,636) |
| Imports | 85 |
| Stocks: US / Gulf Coast (PADD 3) / East Coast (PADD 1) | **107.4 / 44.4 / 22.2 M** (Sep-2025: 120.6–124.7 M US) |
| Highest since 2015: US / Gulf Coast | 180.0 M (7/31/2020) / 62.4 M (8/21/2020) |
| Gasoline exports / stocks / refinery utilization | 838 kb/d / 206.0 M / 94% |

- A researcher's secondary source quotes Reuters at ~97 M bbl of distillate. **The EIA primary is 107.4 M, and the primary governs.**
- Destinations, Jan–Jun 2026 average (EIA monthly): Mexico ~220 kb/d, Netherlands ~203, Chile ~119, UK ~95. Europe's share is ~50% (WoodMac).

**How fast storage fills (my estimate, [EST]):**
- A full ban strands **1.33–1.56 mb/d, i.e. 9.3–10.9 M bbl per week.**
- **Gulf Coast:** 18.0 M bbl of headroom to its 2020 high ⇒ **~2 weeks** if the barrels stay in PADD 3.
- **Whole US:** 72.5 M bbl of headroom ⇒ **~7 weeks.**
- WoodMac: Gulf storage full "just over a month".
- **Working range: 2–5 weeks until refiners must cut runs.** Caveats:
  - the 2020 high is a demonstrated level, not tank capacity;
  - some barrels move to PADD 1 by the Colonial pipeline and Jones-Act ships (waiver in force);
  - demand and imports respond.
- **A voluntary 25% curb ≈ 0.4 mb/d ≈ 2.7 M bbl per week: about a quarter of a ban's force, in the same direction.**

## 3 · Transmission to OUR lines: ASSESSMENT on Goldman's scenario numbers

Goldman (9/26) frames this as a **scenario, explicitly not its base case**. I converted its figures to $/bbl myself (×42).

**Stage 1, while storage lasts: US retail diesel −25¢/gal per week ≈ −$10.50/bbl per week.**
- **VLO scale filter F1** (TERRY's gate; $95 on the matched November ULSD crack, HOX26×42 − CLX26):
  - 9/28 settle-proxy reading is **$96.23 (cushion $1.23)**.
  - Post-settle at 16:12 it reads $97.33. That is not a grade.
  - **One week of stage 1 takes out the cushion about 8 times over.**
- **HEN-46 "thesis dead" tier ($90.16, HENRY's):** inside one week.
- ⚠️ **The instrument understates the harm:**
  - NYMEX HO delivers in New York Harbor, and the East Coast is short (PADD 1 imports 85 kb/d; pipeline-constrained).
  - The stranded barrels sit on the **Gulf Coast**, where the export-heavy refiners run: VLO Q2 throughput was 3.0 mb/d, and it is called "most export-levered" by a secondary source.
  - ⇒ Gulf Coast realized margins could fall **more** than the HO crack shows.
  - The graded instrument would lag the P&L it stands for.

**Stage 2, once storage fills and runs are cut: US gasoline +30¢/gal per week ≈ +$12.60/bbl per week.**
- **Boundary #6** is WALTER's letter: a gasoline crack spike ≥$50, or a re-cross of $30 from below.
  - Matched crack at 16:12: **Nov $39.93** (RBX26×42 − CLX26) · **Dec $35.67**.
  - It needs +$10.07 on November and +$14.33 on December.
  - ⇒ **it plausibly crosses ≥$50 about one week into stage 2, i.e. roughly 3–6 weeks after a ban starts.**
  - The re-cross leg is not in play: the crack has not been below $30.
  - Name the month when grading (overlay #6: month-dependent).
- **9/23 (the float day):** Nov crack **$48.14**, $1.86 short of the spike leg. RBX26 rose 3.7% while HOX26 fell 2.7%: gasoline up and diesel down, the ban-shaped move. The timing matches; **the cause has not been established** (Brent was also up on Iran).

**Crude:** lower US runs ⇒ a weaker WTI relative to Brent.
- 9/25: −$12.02, the widest since 5/6, which Reuters read as ban pricing.
- 9/28 Nov-matched, 16:12: **−$12.83** (BZX26 105.72 − CLX26 92.89).
- This is a mild negative for USO (a WTI product), not a thesis change.

## 4 · What the tape says: FACT (yfinance closes; not settles)

| | VLO | MPC | PSX | PBF | DINO | XLE |
|---|---|---|---|---|---|---|
| 9/18 → 9/22 | **−8.7%** (413.28 → 377.14) | −8.3% | −6.0% | −7.4% | −7.9% | −3.4% |
| 9/22 → 9/28 | **+3.3%** (→ 389.57) | −0.1% | −1.3% | +4.1% | −0.5% | +0.5% |

- **Monday 9/28, after Trump's Sunday "we may do it":** HOX26 +1.5%, RBX26 −0.8%, VLO +0.6%. That is the **opposite** of the ban-shaped move.
- **ASSESSMENT:** the market is pricing the voluntary path (Cruz, Wright), or the Russia supply news dominated. Cause not established.
  - **If the market is wrong, the repricing is one-directional and fast** (9/23 template: HO −4% on the day, ICE gasoil up to +7%).
- The held VLO share: fill $412.00 (9/18) vs $389.57 ⇒ **−5.4%**. Recorded for scale; a mark, not a rule. Positions are TRADE.md's; the card is TERRY's.

## 5 · What to watch (dated)

| When | What | What it tells us |
|---|---|---|
| Any day | Executive order / IEEPA emergency declaration | A ban. No rulemaking lag; stage 1 starts within days |
| **Wed 9/30 10:30** | EIA weekly exports (week ending 9/25) | A sharp drop from ~1.3–1.6 mb/d ⇒ voluntary curbs are biting (same direction, smaller) |
| **Wed 9/30** | Russia's producer diesel-export ban expires or is extended | An extension keeps global diesel tight ⇒ more political pressure on US exports |
| Weekly | AAA/EIA retail diesel ($6.45 AAA 9/28; $6.529 EIA wk-9/21) | Staying ≥$6.50 is the political trigger |
| Refiner statements | VLO/MPC/PSX on voluntary curbs | Unknown today: the biggest open fact |

**Owners:** F1 and the VLO card → TERRY (the trade-construction owner). HEN-46 → HENRY. Boundary #6 letter and routing → WALTER. Consumer pass-through → CARL. This note is an input and grades nothing.
