# BOND — Run Receipt

**Run:** 2026-07-28 ~14:25–14:50 ET · **PROME-spawned, teams-mode** · scoped task: **grade the 1:00PM 7Y auction against the frozen pre-registration**
**Mode:** live-event override — analysis + STATUS/SCRATCH non-negotiable, remaining write-back compressed.
**Prior run this same day:** ~02:50–06:00 ET (5-day-dark boot + 12-item mail drain + Will-tasked file-by-file review + FR2004 root-cause fix). That receipt is superseded here; its content survives in git and in `SCRATCH.md` history.
**Mail state at close:** general inbox **EMPTY** · WALTER lane **EMPTY** · outbox **+1** (PROME).

---

## 1. Task disposition

| # | Tasked | Status |
|---|---|---|
| 1 | Pull the **official** 7Y result from TreasuryDirect (primary, not headlines/trackers) | ✅ TA_WS `/securities/Note` + `/securities/auctioned`, **CUSIP 91282CRC7**, pulled ~14:30 ET. TD `updatedTimestamp` **2026-07-28T13:03:18**; competitive results `R_20260728_2.pdf`. **No secondary source used for any graded figure.** |
| 2 | Grade the FROZEN pre-registration **exactly as frozen** (§4, `BND-13`) — no spec edits | ✅ **Branch B (POLICY-PATH HOLDS). BND-13 → TRUE.** §4 not edited. A/C/D and the tie-break all graded and recorded. |
| 3 | **Also** report the indirect leg **standalone** vs both 56.4% and the 15th-pctile rule; **no cross-denominator porting**; report disagreement, don't average | ✅ **NO DISAGREEMENT.** Fails to fire vs the frozen min **56.42%** (by 13.73pp) and vs the looser **15th pctile 57.24%** (by 12.91pp). ⚠️ 57.24% **recomputed inside the of-competitive-accepted denominator** — the backtest's of-offering numbers were **not** ported (~05:15 amendment honoured). |
| 4 | Grade against the composition-keyed hypothesis set incl. the **third** hypothesis (basis-trade shrinkage, ESTIMATE, **LIQUID owns**) — route, don't adjudicate | ✅ First read taken and **routed to LIQUID, explicitly not adjudicated.** Thin cover did **not** extend to the 7Y 24h later in a longer tenor ⇒ points 5Y-specific; the same evidence cuts against the FOMC-eve confound. Three alternatives I can't discriminate listed for them. |
| 5 | Known bias disclosure travels with the verdict; state which side of it the print landed on | ✅ **Landed on the NO-FIRE side = the weak-evidence side**; HENRY's discount instruction restated as standing. **Calibrated rather than waved:** placement error **0.82pp** vs indirect margin **~13pp** ⇒ discount the gate, not the measurement; dealer leg cleared by **0.032pp** ⇒ full discount there. Stated in the memo, all three packets, PREDICTIONS, VX-01, STATUS and the outbox note. |

## 2. The primary (single source of truth for every figure below)

**7-Year Note · 91282CRC7 · 2026-07-28 · $44.0B · single-price · issue 7/31/26 · maturity 2033-07-31**

| | | vs trailing-12 7Y |
|---|---:|---|
| Bid-to-cover | **2.49** | median 2.495 → **dead on median** |
| Indirect | **70.15%** | median 60.65% → **+9.50pp**; clears the frozen 56.4% bar by **13.73pp** |
| Direct | **16.88%** | −12.82pp vs 6/25 |
| Dealer | **12.97%** | max 13.14% → **below it; not stuffed** |
| High yield | **4.4730%** | **+21.3bp** vs the 6/25 7Y |

Denominator = **competitive accepted $43,909,474,000** (competitive tendered $109,314,764,000; noncompetitive $90,527,200; SOMA add-on $4,864,689,800 correctly **excluded**). Arithmetic verified: 70.15+16.88+12.97 = 100.00; comp+noncomp = $44.000B = offering.

**Reported against my own headline:** the +12.60pp indirect move **overstates real demand** — directs fell −12.82pp, so **end-user take was 87.03% vs 87.25% on 6/25 = flat**, and that boundary is reclassification-sensitive. Reclassification-proof instead: dealers not stuffed · gross tendered $109.3B vs a $109.6B median = normal · dealer hit-rate 9.27% on a full $61.4B backstop · concession paid in price. And 70.15% is **#17 of 50** (67th pctile) — strong, **not** a record.

## 3. Files written

