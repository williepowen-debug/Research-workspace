# ZHAO STATUS — COLD ROTATION 2026-11-06

Moved VERBATIM from STATUS.md at the 11/06 rewrite (READ-CAP rule 5: rotate-tier at 75% of budget). Nothing here is current; record = `workbook/KB.tsv`.

## ⓐ Header lines through 11/02

**Updated:** 2026-11-02 08:52 ET (by `date`) — **Session prome-40 L482 spawn: instrument re-check + L0 drain 3/3** (KB-221..223). Prior: 2026-10-29 14:36 ET closeout, session zhao-02 desk sweep (`reports/2026-10-29_DESK_SWEEP.md`).
📌 **THIS WEEK, IN ORDER OF WHAT MATTERS:** ① **11/10: two export-control clocks restart, still no instrument** (US BIS Affiliates Rule · China 公告70); USTR's s.301 ship-fee proposal to 1/9 is the only paper and re-dates neither (KB-210); **ZHA-19 65% / ZHA-20 70%** that both get paper in time. ② **NPCSC 11/2–6** is the only near venue for a fiscal number; the Plenum (10/26–29) gave none (KB-214); **ZHA-21 12%**. Opened 11/2 with the Financial Law 2nd reading; full opening agenda not located 08:51 ET; the 10/22 proposed agenda has no budget item (KB-222). ③ **HK peg at its 7.85 weak edge**, HIBOR-SOFR YELLOW, no HKMA intervention yet (KB-216). ④ **The PBOC is holding the yuan BACK** (fix weaker than market every month since Dec-2025; V6 3·A, KB-219). ⑤ Sep data: exports +36.3%, PPI +5.0%, gold +23 t, CGB 1.63% (KB-217).

## ⓑ POST-SUMMIT clock block through 11/02

## 📌 **POST-SUMMIT: THE 11/10 CLUSTER IS TWO LIVE CLOCKS, NOT THREE — AND BOTH STILL READ 11/10 ON THEIR OWN INSTRUMENTS**

| Clock | Instrument | Reads today | Status |
|---|---|---|---|
| US perimeter | BIS Affiliates Rule (FR 2025-19846) — reimposed **effective 11/10** | 11/10 — no stay extension in FR (published or public inspection) through **11/02 08:49 ET** | 🔴 LIVE (KB-177, 192, 202, 210, 221) |
| China perimeter | MOFCOM/GAC 公告2025年第70号 — suspends 55-58, 61 一(一)(二), 62 「至2026年11月10日」 | 11/10 — no re-suspension 公告 through **11/02 08:50 ET (list still to No.52; 46 located, 45/47 not)**; MOFCOM 9/28 statement names 1/10 (not an instrument) | 🔴 LIVE (KB-172..180, 189, 192, 202, 210, 221) |
| 🆕 US s.301 ships (separate) | USTR s.301 maritime action, suspended to **11/9 23:59 ET**; FR 2026-21755 **PROPOSES** extension to **2027-01-09** | proposal only; comments closed 10/30; final notice **not yet published at 11/02 08:49 ET** | 🟠 first instrument carrying the 1/9–1/10 date (KB-210) |
| ~~US tariff~~ | ~~EO 14358 §2 (heading 9903.01.63)~~ | — | ⛔ **VOID since 2026-02-24** (EO 14389, KB-183) |
| 🆕 China (separate) | MOFCOM 公告2024年第46号 **clause 2** suspended to **2026-11-27** | 11/27 | 🟠 B2, content UNVERIFIED (KB-185) |

**If the 1/10 extension (Bessent verbal 9/23; MOFCOM written 9/28) becomes instruments, the two live clocks re-date to 2027-01-10; until an instrument publishes, they stand.** ✅ 10/09, 10/20, 10/29 and **11/02** re-checks: **none published for either clock** (KB-192, 202, 210, 221) — the only paper is USTR's s.301 ships proposal, a separate instrument. Next look **11/9 (MUST-RUN)**, then 11/10 Beijing for ZHA-20; blind spots = MOFCOM 公告 39/43/45/47 (not located); Tariff Commission now reachable. ⛔ DO-NOT-MERGE still binds. The 8/22 Canada precedent (announced, never instrumented, tariff went live) is why a verbal extension is not graded as done.

