# HEN-46 `F3` — BASIS STATED + LEG 1 GRADED · 2026-09-30 Wed 08:04–08:1x ET (`date`)

**Owner:** HENRY (F3 is HEN-46's falsifier). **Asked by:** PROME `prome-f4`, DOCKET L385 (Tier 1, WQ-184 driver). **Consumers informed:** TERRY (construction, matched-basis check at fire-time), BRENT.
**Scope:** a BASIS DISCLOSURE on a frozen letter + a grade of its first leg. ⛔ No letter re-specced, no threshold moved ($95.00 / $90.16 unchanged), no confidence re-marked, no trade view, $0.

**The letter, as written (PREDICTIONS.tsv HEN-46):** *"F3 Russian product-export ban lapses 9/30 without extension AND crack < $95 within 10 sessions."*

## 1. LEG 1 — did the ban lapse? **NO. Russia extended it to 2026-10-31. F3 leg 1 NOT MET ⇒ F3 NOT FIRED; the 10-session clock does not start.**

| Source | Tier | What it says | Read |
|---|---|---|---|
| Rigzone wire (Bloomberg News), 2026-09-30 06:01 ET | named SECONDARY | Government extended the ban on most diesel exports, bunker fuel and gasoils to **Oct 31**; quote: *"to support stability of the domestic fuel market, also taking into account higher demand for motor fuels during the harvesting season"* | 08:1x ET |
| The Moscow Times, 2026-09-30 | named SECONDARY (cites a "government press release", no decree number) | Producer diesel ban → **Oct 31**; non-producer diesel ban through January; jet fuel through November; gasoline through January | 08:1x ET |
| government.ru (the PRIMARY) | — | **UNREACHABLE** from our tools (fetch failed 08:1x ET). No decree number read. | Will can read it; an LLM here could not |

**Grade: NOT MET on two independent named secondaries (Bloomberg; Moscow Times citing the government release). Confidence token: INFERRED (not read at the primary).** This matches the 9/21 WALTER relays (SIG-W-20260921-002/-019, "set to extend") and supersedes their "not decreed" caveat at secondary strength only.

### ⚖️ The one letter-meaning question this creates — NAMED, NOT DECIDED (Will's)
The letter keys leg 1 to **"lapses 9/30 without extension."** It was extended. Two readings:
- **(a) As written:** F3 is a single-date conditional. The 9/30 expiry passed with an extension ⇒ F3 is **spent — NOT FIRED, closed**. A lapse on 10/31 is not the event the letter names.
- **(b) The DOCKET L385 anchor-type reading:** leg 1 is a *policy-expiry* event, "extendable, early or partial", and the 10-session clock starts from a *confirmed lapse at a primary*. On that reading F3 **re-arms at the next expiry (10/31)** and its window would run from a confirmed lapse into November — **after** the fixed-November basis (10/14) and after the 10/6 sitting, and on a different contract month.
- **Reading (b) changes what the letter measures** (a different date, a different window, a different contract month), so choosing it is a letter change. **HENRY does not choose. I grade on (a), as written, and name (b) as a Will decision** — natural home: the WQ-252 sitting (DOCKET L471, 10/6), which already owns the post-10/14 month. **Which way (b) cuts:** it keeps a falsifier of my own thesis alive longer, so it is the reading that is *less* favourable to HEN-46; (a) retires a falsifier. Disclosed because the conflicted party is the one grading.

## 2. THE BASIS F3 GRADES ON (the L385 ask)

| Leg | F3 basis (identical to F1's, `reports/2026-09-24_F1-basis-named.md`) |
|---|---|
| **Series** | **Named matched contracts `HOX26 × 42 − CLX26`** ($/bbl, November ULSD vs November WTI). **NOT** the continuous `HO=F × 42 − CL=F`. |
| **Month** | **November, fixed, through 2026-10-14** (WQ-252: HENRY's basis governs until the sitting rules). |
| **Price** | CME **settlement** per session; tier ladder unchanged (1 CME official — blocked to our tools · 2 finalized vendor daily row dated to the session · 3 14:28–14:30 ET 1-min VWAP ESTIMATE, ±$0.15 near-line ⇒ UNKNOWN). |
| **Session label** | Select the row by DATE; after ~18:00 ET the newest daily bar is the NEXT session (DOCKET L462). |
| **Identity check, every pull** | `expireDate` on both legs **+ a negative control** (a different month must return a different value). |
| **Sessions after 10/14** | Grade on whatever month the **10/6 sitting (L471)** rules. **If it has not ruled, the cell is UNKNOWN, never graded on November by default and never on December by default.** Under reading (a) this is moot — F3 is spent. |

### The 10/14 HO roll inside F3's own window — how it is handled
- **It does not touch the named-contract basis.** `HOX26` trades to 2026-10-30 and `CLX26` to 2026-10-20 (`expireDate`, pulled 08:05 ET today). A volume roll of the continuous `HO=F` onto `HOZ26` (expected ~mid-October, lead variable) changes what `HO=F` *means*; it does not change `HOX26`. **Named contracts are immune to the continuous roll by construction — that is why the basis is named.**
- **The hazard is only live for anyone reading the continuous tickers.** Any sub-$95 print on `HO=F × 42 − CL=F` must be re-read on the matched pair before it is called (L384/L385/L386 test: matched months + negative control).
- **The real 10/14 boundary is the basis expiry, not the roll:** after 10/14 the month is the sitting's choice (row above).

## 3. NEW MEASUREMENT — the vendor's continuous history is RE-STITCHED (strengthens L386; applies to F1 as well)

Today's pull (08:05–08:07 ET, yfinance, `auto_adjust=False`):

| Date | `HO=F` row today | `HOV26` (Oct) | `HOX26` (Nov) | HENRY's recorded `HO=F` on the day |
|---|---:|---:|---:|---:|
| 9/14 | **4.9615** | **4.9615** | 4.7553 | **4.7526** (PREDICTIONS.tsv 9/14 F1 grade) |
| 9/22 | 4.9421 | 4.9421 | 4.7621 | — |
| 9/29 | **4.8979** | **4.8979** | 4.5100 | — |
| 9/30 (live) | 4.7386 | 5.0900 (expiry day) | **4.7386** | — |

- **Every `HO=F` daily row 9/10 → 9/29 now equals `HOV26` exactly, and the 9/30 row equals `HOX26`**, while `HO=F`'s metadata `expireDate` reads **2026-10-30 (November)**. On 9/14 HENRY recorded `HO=F` = 4.7526 — within 0.3¢ of `HOX26`, $0.21 from today's `HO=F` row for the same date.
- ⇒ **A continuous-ticker row's contract identity changed between pulls (VERIFIED for today's pull; the 9/14 value is from the record).** The metadata `expireDate` describes the ticker *now*, never a historical row. **A continuous-series figure cannot be reproduced from a later continuous pull.** The negative control passes (V ≠ X ≠ Z on every date).
- **Size of the artefact on the continuous crack, 9/29:** `HO=F×42 − CL=F` = **$116.33** (Oct HO vs Nov CL) vs matched Nov **$100.04** ⇒ **$16.29 of pure roll.** Anyone quoting "crack $116" for 9/29 is quoting an expiring-October squeeze.

## 4. The crack on the named basis (context — F3 is not armed; F1 grades on the same pair)

| Session | `HOX26` | `CLX26` | **Nov crack** | Dec crack (context, not graded) | Basis |
|---|---:|---:|---:|---:|---|
| 9/25 | 4.4621 | 92.41 | 94.998 | 95.023 | finalized row (tier 2) — F1 FIRED 9/25, recorded 9/28 |
| 9/28 | 4.4953 | 92.60 | 96.203 | 94.450 | finalized row (tier 2) |
| **9/29** | **4.5100** | **89.38** | **100.04** | 94.707 | finalized row (tier 2); CLX26 89.38 = the squawk-relayed WTI settle (SIG-W-20260929-012) |
| 9/30 **LIVE 08:05 ET** | 4.7386 | 90.78 | 108.24 | 101.82 | ⚠️ overnight/day-session trade, **NOT a settle, not gradeable** |

- **F1 9/29: NOT FIRED — $100.04, buffer $5.04** (tier 2, INFERRED = settle). Thesis-dead $90.16 buffer $9.88.
- 🟡 **`HOX26` +22.9¢ (+5.1%) overnight** (4.51 → 4.74; 30-min volume ×2–4 at 07:00–07:30 ET). **Co-timed with, not attributed to, the ban extension** — the move began ~03:30 ET, before the 06:01 ET Bloomberg item. Cause UNESTABLISHED.

## 5. Confidence tokens
- Ban extended to 10/31: **INFERRED** (two named secondaries; primary unreachable).
- Contract identities, expiries, bars: **VERIFIED** (own pull + negative control).
- Finalized row = CME settlement: **INFERRED** (unchanged from 9/24/9/28 validation).
- Continuous re-stitch: **VERIFIED** for today's pull vs HENRY's recorded 9/14 figure.

## 6. CORRECTION — 2026-09-30 08:15 ET (`date`), on TERRY's read, verified at the vendor
The §4 label "finalized row (tier 2)" for **9/29** is WRONG: the 9/29 daily rows carry **9/28's exact volume on both legs** (HOX26 63,292 · CLX26 370,326) — a copy-forward signature — and the finalization test (§1 of the 9/24 basis report) was not run. **Relabel: tier 2 NOT ESTABLISHED.** The figure ($100.04) agrees with TERRY's tier-3 grade; **F1 9/29 NOT FIRED is unchanged** (buffer ~$5, outside the ±$0.15 band). The 9/25 and 9/28 rows keep their earlier labels (not re-tested here).
