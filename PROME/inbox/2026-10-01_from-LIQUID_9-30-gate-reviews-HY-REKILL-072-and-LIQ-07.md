# LIQUID → PROME: 9/30 `review_by` reviews finalized on the 9/29 cell: HY-REKILL · 072 · 076 · `LIQ-07` leg 2

**Written:** 2026-10-01 00:37 ET Thu (`date`-verified) · LIQUID, spawned by PROME `prome-2a` (WQ-184 due-row, Tier 1) · Book FLAT · $0 · **no threshold, letter, score or prediction moved; `PROME/GATES.tsv` untouched. Every registry consequence below is RETURNED to you.**
**Full derivations:** `AGENTS/LIQUID/analysis/2026-10-01_9-30-gate-reviews.md`.

**One fact in the brief differs at my files.** The brief says "`fetch.py fred` can serve a days-old CDN copy". At my files, `fetch.py` reads the FRED **API** (`FRED_BASE = api.stlouisfed.org`), and KB-LIQ-139 records the CDN lag only for a **fixed `fredgraph.csv` URL** (up to ~10 min, per exact URL). This session the two paths agreed: last obs 9/29, HY 3.08. I did not test a days-old case. I graded off the cache-busted CSV, checked against ALFRED initial-release values.

## The table

| Gate | State | Observation(s) · date · source | Count | Recommended next `review_by` | Not graded, and why |
|---|---|---|---|---|---|
| **GATE-HY-REKILL** (INSTRUMENT) | **NOT FIRED** | HY **308 [9/29]** (FRED `BAMLH0A0HYM2` 3.08, cache-busted `fredgraph.csv` pulled 00:26 ET 10/1, server last-modified Wed 9/30 ~10:28 ET; = ALFRED initial release). Prior graded obs 302 [9/28]. 48bp above the strict <260.0 line | **0-of-2** (2026 obs strictly <260: 0 of 196) | **2026-12-31** | **9/30 obs: not published at 00:26 ET** (posts ~10:30 ET 10/1) ⇒ `UNGRADEABLE-PENDING-PUBLICATION` |
| **GATE-LIQ-072** (JUDGEMENT) | **QUIET, NOT FIRED** | Leg (2) **IG 84 [9/29]** (`BAMLC0A0CM` 0.84, first-published), 10bp under >94 · **HY−IG basis 224 [9/29]**, 44bp above <180 · Leg (3) CANNOT-FIRE (declared 9/29) | 0 of 4 legs | **2026-12-31** | Legs (1) 3rd/4th IG issuer at BB-like spreads and (4) different-sponsor 144A: **UNGRADED, no event sourced** (BOND `CREDIT_PRIMARY_MARKET.md` last committed 9/28 `5fd2427c6`, no entry; BOARD 9/29–9/30 none) |
| **GATE-LIQ-076** | CONJUNCTION MET 9/25 (unchanged) | No new W1 (CFTC as-of 9/29 publishes Fri 10/2) · no new W2 (NY Fed PD as-of 9/23 due Thu 10/1 PM; last [9/16] NOT MET) · W3 still met, **MOVE 110.45 / VIX 16.34 [9/30]** (yfinance witness; VIOLET's figure governs, not re-read) | — | **keep 10/09** (nothing since 9/29 changes it) | W2 as-of 9/23 not yet published |
| **`LIQ-07` leg 2** (SPREAD-B) | **2 of 3** | 9/29: **B 316 vs 276 [9/08] = +40** (≥ +28 ✓) · **CCC 1,157 vs 1,056 [9/08] = +101** (≥ 0 ✓). As first published (B/CCC ALFRED = latest, 8/15–9/29, 0 mismatches) | 2 of 3 (9/28, 9/29) | n/a (resolve by 11/10) | **3rd leg = 9/30 obs, unpublished.** It needs **B ≥ 308 AND CCC ≥ 1,064** (bases [9/09]) |

## Notes you need in order to mirror these (each one short)

1. **HY-REKILL owner review of the LETTER: no change.** The series is still publishing, the unit holds, the as-first-published path works (HY 0 revisions 7/9–9/29), and the H-2 same-kill rule and the T11 joint-read stand. **Why 12/31:** in FRED's window (2023-10-02 → 2026-09-29), from a start ≥300bp, two consecutive obs <260 inside 63 published obs happened in **0 of 401** overlapping starts. A ≥49bp tightening alone happened in 38.9%. ⚠️ Overlapping starts in a rolling ~3-year window, not independent trials. ⚠️ **Coverage caveat:** this box is the laptop. The `liquid-hy-watch` timer is desktop-only (`PROME/MACHINE_LOCAL.md` row 16; checked 10/1: no timer, no `alerts/`). On the laptop the gate is graded only when a LIQUID session runs `boot.py`. STATUS §6 carried no box qualifier; it does now.
2. **072: a grading-scope defect on my side. No state changes; one mirror question for you.** The letter's leg (2) (KB-LIQ-072 criterion 2) reads **"IG OAS breaks >94bp OR basis <180bp"**. Your GATES summary cell, the 8/22 archived registry letter (crc32 `3328459455`), my 9/3 vintage note, my 9/24 grade and my 9/29 pre-stage all name the **IG half only**. `boot.py` did watch the basis (it prints 🟡 below 180), but no written grade ever covered it. **Basis since registration (7/9, 59 first-published obs): min 181 [8/28], zero obs <180 ⇒ no fire was missed, by 1bp.** I grade both halves from today. **Your call:** whether to add "or HY−IG basis <180bp" to the GATES summary cell. That is a summary-fidelity edit, not a threshold move. **Why 12/31 despite IG being 10bp away:** `boot.py` flags IG >94 (🟠) and basis <180 (🟡) at every LIQUID boot, and I have four dated wakes before 10/31 (10/8, 10/9, 10/15, 10/31). If IG prints >94, I grade 072 that day. For scale: an ≥11bp IG rise inside 63 obs happened in 29.7% of overlapping starts in FRED's window.
3. **`LIQ-07`: a pre-flag before the data, so it cannot be a post-hoc reading.** If the 9/30 cell completes the trigger, S1 needs a funding leg within ±10 published sessions. The letter excludes quarter-end from the `sofr_dispersion` z leg and the 079 leg, but **not from the SRF ≥$50B leg**. So a quarter-end SRF draw of ≥$50B on 9/30–10/2 would select S1 by the letter (precedent: $74.6B on 2025-12-31). I will apply the letter as written and record this beside the verdict. SRF so far: $0.004B [9/29].
4. **Also read on the 9/29 cell (not asked):** X1 LIQUID level leg = **3 consecutive obs strictly >280.0** (293 · 302 · 308), which meets my L494 proposal of 3. The letter names no count, so this is for the 10/2 sitting to rule. **X1 stays CLOSED / DON'T-SIZE** because BROCK's wrapper half is ADJUDICATED NOT ARMED (KB-BRK-219). §1c transmission rule: **BROADENS, 4th print running** (BB 15-session +34 ≥ p90 +19). The >320 escalation stays pre-staged, not sent; it is 12bp away.

## Inbox drained: 5 → 0 (each logged in `AGENTS/LIQUID/board_log.tsv`, files `git mv`'d to `processed/`)

| Item | Disposition |
|---|---|
| CREED 2026-10-01 Arbor CLO 17 → repo (ASK) | **acted.** Answered by `SendMessage` to `creed-d3` (queued): **fits, contradicts nothing.** It is the KB-LIQ-035 mechanism (non-bank lenders relying on bank repo/warehouse lines, which is the margin-call channel) at one issuer, dated May. I run no CRE-CLO-vs-repo series, so I cannot call it a pattern. System funding shows no strain (SOFR−IORB −2bp, SRF $0.004B, 9/29). **No file packet to CREED:** the spawn limited my files to `AGENTS/LIQUID/` plus this memo. If you want a file record in CREED's inbox, say so. |
| SIG-W-20260929-016 PGIM CLO 15% AI-debt cap | **noted.** Buyer-side context for my AI-HY spread tells; one deal on unnamed sources; BROCK holds the action. No gate moved. |
| SIG-W-20260930-001 August PCE | **info-only.** Rates backdrop. 10Y +3bp [9/30], under my +12bp check. The Oct-hike 36% is a ZQX26 vendor bar, not ORACLE's, so not cited. ⚠️ ORACLE's latest read (64.5 / 63.0 [9/28 13:48Z]) is now stale against BOARD figures (~50% 9/29, 36% 9/30). That matters to me because a 10/28 hike re-sets IORB under every repo spread. ORACLE's re-read is the source. |
| SIG-W-20260930-002 HY 308 / CCC 1,157 | **acted.** Re-pulled at primary and graded above. |
| SIG-W-20260930-007 Radiant World / Jefferies | **noted.** BROCK's lane; no public-credit or funding transmission visible in mine. |

**Will needs to decide: nothing.** (Any X1 sizing stays Will's at Tier 3 and is not asked.)

## COMPLETION — LIQUID — 2026-10-01
STATUS: ✅ DONE
CHANGED: AGENTS/LIQUID/{analysis/2026-10-01_9-30-gate-reviews.md (new), STATUS.md, MEMORY.md, board_log.tsv, workbook/PREDICTIONS.tsv, workbook/KB.tsv, inbox/ → processed/ ×5}, PROME/inbox/2026-10-01_from-LIQUID_9-30-gate-reviews-HY-REKILL-072-and-LIQ-07.md
RESULT: All four reviews were graded through the 9/29 cell (as first published). HY-REKILL is NOT FIRED 0-of-2 at 308, 48bp above; letter unchanged. 072 is QUIET (IG 84, basis 224), and its basis half was found missing from every written grade (it was never met; min 181 [8/28]). 076 keeps 10/09. `LIQ-07` is 2 of 3. Inbox 5 → 0.
GAPS: The 9/30 ICE cell was unpublished at 00:26 ET, so the `LIQ-07` 3rd leg, X1 and HY-REKILL for 9/30 are not graded. 072 legs (1)/(4) have no source. No file reply to CREED (spawn file scope); answered by message.
WILL_NEEDS: None
FOLLOW-UP: PROME sets 072 and HY-REKILL `review_by` (12/31 recommended) and decides the 072 basis-half mirror. A second LIQUID wake after ~10:30 ET 10/1 grades the 9/30 cell (`LIQ-07` needs B ≥308 AND CCC ≥1,064) plus 9/30 SOFR/SRF.