## ⓒ Dashboard rows superseded 11/06

| Brent crude | **$112.46** (live 10/22 13:26 ET, +3.34%; contract label UNKNOWN, WALTER: Dec) | Asia shock transmission | 🟠 | boot.py `BZ=F` front — **never compute a % move across a roll.** **HAWK/BRENT own the price** |

## ⓒ-2

| USD/CNY | **6.65** (yfinance 10/29 13:31 ET; CNH 6.656) · CFETS fix **6.7147** (10/29, KB-212) — fix **~1% weaker than spot** | >7.30 = 🟠 | 🟢 **CORRECT BUT UNINFORMATIVE** | ★ **Fix set WEAKER than market ⇒ PBOC leans AGAINST the pace of appreciation.** Now measured both ways: V6 **3·A**, V9 **2·A** (`VX-2.10/2.11`, KB-219). ~9.8% from 7.30 · `VX-2.01` |
| USD/KRW | **1,339** (intraday 10/29; 10/28 close 1,326.8) | >1,500 = BoK selling | 🟢 **EASED THROUGH** | **~47 won stronger than 9/18 (1,385.95)**; 161 won from the line. ⚠️ two 8/3 caveats still UNVERIFIED · `VX-2.05`, KB-126/216 |
| HK Aggregate Balance | **HK$53,999M** (10/29) | <$45B = 🟡 | 🟢 | HKMA API — flat vs 9/18; **no intervention 10/22–29**. 🟡 **USD/HKD 7.8461 = 0.004 from the 7.85 weak side** — at 7.85 HKMA must buy HKD and this balance falls; that is the next tell · `VX-2.03`, KB-216 |
| 1-mo HIBOR | **2.71494%** (10/29) | — | 🟢 | **−15bp vs 9/18** — cheaper HKD funding = carry pressure on the peg · KB-216 |
| HIBOR-SOFR Spread | **−122.5bps** (5d-mean −119.7) | worse than −200bps = 🟠 | 🟡 **GREEN → YELLOW 10/29** | HIBOR 2.715% (HKMA 10/29) − SOFR 3.94% (NY Fed 10/28). Both bases past −100 ⇒ not boundary noise. 78bp from Orange · `VX-2.04`, KB-216 |

## ⓒ-3

| 🟠 **Construction PMI (SEP)** | **50.3** (Aug 46.9, +3.4) · new orders **45.7** · employment **44.3** | 🟠 **TRIPWIRE FIRED (>47.5) ⇒ V5 5→4 by the letter.** ⚠️ Disagreement recorded: a special-bond-funded activity bump (secondary attribution), demand still contracting | NBS primary 10/09 · `VX-6.12`, KB-193 |
| **PMI cluster (SEP)** | mfg **50.1** · non-mfg **50.2** · svcs **50.2** · composite **50.7** | 🟢 **all back above 50**; small firms 48.9 | `VX-6.12`, KB-193 (Aug: KB-128) |

## ⓒ-4

| **RatingDog Mfg PMI (SEP)** | **52.1** vs NBS **50.1** — gap **+2.0** (on the Orange line) | 🟡 private strength persists, still export-composed (Aug read, KB-158); services 51.6; input prices up 4-month high | `VX-6.14`, KB-217 |

## ⓓ Routing state 10/29

