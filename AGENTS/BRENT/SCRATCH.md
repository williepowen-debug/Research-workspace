# BRENT SCRATCH — October 1, 2026 (Thursday; brent-1001, PROME prome-0c Tier-1 spawn; boot 13:17 ET by `date`)

## CHANGES SINCE LAST SESSION
- **The 9/30 session died in the box crash (~15:0x)** after its last commit `98d07c696` (12:01). Its grades are in STATUS/THESIS: BRT-29 FAILED · BRT-12 VOID · **F-b Cushing FIRED** (THESIS v5.11) · BZZ26 graded from 9/30. It wrote no SCRATCH or NEXUS write-back; both are rewritten here.
- **Will, 9/30:** sold the USO Sep-30 $159C ×2 @ $0.01 (−$919.46) and rolled into the USO Oct-09 $150C ×2 @ $2.99. On 10/1 he sold 1 of 2 @ $3.92 (+$91.67), leaving ×1. WQ-346 RULED (BRT-31 v2). Standing practice: **sell or roll every option before expiry** (USER.md).
- **Supply news:** Russia's producer diesel ban was extended to 10/31. China halted product exports beyond HK/Macau until Beijing guidance after Golden Week (10/7). The US offered the last ≤40M bbl SPR exchange (deliveries Nov–Dec). MRPL cancelled spot tenders. Four Hormuz hulls were hit 9/28–9/29 (none sunk). FALCON saw a new non-flare heat source at Ghawar/Ain Dar 9/29–9/30 (strike NOT established). US export ban: still unsigned; the WH is leaning to red-dyed diesel.

## WHAT I DID THIS SESSION
- **L0 drain:** 13 items = 13 board_log rows = 13 `git mv`s. Graded the three ACTIONs: China (-008), SPR (-019), the 9/30 squeeze (-006). **Nothing fires.** Note: [research/2026-10-01_l0-drain/NOTE.md](research/2026-10-01_l0-drain/NOTE.md).
- **VLO-HELD-01:** B1 NOT FIRED (FR + public inspection + WH, 13:20–13:2x ET). Leg A NOT FIRED (9/30 Nov crack proxy $106.51).
- **BRT-31 REGISTERED** (WQ-346): row, note, CHANGELOG, THESIS version-line note, RULINGS § R-2026-10-01-WQ345-346, banner on the v2 draft.
- **TRADE.md corrected from FORGE:** 159C sold; 150C ×1 `expiry=2026-10-09`. `pending_receipts` rc=0; guard falsified (flags it on 10/10).
- **9/30 settle-window proxies published.** METI August read at the primary, packet to SAM (`ee0f0d231`). OSPREY's Bloomberg ask answered (`4e571c612`).
- **CATALYSTS:**
  - Russia ban graded EXTENDED, successor row 10/31;
  - XLE row graded;
  - new rows: SPR bids 10/06, China guidance 10/08.
- **REGISTRY header:** vendor expireDate convention clarified (BZ = day after; CL/HO = last trade day).
- **DAEDALUS WQ-252 A′:** states my form correctly, with 2 notes (in the PROME memo).
- **Rotations:**
  - STATUS 91% → 83% (9/28 PM block → `archive/STATUS_dated_2026-09-28_PM.md`, 3430 B crc32 `9ff2228d`);
  - NEXUS banners → `archive/NEXUS_BRIEF_banners_2026-09-28_to_09-18.md` (3040 B crc32 `01317ace`);
  - STANDING STATE re-stamped 10/1 (JWLA-035 re-read; archive CRCs reproduced);
  - TRACKER re-stamped.
- **$0. No trade, band, threshold or score change.**

## ⚠️ MY ERRORS / NEAR-MISSES
- My REGISTRY sentence "vendor expireDate = the day AFTER last trade" was true only for Brent. Ported to CL/HO it would switch the crack a day early. Caught while checking DAEDALUS's dates; clarified.

## NEXT SESSION (dated, future-verifiable)
1. **Thu 10/1 after ~14:30 ET (this session's phase 2, on PROME's re-ping):** publish the 10/1 settle-window proxies (BZZ26, CLX26, HOX26, Nov/Dec cracks) in STATUS + the PROME memo.
2. **Fri 10/2 ~15:30 ET:** COT-35B #8 (as-of 9/29). Run `cot_grade.py --expect 2026-09-29`; cross-check the raw `f_disagg.txt`. COT_VINTAGES is +12d stale until then.
3. **Sun 10/4:** OPEC+ (a November number only; grade on the Secretariat text).
4. **~Mon 10/5:** Aramco Nov OSP (Yanbu record-only, WQ-331 P4).
5. **Tue 10/6:** WQ-252 crack-month sitting (L471). SPR exchange bids close 11:00 CT, then read the DOE award volume and return terms.
6. **Wed 10/7 WPSR:** Cushing after F-b; distillate exports vs curbs; the SPR draw.
7. **Thu 10/8:** China export guidance after Golden Week; read the named Nov cracks.
8. **Thu 10/15:** BRT-31 first window print (w/e 10/9).
9. **Sat 10/24:** WQ-264 shadow run ends; the Saudi resolver registers only after it.
10. **Owed, carried:**
    - INCIDENTS: Kuibyshev + Bashneft-UNPZ 9/22 (processing status unstated); 11 ACTIVE rows past 60d.
    - Path-B successor letter: DONE (BRT-31).

## OPEN THREADS / WATCHES
- 🔴 **US diesel export ban:** unsigned. A signed text = VLO-HELD-01 B1 ⇒ packets to TERRY/HENRY/WALTER the same day.
- 🟠 **China product-export halt:** size UNKNOWN until GAC data (~11/20); restart date unset.
- 🟠 **Ghawar/Ain Dar heat source:** FALCON's lane. A Saudi R1 statement or a FAL-01-class output figure would be the first thing that could matter to BG-02's successor.
- 🟡 **METI Kuwait/Qatar:** do joint-stockpile draws book as imports? SAM's MOF table is the cross-check.

## POSITION DECISIONS PENDING
- **USO Oct-09 $150C ×1:** Will's hand, sell-or-roll before Fri 10/09 (TERRY `MGMT-USO150C-OCT09` rail 15:00 ET).
- VLO 1 sh: exit rule VLO-HELD-01 (TERRY grades). USO 37 sh: hand-managed (WQ-200). WQ-192 STAND DOWN.

## MAIL STATE
- **Inbox:** clear at 13:28 ET (13 consumed, all logged + moved).
- **Sent (all committed):** SAM `ee0f0d231` · OSPREY `4e571c612` · PROME memo `cab0090d8`. SAM and OSPREY are DARK; their packets wait in their inboxes. No open outbox.
