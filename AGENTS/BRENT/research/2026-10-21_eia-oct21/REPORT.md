# BRENT — October 21 catch-up: EIA week October 16, BRT-31 week 2, Hormuz flow basis, tape and mail

**Session:** 2026-10-21 21:11–21:4x ET (Will: "boot up and catch up on all new/recent news and data"). Research and record only: no threshold re-levelled, no gate armed, no position or capital authority changed. `$0` moved.

## 1. Five consequential findings (LESSONS #4)

| # | Finding | Basis |
|---|---|---|
| 1 | **US gasoline demand is not weakening: four-week product supplied +1.4616% YoY (8,712.0 vs 8,586.5 kb/d); the week alone printed 8,982 kb/d.** BRT-31 week two is NON-QUALIFYING (needs ≤ −1.5%); streak 0. | EIA psw01 `WGFUPUS2`, release-day capture [CONF EIA 10/21] |
| 2 | **Crude tightness continues: commercial crude −3.061 M bbl to 412.517 M (3% below five-year), gasoline −2.952 M, total commercial −8.454 M.** Distillate +1.674 M to 104.286 M, still 9% below five-year. Cushing +0.987 M to 27.594 M. SPR −0.300 M to 282.683 M. | EIA Table 1/4, week ending 10/16 [CONF EIA 10/21] |
| 3 | **US crude production printed 13,269 kb/d, −410 kb/d w/w (Lower 48 −457).** Crude exports fell 1,128 kb/d to 3,442 kb/d; refinery input 16,649 kb/d, 93.4% utilisation. One weekly estimate; the four-week average is 13,721 kb/d. Do not read one weekly production print as a trend. | EIA Table 9 [CONF EIA 10/21] |
| 4 | **Hormuz flow figures disagree because they measure different things.** PortWatch counts AIS-visible ships; Kpler and the IEA estimate barrels and identify dark tankers by satellite. The AIS-visible tanker capacity PortWatch saw for 10/12–10/18 is under 1% of the barrels Kpler reports. The volume figures are the ones for the crude thesis. | §3 below |
| 5 | **Prices: Brent December (`BZZ26`) settled $108.82 (+$0.03) and WTI December (`CLZ26`) $97.15 (−$0.67) on 10/21.** Evening session 21:02 ET: `BZZ26` $110.44, `CLZ26` $98.37, after the Saudi Shaybah drone intercept. Brent touched $111.99 on 10/20 (five-month high), then settled $108.79. | §2 below |

**Boot reconciliation (step 2b).** The newest routine output is `demand_destruction/data/eia_2026-10-21.md` (autonomous, 11:1x ET). My first boot listing sorted it out of view; it was read before any STATUS write. Every week-10/16 figure above matches it exactly. The routine could not get retail gasoline (FRED scheduled maintenance); this session supplies it from EIA directly. Boot's FRED-DEAD findings have that same cause.

## 2. Market tape (named contracts)

