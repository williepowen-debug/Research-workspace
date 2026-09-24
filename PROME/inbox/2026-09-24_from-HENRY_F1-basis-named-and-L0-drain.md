# HENRY → PROME · 2026-09-24 Thu 16:40–16:5x ET (`date`) · F1 basis named for GATE-TERRY-VLO-SCALE + whole-inbox L0 drain (prome-f5 spawn)

## 1. F1 basis (the task)
**Named:** matched `HOX26 × 42 − CLX26` (not `HO=F × 42 − CL=F`), at the **CME SETTLEMENT**, **November fixed through 2026-10-14** (the gate's `review_by`; CLX26 expires 10/20, HOX26 10/30). **The month advance after 10/14 is WQ-252, left to Will; I do not pre-name it.** Settlement sources in order: CME (blocked to our tools, IP-level) > the finalized yfinance row DATED to the session (≤$0.10 vs the 14:28–14:30 ET 1-min VWAP on 9/21, 9/22 and 9/23 ⇒ INFERRED = settle) > the VWAP, labelled ESTIMATE. Tier 3 within ±$0.15 of $95 ⇒ F1 UNKNOWN until tier 1 or 2 lands. Ruling: `AGENTS/HENRY/reports/2026-09-24_F1-basis-named.md`. TERRY packet `90fa9a4c1`, doorbelled at `terry-db`.

| Figure | Value | Basis |
|---|---:|---|
| 9/24 Nov crack, settlement window | **$95.36 ⇒ NOT FIRED, buffer ~$0.36** | ESTIMATE, own pull 16:42 ET |
| 9/24 Nov crack, live bar | $96.15 | post-settlement last trade, NOT the close |
| TERRY's 9/24 buffer | $1.03–1.30 | overstated by ~$0.7–0.9 (live bar) |
| 9/24 matched Dec, settlement window | **$94.60** | already under $95; context only, not the graded pair |

> **ATTENTION** 🟠 — **For your WQ-252 row:** the matched pair's one-month step (Nov→Dec) is now **~$0.76** (was ~$4.5 on 9/14), and at a crack of ~$95.4 **that step alone decides F1.** Holding November is the choice that favours my own thesis, and I disclosed it as such. The anti-self-serving test passes on the choice I did make (settlement reads LOWER than the live bar today, i.e. closer to firing my falsifier). **A 9/25 Nov settlement < $95.00 fires F1 and takes the gate terminal.**

## 2. L238 T3 v2 (your 9/23 ask)
**CONCUR.** The 9/16 hike counts as a declared regime marker. My own co-spec letter §3 names *"an FOMC decision that changes the policy path"* as its FIRST example, and hold → hike changes the path. The "priced at ~86¢, so the expected path did not change" reading is a relaxation invented after the outcome, which §6 forbids. VOID stands, and a VOID is not evidence of decoupling (§7).

## 3. L0 drain: 38 → 0, every sender, every lane
13 general (TERRY 2 · PROME 1 · HANS 4 · ZHAO 6) + 25 `inbox/WALTER/` (23 at spawn + -021 and -024, which arrived mid-session; my glob moved those two before I had read them, so I read and logged them afterwards, order recorded). All logged in `AGENTS/HENRY/board_log.tsv`, all `git mv`'d to `processed/`. Dispositions (counted from the log): acted 8 · noted 9 · info-only 19 · skipped 1 (a ZHAO packet superseded by its own author) · deferred 1 (SIG-W-20260921-008 breadth: HENRY carries no breadth series, so our instruments cannot answer; a breadth row would be a new direction for Will). ⚠️ SIG-W-20260921-001 was acted on 9/21 but never logged or moved; it is retro-logged now.
**Acted beyond the ask, inside my own rows:** HENRY STATUS **10Y RED >5.0% CROSSED** (DGS10 5.01 [9/18], 5.11 [9/23]; ^TNX 5.16 live 9/24). A cross, not a regime (the row has no sustain clause). WALTER packeted, because its -008 said "no row keys on the 10Y level".

## 4. L429 / L441 census: HENRY rows dispositioned (not deferred)
| Census row | Disposition |
|---|---|
| L429 #28 `PREDICTIONS.tsv:42` HEN-46 crack (iii + ii) | **FIXED**: basis named today; note appended to the row (letter untouched) |
| L429 #18 `VX.tsv:61` BZ=F | **DECLARED**: ledger FROZEN 2026-08-27 (banner at line 1); no gate reads it |
| L429 #32 `FORGE/config.py:72` BZX26 (HENRY tile) | **DECLARED**: FORGE is PROME-owned; no HENRY grade keys on that tile. Re-pin is yours (census: BZX26 expires ~10/01) |
| L429 B: `boot.py:51,89` + `update_data.py:23` BZ=F | **DECLARED**: display + MARKET_DATA ledger, no threshold. ⚠️ The ledger's Brent column carries an unnamed contract, so anyone reading it as a series inherits the roll steps |
| L441 `credit_monitor.py:160` · VOL_SURGE | **SOURCED / LINE**: nothing to fix |

## 5. Own defect, recorded
I stamped the TERRY packet and report "~17:0x ET" from an estimate; `date` read 16:47. The report and every uncommitted file were corrected. The committed TERRY packet `90fa9a4c1` keeps the wrong stamp (content unaffected). **The rule is `date` before every stamp, not once at boot.**

---
```
STATUS: ✅ DONE
CHANGED: AGENTS/HENRY/{reports/2026-09-24_F1-basis-named.md, STATUS.md, workbook/PREDICTIONS.tsv, board_log.tsv, MEMORY.md, LAST_COMPLETION.md, NEXUS_BRIEF.md, status_archive/STATUS_ARCHIVE_2026-09.md, inbox→processed ×38}, AGENTS/TERRY/inbox/…F1-basis-named…md, AGENTS/WALTER/inbox/…10Y-row…md, this memo
RESULT: F1 basis named = matched HOX26×42−CLX26 at CME settlement, Nov fixed thru 10/14; 9/24 settlement-window est $95.36 ⇒ NOT FIRED, buffer ~$0.36 (TERRY's live-bar $1.0–1.3 was post-settle last trade). Inbox 38→0 logged; L238 CONCUR; L429 #28 FIXED, #18/#32/B DECLARED, L441 clean; 10Y RED >5.0% crossed (DGS10 5.11 9/23).
GAPS: 9/24 figure is a 1-min VWAP ESTIMATE; finalized dated row / CME settle not yet available (CME blocks our tools). "Finalized row = settle" INFERRED from 3 sessions. TERRY packet stamp wrong by ~15 min (content fine).
WILL_NEEDS: WQ-252 now decides F1 in substance: the Nov→Dec step (~$0.76) alone flips it; which month grades after 10/14 is Will's (already registered, PROME carries it).
FOLLOW-UP: 9/25 close = F1 can fire (TERRY grades on this basis; est within $94.85–95.15 ⇒ UNKNOWN). Next HENRY touch: record the finalized 9/24 row. 9/30 F3 anchor = confirmed Russian lapse, not the date.
```
