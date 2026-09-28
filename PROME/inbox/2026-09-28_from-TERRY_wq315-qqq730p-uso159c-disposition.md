# TERRY → PROME · 2026-09-28 Mon · WQ-315 disposition read: QQQ $730P ×10 + USO $159C ×2 (Sep-30-2026, Fidelity)

**Spawn:** `prome-7f`, Tier 1, WQ-315 (Will's word, verbatim in the card header). **Card (full read, sources, mechanics):** `AGENTS/TERRY/setups/QQQ730P-USO159C_sep30-disposition_2026-09-28.md` (`MGMT-QQQ730P-USO159C-SEP30`). **`$0` moved · no order · no new trade proposed · no gate or threshold moved.** Recommendations only; orders are Will's.

## Verdicts

| | QQQ $730P ×10 | USO $159C ×2 |
|---|---|---|
| **Call** | **SELL all 10, today Mon 9/28, before 15:45 ET** | **SELL both, today Mon 9/28, before 15:45 ET** (low stakes) |
| **Hard deadline if held** | **Wed 9/30 15:00 ET** | **Wed 9/30 15:00 ET** (after the 10:30 EIA report) |
| Open status | Open at the 9/25 close (ANVIL, f39c70073). **UNVERIFIED since** | Same |
| Underlying, 10:53 ET (fetch.py) | QQQ **$732.18, −1.65%** ⇒ put **~0.3% OTM** | USO **$152.96, +3.12%** ⇒ call **4.0% OTM** |
| Option bid/ask (chain_fetch, yfinance) | 10:51 **2.23/2.24** · 10:53 **2.18/2.20**; vol 8,335, OI 46,907 | 10:51 **0.55/0.62** · 10:53 **0.58/0.67**; 12–14% wide |
| Worth if sold now (gross, at bid) | **≈$2,180–2,230** vs cost $2,486.63 (≈ −$257 to −$307 realized) | **≈$110–116** vs $921.33 (≈ −$805 to −$811) |
| Worth at expiry | $0 if QQQ ≥ $730; beats selling now only if QQQ ≤ ~$727.8 (model odds 29–36%, INFERRED) | $0 if USO ≤ $159; beats selling now only if USO ≥ ~$159.6 (odds 14–18%, INFERRED) |
| Root rule #6 | Red day ⇒ selling a put is the right side. **SELL: no break. HOLD = implicit re-buy of a put on a red day** | Green day ⇒ selling a call is the right side. **SELL: no break** |

⚠️ **Quote caveat that must travel:** one vendor (yfinance), screening grade. Option bid/ask lags spot by about 15 minutes (`DIRINC` fired at 10:53). Will reads Fidelity's own live bid before any order.

## Why

- **QQQ put:** it recovered from $1.30 (9/25c) to about $2.20 in one red session and is now within ~10% of cost. Holding from here equals buying a new 2-day, slightly-OTM put for $2,200, with no card, no invalidation and no thesis owner. **Book context (WQ-297 A):** this is **not a hedge of the oil bet**. It is a separate equity-down bet: about $330k of delta-adjusted short-QQQ (delta INFERRED) against ~$4.4k of held equity (AAPL/APD/VLO). **Counter-case stated:** BOND's 9/28 global sell-off read (30Y 5.55% intraday, HY 293bp) would pay the put if it continues; QQQ $725 at Wednesday's close ⇒ ~$5,000. If Will holds that view, the construction answer is a later tenor bought on a green day with a card (construction rule #16). That is not proposed here. A partial hold is a trim (root rule #7) and is Will's to choose only on his own view.
- **USO call:** about $110 remains. It adds oil-up exposure to a book that is already one oil bet and diversifies nothing. Holding it is a ~$110 lottery on the Wednesday 10:30 EIA print, and it is not a mistake of consequence either way.

## Wednesday mechanics (known vs inferred)

- **VERIFIED** (Fidelity published pages, read 9/26 for the WQ-302 cards): auto-exercise at ≥ $0.01 ITM. Do-Not-Exercise deadline is 16:15 ET (web) / 16:20 ET (Options Agreement). DNE forfeits an ITM option's value, so it is dominated. An IRA cannot sell short.
- **Consequence:** 10 ITM puts exercised with no shares = **short 1,000 QQQ (~$730k)** in an IRA that cannot hold it. 2 ITM calls exercised = **$31,800 cash** needed against **$17,512.69** held. **What Fidelity does, and when, is UNKNOWN** (D-60: four "OPTION LIQUIDATION" rows, each on its contract's own expiry day). A slightly-ITM QQQ put at Wednesday's close is exactly this case, so don't let it reach the close.
- **INFERRED:** the 16:00 ET last-trade time for expiring ETF options; the Traditional IRA account type; the call-side cash handling.

## Broker information Will must supply

1. Both lines are still open at ×10 and ×2 (Fidelity positions screen).
2. Any working orders on either contract, to avoid a double sale.
3. Fidelity's live bid/ask on each at order time.
4. Only if either line is held into Wednesday: one Fidelity call, folded into the WQ-302 / D-60 question — what time on expiry day Fidelity closes an ITM or near-ITM option itself in this IRA, and what it charges.
5. Low priority: confirm the account type and the per-contract commission (assumed $0.65).

**Untouched:** TLT $77P ×20 **HOLD to expiry** stands (WQ-168 ④ / WQ-217); KRE $60P Sep-30 ×2 **LAPSE** (WQ-168 ⑥).

**Inbox drain:** 1/1. REGINALD ROLL70-EXIT clause (d) CONCUR, logged `noted` in `board_log.tsv` (run 0-of-3 through 9/25; no card change) and moved to `processed/`. `inbox/WILL/` holds README only. BOARD scan: 21 action-line signals, all logged (boot.py).

---

```
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/setups/QQQ730P-USO159C_sep30-disposition_2026-09-28.md (new), AGENTS/TERRY/setups/INDEX.md, AGENTS/TERRY/STATUS.md, AGENTS/TERRY/board_log.tsv, AGENTS/TERRY/inbox/processed/2026-09-26_from-REGINALD_ROLL70-EXIT-clause-d-CONCUR.md (moved), this memo
RESULT: SELL both today, before 15:45 ET. QQQ 730P ×10 ≈$2,180–2,230 at bid vs cost $2,486.63; USO 159C ×2 ≈$110–116 vs $921.33. Selling is on the right side of root rule #6 for both (red day for the put, green day for the call); holding is the implicit re-buy. Hard deadline if held: Wed 9/30 15:00 ET. An ITM put at the close means −1,000 QQQ short, which an IRA cannot hold; Fidelity's action is UNKNOWN (D-60).
GAPS: Open status UNVERIFIED past the 9/25 close. Quotes are yfinance screening grade with a ~15-min option lag (DIRINC). No greeks; odds and delta are INFERRED. Fidelity's expiry-day liquidation time is UNKNOWN.
WILL_NEEDS: Two hold/sell calls: QQQ 730P (rec SELL today) and USO 159C (rec SELL today); hard deadline for both Wed 9/30 15:00 ET. Broker facts: lines still open ×10/×2 · any working orders · Fidelity live bid at order time · (only if held into Wednesday) Fidelity's expiry-day close time and fee for this IRA.
FOLLOW-UP: On Will's fill or hold word → record it on the card + FORGE (ANVIL). If either is held into Wed, TERRY re-reads quotes Wed before 15:00 ET.
```
