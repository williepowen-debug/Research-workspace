# HEN-46 `F1` (and `F3`) — BASIS NAMED · 2026-09-24 Thu ~16:4x–17:0x ET (`date` wall clock)

**Owner:** HENRY (F1 is HEN-46's falsifier). **Asked by:** TERRY `7a8c291a0` (14:27) + `be312801d` (16:4x ADDENDUM). **Referent:** `PROME/GATES.tsv` `GATE-TERRY-VLO-SCALE` (WQ-282, Will 14:59 ET), "F1: ULSD crack close < $95, on the basis HENRY names". **Spawned by:** PROME `prome-f5`, Tier 1.
**Scope:** names a BASIS. No threshold moved ($95.00 stand-down / $90.16 thesis-dead unchanged), no score changed, no trade view, $0.

## 1. THE BASIS (answer)

| Leg | Named | NOT this |
|---|---|---|
| **Series** | **Named matched contracts: `HOX26 × 42 − CLX26`** (Nov heating oil vs Nov WTI, $/bbl) | `HO=F × 42 − CL=F` (continuous) |
| **Month** | **November, fixed, through 2026-10-14** (the gate's `review_by`). Both legs keep trading past that date: CLX26 expires 2026-10-20, HOX26 2026-10-30 (yfinance `expireDate`, pulled 16:42 ET) | Any month-advance rule. **What pair grades after 10/14 is WQ-252 (Will's call). I do not pre-name it.** |
| **Price** | **The session's CME SETTLEMENT** (the official close, struck in the 14:28–14:30 ET window) | A vendor daily bar read before it finalizes. That bar is a **post-settlement LAST TRADE**, not the close |
| **Session label** | The row whose DATE is the session. After ~18:00 ET the newest daily bar belongs to the NEXT session's evening trade (HEARTBEAT §2R / DOCKET L462). **Select by date, never "latest bar."** | "the last bar" |
| **Identity check, every pull** | `expireDate` on both legs + a negative control (`HOV26` ≠ `HOX26`) | — |

**Settlement sources, in order (a lower tier is used only when the tier above is unavailable, and it is labelled):**
1. **CME official settlement.** ⛔ Our tools cannot reach it: `cmegroup.com` settlements API returned an IP block (scraping ToU), 2026-09-24 16:4x. **Will can read it on the CME site; an LLM cannot.**
2. **The vendor (yfinance) daily-bar row dated to the session, once FINALIZED.** On the three finalized sessions I could test, that row tracked the settlement window to ≤$0.10 (table §2). ⇒ **INFERRED that the finalized row IS the settlement.** Finalization test: the dated row sits within $0.15 of the §3 VWAP estimate. A row that still equals the latest intraday tick is NOT final.
3. **ESTIMATE: 1-minute VWAP of each leg over 14:28–14:30 ET**, crack computed from the two VWAPs. Labelled ESTIMATE.

**Near-line rule (a basis procedure, not a threshold):** if only tier 3 is available and it sits within **±$0.15** of $95.00 (the tier-2 validation error plus margin), F1 is **UNKNOWN** for that session until tier 1 or 2 lands. It is held, never skipped, per the letter ("a missing vendor bar is graded on a labelled substitute or held UNKNOWN, never skipped"). ⚠️ Under the letter's `AND NOT F1`, an UNKNOWN F1 blocks a fire the same way a fired F1 does. It delays terminality; it cannot enable an add.

## 2. WHY — and which way each choice cuts against my own thesis

**Matched, not continuous: this is the letter's own history, not a fix I chose.** My 9/14 roll correction (PREDICTIONS.tsv HEN-46, notes) verified that the crack series was **calendar-matched at every observation F1 was calibrated on**, including the $90.16 baseline (7/23) and the $109.93 peak (9/10). It went mismatched only on 9/14. A mismatched pair (e.g. Dec heating oil vs Nov crude) is not the refining margin of any delivery month. So naming "matched" keeps the calibration basis; it does not change it. It also matches the registered default in the GATES cell ("matched front-winter contracts, currently HOX26×42 − CLX26").

**Settlement, not the live bar: this is the choice I actually made, and today it cuts AGAINST HEN-46.**

| Session | Finalized vendor row (crack) | 14:28–14:30 ET 1-min VWAP crack | Δ | Post-settle last trade ~17:00 ET (crack) |
|---|---:|---:|---:|---:|
| 9/21 Nov | 105.34 | 105.38 | −0.04 | 105.27 *(HO 4.6963 · CL 91.97)* |
| 9/22 Nov | 109.49 | 109.58 | −0.09 | 108.26 *(HO 4.717 · CL 89.85)* |
| 9/23 Nov | 102.45 | 102.50 | −0.05 | 104.10 *(HO 4.686 · CL 92.71)* |
| **9/24 Nov** | **not final** — live 96.15 at 16:42 (HO 4.5523 · CL 95.05) | **95.36** (HO 4.5244 · CL 94.6678) | — | (session still trading) |
| 9/24 Dec *(context only, not the graded pair)* | not final — 95.47 live | **94.60** (HO 4.4177 · CL 90.9422) | — | — |

*Source: own yfinance pull, `auto_adjust=False`, 16:42 ET 2026-09-24, before 18:00 ⇒ the 9/24 rows are the 9/24 session. VWAP = Σ(close×volume)/Σ(volume) over the 14:28 and 14:29 1-minute bars; yfinance volume, so it approximates CME's settlement method and does not reproduce it exactly.*

- Across 9/21–9/23 the post-settle last trade differed from the finalized close by **−$0.07, −$1.23 and +$1.65**, so both size and sign vary. **A pull taken at ~16:3x ET is not the close.** That is why TERRY's two pulls moved (96.03 → 96.30): the market was still trading after the settlement.
- **9/24 on the named basis: NOT FIRED — ESTIMATE $95.36, buffer ~$0.36** (tier 3; outside the ±$0.15 band, so it is gradeable, provisional until the finalized row lands). **TERRY's $1.03–1.30 buffer overstates it by ~$0.7–0.9.** Thesis-dead $90.16: buffer ~$5.20.
- **The direction is disclosed because it is the test of the choice:** today settlement reads LOWER than the live bar, i.e. closer to firing my own falsifier. The anti-self-serving test passes. It could run the other way on another day; the choice is made on definition ("close" on a futures contract = settlement, the same rule RED set for Brent on 8/12 and that my `boot.py` N5 guard already carries), not on which side it lands.

**Fixed November through 10/14: disclosed as the one choice that currently cuts IN my favour.** On the same settlement window, matched **December read $94.60, already under $95.** A basis that advanced to December today would have fired F1 on 9/24. I am not advancing it. Nov is the registered default and the front month on both legs, and the gate's life ends 10/14. **But Will should see this fact for WQ-252:** the third roll form (a matched pair stepping down one calendar month) is now about **$0.76** (Nov−Dec, 9/24 settlement window). That is enough to decide F1 on its own. On 9/14 it was ~$4.5. The step has narrowed a lot as the curve flattened, but at this level it still decides the grade.

## 3. What this does NOT decide
- **WQ-252** (the letter-design question: which month after a roll, whether to widen the separation, whether to move to a roll-adjusted series). Still Will's, still at HEN-46's resolution or a convened session. Nothing here pre-empts it.
- **Any VLO rec.** TERRY grades; Will decides. $0.
- **F3** (Russian ban lapse 9/30 + crack < $95 within 10 sessions) grades on **this same basis**. Its window (9/30→10/14) sits inside the fixed-November span. ⚠️ SIG-W-20260921-002/-019: Russia is reported *set to extend* the diesel ban (not decreed). If extended, F3's first leg does not start.

## 4. Confidence tokens
- Contract identity, expiries, 9/21–9/24 bars: **VERIFIED** (own pull).
- "The finalized vendor row = CME settlement": **INFERRED** (3/3 sessions within $0.10 of the settlement window; not checked against CME, which blocks us).
- 9/24 settlement $95.36: **ESTIMATE** (tier 3). Re-read the dated 9/24 row once it finalizes (next morning) and record it.
