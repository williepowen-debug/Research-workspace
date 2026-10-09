# RED hypothesis-weight re-derivation — S51, Fri 2026-10-09 (owed since S50 "after Fri 10/2 NFP, by 10/09")

**Written:** 2026-10-09 (`date` at session start 10:25 EDT). PROME spawn prome-75 (Tier 1, Will's word 10:24 ET). **Every figure is RED's own pull on 10/09** through `FORGE/tools/market-data/fetch.py` (FRED, plus yfinance prices) or the Cleveland Fed `nowcast_month.json` (stamp 2026-10-09 00:00). Inputs: `reports/2026-10-01_S50_countersignals_repull.md` (row weights), LABOR's 10/2 packet (verified at the FRED primary below), and the pre-committed NFP bands on `docket/CATALYSTS.tsv` row 2026-10-02.

**Result: net-bear 58 → 60 (+2, both DISCRETIONARY and labelled). Confidence 70 unchanged** (no registered CONF leg fired). **No mechanical move:** no registered trigger fired between 10/01 and 10/09 (FT-02 0 of 3, below).

---

## 1. Tape, 10/01 → 10/09 (what moved while RED was dark)

| Row | 10/01 repull [obs] | 10/09 pull [obs] | Δ | Reads |
|---|---|---|---|---|
| 10Y real (DFII10) | 2.93 [9/30] | **2.92 [10/7]** (range 2.88–2.95 over 6 obs) | −1bp | the +51bp move **held** for 7 sessions; plateau, not a spike |
| 30Y (DGS30) | 5.64 [9/30] | **5.67 [10/7]** | +3bp | same |
| HY OAS | 312 [9/30] | **315 [10/8]** (one print 324 [10/1]) | +3 | FT-02 0 of 3 (§3) |
| BB / B / CCC | 194 / 316 / 1,179 | **194 / 315 / 1,252** [10/8] | 0 / −1 / **+73** | the widening since 9/30 is **CCC only**; BB and B flat |
| IG (BAMLC0A0CM) | 84 [9/30] | **82** [10/8] | −2 | IG tightening while CCC widens |
| KRE / WAL / OZK | 69.44 / 75.10 / 45.96 [9/30] | **69.17 / 74.04 / 44.55** [10/9 intraday] | −0.4% / −1.4% / −3.1% | drift lower, no break |
| Dated Brent (DCOILBRENTEU) | 113.96 [9/29] | **135.51 [10/2] · 125.51 [10/5] · 125.44 [10/6]** | +$11–21 | physical premium over paper now **~$21** |
| Brent paper (BZ=F) | 102.46 [10/1 intraday] | **104.00** [10/9 intraday] | +1.5% | paper did not follow physical |
| OVX | 52.24 [9/30] | **48.40** [10/8] | −3.8 | |
| 5y5y (T5YIFR) | 2.36 [10/1] | **2.33** [10/8] | −3bp | anchored |
| VIX (VIXCLS) | 16.39 [10/1] | **15.41** [10/8] | −1.0 | FT-06 still banked |
| ^SKEW (CBOE) | 141.92 [9/30] | **149.19** [10/8 bar] | +7.3 | FT-10 0-of-4; 0.81 below the line |
| Initial claims | 197K [9/26] | **197K** [w/e 10/3] | = | |
| USD/JPY | 158.05 | **158.34** | | WL-07 1.66 away |

**Labour, at the primary (FRED, 10/2 vintage) — LABOR's packet reproduces exactly:** PAYEMS Sep 159,044 · Aug 159,015 · Jul 158,882 · Jun 158,892 ⇒ **Sep +29K · Aug +133K (was +162K) · Jul −10K (was +21K)**; 3-mo avg **+50.67K** (BLS rounds 51K). CPS: U-3 **4.1 → 4.2**, LFPR **61.6 → 61.8** (labour force +485K per LABOR/BLS). AHE (CES0500000003) **$37.81**: 3-mo annualized **2.36%** (was 2.80% at S41), YoY **3.02%**. Two witnesses (CES, CPS), counted as two, never more (ML-186).

**Prior for 10/14 unchanged:** Cleveland nowcast Sept core CPI **+0.20%**, headline **+0.53%** (stamp 10/09; the value has not moved since 10/01, so it is not a fresh witness). CPILFESL Jun/Jul/Aug levels 336.065 / 336.789 / 337.765 are unrevised. The S50 tree stands (§5).

## 2. The pre-committed NFP band (written 10/01, before the data) — graded on its letter

| Branch | Letter | Result |
|---|---|---|
| **Bear** (Soft-Landing growth leg failing again; the S41 re-mark is re-litigated) | 3-mo < +50K **OR** U-3 ≥ 4.3 **OR** LFPR up with U-3 up | **MET on the third disjunct**: LFPR +0.2 with U-3 +0.1. (The first disjunct missed by 0.67K: 50.67 vs <50. U-3 4.2 < 4.3.) |
| Bull (the S41 soft-landing shape holds) | 3-mo ≥ +100K AND U-3 ≤ 4.1 AND AHE 3-mo ≤ 3.0 | NOT met (3-mo 51K, U-3 4.2) |

⚠️ **The band registered a DIRECTION and no MAGNITUDE.** That is the S29 defect (ML-144/151) in a new place: the letter forced a re-litigation of the Soft bucket but did not say by how much. The magnitude below is discretionary and labelled as such.

## 3. FT-02 (HY OAS >320, sustain 3) — the count RED keeps

**Basis:** registry `instrument_basis`: FRED BAMLH0A0HYM2, percent ×100 = bps, **the FRED observation date governs the sustain count**. The registry row does not pin a vintage. RED's practice is the value as pulled (latest-revised at pull). **Today both bases agree cell for cell:** `fetch.py fred BAMLH0A0HYM2 --first-published` (output_type 4, realtime from 2026-08-12) returns the identical values with `short=false, missing=[]`. FRED stamps each cell's first release on its own observation date, so the "~T+1" publication lag is not visible in the vintage stamp.

| Obs date | bps (first-published = latest-revised) | >320? | run |
|---|:-:|:-:|:-:|
| 9/30 | 312 | no | 0 |
| **10/1** | **324** | **YES** | **1** |
| 10/2 | 310 | no | **reset → 0** |
| 10/5 | 312 | no | 0 |
| 10/6 | 303 | no | 0 |
| 10/7 | 309 | no | 0 |
| 10/8 | 315 | no | 0 |

**Grade: 0 of 3 at the 10/8 observation; NOT FIRED.** The run reached its maximum of **1 of 3** on 10/1 (WALTER SIG-W-20261002-005 graded the same 1 of 3), and 10/2 reset it. 5bp away. The HEARTBEAT sequence 324 → 310 → 312 → 303 → 309 → 315 matches. Composition 9/30 → 10/8: BB 0 · B −1 · **CCC +73** · IG −2. The index is not walking toward 320 on breadth. The CCC tail is doing all of it. REGINALD's REG-T-03 is a separate count and is not merged here. RED grades and does not size.

## 4. The re-derivation

**Count once (S50 independence check):** rates, banks and part of HY share ONE antecedent, the 9/22→9/30 long-end sell-off. That gets ONE move. Physical oil is a separate antecedent. Labour is a third.

| Hypothesis | S29/S41 | **S51** | Δ | Label | Evidence named |
|---|:-:|:-:|:-:|---|---|
| Managed Decline / Muddle | 32 | **31** | −1 | (net of the three below) | receives Soft's −1; funds Acute +1 and War +1 |
| Full Stagflation Spiral | 32 | **32** | = | **held on purpose** | Two inputs pull opposite ways: wages decelerated again (AHE 3-mo 2.80 → **2.36%**) while physical oil spiked. **The registered test is 5 days out (FT-08 / CHG-028, 10/14 + 11/10).** Moving Stag now would pre-empt its own falsifier. |
| Acute Financial Dislocation | 13 | **14** | **+1** | **DISCRETIONARY** | **The real-rate leg, counted ONCE for rates + banks + HY:** DFII10 +51bp in 4 weeks (2.42 [9/3] → 2.93 [9/30]) and it **held** 2.88–2.95 for 7 sessions. KRE −7.6% · WAL −8.6% · OZK −11.2% since 9/3 (74.87 / 81.00 / 50.17 → 69.17 / 74.04 / 44.55). No registered trigger covers a real-rate LEVEL (FT-11 is a 30Y rally attribution). ⚠️ This is **not the credit leg**: FT-02 (HY >320 s=3) keeps its own +3, and this +1 is not netted against it or used to pre-empt it. If FT-02 fires, both stand. They are different evidence (rate level vs credit sustain). |
| War Escalation | 13 | **14** | **+1** | **DISCRETIONARY** | The Hormuz workaround became a target: **Yanbu port struck 10/1** (WALTER SIG-W-20261002-014/-016, terminal-wide suspension on the stronger source) and **a new Hormuz tanker hit on 10/2** (SIG-W-20261002-018). NYT (secondary) reports 13 ships struck since 9/10. **Dated Brent 114.82 → 135.51 [10/1→10/2], holding 125 [10/5–6].** ⚠️ **Counter-witnesses, both against:** paper Brent ~$104 (flat; FT-03 >130 on PAPER is 26 away) and OVX 52 → 48. The registered object (paper) did not move. This +1 rests on the physical market and the event record, which is why it is +1 and not more. |
| Soft Landing | 6 | **5** | **−1** | **DISCRETIONARY inside a pre-committed band** | The 10/2 band's bear branch was MET (LFPR up with U-3 up). The S41 +2 rested on "+71K 3-mo, growth slow but not failing". At the issuer that is now +51K, with Jul+Aug revised −60K and U-3 4.2. Half the S41 +2 is given back. **Not all of it:** claims are 197K, the bull kill did not fire, and inflation (the other leg) is unchanged. |
| Policy Rescue | 4 | **4** | = | held | The Fed hiked 9/16. Futures price ~25bp more by year-end, down from ~39bp on 9/28 (WALTER SIG-W-20261002-032, secondary). Nothing points to rescue. |

**Sum 100 · net-bear (Stag + Acute + War) 58 → 60 · Managed + Rescue 35 · Soft 5.** Bounds hold (none <2, none >60). **Confidence 70 (=).**

**Symmetry test (what would have moved it the other way):** if the real rate had retraced to ≤2.6 by 10/9, if paper Brent had followed Dated above $120, or if the 3-mo payroll average had been ≥100K, the same rule would have moved Acute −1, War +2 or Soft +1 respectively. **What the bull won this week, honestly:** 5y5y down to 2.33, VIX 15.4, OVX −4, IG tighter, BB and B flat, and claims 197K. The equity-vol and inflation-expectations complex is not transmitting the shock. That keeps this +2, not +4.

## 5. The 10/14 CPI tree (S50c) — CONFIRMED, STANDS

`research/2026-10-14_SEPT_CPI_DECISION_TREE.md`: inputs unrevised (CPILFESL Jun/Jul/Aug as written), nowcast unchanged (+0.20 core), basis ruling unchanged (Table A governs). As its own ⚠️ line pre-registered, **the +3 applies to the re-derived weights with the offset buckets unchanged:** on a fire, Stag 32 → 35, Managed 31 → 29, Soft 5 → 4, so **net-bear 60 → 63** (the tree's "→ 61" was written on the 58 base). No other change.

## 6. Bull steelman (re-steelmanned, same pass)

1. **Nothing priced in vol, inflation expectations or IG is transmitting.** 5y5y 2.33, VIX 15.4, IG 82: the real-rate shock and the oil shock both reached markets that are discounting them as temporary.
2. **The credit widening is a CCC story again.** BB and B were flat from 9/30 to 10/8 while CCC rose +73. KB-081 puts CCC at about 13% of the index flow. The same composition read RED applied in March (cable/media/healthcare, not systemic) is live.
3. **Physical oil is screaming and paper is not following.** That is the CHG-042 split, and twice now paper has been right about where the price settles.
4. **The labour market is cooling without breaking.** Claims sit at 197K, wages are decelerating, and the labour force is growing. A 51K 3-mo average with rising participation is a supply-side soft patch, not a layoff cycle.
**What the steelman cannot answer:** the real rate held +50bp for seven sessions with nothing to retrace it, and the Hormuz workaround is now being hit.

## 7. What this does NOT do
No threshold, sustain rule or registry letter changed. The recession number (4–12%, 9/6) is carried, not re-derived. No trade view. $0.
