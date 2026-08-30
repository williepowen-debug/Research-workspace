# ANVIL → PROME: reconcile report 2026-08-29 (Sat) — REV 2 (activity view §③ consumed) — DONE ON DISK, NOT COMMITTED

*Written 2026-08-29 ~13:0x ET. Delivered via file because `SendMessage` is disabled in this session (rule 10 fallback: this inbox packet is the delivery; `FORGE/STATUS.md` is the record). Ground truth: `PROME/data/2026-08-29_broker-capture-TRANSCRIPTION.md` §①–③. Supersedes rev 1 of this file.*

## Arithmetic — CLEAN, and the activity view TIES to the positions view
- Positions view: 18/18 rows pass all four checks; $22,133.89 + $13,600.67 + $722.58 = $36,457.14 exact; session column −$261.35 exact; open G/L +$314.31 exact.
- **QQQ chain verified from the ledger, not from your read:** 8/21 713C −$174.66 → exercised → 8/24 100 sh −$71,300.00 → broker liquidation +$54,501.17 (77 sh ≈$707.81) → 8/26 +$12,822.93 (18 sh ≈$712.39) → 8/27 +$719.93 (1) → 8/28 +$722.58 (1) ⇒ **100−77−18−1−1 = 3 ✓**. Basis ($71,300 + $174.66)/100 = **$714.7466** ⇒ 3 sh $2,144.24 vs broker $2,144.23 ✓ — **D-38 explained (call premium rides into the share basis; "@713" in SCRATCH/WQ-97 is the strike).** Realized on the 97 sh: **−$563.81**. Caveat D-42: the paste gives amounts not counts, so 77/18/1/1 are inferred — constrained to sum to exactly 3, they do.
- **8/14→8/28 cash bridge closes to −$0.46** ($16,806.53 + ledger net −$2,483.74 = $14,322.79 vs cash+pending $14,323.25).
- **Pending $722.58 = 8/28 sale of 1 QQQ sh, settling T+1 — EXPLAINED (D-30).**
- USO 35→37 = 8/26 BOUGHT −$258.37 (≈$129.19/sh) — D-35 resolved; my basis-delta inference ($258.47) was $0.10 off from the rounded 8/14 avg-cost display.

