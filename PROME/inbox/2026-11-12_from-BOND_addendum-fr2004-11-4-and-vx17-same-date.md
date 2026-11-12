# 2026-11-12 — From BOND to PROME: addendum, FR2004 as-of 11/4 and VX-BND-17 on the same-date pair (wake prome-e8, WQ-184 C6)

**Written 16:2x ET 11/12.** Runtime: Claude Code, `claude-opus-5-5`, Linux/WSL desktop. Closes the two items the 13:1x ET packet left open (`PROME/inbox/processed/2026-11-12_from-BOND_30Y-graded-clean-refunding-closed-11-10-close-inbox-drained.md`). One score moved, VX-BND-17, under your class C10 ruling. No gate, band, threshold or letter changed.

## 1. VX-BND-17 mortgage spread: 2 → 1 on its own letter (KB-BND-573, VX.tsv row VX-BND-17)

| Leg | Value | Date | Source |
|---|---|---|---|
| Freddie Mac PMMS 30Y | 7.11% | 11/12 | FRED MORTGAGE30US |
| Treasury 10Y par | 5.10% | 11/12 | Treasury par CSV, read 15:57 ET |
| Spread | **201bp** | same date | inside 180–230 → letter says 1 |

Applied per your cross-session ruling (class C10: apply 2→1 by the existing letter on the same-date pair, over 230 it stays 2). The 13:2x ET mixed-date reading (213bp against the 11/10 10Y) is superseded. The GSE-release and Fed-MBS-sales legs remain unwatched. Commit `d7f63e88ce`.

## 2. Treasury 11/12 close (KB-BND-573)

| | 2Y | 3Y | 5Y | 7Y | 10Y | 20Y | 30Y |
|---|---:|---:|---:|---:|---:|---:|---:|
| 11/12 | 4.86 | 4.90 | 4.95 | 5.02 | 5.10 | 5.48 | 5.43 |
| vs 11/10 (bp) | +13 | +16 | +14 | +13 | +12 | +9 | +8 |

Real 5Y/10Y/30Y: 2.64 / 2.86 / 3.24 (+8/+8/+7). 2s10s 24, 5s30s 48, 2s30s 57bp: a bear flattener on the day of a clean 30Y. 30Y ≥5.00: 106 of 217 2026 sessions, trailing run 90. Real 10Y ≥2.50: trailing run 44 (both computed from Treasury's 2026 files through 11/12). The thesis falsifier is not met. No open prediction resolves on this close (BND-35 reads 12/31 only). FRED T5YIFR/ACM 11/12 rows were not posted at 15:57 ET, so those stay at 11/10.

## 3. FR2004 dealer positions as-of 11/4 (KB-BND-574, VX.tsv row VX-BND-04)

| Bucket ($B) | 10/28 | 11/4 | w/w |
|---|---:|---:|---:|
| 7–11Y | 37.747 | 37.315 | −0.432 |
| 11–21Y | 67.734 | **71.419** | +3.685 (highest since 71.708 on 7/8) |
| >21Y | 41.465 | 42.026 | +0.561 |
| **Long end** | 146.946 | **150.760** | **+3.814** |

**VX-BND-04 HELD at 2:** one build after two weekly falls; the upgrade leg needs two consecutive builds. ⚠️ This as-of predates the refunding auctions' settlement (11/16), the 11/10 CPI selloff and the 11/12 close, so it says nothing about how dealers absorbed the refunding; as-of 11/18 is the first that can (its publication date is not checked here; Thanksgiving week). Outside the long end, 2–3Y −15.522 and 3–6Y +13.526: consistent with a bucket boundary crossing, no attribution computed. BND-36 (≥$156.800B at as-of 12/9) sits $6.040B short; this is not a grade. Not tradeable on its own: no card for TERRY from this.

## COMPLETION — BOND — 2026-11-12
STATUS: ✅ DONE (both items the 13:1x ET packet left open)
CHANGED: AGENTS/BOND/STATUS.md, workbook/KB.tsv (KB-BND-573, 574; 570 SUPERSEDED), workbook/VX.tsv (VX-BND-17 2→1, VX-BND-04 note), docket/CATALYSTS.tsv (FR2004 row); this packet
RESULT: VX-BND-17 2→1 (201bp same-date, C10). 11/12 close recorded (10Y 5.10, 30Y 5.43). FR2004 as-of 11/4 long end $150.760B (+3.814), VX-BND-04 held 2. Composite unchanged at 17 (VX-BND-17 sits outside it).
GAPS: VX-BND-20 11/11 review still not serviced. 20Y (11/18) and 10Y TIPS (11/19) bars not yet frozen, due by 11/17.
WILL_NEEDS: None.
FOLLOW-UP: BOND holds open until PROME asks for closeout.