🔔 **Routing state 10/29 (checked at recipients' inboxes):** 10/29 USTR-ships packet and 10/29 HAWK plenum FYI **delivered**. **NOT relayed, flagged to PROME 10/29:** `outbox/2026-10-20_…_no-extension-instrument-and-two-new-trade-levers.md` (§2 公告48 AI/PV, §3 Graham-Act EO → BRENT) and `outbox/2026-10-16_…_minus-41pct-is-June-CRUDE-imports-not-copper.md` (→ MIDAS). Awaiting routing: 10/29 LIQUID HK-peg FYI, 10/29 kill-leg/V6-V9 FYI. 9/25 routed; 9/30 declined as duplicate. History → COLD_20260925 §ⓕ. Still owed: `VX` row for the Chinese clock (NEXT #12).

## ⓔ Calendar rows through 11/10

| ✅ Thu Oct 1 | H.4.1 week of 9/30 — **closed 10/29 as overtaken, not read** (BOND's 9/23 question answered by KB-186) | — |
| ✅ Thu Oct 22 | Selloff read (KB-207) · L482 pre-fetch: none (KB-208) · Plenum re-confirmed (KB-206) | — |
| ✅ Mon–Thu Oct 26–29 | **Fifth Plenum — GRADED 10/29:** communiqué (Xinhua 05:42 ET) = Party self-governance decision; **no fiscal figure, no FYP content**; 21st Congress H2 2027 (KB-214/215) | — |
| ✅ Thu Oct 29 | L482 re-check (due 10/27): no instrument for either 11/10 clock; USTR s.301 ships proposal to 1/9 (KB-210) | — |
| Sat Oct 31 | NBS October PMI (mfg 50.1 in Sep; construction 50.3 = V5 re-raise test <47.5) | 🟡 |
| Mon Nov 2 | RatingDog Oct PMI · L482 re-check (then **MUST-RUN 11/9** = BIS stay's last day; USTR s.301 ships suspension also ends 11/9 23:59 ET) | 🟠 |
| Mon–Fri Nov 2–6 | **NPC Standing Committee, 25th session** — the legal venue for any budget revision; none on the 10/22 proposed agenda (KB-206). **ZHA-21 12%** | 🟠 |
| Sat Nov 7 · Tue Nov 10 | SAFE Oct reserves/gold · **11/9–11/10 clocks: ZHA-19 65% / ZHA-20 70%** · Oct trade/CPI (~) | 🔴 |

## ⓕ NEXT ACTIONS items 2 and 9

2. ✅ **DONE 10/9 + 10/20 + 10/29 — instrument re-check: none for either clock** (KB-192, 202, 210); USTR s.301 ships proposal is the first US paper with the 1/9 date. 🔴 **NEXT: 11/2, MUST-RUN 11/9** — read the USTR FINAL notice when it lands; China MoT port-fee mirror (primary unread); locate MOFCOM 公告 39/43/45/47; 公告2025年第72号 primary (46号 cl.2) still owed; WATT T2 read carried.

## ⓕ-2

9. ✅ **10/29 maintenance (step 5):** KB `Stale_By` now has a reader (boot §6: **87** rows past due — a re-check backlog; ⛔ never bulk-mark SUPERSEDED) · 5 Feb-2026 VX rows 🧊 FROZEN · catalyst reader fixed (DONE/RESOLVED rows no longer fire; open rows never age out) · boot pulls the CFETS fix (V6/V9) and HKMA (peg) live · NEXUS brief CALIBRATION/SENDING/CATALYSTS rewritten · 5 files archived · charter trimmed to 32,211 B · `workbook/LEDGER_GLOB` declared. **Open-items pass 10/29 (KB-220):** Vector 8 row `VX-8.02` ✅ · ZHA-05 → STUCK, successor `VX-6.15` ✅ · V6 market leg → Fed H.10 ✅ (CFETS 16:30 close endpoint not found) · 5 packets delivered directly ✅. **Still owed:** Vector 8 rescore 4→5 question (needs a China LNG/crude-import leg) · base-rate rural NPL history, then register a ZHA-05 successor · ZHA-10 `Date_Made` defect.

## ⓖ Bottom line OCT 29

**OCT 29 — Quiet desk, busy domain: what the last three weeks actually say.** China is booming abroad and soft at home. Exports rose 36% on the year in September, factory prices are rising again on energy, and the central bank is buying dollars and gold (about 23 tonnes in September) while deliberately holding the yuan back from rising. That is the opposite of a country selling Treasuries under pressure. The selling is still happening, but at half the pace each month. At home, construction orders are still shrinking and the 10-year government yield has fallen to 1.63%, a sign of weak loan demand, not safety-buying. The near-term risk is not a China crisis but a calendar one. **On 11/10 both governments' suspended export controls switch back on unless paper arrives**, and so far only a side rule (US port fees on Chinese ships) has paper. I put 65–70% on both getting extended in time, but the two calls are really one bet on the same deal. Watch Hong Kong too: its dollar is at the edge of its band, and if the HKMA has to step in, money drains from Hong Kong's banking system.



## ⓗ November-window paragraph (moved verbatim from STATUS CALENDAR, 2026-11-06 16:49 ET). Its US leg was overtaken by FR 2026-22793

> 🔴 **THE NOVEMBER WINDOW — TWO LIVE CLOCKS ON 11/10 + ONE ON 11/27 (corrected 9/25).** **Tue 11/10 US:** BIS Affiliates Rule reimposed effective (≥50% aggregate ownership, zero new listings). **Tue 11/10 CHINA:** 公告70 expires — six announcements incl. **Li-battery/LFP cathode/graphite anode (公告58) — WATT's triggered channel keys on the MOFCOM instrument, not the date** (`reports/2026-09-25_WATT_TRIGGER_WORDING_gonggao58.md`). **Fri 11/27 CHINA:** 公告2024年第46号 clause 2 (B2). ⛔ ~~US IEEPA reciprocal lapse~~ **VOID since 2/24/2026.** Full verbatim prior → COLD_20260925 §ⓒ.


## ⓘ 11/08 header, 11/10 cluster, resume notes and bottom-line opener (moved verbatim from STATUS 2026-11-09 12:14 ET). Overtaken by the 11/9 re-suspensions, KB-246 to 249

**Updated:** 2026-11-08 12:09 ET (by `date`) — **L482 and L858 instrument checks run a day early (PROME prome-bf, Will's word), KB-242..245.** Only the 11/10 cluster, resume notes, calendar and bottom line changed; every other cell is as of the 11/06 close. Prior: 2026-11-06 17:47 ET.
📌 **THIS WEEK, IN ORDER OF WHAT MATTERS:** ① **China's 11/10 clock is the only export-control clock still open.** The US stay is now in the published 11/9 Federal Register (KB-242). MOFCOM has nothing as of 18:01 Beijing 11/08; **ZHA-20 85%**, with two adverse inputs since the mark: the US call (KB-240) and MOFCOM's 11/07 complaint that the US is "departing from the heads-of-state consensus" (KB-244). The ships suspension has no US final notice and cannot get one in the FR before it ends 11/9 23:59 ET; last year's came 3 days late, so that does not mean fees resume (KB-243). ② **🔴 The PBOC moved its main policy rate to overnight at 1.25% on 11/02, and this desk missed it for 4 days (KB-238).** ZHA-24 withdrawn on Will's word, ZHA-26 replaces it (KB-241). ③ **China 10Y 1.59%, through the 1.60 Orange line** (KB-239). ④ **October activity fell back under 50:** mfg 49.3, composite 49.7, construction new orders 40.0 ⇒ **V5 4→5, total 29** (KB-227). ⑤ **NPCSC closed with no fiscal figure,** ZHA-21 NO (KB-224). ⑥ China's security review prohibited SoftBank's ABB Robotics deal in China, the China business only (KB-228, 236). ⑦ HK off the weak edge (7.84), no HKMA activity, spread −135.9bp YELLOW.

## 📌 **THE 11/10 CLUSTER: THREE SEPARATE CLOCKS (read 11/08 12:01-12:07 ET)**

| Clock | Instrument | Reads 11/08 | Status |
|---|---|---|---|
| US perimeter (L435) | BIS Affiliates Rule stay | **Published** in the 11/9 FR issue, 91 FR 70789-70790, text unchanged from public inspection: "further stayed until January 10, 2027". Branch C did not occur | 🟢 PAPER PUBLISHED; ZHA-19 grades 11/10, not re-marked (KB-242) |
| China perimeter (L437) | MOFCOM/GAC 公告2025年第70号 | 至2026年11月10日. No re-suspension on the live list (MakeTime 18:01 Beijing 11/08); newest still 第56, 57号. GAC unread (HTTP 412) | 🔴 LIVE; ZHA-20 85% (KB-242, 244) |
| US s.301 ships (L858) | USTR proposal FR 2026-21755 to 1/9 | Suspension ends 11/9 23:59 ET. **No final notice published or on public inspection; the complete 11/9 issue has none, so FR publication before the end is no longer possible.** ⚠️ 2025 precedent: final published 11/13 for a suspension effective 11/10, so fees resuming does not follow from FR timing | 🟠 OPEN until USTR acts (KB-243) |
| China ships mirror | MoT 公告2025年第60号 · MOFCOM 令2025年第7号 (Hanwha) | Both 1 year from 2025-11-10, keyed on the US suspension. No re-suspension seen (MoT home page only) | 🟠 follows the US act (KB-243) |
| ~~US tariff~~ | ~~EO 14358 §2~~ | — | ⛔ **VOID since 2026-02-24** (KB-183) |
| China (separate) | 公告2024年第46号 clause 2 | 11/27 | 🟠 B2, content UNVERIFIED (KB-185) |

⚠️ **MOFCOM list: read `mofcom.gov.cn/zwgk/zcfb` via the unit API WITH `parseType=bulidstatic`. Without it the API answers 200 with an EMPTY list, which is a bad request, not "nothing filed" (KB-237). `/zcfb/index.html` froze at 10/26**, so 11/02's "newest is 第52号" could not see later rows (KB-221 corrected, no conclusion changed). Run book, branch table, WATT T1/T2 state: `reports/2026-11-06_PREP_11-10-clocks.md`. ⛔ DO-NOT-MERGE: the US stay is not evidence China extended. Next: ZHA-19 grade and the ships outcome on 11/10, the Beijing read for ZHA-20 at 11/10 to 11/11.

---

## ▶️ RESUME NOTES (2026-11-08 12:09 ET, prome-bf instrument check)

No job running. **Clocks last read 12:01-12:07 ET 11/08; re-read before citing.** Unpublished at the 11/06 read, not re-read today: SAFE Oct reserves and gold, GACC Oct trade.
- **L482 done a day early (KB-242):** no new document matching the 1/10 extension. BIS stay published 11/9. MOFCOM 公告70 armed. WATT T1 and T2 unfired.
- **L858 (KB-243):** no USTR final in the FR before 11/9 23:59 ET is now certain; the consequence is not. **Owed 11/10:** read USTR (press releases, public inspection for 11/10 and 11/12 issues) for the determination, and MoT/MOFCOM for China's matching notices.
- **Tue 11/10:** grade ZHA-19 on the 11/10 record. **Wed 11/11:** read ZHA-20 at the Beijing 11/10 close, send WATT its notice the same session on either branch. Run book: `reports/2026-11-06_PREP_11-10-clocks.md`.
- **Needs Will's word, not a peer's:** two `CLAUDE.md` lines, the WQ-622 line and NEXUS's B24 change at `CLAUDE.md:37`, within 290 B of cap room. The NEXUS packet is filed to `processed/` (KB-245); the ask lives in NEXT ACTIONS 9. DAEDALUS gets the applied commit after.

---

**NOV 8 NOON CHECK — nothing new is on paper.** The US export-control hold is now in Monday's printed Federal Register, unchanged. China's Commerce Ministry still has no notice extending its own hold, and on Saturday it complained that the US is walking away from the leaders' deal; I log that against my 85% but do not move it. The ships deal has no final US notice and cannot get one in the Federal Register before it lapses at midnight Monday, but last year's notice came three days after the fact, so that alone does not mean the fees come back. Tuesday decides it.