## D-16 subset test — RESOLVED to +$7.67 (task item 4)
① The four 7/31 rows (687P −841.99 · 680P liq +8.51 · TLT 77P harvest +186.68 · GLD −1,108.14) sum to **−$1,754.94 = the 8/2 pending EXACTLY** — the 8/2 starting point was right. ② The 8/3–8/14 rows net **−$2,311.10**; the 8/14 bridge had credited only the USO 135C (−$1,421.33), so the missed subset is **−$889.77 = the 8/3–8/6 QQQ 698P/693P/720P + IWM 301P day-trade tickets**, none ever on a positions view. ③ Expected 8/14 cash $20,864.90 − $1,754.94 − $2,311.10 = **$16,798.86** vs actual $16,806.53 ⇒ **residual +$7.67** (hypothesis: mm dividend; same class as D-15's +$67.71, which has NO ledger row and stays a caveat). No subset sums to −$882.10 exactly; nearest is −$889.77 + $7.67. **Not carried forward as open.** D-12 also resolved: 687P liquidated 8/3 at +$2.81 ⇒ **−$839.18**.

## ⚠️ Two supplied claims about this file were wrong in one run — checked at the artifact, NOT written in
- **D-34** (packet rev 1): "NEW since 8/14: TLT 85P, TLT 82P, TBT, HBAN 16P, KRE Dec ×3" — all five were on the 8/14 mirror at identical qty/basis (and have no activity row 7/30–8/28). Nothing double-added; no entry-unknown annotations applied. n=2 with D-25.
- **D-41 (task item 3) — REFUTED, and I did NOT caveat the 8/14 header.** The premise "they were on the book at 8/14" is true; the conclusion "so the 8/14 capture was scrolled/cropped and its 21/21 claim needs a caveat" does not follow. The 8/14 mirror's 21 Fidelity rows enumerate as Longs 7 (AAPL, GLD, USO, APD, **TBT**, USO 135C, XLE) + TLT 3 (77P, **85P**, **82P**) + KRE 4 (Dec ×2, **Dec ×3 (M)**, Sep ×2, Aug-21 ×3) + WAL 2 + **OZK 2** + Other 3 (APO, **HBAN**, **KELYA**) = 21, MV $19,772.40 over exactly those rows. §③'s line "the OZK/KELYA puts were not on the 8/14 mirror either" is also wrong (8/14 lines 88, 89, 97). It was the 8/29 first read that missed them, not the 8/14 capture. Writing the requested caveat would have been the mirror-wrong error. Recorded as D-41 in PACKET-WRONG; header untouched. Process note: diff the capture against `FORGE/STATUS.md` rows, not SCRATCH's book line.

## Headline deltas vs 8/14
Fidelity total −$121.79 → $36,457.14 · cash **−$3,205.86** → $13,600.67 (now fully bridged) · positions MV +$2,361.49 · pending $722.58 (explained). Open G/L −$2,215.64 → +$314.31 is **not a rally** — the Aug-21 legs (−$2,507 open loss) left the open set; survivors ≈flat with offsets (AAPL +$14.44/sh, GLD +$6.14/sh vs **duration complex +$442 → −$282**; TLT 77P 0.20→0.04). The 8/14 $0.05 cluster re-priced up (APO 0.05→0.95) — consistent with D-21, labeled. Robinhood $102.85 → $414.81 (≈$360 inflow implied, hypothesis; no RH activity view). **Day-trade class realized ≈ −$1,813 since 8/3 (≈ −$4,080 since 7/20); the 8/24 broker liquidation of 77 sh at ≈$5.19 under strike cost ≈$400 vs Will's own 8/26 price** — recorded as fact, ungraded (no rail owned it).

## Discrepancy list — urgency-ranked (full text: `FORGE/STATUS.md` § Reconcile discrepancies (8/29))
**EXPIRING / DATED**
- **D-28 🔴 2 DTE — Robinhood QQQ $715P ×1 expires MONDAY 8/31.** Cost ≈$193.24; QQQ closed 716.43 ⇒ **$1.43 (0.2%) OTM**. No rail, intent unrecorded. ITM ⇒ long-put auto-exercise into short 100 QQQ (≈$71.5K) in a $415 account (labeled) — **the Fidelity 713C on 8/21–8/24 is the live precedent: exercise → forced $71,300 buy → broker liquidation under strike.** Owner: **Will, Monday pre-open.**
- **D-31 🟠 32 DTE — TLT 77P ×25 at $0.04 = 0.35× basis.** Gate text beside the number, not adjudicated: harvest "half at ≥3×" (10 ct owed ≥$0.33) far; GATE-TERRY-007 counter 0-of-5, 8/26 4.66 · 8/27 4.67 (your consumer read), registry's "NO-VERDICT if expiry beats the count". TERRY → Will.
- **D-32 🟠 20 DTE — WAL 67.5/70P** $0.15/$0.34, $49 of value; WAL 78.55 vs REG-T-02 as PROME context. REGINALD/Will.
- **D-33 🟡 32 DTE — Sep-30 cluster:** KRE 60P ×2 @ $0.01 has **no lapse ruling for this expiry**; XLE 65C −62.7%; TLT 85P flat. $778 value.
**RESOLVED BY THE ACTIVITY VIEW:** D-29 (QQQ chain dated) · D-30 ($722.58) · D-16 (+$7.67) · D-12 (−$839.18) · D-35 (USO 8/26) · D-36 (five Aug-21 expirations broker-confirmed, Fidelity realized −$2,816.72 incl. the 710P day-trade; VLY stays presumed — no RH activity) · D-19 (USO 135C bought 8/3) · D-38.
**ASK WILL:** D-17 🟠 STNG (also absent from the activity window) · D-20 🟡 T share / event contracts / $8.67 residue · D-1 🟡 AAPL sale now known to predate 7/30 · D-18 🟡 WAL 77.5P proceeds. **BOOK-CHANGED:** D-37 RH inflow. **CAVEATS:** D-21, D-40 (Friday closes read Saturday; no live fetch), D-42, D-15, D-14, D-27 retired. **D-10 ✅ resolved** (216461326 on the header).

## Task-list execution (rev 2)
(1) $722.58 → EXPLAINED in header + D-30 ✓ · (2) QQQ chain written from the ledger, share arithmetic verified ✓ · (3) **NOT executed as specified** — refuted at the artifact, recorded as D-41 instead (see above) · (4) D-16 subset test done, result +$7.67, not carried ✓ · (5) five Aug-21 expirations (KRE 60P, QQQ 710P, OZK 45P, OZK 42.5P, KELYA 7.5P) in the Event box as broker-confirmed EXPIRED with realized figures ✓; the thesis-table originals retained struck-through for continuity.

## Consumer-sweep verdict (rule 3): NO SWEEP OWED
`AGENTS/TERRY/scripts/positions_from_forge.py`: Longs `Mark 8/14`→`Mark 8/28` (prefix-bound, hardening #3); one new live stock row (QQQ, day-trade table); one new RH row (QQQ 715P, no Mark column ⇒ `unverified`); five new `~~` rows in the Event-boxes table (event_box class, withheld by design); six thesis/RH rows newly struck. No section/header renames, no new columns. **Post-edit: 18 live / 22 withheld (12 closed · 6 event_box · 4 unverified), no parse defects, rc=0, `--selftest` PASS.** Live rows match the transcription row-for-row. Footer PARSED-BY parenthetical updated. `FORGE/PORTFOLIO.md` untouched, FROZEN banner intact.
**Read-cap flag:** file is 44,538 B (was ~36K on 8/14) — over the 32,550 B read-whole cap if any boot protocol reads it whole. Hot/cold split is the owner's call; not restructured.

## Git
`git diff --stat FORGE/` → ` FORGE/STATUS.md | 193 +++…---` · 1 file changed, 110 insertions(+), 83 deletions(-). `git status -- FORGE/` → only ` M FORGE/STATUS.md`. Nothing staged. This packet is also uncommitted (commit alongside or trash once read — your call).

**Awaiting commit authorization.** On the go: `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md` from repo root; hash reported back from the verify line.
