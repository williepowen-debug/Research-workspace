# US diesel export ban: risk read

**Written 2026-09-28 16:57 EDT (Mon), BRENT live session, Will-directed. $0: no trade, no line moved, no grade.**
**Sources:** policy, legal and precedent sourcing is in [`2026-09-28_us-diesel-export-ban_source-research.md`](2026-09-28_us-diesel-export-ban_source-research.md). Tags there are [PAGE] (read at the page) or [SNIP] (search snippet only). An Opus research subagent wrote it; I re-read Trump's 9/27 quote and the 9/28 Yahoo article at the page. The balances come from my own EIA v2 API pull (primary). The tape is my own yfinance pull (single vendor; daily closes are not official settles).
**Answers:** WALTER SIG-W-20260928-010 ask (B). **§3 CORRECTED ~17:3x ET after CATO MR19: breach timings withdrawn, recast as conditional sensitivities.** Ask (A) was withdrawn by WALTER's own correction at 20:09Z.

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

## 3 · Transmission to OUR lines: CONDITIONAL SENSITIVITIES, not forecasts

> 🔧 **CORRECTED 2026-09-28 ~17:3x ET (CATO MR19, relayed by PROME; verified at `88da0c1fe`).** The first draft of this section multiplied Goldman's **retail** ¢/gal figures by 42 and read them as **futures-crack** moves, then derived **breach timings**: "F1's cushion gone ~8× in one week", "HEN-46 inside one week", "#6 ≥$50 ~1 week into stage 2; ~3–6 weeks after a ban". **×42 changes units; it does not establish transmission.** Retail diesel carries crude, refining margin, distribution/retail margin and taxes. A crack is wholesale/futures product minus crude, at a named hub and month. Counterexample: a 25¢ retail fall that comes with an equal fall in crude leaves the crack unchanged. **The breach timings are WITHDRAWN as findings.** They survive only as the labelled sensitivities below. Nothing here grades a gate. The same timings were in the WALTER/TERRY packets, STATUS and NEXUS as first committed (`6691e5661`, `4f92f6a15`, `6f6a12c40`); each carries this correction.

**What IS established:**
- **Direction.** NYMEX HO delivers in New York Harbor, a US location. A ban or voluntary retention adds US supply, so US diesel should weaken relative to crude and to ICE gasoil. If refiners then cut runs, US gasoline supply falls, so gasoline should strengthen. WTI should weaken relative to Brent.
- **The one observed reading (float day 9/23, yfinance closes):** HOX26 4.762 → 4.634 (**−$5.38/bbl** on product); Nov ULSD crack **109.49 → 102.45 (−$7.04)**; RBX26 +3.7%; Nov gasoline crack 44.81 → **48.14**. ⚠️ Brent rose ~$3.83 the same day on Iran, so the cause is **not established**. It is a proxy for how fast the futures crack can move on ban news, not a pass-through estimate.

**Sensitivities (IF-THEN; the assumptions are the claim):**

| Assumption set | Nov ULSD crack (9/28 settle-proxy $96.23; F1 $95; HEN-46 $90.16) | Nov gasoline crack ($39.93 at 16:12; #6 spike leg ≥$50) |
|---|---|---|
| **A. Full pass-through, crude flat:** Goldman's retail move shows up 1:1 in NYH futures, WTI unchanged | −$10.50/bbl per week ⇒ below $95 and $90.16 in week 1 | +$12.60/bbl per week once runs are cut ⇒ ≥$50 in week 1 of stage 2 |
| **B. Half pass-through, crude flat** | −$5.25 per week ⇒ below $95 in week 1, below $90.16 in week 2 | +$6.30 per week ⇒ ≥$50 in week 2 of stage 2 |
| **C. Crude falls with product** (WTI weakens on lower US runs, as 9/25's −$12.02 WTI−Brent suggests) | Crack falls LESS than product; may not cross | Crack rises MORE than product |
| **D. Voluntary curb only** (e.g. 25% ≈ 0.4 mb/d) | Direction the same, magnitude unknown | Stage 2 may never come if storage never fills |

- **Stage-2 start** also depends on the storage-fill [EST] in §2 (Gulf Coast 2–5 weeks), which carries its own caveats.
- **Goldman's $0.25 and $0.30 are unverified here:** the source file has them as a snippet via BOE plus WALTER's first-page read.
- ⚠️ **The instrument-vs-P&L point stands on its own logic, not on the sensitivities.** HO is NYH-delivered and the stranded barrels are on the Gulf Coast, so VLO's realized Gulf margins could fall more than the graded crack shows. That is direction only; magnitude unmeasured.
- **Crude:** 9/28 Nov-matched WTI−Brent is −$12.83 (BZX26 105.72 − CLX26 92.89). A mild negative for USO; not a thesis change.
- **#6:** the re-cross leg is not in play (the crack has not been below $30). Name the month on any fire (overlay #6).

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
| **Wed 9/30 10:30** | EIA weekly exports (week ending 9/25) | A sharp drop from ~1.3–1.6 mb/d is **consistent with** voluntary curbs but does not prove them: weekly exports are noisy (1,331–1,935 kb/d over the last 8 weeks; 851 in one Sep-2025 week). Look for a multi-week pattern plus refiner statements |
| **Wed 9/30** | Russia's producer diesel-export ban expires or is extended | An extension keeps global diesel tight ⇒ more political pressure on US exports |
| Weekly | AAA/EIA retail diesel ($6.45 AAA 9/28; $6.529 EIA wk-9/21) | Staying ≥$6.50 is the political trigger |
| Refiner statements | VLO/MPC/PSX on voluntary curbs | Unknown today: the biggest open fact |

**Owners:** F1 and the VLO card → TERRY (the trade-construction owner). HEN-46 → HENRY. Boundary #6 letter and routing → WALTER. Consumer pass-through → CARL. This note is an input and grades nothing.
