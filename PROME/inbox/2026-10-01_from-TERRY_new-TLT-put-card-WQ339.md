# TERRY → PROME · 2026-10-01 21:1x ET · spawn `prome-e4` · WQ-339: the new TLT-put card

**Card:** `TRY-COND-TLTPUT-WQ339` — `AGENTS/TERRY/setups/TLT_dec18-77P-x2_new-duration-put_WQ339_2026-10-01.md` (commit `4010e7ad6`). **CONDITIONAL. A recommendation only: no order, no fill, no [Approve] implied.**

## The card in one paragraph
Buy **2 TLT Dec-18-2026 $77 puts** (strike = at or just below TLT at the fill), limit **≤ $2.45 each, ≤ $491.30 total** (≈ **$417.30** at tonight's after-hours vendor asks), on the **first session from Fri 10/02 09:45 ET to Wed 10/14 15:00 ET on which TLT is green and TBT red at the moment of the fill**, TLT ≥ $74.50, no official DGS10 close < 4.50 before it. Harvest 1 of 2 at ≥3× the fees-in basis (needs TLT ≈ $71, −8.6% — a tail); sell-or-roll both by Wed 11/18 15:00 ET. 78 DTE (inside the 60–90 band; a strike/expiry change is a new deployment, construction rule #21).

## The seven packet requirements — where each sits on the card
| # | Requirement | Card § | Met? |
|---|---|---|---|
| 1 | BOND's kill MET + exit rec, stated not argued | §1 | ✅ — "it does not square, it overrides"; also: no registered trigger licenses the card (6/26 rule) |
| 2 | Complete dated book under WQ-357 A/B/C, with/without the card | §3 | ✅ — A+card ≈ $417 at risk / ≈ $6.9k TLT-equiv (84% of today's direction re-bought); C+card ≈ $1,259 / ≈ $15.1k (an add, ≈1.8×) |
| 3 | TLT-green entry, dividend-neutral, ex-date verified | §2, §4 E-3 | ✅ — see below |
| 4 | Size against the SLEEVE (WQ-297 A) | §6 | ✅ — oil book $6,379.20 + duration; N_eff = 1 |
| 5 | Standing guards (harvest-half ≥3× · DGS10 <4.50 · no red-tape entry) | §4, §6 | ✅ — ⚠️ the *"multi-session red tape"* phrase is SEARCH-NOT-FOUND in the current ACTIVE_DECISIONS cell; encoded from card 004's 7/16→7/17 precedent |
| 6 | Entry rule that survives payrolls | §4 | ✅ — a colour-at-fill rule, no level |
| 7 | After-hours marks disclosed; Fidelity governs | header, §8 | ✅ |

## Verified vs inferred
**VERIFIED (at the artifact / instrument):**
- TLT ex-distribution **Thu 10/1, $0.311581** (declared 9/30, pay 10/6) — Nasdaq dividend-history API, read 20:59 ET. IEF ($0.306924) and SHY ($0.241001) also ex 10/1. TBT none (last ex 9/23).
- **10/1 dividend-neutral day colour: TLT +0.31%** (price −0.09%, $77.78 → $77.71 vendor closes); TBT −0.71% ⇒ index **+0.35%**; IEF +0.33%; SHY +0.17%. **Green for long bonds.** First green after seven straight red sessions (9/22–9/30, −4.9%). Recovered ≈ 6% of that drop.
- Official Treasury curve 10/1 vs 9/30: 2Y −10bp, 10Y 5.29→5.24, 30Y 5.64→5.61 — front-led bull steepener (home.treasury.gov CSV, 20:59 ET).
- BOND state at the artifacts (BOND dark): `kill=MET-REC@2026-10-01; posture=HOLD-NO-ADD`; add DECLINED (WQ-280); re-arm spent on 004.
- Chain: TLT Dec-18 77P bid/ask 2.05/2.08, IV 16.97%, OI 35,396, quote sanity clean (`chain_fetch.py --no-cache` 21:00 ET) — **screening only**.
**INFERRED / MODEL:** Greeks and scenario P/L (Black–Scholes, flat IV); next TLT ex-date ~Mon 11/2 (monthly pattern, not declared); realized vol 10–11% vs 17% implied (vendor bars).

## Interactions PROME should know
- **USO $150C Oct-09 exercise headroom:** $524.70 today [10/1 pc]; this card alone leaves ≈ $107. If WQ-357 A executes the same day, sell first, then buy (≈ +$841 proceeds).
- On a green Friday the WQ-357 exit is the measured break already on the exit card and this card may fill; on a red Friday the exit is clean and this card waits.

## COMPLETION — TERRY — 2026-10-01
STATUS: ✅ DONE (card drafted and committed; preparation only)
CHANGED: AGENTS/TERRY/setups/TLT_dec18-77P-x2_new-duration-put_WQ339_2026-10-01.md (new) · setups/INDEX.md · STATUS.md · MEMORY.md · board_log.tsv · inbox packet → processed/ · this memo
RESULT: TRY-COND-TLTPUT-WQ339 = TLT Dec-18 $77P ×2, ≤ $491.30 (≈ $417.30 at 10/1 after-hours asks), green-day entry 10/02 09:45 → 10/14 15:00 ET, all seven packet requirements on its face. 10/1 measured: TLT ex $0.311581 ⇒ −0.09% price but +0.31% dividend-neutral (TBT implies +0.35%) — Will's "recovered somewhat" is true and small.
GAPS: Fidelity chain unseen (all marks vendor after-hours); distribution from Nasdaq only (iShares page not checked); "multi-session red tape" guard text SEARCH-NOT-FOUND in ACTIVE_DECISIONS, encoded from card 004 precedent; BOND (dark) has no re-entry-after-kill view on file; SETUPS/TRADE_BOOK rows not written (rotate tier, owed by 10/05)
WILL_NEEDS: ⚖️ Approve or reject: buy 2 TLT Dec-18 $77 puts for about $417 (cap $491), only on the first session from Fri 10/02 09:45 to Wed 10/14 on which TLT is up on the day at the fill, harvest one at 3×, sell-or-roll by 11/18. ⚠️ Caveat most likely to change it: BOND's pre-registered kill fired on 10/1 and BOND recommends exiting duration shorts — this card bets the other way on no registered trigger, and with WQ-357 A it re-buys ~84% of the direction the kill said to drop.
FOLLOW-UP: PROME registers the card's [Approve] row (WQ-339 closes on it) · re-read the sleeve from the mirror after Friday's fills · TERRY records the ruling on the card/INDEX (root rule #10)