| Item | Value | Class / source |
|---|---|---|
| Brent Dec `BZZ26` settle 10/21 | **$108.82 (+$0.03)** | [CONF secondary] The Nation 2026-10-22 ("settled nearly flat at US$108.82"); matches vendor 10/20 bar $108.79 + $0.03 |
| WTI Dec `CLZ26` settle 10/21 | **$97.15 (−$0.67)** | [CONF secondary] same article; matches vendor 10/20 `CLZ26` $97.82 − $0.67. Nov `CLX26` expired 10/20 at $101.79 (Discovery Alert) |
| Brent 10/20 intraday high / settle | $111.99 / $108.79 (−$0.76) | [CONF secondary] Discovery Alert 2026-10-21 |
| `BZZ26` / `BZF27` / `BZG27` evening | $110.44 / $106.49 / $102.39 | [CONF vendor live, 21:02 ET; evening-session bar, not a settle] `fetch.py` |
| `CLZ26` / `CLF27` evening | $98.37 / $96.61 | same |
| `HOZ26` / `RBZ26` evening | $4.63 / $3.07 per gal | same |
| USO | $159.80 (−0.50%) | vendor, 10/21 |
| Brent M1−M3 (`BZZ26`−`BZG27`) | 10/20 vendor bars **+$6.93**; 10/19 routine +$5.72; evening +$8.05 is diagnostic only (`BZG27` last traded 19:08 ET, `BZZ26` 21:02 ET) | Backwardated on every read, and wider than 10/19; TRACKER contango line not fired |
| WTI−Brent, December both legs | **−$11.67** at 10/21 settles | TRACKER line (> +$5) not breached |
| Diesel crack, `HOZ26`×42 − `CLZ26` | evening ≈ **$96.1/bbl**; 10/20 vendor bars ≈ $100.0 | Context only. HENRY's F1 basis is the 14:28–14:29 VWAP tier; this evening value is not that basis and grades nothing. It is within about $1 of HENRY's 95 line |
| Gasoline crack, `RBZ26`×42 − `CLZ26` | evening ≈ $30.6/bbl | Context only |
| US regular retail gasoline 10/19 | **$4.284/gal** vs $3.019 on 2025-10-20 (+41.9%) | [CONF EIA `EMM_EPMR_PTE_NUS_DPG`, pswrgvwall.xls] |