| File | What |
|---|---|
| `analysis/2026-07-28_grade_7Y_BND-13-resolution.md` | **NEW** — full grade: primary, §4 graded as frozen, secondary standalone read, bias calibration, basis-trade routing, write-back consequences, v1.1.4 carry-forward |
| `STATUS.md` | state line · matrix row VX-01 **3→2** · composite re-summed **12/35** · long-end row (auction path to 4 now closed) · configuration block · Trade Interface gate (c) resolved · OPEN PREDICTIONS line · catalyst row · **new BOTTOM LINE** |
| `workbook/KB.tsv` | **+4: KB-BND-097** (the print) · **098** (gate/backtest agreement + denominator discipline + the calibration lesson) · **099** (non-exhaustive branch set) · **100** (5Y-vs-7Y cross-auction read, ESTIMATE, LIQUID-owned) |
| `workbook/VX.tsv` | **VX-BND-01 3 → 2** (registered revert) · **VX-BND-08** evidence refreshed, **score HELD at 3 with the reason recorded** + a registered condition for the next move |
| `thesis/PREDICTIONS.tsv` | **BND-13 → TRUE**, resolved 2026-07-28, full outcome + caveats |
| `docket/CATALYSTS.tsv` | 7/28 7Y row → RESOLVED with the grade |
| `SCRATCH.md` | rewritten — verdict, the three self-arguments, score changes, next-session list |
| `outbox/2026-07-28_to-PROME_7y-grade.md` | verdict one-liner + composite change |
| `memory/auto/finding_gate_bias_is_placement_error_compare_to_margin.md` + `MEMORY.md` index row | auto-memory promoted (fleet-transferable, not duplicated locally) |

**Packets delivered (self-authored → committed by me per root carve-out ①, recipient named in the commit subject):**
`AGENTS/HENRY/inbox/2026-07-28_from-BOND_7Y-graded-BND-13-CONFIRMED-branch-B.md` · `AGENTS/NEXUS/inbox/2026-07-28_from-BOND_7Y-graded-BND-13-CONFIRMED-branch-B.md` · `AGENTS/LIQUID/inbox/2026-07-28_from-BOND_5Y-thin-cover-did-not-extend-to-7Y-basis-trade-observation.md`

## 4. Constraint compliance

| Constraint | Compliance |
|---|---|
| No thresholds moved outside pre-registered paths | ✅ Only move made was the **registered** VX-01 revert. VX-08 explicitly **held** rather than moved, with the reason recorded and a condition registered for next time. |
| No trades / capital actions | ✅ None. TLT puts **HOLD, no add**; Will's 7/16 NO-ADD stands; add-gate (c) resolved DID-NOT-FIRE. |
| No edits to HENRY / NEXUS / LIQUID files beyond inbox packets | ✅ Three inbox packets only; nothing else touched in their dirs. |
| Every number carries source + date | ✅ All auction figures [CONF TreasuryDirect TA_WS 91282CRC7, 7/28]; rates [CONF FRED, 7/24]; marks [CONF yfinance, 7/28 ~14:30 ET], flagged as context not a graded input. |
| If TD not yet posted, wait — never substitute a secondary | ✅ Not needed; TD had posted (13:03:18) before the pull. **No 7Y "tail" was carried** — unscoreable from primaries by construction. |
| WALTER has live uncommitted files — no pull/stash/sweep | ✅ No pull, no stash, no `git add .`/`-A`. Pathspec commits from repo root only. |

## 5. Flagged, not fixed (deliberate — out of scope or needs a registered path)

1. **`VX-BND-09 "Auction Tail"` still scores 2 on a metric formally retired as unscoreable** (7/28). Live internal inconsistency; a score change needs a registered path. → queued with v1.1.4.
2. **The VX-01 revert rule may be too fast** — one benign auction round-trips a state vector. **Registered, so it executed as written**; declining it because I dislike the result is the exact failure the method exists to prevent. → v1.1.4 review (KB-BND-099).
3. **`workbook/KB.tsv` has 4 bare-LF terminators** at the KB-073…076 boundaries — **pre-existing, verified identical in git HEAD**, not introduced this session. Field counts all validate at 13. Fix opportunistically.
4. **`NEXUS_BRIEF.md` still 7/23-vintage** — NEXUS told to pull from the packet/memo instead until refreshed.
5. **LIQUID still owes the 7/01→7/15 repo/funding refuse-or-confirm** from the ~04:30 packet — matters more than today's routing, since a confirm flips the dealer unwind from benign distribution to forced de-risking (**more** bearish).

## 6. Next 🔴

**FOMC Wed 7/29 2:00PM ET** — ~34% hike / ~65% hold, **forward guidance removed**, presser 2:30. **Nothing in today's auction speaks to it.** Frozen falsifier: arm BREAKS on 2Y <3.85 AND DFII10 <2.15 AND 10Y <4.35 sustained 3 sessions — **deep-lit against dovish** (2Y 4.33 / DFII10 2.43 / 10Y 4.69 [FRED, 7/24]). **DFII10 >2.5 is 7bp away and is now the nearest live add-gate.**
