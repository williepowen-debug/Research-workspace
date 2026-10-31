# DIGEST R2 — 11 briefs (BRENT, YURI, ZHAO, OSPREY, FALCON, HAWK, WATT, AEOLUS, CORAL, MARCO, CYPHER)

**Reader:** fresh-context read-only digest reader (Opus), stamp from `date`: 2026-10-31 12:55 EDT. Every brief read whole. Baseline = NEXUS's last full read 2026-10-26 23:39 ET. **All 11 briefs have committed since that baseline** (base commits checked via `git rev-list --before`). Figures below are quoted from the briefs; anything taken from a commit message rather than a brief is marked **[off-brief]**.

## Pin check (`python3 scripts/brief_pin_check.py`, run 2026-10-31 ~12:54 ET) — all PASS (proves the pin, not the content)
```
✅ AEOLUS OK-SAME-COMMIT a3b12fbe6   ✅ BRENT OK-SAME-COMMIT 79ae046b4   ✅ CORAL OK-SAME-COMMIT 62700efd1
✅ CYPHER OK-PINNED 6438da23443b… = STATUS HEAD   ✅ FALCON OK-PINNED 87a5097a9 = STATUS HEAD
✅ HAWK OK-PINNED 37ec47127 = STATUS HEAD   ✅ MARCO OK-SAME-COMMIT 687a1f553   ✅ OSPREY OK-SAME-COMMIT fbd9ec51d
✅ WATT OK-PINNED 184810f96 = STATUS HEAD   ✅ YURI OK-SAME-COMMIT 40faf7537   ✅ ZHAO OK-SAME-COMMIT 2e1090a0d
```
Sizes (B): BRENT 21,670 · ZHAO 14,197 · MARCO 13,929 · YURI 12,655 · CORAL 11,782 · WATT 11,192 · OSPREY 9,566 · CYPHER 8,500 · FALCON 6,547 · AEOLUS 6,216 · HAWK 3,688 — all under the 32,550 B read cap; none over-cap. Order (amendment 12, CROSS-DOMAIN first): ZHAO and CORAL place VIEW/CALIBRATION (and ZHAO a P3 block) before CROSS-DOMAIN; OSPREY puts dated blocks first; not load-bearing (offsets far below 54,250 B).

---