Vendor daily bars for 10/21 show evening-session volume (`BZZ26` 641), and `CLZ26`/`RBZ26` repeat identical 10/19–10/20 volumes. They are not settlements and are used only for the arithmetic checks above (LESSONS #5; `finding_a_daily_bar_read_after_the_evening_open_belongs_to_the_next_session`).

**Price drivers as reported (secondary, not graded):** Russia agreed to resume US-mediated talks with Ukraine (bearish); a larger-than-expected EIA crude draw; no US–Iran dialogue; continued tanker attacks; Houthi claims against Aramco sites on 10/19. The 10/20 pullback was attributed to Pakistan's army chief meeting Iran's president about mediation.

## 3. Hormuz flow instruments: basis settled (PROME packet 10/21, HAWK KB-446)

| Instrument | Figure | Basis at primary | What it can and cannot say |
|---|---|---|---|
| **IMF PortWatch** chokepoint6 (direct ArcGIS query, 21:16 ET) | 10/12–10/18 daily `n_total` 3, 7, 3, 2, 7, 0, 4 (26 ships in 7 days); `n_tanker` 0, 0, 0, 1, 1, 0, 2; **`capacity_tanker` total 87,683 t for the week** | AIS-derived ship transits. Saved: `portwatch-hormuz.json` | A **lower bound on AIS-visible transits**. Blind to AIS-dark hulls; the IRGC says the ships it hit had AIS off. Not a volume |
| **Kpler** (explainer, Kpler data as of 2026-09-29, author E. Belostrino; read at primary) | September: **≥16.5 mb/d** leaving the region excluding Iran (pre-war match); **~9.9 mb/d physically crossed Hormuz (60%)**, mostly on shuttle VLCCs; 23% loaded in the Gulf of Oman (Fujairah ~54%, Sohar ~45% of transfers); 17% via the Red Sea | **Crude + condensate only**; "minimum confirmed volumes", backfilled; STS counted even when one tanker is dark; crossings confirmed by Sentinel-1 radar, draught and destination checks | Barrel volume including dark traffic. Over 70% of August Hormuz crude changed tankers offshore; at least 63 VLCCs in the shuttle trade |
| **Kpler via WSJ** (secondary relay; WSJ not read) | Week through 10/18: **~14 mb/d = 82% of pre-war**, "including offshore transfers in the Gulf of Oman", **preliminary**; all Middle East routes **>24 mb/d vs 23.3 pre-war** | Basis wording includes Gulf of Oman offshore transfers, so it is wider than "crossed the strait" | Preliminary and relayed. Not the same basis as Kpler's September 9.9 crossing figure |
| **IEA OMR October** (FALCON relay of direct read) | September **total oil through Hormuz 10.9 mb/d** (+3.7 m/m); Gulf crude exports 13.9; bypass 5.6 | Total oil (crude + products) | Monthly; predates the 10/12–10/18 week |

**Verdict: PROME's hypothesis holds in part, and the main driver is AIS-darkness rather than bypass alone.** Bypass explains why regional exports (>24 mb/d) exceed Hormuz volume (~14 mb/d). It does not explain the gap between ~14 mb/d of Hormuz-basis volume and about four AIS-visible ships a day. PortWatch's own tanker-capacity field (87,683 t across the week, roughly 0.09 mb/d at about 7.3 bbl/t) is under 1% of Kpler's volume. Most crossing barrels therefore move on dark VLCC shuttles that PortWatch cannot see. Both figures can be true; they are not substitutes.

**One Hormuz figure for BRENT files:** **~14 mb/d, week through 10/18, 82% of pre-war (Kpler, preliminary, via WSJ; includes Gulf of Oman offshore transfers)** [EST secondary]. Anchors: Kpler September crossing-only ~9.9 mb/d crude + condensate [CONF primary], IEA September total oil 10.9 mb/d [CONF via FALCON]. **PortWatch stays a lower-bound transit count, never a volume or a falsifier.** The October-week Kpler primary was not read. If the 14 mb/d is revised, the conclusion that "most volume moves dark" survives, because PortWatch's tanker capacity is two orders of magnitude below any of the volume figures.

**What leans on it:** BRT-30 leans on **neither** figure; it resolves on the JWC listing (below). The WAIT judgment leans on the **volume** basis and on "net loss after the latest attacks is unmeasured". The volume read is consistent with HAWK's and FALCON's route-loss reading. Volume back near pre-war while Brent holds above $108 points to freight, insurance and inventory scarcity rather than lost crossing barrels. This is the October 14 product-scarcity line, not a new thesis version. The 10/11 Kpler daily dip (~2.9 M bbl, Al Jazeera relay) and the WSJ week average are different windows; daily volatility is high.

## 4. War-risk listing (BRT-30, resolves 10/26)

IUA JWC risk-list index read 21:16 ET (`jwc-iua.html`, HTTP 200): **newest circular is JWLA-035 Black Sea; no JWLA-036 or later.** No circular has removed the Persian/Arabian Gulf or the Gulf of Oman. BRT-30 is still OPEN and is graded only on 10/26. JMIC holds Hormuz at SEVERE (10/18 advisory) and raised the wider Gulf to SUBSTANTIAL (gCaptain 10/21). This is an index-number read only; JWLA-035's area text was read 2026-09-18 and was not re-opened.

## 5. BRT-31 (gasoline demand) — data week October 16, release October 21

| Field | Value |
|---|---|
| Current rows (10/16, 10/9, 10/2, 9/25) | 8982, 8408, 8769, 8689 kb/d |
| Base rows (364 days earlier: 10/17, 10/10, 10/3, 9/26/2025) | 8454, 8455, 8919, 8518 kb/d |
| Exact four-week YoY | **+1.461596692482385%** (summary rounds +1.5%) |
| Qualifying (≤ −1.5%)? | **No.** Streak 0 |
| Price check (Monday after data week) | 10/19 $4.284 vs 2025-10-20 $3.019 = **+41.90%**; below-20% counter **0 of 3** |
| Revisions to prior-week inputs | None against the 10/20 capture's workbook |
| Result | **OPEN, 40% unchanged, no terminal event.** Both window prints so far are > −1.0%, which keeps the NOT MET branch open at window end |

**Basis notes.** Release-day capture of ir.eia.gov current files, first-published values (the 10/15 week was reconstructed from archives; this one was not). The price check used EIA's own weekly retail series. That is the letter's named fallback for GASREGW; boot found FRED unreachable on both paths tonight, and GASREGW is FRED's copy of this same EIA survey. Contamination screening was not re-run: the closed list can only refuse NOT MET, and no terminal grade is possible this week. The bounded 50-state caveat from 10/20 still applies before any final NOT MET. Reproduce with `evaluate.py` (venv; writes `evaluation.json` with sha256 of every input).

## 6. Mail and news triaged this session

| Item | Disposition | Effect |
|---|---|---|
| WALTER -004 Russian diesel departures (Leruo → Manaus; Dolunay → Alanya) | acted | Diesel supply: departures, not deliveries. Read with -016 |
| WALTER -016 CORRECTION: Russia granted a partial 500 kt permission from 10/10, not a lift; producer restriction to 10/31, broader to 1/31/2027 | acted | BRENT live analytical files were grepped for "ban lifted" wording: STATUS, THESIS, NEXUS_BRIEF and TRACKER carry none; the docket's 9/1 row says "partial lift", which is consistent. The 10/31 docket row already frames the producer restriction as running to 10/31 |
| WALTER -017 Kremlin: first 40 kt diesel "in two to three days" (intent); talks mid-November | noted | Announced intent; not a flow |
| WALTER -007 Saudi MoE: Shaybah drone **intercepted** 10/21, debris killed two outside the perimeter, operations unaffected | acted | Supply relevance: **none measured.** No production or export loss on the ministry's wording. A risk-premium input only (the evening Brent bid). No INCIDENTS row: an intercept is not facility damage. FALCON grades the rung |
| WALTER -011 CORRECTION: MT ST 3 (IMO 9220964) struck 68 NM NE of Al Jubail, not in Hormuz | noted | No BRENT route or flow note counted ST 3 as a Hormuz casualty (grep clean). Nothing to re-place |
| WALTER -012 UKMTO 174–180 mapped (AL DASMA = one Bukha event; SOYIA off Al Faw) | info-only | Hull counts are FALCON's |
| WALTER -014 Southwest Q3: fuel $3.92/gal; Q4 assumed ~$4.55 off the 10/15 curve | info-only | An issuer's jet-fuel assumption ~16% above Q3; HENRY's resolution |
| WALTER -006 Dutch storage above a lowered target; EU gap −14.6 pp | info-only | HANS domain |
| PROME 10/21 Hormuz instruments | acted | §3; packet to HAWK, reply to PROME |
| PROME 10/20 consistency-pass go-ahead | acted | Completed 10/20 (SCRATCH 10/20 consistency repair, archive manifest); filed now |
| HENRY 10/19 December measurement | **deferred** | The adopt-or-reject decision is owner research; not started in this catch-up. Context: the evening diesel-crack value is near 95 (§2) |
| OSPREY 10/15 OSP-06 / L544 / pause lifted | **deferred** | The ask (confirm Bloomberg Russia 4-week exports to 10/11 at text) was not attempted; the article was a 403 for OSPREY |

**Not re-verified this session:** COT (next release Friday 10/23), Baker Hughes, JWLA-035 area text, the Kpler October primary, the WSJ article, TRADE positions or broker truth, the 25 aged INCIDENTS rows, and the HENRY December basis.

## 7. Addendum 21:2x ET — October-week volume read (PROME ask 4, prome-56 message)

**No primary gives an October-week Hormuz volume.** The Kpler October primary is not reachable; Bloomberg (10/21) is paywalled. All of these are secondary relays of Kpler, so they are one vendor lineage, not independent confirmations:

| Window | Figure | Basis as relayed | Relay |
|---|---|---|---|
| Day 10/8 | ~20.8 M bbl | "oil passed through the strait"; source attribution implied | Al Jazeera 10/14 |
| Day 10/11 | ~2.9 M bbl | same; pre-war average **17.1 mb/d** | Al Jazeera 10/14 (Kpler) |
| Week to 10/7 | ~8.5 mb/d (~40% below normal) | Kpler weekly crude | search summary only; not read |
| Week to 10/13 | ~11.6 mb/d (~68% of pre-war) | Kpler | global-energy-flow.com tracker; not read |
| Week to 10/18 | **~14 mb/d (82%)** | through the strait incl. Gulf of Oman offshore transfers, preliminary | WSJ via IBTimes / Seeking Alpha |
| Week to 10/18 | Gulf crude + condensate exports **24.6 mb/d** (a high); October-to-date still below pre-war | all routes | Bloomberg 10/21 headline/summary; body not read |
| Recent | 9–10 mb/d | Windward, a different vendor | relayed, not read |

**Cross-check:** 14 / 17.1 = 81.9%, so the WSJ 82% sits on Al Jazeera's 17.1 mb/d Kpler Hormuz pre-war baseline. The level and baseline are internally consistent. **Reading:** the 10/12–10/18 week did not deepen on volume. Relayed Kpler shows a recovery from a 10/11 trough (~8.5 → ~11.6 → ~14 mb/d), while PortWatch's AIS-visible count deepened in the same week. That divergence is what an AIS-dark shuttle trade predicts. Windward's 9–10 mb/d is a lower vendor estimate, and the vendor spread is wide. Treat ~14 mb/d as the upper end of a relayed range, not a measurement. The recorded figure in §3 stands with its [EST secondary] tag.

## 8. Kpler October check (Will 21:59 ET) — what the primaries say

**Kpler primary, newest reachable: "Hormuz: Normalisation no longer needs to wait for a deal", Matt Wright, 2026-10-01 (read at kpler.com).** No weekly or October-dated flow figure is in the text; chart values are images.

| Kpler primary statement (10/1) | Basis as written |
|---|---|
| Crude exiting the Gulf (excl. Iran) plus West Coast Saudi and East Coast UAE "around pre-conflict levels of 18.5 Mbd" ("now around 100%") | Crude; Gulf exits plus bypass routes; Iran excluded; period unstated |
| **Clean products: 3 Mbd "earlier in September", 2.5 Mbd "in recent days", "around 50% below pre-war levels"**; "the key pressure point"; Gulf refinery runs and exports "have not normalised alongside crude" | Clean products, Mideast Gulf plus diverted routes |
| "Since early September, Qatar has re-commenced shipping cargoes through Hormuz on a dark basis, alongside sustained dark transits from the UAE" | Qualitative; confirms dark transits at primary |
| Base case: "slower, uneven normalisation under continued conflict"; full reopening "should not be expected in the next six months"; freight "elevated" and embedded in delivered crude | Outlook |

**The October-week Kpler figures remain secondary-only** (WSJ via IBTimes 10/21 13:31 ET; Bloomberg 10/21 summary): Hormuz ~14 mb/d (82%, preliminary, incl. Gulf of Oman offshore transfers); Persian Gulf crude + condensate 24.6 mb/d in the week to 10/18 (a high, vs 23.3 pre-war), October-to-date still below pre-war. VLCC Gulf→China freight ~$37.37/bbl (Kpler); war-risk insurance up to 10% of hull value vs <3% (Windward).

**Independent cross-check (non-Kpler, unverified tracker):** Lvision (pgcrudeflows.lvision.ae, an X trader account; read 10/21). It shows a 7-day average to 10/18 of **11.2 mb/d via Hormuz plus 3.5 mb/d from Fujairah/Omani ports = 14.7 mb/d** (relayed by D. Jensen, Substack 10/21; Lvision's own page is AIS + satellite). By its own methodology "some Suezmaxes / all Aframaxes and Panamaxes are not tracked", so it is a partial-fleet lower bound. **It roughly corroborates Kpler's ~14 mb/d on the Hormuz-plus-Gulf-of-Oman basis.** Jensen disputes the **24.6 regional** figure, citing very low Yanbu loadings on satellite to 10/17 (MerruX on X; no number). That dispute is unresolved and BRENT does not adopt either side. Ship counts disagree by an order of magnitude across counters: PortWatch 26 per week (AIS-visible); Kpler ~20 known completions over ten days; CENTCOM ~400 merchant ships in the prior week (relayed; not read at primary).

**Effect on BRENT's recorded figure:** unchanged. ~14 mb/d Hormuz basis (Kpler preliminary) [EST secondary], now with partial independent corroboration (Lvision 14.7, partial fleet). The regional 24.6 is **not** adopted. **New and material for the thesis:** Kpler's own primary puts clean products ~50% below pre-war while crude is ~100%. That is direct support at primary for v5.13's product-scarcity line (crude recovers, products lag), and it is the strongest reason Brent and the diesel margin stay high with crude back. It is not a version change. The figure is dated early October; current product volume is unmeasured.
