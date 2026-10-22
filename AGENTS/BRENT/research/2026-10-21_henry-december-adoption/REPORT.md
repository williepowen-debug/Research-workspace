# BRENT — adoption of HENRY's December crack observations (WQ-386 / WQ-392 / WQ-420 common basis)

**Session:** 2026-10-21 21:30–21:36 ET, Will: "do the HENRY December measurement adoption now". **Packet consumed:** `inbox/2026-10-19_from-HENRY_december-measurement-proof.md` (HENRY `6474d8726`). **Read before deciding:** TRADE.md (whole) · the WQ-420 Approved exact insert (whole) · WQ-386 letter (TRADE reproduction) · TERRY `VLO-SHARE_management-proposal_2026-09-28.md` current state, §2-bis and missing-data table · HENRY `DATA.md`, `f1-calculations.json`, `f1-identity-f5.json`. **Not read:** TERRY's 110 KB parent card beyond the leg-A sections; SPECS_TRADE_RULES has no leg-A clause (grep). This is a **measurement publication, not a holding grade**. TERRY grades leg A, Will executes; no threshold, basis, scope or order changed. `$0` moved.

## Verdict

**ADOPTED, on the WQ-420 native-tick basis, for sessions 10/15, 10/16 and 10/19; extended by BRENT to 10/20 and 10/21.** All five are source-(3) ESTIMATES (14:28 + 14:29 ET bars, Close × Volume per leg, C3 = 42 × P_HO − P_CL). None is a CME settlement.

| Session | BRENT published C3 (native-tick, exact Decimal) | HENRY C3 (raw transport) | \|Δ\| | < $95 notice | < $90.16 exit | Margin to $95 | Near-line flags |
|---|---:|---:|---:|---|---|---:|---|
| 10/15 | **98.92125525772** | 98.92125482008 | 4.4e-7 | No | No | +3.921 | none |
| 10/16 | **99.45090729063** | 99.45090889319 | 1.6e-6 | No | No | +4.451 | none |
| 10/19 | **99.86566305180** | 99.86566445725 | 1.4e-6 | No | No | +4.866 | none |
| 10/20 | **100.17681945020** | — | — | No | No | +5.177 | none |
| 10/21 | **95.04790847983** | (HENRY STATUS: $95.05) | — | **No (by $0.048)** | No | **+0.048** | **inside ±$0.15 of $95**; $4.89 from $90.16 |

Display values are rounded only after the exact comparison. The machine records are `calculations.json` (transport values, compared with HENRY) and `normalized.json` (published basis).

**Leg inputs for 10/21:** HO 14:28 4.5758 × 1,304, 14:29 4.5755 × 885 ⇒ P_HO 4.575678...; CL 14:28 97.10 × 2,387, 14:29 97.16 × 2,484 ⇒ P_CL 97.130598... Minute closes 14:20–14:35 imply a crack range of about $94.8–95.1 (HENRY reports $94.82–95.09).

## Why adopted: what was checked

1. **Independent extraction, same vendor lineage.** BRENT pulled its own one-minute bars at 21:31 ET (`raw/`). For 10/15–10/19 every input bar (label, close, volume) matches HENRY's retained rows exactly (`input_match: true`). This is an independent pull of **one** vendor, not an independent source (LESSONS #1).
2. **Contract identity with a negative control:** `HOZ26.NYM` expireDate 2026-11-30, `CLZ26.NYM` 2026-11-20 (both NYM FUTURE USD, underlying HO/CL). The control `HOF27.NYM` returns 2026-12-31, a different date, so the resolver discriminates.
3. **Bar-label convention:** same-feed SPY has 390 regular bars from 09:30 to 15:59 on each of the five dates. Labels are bar-open times, so 14:28 and 14:29 cover [14:28, 14:30). The 14:30 bar is excluded.
4. **Both bars present, positive volume, on both legs, all five days.**
5. **Precision (WQ-420 ¶1, the one correction to HENRY).** WQ-420 says a transport artifact "may be normalized only to its verified published price". HENRY computed on raw float32 transport values; BRENT normalizes each close to its CME native tick (HO $0.0001/gal, CL $0.01/bbl, per TERRY's 10/19 primary read of CME rules 150102.C and 200102.C, **not re-read by BRENT**). A normalization is accepted only if the tick value round-trips exactly to the float32 value and both adjacent ticks do not; all 20 inputs pass. **Guard falsified:** off-tick values (HO 4.57585, CL 97.105) fail. Limit: the check cannot detect a wrongly assumed finer tick. Result: BRENT's 10/16 and 10/19 values reproduce **TERRY's graded values exactly** (99.4509072906, 99.8656630518). HENRY's values differ by ≤ $0.0000016, which decides nothing.
6. **Hierarchy.** Source (1), the CME settlement, was **not obtained**. CME's settlement service returned HTTP 403 "IP address is blocked ... use of scripts ... prohibited", and BRENT did not attempt to circumvent it (Will can read cmegroup.com by hand). Source (2), vendor daily rows, is **rejected**: `CLZ26` repeats 319,879 volume on 10/19 and 10/20, and the 10/21 rows are evening-session bars. This is the copy-forward/provisional signature the letter rejects; TERRY and HENRY rejected the same rows. Only source (3) remains.

## The 10/21 near-line case — stated plainly

- **On HELD-01 leg A's own letter (§2-bis):** the ±$0.15 UNKNOWN band attaches only to the **$90.16 exit**: "If only (3) is available within ±$0.15 of $90.16 ... UNKNOWN". At $95 the comparison is strict: **$95.0479 is not below $95**. On that letter the 10/21 observation is valid and gives **no notice and no exit**.
- **On the gate letter used for F1:** TERRY's missing-data table says "same band the gate letter uses at $95". HENRY's F1 applies ±$0.15 at $95, so **HENRY's F1 = UNKNOWN for 10/21** on HENRY's own rule. BRENT does not adjudicate HENRY's letter; it concurs that 10/21 sits inside that band.
- **Open question for TERRY (owner), not decided here:** whether the leg-A notice inherits the $95 near-line band. The literal §2-bis wording says no. The consequence is notice only, with no action, so nothing changes for the share either way.
- **Robustness of the margin:** the CL proxy, 97.1306, sits $0.019 below the reported 10/21 CL settle of $97.15 (secondary: The Nation; see the catch-up report). If HO settled at its window VWAP, C ≈ $95.03, still above. **With CL at $97.15, an HO settlement ≥ ~$0.0007/gal below the window VWAP (4.575678) would put the settlement below $95** (break-even HO = (95 + 97.15) / 42 = 4.575000). That is plausible and unmeasured. If anyone reads the CME 10/21 HOZ26/CLZ26 settlements, those govern under source order (1).

## What this publication is and is not

- **Is:** BRENT's owner-published December F1 readings for 10/15–10/21 on the common basis HENRY requested. HENRY may now treat common F1 as published for these sessions; 10/21 stays F1 UNKNOWN on HENRY's band rule.
- **Is not:** a TERRY holding grade; a replacement of TERRY's accepted 10/15 history (TERRY's 10/15 98.9213 and BRENT's 98.92125525772 agree); a CME settlement; authority for the two added VLO shares (scope UNKNOWN); a new monitor or threshold. Diesel strength is moving toward the notice line (100.18 on 10/20 → 95.05 on 10/21, −$5.13 in one session as HOZ26 fell ~13.8¢/gal). That is a fact about the instrument, not a sell signal; the exit line is $4.89 below.

Reproduce: `compute.py` (fresh-pull extraction plus comparison with HENRY), then `normalize.py` (WQ-420 native-tick basis). Both run under the project venv.
