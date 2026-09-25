# MIDAS — STATUS

**Last Updated:** 2026-09-25 ~10:xx ET (Fri). **WILL-DIRECTED BOOT after 14 dark days: news catch-up, silver/Pt/Pd made first-class coverage (Will's word), full-page STATUS re-base.** The 9/11 page is preserved verbatim at `analysis/STATUS_ARCHIVE_2026-09.md` §⑩, off the boot path, and every obligation on it is re-homed below. **M1 holds 4. Composite 8/20 UNCHANGED. Zero capital. No card, no order, no band or threshold moved.**
**Class:** Market-agent (metals as macro tells) · **Spawnable by:** PROME or Will · **Fleet maturity: L4** (FLEET_MAP since 2026-09-08; DAEDALUS PR6 9/17 — this line read L3 until today) · **Cadence: WEEKLY** (declared 9/25, WQ-295) · **Instrument coverage: tier 2** *(spot/yield/GSR/LME + the contract-identity guard via `metals_watch.py`; gold COT via `cot_gold.py` = boot leg 3; **silver/Pt/Pd COT via `cot_metals.py`, new 9/25, on-demand**; one-shot graders on-demand by design)*

> ### 🔴 LIVE MARKS — explicit contract months, settled closes [9/24 unless stated]. Never the `=F` pointer.
> | Metal | Contract | 9/24 | since 9/9 | since 9/10 | ETF (9/24) | ETF off its 2026 high |
> |---|---|---|---|---|---|---|
> | Gold | `GCZ26` | **$4,298.00** | −3.65% | −2.48% | GLD $391.69 | −21.0% (1/29) |
> | Silver | `SIZ26` | **$64.00** | −6.77% | −1.43% | SLV $57.62 | **−45.4%** (1/28) |
> | Platinum | `PLV26` | **$1,752.0** | **−8.70%** | −2.73% | PPLT $15.90 | −37.0% (1/23) |
> | Palladium | `PAZ26` | **$1,282.1** | −7.16% | −0.97% | PALL $23.00 | −38.1% (1/28) |
> | Copper | `HGZ26` | $6.79 | — | — | CPER $40.65 | — |
>
> **GSR 67.16** (explicit months; the `=F` pointer ratio mixes months: 66.97) · **Pt/Pd 1.37** · **Pt/Au 0.408** [9/24]. **DFII10 2.76 [FRED 9/23] = highest since 2008-11-25** (full series n=5,936; the 2023 peak was 2.52). Path: 2.46 [9/9] → 2.55 [9/10] → 2.60 [9/11] → 2.68 [9/16] → **2.76 [9/23]**. **Fed +25bp to 3.75–4.00% on 9/16** (first hike since 2023). **LME Cu 251,175t [24 Sep] = +7.0% vs the 2yr median 234,750t.** **Gold COT net/OI 56.19% [as-of 9/15] = 99.31th pct** of 2010–26 (n=868). That vintage is from the day BEFORE the hike. → KB-116/117
> ⚠️ **Contract identity [9/24 guard]:** `GC=F` = `GCZ26` (OK). `SI=F`/`HG=F`/`PL=F`/`PA=F` are all **DYING** (0–2.6% of front-month volume). ⚠️ **`PLV26`→`PLF27` roll is close:** 25,587 vs 14,932 lots [9/22], and `FRONT_MONTHS` has to be rolled by hand.
>
> ### ⛔ THREE STANDING INSTRUMENT WARNINGS (each bought by a published error; full text → archive §④/§⑩)
> **① No settle from this vendor (KB-088).** The daily bar tracks the last trade of the calendar day, not the 13:30 ET settle. Label intraday figures IN-FLIGHT. **② `=F` pointers are roll-contaminated across the WHOLE complex (KB-080/087/112, L-40).** The guard is mechanised (`check_contract_identity()`, rc=1 REVIEW). Quote the explicit month; never a cross-roll delta; **GLD is the no-roll arbiter**; never take a settle from `fast_info`. **③ A bar that can still move is not a close (L-37, KB-079).** Pull twice and diff; re-confirm T+1. 📏 **8/7 marks:** settled gold **$4,340.70** = MIDAS-06's branch-(a) key (HEARTBEAT Am.#2, KB-038).

## ✅ HEADLINE — GOLD HAS ABSORBED A FED HIKE AND +21bp OF REAL YIELD FOR UNDER 1%, AND MY OWN VECTOR-3 FALSIFIER FIRED (KB-115)

🔑 **VECTOR-3 (9/11, KB-114/L-51):** gold hedges the *disinflationary consequence* of an oil shock, never the shock. Its response is **monotone in the same-day ΔDFII10**: on 168 Brent ≥+3% sessions since 2017, **≤−3bp gives GLD +1.071% (81% up)**, **>+5bp gives −1.063% (20% up)**, unconditional +0.138%. ⛔ **Univariate. Never cross-attribute to BOND's decomposition (L-35).**
🔴 **RE-MEASURED 9/25, as the standing instruction requires. The two instruments now DISAGREE, and both are reported:**
- **Rolling beta, GLD % on ΔDFII10:** **−0.1551 %/bp (t −4.42, n=120, to 9/23)**, down from −0.1860 on 9/11. 60-session −0.138 (t −2.89); **20-session −0.122 (t −1.85, not significant).** **The −0.08 flip is NOT reached, so the beta does not retire the read.**
- **The memo's own falsifier FIRED on the letter.** It needed 2 sessions in 10 with ΔDFII10 ≥+5bp AND GLD ≥+0.5%, and got **9/11 (+5bp exactly, +0.61%)** and **9/18 (+7bp, +0.71%)**. One of the two sits ON the boundary.
- **The aggregate sides with the falsifier:** 9/10 → 9/23 DFII10 **+21bp**, GLD **−0.88%**; the beta implied about −3.3%.
⇒ **The direction is decoupling since 9/10; the regression is slower to show it than the count.** Not resolved backwards either way (`finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect`). **Offsets in the flow data:** August ETF inflow **$18bn**, holdings a record **4,189t** (WGC 9/9); **PBoC +20.2t in August**, the largest month since Oct-2023. The weak leg is China physical: **SGE withdrawals −27% y/y**. → KB-116
📖 **BOOK READ (9/11, for TERRY/Will; NO card, $0):** keep the 16 GLD shares, but stop calling them a duration hedge. ⚠️ **The falsifier firing weakens the "drag" half of that read.** GLD and USO fail *together* in the 2022 corner (Brent −26%, GLD −21%, DFII10 +278bp). **TERRY owns any action and still owes the TLT $77P delta vs 0.0504.** Full arithmetic → `analysis/2026-09-11_VECTOR-3-…md`.

**Carried from the rotated page (live, cite exactly):** MIDAS-08 **TERMINAL (b)** 9/5 (Δ −1.9163pp vs −2.00pp): M1 holds 4, **no BOND correction owed** (KB-109). Gold 8/28 → 9/1: **cite −2.95%** (three bases within 0.064pp), never a bare 1-day 9/1 figure. **Nobody carries −2.35%** (KB-111). **MIDAS-06 CONSUMED and TERMINAL** (graded (a) 8/31, M1 3 → 4). The band fence was honoured; do not re-litigate.

## ▶ NEXT — what is actually open
1. 🔴 **Send PROME/TERRY the KB-115 falsifier result.** It bears on how GLD is described in the book.
2. 🔴 **M1 STILL HAS NO LIVE REGISTERED TEST.** WQ-161 is now canon (`FORGE/PREDICTION_DISCIPLINE.md`, read 9/25). A successor must register the **beta** (window + vintage + flip) and name the grading basis for every observation (WQ-162). *NO-VERDICT vs (d) INDETERMINATE* is settled by WQ-161 ①: non-resolution = STATUS, no mass.
3. 🔴 **Silver/PGM bands = WILL'S DECISION.** Draft at `analysis/2026-09-25_silver-pgm-bands-DRAFT.md`. Without bands, M2 and I2 cannot score a price move of any size.
4. **9/30 triple:** MIDAS-01 + MIDAS-02 on their frozen letters, **ALL BASES printed** (WQ-91), including `GCZ26`/GLD and `HGZ26`/CPER. **STUCK, not MISS, if data is unavailable.** **MIDAS-02's RED bar is DECLARED FROZEN at the pinned 479kt, with both bases printed** (OPEN_ITEMS 22). China September construction is ZHAO's settler.
5. **Roll `FRONT_MONTHS` `PLV26`→`PLF27`** when volume crosses. **MIDAS-09 (silver vs gold, GLD/SLV) and MIDAS-10 (Pt vs Pd, PPLT/PALL) resolve 2026-10-30** on frozen 9/24 baselines (first silver/PGM rows, registered 9/25). ✅ PROME L429 answered (the GSR mixed-month line now prints in `metals_watch.py`); ✅ DAEDALUS PR6 answered.
6. 🟠 **NEXUS_BRIEF.md is 72,126 B vs a 22,785 B stop** (PROME notice 9/24).

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **M1** | Gold: debasement / real rates (v2, kill-cond #3 FIRED) | **4 🔴** = | **Premium re-asserting against a record real-yield regime, on two instruments that disagree on how fast** (KB-115, above). **MIDAS-06 branch (a) survival, stated not re-graded:** rate leg holds (2.76 vs the 2.40 key); **gold leg now FAILS on both bases**: `GCZ26` $4,298.00 is −0.98% below the $4,340.70 key (and that comparison crosses the Q→Z roll in gold's favour), and GLD is −1.70% below its 8/7 close ($398.47 → $391.69). **Registered flip ($4,050 with DFII10 ≥2.40) NOT fired: gold is 6.12% above it** ⇒ M1 holds 4. ⛔ **THE THREE CARVE-OUTS THAT TRAVEL WITH THIS SCORE** *(adopted verbatim by BOND 9/1)*: **diverge-test-not-composition** (COT #3 fired 8/28 ⇒ part of the 8/19 residual is spec flow, share unquantified, KB-090) · **rates-ASSISTED, not rates-EXPLAINED** · **un-banded**. ⛔ **CITE 87.7–91.1% unexplained (UNIVARIATE, COMPUTED)**; currency-stripped 90–93% and two-factor 61–69% answer different questions, and the beta is a fourth construction. **Never cross-attribute (L-35).** ⛔ A bare **"+2.00σ / top 5.3%" is kill-on-sight** (GLD-only). | monetary root (shared w/ M2) | DFII10 **2.76 [9/23]**; `GCZ26` **$4,298.00** / GLD **$391.69 [9/24]**; **beta −0.1551 [120 sess to 9/23]**; **net/OI 56.19% [COT 9/15, 99.31th pct]**; PBoC **+20.2t [Aug]**; ETF **4,189t [Aug]** | ⛔ **No live registered test.** A successor registers the beta (window + vintage + flip level), not only a level pair (L-51) |
| **M2** | Silver + gold/silver ratio | **1 ⚪ BAND-BLIND** = | ⭐ **Silver is first-class coverage (Will 9/25).** **SLV −45.4% from its 1/28 high, and this cell read "dormant" the whole way down.** The only band is the GSR, and a ratio cannot see a crash in which both legs fall. **So `1` means UNSCOREABLE, not calm.** Since 9/10 silver has held **better** than gold (`SIZ26` −1.43% vs `GCZ26` −2.48%), so industrial weakness is not dominating the tape. Headwind: solar thrifting (PV silver demand −19% in 2026, secondary). JPM FY forecast $60–65 (from $81). 2026 deficit 46.3 Moz, 6th straight year (secondary). ⚠️ **GSR is basis-robust across the Q→Z roll** (artifact 0.029 pts, KB-067). Four-mechanism frame → THESIS §M2 re-base | monetary root (shared w/ M1) + industrial | GSR **67.16**; `SIZ26` **$64.00**; SLV **$57.62 [9/24]**; silver COT → `cot_metals.py` | GSR >85 for 3+ sessions → 2; >95 → 4. **Standalone silver bands: Will's decision (draft filed)** |
| **I1** | Copper: Dr. Copper / China | **1 ⚪ UNSCOREABLE↑** = | 🔴 **The read is AMBIGUOUS (KB-113):** COMEX holds **695,624t [9/4] = 2.96× LME** while LME and SHFE fell, so the LME drawdown may be tariff **diversion** (a shipping manifest), not tightening. Relocation is not purchase: real demand needs all three venues falling. 🆕 **LME has since RE-BUILT: 234,750t [10 Sep] → 251,175t [24 Sep] = +7.0% vs the 2yr median.** Not a band fire; read with KB-113. **Registered discriminator fired 8/31 for the structural read:** construction **46.9, a record low**, with copper firm (KB-107 corrected my 9/2 wrong-leg grade, L-48). ⛔ **My branch set is not MECE**: recorded, not repaired (WQ-91). **ZHAO's settler, adopted:** September construction ~9/30; a rebound >47.5 retires the weather reading, a third sub-47 retires weather entirely. ⛔ **Construction→copper LAG is UNESTABLISHED; "no lag estimate" is not "no lag".** ⛔ **−41.3% China import figure is NOT ZHAO-verified.** | industrial/China root (separate from monetary) | construction **46.9** · composite **49.5 [NBS Aug]**; `HGZ26` **$6.79 [9/24]**; **LME 251,175t [24 Sep]** vs median **234,750t (n=507)** | copper QoQ < −5% → 2; conjunction fire (5) needs copper −20% **AND** inventory +100%. ⚠️ **Bands are all-downside (L-13(a)); upside design constraint RATIFIED 8/21, no build commissioned** |
| **I2** | PGMs: platinum / palladium | **2 🟡** = | ⭐ **First-class coverage (Will 9/25); PGMs carry a precious leg as well as an industrial one.** They peaked with gold and silver in the same January week. **PPLT −37.0% and PALL −38.1% off their highs**, and this cell has no band that sees price. **Pt was the weakest of the four since 9/9 (−8.70%).** **Pd: UBS raised targets 9/21** (+$200/oz for Dec-26 and Mar-27) on falling mine supply. ⛔ **The US duty channel on Russian Pd is CLOSED** (USITC negative 5/29, no order; KB-101; THESIS corrected 9/25). 🔴 **n=3 Pd-led tail events. CITE +4.03σ** (8/28; the in-flight +4.72/+4.53 are superseded). **The score held at 2 is a deliberate refusal:** no registered trigger fired, and moving it would be setting a threshold, which is Will's. **The n=3 premise is itself unruled:** HAWK's country discriminator must use RAW RETURN, not σ, and on that basis 8/4 is not Russia-only and 8/28 is not SA. ⛔ **BIS export controls still unprobed.** | supply root (SA/Russia) + precious leg | `PLV26` **$1,752.0** / `PAZ26` **$1,282.1 [9/24]**; Pt/Pd **1.37**; Pt/Pd COT → `cot_metals.py` | confirmed major SA/Russia outage → 4. **Price/positioning bands: Will's decision (draft filed).** Absent instruments: **PGM lease rates · NYMEX PGM stocks · PPLT/PALL flows** |

**Composite: 8/20** *(M1 **4** + M2 1 + I1 1 + I2 2). **UNCHANGED:** a Fed hike, a 17-year real-yield high and a fired falsifier all landed, and none is a registered trigger. ⛔ **Three of four channels are band-blind, not calm** (M2 and I2 have no price bands; I1 is `UNSCOREABLE↑`). The composite understates by an amount this desk cannot quantify without Will's band rulings.*

**Independence:** M1 and M2 share the monetary root, so count it once. The 9/10 five-metal liquidation was **one discount-rate root** hitting every real asset, not four signals. **Gold fell least, so gold is the defensive METAL but not the defensive ASSET against a real-yield shock.**

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

**Kill rail re-derived: 2026-08-07.** *(Levels refreshed 2026-09-25 to 9/23–9/24 closes; the RULES are unchanged and no leg was re-derived, so the stamp is NOT restamped: `finding_hygiene_commit_rearms_the_staleness_lie`.)*

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| M1 (v2) | gold <$3,317 without a yield spike · WGC CB buying <100t/q · **gold re-decouples UP for 3+ weeks** *(weekly endpoint basis, RULED 8/21, L-12)* | `GCZ26` **$4,298.00**, **29.6% above** the $3,317 shelf; **CB Q2 288.9t = 2.89× the 100t line**. ⚠️ **CB custody relocations are NOT purchases** (DNB/BdF sale-and-repurchase, NET ZERO tonnage, KB-110). **3wk 9/2 → 9/23: DFII10 +31bp, GLD −2.46%** ⇒ the shape is absent | **🔴 FIRED** (leg 3, 7/17 → 8/7 window). Legs 1–2 measured and clear |
| M2 | GSR >95 sustained (risk-off) | GSR **67.16 [9/24]** | NOT-FIRED ⚠️ *and blind to a both-legs-down crash* |
| I1 | copper −20% AND LME inventory +100% | `HGZ26` **$6.79**; LME **251,175t = +7.0%** vs median | NOT-FIRED ⚠️ *(L-13(a): cannot score this direction)* |
| I2 | major SA/Russia PGM supply outage/sanction | `PAZ26` **$1,282.1**, no outage evidence; US duty channel closed | NOT-FIRED |

**Fired-count: 1 of 4.** ✅ Will RULED 2026-08-21 (row 65, `PROME/proposals/2026-08-21_midas-rows-65-69-RULED.md`): weekly-continuous DECLINED and the retroactive re-mark REFUSED, so the endpoint basis and the 7/17 → 8/7 fire STAND.

**Bidirectional flip:** **falsifies premium re-assertion** if gold retraces below **~$4,050** while DFII10 holds ≥2.40, which re-instates the "re-coupled/capped" frame and moves M1 → 2 (**not fired: +6.12% clear**). **Confirms and escalates** if DIVERGE repeats on a rising-yield 3-week window (KC#3 shape).

---

## OPEN ON MIDAS — top 3 live; **full register → `AGENTS/MIDAS/OPEN_ITEMS.md`** (not optional reading)

1. 🔴 **M1 has no live registered test.** The successor must register the beta, and WQ-161/162 canon now governs its letter.
2. 🔴 **Silver/PGM bands: Will's ruling** (draft filed 9/25). **PGM mechanism (n=3) still blocked** on three absent instruments; HAWK has been asked 5×, and an explicit "no access here" would close it.
3. 🟠 **9/30: MIDAS-01/02 on frozen letters, ALL BASES, STUCK-not-MISS** (OPEN_ITEMS 22) · I1 ambiguity (KB-113) needs dated COMEX/SHFE series this desk does not hold.

## BOTTOM LINE

**MIDAS 2026-09-25:** the Fed hiked on 9/16, officials say more is coming, and the inflation-adjusted 10-year yield reached **2.76%, its highest since November 2008**. That is the environment that crushed gold in 2022. **Gold has so far taken it for under 1% since 9/10.** Money kept flowing in (a record 4,189t in ETFs in August; China's central bank bought its most in nearly three years), and the test I set on 9/11 to catch exactly this has fired. My slower regression still says gold is tightly rate-bound, so I am reporting both results and resolving neither. **The damage this year is in the other precious metals:** every one peaked in the last week of January, and silver is **45%** off its high, palladium **38%**, platinum **37%**, against gold's **21%**. No MIDAS alarm could see any of it, because silver and the PGMs have no price bands. That is now a decision for Will, with a draft filed.
- **Gold** `GCZ26` **$4,298.00 [9/24]**, −2.48% since 9/10: a Fed hike and hawkish speakers, partly offset by ETF inflows and PBoC buying.
- **Silver** `SIZ26` **$64.00 [9/24]**, −1.43% since 9/10 (−6.77% since 9/9): the 9/10 liquidation and a firm dollar (DXY >100). Solar thrifting is the structural headwind. GSR 67.16.
- **Platinum** `PLV26` **$1,752.0 [9/24]**, −2.73% since 9/10 (−8.70% since 9/9), the weakest of the four; no dated supply event found; contract roll due.
- **Palladium** `PAZ26` **$1,282.1 [9/24]**, −0.97% since 9/10: UBS raised targets on falling Russian/SA mine supply, and there is no US tariff on Russian metal.
