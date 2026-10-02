# BRENT SCRATCH — October 2, 2026 (Friday; PROME prome-70 spawn + four follow-ups; boot 08:30 ET, closeout 11:2x ET by `date`)

## CHANGES SINCE LAST SESSION
- **Thu 10/1:** Dec Brent settled **$102.31 (+$4.28)** (Reuters). Drivers: China's product-export halt and the WSJ deployment report (third carrier + 9–10k troops; one US official says it is a carrier RELIEF).
- **Fri 10/2:**
  - Oil gave it back. The **G7 DECIDED a release of up to 100M bbl of diesel + crude over 4 months, with diesel within 20 days** (NBC 10:22 ET quoting the G-7 statement; Macron; Trump). The split is unpublished, and the US ban threat is NOT withdrawn.
  - **Nov ULSD crack 102.10 (10/1 proxy) → 95.87 intraday 10:30** (vendor, not a settle).
  - TERRY graded its USO150C early-sell condition MET (lean SELL 10/2; the order is Will's).

## WHAT I DID THIS SESSION
- **10/1 proxies published:** Nov crack $102.10, BZZ26 102.37. Thursday's move attributed. → [note](research/2026-10-02_proxies-oil-move-cot/NOTE.md)
- **COT-35B:** 4.9086% and base 122,904.5 re-reproduced at the CFTC archive. 9/29 vintage not posted. NOT GRADED.
- **10/2 drop:** attributed to the Reuters report of the French 50+50 plan; the step at 03:50–04:05 ET was diesel-led.
- **G7 release:** verified at the wires. **B1 NOT FIRED** (FR 10:41). Leg A measured. TERRY packeted (`422d0ba24`) and doorbelled.
  - → [note](research/2026-10-02_g7-release/NOTE.md)
- **Events 10/2–10/16:** memo to PROME. **WPSR moves to Thu 10/15 12:00 (Columbus Day)**; COT not shifted; VLO earnings 10/22.
- **L0:** 12 WALTER items logged + `git mv` (7 + 2 + 2 + 1). -008/-019 (10/1) were already done.
- **CATALYSTS:**
  - 10/02 EU taskforce row added, graded, then re-graded (superseded by the G7 decision);
  - successor **10/22 ⌁**.
- **CHANGELOG** 10/02 evidence entry (v5.11 unchanged).
- **STATUS:**
  - 8 standing rows re-verified and re-stamped 10/2: CRCs reproduce, JWLA-035 newest, BRT-26 resolved, THESIS/BG-02 re-read.
  - Rotations: AM block → `archive/STATUS_dated_2026-10-02_AM.md`; receipts → `archive/STATUS_rotation_receipts_2026-10.md`; the G7 block moved to its note.
- **$0.** No trade, band, threshold or score change.

## NEXT SESSION — ⏰ ARMED, NOT DONE (also at the top of STATUS)
1. **COT-35B #8** (10/2 15:30 print, as-of 9/29). Run `cot_grade.py --expect 2026-09-29`, plus a second raw pull.
   - Pre-registered: SPENT practically unreachable. NO-VERDICT if shorts ≤118,325; otherwise NOT-SPENT.
   - Then propose review_by 10/09 to PROME.
   - **Never stack it with the 10/9 print.**
2. **10/2 settle-window proxies** (14:28–29 VWAP, rows dated 10/02):
   - Report the Nov ULSD crack against VLO-HELD-01 leg A ($95 notice / $90.16 sell). Packet TERRY.
   - **Before Thu 10/8** (1-min bars expire).
   - Also the 10/2 vendor daily row (L462 session check).
3. **OPEC+ 10/4 grade, Mon 10/5–Tue 10/6:** the Secretariat text at opec.org. Re-pull the spare figure first (Oct STEO 10/6).
4. **Tue 10/6:** WQ-252 crack-month sitting (L471). SPR exchange bids close 12:00 ET; read the award. Oct STEO.
5. **Wed 10/7 10:30 WPSR:** Cushing after F-b; distillate stocks/exports; SPR draw.
6. **~Thu 10/8:** China guidance.
7. **Fri 10/9:** the USO $150C expires (Will).
8. **Wed 10/14:** IEA OMR; VLO-HELD-01 leg A suspension date.
9. **Thu 10/15 12:00:** WPSR + BRT-31 first print.
10. **~10/22:** G7 first diesel window; VLO Q3 earnings.
11. **Owed, carried:**
    - INCIDENTS: Kuibyshev + Bashneft-UNPZ; **Volgograd (Lukoil) + Transneft Samara 10/02 (WALTER -010; damage NOT established; check OSPREY's grade first)**; 11 ACTIVE rows past 60d.
    - TANKER-LIVENESS human stamp (58d; boot BLOCKING).
    - TRADE.md not re-checked against FORGE since `dac72b4ae`: Will may sell the 150C today.

## OPEN THREADS / WATCHES
- 🔴 **US diesel export ban:** unsigned and NOT withdrawn after the G7 release. A signed text = B1 ⇒ packets to TERRY/HENRY/WALTER the same day.
- 🔴 **VLO-HELD-01 leg A:** intraday $0.87 above the $95 notice line. The sell line is a settle < $90.16. TERRY grades.
- 🟠 **G7 release mechanics:** split, country volumes, start of draws.
- 🟠 **China halt:** size UNKNOWN.

## POSITION DECISIONS PENDING
- **USO Oct-09 $150C ×1:** Will's hand. TERRY lean SELL today (≈$125 net at the 1.26 bid; wrong-colour sale).
- **VLO 1 sh:** VLO-HELD-01. **USO 37 sh:** hand-managed (WQ-200). WQ-192 STAND DOWN.

## MAIL STATE
- **Inbox:** WALTER lane clear at 11:2x ET after -010 (Volgograd/Samara, noted); top level empty.
- **Sent:**
  - PROME memos ×4 (`c0f0f9b4e`, `5ddb2dfea`, `422d0ba24`, `293c070fc`);
  - TERRY packet `422d0ba24` (receipted by TERRY at `235ef74ea`, loop closed).
- **Outbox:** nothing open.
