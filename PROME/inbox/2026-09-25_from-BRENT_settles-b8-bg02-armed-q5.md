# BRENT → PROME · 2026-09-25 03:07 ET · L329 due-row + L477 Q5 — settles published, #8 graded, BG-02 ARMED (not graded), inbox drained, Q5 delivered

**Spawn:** prome-fa, Tier-1 due-row (L329, WQ-184) + Tier-2 Q5 on Will's 02:55 ET word. Boot 02:58 ET; boot.py rc=2. The standing findings continue. **One is new and blocking: `KILL-LEG2-JWC-LISTING` is stale** (the datapoint is 10 days old against a 9-day budget). Not re-read this session → carried in SCRATCH.

## 1 · Brent settles (L430/L462) — the settle-proxy basis, stated
yfinance daily close on named contracts. It matches the 14:15–14:30 ET 15-min bar to within $0.08 on both days. That makes it a settle proxy, **not an exchange-authenticated settle**.

| | BZX26 Nov | BZZ26 Dec | Nov−Dec | M1−M3 |
|---|---|---|---|---|
| 9/23 | **103.08** | **98.12** | +4.96 | +8.05 |
| 9/24 | **106.60** | **100.22** | +6.38 | +10.18 |

- **SAM's $107.31 / $100.77 "[9/24 close]" = the 16:00–16:15 ET POST-settle trade**, +$0.71 / +$0.55 above settle. Adjudicated; packet sent to SAM.
- ⚠️ Vendor printed identical 9/23 and 9/24 daily VOLUMES on every contract. Closes unaffected. Note for the L462 fetch.py work.
- **L461:** word unchanged — re-pin to BZZ26 from the 9/30 session.

## 2 · Boundary #8 (WALTER -001/-016) — graded on NOVEMBER per the WQ-252 interim
- **9/15–9/23 crossing STANDS:** 7 sessions, margins $2.29–7.64, zero roll.
- **9/24 = 50.12, NOT MEASURABLE.** -016's 49.3–49.4 used post-settle bars.
- **December:** 2 sessions; does not count.
- ⚠️ **The November Brent leg ends 9/30 while the product legs run to end-October.** This is a basis gap for the 10/06 WQ-252 sitting. Packet sent to WALTER.

## 3 · BG-02 — ARMED, NOT GRADED (the window closes 17:00 ET; a WAIT of ~13 h ⇒ closing out per spawn rule)
- Pre-committed decision tree: `AGENTS/BRENT/setups/2026-09-25_BG-02-grade-PREP.md`.
- As of 03:0x ET: **no R1** (every restart and damage item is unnamed-source wire, C4) · **no R4** · Kpler is single-vendor, so **C5 gives it zero weight** ⇒ **modal LAPSE = NOT MET, not extended (WQ-264 ③)**.
- ⚠️ **Caveat that must travel:** in substance, Yanbu crude liftings were ZERO on 9/23–24. **NOT MET means "not established on the letter". It does not mean "no barrels lost".**
- **⇒ Re-spawn BRENT at/after 17:00 ET** for the grade. The same session can take rigs (BRT-26 final September print) + COT #7 (as-of 9/22, ~15:30 ET).

## 4 · WQ-264 encode confirm (leg ①)
- **Shadow-run window 2026-09-25 → 2026-10-24.** First read 03:01 ET 9/25: `AGENTS/BRENT/demand_destruction/data/yanbu_berth_2026-09-25.tsv`.
- **Observation:** the page snapshot is dated 9/22 — Al Muajjiz est. 476k · North Pt2 1.05m · North Pt1 0. It predates the window, so it is logged as a baseline and not scored.
- Mon/Fri routines instructed through the TRACKER alert-lines block (the design-contract path).
- ⚠️ **Not verified: whether the routines follow a new write instruction from TRACKER.** Check 9/28. If they don't, the prompt needs a RemoteTrigger update, which is your path.
- **Leg ③ closes at the 17:00 grade.**

## 5 · Q5 (LEAD) — `AGENTS/BRENT/research/2026-09-25_L477_Q5_energy-thesis-vs-held-expressions.md`
- **USO:** a WTI expression, not Brent (WTI−Brent −$11.99). **No position-level exit exists** (WQ-200 declined).
- **VLO:** the same bet as the staged shares, **looser entry** (no crack filter).
  - The refining margin is already decoupling: the Nov ULSD crack went **109.49 → 95.57 (9/22→9/24) while Brent rose $7.35**. A crude-led shock compresses the refiner's margin.
  - F1 < $95 is not fired on the proxy (+$0.57); HENRY/TERRY grade it on the CME settlement.
  - **An F1 stand-down would be the first numeric reading of the held share's own verbal invalidation ("crack rolls over hard"), and the held share has no numeric exit.** Named, not filled — that would be a TERRY card for Will.
- **Duration shorts:** running on real rates, not oil (HENRY `0d8616964`).
- HENRY leg integrated. **TERRY leg: asked 03:0x ET (terry-fa); see COMPLETION GAPS.**

## 6 · Inbox drain + other
- 12 consumed (8 WALTER + 4 top-level); board_log 12 rows = 12 moves. COR-20260924-11 APPLIED.
- Diesel-ban state: floated, denied on the record 9/23, no order. The US product legs of #8/F1 are exposed.
- OSPREY: Novorossiysk halt cause UNESTABLISHED (reply sent).
- MARCO registered as a consumer of `MKT-BZ-F-BELOW-85`.
- ⚠️ **`NEXUS_BRIEF.md` = 31,498 B, 97% of the 32,550 read cap.** A rotation is owed at the next session.
- **$0 · no trade, threshold, band or score moved.**

## COMPLETION — BRENT — 2026-09-25
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/BRENT/{STATUS,SCRATCH,NEXUS_BRIEF,RULINGS}.md, board_log.tsv, registry/corrections_receipts.tsv, workbook/REGISTRY.tsv, demand_destruction/TRACKER.md, demand_destruction/data/yanbu_berth_2026-09-25.tsv, setups/2026-09-25_BG-02-grade-PREP.md, research/2026-09-25_L477_Q5_*.md, archive/STATUS_dated_2026-09-23.md, 12 inbox moves; packets → WALTER/SAM/OSPREY inboxes; this memo
RESULT: Published Brent settle-proxies 9/23 $103.08 / 9/24 $106.60 (Nov; Dec $98.12/$100.22). Graded #8 on Nov (9/15–9/23 crossing stands, 7 sessions; 9/24 50.12 unmeasurable). Drained 12 inbox items. Started the WQ-264 shadow run (9/25→10/24). Delivered Q5: Nov ULSD crack −$13.92 while Brent +$7.35, so the refining expression is decoupling from crude.
GAPS: BG-02 NOT graded — window closes 17:00 ET (modal LAPSE, prep armed). Rigs/COT #7 print later today. TERRY's Q5 exposure leg not received by memo time. Routine compliance with the shadow-run TRACKER instruction unverified until 9/28. No exchange settle on any figure (single vendor).
WILL_NEEDS: None.
FOLLOW-UP: Re-spawn BRENT at/after 17:00 ET 9/25 for the BG-02 grade + BRT-26 rigs + COT #7 (L329); the F1 CME grade is HENRY/TERRY's after today's close.
