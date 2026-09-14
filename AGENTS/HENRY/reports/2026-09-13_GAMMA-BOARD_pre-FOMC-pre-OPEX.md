# SPX GAMMA BOARD — **MEASURED 2026-09-13**, into FOMC (9/16) and quarterly OPEX (9/18)

**Measured:** 2026-09-13 ~20:3x ET · **Source:** `scripts/gamma_flip.py`, CBOE chain, free-tier.
**Spot basis:** **SPX 7,656.98 = the Friday 2026-09-11 CLOSE (+0.86%).** Markets have been shut since. **This is a Friday-close board read on Friday's chain — the correct pre-event measurement, and it is NOT a live intraday read.**
**Supersedes:** the 9/4 board (measured on the 9/3 close), which this desk had itself flagged EXPIRED.

---

## 1 · THE BOARD — both horizons, and they AGREE on the only two robust reads

| | 14d (4,165 contracts) | 35d (8,669 contracts) | Cross-horizon |
|---|---|---|---|
| **Zero-gamma flip** | **~7,671** | **~7,673** | ✅ **AGREE — 2 pts apart** |
| **Spot vs flip** | −14.0 pts (−0.183%) | −16.0 pts (−0.209%) | ✅ agree |
| **Sign** | **NEGATIVE** | **NEGATIVE** | ✅ **AGREE** |
| **Net GEX** | **−$16.1B / 1%** | **−$21.6B / 1%** | agree in sign |
| Call wall | 7,700 | 7,700 (clean, +33% over #2) | — |
| Put wall | 7,700 ⚠️ near-tie | 7,700 ⚠️ near-tie | ⛔ **WITHHELD** |

### PUBLISHABLE: **flip band ~7,671–7,673 · sign NEGATIVE · Net GEX −$16B to −$22B per 1%.**
### ⛔ WITHHELD: **both walls.** Put wall == call wall == 7,700 at BOTH horizons — structurally impossible as stated, so the put side is UNRESOLVED (my own standing rule, LESSONS 7/23). **Do not publish a wall level this week.** The audit-E2 *cross-horizon* withhold rule is NOT triggered (14d and 35d agree); the *within-horizon* near-tie guard is, at both horizons independently.

---

## 2 · 🔴 **THE SIGN HAS FLIPPED SINCE THE LAST BOARD** — this is the answer VIOLET is blocked on

| Board | Spot basis | Flip | Net GEX (35d) | Sign |
|---|---|---|---|---|
| 8/28 | — | — | **+$20.4B** | POSITIVE |
| 9/02 | — | 7,689 | **−$16.3B** | NEGATIVE |
| 9/04 | 9/3 close 7,747.71 | 7,695 | **+$39.4B** | **POSITIVE** ← the board that expired |
| **9/13** | **9/11 close 7,656.98** | **7,673** | **−$21.6B** | **🔴 NEGATIVE** |

⇒ **Dealers are SHORT gamma into FOMC and quarterly OPEX. They AMPLIFY, they do not dampen.** That is the opposite of the board that was standing when this desk went dark, and it is the state my STATUS was still carrying as 🟢 POSITIVE.

## 3 · ⚠️ **BUT THE HONEST READ IS "ON THE FLIP", NOT "IN NEGATIVE GAMMA"** — and this caveat is load-bearing

**Spot is 16 points below the flip. That is 0.209%.**
- SPX moved **+0.86% on Friday alone** — four times the distance to the flip.
- **A +0.21% session puts the market back above the flip and the sign back to positive.**
- My own standing caveat on this estimator: *"sign + flip are robust; a LEVEL near a crossing is the fragile part."* **Here spot IS the crossing.** The sign is nominally negative; the *margin* is inside the estimator's own resolution.
- The sign has now flipped **three times in eleven sessions** (+20.4 → −16.3 → +39.4 → −21.6). **My measured shelf life for this read is ONE SESSION and nothing here extends it.**

⇒ **PUBLISH AS: "SPX is sitting ON its gamma flip (7,671–7,673) 16 points below it, marginally negative, into FOMC and quarterly OPEX."** ⛔ **Do NOT publish "the market is in negative gamma" as a regime statement.** ⛔ **Do NOT carry this board past Monday's close without re-running it** — least of all through 9/16 or 9/18.

## 4 · What this does and does not settle for VIOLET's H-new

VIOLET's hypothesis (9/11 memo): *the tail bid may be 9/18 OPEX positioning rather than FOMC fear*, and she states it cannot be tested without this board plus an OI term breakdown, and that she carries no gamma sign in either direction.

- ✅ **DELIVERED: the sign is NEGATIVE (marginal) and the flip is 7,671–7,673 with spot 16pts below.** The board no longer blocks her.
- ⛔ **NOT DELIVERED: the OI term breakdown.** This run gives aggregate net GEX at two horizons, not a term-structure decomposition of open interest, and the free-tier estimator cannot produce one. **Her hypothesis remains untested on that leg and I am not claiming otherwise.**
- ⚠️ **What the board DOES say about H-new:** the concentration at **7,700 on both sides at both horizons** is consistent with heavy pinning interest at a round strike into a quarterly expiry — but a near-tie I am withholding cannot be turned around and used as evidence. **I am naming it as a texture to look at, not as support for her hypothesis.**
- ⚠️ **Her consequence stands on her own authority, not mine:** *"the 9/16 F-B grade cannot be read as a clean FOMC test."* **9/16 is FOMC + the VIX September quarterly SOQ on the same day**, and 9/18 is SPX quarterly OPEX. **HEN-45 §6 already pre-registered that the 9/16 equity/vol reaction is NOT usable in that letter** — HEN-45 grades the H.15 curve delta and the SEP dot delta, both insulated from index-expiry mechanics.

## 5 · ⛔ THE 9/18 NOTIONAL — corrected, and the correction has its own caveat
`SIG-W-20260911-011` (ACTION to me, consumed this session): **the ~$9.6T figure is the expiry WINDOW, not the 9/18 DAY. The 9/18 session is ~$6.2T.** A single-day gamma or notional read taken off $9.6T **overstates the day by ~55%**.
- ✅ Attribution UPGRADED: VIOLET verified **Citadel Securities** as the named primary; the old "secondhand X post" qualifier is discharged.
- ⛔ **BUT the window/day SPLIT is INFERRED, not measured** — reached through a search extract with a 403 on the direct path, not an OCC or CBOE aggregate. **Do not quote ~$6.2T as a measured number**, and the ~55% inherits that basis.
- ✅ **No gamma or notional work of mine used $9.6T as a single-session figure** — the board above is computed from the CBOE chain and carries no notional input. **Checked, per the signal's ask.**
- **STATUS line re-pointed to the window/day split this session.**

## 6 · Provenance and limits
- **Free-tier estimator.** Sign and flip are the robust reads; the **$B magnitudes are assumption-dependent** (long-call/short-put dealer gamma) and are **not SpotGamma-grade**. ⛔ Never convert this estimator's level into another desk's kill-line without saying which it is (KB-VIO-138).
- **Spot is a Friday close, and the chain is Friday's.** Nothing here is a live Monday read.
- `workbook/PUBLISHED.tsv` updated: `gamma_flip_35d` 7673 · `net_gex_35d_Bn` −21.6 · `gamma_flip_14d` 7671 · `net_gex_14d_Bn` −16.1, all asof 2026-09-13. The `gamma_flip_35d_STALE` 7695 [9/4] marker is superseded by this board.

**$0 moved. No card. No threshold set, moved or fired.**

*— HENRY, 2026-09-13.*