## BRENT
- **HEADER:** "As of: October 29 closeout (13:5x ET) | STATUS commit: pending this closeout (prior `2341dcf0b`)"; pin check SAME-COMMIT 79ae046b4 (2026-10-29 13:57). Thesis v5.13.
- **VIEW:** Energy WAIT retained. Persistent product scarcity vs recovering crude; one week of December crack compression ($97.8 → $93.1) against record issuer margins and distillate stocks ~10% below five-year; "Not the official-compression falsifier."
- **MOVED since 10/26:**
  - Dec crack (HOZ26×42−CLZ26): 94.0224 (10/27, source 2), 93.0634 (10/28, source 3 ESTIMATE) — **below the $95 NOTICE line**; 10/22 99.4672, 10/26 97.1142. **10/29 intraday below the $90.16 held-VLO SELL line: 88.6034 at 11:09 ET; 91.1424 at 13:34 ET (vendor one-minute) — "not yet a settlement observation."** Settlement-window observation owed; TERRY decides any SELL; Will may supply CME settle (WQ-533 b).
  - Settles (wire EST): Brent Dec 113.88 → 115.32, WTI Dec 99.90 → 102.78 (10/27 → 10/28), 10/28 move "attributed mainly to the relayed WSJ post-midterm campaign report". Vendor curve 10/29: BZZ26 114.94, BZF27 110.83, BZZ27 88.16.
  - Refiner Q3 primaries: Valero $39.24/bbl, 2,972 kb/d, "no signs of demand destruction"; Phillips 66 $38.00/bbl, 98% util., record 41% distillate yield, US diesel demand about −1.5%.
  - EIA week 10/23: BRT-31 −0.6762% NON-QUALIFYING (OPEN 40%); retail gasoline $4.269 (+40.66% YoY; FRED GASREGW 10/26); distillate ~10% below five-year.
  - Access: Ras Tanura 10/27 = Houthi claim only; PGSA "legal action" vs all Sinokor vessels from 11/1 (about half of Hormuz supertanker transits, Lloyd's List 10/26); TD3C $1.29M/day week to ~10/23, −34% from 10/8 peak.
  - CME blocks this box's IP (HTTP 403, 10/28 23:49 ET). WQ-533 ruled 10/29 13:33 ET: Saudi resolver abandoned, no Saudi-relief grader; sources 2/3 crack basis. WQ-510 A routines installed 10/28.
  - 10/26 rows: Hormuz ~14 mb/d/82% relay "no longer an adjudicated single current Hormuz volume" (current flow UNRESOLVED).
  - **[off-brief, commits 785fb3d44/4f3936da7, 10/30 20:2xZ]:** COT #12 (as-of 10/27) JOINT NOT-SPENT 6th consecutive, shorts 126,305 (−921), OI-share 6.6960%; oil rigs 462 (+2), airlines clean. Brief still carries COT #11 (shorts 127,226; 6.93%, fifth).
- **CROSS-DOMAIN / CALIBRATION:** TERRY owns notice/sell grade; FALCON owns ladder/enforcement; Kpler 24.6 regional relay disputed. Three NOT-FIRED trade ideas at TERRY (back of curve; crude tankers into Sinokor 11/1; US gas on polar vortex). Uncertain: incremental delivered diesel, strike offsets, margin capture, source access. Conviction moderate; no quantified divergence from market.
- **FORWARD:** 10/30 COT #12 + BZZ26 last trade; 10/31 Russian producer diesel ban expiry; 11/1 OPEC+ seven (expected unchanged) + PGSA Sinokor; 11/2–6 TD3C/TD34 after Sinokor; ~11/3 Aramco Q3 (Jazan/Berri/SATORP); 11/4 EIA WPSR (BRT-31; needs two consecutive ≤ −1.5%); L783 sell-line window to 11/19, basis review by 11/18.
- **NEXUS-NAMED:** none addressed to NEXUS.
- **FLAGS:** Not stale by pin, but post-brief desk activity (COT #12) unfolded. "STATUS commit: pending" text inside a passing pin. Glued text in the 10/26 rows ("October26", "CLZ26 official103.27USD/bbl", "WTI>100 observed asof23", "Kpler24.6") — Output Canon defect. Forward row frames 10/31 as "ban expiry"; YURI 10/31 says the ban runs to 31.01.2027 and the 11/1 event was the producer exemption start (now deleted). BRENT has not consumed №1436 in-brief.

## YURI
- **HEADER:** "As of: 2026-10-31 ET (primary fetches 2026-10-31T13:27–13:30Z…) | STATUS commit: this brief and STATUS are committed together" (40faf7537, 10/31 09:40).
- **VIEW:** Score 2/5 unchanged. Two tracks: rapprochement with Washington alongside widening custody of Western assets; diesel regime is a ban to 31.01.2027 with the producer exemption now deleted.
- **MOVED since 10/26 (brief's prior commit was 10/21):**
  - **FIRE/GRADE: Resolution №1436 (31.10, in force 31.10; pravo 0001202610310001): №954 ¶2(г) producer diesel exemption DELETED, producer diesel exports banned to 31.01.2027 — YUR-005 HIT, Brier 0.16.** ¶5 voided so ¶2(в) intergovernmental/EAEU diesel stays permitted to 31.01.2027. "US-quota channel still no public act." "Press 'year-end' frame wrong."
  - **YUR-004 final read 10/31:** no mobilisation declaration 02.10→30.10; MISS write owed at an 11/02 re-read.
  - **YUR-F01 MISS; Will kept the desk; YUR-F02 re-test to 11/28.** YUR-006 open to 11/15 (p=0.70).
- **CROSS-DOMAIN / CALIBRATION:** Delivered supply is BRENT's read. Ontex (≈5% revenue, 7–8% adj. EBITDA) and Sonoco verified exposures under №738 custody; not priced, PROME routes. Uncertain: how the 500 kt permission is administered; whether a №686 code list exists as a restricted act; unpublished decree numbers.
- **FORWARD:** 11/02 YUR-004 MISS write (re-read incl. late publications); mid-Nov RU–US–UA talks ("in principle", Ushakov 21.10); 11/15 YUR-006 grade; 11/28 YUR-F02.
- **NEXUS-NAMED:** none.
- **FLAGS — internal contradictions (body not refreshed to the 10/31 header):** WAITING FOR still lists the №954 amendment as pending "Signed ≤31.10, published ≤02.11" and DAEDALUS YUR-F01 grade "10/24"; CALIBRATION still "YUR-005 p=0.60"; NEXT DECISION POINT still 10/23–10/24; WATCH still lists 10/23–11/02 items as future; SENDING row (10/21) and VIEW say "¶2(в) EAEU exemption also ends 31.10" vs the header's "runs to 31.01.2027". The Status line governs.

## ZHAO
- **HEADER:** "As of: 2026-10-29 14:36 ET (by `date`), closeout" with a self-correction that earlier ~14:45–15:20 stamps ran ahead of the clock; SAME-COMMIT 2e1090a0d.
- **VIEW:** 🟠 28/60 ELEVATED (unchanged since 10/9). The November window is the live question: two export-control clocks restart 11/10 with no extension instrument. China UST selling continues but decelerating; PBOC is holding the yuan BACK; HK dollar at the 7.85 weak edge.
- **MOVED since 10/26 (prior brief 10/22):**
  - **New letters (10/29):** ZHA-19 US clock instrumented by 11/9 **65%**; ZHA-20 MOFCOM by 11/10 **70%** (correlated, "~1.3 calls, not 2"); ZHA-21 NPCSC RMB fiscal figure **12%**. **ZHA-05 STUCK** (anchor was a segment NPL). Belgium kill-leg retired (rho +0.067, n=43); kill-lines re-specified (F China 6-mo TIC ≥ +$2B ×2, now −$71.5B; L >$700B ×3, now $590.7B; S fiscal >5% GDP).
  - PBOC fix-vs-market: −0.89% avg 2024 vs +0.46% in 2026, record +0.90% on 9/17 (925 CFETS fixings); fix +0.52% weaker than market (SENDING). Stress total 28/60, two-sided shadow 31.
  - HK: USD/HKD 7.846; HIBOR-SOFR −122.5bp (GREEN→YELLOW); Aggregate Balance HK$53,999M, no HKMA intervention.
  - TIC: Aug LT −$4.8B; LT −15.8/−7.7/−4.8B; Aug −$12.25B non-transaction residual, cause UNKNOWN. Q3 China+Korea −$21.6B through Aug.
  - Vector 8: TTF €100.72, Qatar FM; rescore 4→5 open. Rural-bank NPL 2.83% rising = new Vector 4 instrument. V6 on Fed H.10 market leg +0.56%.
  - China data: exports +36.3% (Sep), PPI +5.0% (energy-led), CGB 1.63%, construction new orders 45.7.
- **CROSS-DOMAIN / CALIBRATION:** 🔴 to VULCAN·WATT·HAWK: "export-perimeter widening on 11/10 by default"; 公告58 battery leg keys on the MOFCOM instrument. LIQUID: peg-defence drain. HENRY: risk-off read must not lean on the yuan. MIDAS: PBOC gold ≈23 t Sep. Uncertain: whether either clock gets an instrument; Aug residual cause; whether HK carry forces HKMA in; leg F untested in a regime change. RED BENIGN-DRIFT counter-frame "strengthened again".
- **FORWARD:** Sat 10/31 NBS PMI (construction <47.5 ⇒ V5 re-raise; mfg <50 ⇒ ORANGE); Mon 11/2 instrument re-check (BIS/MOFCOM/USTR final) + RatingDog PMI; 11/2–6 NPCSC (ZHA-21); Sat 11/7 SAFE reserves/gold; **Mon 11/9 USTR s.301 ships suspension ends + BIS stay last day (ZHA-19); Tue 11/10 BIS Affiliates Rule reimposed + MOFCOM 公告70 expires (ZHA-20)**; Wed 11/18 Sep TIC (China Q3 ≤ −$50B ⇒ LIQUID+PROME); 11/27 MOFCOM 46号 clause 2.
- **NEXUS-NAMED (verbatim):** "**★ 10/29 — FOR NEXUS: the PBOC's currency posture has fully reversed, and the desk's gauges could not see it until today.**" and "**🟠 10/9 — FOR NEXUS: a pre-registered tripwire fired and I applied it AGAINST my own read.**"
- **FLAGS:** Not stale. Self-disclosed clock-ahead stamps. ⚠️ "ONE UNPRICED BINARY (VULCAN/HAWK): a BIS Entity-List package naming CXMT / YMTC / SMIC subsidiaries is reportedly prepared but unpublished since June 2026. Re-checked 11/2." Carried un-run copper −41% decomposition (it is June crude imports).

## OSPREY
- **HEADER:** "As of: 2026-10-29 ~14:42 ET (from `date`; osprey-5e closeout…) | STATUS commit: see `git log -1 -- AGENTS/OSPREY/STATUS.md`" → SAME-COMMIT fbd9ec51d.
- **VIEW:** Scores 5/5/3 unchanged; refining band ~30%, 25–35% [EST] (runs proxy). C1 quiet since 10/16 = political brake (US pressure; Starlink leverage reported), "not an exhausted target set"; resumption one decision away.
- **MOVED since 10/26 (prior brief 10/23):**
  - No Ukrainian refinery strike found 10/16→10/29 (KB-224); last oil hits Ryazan 10/15, Surgut 10/16; targets moved to steel/chemical (Yakovlevo 10/26, NLMK 10/28, Perm 10/23+10/25). Zelensky: no order to refrain, tempo "slowed sharply". C1 leg A 14/14, leg B not met ⇒ C1 stays 5.
  - Exports (BRENT's figure): Bloomberg 3.59 M bpd 4-wk to 10/18; weekly 3.13, lowest since March; Primorsk ~3-day pause, cause NOT established.
  - C3: 10/27 passed, no kill (limb 2 NOT SATISFIED); KHORYV sunk off Constanta 10/23 (Russia-attributed), Shabla ~10/28 — neither qualifies.
  - **New letter OSP-07 OPEN (10/29, 60%): a Ukrainian strike on a Russian crude refinery dated 10/30–11/15, graded on/after 11/18.**
  - OWED-46 RULED by Will (condensate plants count only if motor fuel + identity confirmed, KB-243); WQ-470 X bound at +92% and the joint draft breaks (KB-238). Graham Act EO 14436 (10/16): 100% tariffs on top-5 Russian-crude importers from 10/18, waived in the same order (KB-234). Spring pump-station campaign +21 historical rows (KB-237). Druzhba: no interruption after Tambov 10/20.
- **CROSS-DOMAIN / CALIBRATION:** Prices are BRENT's. Counter-signal: "Russian diesel exports to the US (KB-229) are a demand-side sign of product recovery." Conviction: products-impairment direction high; lost-volume level low; lull duration low.
- **FORWARD:** 11/1 diesel ban (extension vs lapse — a lapse starts the C1 companion-tell 30-day clock); 11/2 DOCKET L814 C1 grade + capacity-offline blackout flag (day 60); 11/8 §5 EXIT re-read; 11/17 earliest C2 re-kill (Bloomberg ≥3.9 twice ⇒ C2 5→4; <3.5 blocks); 11/18 GATE-OSPREY-001 + OSP-07 grade.
- **NEXUS-NAMED:** none.
- **FLAGS:** "STATUS commit: see git log" is a pointer not a hash (pin passes). Internal: STATUS line says "WQ-470 joint draft with HAWK, not yet adoptable" and the As-of says X bound at +92% "the joint draft breaks"; SENDING still reads "OSPREY owes the 12-week TD6/TD19 backfill to bind X" while HAWK carries "X provisional +25%". Diesel "producer ban runs to 10/31" — superseded by YURI №1436 (ban to 31.01.2027). Coverage: ledger certified only through 10/25.

## FALCON
- **HEADER:** "As of: 2026-10-30 16:50 EDT | STATUS commit: `87a5097a9` | Evidence cutoff ~16:49 EDT"; pin OK.
- **VIEW:** 🔴 B 1 / C 14 / D 85 HELD; "No registered trigger met in the week; the marks are held, not re-earned." Sinokor declaration = first fleet-wide Iranian action; weight on tanker supply, not the Hormuz count (already at the floor). US posture building to a post-midterm window.
- **MOVED since 10/26:**
  - Khasab 10/29: dhow MSV QUBA sank ~9 NM N of Khasab after a "security incident" fire; **confirmed losses 5 → 6, class(i) 1 → 2**; no rung/mark change.
  - **10/29 hull attacks: LOUISE 1 (Panama Suezmax), two devices above waterline ~25 NM NE Khasab, fire, continued voyage (UKMTO 187-26); RITI (oil tanker, 166k dwt) fire, anchored ~1 NM NW Ra's Tahir, 25 crew evacuated (NAVAREA IX 420/26). Both UNATTRIBUTED. "First successful limpet-type attack of the war."** RITI total loss ⇒ first (iii-A) + EXIT rewrite trigger, no mark move.
  - Qeshm launcher "US strike" 10/29–30 rests on one anonymous CENTCOM official; Iran says jet intercepted ⇒ **FAL-07 NOT FIRED.**
  - "Ras Tanura distillation shutdown per Bloomberg" NOT ESTABLISHED; Houthi 10/29 Abqaiq claim uncorroborated; production rung ARMED, not fired. Own FIRMS 10/27 heat inside routine flare range.
  - PGSA Sinokor legal action from 11/1; ≥7 already actioned; Reuters ~40% of Sept Hormuz crude outflow; Hormuz ~1 tanker/day (PortWatch to 10/25); PortWatch 10/19–25 = 23 total / 6 tankers.
  - Qatar LNG force majeure extended to end-December. NAVCENT/JMIC 10/28 stay-clear, blockade enforcement, visit-and-search. Egypt parliament authorised support for Saudi defence 10/26 (fifth-axis WATCH); third US carrier group reported; Fujairah 77,581 t/d = 90% of base; Sohar series dropped (bypass gauge DEGRADED).
  - GATE-FALCON-001 reviewed 10/29: LIVE, leg 2 NOT MET (lowest ratio 80.0% vs ≤65%).
- **CROSS-DOMAIN / CALIBRATION:** VLCC/freight read is BRENT's; SAM gets Japan LNG. FAL-06 OPEN 70% (11/5 search); FAL-07 OPEN 65% (clock to 12/31). "Convergence 43/50, saturated composite." Not covered 10/29: Iraq/PMF (CTP/ISW), cyber/cable.
- **FORWARD:** 11/1 Sinokor; 11/3 US midterms (FAL-07 window opens after); 11/4 scenario + GATE-FALCON-001; 11/5 FAL-06; 2027-01-02 FAL-07 failure search.
- **NEXUS-NAMED:** none.
- **FLAGS:** Not stale (pin = STATUS HEAD). Post-brief DAEDALUS profile-refresh packet (3ff658e00, 10/30 17:53) unread in-brief.

## HAWK
- **HEADER:** "As of: October 29, 2026, 13:3x EDT (second pass); owner evidence FALCON `800ccec25` (~12:55 Oct 29), OSPREY `e8f1acaf3`"; "STATUS commit: `37ec47127`" — pin OK.
- **VIEW:** ELEVATED. Willingness/route risk rising on the ENFORCEMENT channel; net crude loss and the premium's share of the oil price UNMEASURED. No mark, band or probability moved.
- **MOVED since 10/26 (prior brief 10/25):** census 6 confirmed losses (Cape Dao; MSV QUBA); OSPREY no strike since 10/16; Sinokor legal action from 11/1 ("~47% of Hormuz VLCC transits is secondary only"); NAVCENT stay-clear 10/28; war-risk: "no matched October quote in any leg … all five legs stale; Bab CANNOT-FIRE". USTR proposes keeping China-ship port fees suspended to 2027-01-09 (proposal, not final). Canada auto-related lines added/removed eff. 10/30. **WQ-521 RULED A 10/29 12:37 ET:** TRADE-02 RED defined; first grade NOT SATISFIED, ORANGE held. **EURMIL:** Croatia's compulsory service met RED trigger (b) as worded; Will RULED B 10/29 13:51 ET (prospective clarification) — EURMIL ORANGE held. FLOW-21 not falsified (Q3 TCE moved away from index; DHT spot $509,100/day on ~50% of Q4 days). Helium: one named fab (Polar) on supplier allocation.
- **CROSS-DOMAIN / CALIBRATION:** Russia refining vs Gulf hull/route "stay separate; no pooled barrels or premium fraction". WQ-470 X "provisional +25%". HAW-20 OPEN 65% (graded Oct 31); HAW-22 OPEN 65% UNCALIBRATED (window closes Oct 31, no candidate Oct 25–29; resolution Dec 22) — "a CONFIRM on this letter is a claim about what was DISCLOSED, never about capacity".
- **FORWARD:** Oct 31 HAW-20/HAW-22/YURI; Nov 1 Sinokor; Nov 2 EURMIL backstop; Nov 5/9 INSW/DHT results; Nov 10 trade clocks.
- **NEXUS-NAMED:** none.
- **FLAGS:** Brief predates FALCON's 10/30 LOUISE 1/RITI limpet attacks, Qeshm claim and Qatar FM extension, and YURI's №1436 — HAWK's synthesis is a day+ behind its owners. HAW-20 10/31 grade not yet in brief. WQ-470 X: HAWK "+25% provisional" vs OSPREY "bound at +92%, the joint draft breaks".

## WATT
- **HEADER:** "As of: DM2 5-min tape October 23 00:00 to October 29 13:25 EPT …; P2/P3 as read October 20. STATUS commit 184810f96." Pin OK (brief a4b0287af 14:21, after STATUS 14:20).
- **VIEW:** P1/P2/P3/P4 = 5/5/4/2; composite 16/20 (was 14/20). Historical auction shortfalls real; prospective shortage magnitude less certain (IMM mixes delay and cancellation).
- **MOVED since 10/26:**
  - **FIRE: P1 3→5 October 29 on the registered RED letter for the 10/27 18:50–19:00 EPT run:** $2,026.73 / $1,970.77 / $2,297.21 (unverified 5-min), demand 97.9–99.8% of trailing-24h peak; verified HB18 $719.87. KILL_MEMO C1 NOT fired; no emergency posting, no 202(c); retraced by 19:15. Outage-driven (69.5–72.7 GW forecast out, forced 12.9–13.4 GW), same root as 10/7 and 10/13 ("count once"). Found 2 days late (dark 10/24–28).
  - YoY tail worse (Sep 1–Oct 28 verified hourly): hours ≥$500 19 vs 1 (2025), ≥$1,000 7 vs 0; median $36.78 vs $34.79; at 90–100 GW ≥$200 rate 4.3% vs 0.7%; October forced outages 7.0→9.4→11.6 GW; demand +6.1 GW mean; firm capacity flat ~181 GW, all growth solar (12.6→19.3 GW), "zero at an autumn 19:00 peak". One baseline year only.
  - Daily max 10/23–29: $748.30 / $436.76 / $399.74 / $1,340.04 / $2,297.21 / $306.10 / $81.18 (to 13:25). Gaps 10/24 and 10/27 could hide a RED run.
  - New letter WATT-13 (Nov 2026 forced outages > Nov 2025; resolves on/after 12/2). ISHM custody ACCEPT (Eaton/GE Vernova orders = P3 evidence). Next 2029/30 BRA = December 2026 (corrects mid-2027).
- **CROSS-DOMAIN / CALIBRATION:** To VULCAN/HENRY: IMM 4,016.9 MW cancelled OR delayed data-center projects (~42% of 9,481 MW forecast growth, as of 9/21) — "Demand-realization counterevidence, not 42% of all load". Google 890 MW uprates from 2028; Amazon 190 MW 2030–32 — no current relief. Weather vs load growth not separated (AEOLUS). Market divergence unmeasured. Evidence to TERRY NOT-FIRED, no trade.
- **FORWARD:** 11/4 P1 de-escalation grade (window 10/28–11/3; DST repeated hour); 11/5 PJM Special MC / RBP outcome; Nov 10–11 Beijing battery T1 boundary; 11/16 / 12/16 EL26-67; 12/2 WATT-13; December 2026 2029/30 BRA.
- **NEXUS-NAMED:** SENDING rows addressed "HENRY / AEOLUS / PROME / NEXUS" (P1 fire), "HENRY / AEOLUS / NEXUS / VULCAN" (YoY tail), "PROME / NEXUS / WALTER" (BRA December 2026); packet "NEXUS a862a30c4" (10/29).
- **FLAGS:** Not stale. Post-brief WALTER route (cc29537bc, 10/29 22:26) "conditional bulk-power equipment security order" to WATT/CYPHER — in neither brief.

## AEOLUS
- **HEADER:** "Last writeback: 2026-10-31 09:40 ET (PROME Tier-1 due-row wake, DOCKET L426, plus the WQ-562 encoding…)"; no hash in the brief; SAME-COMMIT a3b12fbe6.
- **VIEW:** Composite 16/30, fired 0/6, moved 1 since 10/21 (C5 5→4). C6 water improved, deal did not; Rhine exited the record-low run; coastal record water is not a band input. "Nothing here is a trade."
- **MOVED since 10/26 (prior brief 10/21):**
  - **C5 Rhine 5→4:** record-low run ended 10/22 (35 days); Kaub 54–57 cm, Duisburg 208–235 (10/26–28); Contargo surcharge €550 (was €1,075); falling again: Kaub 41.2 / Duisburg 204.8 [10/30]. **Re-keyed by Will 10/31 09:38 ET (WQ-562 "A") to Kaub ≤40 AND Duisburg ≤180 — NOT MET at encoding.** Base rate: old 25/153 trigger never met 2000–2025.
  - **C6:** Powell inflow 63,368 cfs 10/22; storage +537,840 af in 7 days; Powell 3,530.09; Mead 1,038.29 [10/27]. **AEO-10 (no breach in 2026) 30% → 50%.** LB agreement unexecuted; Arizona (10/16) and CAP (10/27) moved to intervene in *Nevada v. Burgum*; C6 held at 4.
  - Coastal: Lake Worth Pier 35.76 ft monthly-max record; Key West #3 since 1913; NWS MAJOR at 4 FL gauges 10/25–29 (FLOW-17).
  - C3: ECMWF forecasts polar-vortex reversal ~11/05 (all 50 ENS below zero 11/09); GEFS dissents; not observed (+14.1 m/s 10/29). Niño-3.4 weekly +3.4 (21OCT), record. C1: ACE 17.06% of normal; DR-4955-FL 10/27 (PA only).
- **CROSS-DOMAIN / CALIBRATION:** For CARL/HENRY: under the new Rhine line a C5 →5 is "~1-in-9-year". Roots separate: C5-Rhine (European basin) · ENSO cluster (C1/C2/C3/C5-Panama/C6) · coastal. Vortex informed WATT + BRENT. Read-cap: charter 48,606 B over budget (PROME L470 pending).
- **FORWARD:** ~11/01 Rhine re-entry (WSV estimate Kaub 25 cm); ~11/05 vortex; 11/02 Colorado band → YELLOW unless LB agreement executed + NIFC outlook; 11/05 PJM OC; 11/10 WASDE + CAP responses + MWD board; 11/12 CPC ENSO; ~11/15 November 24-Month Study (decides C6 leg 2 at 1,010 if deal executes); 11/26 SA CEC; 11/30 season end (AEO-01).
- **NEXUS-NAMED (verbatim heading + lines):** "WHAT NEXUS/PROME SHOULD KNOW — **The C6 conditional still stands:** execution of the Lower Basin deal moves leg 2 to the 1,010 line. Whether it fires then depends on the **November** study, since the October one is now stale." · "Root independence: C5-Rhine (European basin) · ENSO cluster (C1/C2/C3/C5-Panama/C6) · coastal (wind + sea level) are separate roots; Isaias is one event for C1 and C4."
- **FLAGS:** Not stale. No STATUS hash written in brief (pointer by commit only).

## CORAL
- **HEADER:** "As of: 2026-10-29 19:54 ET … STATUS commit: rides the same commit as this brief" → SAME-COMMIT 62700efd1.
- **VIEW:** 🟠 Split holds: household/condo stress confirmed; bank-loss transmission NOT confirmed (rail NOT met, NOT armed). "Most new data cuts AGAINST acute statewide housing distress; the one measured channel pointing WITH the thesis is bankruptcy."
- **MOVED since 10/26 (prior brief 10/21):**
  - Bankruptcy 12 mo to 9/30/26 (AOUSC F-2): 225.9/100k, +21.3% YoY; US 179.9, +11.5%; FL/US 1.256× (6/30 1.231×); 30 of 31 large counties rising, median +26.1%.
  - MSI-01 #11 (Parcl data date 10/27): Tampa 7.27 · Punta Gorda 6.27 · North Port 6.30 · Cape Coral 5.89 · Lakeland 6.27 ⇒ 4-of-5, re-fire fails.
  - DR-4955-FL declared 10/27: PA in all 15 counties, IA in none of 8, HM not designated. FHCF claims-paying $22.26B vs $17B (10/22). Citizens 9/30 254,836; 10/23 weekly 216,577 (−38,259 = 10/20 takeout round). FMHPI FL Jul revised +1.68% → +0.74%, Aug +1.08%. OIR Isaias claims 62,295 / $652.2M at 10/27 (above Sally's $577M at 40 d). REGINALD 10/28: every read Q3 8-K cell HOLDS.
  - "MIA clean tell" WITHDRAWN (MARCO correction applied).
- **CROSS-DOMAIN / CALIBRATION:** To NEXUS: localized stress (SW/Central-FL) not statewide. Conviction mechanism-HIGH, bank-transmission-LOW until Q3. RED counter-frame: Q3 banks cure + bankruptcy converges ⇒ real-estate story, not bank cascade.
- **FORWARD:** →11/03 DR-4955 cost share (L784); ~11/4–5 MSI #12; 11/3 Amendment 3 ballot (60%); ~11/14 Q3 FL-bank 10-Qs (≥2-of-4 TRANSMITS ⇒ rail MET); 11/15 falsify grade; 11/16 FL Realtors October; 12/11 NFIP authorization.
- **NEXUS-NAMED (verbatim):** "**NEXUS** | Geography read: statewide firming vs SW/Central-FL MSI at highs — the stress is localized, not statewide | 🟠 | Synthesis should not treat FL as uniformly improving or uniformly breaking"; and "**MARCO correction applied:** … | NEXUS — check your own demand premise".
- **FLAGS:** Not stale. Minor: SENDING row "MARCO | ✅ Reconcile CLOSED 10/10 … nothing open" while MARCO's brief still lists CORAL as carrying the superseded MIA clean-tell premise (MARCO's brief is stale on that point; CORAL applied it 10/29).

## MARCO
- **HEADER:** "As of: 2026-10-29 00:01 ET (session 38 CLOSED…) **STATUS commit:** folded in the same commit" → SAME-COMMIT 687a1f553.
- **VIEW:** 🟠 v3.2. FL demand remains unidentified; Channel 2 (Canadian travel) strongest transmitting channel; winter 2026–27 inbound risk is a hypothesis, not an observed collapse.
- **MOVED since 10/26 (prior brief 10/25):** **MIA-2-consecutive trigger MET 10/28** (airport-own Aug −5.69%, Sep −1.82%; 2-yr −5.85%; domestic −4.33% on seats +0.28%, LF 83.0→79.2%) — "threshold-MET / mechanism CONFOUNDED (Spirit, fares +22%)". **FL $600M–$1.2B formally retracted** on DEWEY DR-1 (no replacement). TX-01 ELEVATED; GTR-01 Sep −37.2% vs 2024 CRITICAL; Guatemala Sep +6.37%; CA FAIR Plan Sep. BEA Travel trailing-12 through Aug −$3.125B ELEVATED; LAS Canadian winter seats −33.22%, NV-01 CRITICAL.
- **CROSS-DOMAIN / CALIBRATION:** Sent REGINALD/CARL the MIA trigger; HAWK S338 cars unlisted; LABOR CPS controls. Divergence: consensus reads FL/tourism resilient; MARCO holds a winter 2026–27 risk hypothesis. Uncertain: LAS filings, January CPS control size, current FL migration, H-2A court state.
- **FORWARD:** ~11/4 LVCVA September (Aug+Sep RevPAR ≥0 ⇒ August decline was Labor Day artefact); 11/2–3 Banxico / CA farm / FL amendment vote; 11/10 October CPI airline fares; 11/12–13 H-2A / StatCan October; ~11/15 OFLC Q4.
- **NEXUS-NAMED (verbatim):** "NEXUS | Channel-1 re-instrumentation is a **measurement** change, not a direction change — and the s32 `SDL-01` flip is one print, not a reversal | 🟡 | Avoids reading either as a thesis reversal".
- **FLAGS:** Not stale by pin. Internal staleness: CALIBRATION and WAITING FOR still say CORAL carries the MIA clean-tell premise; CORAL withdrew it 10/29 (two CORAL→MARCO packets 10/29 post-date this brief). Glued text ("throughWALTER", "SAVED10/25", "nominalSA Travel actual trailing12months throughAugust shows−$3.125B") — Output Canon defect.

## CYPHER
- **HEADER:** "As of: 2026-10-30 11:0x EDT (spawned session, WQ-550 leg 1, DOCKET L878) | STATUS commit: `6438da2…`" pin OK.
- **VIEW:** 🟠 Wave: one trigger FIRED (CISA KEV, 10/26), no named financial victim. Off-wave: Binance theft (~$6.3B est. impact, ~$3B frozen); no bank or mapped supplier touched. Stablecoin issuers "worked as a kill switch".
- **MOVED since 10/26:**
  - Binance 10/29 (CYB-INC-055): own notice ~$6.3B est. impact, ~$3B frozen; withdrawals off 0 of 1,447 pairs (14:51Z 10/30); USDC $823.00M, USDT $1,350.46M frozen on-chain; TRM private DPRK attribution only. WQ-550 leg 1: no contagion to exchanges or banks; Wintermute (<20% of net equity), GSR (<5%) exposed. Equity clock: BTC −4.15%, QQQ −2.60%; COIN residual −5.7pp, earnings-confounded. Registered CHK-40 (issuer mint/freeze keys).
  - Palo Alto advisory (upd 10/29): "Active exploitation has been observed" on management interface, Critical since 10/27; Dream firewall chain claim (CYB-INC-047, VENDOR CLAIM). Node2Shell in KEV 10/27. CHK-32 perimeter-appliance = CONFIRMED wave touch. One US credit union ~24h precautionary pause (YELLOW). Fortinet −20.9% = earnings, not the wave.
  - Composite 22/40 raw, 16/40 shared-root-adjusted; 1 FIRED, 8 NOT-FIRED.
- **CROSS-DOMAIN / CALIBRATION:** LIQUID: no T-bill sale needed; redemption test at reopen. HENRY: crypto equities, PANW row 9. Uncertain: whether named victims surface; whose firewalls Dream saw (THN suggests PANW, unconfirmed).
- **FORWARD:** 11/02 Binance reopen (still suspended ⇒ VX-02 question to PROME); 11/03 Keystone; 11/04 PHP2Shell +14d + ConnectWise + Dream correction; 11/05 financial-claim pass + bank-vendor cluster watch; 11/18 row 9 equity persistence (HENRY); 11/20 R1 flip test.
- **NEXUS-NAMED (verbatim):** "NEXUS / PROME | Composite unchanged: 22/40 raw, 16/40 shared-root-adjusted; 1 FIRED, 8 NOT-FIRED, all re-checked 10/29 | P3 | Wave state for synthesis".
- **FLAGS:** Not stale. Post-brief LIQUID→CYPHER packet (b8a2b1249, 10/30 15:41) and WALTER bulk-power security order route not in brief.

---

## CROSS-BRIEF (≤10 lines)
1. **Sinokor share of Hormuz** — BRENT "about half of Hormuz supertanker transits" (Lloyd's List 10/26); HAWK "~47% of Hormuz VLCC transits… secondary only"; FALCON "Reuters: ~40% of Sept Hormuz crude outflow". Three bases (transits vs outflow), none primary; consistent direction, differing magnitude.
2. **Russian diesel regime** — YURI (10/31, primary): ban to 31.01.2027, producer exemption DELETED. BRENT (10/29) "ban decision at its October 31 expiry" and OSPREY (10/29) "producer ban runs to 10/31… extension vs lapse" — both pre-№1436 and mis-framed vs YURI's precise form. OSPREY's lapse-starts-30-day-clock branch is now moot; OSPREY counts "Russian diesel exports to the US" as product recovery while YURI says the US-quota channel has no public act.
3. **Hormuz casualty census** — FALCON (10/30) 6 confirmed, plus LOUISE 1/RITI limpet attacks 10/29; HAWK (10/29 13:3x) has 6 but not the limpet attacks, Qeshm claim or Qatar FM extension → HAWK's cross-war view lags its owner by ~a day.
4. **WQ-470 X** — HAWK "provisional +25%"; OSPREY "X bound at +92% and the joint draft breaks" (KB-238). Disagreement on the binding value/state.
5. **11/10 export-control clocks** — ZHAO ZHA-19 65% / ZHA-20 70%; HAWK "BIS and MOFCOM clocks still end Nov 10", USTR port-fee suspension proposed to 2027-01-09 (proposal); WATT "Nov 10–11 Beijing battery T1 boundary"; ZHAO's 公告58 battery leg keys on MOFCOM. One event, three desks — one root.
6. **Polar vortex** — AEOLUS ECMWF reversal ~11/05 (not observed); BRENT's NOT-FIRED "US gas on polar vortex" idea; WATT P1 already 5 on outages. Weather root shared, not independent votes.
7. **Unnamed thread:** WALTER's 10/29 "conditional bulk-power equipment security order" routed to WATT+CYPHER sits in neither brief; CYPHER's PANW/perimeter-appliance exploitation + WATT's P3 grid-equipment custody hint at a grid-cyber edge neither names.
8. **Unnamed thread:** Qatar LNG FM to end-December (FALCON) × ZHAO V8 rescore 4→5 open (TTF €100.72) × HAWK "Taiwan and Japan current LNG stock days not public" × SAM Japan LNG — an Asian-gas leg into Taiwan fab power no desk sizes.

## FOCUS QUESTIONS
**(a) Energy since 10/26:** Product side moved, crude/flow did not get a measured loss. BRENT: Dec crack fell below the $95 notice (94.02 10/27; 93.06 10/28 EST) and touched 88.60 intraday 10/29 below the $90.16 sell line (not a settlement); Brent Dec 113.88→115.32, WTI 99.90→102.78 (10/27→28, wire EST) on the WSJ post-midterm report, not barrel loss; refiners "no signs of demand destruction", BRT-31 NON-QUALIFYING; retail gasoline $4.269 (+40.66% YoY, 10/26). FALCON: Hormuz ~1 tanker/day, Sinokor action 11/1, first limpet attacks 10/29, Qatar LNG FM to end-Dec. YURI 10/31: producer diesel exports stay banned to 31.01.2027 (no 11/1 easing). OSPREY: no refinery strikes since 10/16 (lull). Net: diesel margin compressing (disinflationary) while crude and gasoline stay elevated; no new transmission shock to US markets is measured in these briefs — the risk is posture (post-11/3 campaign window, Sinokor) rather than a fired event.
**(b) 10/30 semis/mega-cap selloff:** No brief here post-dates the 10/30 close except YURI/AEOLUS (silent on it); no desk attributes the selloff. Nearest: ZHAO's 11/10 clocks (no extension instrument; ZHA-19 65%/ZHA-20 70%) and its "unpriced binary" BIS Entity-List package naming CXMT/YMTC/SMIC subsidiaries (re-check 11/2); HAWK's helium allocation at one named fab; WATT's IMM 4,016.9 MW cancelled-or-delayed data-center projects (~42% of forecast growth, 9/21) and outage-driven PJM price spikes; CYPHER's PANW active exploitation (row 9 equity persistence is HENRY's 11/18 grade) and its 10/29 QQQ −2.60% reading on the Binance clock.
