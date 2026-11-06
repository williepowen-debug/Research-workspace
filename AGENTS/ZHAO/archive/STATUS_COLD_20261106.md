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

